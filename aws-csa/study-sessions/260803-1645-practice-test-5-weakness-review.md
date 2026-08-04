# Practice Test 5 — Weakness Review

**Score:** 48/65 (74%) — PASS
**Date:** 2026-08-03
**Weakest → Strongest:** High-Performing (57%) → Cost-Optimized (70%) → Secure (83%) → Resilient (88%)

---

## Pattern 1: Confusing Similar AWS Services (9 errors)

The biggest error pattern — picking a service that sounds right but serves a different purpose.

### 1.1 Kinesis Data Streams vs Kinesis Data Firehose

| | Data Streams | Data Firehose |
|--|-------------|---------------|
| **Consumer model** | Multiple independent consumers | Single delivery destination |
| **Use case** | Fan-out to multiple apps | Deliver to S3/Redshift/OpenSearch |
| **Ordering** | Per-shard ordering | Near real-time batched delivery |
| **Retention** | 1-365 days | No retention (delivers immediately) |
| **Scaling** | Manual shards or on-demand | Auto-scales |

**Exam signal words:**
- "share with multiple applications" / "multiple consumers" → **Data Streams**
- "deliver to S3" / "load into Redshift" / "near real-time ETL" → **Firehose**

**Your mistake (Q30):** Saw "share transactions with multiple internal applications" but picked Firehose. Firehose delivers to ONE destination — Data Streams supports multiple independent consumers.

---

### 1.2 Comprehend vs Transcribe vs Translate vs Athena vs QuickSight

| Service | Purpose | Input → Output |
|---------|---------|----------------|
| **Comprehend** | Sentiment analysis, entity extraction | Text → sentiment/entities |
| **Transcribe** | Speech to text | Audio → text |
| **Translate** | Language translation | Text → translated text |
| **Athena** | Ad-hoc SQL queries on S3 | SQL → query results |
| **QuickSight** | BI dashboards & visualization | Data → charts/dashboards |

**Exam signal words:**
- "sentiment analysis" → **Comprehend**
- "convert audio/speech to text" → **Transcribe**
- "ad-hoc SQL queries" → **Athena** (NOT QuickSight)
- "dashboards" / "visualization" → **QuickSight**

**Your mistakes:**
- **Q37:** Picked Step Functions + Transcribe for text feedback sentiment. Transcribe is speech→text, not text analysis. Comprehend does sentiment.
- **Q54:** Picked QuickSight for "ad-hoc SQL queries." QuickSight is visualization, Athena is the SQL engine.

---

### 1.3 IAM Access Analyzer vs Amazon Inspector vs Access Advisor

| | Access Analyzer | Inspector | Access Advisor |
|--|----------------|-----------|----------------|
| **Analyzes** | Resource/IAM policies | EC2/container software | Service last-accessed data |
| **Finds** | External/public access to S3, IAM roles, KMS, SNS | CVEs, network exposure | Unused permissions |
| **Purpose** | "Who can access my resources?" | "Are my instances patched?" | "When was this permission last used?" |

**Exam signal words:**
- "unintended external access" / "shared with other accounts" / "publicly accessible" → **Access Analyzer**
- "software vulnerabilities" / "CVE" / "patch compliance" → **Inspector**

**Your mistake (Q34):** Saw "overly permissive resources shared with external accounts" but picked Inspector. Inspector scans for software vulns, not policy analysis.

---

### 1.4 Redis vs Memcached vs Global Accelerator vs DAX

| | Redis | Memcached | DAX | Global Accelerator |
|--|-------|-----------|-----|-------------------|
| **Type** | In-memory cache | In-memory cache | DynamoDB cache | Network routing |
| **Geospatial** | Yes (GEOADD) | No | No | No |
| **Data structures** | Sorted sets, lists, hashes | Simple key-value | DynamoDB items | N/A |
| **Multi-threaded** | No (single) | Yes | N/A | N/A |

**Exam signal words:**
- "geospatial" / "sorted sets" / "pub/sub" → **Redis**
- "multi-threaded" / "simple caching" → **Memcached**
- "DynamoDB read acceleration" → **DAX**
- "global routing" / "static IPs" / "cross-Region failover" → **Global Accelerator**

**Your mistake (Q43):** Saw "geospatial caching" but picked Global Accelerator. GA is networking, not caching. Redis has native geospatial commands.

---

## Pattern 2: Wrong Migration/Storage Tool Selection (3 errors)

### 2.1 DataSync vs File Gateway vs FSx Lustre

| | DataSync | File Gateway | FSx Lustre |
|--|----------|-------------|------------|
| **Purpose** | Bulk data migration | Ongoing hybrid access | HPC file system |
| **Speed** | High-throughput transfer | Local cache + S3 backend | Extreme IOPS |
| **Use when** | Moving TBs/PBs to AWS | On-prem apps need S3 access daily | ML/HPC workloads |
| **Cost** | Pay per transfer | Gateway appliance + S3 | Expensive per-TB |

**Decision tree:**
1. "Migrate hundreds of TBs" → **DataSync**
2. "On-prem needs ongoing low-latency access to S3" → **File Gateway**
3. "HPC / machine learning / extreme IOPS" → **FSx Lustre**
4. Migrate THEN ongoing access → **DataSync first, then File Gateway**

**Your mistakes:**
- **Q24:** Picked File Gateway for both migration AND ongoing access. File Gateway is too slow for bulk migration. Use DataSync to migrate, then File Gateway for ongoing.
- **Q17 (Cost):** Picked FSx Lustre for rendering engine needing S3 access. FSx Lustre is HPC-grade overkill. File Gateway provides the local cache for on-prem apps.

---

### 2.2 EBS Fast Snapshot Restore

**What it does:** Pre-initializes EBS volumes created from snapshots so they have full performance immediately (no lazy-loading penalty).

**Without FSR:** New volumes from snapshots degrade I/O until all blocks are fetched from S3 on first access.

**Exam signal words:**
- "high consistent I/O" + "from snapshots" + "minimize provisioning time" → **FSR**
- "clone production data for testing" + "high IOPS immediately" → **Snapshot + FSR + new volume**

**Your mistake (Q4):** Picked AWS Backup restore. Backup is slower and doesn't guarantee immediate full I/O. FSR is purpose-built for this.

---

### 2.3 Instance Store vs Storage Gateway (tiered storage)

| Need | Service |
|------|---------|
| Maximum I/O, temporary data | Instance Store |
| Durable object storage | S3 |
| Long-term archive | S3 Glacier |
| On-prem hybrid access | Storage Gateway |

**Your mistake (Q35):** Picked Storage Gateway for "durable storage" tier. Storage Gateway is hybrid access, not a durable storage tier. S3 is the durable storage tier.

---

## Pattern 3: Cost Optimization Traps (3 errors)

### 3.1 DX Egress vs Internet Egress

| Path | Cost per GB |
|------|------------|
| Within AWS Region | Free (same AZ) or ~$0.01 (cross-AZ) |
| AWS → Internet | ~$0.09/GB |
| AWS → Direct Connect | ~$0.02/GB |

**Strategy:** Keep large data flows inside AWS. Only send small results out. When egress is needed, DX is 4-5x cheaper than internet.

**Your mistake (Q22):** Picked "access via internet" instead of "access via DX." Both keep the 60MB query internal, but DX egress for the 600KB webpage is cheaper than internet egress.

---

### 3.2 CloudWatch EC2 Alarm Actions

Built-in actions — no Lambda, no SNS, no extra services:
- **Stop** — stop the instance
- **Terminate** — terminate the instance  
- **Reboot** — reboot the instance
- **Recover** — recover to new hardware

**Exam signal words:**
- "most cost-optimal" / "resource-efficient" / "automated reboot" → **CloudWatch Alarm Action** (fewest moving parts)
- Complex orchestration / conditional logic → Lambda

**Your mistake (Q29):** Picked EventBridge + Lambda. CloudWatch has a native EC2 Reboot action — one alarm, zero code.

---

### 3.3 Reserved + Spot for Fault-Tolerant Workloads

| Workload Type | Best Purchasing Strategy |
|--------------|------------------------|
| Steady baseline | Reserved Instances |
| Spikes, fault-tolerant (SQS, batch) | Spot Instances |
| Spikes, NOT fault-tolerant | On-Demand |

**Key insight:** SQS-based workloads are inherently Spot-friendly. If a Spot instance is reclaimed, the message returns to the queue automatically. No data loss.

**Your mistake (Q44):** Picked On-Demand for spikes. SQS processing is fault-tolerant → Spot is cheaper and safe.

---

## Pattern 4: Aurora vs RDS Terminology (2 errors)

### Aurora Replicas vs RDS Standbys

| | Aurora Replica | RDS Multi-AZ Standby |
|--|---------------|---------------------|
| **Readable?** | Yes (reader endpoint) | No (passive) |
| **Failover target?** | Yes (automatic) | Yes (automatic) |
| **Replication** | Shared storage (microseconds) | Synchronous (milliseconds) |
| **Term used** | "Replica" | "Standby" |

**Your mistake (Q39):** Picked "standby Aurora instance" (option E). Aurora doesn't have standbys — it has replicas that serve reads AND act as failover targets simultaneously.

### DynamoDB Global Tables vs RDS Cross-Region Replicas

| | DynamoDB Global Tables | RDS Cross-Region Replicas |
|--|----------------------|--------------------------|
| **Multi-Region writes** | Yes (multi-active) | No (read-only replicas) |
| **Replication lag** | Sub-second | Seconds to minutes |
| **Consistency** | Eventually consistent | Async replication |

**Your mistake (Q21):** Picked RDS cross-Region replica for "global consistency with sub-second updates." RDS replicas are read-only. DynamoDB global tables support multi-Region writes.

---

## Pattern 5: Monitoring Overkill (1 error)

### EC2 Monitoring Options

| Option | Interval | Effort | Use When |
|--------|----------|--------|----------|
| Basic monitoring | 5 min | Zero (default) | Normal ops |
| **Detailed monitoring** | **1 min** | **Toggle ON** | **"≤2 min intervals" + "quick + low-maintenance"** |
| CloudWatch agent | Custom (1s+) | Install + configure | RAM, disk, custom metrics |
| Custom + Athena/OpenSearch | Custom | High | Complex log analysis |

**Your mistake (Q9):** Picked CloudWatch agent + high-res + Athena. The question asked for "≤2 min intervals" + "quick to implement + low-maintenance." Detailed monitoring is a one-click toggle — simplest possible solution.

---

## Summary: Top 5 Rules to Drill

1. **"Multiple consumers/apps" = Kinesis Data Streams** (not Firehose)
2. **"Sentiment analysis" = Comprehend; "Ad-hoc SQL" = Athena** (not QuickSight)
3. **"Migrate TBs" = DataSync; "Ongoing on-prem access" = File Gateway; "HPC" = FSx Lustre**
4. **"Most cost-optimal automation" = check for native CloudWatch/AWS actions first** before Lambda
5. **Aurora has replicas (read+failover); RDS has standbys (passive failover only)**
