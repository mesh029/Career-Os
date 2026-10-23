#!/usr/bin/env python3
"""Client Intake & Care Support Coordinator, Seamless Assist (US home care agency client).
Part-time 20 h/week, remote, US Eastern business hours, USD 4-6/hour.
Healthcare-adjacent positioning: PATH health facilities, OVC / DREAMS caregiving programmes.
Do not claim Spanish, geriatric or cardiology experience, HIPAA certification, or invoicing ownership.
CRM = setup support for small businesses (HubSpot/Salesforce concepts) and Salesforce user tickets.
Run: python3 "applications/Seamless Assist Client Intake Care Support Coordinator/build.py"
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT = br.CONTACT
COVER_TITLE = "Client Intake & Care Support Coordinator  |  Remote, US Eastern hours"

cv = {
"headline": "Client Intake and Care Support Coordinator  |  Healthcare Settings  ·  Fast Follow-up  ·  Scheduling  ·  Health-Data Privacy",
"metrics": [
    ("3+ yrs", "healthcare settings"),
    ("20+", "requests handled daily"),
    ("~25%", "faster response"),
    ("80+", "health workers trained"),
],
"summary": ("Healthcare-adjacent support coordinator with 3+ years at PATH, an international health "
    "organisation, working every day with clinicians, facility staff, case workers and programme teams. I "
    "answer people quickly and warmly by phone, email and message, log every contact, and follow up until it is "
    "closed. I keep calendars, trackers and records accurate, run recurring reports on schedule, and handle "
    "confidential health information inside secure, access-controlled systems. Clear written and spoken English, "
    "a calm phone manner, and available for US Eastern business hours."),
"skills": [
    ("Intake and follow-up", "Phone, email and message response; structured follow-up until closed; queue and contact logging (Freshdesk, Zoho Desk, Jira); CRM (Salesforce user side, HubSpot setup for small businesses)"),
    ("Scheduling and records", "Calendars and bookings in Outlook / Microsoft 365 and Google Workspace; Excel and Google Sheets trackers; accurate, organised records"),
    ("Billing and compliance support", "Recurring monthly reporting on deadline; renewal tracking; online payment collection setup (Paystack, M-Pesa); audit-ready documentation"),
    ("Privacy and care", "Confidential health information, access control, MFA, data-protection practice; patient, empathetic communication with families, caregivers and non-technical users"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kenya (health facilities)", "bullets": [
        "First point of contact for clinicians and facility staff by phone and in person when records or systems go wrong; respond fast, stay calm, and follow up until each issue is closed.",
        "Keep patient-related health records accurate and confidential in secure, access-controlled systems (KenyaEMR, DHIS2) under data-protection rules.",
        "Run recurring monthly reporting to national systems on schedule, with accuracy checks that cut reporting time about 40%.",
        "Schedule and deliver training for health workers; write simple guides they keep using.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya", "bullets": [
        "Handled about 20 requests a week by phone, email and ticket for 120+ staff; responded quickly, kept notes on every contact, and followed up until closed, improving response time about 25%.",
        "Supported OVC case workers and DREAMS mentors who serve vulnerable children, families and young women, keeping their devices, data tools and records working so they could submit on time.",
        "Onboarded new staff, managed accounts and access, and resolved Salesforce user tickets (login, forms, reports).",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Homa Bay, Kenya", "bullets": [
        "Logged and tracked support requests under service-level targets and kept process documentation up to date.",
    ]},
],
"projects": [
    {"title": "Small-business admin systems (independent, project-based)", "dates": "2023 to Present",
     "org": "Small business clients", "bullets": [
        "Set up Microsoft 365, Zoho and Google Workspace, supported CRM setup, and configured online payment collection (Paystack, including M-Pesa) so clients could book, follow up and get paid.",
    ]},
],
"certs": ("Google IT Support  |  IBM Technical Support  |  Microsoft Data Analysis  |  "
          "DHIS2 Academy certificate  |  Microsoft Azure Fundamentals (AZ-900)"),
"compact_education": True,
"show_referees": False,
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: Client Intake & Care Support Coordinator",
    "",
    "I am applying for the Client Intake & Care Support Coordinator role. For more than three years I have worked "
    "in healthcare settings with PATH, an international health organisation, and a big part of every day has "
    "been the work you describe: answering people quickly and kindly, keeping track of every request, following "
    "up until it is done, and keeping the records and reports behind it accurate.",
    "",
    "Most of the people I support are clinicians, facility staff and case workers, often under pressure. I have "
    "handled around twenty requests a week by phone, email and ticket, logged every contact, and followed up "
    "until each one was closed, which cut our response time by about a quarter. I worked alongside case workers "
    "and mentors who care for vulnerable children and families, so I understand that the person on the other end "
    "is often making a hard decision and needs patience, not a script.",
    "",
    "Behind the scenes I am at home with detail-heavy, recurring work: calendars, trackers, monthly reports that "
    "go out on deadline, and confidential health information handled inside secure, access-controlled systems. I "
    "write my own messages and do my own work without AI tools, and I follow privacy rules strictly. I am "
    "available for US Eastern business hours, including late morning through early evening.",
    "",
    "Thank you for considering my application. I would be glad to talk.",
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
