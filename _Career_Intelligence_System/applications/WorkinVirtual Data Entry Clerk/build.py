#!/usr/bin/env python3
"""Data Entry Clerk (100% remote, worldwide), WorkinVirtual Private Limited.
USD 18-22/hour. Needs 4+ hours overlap with New York (ET). 1-3 years experience.
WorkinVirtual is a Pakistan-registered remote job board / recruiter. Never pay a fee.
Salesforce = PATH tickets resolved, not admin. Do not claim typing speed tests or CRM admin.
Run: python3 "applications/WorkinVirtual Data Entry Clerk/build.py"
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT = br.CONTACT
COVER_TITLE = "Data Entry Clerk  |  Remote, US Eastern overlap"

cv = {
"headline": "Data Entry and Records Specialist  |  Excel  ·  Google Sheets  ·  Data Validation  |  Remote, ET overlap",
"metrics": [
    ("3+ yrs", "data entry and records"),
    ("~40%", "less manual reporting"),
    ("DQA", "validation checks"),
    ("4+ hrs", "ET overlap daily"),
],
"summary": ("Detail-focused data entry and records professional with 3+ years at PATH, an international "
    "health nonprofit, entering, checking and maintaining records in databases, spreadsheets and online "
    "systems. I verify source documents before entry, catch missing, duplicate and inconsistent records, "
    "correct errors by procedure, and keep files organised and confidential. Comfortable with Excel, "
    "Google Sheets, Microsoft 365 and Google Workspace. Kenya-based, working remotely with at least four "
    "hours of overlap with New York time."),
"skills": [
    ("Data entry", "Accurate entry and updates in databases, spreadsheets and web systems; paper and digital sources; record reconciliation"),
    ("Data quality", "Source verification, missing / duplicate / inconsistent record checks, error correction by procedure, follow-up tracking"),
    ("Tools", "Microsoft Excel (formulas, pivots, filters, Power Query), Google Sheets, Microsoft 365, Google Workspace, Kobo Toolbox, DHIS2, Salesforce (user side)"),
    ("Records and confidentiality", "Naming and filing standards, digital file organisation, backups, basic reports; health-data privacy and access control"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kenya (hybrid)", "bullets": [
        "Enter, review and update health records and programme data in DHIS2, KenyaEMR and Excel, checking each batch against source documents.",
        "Built validation checks that flag missing, duplicate and inconsistent records before reports go out; corrections go back to the right team, and reporting time fell about 40%.",
        "Prepare routine summaries and reports in Excel for programme and leadership teams, on agreed deadlines.",
        "Handle confidential health information under privacy, access and data-handling procedures.",
    ]},
    {"org": "PATH", "title": "ECD Programme MIS and ICT", "dates": "2024 to 2025",
     "loc": "Kenya  |  programme closed 2025", "bullets": [
        "Entered field forms into Excel and Kobo trackers, cleaned and reconciled records, and kept hard-copy and digital files organised and backed up until close-out.",
        "Tracked late and incomplete submissions and followed up with field staff until records were complete.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya", "bullets": [
        "Maintained user and asset records, logged every request in Freshdesk and Zoho Desk, and kept ticket data accurate for SLA reporting.",
        "Resolved Salesforce user tickets for PATH staff (login, access, forms, reports) and wrote step-by-step procedures for routine tasks.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Homa Bay, Kenya", "bullets": [
        "Created and tracked tickets, updated inventory records and contributed to process documentation and internal audits.",
    ]},
],
"certs": ("Microsoft Data Analysis  |  DHIS2 Academy certificate  |  Google IT Support  |  "
          "IBM Technical Support  |  Microsoft Azure Fundamentals (AZ-900)"),
"compact_education": True,
"show_referees": False,
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: Data Entry Clerk (100% remote)",
    "",
    "I am applying for the remote Data Entry Clerk role. For more than three years at PATH, an international "
    "health nonprofit, a large part of my work has been exactly this: entering and updating records in "
    "databases and spreadsheets, checking them against the source, and keeping them accurate and confidential.",
    "",
    "Most of my records are health data, so mistakes matter and privacy is not optional. I check the source "
    "before I enter anything. I look for missing fields, duplicates and entries that do not match, correct them "
    "by the procedure, and send questions to the right person instead of guessing. I built simple validation "
    "checks that catch these problems before a report goes out, which cut our reporting time by about 40%. On "
    "one programme I entered paper field forms into Excel and Kobo, tracked the incomplete ones until they were "
    "fixed, and kept every file named, filed and backed up.",
    "",
    "I work daily in Excel, Google Sheets, Microsoft 365 and Google Workspace, and I pick up new online systems "
    "quickly. I am comfortable with repetitive work and I keep my accuracy on the hundredth record, not just the "
    "first. I am based in Kenya and can work at least four hours of overlap with New York time every working day.",
    "",
    "Thank you for considering my application. I would be glad to do a short test task.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


if __name__ == "__main__":
    files = br.pack_files(HERE)
    br.build(cv, files["cv_docx"])
    br.build_cover(COVER_BODY, COVER_TITLE, files["cover_docx"], CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], CONTACT, COVER_TITLE)
    print("Generated:", HERE)
