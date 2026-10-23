# SAP-C02 Rule Sheet (1 page)

Built 2026-10-13 from 376 per-question rules: TD1, TD2, TD3, TD5, TD6 + Udemy #2/#3 unseen; TD4 (Gate 2) rules added 2026-10-19 (`practice-exam/sap/*_review_notes.json`). Validated 2026-10-13 (see § Corrections).
🔁 = missed 2+ times. Format: **trigger in the stem → answer** (✗ = the trap you picked).
HTML view: `rule-sheet.html` (search + self-test); rebuild after editing this file: `python3 aws-sap/build_study_pages.py`. Drill: `rule-sheet-flashcards.html` (133 two-option cards, deck `decks/rule-sheet-deck.json`).

## 0. Read the stem first (7 meta-rules behind most repeat misses)
1. **Find the constraint word** — *least overhead · most cost-effective · quickest · minimal changes · no code changes*. It picks between 2 working options.
2. **Managed service > DIY.** Lambda/SQS/EC2 pipeline when Glue, MediaConvert, Transfer Family, Patch Manager, Service Catalog, IoT Core or Batch exists → ✗.
3. **Don't overbuild.** One-off / short deadline / "quick" → no RIs, no full migration, no hot standby. Match the DR tier to the RTO. Pick the **lightest feature** that works: Athena > Redshift for a nightly window, CloudFront Functions > Lambda@Edge for rewrites. 🔁×3 (TD3, Udemy3, TD6)
4. **Detect ≠ prevent.** "Don't block developers" / "detect" → Config rule + remediation. "Prevent" / "**enforce**" / "block" → SCP / IAM deny (+ tag policy). 🔁
5. **Multi-select:** both picks must complete the **same** solution; after the sure pick, test every other option against **each** stem requirement (TD4 7/7, Neal A 8/9 misses were half right). Kill any option with one wrong clause or an internal contradiction.
6. **"Serverless" in the stem** → Aurora Serverless, Redshift Serverless, Fargate, DynamoDB, EventBridge.
7. **Twin options:** when 2 options are almost word-for-word the same, find the ONE phrase that differs and judge only that (IA vs Deep Archive, public vs VPC endpoint, ALB vs NLB, which account). 🔁 (TD5 marathon 5/10; TD4 Q14 CodeDeploy clause, Q63 SQS→Step Functions, Q41 behavior vs ALB rule)

## 1. Identity & governance
- Corporate **SAML** → Identity Center / `AssumeRoleWithSAML` ✗ WebIdentity 🔁 · **social/mobile/SPA** → Cognito / `AssumeRoleWithWebIdentity`, temp creds, never access keys 🔁
- **LDAP, no SAML** → custom identity broker → STS · **3rd party** → trust policy + `sts:ExternalId` · **GitHub CI** → IAM OIDC provider
- Cross-account role lives in the **TARGET** account; fix access = its **trust policy** → trust the caller's **role ARN**, not the account root (least privilege) · EC2 → AWS API = instance profile, nothing else
- **SCP never grants**; allow-list SCP must list every action; doesn't affect the mgmt account or service-linked roles 🔁 · team access = IAM policy
- Deny at root hits every OU → attach at the OU · protect tagged resources → SCP deny + `aws:ResourceTag` · MFA ≠ authorization
- **Enforce tag values** → tag policy (allowed values) + SCP deny `CreateStack`/create without `aws:RequestTag` ✗ Config 🔁 · VPC-only access points → SCP + `s3:AccessPointNetworkOrigin` · org-only ECR/S3 → `aws:PrincipalOrgID`
- Central backups + retention + cross-Region copy + alerts → **AWS Backup** plan (copy action + SNS) ✗ DLM/Lambda glue
- Existing Microsoft AD → **Directory Service** (Managed AD + trust) → SSO; don't recreate users in Identity Center
- Rotation/lifecycle → **Secrets Manager** (ECS `secrets`/`valueFrom`) ✗ Parameter Store 🔁 · CFN → `{{resolve:secretsmanager:…}}`
- Team isolation + per-team billing → **account per team** in Organizations + SCPs; security tooling in a **delegated security account**, never the management account (✗ security account as mgmt/payer) · Org: RAM needs **trusted access** · StackSets **service-managed** + auto-deploy · org trail + Config aggregator + Security Hub delegated admin
- Cost by tag → activate tags in the **mgmt account** + CUR 🔁 · org dashboard → CUR → QuickSight · alerts → Budgets · self-service → Service Catalog + launch constraint
- Alert on cost, RI/SP **coverage** or utilization → **AWS Budgets** (coverage/utilization budget) ✗ CloudWatch/CloudTrail 🔁 (Neal A Q13, Q32) · spend **spike vs historical pattern** → **Cost Anomaly Detection** (learns baseline) ✗ Budgets = static thresholds you set · admin access with no open ports → **Session Manager** + IAM (no bastion, no inbound SSH/RDP)
- Tamper-proof CloudTrail → log file validation + MFA Delete (KMS = confidentiality only)
- "Notify + auto-fix on an API call" (CreateUser…) → CloudTrail → **EventBridge rule** → Step Functions/Lambda remediate + SNS 🔁 (TD4 Q5) · zonal RIs share across consolidated-billing accounts only in the **same AZ + type**

## 2. Networking, DNS, edge
- IPsec VPN over DX → **PUBLIC VIF** 🔁×5 · cheapest DX backup → S2S VPN · one DX → many VPCs/Regions → **DX Gateway** + VGW per VPC (allowed prefixes ⊇ VPC CIDRs) 🔁×3 (TD1, TD5, TD4 Q58)
- VPN HA → 2nd **CGW** (VGW already has 2 tunnels; 1 VGW per VPC)
- Remote workstations → peered VPCs → **Client VPN** client + ONE endpoint in the main VPC (✗ new TGW) · UDP → **NLB** + NACL deny non-UDP (WAF/ALB = L7)
- PrivateLink service = **NLB**/GWLB, never ALB 🔁×5 · appliance fleet → **GWLB + ASG** 🔁 · central inspection → TGW + GWLB VPC · URL filter → proxy / Network Firewall
- S3 from private subnet → **gateway endpoint** ✗ NAT 🔁 · lock it down → endpoint policy + access point + bucket policy (`aws:sourceVpce`) 🔁
- Packet contents → **Traffic Mirroring** ✗ Flow Logs 🔁 · block an IP → NACL deny · REJECT + source IP → Flow Logs
- Cross-account PHZ → `create-vpc-association-authorization` + `associate-vpc-with-hosted-zone` ✗ NS delegation 🔁 · Resolver **outbound** + forwarding rule = queries leaving the VPC (on-prem / custom AD domain) · inbound = into the VPC
- On-prem resolves a **private hosted zone** → Resolver **inbound** endpoint + PHZ associated with every VPC that needs it · most resilient hybrid link → 2nd DX at a different location/carrier (VPN = cheaper backup)
- Private-IP health check → CloudWatch alarm → Route 53 health check on the alarm · PHZ resolution → `enableDnsSupport` + `enableDnsHostnames`
- R53: failover = active-passive · latency + Evaluate Target Health = active-active · geolocation doesn't block · apex → alias
- **DNS caching blocks a fast shift** → Global Accelerator dials/weights · user → specific instance → GA custom routing · **GA can't front S3** 🔁
- CloudFront: custom domain → ACM in **us-east-1** · 504 → **origin group failover** 🔁 · custom origin → header + WAF on ALB · S3 → OAC · one client → signed URL/cookies
- Add S3 content to an ALB-origin distribution → new **S3 origin (OAC) + path-pattern behavior** (✗ ALB rule forwarding to S3)
- Simple header/URL/query rewrite → **CloudFront Functions** ✗ Lambda@Edge (only for network calls, body access, longer runtime)
- Many domains on one ALB → **SNI** multi-cert (wildcard = one domain only) · route by hostname → ALB **host** condition · static IP for ALB → NLB in front · non-HTTP ports → NLB (ALB = HTTP/HTTPS only)

## 3. Security & data protection
- Own key + rotation → **SSE-KMS** · key from own HSM → KMS `Origin=EXTERNAL` · key never leaves + HA → CloudHSM ≥2 AZ · force TLS → `aws:SecureTransport`
- Stop public objects → Block Public Access · DDoS L3/L4 → Shield Advanced · SQLi/XSS → WAF · GuardDuty only detects
- Alert near a service quota → CloudWatch alarm on the **AWS/Usage** metric with `SERVICE_QUOTA()` math (✗ SampleCount) + SNS
- PII → Macie · CVEs → Inspector · config drift → Config · who read what → CloudTrail data events · app → DB → SG-to-SG reference
- Inspector for Lambda = **standard scan** (CVEs in packages/layers) + **code scan** (code flaws) + `InspectorCodeExclusion` tag to skip functions (✗ IAM)

## 4. Compute, serverless, deployment
- VPC Lambda → **private subnets** + gateway endpoint/NAT (✗ public subnet: Lambda ENIs never get public IPs) · containers also on other clouds → **EKS** (✗ ECS = AWS-only) 🔁
- Job > 15 min → Fargate task (Lambda/EventBridge `RunTask`) or EC2 ASG on SQS depth · simple HTTPS for a function → Function URL
- Lambda floods RDS → **RDS Proxy** + connection outside the handler 🔁 · faster failover + keep connections → **RDS Proxy + Aurora replicas** 🔁 (TD4 Q28) · isolate a function → reserved concurrency · cut calls → API GW cache
- API GW + IAM principals → `AWS_IAM` (SigV4) + X-Ray (CORS isn't auth) · per-client quotas → usage plans + API keys
- Batch, least ops → **AWS Batch** + Spot + S3 🔁 · tight HPC → cluster PG + EFA + FSx Lustre · many small apps → bin-pack on ECS
- Full capacity during deploy → Beanstalk **immutable**/blue-green · Lambda canary/linear → SAM + CodeDeploy
- Always-on prod tier → On-Demand/RI, **never Spot** · slow boot + big static data → bake AMI + mount **EFS** (✗ user-data download)
- Cheapest resilient web tier → **Spot Fleet** (On-Demand baseline + Spot) across AZs + ALB (✗ all Spot) · dynamic web + queue jobs → Fargate web + Spot workers
- Move instance into a placement group → **stop → modify placement → start** · latest AMI in CFN → **SSM parameter type** + update-stack · new AMI to an ASG, no downtime → CFN **UpdatePolicy rolling update** (✗ change set = preview only) · CFN CI/CD → CodePipeline + change set + CodeBuild (✗ CodeDeploy)
- Real-time push to clients → **AppSync** subscriptions (WebSockets) · MAC-bound license → pre-licensed **ENI pool** + config in Parameter Store
- ASG: debug → suspend **Terminate** 🔁 · save data first → lifecycle hook · in-flight → deregistration delay · slow boot → golden AMI
- Savings Plans scope: steady EC2 → **EC2 Instance SP** (up to 72%) · EC2/Fargate/Lambda mix → **Compute SP** (up to 66%) · Compute SP never covers DBs/caches → RDS/ElastiCache/MemoryDB **reserved nodes**

## 5. Data, streaming, analytics
- RDS MySQL read replicas = one endpoint each, no shared reader endpoint → quick fix **ElastiCache** 🔁 · Aurora Auto Scaling = readers only · write bursts → SQS buffer
- Multi-Region: Aurora Global (1 writer, RPO < 1 s) · DynamoDB global tables = active-active · Oracle RAC → EC2 (RDS has no RAC)
- Same record to many apps → **KDS** ✗ SQS · lagging consumers → Enhanced Fan-Out · transform + land → Firehose + Lambda · KDS → Redshift: Firehose is the usual exam answer (Redshift streaming ingestion can also read KDS directly)
- ETL → Glue · ad-hoc / nightly SQL on S3 (ORC/Parquet) → **Athena** + Glue Catalog ✗ Redshift cluster 🔁 · WAF logs → Firehose → S3 → Athena · search → OpenSearch
- Redshift read bursts → **concurrency scaling** ✗ offload to EMR/RDS
- "Quick + cost-effective" DB latency → **add ElastiCache**, don't migrate the DB 🔁 (TD3 Q1) · Read-heavy RDS on a budget → read replicas + **ElastiCache** + sharding (✗ bigger instance / PIOPS) · Step Functions can't take **SQS** as direct input
- DynamoDB time-series → **table per period** (drop old whole) + device PK + timestamp SK · steady throughput → **reserved capacity** · Redshift DR other Region → automated snapshots + **cross-Region snapshot copy** (KMS → **snapshot copy grant** first) 🔁×3 (TD4 Q64, TD3 Q62)
- One-off EMR → On-Demand master/core + **Spot task**, never RI 🔁 · OpenSearch → hot + UltraWarm + cold 🔁 · Redshift KMS cross-Region → snapshot copy grant

## 6. Storage, hybrid, migration, DR
- Tape + **process** the content → **File Gateway** + Rekognition ✗ Tape GW 🔁×3 · Windows SMB **in AWS** → FSx Windows + DataSync 🔁 · EFS = Linux only
- S3 website = **static files only** (✗ interactive NGINX+MySQL app 🔁) · site shows nothing → bucket **public read** (✗ "wait for DNS propagation")
- Volume GW cached (hot subset) vs stored (full copy) · recover → snapshot → EBS · replication SLA → **S3 RTC** 🔁 · far uploads → Transfer Acceleration
- Snow math: 1 Gbps ≈ 10.8 TB/day; > 1 week → Snowball Edge (80 TB usable; newer 210 TB model); ≥ 10 PB → Snowmobile (retired 2024, may still appear as a distractor); lands in S3, then lifecycle
- VM as-is → VM Import · continuous block replication → **MGN** · TCO → Migration Evaluator · discovery → ADS / AWS Transform
- Heterogeneous DB → SCT + DMS (CDC) · replatform = managed platform, no code rewrite · SFTP → Transfer Family (VPC endpoint for EIP + SG)
- Shared dataset copied to many EBS → one **EFS, Provisioned Throughput** (✗ Max I/O = more latency) · RDS MySQL → on-prem replica → VPN + mysqldump + external replica · docs + versions + ACL → WorkDocs (retired 2025, still an exam answer)
- RDS Multi-AZ failover = **CNAME** flips to the standby (not the IP) · IaC → CloudFormation (✗ Beanstalk) · app push → SNS **Mobile Push** (✗ SMS)
- DR by RTO: hours → backup/restore · tens of min → pilot light · minutes → warm standby · ~0 → multi-site. **Multi-AZ ≠ DR** 🔁
- Fit: VOD → MediaConvert + HLS · MQTT → IoT Core · offline edge ML → Greengrass · speech → Transcribe · OCR → Textract · bot → Lex · stateful workflow → Step Functions

## Corrections (validated 2026-10-13)
- KDS → Redshift: Redshift streaming ingestion reads KDS/MSK directly; Firehose is still the classic "deliver to Redshift" answer.
- RDS MySQL: classic read replicas have no shared reader endpoint (a Multi-AZ **DB cluster** does have one); ElastiCache is still the "quick" answer.
- Snowmobile was retired in 2024; Snowball Edge Storage Optimized also comes in a 210 TB model.
