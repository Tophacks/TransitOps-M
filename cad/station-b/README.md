# Station B — expanded modular interchange (v0.2)
HO 1:87 scale. **Concept geometry, not validated fabrication CAD.**
Run `Station_B_v02.FCMacro` using **FreeCAD 1.x → Macro → Macros → Execute** to generate an editable `Documents/TransitOps-M-CAD/TransitOps_M_Station_B.FCStd` native document.

## Dimensions (mm)
| Part | Size |
|---|---|
| Platform | 220 × 52 × 3 |
| Separate roof | 144 × 35 × 2.2 |
| Roof top elevation | 38.2 |
| Support-post footprint | 132 × 28 |
| Ticket kiosk | 11 × 9 × 25 |
| Route totem | 10 × 5 × 32 |

Contains curb indication, tactile-strip placeholder, four roof supports, glazed panels, two benches, map case, kiosk, signs, sensor cabinet and wiring-channel placeholder. Unlike a static drawing, each component is separately editable using native FreeCAD primitives.

**Before manufacturing:** choose the actual motorized bus chassis, confirm guide-wire centerline and bus swept path, define platform/curb clearance, validate sensor arrangements, redesign delicate parts to printer tolerances and test assembly fit. No charging functionality or physical stopping mechanism is present. Macro has been Python syntax-checked but has not yet been executed in FreeCAD.