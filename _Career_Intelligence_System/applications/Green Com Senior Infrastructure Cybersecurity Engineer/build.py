#!/usr/bin/env python3
"""Senior Infrastructure and Cybersecurity Engineer, Green Com Enterprise Solutions.
Deadline 30 Sep 2026. Email careers@greencom.co.ke.
CCNA held. Do not claim Network+, Security+, RHCSA, LPIC, FCA, or Windows Server Hybrid.
Canonical PATH titles. No relocation note on the location field.
Run: python3 "applications/Green Com Senior Infrastructure Cybersecurity Engineer/build.py"
"""
import os, sys
from docx import Document
from docx.shared import Pt

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT = (
    "Kisumu, Kenya  |  +254 741 174 779  |  aririmeshack@gmail.com  |  "
    "linkedin.com/in/meshack-ariri  |  meshreallycodes.online"
)

cv = {
"headline": "Infrastructure and Cybersecurity Engineer  |  CCNA  |  Windows, Linux, Hyper-V, VMware, Proxmox",
"metrics": [
    ("3+ yrs", "infrastructure"),
    ("CCNA", "certified"),
    ("~98%", "availability"),
    ("L2 / L3", "support"),
],
"show_referees": True,
"compact_education": True,
"summary": ("Infrastructure and cybersecurity engineer with 3+ years at PATH deploying, administering "
    "and monitoring ICT infrastructure: Windows Server and Linux, Hyper-V, VMware and Proxmox, LAN, WAN, "
    "VPN, firewalls and wireless, at roughly 98% availability. I patch, back up, test recovery, plan "
    "capacity, respond to security events, and work second- and third-level under SLA. CCNA, AZ-900, "
    "BSc Applied Computing specialised in cybersecurity and digital forensics."),
"skills": [
    ("Servers and virtualization", "Windows Server administration; Linux administration (Ubuntu, Debian, CentOS, Red Hat / Rocky family); physical and virtual servers; Hyper-V, VMware, Proxmox; patching, updates, backups, disaster recovery testing, capacity planning, performance and availability monitoring"),
    ("Network infrastructure", "TCP/IP, DNS, DHCP, VLANs, routing and switching; LAN, WAN, VPN and remote access; routers, switches, firewalls and wireless (Cisco Meraki, MikroTik, Fortinet FortiGate); firewall rules and VPN administration"),
    ("Cybersecurity and access control", "Network security controls, identity and access control (Active Directory, Entra ID, MFA, least privilege), security event monitoring, incident response, vulnerability assessment and patch management, endpoint protection"),
    ("Hardware, cloud, automation", "Servers, storage, desktops, laptops and ICT asset lifecycle; Microsoft Azure (AZ-900), AWS and Google Cloud familiarity; PowerShell, Bash and Python; second-level and third-level support; technical documentation, infrastructure diagrams and operating procedures"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kenya (multi-site)", "bullets": [
        "Deploy, configure, maintain and optimize Windows and Linux server environments hosting critical systems at over 98% availability, including patching, updates, backups, disaster recovery testing and capacity planning.",
        "Create, manage and monitor virtual machines on Hyper-V, VMware and Proxmox, and watch server performance, availability and infrastructure health.",
        "Monitor security events, run vulnerability assessments and access-control reviews, and keep technical documentation, infrastructure diagrams and operating procedures current.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kenya (multi-site)", "bullets": [
        "Installed, configured and maintained routers, switches, firewalls and wireless infrastructure; supported LAN, WAN, VPN and remote access; administered firewall rules, VPN and network security controls.",
        "Managed identity and access control in Active Directory and Entra ID, endpoint protection, MFA and patching, and responded to infrastructure-related incidents within SLA, cutting response time about 25%.",
        "Installed and maintained servers, storage, desktops, laptops and related ICT equipment, kept ICT asset inventories and lifecycle records, and provided second-level and third-level technical support.",
        "Used PowerShell, Bash and Python for patching, checks and recovery tasks, and took part in infrastructure improvements and Microsoft Azure cloud connectivity.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Kenya", "bullets": [
        "Supported LAN and WAN, routers, switches, cabling, server-room diagnostics, imaging and Linux provisioning with senior engineers.",
    ]},
],
"certs": "CCNA  |  AZ-900  |  Google IT Support  |  IBM Technical Support  |  GitHub Professional  |  Microsoft Data Analysis",
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: Senior Infrastructure and Cybersecurity Engineer",
    "",
    "I am applying for the Senior Infrastructure and Cybersecurity Engineer role at Green Com Enterprise Solutions. For more than three years at PATH I have done this work: Windows Server and Linux, Hyper-V, VMware and Proxmox, LAN, WAN, VPN, firewalls and wireless, backups and disaster recovery, and second- and third-level support, holding availability near 98%. I am CCNA certified, I hold Azure Fundamentals (AZ-900), and I have a BSc in Applied Computing from KCA University with a specialisation in cybersecurity and digital forensics.",
    "I deploy, configure, maintain and optimize Windows and Linux servers, including Ubuntu, Debian-family and CentOS / Red Hat-family hosts. I create and monitor virtual machines, patch, update, back up, test recovery and plan capacity. I install and maintain routers, switches, firewalls and wireless, and I support LAN, WAN, VPN and remote access. Firewall rules, VPN and access control are part of the daily job, as is watching security events and closing infrastructure incidents. I keep ICT asset inventories, diagrams and operating procedures current.",
    "Your preferred list is the stack I already run. CCNA is in hand. Azure is in hand. FortiGate is the firewall I operate. Scripting is PowerShell, Bash and Python. Give me the environment and I will run it.",
    "I am available as soon as possible.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


def build_cover_letter(path):
    doc = Document()
    br.set_base_style(doc)
    br.add_name(doc, "MESHACK ARIRI")
    br.add_title(doc, "Senior Infrastructure and Cybersecurity Engineer")
    br.add_contact(doc, CONTACT)
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
    original = br.CONTACT
    br.CONTACT = CONTACT
    br.build(cv, files["cv_docx"])
    build_cover_letter(files["cover_docx"])
    cover_title = cv["headline"].split("|")[0].strip()
    pb.build_cv_pdf(cv, files["cv_pdf"], br.CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], br.CONTACT, cover_title)
    br.CONTACT = original
    print("Generated:", HERE)
