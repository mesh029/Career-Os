#!/usr/bin/env python3
"""Shared PDF builder (reportlab) for CVs and cover letters.

Editorial light header (navy on white, copper hairline), metric chips, toolkit
ribbon instead of a Core Skills section. ATS-friendly selectable text.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, KeepTogether)

from resume_theme import (
    HEADER_FG, HEADER_SUB, HEADER_MUTED, WARM,
    ACCENT, ACCENT_DARK, ACCENT_MID, ACCENT_LIGHT, ACCENT_PALE,
    SLATE, SLATE_MUTED, format_contact_lines, format_certs_line,
    EDU_DEGREE, EDU_SCHOOL, EDU_DATE, EDU_SPEC, EDU_CAPSTONE,
)

NAVY = HexColor(HEADER_FG)
SUB = HexColor(HEADER_SUB)
COPPER = HexColor(WARM)
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
PAGE_W = 7.2 * inch


def _styles():
    return {
        "name": ParagraphStyle(
            "name", fontName=FONT_B, fontSize=22, textColor=NAVY,
            alignment=TA_LEFT, spaceAfter=1, leading=26,
        ),
        "title": ParagraphStyle(
            "title", fontName=FONT, fontSize=9.6, textColor=SUB,
            alignment=TA_LEFT, spaceAfter=3, leading=13,
        ),
        "contact": ParagraphStyle(
            "contact", fontName=FONT, fontSize=8.0, textColor=MUTED,
            alignment=TA_LEFT, spaceAfter=1, leading=11,
        ),
        "heading": ParagraphStyle(
            "heading", fontName=FONT_B, fontSize=8.6, textColor=NAVY,
            spaceBefore=0, spaceAfter=0, leading=11,
        ),
        "summary": ParagraphStyle(
            "summary", fontName=FONT, fontSize=9.4, textColor=BODY,
            alignment=TA_JUSTIFY, leading=12.8, spaceAfter=2,
        ),
        "toolkit": ParagraphStyle(
            "toolkit", fontName=FONT, fontSize=8.5, textColor=BODY,
            leading=12.2, spaceAfter=1.2,
        ),
        "cred_label": ParagraphStyle(
            "cred_label", fontName=FONT_B, fontSize=7.0, textColor=COPPER,
            alignment=TA_RIGHT, leading=10, spaceAfter=0,
        ),
        "cred_value": ParagraphStyle(
            "cred_value", fontName=FONT_B, fontSize=9.3, textColor=NAVY,
            leading=12.4, spaceAfter=0,
        ),
        "cred_meta": ParagraphStyle(
            "cred_meta", fontName=FONT, fontSize=8.2, textColor=MUTED,
            leading=11.2, spaceAfter=0,
        ),
        "cred_certs": ParagraphStyle(
            "cred_certs", fontName=FONT, fontSize=8.4, textColor=BODY,
            leading=12.0, spaceAfter=0,
        ),
        "roleL": ParagraphStyle(
            "roleL", fontName=FONT_B, fontSize=10.0, textColor=NAVY,
            leading=12, spaceAfter=0,
        ),
        "roleR": ParagraphStyle(
            "roleR", fontName=FONT, fontSize=8.4, textColor=MUTED,
            alignment=TA_RIGHT, leading=12,
        ),
        "org": ParagraphStyle(
            "org", fontName=FONT_I, fontSize=8.7, textColor=MUTED,
            leading=11.5, spaceAfter=2, leftIndent=1,
        ),
        "bullet": ParagraphStyle(
            "bullet", fontName=FONT, fontSize=9.05, textColor=BODY,
            leading=11.8, leftIndent=12, firstLineIndent=-9, spaceAfter=1.2,
        ),
        "small": ParagraphStyle(
            "small", fontName=FONT, fontSize=8.9, textColor=BODY,
            leading=12.0, spaceAfter=1.5,
        ),
        "smallg": ParagraphStyle(
            "smallg", fontName=FONT, fontSize=8.5, textColor=MUTED,
            leading=11.4, spaceAfter=1.2,
        ),
        "metric_v": ParagraphStyle(
            "metric_v", fontName=FONT_B, fontSize=11.5, textColor=COPPER,
            alignment=TA_CENTER, leading=14, spaceAfter=0,
        ),
        "metric_c": ParagraphStyle(
            "metric_c", fontName=FONT, fontSize=6.8, textColor=MUTED,
            alignment=TA_CENTER, leading=9, spaceAfter=0,
        ),
        "letter": ParagraphStyle(
            "letter", fontName=FONT, fontSize=10.2, textColor=BODY,
            alignment=TA_JUSTIFY, leading=14.5, spaceAfter=8,
        ),
        "sign": ParagraphStyle(
            "sign", fontName=FONT, fontSize=10.2, textColor=BODY, leading=13,
        ),
    }


def _rule(color=COPPER, thickness=1.15, space=1, width="100%"):
    return HRFlowable(
        width=width, thickness=thickness, color=color,
        spaceBefore=space, spaceAfter=space + 1, lineCap="round",
    )


def _doc(path):
    return SimpleDocTemplate(
        path, pagesize=A4, topMargin=0.38 * inch, bottomMargin=0.36 * inch,
        leftMargin=0.52 * inch, rightMargin=0.52 * inch, title="Meshack Ariri",
    )


def _sep(text, color=HEADER_MUTED):
    return text.replace("|", f'<font color="{color}">  ·  </font>')


def _header(story, S, name, title, contact, metrics=None):
    """Light header: navy name on white, copper hairline. No dark block."""
    story.append(Paragraph(name, S["name"]))
    story.append(Paragraph(title, S["title"]))
    for line in format_contact_lines(contact):
        story.append(Paragraph(_sep(line), S["contact"]))
    story.append(Spacer(1, 4))
    story.append(_rule(color=COPPER, thickness=2.4, space=0))

    if metrics:
        packed = []
        for value, caption in metrics:
            packed.append(Table(
                [[Paragraph(value, S["metric_v"])],
                 [Paragraph(caption.upper(), S["metric_c"])]],
                colWidths=[PAGE_W / len(metrics)],
            ))
        row = Table([packed], colWidths=[PAGE_W / len(metrics)] * len(metrics))
        row.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), T_LT),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("LEFTPADDING", (0, 0), (-1, -1), 2),
            ("RIGHTPADDING", (0, 0), (-1, -1), 2),
            ("LINEAFTER", (0, 0), (-2, -1), 0.4, T_MID),
        ]))
        story.append(row)
        story.append(Spacer(1, 6))
    else:
        story.append(Spacer(1, 8))


def _heading(story, S, text):
    story.append(Spacer(1, 5))
    story.append(Paragraph(text.upper(), S["heading"]))
    story.append(_rule(color=COPPER, thickness=0.9, space=1))


def _toolkit(story, S, skills):
    """Keyword ribbon. Not a Core Skills heading. Copper rail + sand wash."""
    if not skills:
        return
    lines = []
    for label, items in skills:
        lines.append(
            f'<font name="{FONT_B}" color="{ACCENT}">{label}</font>'
            f'&nbsp;&nbsp;{items}'
        )
    inner = Paragraph("<br/>".join(lines), S["toolkit"])
    rail = Table(
        [[Paragraph("", ParagraphStyle("rail", fontSize=1)), inner]],
        colWidths=[0.11 * inch, PAGE_W - 0.11 * inch],
    )
    rail.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), COPPER),
        ("BACKGROUND", (1, 0), (1, 0), T_PL),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 0),
        ("LEFTPADDING", (1, 0), (1, 0), 8),
        ("RIGHTPADDING", (1, 0), (1, 0), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(rail)
    story.append(Spacer(1, 2))


def _credentials(story, S, data):
    """Full-width Education + Certifications strip. Never a two-column footer."""
    degree = (
        f'{EDU_DEGREE}'
        f'&nbsp;&nbsp;<font color="{ACCENT}">·</font>&nbsp;&nbsp;'
        f'{EDU_SCHOOL}'
        f'&nbsp;&nbsp;<font color="{ACCENT}">·</font>&nbsp;&nbsp;'
        f'{EDU_DATE}'
    )
    spec_bits = [EDU_SPEC]
    if not data.get("compact_education"):
        spec_bits.append(EDU_CAPSTONE)
    spec = " ".join(spec_bits)
    certs = format_certs_line(data.get("certs") or "")

    label_w = 1.12 * inch
    value_w = PAGE_W - 0.11 * inch - label_w
    inner = Table(
        [
            [
                Paragraph("EDUCATION", S["cred_label"]),
                [
                    Paragraph(degree, S["cred_value"]),
                    Paragraph(spec, S["cred_meta"]),
                ],
            ],
            [
                Paragraph("CERTIFICATIONS", S["cred_label"]),
                Paragraph(certs, S["cred_certs"]),
            ],
        ],
        colWidths=[label_w, value_w],
    )
    inner.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, -1), 8),
        ("LEFTPADDING", (1, 0), (1, -1), 2),
        ("RIGHTPADDING", (1, 0), (1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, 0), 0.35, T_MID),
    ]))
    rail = Table(
        [[Paragraph("", ParagraphStyle("cred_rail", fontSize=1)), inner]],
        colWidths=[0.11 * inch, PAGE_W - 0.11 * inch],
    )
    rail.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), COPPER),
        ("BACKGROUND", (1, 0), (1, 0), T_PL),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    story.append(Spacer(1, 8))
    story.append(rail)
    story.append(Spacer(1, 3))


def build_cv_pdf(data, path, contact):
    S = _styles()
    story = []
    _header(
        story, S, "MESHACK ARIRI", data["headline"], contact,
        metrics=data.get("metrics"),
    )

    _heading(story, S, "Profile")
    story.append(Paragraph(data["summary"], S["summary"]))
    _toolkit(story, S, data.get("skills") or [])

    _heading(story, S, "Experience")
    for role in data["experience"]:
        loc = role.get("loc", "")
        row = Table(
            [[Paragraph(role["title"], S["roleL"]),
              Paragraph(role["dates"], S["roleR"])]],
            colWidths=[4.95 * inch, 2.25 * inch],
        )
        row.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
            ("LEFTPADDING", (0, 0), (-1, -1), 1),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]))
        block = [
            row,
            Paragraph(
                f'{role["org"]}'
                + (f'  <font color="{ACCENT}">·</font>  {loc}' if loc else ""),
                S["org"],
            ),
        ]
        for b in role["bullets"]:
            block.append(Paragraph(
                f'<font color="{ACCENT}">▸</font>&nbsp;&nbsp;{b}', S["bullet"],
            ))
        story.append(KeepTogether(block))

    if data.get("projects"):
        _heading(story, S, "Selected work")
        for proj in data["projects"]:
            loc = proj.get("loc", "")
            row = Table(
                [[Paragraph(proj["title"], S["roleL"]),
                  Paragraph(proj.get("dates", ""), S["roleR"])]],
                colWidths=[4.95 * inch, 2.25 * inch],
            )
            row.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
                ("LEFTPADDING", (0, 0), (-1, -1), 1),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]))
            org = proj.get("org", "")
            block = [row]
            if org or loc:
                block.append(Paragraph(
                    org
                    + (f'  <font color="{ACCENT}">·</font>  {loc}' if loc else ""),
                    S["org"],
                ))
            for b in proj["bullets"]:
                block.append(Paragraph(
                    f'<font color="{ACCENT}">▸</font>&nbsp;&nbsp;{b}', S["bullet"],
                ))
            story.append(KeepTogether(block))

    _credentials(story, S, data)

    if data.get("languages"):
        _heading(story, S, "Languages")
        story.append(Paragraph(data["languages"], S["small"]))

    if data.get("achievements"):
        _heading(story, S, "Selected results")
        for a in data["achievements"]:
            story.append(Paragraph(
                f'<font color="{ACCENT}">▸</font>&nbsp;&nbsp;{a}', S["bullet"],
            ))

    if data.get("show_referees", True):
        ref_block = [
            Spacer(1, 5),
            Paragraph("REFEREES", S["heading"]),
            _rule(color=COPPER, thickness=0.9, space=1),
        ]
        if data.get("referees"):
            for ref in data["referees"]:
                ref_block.append(Paragraph(ref, S["small"]))
                ref_block.append(Spacer(1, 2))
        else:
            ref_block.append(Paragraph("Available upon request.", S["smallg"]))
        story.append(KeepTogether(ref_block))

    _doc(path).build(story)
    print("Saved:", path)


def build_cover_pdf(paragraphs, path, contact, headline="ICT Manager"):
    S = _styles()
    story = []
    _header(story, S, "MESHACK ARIRI", headline, contact)
    story.append(Spacer(1, 10))
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
