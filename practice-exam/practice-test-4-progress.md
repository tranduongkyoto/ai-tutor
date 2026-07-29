# Practice Test #4 — Progress Tracker
**Source:** `practice-test-4-questions.md` (65 questions)
**Started:** 2026-07-29

## Domain Progress

| Domain | Questions | Score | Status |
|--------|-----------|-------|--------|
| Design Secure Architectures | 15 | 8/15 (53%) | Done |
| Design High-Performing Architectures | 20 | — | In Progress (resume Q17) |
| Design Resilient Architectures | 19 | — | Not started |
| Design Cost-Optimized Architectures | 11 | — | Not started |

## Design Secure Architectures — 8/15 (53%)

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 7 | S3 cross-account access | C | B | Wrong |
| 2 | 8 | ELB unhealthy instances | B,D | B,D | Correct |
| 3 | 9 | SSO across Organizations + on-prem AD | D | B | Wrong |
| 4 | 12 | CloudFormation SG snippet | B,F,G | B,F,G | Correct |
| 5 | 13 | IAM resource-based policy | B | C | Wrong |
| 6 | 14 | Direct Connect + VPN backup | C,D | C,D | Correct |
| 7 | 20 | S3 Object Lock vs Glacier Vault Lock | D | B | Wrong |
| 8 | 21 | S3 bucket policy (CIDR + NotIP) | C | C | Correct |
| 9 | 33 | SG: allow traffic from ALB only | C | A | Wrong |
| 10 | 41 | Lambda → RDS short-lived credentials | B,C | B,D | Wrong |
| 11 | 43 | Multiple domains HTTPS on one LB | C | C | Correct |
| 12 | 48 | Cross-region Direct Connect gateway | B | B | Correct |
| 13 | 50 | Gateway Endpoints (S3 + DynamoDB) | C,D | C,D | Correct |
| 14 | 52 | RDS data-in-transit security | A | B | Wrong |
| 15 | 63 | Can't ping EC2 troubleshooting | C,D | C,D | Correct |

### Weak Areas — Secure Architectures
1. **S3 cross-account** — must use bucket policy (user policies don't work cross-account)
2. **IAM Identity Center** — for enterprise SSO across Organizations (not Cognito)
3. **Trust policy** — only resource-based policy IAM supports (not ACL)
4. **Object Lock Compliance vs Governance** — Compliance truly immutable; Governance overridable
5. **SG reference vs CIDR** — reference ALB's SG, not subnet CIDR
6. **IAM auth to RDS** — generates short-lived tokens (not SSM credential rotation)
7. **SSL for data-in-transit** — SSL encrypts network data; IAM auth is authentication only

## Design High-Performing Architectures — In Progress

| Q# | Orig# | Topic | Your | Correct | Result |
|----|-------|-------|------|---------|--------|
| 1 | 1 | Transit Gateway + ECMP for VPN throughput | B | A | Wrong |
| 2 | 10 | Tape Gateway for tape backup workflow | B | B | Correct |
| 3 | 11 | Real-time analytics pipeline | A | A | Correct |
| 4 | 17 | EFS mount targets per AZ | A | A | Correct |
| 5 | 18 | CloudFormation for RDS best practices | D | D | Correct |
| 6 | 22 | Flash sale 10x dynamic content | D | C | Wrong |
| 7 | 27 | Geoproximity routing (dynamic geo area) | B | D | Wrong |
| 8 | 34 | Neptune for graph queries | B | B | Correct |
| 9 | 37 | Amazon MQ for MQTT protocol | A | A | Correct |
| 10 | 42 | Transit Gateway as central hub | A | C | Wrong |
| 11 | 44 | Global Accelerator for multi-region ALBs | A | A | Correct |
| 12 | 46 | DMS as S3→Kinesis bridge | C | B | Wrong |
| 13 | 51 | Cluster placement group for HPC | C | C | Correct |
| 14 | 53 | DynamoDB on-demand for unpredictable spikes | B | D | Wrong |
| 15 | 55 | Aurora I/O-Optimized storage | C | B | Wrong |
| 16 | 57 | DynamoDB DAX for hot partition | A | A | Correct |

**Resume from: Q17/20** (Orig #58 — Lambda serverless best practices, select three)

### Weak Areas (so far) — High-Performing
1. **Transit Gateway + ECMP** — aggregates VPN bandwidth across multiple tunnels
2. **Dynamic content scaling** — ASG for compute, not CloudFront (CDN caches poorly for dynamic)
3. **Geoproximity routing** — uses bias to expand/shrink geographic routing area
4. **Transit Gateway** — managed central hub (not VPC peering mesh)
5. **DMS S3→Kinesis** — DMS supports S3 as source + Kinesis as target for streaming
6. **DynamoDB on-demand** — instant scaling for unpredictable spikes (auto-scaling too slow)
7. **Aurora I/O-Optimized** — Aurora's own storage type; doesn't use EBS volume types
