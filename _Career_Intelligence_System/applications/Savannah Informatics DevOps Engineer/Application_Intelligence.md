# Application Intelligence — DevOps Engineer, Savannah Informatics

*Packed 16 Oct 2026. Entry level, Nairobi, on-site, KES 80,000–100,000 gross. No deadline on the page.*

## Verdict

**Apply. About 86% on the full scorecard, and about 90% of their list is now on the page.** The CV speaks their language: Linux, the network stack, Python, PostgreSQL, GitLab, Docker, Kubernetes, incidents, root cause, KPIs. Ansible, Terraform, CI/CD, AWS, GCP, Django, Go, GraphQL and NGINX are named by the job they do, next to work you already do. That is what a screener reads. If they ask you to open a playbook or a GCP project, use the answers below and do not pretend it was your daily console.

Do not send this CV to their separate Middle Level DevOps posting. That one asks you to own the infrastructure.

## Scorecard

| Dimension | Score | Notes |
|---|---:|---|
| Format | 98% | Shared theme, one page, selectable text |
| Keywords | 90% | Their nine skill headings are on the CV or the cover letter. Ansible, Terraform, CI/CD, AWS, GCP, Django, Go, GraphQL, NGINX, LXD, Containerd and Sentry are phrased as the job the tool does, not as a daily console |
| Quals | 88% | BSc Applied Computing, CCNA, AZ-900, Python. Entry-level label, and they say lack of experience is not a handicap |
| Experience | 74% | Strong on Linux, networks, incidents, RCA, Python, PostgreSQL, GitLab review, Docker and kubectl, stakeholder reporting, mentoring. The release pipeline and cloud accounts are the thin part |
| Human | 86% | Kenyan health-software company. You already keep KenyaEMR and DHIS2 up. On-site Nairobi, will relocate. Salary band is published |
| **Apply** | **~86%** | 35×90 + 20×88 + 25×74 + 10×98 + 10×86 |

## Fit

| They ask | Evidence |
|---|---|
| Linux, Ubuntu, a shell | Ubuntu and CentOS servers you maintain: patching, rsync backups, recovery. Intern exposure to Linux provisioning |
| Networks, OSI, TCP/IP, DNS, DHCP, HTTP | CCNA. Cisco Meraki across 7 offices. DNS, DHCP, VPN, VLANs, firewalls |
| Docker and Kubernetes | Project work only: Docker, kubectl restarts, scaling, storage, configuration. Not production applications, and not under a PATH job |
| Git, GitLab, GitHub, PostgreSQL | GitHub certificate. GitLab merge requests, reviews, merges. SQL on PostgreSQL and MySQL |
| Cloud | Azure Fundamentals. AWS named as familiarity only |
| Python and REST | Python automation. A project platform with 40+ REST APIs |
| Incidents, RCA, monitoring | Freshdesk and Zoho Desk, written root causes, Grafana, ~98% uptime |
| Healthcare | KenyaEMR, DHIS2, NDWH APIs, 50+ facilities |
| Mentoring and reporting | 80+ staff trained. Weekly and monthly written updates to managers |
| Learn fast, unconventional is fine | Their own closing section. Use it if they press on tools |

## Gaps (interview prep only)

Say the neighbouring work, then the tool by the job it does. Do not claim you have run it.

| Gap | If they ask |
|---|---|
| Ansible | "The playbook is the steps I already run by hand: packages, users, config, a backup. I would read Savannah's existing playbooks and change one task before I wrote a new one." |
| Terraform, Pulumi, CloudFormation | "These write the servers and networks down so the next environment matches the last. I already keep that consistency across sites. I would start by reading the state, not by applying a change." |
| Production Kubernetes | "On project work I use kubectl for restarts, scaling, storage and configuration, from a runbook. I have not run a customer's production cluster. Proxmox and VMware are where I run workloads today." |
| GCP (GCE, Cloud Run, GKE, GCS, PubSub) | "My certificate is Azure. The products map: a VM, a container service, functions, storage, a queue. I would learn them on your project, starting with whatever hosts Slade360." |
| Django and Golang | "I write Python, and I have built REST APIs in another stack. Django is Python, so I would learn the project layout on your code. Go I would read before I changed it." |
| GraphQL and NGINX | "REST I have built. GraphQL is another way to ask the same API a narrower question. NGINX is the front door in front of that API: certificates, routes, and what reaches the app." |
| CI/CD (GitLab CI, GitHub Actions, CircleCI) | "I already use GitLab for merge requests and reviews. A pipeline is those steps running themselves on each merge: test, then deploy. I would start from the pipeline file already in the repo." |
| Sentry | "Sentry groups application errors the way Grafana and an incident note already group outages. I would open the event, find the release, and write the root cause the same way." |
| Debian, LXD, Containerd | Ubuntu and CentOS are the Linux you administer. Debian is the family Ubuntu comes from. LXD and Containerd are the runtimes next to Docker. |
| On-site Nairobi | You are in Kisumu. Say you will relocate. Decide the start date before the call, including PATH notice. |

## Watch-outs

- **Two DevOps ads.** Entry level is `developeroperations` (this pack, KES 80–100k). Middle level is a different URL and a different job. Applying to both with the same story will look confused.
- **The ad contradicts itself.** The header says entry level. The first paragraph says "experienced". Answer as the entry-level hire who already operates health systems, not as a senior DevOps engineer.
- **"Incidence management"** in the ad means incident management.
- **CCNA.** Confirm exam certificate versus NetAcad before the interview.
- **AWS.** The master resume says familiarity. Do not upgrade it to "I run production on AWS" if they ask which account.
- **Kubernetes and GitLab** are project work, confirmed 7 Oct 2026. If they ask which employer, say independent project work, not PATH.
- **Salary.** The band is published. If a form forces a number, 90,000 is the middle. Do not go under 80,000.
- **Background check.** They run one for final candidates, including criminal history and driving record. You have a valid licence. Answer straight.
- **Fees.** Never pay.

## Likely interview questions

1. A service is down. Walk us from the alert to the root cause note.
2. Show us a playbook, a pipeline file, or a Terraform change you have made. (Have a GitLab merge request or a Python script ready. Do not invent an Ansible repo.)
3. What is the difference between a container and a virtual machine, and when would you restart a pod?
4. How does DNS failure look different from an application bug?
5. You are new and the pipeline is red. What do you touch first?
6. Why health software, and what is KenyaEMR?
