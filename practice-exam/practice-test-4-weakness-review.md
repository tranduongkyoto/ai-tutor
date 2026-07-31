# Practice Test #4 — Weakness Review

**Score: 40/65 (62%) — FAIL** | 25 wrong answers across 4 domains
**Date:** 2026-07-31

---

## Design Secure Architectures — 8/15 (53%) — 7 errors

### Q7: S3 Cross-Account Access
**Your answer:** C | **Correct:** B — Bucket policy for cross-account

Cross-account S3 access requires a **bucket policy** on the destination account granting permissions to the source account. IAM user policies in the source account alone cannot grant access to resources in another account. Bucket policies are resource-based policies that can reference external AWS account principals.

**Rule:** Cross-account = resource-based policy (bucket policy). Same-account = IAM user/role policy works.

---

### Q9: SSO Across Organizations + On-Prem AD
**Your answer:** D | **Correct:** B — IAM Identity Center + AWS Directory Service + two-way trust

For enterprise SSO across multiple AWS accounts with on-premises Active Directory:
1. Deploy **AWS IAM Identity Center** (successor to AWS SSO)
2. Use **AWS Directory Service for Microsoft AD** (Enterprise Edition)
3. Establish **two-way trust** between managed AD and on-prem AD

**Rule:** Cognito = customer-facing apps. IAM Identity Center = workforce/employee SSO across AWS accounts.

---

### Q13: IAM Resource-Based Policy Type
**Your answer:** B | **Correct:** C — Trust policy

IAM supports only one type of resource-based policy: the **trust policy** attached to IAM roles. Trust policies define which principals (users, roles, services, accounts) can assume the role. IAM does not support ACLs or other resource-based policy types.

**Rule:** IAM resource-based policy = trust policy only. S3/SQS/Lambda have their own resource-based policies.

---

### Q20: S3 Object Lock vs Glacier Vault Lock
**Your answer:** D | **Correct:** B — Object Lock Compliance + Glacier Vault Lock

- **S3 Object Lock Compliance mode** = truly immutable, nobody can delete (not even root). For regulatory retention.
- **S3 Object Lock Governance mode** = can be overridden by users with special permissions.
- **S3 Glacier Vault Lock** = immutable vault-level policy for Glacier archives.

**Rule:** "Cannot be deleted by anyone" = Compliance mode. "Admin can override" = Governance mode.

---

### Q33: SG — Allow Traffic from ALB Only
**Your answer:** C (CIDR-based rule) | **Correct:** A — Reference the ALB's security group

To allow traffic only from an ALB to backend instances, reference the **ALB's security group ID** in the instance's SG inbound rule — not the subnet CIDR. SG referencing ensures only traffic originating from the ALB (not other resources in the same subnet) is allowed.

**Rule:** SG-to-SG referencing > CIDR for service-to-service access control.

---

### Q41: Lambda → RDS Short-Lived Credentials
**Your answer:** B,C | **Correct:** B,D — IAM role on Lambda + IAM auth to RDS

- **B:** Attach IAM role to Lambda (execution role for AWS API access)
- **D:** Use **IAM authentication** to RDS PostgreSQL — generates short-lived auth tokens (15 min) instead of storing DB passwords

IAM auth to RDS uses `rds-db:connect` IAM action + generates temporary tokens via `aws rds generate-db-auth-token`.

**Rule:** "Short-lived credentials to RDS" = IAM database authentication. Not SSM Parameter Store credential rotation.

---

### Q52: RDS Data-in-Transit Security
**Your answer:** A (IAM auth) | **Correct:** B — SSL for data in transit

- **SSL/TLS** encrypts data **in transit** (network level)
- **IAM authentication** handles **authentication** (who can connect), NOT encryption

These are separate concerns. IAM auth generates a token to prove identity; SSL encrypts the actual data flowing over the network.

**Rule:** Data in transit = SSL/TLS. Authentication = IAM auth. They complement each other but solve different problems.

---

## Design High-Performing Architectures — 14/20 (70%) — 6 errors

### Q1: Transit Gateway + ECMP for VPN Throughput
**Your answer:** D | **Correct:** A — Transit Gateway with ECMP + additional VPN tunnels

**Equal Cost Multi-Path (ECMP)** routing on Transit Gateway aggregates bandwidth across multiple VPN tunnels. Each Site-to-Site VPN tunnel provides ~1.25 Gbps. With ECMP, adding more tunnels linearly increases total throughput.

**Rule:** Need more VPN bandwidth? TGW + ECMP + more tunnels. Single VPN connection = max 2 tunnels (active/passive). TGW enables active/active across multiple connections.

---

### Q10: Tape Gateway for Tape Backup Workflow
**Your answer:** C | **Correct:** B — Tape Gateway preserves existing tape workflows

**Tape Gateway** presents virtual tape libraries (VTL) to existing backup software. The application continues using its tape backup workflow unchanged — tapes are stored in S3/Glacier instead of physical tapes.

**DataSync** is for file-based transfers and would require changing the backup workflow entirely.

**Rule:** "Preserve existing tape backup workflow" = Tape Gateway. "File-based migration" = DataSync.

---

### Q44: Global Accelerator for Multi-Region ALB Whitelisting
**Your answer:** B | **Correct:** A — Global Accelerator provides 2 static anycast IPs

Global Accelerator gives you **2 static anycast IP addresses** that route traffic to the nearest healthy ALB across regions. These static IPs can be whitelisted in on-premises firewalls.

ALBs have dynamic IPs that change — you can't whitelist them. NLBs have static IPs but are per-region, not global.

**Rule:** "Static IPs for global multi-region" = Global Accelerator. "Static IPs per region" = NLB. "Dynamic IPs" = ALB.

---

### Q46: DMS as S3→Kinesis Bridge
**Your answer:** A | **Correct:** B — DMS supports S3 as source and Kinesis as target

AWS Database Migration Service natively supports:
- **S3 as a source** (reads CSV/Parquet files)
- **Kinesis Data Streams as a target** (writes change records)

This makes DMS a bridge for S3→Kinesis data pipelines without custom code.

**Rule:** DMS isn't just for database-to-database. It supports S3, Kinesis, Kafka, DocumentDB, and more as sources/targets.

---

### Q58: Lambda Serverless Best Practices (Select 3)
**Your answer:** A,B,C | **Correct:** B,C,D

- **A is FALSE** — Lambda DOES support container images (up to 10 GB). You can package Lambda functions as Docker containers.
- **B is TRUE** — Lambda Layers for reusable code across functions
- **C is TRUE** — VPC-enabled Lambda needs NAT Gateway for public internet access
- **D is TRUE** — CloudWatch Alarms on ConcurrentExecutions/Invocations for monitoring runaway scaling
- **E is FALSE** — AWS recommends right-sizing timeout, not over-provisioning
- **F is FALSE** — Lambda Layers are the solution, not "separate packages"

**Rule:** Lambda supports containers. Monitor with CW Alarms on concurrency metrics.

---

### Q65: ElastiCache Redis for Real-Time GPS
**Your answer:** A (read replicas) | **Correct:** D — ElastiCache Redis with TTL

For high-frequency reads AND writes of ephemeral data (GPS coordinates):
- **Redis** provides sub-ms latency for both reads and writes
- TTL-based eviction naturally handles constantly-changing location data
- Read replicas only help reads, not writes — the primary DB write bottleneck remains

**Rule:** Ephemeral, frequently-updated data with high read+write = Redis cache. Read replicas = read-only scaling.

---

## Design Resilient Architectures — 12/19 (63%) — 7 errors

### Q4: CloudFront Capabilities (Select 3)
**Your answer:** A,E,F | **Correct:** A,B,E

- **A:** Origin groups for HA/failover ✓
- **B:** **Field-level encryption** — CloudFront-specific feature encrypting sensitive POST fields at edge with public key. Only your app (with private key) can decrypt.
- **E:** Content-type-based routing (path patterns to different origins) ✓
- **F is WRONG** — KMS encryption is for S3/EBS, not a CloudFront feature

**Rule:** CloudFront security = Field-level encryption (edge-level, per-field). KMS = storage encryption.

---

### Q5: DR Strategy — Scaled-Down Full Environment
**Your answer:** B (Pilot Light) | **Correct:** A — Warm Standby

| Strategy | What's Running | RTO |
|----------|---------------|-----|
| Backup & Restore | Nothing | Hours |
| **Pilot Light** | **Core only (DB replication)** | **10s of min** |
| **Warm Standby** | **Scaled-down FULL environment** | **Minutes** |
| Multi-Site | Full production copy | Near-zero |

**Key difference:** Pilot Light = only essential core (database). Warm Standby = complete but smaller version of production (app servers + DB + networking, all running).

**Rule:** "Scaled-down version of fully functional" = Warm Standby. "Minimum core infrastructure" = Pilot Light.

---

### Q15: EKS Node Auto-Scaling
**Your answer:** A (EC2 ASG + CW alarms) | **Correct:** C — Kubernetes Cluster Autoscaler

The **Kubernetes Cluster Autoscaler** is the standard solution:
- Watches for **pending (unschedulable) pods**
- Triggers EC2 ASG to add/remove nodes
- Kubernetes-native, understands pod resource requests

Custom CloudWatch alarms on CPU/memory don't understand Kubernetes scheduling. CPU might be fine but pods can't schedule due to memory/affinity constraints.

**Rule:** EKS node scaling = Cluster Autoscaler (K8s-native). Pod scaling = Horizontal Pod Autoscaler (HPA).

---

### Q32: SaaS Inter-App + Third-Party Decoupling
**Your answer:** C (SQS) | **Correct:** D — Amazon EventBridge

**EventBridge** is designed for event-driven architectures with:
- Native **SaaS partner integrations** (Zendesk, Datadog, PagerDuty, etc.)
- **Rules-based event filtering** and routing to multiple targets
- Cross-account event delivery

**SQS** is point-to-point (one consumer per message) and has no SaaS integration.

**Rule:** "SaaS app feeds to multiple in-house + third-party apps" = EventBridge. "Queue for one consumer" = SQS.

---

### Q36: Cross-Region S3 One-Time Copy (1 PB)
**Your answer:** A,D | **Correct:** A,C

- **A:** `aws s3 sync` — works for cross-region copy ✓
- **C:** **S3 Batch Replication** — replicates existing objects on-demand (unlike live replication which only handles new objects). Set up, copy, delete config.
- **D is WRONG** — S3 Transfer Acceleration speeds uploads FROM CLIENTS to S3 using CloudFront edges. It does NOT copy between buckets.

**Rule:** Copy existing objects cross-region = `s3 sync` or S3 Batch Replication. S3TA = accelerate client→S3 uploads only.

---

### Q60: SQL Server Migration — Max HA, Min Ops
**Your answer:** C (cross-region Multi-AZ) | **Correct:** B — RDS Multi-AZ (single region)

**Cross-region Multi-AZ does not exist for RDS.** Multi-AZ is always within a single Region (across AZs in that Region). For cross-region redundancy, you'd use read replicas or Aurora Global Database.

RDS Multi-AZ provides: automatic failover, synchronous replication, managed backups/patching — all with minimal operational overhead.

**Rule:** RDS Multi-AZ = single region, cross-AZ. "Cross-region Multi-AZ" is a made-up option — always a distractor.

---

## Design Cost-Optimized Architectures — 6/11 (55%) — 5 errors

### Q3: API Gateway Caching for Read-Heavy API
**Your answer:** C (Lambda In Memory Caching) | **Correct:** D — API Gateway Caching

**API Gateway Caching** is a built-in feature — enable it with a TTL (e.g., 24 hours). Cached responses are served directly from the gateway without invoking Lambda or hitting Aurora.

"Lambda In Memory Caching" is NOT a real AWS feature. Lambda functions are stateless/ephemeral — variables don't persist across invocations reliably.

**Rule:** Read-heavy API with stale-tolerant data + minimal changes = API Gateway Cache. Not Lambda-level caching.

---

### Q23: S3 Lifecycle — Prefix vs All Objects
**Your answer:** B,D | **Correct:** A,D

- **D:** Prefix `images/` → Standard IA after 45 days (only images become infrequent) ✓
- **A:** ALL objects → Glacier after 180 days (BOTH images and thumbnails archive at 180 days)
- **B is WRONG** — prefix-based Glacier at 180 days would only target one folder, but BOTH need archiving

**Rule:** When ALL objects share the same transition timing → use "all objects" rule. When only some objects → use prefix filter.

---

### Q25: EFS Burst Throughput for Sporadic Workloads
**Your answer:** A (EFS IA) | **Correct:** B — Burst throughput + General Purpose + Standard

EFS **burst throughput mode** accumulates burst credits during low-usage periods, then allows high throughput during spikes. Perfect for "sporadic bursts with low average demand."

**EFS Infrequent Access (IA)** introduces higher latency on first access (files retrieved from IA tier) — bad for burst workloads that need fast access.

**Rule:** Sporadic bursts + low average = burst throughput (default). Rarely accessed cold files = IA storage class.

---

### Q29: Minimize Cost for Async Image Processing
**Your answer:** B,C | **Correct:** A,B — Spot Instances + SQS

- **SQS** — async processing, retry on failure, decoupling ✓
- **Spot Instances** — up to 90% cheaper than On-Demand. Safe here because:
  - Clients are willing to wait (fault-tolerant workload)
  - SQS handles retries if Spot instance is interrupted
  - Async = no real-time requirement

**Rule:** "Minimize cost" + "async" + "willing to wait" + "retry on failure" = Spot + SQS. These keywords scream Spot.

---

### Q49: Storage Gateway Cached vs Stored Volumes
**Your answer:** A (FSx) | **Correct:** B — Storage Gateway cached volumes

| Type | Primary Data | Local | Use Case |
|------|-------------|-------|----------|
| **Cached volumes** | **S3** | Hot cache | Extend storage to cloud, local access to hot data |
| **Stored volumes** | **On-prem** | Full dataset | Full local access, async backup to S3 |

The question asks to "extend storage capacity to AWS" + "quick local access to critical records" = **cached volumes** (primary in S3, hot cache local).

FSx replaces on-prem NAS entirely — doesn't "extend" storage, requires VPN for every access.

**Rule:** "Extend to cloud + local cache" = cached volumes. "Keep everything local + backup" = stored volumes.

---

## Pattern Analysis — Common Mistake Types

### 1. Confusing Similar Services (8 errors)
- Pilot Light vs Warm Standby
- SQS vs EventBridge (SaaS integration)
- S3 Transfer Acceleration vs S3 Batch Replication
- Cached volumes vs Stored volumes
- Field-level encryption vs KMS
- IAM auth vs SSL (authentication vs encryption)
- Lambda In Memory Caching vs API Gateway Caching
- EC2 ASG alarms vs Kubernetes Cluster Autoscaler

### 2. Missing "Minimize Cost" Signals (3 errors)
- Spot Instances for async/fault-tolerant workloads
- API Gateway Caching to eliminate Lambda+DB calls
- EFS burst mode vs provisioned throughput

### 3. Non-Existent Features (3 errors)
- "Cross-region Multi-AZ" for RDS (doesn't exist)
- "Lambda In Memory Caching" (not a feature)
- "Beanstalk deployment caching" (not a feature)

### 4. Scope/Boundary Confusion (3 errors)
- S3 lifecycle prefix vs all objects
- SG referencing vs CIDR
- Trust policy as IAM's only resource-based policy
