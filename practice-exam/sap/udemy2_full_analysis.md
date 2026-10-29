# Udemy Practice Test #2 (full timed) — Analysis

**Date:** 2026-10-28 · **Source:** exam page `aws-sap/exam-udemy2.html` · **all 75 seen before** (48 in chapter drills, 27 in Gate 1 on 10-08) → pacing run, not a readiness signal · 210 min, finished with 13 min left
**Score:** 61/75 (**81.3%**) · before flag review 60/75 (80.0%)
**Review file:** `udemy2_full_review.md` (14 wrong + tracker + 🇻🇳) · pre-review snapshot `exam_runs/udemy2-pre-review-snapshot-261028.json`

## Scores

| Domain (approx., Udemy has no official tags) | Score |
|---|---|
| Organizational Complexity | 81.8% |
| Design for New Solutions | 84.2% |
| Continuous Improvement | 83.3% |
| **Migration & Modernization** | **73.3%** 🟡 |

| Slice | Result |
|---|---|
| Single-choice | 43/50 (86%) |
| Multi-select | 18/25 (72%) — **7/7 misses had ≥1 right pick** (half-right pattern again) |
| Per third (page order) | 20 · 22 · 19 |

## Pacing (first run with the per-question timer)

| Phase (learner's 4-phase order) | Qs | Right | Clock | Avg/Q |
|---|---|---|---|---|
| 1. Short singles, first pass | 44 | 37 (84%) | 2 → 91 min | 1:58 |
| 2. Skipped long singles | 6 | 6 (100%) | 95 → 141 min | 3:23 |
| 3. Select TWO | 19 | 14 (73%) | 103 → 148 min | 2:10 |
| 4. Select THREE | 6 | **3 (50%)** | 151 → 165 min | 3:27 |
| Flag review (30 flags) | — | 5 changes: 3 fixed, **2 broken** (Q11, Q67) → +1 | 169 → 197 min | ~56 s |

- **Pacing fixed:** 25 answered at 51', 50 at 105', all 75 at 165' — first test not timed out (Neal A/B both timed out).
- **Flags are well calibrated:** flagged 17/30 right vs unflagged 43/45; 13 of 15 pre-review misses were flagged.
- **Review leak:** both broken changes were single-answer questions changed without new evidence; 6.5 min spent re-reading two already-right questions (Q15, Q61).

## Wrong answers by pattern (14)

| Group | Q | Rule |
|---|---|---|
| A. Fact/limit not known cold | 11, 33, 45, 54 | gp2 = 3 IOPS/GiB · Redshift copy grant in destination Region · RDS replica → standalone, Aurora replica → primary · Firehose has no DynamoDB target |
| B. Multi-select half right | 13, 24, 25, 46, 59, 63 | GA never fronts CloudFront/S3 · 504 root cause = X-Ray + Lambda logs · VPC Lambda needs NAT · WAF never on EC2/ASG · "in-memory" = Redis/DAX · ACL detection = CloudTrail data events + EventBridge |
| C. Hybrid / migration path | 19, 65, 67, 68 | Chef → OpsWorks (dated) · many idle apps → containers on ECS · HA high-bandwidth = redundant DX · on-prem → S3 over DX = public VIF |

🔁 repeats: Q13 (GA), Q24 (missed 10-08 too), Q33 (copy grant), Q54 (Firehose targets), Q63 (S3 data events), Q68 (public VIF).
⚠️ Dated/simplified keys: Q19 (OpsWorks EOL 2024), Q45 (Aurora "synchronous Multi-AZ" wording), Q68 (S3 interface endpoint over private VIF now possible).

## 10 rules

1. On flag review, change a single-answer pick **only** with a concrete missed constraint — 2 of 5 changes broke right answers.
2. Review multi-select flags first; that is where changes paid off (Q55 fixed).
3. Cap review at ~90 s per flag; skip flags you already resolved in the first pass.
4. gp2 IOPS = 3 × GiB (max 16,000); growing gp2/gp3 is cheaper than io1 for a +3,000 IOPS gap.
5. KMS keys are Regional: cross-Region copy needs a key/grant in the destination Region.
6. Firehose cannot write to DynamoDB; serverless + no capacity planning = SQS + Lambda.
7. Global Accelerator fronts ALB/NLB/EC2/EIP only — never CloudFront or S3.
8. Each multi-select pick must be true on its own *and* serve the same solution — drop any sibling feature that only partly fits (DynamoDB without DAX, API Gateway logs without X-Ray).
9. On-prem → S3 over Direct Connect = public VIF; a private VIF reaches VPC resources.
10. Select THREE late in the test is your weakest slice (3/6) — try them right after the short singles in Udemy #3.

## Next actions

- 10-29: Udemy #3 timed — move Select THREE earlier; apply review rules 1–3; compare phase accuracy.
- Redo group A–C misses in 3–4 days (`sap test-review udemy2_full redo A, B, C`).
- 10-30: Official Practice Exam (180 min → first pass target ≤ 165 min, review multi flags only).
