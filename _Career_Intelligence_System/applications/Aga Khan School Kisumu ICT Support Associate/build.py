#!/usr/bin/env python3
"""ICT Support Associate, Aga Khan School Kisumu (AKDN Brassring 5021BR). Closes 14 Oct 2026.
THIS PACK ONLY: current PATH role is written as "HMIS Associate" (user instruction).
Master resume and every other pack keep "Health Informatics / HMIS Officer".
Aruba = framed as same family as Cisco Meraki; do not claim hands-on Aruba. ITIL = practice, not a cert.
Run: python3 "applications/Aga Khan School Kisumu ICT Support Associate/build.py"
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT = br.CONTACT
COVER_TITLE = "ICT Support Associate  |  Aga Khan School, Kisumu (5021BR)"

cv = {
"headline": "ICT Support Associate  |  User Support  ·  Networks and Wireless  ·  Cybersecurity  ·  Kisumu",
"metrics": [
    ("120+", "users supported"),
    ("~98%", "system uptime"),
    ("80+", "staff trained"),
    ("~25%", "faster ticket response"),
],
"summary": ("ICT support professional with 3+ years at PATH keeping 120+ users, offices and sites "
    "working at about 98% uptime. I install, configure and maintain hardware, software, networks and "
    "servers, manage wireless access points, keep ICT assets and repairs on track, and handle user "
    "accounts and data under strict protection rules. Patient trainer of non-technical users, with "
    "experience supporting early childhood and youth programmes. BSc Applied Computing (Cybersecurity), "
    "CCNA. Based in Kisumu."),
"skills": [
    ("User support", "First- and second-line support, Freshdesk, Zoho Desk, ITIL workflows, SLAs, ICT procedures and SOPs, knowledge base, user training"),
    ("Hardware and software", "Windows 10/11 installation and imaging (PXE), Microsoft 365, printers, VoIP/3CX, AV and classroom-style setups, software licences"),
    ("Networks and servers", "LAN/WAN, VLANs, DNS/DHCP, VPN, Cisco Meraki wireless access points and switches, MikroTik, structured cabling, Windows and Linux servers, Active Directory, backups"),
    ("Security and assets", "MFA, least privilege, endpoint protection, patching, security awareness, data protection; ICT asset inventory, repairs and vendor coordination"),
],
"experience": [
    {"org": "PATH", "title": "HMIS Associate", "dates": "Mar 2025 to Present",
     "loc": "Kisumu / Nyamira, Kenya (hybrid)", "bullets": [
        "Provide first- and second-line ICT support to 120+ users across offices and health facilities, keeping critical systems above 98% uptime.",
        "Maintain Windows and Linux servers and endpoints: installation, patching, backups, encryption and recovery.",
        "Manage user accounts and access in Microsoft 365 and Active Directory with MFA and least privilege, handling confidential records under data protection rules.",
        "Train staff and non-technical users on digital systems and secure use, and write the SOPs and job aids they keep using.",
        "Ran digital and manual information systems and field ICT for PATH's early childhood development (ECD) programme until its close-out in 2025.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya", "bullets": [
        "Resolved first- and second-line incidents for 120+ users in Freshdesk and Zoho Desk under ITIL and SLA, improving response time by about 25%.",
        "Configured and monitored Cisco Meraki access points, switches and security appliances; diagnosed LAN/WAN, Wi-Fi, DNS, DHCP and VPN faults.",
        "Ran onboarding and offboarding (devices, Active Directory, Microsoft 365, licences), kept the ICT asset inventory accurate and coordinated vendors and ISPs for repairs and connectivity.",
        "Supported endpoint protection, patching and MFA; supported OVC and DREAMS field teams as the ICT person, mentored youth and trained ICT hubs.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Homa Bay, Kenya", "bullets": [
        "Supported LAN/WAN, routers, switches and structured cabling; deployed printers, VoIP phones and desktop imaging; assisted server-room audits and IT documentation.",
    ]},
],
"certs": ("CCNA  |  Microsoft Azure Fundamentals (AZ-900)  |  Google IT Support  |  "
          "IBM Technical Support  |  Microsoft Data Analysis"),
"compact_education": True,
"show_referees": False,
}

COVER_BODY = [
    "The ICT Manager",
    "The Aga Khan School, Kisumu",
    "",
    "Re: ICT Support Associate (5021BR)",
    "",
    "Dear Sir or Madam,",
    "",
    "I am applying for the ICT Support Associate role at The Aga Khan School, Kisumu. I live in Kisumu "
    "and have spent more than three years at PATH, an international health organisation, giving first- and "
    "second-line ICT support to more than 120 users across offices and sites, with critical systems at "
    "about 98% uptime. I am currently an HMIS Associate there.",
    "",
    "Most of my day is the work this role describes. I install, image and maintain Windows devices, "
    "Microsoft 365, printers and VoIP phones, and I maintain the Windows and Linux servers behind our "
    "systems, with patching, backups and recovery. I configure and monitor Cisco Meraki access points and "
    "switches and fix LAN, Wi-Fi, DNS, DHCP and VPN faults. Aruba sits in the same family of managed "
    "wireless as Meraki: the same SSIDs, VLANs, access policies and client troubleshooting, so your network "
    "will feel familiar quickly. I keep the ICT asset inventory accurate, log every issue against an SLA "
    "and coordinate vendors for repairs and connectivity.",
    "",
    "I take cybersecurity and data protection seriously because I handle confidential health records. "
    "I manage accounts with MFA and least privilege, keep endpoints patched and protected, and train "
    "users to spot risks. A school holds sensitive information about children and families, and I would "
    "protect it the same way.",
    "",
    "Training non-technical people is one of my strengths. I have trained more than 80 staff on digital "
    "systems and secure use, and I write simple procedures people keep using. I supported PATH's early "
    "childhood development programme, mentored young people and trained ICT hubs, so I am comfortable "
    "helping teachers and learners. When several things break at once, I sort by impact first: a "
    "classroom that cannot teach comes before a routine request.",
    "",
    "I hold a BSc in Applied Computing (Cybersecurity and Digital Forensics) from KCA University, CCNA, "
    "Microsoft Azure Fundamentals (AZ-900) and Google IT Support, and I work in ITIL-based helpdesk "
    "processes every day. I would be glad to bring this to the school and to the ICT Manager's team.",
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
