#!/usr/bin/env python3
"""Comprehensive technical support CV + cover (DOCX + PDF).
PATH support results, cybersecurity specialisation, named hackathons.
No intern origin story. Canonical PATH titles.
Facts per 00_Master_Resume.md.
Run: python3 "applications/Technical Support Agent/build.py"
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
"headline": "Technical Support Specialist  |  Cybersecurity and digital forensics  |  Service desk · 120+ users",
"metrics": [
    ("120+", "users supported"),
    ("~98%", "uptime held"),
    ("~25%", "faster tickets"),
    ("80+", "staff trained"),
],
"show_referees": False,
"compact_education": True,
"summary": (
    "Technical support specialist with three years at PATH, a BSc in Applied Computing, and a "
    "specialisation in cybersecurity and digital forensics. I own first and second line for more "
    "than 120 users, keep clinical systems above 98 percent uptime, and cut a monthly reporting "
    "grind by about 40 percent with SQL and Python. I work Freshdesk and Zoho Desk under ITIL and SLA. "
    "I isolate whether a fault is the account, the device, the network, or the application, then I "
    "write a note the next person can use."
),
"skills": [
    ("Service desk", "First and second line, Freshdesk, Zoho Desk, Jira Service Management, ITIL, SLA, knowledge base, 20+ tickets a day"),
    ("Product diagnostics", "Reproduce the fault, read logs and REST payloads, SQL checks, Grafana, clean handoff to Engineering"),
    ("Identity and endpoints", "Active Directory, Microsoft 365, Windows 10 and 11, MFA, imaging, printers, VoIP and 3CX, Salesforce tickets"),
    ("Networking", "LAN, WAN, VPN, DNS, DHCP, Cisco Meraki, MikroTik, Wi-Fi. CCNA."),
    ("Security", "Cybersecurity and digital forensics specialisation. Awareness training, access control, vulnerability reporting. Hackathons with CA Kenya and Huawei. Cyber Shujaa programme."),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kisumu and Nyamira, Kenya (hybrid)", "bullets": [
        "Owned the tickets that leave the article: KenyaEMR, DHIS2, accounts, devices, and the joins between laboratory, pharmacy, and reporting. Services stayed above 98 percent uptime.",
        "Reproduced faults before escalating. Read the logs, the SQL, and the API payload, then named whether the break was identity, endpoint, network, or the application. Engineering got a defect, not a feeling.",
        "Built SQL and Python checks that cut a monthly reporting job by about 40 percent, the same habit I use to stop the same support ticket coming back every week.",
        "Trained more than 80 staff and wrote the SOP so a fix does not live only in my head.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya", "bullets": [
        "Ran first and second line for more than 120 users across sites, often more than 20 tickets a day. Uptime stayed around 98 percent. Response time improved about 25 percent once the queue had a real path.",
        "Closed login, MFA, Microsoft 365, Windows, printer, VoIP, and Salesforce access tickets in Freshdesk and Zoho Desk. Administered Active Directory with least privilege. Diagnosed LAN, WAN, VPN, DNS, and DHCP on Cisco Meraki.",
        "Turned repeat fixes into knowledge-base articles. Supported OVC and DREAMS in the field as the ICT person. Ran digital and manual MIS for PATH ECD until that workstream closed in 2025.",
    ]},
    {"org": "Independent", "title": "Remote IT support and platform operations", "dates": "2023 to Present",
     "loc": "Remote (project-based, alongside PATH)", "bullets": [
        "Supported small teams on Microsoft 365, Google Workspace, and onboarding, remotely, with the same ticket discipline I use at PATH.",
        "Built an operations platform used to prove a product defect: Next.js, TypeScript, MySQL, more than 40 REST APIs, an incident module, and Grafana-style dashboards.",
    ]},
],
"certs": (
    "Google IT Support  |  IBM Technical Support  |  AZ-900  |  CCNA  |  GitHub Professional  |  "
    "Microsoft Data Analysis  |  Cyberise (CA Kenya and Huawei, 2022)  |  Cyber Rise (Huawei, 2023)  |  "
    "NRF Cybersecurity Challenge (2024)  |  Blockchain Security (CP Hub, 2024)  |  "
    "KCA Innovation Weeks  |  Cyber Shujaa programme"
),
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "I am applying for the Technical Support role.",
    "For three years at PATH I have owned first and second line for more than 120 users. Uptime has stayed around 98 percent. Ticket response improved about 25 percent. I take the cases the first article cannot finish, keep KenyaEMR and DHIS2 working, and cut a monthly reporting grind by about 40 percent with SQL and Python. I isolate whether the break is the account, the device, the network, or the application, then I write a note Engineering can use.",
    "I hold a BSc in Applied Computing from KCA University with a specialisation in cybersecurity and digital forensics. I have competed in the Cyberise Hackathon run by the Communications Authority of Kenya with Huawei, in Cyber Rise with Huawei, in the National Research Fund Cybersecurity Challenge, and I completed the Cyber Shujaa programme. That is how I think about a ticket that has a security edge, not only a password reset.",
    "Independently I also built an operations platform with more than 40 APIs, which is why I can step into a product instead of guessing from the subject line. I am based in Kisumu, Kenya, and I am ready to work remote. Google IT Support, IBM Technical Support, Azure Fundamentals, and CCNA are on the CV.",
    "Thank you.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


def build_cover_letter(path):
    doc = Document()
    br.set_base_style(doc)
    br.add_name(doc, "MESHACK ARIRI")
    br.add_title(doc, "Technical Support Agent")
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
