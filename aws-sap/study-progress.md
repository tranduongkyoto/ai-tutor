---
certification: SAP-C02
started: 2026-09-04
last_updated: 2026-10-06
current_phase: 2
schedule: ~25h+/week sprint until exam (was ~15h/week)
deadline: 2026-11-16 (last day for SAP-C02; SAP-C03 GA 11-17)
exam_accommodation: ESL +30 approved (210 min, never expires)
latest_timed_score: 56.0% (TD Set 3, 2026-10-05)
target_exam_window: 2026-11-10 to 2026-11-13 (SAP-C02, before retirement)
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
| Amazon VPC | Done | Udemy 23/30 (77%) | #2856, #244; #354 skipped (10-07) |
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
| #354 | Gateway VPC Endpoints + Endpoint Policies | VPC | Skipped (learner decision) | 10-07 |

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
| A (9) — overbuilt: simplest/cheapest fix | 10-06 — 9/9 | ~10-10 | ~10-14 |
| B (6) — data protection & network access | 10-06 — 6/6 | ~10-10 | ~10-14 |
| C (5) — governance, compliance & IAM | 10-06 — 5/5 | ~10-10 | ~10-14 |
| D (4) — edge, TLS & API auth | 10-06 — 4/4 | ~10-10 | ~10-14 |
| E (6) — service fit & limits | 10-06 — 6/6 | ~10-10 | ~10-14 |
| F (3) — HA, hybrid, troubleshooting | 10-06 — 2/3 ❌ Q6 | ~10-10 | ~10-14 |
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
| **Gate 2 (final)** | **TD Set 4 timed** (75 unseen) | ~10-28 | ≥75% | <70% |
| Retake check | One full timed retake of TD1/2/3/5, ≥2 weeks after last seen; every answer justified | ~10-20 onward | ≥85% | — |

**Book / keep the exam date only if** Gate 2 ≥75% **and** one retake ≥85%.
Udemy Test #2/#3: 48 of 75 questions each were already seen in chapter drills, so their remaining unseen questions + TD6 are taken as separate isolated tests (split from the merged mock on 10-08).
**TD4 is the last unseen material** — no Dojo drills (they contain TD4/TD6 questions).

Book the SAP-C02 slot now (slots near 11-16 fill up); check the Pearson VUE reschedule/cancel window and the
SAA-C03 50% discount voucher (Certification account → Benefits) when booking.

### Sprint plan (SAP-C02, 10-06 → 11-13) — updated 10-07

| Date | Focus |
|---|---|
| 10-06 | ✅ TD3 review + Pass 1 (32/33) · TD1 Pass 3 (28/29) · TD5 Pass 3 (40/44) |
| 10-07 | ✅ TD5 4-miss retry (4/4) · ✅ Cost Control chapter · ✅ re-watch ELB types · ✅ Data Engineering chapter · ✅ Other Services + ML skim · ✅ re-watch FSx + Transfer Family · ✅ 🇻🇳 right-answer sections TD2/3/5 · Gate 1 started (18 answered, carried into the isolated tests) · **book exam** |
| 10-08 | **Gate 1: Udemy #2 unseen ✅ 13/27 (48%)** — misses: Kinesis KDS/Firehose/fan-out ×3, Snow sizing ×2, WAF logs, SSM RunPatchBaseline, SQS message timer, Global Accelerator for DNS caching, CloudFront regional-edge bypass, tenancy, ASG health-check replace · 🇻🇳 review + **redo Pass 1 14/14** · Udemy #3 unseen next |
| 10-09 | **Gate 1: TD6 + Udemy #1 mini** · combined score · TD3 Pass 2 D–F (A–C ✅ 18/20 on 10-08; misses Q63 AppStream, Q71 PowerUserAccess) |
| 10-10 – 10-14 | TD3 right-answer "Guessed?" review · repeat-miss list · Gate 1 misses Pass 2 (10-13) |
| 10-15 – 10-19 | weak-area re-watch (from Gate 1 domains) · TD3 Pass 3 · wrong-answer marathon round 1 |
| ~10-20 | **TD5 full timed retake** (retake check) |
| 10-21 – 10-26 | TD1/TD2 retake · Gate 1 misses Pass 3 · Exam Preparation chapter (10-26) |
| **~10-28** | **TD Set 4 timed — Gate 2 (final)** → `test-review --vi` |
| 10-29 – 10-30 | TD4 review + Pass 1 |
| 10-31 – 11-09 | Pass 3s · wrong-answer marathon (all 🔁 repeat misses) · 10 rules per set |
| **11-10 – 11-13** | **Exam (210 min with ESL +30)** |

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
