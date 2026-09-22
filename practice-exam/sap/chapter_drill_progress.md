# SAP-C02 Chapter Drill Progress

## security — 2026-09-15
Score: 10/13 (77%)

| Q Ref | Topic | Your | Correct | Result |
|-------|-------|------|---------|--------|
| T1:Q6 | WAF rules across multi-account (Config+SSM+CF StackSets) | B | B | Correct |
| T1:Q20 | WAF+Inspector+GuardDuty roles (monitor vs block) | B | B | Correct |
| T1:Q25 | Secrets Manager rotation in VPC (interface endpoint) | C | A | Wrong |
| T1:Q30 | KMS client-side encryption (GenerateDataKey) | A | C | Wrong |
| T2:Q6 | WAF geo match + IP set (block country, allow dev team) | C,E | C,E | Correct |
| T2:Q14 | ACM certs are Region-specific (multi-Region ALB) | C | C | Correct |
| T2:Q18 | Redshift KMS cross-Region snapshots (grant in dest) | D | B | Wrong |
| T2:Q34 | DDoS defense (Route53 + CloudFront + WAF + S3) | C,E | C,E | Correct |
| T3:Q16 | CloudFront 502 (expired origin SSL cert, need trusted CA) | A | A | Correct |
| T3:Q29 | Redshift audit logs (SSE-S3 + Spectrum, cost-effective) | A | A | Correct |
| T3:Q38 | KMS key access restriction (PrincipalOrgID + Org ID) | C | C | Correct |
| T3:Q54 | Country restriction (WAF geo match on ALB) | D | D | Correct |
| T3:Q60 | Vulnerability scanning (Inspector, not SSM) | D | D | Correct |

### Weak Areas — Security
1. **VPC endpoints for Secrets Manager** — Lambda timeout in private subnet = needs VPC interface endpoint for Secrets Manager (not Lambda, not SSL issue)
2. **kms:GenerateDataKey** — client-side envelope encryption requires GenerateDataKey for uploads, Decrypt for downloads. kms:Encrypt alone is NOT sufficient
3. **Redshift cross-Region snapshots** — snapshot copy grant in DESTINATION Region, KMS key in DESTINATION Region, configure in SOURCE Region. No "cross-Region replication" exists for Redshift

## identity-federation — 2026-09-15
Score: 8/15 (53%)

| Q Ref | Topic | Your | Correct | Result |
|-------|-------|------|---------|--------|
| T3:Q33 | Confused deputy (external ID from partner) | A | C | Wrong |
| T1:Q27 | Centralized RI purchasing (Orgs all-features + SCP) | C,B | A,B | Wrong |
| T2:Q47 | SCP behavior (root user, service-linked roles) | B,F,E | B,D,E | Wrong |
| T3:Q18 | SCP true statements (root user, deny overrides) | C,E | C,E | Correct |
| T2:Q38 | SAML federation + RDS Region restriction | B | D | Wrong |
| T1:Q28 | Multi-account OUs + Budget alerts + GuardDuty delegated admin | A,C,E | A,C,D | Wrong |
| T3:Q17 | API Gateway throttle (no Lambda logs = blocked before Lambda) | C | C | Correct |
| T1:Q6 | WAF rules across multi-account (Config+SSM+CF StackSets) | B | B | Correct |
| T3:Q19 | SCP JSON syntax (Statement as array) | C | C | Correct |
| T3:Q37 | Cross-account Lambda (execution role + AssumeRole) | C,D | C,D | Correct |
| T3:Q38 | KMS key access restriction (PrincipalOrgID + Org ID) | C | C | Correct |
| T3:Q58 | Region restriction (SCP deny non-core at root OU) | A | A | Correct |
| T3:Q13 | CodePipeline cross-account (KMS+S3 in A, role+CF in B) | C,B,A | A,D,E | Wrong |
| T2:Q75 | SNS→Lambda throttling (Lambda concurrency quota) | A | A | Correct |
| T3:Q66 | ABAC session tags (STS tag + IAM deny StringNotEquals) | A | D | Wrong |

### Weak Areas — Identity & Federation
1. **External ID direction** — external ID comes FROM the third-party partner (they generate it for uniqueness), not created by you
2. **AWS Organizations all features vs consolidated billing** — SCPs require all features mode; consolidated billing mode does NOT support SCPs
3. **SCPs affect root user** — SCPs affect ALL identities in member accounts INCLUDING root; they do NOT affect service-linked roles or the management account root
4. **PowerUserAccess vs AdministrativeAccess** — PowerUserAccess = AdministrativeAccess minus IAM management; use PowerUser for least privilege when IAM access not needed
5. **OUs vs SCPs as containers** — accounts are organized into OUs, not into SCPs; SCPs are attached TO OUs
6. **Cross-account CodePipeline direction** — pipeline in account A: KMS key + S3 bucket + AssumeRole permission in A; cross-account role + CF service role in target account B
7. **ABAC with STS session tags** — for shared accounts, use SAML session tags + IAM deny with StringNotEquals on aws:PrincipalTag; can't use separate OUs for a single shared account

## vpc — 2026-09-16 (30 of 34 answered, skipped 4 non-VPC: T1:Q29, T3:Q40, T3:Q57, T3:Q64)
Score: 23/30 (77%)

| Q Ref | Topic | Your | Correct | Result |
|-------|-------|------|---------|--------|
| T3:Q1 | QuickSight VPC connection (private subnet + SG + ENI) | C | C | Correct |
| T3:Q5 | Route53 Resolver inbound + private zone + CNAME for EFS | C | C | Correct |
| T2:Q4 | Multi-DC hybrid (DX per DC from different providers) | B | D | Wrong |
| T3:Q8 | Cross-VPC load balancer access (VPC peering, cost-effective) | B | B | Correct |
| T3:Q9 | Encrypted DX (public VIF + Site-to-Site VPN) | C | D | Wrong |
| T3:Q11 | Storage Gateway to S3 private (Gateway + Interface endpoints) | B,A | B,D | Wrong |
| T3:Q14 | Private IP S3 access over DX (private VIF + interface endpoint) | A | A | Correct |
| T2:Q13 | S3 access restricted to VPC endpoint only | A | A | Correct |
| T3:Q20 | Encrypted DX to VPC (public VIF + VPG + IPsec) | D,A,F | C,D,F | Wrong |
| T3:Q21 | Move EC2 to different subnet (AMI + new instance + Route53) | C | B | Wrong |
| T3:Q25 | Isolated VPCs via PrivateLink (NLB + endpoint service + ALB) | B | C | Wrong |
| T3:Q28 | Automated VPC CIDR (CloudFormation custom resource + IPAM) | C | A | Wrong |
| T2:Q17 | Hub-spoke shared services (Centralized VPC Endpoints) | C | C | Correct |
| T2:Q31 | Private hosted zone not resolving (enable DNS hostnames+resolution) | D | D | Correct |
| T2:Q32 | Lambda VPC best practices (Layers, NAT, CloudWatch alarms) | E,A,F | A,E,F | Correct |
| T2:Q42 | Bidirectional DNS (inbound + outbound R53 Resolver endpoints) | B,C | B,C | Correct |
| T2:Q51 | Multi-site communication (VPN CloudHub) | D | D | Correct |
| T2:Q55 | Shared VPCs (VPC sharing = share subnets via RAM) | A | A | Correct |
| T2:Q57 | Default SG vs new SG (self-referencing inbound vs no inbound) | D | D | Correct |
| T2:Q64 | VPC peering + routes both directions (172.20 ↔ 172.30) | A,B | A,B | Correct |
| T2:Q72 | 140TB archive over DX (public VIF to S3) | D | A | Wrong |
| T3:Q46 | Same-CIDR peered VPCs (/28 subnets + 2 route tables) | A,E | A,E | Correct |
| T3:Q52 | Flow logs ACCEPT/REJECT (NACL outbound on subnet) | D | D | Correct |
| T3:Q61 | Lambda in VPC no internet (NAT Gateway needed) | A | A | Correct |
| T3:Q70 | Direct client access bypassing ELB (SG restrict to ELB only) | A | A | Correct |
| T1:Q2 | VPC Flow Logs NAT gateway (CloudWatch + dstAddr filter) | D | D | Correct |
| T1:Q12 | Security groups EC2↔RDS (outbound EC2 + inbound DB, port 3306) | E,B | B,E | Correct |
| T1:Q24 | Interface VPC endpoint for Kinesis (not Gateway) | C | C | Correct |
| T1:Q25 | Secrets Manager rotation timeout (VPC interface endpoint for SM) | A | A | Correct |
| T1:Q26 | DX + VPN for encrypted high-throughput connection | D | B | Wrong |

### Weak Areas — VPC
1. **Public VIF for encrypted DX** — VPN over Direct Connect requires PUBLIC VIF (VPN endpoint has public IP). Private VIF = private IP access to VPC only. Pattern: encryption over DX = public VIF + VPN
2. **Public VIF for S3 over DX** — on-premises → S3 directly over DX = public VIF (S3 is a public service). Only use private VIF + interface endpoint when bucket policy denies public IPs
3. **S3 supports both Gateway AND Interface VPC endpoints** — Private Virtual Interface is for Direct Connect only, not Storage Gateway to S3
4. **Can't move EC2 to different subnet** — must create AMI → launch new instance in target subnet → update DNS → terminate old
5. **PrivateLink for isolated cross-VPC** — NLB as endpoint service + interface VPC endpoint. VPC peering opens bidirectional traffic. NLB doesn't support host-based routing (ALB only)
6. **Fn::Cidr vs Custom Resource** — Fn::Cidr splits existing CIDRs, can't ensure global uniqueness. Use CloudFormation custom resource + external IPAM for unique CIDR allocation
7. **Multiple DCs need separate DX connections** — one DX per data center from different service providers for max resiliency. Can't share one DX across multiple distant DCs
8. **Minimum subnet CIDR is /28** — AWS doesn't allow /29 or smaller
9. **DX alone is not encrypted** — DX + VPN combo needed for encrypted + low-latency + high-throughput; VPN alone lacks throughput guarantees

## storage — 2026-09-17 (40 core questions, 13 non-core skipped)
Score: 25/40 (63%)

| Q Ref | Topic | Your | Correct | Result |
|-------|-------|------|---------|--------|
| T1:Q3 | FSx Multi-AZ failover test + monitoring | C,B | D,E | Wrong |
| T1:Q7 | VOD storage (S3 Intelligent-Tiering + CloudFront) | B | B | Correct |
| T1:Q9 | CloudFront S3 HTTP 307 (24h propagation) | A,B | A,D | Wrong |
| T1:Q10 | On-prem NAS to S3 (DataSync + Lambda + Step Functions) | C | C | Correct |
| T1:Q15 | Storage Gateway cache stale (RefreshCache) | C | C | Correct |
| T1:Q16 | DataSync + DX private VIF + PrivateLink for EFS | A | A | Correct |
| T1:Q17 | S3 Object Ownership (enforced = permanent ownership) | C,A | D,E | Wrong |
| T1:Q22 | Track S3 upload IP (CloudTrail data events + server access logs) | B,A | B,C | Wrong |
| T2:Q2 | S3 vs EFS vs EBS cost comparison | B | B | Correct |
| T2:Q5 | Video processing dedup (S3 trigger → Lambda → SQS → ASG) | D | D | Correct |
| T2:Q7 | S3 access points + VPC endpoint + bucket policy | D,C,A | A,D,E | Wrong |
| T2:Q11 | Global S3 access (CloudFront + S3 Transfer Acceleration) | B,E | B,E | Correct |
| T2:Q12 | Bulk migration + ongoing access (DataSync + File Gateway) | B | B | Correct |
| T2:Q13 | S3 VPC endpoint restrict access | A | A | Correct |
| T2:Q26 | DataSync supports S3 + EFS + FSx | D | D | Correct |
| T2:Q27 | Global serverless (edge-optimized API GW + S3 Transfer Accel) | A,C | C,D | Wrong |
| T2:Q30 | S3 Byte Range Fetch + S3 Select ScanRange | A,E | A,C | Wrong |
| T2:Q41 | POSIX shared (EFS) + >1M IOPS block (Instance Store) | C,E | C,E | Correct |
| T2:Q44 | S3TA no acceleration = no charge + inbound free | B | B | Correct |
| T2:Q56 | Detect public S3 objects (CloudTrail + EventBridge + SNS) | A,C | C,E | Wrong |
| T2:Q61 | Volume Gateway Cached vs Stored | C | C | Correct |
| T2:Q63 | CRR S3 Standard (not IA) → lifecycle to Glacier (30-day min) | C | D | Wrong |
| T2:Q67 | EFS on-prem + EC2 via Direct Connect (NAS replacement) | A | A | Correct |
| T2:Q68 | gp2 IOPS = 3/GB, add 1TB = +3000 IOPS | D | B | Wrong |
| T2:Q70 | S3 upload speed (multipart + Transfer Acceleration) | A,C | C,D | Wrong |
| T2:Q73 | Glacier Vault Lock for compliance (WORM) | C | C | Correct |
| T3:Q3 | Cold Redshift data → S3 Standard-IA + Athena | C,D | C,D | Correct |
| T3:Q4 | Glacier gzip CSV query (restore to S3 + S3 Select) | A | C | Wrong |
| T3:Q11 | File Gateway private S3 (Gateway + Interface endpoints) | A,B | B,D | Wrong |
| T3:Q15 | S3 Interface endpoint (private IP + on-prem + cross-Region) | A | A | Correct |
| T3:Q27 | S3→SQS SSE (customer-managed KMS key for S3 principal) | D | A | Wrong |
| T3:Q31 | S3 >5000 req/s (customer-specific prefixes) | D | D | Correct |
| T3:Q34 | S3 + Athena (Parquet + Hive date partitioning) | A,B | A,B | Correct |
| T3:Q35 | Glacier Instant Retrieval (2x/yr) + Deep Archive (10yr) | B | B | Correct |
| T3:Q41 | S3 RTC prefix replication + S3 event notification (not EventBridge) | C | B | Wrong |
| T3:Q48 | Single bucket + IAM ${aws:username} prefix isolation | B | B | Correct |
| T3:Q49 | Lifecycle: prefix /images → IA at 45d, all → Glacier at 180d | A,B | A,B | Correct |
| T3:Q50 | FSx Single-AZ → Multi-AZ (new FSx + DataSync, can't convert) | C | A | Wrong |
| T3:Q53 | 24h staging data = S3 Standard (no min duration, no retrieval fee) | C | C | Correct |
| T3:Q73 | Australia slow uploads (multipart + S3 Transfer Acceleration) | D | D | Correct |

### Weak Areas — Storage
1. **FSx failover test** — modify THROUGHPUT CAPACITY to trigger failover; NEVER modify ENIs
2. **S3 HTTP 307** — new bucket takes 24h to propagate; use Regional endpoint
3. **S3 Object Ownership** — enforced mode = permanent ownership even after re-enabling ACLs; old ACL permissions ARE restored
4. **S3 server access logging** — captures IP addresses for uploads (not CloudWatch Logs)
5. **S3 access points** — single data lake VPC + access point per bucket + gateway endpoint + bucket policy deny
6. **Edge-optimized API Gateway** — for global latency, not Global Accelerator (which can't front CloudFront/S3)
7. **S3 Select vs Athena** — S3 Select cheaper for simple queries on known files; Athena for complex analytics
8. **S3 Standard-IA 30-day minimum** — don't use as CRR target when lifecycle transitions immediately
9. **gp2 IOPS formula** — 3 IOPS per GB; increase volume size to cheaply add IOPS
10. **Global Accelerator ≠ S3** — GA endpoints are ALB/NLB/EC2/EIP only; S3 uses Transfer Acceleration
11. **Glacier Select** — only works on UNCOMPRESSED CSV; gzip requires restore to S3 first
12. **S3 VPC endpoints** — S3 supports BOTH Gateway and Interface endpoints; Private VIF is DX only
13. **KMS key types** — AWS-managed keys can't have policy modified; use customer-managed for cross-service access
14. **S3 replication events** — go to S3 event notifications only, NOT EventBridge
15. **FSx deployment type** — immutable after creation; must create new Multi-AZ + DataSync migrate

## databases — 2026-09-18
Score: 19/26 (73%) — skipped T3:Q56 (Elastic Beanstalk, not database-core)

| Q Ref | Topic | Your | Correct | Result |
|-------|-------|------|---------|--------|
| T1:Q8 | RDS to Redshift streaming (DMS) | D | D | Correct |
| T1:Q11 | MySQL migration (Aurora + Redis replication group) | C | A | Wrong |
| T1:Q12 | EC2↔RDS SG least privilege (outbound EC2 + inbound DB) | E,B | B,E | Correct |
| T1:Q14 | Multi-tenant DynamoDB cost allocation (CW Logs + Cost Explorer) | B | D | Wrong |
| T1:Q18 | RDS PostgreSQL DR (cross-Region replicas + automated backups) | A,C | A,C | Correct |
| T2:Q8 | Redshift historical data in S3 (Redshift Spectrum) | B | C | Wrong |
| T2:Q10 | RDS vs Aurora Multi-AZ + Read Replicas (sync/async/promotion) | C,E,F | C,E,F | Correct |
| T2:Q18 | Redshift KMS cross-Region snapshots (grant in dest Region) | D | B | Wrong |
| T2:Q21 | Serverless sensor ingest (SQS → Lambda → DynamoDB) | C | C | Correct |
| T2:Q24 | Aurora Auto Scaling + ALB routing (Replicas + Round Robin) | A,D | A,D | Correct |
| T2:Q36 | RDS DR plan (snapshots shareable + cross-Region + RTO def) | F,D,E | B,E,F | Wrong |
| T2:Q37 | Gaming leaderboard in-memory (ElastiCache Redis + DynamoDB DAX) | B,E | B,E | Correct |
| T2:Q38 | SAML + PowerUserAccess + deny RDS except us-east-1 | D | D | Correct |
| T2:Q39 | Global relational DB (Aurora Global Database) | B | B | Correct |
| T2:Q48 | Semi-structured event viz (Firehose → OpenSearch → Kibana) | D | D | Correct |
| T2:Q49 | DMS migration validation (DMS data validation) | B | B | Correct |
| T2:Q52 | Multi-AZ sync vs Read Replica async | D | D | Correct |
| T2:Q53 | Analytics offload cost-optimal (same-Region Read Replica) | A | A | Correct |
| T2:Q65 | DynamoDB anomaly detection (Streams → Lambda → KDS → KDA) | A | A | Correct |
| T2:Q69 | Redshift DR (CFN StackSet + cross-Region snapshot copy) | A | A | Correct |
| T3:Q3 | Cold Redshift data (S3 Standard-IA + Athena) | C,D | C,D | Correct |
| T3:Q12 | Reporting offload (Read Replica, not Multi-AZ standby) | C | C | Correct |
| T3:Q36 | DMS to Redshift (same Region + SG inbound rules) | A,D | C,D | Wrong |
| T3:Q44 | DynamoDB cost optimization (drop table + SQS buffer writes) | C,E | D,E | Wrong |
| T3:Q50 | FSx Single-AZ → Multi-AZ (new FSx + DataSync) | A | A | Correct |
| T3:Q51 | KCL checkpointing (DynamoDB only + separate table per app) | B,D | B,D | Correct |

### Weak Areas — Databases
1. **Aurora vs RDS for reliability** — Aurora MySQL (5x throughput, 6-way replication) > RDS MySQL Multi-AZ; Redis with replication > Memcached (no replication) for session HA
2. **Multi-tenant DynamoDB billing** — cost allocation tags are resource-level, not per-request; use structured CW Logs + Cost Explorer API proportional allocation
3. **Redshift Spectrum vs Athena** — Spectrum queries S3 FROM Redshift (can JOIN with Redshift tables); Athena is standalone S3 query engine (can't cross-reference Redshift)
4. **Redshift cross-Region snapshots** — snapshot copy grant in DESTINATION Region + KMS key in DESTINATION Region + configure in SOURCE Region; no "cross-Region replication" for Redshift
5. **RDS snapshot sharing** — only MANUAL snapshots shareable (up to 20 accounts); AUTOMATED snapshots cannot be shared directly
6. **Read Replica promotion is manual** — unlike Multi-AZ automatic failover; cross-Region failover requires manual promotion + app reconfiguration
7. **DMS to Redshift prerequisites** — same account + same Region; add replication instance IP to Redshift SG inbound; DMS auto-creates IAM only via console (not CLI/API)
8. **DynamoDB bulk delete** — drop entire table >> delete items one-by-one (avoids double throughput for scan+delete); max item size = 400 KB
9. **DynamoDB write buffering** — SQS queue smooths write peaks → lower provisioned WCU

## compute-load-balancing (dojo) — 2026-09-21/22 (20 core questions)
Score: 13/20 (65%)

| Q Ref | Topic | Your | Correct | Result |
|-------|-------|------|---------|--------|
| TD1:Q33 | ECS awsvpc network mode + SG on tasks + IAM roles | A | A | Correct |
| TD1:Q25 | NAT instance failure 50% → use NAT Gateway | A | A | Correct |
| TD1:Q16 | ASG suspend Terminate process for troubleshooting | C | A | Wrong |
| TD1:Q9 | Aurora auto-scale storage + ASG + Reserved EC2 | C | C | Correct |
| TD1:Q52 | Spot Fleet diversified allocation + Auto Scaling | C | C | Correct |
| TD1:Q21 | EFS mount + SSM patched AMI + CodeDeploy | C | C | Correct |
| TD1:Q57 | Lambda cost: migrate MySQL to RDS + API GW caching | C | A | Wrong |
| TD1:Q14 | S3 CRR + SQS + ASG for scalable storage/compute | D | D | Correct |
| TD2:Q4 | API GW + Lambda + Cognito + DynamoDB + S3 presigned | D | D | Correct |
| TD2:Q11 | Kinesis batch + DynamoDB WCU increase | A,D | B,D | Partial |
| TD1:Q30 | Compute Savings Plans + Spot for EKS peak | C | B | Wrong |
| TD1:Q24 | SSM Patch Manager + AWS Config AMI compliance | C,D | B,D | Partial |
| TD1:Q35 | SSM Parameter Store + CodeDeploy + IAM Service Role | C | C | Correct |
| TD1:Q49 | CloudFormation + ASG + Aurora retain + ALB | B | D | Wrong |
| TD1:Q61 | ECS Fargate secrets (Secrets Manager vs Parameter Store) | B | C | Wrong |
| TD1:Q68 | DDoS mitigation (CloudFront + ALB + WAF + Auto Scaling) | D,E | D,E | Correct |
| TD1:Q69 | ECS Anywhere for hybrid on-prem + Fargate cluster | B | D | Wrong |
| TD2:Q31 | Lambda@Edge User-Agent parsing for device-specific content | D | A | Wrong |
| TD2:Q34 | ALB AZ association (AZ not receiving traffic) | C | C | Correct |
| TD2:Q46 | ASG min 5/max 30 + 5 Reserved Instances (cost-optimize) | C | C | Correct |

### Weak Areas — Compute & Load Balancing
1. **ASG suspend vs EC2 termination protection** — EC2 termination protection does NOT prevent ASG from terminating; must suspend ASG "Terminate" process
2. **API Gateway caching vs CloudFront** — API caching is built into API Gateway (correct); CloudFront in front of API GW is unnecessary overhead
3. **Kinesis for Lambda throttling** — Kinesis data stream batches requests, reducing Lambda concurrency (TooManyRequestsException); increasing Lambda memory alone doesn't fix concurrency limits
4. **Compute vs EC2 Instance Savings Plans** — Compute SP = flexible across instance families (good for EKS); EC2 Instance SP = locked to family but higher discount. Spot for peak surges
5. **SSM Patch Manager vs GuardDuty** — Patch Manager = patching; GuardDuty = threat detection; Config = compliance rules (AMI approval)
6. **NLB vs ALB for web apps** — NLB = Layer 4 (TCP), no HTTP routing; ALB = Layer 7 (HTTP/HTTPS), path/header routing. Web apps need ALB
7. **Secrets Manager vs Parameter Store** — "lifecycle management + key rotation" = Secrets Manager; "config + secrets store" = Parameter Store
8. **ECS Anywhere vs Outposts** — ECS Anywhere = register on-prem in same ECS cluster as Fargate (lightweight); Outposts = expensive hardware, no Fargate support
9. **Lambda@Edge vs CloudFront User-Agent caching** — Lambda@Edge parses headers per-request; caching by User-Agent has terrible hit ratio (thousands of values). Route 53 cannot route by HTTP headers
10. **CloudFormation DeletionPolicy** — "retain" keeps resource on stack delete (fast recovery); "snapshot" requires restore time
11. **ASG right-sizing** — match min capacity to actual baseline utilization (20% of 25 = ~5), not the current instance count. RI only for baseline

## monitoring (dojo) — 2026-09-22 (14 core questions across 2 sessions; 19 non-core skipped)
Score: 11.5/14 (82%)

| Q Ref | Topic | Your | Correct | Result |
|-------|-------|------|---------|--------|
| TD1:Q2 | CloudWatch AWS/Usage + SERVICE_QUOTA() for quota monitoring | A | B | Wrong |
| TD1:Q12 | Unified CloudWatch agent + Logs Insights for EC2 logs | D | D | Correct |
| TD1:Q44 | CloudWatch agent on-prem + metric filter + alarm + SNS | D | D | Correct |
| TD1:Q74 | Resource-based policy cross-account + AWS Config audit | D | D | Correct |
| TD2:Q20 | NACL/SG for connectivity + AWS Config for history tracking | A,B | A,B | Correct |
| TD2:Q60 | CloudTrail logging + IAM read-only user for auditor | B | B | Correct |
| TD2:Q65 | CloudWatch StatusCheckFailed_System + EC2 recovery action | C | C | Correct |
| TD3:Q34 | CodeDeploy Canary + X-Ray active tracing for Lambda | B | B | Correct |
| TD3:Q41 | Inspector CVE + EventBridge 30-day cron + SSM Automation | A,B | B,D | Partial |
| TD4:Q16 | CloudTrail + IAM Access Analyzer for least-privilege audit | A,D | B,D | Partial |
| TD4:Q31 | CloudTrail object-level + EventBridge + Lambda (S3 public) | C | C | Correct |
| TD4:Q44 | EventBridge CreateUser pattern + Step Functions + SNS | A,E,F | D,E,F | Partial |
| TD5:Q44 | CloudTrail organizational trail in management account | B | B | Correct |
| TD5:Q45 | Config rule + SCP tag enforcement + Config aggregator | A,D,E | A,D,E | Correct |

### Weak Areas — Monitoring
1. **CloudWatch SERVICE_QUOTA()** — use AWS/Usage namespace + SERVICE_QUOTA(metricId) math for quota monitoring; Container Insights is for performance, not quota tracking
2. **Inspector vs Config vs SSM for CVE** — Inspector = CVE scanning; Config = configuration compliance only; SSM Agent alone can't run CVE scans. EventBridge cron for scheduled scans
3. **CloudTrail cannot send to SNS directly** — CloudTrail only logs events; EventBridge matches patterns and routes to SNS/Lambda/Step Functions
4. **IAM Access Analyzer needs CloudTrail trail first** — Access Analyzer reads CloudTrail logs to generate least-privilege policies; Audit Manager is for compliance frameworks (SOC2, PCI), not permissions
5. **EventBridge is the event router** — CloudTrail logs → EventBridge pattern match → target (SNS/Lambda/Step Functions). Never CloudTrail → SNS direct
