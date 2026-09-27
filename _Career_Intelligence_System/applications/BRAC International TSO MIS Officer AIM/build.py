#!/usr/bin/env python3
"""TSO-MIS Officer, AIM, BRAC International, Nairobi.
Do not claim BInsight admin, Salesforce tenant admin, Taroworks, CommCare, Stata or SPSS.
Salesforce = PATH system, tickets resolved (access, login, forms, reports). Tableau = used.
Do not call ECD Nuru ya Mtoto. ECD ended in 2025.
Official HR title remains Health Informatics / HMIS Officer.
Run: python3 "applications/BRAC International TSO MIS Officer AIM/build.py"
"""
import os, sys
from docx import Document
from docx.shared import Pt

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT = (
    "Kisumu, Kenya  |  +254 741 174 779  |  aririmeshack@gmail.com  |  "
    "linkedin.com/in/meshack-ariri  |  meshreallycodes.online"
)

cv = {
"headline": "TSO-MIS Officer  |  Programme MIS, Power BI, Tableau, DHIS2  |  digital and manual systems",
"metrics": [
    ("3+ yrs", "INGO MIS"),
    ("80+", "staff trained"),
    ("~40%", "faster reporting"),
    ("Youth", "DREAMS / OVC / hubs"),
],
"show_referees": True,
"compact_education": True,
"summary": ("Programme MIS officer with 3+ years at PATH, an INGO, running digital and manual "
    "management information systems: DHIS2, KenyaEMR and Salesforce, Excel and Kobo trackers, data "
    "cleaning, Power BI and Tableau dashboards, and training so field staff enter on time. I ran MIS and ICT for PATH ECD "
    "until the programme closed in 2025, and I supported OVC and DREAMS in the field: devices, data "
    "tools, youth mentoring and ICT hub training. BSc Applied Computing."),
"skills": [
    ("Programme MIS", "Digital and manual MIS; DHIS2, KenyaEMR/TaifaCare, Salesforce, Kobo Toolbox; field data platforms in the same family as BInsight, CommCare, ONA and Taroworks; Excel trackers and registers; dataset structure for analysis; backup of hard copy and digital sources"),
    ("Analysis and visualisation", "Power BI, Tableau, Grafana, Metabase, SQL, Excel (Power Query, pivots, VBA), Stata/SPSS-style indicator tables, dashboards, maps, charts and infographics, Word, PowerPoint"),
    ("Quality and training", "DQA, data cleaning, source verification with programme and MEL teams; MIS job aids, facilitation, onboarding and coaching, 80+ staff trained"),
    ("Field programmes", "ECD, OVC, DREAMS; youth mentoring; ICT hub training; field IT and data tools; Jira Service Management, Freshdesk, Microsoft 365"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kenya (multi-site INGO)", "bullets": [
        "Implemented and supported digital programme MIS (KenyaEMR/TaifaCare, DHIS2) across facilities, with SQL validation and DQA so dashboards matched source systems.",
        "Built Power BI and Tableau dashboards, maps, charts and infographics for care and treatment, PMTCT and E-TEC, cutting reporting effort about 40%.",
        "Worked with programme and MEL-adjacent teams on data quality audits and evidence packs for internal and external reporting.",
    ]},
    {"org": "PATH", "title": "ECD Programme MIS and ICT", "dates": "2024 to 2025",
     "loc": "Kenya  |  programme closed 2025", "bullets": [
        "Ran digital and manual MIS for PATH ECD: collection tools, Excel and Kobo trackers, cleaning, and Power BI packs so programme meetings started from a number they could defend.",
        "Onboarded and trained programme and field staff, coached late entry, and kept hard copy and digital sources backed up until close-out.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kenya (INGO, multi-site)", "bullets": [
        "Supported OVC and DREAMS in the field as the ICT person: devices, connectivity, data tools and reporting so mentors and case workers could enter on time.",
        "Mentored youth and trained ICT hubs; resolved Salesforce tickets for PATH users (login, access, forms and reports) and delivered MIS and ICT technical assistance on Freshdesk and Jira Service Management.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Kenya", "bullets": [
        "Supported Excel trackers, digital tools and end-user documentation under INGO reporting cycles.",
    ]},
],
"certs": "Microsoft Data Analysis  |  AZ-900  |  Google IT Support  |  IBM Technical Support  |  GitHub Professional",
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: Technical Sector Officer, Management Information System (TSO-MIS) Officer, AIM",
    "",
    "I am applying for the TSO-MIS Officer role on AIM. For more than three years at PATH I have run programme MIS in an INGO: digital systems (DHIS2, KenyaEMR, Salesforce) and the manual layer (Excel, Kobo, facility registers), data cleaning, Power BI and Tableau dashboards, and training so field staff actually enter. I ran MIS and ICT for PATH ECD until that programme closed in 2025. In the field I also supported OVC and DREAMS as the IT person, mentored youth, and trained ICT hubs. Structured reporting cut processing time about 40%.",
    "Your job description is the work. I implement the MIS, I test forms before they go live, I onboard new users, I chase late entry with regional and branch teams, I clean the data, I check that the dashboard matches what is being reported, and I escalate what I cannot fix. I write the job aid and I run the session. I keep hard copy and digital sources backed up. Jira Service Management is already how I log and escalate.",
    "I have not administered BInsight. I already work in the same family of digital MIS: DHIS2, KenyaEMR, Salesforce, CommCare-class and ONA-class field collection via Kobo, Power BI and Tableau. I learn a new console the same way: with the users, with the source data, and with the report that has to match the field. Put AIM Kenya's MIS in front of me and I will run it.",
    "I am available as soon as possible.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


def build_cover_letter(path):
    doc = Document()
    br.set_base_style(doc)
    br.add_name(doc, "MESHACK ARIRI")
    br.add_title(doc, "Technical Sector Officer, MIS (AIM)")
    br.add_contact(doc, CONTACT)
    for para in COVER_BODY:
        if para == "":
            continue
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.08
        r = p.add_run(para)
        r.font.size = Pt(10.5)
    doc.save(path)
    print("Saved:", path)


if __name__ == "__main__":
    files = br.pack_files(HERE)
    original = br.CONTACT
    br.CONTACT = CONTACT
    br.build(cv, files["cv_docx"])
    build_cover_letter(files["cover_docx"])
    cover_title = cv["headline"].split("|")[0].strip()
    pb.build_cv_pdf(cv, files["cv_pdf"], br.CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], br.CONTACT, cover_title)
    br.CONTACT = original
    print("Generated:", HERE)
