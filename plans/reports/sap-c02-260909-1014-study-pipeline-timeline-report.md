# AWS SAP-C02 Study Pipeline & Timeline

**Generated:** 2026-09-09 | **Target:** Pass SAP-C02 with 80%+ on practice tests

## Resources Available

| Resource | Content |
|----------|---------|
| Maarek video course (Udemy) | 21h video + slides v38 |
| Maarek Practice Exams (Udemy) | 3 tests: 30q + 75q + 75q = 180 questions |
| Maarek Hands-on Labs (Udemy) | 11 English labs (60-120m each) |
| Additional Udemy AWS Labs | 42 more labs (31 SAP-relevant) |
| Tutorials Dojo (recommended buy) | 300+ questions (~$15) |
| ExamCert (free) | 600+ free questions |
| AWS Skill Builder (free) | 20 official practice questions |

## Exam Domains & Weights

| Domain | Weight | Key Topics |
|--------|--------|------------|
| Design for Organizational Complexity | 26% | Organizations, SCPs, multi-account, cross-account access, IAM federation |
| Design for New Solutions | 29% | DR patterns, HA architectures, serverless, decoupling, data stores |
| Continuous Improvement | 25% | Cost optimization, monitoring, automation, performance tuning |
| Accelerate Workload Migration | 20% | Migration strategies (6 Rs), DataSync, DMS, MGN, hybrid networking |

## Phase 1: Foundation (Week 1-2)

**Goal:** Build SAP-level knowledge on top of CSA foundation

### Knowledge (10-14h)
- Watch Maarek course at 1.5-2x speed
- Skip sections already mastered from CSA
- DO NOT skip (even if familiar):
  - Organizations, SCPs, multi-account strategies
  - Direct Connect + VPN hybrid architectures
  - Migration strategies (6 Rs, DataSync, DMS, MGN)
  - DR patterns (Pilot Light, Warm Standby, Active-Active)
  - Cost optimization (RI, Savings Plans, cross-account billing)

### Practice Test (5h)
- Take Practice Test 1 (30q) cold — no prep, time yourself
- Score it, categorize every wrong answer by domain
- Read detailed explanations for ALL wrong answers
- Study relevant slides sections for weak topics only

### Labs (0-4h, only if score <60%)
- Lab #176 — ASG + ALB Horizontal Scaling
- Lab #244 — Custom VPC with Public/Private Subnets

## Phase 2: Deep Practice (Week 3-4)

**Goal:** Identify and fill domain-specific gaps

### Practice Tests (8h)
- Take Practice Test 2 (75q) timed at 180min
- Categorize errors by domain, compare to Test 1 weak areas
- Take Practice Test 3 (75q) timed at 180min
- Track domain error progression

### Domain Error Tracker

| Domain (weight) | Test 1 | Test 2 | Test 3 | Status |
|-----------------|--------|--------|--------|--------|
| Organizational Complexity (26%) | _/_ | _/_ | _/_ | |
| Design New Solutions (29%) | _/_ | _/_ | _/_ | |
| Continuous Improvement (25%) | _/_ | _/_ | _/_ | |
| Migration & Modernization (20%) | _/_ | _/_ | _/_ | |

### Knowledge (8-12h)
- Targeted study per weak domain using slides + AWS FAQs
- Read AWS whitepapers for weakest domain

### Labs (4-8h, pick based on 2 weakest domains)

**If weak on DR/HA:**
- Lab #240 — EC2, RDS Multi-AZ, CloudWatch, SNS (Maarek)
- Lab #3486 — RPO/RTO Recovery with RDS (Maarek)
- Lab #3316 — Route53 Failover Routing

**If weak on Networking:**
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
| 1. Foundation (Wk 1-2) | 10-14h | 5h | 0-4h | 15-23h |
| 2. Deep Practice (Wk 3-4) | 8-12h | 8h | 4-8h | 20-28h |
| 3. Volume Drilling (Wk 5) | 0h | 16h | 0h | 16h |
| 4. Final Prep (Wk 6) | 4h | 8h | 0-4h | 12-16h |
| **Total** | **22-30h** | **37h** | **4-16h** | **63-83h** |

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
| Flag & move at 2.5 min | 75q / 180min = 2.4 min/question max |
| Elimination first | Cross out 2 obviously wrong -> 50/50 the rest |

## Maarek Labs Reference (All 11)

| # | Lab ID | Title | Domain | Time | Priority |
|---|--------|-------|--------|------|----------|
| 1 | 176 | ASG + ALB Horizontal Scaling | Compute/HA | 60-120m | High |
| 2 | 240 | EC2, RDS Multi-AZ, CloudWatch, SNS | DR/HA | 90-120m | High |
| 3 | 230 | Lambda + SQS + DynamoDB | Serverless | 60-120m | High |
| 4 | 276 | VPC Flow Logs + CloudWatch | Monitoring | 90-120m | High |
| 5 | 326 | CloudWatch Dashboards & Widgets | Monitoring | 90-120m | Medium |
| 6 | 336 | CloudFormation Provisioning | IaC | 60-90m | High |
| 7 | 3344 | CloudFormation StackSets | IaC/Migration | 60-120m | High |
| 8 | 3342 | Systems Manager Automation | Operations | 60-120m | Medium |
| 9 | 3452 | CloudTrail + CloudWatch Audit | Monitoring | 60-120m | High |
| 10 | 3486 | RPO/RTO Recovery with RDS | DR/Migration | 60-120m | High |
| 11 | 3640 | Security Controls + KMS | Security | 60-120m | High |
