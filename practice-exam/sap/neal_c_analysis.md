# Neal Exam C — Analysis

**Date:** 2026-10-30 · **Source:** audited Neal Davis bank, exam page `aws-sap/neal-exam-C.html` · **unseen** · 35 q / 98 min, used 94:17 (first pass done at 86', review 12')
**Score:** 25/35 (**71.4%**) 🟡 · pre-review 24/35 (`exam_runs/neal-c-pre-review-snapshot-261030.json`) · official-equivalent ≈ 763 (Neal −10.6 pp)
**Review file:** `neal_c_review.md` (10 wrong + tracker + 🇻🇳)

## Scores

| Domain | Score |
|---|---|
| Design Solutions for Organizational Complexity | 66.7% |
| Design for New Solutions | 80% |
| **Continuous Improvement for Existing Solutions** | **53.8% (7/13)** 🔴 |
| Accelerate Workload Migration and Modernization | 83.3% |

| Slice | Official (10-29) | Neal B | **Neal C** |
|---|---|---|---|
| Single-choice | 42/67 (63%) | 36/54 (67%) | **21/28 (75%)** |
| Multi-select | 5/8 | 19/21 | **4/7** — 3/3 misses half right |
| Per third | 17 · 19 · 11 | 20 · 19 · 16 | **7/11 · 7/11 · 9/11** — end held up |
| CI domain | 50% | 74% | **54%** |

**Read-across:** pace fixed (no time-out, last third best). CI is the stable weak spot on both unseen AWS-like signals (Official 50%, Neal C 54%). Two of 10 misses (Q5, Q30) were right on first pick and changed in the same visit; review itself was net +1 (Q22 B→A).

## Wrong answers by pattern (10)

| Group | Q | Rule |
|---|---|---|
| A. Over-built (3) | 5, 7, 13 | Meet the SLA, don't exceed it (RDS 99.5%) · AppStream for remote desktop app · DAX = read cache only · attacks → CloudFront + WAF + origin header lock |
| B. Security control mismatch (4) | 9, 12, 19, 30 | Interface endpoint = SG + DNS, no route · conditions only in bucket policies · SSE-S3 never uses your key → SSE-KMS CMK · NLB instance targets keep client IP |
| C. Resilience / governance lever (3) | 11, 20, 31 | EKS resilience = AZ topology spread · cost per project = cost allocation tags + Service Catalog · DX redundancy = 2nd DX same Region + DX gateway |

🔁 Repeats: Q5 (WorkSpaces vs AppStream, Neal B Q35), Q7 (DAX, Official Q68), Q13 (WAF/CloudFront, Neal B Q22).

## 5 rules
1. **First pick stands** on single-answer questions unless you find a stem phrase that rules it out (Q5, Q30 lost; Udemy #2 Q11/Q67 same).
2. **No extra parts:** if an option adds Multi-AZ/cache/DAX the stem never asked for, it is usually the cost trap.
3. **Control lives where the feature is:** SG on interface endpoint ENI, conditions in bucket policy, customer key only via KMS.
4. **Resilience = across AZs/paths:** spread pods, second DX on the same Region, never "smaller capacity".
5. **Multi-select:** each pick must answer a different requirement line (Q12: at rest ×2 + in transit; Q20: cost attribution + approved services).

## Next actions
1. Read 🇻🇳 group A first (repeats), then B.
2. Redo Pass 1: `/ai-tutor sap test-review neal_c redo A, B, C`.
3. CI drill on Skill Builder Domain Practice (security 3.2, reliability 3.4, cost 3.5) on 10-31.
