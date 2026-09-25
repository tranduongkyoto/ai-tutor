---
certification: SAP-C02
started: 2026-09-04
last_updated: 2026-09-25
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
| TD Set 3, 4, 6 | — | — | **Reserved — keep clean** for checkpoints |

TD Set 5 domains: Migration 27.8% · New Solutions 36.4% · Org Complexity 50.0% · Continuous Improvement 52.9%.
Multi-select 5/21 (24%) vs single 26/54 (48%).

### TD question usage (for keeping mocks clean)
| Set | Seen | Status |
|---|---|---|
| TD1 | 21 in drills | Drill pool |
| TD2 | 14 in drills | Drill pool |
| TD5 | all 75 (timed) | Drill pool / redo |
| TD3, TD4 | 2–3 in drills | **Reserved mock** |
| TD6 | 0 | **Reserved mock** |

## Forecast (updated 2026-09-25, after TD Set 5)

| Scenario | Exam date |
|---|---|
| Optimistic | ~2026-11-09 |
| **Most likely** | **2026-11-16 – 11-27** |
| Conservative | early December |

Assumes ~+8–10 pts per 2 weeks at 15h/week. Book exam only when 2 clean TD sets ≥78%.

### Plan
| Week | Focus | Checkpoint |
|---|---|---|
| 1 (Sep 25–Oct 1) | Redo 44 Set 5 wrong answers + multi-select technique + migrations chapter | — |
| 2 (Oct 2–8) | Multi-account governance (RAM, StackSets, SCP conditions, Service Catalog, Identity Center, billing) | — |
| 3 (Oct 9–15) | DR/Route 53, DX, PrivateLink/GWLB, RDS Proxy + redo all wrong answers | **TD Set 3 timed → 55–60%** |
| 4–5 | Weak domains from Set 3 + unstarted chapters (caching, deployment, cost, data-eng) | **TD Set 4 timed (~Oct 29) → 68–72%** |
| 6–7 | Wrong-answer marathon + Set 6 + Udemy #2/#3 timed retakes | 2 tests ≥78% → **book exam** |

Drill pool: Udemy + TD Sets 1, 2, 5 only.

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

### Repeat misses (drill + Set 5)
- Global Accelerator can't front S3
- S3 access point + gateway endpoint + bucket policy
- S3 RTC with prefix replication rule
- Secrets Manager with ECS (`ValueFrom`)

### From chapter drills
Public VIF for VPN-over-DX (×3), PrivateLink for isolated cross-VPC, can't move EC2 between subnets, Fn::Cidr vs Custom Resource, DX alone not encrypted, Aurora vs RDS reliability, Redshift Spectrum vs Athena, Redshift cross-Region snapshot grant (×2), DynamoDB 400KB + drop table, DMS prerequisites, SCPs + all-features mode, Compute vs EC2 Instance Savings Plans, KPL vs KCL
