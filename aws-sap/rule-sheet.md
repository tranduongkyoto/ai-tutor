# SAP-C02 Rule Sheet (1 page)

Built 2026-10-13 from 376 per-question rules: TD1, TD2, TD3, TD5, TD6 + Udemy #2/#3 unseen (`practice-exam/sap/*_review_notes.json`). Validated 2026-10-13 (see § Corrections).
🔁 = missed 2+ times. Format: **trigger in the stem → answer** (✗ = the trap you picked).
HTML view: `rule-sheet.html` (search + self-test); rebuild after editing this file: `python3 aws-sap/build_study_pages.py`.

## 0. Read the stem first (7 meta-rules behind most repeat misses)
1. **Find the constraint word** — *least overhead · most cost-effective · quickest · minimal changes · no code changes*. It picks between 2 working options.
2. **Managed service > DIY.** Lambda/SQS/EC2 pipeline when Glue, MediaConvert, Transfer Family, Patch Manager, Service Catalog, IoT Core or Batch exists → ✗.
3. **Don't overbuild.** One-off / short deadline / "quick" → no RIs, no full migration, no hot standby. Match the DR tier to the RTO. Pick the **lightest feature** that works: Athena > Redshift for a nightly window, CloudFront Functions > Lambda@Edge for rewrites. 🔁×3 (TD3, Udemy3, TD6)
4. **Detect ≠ prevent.** "Don't block developers" / "detect" → Config rule + remediation. "Prevent" / "**enforce**" / "block" → SCP / IAM deny (+ tag policy). 🔁
5. **Multi-select:** both picks must complete the **same** solution. Kill any option with one wrong clause or an internal contradiction.
6. **"Serverless" in the stem** → Aurora Serverless, Redshift Serverless, Fargate, DynamoDB, EventBridge.
7. **Twin options:** when 2 options are almost word-for-word the same, find the ONE phrase that differs and judge only that (IA vs Deep Archive, public vs VPC endpoint, ALB vs NLB, which account). 🔁 (TD5 marathon 5/10)

## 1. Identity & governance
- Corporate **SAML** → Identity Center / `AssumeRoleWithSAML` ✗ WebIdentity 🔁 · **social/mobile/SPA** → Cognito / `AssumeRoleWithWebIdentity`, temp creds, never access keys 🔁
- **LDAP, no SAML** → custom identity broker → STS · **3rd party** → trust policy + `sts:ExternalId` · **GitHub CI** → IAM OIDC provider
- Cross-account role lives in the **TARGET** account; fix access = its **trust policy** → trust the caller's **role ARN**, not the account root (least privilege) · EC2 → AWS API = instance profile, nothing else
- **SCP never grants**; allow-list SCP must list every action; doesn't affect the mgmt account or service-linked roles 🔁 · team access = IAM policy
- Deny at root hits every OU → attach at the OU · protect tagged resources → SCP deny + `aws:ResourceTag` · MFA ≠ authorization
- **Enforce tag values** → tag policy (allowed values) + SCP deny `CreateStack`/create without `aws:RequestTag` ✗ Config 🔁 · VPC-only access points → SCP + `s3:AccessPointNetworkOrigin` · org-only ECR/S3 → `aws:PrincipalOrgID`
- Central backups + retention + cross-Region copy + alerts → **AWS Backup** plan (copy action + SNS) ✗ DLM/Lambda glue
- Rotation/lifecycle → **Secrets Manager** (ECS `secrets`/`valueFrom`) ✗ Parameter Store 🔁 · CFN → `{{resolve:secretsmanager:…}}`
- Org: RAM needs **trusted access** · StackSets **service-managed** + auto-deploy · org trail + Config aggregator + Security Hub delegated admin
- Cost by tag → activate tags in the **mgmt account** + CUR 🔁 · org dashboard → CUR → QuickSight · alerts → Budgets · self-service → Service Catalog + launch constraint
- Tamper-proof CloudTrail → log file validation + MFA Delete (KMS = confidentiality only)

## 2. Networking, DNS, edge
- IPsec VPN over DX → **PUBLIC VIF** 🔁×5 · cheapest DX backup → S2S VPN · many VPCs/Regions → DX Gateway (allowed prefixes ⊇ VPC CIDRs)
- VPN HA → 2nd **CGW** (VGW already has 2 tunnels; 1 VGW per VPC)
- PrivateLink service = **NLB**/GWLB, never ALB 🔁×5 · appliance fleet → **GWLB + ASG** 🔁 · central inspection → TGW + GWLB VPC · URL filter → proxy / Network Firewall
- S3 from private subnet → **gateway endpoint** ✗ NAT 🔁 · lock it down → endpoint policy + access point + bucket policy (`aws:sourceVpce`) 🔁
- Packet contents → **Traffic Mirroring** ✗ Flow Logs 🔁 · block an IP → NACL deny · REJECT + source IP → Flow Logs
- Cross-account PHZ → `create-vpc-association-authorization` + `associate-vpc-with-hosted-zone` ✗ NS delegation 🔁 · Resolver outbound = AWS → on-prem
- Private-IP health check → CloudWatch alarm → Route 53 health check on the alarm · PHZ resolution → `enableDnsSupport` + `enableDnsHostnames`
- R53: failover = active-passive · latency + Evaluate Target Health = active-active · geolocation doesn't block · apex → alias
- **DNS caching blocks a fast shift** → Global Accelerator dials/weights · user → specific instance → GA custom routing · **GA can't front S3** 🔁
- CloudFront: custom domain → ACM in **us-east-1** · 504 → **origin group failover** 🔁 · custom origin → header + WAF on ALB · S3 → OAC · one client → signed URL/cookies
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
- Lambda floods RDS → **RDS Proxy** + connection outside the handler 🔁 · isolate a function → reserved concurrency · cut calls → API GW cache
- API GW + IAM principals → `AWS_IAM` (SigV4) + X-Ray (CORS isn't auth) · per-client quotas → usage plans + API keys
- Batch, least ops → **AWS Batch** + Spot + S3 🔁 · tight HPC → cluster PG + EFA + FSx Lustre · many small apps → bin-pack on ECS
- Full capacity during deploy → Beanstalk **immutable**/blue-green · Lambda canary/linear → SAM + CodeDeploy
- Always-on prod tier → On-Demand/RI, **never Spot** · slow boot + big static data → bake AMI + mount **EFS** (✗ user-data download)
- ASG: debug → suspend **Terminate** 🔁 · save data first → lifecycle hook · in-flight → deregistration delay · slow boot → golden AMI
- Savings Plans scope: steady EC2 → **EC2 Instance SP** (up to 72%) · EC2/Fargate/Lambda mix → **Compute SP** (up to 66%) · Compute SP never covers DBs/caches → RDS/ElastiCache/MemoryDB **reserved nodes**

## 5. Data, streaming, analytics
- RDS MySQL read replicas = one endpoint each, no shared reader endpoint → quick fix **ElastiCache** 🔁 · Aurora Auto Scaling = readers only · write bursts → SQS buffer
- Multi-Region: Aurora Global (1 writer, RPO < 1 s) · DynamoDB global tables = active-active · Oracle RAC → EC2 (RDS has no RAC)
- Same record to many apps → **KDS** ✗ SQS · lagging consumers → Enhanced Fan-Out · transform + land → Firehose + Lambda · KDS → Redshift: Firehose is the usual exam answer (Redshift streaming ingestion can also read KDS directly)
- ETL → Glue · ad-hoc / nightly SQL on S3 (ORC/Parquet) → **Athena** + Glue Catalog ✗ Redshift cluster 🔁 · WAF logs → Firehose → S3 → Athena · search → OpenSearch
- Redshift read bursts → **concurrency scaling** ✗ offload to EMR/RDS
- One-off EMR → On-Demand master/core + **Spot task**, never RI 🔁 · OpenSearch → hot + UltraWarm + cold 🔁 · Redshift KMS cross-Region → snapshot copy grant

## 6. Storage, hybrid, migration, DR
- Tape + **process** the content → **File Gateway** + Rekognition ✗ Tape GW 🔁×3 · Windows SMB **in AWS** → FSx Windows + DataSync 🔁 · EFS = Linux only
- S3 website = **static files only** (✗ interactive NGINX+MySQL app 🔁) · site shows nothing → bucket **public read** (✗ "wait for DNS propagation")
- Volume GW cached (hot subset) vs stored (full copy) · recover → snapshot → EBS · replication SLA → **S3 RTC** 🔁 · far uploads → Transfer Acceleration
- Snow math: 1 Gbps ≈ 10.8 TB/day; > 1 week → Snowball Edge (80 TB usable; newer 210 TB model); ≥ 10 PB → Snowmobile (retired 2024, may still appear as a distractor); lands in S3, then lifecycle
- VM as-is → VM Import · continuous block replication → **MGN** · TCO → Migration Evaluator · discovery → ADS / AWS Transform
- Heterogeneous DB → SCT + DMS (CDC) · replatform = managed platform, no code rewrite · SFTP → Transfer Family (VPC endpoint for EIP + SG)
- DR by RTO: hours → backup/restore · tens of min → pilot light · minutes → warm standby · ~0 → multi-site. **Multi-AZ ≠ DR** 🔁
- Fit: VOD → MediaConvert + HLS · MQTT → IoT Core · offline edge ML → Greengrass · speech → Transcribe · OCR → Textract · bot → Lex · stateful workflow → Step Functions

## Corrections (validated 2026-10-13)
- KDS → Redshift: Redshift streaming ingestion reads KDS/MSK directly; Firehose is still the classic "deliver to Redshift" answer.
- RDS MySQL: classic read replicas have no shared reader endpoint (a Multi-AZ **DB cluster** does have one); ElastiCache is still the "quick" answer.
- Snowmobile was retired in 2024; Snowball Edge Storage Optimized also comes in a 210 TB model.
