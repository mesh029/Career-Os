#!/usr/bin/env python3
"""Personalized Internet Assessor, English (Kenya), TELUS Digital AI Community.
Freelance, remote, 2-5 h/week, ~USD 5/hour per task. Portal application + exam + ID check.
CV upload is usually optional; no cover letter needed, so this pack builds the CV only.
No rater experience: do not claim prior search-rating or AI data work.
Run: python3 "applications/TELUS Digital Personalized Internet Assessor/build.py"
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT = br.CONTACT

cv = {
"headline": "Information Quality and Research Specialist  |  Guideline-based review  ·  Data Validation  ·  Kenyan Locale",
"metrics": [
    ("3+ yrs", "data quality review"),
    ("~40%", "faster reporting"),
    ("Daily", "online research"),
    ("EN · SW · Luo", "languages"),
],
"summary": ("Detail-focused information and data quality professional with 3+ years at PATH, an international "
    "health organisation, reviewing records and information against detailed national guidelines. I judge "
    "accuracy, completeness and trustworthiness, flag what does not meet the standard, and keep quality "
    "consistent across repetitive, high-volume work. Lifelong Kenya resident who follows Kenyan news, "
    "business, sport, media and culture daily. Fluent English writer; heavy daily user of Google Search, "
    "Gmail, Google Workspace and social media on desktop and mobile."),
"skills": [
    ("Review and rating", "Guideline-based quality review, accuracy and completeness checks, consistency across high volumes, clear written justification"),
    ("Research", "Daily web research and source checking, separating official sources from copies and low-trust pages, health and government information"),
    ("Tools", "Google Search, Gmail, Google Workspace, Microsoft 365, Excel, DHIS2, KenyaEMR, Android and Windows, Chrome"),
    ("Locale and language", "Kenyan current affairs, business, sport, media and social media culture; English (fluent), Swahili, Dholuo"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kenya (hybrid)", "bullets": [
        "Review health records and programme data against national reporting guidelines in DHIS2, KenyaEMR and Excel, rating each batch for completeness and accuracy before it is submitted.",
        "Built validation checks that flag missing, duplicate and inconsistent records; corrections go back to the right team, cutting reporting time by about 40%.",
        "Work under strict privacy and data-handling rules for confidential health information, with work regularly checked through data quality audits.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya", "bullets": [
        "Handled about 20 support requests a week by phone, email and ticket, researching each issue and writing clear step-by-step guides for routine problems.",
        "Supported staff across Google Workspace, Microsoft 365 and mobile devices, keeping ticket records accurate for service-level reporting.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Homa Bay, Kenya", "bullets": [
        "Logged and tracked support requests, updated inventory records and contributed to process documentation and internal audits.",
    ]},
],
"certs": ("Google IT Support  |  Microsoft Data Analysis  |  DHIS2 Academy certificate  |  "
          "IBM Technical Support  |  Microsoft Azure Fundamentals (AZ-900)"),
"compact_education": True,
"show_referees": False,
}


if __name__ == "__main__":
    files = br.pack_files(HERE)
    br.build(cv, files["cv_docx"])
    pb.build_cv_pdf(cv, files["cv_pdf"], CONTACT)
    print("Generated:", HERE)
