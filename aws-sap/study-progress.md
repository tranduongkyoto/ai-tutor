---
certification: SAP-C02
started: 2026-09-04
last_updated: 2026-10-14
current_phase: 2
schedule: 6h+/day sprint, plan A (10-14) — 1 retake/day TD5→TD2→TD3, TD4 gate 10-19, exam ~10-23/24
deadline: 2026-11-16 (last day for SAP-C02; SAP-C03 GA 11-17)
exam_accommodation: ESL +30 approved (210 min, never expires)
latest_timed_score: 88.0% (TD Set 1 retake, 2026-10-14; first-attempt best 56.0% TD3)
exam_booked: 2026-11-02 (SAP-C02, booked 10-12; reschedule decided by gates, max 2 reschedules, decide by 10-31)
target_exam_window: 2026-10-23/24 if Gate 2 passes (retake possible from ~11-07, 9-day buffer before 11-16); fallback keep 11-02
---

# AWS SAP-C02 Study Progress

Background: SAA-C03 passed.

## Phase 1: Foundation — DONE

### Course Progress (Maarek v38 Slides) — updated 2026-10-07 from learner checklist
| Chapter | Status | Drill | Labs |
|---------|--------|-------|------|
| Identity & Federation | Done | Udemy 8/15 (53%) | 2 labs |
| Security | Done | Udemy 10/13 (77%) | #3640 |
| Compute & Load Balancing | Done | TD 13/20 (65%) | #2934, #176 |
| Storage | Done | Udemy 25/40 (63%) | — |
| Caching | Done | — | — |
| Databases | Done | Udemy 19/26 (73%) | #240 |
| Service Communication | Done | TD 7.5/8 (94%) | — |
| Monitoring | Done | TD 11.5/14 (82%) | #3452, #276 |
| Deployment & Instance Management | Done | — | — |
| Migrations | Done | — | — |
| Amazon VPC | Done | Udemy 23/30 (77%) | #2856, #244, #354 (10-09), Traffic Mirroring (10-09) |
| Data Engineering | Done (10-07) | — | — |
| Cost Control | Done (10-07) | — | — |
| Machine Learning | Skimmed 2x (10-07) | — | — |
| Other Services | Skimmed 2x (10-07) | — | — |
| Exam Preparation | Not started | — | — |

### Hands-on Labs
| Lab | Title | Domain | Status | Date |
|-----|-------|--------|--------|------|
| #176 | ASG + ALB Horizontal Scaling | Compute/HA | Done | 2026-09-11 |
| #244 | Custom VPC with Public/Private Subnets | Networking | Done | 2026-09-11 |
| #3640 | Security Controls + KMS + Data Protection | Security | Done | 2026-09-15 |
| #2934 | ASG Lifecycle Hooks + Lambda + SSM | Compute | Done | 2026-09-15 |
| #2856 | Troubleshoot & Secure AWS Network (SG vs NACL) | VPC | Done | 2026-09-16 |
| #240 | RDS Multi-AZ + CloudWatch + SNS | Databases | Done | — |
| #3452 | CloudTrail + CloudWatch Audit | Monitoring | Done | — |
| #276 | VPC Flow Logs + CloudWatch | Monitoring | Done | — |
| (2 labs) | Identity & Federation | Identity | Done | — |
| #354 | Design and Implement Gateway VPC Endpoints (+ endpoint policies) | VPC | Done | 2026-10-09 |
| — | Configuring Traffic Mirroring in AWS VPC | VPC/Security | Done | 2026-10-09 |
| — | Active-Passive Failover with Route 53 Failover Routing | DNS/DR | Done | 2026-10-09 |
| — | Distribute Traffic with Route 53 Weighted Routing | DNS | Done | 2026-10-09 |
| — | Build and Monitor a Resilient System (EC2, RDS Multi-AZ, CloudWatch, SNS) | HA/Monitoring | Done | 2026-10-09 |
| — | Automated Recovery for RPO/RTO with Amazon RDS | DR/Databases | Done | 2026-10-09 |

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
| **TD Set 2 (75q, review mode)** | **2026-09-30 – 10-01** | **43/75 (57.3%) ❌ gate 70%** | Unseen 30/61 (49%), seen 13/14 (93%). Blocks 14/11/18. Analysis: `practice-exam/sap/td_set_2_analysis.md` |
| **TD Set 3 (75q, timed)** | **2026-10-05** | **42/75 (56.0%) ❌ target 65%** | +14.7 pts vs TD5 timed. Analysis: `practice-exam/sap/td_set_3_analysis.md` |
| TD Set 4, 6 | — | — | **Reserved — keep clean** for timed checkpoints |

TD Set 5 domains: Migration 27.8% · New Solutions 36.4% · Org Complexity 50.0% · Continuous Improvement 52.9%.
Multi-select 5/21 (24%) vs single 26/54 (48%).

TD Set 1 domains: Migration 66.7% · New Solutions 53.6% · Org Complexity 84.6% · Continuous Improvement 56.0%.
Multi-select 4/8 (50%) vs single 42/67 (63%).

TD Set 2 domains: Migration 85.7% · Continuous Improvement 73.1% · New Solutions 50.0% · Org Complexity 25.0% 🔴.
Multi-select 10/18 (56%) vs single 33/57 (58%); 7 multi misses had ≥1 correct pick.

TD Set 3 domains: Migration 80.0% · Org Complexity 62.5% · New Solutions 56.5% · Continuous Improvement 51.3% 🔴 (19 of 33 misses).
Multi-select 6/13 (46%) vs single 36/62 (58%); all 7 multi misses had 1 correct pick.

### TD Set 5 wrong-answer redo (tracker: `practice-exam/sap/td_set_5_review.md`)
| Groups | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|
| A + B (21) | 09-25 — 20/21 (miss Q18) | 09-30 — 20/21 (miss Q29) | 10-06 — 19/21 ❌ Q10, Q62 |
| C + D (12) | 09-26 — 12/12 | 09-30 — 12/12 | 10-06 — 11/12 ❌ Q32 |
| E + F (11) | 09-27 — 10/11 (miss Q48) | 09-30 — 9/11 (miss Q21, Q48 🔁) | 10-06 — 10/11 ❌ Q69 |
| **Total** | **42/44 (95%)** | **41/44 (93%)** | **40/44 (91%)** — misses Q10, Q62, Q69 (faded), Q32 (same pick as test); retry 10-07 — 4/4 |

### TD Set 1 wrong-answer redo (tracker: `practice-exam/sap/td_set_1_review.md`)
| Groups | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|
| A + B (8) — networking/DNS, security | 09-29 — 8/8 | 10-02 — 8/8 | 10-06 — 8/8 |
| C + D (7) — ops/patching, governance | 09-29 — 7/7 | 10-02 — 7/7 | 10-06 — 7/7 |
| E (4) — resilience/DR | 09-29 — 4/4 | 10-02 — 2/4 ❌ Q25, Q17 | 10-06 — 4/4 |
| F + G (10) — serverless, migration | 09-29 — 10/10 | 10-02 — 8/10 ❌ Q69, Q57 | 10-06 — 9/10 ❌ Q26 |
| **Total** | **29/29 (100%)** | **25/29 (86%)** — misses Q17, Q57 (same pick as before), Q25, Q69; retry 10-05 — 4/4 | **28/29 (97%)** — miss Q26 (misread) |

### TD Set 2 wrong-answer redo (tracker: `practice-exam/sap/td_set_2_review.md`)
| Groups | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|
| A (9) — identity, access, federation | 10-02 — 9/9 | 10-05 — 9/9 | 10-07 ✅ |
| B (4) — edge/data protection | 10-02 — 4/4 | 10-05 — 4/4 | 10-07 ✅ |
| F (3) — storage/migration | 10-02 — 3/3 | 10-05 — 3/3 | 10-07 ✅ |
| C (6) — DR/HA | 10-02 — 6/6 | 10-05 — 6/6 | 10-07 ✅ |
| D (4) — networking | 10-02 — 4/4 | 10-05 — 4/4 | 10-07 ✅ |
| E (6) — service fit | 10-02 — 6/6 | 10-05 — 6/6 | 10-07 ✅ |
| **Total** | **32/32 (100%)** | **32/32 (100%)** | **32/32 (100%)** (10-07) |

### TD Set 3 wrong-answer redo (tracker: `practice-exam/sap/td_set_3_review.md`)
| Groups | Pass 1 | Pass 2 due | Pass 3 due |
|---|---|---|---|
| A (9) — overbuilt: simplest/cheapest fix | 10-06 — 9/9 | 10-08 — 8/9 ❌ Q63 | ~10-14 |
| B (6) — data protection & network access | 10-06 — 6/6 | 10-08 — 6/6 | ~10-14 |
| C (5) — governance, compliance & IAM | 10-06 — 5/5 | 10-08 — 4/5 ❌ Q71 | ~10-14 |
| D (4) — edge, TLS & API auth | 10-06 — 4/4 | 10-12 — 3/4 ❌ Q10 | ~10-14 |
| E (6) — service fit & limits | 10-06 — 6/6 | 10-12 — 6/6 | ~10-14 |
| F (3) — HA, hybrid, troubleshooting | 10-06 — 2/3 ❌ Q6 | 10-12 — 3/3 | ~10-14 |
| **Total** | **32/33 (97%)** | | |

### TD question usage (for keeping mocks clean)
| Set | Seen | Status |
|---|---|---|
| TD1 | all 75 (review mode, 09-28) | Drill pool / redo |
| TD2 | all 75 (review mode, 09-30 – 10-01) | Drill pool / redo |
| TD5 | all 75 (timed) | Drill pool / redo |
| TD3 | all 75 (timed, 10-05) | Drill pool / redo |
| TD4 | 2–3 in drills | **Reserved timed mock** |
| TD6 | 0 | **Reserved timed mock** |

## Forecast (updated 2026-10-06 — SAP-C02 retires 11-16-2026)

Source: AWS T&C blog "Certification updates: September 2026" — SAP-C03 registration 10-27, **last SAP-C02 day 11-16**,
SAP-C03 GA 11-17 (5 domains; adds GenAI/Bedrock AgentCore, FIS/Resilience Hub/ARC, VPC Lattice, Lake Formation, PQC KMS).

**Decision 10-06: sprint for SAP-C02 at 25h+/week, exam 11-10 – 11-13.**

Timed: TD5 41.3% (09-25) → TD3 56.0% (10-05). Needed pace: **~+10 pts / 2 weeks** → ~66% by mid-Oct, ~76% by early Nov.

**Readiness gates (updated 10-07):** unseen-question scores are the primary signal; retakes are secondary.
No AWS official practice exam (decision 10-07).

| Gate | Source | Date | Go | Switch to SAP-C03 |
|---|---|---|---|---|
| **Gate 1** | **3 isolated unseen tests** (review mode, blocks of 25): Udemy #2 unseen 27 · Udemy #3 unseen 27 · TD6 16 (+ Udemy #1 unseen 5 mini) — combined unseen score; sessions `practice-exam/sap/{udemy2_unseen,udemy3_unseen,td6_isolated,udemy1_unseen}_session.json` | 10-07 – 10-09 | ≥66% combined | <62% (62–65%: keep going) |
| **Gate 2 (final)** | **TD Set 4 timed** (75 unseen) | **10-19** (plan A, 10-14) | ≥75% | <70% |
| Retake check | Full timed retake of TD1/2/3/5; every answer justified | 10-14 – 10-17 | ≥85% on ≥2 of 3 (TD5/TD2/TD3) | — |

**Exam booked 11-02 (10-12).** AWS retake rule: wait 14 calendar days, full fee each attempt, no attempt limit.
11-02 + 14 days = 11-16 = last SAP-C02 day → a C02 retake is possible only if an 11-16 slot exists (zero buffer).

| Gate 2 (TD4, 10-19) + retake check — plan A | Action (decide **10-20**, ≥24 h before the new slot) |
|---|---|
| TD4 ≥75% **and** ≥2 of 3 retakes ≥85% | **Reschedule earlier to 10-23 / 10-24** (uses 1 of 2 reschedules) → C02 retake possible from ~11-07 |
| TD4 70–74% | **Keep 11-02** (+10 days to fix TD4 weak domains) |
| TD4 <70% | Keep 11-02 as last C02 try, or cancel and switch to SAP-C03 |
Gate 1 (10-13) ≥70% → 11-02 looks realistic; <62% → expect to move to 11-10 – 11-13.
Udemy Test #2/#3: 48 of 75 questions each were already seen in chapter drills, so their remaining unseen questions + TD6 are taken as separate isolated tests (split from the merged mock on 10-08).
**TD4 is the last unseen material** — no Dojo drills (they contain TD4/TD6 questions).

Pearson global free-retake offer (09-29 – 11-17) excludes SAP — not usable. Use the SAA-C03 50% voucher if available.

### Sprint plan (SAP-C02, 10-06 → exam 11-02) — updated 10-22 (**plan N**: 10-23 dropped; 2 unseen Neal exams decide whether 11-02 stays)

| Date | Focus |
|---|---|
| 10-06 | ✅ TD3 review + Pass 1 (32/33) · TD1 Pass 3 (28/29) · TD5 Pass 3 (40/44) |
| 10-07 | ✅ TD5 4-miss retry (4/4) · ✅ Cost Control chapter · ✅ re-watch ELB types · ✅ Data Engineering chapter · ✅ Other Services + ML skim · ✅ re-watch FSx + Transfer Family · ✅ 🇻🇳 right-answer sections TD2/3/5 · Gate 1 started (18 answered, carried into the isolated tests) · **book exam** |
| 10-08 | **Gate 1: Udemy #2 unseen ✅ 13/27 (48%)** — misses: Kinesis KDS/Firehose/fan-out ×3, Snow sizing ×2, WAF logs, SSM RunPatchBaseline, SQS message timer, Global Accelerator for DNS caching, CloudFront regional-edge bypass, tenancy, ASG health-check replace · 🇻🇳 review + **redo Pass 1 14/14** · Udemy #3 unseen next |
| 10-09 | ✅ 6 labs: Gateway VPC Endpoints (#354), Traffic Mirroring, Route 53 failover, Route 53 weighted, resilient EC2 + RDS Multi-AZ + CloudWatch/SNS, RDS automated recovery (RPO/RTO) · Gate 1 tests moved |
| 10-10 – 10-11 | Rest (no study) |
| 10-12 | ✅ Udemy #2 unseen Pass 2 14/14 · ✅ TD3 Pass 2 D–F 12/13 (TD3 Pass 2 total 30/33; misses Q63, Q71, Q10 → retry 3/3 ✅) · ✅ **Gate 1: Udemy #3 unseen 19/27 (70%)** (restarted fresh; ~3 near-duplicates of Udemy #2) — misses: ALB host conditions, CloudTrail MFA Delete, MediaConvert+HLS, Traffic Mirroring 🔁, replatform EC2 vs Fargate, Route 53 private-zone health check via CloudWatch alarm, StackSets, Global Accelerator custom routing (subnet endpoints) · Gate 1 running: 32/54 (59%) |
| **10-13** | ✅ **Gate 1 final: TD6 11/16 (69%)** (restarted fresh; misses Athena-on-S3, Inspector Lambda standard scan, CloudFront Functions, tag policy+SCP, Savings Plan scope) · Udemy #1 mini skipped · **Gate 1 = 43/70 (61.4%)**; last two tests 30/43 (70%) · ✅ rule sheet + flashcards + weak-areas validated (TD6 added) · ✅ Udemy #3 redo Pass 1 A–C **8/8** · ✅ TD6 redo Pass 1 A–B **5/5** · ✅ New Solutions flashcards Round 1 **69/72 (96%)** (❌ D11, H3, A3) · ✅ weak-areas Pair drill R1 **55/66 (83%)** (Hybrid networking 7/10, Migration+DR 9/12) · HTML study pages built · ⚠️ TD5 repeat-miss marathon **5/10** (❌ Q12 GA→S3, Q29 cost tag mgmt acct, Q48 OpenSearch Deep Archive, Q69 PrivateLink NLB, Q10 Transfer Family VPC endpoint — all 3rd+ misses) |
| 10-14 | ✅ TD5 marathon misses retry **5/5** (full text, shuffled letters) · ✅ TD1 marathon **5/6** (❌ Q26) · ✅ **TD1 full timed retake 66/75 (88%)** (was 46/75 on 09-28) — 27/29 old misses fixed, 7 regressions; misses Q10 Q21 Q22 Q39 Q45 Q53 Q59 Q68 Q70 · ✅ TD1 retake review 🇻🇳 (`td1_retake_review.md`) · switched to plan A · tonight: TD1 retake redo Pass 1 (9) |
| **10-15** | ✅ TD1 retake redo Pass 1 **9/9** (shuffled letters) · ✅ **TD5 full timed retake 66/75 (88%)** in 21 min (was 31/75 on 09-25) — 41/44 old misses fixed, 6 regressions; misses Q8 Q17🔁 Q22 Q38 Q39 Q44 Q48🔁 Q55 Q70🔁 · ✅ TD5 retake review 🇻🇳 + TD5 flashcards page (75) · ✅ TD5 retake redo Pass 1 **9/9** (shuffled) · ✅ TD1 flashcards R1 **73/75 (97%)** (❌ H3 Fargate quota alarm via AWS/Usage, B7 public VIF for VPN over DX 🔁) · **TD5 full timed retake** (morning) → `test-review --vi` (afternoon) → redo TD5 misses Pass 1 (night) · 15 min rule sheet |
| **10-16** | ✅ TD5 flashcards R1 **75/75 (100%)** · ✅ **TD2 full timed retake 67/75 (89.3%)** (was 43/75) — 31/32 old misses fixed, 7 regressions; misses Q15 Q17 Q26🔁 Q42 Q45 Q53 Q58 Q62 · ✅ TD2 review 🇻🇳 + flashcards · redo TD2 misses tonight |
| **10-17** | **TD3 full timed retake** + review · redo TD3 misses · TD2 misses Pass 2 |
| 10-18 | TD3 misses Pass 2 · one pass over all retake misses (TD1/5/2/3) · rule sheet self-test · light evening, sleep early |
| **10-19** | ✅ TD2 retake redo Pass 1 **13/13** (8 misses + 5 unsure-right, shuffled) · ✅ TD2 flashcards R1 **74/75** (❌ F12 S3 Transfer Acceleration vs multipart) · ⚠️ **TD Set 4 timed — Gate 2: 50/75 (66.7%)** in 180 min — **first attempt, unseen** — Migration 100%, Org 100%, New Solutions 68%, **Continuous Improvement 56%**; multi-select 9/16 (all 7 misses partial); thirds 18/18/**14** · **Gate rule <70% → keep 11-02, no earlier reschedule** |
| **10-20** | ✅ TD4 review 🇻🇳 built 10-19 (25 misses, `td4_review.md`) + flashcards `td4-flashcards.html` · ✅ TD4 redo Pass 1 **25/25** (all groups, shuffled order + letters, ~5 h after reading 🇻🇳) · ✅ TD4 flashcards R1 **74/75 (99%)** (❌ E17 read-heavy RDS → ElastiCache + read replicas, not CloudFront — TD4 Q72) · ~~reschedule to 10-23/24~~ → **decided 10-19: keep 11-02** (TD4 <70%) · new 13-day plan |
| **10-21** | ✅ **TD3 full timed retake 66/75 (88%)** (was 42/75 on 10-05) — CI **87.2%** (was 51%), 29/33 old misses fixed, 5 regressions; misses Q1🔁 Q34 Q38 Q40🔁 Q41🔁 Q47 Q56🔁 Q62🔁 (Redshift DR 3rd) Q68 · ✅ TD3 retake review 🇻🇳 · **10-23 gate: GO** (TD3 ≥80% + CI ≥65%) · ✅ TD3 redo Pass 1 **9/9** (shuffled) · ✅ rule-sheet flashcards page built (133 cards, 36 🔁) |
| **10-22** | ✅ **Neal Exam A 54/75 (72%)** unseen, 210 min (time up, all answered) — ORG 69 · NEW 73 · CI 74 · MIG 69; single 42/54, **multi 12/21 (8/9 misses half right)**; thirds **16**/19/19 · gate ≥80% not met (decision after Neal B) · ✅ review 🇻🇳 (`neal_a_review.md`, 21 misses) |
| 10-23 | ✅ Neal A redo Pass 1 **21/21** (shuffled order + letters; all 9 multi-select complete) · ✅ Q34 explanation corrected (active/active + Spot trap) · ✅ Neal A flashcards R1 **73/75 (97%)** (❌ A7 account per team via Organizations vs security account as mgmt account, H2 Cost Anomaly Detection vs static Budgets) · rule-sheet flashcards 🔁 |
| 10-24 – 10-25 | Fix Neal A weak domains (concept review + targeted drills, no retakes of seen sets) · 1 rest half-day |
| **10-26** | ✅ Rule-sheet flashcards R1 (all 133) **125/133 (94%)** — ❌ G16 EFS Provisioned vs Max I/O, G3🔁 S3 static only, C14🔁 GA can't front S3, C7🔁 S3 gateway endpoint vs NAT, C17 CloudFront Functions, A7🔁 twin options, F16 DynamoDB reserved capacity, E23 CFN pipeline (no CodeDeploy); §2 Networking/edge weakest 15/18 · ✅ **Neal Exam B 55/75 (73.3%)** unseen, 210 min (time up; 6/7 flags in Q69–74) — ORG **57** · NEW 71 · CI 74 · MIG 77; single **36/54 (67%)**, multi **19/21 (90%)** (Select THREE 5/5); thirds 20/19/**16**; misses security-data 6, identity-org 4 · ✅ review 🇻🇳 (`neal_b_review.md`, 20 misses) · gate ≥77/80% not met → decide 11-02 on 10-27 |
| **10-27** | ✅ Neal B redo Pass 1 **19/20** (shuffled order + letters; both multi-select complete) — ❌ Q10🔁 25 TB/1 Gbps chose DataSync (key: S3 Transfer Acceleration; key debatable) · ✅ Neal B flashcards R1 **74/75 (99%)** (❌ E8 burst async jobs → SQS + Lambda, not Step Functions per job; retry 10-29) · ✅ Labs report updated (8 Udemy do / 3 optional / 20 skip + Whizlabs map) + 6 Claude lab guides (SCP, TGW, Resolver, CloudFront, S3 CRR, DMS) · SAP-C02 last day 11-16 confirmed; slots free 11-09/11-13/11-16 · thebeststudy rejected (dump-sourced) · **Gate moved to 10-31** (Official Practice Exam + Neal C): pass → 11-02, else → 11-09 · **Decision (≥24 h before 11-02, uses reschedule 1 of 2):** A ≥80% **and** B ≥80% → **keep 11-02** · 75–79% → keep 11-02 if trend ↑, else move · <75% → **move to 11-06 – 11-10** (last C02 day 11-16, no retake buffer) |
| **10-28** | ✅ **Udemy #2 full timed 61/75 (81.3%)** · ✅ review 🇻🇳 (`udemy2_full_review.md`, 14 misses: A facts 4 · B half-right multi 6 · C hybrid/migration 4; 🔁 Q13 Q24 Q33 Q54 Q63 Q68) (all 75 seen in drills → pacing run, not readiness) — first pass done at **165 min** (25 @ 51', 50 @ 105'), first time not timed out · 4-phase order: single pass1 37/44 · skipped singles 6/6 · multi-2 14/19 · multi-3 **3/6** · flags well calibrated (flagged 17/30 right vs unflagged 43/45) · review 28 min on 30 flags: 5 changes → 3 fixed (Q43, Q52, Q55) / 2 broken (Q11, Q67, both single) = **+1 net** · pre-review snapshot `practice-exam/sap/exam_runs/udemy2-pre-review-snapshot-261028.json` · ✅ Skill Builder annual subscription active (Official Practice Exam SAP-C02 enrolled for 10-30) · exam pages: highlight/strike/keyword + per-question live timer |
| **10-29** | ✅ Udemy #2 redo Pass 1 **14/14** (groups A–C, shuffled order + letters; all 7 multi-select complete, incl. 🔁 Q13 Q24 Q33 Q54 Q63 Q68) · review file now also lists the 5 review-time answer changes (3 fixed, 2 broken) with 🇻🇳 for Q43 Q52 Q55 |
| **10-29** | ✅ **AWS Official Practice Exam: 783 scaled (pass ≥750)** · ✅ review 🇻🇳 (`official_attempt1_review.md`, 28 misses: A twin options 14 · B wrong fit 11 · C org tooling 3) + analysis with raw→scaled equivalence table — raw 47/75 (62.7%), first real attempt (export label 'Lần thi 2' ignored), 195.6 min · domains ORG 10/18 (56%, Task 1.3 resilience 0/2, 1.4 multi-account 1/4) · NEW 14/22 (64%, **Task 2.1 deployment 0/3**) · **CI 10/20 (50%, Needs Improvement**: security 2/5, cost 2/5, reliability 1/3, performance 2/4) · MIG 13/15 (87%) · thirds 17 / 19 / **11** (last third 44%) · single 42/67 · multi 5/8 · 28 misses: ~14 twin-option (one differing phrase: Archive vs Deep Archive, DLM vs AWS Backup, Volume vs File Gateway, Budgets action vs operator, Fargate vs custom AMI…), ORG/governance 6 (Q13 Q26 Q57 Q62 Q64 Q65), automation-over-manual 4 · ⚠️ Q74 key dated (Object Lock can be enabled on existing buckets since 2023) · gate band 750–799 → 11-02 only if Neal C ≥72% in the mix exam |
| **10-30** | ✅ Official redo Pass 1 **28/28** (groups A–C, shuffled order + letters; 3 multi-select complete) — 1 day after review, memory-assisted |
| **10-30** | ⚠️ **Neal Exam C 25/35 (71.4%)** unseen · ✅ review 🇻🇳 (`neal_c_review.md`, 10 misses: A over-built 5 7 13 · B security control 9 12 19 30 · C resilience/governance 11 20 31; 🔁 Q5 Q7 Q13), 94 min of 98 (first pass done at 86'; review 12' made 1 change: Q22 B→A ✅ fixed) — CI **7/13 (54%)** · 10 misses: Q5 Q7 Q9 Q11 Q12 Q13 Q19 Q20 Q30 Q31 · thirds 7/11 · 7/11 · 9/11 · multi 4/7 (3 half-right) · in-pass answer changes: 5 fixed, 2 broken (Q5, Q30) · official-equivalent ≈ 763 (Neal −10.6 pp) · **gate 70–75% band: no time-out + last third 9/11 (82%) → 11-02 allowed, thin margin** · pre-review snapshot `practice-exam/sap/exam_runs/neal-c-pre-review-snapshot-261030.json` (pre-review 24/35) |
| **10-31** | ✅ Final-review flashcards R1 **71/73 (97%)** — official 28/28 · Neal C 8/10 · Neal A/B 17/17 · TD4 + Udemy #2 18/18 · ❌ B2 write-heavy DynamoDB → on-demand only, DAX caches reads only (Neal C Q7 🔁) · B10 DX redundancy + second Region → second DX to the same Region + DX gateway, not a new DX to Region 2 (Neal C Q31 🔁) · retry B2, B10 on 11-01 (2 cards, light review on the rest day) · ✅ TD4 flashcards R2 **73/75 (97%)** (page shows "Round 1" because its saved rounds were reset; R1 was 74/75 on 10-20; E17 now ✅) — ❌ E14 🔁 cut 45-min photo metadata job → split Lambda per metadata type + Step Functions parallel workflow per photo, no SQS in front (TD4 Q63) · D7 CPU ≤15% → terminate one instance via CloudWatch alarm + ASG scale-in policy, not scheduled actions (load is unpredictable) (TD4 Q37) · retry E14, D7 on 11-01 |
| 10-28 – 10-30 | Neal B redo + weak domains · flashcards 🔁 |
| 10-30 / 10-31 | **Neal Exam C** (35, 98 min) final check — ≥80% confirms; <70% → consider moving (still ≥24 h before) |
| 11-01 | Rest · logistics (ID, check-in, ESL +30) |
| **11-02** | **Exam attempt 1 (210 min)** unless moved on 10-27 · retake from 11-16 only if a slot exists |

**Dropped in plan A:** new course material, Udemy passes, extra drills, new tools. Kept: retake → review → redo misses, 15 min rule sheet/day.

### Plan (revised 2026-09-28 — superseded 10-06 by the sprint plan above — full-set review mode replaces topic-by-topic chapter drills)

Why: chapter drills pre-announce the topic; the Set 5 gap (drill 70.5% → timed 41.3%) is largely topic
identification in a mixed set. Full mixed sets in review mode train that, and the test → review → redo loop
already took Set 5 wrong answers to 42/44 on Pass 1.

| Step | Dates (est.) | Focus | Gate |
|---|---|---|---|
| 1 | Sep 28 – Oct 1 | Set 5 redo Pass 2 (A+B, C+D, E+F) + **TD Set 1 review mode** → review wrong + right answers | — |
| 2 | Oct 2 – Oct 5 | Set 5 redo Pass 3 + **TD Set 2 review mode** → review wrong + right answers | — |
| 3 | by Oct 5 | Check scores: if **migration still <50%** in Set 1/2 → migrations chapter drill (dojo) first | Gate: **TD1 and TD2 each ≥70%** |
| 4 | ~Oct 5–8 | **TD Set 3 timed** (first clean checkpoint) → `test-review` + redo passes — **done 10-05: 56.0%** | Target ≥65% ❌ |
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
| Course chapters read | 15/16 (Maarek) — only Exam Prep left (planned 10-14) |
| Chapter drill questions | 117/166 correct (70.5%) — Udemy 85/124 (69%), TD 32/42 (76%) |
| Timed tests | TD Set 5: 41.3% → TD Set 3: 56.0% |
| Labs completed | 10/11 (Maarek) — #354 skipped |
| Current phase | 2 — Chapter drills + timed baseline |
| Hours invested | ~30h |

## Weak Areas

**Ranked view + confusion pairs: `aws-sap/weak-areas.md`** (built 10-13 from all 160 misses). The per-set lists below are the raw source.

### From TD Set 5 (top patterns)
1. **Building your own solution instead of using a managed service** (12 wrong) — Glue, MediaConvert, Service Catalog, Patch Manager, Transfer Family, StackSets service-managed, Compute Optimizer, Lambda Function URL
2. **Multi-account governance** (9) — RAM sharing, SCP `aws:ResourceTag`, cost allocation tags + CUR, Config aggregator, Identity Center + SCIM
3. **Migration tooling** (7) — VM Import, AWS Transform, Migration Evaluator, FSx + DataSync, SES SMTP credentials
4. **DR / Route 53** (5) — cross-Region replica + auto-promote, failover vs weighted, latency + Evaluate Target Health, DX Gateway
5. **Multi-select** — 13/16 misses had 1 correct pick; second pick must complete the same solution

### From TD Set 3 (33 wrong) — Continuous Improvement 51%
1. **Overbuilding** (9) — hot standby / Reserved / full migration / DIY broker when the stem says quick, one-off or cost-effective; EMR one-off missed twice (Q20, Q29)
2. **Data protection & access** (6) — SSE-KMS for own key, KMS EXTERNAL import, S3 Block Public Access, Traffic Mirroring, SG-to-SG
3. **Edge/TLS** (4) — SNI multi-cert, CloudFront default vs ACM cert, API Gateway AWS_IAM + X-Ray
4. Repeats on new questions: file gateway + Rekognition (3rd miss), detect-not-block AMIs (TD1 Q12), SCP allow-list, web identity temp creds
5. Fixed on new questions: External ID, LDAP broker, Storage Gateway → EBS, Redshift snapshot copy grant

### From TD Set 2 (32 wrong) — Org Complexity 25%
1. **Identity & federation** — SAML → AssumeRoleWithSAML/Identity Center (not WebIdentity), External ID for 3rd party, LDAP identity broker, cross-account role lives in the *target* account
2. **SCP vs IAM** — SCPs only set guardrails, never grant access (Q66, Q75)
3. **DR/HA terms** — warm standby (RTO minutes) vs pilot light, Multi-AZ ≠ DR, RDS has no Oracle RAC/RMAN
4. **Service confusion** — Translate vs Transcribe, Storage Gateway cached vs stored, sc1 vs st1 vs io1, SSE-S3 vs SSE-KMS, S3 versioning null IDs
5. **Lambda concurrency** — reserved concurrency to isolate a function (not a separate account)

### From TD Set 1 (29 wrong)
1. **Ops: patching/compliance/troubleshooting** — patch groups + Maintenance Windows, tag by environment, Config `approved-amis-by-id`, suspend ASG Terminate
2. **Serverless & app cost patterns** (6) — API Gateway caching, Cognito/web identity federation, S3+CloudFront for reports, AWS Batch, Connect + Lex
3. **Hybrid networking & DNS** — public VIF for VPN, VPN as DX backup, cross-account PHZ association, NAT GW placement
4. Same wrong pick as drill on TD1 Q57/Q16/Q61 (= Set 1 Q64/Q73/Q74) → wrong belief, not a guess

### Repeat misses (drill + Set 5)
- Global Accelerator can't front S3
- S3 access point + gateway endpoint + bucket policy
- S3 RTC with prefix replication rule
- Cost allocation tags: activate in the **management account** (Set 5 Q29, missed Pass 2)
- OpenSearch storage tiers: keep hot data nodes (fewer) + UltraWarm + cold; ingest needs hot nodes (Set 5 Q48, missed Pass 1 + 2)
- S3 traffic via NAT → S3 gateway endpoint; "availability not compromised" rules out Spot (Set 5 Q21, missed Pass 2)
- Secrets Manager with ECS (`ValueFrom`) — **missed again in TD1 (Q74)** (fixed in TD1 Pass 1 + 2)
- CloudFront 504 + minimal cost → **origin group failover**, not multi-Region + latency routing (TD1 Q17, same D,E pick, missed Pass 2)
- Tape library + process the content → **file gateway** (S3) for Rekognition, not tape gateway (TD1 Q57, same B pick, missed Pass 2; **missed again on new TD3 Q14**)
- RDS MySQL has no single reader endpoint (Aurora only) → offload reads with ElastiCache (TD1 Q25, missed Pass 2)
- HPC batch + least overhead → **AWS Batch** on Spot + S3, not EKS/EBS sc1 (TD1 Q69, missed Pass 2)
- Windows servers **in AWS** need SMB files → **FSx for Windows + DataSync**, not File Gateway (on-prem clients) (Set 5 Q32, same D pick, missed Pass 3)
- PrivateLink endpoint service = **NLB** (or GWLB), never ALB; appliance fleet = **GWLB + ASG** (Set 5 Q69, Q62, missed Pass 3)

### From chapter drills
Public VIF for VPN-over-DX (×4, incl. TD1 Q36), PrivateLink for isolated cross-VPC, can't move EC2 between subnets, Fn::Cidr vs Custom Resource, DX alone not encrypted, Aurora vs RDS reliability, Redshift Spectrum vs Athena, Redshift cross-Region snapshot grant (×2), DynamoDB 400KB + drop table, DMS prerequisites, SCPs + all-features mode, Compute vs EC2 Instance Savings Plans, KPL vs KCL

## Final-review deck round log

Deck: `aws-sap/final-review-flashcards.html` (73 recent misses). Target ≥ 80%.

| Round | Date | Score | ❌ cards |
|-------|------|-------|----------|
| 1 | 2026-10-31 | 71/73 | B2, B10 |
