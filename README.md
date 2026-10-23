# TransitOps-M — Miniature Fleet Simulator v0.1

Hardware-independent Python module for the TransitOps monorepo. Simulates one 1:87 HO bus, two stations, one reservable automated depot bay, two static parking spaces, events, simulated battery usage and a simulation emergency-stop interlock.

## Run (Python 3.10+, zero third-party dependencies)
```bash
python -m unittest discover -s tests -v
python -m transitops_m.api
```
Open http://127.0.0.1:8765/

API: GET /health, GET /api/state, POST /api/command.
Commands: reset_sim (full simulation reset), tick (integer steps 1..100; booleans rejected), return, dock, dispatch, stop, clear, reset, add.

**Safety:** SIMULATION ONLY. Docking is manually confirmed in software. No motor hardware, real emergency-stop circuitry, battery charger, or GPIO interface is implemented. This API must not be exposed to a public network or connected directly to actuators.

## Dashboard buttons and connection modes

The dashboard automatically detects the local Python API. When the server is running, the buttons operate the Python in-memory simulation. If the HTML file is opened directly or the API is unavailable, the dashboard falls back to **browser demo mode**, which runs a separate in-browser simulation. Its state resets on page refresh.

To run the connected Python mode:

```bash
python -m transitops_m.api
```

Visit http://127.0.0.1:8765/ and confirm the banner reads **Connected to Python simulation API**. The GitHub code viewer itself does not execute the dashboard; download or clone the repository to run the app.

## v0.2 operations controls (simulation)

The browser dashboard now has **Start**, **Pause**, **Reset simulation**, and **1× / 2× / 4× speed** controls. When a bus reaches Station A or B, the dispatcher simulates three ticks of boarding dwell and emits arrival/departure events. The SVG shows a **conceptual depot branch**; it is not a drivable geometric route yet. Reserve depot, confirm mock docking and release are discrete simulation commands, not physical routing or sensor validation.

Run:

```bash
python -m unittest discover -s tests -v
python -m transitops_m.api
```

Then visit http://127.0.0.1:8765/ . Stop the Python process before pulling updates, and force-refresh the browser to avoid cached JavaScript. Live mode uses the localhost API; standalone HTML uses an in-browser fallback with independent state.

## Current build readiness

- [Hardware validation plan](docs/PURCHASING_PLAN.md): one test vehicle first; physical compatibility remains unverified.
- [Development log](docs/DEVELOPMENT_LOG.md): dated changes and validation.
- [Public website](https://transitops-m.vercel.app): information site, not the Python API.

The simulator has **one reservable bay and two static spaces**. The larger **two active bays + three staging slots** depot is a separate CAD concept, not the implemented simulator layout.

The threaded HTTP API serializes commands and state snapshots. Commands must be JSON objects; bus IDs must contain 1–32 ASCII letters, digits, underscores or hyphens. This validation does not make the localhost development server suitable for public exposure or hardware operation.
