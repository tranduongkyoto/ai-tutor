# Storage — Mini Exam: Design (Phase 5)
**Date:** 2026-05-17 01:13
**Score:** 6/10 (60%)
**Scope:** design — architecture design decisions and trade-offs (30% medium, 70% hard)

---

## Questions & Results

### Q1 ✓ — Multi-requirement S3 security architecture (s3-security)
**Question:** Bank document system: SSE-KMS CMK (audit), Object Lock Compliance 5-year (immutable), CRR to DR region, deletions must NOT cascade. Which config?

A) SSE-KMS CMK + Object Lock Compliance + CRR (delete markers OFF)
B) SSE-C + Object Lock Governance + CRR (delete markers ON)
C) SSE-KMS CMK + MFA Delete + CRR (delete markers OFF)
D) SSE-S3 + Object Lock Compliance + SRR

**Your answer: A** — Correct. SSE-KMS CMK provides audit via CloudTrail. Compliance mode = immutable. CRR with delete markers disabled prevents cascading. Version ID deletes never replicate by design.

---

### Q2 ✗ — Kinesis Firehose inline format conversion (s3-performance)
**Question:** 2 TB/hour from 10K IoT devices, tiny JSON files, Athena timeouts, Glue crawlers timeout, $50K/month costs. Design optimal architecture.

A) Keep structure + Intelligent-Tiering + increase timeouts
B) Glue ETL compacts to daily Parquet, partition by date, lifecycle raw to Glacier
C) Kinesis Firehose → Parquet directly, partition by date/hour, lifecycle JSON to Glacier Instant
D) Keep structure + S3 Select + Glacier Deep Archive after 30d

**Your answer: B** — Incorrect. Correct: C. Kinesis Data Firehose converts JSON→Parquet at ingestion time, eliminating separate Glue ETL compute costs. Hourly partitions match hourly query pattern. B requires a separate ETL job with daily granularity (too coarse for hourly queries).

---

### Q3 ✓ — Oracle DR with RPO/RTO requirements (ebs-snapshots)
**Question:** Oracle on EC2, single AZ, daily snapshots. Need: RPO 15 min, RTO 5 min, survive full AZ failure. Minimum changes?

A) io2 BE Multi-Attach same AZ + 15-min snapshots
B) Oracle Data Guard cross-AZ + io2 + daily snapshots
C) EBS Multi-AZ replication + CloudWatch
D) Standby EC2 in 2nd AZ + Oracle Data Guard sync + failover script

**Your answer: D** — Correct. Data Guard sync replication to second AZ provides <15-min RPO. Automated failover script achieves <5-min RTO. Second AZ survives AZ failure. Multi-Attach is same-AZ only. EBS doesn't have native Multi-AZ replication.

---

### Q4 ✓ — Intelligent-Tiering for unpredictable hot/cold patterns (s3-classes)
**Question:** 500 TB video content, 10% hot/30% warm/60% cold, shifts weekly, don't know which files. Minimize cost.

A) Intelligent-Tiering for all 500 TB
B) Storage Lens + manual lifecycle to Glacier
C) Split by content type + per-bucket lifecycle
D) S3 Analytics 30 days then apply rules

**Your answer: A** — Correct. When specific hot/cold files are unpredictable and patterns change weekly, Intelligent-Tiering auto-tiers per-object based on actual access. Manual rules become stale immediately with weekly shifts.

---

### Q5 ✗ — Glacier Instant vs Standard-IA minimum periods (s3-lifecycle)
**Question:** 500 MB medical images, processed then accessed once/year for audit. EC2 in VPC accesses S3 over internet (latency + cost issue). Design access + storage architecture.

A) VPC Gateway Endpoint (free) + Standard → Glacier Instant after 7d
B) VPC Interface Endpoint + Standard → Standard-IA after 7d
C) VPC Gateway Endpoint (free) + Standard → Standard-IA after 7d
D) Transfer Acceleration + Standard → Glacier Deep Archive after 7d

**Your answer: A** — Incorrect. Correct: C. Glacier Instant has 90-day minimum storage charge (objects transition at day 7 but pay for 90 days). Standard-IA has only 30-day minimum and provides instant retrieval for annual audits. For once-per-year access, Standard-IA is more cost-effective than Glacier Instant when considering the minimum period penalty.

---

### Q6 ✓ — S3 prefix throttling with 5 exchanges (s3-performance)
**Question:** 50,000 PUT/s across 5 exchanges at `trades/{exchange}/...`. Intermittent throttling. Root cause and fix?

A) Account-level S3 quota exceeded
B) 10K PUT/s per exchange prefix > 3,500 baseline — add hash prefix to distribute
C) Date sub-prefix hot partition — add hourly partitions
D) SSE-KMS quota throttling

**Your answer: B** — Correct. 50K ÷ 5 exchanges = 10K PUT/s per prefix, 3x over the 3,500 baseline. Adding random hash prefix distributes across hundreds of prefixes.

---

### Q7 ✓ — Multi-region backup architecture (ebs-snapshots)
**Question:** EBS cross-region backups <1hr RPO, S3 survive 2 simultaneous region failures, fully automated, <$500/month for 10 TB EBS + 50 TB S3.

A) DLM hourly cross-region snapshots + S3 CRR to 2 regions
B) AWS Backup hourly + S3 CRR to 1 region + Versioning
C) Lambda + EventBridge hourly + S3 CRR to 2 regions + Glacier
D) AWS Backup hourly + S3 CRR to 2 regions via Backup policies

**Your answer: A** — Correct. DLM (free, managed) for hourly cross-region EBS snapshots. S3 CRR to 2 additional regions = data in 3 regions, survives 2 failures. CRR to only 1 region = 2 total regions (can't survive 2 failures).

---

### Q8 ✓ — Instance Store for temporary intensive processing (instance-store)
**Question:** Temporary 10-50 GB files, intensive 2-4 hour processing, disposable, inconsistent EBS latency. Minimize latency + reduce cost.

A) io2 Block Express 100K IOPS per instance
B) Instance Store on i3/i3en storage-optimized instances
C) EFS Max I/O shared across 20 instances
D) S3 Express One Zone single-digit ms

**Your answer: B** — Correct. Instance Store = physically attached NVMe, lowest possible latency, no network hop. Perfect for disposable temporary data. Storage included in instance price (no separate EBS charge).

---

### Q9 ✗ — Bucket policy with VPC condition + cross-account exception (s3-security)
**Question:** S3 bucket must: (1) enforce SSE-KMS only, (2) restrict access to VPC only, (3) allow external auditor read on `audit-reports/` prefix. Configure access controls.

A) Bucket policy: deny non-KMS PUTs + VPC Endpoint condition on all statements + separate cross-account allow for auditor
B) Bucket policy: deny except VPC Endpoint + Access Point VPC origin + external IAM role
C) Default encryption + Security Group + cross-account IAM role
D) Bucket policy: deny non-KMS + VPC Endpoint Policy + Access Point internet origin for auditor

**Your answer: D** — Incorrect. Correct: A. The bucket policy uses VPC Endpoint condition (`aws:sourceVpce`) on EC2 access statements, but the auditor's allow statement is a SEPARATE statement without the VPC condition (since the auditor is external). D's internet-origin Access Point would be blocked by the VPC-only restriction. Security Groups don't apply to S3 (managed service).

---

### Q10 ✗ — Snowball Edge Compute for warehouse edge computing (snow-family)
**Question:** 10 warehouses, 100 GB/day each, need local processing + ML inference + daily S3 sync, limited internet, <$2,000/month per warehouse.

A) Snowcone per warehouse + DataSync
B) Snowball Edge Compute per warehouse + DataSync
C) AWS Outposts rack per warehouse
D) On-prem servers + IoT Greengrass + DataSync

**Your answer: A** — Incorrect. Correct: B. Snowcone only has 8-14 TB storage and 2 vCPUs — insufficient for 100 GB/day (fills in 80-140 days) and cannot run ML inference. Snowball Edge Compute has 80+ TB storage, 52+ vCPUs, and GPU options for ML. Outposts costs $200K+ (way over budget).

---

## Summary
- **Score:** 6/10 (60%)
- **Missed topics:** s3-performance, s3-lifecycle, s3-security, snow-family
- **Strong areas:** s3-security (multi-requirement), ebs-snapshots, s3-classes, s3-performance (prefix distribution), instance-store
- **Key lessons:**
  - Kinesis Data Firehose can convert JSON→Parquet inline at ingestion — eliminates separate Glue ETL jobs
  - Glacier Instant Retrieval has 90-day minimum storage; Standard-IA has 30-day. For short transitions, Standard-IA is cheaper despite higher per-GB cost
  - Bucket policy VPC conditions: add cross-account allow as SEPARATE statement without VPC condition to allow external access
  - Snowcone = 8-14 TB, 2 vCPU (lightweight edge). Snowball Edge = 80 TB, 52+ vCPU, GPU (heavy compute + ML inference)
