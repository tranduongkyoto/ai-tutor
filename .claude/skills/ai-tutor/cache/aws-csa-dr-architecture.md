# Disaster Recovery & Architecture - AWS CSA Content Cache

## Services & Concepts

### Disaster Recovery Core Concepts

- **RPO (Recovery Point Objective)**: Max acceptable data loss — gap between last backup and disaster
- **RTO (Recovery Time Objective)**: Max acceptable downtime — gap between disaster and recovery
- **DR Spectrum** (cheapest/slowest → costliest/fastest): Backup & Restore → Pilot Light → Warm Standby → Hot Site/Multi-Site

### DR Strategy 1: Backup and Restore
- Highest RPO/RTO — cheapest option
- On-prem data pushed to S3/Glacier via Storage Gateway or Snowball
- Scheduled EBS/RDS/Redshift snapshots stored in S3
- Recovery: restore AMI → EC2, restore RDS snapshot → new DB instance
- Lifecycle policy moves data S3 → S3 IA → Glacier to save cost

### DR Strategy 2: Pilot Light
- Small critical core always running in cloud (e.g., RDS replica running, EC2 stopped)
- Data continuously replicated from on-prem to RDS
- On disaster: update Route 53, start EC2 instances from AMI
- Faster than Backup & Restore because DB is already up

### DR Strategy 3: Warm Standby
- Full system running at minimum/reduced capacity in cloud
- ELB + EC2 Auto Scaling (min size) + RDS Secondary running
- On disaster: Route 53 failover, scale ASG to production load
- Higher cost than Pilot Light but faster RTO

### DR Strategy 4: Hot Site / Multi-Site
- Full production scale running in both on-prem AND AWS simultaneously
- Active-active via Route 53 weighted/latency routing
- RTO: minutes or seconds — most expensive
- All AWS Multi-Region variant: uses Aurora Global Database for cross-region replication

### AWS Elastic Disaster Recovery (DRS)
- Formerly "CloudEndure Disaster Recovery"
- Continuous block-level replication (sub-second RPO) from any source to AWS
- Agent installed on source servers (physical, virtual, or cloud)
- Staging: low-cost EC2 + EBS volumes receive continuous replication
- Failover in minutes: spin up target EC2 instances and EBS volumes
- Supports failback to original environment
- Use cases: Oracle, MySQL, SQL Server DBs; SAP; ransomware protection

### AWS Backup
- Fully managed centralized backup service — no custom scripts needed
- Supported services: EC2, EBS, S3, RDS (all engines), Aurora, DynamoDB, DocumentDB, Neptune, EFS, FSx (Lustre + Windows), Storage Gateway (Volume Gateway)
- Cross-region backup supported
- Cross-account backup supported
- Supports PITR (Point-in-Time Recovery) for supported services
- Backup Plans define: frequency, backup window, cold storage transition, retention period
- Frequency options: every 12 hours, daily, weekly, monthly, or custom cron
- Tag-based backup policies for resource targeting

#### AWS Backup Vault Lock
- WORM (Write Once Read Many) enforcement on backup vault
- Prevents: accidental/malicious deletes, retention period shortening
- Even root user cannot delete backups when Vault Lock is enabled
- Key exam signal: "prevent backup deletion even by admins/root"

### DMS (Database Migration Service)
- Migrate databases securely to AWS; source DB remains available during migration
- Runs on an EC2 replication instance you provision
- Homogeneous migration: same DB engine (e.g., Oracle → Oracle) — no SCT needed
- Heterogeneous migration: different engines (e.g., SQL Server → Aurora) — requires SCT
- Continuous Data Replication using CDC (Change Data Capture)
- Multi-AZ: synchronous standby replica in different AZ — eliminates I/O freezes, minimizes latency spikes

#### DMS Sources
- On-prem/EC2: Oracle, MS SQL Server, MySQL, MariaDB, PostgreSQL, MongoDB, SAP, DB2
- Azure SQL Database
- Amazon RDS (all, including Aurora)
- Amazon S3
- DocumentDB

#### DMS Targets
- On-prem/EC2: Oracle, MS SQL Server, MySQL, MariaDB, PostgreSQL, SAP
- Amazon RDS, Redshift, DynamoDB, S3
- OpenSearch Service, Kinesis Data Streams, Apache Kafka
- DocumentDB, Amazon Neptune
- Redis, Babelfish

### AWS Schema Conversion Tool (SCT)
- Converts DB schema from one engine to another for heterogeneous migrations
- OLTP examples: SQL Server/Oracle → MySQL/PostgreSQL/Aurora
- OLAP examples: Teradata/Oracle → Amazon Redshift
- NOT needed for same-engine migrations (e.g., on-prem PostgreSQL → RDS PostgreSQL)
- Use compute-intensive instances for faster conversions

### RDS & Aurora Migration Paths
#### MySQL
- RDS MySQL → Aurora: (1) snapshot restore, OR (2) Aurora Read Replica (promote when lag=0)
- External MySQL → Aurora: (1) Percona XtraBackup to S3 → import (faster), OR (2) mysqldump directly
- Both running: use DMS

#### PostgreSQL
- RDS PostgreSQL → Aurora: (1) snapshot restore, OR (2) Aurora Read Replica (promote when lag=0)
- External PostgreSQL → Aurora: backup to S3 → import using `aws_s3` Aurora extension
- Both running: use DMS

### AWS Application Migration Service (MGN)
- Evolution of CloudEndure Migration, replacing AWS SMS
- Lift-and-shift (rehost) to AWS with minimal downtime
- Continuous replication to low-cost staging (EC2 + EBS)
- Cutover: move to target EC2 + EBS in production
- Supports physical, virtual, cloud-based servers

### AWS Application Discovery Service
- Gathers on-prem server info to plan migrations
- Agentless Discovery (Connector): VM inventory, CPU/memory/disk performance history
- Agent-based Discovery: system config, running processes, network connection details
- Data viewable in AWS Migration Hub

### VM Import/Export
- Import existing on-prem VMs into EC2
- Export EC2 instances back to on-prem (DR repository strategy)
- Supported hypervisors: VMware, KVM, VirtualBox, Hyper-V
- Can download Amazon Linux 2 AMI as .iso for on-prem use

### VMware Cloud on AWS
- Extends on-prem VMware vCenter to AWS using native VMware tooling (vSphere, vSAN, NSX)
- DR strategy for VMware workloads
- Access AWS services (EC2, S3, RDS, FSx, Redshift) from same environment

---

## Classic Solutions Architecture Patterns

### Stateless Web App (WhatIsTheTime.com) — Evolution
1. Single EC2 + Elastic IP (single point of failure)
2. Vertical scaling (downtime required)
3. Horizontal scaling with Route 53 A Record (TTL 1hr) — removed Elastic IP
4. Add ELB + health checks + private EC2 instances + Security Groups
5. Add Auto Scaling Group across multiple AZs
6. Multi-AZ ELB → cost: reserve minimum capacity instances

### Stateful Web App (MyClothes.com) — Session Management Options
- **ELB Stickiness**: sticky sessions pin user to same instance — risk if instance fails
- **User Cookies**: store cart in cookies — stateless but cookies < 4KB, security risk
- **Server Session + ElastiCache**: store session_id in cookie, cart data in ElastiCache — preferred
  - Alternative: DynamoDB instead of ElastiCache for session storage
- **RDS for user data**: persistent user profile, address etc.
- **Read Replicas**: scale reads (RDS Master → Read Replica replication)
- **Lazy Loading via ElastiCache**: EC2 checks cache first, falls back to RDS on miss, writes to cache
- **Multi-AZ**: ElastiCache Multi-AZ + RDS Multi-AZ for disaster survival

### Stateful Web App (MyWordPress.com) — Image Storage
- **EBS**: works for single-instance (AZ-locked, not shared across instances)
- **EFS**: shared NFS via ENI per AZ — all instances see same files (distributed app)
- **Aurora MySQL**: Multi-AZ + Read Replicas instead of plain RDS MySQL

### Typical 3-Tier Web App Architecture
```
Internet → Route 53 → ELB (Multi-AZ, Public Subnet)
         → EC2 ASG (Private Subnet)
         → ElastiCache (session + cache data) + RDS (persistent data) (Data Subnet)
```

### Instantiating Applications Quickly
- **EC2**: Golden AMI (pre-baked dependencies) | User Data (dynamic config) | Hybrid (Beanstalk)
- **RDS**: Restore from snapshot (schema + data ready instantly)
- **EBS**: Restore from snapshot (disk formatted + data ready)

---

## More Solutions Architecture

### Lambda + Messaging Patterns

#### SQS + Lambda
- Lambda polls SQS queue; on failure messages go to DLQ (on SQS side)
- SQS FIFO + Lambda: blocking retry — failures block entire queue until resolved; DLQ on SQS

#### SNS + Lambda
- SNS triggers Lambda asynchronously; Lambda retries internally; on failure → Lambda DLQ (SQS)

### Fan-Out Pattern
- Problem: sending same message to multiple SQS queues requires multiple SDK calls
- Solution: publish once to SNS → multiple SQS queues subscribe to topic
- Fully decoupled, no message loss

### S3 Event Notifications
- Events: ObjectCreated, ObjectRemoved, ObjectRestore, Replication
- Destinations: SNS, SQS, Lambda
- Filter by object name (e.g., `*.jpg`)
- Delivery typically seconds, but can be up to 1 minute
- Via EventBridge: all events forwarded, advanced JSON filtering, 18+ destinations, archive/replay

### EventBridge — Intercept API Calls
- Pattern: API call → CloudTrail logs → EventBridge event → SNS alert
- Example: DynamoDB DeleteTable → CloudTrail → EventBridge → SNS notification

### API Gateway + Kinesis Integration
- Client → API Gateway → Kinesis Data Streams → Kinesis Firehose → S3
- Used to collect high-volume data without exposing Kinesis directly

### Caching Strategies (Layers)
| Layer | Service | Notes |
|-------|---------|-------|
| Edge/CDN | CloudFront | Caches static + dynamic content at edge |
| API layer | API Gateway | Response caching per stage |
| App layer | ElastiCache (Redis/Memcached) | Session, DB query results |
| DynamoDB | DAX | In-memory cache for DynamoDB |
| Static assets | S3 + CloudFront | Origin for static files |

### IP Blocking Patterns
- EC2 direct: NACL (deny rules) + Security Group (allow rules only) + optional firewall software
- With ALB: NACL at subnet level (client IP visible to NACL), ALB Security Group restricts EC2
- With NLB: NACL works (NLB passes client IP through)
- With CloudFront + ALB: NACL NOT helpful (CloudFront IPs hit NACL, not client IP); use WAF on CloudFront for IP filtering; CloudFront Geo Restriction for country-level blocking

### HPC on AWS
#### Networking
- EC2 Cluster Placement Group: same rack, same AZ, 10 Gbps network, low latency
- Enhanced Networking (SR-IOV): higher bandwidth, higher PPS, lower latency
  - ENA (Elastic Network Adapter): up to 100 Gbps
  - Intel 82599 VF: up to 10 Gbps (legacy)
- EFA (Elastic Fabric Adapter): Linux only, MPI standard, bypasses OS for ultra-low latency inter-node communication

#### Storage for HPC
- EBS io2 Block Express: up to 256,000 IOPS
- Instance Store: millions of IOPS, low latency
- FSx for Lustre: HPC-optimized distributed FS, millions of IOPS, backed by S3

#### Orchestration
- AWS Batch: multi-node parallel jobs spanning multiple EC2 instances
- AWS ParallelCluster: open-source HPC cluster management, text-file config, supports EFA

### Highly Available EC2 Instance Patterns
#### Pattern 1: CloudWatch + Lambda
- CloudWatch Event/Alarm monitors EC2 health → triggers Lambda → starts standby EC2, attaches Elastic IP

#### Pattern 2: ASG (1 min, 1 max, 1 desired, ≥2 AZ)
- EC2 User Data attaches Elastic IP by tag on launch
- EC2 instance role needed for Elastic IP API calls

#### Pattern 3: ASG + EBS
- ASG Terminate lifecycle hook → Lambda snapshots EBS with tags
- ASG Launch lifecycle hook → Lambda creates EBS from snapshot, attaches to new instance

---

## Other Services

### AWS CloudFormation
- Declarative IaC: define resources, CloudFormation creates in right order
- Infrastructure as Code — no manual resource creation
- Stack cost tracking via resource tags; cost estimation from templates
- Supports almost all AWS resources; "custom resources" for unsupported
- Infrastructure Composer (formerly CloudFormation Designer): visual diagram of stack
- CloudFormation Service Role: IAM role that allows CF to act on user's behalf; user needs only `cloudformation:*` + `iam:PassRole`

### Elastic Beanstalk
- Developer-centric PaaS on top of EC2, ASG, ELB, RDS
- Managed service: capacity, load balancing, scaling, health monitoring, instance config
- Free — pay for underlying resources
- Supported platforms: Go, Java SE, Java/Tomcat, .NET Core/Linux, .NET/Windows, Node.js, PHP, Python, Ruby, Packer, Docker (single, multi, preconfigured)
- Components: Application → Application Version → Environment (Web Server Tier or Worker Tier)
- Web Server Tier: ELB → ASG → EC2
- Worker Tier: SQS Queue → ASG → EC2; scales based on SQS message count
- Deployment modes: Single Instance (dev, Elastic IP) | High Availability with ALB (prod, Multi-AZ)

### AWS Batch
- Fully managed batch processing at any scale (100,000s of jobs)
- Batch jobs: defined as Docker images, run on ECS/EKS/Fargate
- Dynamically launches EC2 or Spot Instances
- No time limit (vs Lambda's 15-min limit)
- Relies on EBS/instance store for disk; compute managed by AWS

#### Batch vs Lambda
| Feature | Lambda | Batch |
|---------|--------|-------|
| Time limit | 15 min | None |
| Runtimes | Limited | Any (Docker) |
| Disk | Limited (/tmp 10 GB) | EBS/Instance Store |
| Compute | Serverless | EC2 (managed) |

### Amazon SES (Simple Email Service)
- Send emails at scale: transactional, marketing, bulk
- Inbound + outbound
- Supports DKIM, SPF
- Flexible IP: shared, dedicated, customer-owned
- Access via Console, API, SMTP

### Amazon Pinpoint
- 2-way marketing communications: email, SMS, push, voice, in-app
- Segment + personalize messages, receive replies
- Scales to billions of messages/day
- vs SNS/SES: Pinpoint manages templates, schedules, segments, full campaigns
- Stream events (TEXT_SUCCESS, TEXT_DELIVERED) to SNS/Kinesis Firehose/CloudWatch Logs

### AWS Systems Manager (SSM)
#### Session Manager
- Secure shell to EC2/on-prem servers without SSH, bastion hosts, or port 22
- Supports Linux, macOS, Windows
- Session logs → S3 or CloudWatch Logs

#### Run Command
- Execute scripts/commands across multiple instances via resource groups
- No SSH needed; output → Console, S3, CloudWatch Logs
- Notifications via SNS; integrated with IAM/CloudTrail; invokable via EventBridge

#### Patch Manager
- Automates OS/application/security patching on EC2 and on-prem
- On-demand or scheduled via Maintenance Windows
- Generates patch compliance reports

#### Maintenance Windows
- Scheduled windows for instance actions (patching, driver updates, software install)
- Contains: schedule, duration, registered instances, registered tasks

#### Automation
- SSM Documents (Runbooks) define actions on EC2/AWS resources
- Triggered via: Console/CLI/SDK, EventBridge, Maintenance Windows, AWS Config remediation
- Examples: restart instances (AWS-RestartEC2Instance), create AMI, EBS snapshot

### AWS Outposts
- "Server racks" installed in on-prem data centers running AWS APIs/infrastructure
- AWS manages the Outposts Rack; customer responsible for physical security
- Supported services: EC2, EBS, S3, EKS, ECS, RDS, EMR
- Benefits: low latency to on-prem systems, local data processing, data residency, easier migration

### Cost Explorer
- Visualize/manage AWS costs; custom reports; monthly/hourly/resource granularity
- Savings Plan recommendations (alternative to Reserved Instances)
- Forecast usage up to 18 months

### AWS Cost Anomaly Detection
- ML-based continuous monitoring for unusual spend
- Learns historic patterns — no threshold configuration needed
- Root-cause analysis report; alerts via SNS

### Amazon AppFlow
- Managed SaaS ↔ AWS data integration (no code required)
- Sources: Salesforce, SAP, Zendesk, Slack, ServiceNow
- Destinations: S3, Redshift, Snowflake, Salesforce
- Frequency: scheduled, event-driven, or on-demand
- Encrypted over public internet or AWS PrivateLink

### AWS Amplify
- Full-stack web/mobile app development toolset
- Backend: Cognito, S3, AppSync, API Gateway, Lambda, DynamoDB
- Frontend: React, Angular, Vue, iOS, Android, Flutter
- Amplify Console: CI/CD build + deploy via CloudFront

### Instance Scheduler on AWS
- CloudFormation solution (not a native service)
- Auto start/stop EC2, EC2 ASG, RDS instances on schedule
- Schedules stored in DynamoDB; Lambda executes via resource tags
- Cost savings up to 70%; cross-account and cross-region support

---

## Architectural Patterns

### 3-Tier Web App (Classic)
```
PUBLIC SUBNET:   Route 53 → Multi-AZ ELB
PRIVATE SUBNET:  EC2 ASG (Multi-AZ)
DATA SUBNET:     ElastiCache (sessions + cache) + RDS (persistent data)
```
Security: LB SG open to 0.0.0.0/0; EC2 SG allows only from LB SG; RDS/ElastiCache SG allows only from EC2 SG

### Multi-Region Active-Active DR (All AWS)
```
Route 53 (active-active) →  Region A: ELB → EC2 ASG → Aurora Global (primary)
                         →  Region B: ELB → EC2 ASG → Aurora Global (secondary)
Data replication: Aurora Global cross-region
Failover: Route 53 routes all traffic to healthy region
```

### Data Transfer Decision Matrix
| Method | Setup Time | Transfer Time (200 TB) | Best For |
|--------|-----------|------------------------|---------|
| Internet/VPN (100 Mbps) | Immediate | ~185 days | Small amounts |
| Direct Connect 1 Gbps | >1 month | ~18.5 days | Large ongoing |
| Snowball | Days | ~1 week | One-time large |
| DataSync + DX/VPN | Varies | Varies | Ongoing replication |

### Stateless vs Stateful App Design
- Stateless: ELB + ASG + Route 53 Alias (no shared state)
- Stateful (sessions): ElastiCache (or DynamoDB) for session storage
- Stateful (files): EFS for multi-instance shared file access; EBS for single-instance

---

## Important Numbers & Limits

| Service/Feature | Value |
|-----------------|-------|
| EBS io2 Block Express max IOPS | 256,000 IOPS |
| ENA (Enhanced Networking) max bandwidth | 100 Gbps |
| Intel 82599 VF (legacy) max bandwidth | 10 Gbps |
| EC2 Cluster Placement Group bandwidth | 10 Gbps |
| Cookie size limit for web browsers | 4 KB |
| Backup frequency minimum (AWS Backup) | Every 12 hours |
| Cost Explorer forecast horizon | 18 months |
| Pinpoint scale | Billions of messages/day |
| DRS continuous replication latency | Seconds |
| DRS failover time | Minutes |
| AWS SAA-C03 exam passing score | 720/1000 |
| AWS SAA-C03 exam questions | 65 questions in 130 min |
| AWS SAA-C03 exam fee | $150 USD |
| Exam retake waiting period | 14 days |

---

## Diagram Descriptions

### RPO/RTO Timeline Diagram
- Timeline arrow (left to right): RPO point → Disaster event → RTO point
- "Data loss" bracket spans from RPO to Disaster
- "Downtime" bracket spans from Disaster to RTO
- Smaller RPO = more frequent backups; smaller RTO = faster recovery

### DR Strategy Comparison Bar
- Left-to-right gradient bar: Backup & Restore | Pilot Light | Warm Standby | Multi Site
- Arrow above labeled "Faster RTO" pointing right
- Arrow below labeled "AWS Multi Region" spans Pilot Light → Multi Site

### Backup & Restore Architecture
- Left box: Corporate DC (servers + databases)
- Two paths: (1) Storage Gateway/Snowball → S3 → Glacier (lifecycle); (2) EBS/RDS/Redshift → scheduled snapshots
- Right box: AWS Cloud — restore to EC2 (from AMI) or RDS (from snapshot)

### Pilot Light Architecture
- Corporate DC: App Server + Primary DB
- AWS Cloud: RDS running (continuous replication from DC), EC2 NOT running
- Route 53 points to DC normally; on disaster, points to AWS and starts EC2

### Warm Standby Architecture
- Corporate DC: Reverse proxy → App Server → Primary DB
- AWS Cloud: Route 53 → ELB → EC2 ASG (minimum) → RDS Secondary (running)
- Data Replication: DC Primary DB → AWS RDS Secondary
- On disaster: failover in AWS, scale ASG to full production

### Hot Site / Multi-Site Architecture
- Both DC and AWS: active-active via Route 53
- AWS has full production-scale EC2 ASG + RDS secondary
- Route 53 routes traffic to both simultaneously

### EBS vs EFS for WordPress Images
- EBS diagram: each AZ has its own EC2 + separate EBS volume — images NOT shared between AZs
- EFS diagram: both AZs connect via ENI to single EFS — all EC2 instances see same images

### Web Server vs Worker Tier Diagram
- Web Environment: Internet → ELB → EC2 ASG (Web Servers)
- Worker Environment: SQS Queue ← EC2 ASG (Workers) pull messages; scales based on queue depth

---

## Exam-Relevant Details

### DR Strategy Selection Triggers
- "Cheapest DR" / "backup only" → Backup & Restore
- "Core database always running, minimal cost" → Pilot Light
- "Full system at reduced capacity, scale on disaster" → Warm Standby
- "Zero/near-zero RTO, active-active" → Multi-Site Hot Site
- "Continuous block-level replication" / "minutes RTO" / "failback needed" → AWS DRS (Elastic Disaster Recovery)

### Migration Service Distinctions
- **DMS**: database migration; source stays online; needs EC2 replication instance
- **MGN**: application/server migration; lift-and-shift; continuous replication
- **DRS**: disaster recovery (not migration); continuous replication + failback
- **SCT**: schema conversion only (heterogeneous); NOT needed for same-engine migrations
- **Application Discovery Service**: pre-migration assessment only; no actual migration

### Storage for Shared Files
- EBS: AZ-locked, single instance → use for single-instance apps (e.g., single WordPress)
- EFS: multi-AZ, multi-instance shared access → use for distributed/scalable apps
- S3: not a file system (no POSIX) — use for object storage, static websites, backups

### Security Group Chaining (Best Practice)
- LB Security Group: allow HTTP/HTTPS from 0.0.0.0/0
- EC2 Security Group: allow only from LB Security Group (NOT 0.0.0.0/0)
- RDS/ElastiCache Security Group: allow only from EC2 Security Group
- Trap: never open RDS/ElastiCache directly to internet

### Beanstalk Key Facts
- Free service — pay for underlying EC2/RDS/etc.
- Worker Tier scales based on SQS queue depth
- Hybrid: Golden AMI + User Data = Beanstalk's approach
- Single Instance = dev (Elastic IP); HA with Load Balancer = prod

### AWS Backup Vault Lock vs S3 Object Lock
- Both provide WORM; Backup Vault Lock applies to AWS Backup vault
- Root user CANNOT delete backups when Vault Lock enabled → strong compliance signal
- Exam trap: "prevent admins from deleting backups" → Backup Vault Lock

### IP Blocking with CloudFront
- NACL is NOT helpful when CloudFront is in front (NACL sees CloudFront IPs, not client IPs)
- Correct approach: WAF on CloudFront (IP filtering) + CloudFront Geo Restriction (country blocking)

### DMS Multi-AZ
- Provisions synchronous standby replica in different AZ
- Benefits: data redundancy, eliminates I/O freezes, minimizes latency spikes
- Different from RDS Multi-AZ but same concept applied to replication instance

### Well-Architected Framework
- 6 Pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability
- Pillars are a SYNERGY — not trade-offs
- Well-Architected Tool: free, review workloads against 6 pillars, generate reports
- Trusted Advisor: 6 categories (Cost, Performance, Security, Fault Tolerance, Service Limits, Operational Excellence); full checks require Business or Enterprise support plan

### Common Exam Traps
- "Same DB engine migration" → DMS without SCT (trap: SCT not needed)
- "RDS MySQL → Aurora" fastest zero-downtime → Aurora Read Replica (promote at lag=0)
- "External MySQL → Aurora" fastest → Percona XtraBackup to S3 (not mysqldump)
- "Block specific IPs from CloudFront" → WAF, NOT NACL
- "Prevent root from deleting backups" → AWS Backup Vault Lock
- "Continuous replication with failback" → DRS not MGN (MGN is cutover only, no failback)
- "Session data" → ElastiCache (primary) or DynamoDB (alternative)
- "Multi-AZ ELB" → ELB itself spans AZs (it IS Multi-AZ by nature when configured)
- "Cookies limit" → 4 KB maximum

### Keywords → Service Mapping
| Keyword/Scenario | Service |
|------------------|---------|
| "Block-level replication", "failback" | AWS DRS (Elastic Disaster Recovery) |
| "Lift-and-shift", "rehost servers" | AWS MGN (Application Migration Service) |
| "DB migration, source stays up" | AWS DMS |
| "Schema conversion", different DB engine | AWS SCT |
| "Gather on-prem inventory before migration" | Application Discovery Service |
| "Centralized backup, cross-account" | AWS Backup |
| "WORM backups, root can't delete" | Backup Vault Lock |
| "SaaS to AWS data transfer" | Amazon AppFlow |
| "Run commands on EC2 without SSH" | SSM Run Command / Session Manager |
| "Automated OS patching at scale" | SSM Patch Manager |
| "Full-stack web/mobile app toolset" | AWS Amplify |
| "On-prem with AWS APIs, data residency" | AWS Outposts |
| "Extend VMware to AWS" | VMware Cloud on AWS |
| "Bulk/transactional email at scale" | Amazon SES |
| "Multi-channel marketing campaigns" | Amazon Pinpoint |
| "Detect unusual AWS spend via ML" | Cost Anomaly Detection |
| "Forecast AWS costs 18 months" | Cost Explorer |
