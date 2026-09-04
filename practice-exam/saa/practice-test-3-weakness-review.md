# Practice Test #3 — Weakness Knowledge Review
**25 errors across 4 domains | Score: 39/64 (61%) | Target: 72%**

---

## DOMAIN 1: Design Secure Architectures — 8/19 wrong (58%)

### 1. IAM Instance Profiles
**Rule:** To assign an IAM role to an EC2 instance, you use an **instance profile**.
- Instance profile = container for the IAM role
- EC2 console creates instance profiles automatically
- Trust relationship allows the **EC2 service** (`ec2.amazonaws.com`), not the instance itself

**Trap:** "Add instance to trust policy" sounds right but is wrong. Trust policy trusts the service, not specific instances.

### 2. SCPs and Service-Linked Roles

**What SCPs are:** Permission boundaries at the AWS Organizations level. They define the **maximum permissions** for accounts. SCPs are **filters**, not grants — they limit what IAM policies can grant.

```
Effective permissions = IAM policy ∩ SCP
```

If IAM says "allow S3" but SCP doesn't include S3 → **denied**.

**Who SCPs affect:**

| Entity | Affected? | Why |
|--------|-----------|-----|
| IAM users in member accounts | **Yes** | SCPs cap their IAM permissions |
| IAM roles in member accounts | **Yes** | Same |
| **Root user of member accounts** | **Yes** | Root is NOT exempt in member accounts |
| Root user of **management account** | **No** | Management account always exempt |
| **Service-linked roles** | **No** | AWS services must always function |

**What are Service-Linked Roles (SLRs)?** Special IAM roles created **by an AWS service** (not by you) with predefined, locked permissions. Examples:

| Service | SLR | Purpose |
|---------|-----|---------|
| Auto Scaling | `AWSServiceRoleForAutoScaling` | Launch/terminate EC2 instances |
| ECS | `AWSServiceRoleForECS` | Manage ENIs, LB registration |
| ElastiCache | `AWSServiceRoleForElastiCache` | Create/manage cache resources |

**Why SCPs can't restrict SLRs:** If SCP blocks "deny ec2:RunInstances" and Auto Scaling's SLR tries to launch a replacement → it would break Auto Scaling → your app goes down. AWS prevents this by making SLRs immune.

**SLR vs Regular Role:**

| Feature | Regular IAM Role | Service-Linked Role |
|---------|-----------------|---------------------|
| Created by | You (admin) | **AWS service** automatically |
| Permissions | You define | **Predefined**, locked by AWS |
| Can you edit? | Yes | **No** |
| SCP applies? | **Yes** | **No** |
| Naming | Any name | Always `AWSServiceRoleFor<Service>` |

**Practical example:**
```
SCP on Account A: "Deny ec2:RunInstances"

- Admin user → launches EC2 → DENIED (SCP blocks)
- Root user → launches EC2 → DENIED (SCP blocks root too)
- Auto Scaling SLR → launches EC2 → ALLOWED (SCP doesn't apply to SLRs)
```

**Key rule:** IAM policy grants access + SCP denies → user **cannot** perform the action. SCP is the ceiling.

### 3. S3 Encryption — SSE-S3 Behavior
**SSE-S3 automatically generates a unique AES-256 key for EACH object.** Zero overhead, default encryption.
- SSE-KMS: uses KMS keys, supports encryption context, audit trail via CloudTrail
- SSE-C: customer provides the key with each request

### 4. VPC Sharing vs VPC Peering
| Feature | VPC Sharing (AWS RAM) | VPC Peering |
|---------|----------------------|-------------|
| What's shared | **Subnets** (not entire VPC) | Connectivity between 2 VPCs |
| Scope | Within AWS Organizations | Any 2 VPCs |
| Use case | Centrally managed VPC, departments launch into shared subnets | Connect separate VPCs |

### 5. FSx for ONTAP — Multi-Protocol
| Service | Protocol | OS Support |
|---------|----------|------------|
| FSx for Windows | **SMB** | Windows + Linux (via cifs) |
| FSx for ONTAP | **NFS + SMB** | Windows + Mac + Linux |
| FSx for Lustre | POSIX | Linux |
| FSx for OpenZFS | **NFS** | Linux + Mac |
| EFS | **NFS** | Linux only |

**Key:** Need both SMB + NFS → **FSx for ONTAP**. Need SMB + Windows ACLs + AD → **FSx for Windows**.

### 6. Shield Standard vs Shield Advanced
| Feature | Shield Standard | Shield Advanced |
|---------|----------------|-----------------|
| Cost | Free | $3,000/month |
| Protection | Basic DDoS (L3/4) | Enhanced DDoS (L3/4/7) |
| DRT access | No | **Yes** — DDoS Response Team |
| Logging | Basic | **Detailed** diagnostics |
| Architecture changes | None | **None** — applies to existing ALB |

**Key:** DDoS + minimal architecture changes + audit logging → **Shield Advanced** (not WAF+CloudFront which adds infra).

### 7. NAT Gateway Placement
**Rule:** NAT gateways MUST be in a **public subnet** with a route to an Internet Gateway.
- Private subnet route table → `0.0.0.0/0` → NAT gateway (in public subnet)
- NAT gateway needs an Elastic IP
- One per AZ for HA

**Trap:** It serves private subnets but **lives in** the public subnet.

### 8. Security Group Valid Sources
**Valid:** IP address, CIDR block, another security group, prefix list
**Invalid:** Internet Gateway ID, NAT Gateway ID, route table ID, subnet ID

---

## DOMAIN 2: Design High-Performing Architectures — 12/24 wrong (50%)

### 1. EFS Throughput Modes
| Mode | How it works | Best for |
|------|-------------|----------|
| **Bursting** | Throughput scales with storage size (50 MB/s per TB) | Large storage, variable I/O |
| **Provisioned** | Specify throughput **independent of storage** | **Small storage + high I/O** |
| **Elastic** | Auto-scales throughput, pay-per-use | Unpredictable workloads |

**Key:** <1 TB storage + high throughput → **Provisioned** (Bursting baseline too low at 50 MB/s).

### 2. AWS DataSync vs Transfer Family
| Service | Purpose |
|---------|---------|
| **DataSync** | Automate **bulk online transfers** to S3/EFS/FSx |
| **Transfer Family** | Managed **SFTP/FTP/FTPS** server |
| **Snowball** | **Offline** bulk transfer (physical device) |
| **File Gateway** | Ongoing **hybrid access** to S3 via NFS/SMB |

**Key:** "Automate and accelerate online transfers to S3/EFS/FSx" → **DataSync**.

### 3. NLB Routing — Instance ID Targets
**Rule:** Register by **instance ID** → NLB routes via **primary private IP** (always, even in public subnets).
Register by **IP address** → uses the specified IP.

### 4. S3 Transfer Acceleration vs CloudFront
| Feature | S3 Transfer Acceleration | CloudFront |
|---------|------------------------|------------|
| Optimized for | **Uploads** to S3 | **Downloads** from origin |
| How | Edge locations speed up uploads | Caches content at edges |

**Key:** "Upload large files globally" → **Transfer Acceleration**. "Serve content globally" → CloudFront.

### 5. ElastiCache Use Cases
**Good for:** read-heavy workloads, **compute-intensive** (cached leaderboard scores), session stores
**NOT good for:** write-heavy, complex JOINs, ETL

### 6. CloudFormation StackSets vs RAM
| Service | Purpose |
|---------|---------|
| **StackSets** | Deploy same template across **multiple accounts and regions** |
| **AWS RAM** | Share existing **resources** (subnets, Transit Gateways) |

**Key:** "Consistent provisioning" → StackSets. "Share resources" → RAM.

### 7. Lambda vs Fargate — Operational Overhead
| Criteria | Lambda | Fargate |
|----------|--------|---------|
| Infra management | **None** | Must build Docker image |
| Scaling | Automatic, instant | Configure Service Auto Scaling |
| Max runtime | 15 min | Unlimited |

**Key:** "Minimal operational overhead" + short tasks → **Lambda**.

### 8. Instance Tenancy Resolution
**Rule:** The **most restrictive** tenancy wins.

| Launch Template | VPC | Result |
|----------------|-----|--------|
| dedicated | default | **dedicated** |
| default | dedicated | **dedicated** |
| default | default | default |

### 9. API Gateway Types — JWT Authorization
| Type | Auth | Best for |
|------|------|----------|
| **HTTP API** | **Native JWT authorizer** (no code!) | OIDC/OAuth2, cheaper |
| **REST API** | Lambda authorizer, Cognito, IAM | Usage plans, API keys |
| **WebSocket API** | Lambda authorizer | Real-time bidirectional |

**Key:** "JWT validation without custom code" → **HTTP API**.

### 10. Global Accelerator vs CloudFront
| Feature | CloudFront | Global Accelerator |
|---------|------------|-------------------|
| Protocols | HTTP/HTTPS/WebSocket only | TCP + **UDP** |
| IPs | Dynamic edge IPs | **2 static anycast IPs** |
| Caching | Yes | No |

**Key:** **UDP**, **static IPs**, or **non-HTTP** → Global Accelerator. Multi-region ALBs + reduce firewall IPs → Global Accelerator.

### 11. AZ ID vs AZ Name
- **AZ Name** (`us-west-2a`): mapped **differently per account** — randomized
- **AZ ID** (`usw2-az1`): **consistent physical identifier** across all accounts

### 12. EC2 Recovery Behavior
After CloudWatch alarm-triggered recovery:
- **Retained:** instance ID, private IPs, Elastic IPs, **public IPv4**, all metadata
- **NOT retained:** in-memory data (instance reboots)
- **Requirement:** EBS-backed only
- **Cannot recover:** terminated instances

---

## DOMAIN 3: Design Resilient Architectures — 3/13 wrong (77%)

### 1. DynamoDB PITR vs On-Demand Backup
| Feature | PITR | On-Demand Backup |
|---------|------|------------------|
| Granularity | Any **second** in last 35 days | Only to backup creation time |
| Automatic | Yes, continuous | Manual trigger |

**Key:** "Remove corrupted data at the earliest" → **PITR** (pinpoint exact second).

### 2. EC2 Recovery Retains Public IPv4
Recovered instance keeps: instance ID, private IPs, Elastic IPs, **AND public IPv4**.
In-memory data is **NOT retained** (instance reboots).

### 3. SQS Standard → FIFO Migration
- **Cannot convert** in-place — must **delete and recreate**
- FIFO name must end with **`.fifo`**
- Throughput: without batching 300 msg/s, **with batching 3,000 msg/s**

---

## DOMAIN 4: Design Cost-Optimized Architectures — 2/8 wrong (75%)

### 1. AWS SCT vs Basic Schema Copy
| Tool | Handles |
|------|---------|
| **AWS SCT** | Complex: stored procedures, foreign keys, secondary indexes, views, triggers |
| **Basic Schema Copy** | Simple: tables, primary keys, basic columns only |
| **AWS DMS** | Migrates actual data (not schema) |

**Migration workflow:** SCT (convert complex schema) → DMS (migrate data).

### 2. Spot Instance Behavior
| Behavior | True/False |
|----------|-----------|
| Cancel request terminates instance | **FALSE** — must terminate separately |
| Persistent request reopens on **interruption** | **TRUE** |
| Persistent request reopens on **stop** | **FALSE** |
| Spot Fleet replaces terminated instances | **TRUE** — maintains target capacity |

---

## Topic-Based Cross-Reference (original categories)

## Category 1: Networking (8 errors)

### 1.1 NAT Gateway Placement
**Rule:** NAT gateways MUST be in a **public subnet** with a route to an Internet Gateway.
- Private subnet route table → `0.0.0.0/0` → NAT gateway (in public subnet)
- NAT gateway needs an Elastic IP to function
- One NAT gateway per AZ for high availability

**Trap:** Don't confuse "serves private subnet" with "placed in private subnet." It serves private subnets but lives in the public subnet.

### 1.2 NLB Routing — Instance ID Targets
**Rule:** When you register targets by **instance ID**, NLB routes using the **primary private IP** address.
- By instance ID → primary private IP (always)
- By IP address → whatever IP you specify
- Even in public subnets, NLB internally uses private IPs

### 1.3 Security Group Valid Sources
**Rule:** Security group inbound rules accept:
- IP address or CIDR block
- Another security group (same or peered VPC)
- Prefix list (for AWS services)

**Invalid:** Internet Gateway ID, NAT Gateway ID, route table ID — these are NOT valid sources.

### 1.4 Global Accelerator vs CloudFront
| Feature | CloudFront | Global Accelerator |
|---------|------------|-------------------|
| Protocols | HTTP/HTTPS/WebSocket only | TCP + **UDP** |
| Use case | Content delivery (CDN) | Non-HTTP apps, gaming, IoT, VoIP |
| IPs | Dynamic edge IPs | **2 static anycast IPs** |
| Caching | Yes (edge cache) | No caching, proxies traffic |
| Multi-region | Edge locations | Routes to nearest healthy endpoint |

**Key:** If the question mentions **UDP**, **static IPs**, or **non-HTTP** → Global Accelerator. If **content delivery** → CloudFront.

### 1.5 AZ ID vs AZ Name
- **AZ Name** (e.g., `us-west-2a`): mapped **differently per account** — randomized by AWS
- **AZ ID** (e.g., `usw2-az1`): **consistent physical identifier** across all accounts

**Rule:** To ensure same physical AZ across accounts → use **AZ ID**, not AZ name.

### 1.6 VPC Sharing vs VPC Peering
| Feature | VPC Sharing (AWS RAM) | VPC Peering |
|---------|----------------------|-------------|
| What's shared | **Subnets** (not entire VPC) | Connectivity between 2 VPCs |
| Scope | Within AWS Organizations | Any 2 VPCs (same or cross-account) |
| Use case | Centrally managed VPC, departments launch into shared subnets | Connect separate VPCs |
| Owner control | VPC owner retains full control | Both VPC owners manage their side |

**Key:** VPC sharing shares **subnets**, not the VPC itself.

### 1.7 S3 Transfer Acceleration vs CloudFront
| Feature | S3 Transfer Acceleration | CloudFront |
|---------|------------------------|------------|
| Optimized for | **Uploads** to S3 | **Downloads** from origin |
| How | Uses edge locations to speed uploads | Caches content at edge locations |
| Use case | Geographically dispersed users uploading large files | Serving static/dynamic content |

**Key:** "Upload large files globally" → Transfer Acceleration. "Serve content globally" → CloudFront.

### 1.8 Instance Tenancy Resolution
**Rule:** The **most restrictive** tenancy wins between Launch Template and VPC.

| Launch Template | VPC | Result |
|----------------|-----|--------|
| dedicated | default | **dedicated** |
| default | dedicated | **dedicated** |
| dedicated | dedicated | **dedicated** |
| default | default | **default** |

Only both being `default` results in default tenancy.

---

## Category 2: IAM & Security (5 errors)

### 2.1 IAM Instance Profiles
**Rule:** To assign an IAM role to an EC2 instance, you use an **instance profile**.
- Instance profile = container for the IAM role
- EC2 console creates instance profiles automatically
- Trust relationship allows the **EC2 service** (not the instance) to assume the role

**Wrong approach:** Adding instance to trust policy directly. The trust policy trusts `ec2.amazonaws.com` service, not specific instances.

### 2.2 SCPs and Service-Linked Roles
**SCPs affect:**
- All IAM users and roles in member accounts
- **Including** the root user of member accounts

**SCPs do NOT affect:**
- **Service-linked roles** — created by AWS services, permissions defined by the service
- Management account — SCPs never restrict the management account

**Key rule:** If IAM policy grants access but SCP denies → user **cannot** perform the action. SCP is the ceiling.

### 2.3 Shield Standard vs Shield Advanced
| Feature | Shield Standard | Shield Advanced |
|---------|----------------|-----------------|
| Cost | Free (automatic) | $3,000/month |
| Protection | Basic DDoS (Layer 3/4) | Enhanced DDoS (Layer 3/4/7) |
| DRT access | No | **Yes** — DDoS Response Team |
| Logging/reporting | Basic | **Detailed** attack diagnostics |
| Supported resources | All | ELB, CloudFront, Route 53, Global Accelerator, EC2 |
| Architecture changes | None | **None** — applies directly to existing ALB |

**Key:** When question asks for DDoS mitigation + minimal architecture changes + audit logging → **Shield Advanced**. WAF + CloudFront requires adding new infrastructure.

### 2.4 S3 Encryption — SSE-S3 Behavior
**SSE-S3 automatically generates a unique AES-256 key for EACH object.**
- No manual key management needed
- Each object encrypted with its own key
- That key is encrypted with a regularly rotated master key
- Zero overhead — it's the default encryption

**Don't confuse with:**
- SSE-KMS: uses KMS keys, supports encryption context, audit trail via CloudTrail
- SSE-C: customer provides the key with each request

### 2.5 Security Group Sources
Valid: IP, CIDR, security group, prefix list.
Invalid: IGW ID, VGW ID, NAT gateway ID, route table ID, subnet ID.

---

## Category 3: Storage & Data (5 errors)

### 3.1 FSx Family Comparison
| Service | Protocol | OS Support | Use Case |
|---------|----------|------------|----------|
| FSx for Windows | **SMB** | Windows + Linux (via cifs) | Windows workloads, AD integration, NTFS |
| FSx for ONTAP | **NFS + SMB** | Windows + Mac + Linux | Multi-protocol, auto-tiering |
| FSx for Lustre | POSIX | Linux | HPC, ML training |
| FSx for OpenZFS | **NFS** | Linux + Mac | Linux workloads |
| EFS | **NFS** | Linux only | Shared Linux storage |

**Key:** Need both SMB + NFS → **FSx for ONTAP**. Need SMB + Windows ACLs + AD → **FSx for Windows**.

### 3.2 EFS Throughput Modes
| Mode | How it works | Best for |
|------|-------------|----------|
| **Bursting** | Throughput scales with storage size (50 MB/s per TB baseline) | Large storage, variable I/O |
| **Provisioned** | Specify throughput **independent of storage** | Small storage + high I/O |
| **Elastic** | Auto-scales throughput, pay-per-use | Unpredictable workloads |

**Key:** Small storage (<1 TB) + high throughput needs → **Provisioned** (Bursting baseline would be too low).

### 3.3 DynamoDB Recovery Options
| Feature | PITR (Point-in-Time Recovery) | On-Demand Backup |
|---------|------------------------------|------------------|
| Granularity | Any **second** in last 35 days | Only to backup creation time |
| Automatic | Yes, continuous | Manual trigger |
| Use case | Restore to exact moment before corruption | Scheduled snapshots |

**Key:** "Remove corrupted data ASAP" → PITR (pinpoint exact second before corruption).

### 3.4 AWS SCT vs Basic Schema Copy
| Tool | Handles |
|------|---------|
| **AWS SCT** | Complex objects: stored procedures, foreign keys, secondary indexes, views, triggers |
| **Basic Schema Copy** | Simple schemas only: tables, primary keys, basic columns |
| **AWS DMS** | Migrates the actual data (not schema) |

**Migration workflow:** SCT (convert schema) → DMS (migrate data).

### 3.5 ElastiCache Use Cases
**Good for:**
- **Read-heavy** workloads (cache DB query results)
- **Compute-intensive** workloads (cache computed results like leaderboards)
- Session stores, real-time analytics

**NOT good for:**
- Write-heavy workloads (cache doesn't help writes)
- Complex SQL JOINs (not a relational DB)
- ETL processing (that's Glue/EMR)

---

## Category 4: Compute & Deployment (5 errors)

### 4.1 Lambda vs Fargate — Operational Overhead
| Criteria | Lambda | Fargate |
|----------|--------|---------|
| Infra management | **None** | Must build Docker image |
| Deployment | Upload code/zip | Build + push container image |
| Scaling | Automatic, instant | Service Auto Scaling (configure) |
| Max runtime | 15 minutes | Unlimited |
| Best for | Simple functions, event-driven | Long-running, complex apps |

**Key:** "Minimal operational overhead" + short tasks → **Lambda**. "Long-running" or "existing Docker" → **Fargate**.

### 4.2 CloudFormation StackSets vs RAM
| Service | Purpose |
|---------|---------|
| **StackSets** | Deploy same CloudFormation template across **multiple accounts and regions** |
| **AWS RAM** | Share existing **resources** (subnets, Transit Gateways) with other accounts |

**Key:** "Consistent provisioning across accounts/regions" → StackSets. "Share existing resources" → RAM.

### 4.3 API Gateway Types
| Type | Auth | Best for |
|------|------|----------|
| **HTTP API** | **Native JWT authorizer** (no code!) | REST APIs, OIDC/OAuth2, cheaper |
| **REST API** | Lambda authorizer, Cognito, IAM | Full features, usage plans, API keys |
| **WebSocket API** | Lambda authorizer | Real-time bidirectional (chat, gaming) |

**Key:** "JWT validation without custom code" → HTTP API with JWT authorizer. "Usage plans + API keys" → REST API.

### 4.4 Spot Instance Behavior
| Behavior | True/False |
|----------|-----------|
| Cancel request terminates instance | **FALSE** — must terminate separately |
| Persistent request reopens on **interruption** | **TRUE** |
| Persistent request reopens on **stop** | **FALSE** — only on interruption |
| Spot Fleet replaces terminated instances | **TRUE** — maintains target capacity |
| Terminated instances recoverable | **FALSE** |

### 4.5 SQS Standard → FIFO Migration
- **Cannot convert** in-place — must **delete and recreate**
- FIFO queue name must end with **`.fifo`**
- Throughput limits:
  - Without batching: 300 msg/s
  - **With batching: 3,000 msg/s**
  - High throughput mode: 30,000 msg/s (with batching: 90,000 msg/s)

---

## Category 5: Data Transfer & Migration (2 errors)

### 5.1 AWS DataSync vs Transfer Family
| Service | Purpose | Protocols |
|---------|---------|-----------|
| **DataSync** | Automate **bulk data transfers** between on-prem and AWS (S3, EFS, FSx) | Agent-based, network optimized |
| **Transfer Family** | Managed **SFTP/FTP/FTPS** server for file transfers | SFTP, FTP, FTPS, AS2 |
| **Snowball** | **Offline** bulk data transfer (ship physical device) | Physical device |
| **File Gateway** | Ongoing **hybrid access** to S3 via NFS/SMB | NFS, SMB |

**Key:** "Automate and accelerate online transfers to S3/EFS/FSx" → **DataSync**.

### 5.2 EC2 Recovery Behavior
After CloudWatch alarm-triggered recovery:
- **Retained:** instance ID, private IPs, Elastic IPs, **public IPv4**, all metadata
- **NOT retained:** in-memory data (instance reboots)
- **Requirement:** EBS-backed instances only (not instance store)
- **Cannot recover:** terminated instances

---

## Quick-Fire Flashcards by Domain

### Secure Architectures (8 errors)
1. EC2 → IAM role: use **instance profile**, not trust policy
2. SCPs: affect root user, do NOT affect **service-linked roles**
3. SSE-S3: auto-generates **unique key per object**
4. VPC sharing: shares **subnets**, not VPCs
5. FSx for ONTAP: **NFS + SMB** dual protocol
6. Shield Advanced: DDoS protection **on existing ALB**, no architecture change
7. NAT gateway: lives in **public subnet**
8. SG sources: no IGW ID — only IPs, CIDRs, SGs, prefix lists

### High-Performing Architectures (12 errors)
9. EFS Provisioned Throughput: for **small storage + high I/O**
10. DataSync: bulk online transfers to S3/EFS/FSx
11. NLB + instance ID targets: routes via **primary private IP**
12. S3 Transfer Acceleration: for **uploads**; CloudFront for downloads
13. ElastiCache: read-heavy + compute-intensive; NOT write-heavy
14. StackSets: deploy templates **across accounts/regions**
15. Lambda: **least operational overhead** for simple microservices
16. Instance tenancy: **most restrictive wins**
17. HTTP API: **native JWT authorizer** (no Lambda needed)
18. Global Accelerator: **UDP**, static IPs, non-HTTP protocols
19. AZ ID: consistent **physical identifier** across accounts
20. EC2 recovery: **retains public IPv4** and all identity

### Resilient Architectures (3 errors)
21. DynamoDB PITR: restore to **any second** in 35 days
22. SQS Standard → FIFO: must **delete and recreate** (can't convert)
23. FIFO with batching: **3,000 msg/s** limit

### Cost-Optimized Architectures (2 errors)
24. AWS SCT: handles **complex schema** (stored procedures, foreign keys)
25. Spot Fleet: **CAN** maintain target capacity; persistent reopens on **interruption**
