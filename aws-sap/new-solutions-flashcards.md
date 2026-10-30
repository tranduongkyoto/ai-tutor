# SAP-C02 Flashcards — Domain 2: Design for New Solutions (29%)

Built 2026-10-13, validated + TD6 cards added the same day. Updated 2026-10-30 with TD4, Neal A/B/C, Udemy #2 full, Official exam (+50 cards, A9–I12 → 122 total). New Solutions scores: TD5 36.4% → TD1 53.6% → TD2 50.0% → TD3 56.5% → Udemy3 58% → TD6 3/3. It's the biggest domain, so it's worth the most points.
Every card comes from a question you answered (source tag). 🔁 = missed 2+ times. Answers are folded, so say yours out loud first.

**Interactive version:** open `new-solutions-flashcards.html` in a browser (2 options per card, feedback, summary, saved rounds).

**How to use:** 1 round = all cards, ~50 min (or 🔁 only, ~20 min). Mark misses with ❌ in the log at the bottom. Round 2 = only ❌ cards (+2 days).

## A. Compute choice & limits

<details><summary><b>A1.</b> Event-driven job runs ~30 min per file. Least operational overhead?</summary>

Containerize it → **Fargate task** started by Lambda/EventBridge (`ecs:RunTask`). Lambda max = 15 min. An EC2 ASG on SQS depth also works when the stem says "cost-effective", but you still manage EC2. *(TD5 W14/W35, TD3 W1)*
</details>

<details><summary><b>A2.</b> Expose one function over HTTPS, simplest possible.</summary>

**Lambda Function URL**. ✗ Fargate + API Gateway + ALB = overbuilt. *(TD5 W73)*
</details>

<details><summary><b>A3.</b> Nightly HPC batch jobs, least overhead, cost matters.</summary>

**AWS Batch** managed compute environment on **Spot** + S3 for input/output. ✗ SQS + Spot ASG = a DIY scheduler; ✗ EKS/EFS. 🔁 *(TD1 W69)*
</details>

<details><summary><b>A4.</b> Tightly coupled HPC, max performance.</summary>

**Cluster placement group + EFA + FSx for Lustre** (lazy-load from S3). ✗ EFS as scratch. *(TD3 R12/R36)*
</details>

<details><summary><b>A5.</b> Dozens of small, intermittently used apps, each on its own instance.</summary>

Containerize → **ECS on EC2**, bin-pack the tasks behind one ALB, scale on memory. ✗ RIs sized to the ASG max. *(TD5 W49, Udemy2 R5)*
</details>

<details><summary><b>A6.</b> Instances take 20 min to boot because user data installs everything.</summary>

**Golden AMI** (Image Builder / SSM Automation `AWS-CreateImage`). *(TD5 R39)*
</details>

<details><summary><b>A7.</b> Stateful web tier on EC2 + Aurora must scale.</summary>

ALB + **sticky sessions** + ASG (or move state to ElastiCache). Aurora Auto Scaling adds **readers only**. ✗ NLB: only source-IP stickiness, no cookie-based sessions. *(TD5 W13, TD2 R48)*
</details>

<details><summary><b>A8.</b> Steady EC2 fleet + bursty Lambda + MemoryDB nodes. Cheapest commitment?</summary>

**EC2 Instance SP** (steady EC2, up to 72%) + **Compute SP** (Lambda) + **MemoryDB reserved nodes**. ✗ Compute SP for everything (never covers databases/caches). 🔁 *(TD6 W16)*
</details>

<details><summary><b>A9.</b> AWS Batch jobs need a custom AMI, jobs are restartable. Reduce management overhead and cost.</summary>

**Batch managed compute environment on EC2 Spot with the custom AMI**. ✗ Batch on Fargate Spot. Fargate cannot use a custom AMI. Restartable jobs tolerate Spot interruptions. *(Official Q54)*
</details>

<details><summary><b>A10.</b> Tightly coupled HPC: increase network throughput, reduce latency. Pick the instance/AMI settings.</summary>

**EFA-capable instances + cluster placement group (single AZ) + disable hyperthreading, HVM AMI**. ✗ Paravirtual (PV) AMI. PV is legacy and slower. Disabling hyperthreading helps tightly coupled HPC. 🔁 *(Official Q21)*
</details>

<details><summary><b>A11.</b> Grid computing: timeouts between instances, adding instances didn't help. LEAST effort fix?</summary>

**Relaunch the nodes from the AMI into a cluster placement group**. ✗ Enable ENA on the instances. Current instances already use ENA. The problem is inter-node latency. 🔁 *(Official Q58)*
</details>

<details><summary><b>A12.</b> Two EC2 behind an ALB slow down at unexpected sales peaks, no time pattern.</summary>

**Target tracking scaling on `ALBRequestCountPerTarget`**. ✗ Scheduled scaling for the peak hours. Scheduled actions only fit predictable peaks. *(Official Q17)*
</details>

<details><summary><b>A13.</b> SQS workers on EC2 don't scale well. MOST scalable scaling metric?</summary>

**Target tracking on backlog per instance (messages ÷ in-service instances, custom metric)**. ✗ Scale on `ApproximateNumberOfMessagesVisible`. Queue depth doesn't change in proportion to fleet size. FIFO + dedup removes duplicates. *(Official Q60)*
</details>

<details><summary><b>A14.</b> One EC2 instance (RI + On-Demand) must survive an AZ outage. MOST cost-effective?</summary>

**Spot Fleet mixing On-Demand baseline and Spot across AZs behind an ALB**. ✗ Auto Scaling group of On-Demand instances across AZs. All On-Demand works but costs more. All-Spot risks interruption. *(TD4 Q40)*
</details>

<details><summary><b>A15.</b> Always-on production tier in two Regions, failover within 1 minute. Capacity purchase?</summary>

**Active/passive ASG on zonal RIs + On-Demand, failover record with low TTL**. ✗ Active/active on Spot instances. Spot can be reclaimed — never for the always-on production baseline. 🔁 *(Neal A Q34)*
</details>

## B. Decoupling, serverless & workflow

<details><summary><b>B1.</b> Lambda functions overwhelm RDS with connections.</summary>

**RDS Proxy** + open the DB connection **outside the handler** (reuse it). Add SQS to buffer if writes spike. 🔁 *(TD5 W5/W58/R40)*
</details>

<details><summary><b>B2.</b> Spiky writes overwhelm a slow DB / throttle DynamoDB.</summary>

**SQS buffer** + consumer (Lambda or workers) that writes at a steady rate. ✗ Raise WCU or add EMR = costs more. *(TD3 W24/R21/R27)*
</details>

<details><summary><b>B3.</b> One noisy function starves the others of concurrency.</summary>

**Reserved concurrency** on that function. ✗ Separate account + SQS. *(TD2 W59)*
</details>

<details><summary><b>B4.</b> Too many Lambda invocations for the same reads behind API Gateway, cheapest fix.</summary>

**API Gateway caching**. ✗ CloudFront in front + DAX = new paid services. 🔁 *(TD1 W64)*
</details>

<details><summary><b>B5.</b> Multi-step order process that must track state.</summary>

**Step Functions** (+ DynamoDB). ✗ Lambda polling SQS on a schedule. *(TD2 W38)*
</details>

<details><summary><b>B6.</b> Delay one message by 2 min, others go immediately.</summary>

**Message timer** (`DelaySeconds` on send). A delay queue delays **every** message. *(Udemy2 W12)*
</details>

<details><summary><b>B7.</b> Notify by email when a batch finishes.</summary>

**SNS** email subscription. SQS can't send email. *(TD3 W19)*
</details>

<details><summary><b>B8.</b> React to new DynamoDB items.</summary>

**DynamoDB Streams → Lambda**. ✗ Scheduled polling. *(TD3 R67)*
</details>

<details><summary><b>B9.</b> Ordered queue, serverless consumer.</summary>

**SQS FIFO + Fargate/Lambda**. ✗ Amazon MQ (not serverless; only for JMS/AMQP). *(Udemy3 R15)*
</details>

<details><summary><b>B10.</b> Batch scripts → serverless microservices, each step takes seconds. MOST cost-effective orchestration?</summary>

**Lambda functions orchestrated by Step Functions**. ✗ Fargate containers orchestrated by Step Functions. Seconds-long steps fit Lambda's 15 min; Fargate costs more. EventBridge is not an orchestrator. *(Neal A Q15)*
</details>

<details><summary><b>B11.</b> Lambda metadata extraction takes 45 min per photo. Split by metadata type to cut time.</summary>

**Step Functions: Parallel state per metadata type, plus a workflow iterating over photos**. ✗ Lambda sends photos to SQS as the Step Functions input. SQS cannot directly start a Step Functions workflow. *(TD4 Q63)*
</details>

<details><summary><b>B12.</b> Serverless comments app (API Gateway + Lambda + DynamoDB) must show new comments in real time.</summary>

**AWS AppSync GraphQL subscriptions over WebSockets**. ✗ CloudFront caching of the API responses. Cached comments aren't new — real time needs push, not caching or polling. *(TD4 Q17)*
</details>

<details><summary><b>B13.</b> Sensor data → DynamoDB, fully serverless, no manual capacity planning.</summary>

**SQS + Lambda writing to DynamoDB (auto scaling)**. ✗ Kinesis Data Firehose writing directly to DynamoDB. DynamoDB is not a Firehose destination. KDS needs shard planning. 🔁 *(Udemy2 Q54)*
</details>

## C. Data, streaming & analytics

<details><summary><b>C1.</b> Many apps must read the SAME records and replay them.</summary>

**Kinesis Data Streams**. ✗ SQS — one consumer deletes the message. *(Udemy2 W8)*
</details>

<details><summary><b>C2.</b> Many KDS consumers are lagging.</summary>

**Enhanced Fan-Out** (2 MB/s per shard per consumer). ✗ Firehose — apps can't read from it. *(Udemy2 W1)*
</details>

<details><summary><b>C3.</b> IoT stream → transform → S3, minutes of latency OK.</summary>

IoT rule → **Data Firehose + Lambda transform**. ✗ Step Functions per data point. *(TD2 W24, Udemy3 R10)*
</details>

<details><summary><b>C4.</b> Near-real-time ingest + analytics, results in Redshift.</summary>

**KDS + consumers** → Redshift. Classic exam path for the Redshift hop = Firehose (Redshift streaming ingestion can also read KDS directly). ✗ S3 + SQS = batch-ish. *(TD3 W32, Udemy3 R27)*
</details>

<details><summary><b>C5.</b> ETL that new fields can extend with least overhead.</summary>

**Glue crawler + classifier + Glue ETL job**. ✗ Lambda → SQS → Fargate (every new field = redeploy). *(TD5 W1)*
</details>

<details><summary><b>C6.</b> One-off 8-hour EMR job, cheapest without losing data.</summary>

**On-Demand master + core**, **Spot task nodes**. ✗ Reserved (1–3 year term). 🔁 *(TD3 W20/W29)*
</details>

<details><summary><b>C7.</b> Query-heavy logs on S3 with Athena.</summary>

Store as **Parquet** + **partition** by hour/day. Raw archive → Deep Archive; Athena data stays in a queryable class. *(TD5 R37, Udemy2 R14)*
</details>

<details><summary><b>C8.</b> OpenSearch cost too high, old data rarely read.</summary>

Keep fewer **hot** nodes (ingest needs hot) + **UltraWarm** + ISM to **cold**; audit copy → Glacier Deep Archive. 🔁 *(TD5 W48)*
</details>

<details><summary><b>C9.</b> Read-heavy RDS MySQL, quick + cheap latency fix.</summary>

**ElastiCache** in front. RDS MySQL read replicas each have their own endpoint, no shared reader endpoint (Aurora has one). ✗ Migrate to Aurora = not quick. 🔁 *(TD3 W30, TD1 W25)*
</details>

<details><summary><b>C10.</b> Reports change once a day, read heavily.</summary>

Batch-generate to **S3 + CloudFront** with a daily TTL. ✗ ElastiCache cluster. *(TD1 W72)*
</details>

<details><summary><b>C11.</b> SQL on ORC files, queries only 6 PM–2 AM. Most cost-effective?</summary>

**S3 + Athena + Glue Data Catalog** (pay per TB scanned). ✗ Redshift = always-on cluster + loading for a nightly window. 🔁 *(TD6 W1)*
</details>

<details><summary><b>C12.</b> Bursty CPU-heavy read queries slow down Redshift. Cheapest fix?</summary>

**Concurrency scaling** (extra capacity only during bursts). ✗ Offload to EMR/RDS = overbuilt. *(TD6 R2)*
</details>

<details><summary><b>C13.</b> S3 data rarely read after 180 days, must be retrieved within 6 hours. MOST cost-effective?</summary>

**S3 Intelligent-Tiering Archive Access tier**. ✗ Intelligent-Tiering Deep Archive Access tier. Deep Archive Access can take up to 12 h. Match the SLA first, then the cheapest tier. *(Official Q9)*
</details>

<details><summary><b>C14.</b> DynamoDB on-demand, bursts, a few hot keys read repeatedly. Cut cost, LEAST overhead.</summary>

**DAX for hot keys + provisioned capacity with auto scaling (or reserved capacity)**. ✗ DAX + Savings Plans. Savings Plans never cover DynamoDB (EC2/Fargate/Lambda/SageMaker only). 🔁 *(Official Q68)*
</details>

<details><summary><b>C15.</b> Dev DynamoDB provisioned for peak, write-heavy, 2x weekend peak. Optimize cost.</summary>

**On-demand capacity only**. ✗ On-demand capacity + DAX. DAX caches reads only — it never helps writes. No hot data = pure extra cost. 🔁 *(Neal C Q7)*
</details>

<details><summary><b>C16.</b> DynamoDB auto scaling at 70%; predictable spike to 300% causes throttling.</summary>

**Application Auto Scaling scheduled action to raise capacity before the spike**. ✗ Retry throttled writes from a DLQ / rely on target tracking. Target tracking and step scaling react after the breach; predictable spikes need capacity ready. *(Neal B Q17)*
</details>

<details><summary><b>C17.</b> Gaming leaderboard: in-memory, single-digit ms, highly available.</summary>

**ElastiCache for Redis (sorted sets) or DynamoDB + DAX**. ✗ Plain DynamoDB tables. DynamoDB alone is disk-based, not in-memory. *(Udemy2 Q59)*
</details>

## D. Edge, delivery & media

<details><summary><b>D1.</b> CloudFront returns 504 when the origin is down. Minimal cost.</summary>

**Origin group** (origin failover) + Lambda@Edge for auth near users. ✗ Multi-Region app + latency routing. 🔁 *(TD1 W17)*
</details>

<details><summary><b>D2.</b> Custom domain on CloudFront with HTTPS.</summary>

**ACM cert in us-east-1** on the distribution + HTTPS to the origin with a matching cert. The default cert only covers `*.cloudfront.net`. *(TD3 W23/W50)*
</details>

<details><summary><b>D3.</b> ALB serves many different domains, no cert rework per new domain.</summary>

**SNI**: multiple certs on one HTTPS listener. Wildcard = sub-domains of one domain only. *(TD3 W10)*
</details>

<details><summary><b>D4.</b> Data in eu bucket, NA users slow. Global Accelerator?</summary>

No. **GA can't front S3**. Use **S3 CRR** to a US bucket + Lambda@Edge to switch the origin. 🔁 *(TD5 W12)*
</details>

<details><summary><b>D5.</b> Shift traffic fast but clients cache DNS.</summary>

**Global Accelerator** endpoint weights / traffic dials (anycast IPs, no DNS change). ✗ Route 53 weighted. *(Udemy2 W20)*
</details>

<details><summary><b>D6.</b> Route each user to one specific EC2 instance deterministically.</summary>

**GA custom routing accelerator** + VPC subnet endpoints. ✗ NLB (load-balances). *(Udemy3 W26)*
</details>

<details><summary><b>D7.</b> Video-on-demand to many devices.</summary>

**MediaConvert** (adaptive-bitrate renditions) + **HLS** + CloudFront. ✗ S3 + CloudFront alone (no transcoding). ✗ Jenkins on EC2. *(Udemy3 W11, TD5 W72)*
</details>

<details><summary><b>D8.</b> Different content for mobile vs desktop.</summary>

**Lambda@Edge** (or CloudFront + Lambda@Edge + ALB). *(TD2 R6, Udemy3 R23)*
</details>

<details><summary><b>D9.</b> Only one specific partner may download files.</summary>

**Signed URLs** (1 file) / **signed cookies** (many files) + block direct S3. OAC alone still lets anyone with the CloudFront URL in. *(TD2 W44, Udemy2 R25)*
</details>

<details><summary><b>D10.</b> Normalize query strings / rewrite headers at the edge, least overhead and cost.</summary>

**CloudFront Functions** (viewer request, sub-ms, cheapest). Lambda@Edge only when you need network calls, the body, or a longer runtime. 🔁 *(TD6 W11)*
</details>

<details><summary><b>D11.</b> Global app on custom TCP ports 5000/8080, latency routing, data synced worldwide.</summary>

**NLB** per Region (ALB = HTTP/HTTPS only) + Route 53 latency + **DynamoDB global tables**. *(TD6 R8)*
</details>

<details><summary><b>D12.</b> A/B test two site versions in two S3 buckets behind CloudFront; users must not notice.</summary>

**Lambda@Edge on origin request picks the origin (cookie/request attributes)**. ✗ Path-based cache behaviors + redirects. Different paths and redirects are visible to users. *(Official Q38)*
</details>

<details><summary><b>D13.</b> CloudFront default origin = ALB; S3 static assets with OAC return 404.</summary>

**Add an S3 origin + a path-pattern cache behavior in CloudFront**. ✗ ALB listener path rule forwarding to S3. OAC lets only CloudFront read S3; an ALB cannot forward to S3. *(TD4 Q41)*
</details>

<details><summary><b>D14.</b> Serverless upload app, users in many Regions, low latency. API Gateway Regional + S3 today.</summary>

**API Gateway edge-optimized endpoint + S3 Transfer Acceleration**. ✗ Global Accelerator in front of CloudFront. GA fronts ALB/NLB/EC2/EIP only — never CloudFront or S3. 🔁 *(Udemy2 Q13)*
</details>

## E. Security design

<details><summary><b>E1.</b> Company must own the S3 key and rotate it.</summary>

**SSE-KMS** with a customer managed key; transit → `aws:SecureTransport` bucket policy. ✗ SSE-S3 (AWS owns the keys). *(TD3 W13)*
</details>

<details><summary><b>E2.</b> Key material comes from the company's own on-prem HSM.</summary>

KMS key with **Origin = EXTERNAL** + import key material. ✗ CloudHSM key store (that's AWS CloudHSM). *(TD3 W28)*
</details>

<details><summary><b>E3.</b> Keys must never leave a dedicated HSM, highly available.</summary>

**CloudHSM cluster across ≥2 AZs** (+ TCP LB pass-through). One HSM = single point of failure. *(TD1 W47)*
</details>

<details><summary><b>E4.</b> API Gateway: only IAM users/roles, trace each request end-to-end.</summary>

**AWS_IAM authorization** (SigV4) + **X-Ray**. CORS isn't authentication. *(TD3 W7)*
</details>

<details><summary><b>E5.</b> App tier → DB access, least privilege.</summary>

**SG-to-SG reference** (DB SG inbound from the app SG). ✗ NACL with the subnet CIDR. *(TD3 W55)*
</details>

<details><summary><b>E6.</b> Prevent man-in-the-middle on a public site.</summary>

**Route 53 DNSSEC** + **ACM cert** on the ALB + CloudFront HTTP→HTTPS redirect. *(TD1 W68)*
</details>

<details><summary><b>E7.</b> DB password rotated automatically, used by ECS tasks.</summary>

**Secrets Manager** referenced in the task definition `secrets` (`valueFrom`) + task execution role. ✗ Parameter Store (no built-in rotation). 🔁 *(TD1 W74)*
</details>

<details><summary><b>E8.</b> Public website on ALB/CloudFront needs a TLS cert.</summary>

**Public ACM cert (free)** on ALB/CloudFront. ✗ ACM Private CA (monthly fee). Classic public ACM certs can't be exported; since 2025 ACM also sells *exportable* public certs (paid), but on the exam "free + integrated" = ACM on the ALB/CloudFront. *(TD2 W1)*
</details>

<details><summary><b>E9.</b> Find CVEs in Lambda functions + layers, code-scan only some functions.</summary>

**Inspector standard scanning** (packages/layers) + **code scanning** + `InspectorCodeExclusion` tag on the skipped functions. ✗ IAM to exclude targets. *(TD6 W6)*
</details>

<details><summary><b>E10.</b> Lambda functions share hardcoded RDS credentials. Improve security, LEAST development effort.</summary>

**Secrets Manager with managed rotation**. ✗ Parameter Store + EventBridge-driven custom rotation. Parameter Store has no native RDS rotation — you'd build it yourself. 🔁 *(Official Q11)*
</details>

<details><summary><b>E11.</b> Remove open SSH/RDP and bastions, log commands per session, keep port forwarding.</summary>

**Systems Manager Session Manager (close port 22, logs to S3/CloudWatch)**. ✗ Client VPN or EC2 Instance Connect. VPN keeps SSH open, no session logs; Instance Connect still needs port 22. 🔁 *(Official Q53, Neal A Q5/Q53)*
</details>

<details><summary><b>E12.</b> FIPS 140-2 Level 3 keys, needed only in business hours, HA. MOST cost-effective?</summary>

**CloudHSM multi-AZ cluster; delete/restore from backup outside hours**. ✗ KMS key with scheduled disable/enable. Exam treats KMS as Level 2. (Real AWS: KMS reached Level 3 in 2023 — answer CloudHSM.) 🔁 *(Official Q70)*
</details>

<details><summary><b>E13.</b> Millions of unencrypted S3 objects, many apps use the bucket. Find PII, encrypt, LEAST effort.</summary>

**Default encryption + S3 Inventory + Batch Operations copy-in-place; Macie finds PII**. ✗ Copy everything to a new encrypted bucket. A new bucket forces every application to change bucket names. *(Official Q43)*
</details>

<details><summary><b>E14.</b> S3 behind CloudFront: encrypt in transit and at rest.</summary>

**Default encryption + bucket policy denying unencrypted PutObject + CloudFront HTTP→HTTPS redirect**. ✗ `aws:SecureTransport` condition in S3 ACLs. ACLs can't hold condition keys — only bucket policies can. *(Neal C Q12)*
</details>

<details><summary><b>E15.</b> PII on SSE-S3 today; security team must manage keys for current and future objects.</summary>

**SSE-KMS customer managed key + deny unencrypted PutObject + re-copy existing objects**. ✗ SSE-S3 with a customer managed key. SSE-S3 keys are always AWS-owned; that option is impossible. 🔁 *(Neal C Q19)*
</details>

<details><summary><b>E16.</b> ECS behind ALB suffers attacks causing outages. Prevent attacks, MOST cost-effective.</summary>

**CloudFront + WAF web ACL + custom-header origin lock on the ALB**. ✗ Auto scaling + DAX. Scaling and caching absorb load; they don't stop attacks or bypass to the ALB. 🔁 *(Neal C Q13)*
</details>

<details><summary><b>E17.</b> Serverless global app: low latency + baseline DDoS protection for S3 content.</summary>

**CloudFront (Shield Standard included) in front of S3**. ✗ WAF web ACL for DDoS. WAF filters L7 rules (SQLi/XSS); baseline DDoS comes free with CloudFront. 🔁 *(Neal B Q22)*
</details>

<details><summary><b>E18.</b> NLB with instance-id targets, targets healthy, but office users can't connect.</summary>

**Allow the office CIDR in the EC2 security group**. ✗ Allow the NLB subnets in the EC2 security group. Instance-id targets preserve the client IP. Healthy targets = health check already open. 🔁 *(Neal C Q30)*
</details>

<details><summary><b>E19.</b> Interface endpoints in private subnets, private IPs only, connections fail. Configuration fix?</summary>

**Endpoint ENI security group allows 443 from the VPC (+ private DNS)**. ✗ Add a route table entry for the endpoint. Interface endpoints are ENIs reached via DNS; only gateway endpoints use route tables. *(Neal C Q9)*
</details>

<details><summary><b>E20.</b> Regional REST API hit by botnets; only a few known US companies call it twice daily. Minimum cost.</summary>

**WAF IP allow-list on the API + usage plan and API key**. ✗ CloudFront + WAF per-day rate-based rule. Rate rules use short windows, not per day; CloudFront adds cost. 🔁 *(Neal A Q41)*
</details>

<details><summary><b>E21.</b> HA EC2 app: filter common exploits, send rejected requests to a third-party audit tool.</summary>

**Multi-AZ ASG behind ALB + WAF managed rules + WAF logging to Firehose**. ✗ WAF logs via CloudWatch + Lambda polling, no multi-AZ ASG. Firehose can deliver WAF logs to third-party endpoints; HA needs a multi-AZ ASG. *(Neal A Q17)*
</details>

<details><summary><b>E22.</b> Detect an API action (CreateUser, public-read PutObject), notify and auto-remediate.</summary>

**CloudTrail event → EventBridge rule → Step Functions/Lambda remediate + SNS notify**. ✗ CloudTrail alone or S3 event notifications. CloudTrail doesn't notify; S3 events can't filter on ACL. 🔁 *(TD4 Q5, Udemy2 Q63)*
</details>

## F. Identity for apps

<details><summary><b>F1.</b> Mobile/SPA app with Google/Facebook login reads DynamoDB.</summary>

**Cognito** / **web identity federation** → temporary STS creds scoped to the user's items. ✗ Long-term keys in the app. 🔁 *(TD1 W21/W65, TD3 W57)*
</details>

<details><summary><b>F2.</b> Corporate SAML IdP users need AWS access.</summary>

**IAM Identity Center** / `AssumeRoleWithSAML`. ✗ WebIdentity (that's social IdPs). 🔁 *(TD2 W31)*
</details>

<details><summary><b>F3.</b> GitHub Actions deploys to AWS.</summary>

**IAM OIDC identity provider** + role trusting `sts:AssumeRoleWithWebIdentity`. *(TD5 R70)*
</details>

<details><summary><b>F4.</b> WorkSpaces users sign in with on-prem AD; credentials must not be stored outside the company.</summary>

**AD Connector (proxy, no caching)**. ✗ AWS Managed Microsoft AD with a trust. Managed AD is a real directory — credentials then live in AWS. *(Official Q32)*
</details>

<details><summary><b>F5.</b> Mobile app with custom authentication must get IAM role credentials. Pick the federation path.</summary>

**OIDC IdP + Cognito identity pool, or SAML assertion via an IAM SAML IdP**. ✗ LDAP connector + API Gateway Lambda authorizer issuing JWTs. Authorizers only authorize API calls; they never issue AWS credentials. *(Neal B Q51)*
</details>

<details><summary><b>F6.</b> Security team wants all identities central across prod/test accounts.</summary>

**IAM users in one identity account; roles in target accounts trust that account**. ✗ IAM users in every account restricted with SCPs. SCPs only restrict, never grant; users stay scattered. 🔁 *(Neal B Q56)*
</details>

## G. Reliability & DR

<details><summary><b>G1.</b> Pick the DR tier: RTO hours / tens of minutes / minutes / ~0.</summary>

Backup & restore / **pilot light** / **warm standby** / multi-site active-active. Pilot light still has to build the web/app tiers → it can't meet a 5-min RTO. *(TD2 W9)*
</details>

<details><summary><b>G2.</b> RTO 30 min, cost-effective.</summary>

Backup/restore for the stateless tiers (AMIs/snapshots) + **cross-Region read replica** for the DB. ✗ Hot standby. 🔁 *(TD3 W16)*
</details>

<details><summary><b>G3.</b> RTO < 1 h, RDS cross-Region.</summary>

**Cross-Region read replica + automated promotion + Route 53 failover**. ✗ Snapshot restore. *(TD5 W9/W61)*
</details>

<details><summary><b>G4.</b> RPO < 1 min cross-Region relational.</summary>

**Aurora Global Database**. *(TD5 R53, TD3 R15)*
</details>

<details><summary><b>G5.</b> Multi-Region active-active writes, NoSQL.</summary>

**DynamoDB global tables**. Aurora Global = one writer Region. *(TD1 R16, TD3 R38)*
</details>

<details><summary><b>G6.</b> Is RDS Multi-AZ a DR plan?</summary>

No. Multi-AZ = HA in one Region. DR = backups/replica in **another Region**. 🔁 *(TD2 W14)*
</details>

<details><summary><b>G7.</b> Active-active Regions vs active-passive in Route 53.</summary>

Active-active → **latency + Evaluate Target Health**. Active-passive → **failover**. Weighted ≠ failover. *(TD5 W42/W61, TD3 R43)*
</details>

<details><summary><b>G8.</b> Health check for a resource with only a private IP.</summary>

CloudWatch metric → **alarm** → Route 53 health check **on the alarm state**. Route 53 checkers can't reach private IPs. *(Udemy3 W21)*
</details>

<details><summary><b>G9.</b> Multi-Region API Gateway: reroute automatically on full AND partial failures from CloudWatch metrics.</summary>

**Route 53 ARC routing controls driven by alarms + Lambda**. ✗ Route 53 Evaluate Target Health. Evaluate Target Health sees only the endpoint record, not partial failures inside the microservices. *(Official Q16)*
</details>

<details><summary><b>G10.</b> Multi-AZ app with one NAT gateway and DynamoDB tables. Increase resilience.</summary>

**One NAT gateway per AZ**. ✗ DynamoDB global tables. DynamoDB is already multi-AZ. The single NAT gateway is the zonal SPOF. *(Official Q19)*
</details>

<details><summary><b>G11.</b> Protect S3, EBS, EFS, RDS, Volume Gateway against a Regional outage, LEAST overhead.</summary>

**AWS Backup plan with cross-Region copy to a vault in another Region**. ✗ AWS Backup plus RDS cross-Region read replicas. Replicas aren't backups and add overhead; AWS Backup already covers RDS. *(Official Q25)*
</details>

<details><summary><b>G12.</b> Aurora Global Database: local low-latency reads with read-after-write consistency, test DR.</summary>

**Write forwarding on the secondary + managed (planned) failover for DR tests**. ✗ Read from the secondary, write to the primary. Secondary reads may be stale and break read-after-write. *(Official Q45)*
</details>

<details><summary><b>G13.</b> SLA 99.5%, minimize changes and cost; remote users find the desktop client slow.</summary>

**Keep RDS single-AZ; stream the client with AppStream 2.0**. ✗ Add RDS Multi-AZ + ElastiCache. Single-AZ already meets 99.5%; a cache doesn't fix a slow remote desktop client. 🔁 *(Neal C Q5)*
</details>

<details><summary><b>G14.</b> 99.9% SLA, or HA across three AZs, for an app with PostgreSQL. Users in Europe/US.</summary>

**One Region: Aurora writer + replicas in other AZs; CloudFront for global latency**. ✗ Two Regions with Aurora Global Database. Aurora Global is cross-Region DR — overbuilt for a single-Region SLA. 🔁 *(Neal B Q61/Q63)*
</details>

<details><summary><b>G15.</b> EKS stateless pods, highly variable load. Optimize node resilience.</summary>

**Topology spread constraints across AZs + node groups in multiple AZs**. ✗ Cluster Autoscaler with under-provisioning. Resilience = survive an AZ failure; autoscaler sizing is capacity, not fault tolerance. *(Neal C Q11)*
</details>

<details><summary><b>G16.</b> RDS Multi-AZ failover 40 s → under 20 s, keep connections alive, queue writes.</summary>

**RDS Proxy + Aurora with Aurora Replicas**. ✗ Redis cache + RDS MySQL read replicas. Caches can't queue writes; RDS replicas don't give fast failover. 🔁 *(TD4 Q28)*
</details>

<details><summary><b>G17.</b> KMS-encrypted Redshift: RPO 24 h, RTO 1 h, survive a Regional outage.</summary>

**Cross-Region snapshot copy; snapshot copy grant for a key in the DESTINATION Region**. ✗ Redshift replication to a cluster in another Region / grant in source Region. Redshift has no cross-Region replication. KMS keys are Regional. 🔁 *(TD4 Q64, Udemy2 Q33)*
</details>

<details><summary><b>G18.</b> Single Direct Connect for business-critical traffic. MOST resilient connectivity?</summary>

**Second DX connection, different carrier/location, same Region**. ✗ VPN backup or a new DX to another Region. VPN is low-bandwidth backup; DX to another Region isn't redundancy for this one. 🔁 *(Neal A Q56, Neal C Q31, Udemy2 Q67)*
</details>

<details><summary><b>G19.</b> One data center needs low-latency links to VPCs in US East and US West.</summary>

**One DX connection + Direct Connect gateway with a VGW per VPC (private VIFs)**. ✗ A separate DX connection per Region. A DX gateway is global — one connection reaches VPCs in many Regions. 🔁 *(TD4 Q58, Neal C Q31)*
</details>

## H. Deployment

<details><summary><b>H1.</b> Keep full capacity during a Beanstalk deploy.</summary>

**Immutable** or **blue/green** (swap CNAMEs). ✗ All-at-once / Rolling. *(TD3 W53/R54)*
</details>

<details><summary><b>H2.</b> Lambda traffic shift with automatic rollback.</summary>

**SAM + CodeDeploy** canary/linear + CloudWatch alarms. Canary = 2 steps; linear = many. *(Udemy2 R18, TD3 R31)*
</details>

<details><summary><b>H3.</b> Replace ASG instances on a CloudFormation update.</summary>

**UpdatePolicy `AutoScalingRollingUpdate`** (✗ CreationPolicy). DeletionPolicy: **Snapshot** for RDS, **Retain** for S3. *(TD3 R46, TD1 R45)*
</details>

<details><summary><b>H4.</b> Runbook describes install and config steps. LEAST overhead, must allow future changes.</summary>

**CloudFormation for infra + user data / cfn-init for install; change via stack updates**. ✗ CloudFormation for infra, keep manual runbook steps for software. Automate the whole runbook, not just the infrastructure. *(Official Q30)*
</details>

## I. Service fit (managed > DIY)

<details><summary><b>I1.</b> Sensors speak MQTT to a self-managed broker on EC2.</summary>

**AWS IoT Core** endpoint + IoT rule → DynamoDB. ✗ Scaling your own broker. *(TD3 W26)*
</details>

<details><summary><b>I2.</b> Offline ML inference on a local server at the edge.</summary>

**IoT Greengrass** (+ components). *(TD2 W32)*
</details>

<details><summary><b>I3.</b> Speech → text → another language → speech.</summary>

**Transcribe** → **Translate** → **Polly**. *(TD2 W50)*
</details>

<details><summary><b>I4.</b> Contact center + conversational bot.</summary>

**Amazon Connect + Lex** (+ Lambda for backends). *(TD1 W62)*
</details>

<details><summary><b>I5.</b> Scanned forms, extract fields, reduce human work.</summary>

**Textract** (+ Comprehend, orchestrated by Step Functions). Rekognition isn't document OCR. *(TD3 R11)*
</details>

<details><summary><b>I6.</b> Archived video must get face tagging.</summary>

**File Gateway → S3** + **Rekognition** face collection via Lambda. ✗ Tape Gateway (it's for backup, not processing). 🔁×3 *(TD1 W57, TD3 W14)*
</details>

<details><summary><b>I7.</b> Stream desktop apps to users vs full desktops.</summary>

Apps → **AppStream 2.0**. Full per-user desktops → WorkSpaces (costs more). *(TD3 W63)*
</details>

<details><summary><b>I8.</b> Legacy app sends mail over SMTP.</summary>

**SES SMTP credentials** + SES SMTP endpoint, port 587 STARTTLS. An IAM role doesn't work for SMTP. *(TD5 W74)*
</details>

<details><summary><b>I9.</b> Blockchain ledger that holds PII.</summary>

**Hash on-chain, PII off-chain** (DynamoDB). Immutable chain = can't delete PII. *(TD5 R25)*
</details>

<details><summary><b>I10.</b> PHP LAMP app, developer with little AWS skill, stable traffic, predictable pricing.</summary>

**Amazon Lightsail**. ✗ Elastic Beanstalk + DynamoDB. Pay-per-resource pricing and a new NoSQL DB break the asks. *(Official Q73)*
</details>

<details><summary><b>I11.</b> On-prem apps on several servers share static files over NFS; move to S3, one copy.</summary>

**S3 File Gateway**. ✗ Volume Gateway (iSCSI). Volume Gateway stores block volumes, not S3 objects, and can't be shared like NFS. 🔁 *(Official Q61)*
</details>

<details><summary><b>I12.</b> 350 remote staff need full Windows/Linux desktops with on-prem AD and MFA.</summary>

**WorkSpaces + AD Connector + RADIUS MFA**. ✗ AppStream 2.0. AppStream streams apps, not full desktops. 🔁 *(Neal B Q35)*
</details>

## Round log

| Round | Date | Score | ❌ cards |
|---|---|---|---|
| 1 | 2026-10-13 | 69/72 (96%) | D11, H3, A3 🔁 |
| 2 (due 10-15) | | /3 | |
| 3 (due 10-31) | | /122 | |
