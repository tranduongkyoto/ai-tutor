# Practice Exam Wrong Answers — High-Performing Knowledge Review

**Date:** 2026-06-24 | **Errors:** 18/56 (30% of all errors)
**Source:** Udemy Practice Exams 1 & 2

---

## Topic A: Global Accelerator vs CloudFront (3 errors)

### Decision Tree

| Feature | AWS Global Accelerator | Amazon CloudFront |
|---------|----------------------|-------------------|
| Layer | Layer 4 (TCP/UDP) | Layer 7 (HTTP/HTTPS) |
| Static IPs | Yes — 2 anycast IPs | No static IPs |
| Protocol | TCP, UDP | HTTP, HTTPS, WebSocket |
| Caching | No | Yes (edge caching) |
| Use case | Gaming, VoIP, IoT, non-HTTP | Web content, APIs, streaming |
| Blue-green | Traffic dial % per endpoint group | Not natively |
| DNS caching | Immune (uses anycast IP) | Affected by DNS TTL |
| Endpoints | NLB, ALB, EC2, Elastic IP | S3, ALB, EC2, custom origin |

### When to pick Global Accelerator:
- **UDP traffic** (gaming, VoIP) → GA (CloudFront is HTTP only)
- **Static anycast IPs** needed (whitelisting, firewall rules) → GA
- **Blue-green with DNS-caching-prone clients** (mobile) → GA traffic dial (instant, no DNS TTL)
- **NLB endpoints** for global routing → GA
- **Fast regional failover** → GA (automatic, no DNS propagation)

### When to pick CloudFront:
- **HTTP/HTTPS content** caching at edge → CF
- **On-premises web servers** as custom origin → CF
- **S3 static website** acceleration → CF
- **Lambda@Edge** processing → CF

### Wrong Answers
- **E1-Q20**: Gaming + UDP + fast failover → **Global Accelerator** (not CloudFront — CF doesn't do UDP)
- **E2-Q20**: Blue-green + DNS-caching mobile phones → **Global Accelerator** traffic dial (not Route 53 weighted — DNS cache delays)
- **E2-Q21**: Video conferencing + NLBs + reduce latency globally → **Global Accelerator** (not CloudFront — CF can't cache NLB TCP traffic)

---

## Topic B: Data Analytics Services (3 errors)

### Glue DataBrew vs Glue Studio vs Athena vs EMR

| Service | Purpose | Code required? | Key feature |
|---------|---------|---------------|-------------|
| **Glue DataBrew** | Visual data prep | No code | Recipes, profiling, lineage |
| **Glue Studio** | Visual ETL jobs | Low code | Job editor, Spark under hood |
| **Athena** | SQL queries on S3 | SQL only | Serverless, pay per query |
| **EMR** | Big data frameworks | Yes (Spark/Hive) | Full control, expensive |
| **Redshift** | Data warehouse | SQL | MPP, ML integration |
| **Redshift Serverless** | Same as above | SQL | No cluster management |

### Key decisions:
- "Code-free data prep with profiling" → **Glue DataBrew**
- "SQL-based ML on warehouse data" → **Redshift ML** (SQL syntax, no Python needed)
- "Serverless MPP warehouse" → **Redshift Serverless**
- "Daily ETL from S3 to warehouse" → **Glue job → Redshift**
- EMR = overkill when Glue + Redshift Serverless can do the job

### Wrong Answers
- **E1-Q6**: Code-free prep + profiling + recipes → **Glue DataBrew** (not Athena SQL queries)
- **E1-Q45**: Daily ETL + serverless MPP + SQL-based ML → **Glue + Redshift Serverless + Redshift ML** (not EMR + Spark)

---

## Topic C: Storage Performance — Instance Store vs EBS vs EFS (3 errors)

### Storage Comparison

| Storage | I/O Performance | Persistence | Boot volume? | Cost |
|---------|----------------|-------------|-------------|------|
| **Instance Store** | Highest (local NVMe) | Ephemeral (lost on stop) | No | Free (included) |
| **EBS gp3/io2** | High (configurable IOPS) | Persistent | Yes | Per GB + IOPS |
| **EBS st1** | High throughput HDD | Persistent | No | Lower per GB |
| **EBS sc1** | Low throughput HDD | Persistent | No | Lowest per GB |
| **EFS** | Moderate (network) | Persistent | No | Per GB used |

### Key decisions:
- "High random I/O + data is replicated/ephemeral OK" → **Instance Store** (fastest, cheapest)
- "Boot volume" → Only **EBS gp2/gp3/io1/io2** (st1, sc1, Instance Store CANNOT boot)
- "Cannot be boot volume" → **sc1 (Cold HDD)** and **st1 (Throughput HDD)**
- Instance Store CAN be used alongside boot EBS but NOT as boot itself

### Wrong Answers
- **E1-Q8**: High random I/O + resilient app (data replicated) → **Instance Store** (not EFS — network latency)
- **E1-Q58**: Cannot be boot volume → **sc1 + st1** (not Instance Store — trick: Instance Store isn't even an EBS type, it can't boot but the question asks about EBS volume types)

---

## Topic D: API Gateway Protocols (1 error)

- **REST API** = **stateless** (each request independent, no connection persistence)
- **WebSocket API** = **stateful** (persistent full-duplex connection between client/server)

### Wrong Answer
- **E1-Q15**: REST = stateless, WebSocket = stateful → Answer C (you picked D: REST=stateful, which is wrong)

---

## Topic E: Placement Groups (1 error)

| Type | Purpose | Use case |
|------|---------|----------|
| **Cluster** | Low latency, high throughput | HPC, tightly coupled |
| **Spread** | Max isolation | Critical instances, max 7 per AZ |
| **Partition** | Large distributed workloads | Hadoop, Cassandra, Kafka |

- HPC = **Cluster** (same rack, 10 Gbps, low latency)
- Not partition (partition spreads across racks = higher latency)

### Wrong Answer
- **E1-Q30**: HPC + low latency → **Cluster placement group** (not partition)

---

## Topic F: S3 Transfer Acceleration Pricing (1 error)

- S3TA speeds up uploads using CloudFront edge locations
- **If S3TA is NOT faster than standard transfer, AWS does NOT charge S3TA fees**
- You only pay S3TA charges when it actually accelerates the transfer
- Standard S3 data-in transfer is always free

### Wrong Answer
- **E1-Q36**: S3TA not faster → **No charges at all** (data-in is free, S3TA waived when not accelerated)

---

## Topic G: Serverless Stream Processing (1 error)

- Kinesis Data Streams → **Lambda** = fully serverless, auto-scaling, minimal management
- Kinesis Data Streams → EC2 fleet = you manage scaling, patching, instances
- "Minimize management overhead" = Lambda over EC2

### Wrong Answer
- **E1-Q40**: Kinesis + minimal management → **Lambda** (not EC2 fleet with Auto Scaling)

---

## Topic H: AMI and Snapshot Cross-Region (1 error)

When you copy an AMI to another region:
- The **AMI** is copied
- The **underlying EBS snapshot** is also copied (AMI references snapshot)
- Both exist in the target region

So: Region B has **1 EC2 instance + 1 AMI + 1 snapshot**

### Wrong Answer
- **E1-Q44**: Copy AMI to Region B → 1 instance + 1 AMI + **1 snapshot** (snapshot comes with AMI copy)

---

## Topic I: CloudFront Custom Origins (1 error)

- CloudFront can use **on-premises servers** as custom origins
- Caches content at edge locations worldwide → reduces latency for distant users
- Works immediately — no migration needed
- Route 53 geo-proximity just routes to nearest endpoint, doesn't cache or reduce latency

### Wrong Answer
- **E1-Q46**: On-prem website + optimize for Asia → **CloudFront custom origin** (not Route 53 geo-proximity)

---

## Topic J: EFS Cross-Region Access (1 error)

- EFS supports **inter-region VPC peering** for cross-region access
- No need to copy data to S3 or replicate to another EFS
- VPC peering connection enables direct NFS mount from any peered region

### Wrong Answer
- **E1-Q51**: EFS spreadsheet access from other regions → **Inter-region VPC peering** (not copy to S3)

---

## Topic K: Aurora Global Database (2 errors)

- **Aurora Global Database**: single Aurora DB spanning multiple regions
- Read replicas in each region for low-latency local reads
- RPO: seconds | RTO: ~1 minute
- Use for: global apps needing local reads + fast disaster recovery

- **Aurora Serverless**: auto-scaling capacity, single region only
- **Aurora Multi-Master**: multi-write in same region only (deprecated)

### Wrong Answers
- **E2-Q1**: Global app + relational + fast local reads → **Aurora Global Database** (not EC2 MySQL per region)
- **E2-Q50**: Global low latency + RPO seconds + RTO minute → **Aurora Global Database** (not Aurora Serverless — single region)

---

## Topic L: RDS Proxy & Async Decoupling (1 error)

When Aurora gets overwhelmed by connection spikes:
1. **RDS Proxy** = connection pooling, reuses DB connections, reduces connection overhead
2. **SQS queue + workers** = async decoupling, buffer requests during spikes

ElastiCache caches reads but doesn't help with write/transaction spikes.

### Wrong Answer
- **E1-Q57**: Aurora timing out during spikes → **SQS + workers (A) + RDS Proxy (D)** (not ElastiCache — caching doesn't solve transaction overload)

---

## Topic M: EC2 User Data (1 error)

- User data runs **only on first boot** (not every restart)
- Scripts execute with **root privileges** by default
- Cannot update user data while instance is running (must stop first)
- To run on every boot: use cloud-init `[scripts-user, always]` or put in `/var/lib/cloud/scripts/per-boot/`

### Wrong Answer
- **E2-Q38**: User data truths → **A) first boot only + E) root privileges** (not "runs on restart" or "update while running")
