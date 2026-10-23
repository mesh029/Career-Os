#!/usr/bin/env python3
"""Senior Officer, IT, AIM (Kisii / Kakamega), BRAC International. Trakstar Hire form.
Close 9 Oct 2026. Separate uploads: CV and cover letter. "Resume including all job assignments in detail."
Do not claim BInsight, sbiCloud or Orbit use, or macOS administration.
ECD = closed 2024 to 2025 workstream, never Nuru ya Mtoto. Salesforce = tickets, not tenant admin.
Second BRAC application (TSO-MIS Officer, AIM, Nairobi is the first). Keep facts identical.
Run: python3 "applications/BRAC International Senior Officer IT AIM Kisii Kakamega/build.py"
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT = br.CONTACT
COVER_TITLE = "Senior Officer, IT, AIM  |  Kisii / Kakamega"

cv = {
"headline": "Senior Officer, IT  |  Field IT and Application Support  ·  Networks  ·  Endpoints  ·  Jira  |  INGO",
"metrics": [
    ("3+ yrs", "INGO field IT"),
    ("120+", "users, multi-site"),
    ("~98%", "uptime"),
    ("80+", "staff trained in person"),
],
"summary": ("Field IT and application support officer with 3+ years at PATH, an international NGO, supporting "
    "regional offices, health facilities and programme teams across western Kenya. I give first-line support "
    "for business and programme applications (KenyaEMR, DHIS2, Salesforce, Microsoft 365, Kobo), troubleshoot "
    "configuration and application errors on site, and escalate what I cannot fix through Jira with clear "
    "root-cause notes. I run routers, switches and access points, set up and secure laptops, printers and "
    "scanners, keep every ticket documented, and train users in person. Field ICT for OVC and DREAMS (AGYW) "
    "teams and youth ICT hubs. Based in Kisumu, next to Kisii and Kakamega, and ready to travel extensively."),
"skills": [
    ("Application support", "First-line support, configuration and error handling for KenyaEMR/TaifaCare (OpenMRS), DHIS2, Salesforce (user side), Microsoft 365, Kobo Toolbox; triage and root-cause analysis; Jira Service Management, Freshdesk, Zoho Desk; knowledge base"),
    ("Networks", "TCP/IP, LAN/WAN, DNS, DHCP, VLANs, VPN, Wi-Fi; routers, switches, access points and firewalls (Cisco Meraki, MikroTik, Fortinet FortiGate); connectivity diagnosis with ISPs"),
    ("Endpoints and security", "Windows 10/11, Linux (Ubuntu), laptops, desktops, printers, scanners, imaging (PXE); endpoint protection, antivirus, patch management, MFA, least-privilege access"),
    ("Cloud and governance", "Microsoft 365, Active Directory / Entra ID, Azure (AZ-900); data protection and access control (Kenya Data Protection Act awareness); IT policies, SOPs and audits; technology adoption"),
    ("Field and people", "In-person training (80+ staff), onboarding, job aids; liaison between field, programme and IT; extensive travel; English, Swahili, Dholuo"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kisumu/Nyamira, Kenya", "bullets": [
        "Provide first-line and on-site support for KenyaEMR/TaifaCare and DHIS2 across health facilities at over 98% uptime: application errors, configuration, user access and data issues.",
        "Triage problems that cannot be fixed on site and escalate them to national and head-office technical teams with documented steps and root cause, then follow through to closure.",
        "Maintain the Windows and Linux servers that host these systems: backups, encryption, patching and disaster recovery.",
        "Run system audits, data-flow reviews and access checks against national standards; enforce secure use and access policies at facility level.",
        "Train facility staff, ICT officers and programme teams in person on system modules, data quality and secure use; write SOPs and job aids.",
    ]},
    {"org": "PATH", "title": "ECD Programme MIS and ICT", "dates": "2024 to 2025",
     "loc": "Kenya  |  programme closed 2025", "bullets": [
        "Ran digital and manual MIS and field ICT for the ECD programme: tested forms before go-live, onboarded and trained field staff, supported devices and data tools, and kept backups until close-out.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya (multi-site)", "bullets": [
        "Delivered first and second line support to 120+ users across offices and field sites at about 98% uptime; logged, tracked and escalated every issue in Freshdesk, Zoho Desk and Jira Service Management under ITIL/SLA, improving response time about 25%.",
        "Configured and monitored Cisco Meraki access points, switches and security appliances; diagnosed and fixed LAN/WAN, VPN, DNS, DHCP and Wi-Fi problems across sites.",
        "Installed, configured and maintained laptops, desktops, printers and VoIP phones; rolled out endpoint protection, patching and MFA.",
        "Provisioned Active Directory and Microsoft 365 accounts and handled technical onboarding for new staff at their location.",
        "Served as the field ICT person for OVC and DREAMS (AGYW) teams: devices, connectivity, data tools and reporting so mentors and case workers could submit on time.",
        "Mentored youth and trained community ICT hubs; resolved Salesforce tickets (login, access, forms, reports); wrote knowledge-base articles.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Homa Bay, Kenya", "bullets": [
        "Supported LAN/WAN, routers, switches and cabling; deployed printers, VoIP phones and desktop images (PXE); logged Freshdesk tickets under SLA; assisted facility system deployment and IT audits.",
    ]},
    {"org": "Indoor Residual Spraying (IRS) Campaign", "title": "IT Assistant", "dates": "2023  |  one campaign",
     "loc": "Homa Bay County, Kenya", "bullets": [
        "Field IT support for spray teams on ODK / Kobo Collect: forms on devices, daily submissions and sync problems fixed on site.",
    ]},
],
"certs": ("CCNA  |  Microsoft Azure Fundamentals (AZ-900)  |  Google IT Support  |  "
          "IBM Technical Support  |  Microsoft Data Analysis  |  DHIS2 Academy certificate"),
"compact_education": True,
"languages": "English (fluent)  ·  Swahili (fluent)  ·  Dholuo (fluent)",
"referees": [
    "Patrick Ondieki, ICT Officer, PATH  |  pondieki@path.org",
    "Marvin Ngosa, Systems Administrator, PATH  |  mngosa@path.org",
    "Gadaffi Ochieng, Procurement Officer, Ampath  |  ochienggadaffi@gmail.com",
],
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: Senior Officer, IT, AIM (Kisii / Kakamega)",
    "",
    "I am applying for the Senior Officer, IT role on AIM in Kisii and Kakamega. For more than three years at "
    "PATH, an international NGO, I have been the IT person for offices, health facilities and programme teams "
    "across western Kenya. I live in Kisumu and work in Nyamira, next door to Kisii, so this region and its "
    "roads are already my workplace.",
    "",
    "The job you describe is the one I do. I give first-line support for the applications people depend on, "
    "KenyaEMR, DHIS2, Salesforce, Microsoft 365 and Kobo, and I sort out configuration and application errors on "
    "site. What I cannot fix I escalate with the steps I took and the likely root cause, and Jira Service "
    "Management is already part of how I log and escalate. I manage Meraki routers, switches and access points, "
    "set up and secure laptops, printers and scanners with endpoint protection and patching, and record every "
    "issue and fix in the ticketing system and knowledge base.",
    "",
    "Most of my best work has been in person. I have trained more than 80 staff at their desks, onboarded new "
    "users where they work, and written the job aids they keep. As the field ICT person for OVC and DREAMS, I "
    "worked with mentors serving adolescent girls and young women, and I mentored youth and trained community "
    "ICT hubs. I know what it takes for a field team to trust a new system.",
    "",
    "BInsight, sbiCloud and Orbit sit in the same family as the systems I support every day: field data "
    "platforms, cloud business applications and programme MIS. I get productive on an application the way I did "
    "on KenyaEMR and DHIS2: alongside the users, with the documentation open, and with an escalation path I respect. I hold CCNA "
    "and Azure Fundamentals (AZ-900) and a BSc in Applied Computing. I am ready to be based in Kisii or "
    "Kakamega and to travel extensively across the branches.",
    "",
    "Thank you for considering my application.",
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
