#!/usr/bin/env python3
"""AFOSI Field Project Officer — Technology & Digital Integration CV + Cover."""
import os, shutil, sys
from docx import Document
from docx.shared import Pt

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT = (
    "Kisumu / Nairobi, Kenya (open to Kilifi)  |  +254 741 174 779  |  aririmeshack@gmail.com  |  "
    "linkedin.com/in/meshack-ariri  |  meshreallycodes.online"
)

cv = {
"headline": (
    "Field Project Officer Candidate  |  Digital Integration · Digital Skills · "
    "Donor-Funded Delivery  |  Applied Computing"
),
"summary": (
    "Applied Computing graduate with ~3 years at PATH delivering technology-enabled work on "
    "donor-funded multi-site health programs. Combines digital systems implementation and support "
    "(EMR/DHIS2, project databases, Microsoft 365), digital skills training for 80+ staff, product "
    "ownership of a county health operations platform, and monitoring/reporting through SQL, Excel, "
    "and Power BI/Grafana dashboards. Strong at turning field needs into usable digital workflows, "
    "SOPs, and results tracking. Seeking to lead technology and digital integration delivery with AFOSI in Kilifi."
),
"skills": [
    ("Digital project delivery", "Technology-enabled program activities, digital tool rollout, SOP design, multi-site coordination, donor-funded delivery discipline"),
    ("Digital skills & enablement", "Curriculum-style job aids, 15+ training sessions, 80+ staff trained, e-learning friendly documentation, non-technical facilitation"),
    ("Product & systems", "Requirements-to-delivery ownership of reporting/ops platform; KenyaEMR/DHIS2 support; PRISM project database workflows; Microsoft 365"),
    ("Data, M&E & reporting", "SQL validation, DQA, Excel analytics, Power BI/Grafana dashboards, indicator tracking, timely progress reporting"),
    ("Innovation & tech stack", "Full-stack web (Next.js/TypeScript), cloud DB, AI coursework, automation; rapid prototyping via national hackathons"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 – Present", "loc": "Kisumu/Nyamira, Kenya (Hybrid)", "bullets": [
        "Lead day-to-day digital systems support for KenyaEMR/DHIS2 and related reporting tools across facilities — uptime, data quality, and user adoption.",
        "Design and deliver digital skills sessions for facility and program teams (part of 80+ staff trained); write SOPs and job aids that stick in the field.",
        "Own monitoring and reporting workflows: SQL/Excel validation, dashboards (Power BI/Grafana), and timely indicator packages for program review.",
        "Coordinate with multidisciplinary teams on digital tools for nurturing care / ECD data support; translate field feedback into system improvements.",
        "Drive innovation through automation that cut reporting/processing effort ~40% while protecting data integrity.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 – Mar 2025", "loc": "Kisumu, Kenya", "bullets": [
        "Delivered technology-enabled operations for 120+ users across multi-site programs — Microsoft 365, identity, networking, and ITIL-style service workflows (~98% uptime).",
        "Ran digital onboarding/offboarding and user training; built knowledge-base content so teams could adopt tools without constant escalation.",
        "Supported surveillance data accuracy with SQL checks and structured ticket discipline (~25% faster response).",
        "Acted as primary digital contact for non-technical users — clear communication, field-friendly troubleshooting, documented fixes.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 – Dec 2023", "loc": "Homa Bay, Kenya", "bullets": [
        "Supported facility digitalization and ICT rollout — connectivity, devices, and day-to-day enablement for health workers.",
        "Logged incidents, contributed to process documentation, and assisted deployments under program timelines.",
    ]},
],
"certs": (
    "CCNA  |  Microsoft Azure Fundamentals (AZ-900)  |  Google IT Support Professional  |  "
    "IBM Technical Support  |  GitHub Professional  |  Microsoft Data Analysis  |  "
    "Cyberise Hackathon (CA Kenya)  |  NRF Cybersecurity Hackathon"
),
"achievements": [
    "Product-owned County Health Systems Operations Platform (NDWH & CBS) — facility reporting, EMR overview, assets, and tickets across four counties.",
    "Trained 80+ staff on digital tools, data quality, and secure use across 15+ sessions.",
    "Sustained ~98% uptime for digital services supporting 120+ users on donor-funded programs.",
    "National innovation/hackathon participant (Cyberise / CA Kenya; NRF) — rapid digital problem-solving under time pressure.",
],
"languages": "English (excellent)  |  Kiswahili (fluent)",
"referees": [
    "Patrick Ondieki — ICT Officer, PATH  |  pondieki@path.org",
    "Marvin Ngosa — Systems Administrator, PATH  |  mngosa@path.org",
    "Gadaffi Ochieng — Procurement Officer, Ampath  |  ochienggadaffi@gmail.com",
],
}

COVER_BODY = open(os.path.join(HERE, "Meshack Ariri Cover Letter.txt"), encoding="utf-8").read().splitlines()

def build_cover_docx(path):
    doc = Document()
    br.set_base_style(doc)
    br.add_header(doc, "MESHACK ARIRI", "Field Project Officer — AFOSI (Technology & Digital Integration)", CONTACT)
    for para in COVER_BODY:
        if para == "":
            continue
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.08
        r = p.add_run(para)
        r.font.size = Pt(10.5)
        r.font.name = br.FONT_NAME
    doc.save(path)
    print("Saved:", path)

def export_copies(*paths):
    targets = [
        os.path.join(ROOT, "downloads", "JOBS", "AFOSI Field Project Officer"),
        os.path.join("/workspace", "JOBS", "AFOSI Field Project Officer"),
        "/opt/cursor/artifacts/meshack-cvs/AFOSI Field Project Officer",
    ]
    for dest in targets:
        os.makedirs(dest, exist_ok=True)
        for src in paths:
            if os.path.isfile(src):
                shutil.copy2(src, dest)
                print("Copied:", os.path.join(dest, os.path.basename(src)))

if __name__ == "__main__":
    cv_docx = os.path.join(HERE, "Meshack Ariri CV.docx")
    cv_pdf = os.path.join(HERE, "Meshack Ariri CV.pdf")
    cl_docx = os.path.join(HERE, "Meshack Ariri Cover Letter.docx")
    cl_pdf = os.path.join(HERE, "Meshack Ariri Cover Letter.pdf")
    notes = os.path.join(HERE, "Application notes.txt")
    jobs_notes = "/workspace/JOBS/AFOSI Field Project Officer/Application notes.txt"
    if os.path.isfile(jobs_notes):
        shutil.copy2(jobs_notes, notes)

    original = br.CONTACT
    br.CONTACT = CONTACT
    try:
        br.build(cv, cv_docx)
        build_cover_docx(cl_docx)
        pb.build_cv_pdf(cv, cv_pdf, CONTACT)
        pb.build_cover_pdf(
            COVER_BODY, cl_pdf, CONTACT,
            "Field Project Officer — AFOSI (Technology & Digital Integration)",
        )
    finally:
        br.CONTACT = original

    extras = [
        os.path.join(HERE, "Meshack Ariri Cover Letter.txt"),
        os.path.join(HERE, "Certifications form answer.txt"),
        os.path.join(HERE, "Job_Description.md"),
        os.path.join(HERE, "Application_Intelligence.md"),
        notes,
    ]
    export_copies(cv_docx, cv_pdf, cl_docx, cl_pdf, *[e for e in extras if os.path.isfile(e)])
    print("AFOSI Field Project Officer pack generated.")
