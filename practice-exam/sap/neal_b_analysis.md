# Neal Exam B — Analysis

**Date:** 2026-10-26 · **Source:** audited Neal Davis bank, exam page `aws-sap/neal-exam-B.html` · **unseen** · 210 min, **time up** (all 75 answered; 6 of 7 flags in Q69–74)
**Score:** 55/75 (**73.3%**) 🟡 — Neal A 72% → +1 · gate ≥77/80% not met
**Review file:** `neal_b_review.md` (20 wrong + tracker + 🇻🇳)

## Scores

| Domain | Score |
|---|---|
| Accelerate Workload Migration and Modernization | 76.9% |
| Continuous Improvement for Existing Solutions | 74.1% |
| Design for New Solutions | 71.4% |
| **Design Solutions for Organizational Complexity** | **57.1%** 🔴 |

| Slice | Neal A | **Neal B** |
|---|---|---|
| Single-choice | 42/54 (78%) | **36/54 (67%)** 🔴 — 18 of 20 misses |
| Multi-select | 12/21 (57%) | **19/21 (90%)** 🟢 (Select THREE 5/5) |
| Per third | 16 · 19 · 19 | 20 · 19 · **16** — rushed end |
| Topics most missed | Edge/DNS 3/4 | **security-data 6**, **identity-org 4** |

**Read-across:** multi-select discipline fixed, but single-answer accuracy and end-of-test pace slipped. Two unseen Neal tests (72%, 73%) → plateau ≈ 72–73% (≈ 71% re-weighted to a real-exam multi mix). Projected real exam ≈ 71–74%.

## Wrong answers by pattern (20)

| Group | Q | Rule |
|---|---|---|
| A. Over-built / DIY | 10, 61, 63, 71 | Do the transfer math · match design to SLA (99.9% = Multi-AZ) · Aurora replicas for AZs · Control Tower + Account Factory |
| B. Identity / org scope | 14, 23, 28, 51, 56, 59 | Deny-list SCP keeps FullAWSAccess · mgmt account exempt from SCPs, holds no workloads · central identity account + target-account roles · bucket policy names the role |
| C. Right family, wrong variant | 17, 22, 34, 35, 37, 45 | Scheduled scaling for predictable spikes · signed URL vs cookies · WorkSpaces (desktop) vs AppStream (apps) · CodeBuild S3 cache · abort incomplete multipart uploads |
| D. Misread / rushed | 41, 68, 70, 74 | 403 → task role · EBS direct APIs on a snapshot · quota alerts ≠ Budgets |

## 4 rules
1. **Pace:** ≤ 2.5 min/question; Q50 by 125 min; guess-flag-move after 2.5 min. Both Neal tests ran out of time.
2. **SCP logic:** deny list (keep FullAWSAccess) for "block a few"; SCPs never grant; never affect the management account.
3. **Org layout:** workloads/users in member accounts; identities in one account, roles in target accounts; Control Tower for multi-account setup.
4. **Variant check:** same service family, different feature — read which feature the stem needs (scheduled vs target tracking, signed URL vs cookie, WorkSpaces vs AppStream).

## Next actions
1. Read 🇻🇳 (group B first — identity/org).
2. Redo Pass 1: `/ai-tutor sap test-review neal_b redo A, B, C, D`.
3. Decide 11-02 by 10-27.
