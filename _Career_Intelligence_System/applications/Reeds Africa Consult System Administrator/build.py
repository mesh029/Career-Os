#!/usr/bin/env python3
"""System Administrator, Reeds Africa Consult (agency, client undisclosed), Nairobi.
Deadline 14 Oct 2026. Apply at reedsafricaconsult.com. Canonical PATH titles.
CCNA + AZ-900 hit their preferred certs. Azure/O365 carry the cloud line.
Do not claim AWS production administration or a tier-3 data centre.
Run: python3 "applications/Reeds Africa Consult System Administrator/build.py"
"""
import os, sys
from docx import Document
from docx.shared import Pt

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT_NAIROBI = (
    "Nairobi / Kisumu, Kenya  |  +254 741 174 779  |  aririmeshack@gmail.com  |  "
    "linkedin.com/in/meshack-ariri  |  meshreallycodes.online"
)

cv = {
"headline": "System Administrator  |  3+ yrs system and network administration  |  CCNA, AZ-900  |  Nairobi",
"metrics": [
    ("3+ yrs", "systems and networks"),
    ("~98%", "uptime"),
    ("120+", "users, multi-site"),
    ("CCNA", "and AZ-900"),
],
"show_referees": True,
"compact_education": True,
# Agency screen: referees on request keeps this to one page and avoids the missing-phone
# problem. Named referees live in Portal_Application_Pack.md for their form.
"summary": ("System and network administrator with 3+ years active experience at PATH, a global health "
    "organisation, owning ICT infrastructure end to end for 120+ users across multiple sites at roughly "
    "98% uptime: servers, virtualisation, identity, network and security. Second-level and third-level support under agreed service "
    "levels, with root cause analysis and the SOP written up. CCNA and AZ-900. Bachelor's degree in "
    "Applied Computing."),
"skills": [
    ("Servers and virtualization", "Windows Server 2016-2022, Linux, physical and virtual servers, VMware and Hyper-V virtualization, operating systems, system software and enterprise applications, upgrades and patches, performance, availability, reliability and capacity"),
    ("Identity and cloud", "Active Directory, Microsoft Entra ID / Azure AD, user accounts, permissions and access controls, Microsoft 365 / O365, Microsoft Azure (AZ-900), AWS familiarity"),
    ("Network and data centre", "Network security: LAN, WAN, VPN, Wi-Fi, internet connectivity; routers, switches, firewalls and network appliances (Cisco Meraki, MikroTik, FortiGate); IP addressing, DNS, DHCP; server health, storage, UPS and environmental controls, preventive maintenance"),
    ("Security, service, governance", "ICT security controls and policy, endpoint protection, vulnerability assessment and patch management, system logs and security alert monitoring, audits and risk assessment; backup and disaster recovery (Veeam, rsync) and business continuity; second-level and third-level support, escalation to vendors and service providers, migrations, ICT projects, technical documentation and SOPs, asset and license inventory, mentoring of junior ICT staff"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kenya (multi-site)  ·  available for Nairobi", "bullets": [
        "Administer Windows and Linux servers hosting critical business applications at over 98% availability: patching, upgrades, capacity monitoring, backups and disaster recovery.",
        "Run system audits, configuration reviews and risk assessments, and keep infrastructure documentation current for audit.",
        "Deliver ICT projects with internal stakeholders and external vendors, writing the implementation plans and technical documentation.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kenya (multi-site)", "bullets": [
        "Owned ICT infrastructure for 120+ users across sites at roughly 98% uptime: servers, Microsoft 365 and Active Directory, endpoints, Cisco Meraki switches, access points and security appliances, VPN, Wi-Fi and internet links.",
        "Administered user accounts, permissions and access controls in Active Directory and Entra ID; enforced firewall policy, VLAN segmentation, endpoint protection, MFA and patching.",
        "Provided second and third-level support and resolved incidents within SLA in Freshdesk under ITIL workflows, cutting response time about 25% and applying root cause analysis to stop repeats.",
        "Coordinated vendors and ISPs, kept ICT asset and licence inventory accurate, and trained staff with user guides.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Kenya", "bullets": [
        "Supported LAN and WAN, routers, switches, cabling, imaging and server-room diagnostics with senior engineers.",
    ]},
],
"certs": "CCNA  |  AZ-900  |  Google IT Support  |  IBM Technical Support  |  GitHub Professional  |  Microsoft Data Analysis",
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: System Administrator",
    "",
    "I am applying for the System Administrator position. I have 3+ years of active experience in system and network administration at PATH, a global health organisation, where I have owned ICT infrastructure for 120+ users across multiple sites at roughly 98% uptime. I hold CCNA and Microsoft Azure Fundamentals (AZ-900) and a BSc in Applied Computing from KCA University with a specialisation in cybersecurity and digital forensics.",
    "Your requirements match what I do daily. I install, configure, monitor and maintain physical and virtual servers on Windows Server and Linux, with VMware and Hyper-V virtualisation, patching, upgrades and capacity monitoring, and backup and disaster recovery I have had to restore from. I administer Active Directory and Entra ID — accounts, permissions, group policy, least privilege, MFA — alongside Microsoft 365 and Azure. On the network side I run LAN, WAN, VPN, Wi-Fi and internet connectivity with Cisco Meraki, MikroTik and FortiGate devices, IP addressing, DNS and DHCP, VLAN segmentation and network performance monitoring.",
    "I work at second and third level. Incidents are resolved within agreed service levels in Freshdesk under ITIL workflows, which cut response time by about 25%, and I do the root cause analysis and write the preventive procedure so the same incident does not come back. I enforce ICT security controls, monitor system and security logs, run endpoint protection and patch management, and support audits and risk assessments. I keep system, network and infrastructure documentation current, maintain ICT asset and licence inventory, coordinate vendors and ISPs, and train users — 80+ staff trained across 15+ sessions, plus mentoring for junior ICT colleagues.",
    "Because I was the main ICT point of contact for my sites, I learned to hold servers, identity, network and security together rather than one of them, and to stay calm when an urgent incident lands during business hours with people waiting. I am based in Nairobi, available immediately, and happy to discuss the client's environment and priorities.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


def build_cover_letter(path):
    doc = Document()
    br.set_base_style(doc)
    br.add_name(doc, "MESHACK ARIRI")
    br.add_title(doc, "System Administrator")
    br.add_contact(doc, CONTACT_NAIROBI)
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
    br.CONTACT = CONTACT_NAIROBI
    br.build(cv, files["cv_docx"])
    build_cover_letter(files["cover_docx"])
    cover_title = cv["headline"].split("|")[0].strip()
    pb.build_cv_pdf(cv, files["cv_pdf"], br.CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], br.CONTACT, cover_title)
    br.CONTACT = original
    print("Generated:", HERE)
