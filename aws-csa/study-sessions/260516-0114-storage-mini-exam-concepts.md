# Storage — Mini Exam: Concepts (Phase 2)
**Date:** 2026-05-16 01:14
**Score:** 8/10 (80%)
**Scope:** concepts — test conceptual knowledge from concept-mapper

---

## Questions & Results

### Q1 ✓ — Instance Store for HPC scratch data (instance-store)
**Question:** A company needs to run a high-performance computing (HPC) workload on Amazon EC2 instances that requires temporary scratch storage with the lowest possible latency. The data does not need to persist after the computation completes. Which storage option provides the highest I/O performance for this use case?

A) Amazon Elastic Block Store (EBS) io2 Block Express volume with 256,000 provisioned IOPS
B) Amazon Elastic File System (EFS) with Provisioned Throughput mode set to maximum
C) EC2 Instance Store volumes physically attached to the host machine
D) Amazon Simple Storage Service (S3) Express One Zone with single-digit millisecond latency

**Your answer: C** — Correct. Instance Store provides highest I/O as physically attached disk with no network overhead. Ideal for temporary/scratch data.

---

### Q2 ✗ — Tape Gateway for tape migration (storage-gateway)
**Question:** An organization wants to migrate their on-premises backup tapes to AWS while maintaining the same backup software and workflows. The archived data must be stored at the lowest possible cost for long-term compliance retention. Which AWS Storage Gateway type and S3 storage class should they use?

A) S3 File Gateway storing backups in Simple Storage Service (S3) Glacier Deep Archive
B) Volume Gateway in cached mode with Elastic Block Store (EBS) snapshots in S3 Standard-IA
C) Tape Gateway with virtual tapes archived to Simple Storage Service (S3) Glacier Deep Archive
D) FSx File Gateway connected to FSx for Lustre with lifecycle rules to Glacier Flexible Retrieval

**Your answer: A** — Incorrect. Correct answer: C. Tape Gateway emulates Virtual Tape Library (VTL) so existing tape backup software works unchanged. S3 File Gateway presents NFS/SMB — would require changing backup workflows.

---

### Q3 ✓ — EBS volume type specifications (ebs-types)
**Question:** Which two statements about Amazon Elastic Block Store (EBS) volume types are correct? (Select TWO)

A) gp3 volumes provide a baseline of 3,000 IOPS and 125 MiB/s throughput regardless of volume size
B) st1 (Throughput Optimized HDD) volumes can be used as boot volumes for cost-effective EC2 instances
C) io2 Block Express volumes support up to 256,000 IOPS and a maximum size of 64 TiB
D) gp2 volumes provide 3 IOPS per GiB with a burst capability, maximum 16,000 IOPS at 5,334 GiB or larger

**Your answer: A, C** — Correct. gp3 has fixed 3,000 IOPS/125 MiB/s baseline independent of size. io2 Block Express goes to 256K IOPS and 64 TiB. st1/sc1 cannot be boot volumes.

---

### Q4 ✗ — EBS Multi-Attach io1/io2 only (ebs-multi-attach)
**Question:** A solutions architect needs to enable multiple EC2 instances in the same Availability Zone (AZ) to simultaneously read and write to the same Elastic Block Store (EBS) volume for a clustered database. Which EBS volume type supports this capability?

A) gp3 (General Purpose SSD) with enhanced networking enabled on all instances
B) io1 or io2 (Provisioned IOPS SSD) with Multi-Attach enabled
C) st1 (Throughput Optimized HDD) with shared mount points configured
D) gp2 (General Purpose SSD) attached to multiple instances via Network File System (NFS)

**Your answer: D** — Incorrect. Correct answer: B. EBS Multi-Attach is only available on io1/io2 volumes, same AZ only, up to 16 instances. EBS is block storage — cannot be shared via NFS (that's EFS).

---

### Q5 ✓ — S3 Lifecycle rules for cost optimization (s3-lifecycle)
**Question:** A company stores log files in Simple Storage Service (S3) Standard. The logs are analyzed frequently during the first 30 days, rarely accessed between 30-90 days, and must be retained for 7 years for compliance. Which configuration minimizes storage costs while meeting these requirements?

A) S3 Intelligent-Tiering with optional Archive Access tier enabled after 90 days
B) S3 Lifecycle rule: Standard → Standard-IA after 30 days → Glacier Flexible Retrieval after 90 days → Glacier Deep Archive after 365 days
C) S3 Lifecycle rule: Standard → One Zone-IA after 30 days → Glacier Deep Archive after 90 days
D) Store all logs in S3 Glacier Instant Retrieval from day one with 7-year Object Lock retention

**Your answer: B** — Correct. Progressive lifecycle matches known access patterns better than Intelligent-Tiering (which charges monitoring fees). Standard-IA for 30-90d, Glacier Flexible for 90-365d, Deep Archive for 365d+ minimizes cost at each stage.

---

### Q6 ✓ — CRR only replicates new objects (s3-replication)
**Question:** A developer configures Simple Storage Service (S3) Cross-Region Replication (CRR) on a bucket that already contains 500,000 objects. After enabling CRR, they notice the existing objects are not appearing in the destination bucket. What explains this behavior and what is the solution?

A) CRR requires both buckets to have versioning enabled — enable versioning on the destination bucket to trigger replication
B) CRR only replicates objects uploaded AFTER replication is enabled — use S3 Batch Replication to copy existing objects
C) CRR has a 24-48 hour initial sync delay — wait for the replication queue to process all existing objects
D) CRR requires IAM permissions on the source bucket only — the destination bucket automatically accepts replicated objects

**Your answer: B** — Correct. Replication only applies to NEW objects. S3 Batch Replication handles existing objects and previously failed replications.

---

### Q7 ✓ — EFS characteristics (efs)
**Question:** Which statement about Amazon Elastic File System (EFS) is correct?

A) EFS supports both Windows and Linux instances via SMB and NFS protocols respectively
B) EFS One Zone storage class provides high availability across multiple Availability Zones at reduced cost
C) EFS automatically scales storage capacity and supports thousands of concurrent NFS client connections
D) EFS uses the ext4 filesystem and requires volume size to be provisioned in advance like EBS

**Your answer: C** — Correct. EFS auto-scales with no provisioning needed, supports thousands of concurrent NFS connections. Linux/POSIX only, not Windows.

---

### Q8 ✓ — SSE-KMS throttling (s3-security)
**Question:** A company uses Simple Storage Service (S3) with server-side encryption using AWS Key Management Service (SSE-KMS). During peak hours, their application receives throttling errors when uploading objects. What is the most likely cause?

A) The S3 bucket has exceeded its maximum request rate of 3,500 PUT requests per second per prefix
B) The KMS key has hit its API request quota (5,500-30,000 requests/second depending on region)
C) SSE-KMS encryption is incompatible with S3 Transfer Acceleration, causing upload failures
D) The IAM role attached to the application has exceeded its maximum concurrent session limit

**Your answer: B** — Correct. SSE-KMS requires KMS API call per S3 operation. KMS quota (5,500-30,000 req/s) becomes the bottleneck before S3's own limits during burst uploads.

---

### Q9 ✓ — Pre-signed URLs for temporary access (s3-security)
**Question:** A company wants to allow a third-party analytics partner to download specific datasets from their Simple Storage Service (S3) bucket without creating an IAM user for them. The access should expire after 24 hours. Which approach meets this requirement?

A) Create an S3 Access Point with a policy granting the partner's AWS account access for 24 hours
B) Generate an S3 Pre-signed URL for each dataset object with a 24-hour expiration time
C) Enable S3 Requester Pays and share the bucket name with the partner for anonymous access
D) Configure a bucket policy with a time-based condition allowing public read access for 24 hours

**Your answer: B** — Correct. Pre-signed URLs grant temporary access to specific objects without requiring AWS credentials. Expiration up to 7 days (CLI) or 12 hours (Console).

---

### Q10 ✓ — Snowball for large migration (snow-family)
**Question:** A company needs to transfer 80 TB of data from their on-premises data center to Amazon Simple Storage Service (S3). Their internet connection is 1 Gbps. They need the data in AWS within 2 weeks. Which transfer method is most appropriate?

A) Use S3 Transfer Acceleration with multi-part uploads over the existing 1 Gbps connection
B) Order an AWS Snowball Edge device, load the data locally, and ship it to AWS
C) Set up AWS Direct Connect (DX) with a 10 Gbps dedicated connection to accelerate the transfer
D) Use multiple parallel S3 PUT operations with byte-range uploads over the existing connection

**Your answer: B** — Correct. Snowball Edge (80 TB) ships in 5-7 days total. Direct Connect takes weeks/months to provision. 80 TB over 1 Gbps = 8+ days at max theoretical throughput.

---

## Summary
- **Score:** 8/10 (80%)
- **Missed topics:** storage-gateway, ebs-multi-attach
- **Strong areas:** instance-store, ebs-types, s3-lifecycle, s3-replication, efs, s3-security, snow-family
- **Key lessons:**
  - Tape Gateway emulates VTL for existing tape backup workflows — keyword "same backup software" = Tape Gateway
  - EBS Multi-Attach is ONLY available on io1/io2 (Provisioned IOPS). gp2/gp3 and HDD types do NOT support it. Requires cluster-aware filesystem.
