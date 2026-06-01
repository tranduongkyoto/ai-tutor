# Serverless — Learn and Test (Phase 1)
**Date:** 2026-05-31 11:36
**Score:** 18/18 (100%) — All 7 sections complete
**Status:** Complete

---

## Section 1: Service Overview

### AWS Lambda
Virtual functions — no servers to manage. Event-driven, on-demand execution with automated scaling. Pay per request + compute time.

| Feature | Detail |
|---------|--------|
| Max execution time | 900 seconds (15 minutes) |
| Memory | 128 MB — 10 GB (1 MB increments) |
| /tmp storage | 512 MB — 10 GB |
| Concurrent executions | 1,000 per region (can increase) |
| Deployment package | 50 MB compressed, 250 MB uncompressed |
| Environment variables | 4 KB total |

**Key behaviors:**
- Increasing RAM also improves CPU and network quality
- **Cold starts**: new instance loads init code; mitigated by Provisioned Concurrency or SnapStart (Java/Python/.NET)
- **SnapStart**: pre-initializes function from snapshot — 10x performance improvement, no extra cost
- Default Lambda runs in AWS-owned Virtual Private Cloud (VPC) — cannot access private resources (Relational Database Service (RDS), ElastiCache)
- To access private resources: deploy Lambda in customer VPC (adds Elastic Network Interface (ENI) creation latency)

**Language support:** Node.js, Python, Java, C# (.NET), Ruby, Custom Runtime API (Rust, Go), Lambda Container Image (must implement Lambda Runtime API). For arbitrary Docker: use Elastic Container Service (ECS)/Fargate, NOT Lambda.

**Invocation types:**
- **Synchronous**: caller waits for response; ThrottleError 429 on limit
- **Asynchronous**: auto-retries (exponential backoff 1s → 5min, up to 6 hours); goes to Dead Letter Queue (DLQ) after exhaustion

### Amazon API Gateway
Expose Lambda/HTTP/AWS services as REST API with HTTPS. Supports WebSocket, versioning, environments (dev/test/prod), authentication, API keys, throttling, request/response transformation.

**Endpoint types:**
| Type | Use Case | TLS Certificate Region |
|------|----------|----------------------|
| Edge-Optimized (default) | Global clients, routed through CloudFront | us-east-1 |
| Regional | Same-region clients | Same region as API Gateway |
| Private | VPC-only access via Interface Endpoint | Same region |

**Integrations:** Lambda Function, HTTP (on-premises, Application Load Balancer (ALB)), AWS Service (Step Functions, Simple Queue Service (SQS)).

### AWS Step Functions
Serverless visual workflow to orchestrate Lambda functions. Supports sequence, parallel, conditions, timeouts, error handling, and human approval. Integrates with Elastic Compute Cloud (EC2), ECS, on-premises, API Gateway, SQS.

### Amazon Cognito

**Cognito User Pools (CUP):**
- Sign-in functionality: username/password, email, Multi-Factor Authentication (MFA), federated identities (Facebook, Google, SAML)
- Integrates with API Gateway and Application Load Balancer (ALB) for token verification
- Flow: Client → CUP → token → API Gateway/ALB verifies token

**Cognito Identity Pools (Federated Identity):**
- Get **temporary AWS credentials** for users to access AWS resources directly
- Sources: User Pools, third-party logins (Google, Facebook, SAML, OpenID)
- IAM policies customizable by user_id for fine-grained control
- Default roles: authenticated and guest
- **Row-level security**: policy conditions check `cognito-identity.amazonaws.com:sub`

**Critical distinction:** User Pools = sign-in/authentication. Identity Pools = direct AWS access with temporary credentials.

### CloudFront Functions vs Lambda@Edge

| Feature | CloudFront Functions | Lambda@Edge |
|---------|---------------------|-------------|
| Runtime | JavaScript only | Node.js, Python |
| Requests/sec | Millions | Thousands |
| Triggers | Viewer Request/Response only | Viewer + Origin Request/Response |
| Execution time | < 1 ms | 5-10 seconds |
| Memory | 2 MB | 128 MB — 10 GB |
| Package size | 10 KB | 1 MB — 50 MB |
| Network/file access | No | Yes |
| Request body access | No | Yes |
| Pricing | 1/6th cost of Lambda@Edge | Per request + duration |

**CloudFront Functions use cases:** cache key normalization, header manipulation, URL rewrites, JWT validation.
**Lambda@Edge use cases:** longer execution, third-party libraries, network access, file system access.

### Quiz: Section 1
**Q1** ✓ — cognito-identity-pools
Mobile app needs direct S3 uploads per-user. Which Cognito feature provides temporary AWS credentials?
A) User Pools with S3 policy B) Identity Pools (temp AWS credentials + IAM) C) API Gateway proxying D) Lambda pre-signed URLs
💡 Hint: User Pools = tokens. Which feature gives actual AWS credentials?
**Your answer: B** — Correct. Identity Pools provide temporary AWS credentials with IAM policies scoped per user.

**Q2** ✓ — lambda-vpc
Lambda with default settings fails to connect to Aurora in private subnet. Root cause?
A) Missing IAM permissions B) Default Lambda outside VPC C) Aurora SG needs Lambda IPs D) Lambda requires RDS Proxy
💡 Hint: Where does Lambda run by default?
**Your answer: B** — Correct. Default Lambda runs in AWS-owned VPC, cannot reach private resources.

**Q3** ✓ — cloudfront-functions
JWT validation at edge, sub-millisecond, millions req/s, no network needed. Which edge compute?
A) Lambda@Edge B) CloudFront Functions C) API Gateway Authorizer D) WAF rules
💡 Hint: Simple logic, <1ms, millions req/s, no network.
**Your answer: B** — Correct. CloudFront Functions: JS, <1ms, millions req/s, perfect for simple JWT validation.

---

## Section 2: Real-World Use Cases

### When to Use Which Serverless Service
- REST API with unpredictable traffic → API Gateway + Lambda + DynamoDB
- User authentication for mobile/web → Cognito User Pools
- Direct S3 access from client → Cognito Identity Pools (temporary credentials)
- Scheduled background jobs → EventBridge/CloudWatch Events + Lambda
- Visual workflow orchestration → Step Functions
- Real-time reaction to data changes → DynamoDB Streams + Lambda
- Lightweight edge processing (URL rewrite, JWT) → CloudFront Functions
- Complex edge processing (third-party libs, network) → Lambda@Edge

### Real-World Scenarios
1. **Mobile App Backend**: API Gateway (REST HTTPS) + Cognito (auth) + Lambda (logic) + DynamoDB (data) + S3 (file uploads via Cognito Identity Pools)
2. **Image Processing Pipeline**: S3 upload → Lambda trigger → create thumbnail → save to S3 + metadata to DynamoDB → notify via Simple Notification Service (SNS)/Simple Queue Service (SQS)
3. **Scheduled Reports**: EventBridge rule (every 6 hours) → Lambda → query DynamoDB → generate report → store in S3
4. **Welcome Email Flow**: User inserted in DynamoDB → DynamoDB Streams → Lambda → Simple Email Service (SES) sends welcome email
5. **Global Blog**: CloudFront (static from S3 with Origin Access Control (OAC)) + API Gateway + Lambda + DynamoDB Global Tables + DynamoDB Accelerator (DAX) for read caching

### Quiz: Section 2
**Q1** ✓ — eventbridge-lambda
Daily report at 2 AM, queries DynamoDB, writes CSV to S3, no servers. Which combination?
A) EC2 + cron B) EventBridge schedule → Lambda C) Step Functions wait → Lambda D) SQS scheduled → Lambda
💡 Hint: "Scheduled task" + "serverless" = serverless cron.
**Your answer: B** — Correct. EventBridge scheduled rule = serverless cron.

**Q2** ✓ — s3-lambda-trigger
Photo upload to S3 → auto-generate thumbnail → save to output bucket + DynamoDB metadata. Which pattern?
A) S3 event → Lambda → thumbnail + DynamoDB B) CloudWatch polling → Lambda C) API Gateway → Lambda → S3 D) SQS → ECS Fargate
💡 Hint: S3 natively triggers Lambda on object events.
**Your answer: A** — Correct. S3 event notifications → Lambda is the native file processing pattern.

---

## Section 3: Service Integrations

### Lambda + DynamoDB
- Lambda reads/writes DynamoDB directly (IAM role on Lambda)
- DynamoDB Streams → Lambda trigger for real-time reactions (INSERT, MODIFY, REMOVE)
- DynamoDB Accelerator (DAX) between Lambda and DynamoDB for microsecond read caching (no code change)

### Lambda + Relational Database Service (RDS)
- Lambda in VPC → RDS Proxy → RDS/Aurora (connection pooling)
- RDS Proxy reduces failover by 66%, enforces IAM auth, credentials in Secrets Manager
- RDS Proxy is **never publicly accessible** — VPC only
- Lambda must be deployed in VPC to use RDS Proxy

### Lambda + API Gateway
- API Gateway invokes Lambda synchronously
- API Gateway handles auth (Cognito, IAM, Custom Authorizer), throttling, caching
- API Gateway response caching reduces Lambda invocations

### Lambda + Simple Storage Service (S3)
- S3 event notifications trigger Lambda (PUT, DELETE, etc.)
- Common pattern: S3 upload → Lambda processes → output to S3/DynamoDB
- S3 Transfer Acceleration for global uploads

### Lambda + Step Functions
- Step Functions orchestrate multiple Lambda functions
- Supports: sequence, parallel, branching, error handling, retries, timeouts
- Human approval steps supported
- Use case: order fulfillment, data processing workflows

### Invoking Lambda from RDS & Aurora
- Supported: RDS PostgreSQL, Aurora MySQL
- Requirement: outbound traffic allowed (Public, NAT Gateway (NAT GW), VPC Endpoints)
- Permissions: Lambda resource-based policy + IAM policy on DB instance
- Use case: trigger email on user INSERT in database

### RDS Event Notifications
- DB instance events (created, stopped, started) — NOT data changes
- Near real-time (up to 5 minutes latency)
- Targets: Simple Notification Service (SNS) or EventBridge

```
Integration flow:
Client ──REST──► API Gateway ──► Lambda ──► DynamoDB
                                  │             │
                                  │             └──► DAX (cache)
                                  └──► RDS Proxy ──► Aurora
S3 upload ──event──► Lambda ──► S3 (thumbnail) + DynamoDB (metadata)
EventBridge ──schedule──► Lambda ──► any AWS service
DynamoDB ──streams──► Lambda ──► SES (email) / SNS / SQS
```

### Quiz: Section 3
**Q1** ✓ — dynamodb-streams-lambda
Welcome email when new user added to DynamoDB, within seconds. Which integration?
A) CloudWatch polling B) DynamoDB Streams INSERT → Lambda → SES C) API Gateway webhook D) DynamoDB TTL
💡 Hint: Which DynamoDB feature streams item-level modifications to Lambda in real-time?
**Your answer: B** — Correct. DynamoDB Streams captures INSERT events, triggers Lambda in real-time.

**Q2** ✓ — rds-proxy-lambda
Lambda exhausting Aurora connection limit during spikes. AWS-recommended solution?
A) Increase max_connections B) RDS Proxy (connection pooling) C) Migrate to DynamoDB D) Lambda global variable pooling
💡 Hint: Managed service between Lambda and RDS/Aurora for connection pooling.
**Your answer: B** — Correct. RDS Proxy pools connections, enforces IAM, reduces failover 66%.

**Q3** ✓ — rds-event-notifications
RDS event notification reports "DB stopped" but architect wanted data change alerts. What's wrong?
A) Use DynamoDB Streams B) RDS events = instance lifecycle only; invoke Lambda from RDS for data changes C) CloudTrail data events D) Enhanced Monitoring
💡 Hint: RDS events cover instance lifecycle, not SQL data modifications.
**Your answer: B** — Correct. RDS events = instance events only. For data changes, invoke Lambda from RDS/Aurora directly.

---

## Section 4: Architectural Patterns

### Pattern 1: Basic Serverless REST API
```
Client ──HTTPS──► API Gateway ──► Lambda ──► DynamoDB
                    │
                    └── Cognito (authentication)
```
- **When to use**: Any backend API with unpredictable traffic, zero server management
- Pay per request; scales from 0 to millions automatically

### Pattern 2: High Read Throughput
```
Client ──► CloudFront (static cache) ──► API Gateway (response cache) ──► Lambda ──► DAX ──► DynamoDB
```
- **When to use**: Read-heavy workloads (product catalog, content delivery)
- Three caching layers: CloudFront (edge), API Gateway (API-level), DAX (database-level)

### Pattern 3: Serverless File Processing
```
S3 upload ──event──► Lambda ──► process ──► S3 output
                                  └──► DynamoDB (metadata)
                                  └──► SNS/SQS (notify)
```
- **When to use**: Image/video processing, document conversion, ETL
- S3 Transfer Acceleration for global uploads

### Pattern 4: Global Serverless Application
```
Region 1: CloudFront ──► S3 (static) + API Gateway ──► Lambda ──► DynamoDB Global Tables
Region 2: same stack, active-active replication via Global Tables
```
- **When to use**: Global user base, low-latency reads AND writes in multiple regions
- DynamoDB Global Tables: active-active, requires Streams enabled

### Pattern 5: Microservices with DNS Routing
```
Route 53 ──► service1.example.com → API Gateway + Lambda + DynamoDB
         ──► service2.example.com → ALB + ECS + RDS
         ──► service3.example.com → ALB + ASG + EC2
```
- **When to use**: Independent services with different architectures
- Each service scales independently; REST API communication between services

### Pattern 6: Software Update Offloading
```
Before: Users ──► ALB ──► ASG (many EC2) ──► high bandwidth costs
After:  Users ──► CloudFront ──► ALB ──► ASG (fewer EC2) ──► low bandwidth
```
- **When to use**: Large static file distribution (software updates, media)
- CloudFront caches at edge; EC2 handles less load

### Quiz: Section 4
**Q1** ✓ — serverless-caching
Product catalog API, 95% reads, Lambda costs rising. Best caching strategy?
A) DAX only B) API Gateway cache only C) API Gateway cache + DAX (two layers) D) CloudFront only
💡 Hint: Multiple caching layers at different levels provide most comprehensive cost reduction.
**Your answer: C** — Correct. API Gateway cache reduces Lambda invocations; DAX reduces DynamoDB RCU costs.

**Q2** ✓ — cloudfront-offloading
2 GB software updates via ALB+ASG, 50 EC2 on release day. Reduce costs without app changes?
A) API Gateway + Lambda B) CloudFront in front of ALB C) S3 + pre-signed URLs D) ElastiCache
💡 Hint: Cache static files at edge globally without application changes.
**Your answer: B** — Correct. CloudFront caches at 400+ edge locations; EC2 barely touched after first download.

---

## Section 5: Cost Implications

### Lambda Pricing
| Component | Rate | Free Tier |
|-----------|------|-----------|
| Requests | $0.20 per 1M requests | 1M requests/month |
| Compute | $1.00 per 600,000 GB-seconds | 400,000 GB-seconds/month |

- More RAM = higher per-second cost but faster execution (may reduce total cost)
- Provisioned Concurrency incurs additional charges (pre-allocated instances)
- SnapStart: no extra cost (free performance improvement)

### API Gateway Pricing
- REST API: per API call + data transfer
- Caching: hourly charge per cache size
- Cost optimization: enable caching to reduce Lambda invocations

### DynamoDB Pricing
| Mode | Pricing | Best For |
|------|---------|----------|
| Provisioned | Per RCU/WCU provisioned | Predictable workloads |
| On-Demand | Per read/write request | Unpredictable traffic |

- DAX: node-hours (only provision when microsecond reads needed)
- Global Tables: pay for replicated writes in each region
- DynamoDB Streams: free with Lambda triggers (2 free reads/second/shard)

### Cost Optimization Tips
- **Lambda**: right-size memory (higher RAM = faster = potentially cheaper); use SnapStart over Provisioned Concurrency when possible
- **API Gateway**: enable response caching to reduce backend calls
- **DynamoDB**: use provisioned + auto-scaling for predictable; on-demand for spiky
- **CloudFront**: offload static content from Lambda/EC2 to reduce compute costs
- **Step Functions**: Standard workflows for long-running; Express workflows for high-volume, short-duration (10x cheaper)

### Quiz: Section 5
**Q1** ✓ — snapstart-cost
Cold starts affecting 5% of 10M requests/month. Most cost-effective elimination?
A) Provisioned Concurrency B) SnapStart (no extra cost) C) Increase memory to 10 GB D) EC2 Reserved Instances
💡 Hint: One option eliminates cold starts without any additional charge.
**Your answer: B** — Correct. SnapStart pre-initializes from snapshot, no extra cost.

**Q2** ✓ — step-functions-express
50K short tasks/hour, high Step Functions bill. Best cost reduction?
A) SQS + Lambda B) Express Workflows (10x cheaper) C) Reduce states D) Lambda Destinations
💡 Hint: Step Functions offers two workflow types for different volume/duration profiles.
**Your answer: B** — Correct. Express Workflows are 10x cheaper for high-volume, short-duration.

**Q3** ✓ — api-gateway-caching
Read-heavy API, Lambda costs 70% of bill, same catalog data. Reduce Lambda costs?
A) DynamoDB provisioned mode B) API Gateway caching (reduces invocations) C) DAX D) Increase Lambda memory
💡 Hint: Reduce invocation count, not per-invocation cost.
**Your answer: B** — Correct. API Gateway caching intercepts repeated requests before reaching Lambda.

---

## Section 6: Security Considerations

### Lambda Security
- **Execution role**: IAM role granting Lambda permissions to access AWS services
- **Resource-based policy**: controls WHO can invoke the Lambda function
- **VPC deployment**: required for accessing private resources (RDS, ElastiCache)
- **Environment variables**: can be encrypted with Key Management Service (KMS)
- **Reserved concurrency**: prevents one function from consuming all concurrent executions

### API Gateway Security
| Method | Use Case |
|--------|----------|
| IAM Roles | Internal applications |
| Cognito User Pools | External/mobile users |
| Custom Authorizer (Lambda) | Custom authentication logic |

- HTTPS via AWS Certificate Manager (ACM)
- Edge-Optimized: certificate must be in us-east-1
- Regional: certificate in same region as API Gateway

### Cognito Security
- User Pools: handles authentication (username/password, MFA, federated login)
- Identity Pools: provides temporary AWS credentials with fine-grained IAM policies
- Row-level security: IAM policy condition on `cognito-identity.amazonaws.com:sub` ensures users access only their own data

### DynamoDB Security
- Access controlled via IAM only (no Security Groups, no username/password)
- Encryption at rest with Key Management Service (KMS)
- VPC Gateway Endpoint for private access (free)
- DynamoDB Streams + Lambda for event-driven processing (IAM role on Lambda)

```
Security layers (serverless):
┌──────────────────────────────────────────┐
│ CloudFront (edge filtering, WAF)          │
│  ┌───────────────────────────────────┐   │
│  │ API Gateway (auth, throttling)     │   │
│  │  ┌────────────────────────────┐   │   │
│  │  │ Cognito (identity)          │   │   │
│  │  │  ┌─────────────────────┐   │   │   │
│  │  │  │ Lambda (exec role)   │   │   │   │
│  │  │  │  ┌──────────────┐   │   │   │   │
│  │  │  │  │ IAM (DynamoDB)│   │   │   │   │
│  │  │  │  └──────────────┘   │   │   │   │
│  │  │  └─────────────────────┘   │   │   │
│  │  └────────────────────────────┘   │   │
│  └───────────────────────────────────┘   │
└──────────────────────────────────────────┘
```

### Quiz: Section 6
**Q1** ✓ — lambda-execution-vs-resource-policy
Lambda reads S3 + writes DynamoDB; ECS needs to invoke it. Which two mechanisms?
A) Execution role (S3+DynamoDB) + resource-based policy (ECS invoke) B) Execution role for all + IAM user C) Resource-based for access + execution for invoke D) Security Group + IAM role
💡 Hint: Execution role = what Lambda can do. Resource-based = who can invoke.
**Your answer: A** — Correct. Execution role for outbound access; resource-based policy for inbound invocation.

**Q2** ✓ — cognito-row-level-security
Mobile app, Cognito Identity Pools, users must only access own S3 folder. How?
A) S3 bucket policy + IP B) IAM condition on cognito sub C) Lambda authorizer D) API Gateway resource policy
💡 Hint: Identity Pools issue temporary credentials with IAM policies scoped per user.
**Your answer: B** — Correct. `cognito-identity.amazonaws.com:sub` in IAM policy restricts per-user access.

**Q3** ✓ — api-gateway-acm-region
Edge-Optimized API Gateway, ACM cert in eu-west-1, custom domain fails. Why?
A) Edge-Optimized requires cert in us-east-1 B) ACM not supported C) No custom domain on Edge D) Cert must be in CloudFront
💡 Hint: Edge-Optimized routes through CloudFront — certs must be in us-east-1.
**Your answer: A** — Correct. Edge-Optimized uses CloudFront, which requires ACM certs in us-east-1.

---

## Section 7: Exam Tips

### Keyword-to-Answer Decision Tree
```
"Serverless REST API" ──► API Gateway + Lambda + DynamoDB
"User sign-in / authentication" ──► Cognito User Pools
"Direct AWS access from app" ──► Cognito Identity Pools
"Schedule background task" ──► EventBridge + Lambda
"Orchestrate Lambda functions" ──► Step Functions
"React to DB changes" ──► DynamoDB Streams + Lambda
"Lambda can't connect to RDS" ──► Deploy Lambda in VPC
"Lambda connection exhaustion" ──► RDS Proxy
"Lightweight edge processing" ──► CloudFront Functions
"Complex edge processing" ──► Lambda@Edge
"Cache DynamoDB reads" ──► DAX
"Reduce static content costs" ──► CloudFront in front of ALB/S3
```

### Critical Distinctions (Exam Traps)

| Statement | True/False | Explanation |
|-----------|-----------|-------------|
| Lambda can run indefinitely | **FALSE** | Max 15 minutes (900 seconds) |
| Lambda in default VPC can access RDS | **FALSE** | Must deploy in customer VPC to access private resources |
| Cognito User Pools give AWS credentials | **FALSE** | User Pools give tokens for auth; Identity Pools give AWS credentials |
| DAX requires code changes | **FALSE** | Seamless, no app code change |
| CloudFront Functions can access network | **FALSE** | No network access; use Lambda@Edge for that |
| DynamoDB uses Security Groups | **FALSE** | IAM only |
| RDS Proxy is publicly accessible | **FALSE** | Never; VPC only |
| Lambda@Edge runs at origin only | **FALSE** | Runs at both viewer and origin request/response |
| Step Functions can include human approval | **TRUE** | Supports human approval steps |
| API Gateway Edge-Optimized cert must be in us-east-1 | **TRUE** | Certificate in ACM must be in us-east-1 |

### Lambda Concurrency — The Hidden Exam Topic
- Default: 1,000 concurrent executions per region (ALL functions share this)
- If Auto Scaling Group (ASG) event processing consumes all 1,000 → API Gateway Lambda gets throttled
- Solution: **Reserved concurrency** on critical functions
- Provisioned concurrency: pre-allocates instances (eliminates cold starts, costs more)

### Cognito User Pools vs Identity Pools — #1 Exam Distinction
| Feature | User Pools | Identity Pools |
|---------|-----------|----------------|
| Purpose | Authentication (sign-in) | Authorization (AWS access) |
| Output | JWT token | Temporary AWS credentials |
| Use with | API Gateway, ALB | Direct S3/DynamoDB access |
| MFA | Yes | N/A |
| Federated login | Yes (via User Pool) | Yes (via any identity source) |

### Key Takeaways
- **Lambda** = short execution (max 15 min), event-driven, auto-scaling, pay per use
- **API Gateway** = managed REST API with auth, throttling, caching
- **Step Functions** = orchestrate Lambda workflows with visual state machine
- **Cognito User Pools** = authentication; **Identity Pools** = temporary AWS credentials
- **CloudFront Functions** = lightweight edge (< 1ms, JS only); **Lambda@Edge** = complex edge (network, body access)
- **DAX** = microsecond DynamoDB cache, zero code change
- **RDS Proxy** = Lambda → RDS connection pooling, VPC only, IAM auth
- **Lambda in VPC** = required for private resources (RDS, ElastiCache), NOT default behavior

### Quiz: Section 7
**Q1** ✓ — lambda-reserved-concurrency
5 Lambda functions, Function A uses 900 of 1,000 regional limit, Function B throttled. Fix?
A) More memory B) Reserved Concurrency on Function A (cap its usage) C) Provisioned Concurrency on B D) API Gateway throttle limit
💡 Hint: All functions share the same regional concurrency pool.
**Your answer: B** — Correct. Reserved Concurrency caps Function A, freeing pool for others.

**Q2** ✓ — cognito-user-vs-identity-pools
Team claims User Pools provides temporary AWS credentials for direct S3 uploads. Correct?
A) Yes B) No — User Pools = JWT tokens; Identity Pools = AWS credentials C) No — Lambda must proxy D) No — API Gateway should proxy
💡 Hint: User Pools output tokens, not AWS credentials.
**Your answer: B** — Correct. User Pools = JWT tokens for auth. Identity Pools = temporary AWS credentials for direct access.
