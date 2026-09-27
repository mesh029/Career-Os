"""Shared visual theme for Career Intelligence System resumes (DOCX + PDF).

Editorial light: navy type on white paper, copper accent. Colour is used on the
name, a thin copper hairline, metric numbers, toolkit labels, and bullets.
No full-width dark header. Body text stays dark slate for print and ATS.

Edit hex values here, then rebuild. Do not put a dark band behind the name.
"""

# PDF colours (hex with #)
NAVY = "#0F2744"          # name, section titles
COPPER = "#C45C26"        # hairline, toolkit labels, bullets, metric values
COPPER_SOFT = "#E8C4A8"   # metric dividers
SAND = "#F6EFE6"          # metric chips and toolkit wash
CREAM = "#FBF7F2"         # faint toolkit fill
SLATE = "#1E293B"         # body text
SLATE_MUTED = "#64748B"   # dates, contact, captions
GREY = "#475569"

# Aliases so existing builders keep importing ACCENT_* names
HEADER_BG = "#FFFFFF"
HEADER_FG = NAVY
HEADER_SUB = "#3D4F63"
HEADER_MUTED = SLATE_MUTED
WARM = COPPER
ACCENT = COPPER
ACCENT_DARK = NAVY
ACCENT_MID = COPPER_SOFT
ACCENT_LIGHT = SAND
ACCENT_PALE = CREAM

# DOCX colours (hex without #)
HEADER_BG_HEX = "FFFFFF"
HEADER_FG_HEX = "0F2744"
HEADER_SUB_HEX = "3D4F63"
HEADER_MUTED_HEX = "64748B"
WARM_HEX = "C45C26"
ACCENT_HEX = "C45C26"
ACCENT_DARK_HEX = "0F2744"
ACCENT_MID_HEX = "E8C4A8"
ACCENT_LIGHT_HEX = "F6EFE6"
ACCENT_PALE_HEX = "FBF7F2"
SLATE_HEX = "1E293B"
SLATE_MUTED_HEX = "64748B"

FONT = "Calibri"
FONT_PDF = "Helvetica"
CONTACT = (
    "Kisumu, Kenya  |  +254 741 174 779  |  aririmeshack@gmail.com  |  "
    "linkedin.com/in/meshack-ariri  |  meshreallycodes.online"
)

CV_DOCX = "Meshack Ariri CV.docx"
CV_PDF = "Meshack Ariri CV.pdf"
COVER_DOCX = "Meshack Ariri Cover Letter.docx"
COVER_PDF = "Meshack Ariri Cover Letter.pdf"

# Canonical education block (Credentials strip). Do not fork this copy in pack builders.
EDU_DEGREE = "BSc, Applied Computing"
EDU_SCHOOL = "KCA University, Nairobi"
EDU_DATE = "November 2023"
EDU_SPEC = (
    "Cybersecurity and Digital Forensics. Coursework: Ethical Hacking, "
    "Digital Forensics, Data Protection, Cloud Computing."
)
EDU_CAPSTONE = (
    "Capstone: designed and implemented a secure office network "
    "(VLANs, Active Directory, backup and disaster recovery)."
)


def split_certs(certs):
    """Turn a pipe-separated certs string into clean items."""
    return [p.strip() for p in certs.replace("  |  ", "|").split("|") if p.strip()]


def format_certs_line(certs):
    """ATS-readable certs with copper-dot separators."""
    return "  ·  ".join(split_certs(certs))


def format_contact_lines(contact):
    """Split the contact string into two balanced lines for the header block."""
    parts = [p.strip() for p in contact.split("|")]
    if len(parts) <= 3:
        return [contact]
    mid = (len(parts) + 1) // 2
    line1 = "  ·  ".join(parts[:mid])
    line2 = "  ·  ".join(parts[mid:])
    return [line1, line2]


def pack_files(here):
    """Standard output paths inside one application folder."""
    import os
    return {
        "cv_docx": os.path.join(here, CV_DOCX),
        "cv_pdf": os.path.join(here, CV_PDF),
        "cover_docx": os.path.join(here, COVER_DOCX),
        "cover_pdf": os.path.join(here, COVER_PDF),
    }
