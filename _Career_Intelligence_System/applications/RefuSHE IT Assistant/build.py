#!/usr/bin/env python3
"""IT Assistant, RefuSHE (Nairobi). Contract, full time. 2 years asked.
Ref RK/HR/REC26-12 (RefuSHE vacancy table, 1 position).
Email application to hr@refushe.org by 23 Oct 2026: cover letter and CV only.
Do not claim macOS, device wiping or refugee-sector employment.
Run: python3 "applications/RefuSHE IT Assistant/build.py"
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
COVER_TITLE = "IT Assistant  |  Nairobi"

cv = {
"headline": "IT Assistant  |  User Support  ·  Devices and Accounts  ·  Networks and Wi-Fi  ·  Data Protection  |  NGO",
"metrics": [
    ("250+", "devices set up"),
    ("7", "offices supported"),
    ("120+", "users supported"),
    ("~98%", "system uptime"),
],
"summary": ("IT support professional with three years at PATH, an international NGO in Kenya. I support 120+ "
    "users across 7 offices in person, by phone and remotely, have set up 250+ desktops, laptops and servers, "
    "and manage accounts, Wi-Fi, backups and security updates at about 98% uptime on systems holding "
    "confidential data. BSc Applied Computing (Cybersecurity), CCNA. Fluent in English and Kiswahili."),
"skills": [
    ("User support and devices", "First-line support in person, by phone and remote; laptops, desktops, printers, VoIP phones, projectors and meeting-room AV; Windows 10/11; Microsoft 365, Outlook, Teams, SharePoint, Google Workspace; Freshdesk, Zoho Desk"),
    ("Networks and internet", "Office LAN, Wi-Fi (Cisco Meraki, MikroTik), routers and switches, internet connectivity and ISP follow-up, DNS, DHCP, VPN, structured cabling"),
    ("Security and data protection", "User accounts, passwords and MFA (Active Directory, Entra ID); antivirus and endpoint protection, security updates, backup and recovery; phishing and password awareness training; Kenya Data Protection Act, 2019"),
    ("Assets, purchasing and suppliers", "IT asset register, software licence tracking, equipment specifications and purchase requests, ISP and vendor evaluations, contract renewal inputs, contractor checks; support records, SOPs and job aids"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kisumu/Nyamira, Kenya", "bullets": [
        "Maintain physical and remote Windows and Linux servers across 50+ facilities: backups, antivirus, security updates and recovery, keeping critical services above 98% uptime.",
        "Protect confidential personal data with access checks, least privilege and secure storage; report suspicious activity.",
        "Train staff on safe use of systems, passwords and data protection; write SOPs and job aids.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya (multi-site)", "bullets": [
        "Gave first and second line support to 120+ users in person, by phone and remotely, logging every request in Freshdesk and Zoho Desk under SLAs; response time improved by about 25%.",
        "Imaged and set up desktops, laptops and servers (250+ across my PATH roles); installed printers, VoIP phones and meeting-room AV for trainings and online meetings.",
        "Managed user accounts, email, passwords and access in Active Directory and Microsoft 365 for joiners, movers and leavers, using onboarding and offboarding checklists I wrote.",
        "Looked after Cisco Meraki Wi-Fi, switches and routers across 7 offices; followed up internet providers on outages; ran ISP and vendor evaluations and prepared contract renewal inputs.",
        "Kept a live IT asset and licence register; reassigned unused licences; prepared purchase requests with procurement.",
        "Field ICT for DREAMS (HIV prevention for adolescent girls and young women) and OVC (orphans and vulnerable children): devices, connectivity and data tools for mentors and case workers.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Homa Bay, Kenya", "bullets": [
        "Supported LAN/WAN, routers, switches, cabling, printers and VoIP phones; logged tickets under SLA; assisted IT audits.",
    ]},
],
"certs": ("CCNA  |  Microsoft Azure Fundamentals (AZ-900)  |  Google IT Support  |  "
          "IBM Technical Support  |  Cyber Shujaa cybersecurity programme"),
"compact_education": True,
"referees": [
    "Patrick Ondieki, ICT Officer, PATH  |  pondieki@path.org",
    "Marvin Ngosa, Systems Administrator, PATH  |  mngosa@path.org",
],
}

COVER_BODY = [
    "Dear Hiring Manager,",
    "",
    "Re: IT Assistant – RK/HR/REC26-12",
    "",
    "I am applying for the IT Assistant role at RefuSHE. For three years at PATH, an international health NGO "
    "in Kenya, I have kept computers, networks, phones and systems working for 120+ users across 7 offices at "
    "about 98% uptime. I would like to bring that to RefuSHE, so your team can focus on the girls, young women "
    "and families you serve, not on a laptop that won't start or Wi-Fi that keeps dropping.",
    "",
    "First-line support is my daily work. I help staff in person, by phone and remotely, and log every request "
    "in the helpdesk; tightening that process cut our response time by about 25%. I have imaged and set up more "
    "than 250 desktops, laptops and servers, and I set up printers, phones and meeting-room AV for trainings and "
    "online meetings. I manage accounts, email, passwords and access for staff who join, move or leave, using "
    "checklists I wrote so nothing is missed. When the internet drops, I check our network equipment first, then "
    "stay on the provider until it is fixed.",
    "",
    "The systems I maintain hold confidential patient data, so antivirus, security updates, backups and access "
    "reviews are routine, guided by the Kenya Data Protection Act, 2019. I train staff on passwords, phishing and "
    "safe use of systems, in English or Kiswahili, and I am patient with every level of skill. I keep the IT "
    "asset and licence register current and work with procurement on quotes, specifications and renewals.",
    "",
    "RefuSHE's work is close to mine. At PATH I was the field ICT support for DREAMS, an HIV prevention "
    "programme for adolescent girls and young women, and for OVC, which supports orphans and vulnerable "
    "children and their families. I kept devices and data tools working for the mentors and case workers who "
    "met them, and protected the sensitive information they collected. For the girls you serve, a data breach "
    "is a safety risk, and I am committed to gender equality, inclusion and safeguarding.",
    "",
    "I hold a BSc in Applied Computing (Cybersecurity) from KCA University, plus CCNA, Microsoft Azure "
    "Fundamentals and Google IT Support. I am ready to start in Nairobi. My referees, "
    "including my current employer PATH, are on my CV.",
    "",
    "Thank you for considering my application.",
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
