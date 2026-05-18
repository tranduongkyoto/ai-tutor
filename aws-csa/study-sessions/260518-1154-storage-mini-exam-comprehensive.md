# Storage — Mini Exam: Comprehensive Final (Phase 6)
**Date:** 2026-05-18 11:54
**Score:** 9/10 (90%)
**Scope:** comprehensive — Full domain exam covering all topics

---

## Questions & Results

### Q1 ✓ — S3 Lifecycle Cost-Effective Configuration (s3-lifecycle)
**Question:** A media company stores video files in Simple Storage Service (S3) Standard. Videos are frequently accessed for the first 45 days, then rarely accessed for the next 6 months, after which they must be retained for 7 years for compliance. The company wants to minimize storage costs while maintaining instant retrieval for the first 6 months. Which lifecycle configuration is most cost-effective?

A) Transition to S3 Standard-Infrequent Access (Standard-IA) after 45 days, then transition to S3 Glacier Instant Retrieval after 120 days, then transition to S3 Glacier Deep Archive after 210 days
B) Transition to S3 Glacier Instant Retrieval after 45 days, then transition to S3 Glacier Deep Archive after 180 days
C) Transition to S3 Standard-Infrequent Access (Standard-IA) after 45 days, then transition to S3 Glacier Deep Archive after 180 days
D) Transition to S3 Intelligent-Tiering after 45 days, then transition to S3 Glacier Flexible Retrieval after 180 days

**Your answer: A** — Correct. Option A respects all minimum storage durations: Standard-IA stays 75 days (exceeds 30-day min), Glacier Instant stays 90 days (meets 90-day min), then Deep Archive for long-term compliance.

---

### Q2 ✓ — EBS Volume Type for High IOPS (ebs-types)
**Question:** A company runs a high-performance database on Amazon Elastic Compute Cloud (EC2) with an Elastic Block Store (EBS) volume. The database requires consistent sub-millisecond latency and 200,000 Input/Output Operations Per Second (IOPS). Which EBS volume type meets these requirements?

A) gp3 (General Purpose Solid-State Drive) with provisioned IOPS set to 200,000
B) io2 Block Express (Provisioned IOPS Solid-State Drive) with 200,000 IOPS provisioned
C) io1 (Provisioned IOPS Solid-State Drive) on a Nitro-based instance with 200,000 IOPS
D) Two gp3 volumes in RAID 0 configuration, each provisioned at 100,000 IOPS

**Your answer: B** — Correct. io2 Block Express supports up to 256,000 IOPS with sub-millisecond latency — the only EBS type capable of 200,000 IOPS on a single volume.

---

### Q3 ✓ — S3 Object Lock Compliance vs Governance (s3-security)
**Question:** A healthcare company stores patient records in Simple Storage Service (S3). Regulations require that records cannot be deleted or overwritten by ANY user — including the AWS account root user — for 10 years. Which combination of S3 features enforces this requirement?

A) S3 Versioning enabled with a bucket policy that denies `s3:DeleteObject` for all principals
B) S3 Object Lock in Governance mode with a 10-year retention period
C) S3 Object Lock in Compliance mode with a 10-year retention period
D) S3 Versioning with Multi-Factor Authentication (MFA) Delete enabled and a 10-year lifecycle expiration rule

**Your answer: C** — Correct. Compliance mode prevents ALL users — including root — from deleting or overwriting objects during retention. True WORM protection.

---

### Q4 ✓ — Snow Family Device Selection (snow-family)
**Question:** A research team at a remote Arctic station needs to transfer 6 TB of climate sensor data to AWS. The station has intermittent satellite connectivity (256 Kbps, available 4 hours/day). Which AWS Snow Family device is most appropriate?

A) AWS Snowball Edge Storage Optimized shipped to the station, data loaded locally, then shipped back to AWS
B) AWS Snowcone shipped to the station, data loaded locally, then shipped back to AWS
C) AWS Snowmobile driven to the nearest accessible road, with data transferred via satellite link to the Snowmobile
D) AWS Snowball Edge Compute Optimized shipped to the station for edge processing and data collection

**Your answer: B** — Correct. Snowcone fits 8 TB HDD (or 14 TB SSD), is backpack-portable, ideal for remote/harsh environments. 6 TB fits within capacity.

---

### Q5 ✓ — S3 Prefix Throughput and Hot Spots (s3-performance)
**Question:** A data lake receives 25,000 PUT requests per second to Simple Storage Service (S3), all writing to the key pattern `s3://data-lake/raw/2026/05/18/sensor-{id}.json`. The team reports frequent HTTP 503 Slow Down errors. What is the most effective solution?

A) Enable S3 Transfer Acceleration on the bucket to increase upload throughput
B) Distribute objects across multiple prefixes by adding a hash prefix, such as `s3://data-lake/raw/{hash}/2026/05/18/sensor-{id}.json`
C) Switch the bucket to S3 Express One Zone for higher request throughput
D) Increase the S3 request rate limit by submitting a service quota increase request to AWS Support

**Your answer: B** — Correct. S3 supports 3,500 PUT/s per prefix. Distributing across hash prefixes multiplies available throughput.

---

### Q6 ✓ — EFS vs EBS for Shared Filesystem (efs)
**Question:** A company runs a containerized application across 50 Amazon Elastic Compute Cloud (EC2) instances in 3 Availability Zones (AZs). All instances need shared, concurrent read/write access to the same filesystem with POSIX permissions. The data must survive the loss of any single Availability Zone (AZ). Which storage solution meets these requirements?

A) Amazon Elastic Block Store (EBS) with Multi-Attach enabled on an io2 volume, mounted to all 50 instances
B) Amazon Elastic File System (EFS) with Standard storage class configured for Multi-AZ deployment
C) Amazon Simple Storage Service (S3) mounted via S3 File Gateway on each Elastic Compute Cloud (EC2) instance
D) Amazon FSx for Lustre linked to an S3 bucket for shared high-performance access

**Your answer: B** — Correct. EFS Standard provides managed NFS across multiple AZs, concurrent access from thousands of instances, POSIX permissions, and Multi-AZ durability.

---

### Q7 ✓ — S3 Encryption with Audit and Revocation (s3-encryption)
**Question:** A company wants to encrypt objects in Simple Storage Service (S3) with full control over key rotation schedules, the ability to audit every encryption/decryption request, and the option to immediately revoke access to encrypted data by disabling the key. Which TWO encryption approaches satisfy ALL three requirements? (Select TWO)

A) Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3) with automatic rotation enabled
B) Server-Side Encryption with AWS Key Management Service-Managed Keys (SSE-KMS) using a customer managed key
C) Server-Side Encryption with Customer-Provided Keys (SSE-C) with the company managing keys in an on-premises Hardware Security Module (HSM)
D) Client-Side Encryption using AWS Key Management Service (KMS) envelope encryption with a customer managed key

**Your answer: B, D** — Correct. Both use KMS customer managed keys providing: rotation control, CloudTrail audit of every API call, and key disable/revocation capability.

---

### Q8 ✗ — KMS Throttling with SSE-KMS (s3-encryption)
**Question:** A company uses Server-Side Encryption with AWS Key Management Service (SSE-KMS) for all objects in their Simple Storage Service (S3) bucket. During a product launch, the application starts receiving 40,000 GET requests per second and users report intermittent errors. CloudWatch metrics show an increase in Key Management Service (KMS) ThrottlingException errors. What is the most operationally efficient solution?

A) Switch to Server-Side Encryption with S3-Managed Keys (SSE-S3) to eliminate Key Management Service (KMS) dependency entirely
B) Request a Key Management Service (KMS) quota increase for the GenerateDataKey and Decrypt API calls in the affected Region
C) Enable S3 Bucket Keys to reduce the number of Key Management Service (KMS) API calls by caching a bucket-level data key
D) Distribute objects across multiple buckets, each with a separate Key Management Service (KMS) key, to spread the KMS API load

**Your answer: B** — Incorrect. Correct answer: C. S3 Bucket Keys reduce KMS API calls by ~99% by caching a bucket-level data key. One setting toggle, instant effect, no support ticket wait time.

---

### Q9 ✓ — CRR Existing Object Replication (s3-replication)
**Question:** A company enables Cross-Region Replication (CRR) on an existing Simple Storage Service (S3) bucket containing 500,000 objects. After enabling CRR, only new uploads appear in the destination bucket. How should the solutions architect replicate the existing 500,000 objects?

A) Delete and re-upload all existing objects to trigger the replication rule on the new uploads
B) Use S3 Batch Replication to create a one-time job that replicates all existing objects to the destination bucket
C) Disable and re-enable Cross-Region Replication (CRR) to force a full synchronization of all objects including existing ones
D) Use the AWS Command Line Interface (CLI) aws s3 sync command to copy existing objects to the destination bucket, then rely on CRR for new objects

**Your answer: B** — Correct. S3 Batch Replication is purpose-built for replicating existing objects, failed replications, and objects from older rules.

---

### Q10 ✓ — Storage Gateway Types (storage-gateway)
**Question:** A company needs to provide on-premises applications with low-latency access to frequently used files while storing the complete dataset in Simple Storage Service (S3). The on-premises servers use the Network File System (NFS) protocol. Additionally, they need a separate solution to archive legacy backup tapes to AWS without changing their existing tape-based backup workflows. Which TWO AWS Storage Gateway configurations meet these requirements? (Select TWO)

A) S3 File Gateway configured with NFS mount points for the file access requirement
B) Volume Gateway in Cached mode for file access, with snapshots stored in S3
C) Tape Gateway configured as a Virtual Tape Library (VTL) for the tape backup requirement
D) FSx File Gateway to provide low-latency access to Amazon FSx for Windows File Server

**Your answer: A, C** — Correct. S3 File Gateway provides NFS access with local cache backed by S3. Tape Gateway presents as a VTL for existing tape workflows, storing virtual tapes in S3/Glacier.

---

## Summary
- **Score:** 9/10 (90%)
- **Missed topics:** s3-encryption (S3 Bucket Keys)
- **Strong areas:** s3-lifecycle, ebs-types, s3-security, snow-family, s3-performance, efs, s3-replication, storage-gateway
- **Key lessons:**
  - When SSE-KMS causes ThrottlingException, the first solution is S3 Bucket Keys (reduces KMS API calls by ~99%). Quota increases are a fallback, not primary fix.
