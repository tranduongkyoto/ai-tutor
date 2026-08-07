# Practice Test #3 — Progress Tracker
**Source:** `practice-test-3-questions.md` (65 questions)
**Started:** 2026-07-21

## Domain Progress

| Domain | Questions | Score | Status |
|--------|-----------|-------|--------|
| Design Secure Architectures | 19 | 11/19 (58%) | Done |
| Design High-Performing Architectures | 25 | 12/24 (50%) 1 skipped | Done |
| Design Resilient Architectures | 13 | 10/13 (77%) | Done |
| Design Cost-Optimized Architectures | 8 | 6/8 (75%) | Done |
| **TOTAL** | **65** | **39/64 (61%)** | **Complete** |

## Design Secure Architectures — 11/19 (58%)

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 5 | EC2 → DynamoDB permissions | A | D | Wrong |
| 2 | 9 | VPC-bound SQS access | A | A | Correct |
| 3 | 12 | CloudFront + S3 IP restriction | A,C | A,C | Correct |
| 4 | 18 | SCP capabilities | A,D,C | A,D,E | Wrong |
| 5 | 30 | GuardDuty vs Macie | B | B | Correct |
| 6 | 31 | Private subnet internet (IPv4) | A | A | Correct |
| 7 | 35 | S3 per-object encryption | A | D | Wrong |
| 8 | 36 | 25 VPCs + Direct Connect | C,E | C,E | Correct |
| 9 | 37 | Config compliance + history | C | C | Correct |
| 10 | 43 | SQS-based Auto Scaling | D | D | Correct |
| 11 | 44 | IPSec VPN config | C | C | Correct |
| 12 | 45 | Shared VPCs via Organizations | D | C | Wrong |
| 13 | 49 | SG stateful vs NACL stateless | B | B | Correct |
| 14 | 52 | Multi-protocol file system (SMB+NFS) | C | B | Wrong |
| 15 | 54 | Route 53 Resolver endpoints | A,C | A,C | Correct |
| 16 | 56 | AMI capabilities | A,B,C | A,B,C | Correct |
| 17 | 61 | DDoS mitigation for ALB | C | D | Wrong |
| 18 | 62 | NAT gateway placement | A | D | Wrong |
| 19 | 64 | Invalid SG inbound source | B | A | Wrong |

### Weak Areas — Secure Architectures
1. **IAM instance profiles** — instance profile assigns role to EC2, not trust policy
2. **SCPs & service-linked roles** — SCPs cannot restrict service-linked roles
3. **SSE-S3** — auto-generates unique key per object, no manual splitting needed
4. **VPC sharing** — shares subnets (not entire VPC) via AWS RAM
5. **FSx for ONTAP** — only option supporting both NFS + SMB protocols
6. **Shield Advanced** — purpose-built DDoS protection, minimal architecture change vs WAF+CloudFront
7. **NAT gateway placement** — must be in public subnet, not private
8. **Security group sources** — cannot use IGW ID; can use other SGs, IPs, CIDRs

## Design High-Performing Architectures — 12/24 (50%) 1 skipped

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 3 | API rate limiting + quotas | C | C | Correct |
| 2 | 4 | NAT instance vs NAT gateway | — | B,E,F | Skipped |
| 3 | 6 | ECS storage high-freq I/O | A | B | Wrong |
| 4 | 14 | Fargate + persistent storage | C | C | Correct |
| 5 | 15 | Static assets cost-optimal | C | C | Correct |
| 6 | 16 | Online data transfer to S3/EFS/FSx | B | D | Wrong |
| 7 | 17 | ECS Auto Scaling metric | A | A | Correct |
| 8 | 19 | NLB routing to instance targets | D | C | Wrong |
| 9 | 20 | Hybrid AD + trust + SQL Server | A | A | Correct |
| 10 | 21 | Upload/download 10GB globally | C | B | Wrong |
| 11 | 22 | Volume Gateway cached vs stored | D | D | Correct |
| 12 | 23 | RDS read replica for reports | A | A | Correct |
| 13 | 24 | ElastiCache use cases | B,E | A,B | Wrong |
| 14 | 25 | SFTP + immediate processing | D | D | Correct |
| 15 | 29 | StackSets cross-account/region | A | B | Wrong |
| 16 | 33 | Python microservice minimal mgmt | B | C | Wrong |
| 17 | 34 | Instance tenancy rules | A | B | Wrong |
| 18 | 41 | 25K IOPS EBS volume | B | B | Correct |
| 19 | 50 | JWT validation OIDC | D | A | Wrong |
| 20 | 51 | Serverless static + dynamic | C | C | Correct |
| 21 | 53 | UDP low-latency global | C | D | Wrong |
| 22 | 57 | Windows ACLs + SMB + Linux access | A | A | Correct |
| 23 | 59 | Aurora to reduce replication lag | C | C | Correct |
| 24 | 60 | AZ ID across accounts | A | C | Wrong |
| 25 | 63 | Reduce IPs multi-region ALBs | C | B | Wrong |

### Weak Areas — High-Performing Architectures
1. **EFS Provisioned vs Bursting Throughput** — Provisioned for high I/O with small storage
2. **AWS DataSync** — for automating online transfers to S3/EFS/FSx (not Transfer Family)
3. **NLB routing** — uses primary private IP when targets registered by instance ID
4. **S3 Transfer Acceleration** — for accelerating uploads; CloudFront for downloads
5. **ElastiCache** — good for read-heavy + compute-intensive, NOT write-heavy
6. **CloudFormation StackSets** — deploy templates across accounts/regions (not RAM)
7. **Lambda vs Fargate** — Lambda = least operational overhead for simple microservices
8. **Instance tenancy** — most restrictive wins (dedicated from either LT or VPC)
9. **API Gateway HTTP API JWT authorizer** — native JWT validation, no custom code
10. **Global Accelerator** — for UDP, multi-region static IPs, non-HTTP protocols
11. **AZ ID** — physical identifier consistent across accounts (AZ names are randomized)

## Design Resilient Architectures — 10/13 (77%)

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 1 | Real-time streaming processor | C | C | Correct |
| 2 | 2 | Cross-zone load balancing | D | D | Correct |
| 3 | 7 | Decouple fast/slow microservices | C | C | Correct |
| 4 | 8 | Windows SMB file storage | A,C | A,C | Correct |
| 5 | 10 | DynamoDB corrupted data recovery | B | A | Wrong |
| 6 | 11 | Windows shared storage + AD | C | C | Correct |
| 7 | 13 | EC2 auto recovery (single instance) | C | C | Correct |
| 8 | 26 | EC2 recovery behavior | B,D | B,C | Wrong |
| 9 | 28 | Synchronous replication (2 nodes) | C | C | Correct |
| 10 | 32 | Who does NAT for public EC2 | A | A | Correct |
| 11 | 39 | Real-time health data + retry | B | B | Correct |
| 12 | 40 | SQS Standard → FIFO migration | F,C,D | A,C,D | Wrong |
| 13 | 58 | Centralized patch management | A | A | Correct |

### Weak Areas — Resilient Architectures
1. **DynamoDB PITR vs on-demand backup** — PITR restores to any second (continuous); on-demand only to snapshot time
2. **EC2 recovery retains public IPv4** — recovered instance keeps instance ID, private IPs, Elastic IPs, AND public IPv4
3. **Cannot convert SQS Standard to FIFO** — must delete and recreate; FIFO with batching = 3,000 msg/s limit

## Design Cost-Optimized Architectures — 6/8 (75%)

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 27 | Route 53 alias vs CNAME (zone apex) | A | A | Correct |
| 2 | 38 | CNAME for non-AWS hostname | A | A | Correct |
| 3 | 42 | DB migration (complex schema) | B,E | B,C | Wrong |
| 4 | 46 | Serverless weekly cron job | B | B | Correct |
| 5 | 47 | SQS cost optimization | A | A | Correct |
| 6 | 48 | Reduce S3 outbound costs | C | C | Correct |
| 7 | 55 | VPC gateway endpoint for S3 | A | A | Correct |
| 8 | 65 | Spot Instance capabilities | C,D,B | C,D,E | Wrong |

### Weak Areas — Cost-Optimized Architectures
1. **AWS SCT vs Basic Schema Copy** — SCT handles complex objects (stored procedures, foreign keys); Basic Schema Copy only handles simple schemas
2. **Spot Fleet maintains target capacity** — Spot Fleets CAN launch replacements; persistent requests reopen on interruption (not on stop)

## Overall Summary — 39/64 (61%) — Passing: 72%

**Priority study areas:**
1. High-Performing (50%) — Global Accelerator, DataSync, StackSets, tenancy, NLB routing, API Gateway HTTP API
2. Secure (58%) — IAM instance profiles, SCPs, VPC sharing, Shield Advanced, NAT placement, FSx for ONTAP

## Retake — 2026-08-06

**Retake Score: 54/65 (83%) — PASS ✓**
**Improvement: +22 points (61% → 83%)**
**Note:** Retake uses different questions than original (Udemy randomizes).

| Domain | Original | Retake | Change |
|--------|----------|--------|--------|
| Design Secure Architectures | 11/19 (58%) | 17/19 (89%) | +31pts |
| Design High-Performing Architectures | 12/24 (50%) | 20/25 (80%) | +30pts |
| Design Resilient Architectures | 10/13 (77%) | 10/13 (76%) | -1pt |
| Design Cost-Optimized Architectures | 6/8 (75%) | 7/8 (87%) | +12pts |

### Wrong on Retake (11 questions — from retake HTML, different questions than original)

| Q# | Domain | Topic |
|----|--------|-------|
| 8 | HP | DataSync for multi-service migration (S3+EFS+FSx) |
| 11 | HP | ECS Auto Scaling on service CPU metric |
| 17 | HP | S3 Transfer Acceleration for global uploads |
| 24 | Secure | SSE-S3 auto-generates unique key per object |
| 26 | Resilient | EC2 recovery retains public IPv4 + instance ID |
| 28 | Secure | IGW ID invalid as security group source |
| 34 | Resilient | Internet Gateway makes subnet public |
| 42 | Cost | Zone apex Alias record (not CNAME) |
| 46 | HP | Cloud Directory + Managed Microsoft AD |
| 56 | Resilient | CloudWatch alarm EC2 recovery action |
| 57 | HP | NAT instance = EC2 (bastion, SG, port forwarding) |
