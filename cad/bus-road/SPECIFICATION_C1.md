# Bus + Roadway C1 — TransitOps-M (1:87 HO)

**Status: pre-procurement engineering study. Not fabrication-certified or validated with a real chassis.**

## Vehicle geometry (CAD clearance dummy)

| Parameter | Preliminary CAD value |
|---|---|
| Body overall length | 138 mm |
| Body nominal width | 30 mm |
| Body nominal height | 38 mm |
| Real-world equivalent | 12.006 m long, 2.610 m wide, 3.306 m tall |
| Steering and wheelbase | **TBD after chassis selection** |
| Front overhang / rear swing | **TBD after swept-path test** |
| Motor, batteries, axle | **Not designed** |

The bus clearance dummy is **not a working chassis or production body shell**. We need a selected powered chassis or mechanism before developing wheel arches, shell mounts, battery enclosure, LEDs and dimensions for a printable body.

## Guide-wire roadway

FALLER official Car System roadway design guide (2022): https://medien.faller.de/xs_db/DOKUMENT_DB/www/_blaetterkatalog/epaper-FALLER_Car_System_2022_EN/epaper/FALLER_Car_System_2022_EN.pdf

- Straight single lane: **50 mm** minimum road width (manufacturer guidance).
- Curve single lane: **70 mm** minimum road width (manufacturer guidance).
- Curve minimum radius: **150 mm** manufacturer minimum; the actual bus may require larger radius.
- Base construction: FALLER recommends 3 mm poplar plywood for roadway and a lightweight supported frame, accommodating their stopping-section coil. This is **not** blanket validation of a 3 mm 3D-printed substrate.
- The guide-wire channel profile and depth must match the actual purchased guidance materials and be determined experimentally.
- Avoid bumps at joint interfaces and verify tracking before scenery, curb edges, or permanent pavement.
- Bench-test the longest vehicle on provisional guide-wire path before road construction.

## C1 CAD macro

Run `Bus_Road_C1.FCMacro` from **Macro → Macros → Execute** inside FreeCAD 1.x. It builds editable solid primitives for a **300 × 65 × 3 mm** test-road envelope, a **138 × 30 × 38 mm** bus clearance dummy and a non-printable R150 guide-wire curvature diagram. The wire shown on the straight road is a *visual marker*, not a machined groove.

The macro saves `TransitOps_M_Bus_Road_C1.FCStd` under `~/Documents/TransitOps-M-CAD`. Inspect in FreeCAD; delete or hide the illustrative annotation geometry for manufacturing exports.

## Integration with Station A / Depot B

- Station A's 180 mm-long platform accommodates the stationary bus length with only 42 mm of combined longitudinal extra length; **approach/departure tracking sections** must be added outside it.
- A minimum 50 mm road lane must remain unobstructed at the station, with the bus positioned using a real tested stop section.
- Depot B's nominal straight-through lane is an *architecture concept*, not a validated connection to the main loop.
- For a 150 mm-radius guide path, the curve centerline alone spans 300 mm diameter, before road width, sidewalk, scenic margin and the bus overhang allowance.
- The master 1000 × 650 mm site is **not yet confirmed suitable** for all required bus turns, switches, stations and depot routes.

## Procurement decision gate

1. Select compatible motorized bus chassis and steering mechanism.
2. Obtain vendor drawings and physical dimensions of front/rear overhang, steer axle and guidance magnet.
3. Provisional test of R150, R180, R220 paths; measure swept width and reliable minimum radius.
4. Freeze roadway CAD and guide-wire trench details only after 20 successful laps per route at operating speed.
5. Validate stopping and switching sections before ordering full depot/scenery prints.

### Potential sponsorship asks

- FALLER / retailer: motorized HO bus chassis, matching guidance wire, stopping section and documentation.
- Fabrication partner: modular road *test pieces* and bus-shell fitment prototypes (not full production city).
- Electronics provider: isolated trackside sensor/actuator controller and power supply.
