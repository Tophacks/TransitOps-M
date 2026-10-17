# TransitOps-M CAD — Station A (HO 1:87)

This directory contains a **native FreeCAD macro** that constructs a physically dimensioned preliminary bus-stop station assembly as editable `Part::Box` / `Part::Cylinder` objects, grouped by component. The macro is source code, **not a pre-rendered FCStd file**.

## Geometry (all mm)

| Item | Value |
|---|---|
| Platform | 180 × 45 × 3 |
| Shelter canopy | 105 × 33 × 2 (95 × 25 post spacing) |
| Canopy top | 36 above origin |
| Guidance road | Not yet modeled |
| Bus stop | 1:87 scale concept; actual bus dimensions must be checked |

Road runs alongside the platform edge y=0. Base and roof are distinct objects; parts must be revised for print tolerances, assembly connectors, drainage, and production materials.

## Generate in FreeCAD 1.1.x (Windows)

1. Download `Station_A_v01.FCMacro` from this folder (GitHub **Raw** / download raw file).
2. Put the macro into the FreeCAD user macro directory, often `%APPDATA%\\FreeCAD\\Macro`, or select an appropriate macro location in FreeCAD preferences.
3. In FreeCAD, choose **Macro → Macros**, select `Station_A_v01`, and click **Execute**.
4. FreeCAD creates and opens the editable model, then writes:
   - `Documents/TransitOps-M-CAD/TransitOps_M_Station_A.FCStd`
   - `Documents/TransitOps-M-CAD/TransitOps_M_Station_A.step`
5. To change major dimensions, edit the constants near the top of the macro and rerun.

**Important:** This model is a first-pass engineering concept, not validated as manufacturable; the shelter roof/post clearance, glass thickness, curb interface and guide-wire mechanism require further design. Do not use it as an uncontrolled production or sponsorship fabrication quote.

No licence has been granted for this code by default; repository visibility does not imply reuse permissions.
