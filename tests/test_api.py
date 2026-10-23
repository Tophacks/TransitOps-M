"""Exercise the real threaded HTTP boundary, including malformed input."""
import json
import unittest
from concurrent.futures import ThreadPoolExecutor
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from threading import Thread
from transitops_m import api


class QuietHandler(api.Handler):
    def log_message(self, *args):
        pass


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), QuietHandler)
        cls.worker = Thread(target=cls.server.serve_forever, daemon=True)
        cls.worker.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.worker.join()

    def setUp(self):
        with api.engine_lock:
            api.engine.reset()

    def request(self, data=None, method='POST', path='/api/command', raw=None):
        connection = HTTPConnection(*self.server.server_address, timeout=5)
        try:
            body = raw if raw is not None else json.dumps(data)
            connection.request(method, path, body if method == 'POST' else None,
                               {'Content-Type': 'application/json'})
            response = connection.getresponse()
            return response.status, json.loads(response.read())
        finally:
            connection.close()

    def test_non_object_json_is_rejected_without_mutation(self):
        for payload in (None, [], 'tick', 1, True):
            with self.subTest(payload=payload):
                status, body = self.request(payload)
                self.assertEqual(status, 400)
                self.assertIn('error', body)
        self.assertEqual(self.request(method='GET', path='/api/state')[1]['tick'], 0)

    def test_invalid_json_and_invalid_utf8(self):
        for raw in (b'{', b'\xff', b'x' * 4097):
            with self.subTest(raw=raw[:8]):
                self.assertEqual(self.request(raw=raw)[0], 400)
        self.assertEqual(self.request({'command': 'tick'})[1]['tick'], 1)

    def test_boolean_steps_rejected(self):
        self.assertEqual(self.request({'command': 'tick', 'steps': True})[0], 400)
        self.assertEqual(self.request(method='GET', path='/api/state')[1]['tick'], 0)

    def test_invalid_bus_ids_do_not_register(self):
        for identifier in (42, None, [], {}, '', ' ', '<script>', 'x' * 33):
            with self.subTest(identifier=identifier):
                self.assertEqual(self.request({'command': 'add', 'bus': identifier})[0], 400)
        state = self.request(method='GET', path='/api/state')[1]
        self.assertEqual(list(state['buses']), ['BUS-01'])
        self.assertEqual(self.request({'command': 'add', 'bus': 'BUS_02'})[0], 200)

    def test_concurrent_ticks_return_distinct_atomic_snapshots(self):
        with ThreadPoolExecutor(max_workers=6) as pool:
            results = list(pool.map(lambda _: self.request({'command': 'tick'}), range(24)))
        self.assertTrue(all(status == 200 for status, _ in results))
        self.assertEqual(sorted(body['tick'] for _, body in results), list(range(1, 25)))

    def test_concurrent_reservations_have_one_winner(self):
        self.request({'command': 'add', 'bus': 'BUS-02'})
        self.request({'command': 'dispatch', 'bus': 'BUS-02'})
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda bus: self.request({'command': 'return', 'bus': bus}),
                                    ('BUS-01', 'BUS-02')))
        self.assertEqual(sorted(status for status, _ in results), [200, 400])
        state = self.request(method='GET', path='/api/state')[1]
        winner = state['bays']['DEPOT-1']['reserved_for']
        self.assertEqual(state['buses'][winner]['state'], 'RETURNING')
        self.assertEqual(sum(b['state'] == 'RETURNING' for b in state['buses'].values()), 1)

    def test_command_recovery_and_reset(self):
        for command in ('return', 'dock', 'dispatch', 'stop', 'clear', 'reset'):
            self.assertEqual(self.request({'command': command})[0], 200)
        status, state = self.request({'command': 'reset_sim'})
        self.assertEqual(status, 200)
        self.assertEqual(state['tick'], 0)
        self.assertEqual(state['buses']['BUS-01']['state'], 'IN_SERVICE')


if __name__ == '__main__':
    unittest.main()
