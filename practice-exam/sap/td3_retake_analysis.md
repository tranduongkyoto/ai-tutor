# TD Set 3 — Timed retake — Analysis

**Date:** 2026-10-21 · **Mode:** TD website timed mode (retake; first attempt 10-05, 16 days earlier) · multi-select all-or-nothing · export time shows 00:00:50 (TD timer glitch)
**Score:** 66/75 (**88%**) 🟢 — first attempt 10-05: 42/75 (56.0%) → **+32 pts**
**Source:** `Retake-AWS_SAP_Timed_Mode_Set_3_Results.md` (raw TD export) → normalized to `td3_retake_export.md`
**Review file:** `td3_retake_review.md` (9 wrong + tracker + 🇻🇳)

## Scores

| Domain | Score |
|---|---|
| Accelerate Workload Migration and Modernization | 100% 🟢 |
| Design Solutions for Organizational Complexity | 87.5% 🟢 |
| Continuous Improvement for Existing Solutions | **87.18%** 🟢 (10-05: 51.3%) |
| Design for New Solutions | 86.96% 🟢 |

| Slice | Score |
|---|---|
| Single-choice | 56/62 (90%) |
| Multi-select | 10/13 — all 3 misses had 1 of 2 correct picks |
| Per third | 24/25 · 20/25 · 22/25 — no end-of-test drop (TD4 last third was 14/25) |

## Old misses vs regressions

| | Count |
|---|---|
| 10-05 misses now right | **29/33** (still wrong: Q1, Q40, Q41, Q56) |
| 10-05 right answers now wrong | **5/42** (Q34, Q38, Q47, Q62, Q68) |

## Gate (exam 10-23 go/no-go)

TD3 ≥80% ✅ (88%) · Continuous Improvement ≥65% ✅ (87.2%) · retakes ≥85% 4/4 ✅ → **GO for 10-23** (slot + possible second fee permitting). Caveat: retake = partial recall; TD4 unseen adjusted ~71% stays the honest floor.

## Wrong answers by pattern (9)

| Group | Q | Correct | Why the pick failed |
|---|---|---|---|
| A. Repeat misses | 1 🔁 | ElastiCache Redis in front of the DB | Migrating to Aurora = not "quick" |
| A | 40 🔁 | Route 53 **alias** to the ELB | A record / CNAME choice decides |
| A | 41 🔁 | Snapshot copy for stateless tiers + Aurora cross-Region replica | Hot standby web/app tier = not cost-effective |
| A | 56 🔁 | S3 SSE-KMS + bucket policy deny `aws:SecureTransport=false` | Not the fully managed + customer key option |
| A | 62 🔁 | Redshift **snapshot copy grant** for KMS-encrypted cross-Region copy | 3rd Redshift DR miss (chapter drills, TD4 Q64) |
| B. Half-right multi-select | 34 | SSE-C headers (algorithm, key, key-MD5) | Wrong header name |
| B | 47 | CloudFormation resource tags + Service Catalog | Config only detects |
| C. One detail decides | 38 | Intelligent-Tiering + temporary FSx for Lustre linked to S3 | Storage class / FSx detail |
| C | 68 | ASG `UpdatePolicy` AutoScalingRollingUpdate | Change set only previews |

## 4 rules
1. "Quick + cost-effective" DB latency → **add a cache**, don't migrate.
2. Redshift DR other Region: snapshots + **cross-Region snapshot copy**; KMS-encrypted → **snapshot copy grant** first. 🔁×3
3. New AMI to an ASG without downtime → CloudFormation **UpdatePolicy rolling update**.
4. Enforce tags at create → **CloudFormation tags + Service Catalog** (Config = detect only).

## Next actions
1. Read 🇻🇳 sections (🔁 first: Q62, Q1, Q40, Q41, Q56).
2. Tonight: `/ai-tutor sap test-review td3_retake redo A, B, C`.
3. 10-22: final pass over still-missed + 🔁 cards, rule sheet; stop by 18:00. 10-23 exam.
