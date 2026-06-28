# Practice Exam Redo — Design Cost-Optimized Architectures (8 Errors)

**Date:** 2026-06-28 | **Source:** Udemy Practice Exams 1 & 2
**Reference:** `260628-0824-cost-optimized-knowledge-review.md`
**Format:** Exact exam questions, full explanations

---

## Results Summary

| # | Exam | Q# | Topic | Result | Correct Answer |
|---|------|----|-------|--------|----------------|
| 1 | E1 | Q7 | S3 One Zone-IA after 30 days (not 7) | ✅ | B |
| 2 | E1 | Q35 | S3 Standard for short-lived heavy-access data | ✅ | C |
| 3 | E1 | Q50 | Storage pricing: S3 < EFS < EBS (provisioned trap) | ✅ | B |
| 4 | E2 | Q27 | Snowball → S3 → lifecycle to Glacier Deep Archive | ✅ | D |
| 5 | E2 | Q35 | VPC Sharing via RAM = cheapest cross-account networking | ✅ | C |
| 6 | E2 | Q45 | ASG terminates oldest launch configuration first | ✅ | B (Instance B) |
| 7 | E2 | Q46 | 3 AZs × 2 instances = 6 total (minimum for HA with 4 required) | ✅ | A |
| 8 | E2 | Q47 | Spot Fleet for short, distributed, failure-tolerant workloads | ✅ | D |

**Final Score: 8/8 (100%) — Previous: 0/8 (0%)**

---

## Key Patterns Reinforced

### S3 Storage Class Selection
- Short-lived (<30 days) + frequently accessed → **S3 Standard** (IA 30-day minimum makes it more expensive)
- Re-creatable + infrequent → **One Zone-IA** (cheapest IA, single AZ OK)
- Transition timing: always wait until **30 days** before moving to IA (min duration charge)
- Long-term archive → **Glacier Deep Archive** (cheapest at $0.00099/GB)

### Storage Pricing
- S3 ($0.023/GB used) < EFS ($0.30/GB used) < EBS (charges for PROVISIONED, not used)
- EBS trap: 100GB provisioned = pay for 100GB even if only 1GB stored

### Snowball Limitations
- Snowball → S3 only (NOT directly to Glacier)
- Use lifecycle policy to move to Glacier/Deep Archive after landing in S3

### Cross-Account Networking Cost
- VPC Sharing via RAM = **free** (cheapest)
- VPC Peering = no hourly cost but N×N complexity
- Transit Gateway = $0.05/hr + data fees (scalable but costs money)

### ASG Default Termination
- AZ with most instances → oldest launch **configuration** → closest to billing hour

### HA Distribution
- 3 AZs = cheaper than 2 AZs for same HA guarantee (lose 1/3 vs 1/2)

### EC2 Purchasing
- Short burst workload + interruptible → **Spot Fleet** (diversified, cheapest)
- Steady 24/7 → Reserved Instances
- 2 hours/month ≠ Reserved Instances
