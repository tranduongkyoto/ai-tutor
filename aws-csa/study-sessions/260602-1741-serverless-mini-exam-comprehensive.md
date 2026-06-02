# Serverless — Mini Exam: Comprehensive Final (Phase 4)
**Date:** 2026-06-02 17:41
**Score:** 7/10 (70%)
**Scope:** comprehensive — Full domain exam with cross-domain integration

---

## Questions & Results

### Q1 ✓ — Lambda Pricing GB-Seconds (lambda)
**Question:** A startup runs an AWS Lambda function that processes uploaded images — resizing and applying filters. The function currently uses 512 MB of memory with an average execution time of 8 seconds. After doubling the memory to 1,024 MB, the execution time drops to 4 seconds. The function is invoked 100,000 times per month. Considering Lambda's pricing model (pay per request + compute duration in GB-seconds), what happens to the monthly compute cost after doubling the memory?

A) The monthly compute cost roughly doubles because memory doubled from 512 MB to 1,024 MB
B) The monthly compute cost stays roughly the same because the memory increase is offset by the proportional execution time decrease
C) The monthly compute cost decreases significantly because the shorter execution time more than offsets the memory increase
D) The monthly compute cost cannot be determined without knowing the specific Lambda pricing tier and Region

**Your answer: B** — Correct. Before: 0.5 GB × 8s = 4 GB-s. After: 1.0 GB × 4s = 4 GB-s. Same cost, better performance.

---

### Q2 ✓ — DynamoDB Streams vs Kinesis (dynamodb)
**Question:** A social media company captures real-time user activity events in an Amazon DynamoDB table. They need to trigger an AWS Lambda function whenever a new item is inserted to update a real-time leaderboard. The system must support high throughput (50,000 events/second) and allow multiple downstream consumers (analytics pipeline, notification service, audit logger) to process the same events independently. Which approach meets these requirements?

A) Enable DynamoDB Streams with a Lambda trigger for the leaderboard, and create additional Lambda triggers on the same stream for analytics, notifications, and audit
B) Enable Amazon Kinesis Data Streams for DynamoDB instead of DynamoDB Streams, and configure separate consumer applications for each downstream service using enhanced fan-out
C) Configure Amazon EventBridge rules on DynamoDB table events to route to multiple Lambda function targets for each downstream consumer
D) Use DynamoDB Streams with a single Lambda consumer that publishes events to an Amazon Simple Notification Service (SNS) topic, with each downstream service subscribing to the topic

**Your answer: B** — Correct. Kinesis Data Streams supports 1-year retention, high consumer count with enhanced fan-out (dedicated 2 MB/s per consumer), unlike DynamoDB Streams' limited consumers and 24-hour retention.

---

### Q3 ✗ — API Gateway Endpoint Types (api-gateway)
**Question:** A company deploys an Amazon API Gateway REST API that serves customers in Europe and Asia. The API is deployed in eu-west-1 with a Regional endpoint type. The team considers switching to an Edge-Optimized endpoint to reduce latency for Asian customers. Which statement about this change is correct?

A) Edge-Optimized endpoints route requests through Amazon CloudFront edge locations, reducing latency for distant clients, but the API Gateway itself and its SSL/TLS certificate must remain in us-east-1
B) Edge-Optimized endpoints deploy the API Gateway infrastructure to all edge locations globally, processing requests at the nearest edge location to the client
C) Edge-Optimized endpoints route requests through CloudFront edge locations to the API Gateway in eu-west-1, and the associated AWS Certificate Manager (ACM) certificate must be in us-east-1
D) Edge-Optimized endpoints are identical to placing a Regional endpoint behind a CloudFront distribution, with no additional configuration or behavioral differences

**Your answer: A** — Incorrect. The API Gateway stays in eu-west-1 (its deployment Region), NOT us-east-1. Only the ACM certificate must be in us-east-1 (CloudFront requirement). Edge-Optimized changes routing via CloudFront, not the API's home Region.

---

### Q4 ✗ — Cognito User Pools vs Identity Pools (cognito)
**Question:** A mobile banking app uses Amazon Cognito for authentication. Users log in with email/password through Cognito User Pools and receive a JSON Web Token (JWT). After authentication, the app needs to upload transaction receipts directly to an Amazon Simple Storage Service (S3) bucket — each user to their own folder — without routing through a backend server. Which Cognito component enables this, and what type of credentials does it provide?

A) Cognito User Pool issues an IAM access key and secret key embedded in the JWT token, which the mobile app uses to call S3 PutObject directly
B) Cognito Identity Pool (Federated Identity) exchanges the User Pool JWT for temporary AWS credentials (access key, secret key, session token) via AWS Security Token Service (STS), which the app uses with IAM policy-based folder isolation
C) Cognito User Pool generates a pre-signed S3 URL embedded in the JWT token's custom claims, which the app uses to upload directly to S3 without AWS credentials
D) Cognito Identity Pool generates a permanent IAM role with S3 access scoped to the user's folder, which the app assumes using the User Pool JWT as proof of identity

**Your answer: C** — Incorrect. Cognito User Pools do NOT generate pre-signed URLs or embed them in JWTs. Identity Pools exchange JWT for temporary AWS credentials (via STS) with IAM policy using `${cognito-identity.amazonaws.com:sub}` for folder isolation. User Pools = authentication (JWT). Identity Pools = authorization (AWS credentials).

---

### Q5 ✓ — Step Functions Standard vs Express (step-functions)
**Question:** A startup builds a document signing service. The flow: user uploads a PDF to Simple Storage Service (S3) → Lambda extracts signature fields → Step Functions orchestrates: (1) validate signer identity via Cognito, (2) generate signing certificate, (3) apply digital signature, (4) store signed document, (5) notify all parties via Simple Notification Service (SNS). Each step takes 10-30 seconds. The company processes 200 documents/day now but expects 50,000/day within 6 months. Which architectural decision ensures cost efficiency at BOTH scales?

A) Use Step Functions Express Workflow for the entire pipeline since it's cheaper at high volume, with CloudWatch Logs for auditing each document's signing status
B) Use Step Functions Standard Workflow for the entire pipeline since it provides exactly-once execution and built-in audit trail for legal compliance
C) Start with Standard Workflow now and migrate to Express Workflow at 50,000/day to optimize cost, using feature flags to switch between them
D) Use Express Workflow for steps 1-3 (fast validation) and Standard Workflow for steps 4-5 (audit-critical storage and notification)

**Your answer: B** — Correct. Document signing requires exactly-once execution (signing twice is legally problematic). Standard Workflow provides this + built-in audit trail. Express has at-least-once delivery and 5-minute max — both disqualifying.

---

### Q6 ✗ — Lambda Concurrency Combined (lambda-concurrency)
**Question:** A gaming company's Lambda function handles player matchmaking. During tournaments, they experience two distinct issues: (1) new function instances take 4 seconds to initialize the matchmaking algorithm's ML model, causing timeouts for the first requests, and (2) during the biggest tournaments, the function hits the Regional concurrent execution limit of 1,000, causing 429 ThrottleErrors for all game services sharing the Region. Which combination addresses BOTH issues simultaneously?

A) Enable SnapStart for the matchmaking Lambda function and request a Regional concurrent execution limit increase to 5,000
B) Configure Provisioned Concurrency at 200 instances for the matchmaking function and set Reserved Concurrency at 500 for the function
C) Enable Provisioned Concurrency at 500 instances for the matchmaking function and request a Regional concurrent execution limit increase to 5,000
D) Reduce the ML model size to decrease cold start time below 1 second and configure Reserved Concurrency at 300 to prevent the function from consuming all Regional capacity

**Your answer: A** — Incorrect. SnapStart reduces cold starts (10x improvement) but doesn't ELIMINATE them for a 4-second ML model init — ~400ms restore time remains. Provisioned Concurrency at 500 completely eliminates cold starts by keeping instances pre-initialized + limit increase expands Regional capacity. SnapStart is also runtime-specific (Java/Python/.NET only).

---

### Q7 ✓ — CloudFront Functions vs Lambda@Edge (cloudfront-functions)
**Question:** A media company needs to add bot detection to their CloudFront distribution. The detection logic checks the User-Agent header against a list of 50 known bot patterns and either blocks or adds a custom header before forwarding to origin. The check is purely string matching with no external lookups. Average check time is under 0.5ms. Which edge compute option is most cost-effective?

A) AWS Lambda@Edge triggered on Viewer Request, with the bot patterns stored in a DynamoDB table for easy updates
B) Amazon CloudFront Functions triggered on Viewer Request, with the bot patterns hardcoded as a JavaScript array in the function code
C) AWS Web Application Firewall (WAF) with a managed bot control rule group attached to the CloudFront distribution
D) Lambda@Edge triggered on Origin Request, with bot patterns loaded from an S3 object at function initialization

**Your answer: B** — Correct. CloudFront Functions: <1ms, millions req/s, 1/6th Lambda@Edge cost. Pure string matching, no network access needed, 50 patterns fit in 10 KB limit. Perfect fit.

---

### Q8 ✓ — Serverless Architecture Design (serverless-architecture)
**Question:** A startup builds a document signing service. Standard Workflow with Map state. Each step takes 10-30 seconds. The company processes 200 documents/day now but expects 50,000/day within 6 months.

A) Use Step Functions Express Workflow for the entire pipeline
B) Use Step Functions Standard Workflow for the entire pipeline
C) Start with Standard Workflow now and migrate to Express Workflow at 50,000/day
D) Use Express Workflow for steps 1-3 and Standard Workflow for steps 4-5

**Your answer: B** — Correct. Standard Workflow provides exactly-once execution and built-in audit trail.

---

### Q9 ✓ — Cross-Domain: Cognito + KMS Security Layers (security-identity:cognito,kms | lambda)
**Question:** A company uses Amazon API Gateway with AWS Lambda to serve a healthcare API. They need to implement three security layers: (1) authenticate users with email/password, supporting Multi-Factor Authentication (MFA), (2) authorize API access based on user groups (doctors, nurses, admins), and (3) encrypt Lambda environment variables containing API keys for third-party services with a company-managed encryption key. (Select TWO.)

A) Configure Amazon Cognito User Pool with MFA enabled and group-based claims, attach it as an API Gateway Cognito authorizer
B) Use AWS Identity and Access Management (IAM) authentication on API Gateway with IAM policies and SSM Parameter Store SecureString
C) Configure a Lambda authorizer that validates credentials against an Amazon RDS database with Lambda env vars encrypted using a KMS CMK
D) Configure Lambda environment variable encryption with a KMS Customer Managed Key (CMK) and grant the Lambda execution role kms:Decrypt permission

**Your answer: A, D** — Correct. A handles auth + MFA + group-based authz. D handles CMK encryption for Lambda env vars. Together they cover all three requirements.

---

### Q10 ✓ — Cross-Domain: Lambda Execution Role vs Resource Policy (security-identity:iam | lambda)
**Question:** An AWS Lambda function processes financial transactions from an Amazon Simple Queue Service (SQS) queue and writes results to Amazon DynamoDB. A separate monitoring Lambda needs to invoke the transaction function directly (synchronous invocation) to run diagnostic checks. The monitoring Lambda's execution role has lambda:InvokeFunction permission. However, invocation attempts return AccessDeniedException. What is the most likely cause?

A) The transaction Lambda's execution role is missing lambda:InvokeFunction permission
B) The transaction Lambda needs a resource-based policy granting the monitoring Lambda's execution role permission to invoke it
C) The monitoring Lambda's execution role needs sts:AssumeRole permission to assume the transaction Lambda's execution role
D) The SQS queue's access policy is blocking cross-function invocation

**Your answer: B** — Correct. Lambda has two permission types: execution role (what the function can DO) and resource-based policy (who can INVOKE it). The caller needs lambda:InvokeFunction (has it), AND the target needs a resource-based policy allowing the caller.

---

## Summary
- **Score:** 7/10 (70%)
- **Missed topics:** api-gateway-endpoint-types, cognito-user-pools-vs-identity-pools, lambda-provisioned-vs-snapstart
- **Strong areas:** lambda-pricing, dynamodb-streams-kinesis, step-functions-standard-vs-express, cloudfront-functions, cognito-kms-security, lambda-resource-policy
- **Key lessons:**
  - Edge-Optimized API Gateway: API stays in deployment Region, only ACM cert must be in us-east-1
  - User Pools = auth (JWT tokens). Identity Pools = AWS credentials (via STS). User Pools do NOT generate pre-signed URLs or embed access keys in JWTs
  - Provisioned Concurrency eliminates cold starts completely; SnapStart reduces but doesn't eliminate (10x improvement, still ~400ms for large inits). Use Provisioned Concurrency for guaranteed zero cold starts
