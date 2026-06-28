# Practice Exam Redo — Design Resilient Architectures (10 Errors)

**Date:** 2026-06-28 | **Source:** Udemy Practice Exams 1 & 2
**Reference:** `260628-0824-resilient-knowledge-review.md`
**Format:** Exact exam questions, full explanations

---

## Results Summary

| # | Exam | Q# | Topic | Result | Correct Answer |
|---|------|----|-------|--------|----------------|
| 1 | E1 | Q43 | ASG Standby + Suspend ReplaceUnhealthy | ✅ | C+E |
| 2 | E1 | Q48 | RDS Multi-AZ sync vs Read Replica async | ✅ | A |
| 3 | E1 | Q55 | SQS FIFO for exactly-once processing | ✅ | C |
| 4 | E1 | Q60 | ALB for content-based routing | ✅ | C |
| 5 | E1 | Q62 | NLB + PrivateLink cross-account | ✅ | B |
| 6 | E1 | Q65 | ASG rebalance (launch first) + unhealthy (terminate first) | ✅ | B+E |
| 7 | E2 | Q10 | Aurora MySQL + restore from automated backups | ✅ | B |
| 8 | E2 | Q33 | RDS storage auto-scaling (not migrate to Aurora) | ✅ | C |
| 9 | E2 | Q34 | ASG not terminating: grace period + impaired + ELB check | ✅ | A+B+F |
| 10 | E2 | Q61 | Engine upgrade = both upgraded simultaneously = downtime | ✅ | A |

**Final Score: 10/10 (100%) — Previous: 0/10 (0%)**

---

## Key Patterns Reinforced

### ASG Lifecycle
- **Maintenance** → Standby state OR suspend ReplaceUnhealthy
- **Rebalancing** → launch new FIRST, then terminate old (protect availability)
- **Unhealthy** → terminate FIRST, then launch new (two separate activities)
- **Grace period** → ASG waits before health-checking newly launched instances
- **Custom health checks** → ASG DOES terminate on custom checks (common myth: it doesn't)

### RDS Multi-AZ
- Replication = **synchronous** (Read Replica = async)
- **Engine upgrade** = both primary+standby simultaneously = **downtime**
- **OS patching** = rolling (standby first → failover → old primary) = minimal downtime
- **Storage auto-scaling** = native RDS feature, no migration needed

### Queue Selection
- "Exactly once" / "no duplicates" → **SQS FIFO**
- "Best effort ordering" / "max throughput" → **SQS Standard**

### Load Balancer Selection
- "Content-based routing" / "path-based" / "host-based" → **ALB** (Layer 7)
- "Static IP" / "UDP" / "ultra-low latency" → **NLB** (Layer 4)

### Cross-Account Private Connectivity
- No internet/VPN/DX available → **NLB + PrivateLink** (stays on AWS backbone)

### Migration Effort
- "Minimum effort" + existing feature available → **enable the feature** (don't migrate)
- RDS storage auto-scaling vs migrate to Aurora = toggle a setting vs full migration
