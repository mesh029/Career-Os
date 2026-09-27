#!/usr/bin/env python3
"""Network Administrator, Gertrude's Children's Hospital, Nairobi.
Deadline 20 Sep 2026. Apply at apps.gerties.org. Canonical PATH titles.
CCNA satisfies their cert gate. Do not claim Fortinet NSE or biomedical engineering.
Run: python3 "applications/Gertrudes Childrens Hospital Network Administrator/build.py"
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
"headline": "Network Administrator  |  CCNA  |  Multi-site clinical networks, ~98% availability  |  Nairobi",
"metrics": [
    ("CCNA", "certified"),
    ("3+ yrs", "network operations"),
    ("~98%", "availability"),
    ("Multi-site", "inter-site links"),
],
"show_referees": True,
"compact_education": True,
"referees": [
    "Patrick Ondieki, ICT Officer, PATH  |  pondieki@path.org",
    "Marvin Ngosa, Systems Administrator, PATH  |  mngosa@path.org",
    "Gadaffi Ochieng, Procurement Officer, Ampath  |  ochienggadaffi@gmail.com",
],
"summary": ("CCNA-certified network administrator with about three years running multi-site network "
    "operations for PATH, a global health organisation, holding clinical and enterprise systems at "
    "roughly 98% availability for 120+ users. I cover LAN and WAN, inter-site links, wireless, VPN, VLAN "
    "segmentation, IP telephony, firewalls and monitoring. Healthcare taught me that network downtime is "
    "a patient-safety event. Bachelor's degree in Applied Computing, specialising in cybersecurity."),
"skills": [
    ("Network operations", "Availability, performance, capacity and integrity of local and wide area networks (LAN/WAN), internet and inter-site links, routing and switching, VLAN segmentation, TCP/IP, DNS and DHCP, VPN, IP addressing and uptime reporting"),
    ("Platforms and wireless", "Cisco Meraki access points, switches and security appliances; MikroTik; Fortinet FortiGate; structured cabling; multi-AP staff and guest Wi-Fi; IP telephony and VoIP (3CX); onboarding and segmentation of clinical and IoT devices"),
    ("Security and resilience", "Firewall rules and policy, segmentation, MFA and identity, access control, endpoint protection, patch management and vulnerability reporting alongside cyber security functions; backups and disaster recovery, cloud and partner-hosted connectivity"),
    ("Service and documentation", "ITIL practice and SLA, Freshdesk and Zoho Desk, incident response and RCA, Grafana monitoring; resilient, well documented and scalable network design; SOPs, ISP and vendor management, user training"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kenya (multi-site)  ·  available for Nairobi", "bullets": [
        "Hold clinical and enterprise systems available around the clock across facilities at over 98% uptime, covering the network path end to end: site links, addressing, connectivity to cloud and partner-hosted systems, and the servers behind it.",
        "Maintain Windows and Linux servers carrying clinical data with backups, encryption, patching and disaster recovery.",
        "Run system audits, data-flow reviews and risk identification against national standards, working with clinical departments, the ICT team and service providers.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kenya (multi-site)", "bullets": [
        "Configured and monitored Cisco Meraki access points, switches and security appliances across sites, sustaining roughly 98% availability for 120+ users on staff and guest wireless, wired LAN and inter-site connectivity.",
        "Administered network security controls: firewall policy, VLAN segmentation, VPN access, MFA and least-privilege identity in Active Directory and Entra ID, endpoint protection and patching, and responded to alerts.",
        "Installed and supported IP telephony and VoIP, cut incident response time about 25% through ITIL workflows and SLA tracking in Freshdesk, and handled ISP and vendor evaluations with network documentation kept current.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Kenya", "bullets": [
        "Supported LAN and WAN, routers, switches, structured cabling and server-room diagnostics; firewall rules and VLAN segmentation with senior engineers.",
    ]},
],
"certs": "CCNA  |  AZ-900  |  Google IT Support  |  IBM Technical Support  |  GitHub Professional  |  Microsoft Data Analysis",
}

COVER_BODY = [
    "Dear Hiring Manager,",
    "",
    "Re: Network Administrator, Gertrude's Children's Hospital",
    "",
    "I am applying for the Network Administrator position at Gertrude's Children's Hospital. I am CCNA certified, which meets your certification requirement, and I hold a BSc in Applied Computing from KCA University with a specialisation in cybersecurity and digital forensics. For about three years at PATH, a global health organisation, I have run multi-site network operations for 120+ users and held clinical and enterprise systems at roughly 98% availability.",
    "The work you describe is the work I do. I configure and monitor Cisco Meraki access points, switches and security appliances across sites; I manage inter-site links, VLAN segmentation, VPN, DNS and DHCP, addressing, staff and guest wireless, and IP telephony; and I keep connectivity to cloud and partner-hosted systems working. On security I implement the controls rather than debate them: firewall policy, segmentation, MFA and least-privilege identity, endpoint protection and patch management, with alerts answered and incidents documented. I keep the network documented, handle ISPs and vendors, and report availability to leadership.",
    "What I would bring that a network administrator from outside healthcare cannot is the instinct that comes from clinical stakes. I have supported facilities where an EMR that cannot reach its server means a clinician waiting with a patient in front of them, so I plan for resilience, watch capacity before it becomes an outage, and treat availability as a care-delivery obligation. Working with 15 facilities, a Cyber Security team and clinical departments is the environment I already operate in, including onboarding and segmenting new devices safely as clinical and IoT technology arrives.",
    "I am based in Nairobi and available immediately. I would welcome the chance to discuss how I can keep Gertrude's network resilient, documented and ready to scale.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


def build_cover_letter(path):
    doc = Document()
    br.set_base_style(doc)
    br.add_name(doc, "MESHACK ARIRI")
    br.add_title(doc, "Network Administrator")
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
