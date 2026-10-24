# Development log

## 2026-10-24 — State-machine and route-boundary correction

### Implemented
- Prevent dwell countdown and station-departure events unless a bus is actively `IN_SERVICE` and the interlock is clear. An emergency-stopped bus now freezes its dwell state.
- Detect arrival on the exact station boundary, clamp the normalized route position to the stop and use identical crossing semantics in Python and the browser demo.
- Add regressions for emergency stop during dwell, exact-boundary arrival and a station reached across the loop wrap.
- Update the public project page to describe the corrected controller behavior without implying hardware readiness.

### Research and decision
No consequential primary-source change this week justified changing the planned simulation stack or purchasing hardware. Eclipse SUMO remains the next intended microscopic backend because its official documentation supports public transport, pedestrians and remote-control APIs: https://eclipse.dev/sumo/ . The physical design remains gated on one guided vehicle and measured geometry.

### Validation
- Full repository suite: 17 tests passed with `python -m unittest discover -s tests -v`.
- Browser dashboard JavaScript parsed successfully after the parity changes.
- No physical vehicle, guide path, sensor, actuator, charging system or public deployment was tested.

### Remaining risks / next milestone
1. Browser/Python parity is still maintained in two implementations; shared scenario fixtures remain necessary.
2. Route occupancy and safe separation are absent, so automatic multi-bus dispatch is not ready.
3. Depot access is conceptual and docking remains a manually injected simulation confirmation.

Next milestone: add a deterministic scenario runner and metrics for trips, dwell, blocked commands and recovery time before multi-bus routing.


## 2026-10-23 — First maintenance and procurement review

### Implemented
- Reject non-object JSON command bodies with HTTP 400 instead of terminating the request on `.get()`.
- Serialize API mutations and snapshots with a shared lock to preserve command/state consistency across threaded requests.
- Reject boolean tick counts and malformed bus IDs; document the accepted identifier format.
- Add seven real HTTP regression tests covering malformed bodies, invalid IDs, concurrent ticks, competing bay reservations and the depot/recovery flow.
- Add a public hardware-readiness page and dated progress section.
- Distinguish the one-bay/two-space simulator from the two-bay/three-slot CAD proposal; label the homepage fleet table illustrative.
- Correct the README run command to match this repository's root directory.

### Research and decision
The [hardware plan](PURCHASING_PLAN.md) records technical validation stages. Compare FALLER 161479 and 161494 for the first test vehicle.

### Validation
- Baseline: 8 existing unit tests passed.
- Updated suite: 15 tests passed with `python -m unittest discover -s tests -v`, including real localhost HTTP requests and concurrent requests.
- Local website link/fragment checks and JavaScript syntax checks passed.
- These checks do not validate physical hardware, CAD manufacture, or public-network API security. Deployment status is reported separately after publication.

### Remaining blockers / next milestone
1. Verify package contents, charging details and chassis dimensions for the first vehicle.
2. Resolve the 44 mm conceptual depot lanes against the roadway study and measured swept path before fabrication.
3. Specify trackside detection, driver and power-loss behavior before hardware integration; automatic charging is deferred.
4. Browser demo and Python engine remain separate implementations. A future review should compare state transitions and station geometry before expanding features.

Next milestone: one compatible test-vehicle package and feasible removable loop, followed by measured lap and stopping trials after acquisition.


## 2026-10-23 — Public-content cleanup and controller review

Removed the requested audience statistic and financial details from current public pages/documentation. Added a code review with reproduced simulator limitations and a prioritized implementation sequence. See [CODE_REVIEW.md](CODE_REVIEW.md). This review does not claim the listed limitations are fixed.
