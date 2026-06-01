# Serverless — Mini Exam: Design (Phase 3)
**Date:** 2026-06-01 22:20
**Score:** 3/10 (30%)
**Scope:** design — Architecture design decisions and trade-offs

---

## Questions & Results

### Q1 ✗ — Lambda concurrency (lambda-concurrency)
**Question:** (from previous partial session — details not preserved)
**Your answer:** — Incorrect.

---

### Q2 ✗ — API Gateway Usage Plans (api-gateway-usage-plans)
**Question:** (from previous partial session — details not preserved)
**Your answer:** — Incorrect.

---

### Q3 ✓ — Lambda Power Tuning (lambda-power-tuning)
**Question:** (from previous partial session — details not preserved)
**Your answer:** — Correct.

---

### Q4 ✗ — Lambda Concurrency Throttling (lambda-concurrency-throttling)
**Question:** A media company runs a serverless video processing pipeline. When a user uploads a video to Simple Storage Service (S3), an AWS Lambda function is triggered to transcode it into multiple formats. During peak hours, hundreds of videos are uploaded simultaneously, and users report significant delays. The Lambda function is configured with 3 GB memory and a 10-minute timeout. CloudWatch metrics show frequent throttling errors but no function errors. The solutions architect needs to ensure consistent processing times during peak hours with the least operational overhead.

A) Increase the Lambda function's reserved concurrency to 500 and enable Amazon Simple Queue Service (SQS) as a buffer between S3 events and Lambda
B) Enable Provisioned Concurrency on the Lambda function set to 200 instances and configure an Auto Scaling policy to adjust based on utilization
C) Replace Lambda with an Amazon Elastic Container Service (ECS) Fargate cluster behind an Application Load Balancer (ALB) to handle the transcoding workload
D) Request a concurrency limit increase for the AWS Region and configure S3 event notifications to invoke Lambda asynchronously with a Dead Letter Queue (DLQ)

**Your answer: B** — Incorrect. The problem is throttling (hitting Regional concurrency limit), not cold starts. Provisioned Concurrency pre-warms instances for cold starts but doesn't increase the Regional limit. Requesting a concurrency limit increase solves the throttling directly with least overhead.

---

### Q5 ✗ — API Gateway Usage Plans (api-gateway-usage-plans)
**Question:** A financial services company uses an API Gateway REST API backed by Lambda functions to serve its trading platform processing 50,000 requests per second. The company wants to monetize the API by offering tiered access — free tier (100 req/day), premium (10,000 req/day), enterprise (unlimited with dedicated throughput guarantee). Which combination of API Gateway features implements this tiered access model?

A) Create three API Gateway stages (free, premium, enterprise) with different throttling settings on each stage, and use Cognito User Pools to route users to the correct stage
B) Configure API Gateway Usage Plans with three tiers, associate each with an API Key, set quota and throttle limits per plan, and distribute API keys to customers
C) Deploy three separate API Gateway REST APIs with different rate limits, use Route 53 weighted routing to distribute traffic, and authenticate with IAM roles per tier
D) Use Lambda authorizer to check the user's tier from DynamoDB, apply request throttling in the Lambda function code, and return HTTP 429 when limits are exceeded

**Your answer: A** — Incorrect. API Gateway stages are for deployment environments (dev/staging/prod), not customer tiers. Usage Plans are the native feature for API monetization — they attach quotas and throttle limits to API keys.

---

### Q6 ✓ — KMS Customer-Managed Keys + CloudTrail (security-identity:kms | lambda)
**Question:** A healthcare company stores patient records in DynamoDB and serves them through Lambda functions via API Gateway. Regulatory requirements mandate encrypted transit, encryption at rest with company-controlled keys that can be rotated on demand, and audit trail of user access to patient records. Which architecture satisfies ALL three requirements with least complexity?

A) Enable DynamoDB encryption with an AWS-managed KMS key, configure API Gateway with ACM certificate for TLS, and enable CloudTrail data events for DynamoDB
B) Enable DynamoDB encryption with a customer-managed KMS key with annual rotation, enforce HTTPS on API Gateway, and enable API Gateway access logging + Lambda logging
C) Implement client-side encryption using DynamoDB Encryption Client with customer-managed KMS key, use mTLS on API Gateway, and integrate with AWS Config
D) Enable DynamoDB encryption with a customer-managed KMS key configured for on-demand rotation, enforce HTTPS on API Gateway, and enable CloudTrail data events for both DynamoDB and Lambda

**Your answer: D** — Correct. Customer-managed KMS keys support on-demand rotation, HTTPS encrypts in transit, and CloudTrail data events capture item-level access for audit.

---

### Q7 ✗ — SQS Write Buffer Pattern (integration-messaging:sqs | lambda)
**Question:** A startup's serverless e-commerce backend (API Gateway → Lambda → DynamoDB) experienced cascading failures during a flash sale: DynamoDB throttling → Lambda errors → API Gateway 502s → client retries amplifying load. Which design change MOST effectively breaks the cascade failure pattern?

A) Add DynamoDB Auto Scaling with aggressive scale-up policies and switch to On-Demand capacity mode
B) Place an SQS queue between API Gateway and Lambda to absorb traffic spikes, process writes asynchronously, and return accepted status immediately
C) Implement API Gateway throttling matching DynamoDB capacity and configure API Gateway response caching with 30-second TTL
D) Deploy DAX for read caching and configure Lambda reserved concurrency to match expected peak

**Your answer: D** — Incorrect. The cascade pattern is a synchronous chain problem. SQS breaks the chain by accepting requests immediately (HTTP 202) and processing asynchronously. DAX helps reads but flash sales are write-heavy; reserved concurrency doesn't prevent the cascade.

---

### Q8 ✗ — Step Functions Map MaxConcurrency (step-functions)
**Question:** A company uses Step Functions to orchestrate a 5-step document processing pipeline. Step 4 calls an external API with 10 req/s rate limit and 30-second response time. Must process 100K documents daily without exceeding rate limit. Which Step Functions configuration handles this most effectively?

A) Standard Workflow with Map state MaxConcurrency 10 and Wait state of 1 second between batches
B) Express Workflow with DynamoDB-based token bucket rate limiter in Lambda
C) Standard Workflow with Map state MaxConcurrency 10, Retry with exponential backoff, and 60-second task timeout
D) Split into Express Workflow (steps 1-3) and Standard Workflow (steps 4-5) with Map MaxConcurrency 10

**Your answer: D** — Incorrect. A single Standard Workflow with Map MaxConcurrency 10 handles the rate limit natively. Retry with exponential backoff handles transient API failures. Splitting into two workflows adds unnecessary coordination complexity.

---

### Q9 ✗ — Multi-Region Serverless (lambda | dns:route-53)
**Question:** A SaaS company serves global users through CloudFront → API Gateway → Lambda → DynamoDB Global Tables. EU users see 3-second latency vs 200ms for US users. API Gateway and Lambda are in us-east-1, Global Tables replicate to eu-west-1. Which change reduces EU latency under 500ms with least architectural change?

A) Deploy second API Gateway + Lambda stack in eu-west-1, use Route 53 latency-based routing for EU users, Lambda reads from eu-west-1 DynamoDB replica
B) Enable API Gateway caching with 60s TTL and increase CloudFront cache duration for API responses
C) Move API Gateway to Regional endpoint in eu-west-1, use CloudFront origin failover between US and EU endpoints
D) Use Lambda@Edge at European edge locations to handle API logic, reading from eu-west-1 DynamoDB replica

**Your answer: B** — Incorrect. Caching doesn't solve the fundamental problem for user-specific data (low hit rates). Deploying a full stack in eu-west-1 with Route 53 latency routing eliminates the transatlantic round trip. Global Tables already replicate data to eu-west-1.

---

### Q10 ✗ — Step Functions Error Handling (step-functions | lambda)
**Question:** A serverless order processing app uses Lambda to write to DynamoDB and call an external payment service (99.9% SLA). When payment service is down, Lambda retries exhaust timeout, consuming concurrent executions and blocking other orders. Which change ensures continued processing during outages with exactly-once payment processing?

A) Circuit breaker in Lambda code using DynamoDB health tracking + SQS FIFO retry queue
B) Step Functions Try/Catch around payment step, Wait state with exponential backoff, DynamoDB conditional write for idempotent payment
C) SQS standard queue between order and payment + payment idempotency key
D) Lambda Destinations routing failed payments to SQS FIFO + separate retry Lambda

**Your answer: A** — Incorrect. Step Functions provides native Try/Catch and Wait states that handle retries without consuming Lambda concurrency. DynamoDB conditional writes ensure exactly-once semantics. Custom circuit breaker code adds unnecessary operational complexity.

---

## Summary
- **Score:** 3/10 (30%)
- **Missed topics:** lambda-concurrency-throttling, api-gateway-usage-plans, sqs-write-buffer-pattern, step-functions, multi-region-serverless, step-functions-error-handling
- **Strong areas:** kms-encryption-controls, cloudtrail-audit
- **Key lessons:**
  - Throttling (Regional limit) ≠ cold starts (Provisioned Concurrency) — request limit increase for throttling
  - Usage Plans + API Keys = native API Gateway monetization mechanism
  - SQS write buffer breaks synchronous cascade failures by decoupling and returning 202
  - Step Functions Map MaxConcurrency is the native rate limiter — simpler than custom solutions
  - Multi-region serverless = duplicate API GW + Lambda per region + Route 53 latency routing
  - Step Functions Try/Catch + Wait handles external service failures without consuming Lambda concurrency
