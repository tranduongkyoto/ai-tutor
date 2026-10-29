# AWS Official Practice Exam SAP-C02 — Attempt 1 — Analysis

**Date:** 2026-10-29 · **Source:** Skill Builder Official Practice Exam (first attempt, **unseen**) → `AWS-SAP-C02-practice-exam-ket-qua.md` + `AWS-SAP-C02-domain-scores.md`, converted by `aws-sap/convert_official_export.py` → `official_attempt1_export.md`
**Score:** **783 scaled — PASS** (≥ 750) · raw 47/75 (62.7%) · time 195.6 min (on a 180-min exam)
**Review file:** `official_attempt1_review.md` (28 wrong + tracker + 🇻🇳)

## Scores (AWS domain report)

| Domain | Right | % | AWS verdict | Weakest tasks |
|---|---|---|---|---|
| Organizational Complexity | 10/18 | 56% | Meets | 1.3 resilience 0/2 · 1.4 multi-account 1/4 |
| Design for New Solutions | 14/22 | 64% | Meets | **2.1 deployment 0/3** |
| **Continuous Improvement** | 10/20 | **50%** | **Needs Improvement** | 3.2 security 2/5 · 3.4 reliability 1/3 · 3.5 cost 2/5 |
| Migration & Modernization | 13/15 | 87% | Meets | — |

| Slice | Result |
|---|---|
| Single-choice | 42/67 (63%) |
| Multi-select | 5/8 — 3/3 misses half right |
| Per third | 17 · 19 · **11** — last third collapses again (Neal A/B: 16/25) |
| Avg time | right 2:26 · wrong 2:53 |

**Read-across:** first unseen AWS-calibrated signal. 783 = pass with a thin margin (+33). The practice banks over-rated CI (Udemy #2 CI 83% vs official 50%): official CI questions are "improve an existing system" with twin options.

## Wrong answers by pattern (28)

| Group | Q | Rule |
|---|---|---|
| A. Twin options — one phrase decides (14) | 9, 13, 30, 38, 43, 45, 54, 60, 61, 64, 65, 66, 68, 74 | Archive (≤5 h) vs Deep Archive (≤12 h) · Org backup policy = AWS Backup · user data, not runbook · Lambda@Edge origin routing · Batch Operations in place · write forwarding · Fargate has no custom AMI · backlog per instance · File GW (NFS) vs Volume GW · lowest priority number first · nest OUs · Budgets action · Savings Plans ≠ DynamoDB · Object Lock |
| B. Working but wrong fit (11) | 11, 16, 17, 19, 21, 25, 32, 53, 58, 70, 73 | Secrets Manager rotation · Route 53 ARC for partial failures · dynamic not scheduled scaling · NAT GW per AZ (not global tables) · disable hyperthreading · AWS Backup only · AD Connector · Session Manager · cluster placement group · CloudHSM (exam) · Lightsail |
| C. Org governance tooling (3) | 26, 57, 62 | Org conformance pack + delegated admin · separate log/tooling/audit accounts · IAM Access Analyzer org zone of trust |

⚠️ Dated keys: Q70 (KMS gained FIPS 140-2 Level 3 in 2023), Q74 (Object Lock on existing buckets since 2023). Keep the keys for the exam.

## 10 rules

1. Twin options: underline the ONE differing phrase in both, then re-read only the stem requirement it touches (14/28 misses).
2. Retrieval SLA picks the archive tier: hours → Archive/Flexible; 12 h+ OK → Deep Archive.
3. "Enforce across the org" = Organizations policy types that call a managed service (backup policy → AWS Backup; conformance pack → Config).
4. Multi-AZ HA review: hunt the single zonal resource (NAT GW, single instance) before reaching for multi-Region.
5. Unpredictable load → dynamic/target tracking; SQS workers → backlog per instance.
6. Automation beats a human step: Budgets action, Secrets Manager rotation, user data, Session Manager.
7. Directory: AD Connector when nothing may be stored in AWS; Managed AD when AWS needs its own directory.
8. Who CAN access (policy analysis) = Access Analyzer; who DID access (activity) = CloudTrail.
9. HPC tightly coupled = EFA + cluster placement + single AZ + hyperthreading off.
10. Pace: last third 11/25 — first pass must end by minute 165 with ≥ 15 min left; take a 30 s reset at ~100'.

## Next actions

- 10-30: mixed mock (`aws-sap/exam-mix-nealc-td6-udemy1.html`) — Neal C subscore is the gate signal.
- 10-31: gate — 783 is in the 750–799 band → 11-02 only if Neal C ≥ 72%, else 11-09.
- Redo groups A–C in 2–3 days (`sap test-review official_attempt1 redo A, B, C`). Do NOT retake the official exam yet — same questions, inflated score.

## Difficulty and score equivalence (added 10-29)

**Bank profile (mean words per question, stem + options; multi-select share):** Official 234 / 11% · Neal A–C 191–204 / 20–28% · TD1–5 251–312 / 11–28% · Udemy #2 229 / 33%, #3 198 / 25%.
Official = shorter than TD, ~20% longer than Neal, few multi-selects, but twin-option heavy (14/28 misses).

**Raw → scaled (one anchor):** 62.7% → 783. Piecewise linear: below anchor 100 + 10.9 × raw%, above 783 + 5.8 × (raw% − 62.7). Implied pass line ≈ **59.6% raw** on this form. Uncertainty ≈ ±30 points.

**Difficulty offsets vs Official (learner-specific estimates):** Neal −10.6 pp (Neal B 73.3% on 10-26 vs Official 62.7% on 10-29), TD −4 pp (TD4 66.7% unseen on 10-19, stems longer than Official), Udemy −8 pp (assumed; Udemy rated easier).

| Test | Date | Raw | Seen? | Direct scaled | Difficulty-adjusted scaled |
|---|---|---|---|---|---|
| TD5 timed | 09-25 | 41.3% | unseen | 550 | 507 |
| TD1 review (unseen part) | 09-28 | 53.7% | unseen | 685 | 642 |
| TD2 review (unseen part) | 09-30 | 49.2% | unseen | 636 | 593 |
| TD3 timed | 10-05 | 56.0% | unseen | 710 | 667 |
| Udemy #2 unseen (27 q) | 10-08 | 48.1% | unseen | 624 | 537 |
| Udemy #3 unseen (27 q) | 10-12 | 70.4% | unseen | 828 | 780 |
| TD6 (16 q) | 10-13 | 68.8% | unseen | 819 | 795 |
| TD4 timed | 10-19 | 66.7% | unseen | 806 | 783 |
| Neal A | 10-22 | 72.0% | unseen | 837 | 769 |
| Neal B | 10-26 | 73.3% | unseen | 845 | 783 (anchor for offset) |
| **Official** | **10-29** | **62.7%** | **unseen** | **783** | **783** |
| TD1/TD5/TD2/TD3 retakes | 10-14 → 10-21 | 88–89% | seen | 930–938 | 907–915 (memory-inflated) |
| Udemy #2 full | 10-28 | 81.3% | seen | 891 | 845 (memory-inflated) |
