# Neal Exam A — Analysis

**Date:** 2026-10-22 · **Source:** Neal Davis bank (audited: 25 bad-key/ambiguous/retired questions removed), exam page `aws-sap/neal-exam-A.html` · **unseen** · 210 min, **time up** (all 75 answered)
**Score:** 54/75 (**72%**) 🟡 — gate ≥80% not met · TD4 unseen 10-19: 66.7% → **+5 pts**
**Review file:** `neal_a_review.md` (21 wrong + tracker + 🇻🇳)

## Scores

| Domain | Score |
|---|---|
| Continuous Improvement for Existing Solutions | 74% |
| Design for New Solutions | 73% |
| Design Solutions for Organizational Complexity | 69% |
| Accelerate Workload Migration and Modernization | 69% |

| Slice | Score |
|---|---|
| Single-choice | 42/54 (78%) |
| **Multi-select** | **12/21 (57%)** — 8 of 9 misses had one correct pick |
| Per third | **16/25** · 19/25 · 19/25 — slow start, used all 210 min |
| Topics most missed | Edge/DNS 3/4 · security-data 3/10 · serverless-integration 3/7 |

**Read-across:** Neal stems are shorter than the real exam but the bank is CI-heavy (36%) → 72% here ≈ **70–73% on the real exam**, consistent with TD4 adjusted (~71%). Domains are now even; the gaps are **multi-select discipline** and **pace**.

## Wrong answers by pattern (21)

| Group | Q | Rule |
|---|---|---|
| A. Known rule, new wording | 11 🔁, 13 🔁, 32 🔁, 34 🔁, 41 🔁 | VM Import · Budgets (cost + RI coverage) · Service Catalog · always-on tier ≠ Spot · WAF IP allow-list + usage plan |
| B. Multi-select half right | 1, 4, 16, 22, 27, 37, 44 | Second pick must satisfy every stem requirement — eliminate, don't guess |
| C. Access & security design | 5, 17, 53, 70 | Session Manager (no open ports) · multi-AZ ASG + WAF logs via Firehose · cross-account role |
| D. Service fit / hidden constraint | 15, 55, 56, 72, 74 | Lambda + Step Functions · Snowball parallel copies · 2nd DX different carrier · drop Oracle licence · PHZ association + inbound resolver |

## 4 rules
1. Multi-select: find the sure pick, then **test each remaining option against every requirement** (cost, ops overhead, HA) before choosing the second.
2. "Alert on cost / RI coverage / usage" → **AWS Budgets** (coverage or utilization budget), not CloudWatch/CloudTrail. 🔁
3. Admin access "most secure / no open ports" → **Session Manager** + IAM; no bastion, no SSH/RDP inbound.
4. On-prem → private hosted zone → **Resolver inbound endpoint** + PHZ associated with each VPC.

## Next actions
1. Read 🇻🇳 sections (🔁 group A first).
2. Redo Pass 1: `/ai-tutor sap test-review neal_a redo A, B, C, D` (shuffled).
3. Pacing for Neal B (10-26): Q25 by 60 min, Q50 by 125 min, flag after 3 min.
