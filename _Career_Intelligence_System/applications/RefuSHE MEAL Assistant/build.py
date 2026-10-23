#!/usr/bin/env python3
"""MEAL Assistant, RefuSHE (Nairobi). Contract, full time. 1 year asked. Reports to MEAL Coordinator.
Email application to hr@refushe.org by 23 Oct 2026: cover letter and CV only.
Also applying for RefuSHE IT Assistant (RK/HR/REC26-12): keep facts identical across both packs.
Do not claim surveys, focus groups, feedback/complaints mechanisms or a statistics degree.
IRS = one campaign, 2023, ODK/Kobo, no employer name.
Run: python3 "applications/RefuSHE MEAL Assistant/build.py"
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
COVER_TITLE = "MEAL Assistant  |  Nairobi"

cv = {
"headline": "MEAL Assistant  |  Data Collection  ·  KoboToolbox / ODK  ·  Data Cleaning  ·  Excel and Power BI  |  NGO",
"metrics": [
    ("80+", "staff trained on data tools"),
    ("50+", "facilities supported"),
    ("~40%", "faster reporting"),
    ("3 yrs", "NGO data work"),
],
"summary": ("MEAL and data professional with three years at PATH, an international NGO in Kenya. I collect, clean "
    "and check programme data on KoboToolbox, ODK, paper forms and DHIS2, correct errors with field staff, and "
    "turn it into Excel and Power BI tables and charts. I have trained 80+ staff on data tools and protect "
    "confidential personal data under the Kenya Data Protection Act. Field ICT for DREAMS and OVC programmes. "
    "English and Kiswahili; willing to travel to field sites."),
"skills": [
    ("Data collection", "KoboToolbox / Kobo Collect, ODK, paper forms and registers, DHIS2, KenyaEMR; form setup and testing; device and sync support"),
    ("Data quality", "Cleaning; checks for errors, missing information and duplicates; source verification, DQA, SQL validation; follow-up with programme staff"),
    ("Analysis and reporting", "Excel (pivots, Power Query, charts), Google Sheets, Power BI; summary tables, trackers, weekly and monthly reports; indicators by age and sex"),
    ("Training, records and data protection", "80+ staff trained on data tools; job aids and SOPs; secure paper and digital filing, backups and access control; Kenya Data Protection Act, 2019"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kisumu/Nyamira, Kenya", "bullets": [
        "Collect, clean and analyse programme data for care and treatment, PMTCT and E-TEC indicators, and produce the Excel and Power BI tables and charts programme teams review.",
        "Built SQL validation and data-quality checks that flag missing, inconsistent and duplicate entries; errors go back to facility staff with a clear list, and reporting time fell about 40%.",
        "Support DHIS2 and KenyaEMR across 50+ facilities; train facility staff on data tools and data quality and write job aids they use after training.",
        "Keep confidential personal data secure with access control, backups and secure storage.",
    ]},
    {"org": "PATH", "title": "ECD Programme MIS", "dates": "2024 to 2025",
     "loc": "Kenya  |  programme closed 2025", "bullets": [
        "Ran digital and manual MIS until close-out: paper and Kobo collection tools, Excel trackers, cleaning, Power BI packs, staff onboarding and secure backups.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya", "bullets": [
        "Field ICT for DREAMS (HIV prevention for adolescent girls and young women) and OVC (orphans and vulnerable children): devices, data tools and reporting so mentors and case workers submitted on time.",
        "Logged, routed and tracked requests from 120+ users until each was closed; trained and onboarded new users on systems.",
    ]},
    {"org": "Indoor Residual Spraying (IRS) Campaign", "title": "IT Assistant", "dates": "2023  |  one campaign",
     "loc": "Homa Bay County, Kenya", "bullets": [
        "Supported field teams on ODK / Kobo Collect: forms on the phones, daily submissions, and sync problems fixed so household data reached the server.",
    ]},
],
"certs": ("DHIS2 Academy certificate  |  Microsoft Data Analysis  |  Google IT Support  |  CCNA"),
"compact_education": True,
"referees": [
    "Patrick Ondieki, ICT Officer, PATH  |  pondieki@path.org",
    "Marvin Ngosa, Systems Administrator, PATH  |  mngosa@path.org",
],
}

COVER_BODY = [
    "Dear Hiring Manager,",
    "",
    "Re: MEAL Assistant – Nairobi",
    "",
    "I am applying for the MEAL Assistant role at RefuSHE. For three years at PATH, an international health NGO "
    "in Kenya, I have collected, cleaned and reported programme data, much of it from community programmes for "
    "girls, young women and children. I would like to help RefuSHE keep its data accurate and on time, so you "
    "can show donors what your programmes achieve and keep improving them.",
    "",
    "Data collection is familiar ground. I worked the 2023 Indoor Residual Spraying campaign in Homa Bay County "
    "supporting field teams on ODK and Kobo Collect, and I ran the paper and Kobo tools for PATH's Early "
    "Childhood Development programme until it closed in 2025. I set up and test forms, get phones ready and "
    "synced, and have trained more than 80 staff on data tools, with short job aids so the training holds.",
    "",
    "I care about clean data. I built checks that flag missing, inconsistent and duplicate entries, and I take "
    "the errors back to the staff who collected them; that work cut our reporting time by about 40%. I turn the "
    "results into Excel and Power BI tables and charts that programme teams read every week. For RefuSHE I would "
    "build gender, age, nationality, disability and location into each form, so the breakdowns are ready when "
    "reports are due.",
    "",
    "At PATH I was the field ICT support for DREAMS, an HIV prevention programme for adolescent girls and young "
    "women, and OVC, which supports orphans and vulnerable children and their families. I handle personal data "
    "as a safety matter: consent first, secure storage, and any safeguarding concern passed to the right person "
    "straight away. I speak English and Kiswahili, work respectfully with communities, and am happy to travel "
    "to field sites.",
    "",
    "I hold a BSc in Applied Computing from KCA University, a DHIS2 Academy certificate and Microsoft Data "
    "Analysis. My referees, including my current employer PATH, are on my CV.",
    "",
    "Thank you for considering my application.",
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
