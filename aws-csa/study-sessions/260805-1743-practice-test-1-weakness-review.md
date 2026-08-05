# Practice Test 1 — Weakness Review

**Original:** 36/65 (55%) — FAIL
**Retake:** 55/65 (85%) — PASS
**Improvement:** +30 points
**Date:** 2026-08-05
**Still wrong:** 11 questions (8 HP, 2 Resilient, 1 Cost)

---

## Pattern 1: Instance Store vs EFS vs File Gateway (3 errors)

Same pattern appeared 3 times — confusing when to use each storage type.

| | Instance Store | EFS | File Gateway |
|--|---------------|-----|-------------|
| **Best for** | Max I/O, temp data | Shared POSIX, multi-AZ | On-prem NFS → S3 backend |
| **Persistence** | Ephemeral (lost on stop) | Persistent, durable | S3 = persistent |
| **Cost** | Included in instance | $0.30/GB/mo | S3 pricing ($0.023/GB) |
| **Use when** | "High random I/O" + data replicated by app | "Shared file system" across EC2/ECS | "On-prem NFS" + "migrate to cloud" + "tiering" |

**Your mistakes:**
- **Q8:** "High random I/O" + app handles replication + resilient to loss → **Instance Store** (picked EFS)
- **Q13:** On-prem NFS + migrate to cloud + auto-tiering → **File Gateway** (picked EFS)

**Rule:** If data can be lost → Instance Store. If on-prem needs S3 → File Gateway. If shared POSIX across AWS compute → EFS.

---

## Pattern 2: Global Accelerator vs Route 53 vs CloudFront (3 errors)

| | Global Accelerator | Route 53 | CloudFront |
|--|-------------------|----------|-----------|
| **Protocol** | TCP, UDP | DNS only | HTTP/HTTPS only |
| **Static IPs** | Yes (anycast) | No | No |
| **Failover speed** | Seconds (health check) | DNS TTL dependent | Origin failover |
| **Custom DNS** | Works alongside custom DNS | IS the DNS | Uses DNS |
| **Caching** | No (network routing) | N/A | Yes (edge cache) |
| **Origin type** | Any IP endpoint | DNS records | HTTP origins |

**Your mistakes:**
- **Q20:** UDP + custom DNS + fast failover → **Global Accelerator** (picked Route 53 — no UDP, IS the DNS service)
- **Q46:** On-prem website + optimize for Asia → **CloudFront custom origin = actual server URL** (picked CloudFront origin pointing to Route 53 DNS record — wrong, origin must point to actual server)

**Rule:** "UDP" or "static IPs" or "custom DNS" → Global Accelerator. "Cache content" → CloudFront. "DNS routing" → Route 53.

---

## Pattern 3: Kinesis Analytics vs QuickSight vs Athena (1 error)

| Service | Purpose | When |
|---------|---------|------|
| **Kinesis Data Analytics** | Real-time SQL on streaming data | "Real-time analytics" + "streaming" |
| **Amazon Athena** | Ad-hoc SQL on S3 data | "Ad-hoc SQL" + "S3 data lake" |
| **Amazon QuickSight** | BI dashboards, visualization | "Dashboards" + "reports" |

**Your mistake (Q33):** Real-time location tracking via REST API → **Kinesis Data Analytics** (picked QuickSight — visualization, not real-time processing)

---

## Pattern 4: Direct Connect + VPN (1 error)

| Requirement | Solution |
|-------------|----------|
| Fast setup + encrypted | VPN only |
| Dedicated + high throughput (no encryption needed) | Direct Connect only |
| **Dedicated + encrypted + high throughput + have time** | **Direct Connect + VPN** |

**Your mistake (Q38):** "Dedicated, encrypted, low latency, high throughput, sufficient time" → **DX + VPN** (picked VPN only — VPN goes over internet, not dedicated)

---

## Pattern 5: ECS Fargate vs EKS Anywhere (1 error)

| | ECS Fargate | EKS Anywhere |
|--|-------------|-------------|
| **Location** | AWS Cloud | On-premises |
| **Management** | Fully managed, serverless | Self-managed K8s |
| **Use when** | Long-running containers, no infra management | Must stay on-prem |

**Your mistake (Q42):** Cloud-based service, long-running, minimal ops → **ECS Fargate** (picked EKS Anywhere — that's on-prem)

---

## Pattern 6: SQS + RDS Proxy for Aurora Scaling (1 error)

| Problem | Solution |
|---------|----------|
| Too many simultaneous DB connections | **RDS Proxy** (connection pooling) |
| Async processing for traffic spikes | **SQS queue + ASG workers** |
| Read scaling | **Read replicas** (but read-only, same Region for writes) |

**Your mistake (Q57):** Aurora timing out during flash sales → SQS async + **RDS Proxy** (picked read replicas — can't write to replicas, and cross-Region replicas don't help with connection overload)

---

## Pattern 7: ASG Rebalancing Behavior (1 error)

| Event | ASG Behavior |
|-------|-------------|
| **AZ rebalancing** (unequal instances across AZs) | Launch new first → then terminate old (preserve capacity) |
| **Unhealthy instance replacement** | Terminate first → then launch new (two separate activities) |
| **Scale-in** | Terminate based on policy (oldest, closest to billing hour, etc.) |

**Your mistake (Q65):** Picked "simultaneous" (A) — ASG never does terminate+launch simultaneously. Rebalancing and unhealthy replacement use different ordering.

---

## Pattern 8: RDS Multi-AZ = Synchronous (1 error)

| | Multi-AZ | Read Replica |
|--|---------|-------------|
| **Replication** | **Synchronous** | Asynchronous |
| **Purpose** | HA failover | Read scaling |
| **Readable?** | No (standby) | Yes |
| **Span** | 2+ AZs, single Region | Same AZ, cross-AZ, or cross-Region |

**Your mistake (Q48):** Picked async for Multi-AZ. Multi-AZ is ALWAYS synchronous — that's how it guarantees zero data loss on failover.

---

## Pattern 9: S3 Deletion Protection (1 error)

| Protection | Mechanism |
|-----------|-----------|
| **Versioning** | Delete adds marker; previous versions preserved |
| **MFA Delete** | Requires MFA to permanently delete versions |
| **Object Lock** | WORM — Compliance (nobody) or Governance (elevated users) |

**Your mistake (Q32):** Picked D (console confirmation — doesn't exist in AWS). The two S3-native protections are **Versioning (C) + MFA Delete (B)**.

---

## Summary: Top 5 Persistent Weaknesses

1. **Instance Store vs EFS vs File Gateway** — match storage type to access pattern and location
2. **Global Accelerator vs Route 53 vs CloudFront** — match by protocol (UDP/TCP/HTTP) and feature (static IPs, caching, DNS)
3. **RDS Proxy for connection pooling** — Aurora overload = RDS Proxy, not read replicas
4. **Multi-AZ = synchronous** — never confuse with async read replica replication
5. **ASG behaviors differ by event type** — rebalance launches first; unhealthy terminates first; never simultaneous
