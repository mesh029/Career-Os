# STAR Evidence Stories — System Administrator (CCaaS & Enterprise Stack)

*Use these in interviews and to fill in real metrics before submitting. Replace `[FILL]` placeholders with numbers you can defend.*

---

## Story 1 — Enterprise stack ownership (VoIP + ITSM + SSO)

**Situation:** PATH program operated across multiple sites with 120+ staff depending on Microsoft 365, Active Directory, VoIP, and a service desk — but tooling was fragmented and incidents lacked leadership visibility.

**Task:** Own the integrated operational stack end-to-end: sustain uptime, enforce secure access, and give management audit-ready reporting — without relying on external MSPs for day-to-day governance.

**Action:**
- Administered **Microsoft 365, Entra ID/Active Directory, MFA, and group policy** with least-privilege access across all sites.
- Architected and maintained the **contact-center-adjacent stack**: **VoIP/3CX** call routing integrated with **Freshdesk/Zoho Desk** under **ITIL/SLA** workflows.
- Configured **Cisco Meraki** networking for reliable site connectivity; coordinated **ISP/vendor** escalations when outages threatened operations.
- Produced recurring **uptime and incident trend reports** for program leadership.

**Result:**
- Sustained **~98% system uptime** across supported sites.
- Improved mean ticket response time by **~25%** under SLA.
- Leadership gained consistent visibility into incidents and system health without ad-hoc status requests.

**JD keywords hit:** CCaaS ecosystem, SSO, security, reporting/analytics, autonomous ownership, vendor coordination.

---

## Story 2 — Software stack audit & license/access optimization

**Situation:** As user count grew, SaaS accounts, M365 licenses, and AD access rights were not reviewed on a fixed cadence — creating cost leakage and stale access risk.

**Task:** Establish a recurring **software stack audit** process to rightsize licenses, deprovision inactive users, and document findings for leadership renewal decisions.

**Action:**
- Maintained a live **hardware/software asset and license register** tied to user roles and locations.
- Ran **[quarterly / FILL: frequency]** reviews of **M365 seats, endpoint inventory, and AD group membership**; flagged inactive or over-provisioned accounts.
- Deprovisioned **[FILL: number]** stale accounts and rightsized **[FILL: number]** license tiers after confirming with role owners.
- Documented findings in a one-page **utilization summary** recommending keep / downgrade / retire actions before vendor renewals.

**Result:**
- Eliminated **[FILL: number or %]** of unused or redundant access before renewal cycle.
- Reduced security exposure from dormant accounts.
- Gave leadership a defensible basis for **vendor contract** and budget decisions.

**JD keywords hit:** IT auditing, license management, software utilization, audit reports, technology expenditure, contracts.

**⚠️ Before interview:** Fill `[FILL]` fields with real numbers from PATH. If exact dollar savings unknown, use account/seat counts.

---

## Story 3 — Employee tool onboarding framework (train-the-trainer)

**Situation:** New staff onboarding depended on informal handoffs — inconsistent device setup, delayed M365 access, and repeated support tickets for the same steps.

**Task:** Design a **structural onboarding/offboarding framework** so operations and support teams could execute frontline rollout without central IT becoming a bottleneck.

**Action:**
- Authored **SOPs and knowledge-base articles** covering AD provisioning, device imaging, M365/Teams/SharePoint access, MFA enrollment, and VoIP extension setup.
- Built a **checklist-driven onboarding playbook** with defined owners (HR, ops, IT) and escalation paths.
- Delivered **15+ training sessions** to facility staff, ICT officers, and program teams — **80+ people trained** total.
- Paired documentation with a **ticket taxonomy** in Freshdesk so recurring onboarding gaps were visible in reporting.

**Result:**
- Faster, more consistent new-user readiness across sites.
- Fewer repeat tickets on basic access and setup issues.
- Support and operations leads could execute onboarding using the framework without daily IT intervention.

**JD keywords hit:** employee tool onboarding, framework, train operations leadership, documentation, QA through ticket taxonomy.

---

## Story 4 — Executive use-case plan for a new tool / module

**Situation:** Program leadership needed better visibility into facility reporting, IT assets, and support incidents — data was scattered across spreadsheets and ad-hoc exports.

**Task:** Develop a clear **use-case plan** and business case for a unified enterprise operations platform; present value, scope, and rollout approach for leadership buy-in.

**Action:**
- Documented the problem: fragmented data, no single **utilization/reporting** view, manual reconciliation, slow incident tracking.
- Drafted a **use-case memo**: target users, modules (reporting, asset register, NOC/ticketing, dashboards), integration approach (**40+ REST APIs**), security model (role-based auth), and phased rollout.
- Built a working prototype (**Next.js, TypeScript, Prisma, MySQL on Aiven**) with demo data to make ROI tangible.
- Scoped modules mirroring enterprise stack needs: **QA-style validation** (NDWH/CBS matching), **analytics dashboards**, **asset lifecycle**, **incident management**.

**Result:**
- Delivered a deployable platform giving real-time reporting visibility, IT asset register, and incident tracking across **four counties**.
- Demonstrated ability to translate operational needs into an **executive-understandable** tool plan — not just a technical spec.
- Proved end-to-end **software lifecycle** ownership: ROI framing → build → integrate → document.

**JD keywords hit:** use-case plans, executive presentation, ROI, enterprise tool framework, reporting/analytics, QA, deployment.

---

## Story 5 — Reporting/analytics pipeline that cut manual work

**Situation:** Surveillance and operational reporting required manual exports, spreadsheet reconciliation, and delayed error detection across multiple systems.

**Task:** Automate validation and reporting so leadership received accurate, timely **audit-ready analytics** with less manual effort.

**Action:**
- Developed **SQL validation scripts** and automated checks for data-quality (DQA) workflows.
- Built **Power BI, Grafana, and Metabase dashboards** for trend analysis, uptime visibility, and program decision-making.
- Integrated automated outputs into recurring operational review cycles for program and operations leads.

**Result:**
- Reduced manual reporting/processing time by **~40%** (defensible per Master Resume).
- Earlier error detection improved data integrity before leadership reporting deadlines.
- Established a repeatable **analytics layer** on top of the operational stack.

**JD keywords hit:** reporting/analytics, QA, audit reports, executive visibility, automation.

---

## Evidence build plan (post-submit — closes gap to ~90%)

### Week 1
- [ ] Fill all `[FILL]` metrics in Stories 2 and 3 from PATH records.
- [ ] Create **SaaS License Utilization Audit Template** (Excel or Power BI) → GitHub + portfolio link.
- [ ] Write a **1-page Tool Evaluation Memo** (sandbox: compare two CCaaS options on cost, SSO, QA, reporting).

### Week 2
- [ ] Complete **Amazon Connect** or **Twilio Flex** sandbox lab; document SSO, queues, recording/QA, reporting export.
- [ ] README: "CCaaS Stack Lab — Integration Architecture Notes."

### Week 3–4
- [ ] Add **license/vendor tracker module** to NDWH platform (or standalone repo) with utilization export CSV.
- [ ] Consider **ITIL 4 Foundation** exam booking.

### Portfolio links to add when ready
- GitHub: license audit template repo
- GitHub: CCaaS lab notes
- Portfolio case study: "Enterprise Tool Stack Governance Platform"
