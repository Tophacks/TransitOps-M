# TransitOps-M purchasing plan

Reviewed: 2026-10-23 · Status: **research shortlist, not an approved shopping cart**.

## Scope and decision

Build one guided HO 1:87 bus on a removable test loop, then one instrumented stop and one depot bay. Reuse the existing Raspberry Pi 4B. Expand toward four buses only after the first vehicle passes measured trials. The provisional CAD $600 total budget is a constraint, not evidence that four motorized buses and infrastructure can be delivered for that amount.

Prefer an assembled guide-wire bus for the first experiment. This is an engineering recommendation to reduce miniature steering fabrication and tool requirements, not a verified vendor compatibility claim. Use trackside observation and stop/release control first; do not assume a stock bus accepts ESP32, Wi-Fi or direct Python commands. Custom onboard control remains a separate design decision.

The current Python simulator has one automated bay and two static spaces. Depot B CAD depicts two active bays and three staging slots. These are different development stages, not interchangeable supported configurations. Depot CAD lanes are 44 mm wide; the existing road study calls for at least 50 mm straight roadway. Do not fabricate the depot unchanged.

## Candidate parts and missing evidence

Prices are observations from the linked pages, not delivered quotes. Availability must be reconfirmed before purchase. EUR and CAD values are deliberately not added together.

| Item / exact reference | Quantity for first stage | Price evidence | Status / purchase blocker |
|---|---:|---|---|
| FALLER 161479 MB O405 starter set | 1, alternative to 161494 | Manufacturer lists EUR 144.99 including VAT, before shipping [1] | Preferred quotation candidate; verify package contents, charger/input compatibility in Canada, bus dimensions, minimum usable turn radius and delivered CAD total. Canadian fulfillment not confirmed. |
| FALLER 161494 Citaro bus | 1, alternative to 161479 | Westend Trains lists CAD 269.99 [2] | Alternative Canadian listing, not a starter-kit-equivalent quote. Page contains conflicting stock labels. Confirm stock, included charging equipment and dimensions. |
| FALLER 161670 guidance wire | Only if not included in selected kit | Manufacturer accessory listing: EUR 20.79 / 10 m [1] | Match guidance system; avoid duplicate kit contents. Canadian price and shipping unverified. |
| FALLER 161675 stop section | 1, stage 2 | Price not verified; manufacturer documentation located [3] | Select a compatible supply and driver only after checking the exact electrical ratings, current and duty requirements. Not a Pi GPIO load. |
| Trackside detection + driver/interface | TBD, stage 2 | No selected part or verified price | Need mounting position, signal levels, bus detection method, power-loss behavior and wiring design before choosing parts. |
| Removable roadway and tools | 1 test loop | Local fabrication/material quote required | Select road substrate, guidance-wire installation method and available cutting tools; no permanent scenery yet. |
| Raspberry Pi 4B | 1 already owned | CAD 0 incremental for board | Verify existing supply, storage and local API operation; do not order a second Pi. |
| Depot/ station prints, branch switch, further buses | Deferred | Not quoted | Wait for tracked turning, stopping, routing and measured clearances. No charging hardware selected. |

At the Canadian alternative's listed price, four buses alone would cost **CAD 1,079.96 before tax/shipping**, exceeding the provisional budget without any infrastructure. Do not present this route as a CAD $600 four-bus build. A single bus leaves CAD 330.01 of that budget before tax, shipping and all remaining components; this is not a complete-build estimate.

## Purchase gates

1. **First test vehicle:** obtain one exact kit/vehicle quote with contents, delivered CAD price, applicable taxes/fees, charging arrangement, dimensions and practical turn-radius guidance. Sketch an unobstructed removable loop within the available desk footprint. Confirm tools and total initial-stage cost. Then a one-vehicle test purchase may be considered; physical tests necessarily follow acquisition.
2. **Road and stop validation:** measure bus wheelbase, overhang and swept width. Trial R150/R180/R220 only where the selected vehicle's guidance permits. Log speed, radius and failures; require 20 consecutive successful laps on the chosen route. Select the stopping method and measure stopping positions over 20 cycles before freezing station clearance. These are project acceptance targets, not manufacturer guarantees.
3. **Controller integration:** specify and bench-test separate actuator supply, appropriate driver and sensor levels. Simulate stale/missing detection, double reservation and power loss. Software emergency stop alone is not a physical stop system. Do not connect this localhost simulation API directly to actuators.
4. **Depot and scaling:** redesign the 44 mm concept lanes using measured envelopes, prove one entry/stop/release path, then commission the remaining depot geometry and fleet. Verify delivered totals again before every stage. Defer automated charging until battery chemistry, charger and contacts are explicitly engineered.

## Next research deliverable

A side-by-side delivered quote for 161479 versus 161494 plus required accessories, with no substitutions hidden in totals. Close dimensions/turn-radius and charging questions first. Supplier outreach and purchases have not been performed.

## Sources

1. [FALLER 161479 product and accessory listing](https://www.faller.de/en/car-system/car-system/2922/car-system-start-set-bus-mb-o405-incl.-decoration-stickers), checked 2026-10-23. Price/part evidence only; no complete Canadian kit quote established.
2. [Westend Trains 161494 listing](https://westendtrains.ca/products/mercedes-benz-citaro-public-bus), checked 2026-10-23. Conflicting stock text prevents treating availability as verified.
3. [FALLER 161675 stop-section instructions](https://medien.faller.de/xs_db/DOKUMENT_DB/www/anleitungen/161675_anl_01.pdf), located 2026-10-23. Full electrical/driver review remains open.
4. [Existing roadway specification](../cad/bus-road/SPECIFICATION_C1.md) and [Depot B geometry](../cad/depot-b/README.md). Current project design constraints, not measured hardware validation.
