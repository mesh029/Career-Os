#!/usr/bin/env python3
"""Project Coordinator — Simera (remote).
Intern omitted. PATH titles canonical. Independent = freelance + flagship platform.
Run: python3 "stretch/Simera Project Coordinator/build.py"
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
"headline": "Project Coordinator  |  Multi-site operations, documentation and stakeholder delivery  |  Remote",
"metrics": [
    ("120+", "people coordinated"),
    ("~98%", "on-time systems"),
    ("80+", "staff enabled"),
    ("Remote", "Teams / M365"),
],
"show_referees": False,
"compact_education": True,
"summary": ("Project coordinator with around three years running multi-site work at PATH: timelines, "
    "task follow-up, stakeholder updates, and documentation for 120+ people at roughly 98% uptime. "
    "Keeps deliverables visible, flags delays early, and writes the record so the next person can pick it up. "
    "Comfortable with Microsoft 365, Google Workspace, Teams, Excel, and ticket/status tools (Freshdesk, "
    "Jira Service Management). Also delivers independent projects remotely for small businesses and ships "
    "a four-county operations platform. English, remote-ready, used to changing priorities."),
"skills": [
    ("Coordination", "Timelines, milestones, task follow-up, meeting cadence, status updates, risk flag and escalate"),
    ("Stakeholders", "Internal teams, field sites, vendors, remote English; Zambia programme touchpoints"),
    ("Documentation", "SOPs, job aids, knowledge base, status notes, reports, SharePoint / Drive records"),
    ("Tools", "Microsoft 365, Google Workspace, Teams, Excel (incl. VBA), Power BI, Freshdesk, Zoho Desk, Jira Service Management"),
    ("Delivery", "Independent remote work, multiple deadlines, process improvement, onboarding logistics"),
],
"experience": [
    {"org":"PATH","title":"Health Informatics / HMIS Officer","dates":"Mar 2025 to Present","loc":"Kisumu/Nyamira, Kenya (Hybrid / Remote)","bullets":[
        "Coordinate HIS and reporting work across facilities: collection cycles, deadlines, and status for programme and leadership, keeping critical systems above 98% uptime.",
        "Run the paper trail: SOPs, job aids, operational reports, and dashboards (Power BI / Grafana) so stakeholders see progress without chasing.",
        "Work across clinical, ICT and monitoring teams. Flag data-flow or access risks and escalate with a clean note.",
        "Follow up until the task is done: training sessions, system changes, and monthly HIS reporting that cut processing time about 40%.",
    ]},
    {"org":"PATH","title":"ECD / Nurturing Care, Nuru ya Mtoto","dates":"Mar 2025 to Present","loc":"Concurrent with HMIS Officer · Hybrid / Remote","bullets":[
        "Support ECD / nurturing-care implementation: trackers, data collection, meeting packs, and follow-up, including Zambia learning touchpoints.",
    ]},
    {"org":"PATH","title":"ICT Associate","dates":"Jan 2024 to Mar 2025","loc":"Kisumu, Kenya","bullets":[
        "Coordinated day-to-day operations for 120+ users: assigned work in Freshdesk/Zoho Desk, tracked SLA, followed up, escalated. Ticket response improved about 25%.",
        "Scheduled onboarding and offboarding, vendor/ISP follow-ups, and Teams updates so joiners, leavers, and blockers did not sit in someone’s inbox.",
        "Kept project records current: knowledge-base articles, asset notes, and meeting follow-ups. Trained 80+ staff so the process carried the work.",
    ]},
    {"org":"Independent","title":"Projects & Consulting (project-based)","dates":"2023 to Present","loc":"Remote","bullets":[
        "Coordinate remote delivery for small businesses: Google Workspace / Microsoft 365 setup, onboarding, documentation, and follow-up until the client can run it without you.",
        "Scoped, tracked, and shipped the County Health Systems Operations Platform (Next.js, 40+ APIs) across four counties, with how-to docs included.",
    ]},
],
"certs": "AZ-900  |  Google IT Support  |  IBM Technical Support  |  GitHub Professional  |  Microsoft Data Analysis",
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "I am applying for the Project Coordinator role. For about three years at PATH I have been the person who keeps multi-site work moving: timelines, follow-up, documentation, and a clear status for people who are not in the same room. 120+ users. About 98% uptime. Ticket response about 25% faster because the queue and the write-up were tight.",
    "That is this job. I coordinate tasks across teams, I keep the record, I chase the deadline, and I escalate a risk before it becomes a surprise. I work in Microsoft 365, Google Workspace, Teams, Excel, and status tools (Freshdesk, Jira Service Management). I will live in your project platform from week one.",
    "On the side I run remote projects for small businesses and I shipped a four-county operations platform with documentation attached. I am based in Kenya, fully remote, and I work in English every day.",
    "Thank you.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]

def build_cover_letter(path):
    doc = Document()
    br.set_base_style(doc)
    br.add_name(doc, "MESHACK ARIRI")
    br.add_title(doc, "Project Coordinator")
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
