# Simulator/controller code review — 2026-10-23

Reviewed `transitops_m/core.py`, `api.py`, `dashboard.html` and existing tests at commit `1bd29a9`. This is a code review and implementation proposal, not a claim of hardware readiness. Findings are tracked below. Items marked resolved have regression coverage in the current default branch.

## Reproduced behavior and design gaps

| Priority | Finding | Evidence / reproduction | Proposed change |
|---|---|---|---|
| Resolved 2026-10-24 | Faulted dwell advanced in both implementations | Emergency stop during a dwell could still count down and emit `STATION_DEPARTURE`. | Python and browser now apply the state/interlock guard before dwell; a regression freezes dwell while faulted. Shared cross-runtime fixtures remain open. |
| 1 | No explicit resume from HOLDING | Python stop → clear → reset → tick(10) leaves BUS-01 HOLDING; dispatch rejects it. Return/dock/dispatch is a workaround, but invokes an unrelated mock depot flow. | Add explicit operator resume, guarded by cleared interlock, battery and route availability. Keep reset itself non-moving. |
| 1 | No route occupancy or separation | Add BUS-02, dispatch it, tick once: both buses have distance 0.025. Depot reservation prevents double booking only in the bay. | Introduce route segments and occupancy/reservations before automatic multi-bus dispatch. Define stopped-leader and entry-conflict scenarios. |
| Resolved 2026-10-24 | Station arrival was detected after crossing | An exact move to 0.20 previously delayed Station A arrival until the next tick. | Both implementations now use the same inclusive forward-crossing rule, clamp to the stop, and test exact arrivals plus loop wrap. Physical units remain undefined. |
| 2 | Rendered geometry is disconnected from simulation | Renderer places BUS-01 on an ellipse, while SVG roadway is a rounded rectangle. It draws only BUS-01 despite API support for additional buses. Depot docking changes state but does not move the marker onto a depot route. | Use one route geometry definition for movement and rendering, and draw every bus. Keep mock docking visibly separate until depot geometry exists. |
| 2 | Time and state are browser-driven and volatile | Start uses setInterval to send tick commands; no server clock or durable run log exists. Multiple clients can advance the same engine, and restart discards state. | Define one simulation clock owner, explicit run/paused state and deterministic scenario runner; export complete run events separately from bounded UI history. |

## Recommended implementation order

1. Establish Python/browser parity fixtures for station dwell, stop/clear/reset, bay reservation, battery depletion and loop wrap. Fix the faulted dwell discrepancy first.
2. Define resume semantics and station arrival precisely before expanding fleet behavior.
3. Add route segment occupancy, shared geometry and a two-bus conflict test.
4. Add reproducible experiments with explicit timestep, scenario metadata and metrics: trips completed, station dwell, blocked dispatches and recovery time. Existing battery values are synthetic; they are not a calibrated power model.
5. Introduce a backend interface only when needed: simulation commands, observations, timestamps, acknowledgements and stale-data handling. A later hardware adapter must not treat a requested stop as sensor-confirmed docking.

## External research applied to the design

- [SUMO Python TraCI documentation](https://sumo.dlr.de/docs/TraCI/Interfacing_TraCI_from_Python.html) describes advancing the simulator via `simulationStep()` and reading subscription results. If a SUMO backend is added later, use an explicit step/observation interface. Do not equate the current normalized route distance with metres or infer physical timing from dashboard animation speed. This is a proposed architecture, not an implemented SUMO integration.
- [Python http.server documentation](https://docs.python.org/3/library/http.server.html) explicitly advises against production use. Keep the current API on localhost; a remotely accessed controller requires a separately designed service boundary. The previous request lock fixes concurrency at the API boundary, not authentication or hardware safety.

## Validation performed

Existing 15 tests pass. Additional diagnostic scripts reproduced overlapping positions, HOLDING recovery behavior, the station-boundary behavior and browser faulted dwell. These diagnostics reveal missing test coverage; passing the existing suite does not establish complete controller correctness. No physical device tests were performed.
