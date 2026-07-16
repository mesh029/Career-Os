# Meshack Ariri — Career Intelligence System

This folder is a permanent, evolving system for maximizing Meshack Ariri's career outcomes.
It is governed by one charter and organized so every future action (resume, cover letter,
LinkedIn edit, job application, market pivot) plugs into the same brain.

> **Read `00_SYSTEM_PROMPT.md` first — it is the constitution. Everything else obeys it.**

---

## Index

| File | Phase | What it is |
|---|---|---|
| `00_SYSTEM_PROMPT.md` | — | The founding charter (KPIs, principles, phases, golden rule) |
| `01_Career_Profile.md` | 1 | Who you are, level now vs. 6–18 mo, target industries/companies, critical findings |
| `02_Skills_Intelligence.md` | 2 | Full skill inventory, hidden skills, missing terminology, skill broadcasting, overselling to fix |
| `03_Application_Intelligence.md` | — | Analysis of all past applications + patterns + strategy + running application log |
| `04_LinkedIn_Transformation.md` | 3 | Full audit + headline/About/experience rewrites, SEO, visuals, GitHub, content plan |
| `05_Learning_Roadmap.md` | 2 | ROI-ranked skills to learn, 6-month sequence |
| `06_Growth_and_Coaching.md` | 6–8 | Personal brand, market trends, continuous coaching |
| `07_Independent_Experience_and_Positioning.md` | 2/6 | Standing directive: value the WHOLE engineer (projects, consulting, hackathons) — truthfully, with evidence |
| `resumes/00_Master_Resume.md` | 4 | **Single source of truth for all facts** |
| `resumes/*.docx` | 4 | ATS-optimized Word resumes (3 tracks) |
| `resumes/build_resumes.py` | 4 | Regenerates the .docx resumes from structured data |
| `templates/Cover_Letters_Messages_Emails.md` | 5 | Cover letters, recruiter DMs, application & follow-up emails |
| `reports/` | 5/7 | Per-application and market-research reports (added over time) |

---

## The current strategy (one line)
**Primary identity = Health Informatics / EMR–DHIS2 specialist.** Two sanctioned variants:
INGO/UN ICT Officer, and Enterprise/Remote IT Operations. Retire off-brand tracks
(web/Webflow, talent acquisition, pure CRM, L1 voice helpdesk, non-health M&E).

## Resume tracks (generated .docx)
1. `Meshack_Ariri_Resume_HealthInformatics.docx` — **default / primary**
2. `Meshack_Ariri_Resume_ICT_Officer_INGO.docx` — UN/INGO IT roles
3. `Meshack_Ariri_Resume_IT_Operations.docx` — enterprise/remote sysadmin & ops

Visual theme (shared across all CV/cover-letter PDFs and DOCX): shaded header band with top accent stripe, two-line contact row, accent-bar section headings, refined slate/teal palette. Defined in `resumes/resume_theme.py`; rendered by `build_resumes.py` and `pdf_builder.py`.

To regenerate after editing facts: `python3 resumes/build_resumes.py`

---

## Top 5 fixes that will move KPIs fastest
1. **Lock one timeline & titles** everywhere (done in Master Resume) — fixes credibility screen-outs.
2. **Fix employer name** ("PATH", not "Program Appropriate for Technology in Health").
3. **Rewrite LinkedIn** headline + About around health informatics + start posting (breaks "0 posts").
4. **Apply into your strength** (health informatics / EMR–DHIS2) far more than you have been.
5. **Quantify everything** (users, uptime %, facilities, % time saved) — recruiters skim for impact.

---

## How to use this system going forward

**When you get a job link (Phase 5):**
1. Add a folder under `reports/[Company-Role]/` with the JD.
2. Ask for: company research, keyword extraction, match %, resume+cover-letter+email tailoring,
   and interview Q&A. The output cites `00_SYSTEM_PROMPT.md` and uses the Master Resume facts.
3. Log it in `03_Application_Intelligence.md` §M.

**When you add new past applications:** drop them in the workspace; they become training data and
`03_Application_Intelligence.md` gets updated.

**When facts change (new role, new metric, new cert):** update `resumes/00_Master_Resume.md` first,
then regenerate resumes and propagate to LinkedIn.

---

## Open items needing YOUR input (to sharpen everything)
- [x] **Canonical current title** at PATH: **Health Informatics / HMIS Officer** (confirmed 2026-07-13).
- [x] **Employment structure** confirmed (2026-07-13): 3 roles — ICT Intern (Apr–Dec 2023) → ICT Associate (Jan 2024–Mar 2025) → Health Informatics/HMIS Officer (Mar 2025–Present).
- [ ] Confirm exact **# of facilities/sites** you support (for metrics).
- [ ] Confirm **CCNA & AZ-900** are exam certs vs. course completions (label correctly).
- [ ] Confirm the **~40%** and **~25%** improvement figures are defensible.
- [ ] Confirm whether the **freelance/consulting** work is currently ongoing (affects resume).
- [ ] Add your **GitHub URL**.
- [ ] **LinkedIn experience** still shows 2 roles with wrong titles/dates — restructure to the confirmed 3 roles.
