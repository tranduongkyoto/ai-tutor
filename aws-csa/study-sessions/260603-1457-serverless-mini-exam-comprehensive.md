# Serverless — Mini Exam: Comprehensive Final (Phase 4 Retry)
**Date:** 2026-06-03 14:57
**Score:** 8/10 (80%) — PASSED
**Scope:** comprehensive — Full domain exam with cross-domain integration (serverless + security-identity)

---

## Weak Topic Review (Pre-Exam)

### 1. API Gateway Endpoint Types
- Edge-Optimized (default): Requests routed through CloudFront Edge locations, API stays in ONE region. ACM cert in **us-east-1**.
- Regional: No CloudFront by default. ACM cert in **same region** as API Gateway.
- Private: VPC only via Interface VPC Endpoint (ENI). Resource policy defines access.
- **Trap:** Edge-Optimized does NOT move the API to edge — only routing goes through CloudFront.

### 2. Cognito User Pools vs Identity Pools
- User Pools = Authentication → returns JWT tokens. For sign-in, MFA, social login.
- Identity Pools = Authorization → returns temporary AWS credentials (via STS). For direct AWS resource access.
- Common pattern: User Pools → JWT → Identity Pools → AWS credentials → S3/DynamoDB.
- **Signal:** "authenticate/sign-in" → User Pools. "Access AWS resources directly" → Identity Pools.

### 3. Lambda Provisioned Concurrency vs SnapStart
- Provisioned Concurrency: **Eliminates** cold starts completely. Extra cost. All runtimes.
- SnapStart: **Reduces** cold starts (up to 10x). No extra cost. Java/Python/.NET only.
- **Signal:** "eliminate cold starts" → Provisioned. "Reduce/no extra cost" → SnapStart.

---

## Questions & Results

### Q1 ✓ — API Gateway Endpoint Types (api-gateway-endpoint-types)
**Question:** A mobile gaming company uses Amazon API Gateway with AWS Lambda for their backend API. They deploy an Edge-Optimized endpoint. Where must the ACM certificate be provisioned, and where does Lambda execute?

A) ACM in same Region as API Gateway; Lambda at nearest edge location
B) ACM in us-east-1; Lambda in the Region where API Gateway is deployed
C) ACM in same Region as API Gateway; Lambda in the Region where API Gateway is deployed
D) ACM in us-east-1; Lambda at nearest CloudFront edge location

**Your answer: B** — Correct. Edge-Optimized requires ACM in us-east-1 (CloudFront requirement). API and Lambda stay in deployment Region — only routing goes through edge.

---

### Q2 ✓ — Cognito User Pools vs Identity Pools (cognito-user-pools-vs-identity-pools)
**Question:** Healthcare startup needs sign-in with MFA + direct S3 uploads scoped to user ID using Cognito. Which combination?

A) Identity Pools for sign-in with MFA, JWTs to call S3 directly
B) User Pools for sign-in with MFA → JWTs → Identity Pools → temporary AWS credentials scoped by IAM policy on user sub
C) User Pools for sign-in, JWT directly to S3 via bucket policy conditions
D) Identity Pools for both sign-in and credential generation with custom auth Lambda

**Your answer: B** — Correct. User Pools handle auth/MFA → JWT. Identity Pools exchange JWT for temporary AWS credentials. IAM policy with cognito-identity.amazonaws.com:sub for per-user S3 folder access.

---

### Q3 ✓ — Lambda Provisioned Concurrency vs SnapStart (lambda-provisioned-vs-snapstart)
**Question:** Java Lambda with 5-second cold starts for trading API. Need to eliminate cold starts for first 500 concurrent requests. Budget not a concern.

A) SnapStart + reserved concurrency at 500
B) Provisioned Concurrency at 500, on-demand for bursts beyond
C) SnapStart + Provisioned Concurrency at 500
D) Reserved concurrency at 500 + SnapStart

**Your answer: B** — Correct. Provisioned Concurrency eliminates cold starts completely for 500 concurrent executions. SnapStart only reduces, doesn't eliminate. Reserved concurrency caps max but doesn't warm instances.

---

### Q4 ✓ — Lambda Concurrency Throttling (lambda-concurrency-throttling)
**Question:** API Gateway → Lambda returning HTTP 429 during viral event. What's happening?

A) SQS queue full, rejecting messages
B) Lambda exceeded concurrent execution limit, synchronous invocations throttled. Fix: reserved concurrency or limit increase.
C) API Gateway account-level throttling limit reached
D) Lambda memory too low causing timeouts reported as 429

**Your answer: B** — Correct. 429 = ThrottleError from Lambda concurrent execution limit (1,000 default per region). Synchronous invocation returns 429 to caller.

---

### Q5 ✗ — Lambda Reserved Concurrency (lambda-reserved-concurrency)
**Question:** Bulk migration of 50,000 docs via S3→Lambda→DynamoDB consumes all 1,000 concurrent executions, starving other functions. How to prevent?

A) Switch DynamoDB to provisioned capacity with auto-scaling
B) Configure reserved concurrency on document processing Lambda to cap its max concurrent executions
C) Increase regional limit to 5,000 + add SQS queue between S3 and Lambda
D) Replace S3→Lambda with S3→SNS fan-out to multiple Lambdas

**Your answer: C** — Incorrect. Correct answer: **B**. Reserved concurrency caps a specific function's concurrent executions, guaranteeing remaining capacity for other functions. Increasing the limit doesn't prevent the same problem at higher scale. SQS buffers events but doesn't cap consumer concurrency.

---

### Q6 ✓ — Step Functions (step-functions)
**Question:** Multi-step order fulfillment with rollback on payment failure. Which orchestration service?

A) SQS with separate queues per step + DLQs for rollback
B) SNS with topic per step + error topic for rollback
C) Step Functions with Catch block on payment state for compensating rollback
D) Lambda direct synchronous invocation with try-catch

**Your answer: C** — Correct. Step Functions provides visual workflow, built-in error handling (Catch/Retry), state tracking, and the saga pattern for compensating transactions.

---

### Q7 ✓ — IAM Lambda Execution Role (security-identity:iam-lambda-execution-role)
**Question:** Lambda needs SSM GetParameter for `/prod/myapp/*` + KMS Decrypt on specific key. Least privilege?

A) IAM policy on execution role: ssm:GetParameter on /prod/myapp/* + kms:Decrypt on specific key ARN
B) AmazonSSMFullAccess + KMS key policy for all keys
C) ssm:GetParameter* on all parameters + KMS key resource policy
D) Lambda resource-based policy allowing SSM/KMS to invoke function

**Your answer: A** — Correct. Scoped ssm:GetParameter to specific path prefix + kms:Decrypt to specific key ARN on the execution role = least privilege.

---

### Q8 ✗ — DynamoDB Streams Idempotency (dynamodb-streams-idempotency)
**Question:** Lambda processing DynamoDB Stream records occasionally processes same record multiple times. How to ensure exactly-once?

A) Replace with Kinesis Data Streams for exactly-once delivery
B) Enable DynamoDB Streams DeduplicationScope setting
C) Implement idempotent processing by tracking processed sequence numbers in separate DynamoDB table
D) Set batch window to 0 + max retries to 0

**Your answer: B** — Incorrect. Correct answer: **C**. DynamoDB Streams provides at-least-once delivery — no built-in deduplication feature exists. DeduplicationScope is fictitious (SQS FIFO has deduplication, not DynamoDB Streams). Standard pattern: make consumer idempotent by tracking processed record IDs.

---

### Q9 ✓ — Cognito API Gateway Authorizer (cognito-api-gateway-authorizer)
**Question:** Cognito User Pools auth + API Gateway + Lambda. Only "premium" group can access /premium-features. Least operational overhead?

A) Cognito Authorizer + API Gateway resource policies for group check
B) Cognito Authorizer for token validation + group check inside Lambda via cognito:groups claim
C) Lambda Authorizer calling Cognito + group check returning IAM policy
D) Cognito Authorizer with authorization scopes matching "premium" group

**Your answer: B** — Correct. Cognito Authorizer handles JWT validation natively. Group-based authorization via cognito:groups claim in Lambda = minimal code, no extra infrastructure.

---

### Q10 ✓ — Cognito Identity Pools + KMS (cognito-identity-pools, security-identity:kms-lambda-environment-encryption)
**Question:** (Select TWO) Users auth via Cognito User Pools, upload files to S3 with specific KMS key, per-user folder isolation.

A) Cognito Identity Pools with IAM role: s3:PutObject on user's sub folder + kms:GenerateDataKey on specific key
B) IAM role attached directly to User Pool with broad permissions
C) S3 bucket policy for all authenticated users + default SSE-KMS
D) Cognito Identity Pools with User Pool as identity provider, exchanging JWTs for temporary AWS credentials

**Your answer: A, D** — Correct. D establishes the identity flow (User Pools → Identity Pools → temp credentials). A defines the scoped permissions (per-user S3 folder + specific KMS key).

---

## Summary
- **Score:** 8/10 (80%) — PASSED
- **Missed topics:** lambda-reserved-concurrency, dynamodb-streams-idempotency
- **Strong areas:** api-gateway-endpoint-types, cognito-user-pools-vs-identity-pools, lambda-provisioned-vs-snapstart, lambda-concurrency-throttling, step-functions, iam-lambda-execution-role, cognito-api-gateway-authorizer, cognito-identity-pools
- **Key lessons:**
  - Reserved concurrency **caps** a function's max concurrent executions — the direct fix for one function starving others. Increasing regional limits doesn't prevent the root cause.
  - DynamoDB Streams provides at-least-once delivery with NO built-in deduplication. Always implement idempotent consumers by tracking processed sequence numbers/event IDs.
- **Previous weak topics mastered:** All 3 from prior attempt (api-gateway-endpoint-types, cognito-user-pools-vs-identity-pools, lambda-provisioned-vs-snapstart)
