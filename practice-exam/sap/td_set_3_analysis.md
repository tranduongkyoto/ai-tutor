# TD Set 3 (Timed) — Analysis

**Date:** 2026-10-05 · **Mode:** timed, first clean checkpoint · multi-select all-or-nothing
**Score:** 42/75 (**56.0%**) ❌ — checkpoint target 65%, gate 70%, exam-ready 78–80%
**Source:** `TutorialsDojo_SAP_Timed_Mode_Set_3.md` (Q numbers = export order, grouped by domain — not the shuffled web order, so per-third accuracy says nothing about fatigue)
**Review files:** `td_set_3_review.md` (33 wrong + tracker + 🇻🇳) · `td_set_3_review_correct.md` (42 right + "Guessed?" tracker)

## Scores

| Domain | Score |
|---|---|
| Accelerate Workload Migration and Modernization | 4/5 (80.0%) 🟢 |
| Design Solutions for Organizational Complexity | 5/8 (62.5%) 🟡 |
| Design for New Solutions | 13/23 (56.5%) 🔴 |
| **Continuous Improvement for Existing Solutions** | **20/39 (51.3%)** 🔴 — 19 of 33 misses |

| Slice | Score |
|---|---|
| Single-choice | 36/62 (58%) |
| Multi-select | 6/13 (46%) — **all 7 misses had one correct pick** |

## Trend

| | TD5 (timed) | TD1 (review) | TD2 (review) | **TD3 (timed)** |
|---|---|---|---|---|
| Total | 41.3% | 61.3% | 57.3% | **56.0%** |
| Migration | 27.8% | 66.7% | 85.7% | **80.0%** |
| Continuous Improvement | 52.9% | 56.0% | 73.1% | **51.3%** |
| New Solutions | 36.4% | 53.6% | 50.0% | **56.5%** |
| Org Complexity | 50.0% | 84.6% | 25.0% | **62.5%** |

Timed vs timed: **+14.7 pts** since TD5 (41.3 → 56.0) in 10 days. Migration is solid. Continuous Improvement
is half of this set and fell back to ~51% — most misses there are "picked the heavier solution" (group A).

## Wrong answers by pattern (33)

| Group | Wrong | Questions |
|---|---|---|
| A. Overbuilt — simplest/cheapest fix wins | 9 | 16, 20, 24, 26, 29, 30, 42, 63, 72 |
| B. Data protection & network access | 6 | 13, 17, 28, 37, 45, 55 |
| C. Governance, compliance & IAM | 5 | 48, 60, 61, 71, 75 |
| D. Edge, TLS & API auth | 4 | 7, 10, 23, 50 |
| E. Service fit & service limits | 6 | 1, 14, 19, 32, 53, 57 |
| F. HA, hybrid & troubleshooting | 3 | 6, 8, 58 |

### A. Overbuilt (9) — biggest group
| Q | Correct | Why your pick failed |
|---|---|---|
| 16 🔁 | EC2 snapshots to backup Region + Aurora cross-Region replica | Hot standby too costly for RTO 30 min |
| 20 | EMR: On-Demand master/core + Spot task | Reserved for a one-off 48 h job |
| 29 | Same as Q20 | Reserved for a one-off 8 h job — **same concept missed twice in one test** |
| 24 | SQS buffer → consumer flushes to on-prem DB | DynamoDB + EMR = far more cost |
| 30 🔁 | ElastiCache for Redis | Migrating to Aurora isn't "quick" |
| 42 | CloudFront in front of on-prem origin | Full migration takes too long |
| 72 | Grow FSx in place (CloudWatch → EventBridge → Lambda) | New FS + copy = manual |
| 63 | AppStream (WorkSpaces applications) + Aurora + ASG/ALB | WorkSpaces per user = expensive |
| 26 | AWS IoT Core + IoT rule → DynamoDB | DIY broker on ASG + NLB + EFS |

### B. Data protection & network access (6)
| Q | Correct | Why your pick failed |
|---|---|---|
| 13 | S3 SSE-KMS + HTTPS-only bucket policy | SSE-S3 = AWS-owned key |
| 17 🔁 | Endpoint policy + IAM role + bucket policy (vpce + role) | NACL can't do this |
| 28 | KMS key Origin=EXTERNAL + import from on-prem HSM | CloudHSM ≠ company's own HSMs |
| 37 🔁 | S3 Block Public Access | SCP = much more effort |
| 45 | VPC Traffic Mirroring | Flow Logs have no payloads |
| 55 | SG-to-SG rules (B + C) | NACL with subnet CIDR = too broad |

### C. Governance, compliance & IAM (5)
| Q | Correct | Why your pick failed |
|---|---|---|
| 48 | Inspector CVE scan + EventBridge 30-day → SSM Automation | Config can't scan the OS |
| 60 🔁 | Config rule + scheduled Lambda (detect after launch) | IAM block stalls CI/CD — **same as TD1 Q12** |
| 61 | EC2 + Patch Manager | CloudShell isn't a server host |
| 71 | PowerUserAccess | AdministratorAccess ≠ least privilege |
| 75 🔁 | SCP allow-list lacks s3:* | SCPs never grant — IAM policy wasn't the blocker |

### D. Edge, TLS & API auth (4)
| Q | Correct | Why your pick failed |
|---|---|---|
| 7 | AWS_IAM auth + SigV4 + X-Ray | CORS isn't auth; CW Logs isn't tracing |
| 10 | ALB SNI multi-cert + CloudFront dedicated-IP SSL | Wildcard ≠ different domains |
| 23 | ACM cert on CloudFront (custom domain) | Default cert only for *.cloudfront.net |
| 50 | Viewer Protocol Policy + default CloudFront cert | ELB cert = origin side only |

### E. Service fit & service limits (6)
| Q | Correct | Why your pick failed |
|---|---|---|
| 1 | SQS + EC2 ASG on queue depth | Lambda max 15 min < 30 min job |
| 14 🔁🔁 | File Gateway → S3 + Rekognition | **Third miss** (TD1 Q57 ×2); SageMaker notebook doesn't recognize faces |
| 19 | Read replica + SNS email | SQS can't send email |
| 32 | Kinesis Data Streams → Redshift | S3 + SQS isn't near-real-time |
| 53 | Beanstalk Immutable + CloudFormation | All at once drops capacity |
| 57 🔁 | Web identity federation (STS temporary creds) | Option used long-term access keys |

### F. HA, hybrid & troubleshooting (3)
| Q | Correct | Why your pick failed |
|---|---|---|
| 6 | URL expired + bad credentials on EC2 | Versioning doesn't invalidate URLs |
| 8 | Second CGW in another data center | Only one VGW per VPC |
| 58 | ASG 3 AZ + ALB + Aurora Replicas + Alias | A record can't point to an ELB |

## Inconsistent concepts (right in one, wrong in another)
| Right | Wrong | Concept |
|---|---|---|
| Q21, Q22, Q27 | Q24 | SQS as write buffer |
| Q40 | Q30 | ElastiCache cuts DB latency |
| Q66 | Q61 | Patch Manager for OS patching |
| Q3 | Q14 | Tape backup → Tape Gateway; process content → File Gateway |
| Q52 | Q17, Q6 | EC2 → S3 via IAM role |
| Q73, Q74 | Q57 | Federation → STS temporary credentials |
| Q59 | Q75 | SCP behavior |
| Q31 | Q7 | X-Ray tracing |
| Q54, Q56 | Q53 | Zero-downtime deployment |
| Q15, Q43 | Q16 | Cross-Region DR sized to RTO |

**Fixed since TD1/TD2 (answered right on new questions):** External ID (Q73), LDAP identity broker (Q74),
Storage Gateway → EBS restore (Q51), Redshift snapshot copy grant (Q65), Oracle RAC → EC2 (Q2).

## Multi-select lesson
7/7 misses had one correct pick (Q6, Q10, Q16, Q48, Q50, Q55, Q60). Second picks failed because they were
**heavier** (hot standby, IAM block) or **the wrong layer** (wildcard cert, ELB cert, NACL CIDR, Config for CVEs,
versioning). Same pattern as TD1/TD2 → check the second pick against the exact requirement word.

## 10 rules
1. **Read the cost/time word first** — "quick", "one-off", "minimal effort", "cost-effective" → the lightest option that works.
2. One-off EMR → On-Demand master/core + Spot task; **never Reserved** for short jobs.
3. RTO tens of minutes for stateless tiers → restore from snapshots, not hot standby.
4. Write bursts → **SQS buffer**; read latency → **ElastiCache**; traffic bursts on-prem → **CloudFront**.
5. "Don't block developers" → **detect + remediate after launch**, never IAM deny.
6. **SCPs never grant**: an allow-list SCP must list every needed action.
7. Tape: backup workflow → Tape Gateway; process/tag the content → **File Gateway + Rekognition**.
8. Lambda max 15 min; longer jobs → EC2/ECS workers on SQS depth.
9. CloudFront certs: *.cloudfront.net → default cert; custom domain → ACM cert in us-east-1.
10. Payloads → Traffic Mirroring; CVEs → Inspector; PII → Macie; own HSM key → KMS EXTERNAL import.

## Next actions
1. Read `td_set_3_review.md` 🇻🇳 sections — group A and the 🔁 questions first.
2. Redo Pass 1 today/tomorrow: `/ai-tutor sap test-review 3 redo A, B` then C–F.
3. Keep spaced passes: TD1 Pass 3 + TD5 Pass 3 (~10-07), TD2 Pass 3 (~10-09).
4. Before TD Set 4: drill Continuous Improvement cost/ops patterns (group A) and edge/TLS (group D).
5. TD Set 4 timed ~10-15 – 10-16 (sprint gate 1: ≥66% keep the SAP-C02 date), see sprint plan in `aws-sap/study-progress.md`.
