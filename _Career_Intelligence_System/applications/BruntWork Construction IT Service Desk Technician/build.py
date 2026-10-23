#!/usr/bin/env python3
"""Construction IT Service Desk Technician, BruntWork. Microsoft 365, remote, Manitoba hours.
Facts per 00_Master_Resume.md. Do not claim construction employment, Intune admin,
or shared-mailbox tenancy as a daily console. ~20 tickets a week, never "a day".
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
    "headline": "IT Service Desk Technician  |  Microsoft 365  ·  Entra ID  ·  Remote support",
    "metrics": [
        ("120+", "users supported"),
        ("~25%", "faster response"),
        ("M365", "and Entra ID"),
        ("3 yrs", "service desk"),
    ],
    "summary": (
        "IT service desk technician with three years at PATH supporting 120+ users across 7 offices and 50+ sites, "
        "much of it by phone. I triage the queue by impact and SLA, reset passwords, fix MFA, and put people in "
        "and out of Microsoft 365 cleanly: Outlook, Teams, SharePoint, OneDrive, licences and security groups. "
        "Leavers lose access the same day. Entra ID, Active Directory, Freshdesk. Clear English with people who "
        "are not IT. Available Monday to Friday on Sunnyside, Manitoba hours."
    ),
    "skills": [
        ("Microsoft 365", "Admin Center, Outlook, Teams, SharePoint, OneDrive, licences, mailbox access, security groups"),
        ("Identity", "Entra ID / Azure AD, Active Directory, MFA and authenticator sign-in, password resets, onboarding and offboarding"),
        ("Service desk", "Freshdesk, Zoho Desk, triage, SLA, root cause notes, escalation, knowledge base and SOPs"),
        ("Remote support", "Windows 10/11, Office, printers, VPN, endpoint setup in the same family as Intune"),
    ],
    "experience": [
        {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
         "loc": "Kenya (hybrid)", "bullets": [
            "Microsoft 365 support for staff across sites: Outlook, Teams, SharePoint, OneDrive, licences and group access, with uptime around 98%.",
            "Onboard and offboard in Entra ID and Active Directory. I agree the access with the manager first. Leavers lose the account, the groups and the licence the same day.",
            "Reviewed licences, removed inactive accounts and reassigned spare ones instead of buying new.",
            "Write the root cause and the short guide when the same ticket repeats, and escalate infrastructure, application or vendor faults with the steps already tried.",
        ]},
        {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
         "loc": "Kisumu, Kenya", "bullets": [
            "First- and second-line desk for 120+ users in Freshdesk and Zoho Desk. Impact and SLA set the order. Response time improved by about 25%.",
            "Remote support for Windows 10/11, Office, printers, VPN and MFA, and installed approved software while imaging devices for starters.",
            "Kept users updated until the ticket closed, including when the fix sat with a vendor or the ISP across 7 offices.",
            "Coordinated starters and leavers with managers, wrote the knowledge-base article, and trained 80+ staff.",
        ]},
        {"org": "PATH", "title": "ECD Programme MIS and ICT Support", "dates": "2024 to 2025",
         "loc": "Remote", "bullets": [
            "Remote first line for field staff who were not at a desk: tablets, logins, sync and access, by phone and chat, plus remote onboarding.",
            "Logged each remote fix so the next person on the queue could repeat it without starting over.",
        ]},
    ],
    "certs": "Microsoft Azure Fundamentals (AZ-900)  |  Google IT Support  |  IBM Technical Support  |  CCNA",
    "compact_education": True,
    "show_referees": False,
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: IT Service Desk Technician (Microsoft 365 and User Support)",
    "",
    "I am applying for the IT Service Desk Technician role. For three years at PATH I have been the service desk for more than 120 users: Microsoft 365, Entra ID, and the ticket that has to be triaged, fixed and written down. Outlook, Teams, SharePoint, OneDrive, password resets, MFA, licences and security groups. Shared mailboxes and distribution lists are that same access, on the mail side. Starters get access that matches the role. Leavers lose it the same day. Response time improved by about 25%, and uptime sits around 98%.",
    "A lot of that support is remote. Field staff call when they cannot get into mail, Teams or the VPN, and I walk them through it. Windows, Office, printers and authenticator sign-in are the same calls. I keep the note in the ticket and I add the short guide when the question comes back. Endpoint setup, imaging and policy are the work an Intune console is built to scale.",
    "Your crews are on sites, not at a desk, and they need an account and a working login before the day starts. That is the support I already give to people spread across more than 50 facilities. I am in Kenya, set up to work remotely, and available Monday to Friday during Sunnyside, Manitoba hours. I hold Azure Fundamentals, Google IT Support and CCNA.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


if __name__ == "__main__":
    files = br.pack_files(HERE)
    br.build(cv, files["cv_docx"])
    br.build_cover(COVER_BODY, "IT Service Desk Technician", files["cover_docx"], br.CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], br.CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], br.CONTACT, "IT Service Desk Technician")
    print("Generated:", HERE)
