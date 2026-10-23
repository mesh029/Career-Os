#!/usr/bin/env python3
"""Technical Support Agent, Influx (Kenya only, WFH, 44h, 24/7 staggered 5-day). Repost of the Sep 2026 L2 ad.
Real PATH titles, with the support level in brackets. Kubernetes and GitLab are hands-on
(confirmed by Meshack 2026-10-07) and sit under independent project work, not PATH.
No CV/ML platform, Datadog, banking or aviation claims.
Run: python3 "applications/Influx Technical Support Agent L2/build.py"
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT = br.CONTACT
COVER_TITLE = "Technical Support Agent  |  Influx, Kenya (WFH)"

cv = {
"headline": "Technical Support Agent  |  Python  ·  GitLab  ·  Kubernetes  ·  Log Analysis  |  Kenya, 24/7",
"metrics": [
    ("3+ yrs", "technical support"),
    ("~98%", "production uptime"),
    ("120+", "users supported"),
    ("~25%", "faster ticket response"),
],
"summary": ("Technical support professional with 3+ years at PATH supporting production health systems and "
    "120+ users, plus hands-on project work in GitLab and Kubernetes. I read system logs, write and run "
    "Python to isolate backend failures, and apply controlled fixes within documented procedures. I know "
    "where reversible ends: a backup and sign-off come before any live-database action that cannot be "
    "undone. I escalate to engineering with complete evidence, explain the issue to the client in plain "
    "English, and write up the root cause and knowledge-base article afterwards. Incident, Change and "
    "Problem Management in Freshdesk and Zoho Desk; Grafana monitoring. Kenya-based, ready for the 24/7 "
    "staggered roster."),
"skills": [
    ("Troubleshooting and escalation", "Deep-dive investigation, pre-approved fix procedures, service restarts, root cause and workarounds, defect confirmation, evidence-ready escalation to Engineering, QA, Infrastructure and Product"),
    ("Logs and scripting", "System and application log analysis, Python (read, write, execute), SQL, Linux shell, operational scripting"),
    ("Platform operations", "GitLab (merge requests, reviews, merges), Kubernetes (kubectl, pod restarts, scaling, storage, configuration), Docker, Git"),
    ("Systems and cloud", "Linux and Windows servers, Apache Tomcat, MySQL, networking (TCP/IP, DNS, VPN), Microsoft Azure (AZ-900), system architecture"),
    ("ITSM and monitoring", "Incident, Change and Problem Management, Freshdesk, Zoho Desk, Jira, Grafana, knowledge base"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer (L2 systems support)", "dates": "Mar 2025 to Present",
     "loc": "Kenya (hybrid)", "bullets": [
        "Take L2 investigations on production health systems (KenyaEMR, DHIS2): read server and application logs, isolate backend failures, restore service and write the root cause. Uptime above 98%.",
        "Use Python and SQL to diagnose data and system errors and automate checks, cutting manual reporting work by about 40%.",
        "Maintain Linux and Windows servers hosting EMR data: patching, backups and recovery. Take a backup and get sign-off before any database change that cannot be reversed.",
        "Escalate confirmed defects to developers and national system teams with reproduction steps, logs and impact, using Grafana dashboards for the live picture.",
    ]},
    {"org": "PATH", "title": "ICT Associate (L1/L2 technical support)", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya", "bullets": [
        "Handled escalated tickets for 120+ users in Freshdesk and Zoho Desk under Incident, Change and Problem workflows. Response time improved by about 25%.",
        "Resolved identity, endpoint, network and application issues, wrote knowledge-base articles and trained 80+ users.",
    ]},
    {"org": "Independent", "title": "Platform and software projects (project-based)", "dates": "2023 to Present",
     "loc": "Remote", "bullets": [
        "Run applications in GitLab and Kubernetes: merge requests, configuration changes, pod restarts, scaling and storage, following a written runbook.",
        "Built an operations platform (Next.js, TypeScript, MySQL, 40+ REST APIs) with incident ticketing and dashboards, plus Python scripts for automation and log checks.",
    ]},
],
"certs": ("GitHub Professional  |  Microsoft Azure Fundamentals (AZ-900)  |  Google IT Support  |  "
          "IBM Technical Support  |  Microsoft Data Analysis"),
"compact_education": True,
"show_referees": False,
}

COVER_BODY = [
    "Dear Influx Hiring Team,",
    "",
    "Re: Technical Support Agent (Kenya, work from home)",
    "",
    "I am applying for the Technical Support Agent role. For more than three years at PATH I have supported "
    "production health systems where downtime stalls clinics, keeping them above 98% uptime for 120+ users. "
    "When the guided steps run out, I am the one who opens the logs.",
    "",
    "My approach matches your brief. I read server and application logs, write and run Python to isolate "
    "the failure, and apply the fix the procedure allows. In my project work I operate in GitLab and "
    "Kubernetes: merge requests, configuration changes, pod restarts, scaling and storage, all from a written "
    "runbook. On live databases I know the line between reversible and not: a backup and sign-off come before "
    "anything that cannot be undone.",
    "",
    "When it is a real defect, Engineering gets reproduction steps, logs and impact, not a vague ticket. The "
    "client gets a plain-English explanation and an honest timeline. Afterwards I write the root cause and the "
    "knowledge-base article so the next agent solves it faster. I work under Incident, Change and Problem "
    "Management in Freshdesk and Zoho Desk, watch systems in Grafana, and cut our ticket response time by "
    "about 25%.",
    "",
    "Your values read like a description of good support: do what you say, show rather than tell, focus on "
    "the facts. I hold a BSc in Applied Computing, GitHub Professional and Microsoft Azure Fundamentals "
    "(AZ-900). I am in Kenya, ready for the 44-hour 24/7 staggered roster including nights, weekends and "
    "holidays, and happy to take your English and technical assessments.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


if __name__ == "__main__":
    files = br.pack_files(HERE)
    br.build(cv, files["cv_docx"])
    br.build_cover(COVER_BODY, COVER_TITLE, files["cover_docx"], CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], CONTACT, COVER_TITLE)
    print("Generated:", HERE)
