#!/usr/bin/env python3
"""Senior IT Service Desk Specialist — Corus International (DC hybrid).
Intern off. PATH as global NGO service desk. Do not claim US work authorization or DC residency.
Run: python3 "applications/Corus Senior IT Service Desk Specialist/build.py"
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
"headline": "Senior IT Service Desk Specialist  |  Freshservice, ITIL, queue and SLA  |  Global NGO",
"metrics": [
    ("120+", "users / queue"),
    ("~98%", "uptime"),
    ("ITIL", "SLA / huddles"),
    ("NGO", "PATH / global"),
],
"show_referees": False,
"compact_education": True,
"summary": ("Senior IT Service Desk Specialist for a global health NGO: the person who keeps the "
    "queue honest. I run day-to-day service desk operations for 120+ users across sites: "
    "Freshservice/Freshdesk, ticket hygiene, SLA, triage, and the huddle that assigns work before "
    "the backlog grows a personality. I resolve Tier 1 through Tier 3, escalate P1/P2 with a "
    "playbook, and write the snapshot (volume, SLA, repeats) so the manager is not guessing. "
    "Microsoft 365, Teams, SharePoint, Entra ID, Intune-style endpoints, remote support. "
    "ITIL: Incident, Request, Problem, Change, Knowledge, Service Catalog. PowerShell and Power "
    "Automate for the repeat work. On-call evenings and weekends. English."),
"skills": [
    ("Service desk / ITSM", "Freshservice, Freshdesk, Zoho Desk; categorization, CI/asset, forms and workflows, ticket QA, shift-left"),
    ("Queue and major incident", "Daily huddles, channel balance (phone, chat, portal, email), SLA/OLA, P1/P2 comms, VIP, vendor and Tier 2/3 coordination"),
    ("ITIL practices", "Incident, Request, Problem, Change, Knowledge, Service Catalog; known errors, workarounds, standard change"),
    ("Identity and endpoints", "Microsoft 365, Teams, SharePoint, Azure AD/Entra ID, Intune-style endpoint management, remote support"),
    ("Automation / ops", "PowerShell, Power Automate basics, daily/weekly snapshots, knowledge base, service catalog entries"),
    ("NGO delivery", "Global multi-site support, stakeholder handling, coach and influence without a direct-report line, on-call"),
],
"experience": [
    {"org": "PATH", "title": "Senior IT Service Desk Specialist", "dates": "Mar 2025 to Present",
     "loc": "Kenya (Hybrid / Remote)  ·  global NGO", "bullets": [
        "Coordinate the day-to-day service desk for 120+ staff: Freshservice/Freshdesk, categorization, CI/asset updates, automations, and the huddle that assigns work across phone, chat, portal, and email. Uptime above 98%.",
        "Triage and escalate. P1/P2 user communications. Coordinate Tier 2/3 and vendors. QA ticket hygiene, first contact resolution, and the tone of the reply. Shift-left through the knowledge base and service catalog.",
        "Capture known errors and workarounds. Contribute to problem reviews. Execute standard change for end-user services. Produce the daily and weekly snapshot: volume, SLA, backlog, repeat contacts.",
        "Still close tickets myself, including VIP and coverage gaps. Entra ID, Microsoft 365, Intune-style endpoints, remote support. On-call evenings and weekends.",
    ]},
    {"org": "PATH", "title": "IT Service Desk Specialist", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kenya (multi-site, global NGO)", "bullets": [
        "Owned the queue for 120+ users under ITIL and SLA. Ticket response about 25% faster once L1 had a real escalation path and a knowledge base that was actually current.",
        "Administered Microsoft 365, Teams, SharePoint, and Entra ID / Active Directory. Imaged and supported endpoints. Remote sessions when the user was not in the room.",
        "Trained 80+ users. Wrote the SOP. Coached colleagues on ticket quality without holding a supervisor title.",
    ]},
    {"org": "Independent", "title": "Service desk tooling (project-based)", "dates": "2023 to Present",
     "loc": "Remote", "bullets": [
        "Built an operations platform with 40+ REST APIs: incident tickets, asset lifecycle, dashboards. PowerShell for the repeat admin. So the queue sees the estate, not a spreadsheet.",
    ]},
],
"certs": "AZ-900  |  Google IT Support  |  IBM Technical Support  |  CCNA  |  GitHub Professional  |  Microsoft Data Analysis",
}

COVER_BODY = [
    "Dear Corus hiring team,",
    "",
    "I am applying for the Senior IT Service Desk Specialist role. For about three years at PATH, a global health NGO, I have run the service desk side of IT: the queue, the SLA, the huddle, the knowledge base, and the tickets that still need a human. Freshservice and Freshdesk. Incident, Request, Problem, Change, Knowledge, Service Catalog. Microsoft 365, Teams, SharePoint, Entra ID, Intune-style endpoints. I resolve Tier 1 through Tier 3, write the operational snapshot, and stay on-call when the evening or the weekend needs a person.",
    "I want to be direct on location. I am based in Kenya and authorised to work here. I do not have US work authorization and I cannot sit Tuesday and Wednesday in the Washington office. If this seat is DC-hybrid only, I am not the hire. If Corus can run it remote for a global NGO operator who already lives in this work, I am ready.",
    "Thank you.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


def build_cover_letter(path):
    doc = Document()
    br.set_base_style(doc)
    br.add_name(doc, "MESHACK ARIRI")
    br.add_title(doc, "Senior IT Service Desk Specialist")
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
