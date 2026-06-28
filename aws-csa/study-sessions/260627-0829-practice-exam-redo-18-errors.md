# Practice Exam Redo — 18 Wrong Answers from High-Performing Knowledge Review

**Date:** 2026-06-27 | **Source:** Udemy Practice Exams 1 & 2
**Reference:** `260624-1427-high-performing-knowledge-review.md`
**Format:** Exact exam questions, shuffled order, full explanations

---

## Results Summary

| # | Exam | Q# | Topic | Result | Correct Answer |
|---|------|----|-------|--------|----------------|
| 1 | E2 | Q1 | Aurora Global Database | ✅ | B |
| 2 | E1 | Q58 | EBS Boot Volumes | ✅ | A+E (sc1+st1) |
| 3 | E1 | Q30 | Placement Groups | ✅ | D (Cluster) |
| 4 | E1 | Q46 | CloudFront Custom Origins | ✅ | A |
| 5 | E1 | Q36 | S3TA Pricing | ✅ | A |
| 6 | E1 | Q44 | AMI + Snapshot Cross-Region | ✅ | A |
| 7 | E2 | Q38 | EC2 User Data | ✅ | A+E |
| 8 | E1 | Q40 | Serverless Stream Processing | ✅ | B |
| 9 | E1 | Q51 | EFS Cross-Region | ✅ | A |
| 10 | E2 | Q21 | Global Accelerator vs CloudFront | ❌ | D (picked A) |
| 11 | E1 | Q8 | Instance Store vs EBS | ✅ | C |
| 12 | E1 | Q57 | RDS Proxy + SQS | ✅ | A+D |
| 13 | E1 | Q15 | API Gateway Protocols | ✅ | C |
| 14 | E2 | Q20 | Blue-Green + DNS Caching | ❌ | D (picked C) |
| 15 | E2 | Q50 | Aurora Global Database | ✅ | D |
| 16 | E1 | Q45 | Data Analytics Services | ✅ | A |
| 17 | E1 | Q6 | Glue DataBrew | ✅ | D |
| 18 | E1 | Q20 | Global Accelerator UDP | ✅ | A |

**Final Score: 16/18 (89%) — Previous: 0/18 (0%)**

**Still wrong (2):** Q10 (E2-Q21), Q14 (E2-Q20) — both Global Accelerator questions

---

## Remaining Weak Spot: Global Accelerator vs CloudFront

Both errors share the same root cause — defaulting to CloudFront/Route 53 when **Global Accelerator** is the correct answer.

### Decision Pattern to Memorize

| Signal in Question | Answer |
|---|---|
| UDP, TCP, non-HTTP traffic | **Global Accelerator** (CloudFront = HTTP only) |
| NLB endpoints | **Global Accelerator** (CloudFront can't front NLBs for TCP) |
| DNS caching concerns (mobile) | **Global Accelerator** (uses anycast IPs, bypasses DNS) |
| Blue-green traffic dial % | **Global Accelerator** (instant, no DNS propagation) |
| Static anycast IPs needed | **Global Accelerator** |
| Fast regional failover | **Global Accelerator** (automatic, no DNS TTL delay) |
| Custom DNS (not Route 53) | **Global Accelerator** (just point your DNS to anycast IPs) |
| HTTP content caching at edge | **CloudFront** |
| S3 static website | **CloudFront** |
| Lambda@Edge processing | **CloudFront** |
| On-prem web server as origin | **CloudFront** (custom origin) |

---

## Detailed Q&A Log

### Q1 — E2-Q1 | Aurora Global Database | ✅

**Q:** An IT company has an ACM application using Amazon RDS for MySQL with performance issues despite Read Replicas. Needs global scale without moving away from relational schema. Most cost-effective and high-performance solution?

**Correct: B — Aurora Global Database** | Cross-region read replicas, <1s replication, MySQL-compatible
- A (EC2+MySQL): Massive management overhead, not cost-effective
- C (DynamoDB): NoSQL — violates relational requirement
- D (Redshift): Data warehouse, not transactional DB

### Q2 — E1-Q58 | EBS Boot Volumes | ✅

**Q:** Which volume types CANNOT be used as boot volumes? (Select two)

**Correct: A+E — sc1 (Cold HDD) + st1 (Throughput Optimized HDD)**
- Only SSD types (gp2/gp3/io1/io2) can boot
- Instance Store (C) is not an EBS type — trick answer

### Q3 — E1-Q30 | Placement Groups | ✅

**Q:** HPC application for NASA — which EC2 topology?

**Correct: D — Cluster placement group** | Same rack, 10 Gbps, lowest latency
- A (Partition): Spreads across racks = higher latency, for Hadoop/Kafka
- C (Spread): Max isolation, max 7/AZ — opposite of HPC needs

### Q4 — E1-Q46 | CloudFront Custom Origins | ✅

**Q:** On-prem US website launching in Asia, immediate solution needed, backend stays in US.

**Correct: A — CloudFront with custom origin pointing to on-prem servers**
- Caches at edge, no migration needed, immediate setup
- D (Route 53 geo-proximity): Only routes DNS, doesn't cache or reduce latency

### Q5 — E1-Q36 | S3TA Pricing | ✅

**Q:** S3TA used but didn't accelerate the 3GB upload. What charges apply?

**Correct: A — No charges at all**
- S3 data-IN is always free
- S3TA fees waived when no acceleration occurs

### Q6 — E1-Q44 | AMI + Snapshot Cross-Region | ✅

**Q:** AMI copied from Region A to Region B, instance launched in B. What exists in Region B?

**Correct: A — 1 EC2 instance + 1 AMI + 1 snapshot**
- Copying AMI also copies underlying EBS snapshot

### Q7 — E2-Q38 | EC2 User Data | ✅

**Q:** Which TWO are true about EC2 user data?

**Correct: A+E — First boot only + root privileges**
- Cannot update while running (must stop first)
- Does NOT run on every restart by default

### Q8 — E1-Q40 | Serverless Stream Processing | ✅

**Q:** Gaming leaderboard, order of receipt, handle spikes, minimize management.

**Correct: B — Kinesis Data Streams → Lambda → DynamoDB**
- Fully serverless pipeline = minimum management
- C (Kinesis → EC2 fleet): EC2 = management overhead

### Q9 — E1-Q51 | EFS Cross-Region | ✅

**Q:** EFS in us-east-1, teams in Asia/Europe need access. Least operational overhead?

**Correct: A — Inter-region VPC peering**
- Direct NFS mount from peered regions, no data copying

### Q10 — E2-Q21 | Global Accelerator vs CloudFront | ❌ (picked A, correct D)

**Q:** Video conferencing + NLBs globally, reduce latency. Keep existing infrastructure.

**Correct: D — Global Accelerator with NLBs as endpoints**
- Video conferencing = TCP/UDP, not cacheable HTTP
- CloudFront can't cache NLB TCP traffic
- GA routes through AWS private network, works natively with NLBs

### Q11 — E1-Q8 | Instance Store vs EBS | ✅

**Q:** High random I/O, data replicated by app, resilient to instance failure. Most cost-optimal?

**Correct: C — Instance Store**
- Highest I/O (local NVMe), free (included), ephemeral OK because app replicates

### Q12 — E1-Q57 | RDS Proxy + SQS | ✅

**Q:** Aurora PostgreSQL timing out during flash sales. Redesign for scalability. (Select two)

**Correct: A+D — SQS queue (async decoupling) + RDS Proxy (connection pooling)**
- B (ElastiCache): Caches reads, doesn't solve write/transaction overload

### Q13 — E1-Q15 | API Gateway Protocols | ✅

**Q:** REST vs WebSocket — stateful vs stateless?

**Correct: C — REST = stateless, WebSocket = stateful full-duplex**

### Q14 — E2-Q20 | Blue-Green + DNS Caching | ❌ (picked C, correct D)

**Q:** Blue-green deployment, 48 hours, mobile users with DNS caching. Test on many users.

**Correct: D — Global Accelerator traffic dial**
- Anycast IPs bypass DNS caching entirely
- Route 53 weighted (C): DNS changes delayed by mobile DNS caching

### Q15 — E2-Q50 | Aurora Global Database | ✅

**Q:** Global healthcare app, Aurora, RPO seconds, RTO 1 minute.

**Correct: D — Aurora Global Database**
- C (Serverless): Single region only, can't meet global latency needs

### Q16 — E1-Q45 | Data Analytics | ✅

**Q:** S3 data lake, daily ETL, MPP warehouse, SQL-based ML, serverless.

**Correct: A — Glue → Redshift Serverless + Redshift ML**
- C (EMR+Spark): Not serverless, SageMaker needs Python

### Q17 — E1-Q6 | Glue DataBrew | ✅

**Q:** Code-free data prep with profiling, lineage, shareable recipes.

**Correct: D — Glue DataBrew**
- A (Glue Studio): Low-code ETL, no native profiling/lineage
- B (Athena): Requires SQL = not code-free

### Q18 — E1-Q20 | Global Accelerator UDP | ✅

**Q:** Gaming (UDP), fast regional failover, custom DNS.

**Correct: A — Global Accelerator**
- D (CloudFront): HTTP only, does NOT support UDP
