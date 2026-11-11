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
    "Applied Computing graduate with ~3 years at PATH on donor-funded, technology-enabled health "
    "programs. Product owner of a multi-county digital ops platform (NDWH/CBS reporting, EMR, assets, "
    "tickets); delivers digital skills training to 80+ staff; coordinates matrix/field teams as primary "
    "digital contact for 120+ users; and owns monitoring/reporting through SQL, Excel, DHIS2/PRISM "
    "workflows and Power BI/Grafana. Strong at work planning for digital rollouts, stakeholder "
    "coordination, and results tracking. Open to Kilifi field delivery with AFOSI."
),
"skills": [
    ("Digital project delivery", "Work planning for digital rollouts, multi-site coordination, SOP/job-aid design, donor-funded delivery discipline, stakeholder updates"),
    ("Team leadership (matrix/field)", "Primary digital contact for 120+ users; coach facility ICT/program users; run 15+ training sessions; assign owners and escalate blockers"),
    ("Product ownership", "County Health Ops Platform (Next.js/TypeScript/MySQL); KenyaEMR/DHIS2; PRISM project DB alongside DHIS2; Microsoft 365"),
    ("M&E, reporting & data", "SQL/DQA, Excel analytics, Power BI/Grafana, indicator packages, uptime/progress reporting for program review"),
    ("Innovation", "Automation (~40% reporting effort cut); AI coursework; hackathons (Cyberise/CA Kenya, NRF); Scrum Product Owner certification in progress"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 – Present", "loc": "Kisumu/Nyamira, Kenya (Hybrid)", "bullets": [
        "Product-own and advance digital tools for donor-funded delivery: KenyaEMR/DHIS2 support, PRISM project-database workflows alongside DHIS2, and SQL/Excel validation.",
        "Lead matrix coordination with facility ICT officers and program teams — set owners for data/system issues, coach users, and close loops before reporting deadlines.",
        "Plan and deliver digital skills training (part of 80+ staff / 15+ sessions); publish SOPs and job aids that drive adoption in the field.",
        "Own M&E inputs: Power BI/Grafana dashboards, indicator packages, and progress/uptime reporting for program and leadership review.",
        "Built County Health Systems Operations Platform (NDWH & CBS) — Next.js/TypeScript/MySQL — for facility reporting, EMR overview, assets and tickets across four counties.",
        "Cut reporting/processing effort ~40% through automation while protecting data integrity on donor reporting cycles.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 – Mar 2025", "loc": "Kisumu, Kenya", "bullets": [
        "Primary digital contact for 120+ users on donor-funded multi-site programs — Microsoft 365, identity, networking, ITIL ticketing; ~98% uptime.",
        "Led work planning for digital onboarding/offboarding and user enablement; knowledge-base content reduced repeat failures.",
        "Coordinated with ICT colleagues and field users to hit SLA targets (~25% faster ticket response) and keep stakeholders updated.",
        "Supported surveillance data quality with SQL checks tied to program monitoring needs.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 – Dec 2023", "loc": "Homa Bay, Kenya", "bullets": [
        "Supported facility digitalization rollout — connectivity, devices, documentation — under program timelines with county-facing teams.",
        "Assisted deployments and day-to-day enablement for health workers adopting new digital tools.",
    ]},
],
"certs": (
    "CCNA  |  Azure Fundamentals (AZ-900)  |  Google IT Support  |  IBM Technical Support  |  "
    "GitHub Professional  |  Microsoft Data Analysis  |  Cyberise / NRF Hackathons  |  "
    "Scrum Product Owner certification — in progress"
),
"achievements": [
    "Product-owned multi-county digital ops platform (NDWH & CBS) with measurable reporting/visibility gains for program teams.",
    "Led digital skills delivery for 80+ staff; primary digital contact coordinating 120+ users to ~98% uptime.",
    "Donor-program M&E support: DQA, dashboards, and timely indicator/uptime inputs for review cycles.",
    "National hackathons (Cyberise / CA Kenya; NRF) — rapid digital problem-solving under time pressure.",
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
        os.path.join(HERE, "Form answers.txt"),
        os.path.join(HERE, "Job_Description.md"),
        os.path.join(HERE, "Application_Intelligence.md"),
        notes,
    ]
    export_copies(cv_docx, cv_pdf, cl_docx, cl_pdf, *[e for e in extras if os.path.isfile(e)])
    print("AFOSI Field Project Officer pack generated.")
