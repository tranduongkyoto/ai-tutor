# SAP-C02 Weak Areas — ranked, with confusion pairs

Built 2026-10-13 from the wrong-answer notes of TD5, TD1, TD2, TD3, TD6 and Udemy #2/#3 unseen (165 misses). Validated + TD6 added 2026-10-13.
Updated 2026-10-30 with TD4, Neal A/B/C, Udemy #2 full, Official exam (118 misses) — final review for the exam on 2026-11-02.
Companion files: `rule-sheet.md` (1-line rules), `new-solutions-flashcards.md` (Domain 2 self-test).
HTML view: `weak-areas.html` (search + self-test + pair drill); rebuild after editing this file: `python3 aws-sap/build_study_pages.py`.
Ranking (10-30) = what cost points in the last 6 tests first (Continuous Improvement, twin options, overbuild, answer switching), then repeat misses, then miss count.

## Priority map

| # | Area | Evidence | Wrong belief behind it | Sprint day |
|---|---|---|---|---|
| 1 | **Continuous Improvement** — security / reliability / cost fixes on existing systems | Official CI 10/20 (**50%, Needs Improvement**: security 2/5, cost 2/5, reliability 1/3) · Neal C CI 7/13 (54%) · TD4 CI 56% | Add more (Multi-AZ, DAX, multi-Region, scaling) and it gets fixed — but the stem wants the one control that removes the failure, at the stated SLA and cost | **10-31** (§9) |
| 2 | **Twin options** | Official 14/28 misses (Archive vs Deep Archive, DLM vs AWS Backup, Volume vs File Gateway, Budgets action vs operator, Fargate vs custom AMI…) | Both look right, pick by feel — find the one differing phrase and test it against the stem | **10-31** + exam-day |
| 3 | **Reading: overbuild / DIY** | Neal C Q5/Q7/Q13 🔁 · Neal B Q61/Q63 🔁 · Official Q19 · TD5 12 · TD3 9 · TD6 3/5 | "More robust = better" — but the stem asked for quick / cheap / least ops / the stated SLA | exam-day |
| 4 | **Answer switching** | Neal C Q5/Q30 (right on first pick, then changed) · Udemy2 Q11/Q67 (broken in review) · Neal C in-pass changes 5 fixed / 2 broken | A second look is better — change only when you find new evidence in the stem | exam-day |
| 5 | **Identity & org governance** | Official ORG 56% (multi-account 1/4), governance misses Q13 Q26 Q57 Q62 Q64 Q65 · Neal B ORG 57% 🔁 Q23 Q56 Q71 · TD2 Org 25% | SCP can grant; one account for everything security; detect = prevent | **10-31** |
| 6 | **Migration + DR / resilience** | Official resilience 0/2 (Q25 Q45 Q61) · Neal B Q61/Q63 🔁 · TD4 Q28/Q64 🔁 · Neal B Q10 🔁 | Multi-Region / global DB is safer; replicas are backups | **11-01** |
| 7 | **Hybrid networking** | Neal C Q9 Q30 🔁 Q31 · Udemy2 Q67/Q68 🔁 · Public VIF ×4 (earlier) | Interface endpoints use routes; a new DX in another Region = redundancy | **11-01** |
| 8 | **Edge & DNS** (Route 53 / CloudFront / GA) | Official Q16 Q38 · Neal B Q22 🔁 · Neal A Q41 🔁 · Udemy2 Q13 🔁 | WAF = DDoS baseline; Evaluate Target Health sees partial failures | **11-01** |
| 9 | **Ops: scaling, deployment, detection** | Official Q17 Q30 Q60 (deployment task 0/3) · Udemy2 Q24/Q63 🔁 | Scale on queue depth / schedule; S3 events can filter by ACL | **10-31** |
| 10 | **Streaming & analytics** | Udemy2 Q54 🔁 · Official Q68 · Neal C Q7 🔁 (DAX) | Firehose writes to DynamoDB; Savings Plans cover DynamoDB | 11-01 (light) |
| 11 | **Multi-select** | Neal C 4/7 (3 half-right) · TD4 9/16 · Neal A 12/21 · Udemy2 Select THREE 3/6 | Second pick can be any true statement | exam-day |

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
**Twin options:** underline the one phrase that differs (Archive vs Deep Archive, DLM vs AWS Backup, Volume vs File Gateway), then test only that phrase against the stem's constraint (Official 14/28).
**Answer switching:** change an answer only when you can name the stem word that proves the first pick wrong (Neal C Q5/Q30, Udemy2 Q11/Q67 were right first).

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
| Organizations backup policy using Data Lifecycle Manager | Organizations **backup policy** → AWS Backup plans in every account | DLM = per-account EBS/AMI lifecycle; twin option (Official Q13) |
| StackSets + drift detection to keep Config rules unchanged | **Organization conformance pack** (excluded accounts) via delegated admin | drift detection only detects (Official Q26) |
| AWS Managed Microsoft AD + trust for WorkSpaces | **AD Connector** | "credentials must not be stored outside the company" (Official Q32) |
| One central security account for logging, tooling and audit | Separate **Log Archive**, **Security Tooling**, **Audit** accounts + Exceptions OU | limit blast radius (Official Q57) |
| CloudTrail data events to find external principals | **IAM Access Analyzer**, organization as zone of trust | "who CAN access", not who called (Official Q62) |
| Firewall Manager strict order: allow rule at the highest order number | Trusted-CIDR allow at the **lowest** number, deny-all after | lowest priority number is evaluated first (Official Q64) |
| Remove accounts from the org and re-invite | Nest the stricter OU under the shared OU, **move** accounts between OUs | SCPs inherit down the tree (Official Q65) |
| Allow-list SCP for many blocked services + exceptions | **Deny-list** SCP, keep FullAWSAccess, exceptions OU with fewer denies | allow list = every action listed 🔁 (Neal B Q23) |
| IAM users in each account + SCPs | Users in one **identity account**, roles in target accounts trusting it | SCPs never grant 🔁 (Neal B Q56) |
| Manual accounts + per-account SAML | **Control Tower** + Account Factory + Identity Center | "minimal overhead" governance 🔁 (Neal B Q71) |

**Re-watch:** Maarek *Identity & Federation* (your lowest drill: 53%) — STS APIs, Identity Center, Cognito. *SCP evaluation* slide.

## 3. Edge & DNS — confusion pairs

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
| Route 53 Evaluate Target Health for partial failures | Route 53 **Application Recovery Controller** routing controls (alarms + Lambda) | "full AND partial failures" (Official Q16) |
| CloudFront path behaviors + redirects for A/B test | **Lambda@Edge** (origin request) picks the origin | "users must not notice" (Official Q38) |
| WAF web ACL for baseline DDoS | **CloudFront** (Shield Standard included) | WAF = L7 rules (SQLi/XSS) 🔁 (Neal B Q22) |
| CloudFront + WAF per-day rate rule for a few known clients | WAF **IP allow-list** on the API + usage plan + API key | rate rules use short windows, CloudFront adds cost 🔁 (Neal A Q41) |

**Routing policy card:** failover = active-passive · latency + Evaluate Target Health = active-active · weighted = % split / testing · geolocation = by user location · geoproximity = bias · multivalue = DNS LB with health checks · alias at the apex.
**Do:** Maarek *Route 53* + *CloudFront* + *Global Accelerator* sections; re-run TD1 Q17, TD5 Q12/Q42, Udemy2 Q20, Udemy3 Q21/Q26 from the review files.

## 4. Streaming & analytics — confusion pairs

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
| Firehose writes sensor data to DynamoDB | **SQS + Lambda** (DynamoDB auto scaling) | DynamoDB is not a Firehose destination 🔁 (Udemy2 Q54) |
| DAX + Savings Plans for DynamoDB hot keys | DAX + **provisioned capacity** + auto scaling (or reserved capacity) | Savings Plans don't cover DynamoDB (Official Q68) |

**Kinesis card:** KDS = real-time, shards, custom consumers, replay (24 h–365 d) · Firehose = near-real-time delivery to S3/Redshift/OpenSearch/HTTP, Lambda transform, no replay · MSF (Managed Flink) = SQL/Flink on streams · Redshift streaming ingestion can also read KDS/MSK directly.
**EMR card:** master + core = On-Demand (core holds HDFS data) · task = Spot · long-running steady → RI/Savings Plans.
**Do:** Maarek *Data Engineering* (Kinesis, EMR, Redshift); TD Dojo drill only from TD1/2/5 pool (not TD4/TD6).

## 5. Migration + DR — confusion pairs

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
| Volume Gateway for shared on-prem files → S3 | **S3 File Gateway** (NFS/SMB) | Volume = iSCSI block; twin option (Official Q61) |
| AWS Backup + RDS cross-Region read replicas | **AWS Backup** plan + vault copy in another Region | replicas are not backups (Official Q25) |
| Aurora Global: read from secondary, write to primary | **Write forwarding** on the secondary; test with managed failover | "read-after-write" (Official Q45) |
| Snowball for 25 TB on a 1 Gbps link | **S3 Transfer Acceleration** over the fastest link | do the math: ~2–3 days online 🔁 (Neal B Q10, key debatable) |
| Two Regions + Aurora Global for 99.9% | **One Region, Multi-AZ** + CloudFront for global latency | match the stated SLA 🔁 (Neal B Q61) |
| Aurora Global database for three-AZ HA | Aurora cluster + **replicas in other AZs** | Global = cross-Region DR 🔁 (Neal B Q63) |
| Redis cache + RDS MySQL read replicas for faster failover | **RDS Proxy** + Aurora with Aurora Replicas | caches don't queue writes 🔁 (TD4 Q28) |
| Redshift replication to a secondary-Region cluster | Automated snapshots + **cross-Region snapshot copy** | Redshift has no cross-Region replication 🔁 (TD4 Q64) |

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
| Route table entry to fix an interface endpoint | Endpoint **ENI security group** allows 443 from the VPC + private DNS | routes = gateway endpoints only (Neal C Q9) |
| EC2 SG allows the NLB subnets (instance-id targets) | EC2 SG allows the **client CIDRs** | instance-id targets keep the client IP; first pick was right 🔁 (Neal C Q30) |
| New DX to the second Region for redundancy | **Second DX** at the same location + DX gateway for the other Region | redundancy = same path doubled (Neal C Q31) |
| DX + VPN backup for HA, high bandwidth, multi-Region | **Redundant DX** at each DC from different providers | VPN = low bandwidth; first pick was right (Udemy2 Q67) |
| S3 gateway endpoint over the private VIF | **Public VIF** on the existing DX | gateway endpoint not reachable from on-prem 🔁 (Udemy2 Q68) |

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
| Scheduled scaling for unexpected peaks | **Target tracking** on `ALBRequestCountPerTarget` | "no correlation with time" (Official Q17) |
| Scale SQS workers on `ApproximateNumberOfMessagesVisible` | Target tracking on **backlog per instance** (custom metric) | queue depth ignores fleet size; twin option (Official Q60) |
| CloudFormation for infra, manual runbook for install | CloudFormation + **user data / cfn-init** | automate the whole runbook (Official Q30) |
| Enable ENA for grid timeouts | **Cluster placement group** | ENA already on; latency is node-to-node (Official Q58) |
| API Gateway execution logging for 504 root cause | **X-Ray** + Lambda CloudWatch Logs | logs confirm the error, X-Ray shows the hop 🔁 (Udemy2 Q24) |
| S3 event notifications to detect public-read objects | **CloudTrail data events** + EventBridge rule → SNS/Lambda | events can't filter by ACL 🔁 (Udemy2 Q63) |

## 8. Final-2-days list (10-31 → 11-01) — 🔁 repeats from recent tests

Redo these from the review files (shuffled letters, every answer justified out loud; for twins, say the one differing phrase):
- Official — `practice-exam/sap/official_attempt1_review.md`: twin options Q9, Q13, Q30, Q38, Q43, Q45, Q54, Q60, Q61, Q64, Q65, Q66, Q68, Q74 · governance Q26, Q57, Q62 (no 🔁 marks — first attempt; CI is the weakest domain)
- Neal C — `practice-exam/sap/neal_c_review.md`: 🔁 Q5, Q7, Q13 · first pick right then changed Q5, Q30 · security control Q9, Q12, Q19
- Neal B — `practice-exam/sap/neal_b_review.md`: 🔁 Q10, Q22, Q23, Q28, Q56, Q61, Q63, Q71, Q74
- Neal A — `practice-exam/sap/neal_a_review.md`: 🔁 Q11, Q13, Q32, Q34, Q41
- TD4 — `practice-exam/sap/td4_review.md`: 🔁 Q5, Q28, Q58, Q64
- Udemy #2 full — `practice-exam/sap/udemy2_full_review.md`: 🔁 Q13, Q24, Q33, Q54, Q63, Q68 · broken in review Q11, Q67

## 9. Continuous Improvement — recent misses (Official, Neal C)

Security, reliability and cost fixes on an existing system. Official CI 10/20 (50%), Neal C CI 7/13 (54%).

| You picked | Correct | Tell |
|---|---|---|
| Intelligent-Tiering Deep Archive Access for 6-hour retrieval | **Archive Access** tier | Deep Archive ≤ 12 h breaks the SLA; twin option (Official Q9) |
| DynamoDB global tables to raise multi-AZ resilience | **One NAT gateway per AZ** | find the one zonal resource (Official Q19) |
| Copy objects to a new encrypted bucket | Default encryption + S3 Inventory + **Batch Operations** copy in place | every app would change bucket names (Official Q43) |
| Client VPN to stop SSH brute force | **Session Manager** (close port 22, log sessions) | "log commands", "keep port forwarding" (Official Q53) |
| AWS Batch on Fargate Spot with a custom AMI | Managed **EC2** compute environment with Spot | Fargate has no custom AMI; twin option (Official Q54) |
| Budgets alert to an operator who stops instances | Budgets forecast alert + **Budgets action** | "lowest risk of overspending" (Official Q66) |
| KMS with scheduled disable/enable for FIPS 140-2 Level 3 | **CloudHSM** cluster (delete/restore from backup off-hours) | exam rule: Level 3 = CloudHSM (real AWS: KMS HSMs Level 3 since 2023) (Official Q70) |
| Elastic Beanstalk + DynamoDB for a simple LAMP app | **Lightsail** | "predictable pricing", "little AWS expertise" (Official Q73) |
| Enable Object Lock on the existing bucket | **New bucket** with Object Lock compliance mode, move objects | exam key (real AWS: existing buckets allowed since 2023) (Official Q74) |
| RDS Multi-AZ + ElastiCache for 99.5% + slow remote desktop client | RDS single-AZ + **AppStream 2.0** | match the SLA; first pick was right 🔁 (Neal C Q5) |
| On-demand + DAX for a write-heavy dev table | **On-demand** capacity alone | DAX caches reads only 🔁 (Neal C Q7) |
| Cluster Autoscaler under-provisioned for EKS resilience | **Topology spread** across AZs + multi-AZ node groups | resilience = survive an AZ failure (Neal C Q11) |
| `aws:SecureTransport` in S3 ACLs | **Bucket policy** denying unencrypted PutObject + default encryption + CloudFront HTTPS redirect | conditions live in bucket policies, never ACLs (Neal C Q12) |
| Auto scaling + DAX to stop web attacks | CloudFront + **WAF** + custom-header origin lock on the ALB | scaling treats symptoms 🔁 (Neal C Q13) |
| SSE-S3 with a customer managed key | **SSE-KMS** with a customer managed key + deny unencrypted PutObject | SSE-S3 never uses your key (Neal C Q19) |
| Custom budgets for cost per project/environment | **Cost allocation tags** + Service Catalog portfolios | budgets alert, they don't attribute (Neal C Q20) |
| CloudTrail data events + billing alarm for team cost | **AWS Budgets** (in CloudFormation) + Service Catalog products | CloudTrail logs API calls, not cost 🔁 (Neal A Q13) |
| Cost Explorer RI utilization report for a 70% target | AWS Budgets **RI coverage** budget | utilization ≠ coverage; Cost Explorer doesn't alert 🔁 (Neal A Q32) |
| AWS Budgets for 80% service-quota alerts | Trusted Advisor check + Lambda → **SNS** (or CloudWatch `AWS/Usage` alarm) | Budgets tracks spend, not quotas 🔁 (Neal B Q74) |
| EFS for +3,000 IOPS on gp2 | **Grow the gp2 volume** (+1 TB = +3,000 IOPS) or gp3 | 3 IOPS/GiB; first pick was right (Udemy2 Q11) |

## Pair drill log (`weak-areas.html` → Pair drill)

| Round | Date | Score | Weakest sections | ❌ pairs |
|---|---|---|---|---|
| 1 | 2026-10-13 | 55/66 (83%) | Hybrid networking 7/10 · Migration + DR 9/12 | Redshift snapshot copy grant 🔁 · warm standby for RTO 5 min · DX Gateway for 2 Regions · CloudFront/WAF geo block · NLB/GWLB endpoint service 🔁 · instance profile alone · ECR endpoints (api + dkr + S3 gateway) · PHZ association authorization 🔁 · AssumeRoleWithSAML 🔁 · Snowball Edge ×N · backup/restore for RTO 30 min 🔁 |
| 2 (due 10-31) | | | | |
