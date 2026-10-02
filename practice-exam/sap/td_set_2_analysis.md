# TD Set 2 (Review Mode) — Analysis

**Date:** 2026-09-30 – 10-01 · **Mode:** review, blocks of 25 (answer 25 → review) · multi-select all-or-nothing
**Score:** 43/75 (**57.3%**) ❌ — gate 70%, target 80%
**Source:** `TD_SAP_Review_Set2_Full.md` (Q numbers = shuffled order; TD Q column maps to `SAP-Review-Mode-Set-2.md`)
**Review files:** `td_set_2_review.md` (32 wrong + tracker) · `td_set_2_review_correct.md` (43 right + "Guessed?" tracker)

## Scores

| Domain | Score |
|---|---|
| Accelerate Workload Migration and Modernization | 85.7% 🟢 |
| Continuous Improvement for Existing Solutions | 73.1% 🟡 |
| Design for New Solutions | 50.0% 🔴 |
| Design Solutions for Organizational Complexity | **25.0%** 🔴🔴 |

| Slice | Score |
|---|---|
| Single-choice | 33/57 (58%) |
| Multi-select | 10/18 (56%) — 7 of 8 misses had ≥1 correct pick |
| Seen in drills / unseen | 13/14 (93%) / 30/61 (49%) |
| Block 1 / 2 / 3 | 14 / **11** / 18 (of 25) |

## Trend

| | TD5 (timed) | TD1 (review) | **TD2 (review)** |
|---|---|---|---|
| Total | 41.3% | 61.3% | **57.3%** |
| Unseen only | 41.3% | 54% | **49%** |
| Migration | 27.8% | 66.7% | **85.7%** |
| Continuous Improvement | 52.9% | 56.0% | **73.1%** |
| New Solutions | 36.4% | 53.6% | **50.0%** |
| Org Complexity | 50.0% | 84.6% | **25.0%** |

Migration + Continuous Improvement keep rising (redo passes are working). Org Complexity collapsed — almost entirely identity/access questions.

## Why block 2 was lowest (11/25)
- Fewest drill repeats (3) → unseen 8/22 (36%)
- Security/identity cluster: 7 of 14 misses (Q26, Q28, Q31, Q37, Q41, Q44, Q49) — New Solutions 2/9 in that block
- 4 multi-select misses with one correct pick (Q27, Q28, Q37, Q44) — fixing the second pick = 15/25
- Q26–Q27 answered after ~5 h of questions on 09-30 (minor fatigue factor)

## Wrong answers by pattern (32)

| Group | Wrong | Questions |
|---|---|---|
| A. Identity, access & federation | 9 | 2, 15, 26, 28, 31, 41, 62, 66, 75 |
| B. Edge & data protection | 4 | 1, 37, 44, 49 |
| C. DR / HA / database resilience | 6 | 7, 9, 14, 23, 45, 68 |
| D. Networking | 4 | 17, 18, 27, 34 |
| E. Service fit | 6 | 3, 24, 32, 38, 50, 59 |
| F. Storage, migration & ops | 3 | 43, 56, 67 |

### A. Identity, access & federation (9) — biggest gap
| Q | Correct | Why your pick failed |
|---|---|---|
| 2 | Tag-based IAM Deny + remove terminate permission | MFA doesn't block an authorized action |
| 15 | IAM role via instance profile | Role ARN in Parameter Store adds nothing |
| 26 🔁 | Secrets Manager + **dynamic reference** | `Ref` returns the secret ARN, not the value |
| 28 | LDAP **identity broker** → STS | DX Gateway / Transit VPC is networking |
| 31 | SAML IdP → STS → **IAM Identity Center** | `AssumeRoleWithWebIdentity` is for Google/Facebook |
| 41 | Role trust policy with **External ID** | Plain AssumeRole → confused deputy |
| 62 | Cross-account role **in Dev/Test**, trusting management | Permissions aren't inherited |
| 66 🔁 | **IAM policy** for the cyber team + SSL on ELB | SCP doesn't grant access |
| 75 🔁 | **IAM role** in prod with resource-level conditions | "SCP that allows" is never right |

### B. Edge & data protection (4)
| Q | Correct | Why your pick failed |
|---|---|---|
| 1 | Public ACM cert on ALB (free) | Private CA = monthly fee |
| 37 | Shield Advanced + **WAF** | Cache hit ratio doesn't stop SQLi/XSS |
| 44 | CloudFront signed URLs + **S3 pre-signed URLs** | OAC doesn't restrict to one client |
| 49 | SSE-S3 = unique key per object, AWS-rotated root key | KMS keys = SSE-KMS |

### C. DR / HA / database resilience (6)
| Q | Correct | Why your pick failed |
|---|---|---|
| 7 | Oracle RAC on **EC2** + DLM + Patch Manager | RDS doesn't support RAC |
| 9 | **Warm standby** (RTO 5 min) | Pilot light rebuild > 5 min |
| 14 | Backups + logs to S3 + CRR, AWS Backup PITR | Multi-AZ sync replication isn't DR |
| 23 | Gateway **cached** volumes | Stored volumes cap at 512 TB, full data on-prem |
| 45 | Restore Storage Gateway data to **EBS** | Gateway-on-EC2 iSCSI adds a layer |
| 68 | RDS **Multi-AZ** | RMAN = backup, not HA |

### D. Networking (4)
| Q | Correct | Why your pick failed |
|---|---|---|
| 17 | ALB + Alias, Route 53 multivalue | CloudFront origin can't be a private IP |
| 18 | Forward **web proxy** with URL rules | NACL/SG can't filter URLs |
| 27 | SG chain endpoint→NLB→instances + NACLs | Instance SG must allow NLB, not clients |
| 34 | **Transit Gateway** + GWLB firewalls | Transit VPC + VPN doesn't scale |

### E. Service fit (6)
| Q | Correct | Why your pick failed |
|---|---|---|
| 3 | Partition S3 origin by month | Price classes don't improve load time |
| 24 | IoT rule → **Firehose** + Lambda transform | Step Functions per data point = costly (right in the drill, wrong now = regression) |
| 32 | **IoT Greengrass** local inference | Edge Manager on cameras lacks server runtime |
| 38 | **Step Functions** + DynamoDB | Polling SQS doesn't track state |
| 50 | S3 + **Transcribe** + serverless portal | Translate ≠ speech-to-text |
| 59 | **Reserved concurrency** | Separate account = much more effort |

### F. Storage, migration & ops (3)
| Q | Correct | Why your pick failed |
|---|---|---|
| 43 | **Replatform** | Rehost = unchanged on EC2 |
| 56 | Pre-existing objects = version ID **null** | IDs are never "1" |
| 67 | **sc1** Cold HDD | io1 = most expensive |

## Inconsistent concepts (right in one, wrong in another)
| Right | Wrong | Concept |
|---|---|---|
| Q72, Q55 | Q15 | IAM role / STS temporary credentials |
| Q57 | Q31 | SAML → AssumeRoleWithSAML |
| Q69, Q53 | Q44 | OAC (path) vs signed URLs (who) |
| Q65 | Q1 | ACM public certificates |
| Q11, Q13, Q46 | Q68, Q14 | Multi-AZ = HA, not DR |
| Q19 | Q75, Q66 | IAM conditions grant; SCPs don't |
| Q58, Q70 | Q24 | Streaming ingestion (Kinesis/Firehose) |

## Multi-select lesson
7 of 8 misses had one correct pick. The wrong second pick was a service that **can't do the job**: MFA (Q2), CloudFront private IP origin (Q17), Multi-AZ as DR (Q14), DX Gateway for auth (Q28), cache hit ratio for L7 (Q37), OAC for one client (Q44), client IPs on the instance SG (Q27). Check each pick on its own.

## 10 rules
1. **SCPs never grant access.** Team access = IAM policy; resource-level terminate = IAM role with conditions.
2. Cross-account role lives in the **target** account and trusts the caller.
3. Third party → **External ID**. SAML → **AssumeRoleWithSAML / Identity Center**. Social → WebIdentity/Cognito.
4. Secret into CloudFormation → **dynamic reference**; app reads Secrets Manager at runtime.
5. DR ladder: backup/restore (hours) → pilot light (10s of min) → **warm standby (minutes)** → multi-site.
6. **Multi-AZ = HA**, not DR. Oracle RAC → EC2 only.
7. OAC = only through CloudFront; **signed URLs** = only this client.
8. Speech→text **Transcribe**; text→language Translate; text→speech Polly.
9. Isolate a Lambda's concurrency → **reserved concurrency**.
10. EBS: io1/io2 IOPS · st1 frequent throughput · **sc1 infrequent + cheapest**.

## Next actions
1. Read `td_set_2_review.md` (with 🇻🇳 sections) — group A first.
2. Redo Pass 1 today/tomorrow: `/ai-tutor sap test-review 2 redo A` then B–F.
3. Identity/access deep-dive session before TD Set 3 timed.
4. Gate missed (TD1 61%, TD2 57%) → per plan: redo Passes 1–2 for TD1/TD2, drill weak domains, TD Set 3 timed by ~10-12.
