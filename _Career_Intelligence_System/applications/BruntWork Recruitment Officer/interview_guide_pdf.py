"""BruntWork Recruitment Officer: clickable one-stop interview prep PDF.

Run: python3 interview_guide_pdf.py [output.pdf]
Default output: ~/Desktop/INTERVIEW /BruntWork Quick Prep.pdf
"""

import sys
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, CondPageBreak, Frame, FrameBreak, KeepTogether,
    NextPageTemplate, PageBreak, PageTemplate, Paragraph, Spacer, Table,
    TableStyle,
)
from reportlab.platypus.flowables import HRFlowable

BG = HexColor("#0B1424")
HEAD_HEX = "#F4EDE4"
ACCENT_HEX = "#E8834A"
TEXT_HEX = "#D9E0EA"
HEAD = HexColor(HEAD_HEX)
ACCENT = HexColor(ACCENT_HEX)
CARD = HexColor("#15233A")
TEXT = HexColor(TEXT_HEX)
MUTED = HexColor("#93A2B8")
LINE = HexColor("#26364F")
GREEN = "#6FCF97"
GREY = "#8C97A6"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation2")
for name, file in [
    ("Sans", "LiberationSans-Regular.ttf"),
    ("Sans-B", "LiberationSans-Bold.ttf"),
    ("Sans-I", "LiberationSans-Italic.ttf"),
    ("Sans-BI", "LiberationSans-BoldItalic.ttf"),
    ("Serif-B", "LiberationSerif-Bold.ttf"),
]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / file)))
pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="Sans-B",
                              italic="Sans-I", boldItalic="Sans-BI")

PAGE_W, PAGE_H = A4
MARGIN = 48
BODY_W = PAGE_W - 2 * MARGIN


def style(name, **kw):
    base = dict(fontName="Sans", fontSize=10, leading=14.2, textColor=TEXT,
                alignment=TA_LEFT)
    base.update(kw)
    return ParagraphStyle(name, **base)


S = {
    "kicker": style("kicker", fontName="Sans-B", fontSize=8.5, textColor=ACCENT,
                    leading=11),
    "title": style("title", fontName="Serif-B", fontSize=30, leading=34,
                   textColor=HEAD),
    "sub": style("sub", fontSize=10, leading=14, textColor=MUTED),
    "toc_sec": style("toc_sec", fontName="Sans-B", fontSize=8.2, leading=10.4,
                     textColor=ACCENT, spaceBefore=7, spaceAfter=2),
    "toc_q": style("toc_q", fontSize=8.3, leading=10.5, leftIndent=16,
                   firstLineIndent=-16, spaceAfter=0.8),
    "sec_num": style("sec_num", fontName="Serif-B", fontSize=34, leading=34,
                     textColor=ACCENT),
    "sec_title": style("sec_title", fontName="Serif-B", fontSize=19, leading=22,
                       textColor=HEAD),
    "q": style("q", fontName="Sans-B", fontSize=11.4, leading=15,
               textColor=HEAD, spaceBefore=11, spaceAfter=5),
    "a": style("a", fontSize=9.9, leading=14.2),
    "bullet": style("bullet", fontSize=9.9, leading=14.2, leftIndent=12,
                    firstLineIndent=-10),
    "note": style("note", fontName="Sans-I", fontSize=9.2, leading=13,
                  textColor=MUTED),
    "say": style("say", fontName="Sans-I", fontSize=10.2, leading=14.6,
                 textColor=HEAD),
    "strip_letter": style("strip_letter", fontName="Serif-B", fontSize=20,
                          leading=22, textColor=ACCENT),
    "strip_label": style("strip_label", fontName="Sans-B", fontSize=9.2,
                         leading=12, textColor=HEAD),
    "strip_desc": style("strip_desc", fontSize=8.6, leading=11.4,
                        textColor=TEXT),
    "intro": style("intro", fontSize=9.8, leading=14, textColor=MUTED,
                   spaceAfter=6),
}

# ---------------------------------------------------------------------------
# Content. Each question: (question, [blocks], optional tag).
# Block prefixes: "- " bullet, "~ " muted note, "> " spoken line.
# ---------------------------------------------------------------------------

SECTIONS = [
    {
        "title": "Challenges I May Face in This Role",
        "qs": [
            ("What challenges do you expect in this role?", [
                "Three, and I have a plan for each:",
                "- <b>1. No formal HR background.</b> Risk: focusing too much on "
                "technical skills. <b>Fix:</b> follow the BruntWork scorecard "
                "strictly in Month 1.",
                "- <b>2. Finding the right people fast, under targets.</b> Good "
                "candidates don't wait. <b>Fix:</b> keep a warm pipeline per role, "
                "reply fast, always have 2-3 backups.",
                "- <b>3. Time zone.</b> Shift is 4PM-1AM Kenya time. <b>Fix:</b> "
                "calendar blocks, clear handover notes, internet and power backup.",
            ]),
            ("What would you change in your last job?", [
                "More flexibility in working across different time zones.",
            ]),
        ],
    },
    {
        "title": "Clients: Unrealistic Timelines and Budgets",
        "intro": "A hot question for BruntWork. They want to see you can say NO "
                 "professionally and still keep the client.",
        "strip": [
            ("1", "ACKNOWLEDGE", "Don't argue. Show you heard the urgency and the budget."),
            ("2", "SHOW DATA", "Market data, not opinion. Time to fill and pay rates."),
            ("3", "GIVE OPTIONS", "Trade-offs, not a dead end. Let the client choose."),
        ],
        "qs": [
            ("How do you handle a client with an unrealistic timeline or budget?", [
                "I handle it in 3 steps: <b>Acknowledge, Show Data, Give Options.</b>",
                "<b>1. Acknowledge, don't argue</b>",
                "> \"I understand you need this urgently and you have a tight budget.\"",
                "<b>2. Show data, not opinion</b>",
                "- <b>Timeline:</b> \"For this kind of IT Support role, our average "
                "time to fill is 12-15 days. If we need it in 5 days, we will need "
                "to move faster on feedback.\"",
                "- <b>Budget:</b> \"For M365 + Active Directory skills in this "
                "market, candidates are asking $800-$1,000. At $500, we are getting "
                "90% rejections at screening.\"",
                "<b>3. Give options, not a dead end</b>",
                "- <b>Option A:</b> Keep budget/timeline but widen the search: "
                "similar titles, adjacent skills, or one-step-below who can grow.",
                "- <b>Option B:</b> Keep the exact profile but adjust budget/timeline: "
                "even $100 more opens 30% more candidates.",
                "- <b>Option C:</b> Split the role: a strong junior now to cover "
                "urgent work, while we search for the senior.",
                "Then I ask:",
                "> \"Which trade-off works best for you?\"",
            ]),
            ("Why does this approach work?", [
                "- I never say \"your budget is unrealistic\". I show market data.",
                "- I give the client control: options, not a NO.",
                "- I protect candidate experience: I don't bring candidates to a "
                "role that will waste their time.",
            ]),
            ("Closing line", [
                "> \"My job is not to say yes to everything. My job is to give the "
                "client a clear picture of what their timeline and budget will buy "
                "in the real market, so they can decide fast.\"",
            ]),
        ],
    },
    {
        "title": "Technical Questions in Plain Language",
        "intro": "Use the MAMA framework whenever you explain something technical.",
        "strip": [
            ("M", "MAKE IT HUMAN", "Talk about who was affected, not the system."),
            ("A", "ANALOGY", "Link it to something they already know."),
            ("M", "MAKE IT PLAIN", "No jargon. Explain it like they are new to the field."),
            ("A", "AFTER vs BEFORE", "Show the actual change: before it was this, now it's that."),
        ],
        "qs": [
            ("What was your greatest challenge? (KenyaEMR onboarding)", [
                "Onboarding 80+ staff onto KenyaEMR in a short time, with no extra hires.",
                "<b>M - Human:</b> 80+ nurses and clerks across 50 clinics. Busy, "
                "short-staffed, and on paper for 15 years.",
                "<b>A - Analogy:</b> Like asking 50 mama mboga shops to stop using "
                "notebooks and use a phone app in 2 weeks.",
                "<b>M - Plain:</b> Tight deadline, no extra staff, so I couldn't "
                "train everyone. I quickly found the right 1-2 fast learners per "
                "facility: people others respect, who handle pressure when the power "
                "goes off. Short calls, then I watched them in their first training.",
                "<b>A - Before vs After:</b> Before: staff stayed till 6pm writing, "
                "and files got lost. After: 80+ users onboarded across 15+ sessions, "
                "daily use started immediately, we hit the go-live date, and clinics "
                "close early with safe records.",
            ]),
            ("Why move from IT to recruitment now?", [
                "I love the people part of IT the most: training, onboarding, "
                "helping someone solve a problem. In recruitment I can do that every "
                "day, and my IT background helps because I understand the technical "
                "roles I'm hiring for. I can tell if a candidate really knows the "
                "work or just wrote it on the CV.",
            ]),
            ("How will your technical knowledge make you a better recruiter?", [
                "A non-technical recruiter checks keywords. I check if it's real. I "
                "can ask \"walk me through how you fixed a network outage\" and know "
                "if the answer is fake. I know the tools (M365, Active Directory, "
                "SQL, Python), so I won't waste the hiring manager's time with "
                "unqualified CVs.",
            ]),
            ("How would you use automation and an ATS?", [
                "To reduce manual work. I use filters and rules in the ATS to tag "
                "CVs, send automatic updates so candidates don't ghost, and keep a "
                "clean tracker in Sheets so I see where each role is leaking. Less "
                "admin, more time talking to good candidates.",
            ]),
            ("How does your SLA experience at PATH help candidate experience?", [
                "In helpdesk, every ticket needs a fast, clear reply or people get "
                "angry. Candidates are the same. I reply fast, tell them where they "
                "are in the process, and never leave them silent.",
                "> My target at PATH was 98% uptime. My target in recruitment: 100% "
                "of candidates know their status.",
            ]),
            ("Walk us through how you trained 80+ staff.", [
                "The biggest challenge was the short time. I couldn't train everyone, "
                "so I found the right fast learners per facility, the ones others "
                "respect. I trained them well with simple one-page guides and "
                "WhatsApp support, and they trained their teams.",
                "> Same in recruitment: find the right person fast, onboard them "
                "well, and stay close in Week 1 so they don't drop off.",
            ]),
            ("How do you explain a technical issue to a non-technical manager?", [
                "Example: the system was down because the internet box lost power. "
                "Like home WiFi when KPLC goes. I added a small backup battery, like "
                "a power bank for the router, and trained one person to restart it.",
                "<b>Before:</b> they waited 2 days for me. <b>After:</b> back in 5 "
                "minutes.",
                "> For hiring managers, I translate a technical profile into business "
                "value: how this skill solves the team's problem now.",
            ]),
        ],
    },
    {
        "title": "General: About You",
        "qs": [
            ("Tell me about yourself. (60 seconds)", [
                "I'm Meshack. 3 years in IT at PATH, from Intern to Associate to "
                "health informatics: helpdesk, networking, M365 and data. I've "
                "trained 80+ people and support 120+ users. Now I want to use "
                "my technical knowledge to match the right technical people to the "
                "right clients. Outside work I play chess. It taught me to think a "
                "few moves ahead.",
            ]),
            ("Why recruitment, coming from IT?", [
                "The people part of IT is what I enjoy most: training, onboarding "
                "and mentoring.",
            ]),
            ("Why hire you over experienced recruiters?", [
                "Many clients hire technical people, and I can screen them properly "
                "from Day 1. I bring people skills from training 80+ staff, "
                "discipline from supporting 120+ users, and hunger to prove myself on "
                "targets.",
            ]),
            ("What are your strengths?", [
                "- I understand technical roles.",
                "- I read people well. Training taught me who learns fast.",
                "- I stay organised under volume.",
            ]),
            ("What is your weakness?", [
                "I used to find it hard to say no, so my workload piled up. Now I "
                "check my load first and set a clear expectation:",
                "> \"I can have it by Thursday\", not an automatic yes.",
            ]),
            ("Why BruntWork? What excites you about this role?", [
                "You connect talent worldwide and fill many technical roles, which is "
                "where I add the most. You give skilled people in Kenya a global "
                "shot. It excites me to put IT knowledge and people impact together "
                "every day.",
                "> I mentored 10 young people and 3 started businesses or got jobs. "
                "That's the feeling I want with every placement.",
            ]),
            ("What motivates you?", [
                "Visible results: a closed ticket, a trained team, and now a placed "
                "candidate. Targets keep me sharp.",
            ]),
            ("What is your greatest achievement?", [
                "Getting 80+ health workers to use KenyaEMR daily across 50+ "
                "facilities. I piloted a few facilities, fixed the training, then "
                "trained 80+ people across 15+ sessions with job aids and support "
                "after go-live.",
            ]),
            ("Tell us about a goal you accomplished.", [
                "I took 10 people through 2 months of self-awareness training. I "
                "planned week by week and checked in with each person. By the end, "
                "3 had started businesses or secured jobs.",
            ]),
            ("How do you set goals?", [
                "Time boxing: break the goal into steps, block them in Calendar with "
                "a deadline, and track them in Tasks.",
            ]),
            ("How do you stay organised?", [
                "Google Tasks for my daily list, Keep for notes, and a Sheets tracker "
                "for every candidate: role, stage, next step, date. I clear the "
                "day's list before I log off.",
            ]),
            ("How do you prioritise?", [
                "By deadline and impact. Urgent client roles and strong candidates "
                "come first, because good candidates don't wait.",
            ]),
            ("How do you handle pressure?", [
                "Break it down and do the highest-impact work first. Monthly "
                "reporting taught me that an early plan beats a late panic.",
            ]),
            ("How do you take feedback?", [
                "Ask for it, write it down, change one thing right away, and check "
                "back later.",
            ]),
            ("Have you worked in a toxic workplace?", [
                "Know your limits and state them early and professionally. Stay "
                "focused on the work, stay respectful, and escalate through the "
                "right channel.",
            ]),
            ("What would your first three months look like?", [
                "- Get trained on BruntWork's methods and ways of doing things.",
                "- Shadow interviews and operations with different recruiters to "
                "learn the BruntWork process.",
                "- Meet different stakeholders to get a feel for how they work.",
            ]),
        ],
    },
    {
        "title": "Recruitment Cycle and Sourcing",
        "qs": [
            ("Walk us through the full recruitment cycle.", [
                "- <b>Intake:</b> must-haves, pay, shift, culture.",
                "- <b>Ad:</b> clear work, pay and shift.",
                "- <b>Sourcing:</b> applicants, LinkedIn Boolean, referrals.",
                "- <b>Screening:</b> skills, pay, shift, setup, start date.",
                "- <b>Assessment:</b> tests.",
                "- <b>Shortlist:</b> top 2-3, with reasons.",
                "- <b>Client interviews.</b>",
                "- <b>Selection and checks.</b>",
                "- <b>Offer:</b> get a clear yes.",
                "- <b>Onboarding:</b> 30/60/90-day check-ins.",
                "~ Throughout: ATS updated, privacy kept.",
            ]),
            ("What is the most important stage?", [
                "Intake. A vague brief wastes every stage after it. 10 sharp minutes "
                "saves weeks.",
            ]),
            ("Where do hires fall apart?", [
                "At the offer, when pay, shift or start date weren't confirmed early. "
                "I settle those at screening, so the offer is a formality.",
            ]),
            ("How do you attract talent? Where do you source IT support?", [
                "Go where they are: LinkedIn, job boards, tech groups on "
                "Facebook/Telegram/WhatsApp, and referrals. Strong people know other "
                "strong people. For IT support: LinkedIn Boolean first.",
            ]),
            ("How do you write outreach that doesn't feel like a template?", [
                "Short and personal. One line about something real in their profile, "
                "one line on the role/pay/shift, and one clear ask: a 15-minute call.",
            ]),
            ("How do you fill a hard-to-fill role?", [
                "Widen the net: similar titles, adjacent industries, one-step-below "
                "people ready to move up. Ask the client which must-haves truly are "
                "must-haves. Ask strong candidates for referrals.",
            ]),
            ("How do you sell a role to a passive candidate?", [
                "Find out what they want first: growth, pay, flexibility, better "
                "work. Show honestly how the role gives it. If it's not a fit, keep "
                "the relationship for next time.",
            ]),
        ],
    },
    {
        "title": "Screening, Candidate Experience and Offers",
        "qs": [
            ("What do you always cover in a screening call?", [
                "Motivation, must-have skills, pay, shift/time zone, internet and "
                "power setup, start date, other offers, and contractor status.",
            ]),
            ("What are your red flags?", [
                "- Vague about their own work.",
                "- Blaming every past employer.",
                "- Pay or shift far from the role.",
                "- Can't explain a tool they listed.",
            ]),
            ("How do you check a remote candidate is genuine?", [
                "Camera on, confirm identity, and ask unscripted follow-ups on the "
                "CV. If they pause, read, or can't explain their own work, I dig "
                "deeper.",
            ]),
            ("How do you handle a CV gap?", [
                "Ask about it neutrally and move on. What matters is that their "
                "skills are current and they can do the job now.",
            ]),
            ("What about an overqualified candidate?", [
                "Overqualified isn't a problem by itself. I check why they want the "
                "role, whether the pay works, and whether they will stay.",
            ]),
            ("How do you assess culture fit without bias?", [
                "Define fit as work behaviours: reliability, communication, "
                "responsiveness, ownership. Ask the same questions and score on the "
                "same criteria.",
                "> \"Someone like me\" is not culture fit.",
            ]),
            ("What questions should you never ask?", [
                "Age, marital status, pregnancy/children, religion, tribe/ethnicity, "
                "health/disability, politics, and in some US states salary history. "
                "Stick to what predicts performance.",
            ]),
            ("What if a candidate lied on their CV?", [
                "End politely, note the facts in the ATS, and don't submit them. One "
                "fake costs the client's trust.",
            ]),
            ("What makes a good candidate experience?", [
                "Fast replies, clear next steps, honest feedback, no silence.",
            ]),
            ("How do you handle ghosting?", [
                "- <b>Day 1:</b> email plus WhatsApp/LinkedIn.",
                "- <b>Day 2:</b> call.",
                "- <b>Day 4:</b> final note: \"I'll close your file Friday unless I "
                "hear from you.\"",
                "- Keep 2-3 backups warm.",
                "<b>Why candidates ghost:</b> usually a slow process, silence from "
                "us, or a faster offer elsewhere.",
                "<b>Prevention:</b> regular updates, even \"no news yet, next update "
                "Friday.\"",
            ]),
            ("How do you secure commitment before the offer?", [
                "No surprises. Confirm pay and shift at screening. Before the offer I "
                "ask:",
                "> \"If it comes at this, will you accept?\"",
            ]),
            ("A candidate wants more than the budget. What do you do?", [
                "Find out early, not at the offer.",
                "- <b>Small gap:</b> check what's flexible: pay review after 90 "
                "days, incentives.",
                "- <b>Big gap:</b> be honest with both sides.",
                "- <b>Market above budget:</b> show the client the data.",
            ]),
            ("A candidate backs out after accepting. What now?", [
                "Find out why, tell the client immediately with a replacement plan, "
                "go to the backups, and fix the cause. It's usually a counteroffer "
                "or a doubt missed at screening.",
            ]),
            ("How do you handle a counteroffer?", [
                "Raise it early:",
                "> \"If your employer counters, what will you do?\"",
                "Then remind them why they started looking.",
            ]),
            ("How do you reject many candidates without being cold?", [
                "Quick and personal. One line of thanks, one line of reason, one line "
                "of encouragement. Under 90 seconds each, and never a silent no.",
            ]),
        ],
    },
    {
        "title": "Clients, Metrics, ATS and Privacy",
        "qs": [
            ("How do you handle an angry client?", [
                "Stay calm and let them finish. Acknowledge the problem, get the "
                "facts, agree a fix and a time, and follow up before they chase.",
                "> They just want to know someone owns it.",
            ]),
            ("What do you ask at intake?", [
                "- Must-haves, nice-to-haves, deal-breakers.",
                "- Pay, shift, time zone.",
                "- What success looks like at 90 days.",
                "- Who interviews, and how fast they decide.",
            ]),
            ("The client rejects strong candidates without clear reasons?", [
                "Ask for specific feedback per candidate, compare it against the "
                "brief, and look for a pattern. Recalibrate with real profiles:",
                "> \"Here are three you rejected. What's missing?\"",
                "Usually the brief changes.",
            ]),
            ("The client wants to skip steps?", [
                "Respect it, but keep the minimum checks: skills, references, privacy "
                "consent. Explain the risk in one sentence and let them decide.",
            ]),
            ("How do you build trust with a client who was let down before?", [
                "Small promises kept fast. A strong shortlist on time, honest "
                "updates, and no padding with weak candidates.",
            ]),
            ("How do you manage targets and volume?", [
                "One tracker, ranked by urgency and how close each role is to "
                "filling. I block my shift: sourcing first, screens in the middle, "
                "updates and admin at the end. Every role gets a touch daily.",
            ]),
            ("You're behind target halfway through the month. What do you do?", [
                "Look at the funnel to find the leak: not enough candidates, too few "
                "passing screens, or clients not converting. Fix that stage: more "
                "sourcing hours, tighter screening, or faster client feedback. And "
                "revisit strong runners-up from earlier roles.",
            ]),
            ("Which metrics matter?", [
                "Time to fill, submissions per hire, interview-to-offer rate, offer "
                "acceptance rate, and how long hires stay. They show where the "
                "process is slow or leaking.",
            ]),
            ("How do you calculate time to fill?", [
                "Days from when the role opens to when the offer is accepted. I'll "
                "learn BruntWork's benchmark per role and aim to beat it.",
            ]),
            ("How do you keep ATS data clean when busy?", [
                "Update as I go, not at the end of the day. Every call ends with a "
                "stage change and a next step.",
                "> If it's not in the ATS, it didn't happen.",
            ]),
            ("Have you used an ATS?", [
                "I ran pipelines in Freshdesk and Zoho Desk: every request logged, "
                "tracked by stage, and closed on time. An ATS is the same family, so "
                "I learn fast.",
            ]),
            ("How do you use AI tools in recruiting?", [
                "To speed up first drafts: job ads, outreach, Boolean ideas. I always "
                "check and personalise. I never paste candidate personal data into "
                "public AI.",
            ]),
            ("How do you protect candidate data? Which privacy laws apply?", [
                "Only collect what the role needs, store it in the ATS (not personal "
                "files or chats), share a CV with a client only with the candidate's "
                "consent, and delete what's not needed. I work with confidential "
                "patient data daily, so it's a habit.",
                "<b>Laws</b> depend on where the candidate and client are: Kenya DPA, "
                "Philippines DPA, GDPR for UK/EU. The principles are the same: "
                "consent, minimum data, secure storage, limited access.",
            ]),
        ],
    },
    {
        "title": "Logistics",
        "qs": [
            ("Can you work 9PM-6AM Manila time?", [
                "Yes. That's 4PM-1AM Kenya time, and I'm set up for it.",
            ]),
            ("What is your internet and power setup?", [
                "A stable home connection plus mobile data backup, and backup power "
                "for the router and laptop.",
            ]),
            ("Are you OK working as an independent contractor?", [
                "Yes. I handle my own taxes and benefits, and I'm happy to be "
                "measured on results.",
            ]),
            ("What are your salary expectations?", [
                "Around <b>USD 600-800 base</b>, and incentives on top motivate me.",
                "<b>If the offer is lower:</b>",
                "> \"I can work with that to start. Is there a review where the base "
                "grows with performance after 90 days on target?\"",
            ]),
            ("When can you start?", [
                "[Your notice period]. I can do training and onboarding during that "
                "time.",
            ]),
            ("Question to ask BruntWork", [
                "> \"You work with companies from specific regions. Many other "
                "companies would also like to use your services. Is expanding to "
                "them something you're thinking about?\"",
            ]),
        ],
    },
    {
        "title": "Candidate CV Assessment",
        "intro": "Save this for last.",
        "qs": [
            ("What was the brief?", [
                "EA + Marketing for Sarah at 439 Consulting, which serves "
                "non-profits.",
                "- <b>EA side:</b> diary, inbox, records, admin, databases, several "
                "projects.",
                "- <b>Marketing side, for 5 client accounts:</b> social, content, "
                "Canva design, some video, campaigns, tracking, presentations, US "
                "grant research.",
                "- <b>Key needs:</b> 3+ years EA, social/content, Canva/design, "
                "video, communication, multitasking, attention to detail.",
            ]),
            ("Who did you endorse, and why?", [
                "<b>Candidate 1 first, Candidate 5 second.</b>",
                "> The role fails if the person is only admin or only marketing. "
                "Those two cover the mix best.",
            ]),
            ("Candidate 1: Ara, Philippines", [
                "<b>Yes:</b> Executive VA 2021-2024 + VA 2018-2021 = 3+ years. "
                "Social on 6 platforms, community replies, YouTube. Canva banners, "
                "flyers and ads. Video editing with captions and overlays. Marketing: "
                "ads, marketing emails. Databases: CRM, client lists, QuickBooks. "
                "Tools: Canva, Asana, Google Workspace, Outlook, Office. Strong "
                "communication as an ex call-centre supervisor/trainer.",
                "<b>Gaps flagged honestly:</b> one business, not five accounts; no "
                "grant research; US exposure only via ecommerce customer service.",
                "<b>Why first:</b> the only one who has already done both halves in "
                "the same seat.",
            ], ("ENDORSE FIRST", GREEN)),
            ("Candidate 5: Tasha, Australia", [
                "<b>Yes:</b> freelance digital marketing for several businesses since "
                "2021. Campaign tracking (reach, engagement, CTR, conversion), +166% "
                "engagement for one client. Brand design for business, community and "
                "government since 2020. Asia Education Foundation internship: copy, "
                "press releases, CRM, workshops. Teach For Australia + Asia "
                "Foundation, close to Sarah's non-profit clients. Market research "
                "interviews, legal research, database/CRM.",
                "<b>Gaps flagged:</b> never an EA; Canva and video not named; the US "
                "link is an academic fellowship, not US grant research.",
                "<b>Why second:</b> strongest on the client and non-profit side, and "
                "the admin side can be tested. Teaching admin is easier than teaching "
                "content and design.",
            ], ("ENDORSE SECOND", GREEN)),
            ("Candidate 4: Nan, Myanmar", [
                "<b>Trap if you think classic EA hire.</b>",
                "<b>Yes, strongest EA:</b> 10 years as EA and office manager (Blink "
                "Company, Sedona Hotel).",
                "<b>But:</b> the only marketing is \"Assist Marketing Comms "
                "Manager\": press clippings, photo shoots, \"social media "
                "promotions\". No Canva, no design, no video anywhere. English B2. "
                "Admin is not the scarce skill here.",
                "~ If Sarah wanted a pure EA, Nan would be the first call.",
            ], ("NOT SELECTED", GREY)),
            ("Candidate 2: Mary Grace, Philippines", [
                "<b>Right titles, weak evidence.</b>",
                "The header says EA, project manager, social media manager. But "
                "Meri's StyleSavvy was only March-July 2024. Upwork EA for one "
                "director: LinkedIn, email, PowerPoint, basic video, spreadsheets. "
                "Accenture Dec 2019-Mar 2024 overlaps the Upwork work, and the duties "
                "read like a copied job advert (\"In this role, you'll play a pivotal "
                "role...\").",
                "~ I wouldn't put her in front of the client without checking.",
            ], ("NOT SELECTED", GREY)),
            ("Candidate 3: Cindi, Indonesia", [
                "<b>Shop owner looking for admin work.</b> Her objective says so.",
                "Experience: her own Shopee/Instagram store, a 2016-2018 student "
                "business, and a social media role from July 2024 only. Canva and "
                "CapCut are in the skills list, not the track record. No EA job and "
                "no 3 years in a support seat. Good TOEFL, but no employment history.",
            ], ("NOT SELECTED", GREY)),
            ("What did your email to Sarah say?", [
                "- Referred to candidates by number only.",
                "- Opened with what she needs (day-to-day support plus social, "
                "content, design and research for non-profits, including US funding) "
                "and said these two come closest.",
                "- <b>Candidate 1</b> has already worked this way with the tools; "
                "check on several accounts and no grant research.",
                "- <b>Candidate 5</b> is the better marketer and closer to the client "
                "base; admin to be tested.",
                "- Ended by asking for her thoughts and offering interviews.",
            ]),
            ("What were your 3 pre-screening questions, and why?", [
                "<b>1.</b> \"This role mixes executive support with content and "
                "marketing for about five client accounts. How have you handled a "
                "week when admin work and content deadlines were both due, and how "
                "many accounts were you responsible for?\"",
                "~ Tests the real shape of the job. Catches Candidate 1's one-brand "
                "gap and Candidate 5's no-EA gap.",
                "<b>2.</b> \"The role calls for graphic design, ideally Canva, and "
                "some video editing. What have you produced yourself, and which tools "
                "did you use?\"",
                "~ Asks for proof, not a skills list. Candidate 1 didn't name a video "
                "tool; Candidate 5 didn't name Canva or video.",
                "<b>3.</b> \"If asked to put together a usable shortlist of US "
                "non-profit funding options by Friday, how would you decide where to "
                "search, what to leave out, and how to send it back?\"",
                "~ Neither finalist has grant research, so test method and judgement "
                "instead of asking them to stretch the CV.",
            ]),
            ("Why not Candidate 4, with the most EA experience?", [
                "Because EA is not the scarce skill. Sarah also needs content, Canva, "
                "video and multiple accounts, and Candidate 4 shows none of it "
                "hands-on.",
            ]),
            ("Isn't Candidate 5 risky with no EA experience?", [
                "Yes, and that's why she's second, not first. I flagged it to Sarah. "
                "Admin can be tested in one call.",
            ]),
            ("Candidate 2 looks perfect on paper. Why not?", [
                "The titles are right but the evidence isn't: a 4-month social role, "
                "overlapping dates, and copied duties.",
            ]),
        ],
    },
]


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

class Doc(BaseDocTemplate):
    def afterFlowable(self, f):
        bm = getattr(f, "_bm", None)
        if bm:
            key, title, level = bm
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(title, key, level=level, closed=level == 0)


def quote_block(blocks, first=True, last=True):
    rows = []
    for b in blocks:
        if b.startswith("- "):
            p = Paragraph(f"<font color='{ACCENT_HEX}'>•</font>&nbsp;&nbsp;{b[2:]}",
                          S["bullet"])
        elif b.startswith("~ "):
            p = Paragraph(b[2:], S["note"])
        elif b.startswith("> "):
            p = Paragraph(b[2:], S["say"])
        else:
            p = Paragraph(b, S["a"])
        rows.append([p])
    t = Table(rows, colWidths=[BODY_W])
    cmds = [
        ("BACKGROUND", (0, 0), (-1, -1), CARD),
        ("LINEBEFORE", (0, 0), (0, -1), 3, ACCENT),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
    ]
    for i, b in enumerate(blocks):
        if b.startswith("> "):
            cmds.append(("TOPPADDING", (0, i), (-1, i), 5))
            cmds.append(("BOTTOMPADDING", (0, i), (-1, i), 5))
    if first:
        cmds.append(("TOPPADDING", (0, 0), (-1, 0), 9))
    if last:
        cmds.append(("BOTTOMPADDING", (0, -1), (-1, -1), 9))
    t.setStyle(TableStyle(cmds))
    return t


def strip(steps):
    n = len(steps)
    gap = 7
    cell_w = (BODY_W - gap * (n - 1)) / n
    row, widths = [], []
    for i, (letter, label, desc) in enumerate(steps):
        row.append([Paragraph(letter, S["strip_letter"]),
                    Paragraph(label, S["strip_label"]),
                    Spacer(1, 2),
                    Paragraph(desc, S["strip_desc"])])
        widths.append(cell_w)
        if i < n - 1:
            row.append("")
            widths.append(gap)
    t = Table([row], colWidths=widths)
    cmds = [("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 9),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10)]
    for c in range(0, len(row), 2):
        cmds += [("BACKGROUND", (c, 0), (c, 0), CARD),
                 ("LINEABOVE", (c, 0), (c, 0), 2.5, ACCENT)]
    t.setStyle(TableStyle(cmds))
    return t


def numbered(sections):
    n = 0
    for si, sec in enumerate(sections, 1):
        items = []
        for q in sec["qs"]:
            n += 1
            items.append((n, q))
        yield si, sec, items


def cover_header(title):
    return [
        Paragraph('<a name="contents"/>INTERVIEW PREP&nbsp;&nbsp;·&nbsp;&nbsp;'
                  'RECRUITMENT OFFICER', S["kicker"]),
        Spacer(1, 6),
        Paragraph(title, S["title"]),
        Spacer(1, 4),
        Paragraph("Meshack Ariri&nbsp;&nbsp;·&nbsp;&nbsp;Click any question to "
                  "jump to the answer. Every page links back here.", S["sub"]),
        Spacer(1, 10),
        HRFlowable(width="100%", thickness=0.8, color=ACCENT, spaceAfter=0),
    ]


def contents(sections):
    out = []
    for si, sec, items in numbered(sections):
        out.append(Paragraph(
            f'<a href="#s{si}" color="{ACCENT_HEX}">{si:02d}&nbsp;&nbsp;'
            f'{sec["title"].upper()}</a>', S["toc_sec"]))
        for n, q in items:
            out.append(Paragraph(
                f'<a href="#q{n}" color="{TEXT_HEX}"><font color="{ACCENT_HEX}" '
                f'name="Sans-B">{n:02d}</font>&nbsp;&nbsp;{q[0]}</a>',
                S["toc_q"]))
    return out


def body(sections, section_break=260):
    out = []
    for si, sec, items in numbered(sections):
        out.append(CondPageBreak(section_break))
        head = Table(
            [[Paragraph(f'<a name="s{si}"/>{si:02d}', S["sec_num"]),
              Paragraph(sec["title"], S["sec_title"])]],
            colWidths=[58, BODY_W - 58])
        head.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ("LINEBELOW", (0, 0), (-1, 0), 0.8, ACCENT),
        ]))
        head._bm = (f"o_s{si}", f"{si:02d}  {sec['title']}", 0)
        block = [Spacer(1, 6), head, Spacer(1, 8)]
        if sec.get("intro"):
            block.append(Paragraph(sec["intro"], S["intro"]))
        if sec.get("strip"):
            block += [strip(sec["strip"]), Spacer(1, 4)]
        out.append(KeepTogether(block))

        for n, q in items:
            question, blocks = q[0], q[1]
            tag = q[2] if len(q) > 2 else None
            tag_html = ""
            if tag:
                label, colour = tag
                tag_html = (f'&nbsp;&nbsp;&nbsp;<font size="8" color="{colour}">'
                            f'{label}</font>')
            qp = Paragraph(
                f'<a name="q{n}"/><font color="{ACCENT_HEX}">Q{n:02d}</font>'
                f'&nbsp;&nbsp;{question}{tag_html}', S["q"])
            qp._bm = (f"o_q{n}", f"Q{n:02d}  {question}", 1)
            if len(blocks) <= 5:
                out.append(KeepTogether([qp, quote_block(blocks)]))
            else:
                out.append(KeepTogether([qp, quote_block(blocks[:3], last=False)]))
                out.append(quote_block(blocks[3:], first=False))
    return out


def paint_bg(c):
    c.setFillColor(BG)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)


def on_cover(c, doc):
    c.saveState()
    c.showOutline()
    paint_bg(c)
    c.setFillColor(ACCENT)
    c.rect(0, PAGE_H - 6, PAGE_W, 6, stroke=0, fill=1)
    footer(c, doc, back_link=False)
    c.restoreState()


def on_contents(c, doc):
    c.saveState()
    paint_bg(c)
    footer(c, doc, back_link=False)
    c.restoreState()


def on_body(c, doc):
    c.saveState()
    paint_bg(c)
    y = PAGE_H - 30
    c.setFont("Sans-B", 7.6)
    c.setFillColor(HEAD)
    c.drawString(MARGIN, y, "BRUNTWORK  ·  RECRUITMENT OFFICER  ·  INTERVIEW PREP")
    c.setFont("Sans", 7.6)
    c.setFillColor(MUTED)
    c.drawRightString(PAGE_W - MARGIN, y, "Meshack Ariri")
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.line(MARGIN, y - 6, PAGE_W - MARGIN, y - 6)
    footer(c, doc, back_link=True)
    c.restoreState()


def footer(c, doc, back_link):
    y = 26
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.line(MARGIN, y + 12, PAGE_W - MARGIN, y + 12)
    c.setFont("Sans", 7.8)
    c.setFillColor(MUTED)
    c.drawRightString(PAGE_W - MARGIN, y, str(doc.page))
    if back_link:
        label = "↑  Back to contents"
        c.setFont("Sans-B", 7.8)
        c.setFillColor(ACCENT)
        c.drawString(MARGIN, y, label)
        w = pdfmetrics.stringWidth(label, "Sans-B", 7.8)
        c.linkRect("", "contents", (MARGIN - 2, y - 3, MARGIN + w + 2, y + 9),
                   relative=0, thickness=0)


def build(out_path, sections=SECTIONS, title="BruntWork Interview Prep",
          compact=False):
    doc = Doc(str(out_path), pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
              topMargin=50, bottomMargin=50,
              title=title, author="Meshack Ariri")
    col_gap = 18
    col_w = (BODY_W - col_gap) / 2
    header_h = 108
    top = PAGE_H - 44
    bottom = 46

    cover_frames = [
        Frame(MARGIN, top - header_h, BODY_W, header_h, id="hdr",
              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0),
        Frame(MARGIN, bottom, col_w, top - header_h - bottom - 4, id="c1",
              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0),
        Frame(MARGIN + col_w + col_gap, bottom, col_w,
              top - header_h - bottom - 4, id="c2",
              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0),
    ]
    contents_frames = [
        Frame(MARGIN, bottom, col_w, top - bottom, id="k1",
              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0),
        Frame(MARGIN + col_w + col_gap, bottom, col_w, top - bottom, id="k2",
              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0),
    ]
    body_frame = [Frame(MARGIN, 50, BODY_W, PAGE_H - 50 - 52, id="body",
                        leftPadding=0, rightPadding=0, topPadding=0,
                        bottomPadding=0)]
    if compact:
        full = [Frame(MARGIN, bottom, BODY_W, top - bottom, id="full",
                      leftPadding=0, rightPadding=0, topPadding=0,
                      bottomPadding=0)]
        doc.addPageTemplates([
            PageTemplate("cover", full, onPage=on_cover,
                         autoNextPageTemplate="body"),
            PageTemplate("body", body_frame, onPage=on_body),
        ])
    else:
        doc.addPageTemplates([
            PageTemplate("cover", cover_frames, onPage=on_cover,
                         autoNextPageTemplate="contents"),
            PageTemplate("contents", contents_frames, onPage=on_contents),
            PageTemplate("body", body_frame, onPage=on_body),
        ])

    first = cover_header(title)
    first[0]._bm = ("o_contents", "Contents", 0)
    if compact:
        story = first + [Spacer(1, 4)] + contents(sections) + [Spacer(1, 14)]
        story += body(sections, section_break=120)
    else:
        story = first + [FrameBreak()] + contents(sections)
        story += [NextPageTemplate("body"), PageBreak()] + body(sections)
    doc.build(story)

if __name__ == "__main__":
    default = Path.home() / "Desktop" / "INTERVIEW " / "BruntWork Quick Prep.pdf"
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else default
    build(out)
    print(out)
