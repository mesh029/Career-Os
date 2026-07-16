"""Shared visual theme for Career Intelligence System resumes (DOCX + PDF).

Palette: Royal Indigo (vibrant, professional, non-teal). Colour is applied only to
the name, section headings, dividers, and a light header band; body text stays a
dark slate on white so the document prints cleanly and passes ATS parsing.

To change the whole look, edit the hex values below and rerun the build scripts.
Alternative accents you can drop in: burgundy (#7A2E3A), forest green (#2E6B4F),
or navy (#1F3A5F).
"""

# PDF colours (hex with #)
ACCENT = "#3730A3"        # deep indigo: section bars, titles, skill labels, bullets
ACCENT_DARK = "#2A2478"   # darker indigo: top stripe and the name
ACCENT_MID = "#6366F1"    # vibrant indigo: thin rules and separators
ACCENT_LIGHT = "#ECEDFB"  # header band background (soft lavender)
ACCENT_PALE = "#F6F6FD"   # section-heading strip background
SLATE = "#1E293B"         # body text
SLATE_MUTED = "#64748B"   # dates and secondary meta text
GREY = "#475569"

# DOCX colours (hex without #)
ACCENT_HEX = "3730A3"
ACCENT_DARK_HEX = "2A2478"
ACCENT_MID_HEX = "6366F1"
ACCENT_LIGHT_HEX = "ECEDFB"
ACCENT_PALE_HEX = "F6F6FD"
SLATE_HEX = "1E293B"
SLATE_MUTED_HEX = "64748B"

FONT = "Calibri"
FONT_PDF = "Helvetica"
CONTACT = (
    "Kisumu, Kenya  |  +254 741 174 779  |  aririmeshack@gmail.com  |  "
    "linkedin.com/in/meshack-ariri  |  meshreallycodes.online"
)


def format_contact_lines(contact):
    """Split the contact string into two balanced lines for the header block."""
    parts = [p.strip() for p in contact.split("|")]
    if len(parts) <= 3:
        return [contact]
    mid = (len(parts) + 1) // 2
    line1 = "  |  ".join(parts[:mid])
    line2 = "  |  ".join(parts[mid:])
    return [line1, line2]
