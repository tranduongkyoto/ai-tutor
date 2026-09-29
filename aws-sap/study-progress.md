---
certification: SAP-C02
started: 2026-09-04
last_updated: 2026-09-28
current_phase: 2
schedule: ~3h/day, 5 days/week (~15h/week)
deadline: none
exam_accommodation: ESL +30 approved (210 min, never expires)
latest_timed_score: 41.3% (TD Set 5, 2026-09-25)
target_exam_window: 2026-11-16 to 2026-11-27
---

# AWS SAP-C02 Study Progress

Background: SAA-C03 passed.

## Phase 1: Foundation — DONE

### Course Progress (Maarek v38 Slides)
| Chapter | Status | Udemy Drill | Date |
|---------|--------|-------------|------|
| Identity & Federation | Done | 8/15 (53%) | 2026-09-15 |
| Security | Done | 10/13 (77%) | 2026-09-15 |
| VPC | Done | 23/30 (77%) | 2026-09-16 |
| Storage | Done | 25/40 (63%) | 2026-09-17 |
| Databases | Done | 19/26 (73%) | 2026-09-18 |

### Hands-on Labs
| Lab | Title | Domain | Status | Date |
|-----|-------|--------|--------|------|
| #176 | ASG + ALB Horizontal Scaling | Compute/HA | Done | 2026-09-11 |
| #244 | Custom VPC with Public/Private Subnets | Networking | Done | 2026-09-11 |
| #3640 | Security Controls + KMS + Data Protection | Security | Done | 2026-09-15 |
| #2934 | ASG Lifecycle Hooks + Lambda + SSM | Compute | Done | 2026-09-15 |
| #2856 | Troubleshoot & Secure AWS Network (SG vs NACL) | VPC | Done | 2026-09-16 |

## Phase 2: Chapter Drills + Timed Baseline — IN PROGRESS

### Chapter Drills — Udemy + TD merged (detail: `practice-exam/sap/chapter_drill_progress.md`)
| Chapter | Udemy | TD (Dojo) | Combined | Answered / pool |
|---|---|---|---|---|
| compute-load-balancing | 0/36 | 13/20 (65%) | 65% 🔴 | 20/131 |
| storage | 25/40 (63%) | 0/94 | 63% 🔴 | 40/134 |
| databases | 19/26 (73%) | 0/74 | 73% 🟡 | 26/101 |
| vpc | 23/30 (77%) | 0/52 | 77% 🟡 | 30/82 |
| identity-federation | 8/15 (53%) | 0/45 | 53% 🔴 | 15/57 |
| monitoring | 0/25 | 11.5/14 (82%) | 82% 🟢 | 14/39 |
| service-communication | 0/22 | 7.5/8 (94%), 14 left | 94% 🟢 | 10/46 |
| security | 10/13 (77%) | 0/24 | 77% 🟡 | 13/37 |
| caching / migrations / deployment / data-eng / cost-control | 0 | 0 | ⬜ | 0/76 |
| **Total** | **85/124 (69%)** | **32/42 (76%)** | **117/166 (70.5%)** | 166/703 |

Note: drill scores give 0.5 partial credit on multi-select; timed tests do not.

### Practice Tests (timed, full-length)
| Test | Date | Score | Notes |
|------|------|-------|-------|
| Udemy Test #1 (30q) | 2026-09-10 | 0/3 (paused Q3) | All 30 Qs later covered via chapter drills |
| Udemy Test #2, #3 (75q) | — | — | Covered via drills only; timed retake planned week 6–7 |
| **TD Set 5 (75q, timed)** | **2026-09-25** | **31/75 (41.3%) ❌** | Finished within 180 min. Analysis: `practice-exam/sap/td_set_5_analysis.md` |
| **TD Set 1 (75q, review mode)** | **2026-09-28** | **46/75 (61.3%) ❌ gate 70%** | Unseen 29/54 (54%), seen 17/21 (81%). Blocks 16/17/13. Analysis: `practice-exam/sap/td_set_1_analysis.md` |
| TD Set 2 (75q, review mode) | — | — | Next. Blocks of 25, multi-select all-or-nothing |
| TD Set 3, 4, 6 | — | — | **Reserved — keep clean** for timed checkpoints |

TD Set 5 domains: Migration 27.8% · New Solutions 36.4% · Org Complexity 50.0% · Continuous Improvement 52.9%.
Multi-select 5/21 (24%) vs single 26/54 (48%).

TD Set 1 domains: Migration 66.7% · New Solutions 53.6% · Org Complexity 84.6% · Continuous Improvement 56.0%.
Multi-select 4/8 (50%) vs single 42/67 (63%).

### TD Set 5 wrong-answer redo (tracker: `practice-exam/sap/td_set_5_review.md`)
| Groups | Pass 1 | Pass 2 due | Pass 3 due |
|---|---|---|---|
| A + B (21) | 09-25 — 20/21 (miss Q18) | 09-28 – 09-29 | ~10-02 |
| C + D (12) | 09-26 — 12/12 | 09-29 – 09-30 | ~10-03 |
| E + F (11) | 09-27 — 10/11 (miss Q48) | 09-30 – 10-01 | ~10-04 |
| **Total** | **42/44 (95%)** | | |

### TD Set 1 wrong-answer redo (tracker: `practice-exam/sap/td_set_1_review.md`)
| Groups | Pass 1 | Pass 2 due | Pass 3 due |
|---|---|---|---|
| A + B (8) — networking/DNS, security | 09-29 — 8/8 | 10-02 – 10-03 | ~10-06 |
| C + D (7) — ops/patching, governance | 09-29 — 7/7 | 10-02 – 10-03 | ~10-06 |
| E (4) — resilience/DR | 09-29 — 4/4 | 10-02 – 10-03 | ~10-06 |
| F + G (10) — serverless, migration | 09-29 — 10/10 | 10-02 – 10-03 | ~10-06 |
| **Total** | **29/29 (100%)** | | |

### TD question usage (for keeping mocks clean)
| Set | Seen | Status |
|---|---|---|
| TD1 | all 75 (review mode, 09-28) | Drill pool / redo |
| TD2 | 14 in drills | Review-mode full set (after TD1) |
| TD5 | all 75 (timed) | Drill pool / redo |
| TD3, TD4 | 2–3 in drills | **Reserved timed mock** |
| TD6 | 0 | **Reserved timed mock** |

## Forecast (updated 2026-09-25, after TD Set 5)

| Scenario | Exam date |
|---|---|
| Optimistic | ~2026-11-09 |
| **Most likely** | **2026-11-16 – 11-27** |
| Conservative | early December |

Assumes ~+8–10 pts per 2 weeks at 15h/week. Book exam only when 2 clean TD sets ≥78%.

### Plan (revised 2026-09-28 — full-set review mode replaces topic-by-topic chapter drills)

Why: chapter drills pre-announce the topic; the Set 5 gap (drill 70.5% → timed 41.3%) is largely topic
identification in a mixed set. Full mixed sets in review mode train that, and the test → review → redo loop
already took Set 5 wrong answers to 42/44 on Pass 1.

| Step | Dates (est.) | Focus | Gate |
|---|---|---|---|
| 1 | Sep 28 – Oct 1 | Set 5 redo Pass 2 (A+B, C+D, E+F) + **TD Set 1 review mode** → review wrong + right answers | — |
| 2 | Oct 2 – Oct 5 | Set 5 redo Pass 3 + **TD Set 2 review mode** → review wrong + right answers | — |
| 3 | by Oct 5 | Check scores: if **migration still <50%** in Set 1/2 → migrations chapter drill (dojo) first | Gate: **TD1 and TD2 each ≥70%** |
| 4 | ~Oct 5–8 | **TD Set 3 timed** (first clean checkpoint) → `test-review` + redo passes | Target ≥65% |
| 5 | ~2 weeks later | Weak domains from Set 3 + **TD Set 4 timed** → review + redo | Target ≥72% |
| 6 | then | Wrong-answer marathon + **TD Set 6 timed** + Udemy #2/#3 timed retakes | 2 clean tests ≥78% → **book exam** |

If TD1/TD2 < 70%: redo their wrong answers (Pass 1–2), drill the weakest domains, then continue to TD Set 3
anyway by ~Oct 12. Don't do review mode on Set 3.

**Review-mode rules** (`/ai-tutor sap review-set <N>`, flow: `references/review-set-flow.md`):
- **Blocks of 25**: answer 25 questions with no feedback, then review all 25, then the next block. Question order is shuffled.
- Multi-select is **all-or-nothing** (no 0.5 partial credit), the same as the timed test.
- Questions already seen in drills (TD1: 21, TD2: 14) are answered and **scored like any other question**. The unseen-only score is shown for information.
- No confidence tags and no keyword step.
- After each set, run the `test-review` flow on `TD_SAP_Review_Set{N}_Full.md` (analysis + review files + redo tracker).

**Keep running alongside:** spaced redo of all wrong answers (Pass 2 at 3–4 days, Pass 3 at ~1 week).
It takes about 30 min per group.

**Time:** each review-mode set takes about 2.5h to answer plus 2–3h to review, so ~5–6h per set.

Drill pool: Udemy + TD Sets 1, 2, 5 only. TD Sets 3, 4, 6 are timed-only.

## Phase 3: Timed Mocks — NOT STARTED
## Phase 4: Final Prep — NOT STARTED

## Summary

| Metric | Value |
|--------|-------|
| Course chapters read | 5/18 (Maarek) |
| Chapter drill questions | 117/166 correct (70.5%) — Udemy 85/124 (69%), TD 32/42 (76%) |
| Timed tests | TD Set 5: 41.3% |
| Labs completed | 5/11 (Maarek) |
| Current phase | 2 — Chapter drills + timed baseline |
| Hours invested | ~30h |

## Weak Areas

### From TD Set 5 (top patterns)
1. **Building your own solution instead of using a managed service** (12 wrong) — Glue, MediaConvert, Service Catalog, Patch Manager, Transfer Family, StackSets service-managed, Compute Optimizer, Lambda Function URL
2. **Multi-account governance** (9) — RAM sharing, SCP `aws:ResourceTag`, cost allocation tags + CUR, Config aggregator, Identity Center + SCIM
3. **Migration tooling** (7) — VM Import, AWS Transform, Migration Evaluator, FSx + DataSync, SES SMTP credentials
4. **DR / Route 53** (5) — cross-Region replica + auto-promote, failover vs weighted, latency + Evaluate Target Health, DX Gateway
5. **Multi-select** — 13/16 misses had 1 correct pick; second pick must complete the same solution

### From TD Set 1 (29 wrong)
1. **Ops: patching/compliance/troubleshooting** — patch groups + Maintenance Windows, tag by environment, Config `approved-amis-by-id`, suspend ASG Terminate
2. **Serverless & app cost patterns** (6) — API Gateway caching, Cognito/web identity federation, S3+CloudFront for reports, AWS Batch, Connect + Lex
3. **Hybrid networking & DNS** — public VIF for VPN, VPN as DX backup, cross-account PHZ association, NAT GW placement
4. Same wrong pick as drill on TD1 Q57/Q16/Q61 (= Set 1 Q64/Q73/Q74) → wrong belief, not a guess

### Repeat misses (drill + Set 5)
- Global Accelerator can't front S3
- S3 access point + gateway endpoint + bucket policy
- S3 RTC with prefix replication rule
- Secrets Manager with ECS (`ValueFrom`) — **missed again in TD1 (Q74)**

### From chapter drills
Public VIF for VPN-over-DX (×4, incl. TD1 Q36), PrivateLink for isolated cross-VPC, can't move EC2 between subnets, Fn::Cidr vs Custom Resource, DX alone not encrypted, Aurora vs RDS reliability, Redshift Spectrum vs Athena, Redshift cross-Region snapshot grant (×2), DynamoDB 400KB + drop table, DMS prerequisites, SCPs + all-features mode, Compute vs EC2 Instance Savings Plans, KPL vs KCL
