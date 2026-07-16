# Flagship Project — County Health Systems Operations Platform (NDWH & CBS)

*Governed by `00_SYSTEM_PROMPT.md`. Evidence-backed per `07_Independent_Experience_and_Positioning.md`. Source: `/home/kenyaemr/Documents/WORK/NATIONAL DATA WARE HOUSE/ndwh & cbs` (own build; git repo present; demo data available for safe screenshots).*

> **Why this matters:** this single project proves your two most valuable layers at once —
> **health informatics** (NDWH, CBS, EMR, facilities, counties) **and full-stack engineering**
> (Next.js, TypeScript, Prisma, MySQL, 40+ APIs, maps, dashboards). It is your strongest portfolio
> asset. Lead with it in Featured, Projects, GitHub, and interviews.

## Suggested public name
**County Health Systems Operations Platform (NDWH & CBS)**
*(Internal/package name "facility-reporting-dashboard" undersells it — use the name above publicly.)*

## What it is
A full-stack web platform to monitor health-facility reporting (NDWH & CBS), EMR deployments, IT
assets, and support incidents across four Kenyan counties — **Kakamega, Vihiga, Nyamira, Kisumu**.

## Feature modules (all real, in the codebase)
- **Facility reporting** — tracks NDWH vs CBS reporting status per county/subcounty; smart
  case-insensitive matching + duplicate prevention; progress %, missing-facility detection;
  CSV/text/clipboard exports.
- **EMR overview** — EMR facilities, versions, and asset views (`app/emr-overview/*`, public EMR APIs).
- **IT asset management** — servers, routers, tablets, mobile phones, LAN & inventory assets;
  asset lifecycle, lost/recovered register, asset-type admin, bulk import.
- **Incident / NOC tickets** — ticket wizard + guest tickets; critical-server-issue tracking;
  filtering by location & subcounty; server-type issue breakdown.
- **Dashboards & geospatial** — national/county overview metrics, county insights, distribution
  map of Kenya (Mapbox / react-simple-maps), enhanced Recharts charts (bar/pie/area/line).
- **Articles/knowledge base**, **file uploads** (xlsx import), **backup**, **guided tour** (driver.js).
- **Auth & access** — login + passcode screen, roles/users, guest view, public API endpoints.
- **UX** — dark mode (next-themes), shadcn/ui, framer-motion, responsive.

## Tech stack (for CV/LinkedIn/interview)
Next.js 14 (App Router) · TypeScript · Prisma ORM · **MySQL on Aiven (cloud)** · Tailwind CSS ·
shadcn/ui · Recharts · Mapbox / react-simple-maps · framer-motion · xlsx · Vercel-ready (serverless).
**Data layer:** Prisma schema with multiple related models (Facility, ServerAsset, RouterAsset,
TabletAsset, MobilePhoneAsset, LanAsset, InventoryAsset, CriticalServerIssue…) with indexes and
relations. **API:** 40+ REST route handlers (facilities, assets, tickets, dashboard, geography,
auth, backup, public).

## Skills this project PROVES (maps to capability layers)
Full-stack development · frontend engineering · backend/API design · **database design & data
modeling** · health information systems (NDWH/CBS/EMR) · IT asset management · data import/ETL
(xlsx) · data visualization/dashboards · geospatial mapping · authentication/authorization ·
cloud database deployment · TypeScript · systems/solution architecture.

---

## Screenshot shot list (what to capture, in priority order)
Run with demo data (`node scripts/add-demo-data.js`) so no real/confidential data is shown.
Use a clean browser window at ~1440px wide. Capture a mix of **light and dark mode** (dark looks modern).

1. **Home / national overview** — the Kenya distribution map + top metrics (hero shot). *Most impressive; use as the main Featured image.*
2. **County/overview dashboard** — the Recharts charts (bar/pie/area/line) + county insights.
3. **Facility reporting dashboard** — NDWH vs CBS reporting %, progress bars, missing-facility view.
4. **EMR overview** — EMR facilities/versions view.
5. **Asset manager / asset command dashboard** — the IT asset register (servers/routers/tablets) with filters.
6. **Tickets / NOC UI** — incident list + critical-server-issues panel.
7. **Reports page** — export options (CSV/text).
8. *(optional)* **Login/passcode screen** (shows auth) and a **dark-mode** version of the dashboard.

Tips: hide any real names (demo data handles this); turn off browser bookmarks bar; capture at a
consistent size; crop tightly. For Featured, either upload the single hero image (#1) or combine
#1–#4 into a one-page PDF case study (more impressive).

---

## LinkedIn "Featured" copy (ready to paste)

**Title:**
```
County Health Systems Operations Platform — NDWH & CBS (Next.js · Prisma · MySQL)
```

**Description:**
```
A full-stack platform I designed and built to monitor health-facility reporting (NDWH & CBS), EMR deployments, IT assets, and support incidents across four Kenyan counties (Kakamega, Vihiga, Nyamira, Kisumu).

• Facility reporting — NDWH/CBS status with smart case-insensitive matching, progress %, and CSV/text exports
• EMR & IT asset management — servers, routers, tablets, phones, LAN; lifecycle + lost/recovered tracking
• Incident/NOC tickets — critical-server issue tracking by location & subcounty
• Interactive dashboards & Kenya map (Recharts + Mapbox), dark mode, role-based auth

Tech: Next.js 14 (App Router), TypeScript, Prisma ORM, MySQL (Aiven cloud), Tailwind + shadcn/ui, Recharts, Mapbox. 40+ REST API routes and a relational data model. (Screenshots use demo data.)
```

## GitHub repo README (one-liner + summary)
- **Repo name idea:** `health-systems-ops-platform` (or `ndwh-cbs-platform`)
- **Bio line:** "Full-stack health-systems platform: NDWH/CBS facility reporting, EMR oversight, IT asset & incident management. Next.js · TypeScript · Prisma · MySQL."
- Add screenshots to the README top; include the feature list + tech stack above.

## Portfolio case study (problem → approach → result)
- **Problem:** County health teams needed a single place to see which facilities were reporting to
  NDWH/CBS, track EMR/IT assets, and manage incidents — data was scattered across spreadsheets.
- **Approach:** Built a Next.js/TypeScript platform with a Prisma/MySQL data model, 40+ APIs,
  smart matching for messy facility names, dashboards/maps, asset lifecycle, and a ticketing/NOC module.
- **Result:** A working, cloud-deployable system giving real-time reporting visibility, an IT asset
  register, and incident tracking across four counties. *(Add concrete outcomes if used in the field:
  time saved, facilities covered, reports generated.)*

## Truthfulness notes
- This is your own build (git history). Claim as **independent/project-based** work.
- If it was used in your PATH work, say "supported/built for county reporting"; if personal, say
  "designed and built independently." Don't imply a client/employer that didn't commission it.
- Always screenshot with **demo data**, never real patient/facility-sensitive data.
