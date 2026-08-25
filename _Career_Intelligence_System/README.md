# Meshack Ariri — Career Intelligence System

This repository is the durable memory for Meshack Ariri's career work. AI chat history,
computer-local settings, and agent memory may disappear; the versioned files in this
repository must contain enough context for a person or a fresh agent to continue safely.

> **Start with this README, then read `00_SYSTEM_PROMPT.md`. Do not rely on a previous chat.**

**Last continuity update:** 2026-08-25
**Repository:** `https://github.com/mesh029/Career-Os.git`
**Default branch:** `main`

---

## 1. Five-minute restart on another computer

### Clone and enter the system

```bash
git clone https://github.com/mesh029/Career-Os.git
cd Career-Os/_Career_Intelligence_System
git pull --ff-only
```

If the repository is already cloned:

```bash
cd /path/to/Career-Os
git status
git pull --ff-only
cd _Career_Intelligence_System
```

Never discard local changes just to pull. If `git status` is not clean, review or save
those changes first.

### Create the Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install "python-docx==1.1.2" "reportlab==3.6.13"
```

These versions reproduce the environment last verified on Python 3.8.10. There is
currently no dependency manifest, so keep this setup block current if dependencies change.

### Read the state in this order

1. `README.md` — continuity guide and latest handoff.
2. `00_SYSTEM_PROMPT.md` — constitution, KPIs, and truthfulness rules.
3. `resumes/00_Master_Resume.md` — canonical personal and employment facts.
4. `applications/APPLICATIONS_TRACKER.md` — active pipeline, deadlines, and submission status.
5. `08_Jobless_Remote_Volume_Playbook.md` — use when income is urgent and remote niche roles are scarce.
6. The active role's `Job_Description.md` and `Application_Intelligence.md`.
7. `03_Application_Intelligence.md` — historical patterns and strategy.
8. `prep/README.md` — interview language, answer cards, drills, and JD registry.
9. `04_LinkedIn_Transformation.md` when working on LinkedIn (includes jobless/remote headline + About).

Then check `git status` and the dates inside the tracker. Job listings and deadlines can
expire, so verify them live before acting.

---

## 2. Copy-paste prompt for any fresh AI agent

```text
You are taking over the Career Intelligence System in this repository.
You have no reliable memory of previous chats. Establish the current state from files.

Read, in order:
1. _Career_Intelligence_System/README.md
2. _Career_Intelligence_System/00_SYSTEM_PROMPT.md
3. _Career_Intelligence_System/resumes/00_Master_Resume.md
4. _Career_Intelligence_System/applications/APPLICATIONS_TRACKER.md
5. The files for the application or task we are currently working on
6. _Career_Intelligence_System/prep/README.md when a JD or interview is involved

Rules:
- Never invent facts, metrics, certifications, experience, links, or outcomes.
- Preserve the canonical PATH employer name, titles, and dates from the Master Resume.
- Treat DOCX/PDF files as generated outputs, not sources of truth.
- Builders currently duplicate facts; they do not read the Markdown Master Resume.
- Before editing a builder, compare its facts against the Master Resume.
- Mark uncertain claims as unverified and ask me before publishing them.
- Keep the application tracker, application log, prep handbook, and LinkedIn guidance
  synchronized when the same change affects them.
- Verify live job deadlines and links; do not trust old tracker dates blindly.
- Preserve the visual theme in resumes/resume_theme.py unless I request a redesign.
- Do not expose this repository publicly without a privacy review.

Before changing anything, report:
1. Git state
2. Current deadlines and unsent applications
3. Unresolved factual confirmations
4. Any source-versus-builder drift relevant to the task
5. The smallest safe next action

At the end, update the repository's durable handoff state instead of relying on chat memory.
```

---

## 3. Source-of-truth hierarchy

When files disagree, use this order:

| Priority | Source | Authority |
|---:|---|---|
| 1 | `00_SYSTEM_PROMPT.md` | Governance, objectives, and ethical rules |
| 2 | `resumes/00_Master_Resume.md` | Canonical facts: titles, dates, metrics, education, certifications |
| 3 | `01_` through `08_*.md` | Strategy and interpretation (incl. jobless/remote volume playbook) |
| 4 | `applications/<Role>/Job_Description.md` | Captured requirements for one role |
| 5 | `applications/<Role>/Application_Intelligence.md` | Fit analysis and honest positioning |
| 6 | `applications/<Role>/build.py` | Renderable role-specific content |
| 7 | Generated `.docx` and `.pdf` files | Outputs only |
| 8 | `applications/APPLICATIONS_TRACKER.md` | Operational status and deadlines |
| 9 | `prep/README.md` | Interview vocabulary and practice material |

### Critical limitation: the builders do not read the master

`resumes/00_Master_Resume.md` is the human source of truth, but `resumes/build_resumes.py`
and every `applications/*/build.py` currently contain duplicated Python data. Therefore,
editing the Master Resume and rerunning a builder **does not automatically propagate the
change**.

For every factual change, manually reconcile:

- `resumes/00_Master_Resume.md`
- `resumes/build_resumes.py`
- affected `applications/*/build.py` files
- LinkedIn copy and reusable templates
- application intelligence and interview material where relevant

Do not assume “regenerate” means “synchronize.”

---

## 4. Current career strategy

**Long-term primary identity:** Health Informatics / EMR–DHIS2 specialist.

**Active survival mode (2026-08-25):** Jobless / remote volume — default public positioning is
**Remote IT Support & Systems Operations**, with PATH health-systems work as proof of seriousness.
Full operating system: `08_Jobless_Remote_Volume_Playbook.md`. LinkedIn paste-ready copy lives
there and in `04_LinkedIn_Transformation.md` (JOBLESS / REMOTE VOLUME headline + About).

Approved variants:

1. Remote IT Support / Tech Ops / SysAdmin (**default while job hunting for income**)
2. INGO/UN ICT Officer
3. Health Informatics / EMR–DHIS2 (**use when a real digital-health JD appears**)

Avoid making off-brand tracks the main identity: web/Webflow, talent acquisition, pure
CRM, generic L1 voice helpdesk, and non-health M&E.

Canonical PATH timeline:

1. **ICT Intern** — Apr 2023 to Dec 2023
2. **ICT Associate** — Jan 2024 to Mar 2025
3. **Health Informatics / HMIS Officer** — Mar 2025 to Present

Employer must be written as **PATH**, not “Program Appropriate for Technology in Health.”
Tailoring bullets and summaries is allowed; silently replacing official job titles is a
credibility risk.

---

## 5. Current operational snapshot

Snapshot from `applications/APPLICATIONS_TRACKER.md`, last updated 2026-07-15:

- Ten application packages are built; none is recorded as sent.
- **Immediate deadline:** ICT Officer — Gas Africa, 2026-07-21, approximately 85% apply score.
- Other strong unsent packages include Solvo Global (~85%), CCaaS SysAdmin (~85%),
  Influx (~82%), Thika SysAdmin/Web Dev (~80%), and Kuehne+Nagel (~78%).
- INSO is a long-shot because French is essential.
- Confirm every listing, deadline, employer, and submission channel before applying.
- `applications/APPLICATIONS_TRACKER.md` is newer than the running log in
  `03_Application_Intelligence.md`; those files need synchronization.

The tracker is the live pipeline. This snapshot is only a handoff summary and will become
stale; update both when the pipeline changes.

### Facts still requiring Meshack's confirmation

- [ ] Exact number of facilities/sites supported.
- [ ] Whether CCNA is an exam certification or a course completion.
- [ ] Whether AZ-900 is an exam certification or a course completion.
- [ ] Whether the approximately 40% processing-time improvement is defensible.
- [ ] Whether the approximately 25% ticket-response improvement is defensible.
- [ ] Whether freelance/consulting work is genuinely ongoing.
- [ ] GitHub URL.
- [ ] LinkedIn experience updated to the canonical three-role timeline.

Until confirmed, do not turn these into stronger or more definite claims.

---

## 6. Repository map

| Path | Purpose |
|---|---|
| `00_SYSTEM_PROMPT.md` | Founding charter and non-negotiable rules |
| `01_Career_Profile.md` | Professional identity, target market, positioning, risks |
| `02_Skills_Intelligence.md` | Skills inventory, hidden strengths, terminology, gaps |
| `03_Application_Intelligence.md` | Historical application analysis and running log |
| `04_LinkedIn_Transformation.md` | LinkedIn audit, copy, SEO, visuals, and content plan |
| `05_Learning_Roadmap.md` | ROI-ranked six-month learning sequence |
| `06_Growth_and_Coaching.md` | Brand, market trends, coaching, and KPI tracker |
| `07_Independent_Experience_and_Positioning.md` | Truthful use of projects, consulting, and hackathons |
| `08_Jobless_Remote_Volume_Playbook.md` | Survival mode: remote browse filter, apply cadence, LinkedIn paste copy |
| `resumes/00_Master_Resume.md` | Canonical facts and master bullet bank |
| `resumes/resume_theme.py` | Shared palette, fonts, and contact header |
| `resumes/build_resumes.py` | Builds the three general DOCX resumes |
| `resumes/pdf_builder.py` | Shared ReportLab renderer for application PDFs |
| `applications/APPLICATIONS_TRACKER.md` | Active application pipeline |
| `applications/<Role>/` | JD, analysis, builder, messages, and generated package |
| `prep/README.md` | Rick-Speak Technical Handbook and interview preparation |
| `templates/` | Reusable cover letters, emails, and recruiter messages |
| `reports/` | Portfolio, market, and supporting research reports |

---

## 7. Build and regeneration guide

Run commands from `_Career_Intelligence_System/`.

### General resume tracks

```bash
python3 resumes/build_resumes.py
```

Outputs:

1. `resumes/Meshack_Ariri_Resume_HealthInformatics.docx` — default
2. `resumes/Meshack_Ariri_Resume_ICT_Officer_INGO.docx`
3. `resumes/Meshack_Ariri_Resume_IT_Operations.docx`

The general builder currently creates DOCX only.

### One application package

```bash
python3 "applications/ICT Officer - Gas Africa/build.py"
```

Each application builder normally creates four files beside itself:

- tailored CV DOCX
- tailored cover letter DOCX
- tailored CV PDF
- tailored cover letter PDF

### All application packages

```bash
for build in applications/*/build.py; do
  python3 "$build"
done
```

After building, inspect the files visually and verify text, dates, page breaks, links,
placeholders, and filename requirements. A successful Python exit does not prove the
documents are factually correct or visually clean.

---

## 8. Visual identity and theme

The source of truth for resume styling is `resumes/resume_theme.py`.

**Current theme:** Royal Indigo and slate, not teal.

| Token | Hex | Use |
|---|---|---|
| Accent | `#3730A3` | Section bars, titles, labels, bullets |
| Accent dark | `#2A2478` | Top stripe and name |
| Accent mid | `#6366F1` | Rules and separators |
| Accent light | `#ECEDFB` | Soft lavender header band |
| Accent pale | `#F6F6FD` | Section-heading strip |
| Slate | `#1E293B` | Body text |
| Muted slate | `#64748B` | Dates and secondary text |

Fonts:

- DOCX: Calibri
- PDF: Helvetica

Layout:

- ATS-safe, single column
- top accent stripe
- shaded centered header
- two-line contact row
- section headings with a left accent bar
- dark body text on white

To change the look globally, edit `resumes/resume_theme.py`, then rebuild all affected
documents. Check `resumes/build_resumes.py` and `resumes/pdf_builder.py` for hard-coded
style values before assuming every token is centralized.

Portability notes:

- Calibri may be substituted on computers where it is unavailable.
- PDFs explicitly use A4; DOCX page size should be visually checked because it may inherit
  a Word/LibreOffice default.
- LinkedIn's blue/teal visual prompts in `04_LinkedIn_Transformation.md` are separate and
  are not generated from the resume theme.

---

## 9. Standard workflows

### Starting any work session

1. Pull the latest `main`.
2. Read this README and the charter.
3. Check `git status`.
4. Read the tracker and verify urgent deadlines live.
5. Read the Master Resume before changing career facts.
6. Work only from confirmed evidence.

### Adding a new job

1. Verify the live posting, employer, location, deadline, and application channel.
2. Create `applications/<Role - Employer>/`.
3. Save the JD and its source/date in `Job_Description.md`.
4. Create `Application_Intelligence.md`: fit, gaps, ATS terms, evidence, risks, and
   recommendation.
5. Create or adapt `build.py` using facts checked against the Master Resume.
6. Add an email/application message when needed.
7. Build and inspect the DOCX/PDF package.
8. Update `applications/APPLICATIONS_TRACKER.md`.
9. Append the application to `03_Application_Intelligence.md`.
10. Update `prep/README.md` with the JD registry, terminology, answer cards, and questions.
11. After submission, record the sent date, channel, response, and outcome.

Active applications belong under `applications/`, not `reports/`.

### Changing a personal fact

1. Confirm the fact and evidence with Meshack.
2. Update `resumes/00_Master_Resume.md` first.
3. Search for every old version across the repository.
4. Update general and application builders manually.
5. Update LinkedIn/template/strategy copy where applicable.
6. Rebuild affected outputs.
7. Inspect output and check `git diff`.

### Ending a work session

Before stopping, leave durable state:

1. Update trackers and checklists with what actually happened.
2. Add a dated note to the “Latest handoff” section below.
3. Record commands needed to regenerate outputs.
4. Record unresolved questions and the next concrete action.
5. Check for accidental secrets, lock files, caches, or personal-data exposure.
6. Commit and push only when Meshack requests it; unpushed work will not appear on another
   computer.

---

## 10. Git, generated files, and portability

The repository is the memory only when changes are committed and pushed to GitHub.
Saving a local file is not enough for cross-computer continuity.

Application DOCX/PDF outputs are intentionally ignored by `.gitignore`. A fresh clone will
contain their source builders but not those generated files. Rebuild them using the commands
above.

The three general resume DOCX files are currently tracked. This mixed policy means:

- application documents must be regenerated after cloning;
- general resumes may exist but can be stale relative to their source;
- generated files must never override Markdown/Python source authority.

Do not commit:

- LibreOffice lock files such as `.~lock.*`
- `__pycache__/` or `.pyc` files
- virtual environments
- credentials, tokens, private keys, or `.env` files
- generated artifacts unless the repository policy intentionally tracks them

Known portability gap: `reports/Project_NDWH_CBS_Platform.md` references an external project
using an old absolute `/home/kenyaemr/...` path. That project does not travel with this
repository, so a new agent cannot independently verify it unless the external source is also
available.

This repository contains personal contact details, employment history, and application
recipient information. Treat it as private unless a deliberate privacy review says otherwise.

---

## 11. Known technical debt and credibility risks

- Builders duplicate master facts instead of importing structured canonical data.
- Several tailored builders use alternative current-role titles. Tailored positioning is
  useful, but official employment titles should remain canonical.
- Certification status and some metrics remain unconfirmed while generated documents may
  phrase them definitively.
- The current application tracker is ahead of `03_Application_Intelligence.md`.
- There is no automated drift check, test suite, requirements file, or output validation.
- Some generated/cache/LibreOffice lock artifacts have historically been tracked.
- General DOCX and application PDF/DOCX tracking policies are inconsistent.
- Historical application analysis references source material not fully represented under
  the current `applications/` directory.

High-value future engineering improvement: move canonical resume data into one structured
source consumed by all builders, then add consistency checks for titles, dates, metrics,
certifications, unresolved placeholders, and stale deadlines.

---

## 12. Latest handoff

### 2026-08-25

**State**

- Meshack needs applications out now (jobless / income-urgent). Remote health-informatics
  roles are scarce; browsing general remote boards is the practical channel.
- Added `08_Jobless_Remote_Volume_Playbook.md`: 60-second JD filter, daily cadence (5–8 apps/day,
  30–50/week), boards, message templates, and LinkedIn jobless-mode copy.
- LinkedIn `04_LinkedIn_Transformation.md` updated with JOBLESS / REMOTE VOLUME headline + About.
- Survival public identity: **IT Support & Systems Operations (remote-ready, Kenya)**; health
  EMR/DHIS2 stays as differentiator, not the only search target.
- Default CV while in this mode: `Meshack_Ariri_Resume_IT_Operations.docx` (CV-A).
- Long-term health-informatics strategy remains valid when those JDs appear.

**Next actions for Meshack**

1. Paste LinkedIn headline + About + Open to Work titles from the playbook today.
2. Align Experience titles/dates to Master Resume; employer = PATH.
3. Send 5 filtered remote IT/support applications today using CV-A.
4. Turn on green Open to Work; pin skills: Technical Support, Systems Administration, Microsoft 365.
5. Verify whether PATH employment is still "Present" — set end date truthfully if not.

**Rule for the next agent**

Do not replace this handoff with chat-only context. Update this section whenever the
operational state changes, keeping the newest dated entry first.

### 2026-07-16

**State**

- Career strategy remains Health Informatics / EMR–DHIS2 first.
- Ten application packages are built and recorded as unsent.
- Gas Africa is the nearest known deadline: 2026-07-21.
- The Royal Indigo/slate theme is implemented in `resumes/resume_theme.py`.
- Canonical PATH timeline is confirmed; LinkedIn alignment is not confirmed complete.

**Next actions**

1. Verify and submit Gas Africa before its deadline if still open.
2. Resolve the certification, metric, facilities, freelance, and GitHub questions above.
3. Synchronize the ten active applications into `03_Application_Intelligence.md`.
4. Reconcile tailored job titles against the canonical Master Resume.
