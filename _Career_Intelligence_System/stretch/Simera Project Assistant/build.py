#!/usr/bin/env python3
"""Project Assistant — Simera (remote). Stretch pack.
Intern omitted. PATH titles canonical. ECD / Nuru ya Mtoto is the lead.
Run: python3 "stretch/Simera Project Assistant/build.py"
"""
import os, sys
from docx import Document
from docx.shared import Pt

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

cv = {
"headline": "Project Assistant  |  ECD programme support, documentation and trackers  |  Remote",
"metrics": [
    ("ECD", "Nuru ya Mtoto"),
    ("120+", "people supported"),
    ("~40%", "faster reporting"),
    ("Remote", "Teams / M365"),
],
"show_referees": False,
"compact_education": True,
"summary": ("Project assistant supporting PATH work on two concurrent lines: ECD / nurturing care "
    "(Nuru ya Mtoto) and Health Informatics / HMIS. On ECD: trackers, data collection, meeting packs, "
    "follow-up and Zambia learning touchpoints. On HMIS: KenyaEMR/DHIS2, reporting cycles and documentation "
    "for 120+ people. Microsoft 365, Google Workspace, Teams, Excel (including VBA), Freshdesk and Jira "
    "Service Management. English, remote, used to several deadlines at once."),
"skills": [
    ("Project support", "Schedules, milestones, task tracking, follow-up, meeting agendas and notes, escalate delays"),
    ("ECD / programmes", "Nuru ya Mtoto nurturing-care implementation, data collection, decision forums, Zambia touchpoints"),
    ("Documentation", "SOPs, job aids, project files, reports, presentations, SharePoint / Drive records"),
    ("Trackers and data", "Excel (pivots, VBA), Google Workspace, Power BI, databases, status spreadsheets"),
    ("Tools", "Microsoft 365, Teams, Freshdesk, Zoho Desk, Jira Service Management, independent remote work"),
],
"experience": [
    {"org":"PATH","title":"ECD / Nurturing Care, Nuru ya Mtoto","dates":"Mar 2025 to Present","loc":"Concurrent with HMIS Officer · Hybrid / Remote","bullets":[
        "Support PATH nurturing-care and ECD implementation: collect and organise field and routine data, keep the tracker current, and turn it into packs for decision-making forums.",
        "Follow up across programme and field teams, including Zambia ECD learning touchpoints. Flag delays in writing and escalate to the lead.",
        "Keep the project file usable: notes, status, SOPs and job aids so the next meeting does not start from zero.",
    ]},
    {"org":"PATH","title":"Health Informatics / HMIS Officer","dates":"Mar 2025 to Present","loc":"Kisumu/Nyamira, Kenya (Hybrid / Remote)","bullets":[
        "Support KenyaEMR/TaifaCare and DHIS2 across facilities, keeping critical HIS services above 98% uptime.",
        "Lead HIS data collection, cleaning and analysis for care and treatment, PMTCT and E-TEC indicators in Excel (including VBA). Reporting effort down about 40%.",
        "Produce HIS documentation and dashboards (Power BI / Grafana) and keep reporting cycles on the calendar.",
    ]},
    {"org":"PATH","title":"ICT Associate","dates":"Jan 2024 to Mar 2025","loc":"Kisumu, Kenya","bullets":[
        "Administrative and operational support for 120+ users: Freshdesk/Zoho Desk, SLA deadlines, follow-up, escalate. Ticket response improved about 25%.",
        "Scheduled onboarding, vendor callbacks and Teams updates. Kept project files and knowledge-base articles current.",
        "Trained 80+ staff so the same process was followed at every site.",
    ]},
    {"org":"Independent","title":"Projects & Consulting (project-based)","dates":"2023 to Present","loc":"Remote","bullets":[
        "Remote project support for small businesses: Google Workspace / Microsoft 365 setup, documentation and follow-up.",
        "Tracked delivery of websites, payment flows and the County Health Systems Operations Platform, then left the runbook.",
    ]},
],
"certs": "AZ-900  |  Google IT Support  |  IBM Technical Support  |  GitHub Professional  |  Microsoft Data Analysis",
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "I am applying for the Project Assistant role. At PATH I hold two concurrent streams. On ECD / Nuru ya Mtoto I support nurturing-care implementation: trackers, data collection, meeting packs, follow-up across teams, and Zambia learning touchpoints. Separately, as Health Informatics / HMIS Officer I keep KenyaEMR/DHIS2 and reporting cycles running, with documentation and Excel workflows that cut reporting effort about 40%.",
    "I also support day-to-day operations for 120+ people: schedules, documentation, Teams, Microsoft 365, Google Workspace, and a live task board (Freshdesk / Jira Service Management). I will live in your project tool from week one.",
    "I am based in Kenya, fully remote, and I work in English every day.",
    "Thank you.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]

def build_cover_letter(path):
    doc = Document()
    br.set_base_style(doc)
    br.add_name(doc, "MESHACK ARIRI")
    br.add_title(doc, "Project Assistant")
    br.add_contact(doc, br.CONTACT)
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
    br.build(cv, files["cv_docx"])
    build_cover_letter(files["cover_docx"])
    cover_title = cv["headline"].split("|")[0].strip()
    pb.build_cv_pdf(cv, files["cv_pdf"], br.CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], br.CONTACT, cover_title)
    print("Generated:", HERE)
