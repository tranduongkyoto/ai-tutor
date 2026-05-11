# Scout Report: AWS CSA Course Content

**Date:** 2026-05-11 | **Source:** Stephane Maarek's AWS Certified Solutions Architect Associate (SAA-C03) course
**Files:** 31 PDFs (849 pages) in `sections/` + `aws-certification-10x-faster.md`

---

## Repository Structure

```
18.aws-csa/
├── aws-certification-10x-faster.md   # AI tutor framework for accelerated learning
├── sections/                          # 31 course PDFs (849 pages total)
│   ├── 00-intro-and-toc.pdf          (13p) Course intro, TOC, 30+ services overview
│   ├── 01-getting-started-with-aws.pdf (10p) AWS history, regions, AZs, edge locations
│   ├── 02-aws-iam.pdf                (17p) Users, groups, policies, MFA, roles, best practices
│   ├── 03-amazon-ec2-basics.pdf      (37p) Instance types, security groups, SSH, user data
│   ├── 04-amazon-ec2-associate.pdf   (15p) Purchasing options, placement groups, ENI, hibernate
│   ├── 05-amazon-ec2-instance-storage.pdf (25p) EBS, snapshots, AMI, instance store, EFS
│   ├── 06-high-availability-and-scalability.pdf (42p) ELB (CLB/ALB/NLB/GWLB), ASG
│   ├── 07-rds-aurora-elasticache.pdf (33p) RDS, Aurora, RDS Proxy, ElastiCache
│   ├── 08-amazon-route-53.pdf        (34p) DNS, record types, routing policies, health checks
│   ├── 09-classic-solutions-architecture.pdf (40p) 3 case studies, Elastic Beanstalk
│   ├── 10-amazon-s3.pdf              (26p) Buckets, objects, versioning, replication
│   ├── 11-amazon-s3-advanced.pdf     (20p) Lifecycle, analytics, requester pays, events
│   ├── 12-amazon-s3-security.pdf     (22p) Bucket policies, encryption, CORS, MFA delete
│   ├── 13-cloudfront-and-global-accelerator.pdf (15p) CDN, origins, caching, Global Accelerator
│   ├── 14-aws-storage-extras.pdf     (25p) Snow Family, FSx, Storage Gateway, Transfer Family
│   ├── 15-aws-integration-and-messaging.pdf (39p) SQS, SNS, Kinesis, Amazon MQ
│   ├── 16-containers-on-aws.pdf      (27p) ECS, ECR, EKS, Fargate, App Runner
│   ├── 17-serverless-overview.pdf    (53p) Lambda, DynamoDB, API Gateway, Cognito, Step Functions
│   ├── 18-serverless-architectures.pdf (22p) Serverless patterns, microservices
│   ├── 19-databases-in-aws.pdf       (14p) Database selection guide (10+ DB types)
│   ├── 20-data-and-analytics.pdf     (33p) Kinesis, Glue, Athena, Redshift, EMR, Lake Formation, MSK
│   ├── 21-machine-learning.pdf       (15p) Rekognition, Transcribe, Polly, SageMaker, Kendra, etc.
│   ├── 22-aws-monitoring-audit-performance.pdf (44p) CloudWatch, CloudTrail, Config, EventBridge
│   ├── 23-advanced-identity-in-aws.pdf (29p) Organizations, SCPs, IAM Identity Center, Control Tower
│   ├── 24-aws-security-and-encryption.pdf (49p) KMS, SSM Parameter Store, Shield, WAF, GuardDuty
│   ├── 25-amazon-vpc.pdf             (78p) VPC, subnets, NAT, peering, endpoints, DX, TGW
│   ├── 26-disaster-recovery-and-migrations.pdf (27p) DR strategies, DMS, DRS, AWS Backup
│   ├── 27-more-solutions-architecture.pdf (22p) HPC, caching, IP blocking, HA patterns
│   ├── 28-other-services.pdf         (28p) CloudFormation, SES, Pinpoint, SSM, Batch, Amplify
│   ├── 29-white-papers-and-architectures.pdf (23p) Well-Architected, Trusted Advisor, exam tips
│   └── 30-exam-preparation-and-congratulations.pdf (2p) Final notes
├── plans/
│   └── reports/
└── docs/
```

---

## Content Summary by Domain

### 1. Compute (Sections 03-04, 16-17)
- **EC2**: instance types (General/Compute/Memory/Storage optimized), security groups, purchasing options (On-Demand, Reserved, Savings Plans, Spot up to 90% discount, Dedicated Hosts), placement groups (Cluster/Spread/Partition), ENI, Hibernate
- **Containers**: ECS (EC2 + Fargate launch types), EKS (managed Kubernetes), ECR, App Runner, App2Container
- **Serverless**: Lambda (VPC deployment, RDS Proxy, Lambda@Edge vs CloudFront Functions), Step Functions

### 2. Storage (Sections 05, 10-14)
- **Block**: EBS (gp2/gp3/io1/io2/st1/sc1), EC2 Instance Store
- **File**: EFS (NFS, multi-AZ, storage tiers), FSx (Windows/Lustre/NetApp ONTAP/OpenZFS)
- **Object**: S3 (storage classes, lifecycle, versioning, replication, encryption SSE-S3/SSE-KMS/SSE-C/client-side, bucket policies, CORS, presigned URLs)
- **Hybrid**: Snow Family (Snowball Edge), Storage Gateway (S3 File/Volume/Tape), Transfer Family (FTP/FTPS/SFTP)
- **CDN**: CloudFront (origins, caching, OAC), Global Accelerator (static IPs, Anycast)

### 3. Databases (Sections 07, 17, 19)
- **Relational**: RDS (6 engines, Multi-AZ, Read Replicas up to 15, RDS Custom, RDS Proxy), Aurora (5x MySQL/3x Postgres perf, 6 copies across 3 AZs, Global Database, Serverless, Babelfish)
- **NoSQL**: DynamoDB (serverless, DAX cache, Streams, Global Tables, TTL, S3 import/export)
- **Cache**: ElastiCache (Redis vs Memcached)
- **Purpose-built**: DocumentDB (MongoDB), Neptune (graph), Keyspaces (Cassandra), QLDB (ledger), Timestream (time-series)

### 4. Networking (Sections 06, 08, 25)
- **Load Balancing**: CLB/ALB (L7, path/host routing)/NLB (L4, static IP)/GWLB (L3, GENEVE); sticky sessions, cross-zone LB, SSL/SNI, connection draining
- **DNS**: Route 53 (A/AAAA/CNAME/Alias records, 8 routing policies, health checks, hybrid DNS resolver endpoints)
- **VPC**: subnets, IGW, NAT Gateway, NACL vs SG, VPC Peering, VPC Endpoints (Gateway free for S3/DynamoDB, Interface for others), Flow Logs, Network Firewall
- **Hybrid**: Site-to-Site VPN, Direct Connect (Dedicated/Hosted, DX Gateway), Transit Gateway (hub-and-spoke, ECMP, IP Multicast)

### 5. Security & Identity (Sections 02, 23-24)
- **IAM**: users/groups/roles, policies, permission boundaries, SCP evaluation order
- **Organizations**: OUs, SCPs (Blocklist/Allowlist), Control Tower (guardrails, Account Factory)
- **Encryption**: KMS (symmetric/asymmetric, multi-region keys), SSM Parameter Store, Secrets Manager
- **Protection**: WAF (Web ACL rules), Shield (Standard free/Advanced $3K/mo), GuardDuty (ML threat detection), Inspector (CVE scanning), Macie (PII in S3)
- **Identity**: IAM Identity Center (SSO), Directory Services, Cognito (User Pools for auth, Identity Pools for AWS credentials)

### 6. Integration & Messaging (Section 15)
- **SQS**: Standard (unlimited throughput) vs FIFO (300-3000 msg/s), visibility timeout, DLQ, long polling
- **SNS**: pub/sub, fan-out to SQS, FIFO topics, message filtering
- **Kinesis**: Data Streams (real-time, replay, 1-365 day retention), Data Firehose (near-real-time, no storage, S3/Redshift/OpenSearch destinations)
- **Amazon MQ**: managed RabbitMQ/ActiveMQ for legacy protocol migration (MQTT, AMQP, STOMP)

### 7. Monitoring & Audit (Section 22)
- **CloudWatch**: metrics, logs, alarms (composite), Unified Agent, Insights (Container/Lambda/Contributor/Application), Canary
- **CloudTrail**: API audit (Management/Data/Insights events), 90-day retention, S3+Athena for long-term
- **Config**: configuration compliance recording, 75+ managed rules, remediation via SSM Automation
- **EventBridge**: event-driven architecture, schedule/pattern, schema registry, cross-account aggregation

### 8. Data & Analytics (Section 20)
- **ETL**: Glue (serverless ETL, Data Catalog, Job Bookmarks, DataBrew, Streaming ETL)
- **Query**: Athena (serverless SQL on S3, $5/TB, Parquet/ORC best), Redshift (OLAP warehouse, Spectrum for S3)
- **Streaming**: Kinesis, MSK (managed Kafka, configurable message size up to 10MB)
- **Lake**: Lake Formation (centralized data lake, row/column-level security, built on Glue)
- **BI**: QuickSight (serverless ML-powered BI, SPICE engine)

### 9. DR & Migrations (Section 26)
- **DR strategies**: Backup & Restore → Pilot Light → Warm Standby → Multi-Site (increasing cost, decreasing RTO)
- **Migration**: DMS (homogeneous/heterogeneous DB migration, CDC), SCT (schema conversion), DRS/CloudEndure (block-level replication), Application Discovery Service, MGN (lift-and-shift)
- **Backup**: AWS Backup (centralized, cross-region/account, Vault Lock WORM)

### 10. Architecture Patterns (Sections 09, 18, 27)
- 3 progressive case studies (stateless → stateful → media-heavy)
- Serverless architectures (mobile app, blog, microservices)
- HPC patterns (Cluster placement, EFA, FSx Lustre, ParallelCluster)
- HA EC2 patterns (ASG min/max=1, EBS lifecycle hooks)
- Caching strategy layers (CloudFront → API GW → ElastiCache/DAX → DB)

### 11. Additional Services (Section 28)
- CloudFormation (IaC), SES (email), Pinpoint (marketing comms), SSM (Session Manager/Run Command/Patch Manager), Cost Explorer, Outposts, Batch, AppFlow, Amplify

### 12. Well-Architected & Exam (Sections 29-30)
- 6 pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability
- Trusted Advisor: 6 categories (Cost/Performance/Security/Fault Tolerance/Service Limits/Operational Excellence)
- Exam: 65 questions, 130 minutes, 720/1000 passing, $150 fee

---

## AI Tutor Framework (aws-certification-10x-faster.md)
- 6 specialized AI tutors: Concept Mapper, Scenario Generator, Weak Spot Analyzer, Hands-On Lab Creator, Architecture Reviewer, Exam Strategy Coach
- 3-week accelerated study plan with prompt templates
- Key insight: AWS certs test architectural thinking, not memorization

---

## Key Exam Numbers to Remember
| Metric | Value |
|--------|-------|
| EC2 Spot discount | up to 90% |
| Reserved Instance discount | up to 72% |
| RDS Read Replicas max | 15 |
| Aurora storage | 10GB-256TB auto |
| Aurora copies across AZs | 6 copies / 3 AZs |
| DynamoDB item size max | 400 KB |
| SQS message size | up to 256 KB |
| Lambda timeout | 15 minutes |
| EBS io2 Block Express IOPS | up to 256,000 |
| VPC max CIDRs | 5 per VPC |
| VPC reserved IPs per subnet | 5 |
| NAT GW throughput | 5-100 Gbps |
| Direct Connect lead time | >1 month |
| CloudTrail retention | 90 days |
| S3 durability | 99.999999999% (11 9s) |
| Route 53 SLA | 100% |
| Kinesis retention | 1-365 days |

## Unresolved Questions
- None; all 31 sections fully read and summarized.
