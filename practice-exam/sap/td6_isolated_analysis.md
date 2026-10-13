# TD Set 6 (16 questions, Gate 1 final) — Analysis

**Date:** 2026-10-13 · **Mode:** review mode, 1 block (restarted fresh) · multi-select all-or-nothing
**Score:** 11/16 (**68.8%**) — best TD score so far (TD5 41% → TD3 56% → TD6 69%)
**Gate 1 final:** Udemy #2 13/27 + Udemy #3 19/27 + TD6 11/16 = **43/70 (61.4%)**; last two tests 30/43 (70%). Udemy #1 mini skipped.
**Review files:** `td6_isolated_review.md` (5 wrong + tracker + 🇻🇳) · `td6_isolated_review_correct.md` (11 right)

## Scores

| Domain | Score |
|---|---|
| Design for New Solutions | 3/3 🟢 |
| Accelerate Workload Migration and Modernization | 1/1 🟢 |
| Design Solutions for Organizational Complexity | 5/7 (71%) 🟡 |
| Continuous Improvement for Existing Solutions | 2/5 (40%) 🔴 |

| Slice | Score |
|---|---|
| Single-choice | 10/14 (71%) |
| Multi-select | 1/2 — miss had 2 of 3 correct picks |

## Wrong answers by pattern (5)

| Group | Q | Correct | Why your pick failed |
|---|---|---|---|
| A. Overbuilt 🔁 | 1 | S3 + Athena + Glue Catalog | Redshift = always-on cluster for a nightly window |
| A. Overbuilt 🔁 | 11 | CloudFront Functions | Lambda@Edge heavier/pricier for simple rewrites |
| A. Overbuilt 🔁 | 16 | EC2 Instance SP + Compute SP (Lambda) + MemoryDB reserved nodes | Compute SP doesn't cover MemoryDB |
| B. Governance tooling | 6 | Inspector standard scan + code scan + exclusion tag | IAM isn't the exclusion mechanism; missed standard scan |
| B. Governance tooling | 15 | Tag policy + SCP deny CreateStack w/o tag | Config detects after the fact |

**Repeat pattern:** 3/5 misses = picked the heavier option when the stem said *cheapest / least overhead* (same as TD3 group A, Udemy #3 Q16).

## 5 rules
1. Occasional SQL on ORC/Parquet → **S3 + Athena** (pay per scan).
2. Simple header/query/URL rewrites at the edge → **CloudFront Functions**.
3. Savings Plans: EC2 Instance SP (steady EC2), Compute SP (EC2/Fargate/Lambda) — **databases/caches use reserved nodes**.
4. Inspector for Lambda = **standard scan** (CVEs) + **code scan** + **exclusion tag**.
5. "**Enforce**" across an org → preventive **SCP** (+ tag policy); "**don't block**" → detect after (Config).

## Next actions
1. Read 🇻🇳 sections in `td6_isolated_review.md`.
2. Redo Pass 1 today: `/ai-tutor sap test-review td6_isolated redo A, B`.
3. Add the 5 rules to the 1-page rule sheet.
