# Compute — Mini Exam: Comprehensive Final (Phase 6)
**Date:** 2026-05-14 12:55
**Score:** 10/10 (100%)
**Scope:** comprehensive — full domain exam, all topics

---

## Questions & Results

### Q1 ✓ — Security Group defaults (security-groups) [Easy]
**Question:** Default behavior of Security Groups on EC2 launch?
**Answer: B** — All inbound blocked, all outbound allowed. Allow rules only.

### Q2 ✓ — RI for steady database (purchasing-options) [Medium]
**Question:** 24/7 PostgreSQL database, 3-year commitment, most cost savings?
**Answer: C** — 3-year All Upfront Reserved Instance (~72% discount). Steady-state = RI.

### Q3 ✓ — App Runner VPC support (elastic-container-service) [Hard]
**Question:** Is App Runner valid for team with minimal AWS experience needing VPC access to Aurora?
**Answer: B** — Yes, App Runner supports VPC access, auto HTTPS, auto-scaling.

### Q4 ✓ — Hibernate requirements (hibernate) [Medium]
**Question:** Which is NOT a requirement for EC2 Hibernate?
**Answer: C** — Instance store root volume is NOT supported. Must be encrypted EBS.

### Q5 ✓ — ECS Fargate + SQS auto scaling (elastic-container-service) [Hard]
**Question:** Order processing via SQS, variable 100-10,000/min, no pre-provisioning. (Select TWO)
**Answer: A, C** — Fargate (serverless, no pre-provisioning) + Service Auto Scaling on SQS queue depth.

### Q6 ✓ — Spread PG limit (placement-groups) [Easy]
**Question:** Max instances per AZ in Spread Placement Group?
**Answer: B** — 7 instances per AZ per group.

### Q7 ✓ — Mixed purchasing options (purchasing-options) [Hard]
**Question:** Web server (24/7) + batch job (interruptible) + quarterly audit (guaranteed AZ capacity)?
**Answer: B** — RI + Spot + Capacity Reservation. Capacity Reservation guarantees AZ-specific capacity.

### Q8 ✓ — Multi-subnet ENI (elastic-network-interface) [Medium]
**Question:** Network monitoring across 3 subnets in same AZ?
**Answer: B** — Three ENIs in different subnets, same AZ. ENIs are AZ-bound.

### Q9 ✓ — Memory Optimized for ML (instance-types) [Medium]
**Question:** 384 GiB RAM for in-memory ML data processing?
**Answer: B** — Memory Optimized R-family. R5.16xlarge offers 512 GiB.

### Q10 ✓ — EKS persistent storage with Fargate (elastic-kubernetes-service) [Hard]
**Question:** Persistent storage for EKS working with both EC2 nodes AND Fargate pods? (Select TWO)
**Answer: A, D** — EFS works with both EC2 and Fargate. CSI driver required for EKS persistent volumes.

---

## Summary
- **Score:** 10/10 (100%)
- **Missed topics:** none
- **All topics covered:** security-groups, purchasing-options, elastic-container-service, hibernate, placement-groups, elastic-network-interface, instance-types, elastic-kubernetes-service
- **Phase 6 PASSED (≥80%)** — Domain complete!
