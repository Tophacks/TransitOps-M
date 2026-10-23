# Development log

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
