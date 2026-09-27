#!/usr/bin/env python3
"""Technical Support Agent (L2) — Influx. Kenya WFH. 24x7 staggered 44h.
Intern off. PATH titles this CV only: L2 engineer / L2 agent.
Run: python3 "applications/Influx Technical Support Agent L2/build.py"
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
"headline": "Technical Support Agent (L2)  |  Python, GitLab, Kubernetes, log investigation  |  Kenya WFH 24x7",
"metrics": [
    ("3+ yrs", "technical / L2"),
    ("Python", "logs and scripts"),
    ("GitLab", "Kubernetes"),
    ("24x7", "Kenya WFH"),
],
"show_referees": False,
"compact_education": True,
"summary": ("L2 Technical Support Engineer, about three years at PATH: the person who takes the "
    "ticket when guided steps fail. I read logs, write and run Python to isolate backend failures, "
    "apply controlled changes in GitLab and Kubernetes (restart, MR merge, storage and capacity "
    "inside the guideline), and I stop before a non-reversible live-database action. I escalate to "
    "Engineering, QA, Infrastructure, and Product with reproduction notes. Grafana, Freshdesk, "
    "Incident/Change/Problem. High-compliance health systems. Kenya, WFH, 24x7 staggered 5-day roster."),
"skills": [
    ("L2 / product support", "Deep-dive troubleshooting, pre-approved fixes, client expectation management, evidence-ready escalation to Engineering/QA/Infra/Product"),
    ("Log and code", "Complex system logs, Python (read, write, execute), operational scripting, backend failure isolation, RCA and workarounds"),
    ("Platform operations", "GitLab and GitHub (MR, review, merge), Kubernetes (controlled config, restart, storage, capacity), reversible vs non-reversible database actions"),
    ("Cloud / systems", "Cloud infrastructure (Azure/AZ-900), networking, system architecture, log analysis, Grafana"),
    ("ITSM / change", "Incident, Change, and Problem Management; Freshdesk, Zoho Desk, Jira; KB, SOPs, monitoring hygiene"),
    ("Compliance / roster", "Controlled high-compliance environments (health systems), access and change discipline; 24x7 staggered 5-day; English"),
],
"experience": [
    {"org": "PATH", "title": "Technical Support Engineer (L2)", "dates": "Mar 2025 to Present",
     "loc": "Kenya (Hybrid / Remote)", "bullets": [
        "Own L2 deep-dives on production health systems: read logs, run Python, isolate backend failures, restore service, write the RCA. Uptime above 98%.",
        "Apply only pre-approved change in GitLab/GitHub and Kubernetes: restarts, MR merges, storage and capacity. Stop before a non-reversible database action and escalate with evidence.",
        "Hand Engineering, QA, and Infrastructure a confirmed defect (reproduction, logs, what is safe to run). Grafana for the live picture. Plain English to the client, then the KB article.",
    ]},
    {"org": "PATH", "title": "Technical Support Agent (L2)", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kenya (multi-site)", "bullets": [
        "L2 queue for 120+ users: Freshdesk and Zoho Desk under Incident, Change, and Problem-style ITIL. About 25% faster response once L1 had a real escalation path.",
        "Closed cases guided steps could not: identity, endpoint, network, application logs. Python and SQL to kill repeat failures. Change discipline on live data. Trained 80+ users.",
    ]},
    {"org": "Independent", "title": "Platform operations (GitLab, Kubernetes, Python)", "dates": "2023 to Present",
     "loc": "Remote (project-based)", "bullets": [
        "Operate GitLab/GitHub and Kubernetes-shaped environments: MRs, config, restarts, capacity. 40+ REST APIs, Python automation, MySQL, Grafana-style dashboards. Reversible actions in the runbook; irreversible SQL does not run.",
    ]},
],
"certs": "GitHub Professional  |  AZ-900  |  Google IT Support  |  IBM Technical Support  |  CCNA  |  Microsoft Data Analysis",
}

COVER_BODY = [
    "Dear Influx hiring team,",
    "",
    "I am applying for the Technical Support Agent (L2) role, Kenya, work from home. I am the L2: when the runbook ends, I read the logs, write and run Python, apply the controlled change in GitLab and Kubernetes, and I do not touch a live database action that cannot be reversed. I escalate to Engineering, QA, Infrastructure, and Product with reproduction and evidence. I explain the same incident to the client in plain English.",
    "About three years at PATH in a controlled high-compliance health-systems environment: access, change management, operational procedure. Grafana in production. Freshdesk under Incident, Change, and Problem workflows. Ticket response about 25% faster once the queue had a real L2 path. I hold a BSc in Applied Computing, GitHub Professional, and Azure Fundamentals (AZ-900).",
    "I am based in Kenya. I can work the 44-hour, 24x7 staggered 5-day roster including nights, weekends, and holidays. I will take your English assessment. Contact me only from an @influx.com address. I will not pay any fee.",
    "Thank you.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


def build_cover_letter(path):
    doc = Document()
    br.set_base_style(doc)
    br.add_name(doc, "MESHACK ARIRI")
    br.add_title(doc, "Technical Support Agent (L2)")
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
