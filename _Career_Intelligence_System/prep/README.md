# The Rick-Speak Technical Handbook

> **Not a guide. A weapon.**  
> Built from every job description you've applied to. Grows every time you drop a new JD here.

**Last synced from JDs:** 2026-07-16 · **Roles indexed:** 10

---

## How this handbook works

1. **You apply to a role** → JD lands in `applications/[Role]/Job_Description.md`
2. **Keywords get extracted** → merged into the Master Lexicon below
3. **You drill daily** → pick today's cluster, run the Rick-Speak reps
4. **You interview** → pull answer cards from the matching JD cluster

**When you post a new JD here, add it to §8 and paste its keywords into §3.**

---

## §1 — Rick-Speak Protocol (how to sound brilliant)

Rick doesn't ramble. Rick reframes the problem, drops the real mechanism, and moves on.
You do the same — in interviews, not a cartoon voice.

### The 4-move pattern

| Move | What it does | Template |
|------|--------------|----------|
| **Reframe** | Show you see the actual problem | "The real issue wasn't [surface symptom] — it was [root cause]." |
| **Mechanism** | Name the system layer | "At the [network / identity / data / integration] layer, here's what was breaking." |
| **Proof** | One number or outcome | "After [action], we cut [metric] by [X]% / held [SLO] at [Y]." |
| **Close** | Land it | "That's not magic. That's [automation / governance / architecture]." |

### Weak → Rick-Speak upgrades

| You say (weak) | You say (Rick-Speak) |
|----------------|----------------------|
| "I fixed computers" | "I stabilized the endpoint layer — provisioning, patching, identity binding — so users stop breaking the same things twice." |
| "I did Excel reports" | "I built a validation pipeline. Garbage in gets flagged before it hits leadership dashboards. That's not reporting — that's data governance." |
| "I integrated an API" | "I mapped the contract, added idempotent sync, and reconciliation checks. Now source and destination either match or scream loudly. No silent drift." |
| "I supported users" | "I ran a tiered support model — L1 deflects noise, L2 owns root cause, L3 gets architecture. SLA isn't a poster on the wall; it's how we triage." |
| "I know Microsoft 365" | "I administer the full M365 stack — Entra ID for identity, Intune for endpoint posture, Exchange/SharePoint/Teams for collaboration, conditional access and MFA for the security boundary." |

### Interview rules (non-negotiable)

- **90 seconds max** per answer. Rick doesn't monologue.
- **Lead with mechanism**, not chronology.
- **One metric minimum** per story.
- **Never fake depth.** If you assisted, say "I supported" — then explain what *you* actually did.
- **Reframe before you solve.** "The ticket said Wi-Fi. The actual problem was DHCP scope exhaustion." — that's the energy.

---

## §2 — Daily drill (20 min, not a course)

| Min | Drill | Action |
|-----|-------|--------|
| 5 | **Lexicon flash** | Pick 5 terms from §3. Define in one line. Use in a PATH example. |
| 5 | **Rick rep** | Take one weak sentence from your CV. Rewrite using §1 table. Say it out loud. |
| 5 | **Card draw** | Pick 1 question from §5 matching tomorrow's interview track. 90-sec answer. Record yourself. |
| 5 | **JD mirror** | Open target JD. Find 3 keywords you didn't use today. Work them into one answer. |

**Weekly rotation:** Mon/Tue = M365 + identity · Wed = network + infra · Thu = data + APIs · Fri = support + escalation · Sat = stack/audit/CCaaS

---

## §3 — Master Lexicon (all JDs merged)

Train until these roll off your tongue. **Bold** = appears in 3+ JDs.

### Identity & endpoint (Bridge, Optimise, INSO, CCaaS, Solvo, Gas Africa)

| Term | One-liner | Rick-Speak example |
|------|-----------|-------------------|
| **Entra ID** | Microsoft's cloud identity plane (formerly Azure AD) | "Entra ID is the front door — who gets in, from where, with what posture." |
| **Active Directory** | On-prem directory for users, groups, GPO | "AD is the source of truth for on-prem identity until Entra syncs it to the cloud." |
| **MFA** | Multi-factor — something you know + something you have | "Passwords alone are a joke. MFA is the minimum viable security boundary." |
| **Conditional Access** | Policy engine: if user/device/location = X, then require Y | "Conditional access is zero-trust at the identity layer — not everyone gets the same door." |
| **Intune / MDM** | Mobile device management — enroll, configure, wipe, compliance | "Intune enforces endpoint posture before the device touches corporate data." |
| **Jamf** | MDM for macOS/iOS (MSP world) | "Jamf does for Apple fleet what Intune does for Windows — enrollment, config, compliance." |
| **DLP** | Data Loss Prevention — block sensitive data leaving the org | "DLP catches the 'oops I emailed the spreadsheet to the wrong person' before it ships." |
| **Endpoint protection** | AV/EDR on workstations and servers | "Endpoint protection is the immune system — detect, quarantine, report." |
| **User provisioning** | Create/disable accounts, assign licenses, group membership | "Provisioning isn't clicking 'new user' — it's lifecycle: onboard, change role, offboard, audit." |
| **GPO** | Group Policy — centralized Windows config | "GPO pushes config at scale so you're not RDP-ing into 120 machines one by one." |

### Microsoft 365 stack (every JD except Influx)

| Term | One-liner | Rick-Speak example |
|------|-----------|-------------------|
| **Exchange Online** | Cloud email/calendar | "Exchange Online is the mail plane — mail flow, retention, compliance." |
| **SharePoint Online** | Document collaboration + sites | "SharePoint is structured file chaos with permissions that actually matter." |
| **Teams** | Chat, meetings, collaboration hub | "Teams is where work happens — and where misconfigured guest access becomes a security incident." |
| **Microsoft 365** | Umbrella: identity + productivity + security | "M365 isn't 'Office' — it's identity, collaboration, compliance, and endpoint in one subscription." |
| **PowerShell** | Automation/scripting for Windows and M365 | "PowerShell turns repetitive admin into a one-liner pipeline. That's how you kill toil." |
| **Email migration** | Move mailboxes from on-prem or provider to M365 | "Migration is cutover planning — DNS, coexistence, throttling, rollback. Not just 'move the mailboxes.'" |

### Network & infrastructure (Gas Africa, ICT Manager, Optimise, Solvo, Thika, INSO)

| Term | One-liner | Rick-Speak example |
|------|-----------|-------------------|
| **LAN/WAN** | Local vs wide area network | "LAN is the building. WAN is how buildings talk. Break either and everyone's 'the internet is down.'" |
| **VLAN** | Logical network segmentation on one physical switch | "VLANs separate traffic without separate cables — guest Wi-Fi doesn't touch finance." |
| **DNS** | Name → IP resolution | "DNS fails, everything looks broken. Ping an IP works but google.com doesn't? That's DNS." |
| **DHCP** | Automatic IP assignment | "DHCP hands out addresses. Scope exhaustion looks like 'random devices can't connect.'" |
| **Firewall** | Traffic filter between zones | "Firewall is policy at the wire — allow, deny, log. Not a magic box." |
| **Wi-Fi** | Wireless access — APs, SSIDs, channels | "Wi-Fi issues are usually RF, DHCP, or auth — not 'the Wi-Fi is broken.'" |
| **Ping / Tracert** | Reachability and path diagnostics | "Ping answers 'is it alive?' Tracert answers 'where did the packet die?'" |
| **Backup / DR** | Copy data + plan to recover from disaster | "Backup without tested restore is wishful thinking. DR is 'how fast can we be back?'" |
| **Uptime / downtime** | Available vs unavailable time | "Uptime is an SLO. Downtime is what happens when you didn't design for failure." |
| **SPOF** | Single point of failure | "One router, one server, one person who knows the password — that's a SPOF. Fix it." |

### Support, ITSM & escalation (Influx, Optimise, Kuehne+Nagel, Solvo, INSO)

| Term | One-liner | Rick-Speak example |
|------|-----------|-------------------|
| **ITIL** | IT service management framework | "ITIL gives you language: incident, problem, change, request. Without it you're just firefighting." |
| **SLA** | Service level agreement — response/resolution targets | "SLA is the contract with the business. Miss it enough and they stop trusting IT." |
| **ITSM** | IT service management platform (tickets, workflows) | "ITSM is the system of record — every touch logged, categorized, escalated, closed." |
| **1st / 2nd / 3rd line** | Support tiers by depth | "L1 deflects and documents. L2 owns root cause. L3 owns architecture. Know your lane." |
| **Escalation** | Hand off when scope/expertise exceeded | "Escalation isn't failure — it's routing the problem to the layer that can actually fix it." |
| **RCA** | Root cause analysis | "RCA asks 'why' five times until you hit the thing that actually broke, not the symptom." |
| **Knowledge base** | Documented solutions for repeat issues | "KB turns tribal knowledge into deflection. Write it once, solve it a thousand times." |
| **Ticket quality** | Complete, categorized, reproducible records | "Bad tickets are archaeology. Good tickets have steps, screenshots, and closure notes." |
| **Service metrics** | Measured support performance | "You can't improve what you don't measure — first response time, resolution time, reopen rate." |

### Enterprise stack, CCaaS & audit (CCaaS, Bridge, ICT Manager)

| Term | One-liner | Rick-Speak example |
|------|-----------|-------------------|
| **CCaaS** | Contact Center as a Service — cloud call center platform | "CCaaS is telephony + routing + QA + reporting as a managed stack, not a PBX in a closet." |
| **VoIP / telephony** | Voice over IP — 3CX, Teams Phone, RingCentral | "VoIP is packets, not copper. QoS and routing matter or calls sound like garbage." |
| **SSO** | Single sign-on — one login, many apps | "SSO kills password sprawl. One identity provider, many apps, audited access." |
| **IAM** | Identity and access management | "IAM is who you are, what you can touch, and provable audit trail when something goes wrong." |
| **IT auditing** | Review what's deployed, used, licensed, secured | "Audit answers: what do we pay for, who uses it, who shouldn't, what's orphaned." |
| **License management** | Track software seats, renewals, compliance | "Licenses are money leaking out of the org if you don't reconcile seats to active users." |
| **Software stack management** | Own the full tool portfolio | "Stack management is portfolio thinking — deploy, integrate, measure utilization, kill waste." |
| **ROI analysis** | Return on investment for tool/process decisions | "ROI isn't vibes — cost vs time saved vs risk reduced. Present it or don't ask for budget." |
| **Use-case plan** | Business case before buying/deploying tools | "No use-case plan, no deployment. What problem, who uses it, how measured, what's the fallback." |
| **Tool onboarding** | Framework for rolling out new tools to staff | "Onboarding is provisioning + training + SOP + support runway. Not 'here's the link, figure it out.'" |

### Data, integration & analytics (your PATH edge + Bridge + CCaaS)

| Term | One-liner | Rick-Speak example |
|------|-----------|-------------------|
| **API integration** | Systems talk via defined endpoints | "API integration is contract-first — schema, auth, retries, idempotency, reconciliation." |
| **Middleware** | Glue between systems (Zapier, custom scripts) | "Middleware is the duct tape that stops humans from being the integration layer." |
| **Reconciliation** | Compare source vs destination for mismatches | "Reconciliation catches drift before leadership reports fiction." |
| **Data quality / DQA** | Accuracy, completeness, timeliness, consistency | "DQA is the immune system for reporting — validate before publish." |
| **ETL** | Extract, transform, load | "ETL moves data from messy source to clean destination with rules in the middle." |
| **Dashboard** | Visual decision layer (Power BI, Grafana) | "Dashboards aren't decoration — they're the SLA for decision speed." |
| **Power BI** | Microsoft's BI/visualization tool | "Power BI turns SQL output into something a director can act on in 30 seconds." |
| **Schema drift** | Upstream data structure changed, downstream broke | "Schema drift is silent death for integrations. Version your contracts." |
| **Idempotency** | Repeat request ≠ duplicate outcome | "Idempotent sync means you can retry without creating ghost records." |

### Security & compliance (Thika, Gas Africa, INSO, ICT Manager, Optimise)

| Term | One-liner | Rick-Speak example |
|------|-----------|-------------------|
| **Cybersecurity** | Protect confidentiality, integrity, availability | "Security is CIA triad — not antivirus and prayers." |
| **Phishing response** | Detect, contain, educate after social engineering | "Phishing response is isolate, reset creds, scan, educate — in that order." |
| **Compliance** | Meet policy/regulatory/organizational standards | "Compliance is provable adherence — logs, configs, access reviews, not good intentions." |
| **Data protection** | Safeguard sensitive data at rest and in transit | "Data protection is encryption, access control, and knowing where the data actually lives." |
| **Access control** | Who can reach what resources | "Access control is least privilege — give the minimum door keys required for the job." |

### Customer-facing & soft-power terms (Influx, Kuehne+Nagel, INSO)

| Term | One-liner | Rick-Speak example |
|------|-----------|-------------------|
| **Customer-focused** | User outcome > ticket closure | "Customer-focused means the user's problem is solved, not that I closed a ticket." |
| **Empathetic** | Acknowledge frustration before solving | "Empathy is 'I get why this is blocking you' before 'have you tried rebooting.'" |
| **Cross-cultural** | Work across countries, time zones, norms | "Cross-cultural is async communication, clear docs, and zero assumptions about context." |
| **Process improvement** | Redesign workflow to reduce friction | "Process improvement is measuring the loop, finding the bottleneck, killing the toil." |
| **Documentation** | Written record of config, process, solution | "If it's not documented, it doesn't exist when you leave or when it's 2am." |

---

## §4 — JD clusters (which lexicon to drill per role)

| Cluster | Roles | Drill focus |
|---------|-------|-------------|
| **A — MSP / 2nd-3rd line** | Optimise Outsourcing | M365 deep, Intune/Jamf, VLANs, IT Glue, escalation, RCA, SLA |
| **B — Enterprise stack / CCaaS** | System Administrator CCaaS | CCaaS, SSO, IAM, IT audit, license mgmt, ROI, executive presentation |
| **C — INGO / global support** | INSO | Remote support, travel, compliance, SharePoint, Intune, French+English, austere env |
| **D — Internal sysadmin / ownership** | Bridge Talent, Gas Africa, ICT Manager | M365, Entra, PowerShell, VoIP, CRM, API integration, vendor mgmt |
| **E — L1 / helpdesk / customer** | Influx, Solvo Global | Ticketing, KB, escalation, empathy, Windows setup, DNS/Ping, documentation |
| **F — Logistics / process** | Kuehne+Nagel | Incident handling, service metrics, process improvement, mentoring, global collab |
| **G — Hybrid tech** | Thika SysAdmin | Infra + web dev + CMS + cybersecurity — bridge both stacks in answers |

---

## §5 — Answer cards (Rick-Speak, mapped to your PATH work)

### Card 1 — "Tell me about yourself" (universal)

> I'm a systems and data operations person. I don't just close tickets — I fix the layer underneath.
>
> At PATH I've gone from ICT intern to HMIS officer supporting national-scale systems. I run the full loop: keep platforms up, automate reporting with Excel VBA and SQL, integrate APIs for national data sync, and build dashboards that leadership actually uses.
>
> Whether it's M365 and endpoint support, network troubleshooting, or data pipeline validation — I speak both technical and business. Give me a fragile process and I'll show you the mechanism that's breaking and the metric that proves it's fixed.

### Card 2 — M365 / identity (Optimise, Bridge, INSO, Gas Africa)

> The real problem in most orgs isn't "email is slow" — it's identity sprawl. Orphaned accounts, over-licensed seats, no conditional access.
>
> I administer Entra ID and Active Directory — provisioning, group policy, MFA, least-privilege access. I've supported 120+ users across Microsoft 365: Exchange, Teams, SharePoint. When onboarding, I don't just create an account — I run a lifecycle: device, identity, apps, training, documented.
>
> That's not helpdesk work. That's identity governance.

### Card 3 — Escalation / tiered support (Optimise, Kuehne+Nagel, Solvo, Influx)

> I work a tiered model. L1 gets the symptom and the KB article. L2 gets root cause — DNS, DHCP, auth, config. L3 gets architecture.
>
> At PATH I logged and tracked incidents in Freshdesk with ITIL workflows, met SLAs, and improved response time ~25%. I know when to own it and when to escalate with a clean handover — steps to reproduce, what I tried, what layer I think it's on.
>
> Escalation isn't failure. Bad escalation is.

### Card 4 — Network troubleshooting (Gas Africa, Solvo, Optimise, ICT Manager)

> Ticket says "internet is down." I don't guess. Ping for reachability. Tracert for path. DNS check for resolution. DHCP scope for address exhaustion. VLAN and firewall for segmentation.
>
> I've supported LAN/WAN, Cisco Meraki APs and switches, structured cabling, guest and staff Wi-Fi. The actual problem is usually one layer down from what the user reports.
>
> That's network diagnostics — not rebooting the router and hoping.

### Card 5 — API / data integration (PATH NDWH — your killer card)

> We had facility data that needed to hit the National Data Warehouse. Manual export was slow, error-prone, and silently drifted.
>
> I mapped the API contract, built validation and sync logic, and added reconciliation so source and destination either match or flag. Combined with SQL checks and Excel VBA automation for the reporting layer, we cut manual processing time ~40% and improved timeliness for national reporting.
>
> That's not "I did reports." That's data pipeline engineering with a governance layer.

### Card 6 — Dashboards / analytics (PATH + CCaaS + Bridge)

> Dashboards are useless if the data underneath is garbage. I validate first — completeness, consistency, timeliness — then visualize.
>
> I've built Power BI and Grafana dashboards for care & treatment, PMTCT, and program surveillance. Leadership doesn't need more charts. They need one chart they can trust. DQA before publish is how you earn that trust.

### Card 7 — IT audit / stack management (CCaaS, Bridge)

> Every org bleeds money on shelfware — licenses nobody uses, tools nobody integrated, access nobody revoked.
>
> I run software stack audits: what's deployed, who's active, what's orphaned, what overlaps. I track hardware and license inventory, coordinate vendor renewals, and build use-case plans before new tools land. ROI isn't a slide deck — it's utilization data plus time saved.
>
> That's portfolio management, not IT shopping.

### Card 8 — Customer support / remote (Influx, INSO)

> Customer support is triage with empathy. User is blocked — acknowledge it, reproduce it, solve it or escalate with a clean ticket.
>
> I've supported 120+ users, documented in knowledge bases, and trained 80+ staff on digital tools. I explain technical fixes in plain language. Calm under pressure, detail on documentation, ruthless about categorization.
>
> The user doesn't care about your OSI model. They care that it's fixed and won't happen again.

### Card 9 — CCaaS / telephony (CCaaS, Bridge, ICT Manager)

> Contact center infrastructure is telephony + routing + QA + reporting + identity — not a phone on a desk.
>
> I've worked with VoIP/3CX integrated with Freshdesk ITSM — ITIL workflows, SLA tracking, call routing. CCaaS adds QA modules, analytics, SSO, and security protocols on top. I understand the full stack even if I wasn't the one who architected the platform from zero.
>
> Peak performance means integrated modules, not siloed tools duct-taped together.

### Card 10 — "Greatest weakness" (Rick reframe)

> I used to over-own — stay on a ticket past the escalation point because I wanted to crack it. That's ego, not efficiency.
>
> Now I timebox diagnosis, document what I've tried, and escalate with a clean handover at the right tier. Faster resolution, better ticket quality, less hero culture. The system wins, not my pride.

---

## §6 — Rapid-fire Q&A (Rick-Speak one-liners)

| Question | Rick-Speak answer |
|----------|------------------|
| How do you prioritize tickets? | Impact × urgency × SLA breach risk. P1 is down business. P4 is "my mouse feels weird." |
| What's your troubleshooting process? | Reproduce → isolate layer → test hypothesis → fix → document → prevent recurrence. |
| How do you handle a user who can't explain the problem? | Ask what they were doing, what they expected, what happened. Screenshots. Remote session. Don't guess. |
| Difference between incident and problem? | Incident is the fire. Problem is the faulty wiring that keeps starting fires. |
| How do you secure endpoints? | Patch, protect (EDR), posture (Intune), identity (MFA/CA), least privilege, audit. |
| How do you handle confidential data? | Need-to-know access, encryption, DLP where available, no sharing via personal channels, log it. |
| Experience with automation? | PowerShell for provisioning, VBA for reporting pipelines, SQL for validation. Kill toil. |
| How do you learn new systems fast? | Docs → sandbox → break it → fix it → document what I learned. |
| Why should we hire you? | I fix mechanisms, not symptoms. I measure outcomes. I document so the next person isn't guessing. |

---

## §7 — SRE / reliability terms (book layer — use when they go deep)

Pulled from Google SRE thinking. Use when interviewers ask "how do you think about reliability?"

| Term | Rick-Speak |
|------|------------|
| **SLI** | The number you actually measure — uptime, error rate, latency. |
| **SLO** | The target for that number — 99.5% availability, <200ms p95. |
| **Error budget** | How much failure you're allowed before you stop shipping features and fix reliability. |
| **Toil** | Manual, repetitive, automatable work. My job is to murder toil. |
| **Blameless postmortem** | After an incident: what broke, why, what we change. No witch hunts. |
| **MTTR** | Mean time to recover. How fast you're back, not how fast you found it. |
| **Observability** | Logs, metrics, traces — can you see inside the system when it misbehaves? |
| **Alert fatigue** | Too many noisy alerts → real ones get ignored. Tune or die. |

**Rick-Speak reliability answer:**
> I treat uptime like an SLO, not a hope. I measure SLIs, automate the toil out of reporting and provisioning, and when something breaks we run a blameless postmortem and fix the mechanism. MTTR matters more than MTBF when users are waiting.

---

## §8 — JD registry (living index)

*Add a row every time you apply to a new role.*

| # | Role | Employer | Cluster | JD path | Keywords added |
|---|------|----------|---------|---------|----------------|
| 1 | ICT Manager | Hospitality (Hotel) | D | `applications/ICT Manager - Hospitality/` | PMS, POS, keycard, 24/7, AV, vendor mgmt |
| 2 | IT Support Engineer 2nd-3rd Line | Optimise Outsourcing | A | `applications/IT Support Engineer 2nd-3rd Line - Optimise Outsourcing/` | M365 deep, Intune, Jamf, DLP, IT Glue, MSP |
| 3 | IT Systems Administrator | Thika (HCO) | G | `applications/IT Systems Administrator (Web Dev) - Thika/` | Web dev, CMS, WordPress, ERP, cybersecurity |
| 4 | System Administrator | CCaaS (unnamed) | B | `applications/System Administrator - CCaaS/` | CCaaS, audit, ROI, license mgmt, SSO |
| 5 | ICT Officer | Gas Africa | D | `applications/ICT Officer - Gas Africa/` | ICT systems, uptime, asset tracking, vendor |
| 6 | Customer Support Specialist | Influx | E | `applications/Customer Support Specialist - Influx/` | Remote support, KB, empathy, CRM, escalation |
| 7 | IT Support Technician | Solvo Global | E | `applications/IT Support Technician - Solvo Global/` | Windows setup, Ping/Tracert/DNS, ITSM, night shift |
| 8 | IT & Systems Administrator | Bridge Talent | D | `applications/IT & Systems Administrator - Bridge Talent/` | Entra, Intune, PowerShell, Zoho, VoIP, API |
| 9 | IT Officer – Global Support | INSO | C | `applications/IT Officer Global Support - INSO/` | INGO, French, travel, compliance, remote |
| 10 | IT Specialist | Kuehne+Nagel | F | `applications/IT Specialist - Kuehne+Nagel/` | Logistics, service metrics, process improvement |

---

## §9 — New JD intake (paste this when you drop a new role)

When you post a new JD, run this checklist:

```
NEW JD INTAKE
─────────────
Role:
Employer:
Cluster (A–G): 
Top 10 keywords from JD:
3 terms I didn't know before:
1 Rick-Speak answer to add:
PATH story that maps to this role:
```

Then:
1. Add row to §8 registry
2. Add new terms to §3 lexicon
3. Write 1 answer card in §5 if the role needs a new angle

---

## §10 — Sources (where terms come from)

| Source | What we pull |
|--------|--------------|
| **Your 10 JDs** | §3, §4, §8 — primary source, always current |
| **Google SRE book** | §7 — SLI/SLO/error budget/toil/postmortem language |
| **Your PATH work** | §5 answer cards — proof layer |
| **New JDs you post** | §9 intake → auto-grows handbook |

---

*Drop the next JD. This handbook eats it and gets sharper.*
