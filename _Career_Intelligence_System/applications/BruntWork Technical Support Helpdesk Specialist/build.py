#!/usr/bin/env python3
"""Technical Support & Helpdesk Specialist (Hardware & SaaS), BruntWork client, Melbourne hours.
Portal application: CV upload, assessment questions, technical check, voice recording (plus video).
Angle: hardware + data + platform access, the three areas the role names.
Remote ECD programme entry replaces ICT Intern here (user-confirmed 2026-10-14). No Upwork.
Do not claim IoT sensor products, SaaS employer, or Zendesk as the main daily tool (Freshdesk/Zoho Desk are).
Ticket volume is ~20 a week: never write "a day".
Run: python3 "applications/BruntWork Technical Support Helpdesk Specialist/build.py"
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT = br.CONTACT
COVER_TITLE = "Technical Support & Helpdesk Specialist  |  Hardware & SaaS"

cv = {
"headline": "Technical Support & Helpdesk Specialist  |  Ticket Triage  ·  Zendesk  ·  SLA  ·  Device Troubleshooting",
"metrics": [
    ("120+", "users supported"),
    ("~25%", "faster ticket response"),
    ("250+", "devices set up"),
    ("50+", "sites supported"),
],
"show_referees": False,
"compact_education": True,
"summary": ("Technical support specialist with three years in IT support at PATH, an international NGO, for 120+ users "
    "across 7 offices and 50+ sites, much of it remote. I lodge, triage and resolve tickets under SLAs, keep "
    "clients updated through the ticket lifecycle, and coordinate with data and technical teams until each "
    "issue is closed. I run first-line checks and remote resets on connected devices before escalating, guide "
    "non-technical users through fixes by phone, email and chat, flag recurring issues and write the "
    "troubleshooting guide. Remote-ready for Melbourne business hours."),
"skills": [
    ("Helpdesk and ticketing", "Zendesk, Freshdesk, Zoho Desk, Jira Service Management, Asana; triage, SLA queue management, escalation, ticket documentation, templates and troubleshooting guides"),
    ("Client communication", "Phone, email and chat support; plain-language guidance for non-technical users; updates through the ticket lifecycle; cross-team coordination; English and Swahili"),
    ("Hardware and devices", "Remote resets on cloud-managed network devices (Cisco Meraki); CCTV cameras, biometric scanners, UPS units, tablets, laptops, printers; device imaging; Wi-Fi, LAN/WAN, DNS, DHCP, VPN"),
    ("SaaS and platform access", "Logins, MFA and permissions (Microsoft 365, Entra ID, Active Directory); web platforms (DHIS2, KenyaEMR); sync issues; data checks in SQL and Excel"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kisumu/Nyamira, Kenya (Hybrid / Remote)", "bullets": [
        "Resolve platform access, data and device issues for users at 50+ sites on web-based systems (DHIS2, KenyaEMR), keeping services above 98% uptime.",
        "Coordinate between data, technical and programme teams to fix issues at source; SQL checks I built cut reporting time by about 40%.",
        "Install and maintain biometric scanners, UPS units and tablets at facilities; spot recurring faults across sites, flag the pattern and write troubleshooting guides; trained 80+ staff.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya (multi-site)", "bullets": [
        "Lodged, triaged and resolved tickets from 120+ users in Freshdesk and Zoho Desk under SLAs, keeping users updated until each was closed; response time improved by about 25%.",
        "Chased vendors, ISPs and internal teams for progress and documented every step in the ticket so anyone could pick it up.",
        "Ran first-line checks and remote reboots on Cisco Meraki access points, switches and security appliances across 7 offices from the cloud dashboard before escalating.",
        "Guided non-technical staff through device, login and connectivity fixes by phone, email and Teams chat; managed accounts, MFA and access in Active Directory and Microsoft 365.",
        "Imaged and set up 250+ desktops, laptops and servers across my PATH roles; supported CCTV cameras, printers and field tablets.",
    ]},
    {"org": "PATH", "title": "ECD Programme MIS and ICT Support", "dates": "2024 to 2025",
     "loc": "Remote  |  programme closed 2025", "bullets": [
        "Remote first line for Early Childhood Development field staff: Kobo forms, tablets, logins and sync problems fixed by phone and chat so data reached the server on time.",
        "Onboarded staff remotely with short how-to guides and closed the programme out in 2025 with final data checks, backups and records handover.",
    ]},
],
"certs": ("Google IT Support  |  IBM Technical Support  |  CCNA  |  Microsoft Azure Fundamentals (AZ-900)"),
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "I am applying for the Technical Support & Helpdesk Specialist (Hardware & SaaS) role. For three years I "
    "have worked in IT support at PATH, for 120+ users across 7 offices and 50+ sites, much of it remotely. The "
    "tickets fall into the same three groups your role covers: a device that has gone offline, data that does "
    "not look right, and a user who cannot get into a platform.",
    "",
    "Running a queue is my daily work. I lodge and triage every request, set the priority against the SLA, and "
    "keep the client updated until it is closed. When the fix sits with another team or a vendor, I chase it and "
    "note each step in the ticket so anyone can pick it up. Tightening that process cut our response time by about "
    "25%. My queues have run in Freshdesk and Zoho Desk; Zendesk follows the same ticket model, and I already "
    "track work in Asana.",
    "",
    "For devices, I look after Cisco Meraki access points and switches across 7 offices from the cloud dashboard: "
    "check when the device last reported, run a remote reboot, then talk the person on site through power, "
    "cabling and Wi-Fi before I escalate with what I have tried. I also maintain biometric scanners, UPS units "
    "and tablets at health facilities and have supported CCTV cameras. When the same fault appears at more than "
    "one site, I flag the pattern and write the troubleshooting guide.",
    "",
    "As Health Informatics Officer I sit between the data and technical teams, so I can tell quickly whether a "
    "problem is the device, the data or the account. On PATH's Early Childhood Development programme I was the "
    "remote first line for field staff I rarely met in person. I explain fixes in plain language, by phone, "
    "email or chat.",
    "",
    "I am based in Kenya with a quiet home setup and stable internet, and I can work Monday to Friday during "
    "Melbourne business hours, with flexibility when global support needs it. I hold Google IT Support, IBM "
    "Technical Support, CCNA and Microsoft Azure Fundamentals. Thank you for considering my application.",
    "",
    "Kind regards,",
    "Meshack Ariri",
]


if __name__ == "__main__":
    files = br.pack_files(HERE)
    br.build(cv, files["cv_docx"])
    br.build_cover(COVER_BODY, COVER_TITLE, files["cover_docx"], CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], CONTACT, COVER_TITLE)
    print("Generated:", HERE)
