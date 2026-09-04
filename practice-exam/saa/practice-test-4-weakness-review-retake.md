# Practice Test #4 — Weakness Review (Retake)
**Date:** 2026-08-07
**Score:** 50/65 (77%) — PASS (improved from 62%)
**Wrong:** 15 questions (4 repeat misses + 11 new misses)

---

## Repeat Misses (Priority — pattern not learned)

### 1. Warm Standby vs Pilot Light
**Q5** — Wrong: B (Pilot Light) → Correct: A (Warm Standby)
- **Warm Standby** = scaled-down but **fully functional** environment always running
- **Pilot Light** = only **core components** running (DB, minimal infra) — NOT fully functional
- **Trigger phrase:** "scaled-down version of a fully functional environment" → always Warm Standby
- **Memory aid:** Warm = warm enough to work; Pilot = just a tiny flame keeping the pilot light on

### 2. Geoproximity Routing
**Q27** — Wrong: B (Weighted) → Correct: D (Geoproximity)
- **Trigger phrase:** "dynamically alter the SIZE of a geographic AREA" → Geoproximity with bias
- Geoproximity uses **bias values** (-99 to +99) to expand/shrink routing area
- Geolocation = fixed by country/continent (can't resize)
- Weighted = percentage-based distribution, no geography
- **Memory aid:** Geo-PROXIMITY = how CLOSE (area size); Geo-LOCATION = WHERE (fixed borders)

### 3. EventBridge for SaaS Integration
**Q32** — Wrong: C (SQS) → Correct: D (EventBridge)
- **Trigger phrase:** "SaaS application" + "third-party" → EventBridge
- EventBridge has **native SaaS partner integrations** (Zendesk, Datadog, Auth0, etc.)
- SQS is point-to-point, no SaaS connectors
- SNS can fan-out but also no native SaaS integration
- **Memory aid:** EventBridge = event BUS for everything (AWS + SaaS + custom)

### 4. Transit Gateway as Central Hub
**Q42** — Wrong: A (VPC peering) → Correct: C (Transit Gateway)
- **Trigger phrase:** "central hub" + "least operational overhead" → Transit Gateway
- TGW = managed hub-and-spoke, connects VPCs + on-prem through one gateway
- VPC peering = point-to-point, NO transitive routing, N² connections at scale
- Transit VPC = self-managed EC2 appliances (high operational overhead)
- **Memory aid:** "Hub" in the question = Transit Gateway. Period.

---

## New Misses — By Concept

### Data-in-Transit vs Authentication
**Q52** — Wrong: A (IAM auth) → Correct: B (SSL)
- **Data-in-transit** = encryption of network traffic → **SSL/TLS**
- **IAM authentication** = WHO can connect → authentication, not encryption
- These are separate concerns: IAM auth + SSL together = secure auth + encrypted data
- **Rule:** "data-in-transit security" → always SSL/TLS

### DynamoDB Capacity Modes
**Q53** — Wrong: B (Provisioned + auto-scaling) → Correct: D (On-demand)
- **Unpredictable** + **very quick spikes** → On-demand (instant scaling)
- Provisioned + auto-scaling takes **minutes** to react — too slow for sudden spikes
- On-demand = zero capacity during idle hours (pay per request)
- **Rule:** "unpredictable" + "quick/sudden" → On-demand; "predictable" + "steady" → Provisioned

### DAX vs ElastiCache for DynamoDB
**Q57** — Wrong: B (ElastiCache) → Correct: A (DAX)
- **"Without a lot of application refactoring"** → DAX (API-compatible, just change endpoint)
- ElastiCache requires writing caching logic in application code
- DAX is DynamoDB-native, transparently caches hot reads
- **Rule:** DynamoDB hot partition + minimal changes → DAX; general caching needs → ElastiCache

### Kinesis Analytics vs Athena
**Q11** — Wrong: B (Athena) → Correct: A (Kinesis Data Analytics)
- **Real-time** analytics → Kinesis Data Analytics (SQL on streaming data)
- Athena = **batch** query service on S3 data (not real-time)
- Pipeline: Streams (capture) → Analytics (real-time query) → Firehose (persist)
- **Rule:** "real-time" + "streaming" → Kinesis Analytics; "ad-hoc query on S3" → Athena

### S3 Object Lock Modes
**Q20** — Wrong: D (Governance for both) → Correct: B (Compliance + Glacier Vault Lock)
- **Compliance mode** = truly immutable, NO ONE can delete (not even root)
- **Governance mode** = can be overridden by users with `s3:BypassGovernanceRetention`
- **Glacier Vault Lock** = vault-level immutability for archival data
- Match: immediate access + immutable → Object Lock Compliance; archival + immutable → Glacier Vault Lock
- **Rule:** regulatory/compliance → Compliance mode; "governance" is the WEAKER option

### S3 Bucket Policy Reading
**Q21** — Wrong: B → Correct: C
- `IpAddress` + `NotIpAddress` in same condition = allow CIDR **except** specific IP
- The bucket doesn't "expose" IPs — it controls access based on source IP
- **Rule:** read S3 policies literally: Condition keys filter who can access

### EFS Throughput Modes
**Q25** — Wrong: D (One Zone) → Correct: B (General Purpose + Standard + burst)
- **Burst throughput** = accumulates credits during low usage, spends during bursts
- Requires **General Purpose** performance mode + **Standard** storage class
- IA storage class adds first-access latency (bad for burst workloads)
- One Zone reduces availability, doesn't change throughput behavior
- **Rule:** sporadic bursts + low average → burst mode (default); consistent high → provisioned

### Golden AMI Pattern
**Q28** — Wrong: D,B → Correct: A,D
- **Golden AMI** = pre-bake static components (the 45-min install)
- **User Data** = customize dynamic parts at boot (seconds)
- "Beanstalk deployment caching" does NOT exist
- **Rule:** slow install → Golden AMI for static + User Data for dynamic

### NLB Static IPs
**Q35** — Wrong: D (Dynamic EIPs) → Correct: A (NLB + ASG)
- NLB provides **static IP per AZ** → easy to whitelist
- ALB/CLB have dynamic IPs that change
- Dynamic EIP attachment to ASG instances is not a standard pattern
- **Rule:** "whitelist IP" + load balancer → NLB (static IPs)

### Lambda Best Practices
**Q58** — Wrong: C,D,F → Correct: B,C,D
- **Lambda Layers** (B) = reuse code across functions ✓
- **VPC + NAT** (C) = VPC-enabled Lambda needs NAT for internet ✓
- **CW Alarms on ConcurrentExecutions** (D) = catch runaway scaling ✓
- Lambda DOES support container images up to 10 GB (A is false)
- F is misleading — Layers organize code but don't specifically reduce cold starts

### RDS Cross-Region Multi-AZ
**Q60** — Wrong: C (cross-region Multi-AZ) → Correct: B (same-region Multi-AZ)
- **Cross-region Multi-AZ does NOT exist** for RDS
- Multi-AZ = same region, automatic failover
- Cross-region = read replicas only (manual promotion, not automatic)
- **Rule:** "max HA + min overhead" for RDS → same-region Multi-AZ deployment

### DynamoDB Deletion Protection vs PITR
**Q64** — Wrong: D (PITR) → Correct: C (Deletion protection)
- **Deletion protection** = PREVENTS table deletion (proactive)
- **PITR** = RECOVERS data after loss (reactive) — doesn't prevent deletion
- Question asks to "prevent future data loss from human error" → prevention, not recovery
- **Rule:** "prevent deletion" → deletion protection; "recover data" → PITR/backups

---

## Study Priority (by frequency of concept confusion)

| Priority | Concept | Times Missed | Action |
|----------|---------|-------------|--------|
| 1 | Warm Standby vs Pilot Light | 2x | Memorize: "fully functional" = Warm Standby |
| 2 | Geoproximity vs Geolocation | 2x | Memorize: "alter area size" = Geoproximity bias |
| 3 | EventBridge for SaaS | 2x | Memorize: SaaS/third-party = EventBridge |
| 4 | Transit Gateway as hub | 2x | Memorize: "central hub" = TGW |
| 5 | DynamoDB patterns (DAX/on-demand/deletion) | 3 Qs | Review DynamoDB decision tree |
| 6 | SSL vs IAM auth | 1x | Separate encryption vs authentication |
| 7 | S3 immutability (Compliance/Governance/Vault Lock) | 1x | Review Object Lock modes |
| 8 | EFS throughput modes | 1x | Review burst vs provisioned |
