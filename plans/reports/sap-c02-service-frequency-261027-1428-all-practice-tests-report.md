# SAP-C02 — Service Frequency & Priority Across All Practice Tests

**Date:** 2026-10-27 · **Corpus:** 886 questions — Udemy 180 (PT1–3) · Tutorials Dojo 391 (Sets 1–6) · Neal Davis 185 (210 minus 25 excluded) · AWS Free 130 (Free Exam 1+2)
**Your misses:** 266 wrong-answer notes from every `*review_notes.json` (TD1/2/3/5 + retakes, TD4, TD6, Udemy unseen, Neal A/B)

## Method
- **Qs** = number of questions whose stem or options mention the service (counted once per question). Regex dictionary of 147 services/features.
- **In correct ans** = number of times the service appears in the correct option(s).
- **Answer-ratio** = in-correct / Qs. A high ratio means the service is usually the answer. A low ratio means it is usually a distractor.
- **Your misses** = your miss notes (keywords/trap/rule) that mention the service.
- **Score** = 45% frequency + 30% correct-answer count + 10% source breadth (4 sources) + 15% your misses, each normalized to the max.
- **Tier** (by Qs): S ≥90 (≥10% of exam) · A 40–89 · B 15–39 · C 5–14 · D <5.

## Key findings
1. **The big 12 cover most of the exam.** S3, EC2, Lambda, VPC, ELB, Auto Scaling, IAM, RDS, CloudFront, DynamoDB, Organizations/SCP and Route 53 each appear in ≥10% of questions. S3 is the #1 service that shows up in correct answers (212).
2. **"Usually the answer" (≥60% answer-ratio):** WAF 77%, IAM 67%, STS/federation 66%, PrivateLink/VPC endpoints 63%, S3 60%, CloudFront 60%, Aurora 60%. Smaller ones: CodeBuild 83%, RDS Proxy 90%, RAM 67%, ACM 73%, Cognito 67%, Lambda@Edge 61%, Compute Optimizer 71%, SCT 67%.
3. **"Usually the distractor" (≤30%):** EBS 18%, VPC Peering 19%, AWS Config 25%, Trusted Advisor 12%, EMR 17%, SES 13%, SMS (legacy) 0%, Outposts 0%. When these appear, check carefully before picking them.
4. **Your weak spots (high misses relative to frequency):** Fargate 15/36, ElastiCache 11/36, STS/federation 11/32, CloudFront 31/116, PrivateLink 15/54, Spot 10/39, Redshift 10/40, Cognito 6/12, ACM 6/11, CloudHSM 4/6, Gateway LB 4/7, Route 53 Resolver 3/7, Snow Family 6/16, Shield 5/13.
5. **Source bias:** Udemy leans on Kinesis/Firehose, Snow, VPC Flow Logs, and S3 Transfer Acceleration. TD leans on EC2/Spot, EBS, SSM patching, Config, and EKS. Neal leans on CodeBuild/CodeDeploy/CodePipeline, ECS, and OpsWorks. AWS Free (closest to the real exam style) leans on Organizations/SCP, PrivateLink, NAT, Transit Gateway, RAM, AWS Backup, and Migration Hub/Discovery.
6. **Zero hits** (skip): VPC Lattice, QLDB, SWF, Verified Access, Cloud9, Bedrock.

## Study priority
| Priority | Services | Action |
|---|---|---|
| P0 — master + weak | CloudFront, PrivateLink/endpoints, STS/federation, Fargate, ElastiCache, Spot, Redshift, Organizations/SCP | Redo misses, then flashcards |
| P1 — master | S3, EC2, Lambda, VPC, ELB, ASG, IAM, RDS, DynamoDB, Route 53, Aurora, CloudWatch, SSM, CloudFormation/StackSets, SQS, API Gateway, Direct Connect | Know features plus trade-offs |
| P2 — solid | SNS, ECS, VPN, EFS, EventBridge, Config, CloudTrail, EBS, WAF, KMS, Kinesis KDS/Firehose, Athena, Glacier, NAT, S3 CRR, Storage Gateway, Savings Plans/RI, Transit Gateway, Cost Explorer/CUR, DMS, MGN, DataSync, Global Accelerator | Know when to pick each, plus the main limits |
| P3 — recognize | Tier C rows below | One-line purpose + keyword trigger |
| P4 — skim | Tier D rows | Name to purpose only |

## Full ranked list (147 services, 141 with hits)
| # | Service | Cat | Tier | Score | Qs | % of 886 | In correct ans | Answer-ratio | Udemy | TD | Neal | AWS-Free | Your misses |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | S3 | Storage | S | 93.0 | 356 | 40.2 | 212 | 60% | 78 | 175 | 55 | 48 | 62 |
| 2 | EC2 | Compute | S | 88.6 | 422 | 47.6 | 162 | 38% | 66 | 215 | 84 | 57 | 44 |
| 3 | Lambda | Compute | S | 62.6 | 247 | 27.9 | 124 | 50% | 36 | 98 | 68 | 45 | 36 |
| 4 | VPC (core: subnets, SG, NACL, route tables) | Networking | S | 54.5 | 200 | 22.6 | 107 | 54% | 42 | 95 | 36 | 27 | 33 |
| 5 | ELB (ALB/NLB/GWLB) | Networking | S | 52.1 | 191 | 21.6 | 90 | 47% | 29 | 97 | 38 | 27 | 37 |
| 6 | EC2 Auto Scaling | Compute | S | 47.2 | 181 | 20.4 | 84 | 46% | 24 | 96 | 37 | 24 | 25 |
| 7 | IAM (roles, policies, users) | Security | S | 44.8 | 139 | 15.7 | 93 | 67% | 18 | 73 | 25 | 23 | 28 |
| 8 | RDS | Database | S | 41.3 | 163 | 18.4 | 64 | 39% | 22 | 86 | 32 | 23 | 20 |
| 9 | CloudFront | Networking | S | 39.8 | 116 | 13.1 | 70 | 60% | 17 | 61 | 25 | 13 | 31 |
| 10 | DynamoDB | Database | S | 33.6 | 108 | 12.2 | 56 | 52% | 14 | 60 | 26 | 8 | 17 |
| 11 | Organizations + SCPs | Security | S | 31.3 | 93 | 10.5 | 48 | 52% | 10 | 43 | 18 | 22 | 19 |
| 12 | Route 53 | Networking | S | 31.1 | 97 | 10.9 | 49 | 51% | 14 | 46 | 23 | 14 | 16 |
| 13 | Aurora | Database | A | 29.0 | 75 | 8.5 | 45 | 60% | 10 | 33 | 19 | 13 | 19 |
| 14 | CloudWatch (metrics/alarms/logs) | Management | S | 28.9 | 98 | 11.1 | 39 | 40% | 23 | 39 | 19 | 17 | 12 |
| 15 | Systems Manager (SSM) | Management | A | 27.8 | 79 | 8.9 | 32 | 41% | 7 | 49 | 9 | 14 | 20 |
| 16 | CloudFormation / StackSets | Management | A | 26.4 | 74 | 8.4 | 38 | 51% | 7 | 37 | 17 | 13 | 13 |
| 17 | SQS | Integration | A | 25.9 | 66 | 7.4 | 37 | 56% | 12 | 33 | 15 | 6 | 15 |
| 18 | API Gateway | Integration | A | 25.2 | 73 | 8.2 | 30 | 41% | 13 | 25 | 21 | 14 | 13 |
| 19 | Direct Connect | Networking | A | 25.1 | 74 | 8.4 | 29 | 39% | 18 | 35 | 14 | 7 | 13 |
| 20 | PrivateLink / VPC endpoints | Networking | A | 24.2 | 54 | 6.1 | 34 | 63% | 14 | 14 | 10 | 16 | 15 |
| 21 | SNS | Integration | A | 22.9 | 61 | 6.9 | 33 | 54% | 12 | 29 | 9 | 11 | 7 |
| 22 | ECS | Compute | A | 21.6 | 59 | 6.7 | 24 | 41% | 7 | 23 | 19 | 10 | 8 |
| 23 | Site-to-Site / Client VPN | Networking | A | 21.1 | 54 | 6.1 | 19 | 35% | 9 | 24 | 13 | 8 | 11 |
| 24 | EFS | Storage | A | 20.8 | 58 | 6.5 | 19 | 33% | 11 | 24 | 13 | 10 | 8 |
| 25 | EventBridge / CloudWatch Events | Integration | A | 20.8 | 58 | 6.5 | 24 | 41% | 9 | 22 | 17 | 10 | 5 |
| 26 | Fargate | Compute | B | 19.6 | 36 | 4.1 | 15 | 42% | 3 | 20 | 8 | 5 | 15 |
| 27 | Redshift | Database | A | 19.2 | 40 | 4.5 | 18 | 45% | 11 | 18 | 7 | 4 | 10 |
| 28 | AWS Config | Management | A | 19.1 | 52 | 5.9 | 13 | 25% | 7 | 32 | 5 | 8 | 7 |
| 29 | STS / AssumeRole / federation | Security | B | 19.0 | 32 | 3.6 | 21 | 66% | 4 | 20 | 4 | 4 | 11 |
| 30 | CloudTrail | Management | A | 18.8 | 40 | 4.5 | 20 | 50% | 13 | 17 | 6 | 4 | 7 |
| 31 | EBS | Storage | A | 18.7 | 57 | 6.4 | 10 | 18% | 8 | 37 | 7 | 5 | 5 |
| 32 | EC2 Spot Instances | Compute | B | 18.6 | 39 | 4.4 | 14 | 36% | 2 | 25 | 7 | 5 | 10 |
| 33 | WAF | Security | B | 18.6 | 31 | 3.5 | 24 | 77% | 8 | 11 | 9 | 3 | 8 |
| 34 | ElastiCache | Database | B | 18.3 | 36 | 4.1 | 13 | 36% | 4 | 20 | 8 | 4 | 11 |
| 35 | KMS | Security | B | 18.0 | 37 | 4.2 | 17 | 46% | 12 | 15 | 7 | 3 | 7 |
| 36 | Kinesis Data Streams | Analytics | A | 17.9 | 41 | 4.6 | 20 | 49% | 19 | 7 | 9 | 6 | 3 |
| 37 | Athena | Analytics | A | 17.9 | 40 | 4.5 | 17 | 42% | 12 | 11 | 10 | 7 | 5 |
| 38 | S3 Glacier | Storage | B | 17.4 | 32 | 3.6 | 18 | 56% | 10 | 17 | 2 | 3 | 6 |
| 39 | NAT Gateway | Networking | B | 17.2 | 38 | 4.3 | 17 | 45% | 8 | 12 | 7 | 11 | 3 |
| 40 | S3 Replication (CRR/SRR) | Storage | B | 16.9 | 35 | 4.0 | 14 | 40% | 6 | 17 | 7 | 5 | 5 |
| 41 | Storage Gateway | Storage | B | 16.9 | 33 | 3.7 | 12 | 36% | 9 | 15 | 4 | 5 | 7 |
| 42 | Savings Plans / Reserved Instances | Management | B | 16.9 | 28 | 3.2 | 14 | 50% | 2 | 13 | 8 | 5 | 8 |
| 43 | Transit Gateway | Networking | B | 16.7 | 30 | 3.4 | 13 | 43% | 3 | 12 | 6 | 9 | 7 |
| 44 | Cost Explorer / CUR / Budgets | Management | B | 16.6 | 27 | 3.0 | 16 | 59% | 3 | 8 | 9 | 7 | 6 |
| 45 | DMS | Migration | B | 16.3 | 30 | 3.4 | 15 | 50% | 5 | 10 | 7 | 8 | 4 |
| 46 | Elastic Beanstalk | Compute | B | 16.1 | 34 | 3.8 | 11 | 32% | 7 | 18 | 4 | 5 | 4 |
| 47 | Kinesis Data Firehose | Analytics | B | 15.9 | 24 | 2.7 | 15 | 62% | 12 | 4 | 4 | 4 | 5 |
| 48 | CodeDeploy | DevTools | B | 15.3 | 28 | 3.2 | 13 | 46% | 4 | 10 | 11 | 3 | 2 |
| 49 | FSx (Windows/Lustre/ONTAP/OpenZFS) | Storage | B | 15.0 | 20 | 2.3 | 12 | 60% | 3 | 7 | 5 | 5 | 5 |
| 50 | Global Accelerator | Networking | B | 14.8 | 27 | 3.0 | 7 | 26% | 9 | 9 | 2 | 7 | 4 |
| 51 | Lambda@Edge / CloudFront Functions | Networking | B | 14.7 | 18 | 2.0 | 11 | 61% | 2 | 10 | 3 | 3 | 5 |
| 52 | S3 Transfer Acceleration | Storage | B | 14.3 | 22 | 2.5 | 9 | 41% | 9 | 5 | 5 | 3 | 3 |
| 53 | Application Migration Service (MGN) | Migration | B | 14.2 | 24 | 2.7 | 8 | 33% | 2 | 14 | 2 | 6 | 2 |
| 54 | DataSync | Migration | B | 14.2 | 22 | 2.5 | 10 | 45% | 7 | 9 | 3 | 3 | 2 |
| 55 | OpenSearch | Database | B | 14.1 | 18 | 2.0 | 10 | 56% | 2 | 11 | 2 | 3 | 3 |
| 56 | CodePipeline | DevTools | B | 14.1 | 20 | 2.3 | 12 | 60% | 1 | 10 | 8 | 1 | 1 |
| 57 | Step Functions | Integration | B | 14.0 | 17 | 1.9 | 7 | 41% | 1 | 9 | 2 | 5 | 5 |
| 58 | QuickSight | Analytics | B | 14.0 | 21 | 2.4 | 9 | 43% | 4 | 8 | 5 | 4 | 2 |
| 59 | EMR | Analytics | B | 13.9 | 24 | 2.7 | 4 | 17% | 3 | 13 | 6 | 2 | 3 |
| 60 | VPC Peering | Networking | B | 13.8 | 27 | 3.0 | 5 | 19% | 7 | 12 | 3 | 5 | 1 |
| 61 | DynamoDB Global Tables | Database | B | 13.8 | 21 | 2.4 | 11 | 52% | 2 | 6 | 8 | 5 | 0 |
| 62 | Secrets Manager | Security | B | 13.8 | 15 | 1.7 | 9 | 60% | 2 | 6 | 6 | 1 | 4 |
| 63 | Glue | Analytics | B | 13.6 | 18 | 2.0 | 7 | 39% | 3 | 8 | 4 | 3 | 3 |
| 64 | Service Catalog | Management | B | 13.6 | 15 | 1.7 | 7 | 47% | 1 | 8 | 3 | 3 | 4 |
| 65 | Inspector | Security | B | 13.5 | 18 | 2.0 | 6 | 33% | 4 | 11 | 2 | 1 | 3 |
| 66 | Directory Service (Managed AD / AD Connector) | Security | B | 13.4 | 16 | 1.8 | 7 | 44% | 1 | 9 | 5 | 1 | 3 |
| 67 | IAM Identity Center (SSO) | Security | C | 13.3 | 13 | 1.5 | 7 | 54% | 1 | 8 | 2 | 2 | 4 |
| 68 | Application Discovery Service | Migration | B | 13.0 | 15 | 1.7 | 8 | 53% | 1 | 4 | 4 | 6 | 1 |
| 69 | Control Tower | Security | B | 13.0 | 17 | 1.9 | 5 | 29% | 2 | 7 | 2 | 6 | 2 |
| 70 | Aurora Global Database | Database | C | 12.9 | 13 | 1.5 | 7 | 54% | 2 | 5 | 4 | 2 | 2 |
| 71 | Schema Conversion Tool | Migration | C | 12.9 | 12 | 1.4 | 8 | 67% | 1 | 7 | 1 | 3 | 2 |
| 72 | Trusted Advisor | Management | B | 12.6 | 17 | 1.9 | 2 | 12% | 1 | 8 | 4 | 4 | 2 |
| 73 | X-Ray | Management | C | 12.4 | 10 | 1.1 | 6 | 60% | 3 | 4 | 2 | 1 | 2 |
| 74 | CodeBuild | DevTools | B | 12.0 | 18 | 2.0 | 15 | 83% | 0 | 7 | 9 | 2 | 2 |
| 75 | Snow Family | Migration | B | 11.8 | 16 | 1.8 | 8 | 50% | 7 | 0 | 6 | 3 | 6 |
| 76 | AppSync | Integration | C | 11.8 | 11 | 1.2 | 3 | 27% | 1 | 6 | 3 | 1 | 1 |
| 77 | DAX | Database | C | 11.7 | 8 | 0.9 | 4 | 50% | 3 | 1 | 3 | 1 | 1 |
| 78 | Migration Hub | Migration | C | 11.7 | 9 | 1.0 | 5 | 56% | 2 | 1 | 1 | 5 | 0 |
| 79 | Amazon MQ | Integration | C | 11.7 | 11 | 1.2 | 2 | 18% | 1 | 4 | 3 | 3 | 1 |
| 80 | Resource Access Manager (RAM) | Security | B | 11.7 | 15 | 1.7 | 10 | 67% | 0 | 7 | 2 | 6 | 5 |
| 81 | Neptune | Database | C | 11.6 | 9 | 1.0 | 3 | 33% | 3 | 3 | 1 | 2 | 1 |
| 82 | VPC Reachability / Traffic Mirroring | Networking | C | 11.4 | 6 | 0.7 | 2 | 33% | 1 | 3 | 1 | 1 | 2 |
| 83 | ACM (certificates) | Security | C | 11.3 | 11 | 1.2 | 8 | 73% | 3 | 7 | 1 | 0 | 6 |
| 84 | Permission Boundaries | Security | C | 11.1 | 8 | 0.9 | 2 | 25% | 2 | 1 | 4 | 1 | 0 |
| 85 | Shield | Security | C | 10.8 | 13 | 1.5 | 5 | 38% | 2 | 10 | 1 | 0 | 5 |
| 86 | Firewall Manager | Security | C | 10.8 | 6 | 0.7 | 1 | 17% | 1 | 2 | 1 | 2 | 0 |
| 87 | EKS | Compute | B | 10.7 | 21 | 2.4 | 5 | 24% | 0 | 14 | 1 | 6 | 1 |
| 88 | RDS Proxy | Database | C | 10.6 | 10 | 1.1 | 9 | 90% | 0 | 5 | 1 | 4 | 3 |
| 89 | VPC Flow Logs | Networking | C | 10.0 | 14 | 1.6 | 4 | 29% | 10 | 3 | 0 | 1 | 2 |
| 90 | ECR | Compute | C | 9.8 | 9 | 1.0 | 6 | 67% | 0 | 5 | 2 | 2 | 2 |
| 91 | GuardDuty | Security | C | 9.8 | 12 | 1.4 | 2 | 17% | 2 | 9 | 0 | 1 | 3 |
| 92 | Gateway Load Balancer | Networking | C | 9.6 | 7 | 0.8 | 3 | 43% | 2 | 4 | 1 | 0 | 4 |
| 93 | Route 53 Resolver (hybrid DNS) | Networking | C | 9.5 | 7 | 0.8 | 4 | 57% | 3 | 3 | 1 | 0 | 3 |
| 94 | AWS Backup | Storage | C | 9.5 | 13 | 1.5 | 4 | 31% | 0 | 6 | 1 | 6 | 0 |
| 95 | IoT Core / Greengrass | EndUser | C | 9.4 | 7 | 0.8 | 5 | 71% | 0 | 5 | 1 | 1 | 2 |
| 96 | Transfer Family | Migration | C | 9.2 | 8 | 0.9 | 4 | 50% | 1 | 5 | 0 | 2 | 1 |
| 97 | Compute Optimizer | Management | C | 9.2 | 7 | 0.8 | 5 | 71% | 0 | 4 | 1 | 2 | 1 |
| 98 | Cognito | Security | C | 8.9 | 12 | 1.4 | 8 | 67% | 0 | 9 | 3 | 0 | 6 |
| 99 | CDK | Management | C | 8.9 | 6 | 0.7 | 4 | 67% | 0 | 4 | 1 | 1 | 1 |
| 100 | SES | Integration | C | 8.7 | 8 | 0.9 | 1 | 12% | 0 | 4 | 2 | 2 | 1 |
| 101 | Security Hub | Security | C | 8.6 | 7 | 0.8 | 1 | 14% | 2 | 4 | 0 | 1 | 1 |
| 102 | Server Migration Service (SMS, legacy) | Migration | C | 8.5 | 7 | 0.8 | 0 | 0% | 3 | 0 | 3 | 1 | 1 |
| 103 | Kinesis Data Analytics / Managed Flink | Analytics | C | 8.5 | 7 | 0.8 | 2 | 29% | 3 | 1 | 3 | 0 | 0 |
| 104 | DocumentDB | Database | C | 8.4 | 7 | 0.8 | 1 | 14% | 1 | 4 | 2 | 0 | 0 |
| 105 | IAM Access Analyzer | Security | C | 8.4 | 6 | 0.7 | 2 | 33% | 1 | 3 | 0 | 2 | 0 |
| 106 | Service Quotas | Management | D | 8.3 | 3 | 0.3 | 2 | 67% | 0 | 1 | 1 | 1 | 1 |
| 107 | Rekognition | ML | C | 7.3 | 9 | 1.0 | 4 | 44% | 0 | 7 | 2 | 0 | 3 |
| 108 | WorkSpaces | EndUser | C | 7.1 | 8 | 0.9 | 4 | 50% | 0 | 6 | 2 | 0 | 3 |
| 109 | CloudHSM | Security | C | 6.9 | 6 | 0.7 | 2 | 33% | 0 | 5 | 1 | 0 | 4 |
| 110 | Macie | Security | C | 6.7 | 7 | 0.8 | 3 | 43% | 0 | 5 | 2 | 0 | 2 |
| 111 | CodeCommit | DevTools | C | 6.5 | 8 | 0.9 | 3 | 38% | 0 | 0 | 6 | 2 | 1 |
| 112 | SageMaker | ML | C | 6.4 | 6 | 0.7 | 2 | 33% | 0 | 5 | 0 | 1 | 2 |
| 113 | Transcribe / Translate / Polly | ML | C | 6.4 | 6 | 0.7 | 2 | 33% | 0 | 5 | 0 | 1 | 2 |
| 114 | AppStream 2.0 | EndUser | D | 6.4 | 4 | 0.5 | 2 | 50% | 0 | 2 | 2 | 0 | 3 |
| 115 | Amazon Connect | EndUser | C | 6.3 | 6 | 0.7 | 3 | 50% | 0 | 5 | 1 | 0 | 1 |
| 116 | Resource Groups / Tag Editor / Tag Policies | Management | D | 6.2 | 3 | 0.3 | 3 | 100% | 0 | 2 | 1 | 0 | 2 |
| 117 | Elemental MediaConvert / Media | EndUser | D | 6.2 | 4 | 0.5 | 2 | 50% | 2 | 2 | 0 | 0 | 2 |
| 118 | AWS Batch | Compute | C | 6.1 | 5 | 0.6 | 2 | 40% | 1 | 4 | 0 | 0 | 1 |
| 119 | OpsWorks | Management | C | 6.0 | 8 | 0.9 | 1 | 12% | 3 | 0 | 5 | 0 | 0 |
| 120 | Migration Evaluator | Migration | D | 5.8 | 3 | 0.3 | 2 | 67% | 0 | 1 | 0 | 2 | 1 |
| 121 | MSK (Kafka) | Analytics | C | 5.8 | 5 | 0.6 | 2 | 40% | 0 | 3 | 2 | 0 | 0 |
| 122 | Network Firewall | Networking | D | 5.7 | 3 | 0.3 | 1 | 33% | 1 | 2 | 0 | 0 | 1 |
| 123 | Comprehend | ML | D | 5.7 | 4 | 0.5 | 2 | 50% | 0 | 3 | 0 | 1 | 0 |
| 124 | Textract | ML | D | 5.7 | 3 | 0.3 | 3 | 100% | 0 | 2 | 0 | 1 | 0 |
| 125 | Outposts / Local Zones / Wavelength | Compute | C | 5.6 | 6 | 0.7 | 0 | 0% | 1 | 5 | 0 | 0 | 0 |
| 126 | Elastic Disaster Recovery (DRS) | Migration | D | 5.6 | 3 | 0.3 | 2 | 67% | 0 | 1 | 0 | 2 | 0 |
| 127 | Managed Grafana / Prometheus | Management | D | 5.6 | 4 | 0.5 | 1 | 25% | 0 | 3 | 0 | 1 | 0 |
| 128 | CodeArtifact / CodeGuru / CodeStar | DevTools | C | 5.6 | 6 | 0.7 | 0 | 0% | 0 | 5 | 0 | 1 | 0 |
| 129 | App Runner | Compute | C | 5.5 | 5 | 0.6 | 0 | 0% | 0 | 4 | 0 | 1 | 0 |
| 130 | Lightsail | Compute | D | 5.4 | 4 | 0.5 | 0 | 0% | 1 | 3 | 0 | 0 | 0 |
| 131 | Data Pipeline | Analytics | D | 5.4 | 4 | 0.5 | 0 | 0% | 1 | 3 | 0 | 0 | 0 |
| 132 | Detective | Security | D | 5.4 | 4 | 0.5 | 0 | 0% | 0 | 3 | 0 | 1 | 0 |
| 133 | Well-Architected Tool | Management | D | 5.3 | 3 | 0.3 | 0 | 0% | 0 | 2 | 0 | 1 | 0 |
| 134 | Amplify | DevTools | D | 5.3 | 3 | 0.3 | 0 | 0% | 0 | 2 | 0 | 1 | 0 |
| 135 | Lex / Kendra / Personalize / Forecast | ML | C | 3.6 | 5 | 0.6 | 2 | 40% | 0 | 5 | 0 | 0 | 1 |
| 136 | Pinpoint | EndUser | D | 3.2 | 4 | 0.5 | 0 | 0% | 0 | 4 | 0 | 0 | 1 |
| 137 | Lake Formation | Analytics | D | 3.1 | 3 | 0.3 | 0 | 0% | 0 | 3 | 0 | 0 | 1 |
| 138 | MemoryDB | Database | D | 3.0 | 1 | 0.1 | 1 | 100% | 0 | 1 | 0 | 0 | 1 |
| 139 | Audit Manager / Artifact | Security | D | 2.9 | 4 | 0.5 | 0 | 0% | 0 | 4 | 0 | 0 | 0 |
| 140 | Data Exchange | Analytics | D | 2.8 | 1 | 0.1 | 0 | 0% | 0 | 1 | 0 | 0 | 1 |
| 141 | Keyspaces | Database | D | 2.7 | 2 | 0.2 | 0 | 0% | 0 | 2 | 0 | 0 | 0 |
| 142 | Timestream | Database | D | 2.7 | 2 | 0.2 | 0 | 0% | 0 | 2 | 0 | 0 | 0 |
| 143 | AppFlow | Integration | D | 2.7 | 2 | 0.2 | 0 | 0% | 0 | 2 | 0 | 0 | 0 |
| 144 | Kinesis Video Streams | Analytics | D | 2.7 | 2 | 0.2 | 0 | 0% | 0 | 2 | 0 | 0 | 0 |
| 145 | License Manager | Management | D | 2.7 | 2 | 0.2 | 0 | 0% | 0 | 2 | 0 | 0 | 0 |
| 146 | Cloud Map / App Mesh | Networking | D | 2.6 | 1 | 0.1 | 0 | 0% | 0 | 0 | 0 | 1 | 0 |
| 147 | Health Dashboard | Management | D | 2.6 | 1 | 0.1 | 0 | 0% | 0 | 1 | 0 | 0 | 0 |

## Caveats
- Regex counts: a service named only in an explanation is not counted, and indirect mentions (e.g. "patch baseline" without "Systems Manager") are partly covered. ±10% noise on mid-tier rows.
- "ELB" also counts the GWLB mentions. "VPC core" includes SG/NACL. "Organizations" includes OU/SCP terms.
- Miss counts include retakes, so a question you missed twice counts twice.
- TD Set 6 is only 16q. Neal excludes 25 flagged questions (`neal_excluded.json`).

## Unresolved questions
- Whizlabs (`whizlabs-sap-c02-111-labs.md`) is a labs list, not a question bank, so it's excluded. Add it if you have Whizlabs questions.
