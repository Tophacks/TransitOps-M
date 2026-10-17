# TransitOps-M engineering pitch package — Concept C0 (October 2026)

The initial **editable CAD package** has been generated as six STEP assemblies and STL previews, with a parametric CadQuery build script and detailed scope/RFQ documentation in the companion downloadable ZIP attached in the project conversation.

**Models generated:** Station A (180×45 mm); Station B (220×52 mm); Depot B (250×190 mm, forward-only through-bay plus two static parking positions); 300×65 mm test road; 138×30×38 mm bus clearance dummy; 1000×650 mm master site massing.

**Open in FreeCAD:** File → Open → `Station_A.step`, `Depot_B.step`, etc. STEP provides editable solids but not native FreeCAD feature history. The CadQuery Python script is the parametric source.

**Design constraints:** The master layout shows footprints and straight segments, not validated driveable turns. The final guide path, radius, vehicle wheelbase, stopping-section interface, switch geometry, roof manufacturing tolerances and battery/charging hardware all await physical vendor hardware testing. Depot bay is straight-through rather than reversing. Do not pitch as a completed operational city.

This repository entry establishes CAD documentation; binary STEP/STL assets are currently provided in the ZIP package, not committed to the repository.