# TD Set 1 (Review Mode) — Analysis

**Date:** 2026-09-28 · **Mode:** review, blocks of 25 (answer 25 → review) · multi-select all-or-nothing
**Score:** 46/75 (**61.3%**) ❌ — gate 70%, target 80%
**Source:** `TD_SAP_Review_Set1_Full.md` (Q numbers = shuffled order; the TD Q column in the export maps to `SAP-Review-Mode-Set-1.md`)
**Review files:** `td_set_1_review.md` (29 wrong + tracker) · `td_set_1_review_correct.md` (46 right + "Guessed?" tracker)

## Scores

| Domain | Score |
|---|---|
| Design Solutions for Organizational Complexity | 84.6% 🟢 |
| Accelerate Workload Migration and Modernization | 66.7% 🟡 |
| Continuous Improvement for Existing Solutions | 56.0% 🔴 |
| Design for New Solutions | 53.6% 🔴 |

| Slice | Score |
|---|---|
| Single-choice | 42/67 (63%) |
| Multi-select | 4/8 (50%) — 3 of 4 misses had ≥1 correct pick |
| Seen in drills / unseen | 17/21 (81%) / 29/54 (54%) |
| Q1–25 / Q26–50 / Q51–75 | 64% / 68% / 52% ⚠️ last block dropped |

## vs TD Set 5 (timed, 09-25)
+20 pts overall (41.3% → 61.3%). Migration jumped 27.8% → 66.7% and Org Complexity 50% → 84.6% (Set 5 redo carried over).
Still weak: **New Solutions** and **Continuous Improvement** (ops: patching, troubleshooting, cost).
Unseen-only 54% is the honest number for a clean set. Expect Set 3 timed to land around 55–60%.

## Wrong answers by pattern (29)

| Group | Wrong | Questions |
|---|---|---|
| A. Hybrid networking & DNS | 4 | 5, 36, 27, 61 |
| B. Security controls | 4 | 68, 22, 47, 74 🔁 |
| C. Ops: patching, compliance, troubleshooting | 4 | 12 🔁, 13, 53, 73 🔁 |
| D. Multi-account governance & cost | 3 | 28, 40, 55 |
| E. Resilience / DR / performance | 4 | 10, 14, 17, 25 |
| F. Serverless & app architecture | 6 | 64 🔁, 21, 65, 72, 69, 62 |
| G. Migration | 4 | 57, 26, 29, 42 |

🔁 = missed before in chapter drills. **Q64, Q73, Q74: same wrong pick as the drill.** These are not guesses. You believe the wrong rule.

### A. Hybrid networking & DNS
| Q | Correct | Why your pick failed |
|---|---|---|
| 5 | **VPN to each VPC's VGW** as DX backup (BGP) | MPLS can't connect directly to VPCs; not cheapest |
| 36 | **Public VIF** + Site-to-Site VPN over DX | Private VIF can't carry the VPN (VPN endpoints are public IPs) — **4th miss on this concept** |
| 27 | Central PHZ + **programmatically associate** other accounts' VPCs | PHZs can't be delegated via NS records |
| 61 | **NAT GW in the public subnet**, public IP disabled | ECR needs interface endpoints, not a gateway endpoint; public IP is useless without an IGW |

### B. Security controls
| Q | Correct | Why your pick failed |
|---|---|---|
| 68 | **Route 53 DNSSEC signing + ACM cert** on ALB + CloudFront HTTPS redirect | Third-party DNS/certs not needed |
| 22 | **NACL deny** + **Shield Advanced** | Windows Firewall per host; GuardDuty only detects |
| 47 | **CloudHSM across 2 AZs**, TCP LB, S3 SSE logs | Single CloudHSM = not HA (only difference between the options) |
| 74 🔁 | **Secrets Manager** + task execution role | Parameter Store has no rotation/lifecycle — same pick as the drill; also a Set 5 repeat |

### C. Ops: patching, compliance, troubleshooting
| Q | Correct | Why your pick failed |
|---|---|---|
| 12 🔁 | **Patch Manager baseline + Config `approved-amis-by-id`** | GuardDuty doesn't check patches/AMIs (drill: C,D → now B,C) |
| 13 | **2 patch groups + 2 non-overlapping Maintenance Windows** | One group + cron = everything reboots together |
| 53 | Tag by **environment + OS**, baseline per env, Patch Groups | Tag by OS only can't exclude prod |
| 73 🔁 | **Suspend ASG Terminate process** + Session Manager | Verbose logs don't stop termination — same pick as the drill |

### D. Multi-account governance & cost
| Q | Correct | Why your pick failed |
|---|---|---|
| 28 | RAM **trusted access** (`enable-sharing-with-aws-organization`) | "Cross-account access" is not the RAM mechanism |
| 40 | Move SCPs **root → Production OU** + temporary Onboarding OU | Removing the root restriction opens Config to every account |
| 55 | **S3 Requester Pays** | s3 sync still pays transfer out + extra storage |

### E. Resilience / DR / performance
| Q | Correct | Why your pick failed |
|---|---|---|
| 10 | Hourly backups to **S3** + logs every 5 min + **Macie** | Glacier retrieval risks RTO <3h |
| 14 | **Aurora Global DB** active-active + geolocation + failover records | MySQL can't sync two writers cross-Region; Multi-AZ ≠ multi-Region |
| 17 | **Lambda@Edge auth + CloudFront origin failover** | Multi-Region deployment = not minimal cost |
| 25 | **Simple HTML health check + ElastiCache** | RDS MySQL has no single reader endpoint; TCP check doesn't test the app |

### F. Serverless & app architecture
| Q | Correct | Why your pick failed |
|---|---|---|
| 64 🔁 | RDS + **API Gateway caching** + right-size Lambda | CloudFront + DAX = extra paid services — same pick as the drill |
| 21 | **Cognito + DynamoDB + S3 + CloudFront** | SAML isn't used for social IdPs; RDS scales worse |
| 65 | **S3 website + AssumeRoleWithWebIdentity** | NGINX EC2 fleet = cost, no STS |
| 72 | Batch reports → **S3 + CloudFront** daily TTL | ElastiCache cluster = extra cost |
| 69 | **AWS Batch + Spot + S3** | SQS + ASG = DIY; EFS pricier than S3 |
| 62 | **Amazon Connect + Lex** | MediaConnect = video; Polly = text-to-speech |

### G. Migration
| Q | Correct | Why your pick failed |
|---|---|---|
| 57 | **File Gateway** + Rekognition via Lambda | Rekognition can't read tape gateway/Glacier |
| 26 | EC2 ×2 AZs + **DMS** + ELB + Route 53 alias | Option says "Multi-AZ RDS in one AZ only" (contradiction) + stale backup import |
| 29 | **AWS MGN** continuous replication | VM Import scripts = overhead, no continuous sync |
| 42 | Data Transfer Terminal + **SCT + DMS CDC** | Needless Oracle RDS hop, increments over internet |

## Inconsistent concepts (right in one question, wrong in another)
| Right | Wrong | Concept |
|---|---|---|
| Q58 | Q27 | Cross-account private hosted zone → VPC association |
| Q54 | Q74 | Parameter Store vs Secrets Manager (rotation) |
| Q70 | Q36 | DX VIF types (private vs public for VPN) |
| Q39 | Q61 | NAT Gateway / private-subnet egress |
| Q11 | Q65, Q21 | Web identity federation / Cognito |
| Q2 | Q13, Q53 | Systems Manager patching |
| Q48, Q63 | Q40 | SCP inheritance root → OU |
| Q19 | Q12 | Config rules for compliance detection |

## Multi-select lesson
3 of 4 multi-select misses had one correct pick (Q12 B, Q14 E, Q17 D). The second pick used a tool that
doesn't do the job (GuardDuty for AMI compliance, cross-Region MySQL writers, multi-Region deploy for a cost question).
Ask: **does each pick do what the requirement says, at the cost the question asks for?**

## 10 rules
1. VPN over Direct Connect → **public VIF**. Cheapest DX backup → **VPN**.
2. "Rotation" / "lifecycle" for secrets → **Secrets Manager** (Parameter Store = plain config/SecureString).
3. Debug instances that the ASG keeps killing → **suspend the Terminate process**.
4. Reduce Lambda invocations cheaply → **API Gateway caching**, not CloudFront + DAX.
5. Detect but don't block → **AWS Config rule**. Block → SCP/IAM. GuardDuty = threats only.
6. Staggered patching → **multiple patch groups + non-overlapping Maintenance Windows**; per-env → tag by environment.
7. Root SCP restriction blocks everyone → **move it to the OU** + onboarding OU.
8. Cross-account PHZ → **association authorization + associate VPC**, never NS delegation.
9. Social login for app users → **Cognito / web identity federation (OIDC)**. SAML = enterprise IdPs.
10. Read every step of long options: one wrong detail (single CloudHSM, "one AZ only", tape gateway) kills the option.

## Next actions
1. **Today (Pass 1):** read `td_set_1_review.md`, then `redo` groups A+B and C+D. Q64/Q73/Q74 first.
2. Skim `td_set_1_review_correct.md` and tick "Guessed?", especially the inconsistent-concept rows.
3. Pass 2 around 10-02 – 10-03, Pass 3 around 10-06.
4. TD1 is below the 70% gate. Continue with **TD Set 2 in review mode** as planned, then target ops (Patch Manager/Config)
   and New Solutions (serverless cost patterns) before TD Set 3 timed.
