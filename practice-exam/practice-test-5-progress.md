# Practice Test #5 — Progress Tracker
**Source:** `practice-test-5-questions.md` (65 questions)
**Started:** 2026-08-03

## Domain Progress

| Domain | Questions | Score | Status |
|--------|-----------|-------|--------|
| Design Secure Architectures | 18 | 15/18 (83%) | Done |

## Design Secure Architectures

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 1 | Site-to-Site VPN encrypted connectivity | C | C | Correct |
| 2 | 3 | Gateway VPC endpoint for S3 | D | D | Correct |
| 3 | 7 | CloudFront OAC + ACM us-east-1 | A, B | A, C | Wrong |
| 4 | 8 | Transit Gateway full mesh VPCs | D | D | Correct |
| 5 | 11 | Site-to-Site VPN fastest encrypted | A | A | Correct |
| 6 | 14 | S3 Object Lock Compliance Mode WORM | B | B | Correct |
| 7 | 20 | PrivateLink for SaaS private access | A | A | Correct |
| 8 | 28 | RDS SG inbound rule for app servers | C | C | Correct |
| 9 | 32 | WAF + CloudFront for SQLi/XSS | B | B | Correct |
| 10 | 34 | IAM Access Analyzer external sharing | D | A | Wrong |
| 11 | 36 | WAF geo match + IP set exception | C, D | C, D | Correct |
| 12 | 40 | WAF on CloudFront for EC2 apps | B | B | Correct |
| 13 | 46 | Transfer Family EFS POSIX SFTP | C | A | Wrong |
| 14 | 48 | Glacier Vault Lock compliance | B | B | Correct |
| 15 | 50 | EBS encryption capabilities | B, C, F | B, C, F | Correct |
| 16 | 52 | S3 Bucket Keys reduce KMS cost | B | B | Correct |
| 17 | 56 | NACL + route table for IGW access | A, B | A, B | Correct |
| 18 | 63 | SCP + tag policy for EC2 tagging | A, B | A, B | Correct |

### Weak Areas — Secure Architectures
1. **CloudFront OAC vs OAI** — OAC is the current best practice for CloudFront→S3 access control. OAC supports uploads (PUT/POST), unlike legacy OAI. S3 static website endpoint does NOT support HTTPS.
2. **IAM Access Analyzer vs Inspector** — Access Analyzer analyzes IAM/resource policies for unintended external access (S3, IAM roles, KMS, SNS). Inspector scans for software vulnerabilities on EC2/containers, NOT policy analysis.
3. **Transfer Family + EFS vs S3** — For SFTP with POSIX file-level access and high IOPS, EFS is correct (preserves Linux user model). S3 is object storage without POSIX support. Transfer Family in VPC with EIPs enables IP-based restriction.
| Design High-Performing Architectures | 21 | 12/21 (57%) | Done |

## Design High-Performing Architectures

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 2 | EBS Provisioned IOPS for high IOPS DB | A | A | Correct |
| 2 | 4 | EBS Fast Snapshot Restore for clones | C | A | Wrong |
| 3 | 6 | DMS Serverless auto-scaling replication | B | B | Correct |
| 4 | 12 | S3 event + Lambda thumbnail | D | D | Correct |
| 5 | 21 | DynamoDB global tables multi-Region | A | D | Wrong |
| 6 | 23 | Kinesis batch messages reduce cost | C | C | Correct |
| 7 | 24 | DataSync migrate + File Gateway ongoing | A | C | Wrong |
| 8 | 26 | EC2 Instance Connect temp key | C | C | Correct |
| 9 | 27 | S3TA + CloudFront for remote uploads | A, C | A, C | Correct |
| 10 | 30 | KDS multi-consumer vs Firehose | B | C | Wrong |
| 11 | 33 | KDS Enhanced Fanout for consumers | D | D | Correct |
| 12 | 35 | Instance Store + S3 + Glacier tiers | B | A | Wrong |
| 13 | 37 | API GW + SQS + Comprehend sentiment | C | D | Wrong |
| 14 | 42 | CloudWatch Logs agent for ASG logs | B | B | Correct |
| 15 | 43 | Redis geospatial caching | D | A | Wrong |
| 16 | 44 | Reserved + Spot for SQS processing | C | D | Wrong |
| 17 | 45 | Global Accelerator cross-Region failover | D | D | Correct |
| 18 | 51 | DynamoDB global tables + provisioned AS | D | D | Correct |
| 19 | 54 | Transcribe + Athena ad-hoc SQL | A | D | Wrong |
| 20 | 61 | ElastiCache session management | C | C | Correct |
| 21 | 64 | NLB TCP/UDP + Global Accelerator | B, D | B, D | Correct |

### Weak Areas — High-Performing Architectures
1. **EBS Fast Snapshot Restore** — FSR pre-warms volumes from snapshots for immediate full I/O performance. Without FSR, new volumes have degraded performance until blocks are fetched from S3. Use for "high consistent I/O + minimize provisioning time."
2. **DynamoDB Global Tables vs RDS replicas** — Global tables support multi-Region multi-active writes with sub-second replication. RDS/Aurora cross-Region replicas are read-only — all writes go to primary Region.
3. **DataSync vs File Gateway** — DataSync = bulk migration tool (hundreds of TBs). File Gateway = ongoing access/caching layer for on-premises apps. Use DataSync to migrate, then File Gateway for ongoing access.
4. **Kinesis Data Streams vs Firehose** — Data Streams supports multiple independent consumers (fan-out). Firehose is a single-destination delivery stream (S3, Redshift, OpenSearch). "Share with multiple apps" = Data Streams.
5. **Instance Store vs Storage Gateway** — "Maximum I/O performance" = instance store (NVMe, physically attached). Storage Gateway is for hybrid on-premises access, not max I/O.
6. **Comprehend vs Transcribe vs Translate** — Comprehend = sentiment analysis. Transcribe = speech→text. Translate = language translation. QuickSight = visualization. Athena = ad-hoc SQL.
7. **Redis vs Global Accelerator** — Redis supports geospatial data types (GEOADD, GEODIST). Global Accelerator is a networking service, not a cache.
8. **Reserved + Spot for queue workloads** — SQS workloads are Spot-friendly (message returns to queue on interruption). Use Spot for spikes over On-Demand to save cost.
| Design Resilient Architectures | 16 | 14/16 (88%) | Done |

## Design Resilient Architectures

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 5 | SSM Automation + Maintenance Windows | B, E | B, E | Correct |
| 2 | 9 | EC2 detailed monitoring 1-min | A | B | Wrong |
| 3 | 10 | EFS + AWS Backup cross-Region | D | D | Correct |
| 4 | 13 | ASG+ALB + Aurora read replicas | C, D | C, D | Correct |
| 5 | 15 | Recycle Bin snapshot retention | C | C | Correct |
| 6 | 16 | ASG EC2 health vs ALB health check | A | A | Correct |
| 7 | 18 | CRR + SSE-KMS MRK + Athena | D | D | Correct |
| 8 | 25 | RDS cross-Region backup + replicas | B, E | B, E | Correct |
| 9 | 31 | SQS dead-letter queue failures | D | D | Correct |
| 10 | 38 | RDS Multi-AZ CNAME failover | D | D | Correct |
| 11 | 39 | Aurora reader endpoint offload | C, E | C | Wrong |
| 12 | 41 | Route 53 active-passive failover | C | C | Correct |
| 13 | 47 | ASG min=4 across 2 AZs for HA | A | A | Correct |
| 14 | 49 | ASG + Spot + ALB for stateless app | C | C | Correct |
| 15 | 57 | Kinesis + OpenSearch + QuickSight | C | C | Correct |
| 16 | 60 | 2 SQS queues + scale on msg count | B | B | Correct |

### Weak Areas — Resilient Architectures
1. **EC2 detailed monitoring** — Detailed monitoring = 1-minute intervals (vs basic 5-min). Just enable it — no agent needed. "Quick to implement + low-maintenance" = simplest built-in option.
2. **Aurora replica vs standby** — Aurora uses replicas (not standbys like RDS Multi-AZ). Replicas serve dual purpose: read scaling + automatic failover target. "Standby" is incorrect Aurora terminology.
| Design Cost-Optimized Architectures | 10 | 7/10 (70%) | Done |

## Design Cost-Optimized Architectures

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 17 | S3 File Gateway on-prem cache | A | C | Wrong |
| 2 | 19 | Instance Store temp high IOPS | A | A | Correct |
| 3 | 22 | DX egress cheaper than internet | C | A | Wrong |
| 4 | 29 | CloudWatch EC2 Reboot alarm action | A | D | Wrong |
| 5 | 53 | Athena SQL on S3 data lake | B | B | Correct |
| 6 | 55 | Global Accelerator for global API | A | A | Correct |
| 7 | 58 | S3 Standard-IA immediate access | B | B | Correct |
| 8 | 59 | S3 Intelligent-Tiering for archive | D | D | Correct |
| 9 | 62 | S3 Intelligent-Tiering auto-tier | A | A | Correct |
| 10 | 65 | Snowball to S3 then lifecycle Glacier | B | B | Correct |

### Weak Areas — Cost-Optimized Architectures
1. **S3 File Gateway** — For on-premises apps needing low-latency access to S3 data, File Gateway provides a local NFS/SMB cache. FSx Lustre is for HPC, not general file serving.
2. **DX egress vs Internet egress** — Direct Connect data transfer out is cheaper than Internet egress. Deploy viz tool in AWS (keep large queries internal), access via DX (cheaper than internet for the small webpage).
3. **CloudWatch EC2 Alarm Actions** — Built-in actions: Stop, Terminate, Reboot, Recover. No Lambda/SNS needed for simple EC2 lifecycle automation. "Most cost-optimal" = fewest services.

## Overall Summary

**TOTAL: 48/65 (74%)**
**Result: PASS (≥72%)**

| Domain | Score | Pct |
|--------|-------|-----|
| Design Secure Architectures | 15/18 | 83% |
| Design High-Performing Architectures | 12/21 | 57% |
| Design Resilient Architectures | 14/16 | 88% |
| Design Cost-Optimized Architectures | 7/10 | 70% |
