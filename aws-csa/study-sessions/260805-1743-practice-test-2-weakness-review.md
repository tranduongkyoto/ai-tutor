# Practice Test 2 — Weakness Review

**Original:** 38/65 (58%) — FAIL
**Retake:** 51/65 (78%) — PASS
**Improvement:** +20 points
**Date:** 2026-08-05
**Still wrong on retake:** 14 questions (7 Secure, 2 HP, 2 Resilient, 3 Cost)

---

## Pattern 1: Security Group Chaining (1 error)

### Q44 — ALB + EC2 + RDS Security Group Chain

The classic 3-tier security group pattern:

```
Internet → ALB (SG: inbound 443 from 0.0.0.0/0)
              → EC2 (SG: inbound from ALB SG)
                  → RDS (SG: inbound from EC2 SG)
```

| Layer | Inbound Rule Source |
|-------|-------------------|
| ALB SG | `0.0.0.0/0` on port 443 (HTTPS) |
| EC2 SG | ALB security group on app port |
| RDS SG | EC2 security group on DB port |

**Key:** Each layer's SG references the PREVIOUS layer's SG — never direct IP or `0.0.0.0/0` for internal tiers.

---

## Pattern 2: WAF vs Security Groups for IP Blocking (1 error)

### Q8 — Block Malicious IPs on CloudFront

| Service | Can Block IPs? | Works With |
|---------|---------------|------------|
| **AWS WAF IP match** | Yes — IP set rules | CloudFront, ALB, API Gateway |
| **Security Groups** | Yes — deny rules | EC2, ALB (but NOT CloudFront) |
| **NACLs** | Yes — subnet level | VPC subnets only |

**Key:** CloudFront sits outside the VPC — security groups and NACLs don't apply. Use **WAF IP match condition** on CloudFront.

---

## Pattern 3: SCP for Organizational Guardrails (1 error)

### Q12 — Prevent Developers from Disabling CloudTrail

| Tool | Scope | Use When |
|------|-------|----------|
| **SCP (Service Control Policy)** | All accounts in OU | "Prevent changes" across all accounts in an organization |
| **IAM Policy** | Single account/user | Per-user or per-role permissions |
| **AWS Config Rule** | Detective (after the fact) | "Detect non-compliance" — doesn't prevent |

**Key:** "Prohibit changes to CloudTrail across all accounts" = **SCP attached to OU**. IAM policies can be overridden per-account; SCPs cannot.

---

## Pattern 4: IAM Policy Interpretation (1 error)

### Q25 — Reading IAM Policy Conditions

Common IAM condition keys:
| Condition Key | Tests |
|--------------|-------|
| `aws:SourceIp` | IP address of API caller |
| `aws:RequestedRegion` | Region the API call targets |
| `aws:PrincipalTag` | Tag on the calling principal |
| `ec2:ResourceTag` | Tag on the EC2 resource |

**Key:** `"Condition": {"IpAddress": {"aws:SourceIp": "x.x.x.x/x"}}` restricts API calls to specific source IPs. Read conditions carefully — they narrow WHICH requests are allowed/denied.

---

## Pattern 5: EFS Performance Modes (1 error)

### Q7 — EFS Max I/O vs General Purpose

| Mode | Throughput | Latency | Use When |
|------|-----------|---------|----------|
| **General Purpose** | Lower | Lower latency | Most workloads, web serving |
| **Max I/O** | Higher (parallel) | Higher latency | Big data, HPC, many clients |

**Key:** "Improve performance" + "big data" + "many parallel workflows" = **Max I/O mode**.

---

## Pattern 6: FSx for Windows File Server (1 error)

### Q40 — SMB Protocol for Windows Workloads

| Service | Protocol | Use When |
|---------|----------|----------|
| **FSx for Windows** | SMB | Windows workstations, AD integration |
| **FSx for Lustre** | POSIX | HPC, ML, Linux |
| **EFS** | NFS | Linux EC2/ECS/Lambda |
| **File Gateway** | NFS/SMB | On-prem → S3 hybrid |

**Key:** "Windows" + "SMB" + "Active Directory" = **FSx for Windows File Server**.

---

## Pattern 7: EC2 Purchasing Mix (1 error)

### Q43 — Reserved + Spot for Mixed Workloads

| Workload Pattern | Purchasing Strategy |
|-----------------|-------------------|
| Steady baseline (always running) | **Reserved Instances** |
| Flexible, interruptible spikes | **Spot Instances** |
| Short-term, can't be interrupted | **On-Demand** |
| 70 always-on + 30 flexible | **70 Reserved + 30 Spot** |

**Key:** Match purchasing to workload pattern. "100 instances, 70% steady + 30% flexible" = 70 RI + 30 Spot.

---

## Pattern 8: ASG Termination Policy (1 error)

### Q45 — Which Instance Gets Terminated During Scale-In?

ASG default termination policy order:
1. Select the AZ with the most instances
2. Within that AZ, select the instance with the **oldest launch configuration/template**
3. If tied, select the instance **closest to the next billing hour**

**Key:** ASG always tries to balance AZs first, then uses launch config age, then billing hour proximity.

---

## Pattern 9: RDS Read Replica Data Transfer Costs (1 error)

### Q48 — Cross-Region Read Replica Charges

| Transfer Type | Cost |
|--------------|------|
| Same Region, same AZ | Free |
| Same Region, cross-AZ | ~$0.01/GB |
| **Cross-Region** | **Data transfer charges apply** |

**Key:** Cross-Region read replica replication incurs data transfer charges. Same-Region does not.

---

## Pattern 10: S3 Access Points (1 error)

### Q54 — Per-Service Access Control for Shared S3 Bucket

| Tool | Use When |
|------|----------|
| **S3 Access Points** | Multiple services/teams need different access to same bucket |
| **Bucket Policy** | Single access pattern for the whole bucket |
| **IAM Policy** | Per-user/role access control |

**Key:** "Multiple analytics services, each needing different access to shared bucket" = **S3 Access Points** with individual access point policies.

---

## Pattern 11: Lambda Cross-Account S3 Access (1 error)

### Q55 — Lambda in Account A Accessing S3 in Account B

Two requirements for cross-account Lambda→S3:
1. **Lambda execution role** in Account A must have S3 permissions
2. **S3 bucket policy** in Account B must trust Account A's Lambda role

**Key:** The Lambda execution role's trust policy must allow `sts:AssumeRole`, and the S3 bucket policy must grant access to that role's ARN.

---

## Pattern 12: SSE-C vs SSE-KMS vs SSE-S3 (1 error)

### Q60 — Customer Provides and Manages Keys

| | SSE-S3 | SSE-KMS | SSE-C |
|--|--------|---------|-------|
| **Who manages key?** | AWS | AWS KMS (you control) | **You provide per-request** |
| **Key stored by AWS?** | Yes | Yes (in KMS) | **No** |
| **Audit trail?** | No | Yes (CloudTrail) | No |
| **Use when** | Default, simplest | Audit + rotation needed | **Full key control, customer manages** |

**Key:** "Customer provides and manages their own encryption keys" = **SSE-C**. "Audit trail" = SSE-KMS.

---

## Pattern 13: RDS Multi-AZ Engine Upgrade (1 error)

### Q61 — Multi-AZ Database Engine Upgrade Behavior

Multi-AZ upgrade process:
1. Upgrade **standby** first
2. Promote standby to primary (brief failover)
3. Upgrade old primary (now new standby)

**Key:** Engine-level upgrades trigger a brief downtime/failover. OS maintenance is similar but can use maintenance windows.

---

## Summary: Top 5 Areas to Drill

1. **Security group chaining** — each tier references the previous tier's SG, not direct IPs
2. **WAF for CloudFront** — SGs and NACLs don't work with CloudFront; WAF does
3. **EFS Max I/O** — big data parallel workloads need Max I/O mode
4. **S3 Access Points** — per-service access control for shared buckets
5. **SSE-C vs SSE-KMS** — "customer manages keys" = SSE-C; "audit trail" = SSE-KMS
