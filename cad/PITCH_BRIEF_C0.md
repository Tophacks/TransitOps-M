# TransitOps-M — physical prototype sponsorship brief
Revision C0 · HO 1:87 scale · October 2026

## Purpose
TransitOps-M extends the working TransitOps miniature fleet simulation into a physical testbed: a guided 1:87 bus, two passenger stations, a forward-only automated depot bay, two static parking bays, and a Raspberry Pi supervisory controller.

## Architecture
Dashboard → Python dispatcher → hardware adapter → trackside sensors/stopping/branch devices → compatible motorized guided vehicle. Sensor feedback must confirm physical arrival and bay occupancy before the software updates its state. Software commands are not a certified emergency-stop circuit.

## CAD package
Station A: 180×45×3mm platform; Station B: 220×52×3mm; Depot B: 250×190mm footprint; test road 300×65mm; nominal 12m bus envelope 138×30×38mm; site footprint study 1000×650mm. STEP/STL files and parametric CadQuery source are supplied in the engineering package separately.

## Sponsorship request
1. Vehicle manufacturer/retailer: one HO motorized guided chassis, compatible track materials and control documentation.
2. Fabrication company: prototyping sponsorship for station platform, shelter and removable depot structures.
3. Electronics supplier: compatible sensors, protected Raspberry Pi interfaces, low-voltage supplies and branch controllers.

In exchange, offer documented engineering integration, sponsor acknowledgements on the TransitOps site, and disclosed mentions in relevant LinkedIn and planned YouTube project updates. Do not guarantee impressions or product endorsements.

## Milestones (goals, not completed claims)
M0 Software / concept STEP models; M1 300mm straight guided test (20 runs); M2 confirmed station stop and departure (10 repeats); M3 two station route; M4 drive-through depot and interlocking; M5 comparison of fixed and intelligent dispatch algorithms.

## Outstanding risks
Hardware ecosystem compatibility; minimum guide bend radius; HO model swept path; realistic switch and stop actuation; road geometry; charging chemistry; tolerances. **Do not manufacture the complete depot or roadway until the vehicle chassis is selected and tested.**