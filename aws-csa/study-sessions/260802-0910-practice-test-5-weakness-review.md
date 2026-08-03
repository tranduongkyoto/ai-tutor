# Practice Test 5 — Weakness Review

**Score:** 42/65 (65%) — BORDERLINE
**Date:** 2026-08-02
**Weakest → Strongest:** Resilient (47%) → High-Performing (62%) → Secure (68%) → Cost-Optimized (86%)

---

## Pattern 1: Confusing Similar AWS Features (8 errors)

These pairs look alike but serve different purposes. The exam tests whether you know the boundary.

### 1.1 Dedicated Hosts vs Dedicated Instances

| | Dedicated Instances | Dedicated Hosts |
|--|-------------------|-----------------|
| **Hardware** | Single-tenant | Single-tenant |
| **Host visibility** | No (no socket/core info) | Yes (socket, core, host ID) |
| **BYOL support** | No | Yes — server-bound licenses need host-level visibility |
| **Cost** | Lower | Higher (pay per physical host) |
| **Use when** | Compliance says "isolated hardware" | Compliance says "bring your own license" |

**Exam signal words:**
- "single-tenant" / "isolated" / "compliance" → **Dedicated Instances** (cheaper)
- "server-bound license" / "BYOL" / "socket-level" → **Dedicated Hosts**

**You got this wrong TWICE** (Q5: picked Hosts when Instances was cheaper; Q38: picked Instances when BYOL needed Hosts). Anchor the rule: **BYOL = Hosts. Isolation only = Instances.**

---

### 1.2 Client-Side Encryption vs SSE-C vs SSE-KMS vs SSE-S3

| | SSE-S3 | SSE-KMS | SSE-C | Client-Side |
|--|--------|---------|-------|-------------|
| **Who manages key?** | AWS | AWS KMS (you control) | You provide key | You manage everything |
| **Algorithm** | AES-256 (AWS) | AES-256 (AWS) | AES-256 (AWS) | **Your own algorithm** |
| **Key stored by AWS?** | Yes | Yes (in KMS) | No (you send per-request) | No |
| **Audit trail?** | No | Yes (CloudTrail) | No | No |

**Exam signal words:**
- "proprietary algorithm" / "custom encryption" → **Client-Side** (only option where YOU choose the algorithm)
- "own key" but standard algorithm → **SSE-C**
- "audit key usage" / "rotation" → **SSE-KMS**
- "simplest" / "default" → **SSE-S3**

**Your mistake (Q55):** Saw "proprietary algorithm," picked SSE-C. SSE-C lets you bring your own **key** but still uses AWS's AES-256 **algorithm**. Proprietary algorithm = must encrypt before upload = client-side.

---

### 1.3 SQS Delay Queue vs Visibility Timeout

```
                    DELAY QUEUE                          VISIBILITY TIMEOUT
                    ──────────                           ──────────────────
Producer → [message] → QUEUE                   Consumer polls → [message received]
                  ↓                                           ↓
           message INVISIBLE                           message INVISIBLE
           for delay period                            for timeout period
           (0-15 min)                                  (default 30s, max 12hr)
                  ↓                                           ↓
           message becomes                             if not deleted,
           VISIBLE to consumers                        message becomes VISIBLE
                                                       again (retry by another consumer)

AFFECTS: NEW messages entering queue        AFFECTS: messages AFTER a consumer receives them
PURPOSE: Postpone delivery                  PURPOSE: Prevent duplicate processing
```

**Exam signal words:**
- "postpone delivery of NEW messages" → **Delay Queue**
- "consumer needs more time to process" / "prevent re-delivery while processing" → **Visibility Timeout**

**Your mistake (Q8):** Question said "postpone delivery of NEW messages." That's delay queue by definition. Visibility timeout applies after a consumer already received the message.

---

### 1.4 ElastiCache: Redis vs Memcached

| | Redis | Memcached |
|--|-------|-----------|
| **Threading** | **Single-threaded** | **Multi-threaded** |
| **Data structures** | Strings, lists, sets, sorted sets, hashes, streams | Simple key-value only |
| **Persistence** | Yes (RDB snapshots, AOF) | No |
| **Replication** | Yes (read replicas, Multi-AZ) | No |
| **Pub/Sub** | Yes | No |
| **Lua scripting** | Yes | No |
| **Backup/restore** | Yes | No |

**Exam signal words:**
- "multi-threading" / "simplest caching" / "scale horizontally" → **Memcached**
- "persistence" / "pub/sub" / "sorted sets" / "complex data types" / "replication" / "HA" → **Redis**

**Your mistake (Q62):** Question explicitly said "supports multi-threading." That's the single strongest Memcached signal. Redis has more features but is single-threaded.

---

### 1.5 CloudFront: Signed URLs/Cookies vs HTTPS

| | Signed URLs / Signed Cookies | HTTPS (TLS) |
|--|------------------------------|-------------|
| **Purpose** | **Access control** — WHO can access | **Encryption** — HOW data travels |
| **Controls** | Expiration time, IP range, authorized user | Cipher suite, certificate, protocol version |
| **Use when** | "only subscribers" / "restrict access" / "bona fide users" | "secure communication" / "encrypt in transit" |

**Your mistake (Q27):** "distribute content only to subscribers" = access control = signed URLs/cookies. You picked HTTPS options which secure the connection but don't restrict who can access content.

---

### 1.6 SQS Priority: Two Queues + Consumer Logic

```
WRONG mental model:                    CORRECT mental model:
  Long polling = higher priority         Two separate queues
  Short polling = lower priority         Consumer polls PRO queue FIRST
                                         Only polls LITE queue when PRO is empty

  Polling type controls EFFICIENCY       CONSUMER LOGIC controls PRIORITY
  (fewer empty responses)                (which queue to check first)
```

**Your mistake (Q53):** Polling type (short vs long) only affects API efficiency and cost. It has zero impact on processing priority. Priority requires separate queues + application-level logic.

---

### 1.7 Read Replica Sizing for Analytics

**Wrong instinct:** "cost-optimal" → pick half capacity to save money.

**Correct reasoning:** Analytics queries are heavy (joins, aggregations, full scans). Half capacity = the replica becomes the new bottleneck → analytics still slow → defeats the purpose. Match primary capacity so analytics runs smoothly without impacting the primary.

**Rule:** "cost-optimal" means cheapest solution that **actually solves the problem**, not cheapest hardware.

---

## Pattern 2: Hard Constraint Facts (7 errors)

These are binary facts — you know them or you don't. No reasoning helps.

### 2.1 EBS Multi-Attach

```
✓ Supported:  io1, io2 (Provisioned IOPS SSD)
✗ NOT supported: gp2, gp3, st1, sc1

Additional constraints:
- Same AZ only (all attached instances must be in same AZ)
- Max 16 instances simultaneously
- Nitro-based instances only
- Must use cluster-aware file system (not ext4/xfs)
```

---

### 2.2 VPC DNS Settings for Private Hosted Zones

```
REAL settings (both required for Route 53 private hosted zones):
  ✓ enableDnsSupport     — enables Amazon DNS server in VPC (default: true)
  ✓ enableDnsHostnames   — assigns public DNS hostnames (default: false)

FAKE settings (don't exist — exam distractors):
  ✗ enableVpcHostnames
  ✗ enableDnsDomain
  ✗ enableVpcSupport
```

---

### 2.3 Instance Store and Hibernation

```
Instance Store data is LOST in ALL cases:
  ✗ Stop         → data lost
  ✗ Terminate    → data lost
  ✗ Hibernate    → data lost (only RAM → root EBS volume is saved)
  ✗ Hardware failure → data lost

Instance Store data SURVIVES:
  ✓ Reboot only
```

---

### 2.4 AWS Firewall Manager Scope

```
Firewall Manager CAN manage:
  ✓ AWS WAF (web ACL rules)
  ✓ AWS Shield Advanced (DDoS protection policies)
  ✓ VPC Security Groups (common SG policies)
  ✓ AWS Network Firewall (network-level filtering)
  ✓ Route 53 Resolver DNS Firewall

Firewall Manager CANNOT manage:
  ✗ Amazon Inspector (vulnerability scanning — not a firewall)
  ✗ Amazon GuardDuty (threat detection — not a firewall)
  ✗ VPC Route Tables (networking config — not a firewall)
  ✗ NACLs (not managed by Firewall Manager)
```

---

### 2.5 Direct Connect Virtual Interface Types

```
┌─────────────────────────────────────────────────────────┐
│                    DIRECT CONNECT                       │
├──────────────┬──────────────────────────────────────────┤
│ Public VIF   │ Access AWS PUBLIC services (S3, DynamoDB │
│              │ public endpoints, EC2 API, etc.)         │
│              │ Uses public IP addresses                 │
│              │ Traffic stays on DX link (not internet)  │
│              │ → "S3 from on-prem via DX" = Public VIF  │
├──────────────┼──────────────────────────────────────────┤
│ Private VIF  │ Access resources INSIDE a VPC            │
│              │ Uses private IP addresses                │
│              │ Connects to VGW or DX Gateway            │
│              │ → "EC2 in VPC from on-prem" = Private VIF│
├──────────────┼──────────────────────────────────────────┤
│ Transit VIF  │ Access resources via Transit Gateway     │
│              │ Uses private IP addresses                │
│              │ Connects to DX Gateway → TGW             │
│              │ → "multiple VPCs from on-prem" = Transit │
└──────────────┴──────────────────────────────────────────┘
```

**Key insight:** S3 is a PUBLIC service. Even though traffic stays on the DX connection (private wire), you still need a Public VIF to reach S3's public endpoints.

---

### 2.6 S3 Storage Lens

```
S3 Storage Lens capabilities:
  ✓ Organization-wide visibility (all regions, all accounts)
  ✓ Bucket-level metrics: versioning status, encryption, replication
  ✓ Usage analytics: request counts, bytes downloaded
  ✓ Advanced metrics: activity, cost optimization recommendations
  ✓ Dashboard — no custom code needed

When to use Storage Lens vs alternatives:
  "audit bucket configs across org"     → Storage Lens (no code)
  "detect API calls on buckets"         → CloudTrail
  "enforce bucket config compliance"    → AWS Config rules
  "analyze access patterns for tiering" → S3 Analytics
```

---

### 2.7 EC2 User Data Default Behavior

```
User data scripts:
  ✓ Run ONCE at first launch (default behavior)
  ✓ Run as root
  ✓ Run before instance is marked "running"

To run on EVERY boot (non-default):
  - Use multipart MIME with cloud-init
  - Or add script to /var/lib/cloud/scripts/per-boot/

Exam trap: Question says "run only once" → answer is plain user data (no config needed)
           Don't pick answers that add extra configuration for "run once" — it's the default
```

---

## Pattern 3: Missing the AWS Managed Service (5 errors)

**Rule of thumb:** When the question says "least operational overhead," "minimal manual intervention," or "managed" — eliminate any option that involves running/managing your own infrastructure.

### 3.1 Aurora Global Database (not DMS)

| Scenario | Wrong Choice | Right Choice |
|----------|-------------|--------------|
| Cross-region Aurora DR, RPO<5min, RTO<15min | DMS continuous replication + manual failover | Aurora Global Database + managed failover |

```
Aurora Global Database:
  - RPO: < 1 second (storage-level replication)
  - RTO: < 1 minute (managed failover)
  - Operational overhead: near zero
  - Setup: convert existing cluster to global

DMS:
  - RPO: depends on replication lag
  - RTO: manual promotion + DNS update
  - Operational overhead: manage DMS instance, monitor lag
  - Setup: provision DMS instance + configure tasks
```

**Signal:** "Aurora" + "cross-region" + "DR" + "minimal overhead" → Aurora Global Database. Always.

---

### 3.2 AWS Batch + Step Functions (not EKS self-managed)

| Scenario | Wrong Choice | Right Choice |
|----------|-------------|--------------|
| Batch image processing, auto-scale, no servers, workflow automation | EKS + self-managed EC2 nodes | AWS Batch + Step Functions |

```
AWS Batch: managed compute for batch jobs (auto-provisions EC2/Fargate)
Step Functions: managed workflow orchestration (sequencing, retries, state)
Combined: serverless batch processing pipeline

EKS self-managed: you manage nodes, scaling, patching, cluster upgrades
```

---

### 3.3 SQS Temporary Queues (not DLQ)

| Scenario | Wrong Choice | Right Choice |
|----------|-------------|--------------|
| High-throughput request-response pattern | Dead-letter queue | Temporary queue |

```
Temporary Queues: virtual queues for request-response, auto-delete, cheap
Dead-Letter Queues: catch failed messages after max retries
Delay Queues: postpone new message delivery
FIFO Queues: strict ordering + exactly-once processing
```

---

### 3.4 Athena (not smaller Redshift cluster)

| Scenario | Wrong Choice | Right Choice |
|----------|-------------|--------------|
| Rarely queried cold data, need SQL, minimize cost | Smaller Redshift cluster (24/7 cost) | Athena on S3 IA (pay-per-query) |

```
Query frequency vs service choice:
  Hot data (constant queries)    → Redshift (provisioned cluster)
  Warm data (daily/weekly)       → Redshift Serverless or Athena
  Cold data (rarely queried)     → Athena on S3 (pay only when queried)
```

---

### 3.5 MGN Workflow (not Auto Scaling)

```
AWS Application Migration Service (MGN) workflow:
  1. Install AWS Replication Agent on source VMs
  2. Continuous block-level replication to AWS
  3. Launch TEST instances → validate
  4. Launch CUTOVER instances → go live
  5. Decommission source

NOT part of MGN: Auto Scaling, manual AMI creation, CloudEndure (deprecated)
```

---

## Pattern 4: Misreading Question Requirements (3 errors)

### 4.1 AWS Alternate Contacts

**What you missed:** "Alternate contacts" is a specific AWS account feature — not a generic concept. Each account has slots for billing, security, and operations contacts. These receive service-specific notifications.

```
Root email       → account-level alerts, centralized mailbox
Alternate contacts:
  Billing        → cost/usage alerts → billing team distribution list
  Security       → security alerts   → security team distribution list
  Operations     → operational alerts → ops team distribution list
```

---

### 4.2 Monolith HA: ASG min=1 max=1 + EIP

**What you missed:** For a monolith that CANNOT run distributed:
- ASG min=1, max=1 = only ONE instance ever (monolith constraint)
- EIP + user-data = stable IP after failover
- Instance Role = needed to call EC2 API to attach EIP
- ALB = unnecessary cost for a single instance (EIP is the endpoint)

---

### 4.3 RDS Multi-AZ: 3 Key Facts

```
1. Standby is NOT readable    → "serve read requests" = WRONG
2. Replication is SYNCHRONOUS  → "asynchronously replicated" = WRONG
3. Backups from STANDBY        → "I/O suspended on primary" = WRONG
                                  (I/O is suspended on standby, not primary)
```

---

## Drill Checklist

Priority study items ranked by impact (errors × exam weight):

| # | Topic | Errors | Domain | Action |
|---|-------|--------|--------|--------|
| 1 | RDS Multi-AZ behavior | 2 | Resilient | Memorize 3 facts above |
| 2 | Dedicated Hosts vs Instances | 2 | Secure + Cost | BYOL=Hosts, Isolation=Instances |
| 3 | SQS queue types + patterns | 3 | Resilient + HP | Build comparison table: delay/visibility/DLQ/temporary/priority |
| 4 | EBS constraints | 1 | Resilient | Multi-Attach = io1/io2 only |
| 5 | Encryption types | 1 | Secure | Client-side = own algorithm, SSE-C = own key |
| 6 | DX VIF types | 1 | Secure | Public VIF = public services, Private VIF = VPC |
| 7 | Redis vs Memcached | 1 | Resilient | Multi-threaded = Memcached |
| 8 | Aurora Global Database | 1 | Resilient | Cross-region DR = Global DB always |
| 9 | CloudFront access control | 1 | Resilient | Signed URLs/cookies = WHO, HTTPS = HOW |
| 10 | Managed services instinct | 5 | All | "Least overhead" = eliminate self-managed options |
