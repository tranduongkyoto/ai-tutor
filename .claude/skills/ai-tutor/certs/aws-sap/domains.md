---
certification: aws-sap
exam_code: SAP-C02
total_domains: 4
pdf_base_path: sections/sap/
exam_questions: 75
exam_duration_minutes: 180
passing_score: 750
practice_test_path: practice-exam/sap/
practice_tests:
  - file: practice_test_1.md
    questions: 30
  - file: practice_test_2.md
    questions: 75
  - file: practice_test_3.md
    questions: 75
---

# AWS SAP (SAP-C02) - Domain Configuration

## Slides

slides:
  name: "AWS Certified Solutions Architect Professional Slides v38"
  pdf: "sections/sap/AWS Certified Solutions Architect Professional Slides v38.pdf"

## Domains

### organizational-complexity
- name: Design for Organizational Complexity
- weight: 26%
- topics: [multi-account-strategies, aws-organizations, service-control-policies, cross-account-access, iam-federation, resource-sharing (RAM), control-tower, identity-center, delegated-admin, tag-policies, backup-policies]
- key-services: [AWS Organizations, IAM Identity Center, AWS Control Tower, AWS RAM, SCPs, CloudFormation StackSets]

### new-solutions
- name: Design for New Solutions
- weight: 29%
- topics: [high-availability-architectures, dr-strategies (pilot-light, warm-standby, active-active), serverless-architectures, decoupled-architectures, data-store-selection, networking (vpc-endpoints, direct-connect, transit-gateway, privatelink), security (waf, shield, guardduty, inspector, kms), storage (s3-classes, efs, fsx, storage-gateway)]
- key-services: [Route53, CloudFront, ALB/NLB, API Gateway, Lambda, SQS, SNS, Kinesis, DynamoDB, Aurora, Redshift, S3, EFS, Direct Connect, Transit Gateway, VPC Endpoints]

### continuous-improvement
- name: Continuous Improvement for Existing Solutions
- weight: 25%
- topics: [cost-optimization (reserved-instances, savings-plans, spot, graviton), performance-tuning, monitoring-and-alerting, automation (systems-manager, cloudformation, config-rules), operational-excellence, caching-strategies (elasticache, cloudfront, dax)]
- key-services: [CloudWatch, CloudTrail, AWS Config, Systems Manager, Trusted Advisor, Cost Explorer, AWS Budgets, ElastiCache, DAX]

### migration-modernization
- name: Accelerate Workload Migration and Modernization
- weight: 20%
- topics: [migration-strategies (6-rs, rehost, replatform, refactor), data-migration (datasync, dms, snow-family, transfer-family), application-migration (mgn, sms), hybrid-architectures (storage-gateway, outposts), database-migration, network-migration (direct-connect, vpn)]
- key-services: [AWS DMS, AWS DataSync, AWS MGN, Storage Gateway, Snowball Edge, Direct Connect, AWS Transfer Family, Elastic Beanstalk]

## Labs (Maarek, by Domain)

### organizational-complexity labs
- Lab #3344 — CloudFormation StackSets (multi-Region deployment)
- Lab #3342 — Systems Manager Automation (large-scale environments)

### new-solutions labs
- Lab #176 — ASG + ALB Horizontal Scaling
- Lab #240 — EC2, RDS Multi-AZ, CloudWatch, SNS
- Lab #230 — Lambda + SQS + DynamoDB (decoupled backend)
- Lab #354 — Gateway VPC Endpoints
- Lab #3316 — Route53 Failover Routing
- Lab #3318 — SNS + SQS Fanout Architecture

### continuous-improvement labs
- Lab #276 — VPC Flow Logs + CloudWatch Monitoring
- Lab #3452 — CloudTrail + CloudWatch Audit
- Lab #326 — CloudWatch Dashboards & Widgets
- Lab #3640 — Security Controls + KMS Data Protection

### migration-modernization labs
- Lab #3486 — RPO/RTO Recovery with RDS (cross-region read replica)
- Lab #336 — CloudFormation Provisioning (automate infra)

## Study Pipeline (4 Phases, 6 Weeks)

### phase-1: Foundation (Week 1-2)
- Watch course at 1.5-2x, skip known CSA topics
- Take practice_test_1.md cold (30q)
- Study wrong answers + relevant slides
- Labs only if score <60%

### phase-2: Deep Practice (Week 3-4)
- Take practice_test_2.md timed (75q, 180min)
- Take practice_test_3.md timed (75q, 180min)
- Categorize errors by domain
- Do labs for 2 weakest domains
- Targeted study per weak domain

### phase-3: Volume Drilling (Week 5)
- Get new question source (Tutorials Dojo or ExamCert free)
- Do 4 full-length exams (75q each)
- Review wrong answers only
- Target: 75%+ by last exam

### phase-4: Final Prep (Week 6)
- Wrong answer marathon (all tests)
- Redo Maarek tests: verify 80%+
- Exam day simulation (75q, 180min, strict)
- Score >=80% -> schedule exam

## Exam Tactics

- Read last sentence first (question at bottom of 200-300 word scenarios)
- "Most operationally efficient" = managed service wins
- "Least development effort" = DMS over Glue, managed over custom
- Gateway endpoint = S3 + DynamoDB ONLY
- Cross-Region = Region-specific (KMS keys, ACM certs)
- "Near real-time" = Kinesis family
- 2.4 min/question max (75q / 180min)
