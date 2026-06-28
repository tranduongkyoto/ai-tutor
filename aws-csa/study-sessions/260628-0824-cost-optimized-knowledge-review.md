# Practice Exam Wrong Answers — Cost-Optimized Architecture Knowledge Review

**Date:** 2026-06-28 | **Errors:** 8/56 (14% of all errors)
**Source:** Udemy Practice Exams 1 & 2

---

## Topic A: S3 Storage Class Selection (3 errors)

### S3 Storage Class Comparison

| Class | Cost/GB | Retrieval | Min Duration | AZs | Use case |
|-------|---------|-----------|-------------|-----|----------|
| **Standard** | $0.023 | Instant, free | None | ≥3 | Frequent access, short-lived data |
| **Standard-IA** | $0.0125 | Instant, per-GB fee | 30 days | ≥3 | Infrequent but needs multi-AZ |
| **One Zone-IA** | $0.01 | Instant, per-GB fee | 30 days | 1 | Infrequent + re-creatable |
| **Glacier Instant** | $0.004 | Instant, higher fee | 90 days | ≥3 | Archive with instant access |
| **Glacier Flexible** | $0.0036 | Min to hours | 90 days | ≥3 | Archive, flexible retrieval |
| **Glacier Deep Archive** | $0.00099 | 12-48 hours | 180 days | ≥3 | Long-term archive |

### Key Decision Rules

1. **Min storage duration charges**: IA classes charge minimum 30 days even if deleted early. Glacier = 90/180 days. Data kept <30 days → **Standard is cheaper** (no min duration penalty)
2. **"Re-creatable" assets** → **One Zone-IA** (cheapest IA, single AZ OK since data can be regenerated)
3. **"Heavily referenced" + short-lived (<30 days)** → **Standard** (IA retrieval fees + 30-day minimum make it MORE expensive for frequently accessed short-lived data)
4. **Lifecycle timing**: "after a week" = 7 days, "after 30 days" = 30 days. Match the transition to when access drops.

### Wrong Answers
- **E1-Q7**: Re-creatable assets, access drops after a week → **One Zone-IA after 30 days (B)** (you picked One Zone-IA after 7 days — but IA has 30-day minimum charge, so transitioning at 7 days wastes 23 days of minimum charge. Wait until 30 days to transition)
- **E1-Q35**: Intermediary results, 24 hours only, heavily referenced → **S3 Standard (C)** (you picked Standard-IA — but data is deleted after 24h, IA charges for 30 days minimum. Plus heavy access = high retrieval fees. Standard is cheapest for short-lived, frequently accessed data)
- **E1-Q50**: Storage cost ordering for 1GB file → **S3 Standard < EFS < EBS** (you swapped EFS and EBS)

### Storage Pricing Order (per GB stored)

```
S3 Standard ($0.023/GB) < EFS Standard ($0.30/GB) < EBS gp2 ($0.10/GB × 100GB provisioned = $10 for 100GB)
```

**Trap**: EBS charges for **provisioned** capacity (100 GB), not used capacity (1 GB). So you pay $10/month for 100GB even though only 1GB is stored. EFS charges per GB **used** = $0.30 for 1GB. S3 = $0.023 for 1GB.

Actual costs: S3 ($0.023) < EFS ($0.30) < EBS ($10.00)

---

## Topic B: Snowball → Glacier Path (1 error)

### Snowball Limitations
- **Snowball CANNOT write directly to Glacier or Glacier Deep Archive**
- Snowball can only target **S3 Standard or S3 Standard-IA**
- To get data into Glacier: Snowball → S3 bucket → lifecycle policy → Glacier

### Correct Pattern
```
Snowball → S3 bucket → Lifecycle policy (same day) → Glacier Deep Archive
```

### Wrong Answer
- **E2-Q27**: Snowball to long-term archive → **S3 bucket + lifecycle to Glacier Deep Archive (D)** (you targeted Glacier vault directly — Snowball can't do that)

---

## Topic C: VPC Sharing vs Transit Gateway Cost (1 error)

### Cross-Account Networking Cost Comparison

| Solution | Cost | Complexity | Use case |
|----------|------|-----------|----------|
| **VPC Sharing (RAM)** | **Free** (no extra infra) | Low | Same region, shared subnets |
| **VPC Peering** | No hourly cost, data transfer fees | Medium (N×N mesh) | Few VPCs, cross-region OK |
| **Transit Gateway** | $0.05/hr + $0.02/GB | High but scalable | Many VPCs, hub-and-spoke |
| **PrivateLink** | $0.01/hr + $0.01/GB | Medium | Service-to-service |

### Decision Rule
- "CHEAPEST" + same region + Organizations → **VPC Sharing via RAM** (zero networking cost, instances share subnets)
- "Scalable hub-and-spoke" + many VPCs → Transit Gateway (costs more but simplifies routing)

### Wrong Answer
- **E2-Q35**: Multiple accounts, same region, cheapest private connectivity → **VPC Sharing via RAM (C)** (you picked Transit Gateway — it works but costs $0.05/hr per attachment. RAM sharing is free)

---

## Topic D: ASG Default Termination Policy (1 error)

### ASG Default Termination Policy (in order)

```
1. Select AZ with most instances
2. Find instances with OLDEST launch configuration/template
   - Launch configuration > launch template (config is "older" concept)
3. Among those, pick instance CLOSEST to next billing hour
```

### Key Distinction
- **Oldest launch configuration** beats **oldest launch template**
- ASG checks launch configuration BEFORE launch template
- "Oldest launch template" ≠ first to terminate (launch config takes priority)

### Wrong Answer
- **E2-Q45**: 4 instances — A (oldest template), B (oldest config), C (newest config), D (closest billing hour) → **Instance B (oldest launch configuration)** (you picked A — oldest launch template. But launch configuration is checked before launch template in the default policy)

---

## Topic E: HA Instance Distribution Across AZs (1 error)

### HA Formula: N+1 AZ Strategy

**Rule**: To survive 1 AZ failure with minimum instances, use **3 AZs with evenly distributed instances**.

| Requirement | 2 AZs | 3 AZs |
|-------------|-------|-------|
| Need 4 running | 4+4 = **8 total** (if 1 AZ dies, 4 survive) | 2+2+2 = **6 total** (if 1 AZ dies, 4 survive) |
| Need 6 running | 6+6 = **12 total** | 3+3+3 = **9 total** |

**3 AZs is always cheaper** for HA because you lose a smaller fraction (1/3 vs 1/2) when an AZ fails.

### Wrong Answer
- **E2-Q46**: Need 4 instances always available, minimum cost → **3 AZs, 2 each = 6 total (A)** (you picked 2 AZs, 4 each = 8 total — works but costs 2 extra instances)

---

## Topic F: Spot Fleet vs Spot Instances (1 error)

### EC2 Purchasing Options for Batch Workloads

| Option | Best for | Cost |
|--------|---------|------|
| **On-Demand** | Unpredictable, can't be interrupted | Full price |
| **Reserved** | Steady-state, 1-3 year commitment | Up to 72% off |
| **Spot Instances** | Single instance type, interruptible | Up to 90% off |
| **Spot Fleet** | Multiple instance types/sizes, interruptible | Up to 90% off + diversified |

### Decision Rule
- "Various sizes" + "variable CPUs" + "withstand failures" → **Spot Fleet**
- Spot Fleet = pool of Spot + optional On-Demand across multiple instance types
- Fleet diversifies across instance types/AZs → less likely ALL get interrupted
- Single Spot Instance = one type, one AZ = higher interruption risk

### Wrong Answer
- **E2-Q47**: Monthly 2-hour job, various server sizes, withstand failures → **Spot Fleet (D)** (you picked Reserved — massively overpriced for 2 hours/month usage, and RI requires 1-3 year commitment)
