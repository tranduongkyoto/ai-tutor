# Practice Test 3 Retake — Weakness Review

**Original:** 39/64 (61%) — FAIL
**Retake:** 54/65 (83%) — PASS
**Improvement:** +22 points
**Date:** 2026-08-06
**Still wrong on retake:** 11 questions (5 HP, 2 Secure, 3 Resilient, 1 Cost)
**Note:** Retake uses different questions than original (Udemy randomizes).

---

## Pattern 1: DataSync vs File Gateway vs Transfer Family (1 error)

### Q8 — DataSync for Multi-Service Online Migration

| Service | Purpose | Destination |
|---------|---------|-------------|
| **AWS DataSync** | **Automated online data transfer** | **S3, EFS, FSx** (all three) |
| File Gateway | Ongoing hybrid NFS/SMB access | S3 only (behind NFS/SMB interface) |
| Transfer Family | SFTP/FTPS for external partners | S3, EFS |
| Snowball | Offline physical transfer (TBs/PBs) | S3 |

**Key:** "Move data to S3, EFS, AND FSx easily and quickly" = **DataSync** (supports all three as targets). File Gateway only backs to S3. Transfer Family is for SFTP protocol, not bulk migration.

---

## Pattern 2: ECS Auto Scaling Metric (1 error)

### Q11 — Scale ECS on Service CPU, Not ALB CPU

| Metric Source | Use For Scaling? |
|--------------|-----------------|
| **ECS Service CPU utilization** | **Yes — this is the container workload metric** |
| ALB CPU utilization | No — ALB is managed, its CPU isn't meaningful |
| ALB target group CPU | No — target group doesn't have its own CPU metric |
| CloudWatch alarm CPU | Vague — which CPU? Must specify the right source |

**Key:** ECS containers run the workload → scale on **ECS service metrics** (CPU, memory). ALB is infrastructure managed by AWS — its CPU is irrelevant to your app's scaling needs.

---

## Pattern 3: S3 Transfer Acceleration vs CloudFront (1 error)

### Q17 — S3TA for Global Large File Uploads

| Service | Best For | Upload? | Download? |
|---------|---------|---------|-----------|
| **S3 Transfer Acceleration** | **Faster uploads from distant locations** | **Yes (primary)** | Yes |
| CloudFront | Content delivery/caching | PUT supported but caching is main feature | Yes (primary) |
| Global Accelerator | TCP/UDP app routing | No S3 integration | N/A |

**Key:** "Upload 10GB video files from global users to S3" = **S3 Transfer Acceleration**. CloudFront is primarily for downloads/caching. S3TA uses edge locations specifically optimized for upload acceleration.

---

## Pattern 4: SSE-S3 Auto-Generates Unique Keys Per Object (1 error)

### Q24 — SSE-S3 for Multiple Keys Without Management

| Encryption | Key Per Object? | Key Management |
|-----------|----------------|----------------|
| **SSE-S3** | **Yes — automatic unique key per object** | **None — fully managed by AWS** |
| SSE-KMS | One CMK, but data keys per object | You manage CMK, audit via CloudTrail |
| SSE-C | You provide key per request | Full customer responsibility |

**Key:** "Multiple encryption keys by dividing data into chunks" = SSE-S3's default behavior. SSE-S3 automatically generates a unique AES-256 key per object. No need for KMS multi-Region keys or separate buckets — SSE-S3 handles it transparently.

---

## Pattern 5: EC2 Instance Recovery Behavior (1 error)

### Q26 — What's Retained During CloudWatch EC2 Recovery

| Attribute | Retained After Recovery? |
|-----------|------------------------|
| Instance ID | **Yes** |
| Private IP addresses | **Yes** |
| Elastic IP addresses | **Yes** |
| **Public IPv4 address** | **Yes** |
| Metadata, placement group | **Yes** |
| In-memory (RAM) data | **No — lost during recovery** |

Recovery = instance migrated to new hardware. Everything persists EXCEPT in-memory data. Terminated instances CANNOT be recovered.

**Key:** "Recovered instance is identical to original" — same ID, same IPs (including public IPv4), same EBS volumes. Only RAM is lost.

---

## Pattern 6: Security Group Source Types (1 error)

### Q28 — Invalid SG Source: Internet Gateway ID

Valid security group inbound rule sources:
| Source Type | Example | Valid? |
|------------|---------|--------|
| Security group ID | sg-0123456789abcdef0 | **Yes** |
| IP address | 10.0.1.5/32 | **Yes** |
| CIDR block | 10.0.0.0/16 | **Yes** |
| Prefix list | pl-0123456789abcdef0 | **Yes** |
| **Internet Gateway ID** | **igw-0123456789abcdef0** | **No ✗** |

**Key:** You CANNOT use an Internet Gateway ID as a security group source. IGW is a VPC-level construct, not a traffic source identifier. SG rules reference IPs, CIDRs, other SGs, or prefix lists.

---

## Pattern 7: What Makes a Subnet Public (1 error)

### Q34 — Internet Gateway Makes a Subnet Public

A subnet is "public" when its route table has a route to an **Internet Gateway**:

```
Route Table Entry:
  Destination: 0.0.0.0/0
  Target: igw-xxxxxxxx  ← THIS makes it public
```

| Component | Makes Subnet Public? |
|-----------|---------------------|
| **Internet Gateway (IGW)** | **Yes — the route to IGW is what defines "public"** |
| Route Table | No — it's just the container for routes |
| Subnet itself | No — subnets aren't inherently public or private |
| NAT instance/gateway | No — NAT is for private subnets to reach internet |

**Key:** The question asks what COMPONENT makes it public. The answer is the **Internet Gateway** — without it, the subnet has no direct internet path regardless of route table configuration.

---

## Pattern 8: Route 53 Alias Record for Zone Apex (1 error)

### Q42 — Zone Apex Cannot Use CNAME

| Record Type | Zone Apex (example.com)? | Subdomain (www.example.com)? |
|------------|-------------------------|------------------------------|
| **Alias** | **Yes ✓** | Yes |
| CNAME | **No ✗** (RFC violation) | Yes |
| A/AAAA | Yes (static IP only) | Yes |
| MX | Yes (email only) | Yes |
| NS | Yes (delegation only) | Yes |

**Key:** Zone apex (naked domain) CANNOT use CNAME per DNS RFC. Route 53 **Alias record** is the AWS-specific solution — it works at zone apex and resolves to AWS resources (ALB, CloudFront, S3, etc.) with no extra charge.

---

## Pattern 9: AWS Directory Service Types (1 error)

### Q46 — Cloud Directory + Managed Microsoft AD

| Service | What It Is | Use When |
|---------|-----------|----------|
| **Amazon Cloud Directory** | **Hierarchical multi-dimensional directory** | Org charts, device registries, course catalogs |
| **AWS Managed Microsoft AD** | **Full Microsoft AD on AWS** | Trust with on-prem AD, supports LDAP, Kerberos, Group Policy |
| Simple AD | Subset of AD features (Samba-based) | Small workloads, no trust relationships needed |
| AD Connector | Proxy to on-prem AD (no data stored in AWS) | Redirect auth to existing on-prem AD |

**Key:** "Uses Microsoft Active Directory on-prem" + "extend to AWS" = **Managed Microsoft AD** (supports trust). Cloud Directory is for application-level hierarchical data, not traditional AD.

---

## Pattern 10: CloudWatch EC2 Recovery Action (1 error)

### Q56 — CW Alarm Recovery Preserves Instance Metadata

| Recovery Method | Preserves Instance? | Managed? |
|----------------|--------------------| ---------|
| **CloudWatch alarm + recover action** | **Yes — same ID, IPs, EBS** | **Yes — automatic** |
| ASG replacement | No — new instance, new ID | Yes |
| Manual stop/start | Depends — public IP may change | No |
| EventBridge | Can't directly trigger EC2 recovery | N/A |

**Key:** For a single EC2 instance (no ASG) that needs automatic recovery with all metadata preserved → **CloudWatch alarm with EC2 recovery action**. This is the simplest disaster recovery for small/startup workloads.

---

## Pattern 11: NAT Instance vs NAT Gateway Features (1 error)

### Q57 — NAT Instance = EC2, NAT Gateway = Managed

| Feature | NAT Instance (EC2) | NAT Gateway (Managed) |
|---------|-------------------|----------------------|
| **Bastion server** | **Yes** (it's an EC2 instance) | No |
| **Security Groups** | **Yes** (EC2 has SGs) | No (uses NACLs only) |
| **Port forwarding** | **Yes** (iptables) | No |
| Bandwidth | Limited by instance type | Up to 100 Gbps |
| HA | Manual (scripts, ASG) | Managed per-AZ |
| Maintenance | You patch OS | AWS manages |

**Key:** NAT instance is just an EC2 instance doing NAT — so it inherits ALL EC2 capabilities: security groups, bastion access, port forwarding. NAT Gateway is a managed black box — higher throughput but no customization.

---

## Summary: Top 5 Areas to Drill

1. **DataSync** — the multi-service online migration tool (S3 + EFS + FSx), not File Gateway or Transfer Family
2. **ECS scaling** — scale on ECS service CPU, not ALB metrics
3. **S3TA vs CloudFront** — S3TA for uploads, CloudFront for downloads/caching
4. **Zone apex** — cannot use CNAME, must use Route 53 Alias record
5. **NAT instance vs gateway** — NAT instance = EC2 (SG, bastion, port forwarding); NAT gateway = managed (no SG, no bastion)
