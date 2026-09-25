# TD Set 5 (Timed Mode) — Analysis

**Date:** 2026-09-25 · **Mode:** Timed on TD website (180 min, finished in time)
**Score:** 31/75 (**41.3%**) ❌ — target 80%
**Source:** `TD_SAP_Timed_Set5_Full.md` (Q numbers = shuffled web order; all 75 Qs verified identical to `SAP-Review-Mode-Set-5.md`)

## Scores

| Domain | Score |
|---|---|
| Accelerate Workload Migration and Modernization | 27.78% 🔴 |
| Design for New Solutions | 36.36% 🔴 |
| Design Solutions for Organizational Complexity | 50.00% 🔴 |
| Continuous Improvement for Existing Solutions | 52.94% 🔴 |

| Slice | Score |
|---|---|
| Single-choice | 26/54 (48%) |
| Multi-select | **5/21 (24%)** — 13 of 16 misses had ≥1 correct pick |
| Q1–25 / Q26–50 / Q51–75 | 28% / 52% / 44% |

## Why drill 70.5% → timed 41.3%
1. Multi-select all-or-nothing (drills gave 0.5 partial credit) — ~13 Qs lost
2. Chapter drills pre-announce topic; mixed test requires identifying it
3. Set 5 migration-heavy; migrations chapter never drilled (0/23); new services (AWS Transform, Migration Evaluator, VM Import, Transfer Family, MediaConvert, Service Catalog)

## Wrong answers by pattern (44)

| Group | Wrong | Questions |
|---|---|---|
| A. DIY over managed service | 12 | 1, 8, 10, 14, 24, 28, 35, 38, 51, 68, 72, 73 |
| B. Multi-account governance | 9 | 16, 18, 19, 29, 31, 36, 54, 62, 67 |
| C. DR / Route 53 | 5 | 9, 20, 42, 57, 61 |
| D. Migration | 7 | 4, 32, 33, 49, 55, 63, 74 |
| E. Serverless + DB | 4 | 5, 13, 30, 58 |
| F. Networking / S3 / perf | 7 | 12, 15, 21, 22, 23, 48, 69 |

### A. DIY over managed service (12)
| Q | Correct | Why yours was wrong |
|---|---|---|
| 1 | **Glue crawler + custom classifier + Glue ETL job** | Lambda→SQS→Fargate = custom code, not easily expandable |
| 8 | **Compute Optimizer + `ExportLambdaFunctionRecommendations`** | Lambda Insights = monitoring, no recommendations/savings |
| 10 | **Transfer Family, VPC-hosted internet-facing endpoint** (keep EIP + SG) | Public endpoint → can't use SG to allowlist partner IPs |
| 14 | 40-min job → **container on Fargate, Lambda calls RunTask** on S3 upload | EC2 ASG + SQS polling = still managing EC2 |
| 35 | **Containerize → ECR** + Fargate task triggered by Lambda | Same as 14; both picks = one solution |
| 28 | **SSM managed nodes + Patch Manager** (patching + compliance reports) | Config = config compliance, not patching |
| 38 | **StackSets trusted access + service-managed + auto-deploy** from mgmt account | Self-managed per member account defeats StackSets |
| 51 | New key pair → **extract public key** → **SSM Run Command** updates authorized_keys | Downloaded .pem = private key |
| 68 | **Service Catalog + launch constraint** | Elastic Beanstalk = convert CFN templates, not least-privilege self-service |
| 72 | **MediaConvert** MP4→HLS + S3 + CloudFront | Jenkins + EC2 + EBS = DIY, low HA |
| 73 | Serverless webhooks → **Lambda Function URL** | Fargate + HTTP API + ALB = over-engineered |
| 24 | WorkSpaces location restriction → **IP access control groups** | Windows Firewall per image = high ops effort |

### B. Multi-account governance (9)
| Q | Correct | Lesson |
|---|---|---|
| 16 | **CUR from management account → QuickSight dashboard** | RAM can't generate CUR |
| 29 | **Activate user-defined cost allocation tag** in mgmt account + CUR tag breakdown | Resource Groups ≠ billing |
| 19 | SCP deny `ec2:AuthorizeSecurityGroup*` with **`aws:ResourceTag/scope`**, attach PROD OU | Tag critical resources; `aws:SourceIp` wrong condition |
| 31 | **SCP deny RunInstances w/o tag + Config rule + Config aggregator** | Security Hub / Inspector don't check tags |
| 67 | **Enable RAM sharing w/ Organizations + RAM share subnets to OU** | No SCP needed — shared-VPC participants can't manage VPC |
| 18 | **Share TGW via RAM + auto-accept attachments** | VPC endpoint per app doesn't scale |
| 54 | **IAM Identity Center + SAML 2.0 + SCIM + ABAC** | Copying users into Managed AD = duplicate identities |
| 36 | **RAM share Aurora cluster → Aurora clone** | Clone faster than snapshot restore (less downtime) |
| 62 | **Gateway Load Balancer + PrivateLink** + ASG w/ launch template for appliances | Direct Connect = on-prem link, not appliance scaling |

### C. DR / Route 53 (5)
| Q | Correct | Lesson |
|---|---|---|
| 9 | RTO 30m → **cross-Region read replica + auto-promote Lambda + R53 failover record** | Snapshot/S3 restore > 30 min |
| 61 | **Failover routing + Lambda scales ASG + promotes replica** | Weighted ≠ failover |
| 42 | Closest + failover → **latency alias + Evaluate Target Health** | Geolocation ≠ latency |
| 20 | **Cross-Region read replica** = DR + analytics offload | Don't migrate to DynamoDB |
| 57 | **2nd DX connection + Direct Connect Gateway** | VGWs in 2 Regions can't share one private VIF |

### D. Migration (7)
| Q | Scenario | Service |
|---|---|---|
| 4 | VMware → EC2, keep config | **VM Import/Export** (OVF → S3 → `import-image`) |
| 32 | On-prem Windows files needed by AWS servers | **FSx for Windows + DataSync** (File Gateway lands in S3) |
| 33 | Hyper-V processes/CPU/deps discovery | **AWS Transform** discovery tool + assessment + reports |
| 63 | TCO assessment | **Migration Evaluator** (ADS = dependencies, not TCO) |
| 49 | Many small intermittent apps, cheapest | **ECS on EC2 cluster** (bin-packing); RIs at max capacity = waste |
| 55 | "serverless" in question | **Serverless variants**: Aurora Serverless, Redshift Serverless, EventBridge |
| 74 | SMTP app → SES | **SES SMTP credentials** (not IAM role) + **port 587 STARTTLS** |

### E. Serverless + DB (4)
| Q | Correct | Lesson |
|---|---|---|
| 5 | **RDS Proxy + SQS queue per Lambda** | SNS retries don't reduce DB load |
| 58 | **DB connection init outside handler + RDS Proxy** | API GW settings irrelevant to DB connections |
| 30 | `DB_HOST` = cluster endpoint, **DB SG inbound from Fargate:3306**, secret via `ValueFrom` | SG direction: destination allows inbound |
| 13 | Aurora Auto Scaling = **read replicas only** + **ALB** sticky sessions | Writer can't autoscale; NLB = no HTTP |

### F. Networking / S3 / perf (7)
| Q | Correct | Lesson |
|---|---|---|
| 12 🔁 | **CRR to us-east-1 + Lambda@Edge origin switch** | GA can't front S3; S3TA doesn't move data |
| 22 🔁 | **Prefix-filtered replication rule + S3 RTC** | S3TA ≠ replication speed |
| 23 🔁 | **Gateway endpoint + access point + bucket policy `s3:DataAccessPointArn`** | NAT = internet path |
| 69 | PrivateLink endpoint service → **NLB** | ALB can't back an endpoint service |
| 21 | Known release times → **scheduled scaling**; S3 via NAT → **gateway endpoint** | Predictive = learned patterns |
| 15 | **Separate ECS services + CloudFront Functions JWT routing** | API GW + Lambda authorizer adds latency |
| 48 | Audit copy of old OpenSearch data → **Glacier Deep Archive** | IA costs more for rarely-read data |

🔁 = repeat of a weak area already logged in chapter drills (storage #5, #10, #14).

## Multi-select lesson
13/16 wrong multi-selects had ≥1 correct pick; the other pick was usually a mismatched tool (Config for patching Q28, Security Hub/Inspector for tags Q31, CloudWatch agent for discovery Q33, EC2+SQS vs containers Q35, snapshot vs clone Q36, self-managed StackSets Q38).
**Rule:** once one pick is clearly right, the next pick must complete the SAME solution. Evaluate each option independently true/false.

## 10 rules to memorize
1. "Least operational overhead" → purpose-built managed service
2. RTO < ~1h → warm replica + auto-promote; never snapshot restore
3. Closest + failover → latency record + Evaluate Target Health
4. Cross-account sharing → RAM (enabled with Organizations)
5. Protect specific resources → SCP + `aws:ResourceTag` condition
6. Org-wide deploy → StackSets service-managed + auto-deploy
7. Lambda overwhelming RDS → RDS Proxy + init outside handler + SQS buffer
8. PrivateLink needs NLB; Global Accelerator never fronts S3
9. Migration: TCO = Migration Evaluator; discovery = AWS Transform / ADS; lift VM as-is = VM Import
10. Security groups: destination allows inbound from source

## Next actions
- Redo 44 wrong Qs from `TD_SAP_Timed_Set5_Full.md` without answers (Groups A+B first); re-redo 🔁 Qs after 3–4 days
- Study migrations chapter (Group D = mostly unstudied services)
