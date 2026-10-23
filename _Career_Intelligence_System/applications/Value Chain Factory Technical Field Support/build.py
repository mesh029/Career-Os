#!/usr/bin/env python3
"""Technical Field Support (Evergreen Requisition), Value Chain Factory. Nairobi, nationwide travel.
Integr8 careers portal. Closes 31 Dec 2026.
Canonical PATH titles. IRS = one 2023 campaign, IT Assistant, ODK/Kobo, no employer name, no device-fleet claim.
Confirmed 2026-10-07: 50+ facilities, 3-4 counties, KenyaEMR install/upgrade, biometric scanners, UPS,
tablets, document scanners, driving licence. Not claimed: POS, access control, solar.
Run: python3 "applications/Value Chain Factory Technical Field Support/build.py"
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT = (
    "Nairobi / Kisumu, Kenya  |  +254 741 174 779  |  aririmeshack@gmail.com  |  "
    "linkedin.com/in/meshack-ariri  |  meshreallycodes.online"
)
COVER_TITLE = "Technical Field Support  |  Value Chain Factory, Nairobi"

cv = {
"headline": "Technical Field Support  |  Government System Rollout  ·  50+ Sites  ·  Biometric and Network Devices  ·  Asset Management",
"metrics": [
    ("50+", "facilities supported"),
    ("120+", "users across sites"),
    ("~98%", "system uptime"),
    ("80+", "users trained"),
],
"summary": ("Field IT support professional with 3+ years at PATH rolling out and supporting hardware and "
    "systems across 50+ health facilities in 3+ counties, including installing and upgrading KenyaEMR, a "
    "Ministry of Health national system. I check site readiness, install and test computers, tablets, "
    "printers, document scanners, fingerprint scanners, UPS units and network equipment, hand over with "
    "clean records, and keep sites running with support and preventive maintenance. Valid driving licence; "
    "ready to travel nationwide."),
"skills": [
    ("Deployment and installation", "Site readiness checks, installation, configuration, testing, tagging and handover of computers, laptops, tablets, printers, document scanners, fingerprint (biometric) scanners, routers, switches and access points; device imaging"),
    ("Support and maintenance", "First- and second-line support, hardware and peripheral faults, preventive maintenance, repairs, replacements and vendor coordination, escalation, Freshdesk and Zoho Desk"),
    ("Connectivity and power", "LAN, Wi-Fi, Cisco Meraki, MikroTik, routers, switches, modems, structured cabling, VPN, internet provider liaison; UPS installation, battery replacement and maintenance; power and surge-risk reporting"),
    ("Assets, security and training", "Hardware registers (serial numbers, sites, users, status, maintenance history), audits; passwords, access control, updates, endpoint protection; user training, guides and checklists"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kisumu / Nyamira, Kenya (multi-site)", "bullets": [
        "Installed and upgraded KenyaEMR, a Ministry of Health national system, at health facilities, and support 50+ facilities across 3+ counties on site, keeping critical services above 98% uptime.",
        "Install and maintain the computers, printers, document scanners, fingerprint scanners for patient identification, network equipment and servers at each facility.",
        "Install and maintain UPS backup (including battery replacement); diagnose hardware, connectivity and power faults on site, fix them or escalate to vendors with full notes.",
        "Train facility staff on device use, troubleshooting and data security; write job aids, checklists, and site visit, uptime and incident reports.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya (multi-site)", "bullets": [
        "First- and second-line support for 120+ users across sites in Freshdesk and Zoho Desk; response time improved by about 25%.",
        "Configured Cisco Meraki access points and switches, fixed LAN and Wi-Fi faults with internet providers, deployed devices, kept the asset inventory accurate and coordinated vendor repairs.",
        "Set up and supported tablets and phones for OVC and DREAMS field teams, with connectivity and data tools, so staff could report on time. Trained 80+ users across programmes.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Homa Bay, Kenya", "bullets": [
        "Supported facility data-system deployment: LAN/WAN, routers, switches and structured cabling, printers, VoIP phones and desktop imaging; assisted server-room audits.",
    ]},
    {"org": "Indoor Residual Spraying (IRS) Campaign", "title": "IT Assistant (short-term)", "dates": "2023",
     "loc": "Homa Bay County, Kenya", "bullets": [
        "Supported field teams on ODK / Kobo Collect data collection during a county-wide campaign.",
    ]},
],
"certs": ("CCNA  |  Google IT Support  |  IBM Technical Support  |  "
          "Microsoft Azure Fundamentals (AZ-900)"),
"compact_education": True,
"show_referees": False,
}

COVER_BODY = [
    "The Hiring Team",
    "Value Chain Factory, Nairobi",
    "",
    "Re: Technical Field Support (Evergreen Requisition)",
    "",
    "Dear Hiring Team,",
    "",
    "I am applying for the Technical Field Support role. For more than three years at PATH I have rolled out "
    "and supported hardware and systems across more than 50 health facilities in several Kenyan counties, "
    "including installing and upgrading KenyaEMR, a Ministry of Health national system. Most of that work "
    "happens on site, not behind a desk.",
    "",
    "Your rollout cycle is work I know. Before a deployment I check the site: power, connectivity, space and "
    "who will use the equipment. I install, configure and test computers, tablets, printers, document "
    "scanners, fingerprint scanners for patient identification, UPS units, routers, switches and access "
    "points, then tag, document and hand them over. After go-live I give first- and second-line support, do "
    "preventive maintenance including UPS battery replacement, and coordinate vendors and internet providers "
    "when a fault is outside my hands. POS terminals sit in the same family as the devices I already deploy: "
    "the same readiness checks, configuration, testing and register discipline.",
    "",
    "Records are where field projects succeed or fail, so I keep the asset register exact: serial numbers, "
    "sites, users, dates, maintenance history and status. I write installation, site visit and incident "
    "reports that a project manager can act on, and I report power, cabling and security risks before they "
    "become outages. I have trained more than 80 non-technical users on device care, basic troubleshooting "
    "and data security, with short guides they keep using.",
    "",
    "I hold a BSc in Applied Computing from KCA University, plus CCNA, Google IT Support and Microsoft Azure "
    "Fundamentals, and a valid driving licence. I work well on my own in the field, I am ready to travel "
    "across the country, and I can work flexible hours during rollouts and emergencies. I would welcome the "
    "chance to support your deployment.",
    "",
    "Yours faithfully,",
    "Meshack Ariri",
]


if __name__ == "__main__":
    files = br.pack_files(HERE)
    original = br.CONTACT
    br.CONTACT = CONTACT
    br.build(cv, files["cv_docx"])
    br.build_cover(COVER_BODY, COVER_TITLE, files["cover_docx"], CONTACT)
    br.build_application(cv, COVER_BODY, COVER_TITLE, files["combined_docx"], CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], CONTACT, COVER_TITLE)
    pb.build_application_pdf(cv, COVER_BODY, files["combined_pdf"], CONTACT, COVER_TITLE)
    br.CONTACT = original
    print("Generated:", HERE)
