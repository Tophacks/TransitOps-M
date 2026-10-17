# Depot B — dual active bays and three staging slots (v0.1)

**Scale:** HO 1:87 · **Status:** conceptual clearance study, not fabrication-ready.

## Layout
- Overall slab: **280 × 280 × 3 mm**
- **2 active, straight-through bays**, each 280 mm long and 44 mm wide (visual guide-path centrelines)
- **3 static staging slots**, each marked at approximately 170 mm long × 34 mm deep on a common apron
- 5 translucent bus clearance dummies, 138 × 30 × 38 mm
- Removable sawtooth-inspired roof panels, posts, equipment/sensor placeholders

**Workflow:** in-service bus → reserve an active bay → enter forward along selected guide path → confirmed stop/service → depart forward. Staging parking is initially **manual/static**; it does *not* yet have independently routed guide wires or automatic parking. A later version may route buses into staging through forward-only circulation loops.

## Important geometry limitations
The 44 mm active lane is an interior envelope study, **not a compliant final guide-wire roadway**. Our previous FALLER-based planning uses ~50 mm straight roadway and more room for bus swept paths. Staging markings allow only 2 mm nominal lateral margin on each side of a 30 mm bus dummy; **that is not sufficient proof of maneuvering or parking clearance**. Final positions, turns, stopping sections, safety margins, guide-wire trenches and switch locations require a chosen physical motorized chassis and track equipment. No functional charging interface is modeled.

## How to open
Download `Depot_B_v01.FCMacro` to FreeCAD and execute via **Macro → Macros → Execute**. The macro creates an editable native document and saves it under `~/Documents/TransitOps-M-CAD/TransitOps_M_Depot_B.FCStd`.

**Do not send the current bay outlines for manufacturing:** dimensioned CAD is preliminary, and some sections intentionally illustrate rather than satisfy clearance requirements.
