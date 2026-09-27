#!/usr/bin/env python3
"""IT Lead/Manager, CURE International Kenya (Kijabe/Kiambu).
LinkedIn Easy Apply. Canonical PATH titles.
Do not claim you wrote CURE AI policy, owned a hospital finance ERP, or managed a named IT Officer at PATH. Chromebooks sit on the device list as endpoints you deploy in the same lifecycle as laptops and tablets.
Run: python3 "applications/CURE International IT Lead Manager/build.py"
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
"headline": "IT Lead  |  Hospital ICT: LAN/WAN, servers, EMR, security, backups  |  CCNA",
"metrics": [
    ("3+ yrs", "hospital-grade ICT"),
    ("~98%", "availability"),
    ("120+", "users trained"),
    ("EMR", "and network"),
],
"show_referees": True,
"compact_education": True,
"summary": ("IT lead with 3+ years running all ICT functions in a health organisation: LAN, WAN, "
    "servers and virtual machines, endpoints, EMR and enterprise applications, daily monitoring, "
    "backups and security, at about 98% availability. I document, automate where it helps, train "
    "staff, mentor junior ICT, and manage vendors and IT resources. CCNA. BSc Applied Computing."),
"skills": [
    ("Deployment and provisioning", "LAN, WAN, network segments, Internet, remote access; install and rebuild servers; hardware, peripherals, services, settings, directories, storage; desktops, laptops, Chromebooks, tablets, printers, routers, switches, firewalls, phones, smartphones and software; deployment and configuration documentation; PowerShell/Bash automation"),
    ("Accounts, security, privacy", "Create, update, disable and delete user accounts and access permissions (Active Directory, Entra ID); security monitoring to identify and remediate risks or intrusions; OS security patches, updates and upgrades; data backup and privacy; acceptable AI use under IT security and data privacy rules"),
    ("Hospital systems and backups", "Enterprise applications: communications, collaboration, EMR (KenyaEMR/TaifaCare, DHIS2), inventory management, human resources, financial management and accounting access; physical servers, virtual machines, WiFi access points, operating systems; automated daily backups to local, external network-attached and offsite cloud storage"),
    ("Lead, training, resources", "Leadership, mentoring, coaching and day-to-day management of junior ICT / IT Officer; hospital staff training on hardware, software and systems; IT budgets, resources and vendor relationships"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kenya (health, multi-site)", "bullets": [
        "Support all IT functions: enterprise applications (communications, collaboration, EMR, inventory management, human resources, financial management and accounting access), physical servers and virtual machines, network and security/access administration, and information backup, management and protection at over 98% availability.",
        "Daily system monitoring of hardware, server resources, systems and key processes: review logs, verify scheduled backup jobs, apply OS security patches, updates and upgrades, and recover from hardware or software failures with status updates to users.",
        "Guide staff on acceptable AI use under security and data privacy rules; mentor and coach junior ICT on the queue; keep IT resources, vendor relationships and budget inputs current.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kenya (health, multi-site)", "bullets": [
        "Deployed and supported LANs, WANs, network segments, Internet and remote access; installed and rebuilt servers; configured desktops, laptops, Chromebooks, tablets, printers, routers, switches, firewalls, phones, smartphones and software to operational standards.",
        "Created, updated, disabled and deleted user accounts and permissions; ran security monitoring; kept automated daily backups to local, network-attached and offsite cloud storage and verified they completed.",
        "Wrote deployment, installation and configuration procedures; automated repeat admin tasks where possible; trained 80+ staff; coordinated vendors and IT spend as the main ICT point of contact.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Kenya", "bullets": [
        "Supported LAN and WAN, imaging, printers, VoIP and server-room diagnostics; logged tickets and wrote procedures.",
    ]},
],
"certs": "CCNA  |  AZ-900  |  Google IT Support  |  IBM Technical Support  |  GitHub Professional  |  Microsoft Data Analysis",
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: IT Lead/Manager, CURE International, Kijabe",
    "",
    "I am applying for the IT Lead/Manager role at CURE Kenya. For more than three years at PATH I have run ICT for a health organisation: the network, the servers, the endpoints, the EMR, the backups and the people. Availability stayed near 98%. I am CCNA certified, with a BSc in Applied Computing specialised in cybersecurity and digital forensics.",
    "Your duty list is the work. I deploy LAN, WAN, network segments, Internet and remote access. I install and rebuild servers, and I configure desktops, laptops, Chromebooks, tablets, printers, routers, switches, firewalls, phones, smartphones and software. I keep deployment and configuration documentation. I create, update, disable and delete accounts. I monitor hardware, logs and scheduled backup jobs every day, including local, network-attached and offsite cloud copies. When something fails I recover it and I tell the users. I patch. I train the hospital. I coach junior ICT the way an IT Officer would report in. I manage vendors, resources and budget inputs. I will follow CURE International Technology standards, including security, privacy and acceptable AI use.",
    "CURE is a children's surgical hospital. I have already kept clinical systems reachable while a clinician was waiting. I will follow CURE International Technology standards, including security, privacy and acceptable use of approved AI tools. I am available as soon as possible for Kijabe.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


def build_cover_letter(path):
    doc = Document()
    br.set_base_style(doc)
    br.add_name(doc, "MESHACK ARIRI")
    br.add_title(doc, "IT Lead/Manager")
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
