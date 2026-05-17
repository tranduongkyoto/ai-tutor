# Storage — Mini Exam: Scenarios (Phase 4)
**Date:** 2026-05-16 05:31
**Score:** 6/10 (60%)
**Scope:** scenarios — test scenario reasoning from scenario-generator

---

## Questions & Results

### Q1 ✓ — FSx for Lustre for video editing (fsx)
**Question:** A video streaming company stores 200 TB of raw footage on-premises. Their editing team of 50 Linux workstations needs shared access with high sequential throughput for 4K video editing. Which solution provides the best performance?

A) Amazon EFS with Provisioned Throughput mode set to 1 GiB/s
B) Amazon FSx for Lustre filesystem linked to an S3 bucket
C) Amazon EBS io2 volumes attached to each workstation with rsync
D) S3 Standard with Transfer Acceleration and byte-range fetches

**Your answer: B** — Correct. FSx for Lustre is purpose-built for HPC/media workloads with massive sequential throughput, POSIX-compatible for Linux.

---

### Q2 ✓ — io2 Block Express with Multi-Attach (ebs-types)
**Question:** SaaS company needs 45,000 sustained IOPS with sub-ms latency for PostgreSQL. Need to attach volume to standby instance in same AZ for rapid failover. Which EBS configuration?

A) Two gp3 in RAID 0
B) io1 with Multi-Attach, 45K IOPS
C) io2 Block Express with Multi-Attach, 45K IOPS
D) io2 with snapshots for failover

**Your answer: C** — Correct. io2 Block Express supports 256K IOPS, sub-ms latency, and Multi-Attach. Snapshot-based failover is too slow.

---

### Q3 ✗ — S3 Object Lock Compliance mode (s3-security)
**Question:** Patient records cannot be modified or deleted for 7 years — even by root account. Which S3 feature?

A) Versioning with MFA Delete
B) S3 Object Lock in Compliance mode with 7-year retention
C) Bucket Policy denying delete/put
D) S3 Object Lock in Governance mode with 7-year retention

**Your answer: C** — Incorrect. Correct answer: B. Compliance mode = WORM, nobody can override including root. Governance mode = privileged users can bypass. Bucket policies can be modified by owner.

---

### Q4 ✗ — S3 prefix hot spot (s3-performance)
**Question:** 500K files/hour written to `logs/2026/05/16/HH-MM-SS-{uuid}.json`. Throttling during peak. Cause and solution?

A) Exceeded max object count
B) Single prefix hitting 3,500 PUT/s limit — distribute across prefixes
C) SSE-KMS hitting KMS API quota
D) Transfer Acceleration not enabled

**Your answer: C** — Incorrect. Correct answer: B. The single key pattern concentrates all writes on one prefix. During peak hours, it exceeds 3,500 PUT/s per prefix. No mention of KMS in the question.

---

### Q5 ✓ — Intelligent-Tiering for zero overhead (s3-classes)
**Question:** Profile images: frequent first week, rare after 30d, never after 1 year. Zero operational overhead. Most cost-effective?

A) Standard + lifecycle to Standard-IA at 30d, expire 365d
B) Intelligent-Tiering + Archive Instant, expire 365d
C) Standard 7d → One Zone-IA 7d, expire 365d
D) Intelligent-Tiering (Frequent + Infrequent only), expire 365d

**Your answer: D** — Correct. Intelligent-Tiering auto-tiers with zero operational overhead. No Archive Instant needed since images expire at 365d anyway.

---

### Q6 ✓ — FSx File Gateway for Windows file shares (storage-gateway)
**Question:** 50 TB Windows file server with SMB + Active Directory. 500 employees need local-speed access with full data in AWS. Which solution?

A) FSx for Windows + FSx File Gateway on-premises
B) EFS + S3 File Gateway
C) S3 + S3 File Gateway with SMB
D) FSx for Lustre + S3 + Direct Connect

**Your answer: A** — Correct. FSx for Windows = native SMB + AD. FSx File Gateway = local cache for on-premises low-latency access.

---

### Q7 ✗ — S3 lifecycle minimum storage periods (s3-lifecycle)
**Question:** 500 GB/day video output. 24hr hot access (10+ times), occasional for 90d, retain 2 years. Minimize cost?

A) Standard → Standard-IA (day 2) → Glacier Flexible (day 91) → expire 730d
B) Standard → Standard-IA (day 30) → Glacier Deep Archive (day 91) → expire 730d
C) Standard → Glacier Instant (day 2) → Glacier Deep Archive (day 91) → expire 730d
D) Standard → One Zone-IA (day 2) → Glacier Deep Archive (day 91) → expire 730d

**Your answer: C** — Incorrect. Correct answer: B. Standard-IA has 30-day minimum storage charge — transitioning at day 2 doesn't save money. Keep Standard for 30 days, then Standard-IA (which is cheaper than Glacier Instant for occasional access with no retrieval fees). Glacier Deep Archive for long-term.

---

### Q8 ✗ — Small files problem with Athena (s3-performance)
**Question:** 200 IoT sensors writing 1 file/sec to S3. Athena queries timing out during peak. Cause?

A) Too many small files — aggregate into Parquet with Glue
B) Exceeded bucket storage quota
C) Athena concurrent query limit
D) Hot partitions from sensor-id prefix

**Your answer: D** — Incorrect. Correct answer: A. 200 sensors × 86,400 sec = 17.28M files/day. Athena's overhead opening millions of tiny JSON files causes timeouts. Solution: compact into larger Parquet files. 200 sensor prefixes already distribute S3 load adequately.

---

### Q9 ✗ — SSE-C when AWS must never store key (s3-security)
**Question:** Agency needs encryption where AWS never stores the key. Agency handles all rotation. Which method?

A) SSE-KMS with Customer Managed Key (CMK)
B) SSE-C over HTTPS
C) SSE-S3 with default encryption
D) Client-side encryption with AWS Encryption SDK

**Your answer: A** — Incorrect. Correct answer: B. SSE-KMS stores keys IN AWS (within KMS service). SSE-C = customer provides key per request, AWS uses it in memory then discards it. "AWS never stores the key" = SSE-C.

---

### Q10 ✓ — Snowball Edge for large transfer with bandwidth constraints (snow-family)
**Question:** 400 TB from Tokyo data center to S3 ap-northeast-1. 10 Gbps internet but can only use 50%. Need within 2 weeks. Which method?

A) Direct Connect 10 Gbps
B) S3 Transfer Acceleration + 50% throttle
C) Multiple Snowball Edge devices
D) AWS DataSync with 5 Gbps throttle

**Your answer: C** — Correct. 5 Snowball Edge devices (80 TB each), load locally at full speed, ship domestically in 1-2 days. Zero network impact, guaranteed timeline. Direct Connect takes months to provision.

---

## Summary
- **Score:** 6/10 (60%)
- **Missed topics:** s3-security, s3-performance, s3-lifecycle
- **Strong areas:** fsx, ebs-types, s3-classes, storage-gateway, snow-family
- **Key lessons:**
  - Object Lock Compliance mode = nobody can override (not even root). Governance = privileged bypass possible.
  - SSE-C = "AWS never stores key." SSE-KMS = key stored in KMS within AWS.
  - Single prefix pattern + high write rate = hot spot throttling. Distribute across prefixes.
  - Millions of small files = Athena timeout. Compact with Glue into Parquet.
  - Standard-IA 30-day minimum: transitioning before day 30 doesn't save money.
