# Practice Test #4 — Progress Tracker
**Source:** `practice-test-4-questions.md` (65 questions)
**Started:** 2026-07-29

## Domain Progress

| Domain | Questions | Score | Status |
|--------|-----------|-------|--------|
| Design Secure Architectures | 15 | 8/15 (53%) | Done |
| Design High-Performing Architectures | 20 | 14/20 (70%) | Done |
| Design Resilient Architectures | 19 | 12/19 (63%) | Done |
| Design Cost-Optimized Architectures | 11 | 6/11 (55%) | Done |

## Design Secure Architectures — 8/15 (53%)

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 7 | S3 cross-account access | C | B | Wrong |
| 2 | 8 | ELB unhealthy instances | B,D | B,D | Correct |
| 3 | 9 | SSO across Organizations + on-prem AD | D | B | Wrong |
| 4 | 12 | CloudFormation SG snippet | B,F,G | B,F,G | Correct |
| 5 | 13 | IAM resource-based policy | B | C | Wrong |
| 6 | 14 | Direct Connect + VPN backup | C,D | C,D | Correct |
| 7 | 20 | S3 Object Lock vs Glacier Vault Lock | D | B | Wrong |
| 8 | 21 | S3 bucket policy (CIDR + NotIP) | C | C | Correct |
| 9 | 33 | SG: allow traffic from ALB only | C | A | Wrong |
| 10 | 41 | Lambda → RDS short-lived credentials | B,C | B,D | Wrong |
| 11 | 43 | Multiple domains HTTPS on one LB | C | C | Correct |
| 12 | 48 | Cross-region Direct Connect gateway | B | B | Correct |
| 13 | 50 | Gateway Endpoints (S3 + DynamoDB) | C,D | C,D | Correct |
| 14 | 52 | RDS data-in-transit security | A | B | Wrong |
| 15 | 63 | Can't ping EC2 troubleshooting | C,D | C,D | Correct |

### Weak Areas — Secure Architectures
1. **S3 cross-account** — must use bucket policy (user policies don't work cross-account)
2. **IAM Identity Center** — for enterprise SSO across Organizations (not Cognito)
3. **Trust policy** — only resource-based policy IAM supports (not ACL)
4. **Object Lock Compliance vs Governance** — Compliance truly immutable; Governance overridable
5. **SG reference vs CIDR** — reference ALB's SG, not subnet CIDR
6. **IAM auth to RDS** — generates short-lived tokens (not SSM credential rotation)
7. **SSL for data-in-transit** — SSL encrypts network data; IAM auth is authentication only

## Design High-Performing Architectures — 14/20 (70%)

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 1 | Transit Gateway + ECMP for VPN throughput | D | A | Wrong |
| 2 | 10 | Tape Gateway for tape backup workflow | C | B | Wrong |
| 3 | 11 | Real-time analytics pipeline | A | A | Correct |
| 4 | 17 | EFS mount targets per AZ | A | A | Correct |
| 5 | 18 | CloudFormation for RDS best practices | D | D | Correct |
| 6 | 22 | Flash sale 10x dynamic content | C | C | Correct (redo) |
| 7 | 27 | Geoproximity routing (dynamic geo area) | D | D | Correct (redo) |
| 8 | 34 | Neptune for graph queries | B | B | Correct |
| 9 | 37 | Amazon MQ for MQTT protocol | A | A | Correct |
| 10 | 42 | Transit Gateway as central hub | C | C | Correct (redo) |
| 11 | 44 | Global Accelerator for multi-region ALBs | B | A | Wrong |
| 12 | 46 | DMS as S3→Kinesis bridge | A | B | Wrong |
| 13 | 51 | Cluster placement group for HPC | C | C | Correct |
| 14 | 53 | DynamoDB on-demand for unpredictable spikes | D | D | Correct (redo) |
| 15 | 55 | Aurora I/O-Optimized storage | B | B | Correct (redo) |
| 16 | 57 | DynamoDB DAX for hot partition | A | A | Correct |

| 17 | 58 | Lambda serverless best practices | A,B,C | B,C,D | Wrong |
| 18 | 61 | Cluster placement group for HPC | A | A | Correct |
| 19 | 62 | Cross-zone LB disabled traffic split | D | D | Correct |
| 20 | 65 | ElastiCache Redis for real-time GPS | A | D | Wrong |

### Weak Areas (restart) — High-Performing
1. **Transit Gateway + ECMP** — aggregates VPN bandwidth across multiple tunnels (still missed)
2. **Tape Gateway** — preserves tape backup workflows; DataSync requires workflow change
3. **Global Accelerator** — provides 2 static anycast IPs for multi-region ALB whitelisting
4. **DMS S3→Kinesis** — DMS natively supports S3 as source + Kinesis as target (still missed)
5. **Lambda container images** — Lambda supports container images up to 10 GB; monitor with CW Alarms on ConcurrentExecutions
6. **ElastiCache for ephemeral data** — Redis for high-frequency read+write of short-lived data (GPS, sessions); read replicas only solve read bottleneck, not writes

## Design Resilient Architectures — 12/19 (63%)

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 2 | S3 multipart upload for large files | C | C | Correct |
| 2 | 4 | CloudFront routing, security, HA | A,E,F | A,B,E | Wrong |
| 3 | 5 | DR strategy scaled-down full env | B | A | Wrong |
| 4 | 6 | Container orchestration serverless | A,B | A,B | Correct |
| 5 | 15 | EKS node auto-scaling for pods | A | C | Wrong |
| 6 | 19 | Route 53 TTL after LB change | A | A | Correct |
| 7 | 28 | Golden AMI + User Data for fast boot | A,D | A,D | Correct |
| 8 | 30 | RDS read throughput scaling | C | C | Correct |
| 9 | 31 | NoSQL serverless for GPS tracking | B | B | Correct |
| 10 | 32 | SaaS inter-app + third-party decouple | C | D | Wrong |
| 11 | 35 | NLB static IP for whitelisting | A | A | Correct |
| 12 | 36 | Cross-region S3 one-time copy 1PB | A,D | A,C | Wrong |
| 13 | 39 | Cross-region DR 5min RTO with AMI | A | A | Correct |
| 14 | 45 | VPC peering for 5 VPCs cost-effective | D | D | Correct |
| 15 | 54 | ElastiCache Redis Multi-AZ failover | A | A | Correct |
| 16 | 56 | ASG scale-in oldest in largest AZ | D | D | Correct |
| 17 | 59 | ELB wildcard host-based routing | C | C | Correct |
| 18 | 60 | SQL Server migration max HA min ops | C | B | Wrong |
| 19 | 64 | DynamoDB deletion protection | C | C | Correct |

### Weak Areas — Resilient Architectures
1. **CloudFront field-level encryption** — CloudFront feature for encrypting sensitive fields at edge (not KMS)
2. **Warm Standby vs Pilot Light** — Warm Standby = scaled-down FULL environment running; Pilot Light = core only (DB)
3. **Kubernetes Cluster Autoscaler** — scales EKS worker nodes based on pending pods; CW alarms don't understand K8s scheduling
4. **EventBridge for SaaS integration** — EventBridge natively integrates with third-party SaaS apps; SQS is point-to-point
5. **S3 Batch Replication** — one-time cross-region copy of existing objects; S3TA only accelerates client uploads
6. **RDS SQL Server Multi-AZ** — cross-region Multi-AZ doesn't exist for RDS; use same-region Multi-AZ for HA

## Design Cost-Optimized Architectures — 6/11 (55%)

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 3 | API Gateway caching for read-heavy | C | D | Wrong |
| 2 | 16 | KMS CMK auto rotation for S3 archive | C | C | Correct |
| 3 | 23 | S3 lifecycle prefix + all objects | B,D | A,D | Wrong |
| 4 | 24 | Predictive + dynamic scaling | B | B | Correct |
| 5 | 25 | EFS burst throughput mode | A | B | Wrong |
| 6 | 26 | Cost Optimization Hub + Compute Optimizer | B | B | Correct |
| 7 | 29 | Spot + SQS for async image processing | B,C | A,B | Wrong |
| 8 | 38 | ElastiCache Redis for repeated queries | B | B | Correct |
| 9 | 40 | EBS io1 to gp2 for cost savings | D | D | Correct |
| 10 | 47 | Min capacity 2 + RI for baseline | B,C | B,C | Correct |
| 11 | 49 | Storage Gateway cached volumes hybrid | A | B | Wrong |

### Weak Areas — Cost-Optimized Architectures
1. **API Gateway Caching** — enable caching with TTL at API Gateway level; no "Lambda In Memory Caching" feature
2. **S3 Lifecycle scope** — use prefix for per-folder rules; "all objects" when both folders transition at same time
3. **EFS burst throughput** — General Purpose + Standard + burst mode for sporadic bursts; IA adds latency on first access
4. **Spot Instances for async** — SQS retries handle Spot interruptions; clients willing to wait = fault-tolerant = Spot
5. **Storage Gateway cached volumes** — primary data in S3, hot cache local; stored volumes = full data local

## Overall Summary

**TOTAL: 40/65 (62%) — FAIL** (need ≥72% to pass)

| Domain | Score | Pct | Status |
|--------|-------|-----|--------|
| Design Secure Architectures | 8/15 | 53% | ✗ |
| Design High-Performing Architectures | 14/20 | 70% | BORDERLINE |
| Design Resilient Architectures | 12/19 | 63% | ✗ |
| Design Cost-Optimized Architectures | 6/11 | 55% | ✗ |
| **TOTAL** | **40/65** | **62%** | **FAIL** |

### Priority Study Areas
1. **Secure Architectures (53%)** — S3 cross-account policies, IAM Identity Center, Object Lock, SG referencing, IAM auth to RDS, SSL vs IAM
2. **Cost-Optimized (55%)** — API Gateway caching, S3 lifecycle rules, EFS throughput modes, Spot Instances, Storage Gateway cached vs stored
3. **Resilient (63%)** — CloudFront field-level encryption, Warm Standby vs Pilot Light, K8s Cluster Autoscaler, EventBridge SaaS, S3 Batch Replication
4. **High-Performing (70%)** — Transit Gateway ECMP, Tape Gateway, Global Accelerator static IPs, DMS S3→Kinesis, Lambda containers
