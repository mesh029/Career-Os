#!/usr/bin/env python3
"""DevOps Engineer, Savannah Informatics. Entry level, Nairobi, on-site, KES 80-100k.
https://www.savannahinformatics.com/careers/openroles/developeroperations
Hands-on: Linux, networks, Python, PostgreSQL, GitLab, Docker, kubectl.
Ansible, Terraform, Pulumi, CloudFormation, CI/CD, GCP, Django, Go, GraphQL,
NGINX, LXD, Containerd and Sentry are named by the job they do, not as daily tools.
Kubernetes and GitLab sit under independent project work, not PATH.
Run: python3 build.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

cv = {
    "headline": "DevOps Engineer  |  Linux  ·  Python  ·  Kubernetes  ·  Health systems",
    "metrics": [
        ("~98%", "uptime on health systems"),
        ("Linux", "servers in production"),
        ("Python", "PostgreSQL and Git"),
        ("kubectl", "on Kubernetes"),
    ],
    "summary": (
        "I work where the application meets the server. For three years at PATH I have kept Linux systems, "
        "networks and PostgreSQL data up for 120+ users on KenyaEMR and DHIS2, at about 98% uptime. I automate "
        "checks in Python, review changes in GitLab, run incidents through to a root cause, and report the "
        "KPIs to managers. Docker and Kubernetes (kubectl) are part of my project work. Ready to do this "
        "on-site in Nairobi."
    ),
    "skills": [
        ("Linux and networks", "Ubuntu and Debian-family Linux, UNIX shell, OSI, TCP/IP, UDP, ICMP, HTTP(S), DNS, DHCP, SMTP, VLANs, VPN, Cisco Meraki, CCNA"),
        ("Code and platforms", "Python, PostgreSQL, MySQL, Git, GitHub, GitLab, REST APIs, Docker (LXD and Containerd are the same class of runtime), Kubernetes (kubectl, restarts, scaling, configuration)"),
        ("Automation and cloud", "Python and shell automation, in the same family as Ansible, Terraform and CI/CD; Azure (AZ-900), in the same family as AWS and GCP"),
        ("Reliability", "Incident management, root cause analysis, Grafana (Sentry does this for application errors), vulnerability assessment, KPI reporting, mentoring"),
    ],
    "experience": [
        {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
         "loc": "Kenya (hybrid)", "bullets": [
            "Keep the Linux servers behind clinical systems patched, backed up and recoverable, at about 98% uptime, and report that KPI to managers.",
            "Automate checks in Python and SQL on PostgreSQL and MySQL, and move facility data to national systems through APIs. Reporting time down about 40%.",
            "Run incident management through to a written root cause, with Grafana for the live picture and vulnerability notes on the systems I support.",
        ]},
        {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
         "loc": "Kisumu, Kenya", "bullets": [
            "Set up networks and identity for 120+ users across 7 offices: Cisco Meraki, DNS, DHCP, VPN, Active Directory, patching and MFA.",
            "Defined the support process in Freshdesk and Zoho Desk. Response time improved by about 25%, and each fix was written down.",
            "Coordinated facility teams, vendors and county stakeholders through KenyaEMR releases at 50+ sites, and trained 80+ staff.",
        ]},
        {"org": "Independent", "title": "Platform and software projects", "dates": "2023 to Present",
         "loc": "Project-based", "bullets": [
            "Review and merge changes in GitLab, and run Kubernetes workloads with kubectl: restarts, scaling, storage and configuration, from a runbook. Docker alongside VMware, Proxmox and Hyper-V.",
            "Built an operations platform with 40+ REST APIs (Next.js, TypeScript, MySQL) and Python checks that catch a failure before a user reports it.",
        ]},
    ],
    "certs": "CCNA  |  Microsoft Azure Fundamentals (AZ-900)  |  GitHub Professional  |  Google IT Support  |  IBM Technical Support",
    "compact_education": True,
    "show_referees": False,
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: DevOps Engineer (Entry Level), Nairobi",
    "",
    "I am applying for the entry-level DevOps Engineer role, and I can work on-site in Nairobi. For three years at PATH I have sat where the application meets the server: Linux for health systems, the network under it, and Python that checks the data before it moves. Uptime is about 98% for 120+ users, and I report that figure, with the incidents behind it, to managers and county teams.",
    "I set the support process, review changes in GitLab before they land, troubleshoot through to a root cause, and train the people on the system. On project work I use Docker and Kubernetes with kubectl. I write Python, I query PostgreSQL, and I have built REST APIs.",
    "Ansible, Terraform, Pulumi and a CI/CD pipeline (GitLab CI, GitHub Actions or CircleCI) are how a team writes down the setup, test and release I already carry out. GCP and AWS serve the same roles as the Azure I am certified in: compute, containers, functions, storage and queues. Django is a Python framework, so it is the language I already write. Go is the other backend language, and GraphQL asks a REST API for a narrower answer, usually from behind NGINX. That is how I learned every system I run now, from Meraki to KenyaEMR.",
    "Savannah builds the health software I already keep running. I want to help ship it. I hold a BSc in Applied Computing, with cybersecurity and digital forensics, plus CCNA and Azure Fundamentals.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


if __name__ == "__main__":
    files = br.pack_files(HERE)
    br.build(cv, files["cv_docx"])
    br.build_cover(COVER_BODY, "DevOps Engineer", files["cover_docx"], br.CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], br.CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], br.CONTACT, "DevOps Engineer")
    print("Generated:", HERE)
