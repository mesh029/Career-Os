#!/usr/bin/env python3
"""Database Support Assistant (REF: DSA/001/2026), Abt Global Central Mechanism
(PMI Evolve Kenya), IRS Busia and Siaya, Kisumu office.
IRS = one campaign, IT Assistant, Homa Bay County, 2023, ODK/Kobo. No employer name.
Do not write "1 year of IRS". Do not claim DHIS2, GPS or device fleet work on the IRS campaign.
DHIS2 hands-on comes from PATH. DHIS2 Academy certificate held.
The portal takes one document: submit "Meshack Ariri Cover Letter and CV".
Run: python3 "applications/Abt Global Database Support Assistant/build.py"
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT = br.CONTACT
COVER_TITLE = "Database Support Assistant  |  IRS Busia and Siaya (REF: DSA/001/2026)"

cv = {
"headline": "Database Support Assistant  |  DHIS2  ·  Data Cleaning  ·  Duplicates and Outliers  |  IRS campaign experience",
"metrics": [
    ("DHIS2", "hands-on + academy"),
    ("IRS", "2023 campaign"),
    ("~40%", "faster reporting"),
    ("Kisumu", "based, office-ready"),
],
"summary": ("Health data and database support professional with 3+ years at PATH keeping DHIS2 and "
    "KenyaEMR data complete, clean and on time. I run data-quality checks (SQL validation, completeness, "
    "duplicates, values that do not add up), trace errors back to source with field teams, and turn "
    "clean data into Excel and Power BI reports. Worked the 2023 IRS campaign in Homa Bay County as IT "
    "Assistant on ODK/Kobo Collect. DHIS2 Academy certificate. BSc Applied Computing. Based in Kisumu."),
"skills": [
    ("Databases and DHIS2", "DHIS2 (data entry, reports, data quality), KenyaEMR/TaifaCare, NDWH sync, SQL (MySQL/PostgreSQL) validation queries"),
    ("Data quality", "Duplicate and completeness checks, outlier review, source verification with field teams, feedback loops, DQA, escalation of gaps"),
    ("Mobile data collection", "ODK / Kobo Collect forms, submissions and sync troubleshooting; paper-to-database entry and reconciliation"),
    ("Excel and reporting", "Formulas, filters and sorting on large datasets, pivots, Power Query, VBA/macros, Power BI dashboards, printed field reports"),
    ("Records and protection", "Hard-copy filing and digital backups, access control, data protection practice (Kenya DPA awareness)"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kisumu/Nyamira, Kenya", "bullets": [
        "Support DHIS2 and KenyaEMR/TaifaCare across health facilities, sustaining >98% uptime so data entry and reporting never stall.",
        "Built SQL validation and data-quality checks for completeness, duplicates and implausible values; errors go back to facilities with a clear list to fix, and reporting time fell about 40%.",
        "Lead collection, cleaning and analysis for care and treatment, PMTCT and E-TEC indicators in Excel (formulas, pivots, Power Query, VBA) with SQL cross-checks.",
        "Synchronise facility data to national systems through NDWH APIs and confirm that what was reported matches the source.",
        "Train facility staff and data clerks on DHIS2, data quality and secure handling of records.",
    ]},
    {"org": "PATH", "title": "ECD Programme MIS and ICT", "dates": "2024 to 2025",
     "loc": "Kenya  |  programme closed 2025", "bullets": [
        "Ran the paper and digital MIS side by side: field forms entered into Excel and Kobo trackers, cleaned, reconciled and reported in Power BI.",
        "Filed hard copies and kept digital backups so every figure could be traced to its source form until close-out.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya", "bullets": [
        "Wrote SQL scripts and automated validation that improved surveillance data accuracy.",
        "Supported OVC and DREAMS field teams as the ICT person: devices, connectivity and data tools so submissions arrived on time.",
        "Provided 1st and 2nd line support to 120+ users under ITIL/SLA ticketing (Freshdesk, Zoho Desk).",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Homa Bay, Kenya", "bullets": [
        "Assisted facility data-system deployment and digitalisation for surveillance and reporting readiness.",
    ]},
    {"org": "Indoor Residual Spraying (IRS) Campaign", "title": "IT Assistant", "dates": "2023  |  one campaign",
     "loc": "Homa Bay County, Kenya", "bullets": [
        "Supported IRS field teams on ODK / Kobo Collect: forms on the phones, daily submissions, and sync problems fixed so spray data reached the server.",
        "Learned the campaign data chain first-hand, from spray operator to team leader to site, and the daily numbers the programme depends on.",
    ]},
],
"certs": ("DHIS2 Academy certificate  |  Microsoft Data Analysis  |  Google IT Support  |  "
          "IBM Technical Support  |  CCNA  |  Microsoft Azure Fundamentals (AZ-900)"),
"compact_education": True,
"languages": "English (fluent)  ·  Swahili (fluent)  ·  Dholuo (fluent)",
"referees": [
    "Patrick Ondieki, ICT Officer, PATH  |  pondieki@path.org",
    "Marvin Ngosa, Systems Administrator, PATH  |  mngosa@path.org",
    "Gadaffi Ochieng, Procurement Officer, Ampath  |  ochienggadaffi@gmail.com",
],
}

COVER_BODY = [
    "Dear Hiring Manager,",
    "",
    "Re: Database Support Assistant (REF: DSA/001/2026), IRS Busia and Siaya, Kisumu Office",
    "",
    "I am applying for the Database Support Assistant role on the Busia and Siaya IRS campaign. I live in "
    "Kisumu, I work in DHIS2 as part of my job, and I have been on an IRS campaign before: I was IT Assistant "
    "on the 2023 campaign in Homa Bay County, supporting spray teams on ODK and Kobo Collect. I know how "
    "campaign data is born in the field and what goes wrong between the phone and the server.",
    "",
    "For more than three years at PATH I have done the work your job description lists. As Health "
    "Informatics / HMIS Officer I support DHIS2 and KenyaEMR across facilities and run the data-quality side: "
    "SQL validation, checks for completeness, duplicates and values that do not make sense, and going back to "
    "the source with the people who entered it when the numbers disagree. That work cut our reporting time by "
    "about 40%. On PATH's ECD programme I ran paper and digital together: field forms entered into Excel and "
    "Kobo trackers, cleaned, reconciled, and filed so every number could be traced back to its form.",
    "",
    "On your campaign that means I can run the daily duplicate report in DHIS2, share the list with field "
    "teams, update the records when their feedback comes in, fill missing fields from verified reports, run "
    "outlier checks in line with MEL guidance, and keep a daily count of submissions per spray operator "
    "against the team leader's numbers. I am quick in Excel with formulas, filters and large datasets, I "
    "enter paper data carefully, and I escalate gaps early instead of letting them pile up.",
    "",
    "I hold a DHIS2 Academy certificate and a BSc in Applied Computing from KCA University. I can commit to "
    "the full campaign, six days a week, Monday to Saturday, from the Kisumu office.",
    "",
    "Thank you for considering my application.",
    "",
    "Sincerely,",
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
