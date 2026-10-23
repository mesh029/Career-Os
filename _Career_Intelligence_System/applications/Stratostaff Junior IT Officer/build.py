#!/usr/bin/env python3
"""Junior IT Officer, Stratostaff (Nairobi, full time, client unnamed).
ATS pass: headline, summary, skills and bullets use the listing's own duty phrases.
Canonical PATH titles. KCSE grade is unknown: do not print a grade.
Run: python3 "applications/Stratostaff Junior IT Officer/build.py"
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
COVER_TITLE = "IT Support and Systems Officer  |  Nairobi"

cv = {
"headline": "IT Support and Systems Officer  |  Microsoft 365  ·  Networks  ·  Cybersecurity  ·  Nairobi",
"metrics": [
    ("3 yrs", "IT support"),
    ("120+", "users supported"),
    ("~98%", "system availability"),
    ("~25%", "faster incident response"),
],
"summary": ("IT support and systems professional who keeps 120+ users and critical systems running at "
    "about 98% availability for PATH, an international organisation in Kenya. Three years of hands-on "
    "work across first-line support, networks, Microsoft 365, Google Workspace, user accounts and "
    "cybersecurity. I diagnose and resolve hardware, software, network and user-access issues fast, "
    "escalate complex incidents with a clean record, keep IT asset registers accurate, and run onboarding "
    "and offboarding with the right access rights. Security controls, software updates, antivirus, backups "
    "and data protection are routine, not afterthoughts. BSc Applied Computing (Cybersecurity), KCSE B+ "
    "and above. Ready to deliver in Nairobi."),
"skills": [
    ("IT support and troubleshooting", "First-line technical support, hardware, software, network and user-access issues, escalate complex incidents, service and incident records"),
    ("Systems and network administration", "Computers, network infrastructure, user accounts, Microsoft 365, Google Workspace, business applications, system availability"),
    ("IT asset and user management", "IT asset and equipment registers, device configuration and deployment, user onboarding and offboarding, access rights"),
    ("Cybersecurity, backup and monitoring", "Security controls, software updates, antivirus and endpoint protection, backups, access management, data protection, IT monitoring and basic IT reports"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kenya (hybrid)", "bullets": [
        "Provide first-line technical support to 120+ users: diagnose and resolve hardware, software, network and user-access issues, and escalate complex incidents with a written record.",
        "Administer computers, user accounts, Microsoft 365 and business applications, with backups, software updates and access management that keep critical systems near 98% availability.",
        "Help implement and maintain technology solutions, monitor systems, keep accurate IT and incident records, document recurring issues and solutions, and prepare basic IT reports.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya", "bullets": [
        "First-line IT support for 120+ employees in Freshdesk and Zoho Desk. Incident response time improved by about 25%.",
        "Day-to-day network administration on Cisco Meraki: access points, switches, Wi-Fi, DNS, DHCP and VPN, plus user accounts in Active Directory and Microsoft 365.",
        "Device configuration and deployment, user onboarding and offboarding, accurate IT asset and equipment registers, and the right access rights on arrival and exit.",
        "Endpoint protection, antivirus, patching and MFA. Supported Google Workspace users alongside Microsoft 365.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Homa Bay, Kenya", "bullets": [
        "Supported computers, printers, LAN/WAN and VoIP, logged incidents, and helped with IT documentation and user requests.",
    ]},
],
"certs": ("Google IT Support  |  Microsoft Azure Fundamentals (AZ-900)  |  "
          "IBM Technical Support  |  Microsoft Data Analysis"),
"compact_education": True,
"show_referees": False,
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: Junior IT Officer (Nairobi, contract)",
    "",
    "I am applying for the Junior IT Officer role with your client in the oil and gas sector. For three years "
    "at PATH I have kept 120+ users and critical systems running at about 98% availability, and I am ready "
    "to bring that to your client on contract in Nairobi.",
    "",
    "In an operation like yours, a locked account or a dead laptop stops work that costs money by the hour. "
    "I come from the same kind of pressure: at PATH, downtime stalls health facilities and puts reporting "
    "deadlines at risk, so I fix fast, fix the right layer, and keep the record straight.",
    "",
    "My day is the work in your advert. I diagnose and resolve hardware, software, network and user-access "
    "issues, and I escalate anything that needs a senior engineer with the incident already documented. I "
    "look after computers, user accounts, Microsoft 365 and Google Workspace, and I configure and deploy "
    "devices when people join or leave. The IT asset register stays current, and access rights are opened "
    "and closed with the person, not left behind.",
    "",
    "I also keep the routine controls that stop small problems becoming outages: software updates, antivirus "
    "and endpoint protection, backups, and data-protection rules for confidential records. A cleaner "
    "incident process I helped run cut response time by about 25%.",
    "",
    "I attained KCSE grade B+ and above, and I hold a BSc in Applied Computing from KCA University, plus Google IT Support and Microsoft Azure "
    "Fundamentals (AZ-900). I learn new business applications quickly, and I write tickets and short guides "
    "that non-technical colleagues can follow.",
    "",
    "Thank you for considering my application. I would be glad to discuss the role.",
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
    pb.build_cv_pdf(cv, files["cv_pdf"], CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], CONTACT, COVER_TITLE)
    br.build_application(cv, COVER_BODY, COVER_TITLE, files["combined_docx"], CONTACT)
    pb.build_application_pdf(cv, COVER_BODY, files["combined_pdf"], CONTACT, COVER_TITLE)
    br.CONTACT = original
    print("Generated:", HERE)
