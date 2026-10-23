#!/usr/bin/env python3
"""Digital Health Systems Strengthening Officer, Living Goods. Kenya, contract.
Resume only on JazzHR. Deadline 23 Oct 2026, rolling.
Do not claim eCHIS, Community Health Toolkit, or that he chaired a county steering committee.
KenyaEMR and DHIS2 are the government systems. Travel: Kisumu base, Vihiga and Kakamega.
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
    "headline": "Digital Health Officer  |  County support  ·  KenyaEMR  ·  DHIS2  ·  Devices",
    "metrics": [
        ("50+", "facilities supported"),
        ("80+", "health staff trained"),
        ("~40%", "faster reporting"),
        ("3–4", "counties"),
    ],
    "summary": (
        "Digital health officer with three years at PATH supporting Ministry of Health systems across 50+ facilities "
        "in 3–4 counties. I train facility teams and ICT officers on KenyaEMR and DHIS2, write the job aids, and "
        "keep data quality and late sync visible with SQL checks and dashboards. I follow an incident through to "
        "a written root cause, keep the device record, and send weekly and monthly progress to managers and county "
        "teams. Based in Kisumu. Ready to travel in Vihiga, Kakamega and assigned counties."
    ),
    "skills": [
        ("Digital health", "KenyaEMR/TaifaCare, DHIS2, NDWH, facility-to-national reporting, Kobo and tablet data collection, interoperability"),
        ("Capacity building", "Training, coaching, job aids, SOPs, troubleshooting guides, peer sessions, meeting notes and follow-up"),
        ("Data for decisions", "Data quality reviews, SQL validation, Power BI, Grafana, sync and reporting timeliness, weekly and monthly reports"),
        ("Continuity and devices", "Incident logs, problem follow-up, root cause sessions, controlled rollout support, asset register, tablet and phone lifecycle, escalation to vendors"),
    ],
    "experience": [
        {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
         "loc": "Kisumu and Nyamira", "bullets": [
            "Support KenyaEMR and DHIS2 at government facilities, holding clinical systems at about 98% uptime, and train facility staff, ICT officers and programme teams on modules, data quality and secure use.",
            "Run SQL data-quality checks and Power BI and Grafana dashboards that cut reporting time by about 40%, and move facility data to national systems through NDWH so reports are not waiting on a late sync.",
            "Send weekly and monthly written updates to managers and county teams: progress, open issues, and the capacity-building done that period.",
            "Log interruptions, restore the service, and write the root cause. Repeat faults become a job aid or a fix in the next update, so the same outage does not return.",
        ]},
        {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
         "loc": "Kisumu, Kenya", "bullets": [
            "Rolled out KenyaEMR, a Ministry of Health system, at facilities across 3–4 counties: the schedule, the per-facility tracker, equipment, and contractor sign-off.",
            "Set up and tracked tablets, phones and clinic devices, trained users to fix the basic fault, and escalated repairs and replacements. 80+ health workers trained across 15+ sessions.",
            "Wrote troubleshooting guides and sat with county and facility teams on rollout issues until the action points were closed.",
        ]},
        {"org": "PATH", "title": "ECD Programme MIS and ICT Support", "dates": "2024 to 2025",
         "loc": "Remote", "bullets": [
            "Remote first line for field staff on tablets, Kobo forms, logins and sync, so data was available for reporting, plus remote onboarding of new users.",
        ]},
    ],
    "certs": "DHIS2 Academy  |  Microsoft Azure Fundamentals (AZ-900)  |  Google IT Support  |  CCNA",
    "compact_education": True,
    "show_referees": False,
}

COVER_BODY = [
    "Dear Hiring Team,",
    "",
    "Re: Digital Health Systems Strengthening Officer, Kenya",
    "",
    "I am applying for the Digital Health Systems Strengthening Officer role. For three years at PATH I have supported Ministry of Health systems at the facilities where care is delivered: KenyaEMR and DHIS2 across 50+ sites in 3–4 counties, with uptime around 98%. I train the people who use them, write the job aid, and send weekly and monthly progress to managers and county teams.",
    "The work you describe is the work I want to spend more of my time on. I already review data quality, watch for late sync, and put the gap on a dashboard managers can use. I already keep an incident log, sit on the root cause, and turn a repeat fault into a guide. I already track devices, train the basic fix, and escalate the rest. On the Early Childhood programme I was the remote line for field staff whose tablets and forms had stopped syncing.",
    "I am based in Kisumu, I drive, and I can travel regularly in Vihiga, Kakamega and other assigned counties. I hold a BSc in Applied Computing and a DHIS2 Academy certificate. I want this role because the point of the support is that the county team can keep the system up after the session.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


if __name__ == "__main__":
    files = br.pack_files(HERE)
    br.build(cv, files["cv_docx"])
    br.build_cover(COVER_BODY, "Digital Health Systems Strengthening Officer", files["cover_docx"], br.CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], br.CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], br.CONTACT, "Digital Health Systems Strengthening Officer")
    print("Generated:", HERE)
