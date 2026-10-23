#!/usr/bin/env python3
"""Recruitment Officer (US Timezone), BruntWork. Remote, independent contractor.
Angle: an IT professional who matches the right technical people to the right clients.
Canonical PATH titles kept. No recruiter, HR, sourcing or ATS titles or claims.
Mentoring result (10 people, two months, 3 started businesses or got jobs) from Meshack 2026-10-08.
Run: python3 "applications/BruntWork Recruitment Officer/build.py"
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb
import prep_pdf

CONTACT = br.CONTACT
COVER_TITLE = "IT Professional  |  Technical Talent Matching  ·  Remote, Manila shift"

cv = {
"headline": ("IT Professional  |  Technical Talent Matching  ·  Skills Assessment  ·  Training and "
             "Onboarding  ·  Remote"),
"metrics": [
    ("80+", "people trained"),
    ("120+", "users supported"),
    ("20+", "requests handled a day"),
    ("~25%", "faster response"),
],
"summary": ("IT professional with 3+ years at PATH, from ICT Intern to ICT Associate to Health Informatics / "
    "HMIS Officer, now using that background to match the right technical people to the right clients. "
    "I know what helpdesk, Microsoft 365, networking, systems and data roles involve day to day, so I can "
    "judge quickly whether someone has real hands-on skill or just a keyword on a CV. I have trained 80+ "
    "people, built onboarding steps that got new staff ready on day one, and mentored young people into "
    "work. I support 120+ users against deadlines, treat confidential data "
    "with care, and am self-managed, target-driven and ready for the Manila shift from Kenya."),
"skills": [
    ("Technical talent matching", "Reading IT job requirements, judging real hands-on depth (helpdesk, Microsoft 365, Active Directory, networking, cloud, data), matching skills, pay and fit to the need"),
    ("People and communication", "Training and coaching (80+ trained), onboarding new staff, mentoring, fluent written and spoken English, Swahili and Dholuo, positive experience for every person"),
    ("Volume and targets", "Multiple open requests at once, deadline and service-level tracking, Freshdesk and Zoho Desk pipelines, Excel and Google Sheets trackers, Asana, LinkedIn, Microsoft 365, Google Workspace"),
    ("Data privacy", "Confidential health data, access control and least privilege, data protection, secure records"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kisumu / Nyamira, Kenya (multi-site)", "bullets": [
        "Support 120+ users and 50+ health facilities across 3–4 counties on KenyaEMR, a Ministry of Health national system, keeping critical systems above 98% uptime.",
        "Trained 80+ health workers across 15+ sessions; judge each group's level first, then adjust the session so people actually use the tools afterwards.",
        "Work daily with county teams, facility managers and national teams: weekly and monthly progress updates, meeting minutes and follow-up on every action point.",
        "Handle confidential patient data under strict privacy rules: access controls, secure backups and least-privilege accounts.",
        "Plan schedules and trackers across 50+ sites and meet fixed national reporting deadlines; cut reporting time by about 40% with automated checks and Power BI.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya (multi-site)", "bullets": [
        "Handled about 20 support requests a week from 120+ users in Freshdesk and Zoho Desk, prioritised against service levels, and improved response time by about 25%.",
        "Built onboarding and offboarding steps (Active Directory accounts, devices, Microsoft 365 access, SOPs) so new staff were productive on day one.",
        "Ran vendor and ISP evaluations: gathered requirements, compared each option against need and cost, and recommended the best fit for leadership sign-off.",
        "Mentored young people and trained ICT hubs; ran a two-month self-awareness programme for 10 people, 3 of whom went on to start businesses or secure jobs.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Homa Bay, Kenya", "bullets": [
        "Supported networks, printers and VoIP phones; logged and tracked requests in Freshdesk against service levels; contributed to IT audits.",
    ]},
],
"certs": ("Google IT Support  |  IBM Technical Support  |  Microsoft Data Analysis  |  "
          "Microsoft Azure Fundamentals (AZ-900)  |  DHIS2 Academy"),
"compact_education": True,
"show_referees": False,
}

COVER_BODY = [
    "The Recruitment Team",
    "BruntWork",
    "",
    "Re: Recruitment Officer (US Timezone), remote",
    "",
    "Dear BruntWork Recruitment Team,",
    "",
    "I am applying for the Recruitment Officer role. I have spent more than three years in IT at PATH, "
    "growing from ICT Intern to ICT Associate to Health Informatics / HMIS Officer, and I want to use that "
    "background to match the right technical people with the right clients.",
    "",
    "BruntWork fills many IT roles: helpdesk, Microsoft 365, networks, systems support and data. I have done "
    "that work, so I know what each job really asks for. In a screening call I can tell quickly whether a "
    "candidate truly knows Active Directory or a network, or has only listed it. That means sharper "
    "shortlists, fewer bad hires and happier clients.",
    "",
    "Sourcing and screening sit in the same family as work I already do every week. I gather requirements, "
    "compare options against need and cost, and recommend the best fit. I built the onboarding steps that "
    "got new staff ready on day one, and I have trained more than 80 people, so I spot quickly who learns "
    "fast and who copes under pressure. I also mentored ten young people through a two-month programme; "
    "three went on to start businesses or secure jobs.",
    "",
    "Volume and targets suit me. I support 120+ users against service levels, improved response "
    "time by about 25%, and keep many pieces of work moving at once with clear trackers. I work with "
    "confidential patient data every day, so data privacy is already a habit. I care about the person on "
    "the other side of the call, and every candidate I speak to will know where they stand.",
    "",
    "I work well on my own, write and speak clear English, and I am ready for the Manila shift from Kenya. "
    "I look forward to the Recruiter Assessment.",
    "",
    "Yours faithfully,",
    "Meshack Ariri",
]


if __name__ == "__main__":
    files = br.pack_files(HERE)
    br.build(cv, files["cv_docx"])
    br.build_cover(COVER_BODY, COVER_TITLE, files["cover_docx"], CONTACT)
    br.build_application(cv, COVER_BODY, COVER_TITLE, files["combined_docx"], CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], CONTACT, COVER_TITLE)
    pb.build_application_pdf(cv, COVER_BODY, files["combined_pdf"], CONTACT, COVER_TITLE)
    prep_pdf.build_prep_pdf(os.path.join(HERE, "Interview_Prep.md"),
                            os.path.join(HERE, "Interview Prep.pdf"),
                            "Meshack Ariri  ·  BruntWork Recruitment Officer  ·  Interview prep")
    prep_pdf.build_prep_pdf(os.path.join(HERE, "Interview_Quick_Guide.md"),
                            os.path.join(HERE, "BruntWork Interview Quick Guide.pdf"),
                            "Meshack Ariri  ·  BruntWork Recruitment Officer", toc=True,
                            subtitle="Recruitment Officer (US Timezone)  ·  Meshack Ariri")
    print("Generated:", HERE)
