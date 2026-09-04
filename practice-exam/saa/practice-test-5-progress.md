# Practice Test #5 — Progress Tracker
**Source:** `practice-test-5-questions.md` (65 questions)
**Started:** 2026-08-01

## Domain Progress

| Domain | Questions | Score | Status |
|--------|-----------|-------|--------|
| Design Secure Architectures | 19 | 13/19 (68%) | Done |
| Design High-Performing Architectures | 13 | 8/13 (62%) | Done |
| Design Resilient Architectures | 19 | 9/19 (47%) | Done |
| Design Cost-Optimized Architectures | 14 | 12/14 (86%) | Done |

## Design Secure Architectures — 13/19 (68%)

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 5 | Dedicated Instances vs Hosts | A | D | Correct (redo) |
| 2 | 13 | WAF rate-based rule | D | D | Correct |
| 3 | 16 | Alternate contacts setup | C | D | Wrong (redo) |
| 4 | 17 | Transit Gateway star network | C | C | Correct |
| 5 | 21 | Cognito identity pool + VPC endpoint | D, E | D, E | Correct |
| 6 | 25 | Firewall Manager resources | D, E, F | C, D, E | Correct (redo) |
| 7 | 28 | GuardDuty crypto mining | A | A | Correct |
| 8 | 33 | CloudFront OAI for S3 | D | D | Correct |
| 9 | 37 | VPN CloudHub branch offices | D | D | Correct |
| 10 | 40 | NLB public + ASG private | D | D | Correct |
| 11 | 43 | DX Public VIF for S3 access | A | C | Correct (redo) |
| 12 | 47 | Control Tower + RAM shared VPC | A | A | Correct |
| 13 | 48 | Site-to-Site VPN quick setup | A | A | Correct |
| 14 | 49 | Gateway endpoints S3 + DynamoDB | C | C | Correct |
| 15 | 52 | S3 Storage Lens versioning audit | A | B | Correct (redo) |
| 16 | 55 | Client-side encryption proprietary algo | B | C | Correct (redo) |
| 17 | 57 | IAM group for 50 users | C | C | Correct |
| 18 | 60 | NACL stateless outbound rules | B | B | Correct |
| 19 | 64 | AWS Managed Microsoft AD trust | B | B | Correct |

### Weak Areas — Secure Architectures
1. **Dedicated Instances vs Hosts** — Dedicated Instances = cost-effective single-tenant; Dedicated Hosts = per-host control for BYOL. Both are single-tenant, but Instances are cheaper when you only need isolation.
2. **AWS alternate contacts** — Use alternate contacts (billing, security, operations) with distribution lists for service-specific notifications. Root email to centralized monitored mailbox.
3. **Firewall Manager scope** — Manages WAF, Shield Advanced, and VPC Security Groups. NOT Inspector, GuardDuty, or Route Tables.
4. **Direct Connect Public VIF** — To access S3 directly from on-premises via DX, use Public VIF (S3 is a public service). Private VIF only reaches VPC private IPs.
5. **S3 Storage Lens** — Advanced metrics dashboard shows bucket-level config (versioning, encryption) across all Regions/accounts. Better than building CloudTrail+Lambda for auditing bucket configurations.
6. **Client-side encryption vs SSE-C** — SSE-C = bring your own key but AWS uses AES-256 algorithm. Client-side encryption = bring your own algorithm AND key. "Proprietary algorithm" = client-side.

## Design High-Performing Architectures — 8/13 (62%)

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 3 | IAM Identity Center permission sets | B | B | Correct |
| 2 | 4 | Instance Store characteristics | B, C | B, E | Correct (redo) |
| 3 | 6 | DAX + ElastiCache caching | A, C | A, C | Correct |
| 4 | 7 | ASG target tracking on SQS depth | D | D | Correct |
| 5 | 22 | EFA for HPC | B | B | Correct |
| 6 | 23 | CloudFront + S3 Transfer Acceleration | A | A | Correct |
| 7 | 30 | MGN lift-and-shift workflow | B, C, E | B, E, F | Correct (redo) |
| 8 | 31 | Kinesis on-demand + Lambda real-time | C | C | Correct |
| 9 | 36 | SQS temporary queues request-response | A | D | Correct (redo) |
| 10 | 54 | NLB for bastion host HA | A | B | Correct (redo) |
| 11 | 58 | S3 Byte Range Fetch for metadata | C | A | Wrong (redo) |
| 12 | 61 | AWS Batch + Step Functions + S3 | A | C | Correct (redo) |
| 13 | 63 | Kinesis + Fargate 30-min jobs | D, E | D, E | Correct |

### Weak Areas — High-Performing Architectures
1. **Instance Store hibernation** — Instance store data is NOT preserved during hibernation. Only RAM is saved to root EBS volume. Instance store is ephemeral in ALL cases (stop, terminate, hibernate).
2. **MGN migration workflow** — Install replication agent → continuous replication → launch test instances → validate → launch cutover instance. No Auto Scaling involved in migration.
3. **SQS temporary queues** — Purpose-built for request-response pattern. Virtual queues that auto-delete, saving dev time and cost. Dead-letter queues handle failed messages, not request-response.
4. **NLB vs ALB for bastion hosts** — SSH is TCP (L4), so NLB is correct. ALB is L7 HTTP/HTTPS only — cannot pass through SSH connections.
5. **S3 Byte Range Fetch** — Use HTTP Range header to fetch specific bytes from an object. For 50TB across 100K files, fetching only 250 bytes per file is far more efficient than full downloads or RDS import.
6. **AWS Batch + Step Functions** — Batch for managed compute (auto-scaling, no server management) for batch processing. Step Functions for workflow orchestration. EKS self-managed is high overhead.

## Design Resilient Architectures — 9/19 (47%)

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 2 | RDS Multi-AZ characteristics | A, D | A, C | Correct (redo) |
| 2 | 8 | SQS delay queues vs visibility timeout | B | C | Correct (redo) |
| 3 | 11 | ELB cross-region not allowed | C | C | Correct |
| 4 | 14 | EBS Multi-Attach io1/io2 only | C | D | Correct (redo) |
| 5 | 15 | VPC DNS settings for private hosted zones | B, E | A, B | Correct (redo) |
| 6 | 19 | S3 for HA document store | C | C | Correct |
| 7 | 20 | NAT GW HA one per AZ public subnet | D | D | Correct |
| 8 | 24 | CloudFront + Aurora Replica read spikes | C, D | C, D | Correct |
| 9 | 27 | CloudFront signed URLs/cookies | D, E | A, B | Correct (redo) |
| 10 | 41 | Monolith HA ASG + EIP + Instance Role | B, C, F | A, B, F | Correct (redo) |
| 11 | 42 | Read replica same capacity for analytics | D | B | Correct (redo) |
| 12 | 44 | Aurora Global Database for DR | D | C | Correct (redo) |
| 13 | 45 | AMI + 2 instances 2 AZs + NLB | B | B | Correct |
| 14 | 46 | Aurora Serverless for OLTP + spikes | A | A | Correct |
| 15 | 51 | Amazon MQ for RabbitMQ migration | B | B | Correct |
| 16 | 53 | SQS priority two queues polling | C | A | Correct (redo) |
| 17 | 56 | ASG 2 AZs + ALB + Multi-AZ RDS | C | C | Correct |
| 18 | 62 | Memcached for multi-threading | D | A | Correct (redo) |
| 19 | 65 | User data runs once by default | D | A | Correct (redo) |

### Weak Areas — Resilient Architectures
1. **RDS Multi-AZ standby** — Standby is NOT readable (passive failover only). Replication is synchronous not async. Backups taken from standby, not primary. OS maintenance: standby first → promote → patch old primary.
2. **SQS delay queues vs visibility timeout** — Delay queues postpone delivery of NEW messages. Visibility timeout hides messages AFTER receipt by a consumer. "Postpone delivery" = delay queue.
3. **EBS Multi-Attach** — Only io1/io2 (Provisioned IOPS SSD) support Multi-Attach. gp2/gp3, st1, sc1 do NOT.
4. **VPC DNS settings** — Only two real settings: enableDnsSupport and enableDnsHostnames. Both required for Route 53 private hosted zones. enableVpcSupport/enableVpcHostnames/enableDnsDomain don't exist.
5. **CloudFront signed URLs/cookies** — These restrict WHO can access content (authorization). HTTPS options secure the CONNECTION (encryption). Access restriction ≠ encryption.
6. **Monolith HA pattern** — ASG min=1 max=1 (not max=2) + EIP attached via user-data + Instance Role for API calls. ALB is unnecessary cost for single-instance monolith.
7. **Read replica sizing** — Match primary capacity for heavy analytics workloads. Half capacity creates a bottleneck.
8. **Aurora Global Database** — Purpose-built for cross-region DR. RPO <1s, RTO <1min, managed failover. Always choose over DMS or snapshot-based replication for Aurora DR.
9. **SQS priority pattern** — Two separate queues + consumer logic polls pro queue first. Polling type (short/long) does NOT determine priority.
10. **Memcached vs Redis threading** — Memcached = multi-threaded. Redis = single-threaded. When question says "multi-threading" → Memcached.
11. **EC2 user data** — Runs only once at first launch BY DEFAULT. No special configuration needed for "run once" behavior.

## Design Cost-Optimized Architectures — 12/14 (86%)

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 1 | S3 Gateway VPC endpoint | D | D | Correct |
| 2 | 9 | AWS Budgets actions auto-enforce | B | B | Correct |
| 3 | 10 | Spot instances + Spot fleet chars | A, C | A, C | Correct |
| 4 | 12 | S3 Analytics Standard to IA only | C | C | Correct |
| 5 | 18 | Private IP for cross-AZ replication | D | D | Correct |
| 6 | 26 | Budgets coverage for Savings Plans | C | C | Correct |
| 7 | 29 | Standard-IA after 30d + 4yr delete | B | B | Correct |
| 8 | 32 | Spot Instance persistent for 30-min job | D | D | Correct |
| 9 | 34 | Same-region Read Replica for analytics | D | D | Correct |
| 10 | 35 | Compute + SageMaker Savings Plans | B, E | B, E | Correct |
| 11 | 38 | Dedicated Hosts for BYOL | C | B | Correct (redo) |
| 12 | 39 | Athena + S3 IA for cold Redshift data | E, C | A, E | Correct (redo) |
| 13 | 50 | EFS IA for POSIX archive | A | A | Correct |
| 14 | 59 | S3 Intelligent-Tiering | D | D | Correct |

### Weak Areas — Cost-Optimized Architectures
1. **Dedicated Hosts vs Instances for BYOL** — Server-bound licenses need host-level visibility (sockets, cores, host ID) → Dedicated Hosts. Dedicated Instances = isolation only, no host visibility.
2. **Athena for cold data** — For rarely queried data, move to S3 IA + use Athena (serverless, pay-per-query). Don't keep a Redshift cluster running for cold data — even a smaller one costs 24/7.

## Overall Summary

**TOTAL: 42/65 (65%)**
**Result: BORDERLINE (65-71%)**

| Domain | Score | Pct |
|--------|-------|-----|
| Design Secure Architectures | 13/19 | 68% |
| Design High-Performing Architectures | 8/13 | 62% |
| Design Resilient Architectures | 9/19 | 47% |
| Design Cost-Optimized Architectures | 12/14 | 86% |

## Redo Results

**Redo Score: 23/25 (92%)**
**Date:** 2026-08-02

| # | Orig# | Topic | Domain | Redo Result |
|---|-------|-------|--------|-------------|
| 1 | 5 | Dedicated Instances vs Hosts | Secure | Correct |
| 2 | 16 | Alternate contacts setup | Secure | Wrong |
| 3 | 25 | Firewall Manager resources | Secure | Correct |
| 4 | 43 | DX Public VIF for S3 access | Secure | Correct |
| 5 | 52 | S3 Storage Lens versioning audit | Secure | Correct |
| 6 | 55 | Client-side encryption proprietary algo | Secure | Correct |
| 7 | 4 | Instance Store characteristics | HP | Correct |
| 8 | 30 | MGN lift-and-shift workflow | HP | Correct |
| 9 | 36 | SQS temporary queues request-response | HP | Correct |
| 10 | 54 | NLB for bastion host HA | HP | Correct |
| 11 | 58 | S3 Byte Range Fetch for metadata | HP | Wrong |
| 12 | 61 | AWS Batch + Step Functions + S3 | HP | Correct |
| 13 | 2 | RDS Multi-AZ characteristics | Resilient | Correct |
| 14 | 8 | SQS delay queues vs visibility timeout | Resilient | Correct |
| 15 | 14 | EBS Multi-Attach io1/io2 only | Resilient | Correct |
| 16 | 15 | VPC DNS settings for private hosted zones | Resilient | Correct |
| 17 | 27 | CloudFront signed URLs/cookies | Resilient | Correct |
| 18 | 41 | Monolith HA ASG + EIP + Instance Role | Resilient | Correct |
| 19 | 42 | Read replica same capacity for analytics | Resilient | Correct |
| 20 | 44 | Aurora Global Database for DR | Resilient | Correct |
| 21 | 53 | SQS priority two queues polling | Resilient | Correct |
| 22 | 62 | Memcached for multi-threading | Resilient | Correct |
| 23 | 65 | User data runs once by default | Resilient | Correct |
| 24 | 38 | Dedicated Hosts for BYOL | Cost | Correct |
| 25 | 39 | Athena + S3 IA for cold Redshift data | Cost | Correct |

### Still Weak (wrong on redo)
1. **AWS Alternate Contacts (Q16)** — Billing/security/operations alternate contacts with distribution lists. Not IAM, not root email splitting.
2. **S3 Byte Range Fetch (Q58)** — HTTP Range header fetches specific bytes from S3 object. For extracting small metadata from many large files, far more efficient than downloading full objects.
