# Practice Exam Analysis — SAA-C03

**Date:** 2026-06-23 | **Source:** Udemy Practice Exams (Stephane Maarek)

---

## Overall Results

| Exam | Score | Percentage | Pass? |
|------|-------|-----------|-------|
| Practice Exam 1 | 36/65 | 55.4% | FAIL (need 72%) |
| Practice Exam 2 | 38/65 | 58.5% | FAIL (need 72%) |
| **Combined** | **74/130** | **56.9%** | — |

**Gap to pass: ~10-15 more correct answers per exam.**

---

## Errors by Domain

| Domain | Exam 1 | Exam 2 | Total | % of Errors |
|--------|--------|--------|-------|-------------|
| Design Secure Architectures | 11 | 9 | **20** | 36% |
| Design High-Performing Architectures | 11 | 6 | **17** | 30% |
| Design Resilient Architectures | 6 | 5 | **11** | 20% |
| Design Cost-Optimized Architectures | 3 | 5 | **8** | 14% |

**Top 2 domains = 66% of all errors.** Security and High-Performance are the priority fix areas.

---

## Critical Knowledge Gaps (Recurring Patterns)

### 1. Global Accelerator vs CloudFront (3 errors)
- **Pattern:** Choosing CloudFront when Global Accelerator is correct
- GA: TCP/UDP, gaming, static anycast IPs, blue-green traffic shifting
- CF: HTTP/HTTPS content caching, custom origins
- **Errors:** E1-Q20 (gaming), E2-Q20 (blue-green), E2-Q21 (NLB endpoints)

### 2. IAM Scoping — SCP vs Permission Boundary vs Policy (4 errors)
- SCP: account-level guardrails in Organizations
- Permission Boundary: per-user/role max permission cap
- IAM Policy: actual permissions
- **Errors:** E1-Q18 (cross-account roles), E2-Q12 (SCP for dev accounts), E2-Q18 (boundaries vs SCP), E2-Q65 (Resource ARN scope)

### 3. Cognito User Pools vs Identity Pools (2 errors)
- User Pools: authentication, JWT, ALB integration
- Identity Pools: AWS credential vending (STS)
- **Errors:** E2-Q19 (ALB auth), E1 serverless study also flagged this

### 4. RDS/Aurora Internals (4 errors)
- Multi-AZ = synchronous replication (not async)
- Aurora Global Database for global low-latency reads
- RDS Proxy for connection pooling
- Engine upgrades affect both primary AND standby
- **Errors:** E1-Q48, E1-Q57, E2-Q1, E2-Q61

### 5. S3 + Storage Nuances (5 errors)
- S3-IA 30-day minimum transition, retrieval fees make IA bad for frequent access
- S3 Standard < EFS < EBS pricing order
- Snowball → S3 → lifecycle to Glacier (no direct Snowball→Glacier)
- EFS cross-region via VPC peering
- S3 Access Points per-service with prefix policies
- **Errors:** E1-Q7, E1-Q35, E1-Q50, E1-Q51, E2-Q27, E2-Q54

### 6. ASG Behaviors (3 errors)
- Suspend `ReplaceUnhealthy` for maintenance patching
- Termination policy logic (which instance gets terminated)
- AZ distribution for fault tolerance (3 AZ × 2 > 2 AZ × 4)
- **Errors:** E1-Q43, E2-Q45, E2-Q46

### 7. Networking Access Patterns (3 errors)
- NLB + PrivateLink for private cross-account connectivity
- VPC sharing via RAM subnets (cheaper than Transit Gateway)
- API Gateway resource policy for IP allowlisting
- **Errors:** E1-Q62, E2-Q35, E2-Q41

### 8. Placement Groups & Instance Types (2 errors)
- Cluster PG = low-latency HPC (not partition)
- Dedicated Instances vs Dedicated Hosts
- **Errors:** E1-Q30, E2-Q37

### 9. EKS/Container Patterns (2 errors)
- IRSA (IAM Roles for Service Accounts) for pod-level access
- AWS Outposts + EKS Anywhere for on-prem
- **Errors:** E1-Q1, E1-Q14

### 10. Serverless/Lambda Patterns (2 errors)
- Kinesis → Lambda (not EC2 fleet)
- Glue for managed ETL (not EMR + Spark for simple jobs)
- **Errors:** E1-Q40, E1-Q45

---

## Cross-Reference with Study Progress

| Gap Topic | Studied? | Notes |
|-----------|----------|-------|
| Security & IAM | Yes (P6 complete, 90%) | SCP/Boundary/Policy distinctions still weak |
| Global Accelerator | Covered in networking P6 | Not deeply drilled — confused with CloudFront |
| RDS/Aurora | Yes (P4 100%) | Multi-AZ sync vs async, engine upgrade behavior missed |
| Storage S3 | Yes (P6 90%) | Lifecycle rules, pricing order gaps |
| ASG behaviors | Yes (P4 90%) | Termination policy, maintenance patterns |
| Cognito Pools | Covered in serverless | Still confusing User vs Identity Pools |
| Glue/EMR/Athena | P1 only (82%) | Needs more scenario practice |
| EKS IRSA/Outposts | Not specifically drilled | New gap area |

---

## Priority Study Plan

### Tier 1 — High Impact (20+ errors, fix these first)

1. **Security deep-dive:** SCP vs Permission Boundary matrix, cross-account role assumption, S3 resource ARN patterns, Dedicated Instances vs Hosts
2. **Global Accelerator vs CloudFront:** Decision tree — when GA, when CF, when both
3. **RDS/Aurora edge cases:** Multi-AZ replication type, engine upgrade behavior, RDS Proxy, Aurora Global DB

### Tier 2 — Medium Impact (10-15 errors)

4. **S3 lifecycle & pricing:** Transition minimums, IA retrieval costs, pricing order, Snowball landing zone
5. **ASG operational patterns:** Suspend processes, termination policy, AZ distribution math
6. **Networking access patterns:** PrivateLink, RAM subnet sharing, API Gateway resource policies

### Tier 3 — Fill Gaps

7. **Complete dr-architecture** P2-P4 (currently P2)
8. **Complete data-analytics** P2-P4 (currently P2)
9. **EKS patterns:** IRSA, Outposts, EKS Anywhere
10. **Keyword drill** on confused service pairs

---

## Recommended Next Actions

1. `/ai-tutor free security-identity mini-exam` — stress-test SCP/Boundary/Policy
2. `/ai-tutor dr-architecture` — continue P2 scenarios
3. `/ai-tutor data-analytics` — continue P2 scenarios
4. Create a **Global Accelerator vs CloudFront** decision cheat sheet
5. Take Practice Exam 3 after completing Tier 1 fixes — target 72%+
