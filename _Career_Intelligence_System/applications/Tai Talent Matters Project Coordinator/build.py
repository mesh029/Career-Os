#!/usr/bin/env python3
"""Project Coordinator / Project Officer, Tai Talent Matters for a telecom and infrastructure client.
Two-page CV. Canonical titles only; Meshack is never titled "project coordinator".
Confirmed by Meshack 2026-10-08: planned the KenyaEMR rollout schedule and per-facility tracker,
weekly/monthly progress updates, site logistics (equipment, materials, transport), purchase requests
and spend tracking against budget, scheduled and checked contractors on site, minutes and action
follow-up, Asana / MS Project / Monday.com / Excel trackers, Google PM certificate in progress.
Confirmed 2026-10-07: KenyaEMR installs/upgrades at 50+ facilities in 3-4 counties, biometric
scanners, UPS, tablets, document scanners, driving licence.
Not claimed: budget ownership, HSE, permits, PM certification completed, CCNA (unverified).
Run: python3 "applications/Tai Talent Matters Project Coordinator/build.py"
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT = br.CONTACT
COVER_TITLE = "Health Informatics and ICT Officer  |  Technology Rollouts  ·  Kisumu"

cv = {
"headline": ("Health Informatics and ICT Officer  |  Technology Rollouts  ·  Site and Contractor "
             "Coordination  ·  Budget Tracking  ·  Reporting"),
"metrics": [
    ("50+", "sites in a national rollout"),
    ("3–4", "counties covered"),
    ("~40%", "faster reporting"),
    ("80+", "staff trained"),
],
"summary": ("ICT and health informatics professional with 3+ years at PATH, planning and delivering "
    "technology rollouts across 50+ health facilities in 3–4 Kenyan counties, including installing and "
    "upgrading KenyaEMR, a Ministry of Health national system. I plan the schedule and keep the site "
    "tracker, line up equipment, materials, transport and contractors before site work, raise purchase "
    "requests and track spend against budget, and send weekly and monthly progress reports to managers "
    "and county teams. I take minutes, chase actions to closure and flag risks early. Comfortable on site "
    "with engineers across networks, cabling, hardware and power, and fast at learning the technical side "
    "of new work. Plans in Asana, MS Project, Monday.com and Excel; Google Project Management Certificate "
    "in progress. Valid driving licence and ready to travel to sites."),
"skills": [
    ("Planning and tracking", "Rollout schedules, work plans, milestone and site trackers, action logs, risk and issue logs, progress against plan, close-out and handover records"),
    ("Site and technical", "Site readiness and mobilisation, logistics (equipment, materials, transport), installation, testing and go-live, LAN and Wi-Fi (Cisco Meraki), structured cabling, UPS and power backup, biometric scanners, tablets"),
    ("Contractors and vendors", "Contractor scheduling, checking completed work before sign-off, vendor and ISP evaluations, technical requirements and quotes, renewal inputs"),
    ("Cost and records", "Purchase requests, spend tracking against budget, asset and licence registers, licence and access reviews, organised project files"),
    ("Reporting and stakeholders", "Weekly and monthly status reports, meeting minutes and action follow-up, county health teams, facility managers, national teams, training and SOPs"),
    ("Tools", "Asana, MS Project, Monday.com, Jira, Excel (advanced: pivots, Power Query), Google Sheets, Power BI, Microsoft 365, Freshdesk"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kisumu / Nyamira, Kenya (multi-site)", "bullets": [
        "Plan the rollout schedule and keep the per-facility tracker (done, pending, issues) for installing and upgrading KenyaEMR, a Ministry of Health national system, across 50+ facilities in 3–4 counties.",
        "Take each site from readiness and mobilisation through installation, testing, go-live and handover to facility staff, keeping critical systems above 98% uptime after go-live.",
        "Organise equipment, materials and transport before site visits, and deploy the hardware each site needs: fingerprint scanners, UPS power backup, tablets and document scanners.",
        "Schedule cabling, electrical and ISP contractors on site, check their work before sign-off and follow up fixes until the site is ready.",
        "Raise purchase requests and track spending against budget; keep a risk and issue log and escalate what needs national or vendor teams with clear notes.",
        "Send weekly and monthly progress reports to managers and county teams, and monthly reports to national systems on deadline; built automated checks and Power BI dashboards that cut reporting time by about 40%.",
        "Take minutes at review meetings with county and facility teams and follow every action point to closure.",
        "Trained 80+ health workers across 15+ sessions and wrote SOPs and job aids so new systems kept running after handover.",
        "Ran digital and manual information systems for PATH's early childhood development programme to close-out in 2025: trackers, data, backups and complete handover records.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya (multi-site)", "bullets": [
        "Coordinated vendor and ISP evaluations: gathered technical requirements and quotes, compared options and prepared renewal inputs for leadership sign-off.",
        "Delivered network setup and upgrade work across sites with Cisco Meraki access points, switches and security appliances.",
        "Kept the asset and licence registers accurate and ran licence and access reviews that removed unused accounts and wasted spend.",
        "Supported OVC and DREAMS field teams as their ICT person: devices, connectivity, data tools and reporting so mentors and case workers could submit on time.",
        "Built onboarding and offboarding steps (accounts, devices, Microsoft 365 access, SOPs) so new staff were ready on day one.",
        "Tracked requests from 120+ users in Freshdesk and Zoho Desk against service levels, handling about 20 a week and improving response time by about 25%.",
        "Mentored youth and trained ICT hubs, with job aids so the tools stayed in use after each session.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Homa Bay, Kenya", "bullets": [
        "Supported facility data-system deployment, structured cabling, LAN and router and switch setup.",
        "Deployed printers and VoIP phones, and assisted server-room audits and diagnostics.",
        "Contributed to process documentation and internal IT audits.",
    ]},
    {"org": "Indoor Residual Spraying (IRS) Campaign", "title": "IT Assistant (short-term)", "dates": "2023",
     "loc": "Homa Bay County, Kenya", "bullets": [
        "Supported field data collection on ODK and Kobo Collect for a time-bound public health campaign, helping field teams submit accurate data on fixed daily deadlines.",
    ]},
],
"projects": [
    {"title": "Operations and asset-tracking platform", "org": "Independent project",
     "dates": "2023 to Present", "bullets": [
        "Built a web platform (Next.js, TypeScript, MySQL, 40+ REST APIs) with modules for asset tracking, issue tickets, validation checks and reporting dashboards, with role-based access.",
    ]},
],
"certs": ("Google Project Management Certificate (in progress)  |  Google IT Support  |  "
          "Microsoft Data Analysis  |  Microsoft Azure Fundamentals (AZ-900)  |  "
          "IBM Technical Support  |  DHIS2 Academy"),
"compact_education": False,
"languages": "English, Swahili, Dholuo",
"show_referees": True,
}

COVER_BODY = [
    "The Hiring Team",
    "Tai Talent Matters",
    "",
    "Re: Project Coordinator / Project Officer",
    "",
    "Dear Hiring Team,",
    "",
    "I am applying for the Project Coordinator / Project Officer role with your telecom and infrastructure "
    "client. For more than three years at PATH I have planned and delivered technology rollouts across more "
    "than 50 health facilities in 3–4 Kenyan counties, including installing and upgrading KenyaEMR, a "
    "Ministry of Health national system. My title is Health Informatics / HMIS Officer, but a large part of "
    "my job is the day-to-day coordination your advert describes.",
    "",
    "I plan the rollout schedule and keep the site tracker that shows what is done, what is pending and "
    "where the issues are. Before a site visit I line up the equipment, materials and transport. On site I "
    "schedule the cabling, electrical and ISP contractors, check their work before sign-off and follow up "
    "fixes. I deploy the hardware each site needs, from fingerprint scanners to UPS power backup and "
    "tablets. I raise purchase requests, track spending against budget, and flag risks early so they do "
    "not become delays.",
    "",
    "Reporting and follow-up are strengths. I send weekly and monthly progress reports to managers and "
    "county teams, take minutes at review meetings and chase every action point to closure. I built "
    "automated checks and dashboards that cut reporting time by about 40%, trained more than 80 health "
    "workers, and closed out a programme's information systems with complete handover records. I plan in "
    "Asana, MS Project, Monday.com and Excel, and I am completing the Google Project Management "
    "Certificate.",
    "",
    "Fibre, wireless, power and civil works sit in the same family as the networks, structured cabling, UPS "
    "power and contractor work I already coordinate, and I learn quickly alongside engineers. I hold a BSc "
    "in Applied Computing and a valid driving licence, and I am ready to travel to sites. I would welcome "
    "the chance to discuss how I can help keep your client's projects on time.",
    "",
    "Yours faithfully,",
    "Meshack Ariri",
]


if __name__ == "__main__":
    files = br.pack_files(HERE)
    br.build(cv, files["cv_docx"])
    br.build_cover(COVER_BODY, COVER_TITLE, files["cover_docx"], CONTACT)
    br.build_application(cv, COVER_BODY, COVER_TITLE, files["combined_docx"], CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], CONTACT, COVER_TITLE)
    pb.build_application_pdf(cv, COVER_BODY, files["combined_pdf"], CONTACT, COVER_TITLE)
    print("Generated:", HERE)
