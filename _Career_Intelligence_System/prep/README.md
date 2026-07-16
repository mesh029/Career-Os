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

**Morning read (primary):** §11 — 10 questions for today's JD. Say every Rick answer out loud before coffee wears off.

**Weekly rotation:** Mon=JD01 · Tue=JD02 · Wed=JD03 · Thu=JD04 · Fri=JD05 · Sat=JD06 · Sun=JD07–10 catch-up

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
4. **Add 10 interview Q&As with Rick answers to §11** (same format as existing JDs)

---

## §10 — Sources (where terms come from)

| Source | What we pull |
|--------|--------------|
| **Your 10 JDs** | §3, §4, §8 — primary source, always current |
| **Google SRE book** | §7 — SLI/SLO/error budget/toil/postmortem language |
| **Your PATH work** | §5 answer cards — proof layer |
| **New JDs you post** | §9 intake → auto-grows handbook |

---

## §11 — Morning Drill: 100 Interview Questions (10 per JD)

**How to use:** Read **10 questions/day** — rotate by JD number (Day 1 = JD01, Day 2 = JD02… Day 10 = JD10, repeat).
Say each **Rick answer** out loud. Under 90 seconds. One PATH proof per answer where it fits.

---

### JD01 — ICT Manager · Hospitality · Cluster D

**Q1. Guest Wi-Fi is down during peak check-in. Walk us through your response.**  
**Rick:** P1 incident — guest-facing revenue is bleeding. I isolate: AP status, controller, DHCP scope, ISP uplink. Fix the layer, not the symptom. Communicate ETA to front desk every 15 min. Post-incident: blameless review — was it capacity, config drift, or no monitoring? At PATH I held ~98% uptime across multi-site Wi-Fi by treating guest connectivity as an SLO, not a nice-to-have.

**Q2. How would you manage PMS, POS, and keycard systems as one ecosystem?**  
**Rick:** They're not three tools — they're one guest journey. PMS is source of truth for occupancy; POS feeds revenue; keycard is physical auth tied to reservation state. I document integrations, test failover, and run vendor SLAs like contracts. Break one link and check-in becomes chaos. Portfolio thinking, not silo admin.

**Q3. The GM wants a technology upgrade but budget is tight. How do you advise?**  
**Rick:** ROI or no slide deck. I audit current stack utilization, quantify downtime cost, and rank upgrades by risk × impact. Quick wins first — license reclamation, automation, security gaps. Big capex gets a use-case plan: problem, users, metric, fallback. That's how you get CEO sign-off without vibes.

**Q4. Describe your approach to cybersecurity in a 24/7 hospitality environment.**  
**Rick:** CIA triad at every layer — guest network segmented from staff, firewall policy, endpoint protection, MFA on admin, patched servers, tested backups. CCTV and access control are part of the surface. Security isn't a project; it's posture plus incident response: isolate, contain, restore, educate.

**Q5. How do you handle vendor and ISP relationships?**  
**Rick:** Vendors are part of your stack whether you like it or not. I keep live inventory, contract dates, escalation contacts, and SLA evidence. When they miss SLA, I log it and renegotiate from data. ISPs get monitored uplink metrics — don't wait for guests to tweet about outage.

**Q6. Conference AV fails 30 minutes before a corporate event. What do you do?**  
**Rick:** Contain panic, run the checklist: input source, HDMI handshake, audio routing, codec, network for VC. Spare adapter kit exists because Murphy lives in event rooms. Parallel path: phone bridge backup. After: document the config that worked and label the ports. AV failures are always "it worked yesterday."

**Q7. How do you prioritize when every department says their issue is urgent?**  
**Rick:** Impact × urgency × SLA. Guest-facing and revenue-blocking beat internal printer drama. I triage openly — "here's the queue, here's why you're third." Transparency kills politics. At PATH I handled 20+ tickets/day without hero culture by making priority logic visible.

**Q8. How do you maintain hardware/software license inventory?**  
**Rick:** If it's not in inventory, it doesn't exist for audit or renewal. Asset tag, owner, warranty, license seat, last audit date. Quarterly reconcile: active users vs. paid seats. Orphaned licenses are cash on the table. I've run stack audits that cut waste before asking for new budget.

**Q9. Tell us about leading IT in a high-pressure environment.**  
**Rick:** 24/7 ops means runbooks, not improvisation. I document SOPs, cross-train, and automate repetitive provisioning. Leadership is calm triage under noise — fix mechanism, communicate status, postmortem after. I trained 80+ users so IT isn't the single point of failure for basic tasks.

**Q10. What's your disaster recovery philosophy?**  
**Rick:** Backup without tested restore is fantasy. DR is RTO/RPO math — how fast back, how much data loss tolerated. 3-2-1 rule, offsite copies, annual restore drill. When disaster hits, you execute the runbook, not Google.

---

### JD02 — IT Support Engineer 2nd–3rd Line · Optimise · Cluster A

**Q1. A client can't receive external email after a DNS change. Diagnose.**  
**Rick:** Mail flow is DNS + auth + transport. I check MX, SPF, DKIM, DMARC, TTL propagation, and Exchange transport rules. Internal works but external doesn't? Usually MX or firewall port 25/587. I verify with message trace — evidence, not guessing.

**Q2. How do you administer Microsoft 365 at scale for an MSP?**  
**Rick:** Entra ID is the spine — users, groups, conditional access, MFA. Exchange/SharePoint/Teams are workloads on top. Intune for endpoint posture. Everything scripted where possible — PowerShell kills toil. Multi-tenant discipline: wrong tenant is a career-ending typo.

**Q3. Intune enrollment fails on a new Windows device. Steps?**  
**Rick:** Enrollment is identity + network + policy. Check Entra join status, autopilot profile, cert chain, firewall to Intune endpoints, compliance policy conflicts. Logs tell the truth — Company Portal and MDM diag reports. Fix the gate, re-enroll, document.

**Q4. macOS user needs Jamf policy update but apps conflict. Approach?**  
**Rick:** Jamf is Intune for Apple — smart groups, config profiles, scope. I reproduce on test device, check profile priority, PPPC permissions, and conflicting MDM payloads. Change one variable at a time. MSP clients don't care about your learning curve — they care that Slack opens.

**Q5. When do you escalate vs. own an issue?**  
**Rick:** I timebox L2 diagnosis — if it's architecture, vendor bug, or permission ceiling, I escalate with reproduction steps, logs, and hypothesis. Escalation isn't failure; bad handover is. At PATH I improved response time ~25% by escalating clean.

**Q6. Explain VLAN troubleshooting for a remote client site.**  
**Rick:** Layer 2/3 separation — wrong VLAN tag means device is alive but deaf. I verify switch port config, trunk allowed VLANs, DHCP scope per VLAN, and inter-VLAN routing. Ping gateway on VLAN, then upstream. "Can't connect" is never one answer.

**Q7. How do you maintain documentation in IT Glue / PSA?**  
**Rick:** Documentation is deflection currency. Every non-trivial fix becomes KB: symptom, cause, fix, prevention. Passwords in vault, configs versioned, vendor portals linked. If the next engineer starts from zero, you failed.

**Q8. DLP policy blocked a legitimate file share. Resolve without weakening security.**  
**Rick:** DLP caught a pattern — good. I trace the rule, classify the data, adjust policy scope or create exception with justification and expiry. Never blanket disable. Security and business share a Venn diagram; find the overlap.

**Q9. VIP client is angry about recurring Teams issues. Handle it.**  
**Rick:** Acknowledge impact first — their time is money. Reproduce, check client version, network QoS, meeting policy, and tenant service health. Fix root cause, not band-aid. Follow up proactively. VIP means higher touch, not lower standards.

**Q10. Describe your experience in an MSP environment.**  
**Rick:** MSP is multi-tenant triage at speed — SLAs, ticket quality, documentation, and depth across M365, endpoint, network. I've supported 120+ users with ITIL workflows in Freshdesk/Zoho. Context-switching is the job; runbooks and automation are how you survive it.

---

### JD03 — IT Systems Administrator (Web Dev) · Thika · Cluster G

**Q1. Company website is down after a CMS update. Response?**  
**Rick:** Rollback first, forensics second. Snapshot before update exists or shame. I check web server logs, PHP/DB errors, plugin conflicts, SSL cert. Restore last known good, then reproduce in staging. Production isn't a lab.

**Q2. How do you balance sysadmin duties with web development?**  
**Rick:** Same brain — different layers. Infra keeps the box up; app layer serves content. I timebox: ops mornings, dev afternoons, incidents override everything. Automation on ops creates dev time. One person roles need ruthless prioritization.

**Q3. Walk through securing a Linux + Windows mixed environment.**  
**Rick:** Harden both — patch cadence, least privilege, firewall zones, centralized logging, encrypted backups. Linux: SSH keys, fail2ban, sudo audit. Windows: GPO, Defender, Entra hybrid if cloud. Mixed env fails at the integration boundary — watch auth and file shares.

**Q4. ERP integration is duplicating records. Fix approach?**  
**Rick:** Integration without idempotency is a duplicate factory. I map the API contract, find the key field, add dedup logic and reconciliation job. Source and destination must match or scream. That's middleware thinking, not spreadsheet hope.

**Q5. How do you handle confidential data as a sysadmin?**  
**Rick:** Need-to-know access, encrypted storage, no personal email exfil, audit logs on sensitive shares. High integrity means you say no when asked to shortcut policy — and you document the request.

**Q6. Network performance degraded across the office. Diagnose.**  
**Rick:** Measure before theorizing — bandwidth, latency, packet loss, DNS time, switch port errors. Rogue device, broadcast storm, failing uplink, or ISP throttle. Baseline vs. now. Fix the bottleneck, not the loudest complaint.

**Q7. Describe your cybersecurity knowledge in practice.**  
**Rick:** Defense in depth: perimeter, endpoint, identity, data. Patch, MFA, segmentation, monitoring, incident response plan. I've supported vulnerability reporting and access controls at PATH. Security is continuous, not a checkbox before audit.

**Q8. How do you work independently under pressure?**  
**Rick:** Pressure means checklist mode — triage, communicate, execute, document. I don't need micromanagement; I need clear priorities and access. Solo IT is ownership: you are L1 through L3 until vendor escalation.

**Q9. UI/UX matters on an internal web tool. Example?**  
**Rick:** Bad UX creates support tickets. I simplify flows, label clearly, validate inputs server-side, mobile-test. Internal tools deserve the same discipline as customer-facing — every confused click becomes your 6pm call.

**Q10. Backup job failed silently for a week. How do you prevent recurrence?**  
**Rick:** Silent failure is the worst failure. Monitoring on backup success, not just schedule. Daily alert on miss, weekly restore test, monthly DR drill. Observability on backups or you're praying.

---

### JD04 — System Administrator · CCaaS · Cluster B

**Q1. What is CCaaS and how would you own that stack?**  
**Rick:** Contact Center as a Service — telephony, routing, IVR, QA, reporting, SSO, security as one platform. I treat it like production infra: uptime SLO, integration map, license utilization, module health. I've worked VoIP/3CX + Freshdesk ITSM — same physics, bigger scale.

**Q2. How do you audit an enterprise software stack?**  
**Rick:** Inventory everything — deploy date, owner, active users, license cost, overlap with other tools. Kill shelfware, consolidate duplicates, rightsized seats. Audit output is CSV truth, not slide deck fiction. CEOs fund savings, not jargon.

**Q3. Present ROI for a proposed tool to executive leadership.**  
**Rick:** Cost vs. time saved vs. risk reduced. Hours reclaimed × rate, error reduction, SLA improvement. Use-case plan: who uses it, how measured, fallback if it fails. Executives buy outcomes; engineers buy features.

**Q4. SSO rollout broke access to a legacy app. Fix?**  
**Rick:** SSO is identity bridge — SAML/OIDC config, attribute mapping, session timeout. Legacy apps often need middleware or phased cutover. I test pilot group, monitor auth logs, keep break-glass local accounts until stable. Never big-bang identity changes without rollback.

**Q5. How do you design employee tool onboarding at scale?**  
**Rick:** Framework: HR trigger → device provision → Entra account → app access by role → training → KB article → support runway. Operations executes frontline; IT owns the template. Ad-hoc onboarding is how orphans and security holes happen.

**Q6. License audit shows 40% unused seats on expensive SaaS. Action?**  
**Rick:** Reclaim immediately — disable inactive, downgrade tier, reassign. Policy: manager approves new seats. Recurring quarterly audit. That's budget recovered without asking for more money.

**Q7. QA module in contact center shows agent scores dropping. Investigate.**  
**Rick:** QA is signal on service quality — sample rate, rubric drift, or real performance issue? I check recording pipeline, scoring calibration, and correlate with ticket volume/spikes. Data before blame. Fix process or coaching based on pattern.

**Q8. How do you operate with autonomy and minimal micromanagement?**  
**Rick:** I ship outcomes — audit report, rollout plan, utilization dashboard — on schedule without being chased. Blockers escalated early with options. Autonomy isn't silence; it's informed independence.

**Q9. Review a vendor contract before CEO signs. What do you check?**  
**Rick:** Term, auto-renew trap, SLA penalties, data residency, exit clause, license metric (per seat vs. per active user), support tier, implementation scope. Detail on contracts is how you avoid vendor lock-in regret.

**Q10. How do you integrate reporting/analytics into CCaaS operations?**  
**Rick:** Reporting must tie to decisions — call volume, ASA, abandonment, QA scores, agent utilization. I pipe to Power BI or native analytics, validate data freshness, dashboard what leadership actually reads. Vanity metrics die in slide decks.

---

### JD05 — ICT Officer · Gas Africa · Cluster D

**Q1. Mission-critical system uptime — how do you guarantee it?**  
**Rick:** You don't guarantee — you engineer probability. Monitoring, redundancy, patch cadence, tested backups, runbooks, vendor SLAs. I sustained >98% uptime at PATH. Uptime is measured, not promised.

**Q2. Walk through your troubleshooting methodology.**  
**Rick:** Reproduce → isolate layer (physical, network, OS, app, identity) → hypothesize → test → fix → document. Ping/Tracert/DNS for network. Event logs for system. One variable at a time. Guessing is not troubleshooting.

**Q3. How do you implement data security and backups?**  
**Rick:** 3-2-1 backups, encrypted at rest, offsite copy, restore tested quarterly. Access control least privilege, patch management, MFA for admins. Backups and security are the same conversation — both are about surviving bad days.

**Q4. User account compromise suspected. Steps?**  
**Rick:** Contain fast — disable account, kill active sessions, force password reset, MFA re-enroll. Scan device, check mail rules and forwarding, audit recent access. Then root cause: phishing? weak password? shared creds? Educate after contain.

**Q5. How do you track ICT assets across the organization?**  
**Rick:** Asset register: tag, serial, assignee, location, warranty, dispose date. Tie to user onboarding/offboarding. Mystery hardware is mystery risk. I've maintained inventory across multi-site deployments.

**Q6. Network performance monitoring — what do you watch?**  
**Rick:** Uplink utilization, latency, packet loss, switch port errors, DNS response, Wi-Fi RF if wireless. Baselines matter — without baseline, "slow" is subjective. Alert on anomaly, not noise.

**Q7. Explain technical concepts to non-technical staff.**  
**Rick:** Metaphor + outcome, skip acronyms. "We're fixing how computers find the server — like updating the address book." Confirm understanding. I trained 80+ health workers on digital tools — if they nod but don't get it, you failed.

**Q8. Multiple urgent tasks — how do you prioritize?**  
**Rick:** Matrix: business impact vs. urgency. Production down beats printer. I communicate queue position honestly. Multitasking is rapid single-tasking with a visible list.

**Q9. Routine maintenance to prevent failures?**  
**Rick:** Patch Tuesday isn't optional. Firmware updates, disk health checks, cert expiry calendar, UPS battery test, log rotation. Preventive maintenance is boring until the day it saves you.

**Q10. Coordinating external vendors for specialist support?**  
**Rick:** Vendor is extension of your team — SLA, escalation path, scope in writing. I gather logs before calling — respect their time, get faster resolution. Post-ticket: did we need vendor or could we self-serve next time?

---

### JD06 — Customer Support Specialist · Influx · Cluster E

**Q1. Angry customer can't log in. First 60 seconds?**  
**Rick:** Empathy before mechanics — "I get why this is blocking you." Verify identity per policy, check account status, password reset flow, browser cache, 2FA device. Calm tone, clear steps, confirm resolution. User remembers how you made them feel.

**Q2. Issue isn't in the knowledge base. What now?**  
**Rick:** Document while solving — you're writing tomorrow's KB article. Reproduce, escalate with clean ticket: steps tried, screenshots, user environment. Escalation isn't "I don't know" — it's "I routed this to the layer that does."

**Q3. How do you handle email, chat, and phone differently?**  
**Rick:** Same brain, different bandwidth. Email: complete, structured. Chat: short, parallel conversations. Phone: lead with reassurance, one step at a time. All channels: categorize accurately or metrics lie.

**Q4. Recurring issue from multiple customers — action?**  
**Rick:** Pattern recognition is gold. Flag to product/ops with frequency count and examples. Propose KB update or process fix. Closing tickets without fixing recurrence is treadmill work.

**Q5. How do you meet remote work setup requirements?**  
**Rick:** Specs exist for a reason — 8GB RAM, stable 40+ Mbps, wired headset, quiet space. I test setup before shift, backup internet if possible. Remote support fails when your environment is the variable.

**Q6. CRM/helpdesk — how do you keep ticket quality high?**  
**Rick:** Category, priority, reproduction steps, resolution notes — every time. Bad data in CRM means bad reporting out. I've used Freshdesk/Zoho with ITIL categorization — garbage in, garbage dashboards.

**Q7. Customer wants you to bend policy. Response?**  
**Rick:** Empathize, explain policy reason, offer allowed alternatives. Escalate if exception warranted — don't rogue-authorize. Trust is consistency, not random favors.

**Q8. How do you learn a new product quickly?**  
**Rick:** Docs → sandbox → break it → support shadow → KB contribution. I map user journeys, not feature lists. Learn the 20% of features that cause 80% of tickets first.

**Q9. Connectivity issue on user's home network — guide them.**  
**Rick:** Layer 1 basics — cable, router reboot, DNS flush, try hotspot isolate. Plain language: "Let's see if it's your network or our app." Remote support is teaching while fixing.

**Q10. Why customer support over pure IT?**  
**Rick:** Support is applied systems thinking with humans in the loop. I like making broken things work under pressure — same triage discipline as IT, plus empathy as a tool. PATH taught me users don't care about your stack; they care that it works.

---

### JD07 — IT Support Technician · Solvo Global · Cluster E

**Q1. Prepare and configure a new Windows workstation for deployment.**  
**Rick:** Standard image, drivers, Windows update, domain join/Entra, M365 apps, security baseline, asset tag, ticket closed with config notes. Consistency beats customization — golden image is freedom.

**Q2. User can't resolve hostname but IP ping works.**  
**Rick:** DNS. Flush cache, check DHCP DNS servers, verify forward lookup zone, test with 8.8.8.8 to isolate local DNS failure. Classic L1 — solve in two minutes if you know the layer.

**Q3. Walk through Ping vs. Tracert vs. DNS in diagnosis.**  
**Rick:** Ping: is it alive? Tracert: where did it die? DNS: can it find the name? Three tools, three questions. Run them in that order before opening the ticket to L2.

**Q4. Basic hardware fault — how do you isolate?**  
**Rick:** Swap test — cable, port, monitor, RAM stick, power supply. POST beeps, smell burnt silicon (bad). Document serial for RMA. Hardware is binary; process is methodical.

**Q5. Night shift — priorities when queue is full?**  
**Rick:** SLA and business impact still rule night. Production blockers first, provisioning second, nice-to-haves when quiet. Document handover for day shift — async continuity is professionalism.

**Q6. ITSM ticket closing standards?**  
**Rick:** Resolution category, root cause tag, time spent, KB link if applicable. Reopen rate tracks your quality. Close means solved, not "stopped replying."

**Q7. Equipment relocation across sites — plan?**  
**Rick:** Inventory what's moving, label cables, shutdown order, transport protection, re-ip plan, test before declaring done. Moves are outage factories without a checklist.

**Q8. Create M365 user account — full steps?**  
**Rick:** Entra user, license assignment, groups for access, MFA enrollment, mailbox config, Teams enable, welcome doc with temp creds via secure channel. Offboarding is the same movie in reverse — disable first.

**Q9. Customer-focused mindset in internal IT?**  
**Rick:** Internal users are customers too. Their downtime is your P1. Communicate, don't condescend. "Have you tried rebooting" without context is how IT earns a bad reputation.

**Q10. IT asset inventory assignment — why it matters?**  
**Rick:** Unknown device = unknown risk and unknown cost. Assignee, location, serial, warranty. Onboard ties asset to user; offboard recovers it. Audit quarterly or finance will audit you.

---

### JD08 — IT & Systems Administrator · Bridge Talent · Cluster D

**Q1. Manage Microsoft 365 across Kenya and Australia hubs.**  
**Rick:** Distributed identity — Entra as source, conditional access for geo risk, license optimization across time zones. Async support docs beat real-time heroics. Australia hours means runbooks Australians can execute without waking you.

**Q2. PowerShell automation example for M365?**  
**Rick:** User provisioning script — create user, assign groups, license, generate report of orphans weekly. PowerShell murders toil. I automated validation at PATH with SQL/VBA — same philosophy, different syntax.

**Q3. Zoho CRM data hygiene — approach?**  
**Rick:** CRM rot is duplicate contacts, stale owners, broken fields. Validation rules, dedup job, mandatory fields, quarterly audit. Clean CRM or sales flies blind.

**Q4. Integrate two internal systems so data doesn't duplicate manually.**  
**Rick:** API or middleware — map fields, idempotent sync, error queue, reconciliation report. Humans as integration layer is how drift happens. I integrated NDWH APIs at PATH — contract-first, validate, reconcile.

**Q5. Set up customer-support call centre infrastructure.**  
**Rick:** VoIP platform, number routing, IVR, queue logic, CRM/ticket integration, recording for QA. Test peak load, failover path, agent headset standard. Calls are real-time — design for failure.

**Q6. Remote staff home internet issue — support from Nairobi?**  
**Rick:** Router reboot, DNS, speed test, wired vs. Wi-Fi, ISP outage map, escalate to ISP with traceroute evidence. Can't fix physics remotely — isolate whose pipe is broken.

**Q7. Intune MDM rollout for remote endpoints?**  
**Rick:** Pilot group, enrollment profile, compliance policy, app deployment rings, helpdesk KB for users. Staged rollout beats big-bang "why is my laptop locked."

**Q8. Phishing email reported by staff. Response?**  
**Rick:** Isolate — don't click links. Search org-wide for same message, block sender/URL, force password reset if anyone clicked, scan endpoints, company-wide alert with screenshot of phish. Speed beats shame.

**Q9. Proactively flag system issues before users scream?**  
**Rick:** Monitoring on disk, cert expiry, backup success, service health, unusual login patterns. Alert on signal, not noise. Proactive is cheaper than postmortem.

**Q10. Research and recommend a new internal tool?**  
**Rick:** Use-case plan: problem statement, alternatives, cost, integration effort, security review, pilot metric. Recommend with data; let leadership choose with eyes open.

---

### JD09 — IT Officer · Global Support · INSO · Cluster C

**Q1. Support a Francophone country office remotely — challenges?**  
**Rick:** Language, bandwidth, time zone, and context. Clear French/English docs, async video tutorials, confirm understanding. Technology is easy; communication gap is the actual outage.

**Q2. Travel to high-risk country for IT project — preparation?**  
**Rick:** Security briefing, local SIM, encrypted devices, offline runbooks, backup hardware, coordinate with country focal point. INGO context means safety first — IT second. Plan B for when Plan A can't ship.

**Q3. Remote support via TeamViewer — best practices?**  
**Rick:** User consent, session recorded if policy allows, least access, fix + teach, document after. Remote into hostile networks — assume compromised client side, don't leave credentials.

**Q4. SharePoint permissions are a mess. Clean up?**  
**Rick:** Audit inheritance, remove over-sharing, group-based access not named users, periodic access review. SharePoint sprawl is security debt with a friendly UI.

**Q5. Country office fails IT standards compliance audit. Plan?**  
**Rick:** Gap list prioritized by risk — patch cadence, AV status, encryption, backup proof, account hygiene. Remediation timeline with owner per item. Compliance is provable, not aspirational.

**Q6. Humanitarian context — how does IT support differ?**  
**Rick:** Austere connectivity, high stakes, low margin for downtime. Empathy for field conditions, rugged solutions, offline-capable where possible. Your ticket isn't a printer — it might be incident reporting for aid worker safety.

**Q7. Create training tutorial for INSO IT tools.**  
**Rick:** Screenshot each step, plain language, FR + EN if required, 5-min video for complex flows. Test with one non-technical user before publishing. KB that isn't read is vanity.

**Q8. Intune deployment in field office with poor bandwidth?**  
**Rick:** Staged downloads, local caching, offline policies, USB fallback image. Design for the network you have, not the network you wish for.

**Q9. Bridge HQ IT and country office conflict on standards.**  
**Rick:** Diplomacy with specs — explain risk in their terms, offer phased path, escalate with evidence not ego. Focal point role is translator between policy and reality.

**Q10. First-line support during site visit vs. second-line remote?**  
**Rick:** On-site: hands, hardware, relationship, observe environment. Remote: depth, architecture, follow-up. I do both at PATH — facility visits plus remote HMIS support. Match mode to problem layer.

---

### JD10 — IT Specialist · Kuehne+Nagel · Cluster F

**Q1. IT in logistics — what's different?**  
**Rick:** Time-sensitive operations — shipment tracking, warehouse systems, global handoffs. Downtime costs money per minute. I speak systems + operations: fix fast, document, prevent recurrence across time zones.

**Q2. Handle escalation from junior admin with poor ticket notes?**  
**Rick:** Send it back with template — reproduction, logs, steps tried. Mentor once, enforce after. Bad handover wastes two people's time. Quality tickets are a culture, not a feature.

**Q3. Improve customer service support quality with metrics?**  
**Rick:** Define metrics — FRT, resolution time, reopen rate, CSAT. Baseline, target, weekly review, process change, re-measure. I've improved response time ~25% at PATH with SLA discipline. What gets measured gets managed.

**Q4. Collaborate with global IT teams across cultures?**  
**Rick:** Async docs, clear ownership, respect time zones, over-communicate handoffs. Assume good intent, clarify ambiguity. Global IT fails at boundaries — be explicit about who owns what.

**Q5. Anti-virus and backup software in networked environment?**  
**Rick:** Central policy, definition updates, scan schedules, quarantine workflow. Backup agents monitored — success/fail alerts. AV without updates is decoration; backup without restore test is hope.

**Q6. Three projects, same deadline — how?**  
**Rick:** Ruthless prioritization, negotiate deadline with data, parallelize what doesn't conflict, daily status without being asked. Under-promise on scope, over-deliver on communication.

**Q7. Mentor a colleague on troubleshooting?**  
**Rick:** Teach the layer model, not the magic fix. Pair on one ticket, they drive, you question. Next ticket they solo, you review. I've trained 80+ users — scaffolding beats lecturing.

**Q8. User says "it's broken" with no details. Investigate?**  
**Rick:** Investigative questions — what were you doing, what did you expect, what happened instead, when did it start, anyone else affected. Screenshots. Reproduce before theorizing. Vague input doesn't get vague output.

**Q9. Flexible hours and short-notice travel — readiness?**  
**Rick:** Go-bag mindset — laptop, adapters, docs accessible offline, comms plan. Flexibility is structured — I know my on-call boundaries and escalation paths before the plane ticket.

**Q10. Why Kuehne+Nagel / logistics IT?**  
**Rick:** Global systems at operational speed — my PATH work was national-scale health data under pressure. Same muscle: reliability, integration, user support, metrics. I fix mechanisms in environments where downtime has real cost.

---

### §11 Quick reference — question types by JD

| JD | Technical | Scenario | Behavioral | Process |
|----|-----------|----------|------------|---------|
| 01 Hospitality | Wi-Fi, PMS/POS, DR | Peak check-in outage | Leadership, vendor mgmt | Budget, 24/7 ops |
| 02 Optimise MSP | M365, Intune, Jamf, VLAN | Email/DNS, VIP client | Escalation, documentation | MSP multi-tenant |
| 03 Thika hybrid | Linux/Win, CMS, ERP | Site down post-update | Independent work | Security, backups |
| 04 CCaaS | SSO, stack audit | License waste | Autonomy, exec presence | ROI, onboarding framework |
| 05 Gas Africa | Network, backups | Account compromise | Non-tech communication | Prioritization, vendors |
| 06 Influx | KB, CRM tickets | Angry customer login | Empathy, policy | Remote setup, multi-channel |
| 07 Solvo L1 | DNS, Ping, imaging | Night shift queue | Customer-focused | ITSM standards, assets |
| 08 Bridge | PowerShell, Zoho, API | Phishing, AU hours | Proactive monitoring | Tool research |
| 09 INSO | SharePoint, Intune | High-risk travel | Cross-cultural | Compliance, tutorials |
| 10 Kuehne+Nagel | AV/backup, global IT | Bad escalation ticket | Mentoring | Metrics, logistics context |

**Add new JDs:** 10 questions + Rick answers → append as JD11, JD12… Update §8 registry.

---

*Drop the next JD. This handbook eats it and gets sharper.*
