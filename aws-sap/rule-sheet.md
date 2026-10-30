# SAP-C02 Rule Sheet (1 page)

Built 2026-10-13 from 376 per-question rules: TD1, TD2, TD3, TD5, TD6 + Udemy #2/#3 unseen; TD4 (Gate 2) rules added 2026-10-19; updated 2026-10-30 with Official practice exam (783), Neal A/B/C, Udemy #2 full and TD1–TD5 retakes (`practice-exam/sap/*_review_notes.json`). Validated 2026-10-13 (see § Corrections).
🔁 = missed 2+ times. Format: **trigger in the stem → answer** (✗ = the trap you picked).
HTML view: `rule-sheet.html` (search + self-test); rebuild after editing this file: `python3 aws-sap/build_study_pages.py`. Drill: `rule-sheet-flashcards.html` (193 two-option cards, deck `decks/rule-sheet-deck.json`).

## 0. Read the stem first (10 meta-rules behind most repeat misses)
1. **Find the constraint word** — *least overhead · most cost-effective · quickest · minimal changes · no code changes*. It picks between 2 working options.
2. **Managed service > DIY.** Lambda/SQS/EC2 pipeline when Glue, MediaConvert, Transfer Family, Patch Manager, Service Catalog, IoT Core or Batch exists → ✗.
3. **Don't overbuild.** One-off / short deadline / "quick" → no RIs, no full migration, no hot standby. Match the DR tier to the RTO. Pick the **lightest feature** that works: Athena > Redshift for a nightly window, CloudFront Functions > Lambda@Edge for rewrites. 🔁×3 (TD3, Udemy3, TD6)
4. **Detect ≠ prevent.** "Don't block developers" / "detect" → Config rule + remediation. "Prevent" / "**enforce**" / "block" → SCP / IAM deny (+ tag policy). 🔁
5. **Multi-select:** both picks must complete the **same** solution; after the sure pick, test every other option against **each** stem requirement (TD4 7/7, Neal A 8/9 misses were half right). Kill any option with one wrong clause or an internal contradiction.
6. **"Serverless" in the stem** → Aurora Serverless, Redshift Serverless, Fargate, DynamoDB, EventBridge.
7. **Twin options:** when 2 options are almost word-for-word the same, find the ONE phrase that differs and judge only that (IA vs Deep Archive, public vs VPC endpoint, ALB vs NLB, which account). 🔁 (TD5 marathon 5/10; TD4 Q14 CodeDeploy clause, Q63 SQS→Step Functions, Q41 behavior vs ALB rule; Official 14/28 misses)
8. **First pick stands** on single-answer questions unless a stem phrase rules it out — review changes without new evidence broke right answers. 🔁 (Neal C Q5, Q30; Udemy2 Q11, Q67)
9. **Match the SLA, don't exceed it.** 99.5% → single-AZ is fine · 99.9% → Multi-AZ in one Region · "resilient across AZs" → fix the one zonal part (one NAT GW → one per AZ) ✗ multi-Region. Extra Multi-AZ/cache/DAX the stem never asked for = cost trap 🔁 (Official Q19, Neal C Q5/Q7, Neal B Q61/Q63)
10. **Automation beats a human step:** Budgets action, Secrets Manager rotation, user data/cfn-init, Session Manager ✗ "alert an operator who acts manually" (Official Q11, Q30, Q66)

## 1. Identity & governance
- Corporate **SAML** → Identity Center / `AssumeRoleWithSAML` ✗ WebIdentity 🔁 · **social/mobile/SPA** → Cognito / `AssumeRoleWithWebIdentity`, temp creds, never access keys 🔁
- **LDAP, no SAML** → custom identity broker → STS · **3rd party** → trust policy + `sts:ExternalId` · **GitHub CI** → IAM OIDC provider
- Cross-account role lives in the **TARGET** account; fix access = its **trust policy** → trust the caller's **role ARN**, not the account root (least privilege) · EC2 → AWS API = instance profile, nothing else
- **SCP never grants**; allow-list SCP must list every action; doesn't affect the mgmt account or service-linked roles 🔁 · team access = IAM policy
- Shared + stricter rules → **nest the stricter OU** under the shared one (SCPs inherit); move accounts between OUs ✗ leave/re-invite (Official Q65) · block **every present + future** member → Deny SCP at **root** (mgmt exempt) (Neal B Q59)
- Block a few services org-wide → **deny-list SCP** + keep FullAWSAccess (exceptions via separate OU) · management account: org tasks only, no workloads/users · central identities in one account, roles in target accounts · multi-account setup with least ops → **Control Tower + Account Factory** (Neal B)
- Deny at root hits every OU → attach at the OU · protect tagged resources → SCP deny + `aws:ResourceTag` · MFA ≠ authorization
- **Enforce tag values** → tag policy (allowed values) + SCP deny `CreateStack`/create without `aws:RequestTag` ✗ Config 🔁 · VPC-only access points → SCP + `s3:AccessPointNetworkOrigin` · org-only ECR/S3 → `aws:PrincipalOrgID`
- Central backups + retention + cross-Region copy + alerts → **AWS Backup** plan (copy action + SNS) ✗ DLM/Lambda glue 🔁 · enforce org-wide → **Organizations backup policy** (an AWS Backup feature ✗ DLM) (Official Q13) · AWS Backup already covers RDS ✗ add cross-Region read replicas (Official Q25)
- Org-wide Config rules members can't change, some accounts excluded → **organization conformance pack** via delegated admin ✗ StackSets + drift detection (detects only) (Official Q26)
- Who **CAN** access (policy analysis, outside the org) → **IAM Access Analyzer**, org = zone of trust ✗ CloudTrail (who DID call) (Official Q62)
- Existing Microsoft AD → **Directory Service** (Managed AD + trust) → SSO; don't recreate users in Identity Center · **nothing may be stored in AWS** → **AD Connector** (proxy) ✗ Managed AD (Official Q32)
- Mobile app, custom IdP → IAM role creds → OIDC + **Cognito identity pool** or SAML IdP in IAM ✗ API GW Lambda authorizer (no AWS creds) ✗ Identity Center (workforce) 🔁 (Neal B Q51, TD1 Q45)
- Rotation/lifecycle → **Secrets Manager** (ECS `secrets`/`valueFrom`; managed RDS rotation) ✗ Parameter Store (no native rotation) 🔁 (Official Q11) · CFN → `{{resolve:secretsmanager:…}}`
- Team isolation + per-team billing → **account per team** in Organizations + SCPs; security tooling in a **delegated security account**, never the management account (✗ security account as mgmt/payer) · OUs per environment + **separate Log Archive, Security Tooling, Audit** accounts + Exceptions OU ✗ one account for all three (Official Q57) · Org: RAM needs **trusted access** · StackSets **service-managed** + auto-deploy · org trail + Config aggregator + Security Hub delegated admin
- Cost by tag → activate tags in the **mgmt account** + CUR 🔁 · cost per project/env + only pre-approved services → **cost allocation tags + Service Catalog** ✗ budgets (alert only) (Neal C Q20) · org dashboard → CUR → QuickSight · alerts → Budgets · self-service → Service Catalog + launch constraint
- Alert on cost, RI/SP **coverage** or utilization → **AWS Budgets** (coverage/utilization budget) ✗ CloudWatch/CloudTrail 🔁 (Neal A Q13, Q32) · spend **spike vs historical pattern** → **Cost Anomaly Detection** (learns baseline) ✗ Budgets = static thresholds you set · admin access with no open ports → **Session Manager** + IAM (no bastion, no inbound SSH/RDP; logs sessions, port forwarding) ✗ Client VPN / VPN / EC2 Instance Connect (port 22 stays open) 🔁 (Official Q53, Neal A Q5/Q53)
- Forecasted overspend → Budgets alert + **Budgets action** (stop EC2/RDS, apply IAM/SCP) ✗ operator stops instances manually (Official Q66)
- Tamper-proof CloudTrail → log file validation + MFA Delete (KMS = confidentiality only)
- "Notify + auto-fix on an API call" (CreateUser…) → CloudTrail → **EventBridge rule** → Step Functions/Lambda remediate + SNS 🔁 (TD4 Q5) · zonal RIs share across consolidated-billing accounts only in the **same AZ + type**

## 2. Networking, DNS, edge
- IPsec VPN over DX → **PUBLIC VIF** 🔁×5 · cheapest DX backup → S2S VPN · one DX → many VPCs/Regions → **DX Gateway** + VGW per VPC (allowed prefixes ⊇ VPC CIDRs) 🔁×3 (TD1, TD5, TD4 Q58)
- VPN HA → 2nd **CGW** (VGW already has 2 tunnels; 1 VGW per VPC)
- Remote workstations → peered VPCs → **Client VPN** client + ONE endpoint in the main VPC (✗ new TGW) · UDP → **NLB** + NACL deny non-UDP (WAF/ALB = L7)
- PrivateLink service = **NLB**/GWLB, never ALB 🔁×5 · appliance fleet → **GWLB + ASG** 🔁 · central inspection → TGW + GWLB VPC · URL filter → proxy / Network Firewall
- S3 from private subnet → **gateway endpoint** ✗ NAT 🔁 · lock it down → endpoint policy + access point + bucket policy (`aws:sourceVpce`) 🔁
- Interface endpoint unreachable → endpoint **ENI security group** (443 from VPC) + private DNS ✗ route table entry (gateway endpoints only) (Neal C Q9)
- NLB with **instance-id** targets preserves client IP → EC2 SG allows **client CIDRs** ✗ NLB subnets; healthy targets = health check already open 🔁 (Neal C Q30)
- Network Firewall strict order: **lowest number first** → trusted-CIDR allow first, deny-all after (Official Q64)
- Packet contents → **Traffic Mirroring** ✗ Flow Logs 🔁 · block an IP → NACL deny · REJECT + source IP → Flow Logs
- Cross-account PHZ → `create-vpc-association-authorization` + `associate-vpc-with-hosted-zone` ✗ NS delegation 🔁 · Resolver **outbound** + forwarding rule = queries leaving the VPC (on-prem / custom AD domain) · inbound = into the VPC
- On-prem resolves a **private hosted zone** → Resolver **inbound** endpoint + PHZ associated with every VPC that needs it · most resilient hybrid link → 2nd DX at a different location/carrier (VPN = cheaper backup) 🔁 (Neal A Q56; Udemy2 Q67 many DCs → DX at each from diverse providers ✗ DX + VPN)
- DX **redundancy** → 2nd connection to the **same** Region; VPC in another Region → DX gateway ✗ new DX to that Region 🔁 (Neal C Q31) · on-prem → **S3** over DX → **public VIF** ✗ S3 gateway endpoint via private VIF (not reachable from on-prem) 🔁 (Udemy2 Q68)
- Private-IP health check → CloudWatch alarm → Route 53 health check on the alarm · PHZ resolution → `enableDnsSupport` + `enableDnsHostnames`
- Reroute on **partial** failures from many metrics → **Route 53 ARC** routing controls + alarms ✗ Evaluate Target Health (endpoint only) (Official Q16)
- R53: failover = active-passive · latency + Evaluate Target Health = active-active · geolocation doesn't block · apex → alias
- **DNS caching blocks a fast shift** → Global Accelerator dials/weights · user → specific instance → GA custom routing · **GA can't front S3 or CloudFront** (ALB/NLB/EC2/EIP only) → global uploads = **S3 Transfer Acceleration** + edge-optimized API GW 🔁 (Udemy2 Q13)
- CloudFront: custom domain → ACM in **us-east-1** · 504 → **origin group failover** 🔁 · custom origin → header + WAF on ALB · S3 → OAC · one client → signed URL/cookies
- One file / non-cookie client → **signed URL**; many files, keep URLs → **signed cookies** (OAC only locks S3 to CloudFront)
- Add S3 content to an ALB-origin distribution → new **S3 origin (OAC) + path-pattern behavior** (✗ ALB rule forwarding to S3)
- Invisible A/B between two S3 origins → **Lambda@Edge origin request** picks origin ✗ path behaviors/redirects (users see them) (Official Q38)
- Few known client IPs, low volume, Regional API → **WAF IP allow-list** on the API + usage plan/API key ✗ CloudFront + per-day rate rule (rate rules = short windows) 🔁 (Neal A Q41)
- Simple header/URL/query rewrite → **CloudFront Functions** ✗ Lambda@Edge (only for network calls, body access, longer runtime)
- Many domains on one ALB → **SNI** multi-cert (wildcard = one domain only) · route by hostname → ALB **host** condition · static IP for ALB → NLB in front · non-HTTP ports → NLB (ALB = HTTP/HTTPS only)

## 3. Security & data protection
- Own key + rotation → **SSE-KMS** (SSE-S3 never uses your key) 🔁 (Neal C Q19, TD3 Q56) · key from own HSM → KMS `Origin=EXTERNAL` · key never leaves + HA → CloudHSM ≥2 AZ · force TLS → `aws:SecureTransport`
- Stop public objects → Block Public Access · DDoS L3/L4 → Shield Advanced · SQLi/XSS → WAF · GuardDuty only detects
- Prevent web attacks → **CloudFront + WAF + origin lock** (custom header on ALB) ✗ scaling/caching 🔁 (Neal C Q13) · baseline DDoS → CloudFront (**Shield Standard**) ✗ WAF (Neal B Q22) · WAF attaches to CloudFront/ALB/API GW/AppSync/Cognito, **never EC2/ASG** (Udemy2 Q46)
- Conditions (`aws:SecureTransport`, deny unencrypted PutObject) live in **bucket policies, never ACLs**; at rest = default encryption + deny unencrypted PutObject; in transit = CloudFront HTTPS redirect (Neal C Q12)
- Encrypt existing objects in place → default encryption + **S3 Inventory + Batch Operations** ✗ copy to new bucket (apps change names) (Official Q43)
- FIPS 140-2 **Level 3** → **CloudHSM** (exam answer; real KMS got L3 in 2023); keys only office hours → delete/restore cluster from backup (Official Q70)
- WORM N years → Versioning + **Object Lock compliance** + default retention; exam key: **new bucket** + move objects (real AWS: existing buckets OK since 2023) (Official Q74)
- Detect an API parameter (public-read ACL) → **CloudTrail data events + EventBridge** → SNS/Lambda ✗ S3 event notifications (type + prefix/suffix only) 🔁 (Udemy2 Q63)
- Alert near a service quota → CloudWatch alarm on the **AWS/Usage** metric with `SERVICE_QUOTA()` math (✗ SampleCount) + SNS ✗ Budgets (cost, not quotas) 🔁 (Neal B Q74)
- PII → Macie · CVEs → Inspector · config drift → Config · who read what → CloudTrail data events · app → DB → SG-to-SG reference
- Inspector for Lambda = **standard scan** (CVEs in packages/layers) + **code scan** (code flaws) + `InspectorCodeExclusion` tag to skip functions (✗ IAM)

## 4. Compute, serverless, deployment
- VPC Lambda → **private subnets** + gateway endpoint/NAT (✗ public subnet: Lambda ENIs never get public IPs) · containers also on other clouds → **EKS** (✗ ECS = AWS-only) 🔁
- Job > 15 min → Fargate task (Lambda/EventBridge `RunTask`) or EC2 ASG on SQS depth · simple HTTPS for a function → Function URL
- Lambda floods RDS → **RDS Proxy** + connection outside the handler 🔁 · faster failover + keep connections → **RDS Proxy + Aurora replicas** 🔁 (TD4 Q28) · isolate a function → reserved concurrency · cut calls → API GW cache
- API GW + IAM principals → `AWS_IAM` (SigV4) + X-Ray (CORS isn't auth) · per-client quotas → usage plans + API keys
- Batch, least ops → **AWS Batch** + Spot + S3 🔁 · custom AMI → managed **EC2** compute env + Spot ✗ Fargate Spot (no custom AMI) (Official Q54)
- Tight HPC → cluster PG + EFA + FSx Lustre + single AZ + **hyperthreading off**, HVM ✗ PV AMI (Official Q21) · node-to-node timeouts → **cluster placement group** ✗ enable ENA (already on) (Official Q58) · many small apps → bin-pack on ECS
- Full capacity during deploy → Beanstalk **immutable**/blue-green · Lambda canary/linear → SAM + CodeDeploy
- Always-on prod tier → On-Demand/RI, **never Spot** · slow boot + big static data → bake AMI + mount **EFS** (✗ user-data download)
- Predictable spike → **scheduled scaling** (target tracking reacts after; DynamoDB too) 🔁 (Neal B Q17) · **unpredictable** peaks → target tracking on `ALBRequestCountPerTarget` ✗ scheduled (Official Q17) · SQS workers → **backlog per instance** ✗ `ApproximateNumberOfMessagesVisible` (Official Q60) · CodeBuild repeated downloads → **S3 cache** in buildspec · full desktop + AD → **WorkSpaces** + AD Connector + RADIUS MFA (AppStream = apps only) (Neal B Q35) · slow desktop app for remote users → **AppStream 2.0** ✗ Multi-AZ/ElastiCache 🔁 (Neal C Q5)
- Cheapest resilient web tier → **Spot Fleet** (On-Demand baseline + Spot) across AZs + ALB (✗ all Spot) · dynamic web + queue jobs → Fargate web + Spot workers
- Move instance into a placement group → **stop → modify placement → start** · latest AMI in CFN → **SSM parameter type** + update-stack · new AMI to an ASG, no downtime → CFN **UpdatePolicy rolling update** (✗ change set = preview only) · CFN CI/CD → CodePipeline + change set + CodeBuild (✗ CodeDeploy)
- Runbook install/config → CFN + **user data/cfn-init** ✗ CFN + manual steps (Official Q30) · simple LAMP, fixed monthly price, little AWS skill → **Lightsail** (Official Q73)
- Bursty app, least overhead → **S3/CloudFront + API GW + Lambda** ✗ ECS on EC2/ASG 🔁 (Neal A Q22, TD5 Q39) · seconds-long steps → Lambda + Step Functions ✗ Fargate (Neal A Q15) · EKS resilience → **topology spread across AZs** ✗ autoscaler sizing (Neal C Q11)
- gp2 = 3 IOPS/GiB → +3,000 IOPS = grow gp2 by 1 TB (or gp3) ✗ EFS/io1 (Udemy2 Q11) · 504/latency root cause → **X-Ray + Lambda logs** ✗ API GW execution logs 🔁 (Udemy2 Q24)
- Real-time push to clients → **AppSync** subscriptions (WebSockets) · MAC-bound license → pre-licensed **ENI pool** + config in Parameter Store
- ASG: debug → suspend **Terminate** 🔁 · save data first → lifecycle hook · in-flight → deregistration delay · slow boot → golden AMI
- Savings Plans scope: steady EC2 → **EC2 Instance SP** (up to 72%) · EC2/Fargate/Lambda mix → **Compute SP** (up to 66%) · Compute SP never covers DBs/caches → RDS/ElastiCache/MemoryDB **reserved nodes**

## 5. Data, streaming, analytics
- RDS MySQL read replicas = one endpoint each, no shared reader endpoint → quick fix **ElastiCache** 🔁 · Aurora Auto Scaling = readers only · write bursts → SQS buffer
- Multi-Region: Aurora Global (1 writer, RPO < 1 s; local writes + read-after-write → **write forwarding**, test with managed failover ✗ read secondary/write primary (Official Q45)) · DynamoDB global tables = active-active · Oracle RAC → EC2 (RDS has no RAC)
- Same record to many apps → **KDS** ✗ SQS · lagging consumers → Enhanced Fan-Out · transform + land → Firehose + Lambda · KDS → Redshift: Firehose is the usual exam answer (Redshift streaming ingestion can also read KDS directly)
- ETL → Glue · ad-hoc / nightly SQL on S3 (ORC/Parquet) → **Athena** + Glue Catalog ✗ Redshift cluster 🔁 · WAF logs → Firehose → S3 → Athena · search → OpenSearch
- Redshift read bursts → **concurrency scaling** ✗ offload to EMR/RDS
- "Quick + cost-effective" DB latency → **add ElastiCache**, don't migrate the DB 🔁 (TD3 Q1) · Read-heavy RDS on a budget → read replicas + **ElastiCache** + sharding (✗ bigger instance / PIOPS) · Step Functions can't take **SQS** as direct input
- DynamoDB: hot keys → **DAX** (reads only, never writes); dev/spiky → **on-demand** ✗ add DAX 🔁 (Neal C Q7) · **Savings Plans never cover DynamoDB** → provisioned + auto scaling / reserved 🔁 (Official Q68) · "in-memory" → ElastiCache Redis (sorted sets) or DAX ✗ DynamoDB alone (Udemy2 Q59)
- Firehose targets S3/Redshift/OpenSearch/Splunk/HTTP, **not DynamoDB**; serverless, no capacity planning → **SQS + Lambda** 🔁 (Udemy2 Q54) · Athena speed → Parquet/ORC + **date partitions** ✗ bucket per date (Neal A Q4)
- DynamoDB time-series → **table per period** (drop old whole) + device PK + timestamp SK · steady throughput → **reserved capacity** · Redshift DR other Region → automated snapshots + **cross-Region snapshot copy** (KMS → **snapshot copy grant** first, for a **destination-Region** key) 🔁×4 (TD4 Q64, TD3 Q62, Udemy2 Q33)
- One-off EMR → On-Demand master/core + **Spot task**, never RI 🔁 · OpenSearch → hot + UltraWarm + cold 🔁 · Redshift KMS cross-Region → snapshot copy grant

## 6. Storage, hybrid, migration, DR
- Tape + **process** the content → **File Gateway** + Rekognition ✗ Tape GW 🔁×4 · on-prem NFS share → S3 objects → **S3 File Gateway** ✗ Volume GW (iSCSI block) (Official Q61)
- Intelligent-Tiering: retrieve ≤ 6 h → **Archive Access** (~5 h) ✗ Deep Archive Access (≤ 12 h) 🔁 (Official Q9) · Windows SMB **in AWS** → FSx Windows + DataSync 🔁 · EFS = Linux only
- S3 website = **static files only** (✗ interactive NGINX+MySQL app 🔁) · site shows nothing → bucket **public read** (✗ "wait for DNS propagation")
- Volume GW cached (hot subset) vs stored (full copy) · recover → snapshot → EBS · replication SLA → **S3 RTC** 🔁 · far uploads → Transfer Acceleration
- Growing S3 cost from failed uploads → multipart + lifecycle **abort incomplete multipart uploads**
- Snow math: 1 Gbps ≈ 10.8 TB/day (25 TB → Transfer Acceleration ✗ Snowball 🔁 Neal B Q10); > 1 week → Snowball Edge (80 TB usable; newer 210 TB model); ≥ 10 PB → Snowmobile (retired 2024, may still appear as a distractor); lands in S3, then lifecycle
- VM as-is → OVF export to S3 + **VM Import** ✗ DataSync/FSx 🔁 (Neal A Q11) · continuous block replication → **MGN** · TCO → Migration Evaluator · discovery → ADS / AWS Transform
- Heterogeneous DB → SCT + DMS (CDC) · replatform = managed platform, no code rewrite · SFTP → Transfer Family (VPC endpoint for EIP + SG)
- Shared dataset copied to many EBS → one **EFS, Provisioned Throughput** (✗ Max I/O = more latency) · RDS MySQL → on-prem replica → VPN + mysqldump + external replica · docs + versions + ACL → WorkDocs (retired 2025, still an exam answer)
- RDS Multi-AZ failover = **CNAME** flips to the standby (not the IP) · IaC → CloudFormation (✗ Beanstalk) · app push → SNS **Mobile Push** (✗ SMS)
- DR by RTO: hours → backup/restore · tens of min → pilot light · minutes → warm standby · ~0 → multi-site. **Multi-AZ ≠ DR** 🔁
- Fit: VOD → MediaConvert + HLS · MQTT → IoT Core · offline edge ML → Greengrass · speech → Transcribe · OCR → Textract · bot → Lex · stateful workflow → Step Functions

## Corrections (validated 2026-10-13)
- KDS → Redshift: Redshift streaming ingestion reads KDS/MSK directly; Firehose is still the classic "deliver to Redshift" answer.
- RDS MySQL: classic read replicas have no shared reader endpoint (a Multi-AZ **DB cluster** does have one); ElastiCache is still the "quick" answer.
- Snowmobile was retired in 2024; Snowball Edge Storage Optimized also comes in a 210 TB model.
