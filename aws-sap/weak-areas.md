# SAP-C02 Weak Areas — ranked, with confusion pairs

Built 2026-10-13 from the wrong-answer notes of TD5, TD1, TD2, TD3, TD6 and Udemy #2/#3 unseen (165 misses). Validated + TD6 added 2026-10-13.
Companion files: `rule-sheet.md` (1-line rules), `new-solutions-flashcards.md` (Domain 2 self-test).
Ranking = repeat misses first, then miss count, then the sprint day it's scheduled for.

## Priority map

| # | Area | Evidence | Wrong belief behind it | Sprint day |
|---|---|---|---|---|
| 1 | **Reading: overbuild / DIY** | TD5 12 · TD3 9 · TD6 3/5 misses · repeats on new questions | "More robust = better" — but the stem asked for quick / cheap / least ops | every test |
| 2 | **Identity & org governance** | TD2 Org Complexity 25% · TD5 9 · TD6 Q6/Q15 (Continuous Improvement 2/5) | SCP can grant; WebIdentity works for SAML; the role lives in the caller's account | 10-14 marathon |
| 3 | **Edge & DNS** (Route 53 / CloudFront / GA) | 🔁 GA→S3, 🔁 origin group, TD3 4, Udemy 4 | GA and Route 53 are interchangeable; any cert works on CloudFront | **10-15** |
| 4 | **Streaming & analytics** (Kinesis / EMR / Redshift) | Udemy2 Kinesis ×3 · EMR ×2 · Redshift grant ×2 (drill) | SQS/Firehose can fan out; RIs are always cheapest | **10-17** |
| 5 | **Migration + DR** | TD5 Migration 27.8% · Snow ×2 · tape/file GW ×3 · DR tier ×3 | Any replication = DR; Tape GW can feed ML | **10-19** |
| 6 | **Hybrid networking** | Public VIF ×4 · PrivateLink NLB 🔁 · GWLB 🔁 · S3 endpoint 🔁 | Private VIF carries VPN; ALB backs PrivateLink | 10-14 marathon |
| 7 | **Ops: patching, ASG, compliance** | TD1 patching ×3 · Udemy2 ×2 · TD3 ×2 | Config patches things; blocking = detecting | 10-21 marathon 2 |
| 8 | **Multi-select** | TD5 5/21 · TD3 all 7 misses had 1 correct pick | Second pick can be any true statement | every test |

## 1. Reading discipline (fix this first — it shows up in every domain)

Before picking, write the **constraint word** on the whiteboard. Then eliminate:

| Stem says | Eliminate | Your past misses |
|---|---|---|
| least operational overhead | anything you'd run on EC2 / your own scripts / custom Lambda pipelines | Glue, MediaConvert, Transfer Family, Patch Manager, Service Catalog, IoT Core, Batch (TD5, TD1, TD3) |
| most cost-effective | new paid services stacked on top; Reserved for short jobs; hot standby; always-on clusters for a nightly window | API GW cache vs CloudFront+DAX (TD1 Q64), EMR RI (TD3 Q20/29), hot standby (TD3 Q16), Redshift vs Athena (TD6 Q1), Compute SP for MemoryDB (TD6 Q16) |
| least overhead **and** cost (edge) | Lambda@Edge for simple rewrites | CloudFront Functions (TD6 Q11) |
| quickly / weeks / short deadline | full migration, re-architecture, new DB engine | CloudFront custom origin (TD3 Q42), ElastiCache vs Aurora (TD3 Q30) |
| minimal changes / no code changes | refactor, DynamoDB/Aurora rewrite, Fargate re-architect | replatform EC2 vs Fargate (Udemy3 Q16) |
| detect / don't block developers | SCP / IAM deny | Config `approved-amis-by-id` (TD1 Q12, TD3 Q60) 🔁 |
| prevent / **enforce** | Config, GuardDuty, Inspector (they only report) | SCP + `aws:ResourceTag` (TD5 Q19), tag policy + SCP on `CreateStack` (TD6 Q15) |

**Multi-select:** after choosing pick 1, ask "*what's still missing for this exact solution?*" — pick 2 must answer that. Reject options with one wrong clause (TD1 Q26: "Multi-AZ RDS in one AZ").

## 2. Identity & org governance — confusion pairs

| You picked | Correct | Tell |
|---|---|---|
| `AssumeRoleWithWebIdentity` for corporate SSO | `AssumeRoleWithSAML` / Identity Center | **SAML** IdP = corporate; Google/Facebook = web identity 🔁 |
| SAML for social login | Cognito / web identity federation | mobile, SPA, "millions of users" |
| Role in the management account | Role in the **target** account, trusting the caller | "access Dev from mgmt" → role lives in Dev |
| "SCP that allows" | IAM policy (grants) + SCP (limits) | an SCP never grants anything 🔁 |
| IAM deny in every account | SCP at the OU | "all accounts", "central" |
| Move SCP deny to … root | Attach at the **Production OU** + onboarding OU | deny at root hits every OU |
| Cost allocation tag in member account | Activate in the **management account** + CUR | 🔁 TD5 Q29 |
| RAM can generate CUR | CUR from mgmt account → QuickSight | TD5 Q16 |
| Parameter Store for rotation | Secrets Manager | "rotation" / "lifecycle" 🔁 |
| Role ARN in Parameter Store for EC2 | Instance profile alone | nothing else is needed |
| AdministratorAccess for devs | PowerUserAccess | "everything except IAM" |
| KMS on CloudTrail = tamper-proof | Log file validation + MFA Delete | KMS = confidentiality |
| Config + automation to enforce tag values | **Tag policy** + SCP deny create without `aws:RequestTag` | "enforce" at creation (TD6 Q15) |
| IAM to exclude functions from Inspector | `InspectorCodeExclusion` tag + standard **and** code scan | TD6 Q6 |

**Re-watch:** Maarek *Identity & Federation* (your lowest drill: 53%) — STS APIs, Identity Center, Cognito. *SCP evaluation* slide.

## 3. Edge & DNS (10-15) — confusion pairs

| You picked | Correct | Tell |
|---|---|---|
| Global Accelerator for S3 | S3 CRR + CloudFront / Lambda@Edge | GA endpoints = ALB, NLB, EC2, EIP only 🔁 |
| Multi-Region + latency routing for 504s | CloudFront **origin group** failover | "minimal cost" 🔁 |
| Route 53 weighted for a fast shift | GA traffic dials / endpoint weights | "DNS caching", "clients ignore TTL" |
| NLB for user→instance pinning | GA **custom routing** | "deterministic", "specific instance" |
| Route 53 health check on a private IP | CloudWatch alarm → health check on the alarm | private hosted zone resources |
| NS delegation for a cross-account PHZ | VPC association authorization (CLI) | 🔁 TD1 Q27 |
| Default cert on a custom domain | ACM cert in **us-east-1** | default = `*.cloudfront.net` only |
| Wildcard for many domains | SNI, multiple certs on the listener | wildcard = one domain's sub-domains |
| ALB path condition for sub-domains | ALB **host** condition | `*.example.com` + apex |
| Lambda@Edge for query-string normalization | **CloudFront Functions** | "least overhead and cost" 🔁 overbuild (TD6 Q11) |
| All CloudFront traffic via the regional edge cache | PUT/POST/PATCH/DELETE/OPTIONS + all-header dynamic skip it | Udemy2 Q21 |
| Route 53 geolocation blocks countries | CloudFront geo restriction / WAF geo match | geolocation only routes |

**Routing policy card:** failover = active-passive · latency + Evaluate Target Health = active-active · weighted = % split / testing · geolocation = by user location · geoproximity = bias · multivalue = DNS LB with health checks · alias at the apex.
**Do:** Maarek *Route 53* + *CloudFront* + *Global Accelerator* sections; re-run TD1 Q17, TD5 Q12/Q42, Udemy2 Q20, Udemy3 Q21/Q26 from the review files.

## 4. Streaming & analytics (10-17) — confusion pairs

| You picked | Correct | Tell |
|---|---|---|
| SQS for many readers | Kinesis Data Streams | "same record", "replay", "multiple apps" |
| Firehose for consumer apps | KDS + **Enhanced Fan-Out** | "consumers lagging" |
| Producers keep calling Firehose PutRecord | Write to the KDS (it's the Firehose source) | KDS as source disables direct PutRecord |
| Step Functions per data point | IoT rule → Firehose + Lambda transform | "minutes of latency OK" |
| S3 + SQS for near-real-time | KDS + consumers → Redshift | "near-real-time analytics" |
| Reserved for a one-off EMR job | On-Demand master/core + **Spot task** | 🔁 TD3 Q20/Q29 |
| Lambda → SQS → Fargate ETL | Glue crawler + ETL job | "extend with new fields" |
| Encrypted Redshift snapshot copy w/o grant | **Snapshot copy grant** in the destination Region | 🔁 drill ×2 |
| KCL to produce | KPL produces, KCL consumes | |
| Redshift for queries 6 PM–2 AM on ORC | **S3 + Athena + Glue Catalog** | pay per scan, no idle cluster (TD6 Q1) |
| Compute SP covers MemoryDB | EC2 Instance SP + Compute SP + **reserved nodes** for DB/cache | TD6 Q16 |

**Kinesis card:** KDS = real-time, shards, custom consumers, replay (24 h–365 d) · Firehose = near-real-time delivery to S3/Redshift/OpenSearch/HTTP, Lambda transform, no replay · MSF (Managed Flink) = SQL/Flink on streams · Redshift streaming ingestion can also read KDS/MSK directly.
**EMR card:** master + core = On-Demand (core holds HDFS data) · task = Spot · long-running steady → RI/Savings Plans.
**Do:** Maarek *Data Engineering* (Kinesis, EMR, Redshift); TD Dojo drill only from TD1/2/5 pool (not TD4/TD6).

## 5. Migration + DR (10-19) — confusion pairs

| You picked | Correct | Tell |
|---|---|---|
| Tape Gateway → Glacier for ML on video | **File Gateway** → S3 + Rekognition | "process / tag the content" 🔁×3 |
| File Gateway for Windows servers in AWS | **FSx for Windows + DataSync** | servers are **in AWS** 🔁 |
| SSM + Image Builder for "keep the VM" | **VM Import/Export** | "as-is" |
| Scheduled VM Import scripts | **MGN** | "continuous replication", "short cutover" |
| Application Discovery Service for TCO | **Migration Evaluator** | "business case", "TCO" |
| CloudWatch agent for discovery | ADS / **AWS Transform** discovery | "dependencies", "inventory" |
| Snowmobile for < 10 PB / network for 200 TB | Snowball Edge ×N | do the math: 1 Gbps ≈ 10.8 TB/day · Snowmobile retired 2024 |
| Snowball straight to Glacier | Snow → S3 → lifecycle rule | |
| Hot standby for RTO 30 min | Backup/restore + cross-Region read replica | 🔁 TD3 Q16 |
| Multi-AZ as DR | Cross-Region backup / replica | Multi-AZ = HA only 🔁 |
| Pilot light for RTO 5 min | Warm standby | pilot light must still build tiers |
| Glacier backups every 15 min | S3 hourly backups + 5-min transaction logs | Glacier retrieval breaks RTO |

**DR ladder:** backup/restore (hours) → pilot light (core DB running, tens of min) → warm standby (scaled-down full stack, minutes) → multi-site (~0). RPO < 1 s → Aurora Global; active-active NoSQL → DynamoDB global tables.
**Migration tool card:** discover = ADS / Transform · TCO = Migration Evaluator · track = Migration Hub · servers = MGN · VM as-is = VM Import · DB = SCT + DMS (CDC) · files = DataSync · offline = Snowball.
**Do:** Maarek *Migrations* (never drilled — 0 questions answered) + DR slides.

## 6. Hybrid networking — confusion pairs

| You picked | Correct | Tell |
|---|---|---|
| Private VIF for VPN-over-DX | **Public VIF** (or transit VIF + TGW) | 🔁×4 |
| Second DX for "cheapest backup" | Site-to-Site VPN | "cheapest" vs "max resilience" |
| One private VIF to 2 Regions | DX Gateway | |
| Second VGW for VPN HA | Second **CGW** | one VGW per VPC |
| ALB for an endpoint service | **NLB** / GWLB | 🔁 TD5 Q69 |
| DX for appliance scaling | **GWLB + ASG** | 🔁 TD5 Q62 |
| NAT for S3 traffic | **Gateway endpoint** | 🔁 TD5 Q21 |
| Single gateway endpoint for ECR | ecr.api + ecr.dkr interface + S3 gateway | private Fargate image pull |
| Flow Logs for packet payloads | **Traffic Mirroring** | 🔁 TD3 Q45, Udemy3 Q14 |
| SG/NACL for URL filtering | Proxy / Network Firewall | domain-based egress |

## 7. Ops — patching, ASG, compliance

| You picked | Correct | Tell |
|---|---|---|
| Config for patching | **Patch Manager** + Maintenance Windows (`AWS-RunPatchBaseline`) | Config = compliance only |
| One patch group + cron | 2+ patch groups (tags) + non-overlapping windows | "staggered" |
| Tag by OS only | Tag by environment + OS | "exclude prod" |
| Verbose logging to debug | Suspend ASG **Terminate** / standby | 🔁 TD1 Q73 |
| ASG terminates + launches in one step | Unhealthy: terminate first · rebalance: launch first | Udemy2 Q27 |
| Config for CVEs | **Inspector** + EventBridge schedule | |
| `.pem` pushed to authorized_keys | Extract the **public** key, push via Run Command | TD5 Q51 |

## 8. Repeat-miss marathon list (10-14 round 1, 10-21 round 2)

Redo these from the review files, every answer justified out loud:
- TD5: Q10, Q12, Q21, Q22, Q23, Q29, Q32, Q48, Q62, Q69
- TD1: Q17, Q25, Q26, Q57, Q69, Q74
- TD3: Q6, Q10, Q14, Q63, Q71
- TD6: Q1, Q11, Q16 (overbuild 🔁), Q6, Q15 — Pass 1 not done yet
- Udemy2 unseen Pass 1 misses (14) · Udemy3 unseen misses (8, Pass 1 not done yet)
