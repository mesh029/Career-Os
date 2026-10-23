"""BruntWork Recruitment Officer: screening-call questions, dark PDF.

Run: python3 interview_screening_pdf.py [output.pdf]
Default output: ~/Desktop/INTERVIEW /BruntWork Screening Questions.pdf
"""

import sys
from pathlib import Path

from interview_guide_pdf import build

SECTIONS = [
    {
        "title": "BruntWork and This Role",
        "qs": [
            ("Where did you hear about BruntWork?", [
                "I came across BruntWork on <b>[say where you actually saw it: "
                "LinkedIn, your careers page, a friend]</b>.",
                "What made me look closer is what you do. You connect talent to "
                "clients worldwide and fill many technical roles, and you give "
                "skilled people in places like Kenya a real shot at global jobs. "
                "When I saw the Recruitment Officer role, it fit my IT background "
                "straight away.",
                "~ Keep the channel honest and short, then move to why it caught "
                "your attention.",
            ]),
            ("Why are you interested in this specific role?", [
                "Because it brings together two things I love:",
                "- <b>From IT:</b> I know what a good technical hire looks like. I "
                "can tell if a candidate really knows Active Directory or just "
                "listed it.",
                "- <b>From training 80+ people:</b> I've seen how much the right "
                "chance changes someone.",
                "The part of IT I enjoy most is the people part: training, "
                "onboarding, mentoring. In this role I do that every day, and I put "
                "the right technical people in the right seats.",
                "> \"When I mentored 10 young people, 3 started businesses or got "
                "jobs. That's the feeling I want every time a placement lands.\"",
            ]),
        ],
    },
    {
        "title": "Your Experience and Track Record",
        "qs": [
            ("Tell us about your last position. What were your responsibilities?", [
                "I'm a <b>Health Informatics / HMIS Officer at PATH</b> (Mar 2025 to "
                "now). Before that I was ICT Associate and ICT Intern, so about 3 "
                "years at PATH in total.",
                "<b>Current role</b>",
                "- Keep KenyaEMR and DHIS2 running across 50+ health facilities, "
                "above 98% uptime.",
                "- Check data quality with SQL validation. My automation cut "
                "reporting time by about 40%.",
                "- Build Power BI dashboards and monthly reports for programme and "
                "leadership teams.",
                "- Train facility staff and ICT officers, and write SOPs and job "
                "aids.",
                "<b>As ICT Associate</b>",
                "- 1st and 2nd line support for 120+ users, about 20 tickets a week, "
                "logged in Freshdesk and Zoho Desk against SLAs.",
                "- Microsoft 365, Active Directory accounts and access, networking.",
                "- Onboarding and training new users.",
                "> \"What ties it together is people, volume and deadlines. That's "
                "what I bring to recruitment.\"",
            ]),
            ("Have you worked with targets? (We work with targets at BruntWork.)", [
                "Yes. Targets have been part of every role at PATH, and they keep me "
                "sharp.",
                "- <b>Uptime:</b> kept systems above 98% uptime for 120+ users.",
                "- <b>Volume and SLAs:</b> 120+ users, about 20 tickets a week, each logged and closed "
                "on time. Response time improved by about 25%.",
                "- <b>Deadlines:</b> monthly national reporting, and the KenyaEMR "
                "go-live date: 80+ users trained across 15+ sessions, on time.",
                "<b>How I'd work your targets</b>",
                "- Work backwards from the monthly number. If the target is 10 "
                "hires, I know how many submissions, screens and sourced candidates "
                "I need each week.",
                "- One tracker ranked by urgency. Every role gets a touch daily.",
                "- Halfway through the month, check the funnel for the leak and fix "
                "that stage.",
                "> \"I'm happy to be measured on results.\"",
            ]),
            ("Your roles look short. Is there a reason? Do you want to grow?", [
                "On paper the dates look short, but it's one employer: about 3 years "
                "at PATH. Each change was a step up, not a move away.",
                "- <b>ICT Intern</b> (Apr to Dec 2023): a fixed-term internship.",
                "- <b>ICT Associate</b> (Jan 2024 to Mar 2025): taken on straight "
                "after the internship.",
                "- <b>Health Informatics / HMIS Officer</b> (Mar 2025 to now): moved "
                "up into data and systems.",
                "- The <b>IRS campaign</b> IT Assistant role (2023) was a 2-month "
                "campaign contract by design.",
                "Yes, I want to grow. I grow by taking on more each time, inside the "
                "same organisation when I can. That's what I want here:",
                "> \"By Month 3, running my own pipelines and hitting my first full "
                "target. In two years, your go-to recruiter for technical roles, "
                "helping train new recruiters.\"",
            ]),
        ],
    },
]


if __name__ == "__main__":
    default = (Path.home() / "Desktop" / "INTERVIEW "
               / "BruntWork Screening Questions.pdf")
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else default
    build(out, SECTIONS, title="BruntWork Screening Questions", compact=True)
    print(out)
