# Practice Test #3 — Progress Tracker
**Source:** `practice-test-3-questions.md` (65 questions)
**Started:** 2026-07-21

## Domain Progress

| Domain | Questions | Score | Status |
|--------|-----------|-------|--------|
| Design Secure Architectures | 19 | 11/19 (58%) | Done |
| Design High-Performing Architectures | 25 | 1/2 then paused | In Progress (resume Q3) |
| Design Resilient Architectures | 13 | — | Not started |
| Design Cost-Optimized Architectures | 8 | — | Not started |

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

## Design High-Performing Architectures — In Progress

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 3 | API rate limiting + quotas | C | C | Correct |
| 2 | 4 | NAT instance vs NAT gateway | — | B,E,F | Skipped |

**Resume from: Q3/25**
