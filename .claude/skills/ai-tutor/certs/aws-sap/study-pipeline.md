# AWS SAP-C02 Study Pipeline & Timeline

**Generated:** 2026-09-09 | **Updated:** 2026-09-18 (combined analysis: Udemy 180q + Tutorials Dojo 391q = 571 questions)
**Target:** Pass SAP-C02 with 80%+ on practice tests

## Data-Driven Analysis (571 Questions: Udemy 180 + TD 391)

### Practice Test Sources

| Source | Tests | Questions | Difficulty | Strengths |
|--------|-------|-----------|------------|-----------|
| Udemy Maarek | 3 (30+75+75) | 180 | 6/10 | Deep S3/VPC/DX, good explanations |
| Tutorials Dojo | 6 (75x5+16) | 391 | 8/10 | Broader services, realistic scenarios, domain tags |
| **Combined** | **9** | **571** | | **Best coverage for exam prep** |

### Service Frequency (Combined 571q)

| Rank | Service | Udemy | TD | Combined | Priority |
|------|---------|-------|-----|----------|----------|
| 1 | S3 | 1201 | 2181 | 3382 | CRITICAL |
| 2 | EC2 | 495 | 1963 | 2458 | CRITICAL |
| 3 | IAM/STS | 156 | 1048 | 1204 | CRITICAL |
| 4 | VPC | 839 | 1033 | 1872 | CRITICAL |
| 5 | Lambda | 367 | 984 | 1351 | CRITICAL |
| 6 | RDS/Aurora | 278 | 1083 | 1361 | CRITICAL |
| 7 | DynamoDB | 152 | 483 | 635 | HIGH |
| 8 | CloudFront | 191 | 788 | 979 | HIGH |
| 9 | **Systems Manager** | 43 | **326** | 369 | **HIGH (was P3)** |
| 10 | CloudWatch | 182 | 316 | 498 | HIGH |
| 11 | **AWS Config** | ~20 | **250** | 270 | **HIGH (was unranked)** |
| 12 | SQS | 142 | 296 | 438 | HIGH |
| 13 | Organizations/SCP | 110 | 428 | 538 | CRITICAL |
| 14 | Direct Connect | 170 | 258 | 428 | HIGH |
| 15 | **ECS/EKS/Fargate** | 65 | **446** | 511 | **HIGH (was P3)** |
| 16 | CloudFormation | 82 | 362 | 444 | HIGH |
| 17 | **Reserved/Savings** | 2 | **158** | 160 | **HIGH (was missing)** |
| 18 | Kinesis | 248 | 138 | 386 | HIGH |
| 19 | KMS | 118 | 166 | 284 | HIGH |
| 20 | **Cognito** | ~5 | **88** | 93 | **MEDIUM (was unranked)** |

### Biggest Udemy Blind Spots (filled by TD)

| Service | Udemy | TD | Gap Factor | Action |
|---------|-------|-----|-----------|--------|
| Reserved/Savings Plans | 2 | 158 | 79x | Study cost optimization chapter |
| AWS Config | ~20 | 250 | 12x | Add to monitoring chapter |
| Cognito | ~5 | 88 | 18x | Add to identity chapter |
| Systems Manager | 43 | 326 | 7.6x | Expand deployment chapter |
| ECS/EKS/Fargate | 65 | 446 | 6.9x | Expand compute chapter |
| Step Functions | ~10 | 69 | 6.9x | Add to service-communication |
| Service Catalog | 0 | 49 | new | Add to identity chapter |
| Control Tower | 0 | 31 | new | Add to identity chapter |

## Course Chapter Priority (Revised with Combined Udemy+TD Data)

Based on combined 571-question frequency analysis. Priorities updated from Udemy-only analysis.

| Priority | Chapter | Combined Evidence | Change | Status |
|----------|---------|-------------------|--------|--------|
| P1 | **Identity & Federation** | IAM 1204 + Orgs 538 + Cognito 93 + Control Tower 31 | same | DONE (53%) |
| P1 | **Security** | KMS 284 + WAF 233 + Macie 44 | same | DONE (77%) |
| P1 | **Amazon VPC** | VPC 1872 + DX 428 + TGW 122 | same | DONE (77%) |
| P1 | **Storage** | S3 3382 + EFS 311 + FSx 199 + Glacier 214 | same | DONE (63%) |
| P1 | **Databases** | RDS 1361 + DynamoDB 635 + Redshift 392 | same | DONE (73%) |
| **P1** | **Compute & Load Balancing** | EC2 2458 + ECS/EKS/Fargate 511 + Lambda 1351 | **P2→P1** | NOT STARTED |
| **P2** | **Monitoring + Config + SSM** | CW 498 + Config 270 + SSM 369 | **P3→P2** | NOT STARTED |
| P2 | **Service Communication** | SQS 438 + SNS 261 + Step Functions 69 | same | NOT STARTED |
| **P2** | **Cost Control** | Reserved/Savings 160 + cost mentions 200+ | **scope expanded** | NOT STARTED |
| P2 | **Migrations** | DMS + DataSync + MGN + Snow | same | NOT STARTED |
| **P2** | **Deployment & Instance Mgmt** | CloudFormation 444 + CodePipeline 70 | **P3→P2** | NOT STARTED |
| P3 | **Caching** | ElastiCache 123 + CloudFront 979 | same | NOT STARTED |
| P3 | **Data Engineering** | Athena 119 + Glue + EMR | same | NOT STARTED |

**Total course time (1.5-2x speed): ~18h**

## Resources Available

| Resource | Content | Status |
|----------|---------|--------|
| Maarek video course (Udemy) | 21h video + slides v38 (18 chapters) | In use |
| Maarek Practice Exams (Udemy) | 3 tests: 30q + 75q + 75q = 180 questions | Chapter drills done (5/13 chapters) |
| Maarek Hands-on Labs (Udemy) | 11 English labs (60-120m each) | 5/11 done |
| Additional Udemy AWS Labs | 42 more labs (31 SAP-relevant) | Selective |
| **Tutorials Dojo** | **6 sets: 75q x5 + 16q = 391 questions** | **NEW — chapter-drill ready** |
| ExamCert (free) | 600+ free questions | Not started |
| AWS Skill Builder (free) | 20 official practice questions | Not started |

## Phase 1: Foundation — DONE (Week 1-3)

**Goal:** Cover P1 chapters via Udemy chapter drills

### Knowledge + Udemy Chapter Drills (completed)
1. ~~Identity & Federation~~ (Done 2026-09-15, drill 8/15 = 53%)
2. ~~Security~~ (Done 2026-09-15, drill 10/13 = 77%)
3. ~~Amazon VPC~~ (Done 2026-09-16, drill 23/30 = 77%)
4. ~~Storage~~ (Done 2026-09-17, drill 25/40 = 63%)
5. ~~Databases~~ (Done 2026-09-18, drill 19/26 = 73%)

**Result:** 5 critical chapters done, 85/124 correct (69%), 39 wrong answers tracked.

### Labs Done
- ~~Lab #176~~ — ASG + ALB (Done)
- ~~Lab #244~~ — Custom VPC (Done)
- ~~Lab #2934~~ — ASG Lifecycle Hooks (Done)
- ~~Lab #3640~~ — Security + KMS (Done)
- ~~Lab #2856~~ — SG vs NACL (Done)

## Phase 2: TD Chapter Drills (Current — Week 4-5)

**Goal:** Drill all chapters with TD questions (broader coverage, harder questions)

### TD Chapter Drills — Priority Order
Use `/ai-tutor sap chapter-drill <chapter> dojo` for each:

| Order | Chapter | TD Questions | Focus (TD fills Udemy gaps) |
|-------|---------|-------------|---------------------------|
| 1 | **compute-load-balancing** | 98 | ECS/EKS/Fargate (511 mentions), Lambda patterns |
| 2 | **databases** | 74 | Aurora Global, DynamoDB patterns, Redshift |
| 3 | **monitoring** | 33 | **SSM (326), Config (250)** — biggest Udemy gaps |
| 4 | **storage** | 94 | Broader S3/EFS scenarios |
| 5 | **service-communication** | 24 | Step Functions, EventBridge patterns |
| 6 | **identity-federation** | 45 | Cognito, Control Tower, Service Catalog |
| 7 | **vpc** | 52 | Transit Gateway, more DX patterns |
| 8 | **deployment-instance-mgmt** | 10 | CloudFormation StackSets, CodePipeline |
| 9 | **cost-control** | 5 | **Reserved/Savings Plans** — critical gap |
| 10 | **migrations** | 16 | DMS, MGN, hybrid patterns |
| 11 | **security** | 24 | Macie, Inspector v2 |
| 12 | **caching** | 11 | ElastiCache patterns |
| 13 | **data-engineering** | 3 | Athena/Glue |

### Redo Udemy Wrong Answers (39 wrong)
After TD drills, redo wrong answers from Phase 1:
- identity-federation: 7 wrong (53% → target 80%)
- storage: 15 wrong
- vpc: 8 wrong
- databases: 7 wrong
- security: 3 wrong

### Labs (pick based on weak areas)
- Lab #240 — RDS Multi-AZ + CloudWatch + SNS (Maarek)
- Lab #230 — Lambda + SQS + DynamoDB (Maarek)
- Lab #3452 — CloudTrail + CloudWatch Audit (Maarek)
- Lab #3344 — CloudFormation StackSets (Maarek)

## Phase 3: Timed Mock Exams (Week 6)

**Goal:** Build exam speed, simulate real conditions

### TD Full Tests (timed, 180min each)
| Order | Test | Questions | Why This Order |
|-------|------|-----------|----------------|
| 1 | TD Set 5 | 75q | Best domain balance (24% Org, 24% Migration) |
| 2 | TD Set 1 | 75q | Second most balanced |
| 3 | TD Set 2 | 75q | Higher multi-choice (24%) |
| 4 | Udemy Test 2 | 75q | Timed retake |
| 5 | Udemy Test 3 | 75q | Timed retake |

Target: 75%+ by test 3, 80%+ by test 5.

### Knowledge (0h)
- No new learning — only review wrong answer explanations

## Phase 4: Final Prep (Week 7)

**Goal:** Close all gaps, verify readiness

### Day 1-2: Wrong Answer Marathon
- Compile ALL wrong from Udemy + TD (est. ~150 wrong)
- Re-quiz as custom set
- Study weak pattern notes

### Day 3-4: Final Mock Exams
- TD Set 3 (75q) timed — target 80%+
- TD Set 4 (75q) timed — target 80%+
- TD Set 6 (16q) bonus

### Day 5: Exam Simulation
- Fresh 75q, strict 180min, no breaks
- Score >= 80% → schedule real exam
- Score < 75% → repeat Phase 3 for 1 more week

### Day 6-7: REST + schedule exam

## Time Budget Summary (Revised)

| Phase | Knowledge | Practice Drills | Labs | Total |
|-------|-----------|----------------|------|-------|
| 1. Foundation — DONE | 14h | 5h (Udemy 124q) | 5 labs | 24h |
| 2. TD Chapter Drills (current) | 0h | 12h (TD 489q) | 4 labs | 16h |
| 3. Timed Mocks | 0h | 10h (5x 75q) | 0h | 10h |
| 4. Final Prep | 4h | 8h (wrong redo + final) | 0h | 12h |
| **Total** | **18h** | **35h** | **~9 labs** | **62h** |

At 2h/day = 4.5 weeks remaining. At 3h/day = 3 weeks remaining.

## Exam Day Tactics

| Tactic | Rule |
|--------|------|
| Read last sentence first | Question is always at bottom of 200-300 word scenarios |
| "Most operationally efficient" | Managed service wins, eliminate manual/Lambda-heavy |
| "Least development effort" | DMS over Glue, managed over custom |
| Gateway endpoint | S3 + DynamoDB ONLY; everything else = Interface endpoint |
| Cross-Region anything | Region-specific (KMS keys, ACM certs, Redshift snapshots) |
| "Near real-time" | Kinesis family, not Lambda cron |
| CloudWatch vs CloudTrail | CW = metrics/logs/alarms; CT = API audit trail ONLY |
| FSx failover test | Modify throughput capacity, NEVER touch ENIs |
| Flag & move at 2.5 min | 75q / 180min = 2.4 min/question max |
| Elimination first | Cross out 2 obviously wrong -> 50/50 the rest |

## Maarek Labs Reference (All 11)

| # | Lab ID | Title | Domain | Time | Priority |
|---|--------|-------|--------|------|----------|
| 1 | 176 | ASG + ALB Horizontal Scaling | Compute/HA | 60-120m | DONE |
| 2 | 240 | EC2, RDS Multi-AZ, CloudWatch, SNS | DR/HA | 90-120m | CRITICAL |
| 3 | 230 | Lambda + SQS + DynamoDB | Serverless | 60-120m | High |
| 4 | 276 | VPC Flow Logs + CloudWatch | Monitoring | 90-120m | High |
| 5 | 326 | CloudWatch Dashboards & Widgets | Monitoring | 90-120m | Medium |
| 6 | 336 | CloudFormation Provisioning | IaC | 60-90m | High |
| 7 | 3344 | CloudFormation StackSets | IaC/Migration | 60-120m | High |
| 8 | 3342 | Systems Manager Automation | Operations | 60-120m | Medium |
| 9 | 3452 | CloudTrail + CloudWatch Audit | Monitoring | 60-120m | High |
| 10 | 3486 | RPO/RTO Recovery with RDS | DR/Migration | 60-120m | CRITICAL |
| 11 | 3640 | Security Controls + KMS | Security | 60-120m | DONE |

## Current Progress (as of 2026-09-18)

| Activity | Status |
|----------|--------|
| **Phase 1 — Udemy Chapter Drills** | **DONE** |
| Udemy: Identity & Federation | Done — drill 8/15 (53%) |
| Udemy: Security | Done — drill 10/13 (77%) |
| Udemy: VPC | Done — drill 23/30 (77%) |
| Udemy: Storage | Done — drill 25/40 (63%) |
| Udemy: Databases | Done — drill 19/26 (73%) |
| Udemy questions answered | 124 (39 wrong) |
| **Phase 2 — TD Chapter Drills** | **CURRENT** |
| TD questions available | 391 (mapped to 13 chapters) |
| TD questions answered | 0 |
| **Labs** | 5/11 Maarek labs done |
| Lab #176 (ASG + ALB) | Done |
| Lab #244 (Custom VPC) | Done |
| Lab #2934 (ASG Lifecycle Hooks) | Done |
| Lab #3640 (Security + KMS) | Done |
| Lab #2856 (SG vs NACL) | Done |
| **Overall accuracy** | 85/124 (69%) — trending up |
| **Estimated time to exam** | 3-4.5 weeks |
