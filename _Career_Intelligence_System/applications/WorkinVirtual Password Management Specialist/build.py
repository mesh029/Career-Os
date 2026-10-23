#!/usr/bin/env python3
"""Password Management Specialist, WorkinVirtual. Remote, worldwide, USD 25-35/hr.
Canonical titles. Entra ID, MFA, SSO, access reviews. No named password-vault product.
ECD remote replaces the intern on this remote-support CV.
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
    "headline": "Password Management Specialist  |  Entra ID  ·  MFA  ·  Access reviews",
    "metrics": [
        ("120+", "accounts administered"),
        ("MFA", "on Entra ID"),
        ("~98%", "system uptime"),
        ("Access", "reviewed on a cycle"),
    ],
    "summary": (
        "Remote password and access specialist with three years supporting PATH users from Kenya. Most of the "
        "account work arrives by ticket, phone, and chat. I create, change, and remove Microsoft Entra ID and "
        "Active Directory accounts for 120+ people across offices and field sites, require MFA, and keep single "
        "sign-on to least-privilege groups. I review access on a cycle, remove inactive accounts, record every "
        "change, and escalate a suspected incident with the notes already written. Authorised to work fully "
        "remote from Kenya, with evening overlap for New York."
    ),
    "skills": [
        ("Identity", "Microsoft Entra ID, Active Directory, MFA, single sign-on, least privilege, role-based access, account recovery"),
        ("Access lifecycle", "Provisioning, deprovisioning, onboarding, offboarding, scheduled access reviews, inactive accounts, licence rightsizing"),
        ("Credentials and records", "Credential handling through Entra ID and MFA. Enterprise password managers store shared secrets under these same rules. Freshdesk, Zoho Desk, SOPs"),
        ("Security operations", "Authentication troubleshooting, incident escalation, endpoint alerts, security documentation, Google Workspace setup for small teams"),
    ],
    "experience": [
        {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
         "loc": "Remote support, Kenya", "bullets": [
            "Support secure sign-in remotely for facility and programme staff on KenyaEMR and DHIS2 across 3–4 counties. Clinical systems stay at about 98% uptime. The account, the MFA prompt, and the access question are handled by phone or ticket when the site is not in the room.",
            "Review who still has access against the role they hold. Remove inactive or overly broad access, write the audit note, and escalate the exception when it does not match the standard.",
            "Write the SOP, the job aid, and the recovery steps for password and sign-in problems, so the next person on the ticket follows the same path. Report a vulnerability or an unauthorized-access concern with the evidence attached.",
            "Train facility staff, ICT officers, and programme teams remotely on secure sign-in and least-privilege use, and confirm they can complete the sign-in before the session ends. I stay on the call until that sign-in succeeds.",
        ]},
        {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
         "loc": "Remote support from Kisumu", "bullets": [
            "Administered Microsoft 365, Active Directory, and Entra ID for 120+ users across 7 offices. Created the account, set the group, required MFA, and kept single sign-on to least privilege. Most requests arrived as a Freshdesk or Zoho Desk ticket.",
            "Ran joiner and leaver steps remotely. A starter received the account, the Microsoft 365 access, and the written steps. A leaver lost the account, the groups, and the licence once the notice was confirmed.",
            "Ran recurring access and licence reviews. Compared the live account with the role, removed inactive and duplicate access, rightsized what remained, and kept a record of the change for the next review.",
            "Took authentication tickets through to a written fix: failed MFA, a locked sign-in, the wrong group, or shared access that should have been removed. Escalated endpoint alerts and anything that looked like unauthorized access. Response time improved by about 25%.",
        ]},
        {"org": "PATH", "title": "ECD Programme MIS and ICT Support", "dates": "2024 to 2025",
         "loc": "Remote", "bullets": [
            "Remote first line for field staff, by phone and chat, on logins, tablets, and sync, including password and access recovery when someone in the field could not sign in.",
            "Onboarded new users remotely onto the programme tools, wrote the procedure, and closed the access out when the programme ended in 2025. The close-out named who had access and when the account was removed.",
        ]},
    ],
    "certs": "Microsoft Azure Fundamentals (AZ-900)  |  Google IT Support  |  CCNA",
    "compact_education": True,
    "show_referees": False,
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: Password Management Specialist",
    "",
    "I am applying for the Password Management Specialist role. For three years at PATH I have administered Microsoft Entra ID and Active Directory for 120+ users: create the account, change the access, remove it when the person leaves, and require MFA. Sign-in is single sign-on with least-privilege groups. I review access on a cycle, remove inactive accounts, and write down every change. I am authorised to work remotely from Kenya.",
    "When someone cannot sign in, I take the ticket in Freshdesk, follow the recovery steps, and escalate a suspected incident with the notes already written. The same onboarding and offboarding ran remotely for field staff: logins, access, and a written procedure. Enterprise password managers hold shared credentials under those same rules. I can cover at least four working hours with New York, 4:00 to 8:00 PM Kenya time until 1 November, and 5:00 to 9:00 PM after that.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


if __name__ == "__main__":
    files = br.pack_files(HERE)
    br.build(cv, files["cv_docx"])
    br.build_cover(COVER_BODY, "Password Management Specialist", files["cover_docx"], br.CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], br.CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], br.CONTACT, "Password Management Specialist")
    print("Generated:", HERE)
