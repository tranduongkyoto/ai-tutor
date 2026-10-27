# SAP-C02 — Service → Technical Keyword Frequency (All Practice Tests)

**Date:** 2026-10-27 · **Corpus:** 886 questions — Udemy 180 · Tutorials Dojo 391 · Neal Davis 185 · AWS Free 130 · **Your misses:** 266 miss notes from all `*review_notes.json`
**Scope:** 121 services/groups · 801 technical keywords. Companion to `sap-c02-service-frequency-261027-1428-all-practice-tests-report.md`.

## Legend
- **Qs**: number of questions whose stem or options mention the keyword (counted once per question).
- **Correct**: number of questions where the keyword is in the correct option. **Ans%** = Correct / Qs. High = usually the answer; low = usually a distractor.
- **+Expl**: questions where the keyword appears anywhere, explanations included. A keyword with Qs=0 but +Expl>0 is taught in explanations but never asked directly.
- **U / TD / N / F**: Udemy / Tutorials Dojo / Neal / AWS Free question counts. **Miss**: your miss notes that mention the keyword.
- **Pri**: ★★★ ≥30 Qs (must know cold) · ★★ 10–29 (know trade-offs) · ★ 3–9 (recognize) · · <3 (skim).
- **Tier** (service): S ≥90 Qs · A 40–89 · B 15–39 · C 5–14 · D <5.

## Contents
- [Networking & Content Delivery](#networking-content-delivery)
- [Compute & Containers](#compute-containers)
- [Storage](#storage)
- [Databases](#databases)
- [Migration & Transfer](#migration-transfer)
- [Application Integration](#application-integration)
- [Analytics](#analytics)
- [Security, Identity & Compliance](#security-identity-compliance)
- [Management, Governance & Cost](#management-governance-cost)
- [Developer Tools / CI-CD](#developer-tools-ci-cd)
- [Machine Learning / AI](#machine-learning-ai)
- [End-user, IoT, Media](#end-user-iot-media)
- [Niche services & tooling](#niche-services-tooling)
- [Architecture concepts & question qualifiers](#architecture-concepts-question-qualifiers)
- [Top 80 technical keywords overall](#top-80-technical-keywords-overall)
- [Your miss hot-spots](#your-miss-hot-spots)

## Top 80 technical keywords overall

| Service | Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Elastic Load Balancing | ALB (Application LB) | ★★★ | 144 | 65 | 45% | 152 | 21 | 69 | 31 | 23 | 26 |
| RDS | Engine: MySQL | ★★★ | 96 | 38 | 40% | 106 | 14 | 44 | 23 | 15 | 10 |
| IAM | IAM roles | ★★★ | 88 | 56 | 64% | 98 | 12 | 47 | 18 | 11 | 11 |
| VPC | Subnets (any) | ★★★ | 71 | 29 | 41% | 104 | 13 | 28 | 15 | 15 | 7 |
| RDS | Multi-AZ (any) | ★★★ | 62 | 25 | 40% | 71 | 11 | 36 | 9 | 6 | 15 |
| RDS | Read replicas | ★★★ | 62 | 30 | 48% | 66 | 9 | 32 | 10 | 11 | 12 |
| IAM | IAM users / groups | ★★★ | 55 | 15 | 27% | 74 | 4 | 31 | 11 | 9 | 4 |
| EC2 | AMI / golden image | ★★★ | 51 | 18 | 35% | 60 | 7 | 27 | 9 | 8 | 10 |
| VPC | Security groups | ★★★ | 48 | 27 | 56% | 61 | 10 | 18 | 14 | 6 | 3 |
| Organizations & SCPs | SCPs (any) | ★★★ | 46 | 28 | 61% | 49 | 7 | 21 | 13 | 5 | 16 |
| Compliance & data protection (concepts) | Encryption in transit (TLS/HTTPS) | ★★★ | 45 | 13 | 29% | 763 | 8 | 26 | 8 | 3 | 9 |
| VPC | Private subnet | ★★★ | 43 | 10 | 23% | 55 | 3 | 19 | 12 | 9 | 2 |
| Compliance & data protection (concepts) | Audit / auditor | ★★★ | 43 | 9 | 21% | 73 | 12 | 22 | 5 | 4 | 6 |
| Elastic Load Balancing | NLB (Network LB) | ★★★ | 40 | 10 | 25% | 51 | 8 | 17 | 7 | 8 | 7 |
| Snow Family | Data volume stated in TB/PB (do bandwidth math) | ★★★ | 40 | 1 | 2% | 43 | 8 | 19 | 10 | 3 | 9 |
| Purchase options & pricing | Spot Instances (any) | ★★★ | 39 | 14 | 36% | 42 | 2 | 25 | 7 | 5 | 10 |
| Organizations & SCPs | Management account | ★★★ | 37 | 25 | 68% | 48 | 1 | 15 | 10 | 11 | 4 |
| CloudWatch | Alarms | ★★★ | 37 | 16 | 43% | 53 | 10 | 13 | 8 | 6 | 4 |
| NAT Gateway | NAT gateway | ★★★ | 35 | 17 | 49% | 38 | 7 | 10 | 7 | 11 | 3 |
| S3 | Replication (CRR/SRR/RTC) | ★★★ | 35 | 14 | 40% | 45 | 6 | 17 | 7 | 5 | 5 |
| S3 | Static website hosting | ★★★ | 35 | 13 | 37% | 46 | 3 | 22 | 8 | 2 | 5 |
| Organizations & SCPs | OUs | ★★★ | 35 | 21 | 60% | 42 | 5 | 17 | 8 | 5 | 7 |
| CloudWatch | CloudWatch Logs / log groups | ★★★ | 35 | 14 | 40% | 39 | 16 | 8 | 6 | 5 | 4 |
| EC2 | Windows workloads | ★★★ | 34 | 10 | 29% | 56 | 5 | 20 | 6 | 3 | 15 |
| VPC | Public subnet | ★★★ | 33 | 8 | 24% | 43 | 4 | 11 | 10 | 8 | 3 |
| Organizations & SCPs | Member accounts | ★★★ | 33 | 14 | 42% | 49 | 3 | 15 | 5 | 10 | 3 |
| EMR | Hadoop / HDFS / Hive / Presto / HBase | ★★★ | 32 | 13 | 41% | 56 | 12 | 14 | 3 | 3 | 8 |
| CLI / SDK / API tooling | AWS CLI | ★★★ | 32 | 11 | 34% | 61 | 5 | 12 | 6 | 9 | 2 |
| AWS Config | Config rules (managed/custom) | ★★★ | 30 | 9 | 30% | 36 | 3 | 18 | 3 | 6 | 7 |
| S3 | Bucket policy | ★★ | 29 | 16 | 55% | 35 | 8 | 12 | 8 | 1 | 8 |
| EventBridge | Rules / event patterns | ★★ | 28 | 16 | 57% | 31 | 3 | 8 | 10 | 7 | 1 |
| VPC | Route tables | ★★ | 27 | 12 | 44% | 41 | 3 | 11 | 7 | 6 | 1 |
| Direct Connect | Any VIF mention | ★★ | 27 | 14 | 52% | 31 | 10 | 8 | 5 | 4 | 7 |
| Migration strategy (7 Rs) | Refactor / re-architect | ★★ | 27 | 6 | 22% | 32 | 5 | 9 | 9 | 4 | 2 |
| CLI / SDK / API tooling | Custom scripts / cron on EC2 | ★★ | 27 | 4 | 15% | 33 | 6 | 13 | 6 | 2 | 0 |
| VPC | Private / public IP address | ★★ | 26 | 7 | 27% | 60 | 6 | 5 | 7 | 8 | 5 |
| Elastic Load Balancing | Health checks (generic) | ★★ | 26 | 17 | 65% | 41 | 7 | 11 | 4 | 4 | 3 |
| CloudWatch | Dashboards | ★★ | 26 | 11 | 42% | 35 | 6 | 12 | 3 | 5 | 2 |
| RDS | Engine: PostgreSQL | ★★ | 25 | 5 | 20% | 43 | 4 | 11 | 4 | 6 | 1 |
| PrivateLink / VPC Endpoints | Gateway endpoint (S3/DynamoDB) | ★★ | 24 | 10 | 42% | 31 | 6 | 6 | 4 | 8 | 8 |
| Route 53 | Failover routing (active-passive) | ★★ | 24 | 14 | 58% | 29 | 2 | 11 | 5 | 6 | 4 |
| EC2 | Instance types / families / Graviton | ★★ | 24 | 7 | 29% | 37 | 1 | 11 | 4 | 8 | 0 |
| Athena | Query S3 / logs with SQL | ★★ | 24 | 9 | 38% | 36 | 7 | 7 | 5 | 5 | 1 |
| Direct Connect | Private VIF | ★★ | 23 | 7 | 30% | 26 | 9 | 7 | 4 | 3 | 6 |
| S3 | Lifecycle policies / transitions | ★★ | 23 | 15 | 65% | 30 | 5 | 10 | 3 | 5 | 1 |
| IAM | Cross-account role / access | ★★ | 23 | 9 | 39% | 33 | 3 | 10 | 7 | 3 | 2 |
| Purchase options & pricing | Reserved Instances (any) | ★★ | 23 | 11 | 48% | 30 | 2 | 11 | 7 | 3 | 6 |
| VPC | Network ACL (NACL) | ★★ | 22 | 5 | 23% | 26 | 3 | 11 | 5 | 3 | 7 |
| Site-to-Site / Client VPN | Site-to-Site VPN | ★★ | 22 | 4 | 18% | 27 | 6 | 6 | 5 | 5 | 4 |
| S3 | Transfer Acceleration | ★★ | 22 | 9 | 41% | 22 | 9 | 5 | 5 | 3 | 3 |
| VPC | Elastic IP | ★★ | 21 | 9 | 43% | 27 | 4 | 8 | 4 | 5 | 2 |
| EC2 | User data / bootstrap | ★★ | 21 | 4 | 19% | 26 | 4 | 13 | 1 | 3 | 2 |
| S3 | Glacier Flexible Retrieval | ★★ | 21 | 12 | 57% | 32 | 6 | 13 | 2 | 0 | 4 |
| DynamoDB | Global Tables | ★★ | 21 | 11 | 52% | 23 | 2 | 6 | 8 | 5 | 0 |
| API Gateway | REST API | ★★ | 21 | 7 | 33% | 31 | 2 | 6 | 10 | 3 | 3 |
| Cognito | Social IdP (Google/Facebook/Amazon) | ★★ | 21 | 3 | 14% | 35 | 9 | 11 | 1 | 0 | 3 |
| Compliance & data protection (concepts) | Encryption at rest | ★★ | 21 | 4 | 19% | 26 | 1 | 13 | 4 | 3 | 1 |
| VPC | Internet Gateway | ★★ | 20 | 1 | 5% | 33 | 4 | 7 | 4 | 5 | 2 |
| Route 53 | Hosted zone (any) | ★★ | 20 | 12 | 60% | 26 | 4 | 8 | 5 | 3 | 4 |
| Storage Gateway | S3 File Gateway (NFS/SMB to S3) | ★★ | 20 | 4 | 20% | 22 | 7 | 8 | 2 | 3 | 5 |
| PrivateLink / VPC Endpoints | Interface endpoint (ENI) | ★★ | 19 | 13 | 68% | 32 | 8 | 3 | 4 | 4 | 2 |
| EventBridge | Scheduler / cron / rate | ★★ | 19 | 4 | 21% | 19 | 5 | 7 | 5 | 2 | 1 |
| Site-to-Site / Client VPN | Virtual private gateway (VGW) | ★★ | 18 | 9 | 50% | 23 | 5 | 8 | 3 | 2 | 8 |
| Route 53 | Alias records | ★★ | 18 | 12 | 67% | 23 | 1 | 12 | 3 | 2 | 8 |
| RDS | Engine: Oracle | ★★ | 18 | 4 | 22% | 30 | 2 | 12 | 2 | 2 | 4 |
| IAM | Trust policy | ★★ | 18 | 16 | 89% | 20 | 2 | 9 | 3 | 4 | 4 |
| CloudWatch | CloudWatch agent (unified) | ★★ | 18 | 8 | 44% | 19 | 4 | 6 | 4 | 4 | 2 |
| Cost tools (Cost Explorer, CUR, Budgets, Anomaly Detection) | Chargeback / showback per team | ★★ | 18 | 8 | 44% | 19 | 2 | 7 | 5 | 4 | 0 |
| Purchase options & pricing | On-Demand | ★★ | 18 | 4 | 22% | 21 | 1 | 9 | 5 | 3 | 0 |
| S3 | Versioning | ★★ | 17 | 2 | 12% | 23 | 2 | 7 | 5 | 3 | 3 |
| Resource Access Manager (RAM) | Share with org / OU | ★★ | 17 | 9 | 53% | 33 | 3 | 6 | 2 | 6 | 5 |
| Systems Manager | Patch Manager / patch baseline / patch group | ★★ | 17 | 10 | 59% | 32 | 1 | 14 | 1 | 1 | 9 |
| CloudFormation | DeletionPolicy / Retain / UpdateReplacePolicy | ★★ | 17 | 7 | 41% | 28 | 3 | 9 | 0 | 5 | 1 |
| VPC | CIDR / overlapping IPs / IPAM | ★★ | 16 | 6 | 38% | 26 | 5 | 4 | 4 | 3 | 2 |
| Route 53 | Private hosted zone | ★★ | 16 | 10 | 62% | 17 | 4 | 6 | 5 | 1 | 3 |
| EC2 | EC2 Instance Connect / SSH keys | ★★ | 16 | 2 | 12% | 25 | 2 | 5 | 7 | 2 | 4 |
| RDS | Cross-Region read replica | ★★ | 16 | 8 | 50% | 20 | 3 | 6 | 5 | 2 | 4 |
| DynamoDB | On-demand vs provisioned / RCU/WCU | ★★ | 16 | 8 | 50% | 26 | 1 | 8 | 5 | 2 | 2 |
| IAM | Least privilege | ★★ | 16 | 2 | 12% | 24 | 3 | 7 | 3 | 3 | 5 |
| STS & federation | AssumeRoleWithSAML / SAML 2.0 | ★★ | 16 | 9 | 56% | 23 | 3 | 8 | 4 | 1 | 7 |

## Your miss hot-spots
Keywords with ≥3 miss notes, ranked by misses relative to frequency.

| Service | Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Elastic Load Balancing | TLS termination / SNI / SSL offload | ★ | 3 | 1 | 33% | 6 | 0 | 3 | 0 | 0 | 3 |
| IAM Identity Center (SSO) | External IdP (Okta/Entra/AD) | ★★ | 10 | 6 | 60% | 23 | 0 | 6 | 3 | 1 | 8 |
| Route 53 Resolver (hybrid DNS) | Inbound endpoint | ★ | 4 | 2 | 50% | 5 | 2 | 2 | 0 | 0 | 3 |
| End-user computing (WorkSpaces, AppStream, Connect, Pinpoint, WorkDocs) | AppStream 2.0 (app streaming) | ★ | 4 | 2 | 50% | 4 | 0 | 2 | 2 | 0 | 3 |
| Route 53 | Geolocation routing | ★ | 6 | 1 | 17% | 10 | 1 | 4 | 1 | 0 | 4 |
| STS & federation | AssumeRoleWithWebIdentity / OIDC | ★ | 8 | 6 | 75% | 11 | 0 | 7 | 1 | 0 | 5 |
| Elastic Load Balancing | GWLB (Gateway LB) | ★ | 7 | 3 | 43% | 14 | 2 | 4 | 1 | 0 | 4 |
| Direct Connect | Direct Connect Gateway | ★★ | 11 | 10 | 91% | 15 | 0 | 5 | 3 | 3 | 6 |
| Systems Manager | Patch Manager / patch baseline / patch group | ★★ | 17 | 10 | 59% | 32 | 1 | 14 | 1 | 1 | 9 |
| VPC | Bastion host | ★ | 6 | 0 | 0% | 10 | 1 | 2 | 3 | 0 | 3 |
| Media (Elemental) | MediaConvert / Elastic Transcoder | ★ | 6 | 3 | 50% | 6 | 3 | 3 | 0 | 0 | 3 |
| Site-to-Site / Client VPN | Virtual private gateway (VGW) | ★★ | 18 | 9 | 50% | 23 | 5 | 8 | 3 | 2 | 8 |
| Route 53 | Alias records | ★★ | 18 | 12 | 67% | 23 | 1 | 12 | 3 | 2 | 8 |
| EC2 | Windows workloads | ★★★ | 34 | 10 | 29% | 56 | 5 | 20 | 6 | 3 | 15 |
| STS & federation | AssumeRoleWithSAML / SAML 2.0 | ★★ | 16 | 9 | 56% | 23 | 3 | 8 | 4 | 1 | 7 |
| Lambda | 15-min timeout / long-running | ★★ | 14 | 1 | 7% | 35 | 1 | 8 | 3 | 2 | 6 |
| Redshift | Snapshots / cross-Region | ★ | 7 | 4 | 57% | 7 | 2 | 3 | 2 | 0 | 3 |
| API Gateway | Custom domain | ★ | 7 | 3 | 43% | 12 | 1 | 5 | 1 | 0 | 3 |
| Snow Family | Snowball (any) | ★★ | 15 | 7 | 47% | 15 | 7 | 0 | 6 | 2 | 6 |
| Shield | DDoS (any) | ★★ | 10 | 3 | 30% | 20 | 3 | 6 | 1 | 0 | 4 |
| CloudFront | Origin Access Control / Identity (OAC/OAI) | ★★ | 13 | 6 | 46% | 14 | 1 | 7 | 4 | 1 | 5 |
| Server Migration Service / VM Import (legacy) | VM Import/Export | ★★ | 13 | 6 | 46% | 15 | 2 | 7 | 2 | 2 | 5 |
| End-user computing (WorkSpaces, AppStream, Connect, Pinpoint, WorkDocs) | WorkSpaces (VDI) | ★ | 8 | 4 | 50% | 8 | 0 | 6 | 2 | 0 | 3 |
| Organizations & SCPs | SCPs (any) | ★★★ | 46 | 28 | 61% | 49 | 7 | 21 | 13 | 5 | 16 |
| PrivateLink / VPC Endpoints | Gateway endpoint (S3/DynamoDB) | ★★ | 24 | 10 | 42% | 31 | 6 | 6 | 4 | 8 | 8 |
| S3 | SSE-S3 / SSE-KMS / SSE-C / DSSE | ★★ | 12 | 7 | 58% | 16 | 2 | 6 | 3 | 1 | 4 |
| Aurora | Aurora Replicas | ★★ | 12 | 10 | 83% | 17 | 1 | 5 | 3 | 3 | 4 |
| Organizations & SCPs | Deny list vs allow list / FullAWSAccess | ★ | 9 | 2 | 22% | 12 | 0 | 1 | 5 | 3 | 3 |
| AI services (Rekognition, Comprehend, Transcribe, Translate, Polly, Textract, Lex, Kendra, Personalize, Forecast, Bedrock) | Rekognition (image/video) | ★ | 9 | 4 | 44% | 9 | 0 | 7 | 2 | 0 | 3 |
| VPC | Network ACL (NACL) | ★★ | 22 | 5 | 23% | 26 | 3 | 11 | 5 | 3 | 7 |
| IAM | Least privilege | ★★ | 16 | 2 | 12% | 24 | 3 | 7 | 3 | 3 | 5 |
| CloudFront | Signed URLs / signed cookies | ★★ | 13 | 7 | 54% | 16 | 3 | 8 | 2 | 0 | 4 |
| Systems Manager | Session Manager (no SSH/bastion) | ★★ | 13 | 7 | 54% | 13 | 1 | 6 | 4 | 2 | 4 |
| RDS | RDS Proxy | ★★ | 10 | 9 | 90% | 10 | 0 | 5 | 1 | 4 | 3 |
| API Gateway | Throttling | ★★ | 10 | 5 | 50% | 23 | 2 | 3 | 4 | 1 | 3 |
| API Gateway | Authorizers (Lambda/Cognito/IAM) | ★★ | 10 | 1 | 10% | 14 | 0 | 3 | 3 | 4 | 3 |
| WAF | Managed rule groups | ★★ | 10 | 3 | 30% | 13 | 0 | 6 | 1 | 3 | 3 |
| Systems Manager | Maintenance windows | ★★ | 10 | 3 | 30% | 13 | 1 | 8 | 1 | 0 | 3 |
| Purchase options & pricing | Spot interruption / 2-min / rebalance | ★★ | 10 | 0 | 0% | 36 | 1 | 5 | 2 | 2 | 3 |
| Resource Access Manager (RAM) | Share with org / OU | ★★ | 17 | 9 | 53% | 33 | 3 | 6 | 2 | 6 | 5 |
| Lambda@Edge / CloudFront Functions | Lambda@Edge | ★★ | 14 | 8 | 57% | 19 | 2 | 7 | 3 | 2 | 4 |
| Systems Manager | Parameter Store / SecureString | ★★ | 14 | 5 | 36% | 14 | 1 | 9 | 1 | 3 | 4 |
| S3 | Bucket policy | ★★ | 29 | 16 | 55% | 35 | 8 | 12 | 8 | 1 | 8 |
| Direct Connect | Private VIF | ★★ | 23 | 7 | 30% | 26 | 9 | 7 | 4 | 3 | 6 |
| Purchase options & pricing | Reserved Instances (any) | ★★ | 23 | 11 | 48% | 30 | 2 | 11 | 7 | 3 | 6 |
| Direct Connect | Any VIF mention | ★★ | 27 | 14 | 52% | 31 | 10 | 8 | 5 | 4 | 7 |
| Purchase options & pricing | Spot Instances (any) | ★★★ | 39 | 14 | 36% | 42 | 2 | 25 | 7 | 5 | 10 |
| EC2 | EC2 Instance Connect / SSH keys | ★★ | 16 | 2 | 12% | 25 | 2 | 5 | 7 | 2 | 4 |
| FSx | FSx for Windows File Server | ★★ | 12 | 6 | 50% | 15 | 3 | 5 | 2 | 2 | 3 |
| Storage Gateway | S3 File Gateway (NFS/SMB to S3) | ★★ | 20 | 4 | 20% | 22 | 7 | 8 | 2 | 3 | 5 |

## Networking & Content Delivery

| Service | Tier | Qs | % of exam | Correct | Ans% | +Expl | Miss |
|---|---|---|---|---|---|---|---|
| VPC | S | 193 | 21.8% | 99 | 51% | 226 | 31 |
| Elastic Load Balancing | S | 191 | 21.6% | 90 | 47% | 208 | 37 |
| CloudFront | S | 116 | 13.1% | 70 | 60% | 140 | 31 |
| Route 53 | S | 97 | 10.9% | 49 | 51% | 111 | 16 |
| Direct Connect | A | 74 | 8.4% | 29 | 39% | 97 | 13 |
| Site-to-Site / Client VPN | A | 54 | 6.1% | 19 | 35% | 73 | 11 |
| PrivateLink / VPC Endpoints | A | 54 | 6.1% | 34 | 63% | 60 | 15 |
| NAT Gateway | A | 41 | 4.6% | 19 | 46% | 52 | 4 |
| VPC Peering | B | 30 | 3.4% | 5 | 17% | 39 | 1 |
| Transit Gateway | B | 30 | 3.4% | 13 | 43% | 42 | 7 |
| Global Accelerator | B | 27 | 3.0% | 7 | 26% | 28 | 4 |
| Lambda@Edge / CloudFront Functions | B | 18 | 2.0% | 11 | 61% | 21 | 5 |
| VPC Flow Logs & network diagnostics | B | 18 | 2.0% | 6 | 33% | 21 | 2 |
| Route 53 Resolver (hybrid DNS) | C | 7 | 0.8% | 5 | 71% | 13 | 3 |
| Network Firewall | D | 3 | 0.3% | 1 | 33% | 4 | 1 |
| Other networking (Lattice, Cloud Map, App Mesh) | D | 2 | 0.2% | 1 | 50% | 2 | 0 |

### VPC
**Tier S** · Qs 193 (21.8%) · correct 99 (51%) · +expl 226 · U 44 / TD 90 / N 31 / F 28 · your misses 31

> Network foundation; every hybrid/multi-account question builds on it

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Subnets (any) | ★★★ | 71 | 29 | 41% | 104 | 13 | 28 | 15 | 15 | 7 |
| Security groups | ★★★ | 48 | 27 | 56% | 61 | 10 | 18 | 14 | 6 | 3 |
| Private subnet | ★★★ | 43 | 10 | 23% | 55 | 3 | 19 | 12 | 9 | 2 |
| Public subnet | ★★★ | 33 | 8 | 24% | 43 | 4 | 11 | 10 | 8 | 3 |
| Route tables | ★★ | 27 | 12 | 44% | 41 | 3 | 11 | 7 | 6 | 1 |
| Private / public IP address | ★★ | 26 | 7 | 27% | 60 | 6 | 5 | 7 | 8 | 5 |
| Network ACL (NACL) | ★★ | 22 | 5 | 23% | 26 | 3 | 11 | 5 | 3 | 7 |
| Elastic IP | ★★ | 21 | 9 | 43% | 27 | 4 | 8 | 4 | 5 | 2 |
| Internet Gateway | ★★ | 20 | 1 | 5% | 33 | 4 | 7 | 4 | 5 | 2 |
| CIDR / overlapping IPs / IPAM | ★★ | 16 | 6 | 38% | 26 | 5 | 4 | 4 | 3 | 2 |
| ENI (elastic network interface) | ★★ | 15 | 6 | 40% | 44 | 9 | 4 | 1 | 1 | 3 |
| Bastion host | ★ | 6 | 0 | 0% | 10 | 1 | 2 | 3 | 0 | 3 |
| Prefix lists | ★ | 5 | 2 | 40% | 8 | 0 | 2 | 2 | 1 | 1 |
| Shared VPC (subnet sharing via RAM) | ★ | 4 | 2 | 50% | 5 | 2 | 2 | 0 | 0 | 2 |
| Egress-only IGW (IPv6) | ★ | 3 | 1 | 33% | 3 | 0 | 1 | 1 | 1 | 0 |
| IPv6 | · | 2 | 1 | 50% | 18 | 1 | 0 | 1 | 0 | 0 |
| DHCP option sets | · | 2 | 2 | 100% | 4 | 0 | 1 | 1 | 0 | 1 |
| Default VPC | · | 1 | 0 | 0% | 2 | 1 | 0 | 0 | 0 | 0 |

### Elastic Load Balancing
**Tier S** · Qs 191 (21.6%) · correct 90 (47%) · +expl 208 · U 29 / TD 97 / N 38 / F 27 · your misses 37

> ALB L7 / NLB L4 static IP / GWLB appliances

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| ALB (Application LB) | ★★★ | 144 | 65 | 45% | 152 | 21 | 69 | 31 | 23 | 26 |
| NLB (Network LB) | ★★★ | 40 | 10 | 25% | 51 | 8 | 17 | 7 | 8 | 7 |
| Health checks (generic) | ★★ | 26 | 17 | 65% | 41 | 7 | 11 | 4 | 4 | 3 |
| Target groups | ★★ | 15 | 8 | 53% | 24 | 3 | 6 | 4 | 2 | 1 |
| Path/host-based routing, listener rules | ★ | 9 | 3 | 33% | 16 | 2 | 2 | 4 | 1 | 0 |
| Listeners (HTTP/HTTPS/TCP/UDP) | ★ | 7 | 4 | 57% | 18 | 1 | 4 | 2 | 0 | 2 |
| GWLB (Gateway LB) | ★ | 7 | 3 | 43% | 14 | 2 | 4 | 1 | 0 | 4 |
| Sticky sessions | ★ | 7 | 4 | 57% | 7 | 4 | 2 | 0 | 1 | 1 |
| Connection draining / dereg delay | ★ | 5 | 4 | 80% | 5 | 1 | 2 | 2 | 0 | 0 |
| X-Forwarded-For / client IP | ★ | 4 | 1 | 25% | 19 | 1 | 2 | 1 | 0 | 1 |
| TLS termination / SNI / SSL offload | ★ | 3 | 1 | 33% | 6 | 0 | 3 | 0 | 0 | 3 |
| Cross-zone LB | · | 2 | 1 | 50% | 3 | 1 | 1 | 0 | 0 | 0 |
| Weighted target groups | · | 1 | 0 | 0% | 2 | 0 | 0 | 0 | 1 | 0 |
| CLB (Classic, legacy) | · | 0 | 0 | – | 2 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* ALB authentication (OIDC/Cognito), Proxy protocol

### CloudFront
**Tier S** · Qs 116 (13.1%) · correct 70 (60%) · +expl 140 · U 17 / TD 61 / N 25 / F 13 · your misses 31

> CDN; caching, edge security, S3 origin protection

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Cache behaviors / TTL / cache policy | ★★ | 14 | 7 | 50% | 17 | 2 | 9 | 1 | 2 | 2 |
| Signed URLs / signed cookies | ★★ | 13 | 7 | 54% | 16 | 3 | 8 | 2 | 0 | 4 |
| Origin Access Control / Identity (OAC/OAI) | ★★ | 13 | 6 | 46% | 14 | 1 | 7 | 4 | 1 | 5 |
| Access / real-time logs (any service) | ★ | 6 | 1 | 17% | 6 | 4 | 1 | 1 | 0 | 1 |
| Origin groups / origin failover | ★ | 5 | 5 | 100% | 6 | 0 | 2 | 0 | 3 | 1 |
| Custom origin headers (secret header) | ★ | 4 | 3 | 75% | 6 | 1 | 1 | 2 | 0 | 1 |
| Viewer protocol / HTTPS redirect | ★ | 4 | 4 | 100% | 6 | 0 | 4 | 0 | 0 | 1 |
| Field-level encryption | ★ | 3 | 1 | 33% | 3 | 0 | 3 | 0 | 0 | 0 |
| Price class | · | 2 | 1 | 50% | 2 | 0 | 1 | 1 | 0 | 1 |
| Geo restriction | · | 1 | 1 | 100% | 2 | 0 | 1 | 0 | 0 | 1 |
| Invalidation | · | 1 | 0 | 0% | 2 | 0 | 1 | 0 | 0 | 1 |
| Origin Shield | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 0 |

### Route 53
**Tier S** · Qs 97 (10.9%) · correct 49 (51%) · +expl 111 · U 14 / TD 46 / N 23 / F 14 · your misses 16

> DNS + routing policies + health-check failover

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Failover routing (active-passive) | ★★ | 24 | 14 | 58% | 29 | 2 | 11 | 5 | 6 | 4 |
| Hosted zone (any) | ★★ | 20 | 12 | 60% | 26 | 4 | 8 | 5 | 3 | 4 |
| Alias records | ★★ | 18 | 12 | 67% | 23 | 1 | 12 | 3 | 2 | 8 |
| Private hosted zone | ★★ | 16 | 10 | 62% | 17 | 4 | 6 | 5 | 1 | 3 |
| Latency-based routing | ★★ | 15 | 8 | 53% | 23 | 3 | 6 | 4 | 2 | 0 |
| CNAME | ★★ | 12 | 2 | 17% | 22 | 1 | 6 | 3 | 2 | 2 |
| Weighted routing | ★★ | 10 | 1 | 10% | 17 | 2 | 1 | 4 | 3 | 1 |
| Route 53 health checks | ★ | 9 | 5 | 56% | 16 | 3 | 4 | 1 | 1 | 1 |
| Geolocation routing | ★ | 6 | 1 | 17% | 10 | 1 | 4 | 1 | 0 | 4 |
| Multivalue answer | ★ | 6 | 1 | 17% | 9 | 0 | 4 | 1 | 1 | 1 |
| Geoproximity routing / bias | ★ | 5 | 0 | 0% | 8 | 1 | 3 | 0 | 1 | 0 |
| Public hosted zone | ★ | 5 | 1 | 20% | 5 | 2 | 2 | 0 | 1 | 1 |
| Traffic Flow | · | 2 | 0 | 0% | 5 | 1 | 1 | 0 | 0 | 0 |
| DNSSEC | · | 2 | 1 | 50% | 2 | 0 | 2 | 0 | 0 | 1 |
| Delegated subdomain / NS records | · | 1 | 1 | 100% | 11 | 0 | 1 | 0 | 0 | 1 |
| Simple routing | · | 1 | 0 | 0% | 5 | 0 | 1 | 0 | 0 | 0 |
| Domain registration / transfer | · | 1 | 1 | 100% | 2 | 0 | 1 | 0 | 0 | 0 |
| Application Recovery Controller | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* IP-based routing

### Direct Connect
**Tier A** · Qs 74 (8.4%) · correct 29 (39%) · +expl 97 · U 18 / TD 35 / N 14 / F 7 · your misses 13

> Private dedicated link to on-prem; consistent bandwidth, not encrypted by default

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Any VIF mention | ★★ | 27 | 14 | 52% | 31 | 10 | 8 | 5 | 4 | 7 |
| Private VIF | ★★ | 23 | 7 | 30% | 26 | 9 | 7 | 4 | 3 | 6 |
| Public VIF | ★★ | 13 | 5 | 38% | 14 | 6 | 4 | 2 | 1 | 1 |
| Direct Connect Gateway | ★★ | 11 | 10 | 91% | 15 | 0 | 5 | 3 | 3 | 6 |
| BGP / ASN / AS_PATH / local pref | ★ | 8 | 4 | 50% | 11 | 2 | 3 | 2 | 1 | 1 |
| Redundant / 2nd DX / resiliency | ★ | 7 | 3 | 43% | 9 | 1 | 4 | 1 | 1 | 1 |
| Dedicated connection | ★ | 5 | 0 | 0% | 10 | 2 | 3 | 0 | 0 | 0 |
| Transit VIF | ★ | 4 | 2 | 50% | 7 | 1 | 1 | 0 | 2 | 2 |
| LAG (link aggregation) | ★ | 4 | 0 | 0% | 4 | 0 | 3 | 1 | 0 | 0 |
| DX location / colocation | · | 1 | 0 | 0% | 12 | 0 | 0 | 0 | 1 | 1 |
| Hosted connection (partner) | · | 1 | 0 | 0% | 3 | 0 | 1 | 0 | 0 | 0 |
| MACsec | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 1 |

*Never mentioned:* SiteLink

### Site-to-Site / Client VPN
**Tier A** · Qs 54 (6.1%) · correct 19 (35%) · +expl 73 · U 9 / TD 24 / N 13 / F 8 · your misses 11

> IPsec over internet; quick/cheap hybrid link or DX backup

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Site-to-Site VPN | ★★ | 22 | 4 | 18% | 27 | 6 | 6 | 5 | 5 | 4 |
| Virtual private gateway (VGW) | ★★ | 18 | 9 | 50% | 23 | 5 | 8 | 3 | 2 | 8 |
| IPsec / VPN over DX (encryption) | ★★ | 13 | 2 | 15% | 22 | 2 | 6 | 5 | 0 | 2 |
| Customer gateway (CGW) | ★ | 6 | 4 | 67% | 8 | 3 | 2 | 0 | 1 | 1 |
| Software VPN on EC2 | ★ | 5 | 1 | 20% | 9 | 2 | 2 | 1 | 0 | 0 |
| Client VPN | ★ | 4 | 3 | 75% | 5 | 0 | 2 | 2 | 0 | 1 |
| VPN CloudHub | ★ | 4 | 1 | 25% | 5 | 1 | 2 | 1 | 0 | 0 |
| VPN as DX backup | · | 2 | 0 | 0% | 3 | 1 | 1 | 0 | 0 | 2 |

*Never mentioned:* Accelerated VPN

### PrivateLink / VPC Endpoints
**Tier A** · Qs 54 (6.1%) · correct 34 (63%) · +expl 60 · U 14 / TD 14 / N 10 / F 16 · your misses 15

> Private access to AWS services or a provider's service without IGW/NAT/peering

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Gateway endpoint (S3/DynamoDB) | ★★ | 24 | 10 | 42% | 31 | 6 | 6 | 4 | 8 | 8 |
| Interface endpoint (ENI) | ★★ | 19 | 13 | 68% | 32 | 8 | 3 | 4 | 4 | 2 |
| Endpoint service (provider side, NLB) | ★ | 7 | 7 | 100% | 13 | 1 | 2 | 2 | 2 | 2 |
| Endpoint policy | ★ | 7 | 7 | 100% | 8 | 2 | 1 | 2 | 2 | 2 |
| Private DNS for endpoints | ★ | 5 | 2 | 40% | 5 | 1 | 2 | 2 | 0 | 2 |
| aws:SourceVpce / SourceVpc condition | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 1 |

### NAT Gateway
**Tier A** · Qs 41 (4.6%) · correct 19 (46%) · +expl 52 · U 10 / TD 12 / N 7 / F 12 · your misses 4

> Outbound-only internet for private subnets; per-AZ for HA; costs per GB

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| NAT gateway | ★★★ | 35 | 17 | 49% | 38 | 7 | 10 | 7 | 11 | 3 |
| NAT instance (legacy) | ★ | 9 | 2 | 22% | 12 | 1 | 6 | 1 | 1 | 0 |
| Centralized egress VPC | · | 1 | 0 | 0% | 2 | 0 | 0 | 0 | 1 | 0 |

### VPC Peering
**Tier B** · Qs 30 (3.4%) · correct 5 (17%) · +expl 39 · U 8 / TD 13 / N 3 / F 6 · your misses 1

> 1:1 non-transitive VPC link; cheap for few VPCs, fails at scale

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Inter-Region peering | ★ | 5 | 0 | 0% | 9 | 1 | 2 | 2 | 0 | 0 |
| Transitive routing (not supported) | · | 2 | 0 | 0% | 8 | 0 | 0 | 2 | 0 | 0 |

### Transit Gateway
**Tier B** · Qs 30 (3.4%) · correct 13 (43%) · +expl 42 · U 3 / TD 12 / N 6 / F 9 · your misses 7

> Hub-and-spoke for many VPCs + VPN/DX; transitive routing

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| TGW attachments | ★ | 6 | 3 | 50% | 7 | 0 | 3 | 1 | 2 | 0 |
| TGW route tables / segmentation | ★ | 5 | 3 | 60% | 11 | 0 | 2 | 2 | 1 | 1 |
| Multicast | · | 1 | 0 | 0% | 2 | 0 | 1 | 0 | 0 | 0 |
| TGW Connect (SD-WAN/GRE) | · | 1 | 0 | 0% | 1 | 0 | 0 | 1 | 0 | 0 |
| Network Manager | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 0 |
| TGW peering (inter-Region) | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* ECMP (VPN bandwidth scaling), Appliance mode

### Global Accelerator
**Tier B** · Qs 27 (3.0%) · correct 7 (26%) · +expl 28 · U 9 / TD 9 / N 2 / F 7 · your misses 4

> Anycast static IPs over AWS backbone; TCP/UDP, fast regional failover

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Anycast / static IPs | ★ | 6 | 2 | 33% | 18 | 2 | 3 | 1 | 0 | 0 |
| Endpoint groups / traffic dial / weights | ★ | 4 | 1 | 25% | 5 | 0 | 3 | 0 | 1 | 1 |
| Custom routing accelerator | · | 2 | 1 | 50% | 3 | 1 | 1 | 0 | 0 | 1 |

### Lambda@Edge / CloudFront Functions
**Tier B** · Qs 18 (2.0%) · correct 11 (61%) · +expl 21 · U 2 / TD 10 / N 3 / F 3 · your misses 5

> Run code at edge: header rewrite, auth, A/B, URL redirect

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Lambda@Edge | ★★ | 14 | 8 | 57% | 19 | 2 | 7 | 3 | 2 | 4 |
| Viewer/origin request/response events | ★ | 6 | 3 | 50% | 14 | 0 | 5 | 1 | 0 | 0 |
| CloudFront Functions | ★ | 5 | 3 | 60% | 5 | 0 | 4 | 0 | 1 | 2 |

### VPC Flow Logs & network diagnostics
**Tier B** · Qs 18 (2.0%) · correct 6 (33%) · +expl 21 · U 10 / TD 5 / N 1 / F 2 · your misses 2

> Troubleshoot traffic (ACCEPT/REJECT), mirror packets, analyze paths

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| VPC Flow Logs | ★★ | 14 | 4 | 29% | 17 | 10 | 3 | 0 | 1 | 2 |
| Traffic Mirroring | ★ | 4 | 2 | 50% | 5 | 1 | 2 | 1 | 0 | 2 |
| Network Access Analyzer | · | 2 | 0 | 0% | 2 | 0 | 1 | 0 | 1 | 0 |

*Never mentioned:* Reachability Analyzer

### Route 53 Resolver (hybrid DNS)
**Tier C** · Qs 7 (0.8%) · correct 5 (71%) · +expl 13 · U 3 / TD 3 / N 1 / F 0 · your misses 3

> Inbound = on-prem resolves AWS; Outbound + rules = AWS resolves on-prem

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Forwarding rules / conditional forwarders | ★ | 7 | 4 | 57% | 11 | 2 | 1 | 3 | 1 | 1 |
| Inbound endpoint | ★ | 4 | 2 | 50% | 5 | 2 | 2 | 0 | 0 | 3 |
| On-prem DNS server | ★ | 3 | 3 | 100% | 11 | 1 | 0 | 2 | 0 | 1 |
| Outbound endpoint | ★ | 3 | 2 | 67% | 3 | 2 | 1 | 0 | 0 | 1 |
| Resolver DNS Firewall | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |
| Resolver query logging | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

### Network Firewall
**Tier D** · Qs 3 (0.3%) · correct 1 (33%) · +expl 4 · U 1 / TD 2 / N 0 / F 0 · your misses 1

> Managed stateful L3-L7 firewall; domain filtering; inspection VPC

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Inspection VPC / third-party appliances | ★ | 4 | 1 | 25% | 11 | 0 | 2 | 0 | 2 | 1 |
| Domain / FQDN filtering | ★ | 4 | 2 | 50% | 5 | 1 | 3 | 0 | 0 | 0 |
| Stateful / stateless rule groups | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

### Other networking (Lattice, Cloud Map, App Mesh)
**Tier D** · Qs 2 (0.2%) · correct 1 (50%) · +expl 2 · U 0 / TD 0 / N 1 / F 1 · your misses 0

> Service-to-service networking/discovery

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Cloud Map / service discovery | · | 1 | 1 | 100% | 1 | 0 | 0 | 1 | 0 | 0 |
| App Mesh / service mesh | · | 1 | 0 | 0% | 1 | 0 | 0 | 0 | 1 | 0 |

*Never mentioned:* VPC Lattice

## Compute & Containers

| Service | Tier | Qs | % of exam | Correct | Ans% | +Expl | Miss |
|---|---|---|---|---|---|---|---|
| EC2 | S | 419 | 47.3% | 158 | 38% | 489 | 44 |
| Lambda | S | 247 | 27.9% | 124 | 50% | 280 | 36 |
| EC2 Auto Scaling | S | 181 | 20.4% | 84 | 46% | 191 | 25 |
| ECS | A | 59 | 6.7% | 24 | 41% | 70 | 8 |
| Fargate | B | 36 | 4.1% | 15 | 42% | 50 | 15 |
| Elastic Beanstalk | B | 34 | 3.8% | 11 | 32% | 38 | 4 |
| EKS | B | 21 | 2.4% | 5 | 24% | 26 | 1 |
| Other compute (App Runner, Lightsail, Outposts, Local Zones, Wavelength) | B | 15 | 1.7% | 0 | 0% | 17 | 0 |
| SAM / Serverless Application Repository | C | 13 | 1.5% | 4 | 31% | 14 | 1 |
| ECR | C | 8 | 0.9% | 6 | 75% | 11 | 2 |
| AWS Batch | C | 8 | 0.9% | 2 | 25% | 12 | 1 |

### EC2
**Tier S** · Qs 419 (47.3%) · correct 158 (38%) · +expl 489 · U 65 / TD 214 / N 84 / F 56 · your misses 44

> Virtual servers; purchase options, placement, AMIs, recovery

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| AMI / golden image | ★★★ | 51 | 18 | 35% | 60 | 7 | 27 | 9 | 8 | 10 |
| Windows workloads | ★★★ | 34 | 10 | 29% | 56 | 5 | 20 | 6 | 3 | 15 |
| Instance types / families / Graviton | ★★ | 24 | 7 | 29% | 37 | 1 | 11 | 4 | 8 | 0 |
| User data / bootstrap | ★★ | 21 | 4 | 19% | 26 | 4 | 13 | 1 | 3 | 2 |
| EC2 Instance Connect / SSH keys | ★★ | 16 | 2 | 12% | 25 | 2 | 5 | 7 | 2 | 4 |
| Instance profile (role on EC2) | ★★ | 14 | 9 | 64% | 20 | 2 | 8 | 2 | 2 | 1 |
| Launch templates / configurations | ★★ | 12 | 4 | 33% | 15 | 2 | 6 | 1 | 3 | 1 |
| BYOL / licensing | ★ | 9 | 1 | 11% | 19 | 0 | 6 | 3 | 0 | 2 |
| Instance store (ephemeral) | ★ | 9 | 1 | 11% | 14 | 2 | 4 | 1 | 2 | 0 |
| HPC / tightly coupled | ★ | 8 | 2 | 25% | 10 | 1 | 4 | 3 | 0 | 1 |
| Enhanced networking / ENA / EFA | ★ | 7 | 4 | 57% | 7 | 0 | 4 | 3 | 0 | 1 |
| Placement groups (cluster/spread/partition) | ★ | 6 | 4 | 67% | 6 | 0 | 3 | 2 | 1 | 1 |
| On-Demand Capacity Reservations | ★ | 4 | 1 | 25% | 4 | 0 | 2 | 0 | 2 | 0 |
| Auto recovery / status checks | ★ | 4 | 2 | 50% | 4 | 2 | 1 | 0 | 1 | 0 |
| Dedicated Instances | · | 2 | 1 | 50% | 4 | 1 | 1 | 0 | 0 | 0 |
| Instance metadata (IMDS) | · | 2 | 1 | 50% | 3 | 0 | 2 | 0 | 0 | 0 |
| EC2 Image Builder | · | 2 | 0 | 0% | 2 | 0 | 1 | 0 | 1 | 1 |
| Nitro / Nitro Enclaves | · | 0 | 0 | – | 4 | 0 | 0 | 0 | 0 | 0 |
| Dedicated Hosts | · | 0 | 0 | – | 3 | 0 | 0 | 0 | 0 | 0 |
| Hibernation | · | 0 | 0 | – | 3 | 0 | 0 | 0 | 0 | 0 |
| Stop/start scheduling (Instance Scheduler) | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* VMware Cloud on AWS

### Lambda
**Tier S** · Qs 247 (27.9%) · correct 124 (50%) · +expl 280 · U 36 / TD 98 / N 68 / F 45 · your misses 36

> Serverless functions; 15-min limit; concurrency; event sources

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| 15-min timeout / long-running | ★★ | 14 | 1 | 7% | 35 | 1 | 8 | 3 | 2 | 6 |
| Concurrency (any) | ★★ | 14 | 4 | 29% | 18 | 3 | 8 | 1 | 2 | 2 |
| Container image Lambda | ★ | 6 | 3 | 50% | 12 | 0 | 2 | 1 | 3 | 0 |
| Memory / ephemeral /tmp | ★ | 6 | 0 | 0% | 8 | 0 | 5 | 1 | 0 | 2 |
| Environment variables | ★ | 6 | 4 | 67% | 7 | 0 | 4 | 1 | 1 | 0 |
| Provisioned concurrency | ★ | 6 | 0 | 0% | 6 | 0 | 5 | 0 | 1 | 0 |
| Lambda in VPC | ★ | 5 | 3 | 60% | 7 | 1 | 1 | 1 | 2 | 1 |
| Versions / aliases / weighted alias | ★ | 4 | 3 | 75% | 10 | 1 | 0 | 2 | 1 | 0 |
| Reserved concurrency | ★ | 4 | 2 | 50% | 4 | 0 | 3 | 1 | 0 | 1 |
| Destinations / DLQ (async failure) | ★ | 3 | 2 | 67% | 5 | 2 | 1 | 0 | 0 | 0 |
| Lambda layers | ★ | 3 | 1 | 33% | 3 | 1 | 1 | 0 | 1 | 0 |
| SnapStart | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 0 |
| Function URLs | · | 1 | 1 | 100% | 1 | 0 | 1 | 0 | 0 | 1 |
| Event source mapping | · | 0 | 0 | – | 3 | 0 | 0 | 0 | 0 | 0 |
| Cold start | · | 0 | 0 | – | 2 | 0 | 0 | 0 | 0 | 0 |

### EC2 Auto Scaling
**Tier S** · Qs 181 (20.4%) · correct 84 (46%) · +expl 191 · U 24 / TD 96 / N 37 / F 24 · your misses 25

> Scale EC2 fleet; policy types, lifecycle hooks, mixed instances

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Min/max/desired capacity | ★★ | 10 | 3 | 30% | 15 | 3 | 4 | 0 | 3 | 0 |
| Scheduled scaling | ★ | 7 | 2 | 29% | 8 | 2 | 3 | 1 | 1 | 2 |
| Lifecycle hooks | ★ | 6 | 3 | 50% | 6 | 1 | 2 | 1 | 2 | 1 |
| Application Auto Scaling (non-EC2) | ★ | 4 | 1 | 25% | 6 | 0 | 1 | 3 | 0 | 1 |
| Termination policy | ★ | 4 | 0 | 0% | 5 | 1 | 1 | 0 | 2 | 0 |
| Predictive scaling | ★ | 3 | 2 | 67% | 3 | 0 | 1 | 0 | 2 | 0 |
| Scale on SQS backlog | · | 2 | 2 | 100% | 6 | 1 | 1 | 0 | 0 | 1 |
| Warm pools | · | 1 | 1 | 100% | 3 | 0 | 0 | 0 | 1 | 0 |
| Step scaling | · | 1 | 0 | 0% | 2 | 0 | 0 | 1 | 0 | 1 |
| Cooldown | · | 1 | 0 | 0% | 2 | 1 | 0 | 0 | 0 | 0 |
| Target tracking scaling | · | 0 | 0 | – | 7 | 0 | 0 | 0 | 0 | 1 |
| Simple scaling | · | 0 | 0 | – | 2 | 0 | 0 | 0 | 0 | 0 |
| Instance refresh | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Mixed instances / multiple types, ELB health check on ASG / grace

### ECS
**Tier A** · Qs 59 (6.7%) · correct 24 (41%) · +expl 70 · U 7 / TD 23 / N 19 / F 10 · your misses 8

> AWS-native containers; tasks/services; EC2 or Fargate launch type

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Task definitions | ★ | 9 | 6 | 67% | 12 | 0 | 7 | 0 | 2 | 1 |
| ECS services | ★ | 8 | 2 | 25% | 11 | 0 | 2 | 3 | 3 | 1 |
| Launch type (EC2 vs Fargate) | ★ | 4 | 2 | 50% | 8 | 0 | 2 | 1 | 1 | 0 |
| Task role / execution role | ★ | 4 | 4 | 100% | 5 | 0 | 2 | 1 | 1 | 2 |
| awsvpc network mode | ★ | 4 | 2 | 50% | 5 | 0 | 2 | 2 | 0 | 0 |
| ECS service auto scaling | ★ | 4 | 2 | 50% | 4 | 0 | 1 | 3 | 0 | 0 |
| Capacity providers | · | 2 | 0 | 0% | 4 | 0 | 1 | 0 | 1 | 0 |
| ECS Anywhere | · | 2 | 1 | 50% | 2 | 0 | 2 | 0 | 0 | 0 |
| Service Connect | · | 1 | 0 | 0% | 2 | 0 | 1 | 0 | 0 | 0 |
| Container Insights | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 0 |

### Fargate
**Tier B** · Qs 36 (4.1%) · correct 15 (42%) · +expl 50 · U 3 / TD 20 / N 8 / F 5 · your misses 15

> Serverless containers; no instance management

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Fargate storage / EFS mount | · | 1 | 1 | 100% | 3 | 0 | 0 | 0 | 1 | 0 |

*Never mentioned:* Fargate Spot

### Elastic Beanstalk
**Tier B** · Qs 34 (3.8%) · correct 11 (32%) · +expl 38 · U 7 / TD 18 / N 4 / F 5 · your misses 4

> PaaS for web apps; deployment policies; least ops for simple apps

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Saved configurations / environments | ★★ | 10 | 4 | 40% | 12 | 4 | 3 | 2 | 1 | 0 |
| Rolling / rolling with additional batch | ★ | 4 | 0 | 0% | 8 | 1 | 2 | 1 | 0 | 0 |
| All at once | · | 2 | 0 | 0% | 8 | 0 | 2 | 0 | 0 | 1 |
| Immutable deployment | · | 2 | 1 | 50% | 8 | 0 | 2 | 0 | 0 | 2 |
| .ebextensions / config | · | 1 | 1 | 100% | 2 | 0 | 1 | 0 | 0 | 0 |
| Traffic splitting | · | 0 | 0 | – | 4 | 0 | 0 | 0 | 0 | 0 |
| Blue/green via swap CNAME/URL | · | 0 | 0 | – | 2 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Worker environment

### EKS
**Tier B** · Qs 21 (2.4%) · correct 5 (24%) · +expl 26 · U 0 / TD 14 / N 1 / F 6 · your misses 1

> Managed Kubernetes; node groups, Fargate profiles, IRSA

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Pods / kubectl / Helm | ★ | 7 | 0 | 0% | 17 | 0 | 4 | 1 | 2 | 1 |
| Managed node groups | ★ | 3 | 1 | 33% | 3 | 0 | 0 | 1 | 2 | 0 |
| EKS Anywhere / Distro | · | 2 | 0 | 0% | 2 | 0 | 2 | 0 | 0 | 0 |
| Karpenter / Cluster Autoscaler | · | 1 | 0 | 0% | 1 | 0 | 0 | 1 | 0 | 0 |
| IRSA / service accounts / Pod Identity | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Fargate profiles

### Other compute (App Runner, Lightsail, Outposts, Local Zones, Wavelength)
**Tier B** · Qs 15 (1.7%) · correct 0 (0%) · +expl 17 · U 2 / TD 12 / N 0 / F 1 · your misses 0

> Edge/simple compute options

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| App Runner | ★ | 5 | 0 | 0% | 6 | 0 | 4 | 0 | 1 | 0 |
| Outposts | ★ | 4 | 0 | 0% | 5 | 1 | 3 | 0 | 0 | 0 |
| Lightsail | ★ | 4 | 0 | 0% | 4 | 1 | 3 | 0 | 0 | 0 |
| Wavelength (5G) | · | 2 | 0 | 0% | 2 | 0 | 2 | 0 | 0 | 0 |

*Never mentioned:* Local Zones

### SAM / Serverless Application Repository
**Tier C** · Qs 13 (1.5%) · correct 4 (31%) · +expl 14 · U 1 / TD 8 / N 2 / F 2 · your misses 1

> IaC shorthand for serverless; gradual Lambda deploys via CodeDeploy

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Serverless Application Repository | · | 2 | 0 | 0% | 2 | 0 | 2 | 0 | 0 | 0 |
| SAM template / sam deploy | · | 1 | 0 | 0% | 3 | 0 | 1 | 0 | 0 | 0 |

### ECR
**Tier C** · Qs 8 (0.9%) · correct 6 (75%) · +expl 11 · U 0 / TD 5 / N 1 / F 2 · your misses 2

> Container registry; scan, replicate, lifecycle

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| ECR lifecycle policies | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Image scanning, ECR replication

### AWS Batch
**Tier C** · Qs 8 (0.9%) · correct 2 (25%) · +expl 12 · U 2 / TD 6 / N 0 / F 0 · your misses 1

> Managed batch jobs on EC2/Spot/Fargate

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Job queues / compute environments | · | 2 | 1 | 50% | 7 | 0 | 2 | 0 | 0 | 0 |

*Never mentioned:* Array jobs

## Storage

| Service | Tier | Qs | % of exam | Correct | Ans% | +Expl | Miss |
|---|---|---|---|---|---|---|---|
| S3 | S | 356 | 40.2% | 210 | 59% | 415 | 62 |
| EFS | A | 58 | 6.5% | 19 | 33% | 64 | 8 |
| EBS | A | 57 | 6.4% | 10 | 18% | 72 | 5 |
| Storage Gateway | B | 33 | 3.7% | 12 | 36% | 33 | 7 |
| FSx | B | 18 | 2.0% | 11 | 61% | 24 | 5 |
| AWS Backup | C | 13 | 1.5% | 4 | 31% | 14 | 0 |

### S3
**Tier S** · Qs 356 (40.2%) · correct 210 (59%) · +expl 415 · U 78 / TD 175 / N 55 / F 48 · your misses 62

> Object storage; classes, lifecycle, security, replication, events

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Static website hosting | ★★★ | 35 | 13 | 37% | 46 | 3 | 22 | 8 | 2 | 5 |
| Replication (CRR/SRR/RTC) | ★★★ | 35 | 14 | 40% | 45 | 6 | 17 | 7 | 5 | 5 |
| Bucket policy | ★★ | 29 | 16 | 55% | 35 | 8 | 12 | 8 | 1 | 8 |
| Lifecycle policies / transitions | ★★ | 23 | 15 | 65% | 30 | 5 | 10 | 3 | 5 | 1 |
| Transfer Acceleration | ★★ | 22 | 9 | 41% | 22 | 9 | 5 | 5 | 3 | 3 |
| Glacier Flexible Retrieval | ★★ | 21 | 12 | 57% | 32 | 6 | 13 | 2 | 0 | 4 |
| Versioning | ★★ | 17 | 2 | 12% | 23 | 2 | 7 | 5 | 3 | 3 |
| Event notifications | ★★ | 14 | 7 | 50% | 18 | 4 | 5 | 3 | 2 | 0 |
| S3 Standard | ★★ | 13 | 5 | 38% | 13 | 6 | 3 | 1 | 3 | 0 |
| SSE-S3 / SSE-KMS / SSE-C / DSSE | ★★ | 12 | 7 | 58% | 16 | 2 | 6 | 3 | 1 | 4 |
| Data lake on S3 | ★★ | 11 | 1 | 9% | 20 | 5 | 5 | 0 | 1 | 1 |
| Glacier Deep Archive | ★★ | 10 | 5 | 50% | 13 | 5 | 2 | 0 | 3 | 1 |
| Multipart upload | ★ | 7 | 5 | 71% | 8 | 2 | 2 | 2 | 1 | 1 |
| Intelligent-Tiering | ★ | 7 | 3 | 43% | 7 | 2 | 3 | 0 | 2 | 2 |
| Access Points | ★ | 6 | 2 | 33% | 9 | 1 | 5 | 0 | 0 | 1 |
| Presigned URLs | ★ | 6 | 4 | 67% | 7 | 0 | 5 | 1 | 0 | 2 |
| S3 ACLs | ★ | 5 | 1 | 20% | 7 | 1 | 2 | 1 | 1 | 0 |
| S3 Select / Glacier Select | ★ | 5 | 2 | 40% | 6 | 2 | 0 | 1 | 2 | 0 |
| Standard-IA | ★ | 4 | 0 | 0% | 10 | 3 | 1 | 0 | 0 | 0 |
| Glacier Instant Retrieval | ★ | 4 | 2 | 50% | 4 | 2 | 2 | 0 | 0 | 1 |
| MFA Delete | ★ | 4 | 2 | 50% | 4 | 1 | 1 | 1 | 1 | 1 |
| Object Lock (WORM, governance/compliance, legal hold) | ★ | 3 | 0 | 0% | 13 | 0 | 2 | 1 | 0 | 0 |
| Client-side encryption | ★ | 3 | 0 | 0% | 3 | 1 | 2 | 0 | 0 | 1 |
| Block Public Access | · | 2 | 2 | 100% | 5 | 0 | 1 | 1 | 0 | 2 |
| Object Ownership / bucket-owner-full-control | · | 2 | 1 | 50% | 3 | 1 | 0 | 1 | 0 | 1 |
| Requester Pays | · | 2 | 1 | 50% | 3 | 1 | 1 | 0 | 0 | 1 |
| Batch Operations | · | 2 | 1 | 50% | 3 | 0 | 0 | 1 | 1 | 0 |
| CORS | · | 2 | 0 | 0% | 3 | 0 | 1 | 0 | 1 | 1 |
| One Zone-IA | · | 2 | 0 | 0% | 2 | 2 | 0 | 0 | 0 | 0 |
| Glacier retrieval (Expedited/Standard/Bulk) | · | 1 | 0 | 0% | 8 | 0 | 1 | 0 | 0 | 1 |
| Byte-range fetch | · | 1 | 0 | 0% | 2 | 0 | 0 | 1 | 0 | 0 |
| Storage Lens / Inventory / Storage Class Analysis | · | 1 | 1 | 100% | 2 | 0 | 1 | 0 | 0 | 0 |
| Glacier Vault Lock | · | 1 | 1 | 100% | 1 | 1 | 0 | 0 | 0 | 0 |
| Multi-Region Access Points | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 0 |
| Bucket Keys | · | 0 | 0 | – | 3 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Express One Zone / directory bucket, S3 Object Lambda

### EFS
**Tier A** · Qs 58 (6.5%) · correct 19 (33%) · +expl 64 · U 11 / TD 24 / N 13 / F 10 · your misses 8

> Shared NFS for Linux; multi-AZ; scales automatically

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| NFS | ★ | 9 | 2 | 22% | 27 | 1 | 3 | 3 | 2 | 1 |
| Throughput mode (Bursting/Provisioned/Elastic) | ★ | 3 | 2 | 67% | 8 | 0 | 2 | 1 | 0 | 1 |
| Performance mode (General Purpose/Max I/O) | · | 2 | 0 | 0% | 4 | 0 | 1 | 1 | 0 | 1 |
| Mount targets | · | 1 | 1 | 100% | 1 | 0 | 0 | 0 | 1 | 0 |
| EFS replication | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* EFS IA / One Zone / lifecycle, EFS access points

### EBS
**Tier A** · Qs 57 (6.4%) · correct 10 (18%) · +expl 72 · U 8 / TD 37 / N 7 / F 5 · your misses 5

> Block volumes for EC2; types, snapshots, encryption

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| IOPS (any) | ★★ | 14 | 1 | 7% | 20 | 3 | 8 | 2 | 1 | 3 |
| io1/io2 (Provisioned IOPS) | ★★ | 11 | 0 | 0% | 13 | 3 | 7 | 1 | 0 | 2 |
| EBS snapshots | ★★ | 10 | 4 | 40% | 14 | 0 | 7 | 2 | 1 | 1 |
| gp2/gp3 (General Purpose SSD) | ★★ | 10 | 2 | 20% | 10 | 2 | 3 | 4 | 1 | 1 |
| EBS encryption / encrypt unencrypted vol | ★ | 6 | 4 | 67% | 11 | 0 | 2 | 4 | 0 | 0 |
| Data Lifecycle Manager | ★ | 6 | 3 | 50% | 6 | 0 | 4 | 1 | 1 | 2 |
| Multi-Attach | ★ | 5 | 0 | 0% | 8 | 0 | 3 | 0 | 2 | 0 |
| st1/sc1 (HDD) | ★ | 4 | 1 | 25% | 5 | 0 | 3 | 1 | 0 | 1 |
| RAID | ★ | 4 | 0 | 0% | 4 | 1 | 3 | 0 | 0 | 0 |

*Never mentioned:* Fast Snapshot Restore, Recycle Bin, Elastic Volumes (modify live)

### Storage Gateway
**Tier B** · Qs 33 (3.7%) · correct 12 (36%) · +expl 33 · U 9 / TD 15 / N 4 / F 5 · your misses 7

> Hybrid on-prem access to S3/FSx/tapes

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| S3 File Gateway (NFS/SMB to S3) | ★★ | 20 | 4 | 20% | 22 | 7 | 8 | 2 | 3 | 5 |
| iSCSI | ★ | 6 | 1 | 17% | 9 | 0 | 5 | 0 | 1 | 1 |
| Tape Gateway / VTL | ★ | 5 | 1 | 20% | 10 | 0 | 4 | 0 | 1 | 1 |
| Volume Gateway stored | ★ | 5 | 0 | 0% | 7 | 1 | 4 | 0 | 0 | 1 |
| Volume Gateway cached | · | 2 | 2 | 100% | 4 | 1 | 1 | 0 | 0 | 1 |
| FSx File Gateway | · | 1 | 0 | 0% | 1 | 0 | 0 | 0 | 1 | 0 |
| RefreshCache | · | 1 | 1 | 100% | 1 | 1 | 0 | 0 | 0 | 0 |

### FSx
**Tier B** · Qs 18 (2.0%) · correct 11 (61%) · +expl 24 · U 3 / TD 7 / N 3 / F 5 · your misses 5

> Managed Windows SMB / Lustre HPC / NetApp ONTAP / OpenZFS

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| FSx for Windows File Server | ★★ | 12 | 6 | 50% | 15 | 3 | 5 | 2 | 2 | 3 |
| SMB / CIFS | ★ | 6 | 0 | 0% | 18 | 0 | 4 | 1 | 1 | 1 |
| FSx for Lustre | ★ | 6 | 3 | 50% | 6 | 0 | 3 | 1 | 2 | 1 |
| Multi-AZ FSx | · | 2 | 2 | 100% | 3 | 2 | 0 | 0 | 0 | 0 |
| DFS Namespaces / DFS-R | · | 1 | 0 | 0% | 5 | 0 | 1 | 0 | 0 | 0 |
| FSx for NetApp ONTAP | · | 0 | 0 | – | 2 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* FSx for OpenZFS

### AWS Backup
**Tier C** · Qs 13 (1.5%) · correct 4 (31%) · +expl 14 · U 0 / TD 6 / N 1 / F 6 · your misses 0

> Central backup policy across services/accounts

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Backup plans / rules | ★ | 4 | 2 | 50% | 5 | 0 | 3 | 0 | 1 | 0 |
| Cross-Region / cross-account copy | · | 2 | 1 | 50% | 3 | 0 | 1 | 0 | 1 | 2 |
| Org backup policies | · | 1 | 0 | 0% | 3 | 1 | 0 | 0 | 0 | 0 |

*Never mentioned:* Backup vaults / Vault Lock, Backup Audit Manager

## Databases

| Service | Tier | Qs | % of exam | Correct | Ans% | +Expl | Miss |
|---|---|---|---|---|---|---|---|
| RDS | S | 163 | 18.4% | 64 | 39% | 183 | 20 |
| DynamoDB | S | 108 | 12.2% | 56 | 52% | 131 | 17 |
| Aurora | A | 75 | 8.5% | 45 | 60% | 93 | 19 |
| Redshift | A | 40 | 4.5% | 18 | 45% | 59 | 10 |
| ElastiCache | B | 36 | 4.1% | 13 | 36% | 38 | 11 |
| Other databases (Neptune, DocumentDB, Keyspaces, Timestream, QLDB, MemoryDB) | B | 21 | 2.4% | 5 | 24% | 28 | 2 |
| OpenSearch | B | 18 | 2.0% | 10 | 56% | 28 | 3 |

### RDS
**Tier S** · Qs 163 (18.4%) · correct 64 (39%) · +expl 183 · U 22 / TD 86 / N 32 / F 23 · your misses 20

> Managed relational DB; Multi-AZ HA, read replicas, backups

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Engine: MySQL | ★★★ | 96 | 38 | 40% | 106 | 14 | 44 | 23 | 15 | 10 |
| Multi-AZ (any) | ★★★ | 62 | 25 | 40% | 71 | 11 | 36 | 9 | 6 | 15 |
| Read replicas | ★★★ | 62 | 30 | 48% | 66 | 9 | 32 | 10 | 11 | 12 |
| Engine: PostgreSQL | ★★ | 25 | 5 | 20% | 43 | 4 | 11 | 4 | 6 | 1 |
| Engine: Oracle | ★★ | 18 | 4 | 22% | 30 | 2 | 12 | 2 | 2 | 4 |
| Cross-Region read replica | ★★ | 16 | 8 | 50% | 20 | 3 | 6 | 5 | 2 | 4 |
| Automated backups / PITR | ★★ | 13 | 3 | 23% | 18 | 2 | 5 | 2 | 4 | 0 |
| Engine: SQL Server | ★★ | 11 | 3 | 27% | 26 | 1 | 6 | 0 | 4 | 0 |
| RDS Proxy | ★★ | 10 | 9 | 90% | 10 | 0 | 5 | 1 | 4 | 3 |
| RDS Blue/Green Deployments | ★ | 9 | 8 | 89% | 13 | 0 | 3 | 6 | 0 | 0 |
| DB snapshots | ★ | 6 | 1 | 17% | 11 | 1 | 2 | 2 | 1 | 0 |
| Connection limits / pooling | ★ | 5 | 2 | 40% | 9 | 0 | 3 | 1 | 1 | 0 |
| Engine: MariaDB | · | 2 | 0 | 0% | 14 | 0 | 1 | 0 | 1 | 0 |
| Encryption at rest / TDE | · | 2 | 2 | 100% | 3 | 0 | 0 | 2 | 0 | 0 |
| Storage autoscaling | · | 2 | 0 | 0% | 2 | 0 | 1 | 1 | 0 | 0 |
| IAM DB authentication | · | 0 | 0 | – | 3 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Performance Insights / Enhanced Monitoring, RDS Custom, Parameter / option groups

### DynamoDB
**Tier S** · Qs 108 (12.2%) · correct 56 (52%) · +expl 131 · U 14 / TD 60 / N 26 / F 8 · your misses 17

> Serverless NoSQL; keys, capacity, streams, global tables

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Global Tables | ★★ | 21 | 11 | 52% | 23 | 2 | 6 | 8 | 5 | 0 |
| On-demand vs provisioned / RCU/WCU | ★★ | 16 | 8 | 50% | 26 | 1 | 8 | 5 | 2 | 2 |
| DynamoDB Streams | ★ | 8 | 4 | 50% | 10 | 2 | 2 | 3 | 1 | 0 |
| DAX | ★ | 8 | 4 | 50% | 8 | 3 | 1 | 3 | 1 | 1 |
| TTL | ★ | 6 | 4 | 67% | 12 | 1 | 3 | 2 | 0 | 2 |
| DynamoDB auto scaling | ★ | 5 | 2 | 40% | 6 | 0 | 2 | 3 | 0 | 1 |
| Partition / sort key | ★ | 3 | 3 | 100% | 8 | 1 | 1 | 0 | 1 | 1 |
| PITR / on-demand backup | · | 1 | 1 | 100% | 3 | 0 | 1 | 0 | 0 | 0 |
| Fine-grained access (LeadingKeys) | · | 1 | 1 | 100% | 2 | 0 | 1 | 0 | 0 | 0 |
| Transactions | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 0 |
| Export to S3 | · | 1 | 0 | 0% | 1 | 1 | 0 | 0 | 0 | 1 |
| GSI / LSI | · | 0 | 0 | – | 3 | 0 | 0 | 0 | 0 | 0 |
| Item size 400KB | · | 0 | 0 | – | 3 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Hot partition, Conditional writes / optimistic locking

### Aurora
**Tier A** · Qs 75 (8.5%) · correct 45 (60%) · +expl 93 · U 10 / TD 33 / N 19 / F 13 · your misses 19

> Cloud-native MySQL/Postgres; 6 copies/3 AZ, fast replicas, Global DB

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Aurora Global Database | ★★ | 13 | 7 | 54% | 14 | 2 | 5 | 4 | 2 | 2 |
| Aurora Replicas | ★★ | 12 | 10 | 83% | 17 | 1 | 5 | 3 | 3 | 4 |
| Aurora Serverless (v1/v2) | ★★ | 12 | 3 | 25% | 13 | 1 | 6 | 2 | 3 | 1 |
| Reader / custom / cluster endpoints | ★ | 5 | 3 | 60% | 5 | 0 | 2 | 1 | 2 | 2 |
| Aurora Auto Scaling (replicas) | ★ | 5 | 4 | 80% | 5 | 1 | 2 | 1 | 1 | 1 |
| Cloning | ★ | 4 | 3 | 75% | 4 | 1 | 1 | 1 | 1 | 1 |
| Multi-master | · | 2 | 0 | 0% | 7 | 0 | 0 | 2 | 0 | 0 |
| Data API | · | 2 | 0 | 0% | 2 | 1 | 1 | 0 | 0 | 0 |
| Database Activity Streams | · | 1 | 1 | 100% | 1 | 0 | 0 | 0 | 1 | 0 |

*Never mentioned:* Backtrack, Babelfish, Write forwarding, I/O-Optimized

### Redshift
**Tier A** · Qs 40 (4.5%) · correct 18 (45%) · +expl 59 · U 11 / TD 18 / N 7 / F 4 · your misses 10

> Data warehouse; Spectrum, concurrency scaling, RA3

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Redshift Spectrum | ★ | 9 | 2 | 22% | 9 | 3 | 3 | 2 | 1 | 2 |
| Snapshots / cross-Region | ★ | 7 | 4 | 57% | 7 | 2 | 3 | 2 | 0 | 3 |
| COPY / UNLOAD | ★ | 4 | 0 | 0% | 5 | 2 | 0 | 1 | 1 | 1 |
| Data sharing | · | 1 | 0 | 0% | 3 | 1 | 0 | 0 | 0 | 0 |
| Concurrency Scaling | · | 1 | 1 | 100% | 1 | 0 | 1 | 0 | 0 | 0 |
| Redshift Serverless | · | 1 | 1 | 100% | 1 | 0 | 1 | 0 | 0 | 1 |
| RA3 / managed storage | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* WLM (workload management), Distribution / sort keys, Federated query, Materialized views, Enhanced VPC Routing

### ElastiCache
**Tier B** · Qs 36 (4.1%) · correct 13 (36%) · +expl 38 · U 4 / TD 20 / N 8 / F 4 · your misses 11

> In-memory cache/session store; Redis features vs Memcached

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Redis | ★★ | 13 | 5 | 38% | 15 | 3 | 5 | 3 | 2 | 1 |
| Session store | ★ | 5 | 2 | 40% | 11 | 1 | 3 | 1 | 0 | 0 |
| Memcached | ★ | 5 | 0 | 0% | 7 | 1 | 2 | 1 | 1 | 0 |
| Sorted sets / leaderboard | ★ | 3 | 1 | 33% | 4 | 2 | 1 | 0 | 0 | 0 |
| Redis AUTH / encryption | · | 1 | 0 | 0% | 2 | 0 | 0 | 0 | 1 | 0 |
| Cluster mode | · | 1 | 0 | 0% | 1 | 1 | 0 | 0 | 0 | 0 |
| Lazy loading / write-through | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Global Datastore

### Other databases (Neptune, DocumentDB, Keyspaces, Timestream, QLDB, MemoryDB)
**Tier B** · Qs 21 (2.4%) · correct 5 (24%) · +expl 28 · U 3 / TD 13 / N 3 / F 2 · your misses 2

> Purpose-built DBs: graph, Mongo, Cassandra, time-series, ledger

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Neptune (graph) | ★ | 9 | 3 | 33% | 9 | 3 | 3 | 1 | 2 | 1 |
| DocumentDB (MongoDB) | ★ | 8 | 1 | 12% | 13 | 1 | 5 | 2 | 0 | 0 |
| Timestream (time series) | ★ | 3 | 0 | 0% | 4 | 0 | 3 | 0 | 0 | 1 |
| Keyspaces (Cassandra) | · | 2 | 0 | 0% | 3 | 0 | 2 | 0 | 0 | 0 |
| MemoryDB | · | 1 | 1 | 100% | 1 | 0 | 1 | 0 | 0 | 1 |
| QLDB (ledger) | · | 0 | 0 | – | 2 | 0 | 0 | 0 | 0 | 0 |

### OpenSearch
**Tier B** · Qs 18 (2.0%) · correct 10 (56%) · +expl 28 · U 2 / TD 11 / N 2 / F 3 · your misses 3

> Search/log analytics; ELK replacement

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| OpenSearch Dashboards / Kibana | ★ | 6 | 3 | 50% | 6 | 1 | 3 | 1 | 1 | 0 |
| Full-text search | · | 2 | 0 | 0% | 6 | 0 | 2 | 0 | 0 | 0 |
| UltraWarm / cold storage | · | 2 | 2 | 100% | 3 | 0 | 1 | 0 | 1 | 1 |

## Migration & Transfer

| Service | Tier | Qs | % of exam | Correct | Ans% | +Expl | Miss |
|---|---|---|---|---|---|---|---|
| Migration strategy (7 Rs) | B | 33 | 3.7% | 9 | 27% | 51 | 4 |
| DMS | B | 30 | 3.4% | 15 | 50% | 32 | 4 |
| Application Migration Service (MGN) | B | 24 | 2.7% | 8 | 33% | 26 | 2 |
| DataSync | B | 22 | 2.5% | 10 | 45% | 22 | 2 |
| Server Migration Service / VM Import (legacy) | B | 18 | 2.0% | 6 | 33% | 19 | 5 |
| Snow Family | B | 16 | 1.8% | 8 | 50% | 18 | 6 |
| Application Discovery Service | B | 15 | 1.7% | 8 | 53% | 16 | 1 |
| Schema Conversion Tool (SCT) | C | 12 | 1.4% | 8 | 67% | 13 | 2 |
| Migration Hub | C | 9 | 1.0% | 5 | 56% | 10 | 0 |
| Transfer Family | C | 9 | 1.0% | 5 | 56% | 9 | 1 |
| Migration Evaluator | D | 3 | 0.3% | 2 | 67% | 4 | 1 |
| Elastic Disaster Recovery (DRS) | D | 3 | 0.3% | 2 | 67% | 3 | 0 |

### Migration strategy (7 Rs)
**Tier B** · Qs 33 (3.7%) · correct 9 (27%) · +expl 51 · U 8 / TD 11 / N 10 / F 4 · your misses 4

> Pick rehost/replatform/refactor/... from the business constraint

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Refactor / re-architect | ★★ | 27 | 6 | 22% | 32 | 5 | 9 | 9 | 4 | 2 |
| Rehost / lift-and-shift | ★ | 6 | 0 | 0% | 24 | 2 | 2 | 2 | 0 | 2 |
| Replatform | ★ | 5 | 3 | 60% | 8 | 2 | 2 | 1 | 0 | 2 |
| Repurchase (SaaS) | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 0 |
| Retire / retain | · | 0 | 0 | – | 4 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Relocate (VMware), Migration Acceleration Program (MAP), Mainframe Modernization

### DMS
**Tier B** · Qs 30 (3.4%) · correct 15 (50%) · +expl 32 · U 5 / TD 10 / N 7 / F 8 · your misses 4

> Migrate/replicate DBs; full load + CDC; heterogeneous with SCT

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Full load + CDC / ongoing replication | ★ | 5 | 1 | 20% | 11 | 0 | 2 | 0 | 3 | 1 |
| Heterogeneous vs homogeneous | ★ | 3 | 0 | 0% | 7 | 0 | 2 | 0 | 1 | 0 |
| Replication instance / task | ★ | 3 | 3 | 100% | 5 | 1 | 1 | 1 | 0 | 0 |
| Data validation | · | 2 | 1 | 50% | 3 | 1 | 0 | 0 | 1 | 0 |

*Never mentioned:* DMS Serverless, Fleet Advisor

### Application Migration Service (MGN)
**Tier B** · Qs 24 (2.7%) · correct 8 (33%) · +expl 26 · U 2 / TD 14 / N 2 / F 6 · your misses 2

> Rehost servers via continuous block-level replication; test then cutover

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Test launch / cutover | ★ | 7 | 4 | 57% | 14 | 1 | 4 | 0 | 2 | 2 |
| Replication agent | ★ | 4 | 3 | 75% | 4 | 0 | 4 | 0 | 0 | 2 |
| Block-level replication | · | 1 | 0 | 0% | 7 | 0 | 1 | 0 | 0 | 1 |

### DataSync
**Tier B** · Qs 22 (2.5%) · correct 10 (45%) · +expl 22 · U 7 / TD 9 / N 3 / F 3 · your misses 2

> Online file transfer NFS/SMB/HDFS to S3/EFS/FSx; scheduled, verified

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| DataSync agent | ★★ | 11 | 6 | 55% | 14 | 1 | 6 | 2 | 2 | 0 |
| Scheduled / incremental tasks | · | 2 | 2 | 100% | 2 | 1 | 0 | 1 | 0 | 1 |

*Never mentioned:* Bandwidth throttle

### Server Migration Service / VM Import (legacy)
**Tier B** · Qs 18 (2.0%) · correct 6 (33%) · +expl 19 · U 3 / TD 7 / N 5 / F 3 · your misses 5

> Older VM migration paths; usually distractor now

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| VM Import/Export | ★★ | 13 | 6 | 46% | 15 | 2 | 7 | 2 | 2 | 5 |
| Server Migration Service (SMS) | ★ | 7 | 0 | 0% | 7 | 3 | 0 | 3 | 1 | 0 |

### Snow Family
**Tier B** · Qs 16 (1.8%) · correct 8 (50%) · +expl 18 · U 7 / TD 0 / N 6 / F 3 · your misses 6

> Offline bulk transfer when network too slow; edge compute

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Data volume stated in TB/PB (do bandwidth math) | ★★★ | 40 | 1 | 2% | 43 | 8 | 19 | 10 | 3 | 9 |
| Snowball (any) | ★★ | 15 | 7 | 47% | 15 | 7 | 0 | 6 | 2 | 6 |
| Snowball Edge Storage Optimized | ★ | 6 | 2 | 33% | 9 | 3 | 1 | 0 | 2 | 1 |
| Snowcone | · | 1 | 1 | 100% | 4 | 0 | 0 | 0 | 1 | 0 |
| Snowmobile (100 PB) | · | 1 | 0 | 0% | 1 | 1 | 0 | 0 | 0 | 1 |
| Snowball Edge Compute Optimized | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* OpsHub

### Application Discovery Service
**Tier B** · Qs 15 (1.7%) · correct 8 (53%) · +expl 16 · U 1 / TD 4 / N 4 / F 6 · your misses 1

> Collect on-prem inventory/utilization/dependencies before migrating

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Agentless Discovery Connector (VMware vCenter) | ★ | 8 | 3 | 38% | 15 | 0 | 3 | 3 | 2 | 0 |
| Discovery Agent (per server, processes/network) | ★ | 6 | 3 | 50% | 7 | 0 | 1 | 1 | 4 | 0 |
| Data exploration in Athena | ★ | 3 | 3 | 100% | 3 | 0 | 1 | 0 | 2 | 0 |
| Server dependencies / network connections | · | 2 | 2 | 100% | 8 | 0 | 1 | 0 | 1 | 0 |

*Never mentioned:* Import template / bulk import

### Schema Conversion Tool (SCT)
**Tier C** · Qs 12 (1.4%) · correct 8 (67%) · +expl 13 · U 1 / TD 7 / N 1 / F 3 · your misses 2

> Convert schema/code between engines; data extraction agents for warehouses

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Assessment report | · | 1 | 1 | 100% | 2 | 0 | 1 | 0 | 0 | 0 |
| Data extraction agents | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

### Migration Hub
**Tier C** · Qs 9 (1.0%) · correct 5 (56%) · +expl 10 · U 2 / TD 1 / N 1 / F 5 · your misses 0

> Single place to track migrations + strategy recommendations

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Home Region | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Strategy Recommendations, Refactor Spaces, Orchestrator

### Transfer Family
**Tier C** · Qs 9 (1.0%) · correct 5 (56%) · +expl 9 · U 2 / TD 5 / N 0 / F 2 · your misses 1

> Managed SFTP/FTPS/FTP/AS2 into S3/EFS

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| SFTP | ★ | 6 | 3 | 50% | 6 | 0 | 4 | 0 | 2 | 1 |
| FTP/FTPS | · | 1 | 1 | 100% | 4 | 1 | 0 | 0 | 0 | 0 |

*Never mentioned:* AS2

### Migration Evaluator
**Tier D** · Qs 3 (0.3%) · correct 2 (67%) · +expl 4 · U 0 / TD 1 / N 0 / F 2 · your misses 1

> Business case / TCO for migration

### Elastic Disaster Recovery (DRS)
**Tier D** · Qs 3 (0.3%) · correct 2 (67%) · +expl 3 · U 0 / TD 1 / N 0 / F 2 · your misses 0

> Continuous replication to low-cost staging for DR (seconds RPO, minutes RTO)

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Staging area / failback | · | 0 | 0 | – | 3 | 0 | 0 | 0 | 0 | 0 |

## Application Integration

| Service | Tier | Qs | % of exam | Correct | Ans% | +Expl | Miss |
|---|---|---|---|---|---|---|---|
| API Gateway | A | 73 | 8.2% | 30 | 41% | 84 | 13 |
| SQS | A | 66 | 7.4% | 37 | 56% | 68 | 15 |
| SNS | A | 61 | 6.9% | 33 | 54% | 70 | 7 |
| EventBridge | A | 58 | 6.5% | 24 | 41% | 61 | 5 |
| Step Functions | B | 20 | 2.3% | 8 | 40% | 21 | 5 |
| Other integration (SES, AppFlow, SWF, MSK) | C | 14 | 1.6% | 3 | 21% | 15 | 1 |
| AppSync | C | 12 | 1.4% | 3 | 25% | 15 | 1 |
| Amazon MQ | C | 11 | 1.2% | 2 | 18% | 11 | 1 |

### API Gateway
**Tier A** · Qs 73 (8.2%) · correct 30 (41%) · +expl 84 · U 13 / TD 25 / N 21 / F 14 · your misses 13

> Front door for APIs; throttling, auth, caching, private APIs

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| REST API | ★★ | 21 | 7 | 33% | 31 | 2 | 6 | 10 | 3 | 3 |
| Endpoint type: edge-optimized / regional / private | ★★ | 13 | 4 | 31% | 15 | 2 | 6 | 3 | 2 | 1 |
| Throttling | ★★ | 10 | 5 | 50% | 23 | 2 | 3 | 4 | 1 | 3 |
| Authorizers (Lambda/Cognito/IAM) | ★★ | 10 | 1 | 10% | 14 | 0 | 3 | 3 | 4 | 3 |
| Usage plans / API keys | ★ | 7 | 2 | 29% | 12 | 1 | 3 | 2 | 1 | 1 |
| Custom domain | ★ | 7 | 3 | 43% | 12 | 1 | 5 | 1 | 0 | 3 |
| WebSocket API | ★ | 7 | 4 | 57% | 11 | 1 | 4 | 2 | 0 | 1 |
| API caching | ★ | 5 | 3 | 60% | 6 | 0 | 3 | 2 | 0 | 1 |
| Stages / canary release | ★ | 4 | 1 | 25% | 6 | 0 | 0 | 3 | 1 | 0 |
| HTTP API | ★ | 4 | 2 | 50% | 5 | 0 | 1 | 1 | 2 | 1 |
| Mutual TLS | ★ | 3 | 0 | 0% | 3 | 0 | 1 | 0 | 2 | 0 |
| Mapping templates / VTL | · | 1 | 0 | 0% | 2 | 0 | 1 | 0 | 0 | 0 |
| Resource policies | · | 1 | 1 | 100% | 1 | 0 | 0 | 1 | 0 | 0 |

*Never mentioned:* VPC Link

### SQS
**Tier A** · Qs 66 (7.4%) · correct 37 (56%) · +expl 68 · U 12 / TD 33 / N 15 / F 6 · your misses 15

> Decouple + buffer; standard vs FIFO; DLQ; visibility timeout

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| FIFO queue | ★ | 7 | 3 | 43% | 11 | 3 | 1 | 3 | 0 | 1 |
| Exactly-once / ordering | ★ | 5 | 0 | 0% | 15 | 4 | 0 | 1 | 0 | 1 |
| Visibility timeout | ★ | 3 | 0 | 0% | 6 | 2 | 1 | 0 | 0 | 0 |
| Dead-letter queue / redrive | ★ | 3 | 2 | 67% | 5 | 2 | 1 | 0 | 0 | 1 |
| Delay queue | · | 1 | 0 | 0% | 2 | 1 | 0 | 0 | 0 | 1 |
| Long polling | · | 1 | 0 | 0% | 1 | 1 | 0 | 0 | 0 | 0 |
| Message group ID / dedup | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* 256 KB / Extended Client (S3)

### SNS
**Tier A** · Qs 61 (6.9%) · correct 33 (54%) · +expl 70 · U 12 / TD 29 / N 9 / F 11 · your misses 7

> Pub/sub fan-out; filter policies; SMS/email/mobile push

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Email / SMS / mobile push | ★★ | 14 | 4 | 29% | 17 | 4 | 4 | 5 | 1 | 1 |
| Fan-out (SNS to SQS) | · | 1 | 1 | 100% | 2 | 1 | 0 | 0 | 0 | 2 |

*Never mentioned:* Message filtering / filter policy, SNS FIFO topic

### EventBridge
**Tier A** · Qs 58 (6.5%) · correct 24 (41%) · +expl 61 · U 9 / TD 22 / N 17 / F 10 · your misses 5

> Event bus + rules; scheduler; cross-account events; SaaS

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Rules / event patterns | ★★ | 28 | 16 | 57% | 31 | 3 | 8 | 10 | 7 | 1 |
| Scheduler / cron / rate | ★★ | 19 | 4 | 21% | 19 | 5 | 7 | 5 | 2 | 1 |
| Event bus / cross-account | · | 0 | 0 | – | 3 | 0 | 0 | 0 | 0 | 0 |
| SaaS partner events | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Pipes, Archive / replay

### Step Functions
**Tier B** · Qs 20 (2.3%) · correct 8 (40%) · +expl 21 · U 3 / TD 10 / N 2 / F 5 · your misses 5

> Orchestrate workflows; retries, human approval, Map

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Task token / wait for callback | · | 2 | 2 | 100% | 2 | 0 | 1 | 1 | 0 | 0 |
| Human / manual approval | · | 2 | 2 | 100% | 2 | 0 | 1 | 0 | 1 | 0 |
| Retry / Catch | · | 2 | 1 | 50% | 2 | 0 | 2 | 0 | 0 | 0 |

*Never mentioned:* Standard vs Express workflows, Map state / Distributed Map

### Other integration (SES, AppFlow, SWF, MSK)
**Tier C** · Qs 14 (1.6%) · correct 3 (21%) · +expl 15 · U 0 / TD 9 / N 3 / F 2 · your misses 1

> Email, SaaS data flows, legacy workflow, Kafka

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| SES | ★ | 8 | 1 | 12% | 8 | 0 | 4 | 2 | 2 | 1 |
| MSK / Kafka | ★ | 5 | 2 | 40% | 6 | 0 | 3 | 2 | 0 | 0 |
| AppFlow (SaaS to AWS) | · | 2 | 0 | 0% | 3 | 0 | 2 | 0 | 0 | 0 |

*Never mentioned:* SWF, MSK Connect / Serverless

### AppSync
**Tier C** · Qs 12 (1.4%) · correct 3 (25%) · +expl 15 · U 1 / TD 7 / N 3 / F 1 · your misses 1

> Managed GraphQL; real-time subscriptions; offline sync

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| GraphQL | ★ | 5 | 1 | 20% | 13 | 0 | 4 | 1 | 0 | 1 |
| Real-time subscriptions | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 1 |

### Amazon MQ
**Tier C** · Qs 11 (1.2%) · correct 2 (18%) · +expl 11 · U 1 / TD 4 / N 3 / F 3 · your misses 1

> Managed ActiveMQ/RabbitMQ; lift existing JMS/AMQP/MQTT apps

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Protocols JMS/AMQP/MQTT/STOMP | ★ | 3 | 1 | 33% | 5 | 0 | 2 | 0 | 1 | 2 |
| RabbitMQ | · | 2 | 0 | 0% | 4 | 1 | 0 | 0 | 1 | 0 |
| ActiveMQ | · | 0 | 0 | – | 3 | 0 | 0 | 0 | 0 | 0 |

## Analytics

| Service | Tier | Qs | % of exam | Correct | Ans% | +Expl | Miss |
|---|---|---|---|---|---|---|---|
| Kinesis Data Streams | A | 47 | 5.3% | 21 | 45% | 50 | 3 |
| Athena | A | 40 | 4.5% | 17 | 42% | 47 | 5 |
| EMR | B | 25 | 2.8% | 4 | 16% | 28 | 3 |
| Kinesis Data Firehose | B | 24 | 2.7% | 15 | 62% | 27 | 5 |
| QuickSight | B | 21 | 2.4% | 9 | 43% | 22 | 2 |
| Glue | B | 18 | 2.0% | 7 | 39% | 19 | 3 |
| Kinesis Data Analytics / Managed Flink / Video | C | 9 | 1.0% | 2 | 22% | 12 | 0 |
| Other analytics (Data Pipeline, Data Exchange, Clean Rooms) | C | 5 | 0.6% | 0 | 0% | 7 | 1 |
| Lake Formation | D | 3 | 0.3% | 0 | 0% | 3 | 1 |

### Kinesis Data Streams
**Tier A** · Qs 47 (5.3%) · correct 21 (45%) · +expl 50 · U 19 / TD 13 / N 9 / F 6 · your misses 3

> Real-time stream; shards; multiple consumers; replay

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Shards | ★ | 3 | 1 | 33% | 13 | 0 | 2 | 1 | 0 | 2 |
| KCL / KPL | ★ | 3 | 3 | 100% | 7 | 1 | 1 | 1 | 0 | 0 |
| Retention / replay | · | 1 | 0 | 0% | 4 | 0 | 1 | 0 | 0 | 0 |
| Enhanced fan-out | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 1 |

*Never mentioned:* On-demand mode

### Athena
**Tier A** · Qs 40 (4.5%) · correct 17 (42%) · +expl 47 · U 12 / TD 11 / N 10 / F 7 · your misses 5

> Serverless SQL on S3; pay per scan; partition + Parquet

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Query S3 / logs with SQL | ★★ | 24 | 9 | 38% | 36 | 7 | 7 | 5 | 5 | 1 |
| Federated query | ★★ | 10 | 4 | 40% | 16 | 0 | 7 | 3 | 0 | 2 |
| Partitioning | ★ | 4 | 4 | 100% | 4 | 2 | 1 | 1 | 0 | 0 |

*Never mentioned:* Workgroups, CTAS

### EMR
**Tier B** · Qs 25 (2.8%) · correct 4 (16%) · +expl 28 · U 4 / TD 13 / N 6 / F 2 · your misses 3

> Managed Hadoop/Spark; node types; Spot task nodes

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Hadoop / HDFS / Hive / Presto / HBase | ★★★ | 32 | 13 | 41% | 56 | 12 | 14 | 3 | 3 | 8 |
| Spark | ★ | 4 | 0 | 0% | 7 | 3 | 1 | 0 | 0 | 0 |
| Primary/core/task nodes | ★ | 4 | 2 | 50% | 6 | 0 | 4 | 0 | 0 | 2 |
| Instance fleets / Spot task nodes | · | 2 | 0 | 0% | 3 | 1 | 1 | 0 | 0 | 0 |

*Never mentioned:* EMR Serverless / on EKS

### Kinesis Data Firehose
**Tier B** · Qs 24 (2.7%) · correct 15 (62%) · +expl 27 · U 12 / TD 4 / N 4 / F 4 · your misses 5

> Near-real-time delivery to S3/Redshift/OpenSearch/Splunk; no code

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Near real-time | ★★ | 14 | 3 | 21% | 25 | 7 | 3 | 2 | 2 | 1 |
| Format conversion Parquet/ORC | ★ | 5 | 4 | 80% | 7 | 2 | 2 | 1 | 0 | 2 |
| Buffer size/interval | ★ | 3 | 1 | 33% | 4 | 0 | 2 | 0 | 1 | 1 |
| Destinations Redshift/OpenSearch/Splunk | · | 2 | 1 | 50% | 12 | 1 | 0 | 0 | 1 | 1 |
| Lambda transformation | · | 2 | 2 | 100% | 7 | 2 | 0 | 0 | 0 | 1 |

### QuickSight
**Tier B** · Qs 21 (2.4%) · correct 9 (43%) · +expl 22 · U 4 / TD 8 / N 5 / F 4 · your misses 2

> BI dashboards; SPICE; RLS; embedding

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Embedded dashboards | · | 1 | 0 | 0% | 9 | 1 | 0 | 0 | 0 | 0 |
| Row-level security | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* SPICE

### Glue
**Tier B** · Qs 18 (2.0%) · correct 7 (39%) · +expl 19 · U 3 / TD 8 / N 4 / F 3 · your misses 3

> Serverless ETL + Data Catalog + crawlers

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| ETL jobs | ★★ | 11 | 4 | 36% | 20 | 2 | 5 | 3 | 1 | 1 |
| Glue Data Catalog | ★ | 5 | 4 | 80% | 7 | 0 | 2 | 2 | 1 | 1 |
| Crawlers | ★ | 4 | 3 | 75% | 5 | 0 | 1 | 2 | 1 | 1 |

*Never mentioned:* DataBrew, Job bookmarks, Glue streaming / Schema Registry, FindMatches (ML dedup)

### Kinesis Data Analytics / Managed Flink / Video
**Tier C** · Qs 9 (1.0%) · correct 2 (22%) · +expl 12 · U 3 / TD 3 / N 3 / F 0 · your misses 0

> SQL/Flink on streams; video ingestion

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Managed Flink / KDA | ★ | 7 | 2 | 29% | 9 | 3 | 1 | 3 | 0 | 0 |
| Kinesis Video Streams | · | 2 | 0 | 0% | 3 | 0 | 2 | 0 | 0 | 0 |

### Other analytics (Data Pipeline, Data Exchange, Clean Rooms)
**Tier C** · Qs 5 (0.6%) · correct 0 (0%) · +expl 7 · U 1 / TD 4 / N 0 / F 0 · your misses 1

> Legacy ETL scheduling, third-party datasets

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Data Pipeline (legacy) | ★ | 4 | 0 | 0% | 6 | 1 | 3 | 0 | 0 | 0 |
| Data Exchange | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 1 |

*Never mentioned:* Clean Rooms

### Lake Formation
**Tier D** · Qs 3 (0.3%) · correct 0 (0%) · +expl 3 · U 0 / TD 3 / N 0 / F 0 · your misses 1

> Data lake permissions: column/row/tag-based on Glue catalog

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Blueprints | · | 0 | 0 | – | 2 | 0 | 0 | 0 | 0 | 0 |
| Column/row/cell-level security | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* LF-Tags / tag-based access

## Security, Identity & Compliance

| Service | Tier | Qs | % of exam | Correct | Ans% | +Expl | Miss |
|---|---|---|---|---|---|---|---|
| IAM | S | 139 | 15.7% | 93 | 67% | 167 | 28 |
| Organizations & SCPs | S | 97 | 10.9% | 49 | 51% | 119 | 20 |
| Compliance & data protection (concepts) | A | 68 | 7.7% | 11 | 16% | 126 | 3 |
| KMS | B | 37 | 4.2% | 16 | 43% | 47 | 7 |
| STS & federation | B | 33 | 3.7% | 16 | 48% | 40 | 8 |
| WAF | B | 31 | 3.5% | 24 | 77% | 33 | 8 |
| Inspector | B | 18 | 2.0% | 6 | 33% | 21 | 3 |
| Control Tower | B | 17 | 1.9% | 5 | 29% | 18 | 1 |
| Shield | B | 17 | 1.9% | 6 | 35% | 22 | 5 |
| Directory Service | B | 16 | 1.8% | 7 | 44% | 22 | 3 |
| Resource Access Manager (RAM) | B | 15 | 1.7% | 10 | 67% | 18 | 5 |
| Secrets Manager | B | 15 | 1.7% | 9 | 60% | 19 | 4 |
| IAM Identity Center (SSO) | C | 13 | 1.5% | 7 | 54% | 22 | 4 |
| Cognito | C | 12 | 1.4% | 8 | 67% | 20 | 6 |
| GuardDuty | C | 12 | 1.4% | 2 | 17% | 13 | 3 |
| ACM (certificates) | C | 11 | 1.2% | 8 | 73% | 13 | 6 |
| CloudHSM | C | 7 | 0.8% | 2 | 29% | 7 | 4 |
| Security Hub | C | 7 | 0.8% | 1 | 14% | 7 | 1 |
| Macie | C | 7 | 0.8% | 3 | 43% | 8 | 2 |
| Other security (Detective, Audit Manager, Artifact, Verified Access, Security Lake) | C | 7 | 0.8% | 0 | 0% | 8 | 0 |
| Firewall Manager | C | 6 | 0.7% | 1 | 17% | 8 | 0 |
| IAM Access Analyzer | C | 6 | 0.7% | 2 | 33% | 7 | 0 |

### IAM
**Tier S** · Qs 139 (15.7%) · correct 93 (67%) · +expl 167 · U 18 / TD 73 / N 25 / F 23 · your misses 28

> Who can do what; roles, policies, cross-account, conditions

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| IAM roles | ★★★ | 88 | 56 | 64% | 98 | 12 | 47 | 18 | 11 | 11 |
| IAM users / groups | ★★★ | 55 | 15 | 27% | 74 | 4 | 31 | 11 | 9 | 4 |
| Cross-account role / access | ★★ | 23 | 9 | 39% | 33 | 3 | 10 | 7 | 3 | 2 |
| Trust policy | ★★ | 18 | 16 | 89% | 20 | 2 | 9 | 3 | 4 | 4 |
| Least privilege | ★★ | 16 | 2 | 12% | 24 | 3 | 7 | 3 | 3 | 5 |
| Access keys / long-term credentials | ★★ | 14 | 0 | 0% | 25 | 1 | 8 | 3 | 2 | 1 |
| MFA | ★★ | 13 | 8 | 62% | 18 | 1 | 8 | 2 | 2 | 3 |
| Identity vs resource-based policy | ★★ | 12 | 9 | 75% | 21 | 5 | 4 | 1 | 2 | 0 |
| Condition keys (PrincipalOrgID, SourceIp, RequestedRegion, tags) | ★ | 9 | 7 | 78% | 16 | 2 | 6 | 1 | 0 | 1 |
| Service-linked role | ★ | 9 | 2 | 22% | 14 | 3 | 4 | 0 | 2 | 0 |
| Permissions boundary | ★ | 8 | 2 | 25% | 9 | 2 | 1 | 4 | 1 | 0 |
| External ID / confused deputy | ★ | 5 | 5 | 100% | 10 | 1 | 2 | 1 | 1 | 1 |
| Root user | ★ | 5 | 3 | 60% | 9 | 3 | 1 | 1 | 0 | 0 |
| Explicit deny | ★ | 4 | 3 | 75% | 10 | 2 | 2 | 0 | 0 | 0 |
| ABAC / session tags | ★ | 3 | 3 | 100% | 3 | 1 | 1 | 0 | 1 | 1 |
| iam:PassRole | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Policy Simulator, Credential report / Access Advisor / last accessed, IAM Roles Anywhere

### Organizations & SCPs
**Tier S** · Qs 97 (10.9%) · correct 49 (51%) · +expl 119 · U 10 / TD 46 / N 19 / F 22 · your misses 20

> Multi-account mgmt, consolidated billing, guardrail policies

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| SCPs (any) | ★★★ | 46 | 28 | 61% | 49 | 7 | 21 | 13 | 5 | 16 |
| Management account | ★★★ | 37 | 25 | 68% | 48 | 1 | 15 | 10 | 11 | 4 |
| OUs | ★★★ | 35 | 21 | 60% | 42 | 5 | 17 | 8 | 5 | 7 |
| Member accounts | ★★★ | 33 | 14 | 42% | 49 | 3 | 15 | 5 | 10 | 3 |
| Consolidated billing | ★ | 9 | 0 | 0% | 16 | 1 | 4 | 2 | 2 | 1 |
| Invite / move accounts | ★ | 9 | 4 | 44% | 16 | 1 | 2 | 4 | 2 | 0 |
| Deny list vs allow list / FullAWSAccess | ★ | 9 | 2 | 22% | 12 | 0 | 1 | 5 | 3 | 3 |
| All features | ★ | 3 | 3 | 100% | 11 | 1 | 0 | 1 | 1 | 0 |
| Delegated administrator | ★ | 3 | 3 | 100% | 6 | 1 | 1 | 0 | 1 | 1 |
| aws:PrincipalOrgID | · | 2 | 2 | 100% | 2 | 1 | 1 | 0 | 0 | 0 |
| Backup / AI opt-out / declarative policies | · | 1 | 0 | 0% | 3 | 1 | 0 | 0 | 0 | 0 |
| Tag policies | · | 1 | 1 | 100% | 1 | 0 | 1 | 0 | 0 | 1 |

*Never mentioned:* Resource control policies (RCP)

### Compliance & data protection (concepts)
**Tier A** · Qs 68 (7.7%) · correct 11 (16%) · +expl 126 · U 14 / TD 41 / N 5 / F 8 · your misses 3

> Regulatory keywords that drive service choice

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Encryption in transit (TLS/HTTPS) | ★★★ | 45 | 13 | 29% | 763 | 8 | 26 | 8 | 3 | 9 |
| Audit / auditor | ★★★ | 43 | 9 | 21% | 73 | 12 | 22 | 5 | 4 | 6 |
| Encryption at rest | ★★ | 21 | 4 | 19% | 26 | 1 | 13 | 4 | 3 | 1 |
| PCI DSS | ★ | 3 | 0 | 0% | 3 | 1 | 2 | 0 | 0 | 0 |
| HIPAA | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* GDPR / data residency

### KMS
**Tier B** · Qs 37 (4.2%) · correct 16 (43%) · +expl 47 · U 12 / TD 15 / N 7 / F 3 · your misses 7

> Managed keys; key policies, grants, multi-Region, envelope encryption

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Customer managed vs AWS managed key | ★ | 6 | 0 | 0% | 12 | 1 | 2 | 2 | 1 | 0 |
| Key rotation | ★ | 6 | 0 | 0% | 8 | 0 | 4 | 2 | 0 | 2 |
| Key policy | · | 2 | 2 | 100% | 6 | 1 | 1 | 0 | 0 | 0 |
| Envelope encryption / data keys | · | 1 | 1 | 100% | 3 | 1 | 0 | 0 | 0 | 0 |
| Imported key material / BYOK | · | 1 | 0 | 0% | 2 | 0 | 0 | 1 | 0 | 1 |
| Custom key store / XKS | · | 1 | 0 | 0% | 1 | 1 | 0 | 0 | 0 | 0 |
| Multi-Region keys | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* KMS grants, Cross-account KMS

### STS & federation
**Tier B** · Qs 33 (3.7%) · correct 16 (48%) · +expl 40 · U 3 / TD 20 / N 6 / F 4 · your misses 8

> Temporary creds; SAML/OIDC federation; identity broker

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| AssumeRoleWithSAML / SAML 2.0 | ★★ | 16 | 9 | 56% | 23 | 3 | 8 | 4 | 1 | 7 |
| Temporary credentials | ★★ | 11 | 6 | 55% | 25 | 0 | 10 | 0 | 1 | 2 |
| AssumeRole | ★ | 8 | 5 | 62% | 13 | 1 | 5 | 0 | 2 | 2 |
| AssumeRoleWithWebIdentity / OIDC | ★ | 8 | 6 | 75% | 11 | 0 | 7 | 1 | 0 | 5 |
| Custom identity broker | · | 2 | 2 | 100% | 2 | 0 | 2 | 0 | 0 | 1 |
| GetSessionToken / GetFederationToken | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 1 |

*Never mentioned:* Session duration

### WAF
**Tier B** · Qs 31 (3.5%) · correct 24 (77%) · +expl 33 · U 8 / TD 11 / N 9 / F 3 · your misses 8

> L7 filtering on CloudFront/ALB/API GW/AppSync

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Web ACLs | ★★ | 14 | 10 | 71% | 16 | 3 | 3 | 7 | 1 | 2 |
| Managed rule groups | ★★ | 10 | 3 | 30% | 13 | 0 | 6 | 1 | 3 | 3 |
| SQLi / XSS | ★ | 6 | 1 | 17% | 9 | 1 | 5 | 0 | 0 | 2 |
| IP sets / block IPs | ★ | 5 | 2 | 40% | 7 | 2 | 2 | 0 | 1 | 1 |
| Geo match / block countries | ★ | 3 | 3 | 100% | 4 | 1 | 1 | 1 | 0 | 1 |
| Rate-based rules | · | 2 | 0 | 0% | 6 | 0 | 1 | 0 | 1 | 2 |
| Bot Control | · | 2 | 1 | 50% | 5 | 0 | 2 | 0 | 0 | 1 |

### Inspector
**Tier B** · Qs 18 (2.0%) · correct 6 (33%) · +expl 21 · U 4 / TD 11 / N 2 / F 1 · your misses 3

> Vulnerability (CVE) scanning for EC2/ECR/Lambda

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| CVE / software vulnerabilities | ★★ | 16 | 5 | 31% | 23 | 3 | 9 | 3 | 1 | 3 |
| Network reachability | · | 1 | 0 | 0% | 5 | 1 | 0 | 0 | 0 | 0 |

### Control Tower
**Tier B** · Qs 17 (1.9%) · correct 5 (29%) · +expl 18 · U 1 / TD 8 / N 2 / F 6 · your misses 1

> Landing zone + guardrails + Account Factory for multi-account setup

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Guardrails / controls (preventive/detective/proactive) | ★ | 5 | 2 | 40% | 14 | 1 | 2 | 1 | 1 | 2 |
| Landing zone | ★ | 5 | 2 | 40% | 7 | 0 | 1 | 1 | 3 | 1 |
| Drift | ★ | 3 | 0 | 0% | 5 | 0 | 2 | 0 | 1 | 1 |
| Account Factory / AFT | · | 1 | 1 | 100% | 1 | 0 | 0 | 1 | 0 | 1 |
| Log Archive / Audit accounts | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Customizations for Control Tower (CfCT)

### Shield
**Tier B** · Qs 17 (1.9%) · correct 6 (35%) · +expl 22 · U 5 / TD 10 / N 2 / F 0 · your misses 5

> DDoS protection; Advanced = SRT + cost protection

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| DDoS (any) | ★★ | 10 | 3 | 30% | 20 | 3 | 6 | 1 | 0 | 4 |
| Shield Advanced | ★ | 8 | 5 | 62% | 10 | 0 | 8 | 0 | 0 | 2 |

*Never mentioned:* Shield Response Team (SRT/DRT)

### Directory Service
**Tier B** · Qs 16 (1.8%) · correct 7 (44%) · +expl 22 · U 1 / TD 9 / N 5 / F 1 · your misses 3

> Managed Microsoft AD / AD Connector / Simple AD; trusts

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| On-prem Active Directory | ★ | 6 | 1 | 17% | 7 | 0 | 5 | 1 | 0 | 1 |
| LDAP / Kerberos | ★ | 5 | 4 | 80% | 5 | 0 | 4 | 1 | 0 | 2 |
| Managed Microsoft AD | ★ | 4 | 1 | 25% | 5 | 0 | 3 | 1 | 0 | 2 |
| AD Connector (proxy to on-prem) | ★ | 3 | 2 | 67% | 3 | 0 | 2 | 1 | 0 | 1 |
| Forest trust (one/two-way) | · | 1 | 1 | 100% | 1 | 0 | 1 | 0 | 0 | 0 |
| Simple AD | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

### Resource Access Manager (RAM)
**Tier B** · Qs 15 (1.7%) · correct 10 (67%) · +expl 18 · U 0 / TD 7 / N 2 / F 6 · your misses 5

> Share subnets/TGW/Resolver rules/License configs across accounts

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Share with org / OU | ★★ | 17 | 9 | 53% | 33 | 3 | 6 | 2 | 6 | 5 |
| Share Transit Gateway | ★ | 4 | 4 | 100% | 6 | 0 | 2 | 0 | 2 | 1 |
| Share subnets / VPC | · | 2 | 1 | 50% | 5 | 2 | 0 | 0 | 0 | 1 |

*Never mentioned:* Share Resolver rules

### Secrets Manager
**Tier B** · Qs 15 (1.7%) · correct 9 (60%) · +expl 19 · U 2 / TD 6 / N 6 / F 1 · your misses 4

> Store + auto-rotate DB creds/API keys; cross-Region replicas

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Automatic rotation | ★ | 6 | 3 | 50% | 13 | 1 | 2 | 2 | 1 | 0 |

*Never mentioned:* Secret replication cross-Region

### IAM Identity Center (SSO)
**Tier C** · Qs 13 (1.5%) · correct 7 (54%) · +expl 22 · U 1 / TD 8 / N 2 / F 2 · your misses 4

> Workforce SSO to many accounts; permission sets; external IdP

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| External IdP (Okta/Entra/AD) | ★★ | 10 | 6 | 60% | 23 | 0 | 6 | 3 | 1 | 8 |
| Permission sets | ★ | 4 | 3 | 75% | 6 | 1 | 1 | 1 | 1 | 0 |
| SCIM provisioning | · | 1 | 1 | 100% | 1 | 0 | 1 | 0 | 0 | 1 |

*Never mentioned:* Identity source

### Cognito
**Tier C** · Qs 12 (1.4%) · correct 8 (67%) · +expl 20 · U 0 / TD 9 / N 3 / F 0 · your misses 6

> App user sign-in (user pools) + AWS creds for app users (identity pools)

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Social IdP (Google/Facebook/Amazon) | ★★ | 21 | 3 | 14% | 35 | 9 | 11 | 1 | 0 | 3 |
| User pools | ★ | 4 | 1 | 25% | 9 | 0 | 3 | 0 | 1 | 0 |
| Identity pools / federated identities | ★ | 3 | 1 | 33% | 5 | 0 | 2 | 0 | 1 | 2 |
| Hosted UI | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

### GuardDuty
**Tier C** · Qs 12 (1.4%) · correct 2 (17%) · +expl 13 · U 2 / TD 9 / N 0 / F 1 · your misses 3

> Threat detection from CloudTrail/VPC flow/DNS logs

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Findings / threat intel / crypto-mining | ★ | 7 | 0 | 0% | 8 | 0 | 7 | 0 | 0 | 0 |

*Never mentioned:* Malware / S3 / EKS / RDS protection

### ACM (certificates)
**Tier C** · Qs 11 (1.2%) · correct 8 (73%) · +expl 13 · U 3 / TD 7 / N 1 / F 0 · your misses 6

> Free public TLS certs auto-renew; us-east-1 for CloudFront; Private CA

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| us-east-1 for CloudFront | ★ | 4 | 1 | 25% | 4 | 1 | 1 | 0 | 2 | 1 |
| Import third-party cert | ★ | 3 | 1 | 33% | 5 | 0 | 3 | 0 | 0 | 0 |
| Private CA | · | 2 | 0 | 0% | 4 | 0 | 1 | 0 | 1 | 1 |
| Expiry / renewal | · | 1 | 1 | 100% | 5 | 1 | 0 | 0 | 0 | 0 |

*Never mentioned:* DNS / email validation

### CloudHSM
**Tier C** · Qs 7 (0.8%) · correct 2 (29%) · +expl 7 · U 1 / TD 5 / N 1 / F 0 · your misses 4

> Single-tenant HSM, FIPS 140-2 L3, you own keys; Oracle TDE/SSL offload

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| HSM cluster | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 1 |
| FIPS 140-2 Level 3 | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

### Security Hub
**Tier C** · Qs 7 (0.8%) · correct 1 (14%) · +expl 7 · U 2 / TD 4 / N 0 / F 1 · your misses 1

> Aggregate findings + compliance standards (CIS, FSBP, PCI)

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Standards CIS / FSBP / PCI | · | 2 | 0 | 0% | 2 | 0 | 2 | 0 | 0 | 0 |
| ASFF / finding aggregation | · | 0 | 0 | – | 2 | 0 | 0 | 0 | 0 | 0 |

### Macie
**Tier C** · Qs 7 (0.8%) · correct 3 (43%) · +expl 8 · U 0 / TD 5 / N 2 / F 0 · your misses 2

> Discover PII/sensitive data in S3

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| PII / sensitive data | ★★ | 12 | 5 | 42% | 20 | 3 | 8 | 1 | 0 | 2 |

### Other security (Detective, Audit Manager, Artifact, Verified Access, Security Lake)
**Tier C** · Qs 7 (0.8%) · correct 0 (0%) · +expl 8 · U 0 / TD 6 / N 0 / F 1 · your misses 0

> Investigation, audit evidence, compliance reports

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Detective | ★ | 4 | 0 | 0% | 6 | 0 | 3 | 0 | 1 | 0 |
| Audit Manager | ★ | 3 | 0 | 0% | 3 | 0 | 3 | 0 | 0 | 0 |
| Artifact (compliance reports) | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 0 |

*Never mentioned:* Verified Access, Security Lake

### Firewall Manager
**Tier C** · Qs 6 (0.7%) · correct 1 (17%) · +expl 8 · U 1 / TD 2 / N 1 / F 2 · your misses 0

> Centrally enforce WAF/Shield/SG/Network Firewall across org

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Security policies across accounts | · | 2 | 0 | 0% | 4 | 0 | 0 | 1 | 1 | 0 |

### IAM Access Analyzer
**Tier C** · Qs 6 (0.7%) · correct 2 (33%) · +expl 7 · U 1 / TD 3 / N 0 / F 2 · your misses 0

> Find external/unused access; generate least-privilege policy

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Policy generation from CloudTrail | · | 2 | 2 | 100% | 2 | 0 | 1 | 0 | 1 | 0 |
| External access findings | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |
| Unused access | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

## Management, Governance & Cost

| Service | Tier | Qs | % of exam | Correct | Ans% | +Expl | Miss |
|---|---|---|---|---|---|---|---|
| CloudWatch | S | 98 | 11.1% | 39 | 40% | 119 | 12 |
| Purchase options & pricing | S | 96 | 10.8% | 34 | 35% | 141 | 17 |
| Systems Manager | A | 81 | 9.1% | 32 | 40% | 83 | 20 |
| CloudFormation | A | 74 | 8.4% | 38 | 51% | 82 | 13 |
| AWS Config | A | 52 | 5.9% | 13 | 25% | 53 | 7 |
| CloudTrail | A | 40 | 4.5% | 20 | 50% | 46 | 7 |
| Cost tools (Cost Explorer, CUR, Budgets, Anomaly Detection) | B | 29 | 3.3% | 17 | 59% | 33 | 5 |
| Tagging | B | 29 | 3.3% | 19 | 66% | 43 | 12 |
| Other management (Service Quotas, License Manager, OpsWorks, Grafana, Resource Groups, Well-Architected, Resilience Hub, FIS, Proton) | B | 25 | 2.8% | 6 | 24% | 34 | 2 |
| Trusted Advisor | B | 17 | 1.9% | 2 | 12% | 17 | 2 |
| Service Catalog | B | 15 | 1.7% | 7 | 47% | 15 | 4 |
| X-Ray | C | 10 | 1.1% | 6 | 60% | 11 | 2 |
| Compute Optimizer | C | 7 | 0.8% | 5 | 71% | 7 | 1 |
| CDK | C | 6 | 0.7% | 4 | 67% | 6 | 1 |
| AWS Health | D | 1 | 0.1% | 0 | 0% | 1 | 0 |

### CloudWatch
**Tier S** · Qs 98 (11.1%) · correct 39 (40%) · +expl 119 · U 23 / TD 39 / N 19 / F 17 · your misses 12

> Metrics, alarms, logs, dashboards, agent, synthetics

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Alarms | ★★★ | 37 | 16 | 43% | 53 | 10 | 13 | 8 | 6 | 4 |
| CloudWatch Logs / log groups | ★★★ | 35 | 14 | 40% | 39 | 16 | 8 | 6 | 5 | 4 |
| Dashboards | ★★ | 26 | 11 | 42% | 35 | 6 | 12 | 3 | 5 | 2 |
| CloudWatch agent (unified) | ★★ | 18 | 8 | 44% | 19 | 4 | 6 | 4 | 4 | 2 |
| Custom metrics | ★ | 4 | 1 | 25% | 7 | 1 | 1 | 1 | 1 | 0 |
| Detailed monitoring | ★ | 4 | 0 | 0% | 6 | 1 | 2 | 0 | 1 | 0 |
| Logs Insights | · | 2 | 1 | 50% | 2 | 0 | 1 | 0 | 1 | 0 |
| Subscription filters | · | 2 | 2 | 100% | 2 | 1 | 0 | 0 | 1 | 0 |
| Metric filters | · | 2 | 1 | 50% | 2 | 1 | 1 | 0 | 0 | 0 |
| Container / Lambda Insights | · | 2 | 0 | 0% | 2 | 0 | 2 | 0 | 0 | 1 |
| Anomaly detection | · | 1 | 1 | 100% | 5 | 0 | 0 | 1 | 0 | 0 |
| Cross-account observability | · | 1 | 0 | 0% | 1 | 0 | 0 | 0 | 1 | 0 |
| Export logs to S3 | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 0 |
| Synthetics canaries | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Composite alarms, RUM, Contributor Insights, Metric streams

### Purchase options & pricing
**Tier S** · Qs 96 (10.8%) · correct 34 (35%) · +expl 141 · U 15 / TD 54 / N 15 / F 12 · your misses 17

> On-Demand / RI / Savings Plans / Spot / data-transfer cost

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Spot Instances (any) | ★★★ | 39 | 14 | 36% | 42 | 2 | 25 | 7 | 5 | 10 |
| Reserved Instances (any) | ★★ | 23 | 11 | 48% | 30 | 2 | 11 | 7 | 3 | 6 |
| On-Demand | ★★ | 18 | 4 | 22% | 21 | 1 | 9 | 5 | 3 | 0 |
| Spot interruption / 2-min / rebalance | ★★ | 10 | 0 | 0% | 36 | 1 | 5 | 2 | 2 | 3 |
| Savings Plans (any) | ★ | 7 | 4 | 57% | 11 | 0 | 2 | 1 | 4 | 1 |
| Spot Fleet / EC2 Fleet | ★ | 6 | 2 | 33% | 8 | 0 | 6 | 0 | 0 | 1 |
| RI / SP sharing across org | ★ | 4 | 0 | 0% | 9 | 2 | 2 | 0 | 0 | 2 |
| Reserved DB / nodes / capacity | ★ | 4 | 2 | 50% | 6 | 0 | 3 | 1 | 0 | 2 |
| EC2 Instance Savings Plans | ★ | 4 | 1 | 25% | 5 | 0 | 2 | 0 | 2 | 0 |
| Compute Savings Plans | ★ | 4 | 4 | 100% | 4 | 0 | 2 | 0 | 2 | 1 |
| Data transfer / egress / inter-AZ cost | ★ | 3 | 1 | 33% | 10 | 2 | 1 | 0 | 0 | 1 |
| Standard vs Convertible RI | · | 2 | 0 | 0% | 2 | 0 | 1 | 0 | 1 | 0 |
| Zonal vs regional RI | · | 1 | 1 | 100% | 1 | 0 | 0 | 1 | 0 | 2 |

### Systems Manager
**Tier A** · Qs 81 (9.1%) · correct 32 (40%) · +expl 83 · U 7 / TD 51 / N 9 / F 14 · your misses 20

> Ops toolbox: Session Manager, Patch, Run Command, Automation, Parameter Store

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Patch Manager / patch baseline / patch group | ★★ | 17 | 10 | 59% | 32 | 1 | 14 | 1 | 1 | 9 |
| Parameter Store / SecureString | ★★ | 14 | 5 | 36% | 14 | 1 | 9 | 1 | 3 | 4 |
| Automation runbooks / SSM documents | ★★ | 13 | 5 | 38% | 20 | 2 | 10 | 0 | 1 | 2 |
| Session Manager (no SSH/bastion) | ★★ | 13 | 7 | 54% | 13 | 1 | 6 | 4 | 2 | 4 |
| Maintenance windows | ★★ | 10 | 3 | 30% | 13 | 1 | 8 | 1 | 0 | 3 |
| OpsCenter / OpsItems | ★ | 8 | 0 | 0% | 8 | 0 | 6 | 0 | 2 | 0 |
| SSM Agent | ★ | 7 | 3 | 43% | 14 | 1 | 6 | 0 | 0 | 1 |
| Run Command | ★ | 7 | 1 | 14% | 10 | 0 | 5 | 2 | 0 | 1 |
| State Manager | ★ | 6 | 0 | 0% | 6 | 0 | 6 | 0 | 0 | 1 |
| Hybrid activations / managed on-prem nodes | ★ | 3 | 1 | 33% | 17 | 0 | 3 | 0 | 0 | 1 |
| Distributor / Fleet Manager | · | 2 | 0 | 0% | 2 | 0 | 2 | 0 | 0 | 1 |
| Incident Manager / Change Manager | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 0 |

*Never mentioned:* SSM Inventory, AppConfig / feature flags

### CloudFormation
**Tier A** · Qs 74 (8.4%) · correct 38 (51%) · +expl 82 · U 7 / TD 37 / N 17 / F 13 · your misses 13

> IaC; StackSets for multi-account; change sets; drift

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| DeletionPolicy / Retain / UpdateReplacePolicy | ★★ | 17 | 7 | 41% | 28 | 3 | 9 | 0 | 5 | 1 |
| Rollback | ★★ | 12 | 7 | 58% | 16 | 1 | 4 | 5 | 2 | 1 |
| StackSets (multi-account/Region) | ★★ | 10 | 5 | 50% | 17 | 0 | 5 | 2 | 3 | 2 |
| Change sets | ★ | 9 | 3 | 33% | 11 | 2 | 3 | 3 | 1 | 2 |
| Nested stacks | ★ | 5 | 0 | 0% | 8 | 0 | 2 | 1 | 2 | 0 |
| Mappings / intrinsic functions | ★ | 4 | 1 | 25% | 9 | 1 | 3 | 0 | 0 | 0 |
| Termination protection | ★ | 4 | 0 | 0% | 4 | 1 | 1 | 1 | 1 | 0 |
| Service-managed permissions / auto-deploy to OUs | ★ | 3 | 2 | 67% | 6 | 0 | 2 | 0 | 1 | 1 |
| Drift detection | ★ | 3 | 0 | 0% | 5 | 0 | 2 | 0 | 1 | 1 |
| cfn-init / cfn-signal / CreationPolicy / WaitCondition | · | 1 | 0 | 0% | 2 | 0 | 1 | 0 | 0 | 0 |
| Custom resources (Lambda-backed) | · | 1 | 1 | 100% | 1 | 1 | 0 | 0 | 0 | 0 |
| Registry / modules / hooks / Guard | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Stack policy, Outputs / Export / ImportValue

### AWS Config
**Tier A** · Qs 52 (5.9%) · correct 13 (25%) · +expl 53 · U 7 / TD 32 / N 5 / F 8 · your misses 7

> Resource config history + compliance rules + remediation

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Config rules (managed/custom) | ★★★ | 30 | 9 | 30% | 36 | 3 | 18 | 3 | 6 | 7 |
| Auto-remediation (SSM Automation) | ★★ | 15 | 2 | 13% | 26 | 2 | 5 | 4 | 4 | 3 |
| Aggregator (multi-account) | · | 1 | 1 | 100% | 3 | 0 | 1 | 0 | 0 | 1 |
| Conformance packs | · | 1 | 0 | 0% | 2 | 0 | 1 | 0 | 0 | 0 |
| Configuration history / timeline | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

### CloudTrail
**Tier A** · Qs 40 (4.5%) · correct 20 (50%) · +expl 46 · U 13 / TD 17 / N 6 / F 4 · your misses 7

> API audit log; org trail; data events; integrity

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Data events vs management events | ★ | 7 | 3 | 43% | 9 | 1 | 3 | 2 | 1 | 1 |
| Multi-Region trail | ★ | 3 | 0 | 0% | 5 | 2 | 1 | 0 | 0 | 0 |
| CloudTrail Lake | ★ | 3 | 1 | 33% | 4 | 0 | 2 | 0 | 1 | 0 |
| Organization trail | · | 1 | 1 | 100% | 3 | 0 | 1 | 0 | 0 | 0 |
| Log file integrity validation | · | 1 | 1 | 100% | 2 | 1 | 0 | 0 | 0 | 1 |
| CloudTrail Insights | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

### Cost tools (Cost Explorer, CUR, Budgets, Anomaly Detection)
**Tier B** · Qs 29 (3.3%) · correct 17 (59%) · +expl 33 · U 3 / TD 10 / N 9 / F 7 · your misses 5

> See, forecast, alert, allocate cost

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Chargeback / showback per team | ★★ | 18 | 8 | 44% | 19 | 2 | 7 | 5 | 4 | 0 |
| Cost Explorer | ★★ | 13 | 4 | 31% | 16 | 3 | 3 | 3 | 4 | 1 |
| Cost & Usage Report (CUR) | ★★ | 12 | 7 | 58% | 13 | 1 | 6 | 1 | 4 | 2 |
| AWS Budgets / budget alerts | ★ | 9 | 5 | 56% | 11 | 1 | 1 | 5 | 2 | 2 |
| Cost allocation tags | ★ | 7 | 3 | 43% | 14 | 1 | 4 | 2 | 0 | 2 |
| Rightsizing | ★ | 7 | 5 | 71% | 10 | 0 | 5 | 1 | 1 | 2 |
| Pricing Calculator / TCO | ★ | 4 | 2 | 50% | 6 | 0 | 4 | 0 | 0 | 1 |
| Cost Categories | · | 1 | 1 | 100% | 2 | 0 | 0 | 0 | 1 | 0 |
| RI / Savings Plans recommendations | · | 1 | 0 | 0% | 1 | 0 | 0 | 0 | 1 | 0 |
| Budget actions | · | 1 | 0 | 0% | 1 | 0 | 0 | 0 | 1 | 0 |
| Cost Anomaly Detection | · | 1 | 1 | 100% | 1 | 0 | 0 | 1 | 0 | 0 |

*Never mentioned:* Billing Conductor / pro forma

### Tagging
**Tier B** · Qs 29 (3.3%) · correct 19 (66%) · +expl 43 · U 2 / TD 18 / N 4 / F 5 · your misses 12

> Tags drive cost allocation, ABAC, automation, compliance

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Enforce tags (tag policy/SCP/Config) | · | 2 | 1 | 50% | 5 | 0 | 2 | 0 | 0 | 1 |

### Other management (Service Quotas, License Manager, OpsWorks, Grafana, Resource Groups, Well-Architected, Resilience Hub, FIS, Proton)
**Tier B** · Qs 25 (2.8%) · correct 6 (24%) · +expl 34 · U 3 / TD 12 / N 7 / F 3 · your misses 2

> Ops & governance helpers

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| OpsWorks (Chef/Puppet) | ★ | 9 | 1 | 11% | 10 | 3 | 1 | 5 | 0 | 0 |
| Service Quotas | ★ | 6 | 3 | 50% | 9 | 2 | 2 | 1 | 1 | 1 |
| Managed Grafana / Prometheus | ★ | 4 | 1 | 25% | 4 | 0 | 3 | 0 | 1 | 0 |
| Well-Architected Tool | ★ | 3 | 0 | 0% | 6 | 0 | 2 | 0 | 1 | 0 |
| Resource Groups / Tag Editor | ★ | 3 | 2 | 67% | 4 | 0 | 2 | 1 | 0 | 1 |
| License Manager | · | 2 | 0 | 0% | 6 | 0 | 2 | 0 | 0 | 0 |
| Proton / Launch Wizard | · | 2 | 0 | 0% | 2 | 0 | 2 | 0 | 0 | 0 |

*Never mentioned:* Resilience Hub, Fault Injection Service / chaos

### Trusted Advisor
**Tier B** · Qs 17 (1.9%) · correct 2 (12%) · +expl 17 · U 1 / TD 8 / N 4 / F 4 · your misses 2

> Best-practice checks (cost, security, limits); full checks need Business+ support

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Checks (cost/security/fault tolerance/limits) | ★ | 5 | 1 | 20% | 7 | 0 | 3 | 2 | 0 | 0 |
| Support plans (Business/Enterprise/TAM) | ★ | 5 | 0 | 0% | 5 | 0 | 2 | 1 | 2 | 0 |
| Service limits | · | 2 | 1 | 50% | 3 | 0 | 1 | 1 | 0 | 0 |

### Service Catalog
**Tier B** · Qs 15 (1.7%) · correct 7 (47%) · +expl 15 · U 1 / TD 8 / N 3 / F 3 · your misses 4

> Pre-approved self-service products with constraints

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Portfolios | ★ | 5 | 4 | 80% | 5 | 0 | 2 | 2 | 1 | 0 |
| Launch / template constraints | ★ | 3 | 3 | 100% | 3 | 0 | 1 | 1 | 1 | 1 |
| Products | · | 2 | 2 | 100% | 5 | 0 | 1 | 1 | 0 | 2 |
| Share portfolio across accounts/org | · | 1 | 1 | 100% | 1 | 0 | 0 | 0 | 1 | 0 |

*Never mentioned:* TagOptions, AppRegistry

### X-Ray
**Tier C** · Qs 10 (1.1%) · correct 6 (60%) · +expl 11 · U 3 / TD 4 / N 2 / F 1 · your misses 2

> Distributed tracing; service map; latency root cause

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Traces / segments / annotations | ★ | 4 | 4 | 100% | 8 | 3 | 1 | 0 | 0 | 1 |
| Service map | · | 2 | 0 | 0% | 4 | 0 | 1 | 0 | 1 | 1 |
| X-Ray daemon / SDK | · | 1 | 1 | 100% | 1 | 1 | 0 | 0 | 0 | 0 |

### Compute Optimizer
**Tier C** · Qs 7 (0.8%) · correct 5 (71%) · +expl 7 · U 0 / TD 4 / N 1 / F 2 · your misses 1

> ML right-sizing recs for EC2/ASG/EBS/Lambda/ECS

### CDK
**Tier C** · Qs 6 (0.7%) · correct 4 (67%) · +expl 6 · U 0 / TD 4 / N 1 / F 1 · your misses 1

> IaC in programming languages; synthesizes CloudFormation

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Constructs | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

### AWS Health
**Tier D** · Qs 1 (0.1%) · correct 0 (0%) · +expl 1 · U 0 / TD 1 / N 0 / F 0 · your misses 0

> Account-specific service events; org view; EventBridge automation

*Never mentioned:* Organizational view

## Developer Tools / CI-CD

| Service | Tier | Qs | % of exam | Correct | Ans% | +Expl | Miss |
|---|---|---|---|---|---|---|---|
| CodeDeploy | B | 28 | 3.2% | 13 | 46% | 33 | 2 |
| CodePipeline | B | 20 | 2.3% | 12 | 60% | 21 | 1 |
| CodeCommit & other dev tools | B | 19 | 2.1% | 8 | 42% | 26 | 3 |
| CodeBuild | B | 18 | 2.0% | 15 | 83% | 18 | 2 |

### CodeDeploy
**Tier B** · Qs 28 (3.2%) · correct 13 (46%) · +expl 33 · U 4 / TD 10 / N 11 / F 3 · your misses 2

> Deploy to EC2/on-prem/Lambda/ECS; in-place vs blue/green; canary/linear

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Blue/green deployment (any) | ★★ | 10 | 8 | 80% | 15 | 1 | 3 | 6 | 0 | 2 |
| Canary / linear / all-at-once configs | ★ | 6 | 2 | 33% | 9 | 0 | 1 | 4 | 1 | 0 |
| In-place deployment | ★ | 3 | 0 | 0% | 8 | 0 | 1 | 2 | 0 | 0 |
| Automatic rollback / alarms | · | 1 | 1 | 100% | 1 | 1 | 0 | 0 | 0 | 0 |

*Never mentioned:* AppSpec / lifecycle hooks, Deployment groups, CodeDeploy agent

### CodePipeline
**Tier B** · Qs 20 (2.3%) · correct 12 (60%) · +expl 21 · U 1 / TD 10 / N 8 / F 1 · your misses 1

> CI/CD orchestration; stages, manual approval, cross-account

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Manual approval action | · | 2 | 2 | 100% | 2 | 0 | 1 | 0 | 1 | 0 |
| Source stage / action | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Cross-account / cross-Region pipeline

### CodeCommit & other dev tools
**Tier B** · Qs 19 (2.1%) · correct 8 (42%) · +expl 26 · U 0 / TD 8 / N 8 / F 3 · your misses 3

> Git repo (closed to new customers), CodeArtifact, CodeGuru, Amplify

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| GitHub / GitLab / Bitbucket / Jenkins | ★★ | 10 | 5 | 50% | 16 | 0 | 5 | 4 | 1 | 2 |
| CodeCommit | ★ | 8 | 3 | 38% | 8 | 0 | 0 | 6 | 2 | 1 |
| Amplify | ★ | 3 | 0 | 0% | 4 | 0 | 2 | 0 | 1 | 0 |
| CodeArtifact | ★ | 3 | 0 | 0% | 3 | 0 | 3 | 0 | 0 | 0 |
| CodeGuru | ★ | 3 | 0 | 0% | 3 | 0 | 2 | 0 | 1 | 0 |

### CodeBuild
**Tier B** · Qs 18 (2.0%) · correct 15 (83%) · +expl 18 · U 0 / TD 7 / N 9 / F 2 · your misses 2

> Managed CI compile and unit-run service; buildspec

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| CodeBuild in VPC / caching | · | 1 | 0 | 0% | 1 | 0 | 0 | 1 | 0 | 0 |

*Never mentioned:* buildspec

## Machine Learning / AI

| Service | Tier | Qs | % of exam | Correct | Ans% | +Expl | Miss |
|---|---|---|---|---|---|---|---|
| AI services (Rekognition, Comprehend, Transcribe, Translate, Polly, Textract, Lex, Kendra, Personalize, Forecast, Bedrock) | B | 17 | 1.9% | 10 | 59% | 17 | 5 |
| SageMaker | C | 6 | 0.7% | 2 | 33% | 7 | 2 |

### AI services (Rekognition, Comprehend, Transcribe, Translate, Polly, Textract, Lex, Kendra, Personalize, Forecast, Bedrock)
**Tier B** · Qs 17 (1.9%) · correct 10 (59%) · +expl 17 · U 0 / TD 14 / N 2 / F 1 · your misses 5

> Pre-trained AI APIs

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Rekognition (image/video) | ★ | 9 | 4 | 44% | 9 | 0 | 7 | 2 | 0 | 3 |
| Comprehend (NLP / sentiment) | ★ | 4 | 2 | 50% | 4 | 0 | 3 | 0 | 1 | 0 |
| Lex (chatbot) | ★ | 4 | 2 | 50% | 4 | 0 | 4 | 0 | 0 | 1 |
| Textract (OCR) | ★ | 3 | 3 | 100% | 3 | 0 | 2 | 0 | 1 | 0 |
| Transcribe (speech to text) | · | 2 | 1 | 50% | 3 | 0 | 2 | 0 | 0 | 1 |
| Translate | · | 2 | 0 | 0% | 2 | 0 | 2 | 0 | 0 | 1 |
| Polly (text to speech) | · | 2 | 0 | 0% | 2 | 0 | 2 | 0 | 0 | 2 |
| Kendra (enterprise search) | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 0 |
| Personalize / Forecast | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |
| A2I human review | · | 0 | 0 | – | 1 | 0 | 0 | 0 | 0 | 0 |

*Never mentioned:* Bedrock (GenAI)

### SageMaker
**Tier C** · Qs 6 (0.7%) · correct 2 (33%) · +expl 7 · U 0 / TD 5 / N 0 / F 1 · your misses 2

> Train/deploy ML models

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Endpoints / inference | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 0 |
| Training jobs | · | 0 | 0 | – | 3 | 0 | 0 | 0 | 0 | 0 |

## End-user, IoT, Media

| Service | Tier | Qs | % of exam | Correct | Ans% | +Expl | Miss |
|---|---|---|---|---|---|---|---|
| End-user computing (WorkSpaces, AppStream, Connect, Pinpoint, WorkDocs) | B | 19 | 2.1% | 9 | 47% | 21 | 7 |
| IoT | B | 18 | 2.0% | 5 | 28% | 22 | 3 |
| Media (Elemental) | C | 7 | 0.8% | 3 | 43% | 8 | 3 |

### End-user computing (WorkSpaces, AppStream, Connect, Pinpoint, WorkDocs)
**Tier B** · Qs 19 (2.1%) · correct 9 (47%) · +expl 21 · U 0 / TD 16 / N 3 / F 0 · your misses 7

> Virtual desktops, app streaming, contact center

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Amazon Connect (contact center) | ★ | 9 | 3 | 33% | 9 | 0 | 8 | 1 | 0 | 1 |
| WorkSpaces (VDI) | ★ | 8 | 4 | 50% | 8 | 0 | 6 | 2 | 0 | 3 |
| Pinpoint (marketing msgs) | ★ | 4 | 0 | 0% | 5 | 0 | 4 | 0 | 0 | 1 |
| AppStream 2.0 (app streaming) | ★ | 4 | 2 | 50% | 4 | 0 | 2 | 2 | 0 | 3 |
| WorkDocs / WorkMail / Chime | · | 1 | 1 | 100% | 3 | 0 | 1 | 0 | 0 | 1 |

### IoT
**Tier B** · Qs 18 (2.0%) · correct 5 (28%) · +expl 22 · U 5 / TD 9 / N 3 / F 1 · your misses 3

> Device ingestion; MQTT; edge with Greengrass

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| IoT Core / MQTT / rules engine | ★ | 5 | 4 | 80% | 6 | 0 | 3 | 1 | 1 | 2 |
| IoT SiteWise / Events / Analytics / Device Shadow | · | 2 | 0 | 0% | 5 | 0 | 2 | 0 | 0 | 0 |
| Greengrass (edge) | · | 2 | 1 | 50% | 2 | 0 | 2 | 0 | 0 | 1 |

### Media (Elemental)
**Tier C** · Qs 7 (0.8%) · correct 3 (43%) · +expl 8 · U 3 / TD 4 / N 0 / F 0 · your misses 3

> Video transcoding/live streaming

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| MediaConvert / Elastic Transcoder | ★ | 6 | 3 | 50% | 6 | 3 | 3 | 0 | 0 | 3 |
| MediaLive / MediaPackage | · | 1 | 0 | 0% | 2 | 1 | 0 | 0 | 0 | 0 |

## Niche services & tooling

| Service | Tier | Qs | % of exam | Correct | Ans% | +Expl | Miss |
|---|---|---|---|---|---|---|---|
| CLI / SDK / API tooling | A | 44 | 5.0% | 14 | 32% | 88 | 2 |
| Niche services seen in questions | B | 18 | 2.0% | 5 | 28% | 28 | 1 |

### CLI / SDK / API tooling
**Tier A** · Qs 44 (5.0%) · correct 14 (32%) · +expl 88 · U 10 / TD 17 / N 7 / F 10 · your misses 2

> How automation calls AWS; scripting answers often lose to managed features

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| AWS CLI | ★★★ | 32 | 11 | 34% | 61 | 5 | 12 | 6 | 9 | 2 |
| Custom scripts / cron on EC2 | ★★ | 27 | 4 | 15% | 33 | 6 | 13 | 6 | 2 | 0 |
| ARN (Amazon Resource Name) | ★★ | 16 | 14 | 88% | 24 | 0 | 12 | 3 | 1 | 3 |
| AWS SDK | ★★ | 12 | 2 | 17% | 28 | 3 | 7 | 1 | 1 | 0 |

### Niche services seen in questions
**Tier B** · Qs 18 (2.0%) · correct 5 (28%) · +expl 28 · U 1 / TD 14 / N 1 / F 2 · your misses 1

> Mostly distractors; know one-line purpose

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| AWS Marketplace (buy 3rd-party AMIs/SaaS) | ★ | 8 | 2 | 25% | 15 | 1 | 5 | 1 | 1 | 0 |
| Managed Blockchain | · | 2 | 1 | 50% | 2 | 0 | 2 | 0 | 0 | 1 |
| App2Container (containerize .NET/Java) | · | 2 | 1 | 50% | 2 | 0 | 1 | 0 | 1 | 0 |
| Device Farm (mobile app testing) | · | 2 | 0 | 0% | 2 | 0 | 2 | 0 | 0 | 0 |
| Alexa for Business | · | 2 | 0 | 0% | 2 | 0 | 2 | 0 | 0 | 0 |
| Cloud Adoption Readiness Tool (CART) | · | 1 | 1 | 100% | 1 | 0 | 1 | 0 | 0 | 0 |
| Ground Station (satellite) | · | 1 | 0 | 0% | 1 | 0 | 1 | 0 | 0 | 0 |

## Architecture concepts & question qualifiers

| Service | Tier | Qs | % of exam | Correct | Ans% | +Expl | Miss |
|---|---|---|---|---|---|---|---|
| Question qualifiers | S | 242 | 27.3% | 2 | 1% | 299 | 43 |
| Architecture patterns | A | 86 | 9.7% | 13 | 15% | 160 | 16 |
| DR & resilience | A | 72 | 8.1% | 27 | 38% | 114 | 25 |
| Deployment strategies | B | 19 | 2.1% | 11 | 58% | 43 | 4 |

### Question qualifiers
**Tier S** · Qs 242 (27.3%) · correct 2 (1%) · +expl 299 · U 44 / TD 126 / N 33 / F 39 · your misses 43

> The constraint word decides between valid options

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Scalable / elastic | ★★★ | 235 | 60 | 26% | 368 | 41 | 121 | 36 | 37 | 19 |
| Multi-select (Select TWO/THREE) | ★★★ | 205 | 0 | 0% | 205 | 53 | 78 | 49 | 25 | 32 |
| Lowest latency / performance | ★★★ | 162 | 24 | 15% | 294 | 34 | 73 | 37 | 18 | 20 |
| MOST cost-effective / lowest cost | ★★★ | 130 | 2 | 2% | 187 | 23 | 77 | 18 | 12 | 33 |
| LEAST operational overhead / effort | ★★★ | 78 | 0 | 0% | 104 | 11 | 35 | 12 | 20 | 12 |
| Highly available / fault tolerant | ★★★ | 70 | 6 | 9% | 126 | 11 | 37 | 13 | 9 | 8 |
| Most secure / least privilege | ★★★ | 43 | 2 | 5% | 108 | 7 | 25 | 6 | 5 | 9 |
| Fastest / minimal downtime | ★★ | 14 | 1 | 7% | 33 | 3 | 5 | 4 | 2 | 6 |

### Architecture patterns
**Tier A** · Qs 86 (9.7%) · correct 13 (15%) · +expl 160 · U 19 / TD 33 / N 23 / F 11 · your misses 16

> Design keywords that hint the answer

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Hybrid / on-premises | ★★★ | 186 | 51 | 27% | 246 | 35 | 91 | 33 | 27 | 9 |
| Serverless | ★★★ | 54 | 7 | 13% | 110 | 13 | 19 | 14 | 8 | 9 |
| Caching layer | ★★★ | 38 | 18 | 47% | 66 | 8 | 22 | 5 | 3 | 9 |
| Stateless vs stateful / session state | ★★ | 19 | 2 | 11% | 28 | 3 | 9 | 3 | 4 | 4 |
| Microservices | ★★ | 12 | 2 | 17% | 35 | 2 | 5 | 4 | 1 | 1 |
| Decoupling / loosely coupled | ★★ | 10 | 4 | 40% | 33 | 3 | 4 | 2 | 1 | 1 |
| Read-heavy / write-heavy | ★ | 6 | 1 | 17% | 20 | 1 | 3 | 1 | 1 | 2 |
| Monolith | ★ | 4 | 0 | 0% | 5 | 0 | 1 | 2 | 1 | 1 |
| Idempotency / duplicates | · | 1 | 1 | 100% | 12 | 0 | 1 | 0 | 0 | 2 |
| Event-driven | · | 1 | 0 | 0% | 8 | 0 | 1 | 0 | 0 | 4 |

### DR & resilience
**Tier A** · Qs 72 (8.1%) · correct 27 (38%) · +expl 114 · U 14 / TD 33 / N 12 / F 13 · your misses 25

> Map RTO/RPO + cost to DR tier

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Multi-AZ / AZ failure | ★★★ | 96 | 38 | 40% | 110 | 17 | 51 | 14 | 14 | 15 |
| Multi-Region | ★★★ | 82 | 20 | 24% | 121 | 14 | 37 | 18 | 13 | 10 |
| Failover (any) | ★★★ | 49 | 22 | 45% | 71 | 8 | 22 | 9 | 10 | 10 |
| RTO / RPO | ★★ | 24 | 1 | 4% | 28 | 2 | 14 | 5 | 3 | 14 |
| Multi-site active-active | ★ | 9 | 3 | 33% | 15 | 2 | 3 | 3 | 1 | 2 |
| Pilot light | ★ | 5 | 0 | 0% | 7 | 1 | 2 | 2 | 0 | 3 |
| Single point of failure | · | 2 | 0 | 0% | 9 | 0 | 2 | 0 | 0 | 3 |
| Backup & restore | · | 1 | 0 | 0% | 6 | 0 | 0 | 0 | 1 | 0 |
| Warm standby | · | 1 | 0 | 0% | 4 | 1 | 0 | 0 | 0 | 1 |

### Deployment strategies
**Tier B** · Qs 19 (2.1%) · correct 11 (58%) · +expl 43 · U 2 / TD 7 / N 9 / F 1 · your misses 4

> Release pattern keywords

| Keyword | Pri | Qs | Correct | Ans% | +Expl | U | TD | N | F | Miss |
|---|---|---|---|---|---|---|---|---|---|---|
| Rollback | ★★ | 12 | 7 | 58% | 16 | 1 | 4 | 5 | 2 | 1 |
| Blue/green | ★★ | 10 | 8 | 80% | 15 | 1 | 3 | 6 | 0 | 2 |
| Rolling | ★ | 9 | 1 | 11% | 30 | 1 | 5 | 3 | 0 | 2 |
| Canary | ★ | 6 | 2 | 33% | 10 | 0 | 2 | 3 | 1 | 0 |
| In-place | ★ | 3 | 0 | 0% | 8 | 0 | 1 | 2 | 0 | 0 |
| Immutable | · | 2 | 1 | 50% | 8 | 0 | 2 | 0 | 0 | 2 |

## Caveats
- Counts come from regex matching on question text and options. Indirect wording (e.g. a scaling policy described without its name) is missed, so mid-range numbers are ±10–15%.
- Generic keywords (Health checks, Alarms, Retention, Rollback, Layers, Checks, Products) also match other contexts. Read them as "topic shows up", not a strict count.
- Service rows count the service name only. Keyword rows are independent, so keywords do not sum to the service total.
- Miss notes include retakes, so a question you missed twice counts twice. TD Set 6 is 16q. Neal excludes 25 flagged questions.

## Unresolved questions
- None blocking. To count Whizlabs or another bank, export it to the same markdown format and rerun.
