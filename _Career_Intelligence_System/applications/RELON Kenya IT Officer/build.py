#!/usr/bin/env python3
"""IT Officer, RELON-Kenya (Refugee-Led Organization Network of Kenya). Nairobi head office, Angaza Program.
Ref RE/KE/AS/IT-/012. One-year fixed term, 3-month probation. Reports to Administration Assistant.
Email application to recruits@relonkenya.or.ke by 25 Oct 2026, 5pm EAT. Cover letter + CV.
Two referees, one from the current employer: both PATH referees listed.
Do not claim warranty management or refugee-sector employment.
Run: python3 "applications/RELON Kenya IT Officer/build.py"
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
COVER_TITLE = "Information Technology Officer  |  Nairobi"

cv = {
"headline": "IT Officer  |  Infrastructure  ·  User Support  ·  Cybersecurity and Backup  ·  Microsoft 365  |  NGO",
"metrics": [
    ("250+", "devices set up"),
    ("7", "offices supported"),
    ("120+", "users supported"),
    ("~98%", "system uptime"),
],
"summary": ("IT Officer with three years at PATH, an international NGO in Kenya. I have imaged and set up 250+ "
    "desktops, laptops and servers, and keep networks, internet connectivity and printers running for 120+ "
    "users across 7 offices at about 98% uptime. I manage user "
    "accounts, access and MFA, run backup and recovery for systems holding confidential personal data, keep "
    "the IT asset and licence inventory current, and set staff up on Microsoft 365 and Teams for meetings "
    "and online training. BSc Applied Computing (Cybersecurity), CCNA. Fluent in English, Swahili and Dholuo. Ready to work in Nairobi."),
"skills": [
    ("Infrastructure and networks", "Computers, servers (Windows Server, Linux), LAN/WAN, internet connectivity, wireless (Cisco Meraki, MikroTik), DNS, DHCP, VPN, printers, VoIP, network monitoring, SQL databases (MySQL, PostgreSQL)"),
    ("User support and platforms", "Hardware, software, network and email troubleshooting; Freshdesk, Zoho Desk, Jira Service Management; Microsoft 365, Teams, SharePoint, Google Workspace; virtual meetings and online training support"),
    ("Security, access and backup", "User accounts, access permissions, passwords and MFA (Active Directory, Entra ID); endpoint protection, patching, firewalls; data backup and recovery, encryption, disaster recovery; vulnerability reporting"),
    ("Assets, procurement and data protection", "IT equipment and software licence inventory, licence and access reviews, ISP and vendor evaluations, purchase requests, contractor oversight; Kenya Data Protection Act principles; SOPs and IT policies"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kisumu/Nyamira, Kenya", "bullets": [
        "Maintain physical and remote Windows and Linux servers that host health information systems across 50+ facilities: backups, encryption, patching and disaster recovery, keeping critical services above 98% uptime.",
        "Monitor system performance and security, run audits and access checks, report vulnerabilities, and protect confidential personal data with least-privilege access and secure storage.",
        "Train facility staff, ICT officers and programme teams on systems and secure use; write SOPs and job aids.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya (multi-site)", "bullets": [
        "Provided first and second line support to 120+ users on hardware, software, network and email issues, logged in Freshdesk and Zoho Desk under SLAs; response time improved by about 25%.",
        "Configured and monitored Cisco Meraki access points, switches and security appliances across 7 offices; fixed internet connectivity, Wi-Fi, LAN/WAN, DNS, DHCP and VPN problems.",
        "Imaged and set up desktops, laptops and servers (250+ across my PATH roles) on Windows 10/11; managed user accounts, access and passwords in Active Directory and Microsoft 365; rolled out MFA, endpoint protection and patching.",
        "Kept a live IT equipment and software licence inventory; removed inactive accounts and reassigned unused licences instead of buying new ones; coordinated ISP and vendor evaluations and raised purchase requests.",
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
    "Dear Hiring Team,",
    "",
    "Re: Information Technology (Head Office-Nairobi) – RE/KE/AS/IT-/012",
    "",
    "I am applying for the IT Officer role at RELON-Kenya. For three years at PATH, an international health "
    "NGO, I have run the IT that programme and operations teams depend on: computers, servers, networks, "
    "internet connectivity and support for 120+ users across 7 offices at about 98% uptime. I would like to do "
    "the same at your Nairobi head office, so the Angaza team can spend its time on young refugee and "
    "host-community women, not on broken laptops and dropped connections.",
    "",
    "The work you describe is what I do every week. I troubleshoot hardware, software, network and email "
    "problems and log each one in the helpdesk; tightening that process cut our response time by about 25%. "
    "I have imaged and set up more than 250 desktops, laptops and servers, and I configure and monitor Cisco "
    "Meraki access points, switches and Wi-Fi across 7 offices. I manage user accounts, permissions, passwords "
    "and MFA, so access is ready on a person's first day and removed on their last.",
    "",
    "The servers I maintain hold confidential patient data, so backups, encryption, patching, disaster "
    "recovery and access reviews are routine, guided by the Kenya Data Protection Act. I keep the IT equipment "
    "and licence inventory current, reassign unused licences before buying new ones, and support procurement "
    "by gathering quotes, raising purchase requests and checking vendors' work before sign-off.",
    "",
    "Angaza's mission is close to work I already know. At PATH I was the field ICT support for two community "
    "programmes: DREAMS, an HIV prevention programme for adolescent girls and young women, and OVC, which "
    "supports orphans and vulnerable children and their families. I kept devices, connectivity and data tools "
    "working for the mentors and case workers who met them, and protected the sensitive personal data they "
    "collected. Refugee data needs the same care, and I never forget that every record is a person.",
    "",
    "I have trained 80+ staff across 15+ sessions and set teams up on Teams and cloud tools for meetings and "
    "online training. I speak English, Swahili and Dholuo and explain technology in plain language. I hold a "
    "BSc in Applied Computing (Cybersecurity) from KCA University, plus CCNA and Microsoft Azure Fundamentals, "
    "and I am ready to start in Nairobi. My referees, including my current employer PATH, are on my CV.",
    "",
    "Thank you for considering my application. I would welcome the chance to discuss how I can support "
    "RELON-Kenya's work.",
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
