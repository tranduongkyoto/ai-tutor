# AWS SAP-C02 Study Pipeline & Timeline

**Generated:** 2026-09-09 | **Updated:** 2026-09-14 (data-driven priority from 180 practice questions)
**Target:** Pass SAP-C02 with 80%+ on practice tests

## Data-Driven Analysis (180 Questions)

### Practice Test Domain Distribution (actual measured)

| Domain | Official Weight | Test 1 (30q) | Test 2 (75q) | Test 3 (75q) | Avg Actual |
|--------|----------------|-------------|-------------|-------------|------------|
| Design New Solutions | 29% | 43.3% (13q) | 38.7% (29q) | 40.0% (30q) | **40%** |
| Organizational Complexity | 26% | 23.3% (7q) | 33.3% (25q) | 33.3% (25q) | **32%** |
| Migration & Modernization | 20% | 10.0% (3q) | 17.3% (13q) | 12.0% (9q) | **14%** |
| Continuous Improvement | 25% | 16.7% (5q) | 5.3% (4q) | 5.3% (4q) | **7%** |

**Key insight:** "New Solutions" and "Org Complexity" dominate the actual questions (72% combined), far exceeding official weights. Continuous Improvement is underrepresented in Maarek's tests — supplement with other sources.

### Top 15 Services by Question Frequency

| Rank | Service | Questions | Priority |
|------|---------|-----------|----------|
| 1 | S3 | 78 | CRITICAL |
| 2 | EC2 | 66 | CRITICAL |
| 3 | VPC | 44 | CRITICAL |
| 4 | Lambda | 38 | HIGH |
| 5 | RDS | 38 | HIGH |
| 6 | NAT Gateway | 45 | HIGH |
| 7 | CloudWatch | 23 | HIGH |
| 8 | Kinesis | 21 | HIGH |
| 9 | Auto Scaling | 23 | HIGH |
| 10 | IAM/STS | 69 | CRITICAL |
| 11 | Direct Connect | 18 | HIGH |
| 12 | CloudFront | 17 | MEDIUM |
| 13 | DynamoDB | 14 | MEDIUM |
| 14 | Route 53 | 13 | MEDIUM |
| 15 | API Gateway | 13 | MEDIUM |

### Top Topics by Frequency

| Topic | Questions | Exam Impact |
|-------|-----------|-------------|
| DR/Failover/RPO/RTO | 61+ | CRITICAL — appears in ~34% of all questions |
| Cost optimization | 43 | HIGH — in ~24% of questions |
| On-premises/hybrid | 33 | HIGH — in ~18% |
| Migration | 17 | HIGH |
| Real-time/streaming | 15 | MEDIUM |
| Serverless | 13 | MEDIUM |
| Security groups/NACLs | 21 | MEDIUM |
| Multi-AZ | 11 | MEDIUM |

## Course Chapter Priority (Maarek v38 Slides — 18 chapters)

Based on measured question frequency, study chapters in this order:

| Priority | Chapter | Exam Impact | Est. Time |
|----------|---------|-------------|-----------|
| P1 | **Identity & Federation** | IAM/STS in 69 questions (38%) | 2h |
| P1 | **Security** | KMS/WAF/GuardDuty/encryption in 30+ questions | 2h |
| P1 | **Amazon VPC** | VPC endpoints, Direct Connect, NAT in 60+ questions | 2h |
| P1 | **Databases** | RDS/Aurora/DynamoDB/ElastiCache in 50+ questions | 1.5h |
| P1 | **Storage** | S3/EFS/FSx/Storage Gateway in 78+ questions | 1.5h |
| P2 | **Compute & Load Balancing** | EC2/ASG/ALB in 66+ questions | 1.5h |
| P2 | **Migrations** | DataSync/DMS/MGN/Snowball in 33+ questions | 1.5h |
| P2 | **Service Communication** | SQS/SNS/Kinesis/API Gateway in 40+ questions | 1h |
| P2 | **Cost Control** | RI/Spot/Savings Plans in 43 questions | 1h |
| P3 | **Monitoring** | CloudWatch/CloudTrail/X-Ray in 23+ questions | 1h |
| P3 | **Data Engineering** | Athena/Redshift/Glue/EMR in 20+ questions | 1h |
| P3 | **Caching** | ElastiCache/DAX/CloudFront in 17+ questions | 0.5h |
| P3 | **Deployment & Instance Management** | CodeDeploy/SSM/Beanstalk | 1h |
| P4 | **Machine Learning** | Low frequency in practice tests | 0.5h |
| P4 | **Other Services** | Niche services | 0.5h |
| — | **Exam Preparation** | Review/tips | 0.5h |

**Total course time (1.5-2x speed): ~18h**

## Resources Available

| Resource | Content |
|----------|---------|
| Maarek video course (Udemy) | 21h video + slides v38 (18 chapters) |
| Maarek Practice Exams (Udemy) | 3 tests: 30q + 75q + 75q = 180 questions |
| Maarek Hands-on Labs (Udemy) | 11 English labs (60-120m each) |
| Additional Udemy AWS Labs | 42 more labs (31 SAP-relevant) |
| Tutorials Dojo (recommended buy) | 300+ questions (~$15) |
| ExamCert (free) | 600+ free questions |
| AWS Skill Builder (free) | 20 official practice questions |

## Phase 1: Foundation (Week 1-2)

**Goal:** Cover P1+P2 chapters, take diagnostic test

### Knowledge — Priority Order (14-16h)
Read/watch in this exact order (highest exam impact first):

1. ~~Identity & Federation~~ (Done 2026-09-11)
2. **Security** — KMS, WAF, Shield, GuardDuty, Inspector, encryption patterns
3. **Amazon VPC** — VPC endpoints (gateway vs interface), Direct Connect, Transit Gateway, PrivateLink, NAT
4. **Storage** — S3 classes, lifecycle, cross-Region replication, EFS, FSx, Storage Gateway
5. **Databases** — RDS Multi-AZ, Aurora replicas, DynamoDB, ElastiCache, Redshift Spectrum
6. **Compute & Load Balancing** — ASG processes, ALB vs NLB, cross-zone LB, placement groups
7. **Migrations** — 6 Rs, DataSync, DMS, MGN, Snowball, hybrid architectures
8. **Service Communication** — SQS (DLQ, visibility timeout, message timers), SNS fanout, Kinesis enhanced fanout

### Practice Test (5h)
- Take Practice Test 1 (30q) cold — no prep, time yourself
- Score it, categorize every wrong answer by domain
- Read detailed explanations for ALL wrong answers
- Study relevant slides sections for weak topics only

### Labs (0-4h, only if score <60%)
- ~~Lab #176~~ — ASG + ALB Horizontal Scaling (Done 2026-09-11)
- ~~Lab #244~~ — Custom VPC with Public/Private Subnets (Done 2026-09-11)

## Phase 2: Deep Practice (Week 3-4)

**Goal:** Identify and fill domain-specific gaps + cover P3 chapters

### Knowledge (6-8h) — P3 chapters + targeted review
9. **Cost Control** — Reserved Instances, Savings Plans, Spot, Budgets actions, Cost Explorer
10. **Monitoring** — CloudWatch vs CloudTrail (key distinction!), VPC Flow Logs, Config rules
11. **Data Engineering** — Athena partitioning, Glue ETL, Redshift Spectrum, Kinesis Firehose
12. **Caching** — ElastiCache Redis vs Memcached, DAX, CloudFront behaviors
13. **Deployment & Instance Management** — CodeDeploy, SAM traffic shifting, SSM

### Practice Tests (8h)
- Take Practice Test 2 (75q) timed at 180min
- Categorize errors by domain, compare to Test 1 weak areas
- Take Practice Test 3 (75q) timed at 180min
- Track domain error progression

### Domain Error Tracker

| Domain (weight) | Test 1 | Test 2 | Test 3 | Status |
|-----------------|--------|--------|--------|--------|
| Organizational Complexity (26%) | 0/3* | _/_ | _/_ | *only 3q attempted |
| Design New Solutions (29%) | _/_ | _/_ | _/_ | |
| Continuous Improvement (25%) | _/_ | _/_ | _/_ | |
| Migration & Modernization (20%) | _/_ | _/_ | _/_ | |

### Labs (4-8h, pick based on 2 weakest domains)

**If weak on DR/HA (most likely — 34% of questions):**
- Lab #240 — EC2, RDS Multi-AZ, CloudWatch, SNS (Maarek)
- Lab #3486 — RPO/RTO Recovery with RDS (Maarek)
- Lab #3316 — Route53 Failover Routing

**If weak on Networking/VPC (second highest):**
- Lab #354 — Gateway VPC Endpoints
- Lab #276 — VPC Flow Logs + CloudWatch (Maarek)
- Lab #3238 — VPC Traffic Mirroring

**If weak on Serverless/Decoupling:**
- Lab #230 — Lambda + SQS + DynamoDB (Maarek)
- Lab #3318 — SNS + SQS Fanout

**If weak on Security/Monitoring:**
- Lab #3640 — Security Controls + KMS (Maarek)
- Lab #3452 — CloudTrail + CloudWatch Audit (Maarek)

**If weak on IaC/Migration:**
- Lab #3344 — CloudFormation StackSets (Maarek)
- Lab #3342 — Systems Manager Automation (Maarek)

## Phase 3: Volume Drilling (Week 5)

**Goal:** Expose to different question styles, build speed

### Practice Tests (16h)
- Get new question source (Tutorials Dojo 300q or ExamCert free 600q)
- Do 4 full-length exams (75q x 4 = 300q)
- Review WRONG answers only (time saver)
- Track score progression: A -> B -> C -> D
- Target: improving trend, 75%+ by Exam D
- **Note:** Maarek tests underrepresent Continuous Improvement (7% vs 25% official). Supplement with Tutorials Dojo for better coverage of cost/monitoring questions.

### Knowledge (0h)
- No new learning — only review explanations of wrong answers

### Labs (0h)
- No labs this week — pure exam drilling

## Phase 4: Final Prep (Week 6)

**Goal:** Verify readiness, close remaining gaps

### Day 1-2: Wrong Answer Marathon
- Compile ALL wrong answers from every test
- Re-do them as a custom "wrong answers only" set
- Study remaining pattern gaps

### Day 3-4: Redo Maarek Tests
- Retake Test 1 (30q) -> verify 85%+
- Retake Test 2 (75q) -> verify 80%+
- Retake Test 3 (75q) -> verify 80%+

### Day 5: Exam Day Simulation
- Take fresh 75q exam, strict 180min timer
- No breaks, no notes — simulate real conditions
- Score >= 80%? -> Schedule real exam
- Score < 75%? -> Repeat Phase 3 for 1 more week

### Day 6: Optional Confidence Labs
- Lab #326 — CloudWatch Dashboards (Maarek)
- Lab #336 — CloudFormation Provisioning (Maarek)

### Day 7: REST + schedule exam for next morning

## Time Budget Summary

| Phase | Knowledge | Practice Tests | Labs | Total |
|-------|-----------|---------------|------|-------|
| 1. Foundation (Wk 1-2) | 14-16h | 5h | 0-4h | 19-25h |
| 2. Deep Practice (Wk 3-4) | 6-8h | 8h | 4-8h | 18-24h |
| 3. Volume Drilling (Wk 5) | 0h | 16h | 0h | 16h |
| 4. Final Prep (Wk 6) | 4h | 8h | 0-4h | 12-16h |
| **Total** | **24-28h** | **37h** | **4-16h** | **65-81h** |

At 2h/day = 6 weeks. At 3h/day = 4 weeks.

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
| 1 | 176 | ASG + ALB Horizontal Scaling | Compute/HA | 60-120m | High — DONE |
| 2 | 240 | EC2, RDS Multi-AZ, CloudWatch, SNS | DR/HA | 90-120m | CRITICAL |
| 3 | 230 | Lambda + SQS + DynamoDB | Serverless | 60-120m | High |
| 4 | 276 | VPC Flow Logs + CloudWatch | Monitoring | 90-120m | High |
| 5 | 326 | CloudWatch Dashboards & Widgets | Monitoring | 90-120m | Medium |
| 6 | 336 | CloudFormation Provisioning | IaC | 60-90m | High |
| 7 | 3344 | CloudFormation StackSets | IaC/Migration | 60-120m | High |
| 8 | 3342 | Systems Manager Automation | Operations | 60-120m | Medium |
| 9 | 3452 | CloudTrail + CloudWatch Audit | Monitoring | 60-120m | High |
| 10 | 3486 | RPO/RTO Recovery with RDS | DR/Migration | 60-120m | CRITICAL |
| 11 | 3640 | Security Controls + KMS | Security | 60-120m | High |

## Current Progress (as of 2026-09-14)

| Activity | Status |
|----------|--------|
| Course chapter: Identity & Federation | Done |
| Lab #176 (ASG + ALB) | Done |
| Lab #244 (Custom VPC) | Done |
| Practice Test 1 | In Progress (Q3/30, 0/3) |
| Course chapters remaining | 17/18 |
| Labs remaining | 9/11 Maarek labs |
