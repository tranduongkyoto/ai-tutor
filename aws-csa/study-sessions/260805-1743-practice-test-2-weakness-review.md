# Practice Test 2 Retake — Weakness Review

**Original:** 38/65 (58%) — FAIL
**Retake:** 51/65 (78%) — PASS
**Improvement:** +20 points
**Date:** 2026-08-05 (review corrected 2026-08-06)
**Still wrong on retake:** 14 questions (8 Secure, 2 HP, 2 Resilient, 2 Cost)
**Note:** Retake uses different questions than original (Udemy randomizes). Questions from `retake-test-2-questions.md`.

---

## Pattern 1: EFS Performance Modes (1 error)

### Q7 — EFS Max I/O for Big Data

| Mode | Throughput | Latency | Use When |
|------|-----------|---------|----------|
| **General Purpose** | Lower | Lower latency | Most workloads, web serving |
| **Max I/O** | Higher (parallel) | Higher latency | Big data, HPC, many parallel clients |
| **Bursting** | Scales with size | Variable | Default throughput mode |
| **Provisioned** | Fixed throughput | Configurable | Known throughput needs |

**Key:** "Big data" + "improve performance" + "parallel processing" = **Max I/O mode**.

---

## Pattern 2: RDS Encrypted Snapshot Sharing (1 error)

### Q8 — Share RDS Database Cross-Account

To share an RDS database with an external account:
1. Create an **encrypted snapshot** of the database
2. **Share the snapshot** with the auditor's AWS account
3. Grant the auditor **access to the KMS key** used for encryption

**Key:** RDS snapshots can be shared cross-account. If encrypted with KMS, the recipient needs KMS key access too. Don't export to text/S3 (insecure, manual). Don't use read replicas (ongoing access, not a copy).

---

## Pattern 3: AWS Transfer Family for SFTP (1 error)

### Q12 — Legacy Vendors Need SFTP to S3

| Protocol Needed | AWS Service |
|----------------|-------------|
| **SFTP** (legacy vendors) | **AWS Transfer Family** (fully managed SFTP → S3) |
| REST API | Direct S3 API |
| NFS | File Gateway or EFS |
| SMB | FSx for Windows |

For vendor access control:
- **IAM roles per vendor** mapped to specific S3 prefixes
- **Transfer Family identity provider** integration (Cognito or custom) for federation

**Key:** "Legacy SFTP" + "fully managed" + "direct to S3" = **Transfer Family with SFTP**. Don't build custom SFTP on EC2.

---

## Pattern 4: KMS Multi-Region Keys for S3 CRR (1 error)

### Q25 — Same Encryption Key Across Regions

| KMS Key Type | Cross-Region? | Same Key? |
|-------------|--------------|-----------|
| **Single-Region key** | No — key stays in one Region | N/A |
| **Multi-Region key** | Yes — replicated across Regions | Same key material |

For S3 Cross-Region Replication with "same key in both Regions":
1. Create a **new bucket** with **KMS multi-Region key** enabled
2. Enable replication to destination Region
3. Copy existing data into the new bucket

**Key:** You can't convert a single-Region KMS key to multi-Region. Must create new key + new bucket. "Same key in both Regions" = multi-Region key.

---

## Pattern 5: S3 Access Points (1 error)

### Q28 — Per-Service Prefix Access Control

| Approach | Scalability | Maintenance |
|----------|------------|-------------|
| Single bucket policy with all ARNs | Low — grows unwieldy | High |
| IAM inline policies per user | Low — manual | High |
| **S3 Access Points per service** | **High — add service = add access point** | **Low** |
| Macie classification | Detective, not preventive | N/A |

**Key:** "Multiple services, each needs own prefix, scalable" = **S3 Access Points**. Each access point has its own policy scoped to a prefix.

---

## Pattern 6: ASG Health Check Grace Period (1 error)

### Q40 — ASG Not Terminating Unhealthy Instance

Common reasons ASG won't terminate an unhealthy instance:
1. **Health check grace period not expired** — ASG waits this period after instance launch before checking health
2. Instance is in **Standby** state
3. **ReplaceUnhealthy** process is suspended
4. Instance is protected with **scale-in protection**

**Key:** New instances get a grace period (default 300s). During this period, ASG ignores unhealthy status to allow app startup time.

---

## Pattern 7: RAM Shared VPC vs Transit Gateway vs VPC Peering (1 error)

### Q43 — Cheapest Cross-Account Private Connectivity

| Solution | Cost | Complexity |
|----------|------|-----------|
| **RAM shared subnets** | **Free** (sharing is free) | Low |
| VPC Peering | Low (per-GB data transfer) | Medium (N×N connections) |
| Transit Gateway | ~$0.05/hr + per-GB | Medium (hub-spoke) |
| PrivateLink | Per-endpoint + per-GB | Low per-service |

**Key:** "CHEAPEST" cross-account private connectivity = **RAM shared VPC subnets**. Instances in shared subnets communicate directly — no data transfer charges, no gateway costs.

---

## Pattern 8: Spot Fleet vs Spot Instances (1 error)

### Q44 — Monthly 2hr Batch Across Various Server Sizes

| | Spot Instances | Spot Fleet |
|--|---------------|------------|
| **Instance types** | Single type per request | **Multiple types, sizes** |
| **Availability** | Single pool | **Multiple pools** (better availability) |
| **Server failures** | Manual handling | **Built-in diversification** |

**Key:** "Multiple servers of various sizes" + "withstand server failures" = **Spot Fleet** (not individual Spot Instances). Spot Fleet spreads across instance types and AZs for resilience.

---

## Pattern 9: SSE-C for Customer-Managed On-Prem Keys (1 error)

### Q45 — Encryption Key Stored On-Premises

| | SSE-S3 | SSE-KMS | SSE-C | Client-Side |
|--|--------|---------|-------|-------------|
| **Key location** | AWS | AWS KMS | **Customer provides per-request** | Customer |
| **Encryption done by** | AWS | AWS | **AWS (server-side)** | Client |
| **Key stored by AWS?** | Yes | Yes (KMS) | **No** | No |

**Key:** "Key on-premises" + "offload encryption to S3" = **SSE-C**. Customer sends key with each request, AWS encrypts server-side, doesn't store the key. Client-side encryption doesn't offload encryption to S3.

---

## Pattern 10: Shared Services VPC (1 error)

### Q48 — Reduce Admin + Cost for Shared Services

| Pattern | Use When |
|---------|----------|
| **Shared Services VPC** | Central services (DNS, AD, monitoring) accessed by all spoke VPCs via Transit Gateway |
| Transit VPC | Legacy pattern (replaced by Transit Gateway) |
| Full mesh peering | Small number of VPCs, no central services |

**Key:** Hub-and-spoke with Transit Gateway already exists → add a **shared services VPC** for common resources. Reduces duplication across accounts.

---

## Pattern 11: Global Accelerator for NLB Endpoints (1 error)

### Q54 — Global Video Platform with NLBs, High Latency

| Solution | Protocol | Caching | Failover |
|----------|----------|---------|----------|
| Route 53 latency routing | DNS-based | No | DNS TTL dependent |
| CloudFront | HTTP/HTTPS | Yes | Origin failover |
| **Global Accelerator** | **TCP/UDP** | **No** | **Seconds (health check)** |

**Key:** "NLBs in multiple Regions" + "reduce latency" + "keep existing NLBs" = **Global Accelerator**. Routes traffic through AWS edge network to nearest healthy NLB. CloudFront can't sit in front of NLBs efficiently for non-HTTP traffic.

---

## Pattern 12: ASG Default Termination Policy (1 error)

### Q55 — Which Instance Gets Terminated?

Default termination policy order:
1. Select AZ with **most instances**
2. Find instance with **oldest launch configuration** (NOT launch template)
3. If tied, select **closest to next billing hour**

| Instance | Attribute | Terminated? |
|----------|-----------|-------------|
| A | Oldest launch **template** | No |
| **B** | **Oldest launch configuration** | **Yes ✅** |
| C | Newest launch config | No |
| D | Closest to billing hour | No (only tiebreaker) |

**Key:** Launch **configuration** (legacy) is checked BEFORE launch **template**. Instance B = oldest launch config → terminated first.

---

## Pattern 13: API Gateway Resource Policy for IP Restriction (1 error)

### Q60 — API Accessible Only from Trusted IPs

| Approach | Works? | Why |
|----------|--------|-----|
| Security Group on API Gateway | **No** | API Gateway doesn't have SGs |
| NACL on subnet | **No** | API Gateway isn't in a VPC subnet (regional API) |
| **Resource Policy with IP deny** | **Yes** | API Gateway resource policies support IP conditions |

**Key:** API Gateway access control = **resource policy** (not SGs, not NACLs). Use `"Condition": {"NotIpAddress": {"aws:SourceIp": [...]}}` to deny all except trusted IPs.

---

## Pattern 14: Global Accelerator for Blue-Green (1 error)

### Q61 — Blue-Green with DNS-Caching Mobile Clients

| Approach | DNS Caching Issue? |
|----------|-------------------|
| Route 53 weighted routing | **Yes** — mobile clients cache DNS, slow to shift |
| ELB traffic distribution | Single Region only |
| **Global Accelerator** | **No** — uses static IPs, traffic shift is instant at network layer |

**Key:** "DNS caching" on mobile phones = Route 53 weighted routing won't shift traffic fast enough. **Global Accelerator** uses static anycast IPs — traffic percentage changes take effect immediately, regardless of client DNS caching.

---

## Summary: Top 5 Areas to Drill

1. **Global Accelerator** — for NLB endpoints, UDP, blue-green without DNS caching issues, static IPs
2. **S3 Access Points** — per-service prefix access at scale
3. **SSE-C** — "key stored on-prem" + "offload encryption to S3"
4. **RAM shared VPC** — cheapest cross-account connectivity (free)
5. **ASG termination policy** — oldest launch CONFIGURATION (not template), then billing hour
