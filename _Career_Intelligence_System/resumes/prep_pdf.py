#!/usr/bin/env python3
"""Render an interview-prep Markdown file to a themed PDF.

Supports the subset used in prep files: # title, ## sections, ### questions, paragraphs,
- bullets, 1. numbered items, > quotes (with bullets and paragraphs inside), ``` code blocks,
| tables |, **bold** and *italic*. With toc=True the first page lists every question as a link,
every page footer links back to it, and the PDF gets a sidebar outline.
"""
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    KeepTogether, PageBreak, Paragraph, Preformatted, SimpleDocTemplate, Spacer, Table, TableStyle,
)
from reportlab.platypus.flowables import HRFlowable

from resume_theme import COPPER, COPPER_SOFT, CREAM, NAVY, SAND, SLATE, SLATE_MUTED

FONT, FONT_B, FONT_I, FONT_M = "Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Courier"
MARGIN = 0.65 * inch
PAGE_W = A4[0] - 2 * MARGIN
C = colors.HexColor


def _styles():
    s = lambda name, **kw: ParagraphStyle(name, **kw)
    return {
        "title": s("title", fontName=FONT_B, fontSize=22, textColor=C(NAVY), leading=26),
        "sub": s("sub", fontName=FONT, fontSize=10, textColor=C(SLATE_MUTED), leading=14),
        "h2": s("h2", fontName=FONT_B, fontSize=10.5, textColor=colors.white, leading=13),
        "q": s("q", fontName=FONT_B, fontSize=10.4, textColor=C(NAVY), leading=13.5),
        "body": s("body", fontName=FONT, fontSize=9.6, textColor=C(SLATE), leading=13.6,
                  alignment=TA_LEFT, spaceAfter=3),
        "bullet": s("bullet", fontName=FONT, fontSize=9.6, textColor=C(SLATE), leading=13.6,
                    leftIndent=12, firstLineIndent=-10, spaceAfter=2),
        "qbody": s("qbody", fontName=FONT, fontSize=9.7, textColor=C(SLATE), leading=13.8, spaceAfter=3),
        "qbullet": s("qbullet", fontName=FONT, fontSize=9.7, textColor=C(SLATE), leading=13.8,
                     leftIndent=13, firstLineIndent=-11, spaceAfter=2.5),
        "code": s("code", fontName=FONT_M, fontSize=8.4, textColor=C(NAVY), leading=11),
        "th": s("th", fontName=FONT_B, fontSize=7.6, textColor=colors.white, leading=9.4),
        "td": s("td", fontName=FONT, fontSize=7.4, textColor=C(SLATE), leading=9.2),
        "td1": s("td1", fontName=FONT_B, fontSize=7.5, textColor=C(NAVY), leading=9.2),
        "toc_h": s("toc_h", fontName=FONT_B, fontSize=8.2, textColor=C(COPPER), leading=11,
                   spaceBefore=6, spaceAfter=1.5),
        "toc_q": s("toc_q", fontName=FONT, fontSize=7.9, textColor=C(NAVY), leading=10.2,
                   leftIndent=15, firstLineIndent=-15, spaceAfter=0.8),
    }


def _inline(text):
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<i>\1</i>", text)
    text = re.sub(r"`(.+?)`", rf'<font face="{FONT_M}">\1</font>', text)
    return text


def _plain(text):
    return re.sub(r"[*`]", "", text)


def _box(content, bg, rail=None, pad=9):
    t = Table([[content]], colWidths=[PAGE_W])
    style = [
        ("BACKGROUND", (0, 0), (-1, -1), C(bg)),
        ("LEFTPADDING", (0, 0), (-1, -1), pad + 2),
        ("RIGHTPADDING", (0, 0), (-1, -1), pad),
        ("TOPPADDING", (0, 0), (-1, -1), pad - 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), pad - 3),
    ]
    if rail:
        style.append(("LINEBEFORE", (0, 0), (0, -1), 2.6, C(rail)))
    t.setStyle(TableStyle(style))
    return t


def _quote(lines, S):
    """Quote lines (without '> ') to a boxed block with paragraphs, bullets and numbered items."""
    parts, para = [], []

    def flush():
        if para:
            parts.append(Paragraph(_inline(" ".join(para)), S["qbody"]))
            para.clear()

    for ln in lines:
        ln = ln.strip()
        if not ln:
            flush()
        elif ln.startswith("- "):
            flush()
            parts.append(Paragraph(f'<font color="{COPPER}">▸</font>&nbsp;&nbsp;{_inline(ln[2:])}', S["qbullet"]))
        elif re.match(r"^\d+\. ", ln):
            flush()
            n, rest = ln.split(". ", 1)
            parts.append(Paragraph(f'<font color="{COPPER}"><b>{n}.</b></font>&nbsp;&nbsp;{_inline(rest)}',
                                   S["qbullet"]))
        else:
            para.append(ln)
    flush()
    return _box(parts, CREAM, COPPER)


def _table(rows, S):
    """Markdown table rows (header first) to a themed Table; first column is the row label."""
    ncol = len(rows[0])
    first = 1.25 * inch if ncol > 2 else 2.0 * inch
    rest = (PAGE_W - first) / (ncol - 1)
    data = [[Paragraph(_inline(c), S["th"]) for c in rows[0]]]
    for r in rows[1:]:
        r = (r + [""] * ncol)[:ncol]
        data.append([Paragraph(_inline(c), S["td1" if j == 0 else "td"]) for j, c in enumerate(r)])
    t = Table(data, colWidths=[first] + [rest] * (ncol - 1), repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), C(NAVY)),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LINEBELOW", (0, 0), (-1, -1), 0.35, C(COPPER)),
    ]
    for k in range(2, len(data), 2):
        style.append(("BACKGROUND", (0, k), (-1, k), C(CREAM)))
    t.setStyle(TableStyle(style))
    return t


def _section(text, anchor, S):
    band = Table([[Paragraph(f'<a name="{anchor}"/>{_inline(text).upper()}', S["h2"])]], colWidths=[PAGE_W])
    band.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), C(NAVY)),
        ("LINEBELOW", (0, 0), (-1, -1), 2, C(COPPER)),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    band._outline = (anchor, _plain(text), 0)
    return band


def _question(text, n, anchor, S):
    p = Paragraph(f'<a name="{anchor}"/><font color="{COPPER}">Q{n}</font>&nbsp;&nbsp;{_inline(text)}', S["q"])
    p._outline = (anchor, f"Q{n}. {_plain(text)}", 1)
    return p


def _parse(md, S):
    """Return (title, intro_paragraphs, body_flowables, toc_entries)."""
    story, block, toc = [], None, []
    title, intro, seen_section = None, [], False
    lines = md.splitlines()
    i, para, qn, sn = 0, [], 0, 0

    def out(f):
        (block if block is not None else story).append(f)

    def flush_para():
        if para:
            text = " ".join(para)
            if not seen_section and block is None:
                intro.append(text)
            else:
                out(Paragraph(_inline(text), S["body"]))
            para.clear()

    def close_block():
        nonlocal block
        if block:
            story.append(KeepTogether(block))
        block = None

    while i < len(lines):
        line = lines[i].rstrip()
        if line.startswith("```"):
            flush_para()
            code = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i])
                i += 1
            out(Spacer(1, 2))
            out(_box(Preformatted("\n".join(code), S["code"]), SAND, COPPER))
            out(Spacer(1, 4))
        elif line.startswith("|"):
            flush_para()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            i -= 1
            out(Spacer(1, 3))
            out(_table(rows, S))
            out(Spacer(1, 5))
        elif line.startswith("# "):
            flush_para(); close_block()
            title = line[2:]
        elif line.startswith("## "):
            flush_para(); close_block()
            seen_section = True
            sn += 1
            anchor = f"s{sn}"
            toc.append(("s", line[3:], anchor, None))
            story.append(Spacer(1, 8))
            story.append(_section(line[3:], anchor, S))
            story.append(Spacer(1, 2))
        elif line.startswith("### "):
            flush_para(); close_block()
            qn += 1
            anchor = f"q{qn}"
            toc.append(("q", line[4:], anchor, qn))
            block = [Spacer(1, 7), _question(line[4:], qn, anchor, S), Spacer(1, 4)]
        elif line.startswith(">"):
            flush_para()
            quote = [line[1:].lstrip()]
            while i + 1 < len(lines) and lines[i + 1].startswith(">"):
                i += 1
                quote.append(lines[i][1:].lstrip())
            out(_quote(quote, S))
            out(Spacer(1, 3))
        elif line.startswith("- "):
            flush_para()
            out(Paragraph(f'<font color="{COPPER}">▸</font>&nbsp;&nbsp;{_inline(line[2:])}', S["bullet"]))
        elif re.match(r"^\d+\. ", line):
            flush_para()
            n, rest = line.split(". ", 1)
            out(Paragraph(f'<font color="{COPPER}"><b>{n}.</b></font>&nbsp;&nbsp;{_inline(rest)}', S["bullet"]))
        elif not line.strip():
            flush_para()
        else:
            para.append(line.strip())
        i += 1
    flush_para(); close_block()
    return title, intro, story, toc


def _toc(toc, S):
    """Two-column clickable list of sections and questions."""
    items = []
    for kind, text, anchor, n in toc:
        if kind == "s":
            items.append(Paragraph(f'<a href="#{anchor}" color="{COPPER}">{_inline(text).upper()}</a>', S["toc_h"]))
        else:
            items.append(Paragraph(
                f'<a href="#{anchor}" color="{NAVY}"><font color="{COPPER}">Q{n}</font>&nbsp;&nbsp;{_inline(text)}</a>',
                S["toc_q"]))
    # Split at a section boundary near the middle so no section straddles the columns.
    weights = [len(_plain(t)) // 62 + 1 for _, t, _, _ in toc]
    total, run, split = sum(weights), 0, len(items)
    for k, (kind, *_rest) in enumerate(toc):
        if kind == "s" and run >= total / 2 - 4:
            split = k
            break
        run += weights[k]
    col_w = (PAGE_W - 0.25 * inch) / 2
    t = Table([[items[:split], items[split:]]], colWidths=[col_w + 0.25 * inch, col_w])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, -1), 0.25 * inch),
        ("RIGHTPADDING", (1, 0), (1, -1), 0),
        ("LINEAFTER", (0, 0), (0, -1), 0.4, C(COPPER_SOFT)),
        ("LEFTPADDING", (1, 0), (1, -1), 10),
    ]))
    return t


class _Doc(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        o = getattr(flowable, "_outline", None)
        if o:
            key, text, level = o
            self.canv.bookmarkPage("o_" + key)
            self.canv.addOutlineEntry(text, "o_" + key, level=level)


def build_prep_pdf(md_path, pdf_path, footer="Meshack Ariri  ·  Interview prep", toc=False, subtitle=None):
    S = _styles()
    with open(md_path, encoding="utf-8") as f:
        title, intro, body, entries = _parse(f.read(), S)

    head = []
    if title:
        head.append(Paragraph(f'<a name="toc"/>{_inline(title)}', S["title"]))
    if subtitle:
        head.append(Spacer(1, 3))
        head.append(Paragraph(_inline(subtitle), S["sub"]))
    head.append(HRFlowable(width="100%", thickness=1.4, color=C(COPPER), spaceBefore=6, spaceAfter=6))
    for p in intro:
        head.append(Paragraph(_inline(p), S["sub"]))
    if toc:
        head.append(Spacer(1, 4))
        head.append(_toc(entries, S))
        head.append(PageBreak())

    def on_page(canvas, doc):
        canvas.saveState()
        canvas.setFont(FONT, 7.5)
        canvas.setFillColor(C(SLATE_MUTED))
        y = 0.4 * inch
        canvas.drawString(MARGIN, y, footer)
        canvas.drawRightString(A4[0] - MARGIN, y, f"Page {doc.page}")
        if toc and doc.page > 1:
            label = "Back to questions"
            w = canvas.stringWidth(label, FONT_B, 7.5)
            x = (A4[0] - w) / 2
            canvas.setFont(FONT_B, 7.5)
            canvas.setFillColor(C(COPPER))
            canvas.drawString(x, y, label)
            canvas.linkAbsolute("", "toc", (x - 4, y - 3, x + w + 4, y + 9))
        canvas.restoreState()

    doc = _Doc(pdf_path, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
               topMargin=0.6 * inch, bottomMargin=0.7 * inch, title=_plain(title or ""),
               author="Meshack Ariri")
    doc.build(head + body, onFirstPage=on_page, onLaterPages=on_page)
    print("Saved:", pdf_path)
