# Udemy Test #3 — Unseen Questions (Gate 1, isolated) — Analysis

**Date:** 2026-10-12 · **Mode:** review mode, blocks of 25 (restarted fresh; earlier mixed-mock answers discarded) · multi-select all-or-nothing
**Score:** 19/27 (**70.4%**) — up from 48% on Udemy #2 unseen (10-08)
**Caveat:** ~3 questions were near-duplicates of Udemy #2 items reviewed the same day (WAF logs, Config+CloudTrail, KDS+Lambda) → true-unseen ≈ 65–68%
**Gate 1 running:** Udemy #2 13/27 + Udemy #3 19/27 = **32/54 (59%)**; TD6 (16) + Udemy #1 mini (5) left
**Review files:** `udemy3_unseen_review.md` (8 wrong + tracker + 🇻🇳) · `udemy3_unseen_review_correct.md` (19 right)

## Scores

| Domain | Score |
|---|---|
| Continuous Improvement for Existing Solutions | 8/10 (80%) 🟢 |
| Accelerate Workload Migration and Modernization | 3/4 (75%) 🟡 |
| Design for New Solutions | 7/12 (58%) 🔴 |
| Design Solutions for Organizational Complexity | 1/1 |

| Slice | Score |
|---|---|
| Single-choice | 16/22 (73%) |
| Multi-select | 3/5 (60%) — both misses had one correct pick |

## Wrong answers by pattern (8)

| Group | Wrong | Questions |
|---|---|---|
| A. Edge, routing & multi-Region delivery | 5 | 3, 11, 21, 25, 26 |
| B. Monitoring, logging & tamper-proofing | 2 | 9, 14 🔁 |
| C. Migration strategy fit | 1 | 16 |

| Q | Correct | Why your pick failed |
|---|---|---|
| 3 | ALB Host `*.ecomm.com` + `ecomm.com` | Redirect action doesn't forward to target groups |
| 11 | MediaConvert + HLS + CloudFront | No transcoding → no adaptive bitrate |
| 21 | CloudWatch alarm → Route 53 health check | Health checkers can't reach private IPs |
| 25 | CloudFormation StackSets | `create-stack` has no `--regions` |
| 26 | Global Accelerator custom routing + subnet endpoints | NLB can't target a specific instance |
| 9 | Integrity validation + MFA Delete | KMS = confidentiality, not tamper-proof |
| 14 🔁 | Traffic Mirroring | Flow Logs = metadata only (same miss as TD3 Q45) |
| 16 | Replatform to EC2 (new AMI) + Snowball | Fargate = re-architecture |

## 7 rules
1. Host-based routing → ALB **Host** conditions; Path conditions = `/paths`.
2. VOD streaming → **MediaConvert + HLS + CloudFront**.
3. Private hosted zone health → **CloudWatch alarm**-based Route 53 health check.
4. Many Regions/accounts → **StackSets**.
5. Deterministic player → instance routing → **Global Accelerator custom routing**.
6. Tamper-proof CloudTrail → **integrity validation + MFA Delete**.
7. Packet payloads → **Traffic Mirroring**; Flow Logs = metadata.

## Next actions
1. Read 🇻🇳 sections in `udemy3_unseen_review.md` (group A first).
2. Redo Pass 1: `/ai-tutor sap test-review udemy3_unseen redo A, B, C`.
3. 10-13: TD6 + Udemy #1 mini → Gate 1 combined decision.
