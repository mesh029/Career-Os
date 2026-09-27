# Portal, assessment, voice, and technical check — BruntWork L2 Healthcare MSP

Use this while the application tab is open. Facts stay consistent with `resumes/00_Master_Resume.md`.
Do not claim Enable/N-able production, CompTIA, or a US HIPAA certificate.

**Timezone for this role:** Mon–Fri 9:00 AM – 1:00 PM Eastern. In Kenya that is **4:00–8:00 PM EAT** during US daylight time (likely through early November 2026) and **5:00–9:00 PM EAT** when the US is on standard time.

---

## 1. Technical check (do this first so you do not fail after writing essays)

Typical BruntWork checks: internet speed, webcam, microphone, quiet room, OS.

| Item | Target | Your note |
|---|---|---|
| Internet | Stable broadband; wired Ethernet if possible. Run speedtest.net on the machine you will use. Screenshot the result. | Fill: ____ down / ____ up Mbps |
| Computer | Windows 10/11, enough RAM to RDP/remote-control (8 GB minimum; 16 GB better) | Fill: CPU / RAM / OS |
| Headset | Wired headset with mute. Test mic in Windows Sound settings. | |
| Webcam | Working, face lit, plain background | |
| Power / backup | Know what happens if mains drop (UPS or hotspot fallback). Do not invent a UPS you do not have. | Fill truthfully |
| Quiet space | Door closed. No TV, no echo. This also feeds the voice recording. | |

If the check fails, stop and fix the connection. Do not submit a weak tech check and a strong CV; BruntWork deprioritises incomplete or failed checks.

---

## 2. Voice recording (60–90 seconds)

Record in one take. Sit up. Smile slightly (it changes the voice). Do not read like a script; you may glance at bullets.

**Script (about 75 seconds at a calm pace):**

> Hello, my name is Meshack Ariri. I am applying for the Technical Support Agent Level 2 role supporting your healthcare MSP clients.
>
> For about three years at PATH I have provided first and second-line IT support for more than 120 users across health facilities, keeping systems at around 98 percent uptime. Day to day that means escalated troubleshooting, Windows and Linux patching, system configuration, and network diagnostics on LAN, WAN, VPN, and Cisco Meraki.
>
> I already work in healthcare IT, so protecting health information is normal for me: access control, encryption, backups, and training staff on secure use. I am willing to sign Business Associate and data security agreements. I also have hands-on VoIP experience with 3CX, which I know is useful in this environment.
>
> I am based in Kenya, fully remote-ready, and available Monday to Friday, 9 AM to 1 PM Eastern. Thank you.

**Delivery checks**

- If you stumble, record again. They hear the last take you upload.
- Do not mention pay, PATH resignation drama, or "I need a job."
- Do not say "HIPAA certified."
- Pronounce 3CX as "three C X." HIPAA as "HIP-uh." BAA as "B A A" or "business associate agreement."

---

## 3. HIPAA / BAA cheat sheet (read twice before the assessment)

You are **not** claiming US HIPAA production. You are showing you understand the rules you will sign.

| Term | One line you can say |
|---|---|
| **PHI** | Protected Health Information: health data that can identify a person (name + diagnosis, MRN, etc.). |
| **ePHI** | The same data in electronic form: EMR, email, backups, tickets, screenshots. |
| **Covered entity** | The clinic/hospital/insurer that owns the patient relationship. |
| **Business Associate** | A vendor (this MSP, and you as contractor) who can touch ePHI while delivering IT. |
| **BAA** | The contract that says how the Business Associate must protect ePHI. Signing it is a requirement of this job. |
| **Minimum necessary** | Only the access and data required to fix the ticket. No browsing charts. |
| **Security Rule (IT-relevant)** | Access control, audit logs, encryption, patching, unique IDs, MFA, backups, incident reporting. |
| **Never** | PHI in personal WhatsApp/Gmail, screenshots of patient records in a ticket without policy, shared admin passwords, leaving a remote session unlocked. |

**PATH translation (truthful):** You already treat EMR data as sensitive: least-privilege AD, MFA, encryption, patching, backups, and staff training. US HIPAA is a named rule-set for the same idea. You will follow the client's procedures and the BAA.

---

## 4. Paste-ready assessment answers

Edit lightly so it sounds like you. Keep the facts.

### Why are you a fit for this role?

I have about three years of IT support and systems work inside healthcare at PATH, including Level 2 troubleshooting, patching, configuration, and network diagnostics for 120+ users at around 98% uptime. I already write SOPs and knowledge-base articles, I explain technical issues to clinicians who are not IT people, and I have VoIP/3CX experience. I have not been employed by a US MSP running Enable/N-able, but I have supported multiple health-facility environments remotely with the same outcomes those tools are built for: stable endpoints, timely patches, clear tickets, and protected health data. I can start on the Monday–Friday 9 AM–1 PM Eastern schedule and I will sign Business Associate and data security agreements.

### Describe your Level 2 / escalation experience.

When a ticket is more than password reset or "have you rebooted," I own root cause. Example pattern: user says the clinical system is down. I check whether it is identity (account/MFA), endpoint (patch, service, disk), network (DNS, DHCP, VPN, VLAN, firewall), or the server (Windows/Linux service, backup job, disk, patch). I reproduce, isolate the layer, fix or apply the standard change, document the ticket, and write a short SOP if it will recur. At PATH I used Freshdesk/Zoho Desk under ITIL/SLA and improved response time about 25% by tightening documentation and workflow, not by guessing faster.

### How do you handle healthcare data / HIPAA?

I treat every clinical system ticket as if the screen may contain identifiable health information. I use unique accounts and least privilege, I do not copy patient data into personal tools, I lock remote sessions, and I only take the access needed to resolve the issue. I have trained 80+ health workers on secure system use. I have not been the HIPAA officer for a US covered entity. I understand PHI, ePHI, minimum necessary, and that a Business Associate Agreement legally binds the MSP and me. I am willing to sign and follow those agreements and the client's incident-reporting process.

### MSP / RMM / Enable experience (honest)

My production environment has been in-house healthcare IT across multiple sites, not a named US MSP stack. I monitor and administer networks on Cisco Meraki, patch Windows/Linux systems, manage identity in Active Directory and Microsoft 365, and support users remotely. I have not administered Enable or N-able N-central in production. I am ready to learn that console immediately: device monitoring, patch approval windows, remote control, scripting, and client separation. I will not click through a healthcare tenant until I understand the client's change window and BAA rules.

### Scripting and automation

I use SQL and Python for validation and automation, and Excel VBA for reporting pipelines. That work cut manual reporting/processing time by about 40% on health data workflows. In an MSP context I would apply the same habit: if a fix is done the same way on every client, it becomes a script or an RMM policy, then an SOP. I will follow the client's change control rather than running untested scripts against production.

### 3CX / phone environment

I have supported IP telephony / VoIP including 3CX: handset and client setup, and tying voice into the support workflow with Freshdesk. I can troubleshoot registration, audio quality (network/QoS), and user setup, and I know a healthcare MSP will also care about recording policies and who can hear calls that may include PHI.

### Availability and contractor terms

I can work Monday to Friday, 9:00 AM to 1:00 PM Eastern, 20 hours per week, fully remote from Kenya. I understand this is an independent contractor role through BruntWork and that the hourly rate is set from the application process. I will complete the technical check and voice recording as required.

### Strengths / weakness (if asked)

Strength: I finish escalations and then write the procedure so the owner is not the only person who knows the fix. Weakness: I used to stay on a ticket past the sensible escalate-or-timebox point. I now timebox diagnosis, document what I tried, and escalate with a clean handover when the next layer is architecture or vendor.

---

## 5. Cover letter paste (if the portal has a text box)

Use the same text as the generated cover letter, or this shorter version:

I am applying for Technical Support Agent Level 2. For three years at PATH I have provided Level 2-style support in healthcare IT: escalated troubleshooting, patching, configuration, and network diagnostics for 120+ users at about 98% uptime. I write SOPs, I explain issues to non-technical clinical staff, I have 3CX/VoIP experience, and I already treat health data as sensitive. I have not run Enable/N-able in production and I am ready to learn that RMM in week one. I can work 9 AM–1 PM Eastern and I will sign Business Associate and data security agreements. CV attached.

---

## 6. What not to say

- "I am HIPAA certified / HIPAA compliant personally."
- "I have X years in an MSP" if PATH is the employer.
- "I am expert in Enable / ConnectWise / Datto."
- Any patient names, facility-level incident details, or internal PATH credentials as examples.
- Willingness to work unpaid "training" or pay for equipment to a personal account (scam pattern).
