import unittest
from transitops_m import Dispatcher, State

class TestFleet(unittest.TestCase):
    def test_station_tracking(self):
        d = Dispatcher(); d.tick(40)
        self.assertEqual([e["station"] for e in d.events if e["type"] == "STATION_ARRIVAL"], ["Station A", "Station B"])

    def test_station_dwell(self):
        d = Dispatcher()
        d.tick(8)
        self.assertEqual(d.buses["BUS-01"].station, "Station A")
        self.assertEqual(d.buses["BUS-01"].dwell_remaining, 3)
        distance = d.buses["BUS-01"].distance
        d.tick(2)
        self.assertEqual(d.buses["BUS-01"].distance, distance)
        d.tick(1)
        self.assertEqual(d.buses["BUS-01"].dwell_remaining, 0)
        self.assertEqual(d.events[-1]["type"], "STATION_DEPARTURE")

    def test_reset_simulation(self):
        d = Dispatcher()
        d.tick(10)
        d.request_depot("BUS-01")
        d.reset()
        self.assertEqual(d.tick_no, 0)
        self.assertEqual(d.buses["BUS-01"].state, State.IN_SERVICE)
        self.assertIsNone(d.bays["DEPOT-1"].reserved_for)

    def test_depot_flow(self):
        d = Dispatcher(); d.request_depot("BUS-01")
        self.assertEqual(d.bays["DEPOT-1"].reserved_for, "BUS-01")
        d.confirm_docked("BUS-01")
        self.assertEqual(d.bays["DEPOT-1"].occupied_by, "BUS-01")
        d.dispatch("BUS-01")
        self.assertIsNone(d.bays["DEPOT-1"].occupied_by)

    def test_double_booking(self):
        d = Dispatcher(); d.add_bus("BUS-02"); d.dispatch("BUS-02")
        d.request_depot("BUS-01")
        with self.assertRaises(ValueError): d.request_depot("BUS-02")

    def test_safe_stop(self):
        d = Dispatcher(); d.emergency_stop()
        self.assertEqual(d.buses["BUS-01"].state, State.FAULT)
        with self.assertRaises(ValueError): d.dispatch("BUS-01")
        d.clear_interlock(); d.reset_bus("BUS-01")
        self.assertEqual(d.buses["BUS-01"].state, State.HOLDING)

    def test_depot_requires_confirmation(self):
        d = Dispatcher(); d.request_depot("BUS-01")
        self.assertIsNone(d.bays["DEPOT-1"].occupied_by)

    def test_invalid_tick(self):
        with self.assertRaises(ValueError): Dispatcher().tick(10000)


    def test_faulted_bus_does_not_complete_dwell(self):
        d = Dispatcher(); d.tick(8)
        d.emergency_stop(); d.tick(5)
        bus = d.buses["BUS-01"]
        self.assertEqual(bus.state, State.FAULT)
        self.assertEqual(bus.dwell_remaining, 3)
        self.assertNotIn("STATION_DEPARTURE", [e["type"] for e in d.events])

    def test_wrapped_step_detects_station_near_zero(self):
        d = Dispatcher(); d.STATIONS = {"Loop Start": 0.01}
        d.buses["BUS-01"].distance = 0.99
        d.tick()
        self.assertEqual(d.buses["BUS-01"].distance, 0.01)
        self.assertEqual(d.buses["BUS-01"].dwell_remaining, 3)

if __name__ == "__main__": unittest.main()
