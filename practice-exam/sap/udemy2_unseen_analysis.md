# Udemy Test #2 — Unseen Questions (Gate 1, isolated) — Analysis

**Date:** 2026-10-07 → 10-08 · **Mode:** review mode, blocks of 25 · multi-select all-or-nothing
**Score:** 13/27 (**48.1%**) ❌ — Gate 1 target ≥66% combined (with Udemy #3 unseen + TD6 + Udemy #1 mini)
**Source:** `udemy2_unseen_export.md` (Q numbers = shuffled position; original Udemy number in the table)
**Review files:** `udemy2_unseen_review.md` (14 wrong + tracker + 🇻🇳) · `udemy2_unseen_review_correct.md` (13 right)
**Note:** Udemy questions have no official domain tags — domains were assigned by stem (approximate).

## Scores

| Domain | Score |
|---|---|
| Accelerate Workload Migration and Modernization | 5/7 (71%) 🟢 |
| Continuous Improvement for Existing Solutions | 5/11 (45%) 🔴 |
| Design for New Solutions | 3/8 (38%) 🔴 |
| Design Solutions for Organizational Complexity | 0/1 |

| Slice | Score |
|---|---|
| Single-choice | 10/19 (53%) |
| Multi-select | 3/8 (38%) — 3 of 5 misses had one correct pick |

## Wrong answers by pattern (14)

| Group | Wrong | Questions |
|---|---|---|
| A. Kinesis family & streaming destinations | 4 | 1, 6, 8, 13 |
| B. Data transfer sizing (Snow vs network) | 2 | 4, 15 |
| C. Ops tooling: monitoring, patching, compliance | 3 | 9, 22, 26 |
| D. Exact feature behavior | 5 | 12, 20, 21, 24, 27 |

### A. Kinesis family (4) — biggest gap 🔁
| Q | Correct | Why your pick failed |
|---|---|---|
| 1 | KDS Enhanced Fan-Out | Firehose has no consumer apps |
| 6 | KDS as Firehose source disables Firehose PutRecord | Agent can write to Firehose |
| 8 | Kinesis Data Streams | SQS = one consumer per message |
| 13 | WAF → Firehose → S3 → Athena | CloudTrail is not a WAF log destination |

### B. Data transfer sizing (2)
| Q | Correct | Why your pick failed |
|---|---|---|
| 4 | Snowball Edge ×N → S3 → lifecycle Glacier | Snowmobile only ≥10 PB |
| 15 | 3 × Snowball Edge | 200 TB over 1 Gbps ≈ 18.5 days |

### C. Ops tooling (3)
| Q | Correct | Why your pick failed |
|---|---|---|
| 9 | Lambda CloudWatch Logs + X-Ray | API GW access logs can't show Lambda processing time |
| 22 | SSM Agent + maintenance window + AWS-RunPatchBaseline | ApplyPatchBaseline = legacy Windows-only; OS-native = more effort |
| 26 | Config rules + CloudTrail → CloudWatch Logs (KMS) | CloudTrail+SNS doesn't auto-revert |

### D. Exact feature behavior (5)
| Q | Correct | Why your pick failed |
|---|---|---|
| 12 | SQS message timers | Delay queue delays every message |
| 20 | Global Accelerator traffic dials | Route 53 weighted defeated by DNS caching |
| 21 | Proxy methods + dynamic (all headers) | Static/photos/videos use the regional edge cache |
| 24 | Both dedicated | Dedicated in LC **or** VPC wins |
| 27 | Unhealthy: terminate → launch · Rebalance: launch → terminate | Not simultaneous |

## Inconsistent concepts
| Right | Wrong | Concept |
|---|---|---|
| Q17 | Q8 | SQS = work buffer, not multi-consumer stream |
| Q16 | Q20 | Exact service behavior (stateful/stateless; DNS vs anycast) |
| Q10 | Q12 | Service knobs (usage plans ✅ vs message timers ❌) |

## 8 rules
1. Many consumers on one stream → **KDS** (+ **Enhanced Fan-Out** if they lag); Firehose only delivers to destinations.
2. KDS as Firehose source → write to the KDS, never to Firehose directly.
3. WAF logs → CloudWatch Logs / S3 / Firehose — never CloudTrail.
4. **Do the transfer math**; >~1 week on the link → Snowball Edge (80 TB each); Snowmobile ≥10 PB; Snow → S3 → lifecycle → Glacier.
5. Patching mixed fleet → **AWS-RunPatchBaseline** + maintenance window.
6. Per-message delay → **message timer**; whole queue → delay queue; visibility timeout ≠ delay.
7. Clients cache DNS → **Global Accelerator** for traffic shifting.
8. ASG: unhealthy → terminate first; AZ rebalance → launch first. Tenancy: dedicated anywhere wins.

## Next actions
1. Read 🇻🇳 sections in `udemy2_unseen_review.md` — group A first.
2. Redo Pass 1 today: `/ai-tutor sap test-review udemy2_unseen redo A, B, C, D`.
3. Then Udemy #3 unseen (`review-set udemy3_unseen`, resumes at Q7).
