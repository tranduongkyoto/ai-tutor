# Storage - AWS CSA Content Cache

## Services & Concepts

**Amazon EC2 Instance Storage**
- Attached directly to EC2 instances; ephemeral (lost when instance stops/terminates)
- High I/O performance compared to network-based storage
- Use cases: buffers, caches, scratch data, temporary content
- Backup and replication are customer responsibility
- Cannot be used as boot volume across instance types

**Amazon EBS (Elastic Block Store)**
- Network drive (not physical) attached to running EC2 instances
- Can be detached and reattached quickly to different instances
- Locked to specific Availability Zone; cannot move across AZs without snapshot
- Supports encryption (SSE-S3 default, SSE-KMS, SSE-C options)
- Max object size: 50TB; requires multi-part upload for files >5GB
- Charged for provisioned capacity (GB + IOPS)
- Can be increased in size over time

**EBS Snapshots**
- Point-in-time backups of EBS volumes
- Can copy across AZs and regions
- EBS Snapshot Archive: 75% cheaper, 24-72 hour restore time
- Fast Snapshot Restore (FSR): Full initialization, no latency on first use (additional cost)
- Recycle Bin: Retain deleted snapshots 1 day to 1 year for recovery

**Amazon EFS (Elastic File System)**
- Managed NFS (Network File System) for EC2 instances
- Works across multiple AZs in a region
- Scales automatically, pay-per-use (no capacity planning)
- Compatible with Linux only (POSIX); uses NFSv4.1 protocol
- Encryption at rest with KMS
- Use cases: content management, web serving, data sharing, WordPress
- 3x cost of gp2 EBS
- Performance modes: General Purpose (default), Max I/O
- Throughput modes: Bursting, Provisioned, Elastic
- Storage tiers: Standard, Infrequent Access (IA), Archive
- Availability: Standard (Multi-AZ) or One Zone (single AZ, 90% cost savings)

**Amazon S3 (Simple Storage Service)**
- Object storage service with infinitely scalable capacity
- Buckets created at region level; globally unique names
- Stores objects (files) with keys (full paths)
- Max object size: 50TB; multi-part upload for >5GB
- Objects have metadata, tags (up to 10), version IDs
- Highly durable (99.999999999% across multiple AZs)
- Default encryption: SSE-S3 enabled for all new buckets

**S3 Storage Classes**
- **S3 Standard**: 99.99% availability, frequently accessed, low latency
- **S3 Standard-IA**: 99.9% availability, infrequent access, retrieval fees, 30-day minimum
- **S3 One Zone-IA**: 99.5% availability, single AZ, data lost if AZ destroyed, 30-day minimum
- **S3 Glacier Instant Retrieval**: Millisecond retrieval, 90-day minimum, retrieval fees
- **S3 Glacier Flexible Retrieval**: Expedited (1-5 min), Standard (3-5 hrs), Bulk (5-12 hrs, free), 90-day minimum
- **S3 Glacier Deep Archive**: Standard (12 hrs), Bulk (48 hrs), 180-day minimum, lowest cost
- **S3 Intelligent-Tiering**: Auto-moves objects between tiers based on access; no retrieval charges
  - Frequent (0-30 days), Infrequent (30-90 days), Archive Instant (90+ days)
  - Optional: Archive Access (90-700+ days), Deep Archive (180-700+ days)
- **S3 Express One Zone**: Single AZ, 100,000s requests/sec, single-digit millisecond latency, 99.95% availability, 10x better than Standard (50% lower costs)

**S3 Security & Access Control**
- User-based: IAM Policies
- Resource-based: Bucket Policies, Object ACL, Bucket ACL
- Access allowed if IAM permissions ALLOW OR bucket policy ALLOWS, AND no explicit DENY
- Block Public Access settings prevent accidental data exposure (can be set account-wide)

**S3 Versioning**
- Enabled at bucket level; creates version IDs for overwrites
- Protects against unintended deletes; can restore old versions
- Suspending versioning doesn't delete previous versions
- Non-versioned files have version "null"

**S3 Replication**
- Cross-Region Replication (CRR) or Same-Region Replication (SRR)
- Requires versioning on both buckets
- Asynchronous copying; IAM permissions required
- Use cases: CRR (compliance, lower latency, cross-account), SRR (log aggregation, test replication)
- Only new objects replicated after enabling
- S3 Batch Replication: Replicate existing objects and failed replications
- No chaining: Bucket1→Bucket2→Bucket3 doesn't replicate Bucket1 objects to Bucket3

**S3 Lifecycle Rules**
- Transition Actions: Move objects to different storage classes (e.g., Standard→IA after 60 days, →Glacier after 6 months)
- Expiration Actions: Delete objects after specified time (e.g., delete logs after 365 days)
- Can apply to object prefixes or tags
- Delete old versions of files (if versioning enabled) or incomplete multi-part uploads

**S3 Performance**
- 3,500 PUT/COPY/POST/DELETE requests per second per prefix baseline
- 5,500 GET/HEAD requests per second per prefix baseline
- Unlimited number of prefixes; distribute load across prefixes for higher throughput
- Multi-Part Upload: Recommended >100MB, mandatory >5GB; parallelizes uploads
- S3 Transfer Acceleration: Upload to edge locations, forward to S3 in target region via private AWS network
- S3 Byte-Range Fetches: Parallelize GETs, better resilience, retrieve only partial data

**S3 Event Notifications**
- Events: ObjectCreated, ObjectRemoved, ObjectRestore, Replication
- Destinations: SNS, SQS, Lambda
- Object name filtering (e.g., *.jpg)
- Event delivery typically in seconds but can take longer
- S3 EventBridge: Advanced filtering, 18+ AWS service destinations, archive, replay

**S3 Analytics**
- Storage Class Analysis: Helps decide when to transition objects to different classes
- Works with Standard/Standard-IA, NOT One Zone-IA or Glacier
- Report updated daily; 24-48 hours to see initial data
- Good first step for lifecycle rules

**S3 Storage Lens**
- Understand, analyze, optimize storage across entire AWS Organization
- 30 days of usage & activity metrics
- Aggregates by organization, accounts, regions, buckets, prefixes
- Free metrics (28 usage metrics, 14-day retention) or Advanced metrics (additional metrics, 15-month retention)
- Default dashboard or custom dashboards
- Export metrics daily to S3 (CSV, Parquet)

**S3 Batch Operations**
- Perform bulk operations on existing objects: modify metadata, copy, encrypt, modify ACLs/tags, restore from Glacier, invoke Lambda
- Manages retries, tracks progress, sends notifications
- Use S3 Inventory + Athena to generate filtered object lists

**S3 Requester Pays**
- Requester (not bucket owner) pays for request and data download costs
- Useful for sharing large datasets
- Requester must be authenticated in AWS (cannot be anonymous)

**S3 Access Points**
- Simplify security management for S3 buckets
- Each access point has DNS name (Internet or VPC origin) and access point policy
- VPC Origin: EC2 instances access only through VPC Endpoint (Gateway or Interface)
- VPC Endpoint Policy required to allow access

**S3 Object Lambda**
- Lambda functions transform objects before retrieval
- One S3 bucket with supporting Access Point + Object Lambda Access Points
- Use cases: Redact PII, convert formats (XML→JSON), resize/watermark images on-the-fly

**S3 Static Website Hosting**
- S3 buckets can host static websites
- URLs: `http://bucket-name.s3-website-aws-region.amazonaws.com` or `http://bucket-name.s3-website.aws-region.amazonaws.com`
- Must enable public access; 403 Forbidden if bucket policy doesn't allow public reads

**S3 CORS (Cross-Origin Resource Sharing)**
- Mechanism to allow cross-origin requests from web browsers
- Origin = scheme (protocol) + host (domain) + port
- Browser sends preflight OPTIONS request; server responds with Access-Control-Allow-Origin headers
- Popular exam question; configure at target bucket

**Amazon AMI (Amazon Machine Image)**
- Customization of EC2 instances: software, OS, monitoring, configuration
- Region-specific; can copy across regions
- Launch EC2 from: Public AMI (AWS), Custom AMI, AWS Marketplace AMI
- Process: Start EC2 → Customize → Stop instance → Build AMI (creates EBS snapshots) → Launch from AMI

---

## Key Configurations

**EBS Volume Types**
- **gp2 (General Purpose SSD)**: 1-16 TiB, 3 IOPS/GiB (max 16,000), burst capable, boot volume capable
- **gp3 (General Purpose SSD)**: 1-16 TiB, baseline 3,000 IOPS + 125 MiB/s, scale IOPS/throughput independently up to 16,000 IOPS & 1,000 MiB/s, boot volume capable
- **io1 (Provisioned IOPS SSD)**: 4-16 TiB, 64,000 IOPS (Nitro) / 32,000 (other), boot volume capable
- **io2 Block Express (Provisioned IOPS SSD)**: 4-64 TiB, up to 256,000 IOPS, 1,000:1 IOPS:GiB ratio, sub-millisecond latency, Multi-Attach support, boot volume capable
- **st1 (Throughput Optimized HDD)**: 125-16 TiB, 500 MiB/s throughput, 500 IOPS, NOT boot volume capable
- **sc1 (Cold HDD)**: 125-16 TiB, 250 MiB/s throughput, 250 IOPS, NOT boot volume capable

**EBS Delete on Termination**
- Root volume: Enabled by default (deleted when EC2 terminates)
- Other volumes: Disabled by default (retained after EC2 terminates)
- Configurable via AWS Console or CLI

**S3 Bucket Naming Rules**
- Globally unique across all AWS accounts and regions
- No uppercase, no underscores
- Not an IP address
- Must start with lowercase letter or number
- Must NOT start with prefix `xn--`
- Must NOT end with suffix `-s3alias`

**S3 Encryption Methods**
- **SSE-S3**: AWS-managed keys, AES-256, default encryption for all new buckets, header `x-amz-server-side-encryption: AES256`
- **SSE-KMS**: KMS-managed keys, user control + CloudTrail audit, header `x-amz-server-side-encryption: aws:kms`, subject to KMS quota limits (5,500-30,000 req/s)
- **SSE-C**: Customer-provided keys, HTTPS mandatory, customer manages key lifecycle, header required on every request
- **Client-Side Encryption**: Client encrypts before upload, manages keys entirely

**S3 Encryption in Transit (SSL/TLS)**
- HTTP endpoint: Non-encrypted
- HTTPS endpoint: Encrypted in flight
- HTTPS recommended and mandatory for SSE-C
- Force encryption via bucket policy using `aws:SecureTransport` condition

**S3 Default Encryption vs. Bucket Policies**
- Default Encryption: SSE-S3 automatically applied to new objects
- Bucket Policies can force specific encryption (SSE-KMS or SSE-C)
- Bucket Policies evaluated before Default Encryption

**S3 Versioning & MFA Delete**
- MFA Delete requires versioning enabled
- MFA required to: permanently delete object version, suspend versioning
- MFA NOT required to: enable versioning, list deleted versions
- Only root account can enable/disable MFA Delete

---

## Architectural Patterns

**EBS vs. EFS vs. Instance Store**
- **EBS**: Single instance, AZ-locked, detachable, persistent, moderate cost, network latency
- **EFS**: Multiple instances across AZs, shared filesystem, NFS protocol, 3x EBS cost, auto-scaling
- **Instance Store**: Single instance, highest performance, ephemeral, temporary data only

**S3 Versioning for Disaster Recovery**
- Enable versioning + lifecycle rules
- Scenario: Recover deleted objects within 30 days (keep standard), then move to IA/Glacier for 365 days
- Use S3 Batch Replication with S3 Inventory for initial existing-object sync

**S3 Multi-Region Failover**
- CRR to secondary region bucket
- Delete marker replication: Optional (can replicate deletion tombstones)
- Deletions with version ID: Never replicated (prevents malicious cascading deletes)
- Applications must switch S3 bucket endpoint on primary failure

**Large File Transfers to S3**
- Multi-Part Upload: Divide files, parallel uploads, resume failed parts
- S3 Transfer Acceleration: Geographic distribution for users far from region
- Byte-Range Fetches on download: Parallelize retrievals, resilience

**S3 & EC2 Integration**
- EC2 Instance Role (IAM role): EC2 accesses S3 via temporary credentials
- S3 Access Points: Simplify access management per team/application
- VPC Endpoint (Gateway): EC2→S3 without internet gateway; VPC Endpoint Policy controls access

**Data Governance Across Organization**
- S3 Storage Lens: Monitor usage, costs, compliance across accounts
- Lifecycle Policies: Auto-transition and expire objects per retention requirements
- Bucket Policies + Access Points: Enforce encryption, versioning, public access blocks account-wide

---

## Important Numbers & Limits

| Metric | Value |
|--------|-------|
| **EBS** |
| Max volume size | 16 TiB (all types except io2 Block Express) |
| Max io2 Block Express volume size | 64 TiB |
| Max IOPS (gp2) | 16,000 |
| Max IOPS (gp3) | 16,000 (independent of size) |
| Max IOPS (io1) | 64,000 (Nitro) / 32,000 (other) |
| Max IOPS (io2 Block Express) | 256,000 |
| EBS Multi-Attach (io1/io2) | Up to 16 instances per volume (same AZ only) |
| **EFS** |
| Scale | Petabyte-scale, auto-grows |
| Concurrent NFS clients | 1000s |
| Throughput | 10 GB/s baseline |
| Elastic throughput (Provisioned) | Up to 3 GiB/s reads, 1 GiB/s writes |
| **S3** |
| Max object size | 50 TB |
| Multi-part upload minimum | 5 GB (recommended >100 MB) |
| Max object parts | 10,000 |
| Baseline requests (per prefix) | 3,500 PUT/POST/DELETE, 5,500 GET/HEAD (req/sec) |
| S3 Durability | 99.999999999% (11 nines) |
| S3 Standard Availability | 99.99% |
| S3 Standard-IA Availability | 99.9% |
| S3 One Zone-IA Availability | 99.5% |
| S3 Glacier Instant Retrieval | Millisecond |
| S3 Glacier Flexible (Expedited) | 1-5 minutes |
| S3 Glacier Flexible (Standard) | 3-5 hours |
| S3 Glacier Flexible (Bulk) | 5-12 hours |
| S3 Glacier Deep Archive (Standard) | 12 hours |
| S3 Glacier Deep Archive (Bulk) | 48 hours |
| S3 Express One Zone | Single-digit millisecond latency, 100,000s req/sec |
| S3 Pre-signed URL (Console) | 1 min to 720 min (12 hours) |
| S3 Pre-signed URL (CLI default) | 3600 seconds (max 604,800 = 168 hours) |
| Standard IA minimum storage | 30 days |
| Standard IA minimum billable object | 128 KB |
| Glacier Instant minimum storage | 90 days |
| Glacier Flexible minimum storage | 90 days |
| Glacier Deep Archive minimum storage | 180 days |
| **S3 Storage Classes Comparison** |
| Standard cost/GB | ~$0.023 |
| Standard-IA cost/GB | ~$0.0125 |
| One Zone-IA cost/GB | ~$0.01 |
| Glacier Instant cost/GB | ~$0.004 |
| Glacier Flexible cost/GB | ~$0.0036 |
| Glacier Deep Archive cost/GB | ~$0.00099 |
| Intelligent-Tiering cost/GB | $0.0025-$0.023 (variable) |

---

## Diagram Descriptions

**EBS Snapshot Flow**
- Source EBS volume in us-east-1a
- Snapshot backup step
- Snapshot restored to EBS volume in us-east-1b
- Demonstrates cross-AZ migration capability

**EFS Multi-AZ Architecture**
- EC2 instances in us-east-1a, us-east-1b, us-east-1c
- Single EFS filesystem spans all AZs with mount targets
- Security group controls access
- All instances share same filesystem with NFSv4.1

**S3 Bucket Structure**
- Bucket contains objects (no actual directory structure, just keys with "/" delimiters)
- Objects have metadata, tags, version IDs
- Key structure: `s3://bucket/prefix/object-name`

**S3 Versioning Lifecycle**
- Object uploaded as Version 1
- Object overwritten creating Version 2
- Object overwritten creating Version 3
- Can restore any previous version
- Delete marker hides current version but retains all historical versions

**S3 Replication (CRR)**
- Source bucket in eu-west-1
- Destination bucket in us-east-2
- Asynchronous replication arrow
- Versioning required on both
- IAM permissions required

**EBS vs. EFS Comparison (Architectural)**
- EBS: One instance, single AZ, fast network access
- EFS: Multiple instances across AZs, shared NFS access, higher cost

---

## Exam-Relevant Details

**EBS Key Distinctions**
- **EBS vs. Instance Store**: EBS persists, Instance Store ephemeral; EBS network-attached, Instance Store physically local
- **gp2 vs. gp3**: gp3 allows independent IOPS/throughput scaling; gp2 IOPS tied to volume size
- **io1/io2 vs. gp3**: When mission-critical databases need sustained IOPS >16,000 or consistent predictability
- **Multi-Attach (io1/io2)**: Only in same AZ; requires cluster-aware filesystem; maximum 16 instances

**EFS Traps**
- EFS only works with Linux/POSIX; NOT Windows
- EFS 3x cost of gp2; expensive for simple workloads
- EFS One Zone ≠ highly available; single AZ failure = data loss
- Lifecycle policies move to IA but still incur retrieval costs on access

**S3 Storage Class Decisions**
- Standard: Default for frequent access
- Standard-IA: Infrequent but rapid access (>30 day minimum penalizes short-term)
- One Zone-IA: Recreatable data (backups); AZ failure = total loss
- Glacier Instant: Quarterly access pattern (90-day minimum)
- Glacier Flexible: Rare archival (expect days to retrieve)
- Glacier Deep Archive: Compliance/legal hold (lowest cost, longest waits)
- Intelligent-Tiering: Unknown access patterns; pays for management

**S3 Security Traps**
- Bucket Policy vs. IAM: Bucket Policy is evaluated first; must ALLOW at either level AND no explicit DENY
- Public Access Blocks: Default blocks all public access; must explicitly disable to allow public buckets
- Default Encryption: SSE-S3 enabled by default; bucket policy can require stronger encryption (SSE-KMS)
- CORS: Configure at bucket receiving cross-origin requests (target bucket), not source

**S3 Performance Traps**
- Prefix hot spots: High load on single prefix (e.g., `2024/01/01/...`) = throttled; distribute across prefixes
- Multi-part uploads: Required >5GB; improves throughput via parallelization
- S3 Transfer Acceleration: Worth cost only for global users far from region; latency benefit ~2x
- Byte-Range Fetches: Not automatic; application must implement to parallelize large downloads

**S3 Versioning & Replication Traps**
- Replication: Only NEW objects replicated; existing objects require S3 Batch Replication
- Deletions: Delete markers replicated (optional), but version IDs never deleted to prevent cascading deletes
- No Chaining: A→B→C replication doesn't replicate A objects to C
- MFA Delete: Only root account can enable/disable; requires MFA device for permanent version deletion

**S3 Lifecycle Rules Traps**
- Minimum storage periods: 30-day, 90-day, or 180-day minimums; shorter holding periods incur full storage + retrieval costs
- Expired vs. Archived: Expiration deletes permanently; Lifecycle moves to cheaper class (still charges per GiB retrieved)
- Versioning interaction: Lifecycle rules apply to current AND non-current versions separately

**S3 Encryption Traps**
- SSE-C: HTTPS mandatory; key not stored by AWS; client manages key rotation
- SSE-KMS: Scales to 5,500-30,000 requests/sec; bursting workloads may hit quota and need request increase
- Encrypt unencrypted objects: No in-place encryption; must copy via S3 Batch Operations or CloudFront
- Default Encryption: Does NOT encrypt existing objects; only new uploads

**S3 & VPC Integration Traps**
- VPC Endpoint (Gateway): Only for S3 and DynamoDB; cheaper but less fine-grained than Interface Endpoints
- Access Points with VPC Origin: Requires VPC Endpoint; VPC Endpoint Policy MUST allow both bucket and access point ARNs
- S3 Object Lambda: Intercepts requests; adds compute overhead (Lambda invocation latency)

**S3 Replication Decision Tree**
- Same region, log aggregation, < 1 hour RPO → SRR
- Different region, compliance requirement, < 15 min RPO → CRR
- Different region, cross-account data sharing → CRR with bucket policy + IAM roles
