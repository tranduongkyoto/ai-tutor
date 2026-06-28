# Practice Exam Wrong Answers — Resilient Architecture Knowledge Review

**Date:** 2026-06-28 | **Errors:** 10/56 (18% of all errors)
**Source:** Udemy Practice Exams 1 & 2

---

## Topic A: Auto Scaling Group Lifecycle & Maintenance (3 errors)

### ASG Instance Lifecycle States

```
InService ──► Standby ──► InService     (maintenance path)
InService ──► Terminating ──► Terminated (unhealthy/scale-in path)
```

### ASG Process Types You Can Suspend

| Process | What it does | When to suspend |
|---------|-------------|-----------------|
| **ReplaceUnhealthy** | Terminates unhealthy + launches replacement | During maintenance (instance will look unhealthy) |
| **HealthCheck** | Marks instances healthy/unhealthy | Rarely — better to use Standby or suspend ReplaceUnhealthy |
| **ScheduledActions** | Executes scheduled scaling | Unrelated to health checks |
| **Launch / Terminate** | Core scaling actions | Rarely |

### Two ways to maintain an ASG instance:
1. **Standby state** — removes instance from ALB, ASG won't replace it. Apply patch → exit Standby → back to InService
2. **Suspend ReplaceUnhealthy** — ASG won't replace instances that fail health checks during maintenance

### ASG Rebalancing Behavior
- When AZs are unbalanced (e.g., 2 instances terminated in AZ-A), ASG rebalances
- **Launches new instances FIRST, then terminates old ones** — protects availability
- Never terminates before launching during rebalance

### ASG Unhealthy Instance Handling
- Terminates unhealthy instance FIRST → then launches replacement (two separate scaling activities)
- Not simultaneous — terminate, then launch

### Wrong Answers
- **E1-Q43**: Maintenance on ASG instance → **Standby state (C) + Suspend ReplaceUnhealthy (E)** (not snapshot+new AMI — too slow and complex)
- **E1-Q65**: AZ rebalance → **launch first then terminate (B)**; unhealthy → **terminate first then launch (E)** (not terminate-before-launch for rebalance — that hurts availability)
- **E2-Q34**: ASG not terminating unhealthy instance → **health check grace period not expired (A) + Impaired status (B) + failed ELB health check (F)** (not "custom health checks can't terminate" — ASG DOES terminate on custom health check failures)

---

## Topic B: RDS Multi-AZ — Replication & Upgrades (3 errors)

### Replication Model

| Feature | Multi-AZ | Read Replica |
|---------|---------|-------------|
| **Replication type** | **Synchronous** | **Asynchronous** |
| **Purpose** | High availability (failover) | Read scaling |
| **Span** | ≥2 AZs, single region | Same AZ, cross-AZ, or cross-region |
| **Readable?** | No (standby is passive) | Yes |
| **Failover** | Automatic (DNS switch) | Manual promotion |

**Memory aid:** Multi-AZ = **S**tandby = **S**ynchronous. Read Replica = **A**sync = **A**vailable for reads.

### Multi-AZ Engine-Level Upgrade Behavior
- **Both primary AND standby are upgraded at the same time**
- This **causes downtime** until the upgrade completes
- NOT a rolling upgrade (standby first, then primary) — that's what happens for OS patching, not engine upgrades
- Engine upgrade = full downtime. OS patch = rolling (no downtime).

### Wrong Answers
- **E1-Q48**: Multi-AZ = **synchronous** replication, Read Replica = **asynchronous** (you picked async for Multi-AZ — wrong)
- **E2-Q61**: Engine upgrade on Multi-AZ → **both upgraded simultaneously, causes downtime (A)** (you picked primary-first-then-standby with no downtime — that's OS patching behavior)

### RDS Storage Auto-Scaling
- RDS MySQL **natively supports storage auto-scaling** — just enable it
- No need to migrate to Aurora for auto-scaling storage
- "Minimum effort" + "storage running out" → enable RDS storage auto-scaling, don't migrate

- **E2-Q33**: Storage running out on RDS MySQL → **enable storage auto-scaling (C)** (not migrate to Aurora — that's more effort than just toggling a setting)

---

## Topic C: SQS Standard vs FIFO (1 error)

### Quick Comparison

| Feature | Standard | FIFO |
|---------|---------|------|
| **Ordering** | Best-effort | Strict FIFO |
| **Delivery** | At-least-once (possible duplicates) | Exactly-once |
| **Throughput** | Unlimited | 300 msg/s (3,000 with batching) |
| **Use case** | High throughput, order doesn't matter | Order matters, no duplicates |

### Decision Rule
- "Processed **exactly once**" or "**no duplicates**" → **FIFO**
- "Order of receipt" or "**in order**" → **FIFO**
- Just "reliable buffering" with max throughput → **Standard**

### Wrong Answer
- **E1-Q55**: "Processed exactly once, no loss of data" → **SQS FIFO (C)** (not Standard — Standard can deliver duplicates)

---

## Topic D: ALB vs NLB Selection (1 error)

### Load Balancer Comparison

| Feature | ALB | NLB |
|---------|-----|-----|
| **Layer** | 7 (HTTP/HTTPS) | 4 (TCP/UDP/TLS) |
| **Content-based routing** | ✅ (path, host, header, query) | ❌ |
| **WebSocket** | ✅ | ✅ |
| **Static IP** | ❌ | ✅ |
| **Ultra-low latency** | No | Yes |
| **Use case** | Web apps, microservices | Gaming, IoT, non-HTTP |

### Decision Rule
- "Content-based routing" or "path-based routing" → **ALB**
- "Static IP" or "UDP" or "ultra-low latency" → **NLB**

### Wrong Answer
- **E1-Q60**: "Content-based routing" + HA → **ALB + Auto Scaling (C)** (not NLB — NLB doesn't do content-based routing)

---

## Topic E: Private Cross-Account Connectivity (1 error)

### AWS PrivateLink Pattern

```
Partner Account                    Your Account
┌─────────────┐                   ┌─────────────┐
│  RDS MySQL  │                   │  Private VPC │
│      ↓      │    PrivateLink    │  (no IGW)   │
│    NLB      │ ──────────────►   │  VPC Endpoint│
└─────────────┘                   └─────────────┘
```

- **NLB + PrivateLink** = expose a service privately to another VPC/account
- No internet, no VPN, no Direct Connect needed
- Consumer creates **interface VPC endpoint** → gets ENI in their VPC
- Traffic stays on AWS backbone, never touches public internet

### Wrong Answer
- **E1-Q62**: Private connectivity to partner's RDS, no internet/VPN/DX → **NLB + PrivateLink (B)** (not public RDS — violates "private VPC, no internet access" requirement)

---

## Topic F: Aurora vs RDS Migration Decisions (1 error)

### Aurora Advantages Over RDS

| Feature | RDS MySQL/SQL Server | Aurora MySQL |
|---------|---------------------|-------------|
| **Read scaling** | Read replicas (async) | Up to 15 Aurora Replicas (faster) |
| **Storage** | Manual provisioning | Auto-scales to 128 TB |
| **Backup restore** | Snapshot restore (slow) | Fast clone / restore from automated backups |
| **Availability** | Multi-AZ (1 standby) | Multi-AZ (up to 15 replicas, any can failover) |
| **Dev DB copy** | Full dump = slow, impacts prod | Restore from automated backup = fast, no prod impact |

### Decision Signals
- "Read-scaling" + "availability" + "dev DB copy without impacting prod" → **Aurora + restore from automated backups**
- "Migrate database engines if required" = permission to switch from SQL Server to Aurora MySQL
- RDS SQL Server has **limited read replica support** (only Enterprise Edition, same region)

### Wrong Answer
- **E2-Q10**: SQL Server + read scaling + dev DB copy causing latency → **Aurora MySQL + restore from automated backups (B)** (not RDS SQL Server + read replicas — SQL Server read replicas are limited, and using standby as dev DB is not supported)
