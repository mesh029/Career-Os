# Application Intelligence — Technical Support Agent, Influx

*Repacked 2026-10-07 for the Kenya-only repost. Different posting from `Influx Customer Support Specialist`.*

## Verdict

**Apply. About 84%.** Same job as September, now Kenya-only, so fewer applicants compete. The hard gate is hands-on GitLab and Kubernetes, which you confirmed. Expect them to test it.

## You already applied in September

Influx has your September CV, which titled your PATH roles "Technical Support Engineer (L2)" and "Technical Support Agent (L2)". The new CV uses your real titles with the support level in brackets:

- Health Informatics / HMIS Officer (L2 systems support)
- ICT Associate (L1/L2 technical support)

If a recruiter asks why the titles differ, say: *"The September CV described the support level. This one uses my official PATH titles, which is what a reference check will show."* Real titles are what survive verification.

If Influx's form shows your earlier application as still active, ask the recruiter (from an @influx.com address only) whether to reapply or update it, instead of creating a duplicate profile.

## Scorecard

| Dimension | Score | Notes |
|---|---:|---|
| Format | 98% | Shared theme |
| Keywords | 92% | Logs, Python, GitLab, Kubernetes, restarts, merge requests, storage, capacity, reversible / non-reversible, escalation, Incident / Change / Problem, Grafana, KB |
| Quals | 82% | 3+ years technical support. GitLab and Kubernetes are from project work, not a full-time DevOps job |
| Experience | 78% | Real L2 investigations on production health systems; Kubernetes is project-scale |
| Human | 76% | Kenya-only helps; 24/7 roster accepted |
| **Apply** | **~84%** | |

## What's on the CV and where

| Claim | Where | Basis |
|---|---|---|
| Logs, Python, SQL, Linux servers, backups, Grafana | PATH | Master resume |
| Reversible vs non-reversible: backup and sign-off first | PATH (EMR servers and databases) | Master resume: backups, DR, SQL validation |
| GitLab merge requests, Kubernetes (kubectl, pod restarts, scaling, storage, configuration) | Independent projects, 2023 to present | Confirmed hands-on by Meshack, 7 Oct 2026 |
| Operations platform, 40+ REST APIs | Independent | Master resume |

**Not claimed:** Kubernetes or GitLab at PATH, computer vision / ML platforms, Datadog, banking or aviation, CCNA.

## Prepare for the technical test

Influx will likely give a practical task or ask scenario questions. Practise:

1. **Kubernetes:**
   - Basic checks: `kubectl get pods -n <ns>`, `kubectl describe pod`, `kubectl logs <pod> --previous`.
   - Restarting safely: `kubectl rollout restart deployment/<name>`, `kubectl rollout status`.
   - Scaling: `kubectl scale deployment/<name> --replicas=N`.
   - Common errors: CrashLoopBackOff, ImagePullBackOff, OOMKilled, Pending (no resources).
   - Storage: PersistentVolumeClaims, and checking a full disk.
2. **GitLab:**
   - Merge requests: review the diff, check pipeline status before merging, approvals, merge vs squash.
   - Reverting: revert a merge request through a new MR rather than rewriting history.
3. **Python log triage:**
   - Write a short script that reads a log file, counts ERROR lines by message, and prints the top 5 with first and last timestamps.
4. **Reversible vs non-reversible:**
   - Reversible: restarting a service, scaling replicas, a config change with a rollback.
   - Non-reversible: `DROP`, `DELETE` without a `WHERE` clause, `TRUNCATE`, schema migrations without a down step, deleting a volume.
   - Rule: no backup and no approval means you don't run it.
5. **Escalation write-up:**
   - Summary, impact, steps to reproduce, logs, what you tried, what is safe to try next.

## Apply

Official Influx channel only (Typeform or influx.com careers / LinkedIn). Contact only from **@influx.com**. Never pay. Expect an English assessment.

## Rebuild

```
python3 "applications/Influx Technical Support Agent L2/build.py"
```
