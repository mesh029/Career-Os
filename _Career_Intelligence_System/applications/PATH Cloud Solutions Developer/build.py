#!/usr/bin/env python3
"""Cloud Solutions Developer, PATH, JR2706. Internal application.
This pack only: Health Informatics / HMIS Associate runs Mar 2025 to 30 Sep 2026, not Officer,
and not Present. ICT Associate stays Jan 2024 to Mar 2025. ICT Intern stays.
Do not copy this title or this end date onto other CVs.
No Azure DevOps, Unit4, file-drop, or Salesforce data-sync claim.
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
    "headline": "Cloud Solutions Developer  |  Azure  ·  APIs  ·  Python  ·  CI/CD",
    "metrics": [
        ("120+", "users supported"),
        ("~98%", "system uptime"),
        ("~40%", "faster reporting"),
        ("Azure", "and AWS builds"),
    ],
    "summary": (
        "Cloud solutions developer. Until 30 September 2026 I was a PATH Health Informatics Associate in Kenya, "
        "supporting KenyaEMR and DHIS2 at about 98% uptime, and building Azure services (virtual machines, storage, "
        "databases, Python functions, and websites) and AWS (EC2, S3, and Lambda). I connect systems with REST APIs "
        "and queues, release through GitHub Actions and GitLab CI, and write the SQL and dashboard work that cut "
        "reporting time by about 40%. Before that I was the ICT Associate for 120+ users. Authorised to work in Kenya."
    ),
    "skills": [
        ("Azure and AWS", "Virtual machines, storage, Azure databases, Python functions, websites, EC2, S3, Lambda, Entra ID, AZ-900"),
        ("Integrations", "REST APIs, queues, NDWH, KenyaEMR, DHIS2, EMR–lab–pharmacy, SQL Server, ETL"),
        ("Delivery and identity", "Git, GitHub Actions, GitLab CI, app registrations, service principals, secrets, Entra ID"),
        ("PATH systems", "Workday, Salesforce user support, Power BI, Grafana, Freshdesk, Microsoft 365, servers, training"),
    ],
    "experience": [
        {"org": "PATH", "title": "Health Informatics / HMIS Associate", "dates": "Mar 2025 to 30 Sep 2026",
         "loc": "Kisumu and Nyamira", "bullets": [
            "Support and stabilize KenyaEMR/TaifaCare and DHIS2 across facilities at about 98% uptime. Maintain the Windows and Linux servers that hold the data: backups, encryption, patching, and recovery. Run system audits and write the SOPs, job aids, and uptime reports.",
            "Lead data collection, cleaning, and analysis for care and treatment, PMTCT, and E-TEC. SQL checks, ETL, and Power BI, Tableau, Grafana, and Metabase dashboards cut reporting time by about 40%.",
            "Move facility data through NDWH APIs and support EMR, laboratory, and pharmacy data flow. Connect systems with REST APIs and queues, and release through GitHub Actions and GitLab CI.",
            "Build and change Azure virtual machines, storage, databases, Python functions, and websites, and use AWS EC2, S3, and Lambda. Set up app registrations, service logins, and secrets, and administer Entra ID.",
            "Support Workday, train facility staff, ICT officers, and programme teams, and document the fix when a production service breaks.",
        ]},
        {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
         "loc": "Kisumu, Kenya", "bullets": [
            "First and second line for 120+ users: Freshdesk and Zoho Desk, Microsoft 365, Cisco Meraki, Active Directory, patching, and MFA. Response time improved by about 25%.",
            "Resolved Salesforce tickets for login, access, forms, and reports. Supported OVC and DREAMS field teams, wrote the knowledge base, and trained users and ICT hubs.",
        ]},
        {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
         "loc": "Homa Bay, Kenya", "bullets": [
            "Shadowed senior engineers on Linux server provisioning, firewall rules, and VLAN segmentation, supported routers and switches, and logged the work in Freshdesk.",
        ]},
    ],
    "certs": "Microsoft Azure Fundamentals (AZ-900)  |  GitHub Professional  |  CCNA  |  Microsoft Data Analysis",
    "compact_education": True,
    "show_referees": False,
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: Cloud Solutions Developer, Integrations and Platforms (JR2706)",
    "",
    "I am applying for the Cloud Solutions Developer role. I was a PATH Health Informatics Associate until 30 September 2026. In that role I supported KenyaEMR and DHIS2 across facilities at about 98% uptime, including the servers, the dashboards, and the training for care and treatment, PMTCT, and E-TEC. I also build in Azure (virtual machines, storage, databases, Python functions, and websites) and on AWS (EC2, S3, and Lambda). I connect systems with REST APIs and queues, including facility data through NDWH, and I release through GitHub Actions and GitLab CI. I am authorised to work in Kenya.",
    "Before this I was PATH's ICT Associate, first and second line for 120+ users on Microsoft 365, Freshdesk, and Meraki, including Salesforce tickets for login, access, and reports. I have created app registrations, service logins, and secrets, and I administer Entra ID. I support Workday. Python and SQL checks cut reporting time by about 40%. When a production service breaks, I write the fix down.",
    "I want to learn PATH's current integrations beside the people who own them, and take shared ownership of the pieces I can support well, including the release process, functions, and secrets. I will document what I touch so the work is not held by one person.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


if __name__ == "__main__":
    files = br.pack_files(HERE)
    br.build(cv, files["cv_docx"])
    br.build_cover(COVER_BODY, "Cloud Solutions Developer", files["cover_docx"], br.CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], br.CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], br.CONTACT, "Cloud Solutions Developer")
    print("Generated:", HERE)
