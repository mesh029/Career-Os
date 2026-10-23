#!/usr/bin/env python3
"""Computer Management Assistant, U.S. Embassy Nairobi (Diplomatic Technology Office).
LE-1810-9, KES 3,068,155/yr. Close 4 Oct 2026 (ERA, erajobs.state.gov). 2 vacancies.
Requires 7 years LAN/WAN + customer support; candidate has ~3.5 (Apr 2023 onward). Built anyway
at the candidate's request. Never state or imply 7 years. Answer ERA screening questions truthfully.
Do not claim Power Automate, SharePoint tenant administration, digital signage or DoS systems.
Run: python3 "applications/US Embassy Kenya Computer Management Assistant/build.py"
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
COVER_TITLE = "Computer Management Assistant  |  U.S. Embassy Nairobi"

cv = {
"headline": "Computer Management Assistant  |  LAN/WAN · VPN · Servers · Microsoft 365  |  Tier 2/3 Support",
"metrics": [
    ("120+", "users, multi-site"),
    ("~98%", "uptime"),
    ("CCNA", "certified"),
    ("Tier 2/3", "support + projects"),
],
"summary": ("IT systems and network professional with 3.5 years at PATH, an international health "
    "organisation, as the main ICT point of contact for multi-site operations. I run LAN/WAN, VPN, "
    "routers, switches, firewalls and wireless; physical and virtual servers; and Microsoft 365, "
    "SharePoint, OneDrive and Active Directory for 120+ users at about 98% uptime. I take tier 2 and "
    "tier 3 tickets to closure with documented steps, set up mobile devices and secure remote access, "
    "run training sessions that move users onto better tools, and scope equipment and services for "
    "procurement. CCNA, AZ-900, BSc Applied Computing (Cybersecurity and Digital Forensics). Ready to "
    "relocate to Nairobi and to undergo a background investigation."),
"skills": [
    ("Networks and remote access", "LAN/WAN, TCP/IP, DNS, DHCP, VLANs, routing and switching, VPN and failover, latency and line troubleshooting, Wi-Fi; Cisco Meraki, MikroTik, Fortinet FortiGate; ISP coordination"),
    ("Servers and storage", "Windows Server 2016-2022, Linux (Ubuntu, CentOS), VMware, Hyper-V, Proxmox, backups (Veeam, rsync) and disaster recovery, server-room management"),
    ("Microsoft 365 and identity", "Microsoft 365 (Outlook, Teams, SharePoint, OneDrive), Active Directory / Entra ID, Group Policy, MFA, least-privilege access, account lifecycle"),
    ("Service and mobility", "Tier 2/3 support, Freshdesk, Zoho Desk, Jira Service Management, ITIL and SLA; laptops, phones, tablets and mobile routers set up for secure access"),
    ("Projects, AV and procurement", "Technical project delivery (network setup and migration), requirements and quotes for procurement, VoIP (3CX), AV and conference-room setups, CCTV; tech-talk training, SOPs and change adoption"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kisumu/Nyamira, Kenya  |  full time", "bullets": [
        "Keep critical systems available at over 98% across facilities: Windows and Linux servers, backups, encryption, patching and disaster recovery for hosted applications and data.",
        "Monitor systems and network links proactively, troubleshoot outages and latency with ISPs and site teams, and escalate infrastructure and security incidents with clear records.",
        "Deliver technical rollouts and system integrations: requirements with users, configuration, testing, training and handover.",
        "Train facility staff, ICT officers and programme teams on new tools and secure use; write SOPs, job aids and uptime reports for management.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya  |  full time", "bullets": [
        "Provided tier 1 and tier 2 support, and tier 3 where no one was above me, to 120+ users at about 98% uptime; took each ticket to resolution, documented the steps and closed it under ITIL/SLA, improving response time about 25%.",
        "Configured and monitored Cisco Meraki access points, switches and security appliances; troubleshot LAN/WAN, VPN, DNS, DHCP and Wi-Fi across sites.",
        "Administered Active Directory and Microsoft 365 (Outlook, Teams, SharePoint, OneDrive): provisioning, permissions, group policy, MFA and least-privilege access.",
        "Set up and supported laptops, phones and connectivity for OVC and DREAMS field teams, including accounts and secure access to programme systems.",
        "Installed VoIP, supported AV and conference-room setups, gathered requirements and vendor quotes for equipment and connectivity renewals, and wrote knowledge-base articles.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Homa Bay, Kenya  |  full time", "bullets": [
        "Supported LAN/WAN, routers, switches and structured cabling; assisted server-room audits, desktop imaging (PXE), printers and VoIP; shadowed senior engineers on firewall rules, VLAN segmentation and Linux server provisioning.",
    ]},
],
"certs": ("CCNA  |  Microsoft Azure Fundamentals (AZ-900)  |  Google IT Support  |  "
          "IBM Technical Support  |  GitHub Professional  |  Microsoft Data Analysis"),
"languages": "English (fluent, written and spoken)  ·  Swahili (fluent)  ·  Dholuo (fluent)",
"referees": [
    "Patrick Ondieki, ICT Officer, PATH  |  pondieki@path.org",
    "Marvin Ngosa, Systems Administrator, PATH  |  mngosa@path.org",
    "Gadaffi Ochieng, Procurement Officer, Ampath  |  ochienggadaffi@gmail.com",
],
}

COVER_BODY = [
    "Dear Hiring Manager,",
    "",
    "Re: Computer Management Assistant, Diplomatic Technology Office",
    "",
    "I am applying for the Computer Management Assistant position at the U.S. Embassy in Nairobi. For three "
    "and a half years at PATH I have been the main ICT point of contact for multi-site operations, doing most "
    "of what this role describes: keeping the network up, running servers, closing difficult tickets, setting "
    "up devices, and helping users adopt better tools.",
    "",
    "On networks, I configure and monitor Cisco Meraki switches, access points and security appliances, "
    "troubleshoot LAN/WAN, VPN and latency problems with ISPs and site teams, and keep critical systems "
    "available at about 98%. I run Windows and Linux servers on VMware, Hyper-V and Proxmox with backups and "
    "disaster recovery. On support, I take tier 2 and tier 3 issues across hardware, Microsoft 365, SharePoint "
    "and OneDrive, own them until they are fixed, and write the steps into the ticket before I close it. I "
    "administer Active Directory and Microsoft 365 accounts with MFA and least-privilege access, and I set up "
    "laptops, phones and secure access for field teams.",
    "",
    "I also like the consulting side of the job. I have trained more than 80 staff and run sessions to move "
    "teams onto new systems, delivered rollouts from requirements to handover, and gathered requirements and quotes "
    "for equipment, AV and connectivity purchases. I hold CCNA and Azure Fundamentals (AZ-900) and a BSc in "
    "Applied Computing specialising in cybersecurity and digital forensics.",
    "",
    "My years at PATH have been full-scope: as a sole or main ICT officer I carried networks, servers, users "
    "and projects at the same time, which is the breadth this role asks for. I am ready to relocate to Nairobi "
    "and to undergo the required background investigation.",
    "",
    "Thank you for considering my application.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


if __name__ == "__main__":
    files = br.pack_files(HERE)
    original = br.CONTACT
    br.CONTACT = CONTACT
    br.build(cv, files["cv_docx"])
    br.CONTACT = original
    br.build_cover(COVER_BODY, COVER_TITLE, files["cover_docx"], CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], CONTACT, COVER_TITLE)
    print("Generated:", HERE)
