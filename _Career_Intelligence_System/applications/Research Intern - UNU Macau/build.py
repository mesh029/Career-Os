#!/usr/bin/env python3
"""UNU Macau Research Intern — CV, cover letter, research sample (DOCX + PDF).
Facts per resumes/00_Master_Resume.md. Run: python3 build.py
"""
import os
import shutil
import sys

from docx import Document
from docx.shared import Pt, Inches
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.colors import HexColor

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb
from resume_theme import ACCENT_DARK, SLATE, SLATE_MUTED

CONTACT = (
    "Kisumu / Nairobi, Kenya  |  +254 741 174 779  |  aririmeshack@gmail.com  |  "
    "linkedin.com/in/meshack-ariri  |  meshreallycodes.online"
)

cv = {
    "headline": (
        "Research Intern Candidate  |  AI · Adult Learning · Digital Education Practice  |  "
        "Applied Computing"
    ),
    "summary": (
        "Applied Computing graduate (BSc, KCA University, 2023) with Artificial Intelligence "
        "coursework and ~3 years at PATH supporting digital systems adoption across multi-site "
        "health programs. Strong English writing, structured analysis, and adult learning practice: "
        "trained 80+ staff on EMR/DHIS2 and data quality; authored SOPs and job aids; supported "
        "data tools for nurturing care / early childhood development work. Uses AI tools daily for "
        "documentation and knowledge drafting. Seeking a supervised remote research internship to "
        "contribute literature reviews and clear drafts on AI and higher education."
    ),
    "skills": [
        (
            "Research & writing",
            "English research briefs, literature synthesis (developing), technical documentation, "
            "SOPs/job aids, structured analysis of operational data",
        ),
        (
            "AI & learning interest",
            "Artificial Intelligence coursework; AI-assisted documentation and troubleshooting; "
            "adult digital-skills training design; interest in AI tutors and cognitive load",
        ),
        (
            "Digital education practice",
            "15+ training sessions; 80+ staff trained; role-based coaching; knowledge-base articles; "
            "remote/hybrid enablement",
        ),
        (
            "Data & systems analysis",
            "SQL validation, DQA workflows, Power BI/Grafana dashboards, EMR/DHIS2 support, "
            "reporting automation",
        ),
        (
            "Collaboration",
            "Multidisciplinary program teams, remote independent work, clear stakeholder communication",
        ),
    ],
    "experience": [
        {
            "org": "PATH",
            "title": "Health Informatics / HMIS Officer",
            "dates": "Mar 2025 – Present",
            "loc": "Kisumu/Nyamira, Kenya (Hybrid)",
            "bullets": [
                "Train facility staff, ICT officers, and program teams on EMR modules, DHIS2, data quality, and secure system use (part of 80+ staff trained overall).",
                "Author SOPs, job aids, and technical documentation that scaffold adult learning on complex digital tools.",
                "Support data tools and decision-support workflows for nurturing care / early childhood development implementation with multidisciplinary teams.",
                "Analyse care, treatment, and related indicators using SQL-assisted validation and Excel tooling; translate findings into practical recommendations.",
                "Build Power BI / Grafana dashboards that give users feedback on data quality and program trends.",
                "Use AI-assisted drafting carefully for documentation and troubleshooting notes, then verify against live systems.",
            ],
        },
        {
            "org": "PATH",
            "title": "ICT Associate",
            "dates": "Jan 2024 – Mar 2025",
            "loc": "Kisumu, Kenya",
            "bullets": [
                "Delivered structured user training and onboarding for Microsoft 365 and workplace digital tools across 120+ users.",
                "Authored knowledge-base articles that reduced repeat support questions and improved independent learning.",
                "Supported SQL validation and surveillance data accuracy improvements through clear analytical checks.",
                "Sustained ~98% uptime under ITIL-style ticketing discipline (Freshdesk/Zoho Desk).",
            ],
        },
        {
            "org": "PATH",
            "title": "ICT Intern",
            "dates": "Apr 2023 – Dec 2023",
            "loc": "Homa Bay, Kenya",
            "bullets": [
                "Assisted facility digitalization and day-to-day coaching of non-technical users on new systems.",
                "Contributed to process documentation and internal IT audits.",
            ],
        },
    ],
    "certs": (
        "CCNA  |  Microsoft Azure Fundamentals (AZ-900)  |  Google IT Support  |  "
        "IBM Technical Support  |  GitHub Professional  |  Microsoft Data Analysis"
    ),
    "achievements": [
        "Trained 80+ health workers across 15+ sessions on digital tools, data quality, and secure use.",
        "Built County Health Systems Operations Platform (NDWH & CBS) — full-stack reporting/analytics across four counties (portfolio).",
        "Coursework included Artificial Intelligence alongside cybersecurity and systems analysis (BSc Applied Computing).",
        "Hackathon participant (Cyberise / CA Kenya; NRF) — rapid research, prototyping, and clear presentation under time pressure.",
    ],
    "languages": "English (excellent written and spoken)  |  Kiswahili (fluent)",
    "referees": [
        "Patrick Ondieki — ICT Officer, PATH  |  pondieki@path.org",
        "Marvin Ngosa — Systems Administrator, PATH  |  mngosa@path.org",
        "Gadaffi Ochieng — Procurement Officer, Ampath  |  ochienggadaffi@gmail.com",
    ],
}

COVER_BODY = open(os.path.join(HERE, "Meshack Ariri Cover Letter.txt"), encoding="utf-8").read().splitlines()


def build_cv_docx(path):
    doc = Document()
    br.set_base_style(doc)
    br.add_header(doc, "MESHACK ARIRI", cv["headline"], CONTACT)

    br.add_heading(doc, "Professional Summary")
    br.add_para(doc, cv["summary"], size=10.2, space_after=4)

    br.add_heading(doc, "Core Skills")
    for label, items in cv["skills"]:
        br.add_skill_line(doc, label, items)

    br.add_heading(doc, "Professional Experience")
    for role in cv["experience"]:
        br.add_role(doc, role["org"], role["title"], role["dates"], role.get("loc", ""))
        br.add_bullets(doc, role["bullets"])

    br.add_heading(doc, "Education")
    br.add_para(
        doc,
        "BSc, Applied Computing  |  KCA University, Nairobi  |  November 2023",
        bold=True,
        size=10.2,
        space_after=1,
    )
    br.add_para(
        doc,
        "Specialized in Cybersecurity and Digital Forensics. Coursework included Artificial "
        "Intelligence, Ethical Hacking, Digital Forensics, Data Protection, Cloud Computing, "
        "and System Analysis & Design.",
        size=9.8,
        color=br.GREY,
    )
    br.add_para(
        doc,
        "Capstone: Designed and implemented a secure office network (VLANs, Active Directory, "
        "backup/DR) simulating real-world IT administration.",
        size=9.8,
        color=br.GREY,
    )
    br.add_para(
        doc,
        "Note: Bachelor’s degree completed. Not yet enrolled in a Master’s programme. Applying "
        "for supervised research experience at the AI–learning–education intersection.",
        size=9.5,
        color=br.GREY,
    )

    br.add_heading(doc, "Selected research / writing")
    br.add_para(
        doc,
        "AI-Supported Adult Learning in Digital Systems Training (2026) — original English "
        "research brief attached to this application.",
        size=9.8,
        space_after=2,
    )
    br.add_para(
        doc,
        "County Health Systems Operations Platform (NDWH & CBS) — analytical platform and "
        "documentation for facility reporting across four Kenyan counties.",
        size=9.8,
        space_after=2,
    )

    br.add_heading(doc, "Languages")
    br.add_para(doc, cv["languages"], size=10)

    br.add_heading(doc, "Certifications")
    br.add_para(doc, cv["certs"], size=10)

    br.add_heading(doc, "Achievements & Activities")
    br.add_bullets(doc, cv["achievements"])

    br.add_heading(doc, "Referees")
    for ref in cv["referees"]:
        br.add_para(doc, ref, size=10, space_after=4)

    doc.save(path)
    print("Saved:", path)


def build_cover_docx(path):
    doc = Document()
    br.set_base_style(doc)
    br.add_header(
        doc,
        "MESHACK ARIRI",
        "Research Intern — UNU Macau (AI, Learning & Higher Education)",
        CONTACT,
    )
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


def build_research_docx(path):
    text = open(os.path.join(HERE, "Meshack Ariri Research Sample.txt"), encoding="utf-8").read()
    doc = Document()
    br.set_base_style(doc)
    for section in doc.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.85)
        section.right_margin = Inches(0.85)
    for i, line in enumerate(text.splitlines()):
        p = doc.add_paragraph()
        if i == 0:
            p.paragraph_format.space_after = Pt(4)
            r = p.add_run(line)
            r.bold = True
            r.font.size = Pt(14)
        elif i in (1, 2, 3):
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(line)
            r.font.size = Pt(10)
            r.italic = True
        elif line.startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "References", "Contact")):
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(4)
            r = p.add_run(line)
            r.bold = True
            r.font.size = Pt(11)
        elif line == "":
            p.paragraph_format.space_after = Pt(4)
            continue
        else:
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(line)
            r.font.size = Pt(10.5)
        r.font.name = br.FONT_NAME
    doc.save(path)
    print("Saved:", path)


def build_research_pdf(path):
    text = open(os.path.join(HERE, "Meshack Ariri Research Sample.txt"), encoding="utf-8").read()
    styles = {
        "title": ParagraphStyle(
            "t", fontName="Helvetica-Bold", fontSize=14, textColor=HexColor(ACCENT_DARK),
            alignment=TA_CENTER, spaceAfter=6, leading=18,
        ),
        "meta": ParagraphStyle(
            "m", fontName="Helvetica-Oblique", fontSize=9.5, textColor=HexColor(SLATE_MUTED),
            alignment=TA_CENTER, spaceAfter=2, leading=12,
        ),
        "h": ParagraphStyle(
            "h", fontName="Helvetica-Bold", fontSize=11, textColor=HexColor(ACCENT_DARK),
            spaceBefore=10, spaceAfter=4, leading=14,
        ),
        "body": ParagraphStyle(
            "b", fontName="Helvetica", fontSize=10.2, textColor=HexColor(SLATE),
            alignment=TA_JUSTIFY, spaceAfter=6, leading=14,
        ),
    }
    story = []
    lines = text.splitlines()
    story.append(Paragraph(lines[0], styles["title"]))
    for line in lines[1:4]:
        if line.strip():
            story.append(Paragraph(line, styles["meta"]))
    story.append(Spacer(1, 8))
    for line in lines[4:]:
        if not line.strip():
            continue
        if line[0].isdigit() and line[1] == ".":
            story.append(Paragraph(line, styles["h"]))
        elif line.startswith("References") or line.startswith("Contact"):
            story.append(Paragraph(line, styles["h"]))
        else:
            story.append(Paragraph(line.replace("&", "&amp;"), styles["body"]))
    doc = SimpleDocTemplate(
        path, pagesize=A4,
        leftMargin=0.85 * inch, rightMargin=0.85 * inch,
        topMargin=0.7 * inch, bottomMargin=0.7 * inch,
    )
    doc.build(story)
    print("Saved:", path)


def build_cv_pdf_custom(path):
    """PDF CV with AI coursework and research section (override stock education)."""
    from reportlab.platypus import KeepTogether
    from reportlab.lib.styles import ParagraphStyle as PS
    S = pb._styles()
    story = []
    pb._header(story, S, "MESHACK ARIRI", cv["headline"], CONTACT)
    pb._heading(story, S, "Professional Summary")
    story.append(Paragraph(cv["summary"], S["summary"]))
    pb._heading(story, S, "Core Skills")
    for label, items in cv["skills"]:
        story.append(Paragraph(
            f'<font color="{pb.ACCENT}"><b>{label}:</b></font> {items}', S["skill"],
        ))
    pb._heading(story, S, "Professional Experience")
    for role in cv["experience"]:
        loc = role.get("loc", "")
        block = [
            Paragraph(f'<b>{role["title"]}</b>', S["roleL"]),
            Paragraph(
                f'{role["org"]}'
                + (f'  <font color="{pb.ACCENT_MID}">|</font>  {loc}' if loc else "")
                + f'  <font color="{pb.ACCENT_MID}">|</font>  {role["dates"]}',
                S["org"],
            ),
        ]
        for b in role["bullets"]:
            block.append(Paragraph(
                f'<font color="{pb.ACCENT}">▪</font>&nbsp;&nbsp;{b}', S["bullet"],
            ))
        story.append(KeepTogether(block))

    pb._heading(story, S, "Education")
    story.append(Paragraph(
        "BSc, Applied Computing&nbsp;&nbsp;"
        f'<font color="{pb.ACCENT_MID}">|</font>&nbsp;&nbsp;'
        "KCA University, Nairobi&nbsp;&nbsp;"
        f'<font color="{pb.ACCENT_MID}">|</font>&nbsp;&nbsp;November 2023',
        PS("edu", parent=S["small"], fontName=pb.FONT_B),
    ))
    story.append(Paragraph(
        "Specialized in Cybersecurity and Digital Forensics. Coursework included Artificial "
        "Intelligence, Ethical Hacking, Digital Forensics, Data Protection, Cloud Computing, "
        "and System Analysis &amp; Design.",
        S["smallg"],
    ))
    story.append(Paragraph(
        "Capstone: Designed and implemented a secure office network (VLANs, Active Directory, "
        "backup and disaster recovery) simulating real-world IT administration.",
        S["smallg"],
    ))
    story.append(Paragraph(
        "Note: Bachelor’s degree completed. Not yet enrolled in a Master’s programme.",
        S["smallg"],
    ))

    pb._heading(story, S, "Selected research / writing")
    story.append(Paragraph(
        "AI-Supported Adult Learning in Digital Systems Training (2026) — original English "
        "research brief attached to this application.",
        S["small"],
    ))
    story.append(Paragraph(
        "County Health Systems Operations Platform (NDWH &amp; CBS) — analytical platform and "
        "documentation for facility reporting across four Kenyan counties.",
        S["small"],
    ))

    pb._heading(story, S, "Languages")
    story.append(Paragraph(cv["languages"], S["small"]))
    pb._heading(story, S, "Certifications")
    story.append(Paragraph(cv["certs"], S["small"]))
    pb._heading(story, S, "Achievements & Activities")
    for a in cv["achievements"]:
        story.append(Paragraph(
            f'<font color="{pb.ACCENT}">▪</font>&nbsp;&nbsp;{a}', S["bullet"],
        ))
    pb._heading(story, S, "Referees")
    for ref in cv["referees"]:
        story.append(Paragraph(ref, S["small"]))
        story.append(Spacer(1, 4))

    pb._doc(path).build(story)
    print("Saved:", path)


def export_copies(*paths):
    targets = [
        os.path.join(ROOT, "downloads", "JOBS", "UNU Macau Research Intern"),
        os.path.join("/workspace", "JOBS", "UNU Macau Research Intern"),
        "/opt/cursor/artifacts/meshack-cvs/UNU Macau Research Intern",
    ]
    for dest in targets:
        os.makedirs(dest, exist_ok=True)
        for src in paths:
            if os.path.isfile(src):
                shutil.copy2(src, dest)
                print("Copied:", os.path.join(dest, os.path.basename(src)))


if __name__ == "__main__":
    # Copy plain text into application folder for reference
    for name in ("Meshack Ariri Cover Letter.txt", "Meshack Ariri Research Sample.txt"):
        src = os.path.join(HERE, name)
        # already in HERE

    cv_docx = os.path.join(HERE, "Meshack Ariri CV.docx")
    cv_pdf = os.path.join(HERE, "Meshack Ariri CV.pdf")
    cl_docx = os.path.join(HERE, "Meshack Ariri Cover Letter.docx")
    cl_pdf = os.path.join(HERE, "Meshack Ariri Cover Letter.pdf")
    rs_docx = os.path.join(HERE, "Meshack Ariri Research Sample.docx")
    rs_pdf = os.path.join(HERE, "Meshack Ariri Research Sample.pdf")
    notes = os.path.join(HERE, "Application notes.txt")

    # human notes also live in JOBS
    jobs_notes = "/workspace/JOBS/UNU Macau Research Intern/Application notes.txt"
    if os.path.isfile(jobs_notes):
        shutil.copy2(jobs_notes, notes)

    original = br.CONTACT
    br.CONTACT = CONTACT
    try:
        build_cv_docx(cv_docx)
        build_cover_docx(cl_docx)
        build_research_docx(rs_docx)
        build_cv_pdf_custom(cv_pdf)
        pb.build_cover_pdf(
            COVER_BODY,
            cl_pdf,
            CONTACT,
            "Research Intern — UNU Macau (AI, Learning & Higher Education)",
        )
        build_research_pdf(rs_pdf)
    finally:
        br.CONTACT = original

    files = [cv_docx, cv_pdf, cl_docx, cl_pdf, rs_docx, rs_pdf, notes]
    # also copy txt sources
    files += [
        os.path.join(HERE, "Meshack Ariri Cover Letter.txt"),
        os.path.join(HERE, "Meshack Ariri Research Sample.txt"),
        os.path.join(HERE, "Job_Description.md"),
        os.path.join(HERE, "Application_Intelligence.md"),
    ]
    export_copies(*[f for f in files if os.path.isfile(f)])
    print("UNU Macau Research Intern application docs generated.")
