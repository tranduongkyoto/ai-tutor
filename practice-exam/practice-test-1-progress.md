# Practice Test #1 — Progress Tracker
**Source:** `practice-test-1-questions.md` (65 questions)
**Started:** 2026-06-23
**Note:** Results recovered from extracted-questions.json (Udemy attempt data)

## Domain Progress

| Domain | Questions | Score | Status |
|--------|-----------|-------|--------|
| Design Secure Architectures | 17 | 10/17 (58%) | Done |
| Design High-Performing Architectures | 24 | 11/24 (45%) | Done |
| Design Resilient Architectures | 13 | 7/13 (53%) | Done |
| Design Cost-Optimized Architectures | 11 | 8/11 (72%) | Done |

## Overall Summary

**TOTAL: 36/65 (55%)**
**Result: FAIL**

## Retake — 2026-08-04

### Design Secure Architectures — Retake: 17/17 (100%) vs Original: 10/17 (58%)

| Q# | Domain | Topic | Original | Retake | Correct | Result |
|----|--------|-------|----------|--------|---------|--------|
| 1 | Secure | EKS IRSA per-Pod IAM roles | Wrong | A | A | Correct |
| 2 | Secure | Aurora Global DB + Aurora regional | Correct | A | A | Correct |
| 3 | Secure | S3 bucket/* ARN for DeleteObject | Correct | C | C | Correct |
| 5 | Secure | GuardDuty S3 + Inspector EC2 | Correct | C | C | Correct |
| 14 | Secure | Outposts + EKS Anywhere on-prem | Wrong | D | D | Correct |
| 17 | Secure | S3 retention: versions + Retain Until Date | Wrong | B, D | B, D | Correct |
| 18 | Secure | IAM role cross-account access | Wrong | D | D | Correct |
| 25 | Secure | MFA + CloudTrail IAM best practices | Correct | A, C | A, C | Correct |
| 27 | Secure | WAF geo match on ALB | Wrong | D | D | Correct |
| 29 | Secure | AD Connector + IAM Identity Center | Correct | D | D | Correct |
| 34 | Secure | CloudFront Geo + Route 53 Geolocation | Correct | A, D | A, D | Correct |
| 37 | Secure | Permissions boundary cap max perms | Correct | A | A | Correct |
| 39 | Secure | EFS: SG + IAM policy access control | Wrong | A, E | A, E | Correct |
| 41 | Secure | Route 53 Resolver outbound to on-prem | Correct | C | C | Correct |
| 47 | Secure | SSE-KMS audit trail no own keys | Correct | A | A | Correct |
| 49 | Secure | Root user: strong password + MFA | Correct | A, E | A, E | Correct |
| 62 | Secure | PrivateLink NLB cross-account RDS | Wrong | B | B | Correct |

### Design High-Performing — Retake: 17/24 (71%) vs Original: 11/24 (45%)

| Q# | Domain | Topic | Original | Retake | Correct | Result |
|----|--------|-------|----------|--------|---------|--------|
| 4 | HP | Redis + DAX leaderboard | Correct | B, C | B, C | Correct |
| 8 | HP | Instance Store high random I/O | Wrong | B | C | Wrong |
| 10 | HP | Comprehend entity extraction S3 | Correct | D | D | Correct |
| 11 | HP | FSx Windows for DFS | Correct | C | C | Correct |
| 15 | HP | REST stateless + WebSocket stateful | Wrong | C | C | Correct |
| 20 | HP | Global Accelerator UDP + custom DNS | Wrong | B | A | Wrong |
| 21 | HP | Babelfish + SCT/DMS migration | Correct | B, D | B, D | Correct |
| 24 | HP | Multipart + S3TA fastest upload | Correct | A | A | Correct |
| 30 | HP | Cluster placement group HPC | Wrong | D | D | Correct |
| 33 | HP | API GW + Kinesis Analytics real-time | Correct | A | B | Wrong |
| 36 | HP | S3TA no charge if not faster | Wrong | A | A | Correct |
| 38 | HP | Direct Connect + VPN encrypted dedicated | Correct | A | C | Wrong |
| 40 | HP | Kinesis + Lambda + DynamoDB ordered | Wrong | B | B | Correct |
| 42 | HP | Lambda + ECS Fargate long-running | Correct | A | B | Wrong |
| 44 | HP | AMI copy = instance + AMI + snapshot | Wrong | A | A | Correct |
| 45 | HP | Glue + Redshift Serverless + Redshift ML | Wrong | A | A | Correct |
| 46 | HP | CloudFront custom origin to on-prem | Wrong | C | A | Wrong |
| 51 | HP | EFS cross-Region via VPC peering | Wrong | A | A | Correct |
| 52 | HP | FSx Lustre for EDA HPC | Correct | C | C | Correct |
| 57 | HP | SQS async + RDS Proxy connection pool | Wrong | A, C | A, D | Wrong |
| 58 | HP | sc1 + st1 cannot be boot volumes | Wrong | A, E | A, E | Correct |
| 63 | HP | Target tracking ASG at 50% CPU | Correct | A | A | Correct |
| 64 | HP | S3 custom prefixes for throughput | Correct | D | D | Correct |
| 65 | HP | ASG rebalance + unhealthy terminate | Wrong | A, B | B, E | Wrong |

### Design Resilient — Retake: 11/13 (85%) vs Original: 7/13 (53%)

| Q# | Domain | Topic | Original | Retake | Correct | Result |
|----|--------|-------|----------|--------|---------|--------|
| 6 | Resilient | Glue DataBrew code-free profiling | Wrong | D | D | Correct |
| 9 | Resilient | ALB path-based routing | Correct | A | A | Correct |
| 12 | Resilient | SQS + Lambda + DynamoDB serverless | Correct | D | D | Correct |
| 16 | Resilient | ASG scheduled action desired=10 | Correct | A | A | Correct |
| 22 | Resilient | Lambda concurrency quota | Correct | A | A | Correct |
| 26 | Resilient | RDS Custom for Oracle multi-AZ | Correct | B | B | Correct |
| 32 | Resilient | S3 versioning + MFA delete | Wrong | C, D | B, C | Wrong |
| 43 | Resilient | ASG Standby + suspend ReplaceUnhealthy | Wrong | C, E | C, E | Correct |
| 48 | Resilient | Multi-AZ sync + read replica async | Wrong | C | A | Wrong |
| 53 | Resilient | CloudWatch metric filter CloudTrail | Correct | A | A | Correct |
| 55 | Resilient | SQS FIFO exactly-once processing | Wrong | C | C | Correct |
| 59 | Resilient | SQS FIFO batch=4 for 1000 msg/s | Correct | B | B | Correct |
| 60 | Resilient | ALB content-based routing + ASG | Wrong | C | C | Correct |

### Design Cost-Optimized — Retake: 10/11 (91%) vs Original: 8/11 (72%)

| Q# | Domain | Topic | Original | Retake | Correct | Result |
|----|--------|-------|----------|--------|---------|--------|
| 7 | Cost | S3 One Zone-IA recreatable assets | Wrong | B | B | Correct |
| 13 | Cost | File Gateway NFS + S3 lifecycle | Correct | D | B | Wrong |
| 19 | Cost | Spot instances interruptible 60min | Correct | A | A | Correct |
| 23 | Cost | S3 Standard-IA for infrequent ms access | Correct | B | B | Correct |
| 28 | Cost | EFS cross-account resource policy | Correct | B | B | Correct |
| 31 | Cost | ECS EC2=EC2+EBS, Fargate=vCPU+mem | Correct | C | C | Correct |
| 35 | Cost | S3 Standard for heavy 24hr access | Wrong | C | C | Correct |
| 50 | Cost | S3 < EFS < EBS storage cost order | Wrong | B | B | Correct |
| 54 | Cost | DAX + CloudFront caching | Correct | C | C | Correct |
| 56 | Cost | S3TA + multipart for upload speed | Correct | B, D | B, D | Correct |
| 61 | Cost | Invalid S3 lifecycle transitions | Correct | C, D | C, D | Correct |

## Retake Summary

**Retake TOTAL: 55/65 (85%) — PASS ✓**
**Original: 36/65 (55%) — FAIL**
**Improvement: +30 points**

| Domain | Original | Retake | Change |
|--------|----------|--------|--------|
| Design Secure Architectures | 10/17 (58%) | 17/17 (100%) | +42pts |
| Design High-Performing | 11/24 (45%) | 17/24 (71%) | +26pts |
| Design Resilient | 7/13 (53%) | 11/13 (85%) | +32pts |
| Design Cost-Optimized | 8/11 (72%) | 10/11 (91%) | +19pts |
