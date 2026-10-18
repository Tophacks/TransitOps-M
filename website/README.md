# TransitOps-M public website

Static, responsive project website with **zero npm dependencies**. This is the sponsor-facing information site, not the localhost Python simulator.

## Run locally

Open `index.html` in a browser, or serve `website/` with `python -m http.server 3000`.

## Deploy on Vercel
Create a Vercel project connected to `Tophacks/TransitOps-M`, set **Root Directory** to `website`, **Framework Preset** to Other, and leave build command empty. Deployments can rebuild automatically from main.

## Accuracy and scope
The moving vehicle in the hero is an **SVG conceptual animation**, not live telemetry or physical bus video. The fleet table is **illustrative**, not a connected dashboard. The site describes current software and CAD progress and explicitly marks hardware/charging/depot features as planned. Contact uses `n2powell@uwaterloo.ca`; replace it before wider outreach if preferred.

Future work: actual FreeCAD screenshots, recorded simulator walkthrough, GitHub README links, sponsor prospectus PDF, privacy-safe contact workflow, accessible interactive showcase.
