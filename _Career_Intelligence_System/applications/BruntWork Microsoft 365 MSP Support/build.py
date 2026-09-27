#!/usr/bin/env python3
"""Tailored CV + Cover Letter (DOCX + PDF) for BruntWork Microsoft 365 MSP Support.
Facts per 00_Master_Resume.md. Do not claim Intune/Defender/Copilot production admin.
Run from repo: python3 "applications/BruntWork Microsoft 365 MSP Support/build.py"
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
"headline": "Microsoft 365 & MSP IT Support  |  Entra ID, Endpoints & Backups  |  Remote SMB",
"metrics": [
    ("120+", "users supported"),
    ("~98%", "uptime"),
    ("M365", "Entra / identity"),
    ("80+", "staff trained"),
],
"show_referees": False,
"compact_education": True,
"summary": ("Microsoft 365 and IT support professional with around three years at PATH supporting 120+ users "
    "across multiple sites at roughly 98% uptime. Administers Microsoft 365, Entra ID and Active Directory "
    "(MFA, least privilege, Teams, SharePoint), keeps backups, patching, and endpoint protection running, "
    "and supports people remotely. Also delivers project-based Microsoft 365 setup for small businesses. "
    "Writes SOPs, works independently, and is ready for Australian Eastern Time hours."),
"skills": [
    ("Microsoft 365 / Entra", "Exchange Online, Teams, SharePoint, licences, Entra ID / Azure AD, Active Directory, group policy, MFA, least privilege"),
    ("Endpoints & security", "Windows 10/11, imaging, patching, endpoint protection/EDR, MFA; ready to work in Intune and Defender"),
    ("Backups & health", "Veeam/rsync backups, disaster recovery, Windows and Linux servers, encryption, uptime monitoring"),
    ("Multi-environment", "Remote support across sites, SMB Microsoft 365 setup, context switching, SOPs, knowledge base"),
    ("Operations", "Freshdesk, Zoho Desk, ITIL/SLA, ticket quality, independent remote delivery"),
    ("RMM-adjacent", "Cisco Meraki monitoring, remote administration; ready to ramp the client's RMM"),
],
"experience": [
    {"org":"PATH","title":"Health Informatics / HMIS Officer","dates":"Mar 2025 to Present","loc":"Kisumu/Nyamira, Kenya (Hybrid / Remote)","bullets":[
        "Administer Microsoft 365 and Entra ID / Active Directory for users across healthcare sites: accounts, MFA, least privilege, Teams and SharePoint access, keeping identity and mail working at over 98% uptime.",
        "Maintain backups, encryption, patching, and endpoint protection on Windows and Linux systems; recover services instead of hoping a reboot is enough.",
        "Support staff remotely across multiple sites — isolate identity vs endpoint vs network, document the fix, and turn repeats into SOPs.",
    ]},
    {"org":"PATH","title":"ICT Associate","dates":"Jan 2024 to Mar 2025","loc":"Kisumu, Kenya","bullets":[
        "Delivered 1st- and 2nd-line support to 120+ users, reaching around 98% uptime and about 25% faster ticket response under SLA.",
        "Configured Microsoft 365 (Outlook, Teams, SharePoint) and Active Directory (provisioning, group policy, MFA, endpoint protection).",
        "Monitored Cisco Meraki networks and diagnosed connectivity faults; kept backups and patching on a schedule rather than waiting for an outage.",
        "Wrote knowledge-base articles and trained users so the same how-to did not become another ticket.",
    ]},
    {"org":"PATH","title":"ICT Intern","dates":"Apr 2023 to Dec 2023","loc":"Homa Bay, Kenya","bullets":[
        "Supported LAN/WAN, desktop imaging, Freshdesk tickets under ITIL/SLA, and IT documentation.",
    ]},
],
"certs": "AZ-900  |  CCNA  |  Google IT Support  |  IBM Technical Support  |  GitHub Professional  |  Microsoft Data Analysis",
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "I am applying for the Microsoft 365 & MSP IT Support Specialist (Infrastructure | Security) role. For the past three years at PATH I have provided remote-ready IT support for more than 120 users across multiple sites, keeping services at over 98% uptime. The core of that work is Microsoft 365, Entra ID and Active Directory, MFA, backups, patching, and endpoint protection.",
    "I already work the way an MSP bench needs: switch between environments without mixing them up, finish the ticket, write the SOP. I have also done project-based Microsoft 365 setup and onboarding for small businesses. PATH is in-house healthcare IT, not a named US or Australian MSP, but the multi-site, multi-context pattern is the same.",
    "I want to be direct on the named tools. I have not administered Intune, Microsoft Defender, or Copilot as production consoles. I already do the underlying jobs — identity, endpoints, backups, security hygiene, and teaching non-technical users new tools — and I can ramp the client's Intune, Defender, RMM, and Copilot enablement in week one.",
    "I am based in Kenya, fully remote-ready, and available Monday through Friday, 9:00 AM to 1:00 PM AEST. I hold a BSc in Applied Computing (Cybersecurity and Digital Forensics) plus Microsoft Azure Fundamentals (AZ-900), CCNA, Google IT Support, and IBM Technical Support. Thank you for the chance to keep your SMB clients stable.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]

def build_cover_letter(path):
    doc = Document()
    br.set_base_style(doc)
    br.add_name(doc, "MESHACK ARIRI")
    br.add_title(doc, "Microsoft 365 & MSP IT Support Specialist")
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
