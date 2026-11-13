#!/usr/bin/env python3
"""Build Meshack Ariri Career Dossier PDF in the shared CV visual theme.

Output:
  JOBS/Career Dossier/Meshack Ariri Career Dossier.pdf
  _Career_Intelligence_System/downloads/JOBS/Career Dossier/ (mirror)
"""
from __future__ import annotations

import os
import shutil
import sys

from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, Spacer, Table, TableStyle

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from pdf_builder import (  # noqa: E402
    ACCENT,
    COPPER,
    FONT_B,
    NAVY,
    PAGE_W,
    T_LT,
    T_MID,
    _doc,
    _header,
    _heading,
    _rule,
    _styles,
    _toolkit,
)
from resume_theme import CONTACT  # noqa: E402

OUT_NAME = "Meshack Ariri Career Dossier.pdf"
JOBS_DIR = os.path.join("/workspace", "JOBS", "Career Dossier")
MIRROR_DIR = os.path.join(
    "/workspace",
    "_Career_Intelligence_System",
    "downloads",
    "JOBS",
    "Career Dossier",
)


def _subhead(story, S, text):
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        f'<font name="{FONT_B}" color="{ACCENT}">{text}</font>',
        S["org"],
    ))


def _bullets(story, S, items):
    for item in items:
        story.append(Paragraph(
            f'<font color="{ACCENT}">▸</font>&nbsp;&nbsp;{item}',
            S["bullet"],
        ))


def _role_row(S, title, dates):
    row = Table(
        [[Paragraph(title, S["roleL"]), Paragraph(dates, S["roleR"])]],
        colWidths=[4.95 * inch, 2.25 * inch],
    )
    row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ("LEFTPADDING", (0, 0), (-1, -1), 1),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return row


def _kv_table(S, rows):
    """Two-column label/value table on a sand wash."""
    data = []
    for label, value in rows:
        data.append([
            Paragraph(
                f'<font name="{FONT_B}" color="{ACCENT}">{label}</font>',
                S["small"],
            ),
            Paragraph(value, S["small"]),
        ])
    t = Table(data, colWidths=[1.55 * inch, PAGE_W - 1.55 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), T_LT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LINEBELOW", (0, 0), (-1, -2), 0.35, T_MID),
    ]))
    return t


def build_story():
    S = _styles()
    story = []

    _header(
        story,
        S,
        "MESHACK ARIRI",
        "Career Dossier  ·  Experiences, certifications, capabilities & CV design",
        CONTACT,
        metrics=[
            ("120+", "users supported"),
            ("~98%", "uptime held"),
            ("80+", "staff trained"),
            ("50+", "facilities on site"),
        ],
    )

    _heading(story, S, "Profile")
    story.append(Paragraph(
        "Health Informatics and IT professional with ~3 years at PATH supporting "
        "national-scale health information systems — KenyaEMR/TaifaCare, DHIS2, and "
        "EMR–laboratory–pharmacy integrations. Combines hands-on EMR/HMIS support with "
        "data quality (DQA, SQL validation), analytics (Power BI, Grafana), and reliable "
        "IT operations (Microsoft 365, Active Directory, networking, ITIL/SLA) for 120+ "
        "users across multiple sites. Center of gravity: keep the digital systems that "
        "run Kenyan healthcare working, and help the people who use them succeed.",
        S["summary"],
    ))

    _toolkit(story, S, [
        ("Health systems", "KenyaEMR / TaifaCare, OpenMRS, DHIS2, NDWH, PRISM (PATH project DB), Kobo"),
        ("Data & MIS", "DQA, SQL, Power BI, Tableau, Grafana, Metabase, Excel (Power Query / VBA), digital + manual MIS"),
        ("IT operations", "M365, AD / Entra ID, Meraki, Freshdesk / Zoho / Jira, Windows / Linux servers, backups / DR"),
        ("Delivery", "Facility rollout, SOPs / job aids, training, vendor / ISP coordination, Asana / MS Project / Monday.com"),
        ("Build", "Next.js, TypeScript, Prisma, MySQL, REST APIs, Recharts / Mapbox"),
    ])

    # —— Identity ——
    _heading(story, S, "Identity snapshot")
    story.append(_kv_table(S, [
        ("Phone", "+254 741 174 779"),
        ("Email", "aririmeshack@gmail.com"),
        ("Location", "Kisumu, Kenya (open to relocate / remote)"),
        ("Languages", "English, Swahili, Dholuo"),
        ("LinkedIn", "linkedin.com/in/meshack-ariri"),
        ("Portfolio", "meshreallycodes.online"),
        ("Employer", "PATH — write PATH only; never the wrong expansion"),
        ("Level", "Mid-junior → mid; niche depth in health IT / programme MIS"),
        ("Salary note", "KES 105,000 gross / month + medical + house allowance (as typed on BRAC form)"),
    ]))

    # —— Employment ——
    _heading(story, S, "Employment timeline")
    story.append(Paragraph(
        "Official PATH HR titles below. Programme workstreams are not separate employers.",
        S["smallg"],
    ))

    roles = [
        (
            "Health Informatics / HMIS Officer",
            "Mar 2025 – Present",
            "PATH  ·  Kisumu / Nyamira (Hybrid)",
            [
                "Support and stabilize KenyaEMR / TaifaCare and DHIS2 across facilities; install and upgrade KenyaEMR on site.",
                "DQA and SQL validation; Power BI / Tableau / Grafana / Metabase dashboards; NDWH API reporting workflows.",
                "Support EMR–lab–pharmacy data flow; maintain Windows / Linux servers hosting EMR data (backups, patching, DR).",
                "Train facility staff and program teams; produce SOPs, job aids, and uptime / progress reports for managers and county teams.",
            ],
        ),
        (
            "ICT Associate",
            "Jan 2024 – Mar 2025",
            "PATH  ·  Kisumu",
            [
                "1st/2nd-line IT for 120+ users; Freshdesk / Zoho / ITIL SLAs; ~98% uptime; M365, AD / Entra ID, Meraki, VoIP / 3CX.",
                "Field ICT for OVC and DREAMS: devices, connectivity, data tools and reporting for mentors and case workers.",
                "Mentored youth and trained ICT hubs; wrote job aids so tools were used after the session.",
                "Salesforce ticket support for PATH users (login / access / forms) — not tenant admin, not Taroworks.",
            ],
        ),
        (
            "ICT Intern",
            "Apr 2023 – Dec 2023",
            "PATH  ·  Homa Bay",
            [
                "LAN / WAN, imaging, VoIP, facility digitalization, ticketing under SLA.",
                "Assisted server-room audits; shadowed senior engineers on firewall rules, VLANs, and Linux provisioning.",
            ],
        ),
        (
            "IT Assistant — Indoor Residual Spraying (IRS) Campaign",
            "2023 · ~2 months (before PATH)",
            "Homa Bay County  ·  one campaign only",
            [
                "Short-term field IT. Tool on record: ODK / Kobo Collect.",
                "Do not claim DHIS2, GPS cleaning, device fleet setup, or spray-tracker ownership unless confirmed. Not “1 year of IRS.”",
            ],
        ),
    ]
    for title, dates, org, bullets in roles:
        block = [
            _role_row(S, title, dates),
            Paragraph(org, S["org"]),
        ]
        for b in bullets:
            block.append(Paragraph(
                f'<font color="{ACCENT}">▸</font>&nbsp;&nbsp;{b}', S["bullet"],
            ))
        story.append(KeepTogether(block))

    # —— Workstreams ——
    _heading(story, S, "Programme workstreams under PATH")
    streams = [
        (
            "ECD Programme MIS & ICT Support",
            "2024 – 2025 · Closed · Remote",
            [
                "Ran digital and manual MIS until close-out: Kobo, tablets, logins, sync by phone and chat, Excel trackers, Power BI packs, onboarding, hard-copy and digital backups.",
                "Never write as Nuru ya Mtoto current role or as a second employer.",
            ],
        ),
        (
            "OVC · DREAMS · Youth mentoring / ICT hubs",
            "During ICT Associate",
            [
                "OVC / DREAMS: field ICT only — devices, connectivity, data tools. Not programme manager, social worker, or DREAMS coordinator.",
                "Youth mentoring: trained 10 people in self-awareness over two months; 3 went on to start businesses or secure jobs (confirm context before use outside PATH youth work).",
            ],
        ),
    ]
    for title, dates, bullets in streams:
        block = [_role_row(S, title, dates)]
        for b in bullets:
            block.append(Paragraph(
                f'<font color="{ACCENT}">▸</font>&nbsp;&nbsp;{b}', S["bullet"],
            ))
        story.append(KeepTogether(block))

    # —— Capability clusters ——
    _heading(story, S, "What I can do")
    _subhead(story, S, "Health information systems")
    _bullets(story, S, [
        "Install, upgrade, and stabilize KenyaEMR at facilities; biometric scanners for patient ID; UPS / power backup; tablets and phones for field teams.",
        "DHIS2 support; PRISM as PATH project database beside DHIS2 (not Prisma ORM; not “PRISM equals DHIS2”).",
        "50+ health facilities supported on site across 3–4 counties; KenyaEMR rollout schedule and per-facility tracker.",
    ])
    _subhead(story, S, "Data quality, MIS & analytics")
    _bullets(story, S, [
        "DQA and SQL validation; Excel (Power Query, pivots, VBA); Power BI, Tableau, Grafana, Metabase.",
        "Digital + manual MIS (registers, Kobo, Excel). Cut reporting grind ~40% where automation held.",
        "Interview posture: start from how the field enters → clean → sample against source → then publish the dashboard.",
    ])
    _subhead(story, S, "IT operations & service desk")
    _bullets(story, S, [
        "~20 tickets/week average; ~25% faster response when queue discipline tightened (confirm before reuse on GreenWheels-style packs).",
        "7 offices; 250+ devices imaged and set up; physical and remote servers; licence cleanup (no invented savings figure).",
        "Restores after outages as soon as possible — no measured restore-time SLO; do not invent one.",
    ])
    _subhead(story, S, "Enablement & delivery")
    _bullets(story, S, [
        "80+ staff trained across 15+ sessions; remote first-line for ECD field staff by phone and chat.",
        "Organised equipment, materials and transport; raised purchase requests; scheduled contractors and signed off work.",
        "Valid driving licence. Tools: Excel / Sheets trackers, Asana, MS Project, Monday.com, Jira.",
    ])

    # —— Flagship project ——
    _heading(story, S, "Flagship project")
    story.append(KeepTogether([
        _role_row(S, "County Health Systems Operations Platform (NDWH & CBS)", "Portfolio"),
        Paragraph("Independent full-stack build  ·  Kakamega, Vihiga, Nyamira, Kisumu", S["org"]),
        Paragraph(
            f'<font color="{ACCENT}">▸</font>&nbsp;&nbsp;'
            "Monitors facility reporting (NDWH vs CBS), EMR deployments, IT assets and incidents across four counties.",
            S["bullet"],
        ),
        Paragraph(
            f'<font color="{ACCENT}">▸</font>&nbsp;&nbsp;'
            "Stack: Next.js 14, TypeScript, Prisma ORM, MySQL (Aiven), 40+ REST APIs, Recharts / Mapbox, auth and roles.",
            S["bullet"],
        ),
        Paragraph(
            f'<font color="{ACCENT}">▸</font>&nbsp;&nbsp;'
            "Proves product ownership, data modeling, health reporting logic and ops thinking — not only ticket closing.",
            S["bullet"],
        ),
    ]))

    # —— Education & certs ——
    _heading(story, S, "Education")
    story.append(Paragraph(
        f'<font name="{FONT_B}" color="{NAVY}">BSc, Applied Computing</font>'
        f'&nbsp;&nbsp;<font color="{ACCENT}">·</font>&nbsp;&nbsp;'
        "KCA University, Nairobi"
        f'&nbsp;&nbsp;<font color="{ACCENT}">·</font>&nbsp;&nbsp;'
        "November 2023",
        S["cred_value"],
    ))
    story.append(Paragraph(
        "Specialization: Cybersecurity and Digital Forensics. Coursework: Ethical Hacking, "
        "Digital Forensics, Data Protection, Cloud Computing, System Analysis & Design, Artificial Intelligence. "
        "Capstone: designed and implemented a secure office network (VLANs, Active Directory, backup and disaster recovery).",
        S["cred_meta"],
    ))

    _heading(story, S, "Certifications & specialised training")
    story.append(Paragraph(
        f'<font name="{FONT_B}" color="{ACCENT}">Verification rule:</font> '
        "Confirm CCNA and AZ-900 as exam cert vs course completion before every submission. "
        "Never invent PMP, PRINCE2, or Certified Scrum Product Owner as completed.",
        S["smallg"],
    ))
    _bullets(story, S, [
        "Cisco Certified Network Associate (CCNA) — verify exam vs NetAcad",
        "Microsoft Certified: Azure Fundamentals (AZ-900) — verify",
        "Google IT Support Professional Certificate (Coursera, 2023)",
        "IBM Technical Support Certificate (Coursera, 2023)",
        "GitHub Professional Certificate (2024)",
        "Microsoft Data Analysis (Microsoft + LinkedIn, 2024)",
        "DHIS2 Academy certificate (write exactly that way)",
        "Cyberise Hackathon Certification (CA Kenya with Huawei, 2022)",
        "National Research Fund Hackathon Certification (2024)",
        "Cyber Shujaa cybersecurity programme (Serianu / KBA / USIU-Africa) — participation only, not a prize",
        "Google Project Management Certificate (Coursera) — started Oct 2026, in progress only",
        "Scrum Product Owner — pursuing / in progress if enrolled; never “certified” until passed",
    ])

    # —— Capability map ——
    _heading(story, S, "Capability map")
    story.append(_kv_table(S, [
        ("Programme MIS", "Lead for BRAC TSO-MIS / MEL / HMIS — DHIS2, KenyaEMR, PRISM, Excel/Kobo, ECD MIS close-out"),
        ("EMR / HIS rollout", "Strongest Kenya differentiator — facility installs, 50+ sites, biometrics, UPS, tablets"),
        ("Data quality", "DQA, SQL, dashboards — start from field entry, not the chart"),
        ("IT / systems ops", "Default remote / university / NGO ICT — 120+ users, M365, AD, Meraki, ~98% uptime"),
        ("Training / adoption", "80+ staff, job aids, remote ECD support — own this aloud in MIS interviews"),
        ("Product / platform", "NDWH & CBS ops platform — use when they want builders, not only operators"),
        ("Vendor / partners", "ISP / vendor evals, contractor sign-off — not Salesforce tenant admin"),
        ("AGYW adjacency", "DREAMS field ICT, youth mentoring, ECD MIS — bridge without overclaiming"),
    ]))

    # —— Gaps ——
    _heading(story, S, "Never claim / verify first")
    _subhead(story, S, "Do not invent")
    story.append(Paragraph(
        "BInsight admin · CommCare · ONA · Stata / SPSS · Salesforce tenant admin / Taroworks · "
        "PMP / PRINCE2 / CSPO completed · living in Nairobi · Nuru ya Mtoto as current ECD title · "
        "1 year of IRS · POS / access control / solar · restore-time SLOs · licence-savings money figures.",
        S["small"],
    ))
    _subhead(story, S, "Verify before leading")
    story.append(Paragraph(
        "Nessus / OpenVAS / Carbon Black depth · “managed Meraki globally” · full interoperability lead claims · "
        "CCNA / AZ-900 exam vs course · any salary figure not already typed on a form.",
        S["small"],
    ))
    story.append(Spacer(1, 3))
    story.append(Paragraph(
        f'<font name="{FONT_B}" color="{ACCENT}">Tone on tools:</font> '
        "Never write “I have not used X.” Frame unfamiliar tools by the job they do and systems already run. "
        "Gaps live in Application_Intelligence for interview prep only — not on the CV or cover letter.",
        S["smallg"],
    ))

    # —— CV design ——
    _heading(story, S, "CV design system")
    story.append(Paragraph(
        "Shared theme: resumes/resume_theme.py. Builders: build_resumes.py (DOCX), pdf_builder.py (PDF). "
        "Facts: resumes/00_Master_Resume.md. This dossier uses the same navy / copper editorial light look.",
        S["smallg"],
    ))

    _subhead(story, S, "Visual standard")
    story.append(_kv_table(S, [
        ("Look", "Light editorial — navy type on white. No full-width dark header block"),
        ("Name", "Navy #0F2744"),
        ("Accent", "Copper #C45C26 — hairline, toolkit labels, bullets, metric values"),
        ("Washes", "Sand #F6EFE6 (chips / toolkit); Cream #FBF7F2 (faint fill); soft copper #E8C4A8 dividers"),
        ("Body", "Slate #1E293B; muted dates / contact #64748B"),
        ("Fonts", "DOCX: Calibri · PDF: Helvetica (ATS-safe, selectable text)"),
        ("Layout", "Single column · real text · no photo · no icons · no skill bars"),
    ]))

    _subhead(story, S, "Page structure (top → bottom)")
    _bullets(story, S, [
        "<b>Header</b> — MESHACK ARIRI · tailored headline · contact. Navy name, copper hairline.",
        "<b>Metric chips (optional)</b> — value + caption on one line so parsers read in order (e.g. “120+ users supported”).",
        "<b>Professional summary</b> — 4–6 lines tailored to the JD; lead with the job’s language; no apology gaps.",
        "<b>Skills toolkit ribbon</b> — labelled clusters ending with a colon; small copper SKILLS label inside the ribbon. Never a big “Core Skills” heading.",
        "<b>Professional experience</b> — PATH roles (+ workstreams when needed). Title bold · dates right · org muted · copper bullets.",
        "<b>Credentials strip</b> — education + certifications together, full-width cream / copper. Never a two-column footer.",
        "<b>Achievements / languages / referees</b> — as needed per pack; keep short.",
    ])

    _subhead(story, S, "Pack file conventions")
    _bullets(story, S, [
        "Folder: applications/Employer Role/ — spaces; no “Role - Employer” hyphens.",
        "Always output: Meshack Ariri CV.pdf/.docx · Meshack Ariri Cover Letter.pdf/.docx.",
        "Combined upload: cover letter first, page break, then CV.",
        "Source: Job_Description.md · Application_Intelligence.md · Portal_Application_Pack.md · build.py.",
        "Generated CVs stay in the pack folder (gitignored there). Use build_resumes.pack_files(HERE).",
    ])

    _subhead(story, S, "Approved CV variants")
    story.append(Paragraph(
        "IT Ops / Systems (default survival)  ·  Health Informatics / HMIS  ·  INGO ICT Officer  ·  "
        "Programme MIS (BRAC TSO-MIS style)  ·  Stretch packs in stretch/ (hard-positioned).",
        S["small"],
    ))

    # —— Positioning ——
    _heading(story, S, "Positioning strategy")
    _bullets(story, S, [
        "<b>Front door:</b> Health Informatics / EMR–DHIS2 / programme MIS when the JD fits.",
        "<b>Volume engine:</b> Remote IT Support & Systems Ops (M365, AD, networking, ticketing) with health systems as proof of seriousness.",
        "<b>Usually skip:</b> Web / Webflow, TA / HR, pure CRM, L1 voice CX, non-health MEL unless entry-level and data-heavy.",
    ])

    story.append(Spacer(1, 10))
    story.append(_rule(color=COPPER, thickness=1.2, space=2))
    story.append(Paragraph(
        "Canonical facts: resumes/00_Master_Resume.md · Skills: 02_Skills_Intelligence.md · "
        "Profile: 01_Career_Profile.md. Update Master Resume first when any fact changes, then rebuild packs.",
        S["smallg"],
    ))

    return story


def main():
    os.makedirs(JOBS_DIR, exist_ok=True)
    os.makedirs(MIRROR_DIR, exist_ok=True)
    out_path = os.path.join(JOBS_DIR, OUT_NAME)
    _doc(out_path).build(build_story())
    print("Saved:", out_path)
    mirror = os.path.join(MIRROR_DIR, OUT_NAME)
    shutil.copy2(out_path, mirror)
    print("Mirrored:", mirror)


if __name__ == "__main__":
    main()
