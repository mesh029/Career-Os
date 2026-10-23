#!/usr/bin/env python3
"""IT Associate, ERP Support, CFAO Mobility Kenya (Head Office, Nairobi).
Reports to the IT Business Applications Administrator. Close 7 Oct 2026, 5 PM, web form.
The form takes one PDF: upload "Meshack Ariri Cover Letter and CV.pdf".
Do not claim SAP, Syspro, Navision, Dynamics 365, Sage, Synertrade, Fleetwave or Annata.
Salesforce = PATH tickets resolved (login, access, forms, reports), not tenant admin.
Paystack = project-based integrations, not Stripe.
Run: python3 "applications/CFAO Mobility IT Associate ERP Support/build.py"
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
COVER_TITLE = "IT Associate, ERP Support  |  CFAO Mobility Kenya"

cv = {
"headline": "IT Associate, ERP Support  |  Business Systems  ·  User Access  ·  SLA  ·  Vendors and Licensing",
"metrics": [
    ("3+ yrs", "business systems support"),
    ("120+", "users supported"),
    ("~98%", "system uptime"),
    ("~25%", "faster ticket response"),
],
"summary": ("IT associate with 3+ years at PATH supporting business-critical enterprise systems for 120+ "
    "users: KenyaEMR/TaifaCare, DHIS2, Salesforce and Microsoft 365. I give first and second line support "
    "under SLA, manage user roles and access reviews, keep licence inventories, work with vendors and service "
    "providers, run data imports, cleaning and validation, test changes before go-live, look after backups and "
    "recovery, and train users with guides they actually use. Integrations with laboratory, pharmacy, national "
    "reporting and payment systems. CCNA, AZ-900, BSc Applied Computing. Ready to relocate to Nairobi."),
"skills": [
    ("Business systems support", "Level 1 and 2 support for enterprise applications (KenyaEMR/TaifaCare on OpenMRS, DHIS2, Salesforce user side, Microsoft 365, Zoho); key-user training and coordination; root cause analysis"),
    ("Access, security, compliance", "Roles and permissions, user access and licence reviews, least privilege, deprovisioning, MFA, Active Directory / Entra ID, encryption; Kenya Data Protection Act awareness"),
    ("Data and change", "Data imports, cleansing and validation (SQL: MySQL, PostgreSQL), testing and QA before go-live, release notes, Excel (Power Query, VBA), Power BI reporting"),
    ("Continuity and integration", "Backups and disaster recovery, patching and updates of application servers (Windows, Linux, Tomcat, MySQL); REST API integrations (NDWH, lab and pharmacy, Paystack / M-Pesa)"),
    ("Service, vendors, licensing", "Freshdesk, Zoho Desk, Jira Service Management, ITIL, SLA; vendor and ISP evaluations, quotes and renewals; licence and asset inventory; SOPs and user guides"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kisumu/Nyamira, Kenya", "bullets": [
        "Support and stabilise KenyaEMR/TaifaCare and DHIS2, the business-critical systems for clinical and reporting users across facilities, at over 98% uptime; first point of contact for users, escalating what cannot be fixed locally with clear diagnostics.",
        "Maintain the Windows and Linux servers that host these systems: backups, encryption, patching, updates and disaster recovery.",
        "Support integrations between the EMR, laboratory and pharmacy systems, and synchronise facility data to national systems through NDWH APIs.",
        "Run data-quality work: SQL validation, data cleansing and audits of data flow against national standards; automation cut manual reporting time about 40%.",
        "Train facility staff, ICT officers and programme teams on system modules and secure use; write SOPs, user guides and uptime reports.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya", "bullets": [
        "Provided first and second line support to 120+ users under ITIL/SLA in Freshdesk and Zoho Desk, cutting response time about 25%; handled about 20 tickets a week.",
        "Resolved Salesforce tickets for PATH users: login, access, forms and reports.",
        "Administered Active Directory and Microsoft 365 roles and access; ran recurring licence and access reviews, deprovisioned inactive users and kept a live software licence inventory.",
        "Coordinated vendor and ISP evaluations, gathered requirements and quotes, and prepared renewal inputs for management sign-off.",
        "Wrote knowledge-base articles and onboarding guides; supported endpoints, connectivity, backup and security for staff.",
    ]},
    {"org": "PATH", "title": "ECD Programme MIS and ICT", "dates": "2024 to 2025",
     "loc": "Kenya  |  programme closed 2025", "bullets": [
        "Ran the programme's digital and manual MIS: tested forms before go-live, onboarded users, imported and cleaned data, and kept backups until close-out.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Homa Bay, Kenya", "bullets": [
        "Supported facility system deployment, LAN/WAN, printers and VoIP; tracked Freshdesk tickets under SLA and contributed to IT documentation and audits.",
    ]},
],
"projects": [
    {"title": "Payment integrations (independent, project-based)", "dates": "2023 to Present",
     "org": "Small business clients", "bullets": [
        "Integrated Paystack payment APIs, including M-Pesa STK push, into more than one business system so they could collect payments across channels.",
    ]},
],
"certs": ("CCNA  |  Microsoft Azure Fundamentals (AZ-900)  |  Google IT Support  |  "
          "IBM Technical Support  |  Microsoft Data Analysis  |  GitHub Professional"),
"compact_education": True,
"referees": [
    "Patrick Ondieki, ICT Officer, PATH  |  pondieki@path.org",
    "Marvin Ngosa, Systems Administrator, PATH  |  mngosa@path.org",
    "Gadaffi Ochieng, Procurement Officer, Ampath  |  ochienggadaffi@gmail.com",
],
}

COVER_BODY = [
    "Dear Hiring Manager,",
    "",
    "Re: IT Associate, ERP Support",
    "",
    "I am applying for the IT Associate, ERP Support role at CFAO Mobility Kenya. For more than three years at "
    "PATH I have supported the business-critical systems an organisation runs on: KenyaEMR and DHIS2 across "
    "health facilities, Salesforce, and Microsoft 365, for more than 120 users, at about 98% uptime.",
    "",
    "Much of your job description is my daily work. I take first-line tickets under SLA and close them, and I "
    "escalate what I cannot fix with the diagnostics the next person needs. I manage user roles and run access "
    "and licence reviews, which is where segregation of duties starts. I keep the licence inventory, gather "
    "quotes and renewal inputs from vendors, and hold service providers to what was agreed. I run data imports "
    "and cleansing with SQL validation, test changes before they go live, and look after backups and recovery on "
    "the servers that host our systems. I have also supported integrations between the EMR, laboratory, "
    "pharmacy and national reporting systems, and built payment integrations with Paystack and M-Pesa.",
    "",
    "Training is the part I enjoy most. I have trained more than 80 staff and written the guides they keep "
    "using, and I am used to working through key users at each site, which is how your super-user model works.",
    "",
    "SAP, Dynamics 365, Sage and the rest of your stack run on the disciplines I already apply every day: "
    "users, roles, data, vendors, licences, SLAs and uptime. I learn a new system with the users and the "
    "documentation side by side, and I would be productive on yours quickly. I hold CCNA and Azure Fundamentals "
    "(AZ-900) and a BSc in Applied Computing, and I am ready to relocate to Nairobi.",
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
    br.build_application(cv, COVER_BODY, COVER_TITLE, files["combined_docx"], CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], CONTACT, COVER_TITLE)
    pb.build_application_pdf(cv, COVER_BODY, files["combined_pdf"], CONTACT, COVER_TITLE)
    print("Generated:", HERE)
