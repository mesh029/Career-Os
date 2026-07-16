#!/usr/bin/env python3
"""Shared PDF builder (reportlab) for CVs and cover letters.
Modern single-column layout, ATS-friendly selectable text, shared theme with DOCX builder.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, KeepTogether)

from resume_theme import (
    ACCENT, ACCENT_DARK, ACCENT_MID, ACCENT_LIGHT, ACCENT_PALE,
    SLATE, SLATE_MUTED, GREY, format_contact_lines,
)

T = HexColor(ACCENT)
T_DK = HexColor(ACCENT_DARK)
T_MID = HexColor(ACCENT_MID)
T_LT = HexColor(ACCENT_LIGHT)
T_PL = HexColor(ACCENT_PALE)
BODY = HexColor(SLATE)
MUTED = HexColor(SLATE_MUTED)
FONT = "Helvetica"
FONT_B = "Helvetica-Bold"
FONT_I = "Helvetica-Oblique"
PAGE_W = 7.1 * inch


def _styles():
    return {
        "name": ParagraphStyle(
            "name", fontName=FONT_B, fontSize=26, textColor=T_DK,
            alignment=TA_CENTER, spaceAfter=4, leading=30, tracking=0.5,
        ),
        "title": ParagraphStyle(
            "title", fontName=FONT, fontSize=10.2, textColor=BODY,
            alignment=TA_CENTER, spaceAfter=6, leading=14,
        ),
        "contact": ParagraphStyle(
            "contact", fontName=FONT, fontSize=8.4, textColor=MUTED,
            alignment=TA_CENTER, spaceAfter=2, leading=11.5,
        ),
        "heading": ParagraphStyle(
            "heading", fontName=FONT_B, fontSize=10.8, textColor=T_DK,
            spaceBefore=10, spaceAfter=0, leading=13, leftIndent=8,
        ),
        "summary": ParagraphStyle(
            "summary", fontName=FONT, fontSize=9.6, textColor=BODY,
            alignment=TA_JUSTIFY, leading=13.5, spaceAfter=4,
        ),
        "skill": ParagraphStyle(
            "skill", fontName=FONT, fontSize=9.3, textColor=BODY,
            leading=12.8, spaceAfter=3, leftIndent=2,
        ),
        "roleL": ParagraphStyle(
            "roleL", fontName=FONT_B, fontSize=10.3, textColor=T,
            leading=12.5, spaceAfter=0,
        ),
        "roleR": ParagraphStyle(
            "roleR", fontName=FONT, fontSize=8.8, textColor=MUTED,
            alignment=TA_RIGHT, leading=12,
        ),
        "org": ParagraphStyle(
            "org", fontName=FONT_I, fontSize=9.1, textColor=MUTED,
            leading=12, spaceAfter=3, leftIndent=2,
        ),
        "bullet": ParagraphStyle(
            "bullet", fontName=FONT, fontSize=9.35, textColor=BODY,
            leading=12.8, leftIndent=14, firstLineIndent=-10, spaceAfter=2.5,
        ),
        "small": ParagraphStyle(
            "small", fontName=FONT, fontSize=9.1, textColor=BODY,
            leading=12.5, spaceAfter=2,
        ),
        "smallg": ParagraphStyle(
            "smallg", fontName=FONT, fontSize=8.9, textColor=MUTED,
            leading=11.8, spaceAfter=2,
        ),
        "letter": ParagraphStyle(
            "letter", fontName=FONT, fontSize=10.2, textColor=BODY,
            alignment=TA_JUSTIFY, leading=14.5, spaceAfter=8,
        ),
        "sign": ParagraphStyle(
            "sign", fontName=FONT, fontSize=10.2, textColor=BODY, leading=13,
        ),
    }


def _rule(color=T_MID, thickness=0.9, space=2, width="100%"):
    return HRFlowable(
        width=width, thickness=thickness, color=color,
        spaceBefore=space, spaceAfter=space + 1, lineCap="round",
    )


def _doc(path):
    return SimpleDocTemplate(
        path, pagesize=A4, topMargin=0.48 * inch, bottomMargin=0.48 * inch,
        leftMargin=0.58 * inch, rightMargin=0.58 * inch, title="Meshack Ariri",
    )


def _teal_sep(text):
    return text.replace("|", f'<font color="{ACCENT_MID}">  |  </font>')


def _header(story, S, name, title, contact):
    """Shaded header band with top accent stripe."""
    # Top accent stripe
    stripe = Table([[""]], colWidths=[PAGE_W], rowHeights=[5])
    stripe.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), T_DK),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(stripe)

    contact_lines = format_contact_lines(contact)
    contact_paras = [
        Paragraph(_teal_sep(line), S["contact"]) for line in contact_lines
    ]
    header_inner = [
        [Paragraph(name, S["name"])],
        [Paragraph(title, S["title"])],
    ]
    for cp in contact_paras:
        header_inner.append([cp])

    header_tbl = Table(header_inner, colWidths=[PAGE_W])
    header_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), T_LT),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ]))
    story.append(header_tbl)
    story.append(_rule(color=T, thickness=1.8, space=4))


def _heading(story, S, text):
    """Section heading with left accent bar."""
    bar_w = 0.14 * inch
    row = Table(
        [[Paragraph("", ParagraphStyle("bar", fontSize=1)),
          Paragraph(text.upper(), S["heading"])]],
        colWidths=[bar_w, PAGE_W - bar_w],
    )
    row.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), T),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 0),
        ("LEFTPADDING", (1, 0), (1, 0), 8),
        ("BACKGROUND", (1, 0), (1, 0), T_PL),
    ]))
    story.append(row)
    story.append(_rule(color=T_MID, thickness=0.6, space=1))


def build_cv_pdf(data, path, contact):
    S = _styles()
    story = []
    _header(story, S, "MESHACK ARIRI", data["headline"], contact)

    _heading(story, S, "Professional Summary")
    story.append(Paragraph(data["summary"], S["summary"]))

    _heading(story, S, "Core Skills")
    for label, items in data["skills"]:
        story.append(Paragraph(
            f'<font name="{FONT_B}" color="{ACCENT}">{label}:</font> {items}',
            S["skill"],
        ))

    _heading(story, S, "Professional Experience")
    for role in data["experience"]:
        loc = role.get("loc", "")
        row = Table(
            [[Paragraph(role["title"], S["roleL"]),
              Paragraph(role["dates"], S["roleR"])]],
            colWidths=[4.85 * inch, 2.25 * inch],
        )
        row.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
            ("LEFTPADDING", (0, 0), (-1, -1), 2),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]))
        block = [
            row,
            Paragraph(
                f'{role["org"]}'
                + (f'  <font color="{ACCENT_MID}">|</font>  {loc}' if loc else ""),
                S["org"],
            ),
        ]
        for b in role["bullets"]:
            block.append(Paragraph(
                f'<font color="{ACCENT}">▪</font>&nbsp;&nbsp;{b}', S["bullet"],
            ))
        story.append(KeepTogether(block))

    _heading(story, S, "Education")
    story.append(Paragraph(
        "BSc, Applied Computing&nbsp;&nbsp;"
        f'<font color="{ACCENT_MID}">|</font>&nbsp;&nbsp;'
        "KCA University, Nairobi&nbsp;&nbsp;"
        f'<font color="{ACCENT_MID}">|</font>&nbsp;&nbsp;November 2023',
        ParagraphStyle("edu", parent=S["small"], fontName=FONT_B),
    ))
    story.append(Paragraph(
        "Specialized in Cybersecurity and Digital Forensics. Coursework included "
        "Ethical Hacking, Digital Forensics, Data Protection, and Cloud Computing.",
        S["smallg"],
    ))
    story.append(Paragraph(
        "Capstone: Designed and implemented a secure office network (VLANs, Active "
        "Directory, backup and disaster recovery) simulating real-world IT administration.",
        S["smallg"],
    ))

    if data.get("languages"):
        _heading(story, S, "Languages")
        story.append(Paragraph(data["languages"], S["small"]))

    _heading(story, S, "Certifications")
    story.append(Paragraph(data["certs"], S["small"]))

    if data.get("achievements"):
        _heading(story, S, "Achievements & Activities")
        for a in data["achievements"]:
            story.append(Paragraph(
                f'<font color="{ACCENT}">▪</font>&nbsp;&nbsp;{a}', S["bullet"],
            ))

    _heading(story, S, "Referees")
    story.append(Paragraph("Available upon request.", S["smallg"]))

    _doc(path).build(story)
    print("Saved:", path)


def build_cover_pdf(paragraphs, path, contact, headline="ICT Manager"):
    S = _styles()
    story = []
    _header(story, S, "MESHACK ARIRI", headline, contact)
    story.append(Spacer(1, 8))
    for para in paragraphs:
        if para == "":
            story.append(Spacer(1, 4))
        elif para in ("Sincerely,", "Kind regards,"):
            story.append(Spacer(1, 6))
            story.append(Paragraph(para, S["sign"]))
        else:
            story.append(Paragraph(para, S["letter"]))
    _doc(path).build(story)
    print("Saved:", path)
