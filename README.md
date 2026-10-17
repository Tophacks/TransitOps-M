# TransitOps-M — Miniature Fleet Simulator v0.1

Hardware-independent Python module for the TransitOps monorepo. Simulates one 1:87 HO bus, two stations, one reservable automated depot bay, two static parking spaces, events, simulated battery usage and a simulation emergency-stop interlock.

## Run (Python 3.10+, zero third-party dependencies)
```bash
cd miniature
python -m unittest discover -s tests -v
python -m transitops_m.api
```
Open http://127.0.0.1:8765/

API: GET /health, GET /api/state, POST /api/command.
Commands: tick (steps 1..100), return, dock, dispatch, stop, clear, reset, add.

**Safety:** SIMULATION ONLY. Docking is manually confirmed in software. No motor hardware, real emergency-stop circuitry, battery charger, or GPIO interface is implemented. This API must not be exposed to a public network or connected directly to actuators.

## Dashboard buttons and connection modes

The dashboard automatically detects the local Python API. When the server is running, the buttons operate the Python in-memory simulation. If the HTML file is opened directly or the API is unavailable, the dashboard falls back to **browser demo mode**, which runs a separate in-browser simulation. Its state resets on page refresh.

To run the connected Python mode:

```bash
python -m transitops_m.api
```

Visit http://127.0.0.1:8765/ and confirm the banner reads **Connected to Python simulation API**. The GitHub code viewer itself does not execute the dashboard; download or clone the repository to run the app.
