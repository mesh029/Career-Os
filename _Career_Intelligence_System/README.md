# Meshack Ariri — Career Intelligence System

This repository is the durable memory for Meshack Ariri's career work. AI chat history,
computer-local settings, and agent memory may disappear; the versioned files in this
repository must contain enough context for a person or a fresh agent to continue safely.

> **Start with this README, then read `00_SYSTEM_PROMPT.md`. Do not rely on a previous chat.**

**Last continuity update:** 2026-09-02
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
| 4 | `applications/<Employer Role>/Job_Description.md` | Captured requirements for one role |
| 5 | `applications/<Employer Role>/Application_Intelligence.md` | Fit analysis and honest positioning |
| 6 | `applications/<Employer Role>/build.py` | Renderable role-specific content |
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

Snapshot from `applications/APPLICATIONS_TRACKER.md`, last updated 2026-09-02:

- **Apply today:** Technical Support Agent L2 — BruntWork healthcare MSP (posted 31 Aug 2026, immediate hiring). Portal: assessment + tech check + voice. Pack built. Apply score ~84%.
- **Email by Sep 14:** ICT Officer — USIU-Africa.
- Older packages remain recorded as unsent; verify those listings before sending.

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
| `reports/Opportunity_Scour_2026-08-25.md` | Live career-page + remote-board scour with links and suitability |
| `downloads/` | Ready-to-download CVs (DOCX+PDF) + apply-links README from chat |
| `resumes/00_Master_Resume.md` | Canonical facts and master bullet bank |
| `resumes/resume_theme.py` | Shared palette, fonts, and contact header |
| `resumes/build_resumes.py` | Builds the three general DOCX resumes |
| `resumes/pdf_builder.py` | Shared ReportLab renderer for application PDFs |
| `applications/APPLICATIONS_TRACKER.md` | Active application pipeline |
| `applications/<Employer Role>/` | JD, analysis, builder, messages, and generated package |
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

The general builder creates DOCX + PDF for the three tracks (filenames stay underscored there because they live together in `resumes/` / `downloads/`).

### One application package

```bash
python3 "applications/Gas Africa ICT Officer/build.py"
```

Each application builder creates four files with the same names in every folder:

- `Meshack Ariri CV.docx`
- `Meshack Ariri Cover Letter.docx`
- `Meshack Ariri CV.pdf`
- `Meshack Ariri Cover Letter.pdf`

The folder already names the job (`Employer Role`, spaces, no hyphens). Do not use `Role - Employer` or underscored filenames.

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

**Current theme:** Editorial Light — navy type on white paper, copper accent. No full-width dark header.

| Token | Hex | Use |
|---|---|---|
| Navy | `#0F2744` | Name, section titles |
| Copper | `#C45C26` | Hairline, toolkit labels, bullets, metric values |
| Copper soft | `#E8C4A8` | Metric dividers |
| Sand | `#F6EFE6` | Metric chips |
| Cream | `#FBF7F2` | Toolkit wash |
| Slate | `#1E293B` | Body text |
| Muted slate | `#64748B` | Dates, contact, captions |

Fonts:

- DOCX: Calibri
- PDF: Helvetica

Layout:

- ATS-safe, single column, real text (no icons, photos, or skill bars)
- Light header: navy name, copper hairline, no dark band
- Optional metric chips under the header (`metrics` on the CV dict)
- Skills as a copper-rail toolkit ribbon (never a "Core Skills" heading)
- Education and certifications as one full-width Credentials strip (never a two-column footer)
- Uppercase section titles with a copper rule
- Dark body text on white

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
2. Create `applications/<Employer Role>/` (spaces, no hyphens, no `Role - Employer`).
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

### 2026-09-14 (ILRI ICT Technician Digital Workplace Services)

**State**

- Pack: `applications/ILRI ICT Technician Digital Workplace Services/`
- Nairobi, Kenyan nationals, HG12. Deadline **28 Sep 2026**. REF: **ICT-CS/2308-09/2026**. Apply **~87%**.
- Canonical PATH titles. Intune = equivalent, not tenant. Copilot = adoption, not rollout lead. Fill referee phones.
- Rebuild: `python3 "applications/ILRI ICT Technician Digital Workplace Services/build.py"`

### 2026-09-14 (St. Kizito Vocational Centre ICT Trainer)

**State**

- Pack: `applications/St Kizito Vocational Centre ICT Trainer/`
- Utawala, Nairobi. Deadline **16 Sep 2026**. Apply **~83%**.
- Training + equipment. No TSC. Relocate. Google Form.
- Rebuild: `python3 "applications/St Kizito Vocational Centre ICT Trainer/build.py"`

### 2026-09-10 (BruntWork IT Microsoft Support Specialist)

**State**

- Pack: `applications/BruntWork IT Microsoft Support Specialist/`
- Seattle healthcare client. 20h, Pacific business hours = **7:00–11:00 PM EAT**. Apply **~87%** if the window is real.
- Not the AEST M365 MSP pack. Not the EST healthcare L2 pack. Do not claim HIPAA, MS-900, or A+.
- Portal: `Portal_Application_Pack.md` (assessment + voice).
- Rebuild: `python3 "applications/BruntWork IT Microsoft Support Specialist/build.py"`

### 2026-09-10 (Corus Senior IT Service Desk Specialist)

**State**

- Pack: `applications/Corus Senior IT Service Desk Specialist/`
- Washington DC hybrid Tue/Wed. US work authorization required. Apply **~45%** because of that gate, not because the NGO service desk story is weak.
- Cover is honest: Kenya, no US work auth. Intern off.
- Rebuild: `python3 "applications/Corus Senior IT Service Desk Specialist/build.py"`

### 2026-09-10 (Influx Technical Support Agent L2)

**State**

- Pack: `applications/Influx Technical Support Agent L2/`
- Kenya WFH, 44h, 24x7 staggered 5-day. Intern off. L2 titles this CV only.
- Apply score **~85%**. Not the Customer Support Specialist pack.
- Apply: official Influx only (@influx.com). Portal answers in `Portal_Application_Pack.md`.
- Rebuild: `python3 "applications/Influx Technical Support Agent L2/build.py"`

### 2026-09-10 (Tier 3 IT Support and NOC Engineer)

**State**

- Pack: `stretch/Tier 3 IT Support NOC Engineer/`
- Stretch. Intern off. Current PATH line = Tier 3 IT Support and NOC Engineer. ICT era = Network Operations Engineer.
- Apply score **~85%**. Employer not in the paste. Swap cover greeting when named.
- Rebuild: `python3 "stretch/Tier 3 IT Support NOC Engineer/build.py"`

### 2026-09-10 (Technical Support Agent base pack)

**State**

- Pack: `applications/Technical Support Agent/`
- Reusable TSA CV. Service desk first. Programming as product diagnostics, application engineering (React, Next.js, Express, Flutter), and assembly-level systems internals.
- PATH titles canonical. Independent line carries the engineering.
- Rebuild: `python3 "applications/Technical Support Agent/build.py"`
- Clone and retarget the cover per employer. Not a substitute for BruntWork L2, Cigna, or Influx customer-support packs.

### 2026-09-08 (Wave HR Systems Analyst)

**State**

- Pack: `stretch/Wave HR Systems Analyst/`
- Kenya remote, UTC+3, pay USD 66.4k–75.8k plus equity.
- HMIS unchanged. ICT era = People Systems and Identity Administrator. Intern off. No ECD line.
- Apply score **~82%**. ICT era = HRIS and People Systems Analyst. Workday as HCM implementation posture.
- Apply: English CV + cover on Wave form.
- Rebuild: `python3 "stretch/Wave HR Systems Analyst/build.py"`

### 2026-09-08 (G Adventures Tour Staff Administrator)

**State**

- Pack: `stretch/G Adventures Tour Staff Administrator/`
- Titles this CV only: ECD = Field Programme Administrator, Nuru ya Mtoto; ICT era = Regional Operations and Staff Administrator; HMIS unchanged.
- Apply score **~68%**. Not G Adventures, not tour leader, not tourism diploma.
- Rebuild: `python3 "stretch/G Adventures Tour Staff Administrator/build.py"`

### 2026-09-08 (Simera Project Assistant)

**State**

- Pack: `stretch/Simera Project Assistant/` (not the Coordinator pack).
- Apply score **~85%**. Intern off. **Nuru ya Mtoto / ECD** is the lead story.
- Upload `Meshack Ariri CV.pdf` from that folder.
- Rebuild: `python3 "stretch/Simera Project Assistant/build.py"`

### 2026-09-08 (Simera Project Coordinator)

**State**

- Pack: `stretch/Simera Project Coordinator/` (hard-positioned; not under `applications/`).
- Apply score **~84%**. Intern omitted. PATH titles canonical. Independent = freelance SMB + County Health Systems Operations Platform.
- Upload `Meshack Ariri CV.pdf` from that folder. Portal answers in `Portal_Application_Pack.md`.
- Rebuild: `python3 "stretch/Simera Project Coordinator/build.py"`

### 2026-09-08 (Bandari Maritime Academy ICT Officer I)

**State**

- Pack: `applications/Bandari Maritime Academy ICT Officer I/` (ref **BMA/26/CEO/ICT1/17**).
- Apply score **~86%**. CCNA + 3 years comparable ICT. Do not claim PSC grade or MCSE.
- Deadline **29 Sep 2026 5:00 PM EAT**. Google Form then email **recruitment@bma.ac.ke**, subject **BMA/26/CEO/ICT1/17 ICT Officer I**.
- Nairobi on-site, permanent and pensionable. Relocate. Pay is public-sector, not Cigna.
- Send USIU and Aga Khan first (both **14 Sep**).
- Rebuild: `python3 "applications/Bandari Maritime Academy ICT Officer I/build.py"`

### 2026-09-07 (BruntWork IT Operations Specialist)

**State**

- Pack: `applications/BruntWork IT Operations Specialist/` (published 7 Sep 2026).
- Apply score **~68%**. Named-tool miss: SimplePractice, Stripe, social scheduler, HIPAA-trained.
- Hours: 9 AM–6 PM US Central = **5:00 PM–2:00 AM EAT** (CDT), 40 hours. Do not stack with PATH.
- Healthcare L2 remains the better BruntWork bet (~84%, 4–8 PM EAT, 20h) if still open.
- Apply: Candidate Portal. Assessment + technical check + voice. Use that folder’s `Portal_Application_Pack.md`.
- Rebuild: `python3 "applications/BruntWork IT Operations Specialist/build.py"`

### 2026-09-07 (Cigna Technical Customer Support Analyst)

**State**

- Pack: `applications/Cigna Technical Customer Support Analyst/` (Nairobi, hybrid 66/34).
- Apply score **~83%**. Service Desk + IMAC + AD + SLA + healthcare is the shortlist case.
- Do not claim Citrix, SCCM, ServiceNow, or Avaya. ITIL practice, not Foundation exam.
- Rota is the filter: Sat 8 AM–1 PM every 3 weeks; Mon–Fri 4 PM–midnight every 6 weeks (from home).
- Apply: https://cigna.wd5.myworkdayjobs.com — upload `Meshack Ariri CV.pdf`.
- Rebuild: `python3 "applications/Cigna Technical Customer Support Analyst/build.py"`

### 2026-09-02 (night — CMMB Kenya IT Specialist volunteer)

**State**

- Pack: `applications/CMMB Kenya IT Specialist Volunteer/` (category listing only; no detailed JD).
- Apply as **Kenya local volunteer**, not the US international $5,000 / NYC orientation track.
- Score **~89%**. PATH health-facility IT is the edge. Do not claim ECHIS.
- Apply: https://cmmb.org/volunteernow/ + volunteer@cmmb.org + CMMB Kenya contact form.
- Confirm 6–12 months and PATH overlap before sending.

### 2026-09-02 (night — Aga Khan Academy IT Associate)

**State**

- Pack: `applications/Aga Khan Academy IT Associate/` (job **4954BR**, deadline **14 Sep 2026**).
- Apply score **~87%**. First-line + infra + security + assets match. Do not claim IB LMS or pentest lead.
- Nairobi campus: relocate. Same deadline as USIU: submit both.
- Apply: https://www.akdn.org/careers (search 4954BR) / Brassring.
- Rebuild: `python3 "applications/Aga Khan Academy IT Associate/build.py"`

### 2026-09-02 (night — BruntWork Microsoft 365 MSP, AEST)

**State**

- Second BruntWork posting packed: `applications/BruntWork Microsoft 365 MSP Support/` (published 1 Sep 2026).
- Apply score **~77%**. Honest gaps: no Intune/Defender/Copilot console, no named RMM. M365 + Entra + backups are real.
- **Hours:** 9 AM–1 PM AEST = **2:00–6:00 AM EAT** (1:00–5:00 AM after AU DST). Apply only if that window is real. Do not stack with healthcare L2 without a sleep plan.
- Healthcare L2 remains the better BruntWork bet (~84%, 4–8 PM EAT, 3CX + healthcare edge).
- Rebuild: `python3 "applications/BruntWork Microsoft 365 MSP Support/build.py"`

**Next actions**

1. Decide hours first. If 2 AM is a no, skip this posting.
2. If yes: portal in one sitting using that folder's `Portal_Application_Pack.md`. Do not paste HIPAA answers.
3. Upload `Meshack Ariri CV.pdf` from that folder.

### 2026-09-02 (evening — folder standard + Editorial Light CV)

**State**

- Every job lives in `applications/Employer Role/` (spaces, no hyphens). Same four output names in every pack: `Meshack Ariri CV.pdf` / `.docx` and `Meshack Ariri Cover Letter.pdf` / `.docx`.
- CV theme is **Editorial Light**: navy on white, copper accent, no dark header block. Core Skills replaced by a toolkit ribbon.
- All 12 application packs rebuilt on the new theme. BruntWork L2 remains **one page**.
- Preview: `reports/cv_visual_targets/Meshack_Ariri_CV_L2_preview.png`
- Apply copies: `applications/BruntWork Technical Support L2/` and `downloads/JOBS/BruntWork Technical Support L2/`

### 2026-09-02 (BruntWork Technical Support Agent L2 — healthcare MSP)

**State**

- Meshack pasted a live BruntWork posting (published 31 Aug 2026): **Technical Support Agent Level 2** for a healthcare-only MSP, 20 hrs/week, Mon–Fri 9:00 AM–1:00 PM Eastern (Kenya 4–8 PM EAT during US daylight time).
- Full Phase 5 pack: `applications/BruntWork Technical Support L2/`
  - JD, intelligence (~84% apply), portal/voice/HIPAA pack, tailored CV + cover (DOCX+PDF).
- This is the BruntWork IT opening the 2026-08-25 scour said to watch: remote L2 + healthcare + 3CX plus.
- Honest gaps: not a named US MSP; no Enable/N-able production; no US HIPAA certificate. Do not fabricate those.
- Contractor pay is likely low vs NGO IT; treat as income floor, not destination.
- PATH Master Resume still says **Present**. Confirm end date / moonlighting before signing a BAA.
- Tracker, `03_Application_Intelligence.md` log, and `prep/README.md` (JD11) updated.
- Rebuild: `python3 "applications/BruntWork Technical Support L2/build.py"`

**Next actions for Meshack**

1. **Apply today** on the BruntWork Candidate Portal. Complete assessment + technical check + voice in one sitting (incomplete apps are deprioritized).
2. Use `Portal_Application_Pack.md`: record the voice script twice; study the HIPAA cheat sheet; paste assessment answers in your own voice.
3. Upload `Meshack Ariri CV.pdf` from that folder.
4. After submit, log date/time in `applications/APPLICATIONS_TRACKER.md`.
5. USIU ICT Officer remains a separate Sep 14 email application; do not let this replace it.

### 2026-08-25 (CVs + apply links packaged)

**State**

- Regenerated all 3 resume tracks as **DOCX + PDF** in `resumes/` and `downloads/`.
- Apply links from chat packaged in `downloads/README.md`.
- Artifacts also copied under `/opt/cursor/artifacts/meshack-cvs/` for download in the agent UI.
- Default jobless CV: `Meshack_Ariri_Resume_IT_Operations.pdf` / `.docx`.

**Next actions for Meshack**

1. Download IT Operations CV and start Influx / Amref / IntelliSOFT / MOHI applications.
2. Use INGO CV for NGO ICT; Health Informatics CV for IntelliSOFT / HIS roles.

### 2026-08-25 (evening — opportunity scour)

**State**

- Web scour completed for NGO career pages, BruntWork, Remote4Africa, Influx, Pavago, IRC, Amref, IntelliSOFT, CarePay, Living Goods, CHAI.
- Report: `reports/Opportunity_Scour_2026-08-25.md` with links + suitability.
- BruntWork classic IT Support posts mostly **closed** today; open adjacent: Lead Triage Administrator (EMR clinic).
- Strongest immediate applies: Influx Tier 2, MOHI IT Support Officer, Amref ICT talent pool, IntelliSOFT talent database, Remote4Africa IT Ops Specialist, Pavago Tech Support.

**Next actions for Meshack**

1. Submit Amref General Interest + IntelliSOFT talent database today.
2. Apply Influx Tier 2 + MOHI (if faith requirement OK) + Remote4Africa IT Ops.
3. Check BruntWork daily for new IT Support/MSP posts.
4. Send any still-open packages from APPLICATIONS_TRACKER (Solvo, Gas Africa if live).

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
- The Editorial Light (navy + copper) theme is implemented in `resumes/resume_theme.py`.
- Canonical PATH timeline is confirmed; LinkedIn alignment is not confirmed complete.

**Next actions**

1. Verify and submit Gas Africa before its deadline if still open.
2. Resolve the certification, metric, facilities, freelance, and GitHub questions above.
3. Synchronize the ten active applications into `03_Application_Intelligence.md`.
4. Reconcile tailored job titles against the canonical Master Resume.
