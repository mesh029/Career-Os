#!/usr/bin/env python3
"""IT Support Specialist III, Compassion International, R8693, Nairobi.
Deadline 26 Oct 2026. Canonical titles. About three years, not five.
No IDS product, no invented faith testimony, no access-control install claim.
Run: python3 build.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

cv = {
    "headline": "IT Support Specialist  |  Field offices  ·  Deployments  ·  VPN  ·  Backups",
    "metrics": [
        ("250+", "devices set up"),
        ("120+", "users supported"),
        ("~98%", "system uptime"),
        ("7", "offices supported"),
    ],
    "summary": (
        "IT support specialist with three years at PATH keeping field offices working: software rollout, "
        "desktop and laptop setup, ticket triage, and servers that can be restored. I have deployed "
        "KenyaEMR across facilities, supported 120+ users and 250+ devices over 7 offices, and held "
        "uptime around 98%. Remote access and VPN, written backup and recovery steps, and training "
        "for the person who will take the next ticket are the daily work. Ready to do this from Nairobi."
    ),
    "skills": [
        ("Field-office support", "Windows 10/11, desktops, laptops, printers, tablets, imaging, diagnostic troubleshooting, hardware installs, Microsoft 365"),
        ("Implementation", "Software rollout and deployment, requirements, schedule and per-site tracker, Asana, MS Project, Monday.com, Jira, Freshdesk"),
        ("Infrastructure", "Server rooms, Windows and Linux servers, backups, encryption, disaster recovery procedures, LAN/WAN, VPN, Cisco Meraki, DNS, DHCP"),
        ("Security and users", "Vulnerability reviews, patching, MFA, endpoint protection, firewall alerts, SOPs, training end users and ICT officers"),
    ],
    "experience": [
        {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
         "loc": "Kenya, multi-site", "bullets": [
            "Maintain the Windows and Linux servers that hold programme data across facilities in 3–4 counties: backups, encryption, patching, and a written recovery procedure. Uptime sits around 98%.",
            "Review those servers and the Microsoft 365 mail platform for weak access, missing patches, and backup gaps. Write the vulnerability and the fix. Firewall and security-appliance alerts are the network check.",
            "Last stop on faults the site cannot close. Restore the service, write the cause, and update the procedure so the same outage does not return.",
            "Train facility staff and ICT officers on the deployed system and on secure use, and coach the first-line fix. Weekly and monthly notes go to managers with what is done, pending, and blocked.",
        ]},
        {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
         "loc": "Kisumu, Kenya", "bullets": [
            "First and second line for 120+ users across 7 offices. Installed and upgraded Windows, Microsoft 365, printers, and meeting-room equipment, and triaged the ticket in Freshdesk and Zoho Desk. Response time improved by about 25%.",
            "Coordinated KenyaEMR implementation at facilities: the schedule, the per-facility tracker, equipment and transport, contractor sign-off, and spend tracked on the purchase request.",
            "Set up remote access and VPN on Cisco Meraki, with DNS, DHCP, and Wi-Fi, so staff at a facility could reach the system. Imaged desktops and laptops as part of 250+ devices.",
            "Ran joiner and leaver steps: account, device, access, and the knowledge-base article. Trained 80+ staff. Supported OVC and DREAMS field teams with tablets, connectivity, and data tools.",
        ]},
        {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
         "loc": "Homa Bay, Kenya", "bullets": [
            "Hands-on in the server room and on the desk: routers, switches, cabling, desktop imaging, printers, and VoIP, logged in Freshdesk.",
            "Shadowed firewall rules, VLAN segmentation, and Linux server provisioning, and wrote the procedure.",
        ]},
    ],
    "certs": "CCNA  |  Microsoft Azure Fundamentals (AZ-900)  |  Google IT Support",
    "compact_education": True,
    "show_referees": False,
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: IT Support Specialist III, Nairobi (R8693)",
    "",
    "I am applying for the IT Support Specialist III role in Nairobi. For three years at PATH I have been the person who deploys the system, fixes the desktop, and keeps the server recoverable. I have set up 250+ devices, supported 120+ users across 7 offices and 50+ facilities, and held uptime around 98%. I can work from the Nairobi office, and travel of about 10% of the schedule fits the field visits I already make.",
    "I plan a rollout on a tracker, install and upgrade the software and the hardware, and triage what the first line cannot finish. Remote access and VPN are how staff reach the system from a facility. I write the backup and recovery steps, and I train the user and the colleague who will take the next ticket. Where a server or the mail platform is weakly configured, I record the gap and apply the patch, the access change, or the backup fix. Firewall alerts are how I see a problem on the network before it becomes an outage.",
    "PATH's programmes include children and vulnerable households. ECD ran until it closed in 2025, and I supported OVC and DREAMS in the field. Accounts stay limited to the person who needs them. I will follow Compassion's child-protection reporting rule on every system I touch. I hold a BSc in Applied Computing. I can start after my notice period at PATH.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


if __name__ == "__main__":
    files = br.pack_files(HERE)
    br.build(cv, files["cv_docx"])
    br.build_cover(COVER_BODY, "IT Support Specialist III", files["cover_docx"], br.CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], br.CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], br.CONTACT, "IT Support Specialist III")
    print("Generated:", HERE)
