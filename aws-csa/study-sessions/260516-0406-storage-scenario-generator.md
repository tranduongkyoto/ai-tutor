# Storage — Scenario Generator (Phase 3)
**Date:** 2026-05-16 04:06
**Scenarios:** 12 (full scenario map coverage)

---

## Scenario 1: gp3 vs io2 vs st1 Selection (ebs-types)

**Context:** A mid-size e-commerce company runs their product catalog database (PostgreSQL) on EC2. The database handles ~8,000 read IOPS and ~4,000 write IOPS during peak holiday sales. They also run a separate analytics workload that sequentially scans 10 TB of log data nightly.

**Requirements:** Database needs consistent low-latency IOPS. Analytics needs high sequential throughput at lowest cost.

**Question:** Which EBS volume types should the solutions architect recommend for each workload?

A) gp3 for the database (scale to 12,000 IOPS), st1 for the analytics logs
B) io2 for the database (provision 12,000 IOPS), gp3 for the analytics logs
C) gp3 for both workloads with independent IOPS and throughput scaling
D) io2 Block Express for the database, sc1 for the analytics logs

**Answer: A**
gp3 supports up to 16,000 IOPS with independent scaling — 12,000 IOPS easily covers the peak. st1 provides 500 MiB/s at lowest cost per GB for sequential reads.

**Why others are wrong:**
- B) io2 at 12,000 IOPS costs significantly more than gp3 for same performance — io2 only justified above 16K IOPS.
- C) gp3 for analytics wastes money — SSD unnecessary for sequential scanning. st1 costs ~50% less per GB.
- D) io2 Block Express is extreme overkill for 12K IOPS. sc1 is for cold/infrequent data, not nightly batch.

**Key Concept:** Match EBS type to workload pattern — gp3 for general IOPS, st1 for throughput-heavy sequential, io2 only when >16K IOPS needed.

---

## Scenario 2: Provisioned IOPS Sizing (ebs-types)

**Context:** A healthcare SaaS company runs Oracle on EC2 Nitro. EHR system requires 80,000 sustained IOPS with sub-millisecond latency. Database is 12 TiB, grows ~500 GB/quarter.

**Requirements:** 80,000 sustained IOPS, sub-ms latency, room to grow beyond 16 TiB.

**Question:** Which EBS configuration meets these requirements?

A) Two io1 volumes in RAID 0 striped configuration
B) Single io2 Block Express volume, 16 TiB, 80,000 provisioned IOPS
C) Single io1 volume with 80,000 provisioned IOPS on Nitro
D) gp3 scaled to 16,000 IOPS with application-level read caching

**Answer: B**
io2 Block Express: up to 256,000 IOPS, 64 TiB, sub-ms latency. Only single-volume option for 80K IOPS.

**Why others are wrong:**
- A) RAID 0 adds complexity, doesn't guarantee sub-ms, doubles snapshot management.
- C) io1 on Nitro maxes at 64,000 IOPS — insufficient.
- D) gp3 maxes at 16,000 IOPS — caching doesn't help sustained write IOPS.

**Key Concept:** io2 Block Express required when IOPS >64K or volume >16 TiB.

---

## Scenario 3: Cross-Region Copy and Lifecycle (ebs-snapshots)

**Context:** Financial services company takes daily EBS snapshots (30 volumes, ~500 GB each). Compliance: 90-day retention in primary, 1-year in DR. Costs growing 15%/month.

**Requirements:** Reduce costs 50%+, 90-day primary availability, 1-year DR, automated.

**Question:** Which approach minimizes costs while meeting compliance?

A) Snapshot Archive for primary >90 days, copy all to DR on day 1
B) Copy to DR immediately, delete primary after 90d, archive DR after 90d
C) Keep 90d primary standard, copy to DR day 1, archive DR after 90d, delete primary after 90d
D) DLM cross-region copy on creation, archive primary after 7d, retain DR standard 1 year

**Answer: C**
Primary: 90-day standard (fast restore). DR: copy day 1, archive after 90 days (75% savings for 9 months). Delete primary at 90 days.

**Why others are wrong:**
- A) Archiving primary means 24-72hr restore for trading platform — unacceptable.
- B) Doesn't specify DR archiving clearly.
- D) Archiving primary after 7 days = most restores require 24-72hr wait.

**Key Concept:** Combine DLM + cross-region copy + Snapshot Archive for cost-optimized retention.

---

## Scenario 4: EFS vs EBS vs FSx Decision (efs)

**Context:** Game studio with 200 Linux build servers compiling assets. Each build reads 50 GB shared source, writes 10 GB output. Builds run in parallel. Target: under 20 minutes.

**Requirements:** Shared read for 200 instances, high throughput, Linux, minimize build time.

**Question:** Which storage solution best meets these requirements?

A) EFS with Provisioned Throughput at 3 GiB/s
B) FSx for Lustre linked to S3 source assets
C) EBS io2 replicated via rsync
D) S3 with parallel byte-range fetches

**Answer: B**
FSx for Lustre: purpose-built for HPC/parallel, hundreds of GB/s, POSIX, S3 integration for lazy-loading source.

**Why others are wrong:**
- A) EFS maxes at 3 GiB/s — may be insufficient for 200 concurrent builders.
- C) rsync 50 GB × 200 instances = 10 TB copying before builds start.
- D) S3 not POSIX, adds per-request latency, poor for random file access.

**Key Concept:** FSx for Lustre = HPC, parallel workloads, S3-linked. Keywords: "build servers", "HPC", "parallel" → Lustre.

---

## Scenario 5: S3 Standard vs IA vs Glacier Selection (s3-classes)

**Context:** Legal firm: active cases (20%) accessed daily, closed cases (50%) accessed 2-3x/year, archived (30%) once per 5 years, 12-hour retrieval SLA.

**Requirements:** Minimize cost. Active: instant. Closed: occasional, minutes OK. Archived: 12hr SLA, lowest cost.

**Question:** Most cost-effective configuration?

A) S3 Standard for all with lifecycle based on access date
B) Standard for active, Standard-IA for closed, Glacier Deep Archive for archived
C) Intelligent-Tiering for all with Archive Access enabled
D) Standard for active, Glacier Instant for closed, Glacier Flexible for archived

**Answer: B**
Standard (daily), Standard-IA (2-3x/year, instant retrieval), Deep Archive (12hr retrieval meets SLA, cheapest).

**Why others are wrong:**
- A) No optimization — 80% of data stored at highest cost.
- C) Monitoring fee on known patterns is wasteful.
- D) Glacier Instant overkill for 2-3x/year. Glacier Flexible more expensive than Deep Archive.

**Key Concept:** Known patterns → explicit lifecycle. Deep Archive cheapest when 12hr retrieval acceptable.

---

## Scenario 6: S3 Intelligent-Tiering (s3-classes)

**Context:** Data science platform, 500+ partners, unpredictable access patterns changing quarterly. Currently $180K/month in S3 Standard.

**Requirements:** Reduce costs, no latency impact for active data, no operational overhead.

**Question:** Best approach to reduce costs?

A) S3 Analytics for 30 days then manual lifecycle rules
B) Intelligent-Tiering with Frequent, Infrequent, and Archive Instant tiers
C) Move all to Standard-IA immediately
D) Per-partner lifecycle rules based on history

**Answer: B**
Intelligent-Tiering auto-tiers based on access. No retrieval fees for main tiers. Zero operational overhead. Ideal for unpredictable, changing patterns.

**Why others are wrong:**
- A) 500+ partners with quarterly changes → lifecycle rules become stale immediately.
- C) Retrieval fees penalize frequently-accessed data. 30-day minimum charges.
- D) 500+ configurations unmanageable, especially with quarterly changes.

**Key Concept:** Intelligent-Tiering ideal when patterns unpredictable and change over time.

---

## Scenario 7: Transition Rules and Expiration (s3-lifecycle)

**Context:** SaaS logs 200 GB/day. 7-day hot debug, 8-30d warm, 31-90d cold (minutes retrieval), auto-delete at 90d.

**Requirements:** Match lifecycle to access tiers, auto-expiry for compliance.

**Question:** Which lifecycle configuration at minimum cost?

A) Standard (7d) → Standard-IA (8d) → Glacier Instant (31d) → Expire (90d)
B) Standard (7d) → One Zone-IA (8d) → Glacier Flexible (31d) → Expire (90d)
C) Standard (30d) → Glacier Instant (31d) → Expire (90d)
D) Intelligent-Tiering with expiration at 90d

**Answer: A**
Standard for hot 7d. Standard-IA from day 8 (instant access, cheaper). Glacier Instant from day 31 (millisecond retrieval for security investigations). Expire at 90d.

**Why others are wrong:**
- B) One Zone-IA risks data loss. Glacier Flexible needs Expedited ($) for minutes.
- C) Standard for 30 days wastes money days 8-30.
- D) Per-object monitoring on 200 GB/day of logs is expensive for known patterns.

**Key Concept:** Chain transitions matching patterns. Respect minimum storage periods.

---

## Scenario 8: Bucket Policy vs ACL vs IAM (s3-security)

**Context:** Media company S3 bucket: EC2 via IAM role, external CDN partner (cross-account), public read for thumbnails/ prefix only.

**Requirements:** IAM for EC2, cross-account CDN, public thumbnails/, everything else private.

**Question:** Correct access control combination?

A) IAM role for EC2, bucket policy for CDN + public thumbnails/*, Block Public Access OFF
B) IAM role for EC2, Object ACLs public-read on thumbnails, bucket policy for CDN, BPA ON
C) Single bucket policy combining all three, BPA OFF
D) IAM role for EC2, Access Point for CDN (VPC origin), pre-signed URLs for thumbnails

**Answer: A**
IAM role (user-based) for EC2. Bucket policy (resource-based) for cross-account CDN + public prefix. BPA must be OFF to allow public statement.

**Why others are wrong:**
- B) BPA ON blocks public access — overrides ACLs.
- C) IAM role access doesn't need bucket policy — handled by IAM policy on the role.
- D) VPC origin Access Points don't work for external CDN. Pre-signed URLs add operational complexity for static thumbnails.

**Key Concept:** Bucket Policy = cross-account + public. IAM = same-account. BPA must be OFF for any public access.

---

## Scenario 9: SSE-S3 vs SSE-KMS (s3-security)

**Context:** Government contractor: 90-day key rotation, decrypt audit trail, key-based access revocation, separation of duties.

**Requirements:** All four security controls must be met.

**Question:** Which encryption approach meets all requirements?

A) SSE-S3 with S3 access logging
B) SSE-KMS with Customer Managed Key (CMK) + CloudTrail
C) SSE-C with application-managed rotation
D) Client-side encryption with CloudHSM

**Answer: B**
SSE-KMS + CMK: auto rotation, CloudTrail audit, disable CMK to revoke all access, IAM separation between S3 admins and KMS admins.

**Why others are wrong:**
- A) SSE-S3: no customer key control, no rotation control, no per-object decrypt audit.
- C) SSE-C: no CloudTrail integration, manual everything, HTTPS mandatory.
- D) CloudHSM overkill when SSE-KMS meets all requirements natively.

**Key Concept:** "audit" + "rotation" + "revoke" + "separation of duties" → SSE-KMS with CMK.

---

## Scenario 10: FSx for Lustre vs FSx for Windows vs EFS (fsx)

**Context:** Three workloads: (1) Video rendering 100 Linux instances, (2) Corporate file share 500 Windows + AD, (3) Web app 20 Linux instances sharing configs.

**Requirements:** Each workload needs optimized shared storage for its OS and pattern.

**Question:** Which storage for each?

A) FSx Lustre for rendering, FSx Windows for corporate, EFS for web app
B) EFS for all three with different throughput modes
C) FSx Lustre for rendering, EFS with SMB for corporate, EFS for web app
D) FSx Windows for rendering and corporate, EFS for web app

**Answer: A**
Lustre: HPC parallel Linux. FSx Windows: SMB + AD. EFS: Linux NFS general-purpose.

**Why others are wrong:**
- B) EFS is Linux/NFS only — can't serve Windows/SMB.
- C) EFS doesn't support SMB natively.
- D) FSx Windows (SMB) can't efficiently serve Linux HPC workloads.

**Key Concept:** Lustre = Linux HPC. FSx Windows = Windows + AD + SMB. EFS = Linux NFS general.

---

## Scenario 11: Snowcone vs Snowball vs Snowmobile (snow-family)

**Context:** Three locations: (1) Remote station no internet, 8 TB, (2) Regional office 1 Gbps, 60 TB, 1-week window, (3) HQ 5 PB, 6-month window.

**Requirements:** Most appropriate device per location.

**Question:** Which Snow Family device for each?

A) Snowcone for station, Snowball Edge for office, Snowmobile for HQ
B) Snowball Edge for all three
C) Snowcone for station, Transfer Acceleration for office, Snowmobile for HQ
D) Snowcone for station, Snowball Edge for office, multiple Snowball Edge for HQ

**Answer: A**
Snowcone (8-14 TB, portable, offline). Snowball Edge (80 TB, 1-week ship). Snowmobile (100 PB, petabyte-scale).

**Why others are wrong:**
- B) 63+ Snowball Edge for 5 PB — logistically complex.
- C) Transfer Acceleration doesn't increase bandwidth pipe — 60 TB over 1 Gbps is tight.
- D) Multiple Snowballs for 5 PB is viable but operationally complex vs Snowmobile.

**Key Concept:** Snowcone <14 TB. Snowball Edge 10-80 TB. Snowmobile for petabytes.

---

## Scenario 12: File vs Volume vs Tape Gateway (storage-gateway)

**Context:** Manufacturing hybrid cloud: (1) NFS from Linux factory to S3 with caching, (2) iSCSI block for ERP with DR snapshots, (3) Veritas NetBackup integration for tape archival.

**Requirements:** File/NFS→S3, block/iSCSI+DR, tape software compatibility.

**Question:** Which Storage Gateway for each?

A) S3 File Gateway for sensors, Volume Gateway (stored) for ERP, Tape Gateway for backups
B) S3 File Gateway for sensors, Volume Gateway (cached) for ERP, Tape Gateway for backups
C) FSx File Gateway for sensors, Volume Gateway (cached) for ERP, S3 File Gateway for backups
D) S3 File Gateway for all three with different lifecycle policies

**Answer: B**
S3 File Gateway: NFS→S3 with local cache. Volume Gateway cached: iSCSI, hot data local, full volume in S3, EBS snapshots for DR. Tape Gateway: VTL compatible with NetBackup, archives to Glacier.

**Why others are wrong:**
- A) Stored mode keeps ALL data on-premises — cached mode better for DR (primary in cloud).
- C) FSx File Gateway is for Windows/SMB, not Linux/NFS. S3 File Gateway can't emulate tapes.
- D) S3 File Gateway can't provide iSCSI or tape library emulation.

**Key Concept:** File Gateway = NFS/SMB→S3. Volume Gateway = iSCSI→S3+EBS. Tape Gateway = VTL→Glacier. "Existing backup software" = Tape Gateway.
