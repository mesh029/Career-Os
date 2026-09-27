#!/usr/bin/env python3
"""Network Engineer, Co-operative Bank of Kenya. Ref NE/IID/2026. Deadline 30 Sep 2026.
Email application to jobs@co-opbank.co.ke.

CCNP is stated as a MUST and we hold CCNA. Never claim CCNP, CCIE, Checkpoint,
Avaya, AIX, Solaris, OpenShift or Service Provider experience.

To switch on a truthful CCNP line, set CCNP_EXAM_BOOKED to the booked exam date
string (e.g. "12 Nov 2026") ONLY after the exam is actually paid for and scheduled.
Leave it as None until then.

Run: python3 "stretch/Co-op Bank Network Engineer/build.py"
"""
import os, sys
from docx import Document
from docx.shared import Pt

CCNP_EXAM_BOOKED = None   # e.g. "12 Nov 2026" once ENCOR 350-401 is actually booked

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT = (
    "Kisumu, Kenya  |  +254 741 174 779  |  aririmeshack@gmail.com  |  "
    "linkedin.com/in/meshack-ariri  |  meshreallycodes.online"
)

certs = "CCNA  |  AZ-900  |  Google IT Support  |  IBM Technical Support  |  GitHub Professional"
if CCNP_EXAM_BOOKED:
    certs = f"CCNA  |  CCNP Enterprise ENCOR 350-401 booked {CCNP_EXAM_BOOKED}  |  AZ-900  |  Google IT Support  |  IBM Technical Support"

cv = {
"headline": "Network Engineer  |  CCNA  |  Multi-site LAN/WAN, firewalls, DR  |  ~98% uptime against SLA",
"metrics": [
    ("3+ yrs", "LAN/WAN operations"),
    ("~98%", "uptime vs SLA"),
    ("Multi-site", "corporate network"),
    ("CCNA", "and AZ-900"),
],
"show_referees": True,
"compact_education": False,
"summary": ("Network professional with 3+ years running multi-site corporate LAN/WAN for PATH, a global "
    "health organisation, holding network and business systems at roughly 98% uptime against agreed "
    "service levels. I monitor performance, logs and events for proactive remedial support; own firewall "
    "policy, signature and patch updates, access control and security policy; and maintain disaster "
    "recovery and business continuity. CCNA certified, with TCP/IP, IP telephony and firewall appliances. "
    "BSc Applied Computing, specialising in cybersecurity."),
"skills": [
    ("Network engineering", "TCP/IP, LAN and WAN, routing and switching, VLAN design and segmentation, VPN, IP addressing, DNS and DHCP, wireless, inter-site links, performance and capacity management against business SLAs"),
    ("Devices and platforms", "Cisco and Cisco Meraki access points, switches and MX security appliances; MikroTik; Fortinet FortiGate firewall appliances; IP telephony (3CX); structured cabling; Windows Server 2016-2022 and Linux in multi-platform environments"),
    ("Monitoring and security", "Network monitoring, logs and events for proactive remedial support; firewall policy, signature updates and patch releases across ICT assets; device access and control policies, security and storage policies, endpoint protection, MFA, vulnerability reporting; modern threat awareness"),
    ("Continuity and delivery", "Disaster recovery, backup policy and business continuity; network and architecture documentation, full ICT component inventory; ITIL and SLA, incident response and root cause analysis; project delivery for network setup and migration, vendor and ISP management, mentoring"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kenya (multi-site)", "bullets": [
        "Keep the corporate network and the business systems on it performing consistently at over 98% uptime against agreed service levels, covering inter-site links, addressing, and connectivity to cloud and partner-hosted platforms.",
        "Maintain disaster recovery and business continuity for Windows and Linux platforms: backup policy, encryption, patching and restore testing, and document architecture components and configurations.",
        "Coordinate infrastructure and integration projects across multi-disciplinary teams and external vendors, from requirements through implementation plans to handover documentation.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kenya (multi-site)", "bullets": [
        "Installed, supported and maintained network devices across sites: Cisco Meraki switches, access points and MX security appliances, routers, firewalls and IP telephony, attending to system failures and coordinating resolution.",
        "Monitored network performance, logs and events and moved the team to proactive remedial support, sustaining roughly 98% availability for 120+ users and cutting incident response time about 25% under ITIL workflows and SLA tracking.",
        "Developed and enforced device access and control policies, firewall rules, VLAN segmentation, VPN access, endpoint protection, MFA and patch and signature updates in line with security policy.",
        "Maintained the full ICT network component inventory and documentation, and ran ISP and vendor evaluations.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Kenya", "bullets": [
        "Supported LAN and WAN, routers, switches, cabling and server-room diagnostics with senior engineers.",
    ]},
],
"certs": certs,
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: Network Engineer, Reference NE/IID/2026",
    "",
    "I am applying for the Network Engineer role, reference NE/IID/2026. For more than three years at PATH I have run the corporate network across multiple sites: performance against SLA, monitoring and proactive support, firewall and access policy, patch and signature updates, disaster recovery, and a complete inventory of the network. Availability has held near 98%. I am CCNA certified, with a BSc in Applied Computing from KCA University, specialised in cybersecurity and digital forensics.",
    "Your job description is the work I already do. I keep LAN and WAN performing so the business systems on them stay up. I watch logs, events and device health and act before users raise a ticket. I write and enforce device access, security, backup and continuity policy. I install and maintain Cisco and Cisco Meraki switches, access points and MX appliances, routers, FortiGate firewalls and IP telephony, and I take the outage when a device fails. I document the architecture and I own the asset list.",
    "I hold CCNA. CCNP is something I am willing to learn. What I bring now is three years of live multi-site network ownership, TCP/IP, firewalls, IP telephony, and the security instinct that comes from a forensics degree and from keeping systems reachable when people are waiting on them. Give me your topology and I will run it.",
    "I am available as soon as possible.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


def build_cover_letter(path):
    doc = Document()
    br.set_base_style(doc)
    br.add_name(doc, "MESHACK ARIRI")
    br.add_title(doc, "Network Engineer")
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
