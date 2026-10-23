#!/usr/bin/env python3
"""IT Support Specialist, DHL Express Kenya. Nairobi, permanent, ref AV-382311.
2-3 years. Do not claim Power Automate, Power Apps, SIM-card fleets,
or a DHL shipping platform. ~20 tickets a week, never "a day".
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
    "headline": "IT Support Specialist  |  Microsoft 365  ·  Assets  ·  Networks  ·  Service desk",
    "metrics": [
        ("3 yrs", "IT support"),
        ("120+", "users supported"),
        ("250+", "devices set up"),
        ("~25%", "faster response"),
    ],
    "summary": (
        "IT support specialist with three years at PATH keeping workplace systems reliable for 120+ users "
        "across 7 offices and 50+ sites. I troubleshoot hardware, software, networks and access, run the "
        "ticket through to a written fix, and train people who are not IT. Microsoft 365, SharePoint, "
        "asset records and SLA reports are the daily work. Ready to do this on-site in Nairobi."
    ),
    "skills": [
        ("Workplace support", "Windows 10/11, desktops, printers, peripherals, meeting-room AV, mobile devices, user accounts"),
        ("Microsoft 365", "Outlook, Teams, SharePoint, OneDrive, Entra ID, licences, security groups, MFA"),
        ("Service desk", "Freshdesk, Zoho Desk, ITIL, SLA, incident notes, escalation, cybersecurity, endpoint protection"),
        ("Assets, data, automation", "Device lifecycle and audit-ready inventory, vendor input for replacements, Excel, SQL and Power BI. Power Automate and Power Apps are the Microsoft 365 form of the repeat checks I already run"),
    ],
    "experience": [
        {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
         "loc": "Kenya (hybrid)", "bullets": [
            "Support users on clinical and workplace systems, holding uptime around 98%, and train facility staff and ICT officers so the tool is actually used.",
            "Report incidents, recurring faults and data-quality gaps to managers, with SQL checks and dashboards that cut reporting time by about 40%.",
            "Track tablets, phones and clinic devices through setup, fault, repair and replacement, and escalate what the site cannot fix.",
        ]},
        {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
         "loc": "Kisumu, Kenya", "bullets": [
            "First- and second-line support for 120+ users. Logged, prioritised and documented every ticket in Freshdesk and Zoho Desk, and escalated with the steps already tried. Response time improved by about 25%.",
            "Installed and supported desktops, printers, meeting-room equipment, Windows 10/11 and Microsoft 365, and kept network access up on Cisco Meraki across 7 offices.",
            "Kept an audit-ready asset and licence record, deployed devices for starters, and gave technical input when equipment or connectivity was due for replacement.",
            "Walked non-technical staff through access, mail and SharePoint in plain language, and trained 80+ people on secure use.",
        ]},
        {"org": "PATH", "title": "ECD Programme MIS and ICT Support", "dates": "2024 to 2025",
         "loc": "Remote", "bullets": [
            "Onboarded field users onto digital tools and stayed with them by phone until logins, tablets and sync were working.",
        ]},
    ],
    "certs": "Microsoft Azure Fundamentals (AZ-900)  |  Google IT Support  |  CCNA  |  Microsoft Data Analysis",
    "compact_education": True,
    "show_referees": False,
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: IT Support Specialist, DHL Express Kenya (AV-382311)",
    "",
    "I am applying for the IT Support Specialist role in Nairobi. For three years at PATH I have been the person 120+ users call when a device, an account or a connection stops the work. I log it, set the priority, fix what I can, and escalate the rest with the steps already written down. Response time improved by about 25%, and uptime sits around 98%.",
    "The workplace stack is the one in your advert. Windows 10 and 11, printers, meeting-room equipment, Microsoft 365, SharePoint, Entra ID, and the network underneath. I keep the asset record current, from deployment to replacement, and I join the conversation when something is due to be standardised or bought. I report incidents, repeat faults and what we changed. I explain the fix in plain language and I train the people who will meet it next.",
    "Digital Customer Solutions are the tools a customer must be able to use without calling twice. I already onboard people onto a system, hand them a working device, and stay until the first real use succeeds. Power Automate and Power Apps are how that same repeat work and those same SharePoint lists run themselves inside Microsoft 365. I am ready to do this on-site in Nairobi.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


if __name__ == "__main__":
    files = br.pack_files(HERE)
    br.build(cv, files["cv_docx"])
    br.build_cover(COVER_BODY, "IT Support Specialist", files["cover_docx"], br.CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], br.CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], br.CONTACT, "IT Support Specialist")
    print("Generated:", HERE)
