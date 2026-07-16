# Phase 2 — Deep Skills Intelligence

*Governed by `00_SYSTEM_PROMPT.md`. Every skill below was extracted from your own documents. Nothing here is invented — where a skill is aspirational or unproven, it is flagged.*

---

## A. Skill Inventory (extracted & categorized)

### Health Information Systems (your differentiator)
- KenyaEMR / TaifaCare (support, troubleshooting, monitoring)
- OpenMRS (support, troubleshooting)
- DHIS2 (data, reporting, dashboards)
- NDWH (National Data Warehouse) — data pipelines, reporting
- EMR ↔ Laboratory ↔ Pharmacy integrations
- Health data quality / DQA (data quality assurance)
- Surveillance workflows, indicator tracking, MoH reporting
- Apache Tomcat (EMR app server), MySQL/MariaDB (EMR DB)
- Kobo Toolbox (data collection)

### IT Support & Service Management
- 1st & 2nd line support, 120+ users, ~98% uptime
- Ticketing: Freshdesk, Zoho Desk, Jira Service Management, Zendesk
- ITIL-based workflows, SLA management, incident/escalation, knowledge base
- User onboarding/offboarding, account lifecycle

### Systems Administration
- Windows 10/11; Windows Server 2016/2019/2022
- Active Directory / Azure AD, Group Policy, least-privilege access
- Microsoft 365 / Office 365 (Exchange Online, Outlook, Teams, SharePoint)
- Linux (Ubuntu/CentOS) server maintenance & patching
- Virtualization: VMware, Hyper-V
- Backup/DR: Veeam, rsync, disaster recovery planning

### Networking
- LAN/WAN, VLANs, VPN, DNS/DHCP, TCP/IP
- Routers, switches, structured cabling, Wi-Fi
- Cisco Meraki (dashboard config & monitoring)
- Network performance monitoring & troubleshooting

### Cybersecurity (verify depth before leading with it)
- Endpoint protection, MFA, patch management, access control
- Vulnerability scanning (Nessus, OpenVAS) *[verify hands-on]*
- Incident response, root-cause analysis
- Security awareness training (80+ staff)
- VMware Carbon Black (EDR) *[verify hands-on]*
- Penetration testing / digital forensics *[hackathon-level — label as such]*

### Data, Analytics & Automation
- SQL (MySQL, PostgreSQL), advanced Excel
- Power BI, Grafana, Metabase (dashboards)
- Python (automation/scripting), PowerShell, Bash
- Data validation scripts, operational/uptime reporting
- Microsoft Data Analysis (certified)

### Cloud & DevOps (foundational)
- Microsoft Azure (AZ-900 certified), Azure AD
- AWS (familiarity), Docker (familiarity)
- Git / GitHub workflows (certified)

### Software / Web
- Web development (HTML/CSS, Node.js/Express, some full-stack — freelance)
- REST API integration, authentication flows
- CMS / page-builder environments; on-page SEO
- Mobile app project (JuaX)

### Delivery, Enablement & Business
- Training & capacity building (health workers, ICT officers)
- Technical documentation, SOPs, job aids, knowledge bases
- Stakeholder engagement (county/national/partner teams)
- IT asset & inventory management
- Requirements gathering / systems analysis & design
- M&E / MEL frameworks, DQA, learning sessions, reporting cycles

---

## B. Hidden Skills Discovery

Skills you clearly *have* (evidenced in your own bullets) but rarely name explicitly. These are
often what actually gets people hired — name them.

| Hidden skill | Evidence in your docs | Why recruiters value it |
|---|---|---|
| **Health-systems interoperability thinking** | EMR↔lab↔pharmacy integrations; KenyaEMR/DHIS2/NDWH data flow | Interoperability is the #1 pain in digital health; few support staff understand it |
| **Data governance & quality** | DQA, validation scripts, "data protection policies," audits | Donors fund data quality; it signals seniority |
| **Requirements → solution translation** | "analyzing user requirements and translating them into technical solutions" | This is business-analysis / solutions work, not just support |
| **Stakeholder management** | county/national/partner collaboration, cross-functional teams | Signals you can operate above the ticket queue |
| **Training / adult learning** | trained 80+ health workers, 15+ sessions, ICT officers, facility teams | Enablement scales impact; implementers pay for it |
| **Systems thinking** | capstone (network design), monitoring, uptime, integration | Architectural mindset — a mid/senior signal |
| **Operational reporting & metrics ownership** | uptime, SLA, incident-trend reports for decision-making | Shows business impact, not just activity |
| **Remote service delivery / consulting** | freelance CRM/SaaS + web clients, remote onboarding | Proves you can earn remotely and self-manage |
| **Change/adoption management** | "improve system adoption," onboarding, reducing repeat incidents | Adoption is where most rollouts fail |
| **Multi-site / multi-country operations** | 120+ users across locations, Meraki across regions | Enterprise-scale signal |

---

## C. Missing Terminology Analysis (recruiter language you should be using)

You describe senior work in junior words. Below: the phrase recruiters expect, and where it goes.

| Say this (recruiter language) | Instead of / in addition to | Where to place it |
|---|---|---|
| **Health Informatics** | "HMIS," "health systems" | LinkedIn headline, resume summary |
| **Electronic Medical Records (EMR/EHR)** | "EMR systems" only | Headline, skills, every health bullet |
| **Interoperability (HL7 / FHIR)** | "integrations" | Skills, summary — *then actually learn FHIR (see roadmap)* |
| **Health Information Exchange (HIE)** | — | Summary, if targeting national/HIE roles |
| **Data Quality Assurance (DQA)** | "audited data" | Skills, achievements |
| **Monitoring, Evaluation & Learning (MEL)** | "reporting" | For M&E-flavored roles |
| **Digital Health / Digital Public Goods (DPG)** | "digital systems" | Summary, About |
| **Implementation / rollout / deployment at scale** | "supported" | Achievements — quantify sites |
| **Service Level Agreement (SLA) / MTTR** | "resolved quickly" | Support bullets with numbers |
| **Root Cause Analysis (RCA)** | "troubleshooting" | Support/incident bullets |
| **Identity & Access Management (IAM)** | "Active Directory / user access" | Sysadmin skills |
| **Endpoint Detection & Response (EDR)** | "endpoint protection" | Security skills |
| **Infrastructure as Code / CI/CD** | — | *Aspirational — learn, then claim* |
| **Stakeholder engagement / capacity building** | "training users" | Delivery section |
| **Data pipelines / ETL** | "data collection" | Analytics bullets |
| **Uptime / availability (%) and throughput** | "kept systems running" | Every metric you can |

**Rule:** every senior term you add must be backed by a bullet you can defend in an interview.
Terminology without evidence is the fastest way to fail a technical screen.

---

## D. Skill Broadcasting Plan

For your top under-advertised, genuinely-held skills — what evidence you have, why it matters,
and exactly how to broadcast it on each channel.

### 1. EMR / KenyaEMR / OpenMRS / DHIS2 support & implementation
- **Evidence:** 3 years supporting KenyaEMR/TaifaCare, DHIS2, EMR-lab-pharmacy integrations, facility rollouts.
- **Why valued:** the exact scarce skill funders pay for in East African digital health.
- **CV:** lead your summary + first experience bullets with it, quantify facilities/users.
- **LinkedIn:** put "Health Informatics | EMR (KenyaEMR/OpenMRS) | DHIS2" in the headline; give the About a full paragraph.
- **GitHub:** pin a repo with EMR/DHIS2 SQL queries, a data-quality script, or a dashboard.
- **Portfolio:** a case study "How I stabilized EMR uptime across N facilities."
- **Interview:** a 2-minute story of one integration/uptime win with numbers.
- **Measurable targets to state:** # facilities supported, uptime %, DQA error reduction %, # staff trained.

### 2. Health data analytics & dashboards (SQL + Power BI + Grafana)
- **Evidence:** SQL validation scripts, Power BI/Grafana/Metabase dashboards, "reduced processing time 40%."
- **Why valued:** turns you from "support" into "insight" — higher pay band.
- **CV/LinkedIn:** a dedicated "Data & Analytics" skill cluster; one dashboard achievement bullet.
- **GitHub/Portfolio:** publish a (dummy-data) health dashboard + the SQL behind it.
- **Interview:** show or describe one dashboard and the decision it drove.

### 3. Training & capacity building
- **Evidence:** 80+ health workers, 15+ sessions, ICT officers, facility teams.
- **Why valued:** implementers and INGOs hire for adoption, not just tech.
- **Broadcast:** quantify people trained + adoption/accuracy improvement; add to About + resume achievements.

### 4. IT support at scale + ITIL/SLA discipline
- **Evidence:** 120+ users, ~98% uptime, Freshdesk/Zoho/Jira, SLA reporting.
- **Broadcast:** one strong metrics bullet; keep it as your reliable "floor" credential.

---

## E. Skills Worth Learning — see `05_Learning_Roadmap.md`

The ranked, ROI-scored learning plan (FHIR/HL7, DHIS2 certification, SQL/Power BI depth,
OpenMRS/Docker, English-of-seniority communication, etc.) lives in its own file so it can be
tracked and updated over time.

---

## F. Overselling to Correct (protect credibility)

Soften or requalify these unless you can defend them live:
- "Penetration testing / digital forensics" → "Cybersecurity hackathon participant; security-awareness and vulnerability-reporting experience."
- "Managed Cisco Meraki globally across multiple countries" → keep only if literally true; otherwise "configured and monitored Meraki network devices."
- "Led interoperability across KenyaEMR/DHIS2/NDWH" → "supported / contributed to."
- Nessus/OpenVAS, Carbon Black → keep only with real hands-on; else drop.

Honesty here is not weakness — it's what lets you speak with total confidence in the room, which
raises the "personal confidence before interviews" KPI directly.
