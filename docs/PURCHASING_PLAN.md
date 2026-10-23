# Hardware validation plan

Reviewed: 2026-10-23. This public document covers engineering readiness only.

## First prototype

Select one guided HO 1:87 bus and a removable test loop, then one instrumented stop and one depot bay. Reuse the existing Raspberry Pi 4B. The two-active-bay / three-staging-slot CAD concept is distinct from the implemented one-bay / two-static-space simulator.

## Candidate platforms

- FALLER 161479 MB O405 starter set: verify contents, bus dimensions, charging arrangement and practical turning radius.
- FALLER 161494 Citaro: alternative platform; verify dimensions, guidance mechanism and charging equipment.
- FALLER 161670 guidance wire and 161675 stop section: evaluate after vehicle selection. A trackside actuator requires a suitable driver and separate supply, not direct GPIO drive.

No physical compatibility or control integration has been validated. A stock vehicle is not assumed to accept wireless or Python commands.

## Validation stages

1. Select the exact vehicle and establish a feasible unobstructed loop footprint using its geometry and guidance requirements.
2. After acquisition, measure wheelbase, overhang and swept path. Target 20 successful laps on the selected route and record 20 stopping cycles before freezing station clearance. These are project targets, not manufacturer guarantees.
3. Specify sensor levels, actuator driver, power-loss behavior and missing-detection handling before connecting hardware. The localhost API remains simulation-only.
4. Revise Depot B’s 44 mm conceptual lanes against the roadway study and measured clearance. Prove one entry/stop/release path before scaling. Automated charging requires a separate verified design.

See [roadway specification](../cad/bus-road/SPECIFICATION_C1.md), [Depot B](../cad/depot-b/README.md), and [code review](CODE_REVIEW.md).
