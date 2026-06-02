# Serverless — Mini Exam: Design (Phase 3 Retry)
**Date:** 2026-06-02 16:14
**Score:** 8/10 (80%)
**Scope:** design — Architecture design decisions and trade-offs (retry after weak topic review)

---

## Questions & Results

### Q1 ✓ — Lambda Concurrency Throttling (lambda-concurrency)
**Question:** A video streaming platform uses AWS Lambda functions triggered by Amazon Simple Storage Service (S3) events to generate thumbnails. During a marketing campaign, uploads surge from 50/minute to 5,000/minute. CloudWatch shows `Throttles` metric spiking to 800/minute, but `Duration` and `Errors` metrics remain normal for functions that do execute. The team wants to handle the surge with the least operational overhead.

A) Enable Provisioned Concurrency set to 500 instances on the thumbnail Lambda function and configure Application Auto Scaling to adjust based on utilization metrics
B) Add an Amazon Simple Queue Service (SQS) queue between S3 event notifications and the Lambda function, configure Lambda to poll the queue with a batch size of 10
C) Request a Lambda concurrent execution limit increase for the Region through AWS Support and set reserved concurrency on the thumbnail function to 2,000
D) Migrate the thumbnail generation to Amazon Elastic Container Service (ECS) Fargate tasks triggered by Amazon EventBridge rules from S3 events

**Your answer: C** — Correct. Throttling confirms the Regional limit is being hit. Limit increase solves it directly with least overhead. Provisioned Concurrency is for cold starts, not throttling.

---

### Q2 ✓ — API Gateway Usage Plans (api-gateway-usage-plans)
**Question:** A healthcare SaaS company exposes a REST API through Amazon API Gateway backed by AWS Lambda. They want to offer three subscription tiers to partner hospitals: Basic (500 requests/day, 5 req/s), Professional (50,000 requests/day, 50 req/s), and Enterprise (unlimited requests, 500 req/s with dedicated throughput). Partners should be authenticated and rate-limited automatically without any custom throttling code. Which approach implements this with least operational overhead?

A) Create three separate API Gateway REST APIs with stage-level throttling configured to match each tier, use Amazon Cognito User Pool groups to route partners to the correct API endpoint
B) Configure three API Gateway Usage Plans with corresponding quota and throttle limits, create API Keys for each partner and associate them with the appropriate Usage Plan
C) Deploy a Lambda authorizer that reads partner tier from Amazon DynamoDB, calculate remaining quota in the authorizer, and return a deny policy when the quota is exceeded
D) Use AWS Web Application Firewall (WAF) rate-based rules attached to the API Gateway stage, create three rule groups matching each tier's rate limit, and tag partners via custom headers

**Your answer: B** — Correct. Usage Plans are API Gateway's native monetization feature — quotas, throttles, and API keys with zero custom code.

---

### Q3 ✓ — SQS Write Buffer Pattern (integration-messaging:sqs | lambda)
**Question:** An e-commerce company runs a serverless checkout pipeline: Amazon API Gateway → AWS Lambda → Amazon DynamoDB. During Black Friday, DynamoDB Write Capacity Units (WCU) are exhausted, causing `ProvisionedThroughputExceededException`. Lambda retries exhaust the 15-minute timeout. API Gateway returns 502 errors. Frustrated customers retry manually, amplifying load 3x. The company needs a solution that prevents cascade failures during traffic spikes while maintaining order data integrity.

A) Switch DynamoDB to On-Demand capacity mode and enable DynamoDB Auto Scaling with a target utilization of 50% to handle spikes faster
B) Insert an Amazon Simple Queue Service (SQS) FIFO queue between API Gateway and the order-processing Lambda function, return HTTP 202 Accepted to clients immediately, and process orders asynchronously with a DLQ for failures
C) Add Amazon DynamoDB Accelerator (DAX) in front of DynamoDB to cache writes, configure Lambda reserved concurrency matching DynamoDB capacity, and enable API Gateway request throttling
D) Deploy an Amazon ElastiCache Redis cluster for write-behind caching, batch DynamoDB writes every 5 seconds, and use API Gateway response caching with 10-second TTL

**Your answer: B** — Correct. SQS FIFO breaks the synchronous cascade, returns 202 immediately, processes asynchronously, and preserves order integrity.

---

### Q4 ✓ — Step Functions Map MaxConcurrency (step-functions)
**Question:** A document processing company uses AWS Step Functions to orchestrate a 6-step pipeline: extract text → classify → enrich with metadata → call a third-party compliance API (rate limited to 20 requests/second, 3-second average response) → generate report → store in S3. They process 500,000 documents daily. The compliance API returns HTTP 429 when rate limit is exceeded. Which Step Functions configuration handles the rate-limited API step most effectively?

A) Use an Express Workflow for the entire pipeline with a Lambda function implementing a token bucket rate limiter using DynamoDB for state tracking
B) Use a Standard Workflow with a Map state wrapping steps 4-6, set MaxConcurrency to 20, and configure Retry with exponential backoff and maximum 3 attempts on the compliance API task
C) Split into two Standard Workflows: steps 1-3 in a parallel-processing workflow, steps 4-6 in a sequential workflow with a Lambda-based semaphore using Amazon Simple Queue Service (SQS)
D) Use a Standard Workflow with Parallel state for steps 1-3 and a nested Map state for steps 4-6 with MaxConcurrency set to 60 to account for the 3-second response time

**Your answer: B** — Correct. Map MaxConcurrency 20 natively limits concurrency to match the API rate limit. Retry with exponential backoff handles transient 429s.

---

### Q5 ✓ — Multi-Region Serverless (lambda | dns:route-53)
**Question:** A global SaaS platform serves users in North America, Europe, and Asia-Pacific through Amazon CloudFront → Amazon API Gateway → AWS Lambda → Amazon DynamoDB Global Tables. Global Tables replicate data to us-east-1, eu-west-1, and ap-southeast-1. However, API Gateway and Lambda are deployed only in us-east-1. European and APAC users experience 2-4 second API latency compared to 150ms for US users. Which change reduces global API latency below 500ms with the least architectural complexity?

A) Deploy identical API Gateway + Lambda stacks in eu-west-1 and ap-southeast-1, configure Amazon Route 53 latency-based routing to direct users to the nearest Region, with each Lambda reading from its local DynamoDB replica
B) Enable API Gateway response caching with a 120-second TTL and increase CloudFront cache duration to serve API responses from edge locations closer to users
C) Replace Lambda functions with Lambda@Edge deployed at European and Asian edge locations, reading directly from the nearest DynamoDB Global Table replica
D) Configure API Gateway with Regional endpoints in all three Regions behind a single CloudFront distribution using origin groups with failover routing

**Your answer: A** — Correct. Duplicate stack per region + Route 53 latency routing eliminates transatlantic round trips. Global Tables already replicate data.

---

### Q6 ✓ — Step Functions Error Handling (step-functions | lambda)
**Question:** A fintech company's order processing pipeline uses AWS Lambda to write trades to Amazon DynamoDB and then call an external settlement service (99.5% SLA, 5-second average response). When the settlement service is unavailable, Lambda functions retry for 15 minutes, consuming concurrent executions and starving other functions. The company needs the pipeline to continue accepting orders during settlement outages and guarantee exactly-once settlement processing. Which approach achieves both requirements?

A) Implement a circuit breaker pattern in the Lambda function code using DynamoDB to track settlement service health status, route failed settlements to an Amazon Simple Queue Service (SQS) FIFO queue for retry
B) Use AWS Step Functions with a Try/Catch block around the settlement task, a Wait state with exponential backoff for retries, and a DynamoDB conditional write (attribute_not_exists) on the settlement record for idempotency
C) Configure Lambda Destinations to route settlement failures to an Amazon Simple Queue Service (SQS) queue, with a separate retry Lambda that processes the queue with reserved concurrency
D) Add an Amazon Simple Queue Service (SQS) standard queue between the trade Lambda and the settlement Lambda, with a visibility timeout of 30 minutes and a message deduplication strategy using trade IDs

**Your answer: B** — Correct. Step Functions Try/Catch + Wait handles retries without consuming Lambda concurrency. DynamoDB conditional write guarantees exactly-once.

---

### Q7 ✗ — API Gateway VPC Access Patterns (api-gateway | security-identity:cognito)
**Question:** A company builds a serverless API using Amazon API Gateway and AWS Lambda. The API serves both internal microservices (running on Amazon Elastic Container Service (ECS) in the same Virtual Private Cloud (VPC)) and external mobile clients authenticated through Amazon Cognito. Internal services need low-latency access without internet traversal, while external clients need standard HTTPS access with token validation. Which architecture supports both access patterns with least duplication?

A) Deploy a single Regional API Gateway REST API with a Cognito User Pool authorizer, create a VPC Interface Endpoint for API Gateway's execute-api service, configure the endpoint policy to allow internal ECS tasks without authentication
B) Deploy two separate API Gateway REST APIs — one Private API for internal ECS access using VPC Endpoint, one Regional API with Cognito authorizer for mobile — both backed by the same Lambda functions
C) Deploy a single Regional API Gateway REST API with a Lambda authorizer that checks the source IP — bypass Cognito for VPC CIDR ranges and enforce Cognito tokens for external requests
D) Deploy a single Private API Gateway accessible via VPC Endpoint for internal services, and use Amazon CloudFront with a custom origin pointing to the Private API for external mobile client access

**Your answer: C** — Incorrect. Source IP-based auth is fragile and insecure. A single Regional API Gateway with Cognito authorizer + VPC Interface Endpoint for internal access is the correct approach — one API, no duplication, secure.

---

### Q8 ✗ — KMS Encryption + CloudTrail Audit (security-identity:kms | lambda)
**Question:** A company stores sensitive customer data in Amazon DynamoDB, accessed through AWS Lambda functions via Amazon API Gateway. Security requirements mandate: (1) Lambda environment variables containing database connection strings must be encrypted with a company-controlled key, (2) DynamoDB data must be encrypted at rest with keys the company can rotate on demand, and (3) all API calls to Key Management Service (KMS) must be auditable. (Select TWO solutions that TOGETHER satisfy all three requirements.)

A) Configure Lambda environment variable encryption using a KMS Customer Managed Key (CMK) with the Lambda function's execution role granted `kms:Decrypt` permission
B) Enable DynamoDB default encryption with an AWS-managed KMS key and configure automatic annual key rotation
C) Enable DynamoDB encryption with a KMS Customer Managed Key (CMK) configured for on-demand rotation and grant the Lambda execution role `kms:Decrypt` and `kms:GenerateDataKey` permissions
D) Enable AWS CloudTrail with management events logging in the Region where the KMS keys are created

**Your answer: C, D** — Incorrect. Correct answers: A and C. A covers Lambda env var encryption with CMK (req 1). C covers DynamoDB encryption with CMK + on-demand rotation (req 2). CloudTrail logs KMS API calls by default as management events (req 3 — no additional setup needed). D is not wrong per se, but A is required to cover requirement 1.

---

### Q9 ✓ — Cognito Identity Pools Direct S3 Access (security-identity:cognito | lambda)
**Question:** A mobile app uses Amazon Cognito User Pools for authentication and Amazon API Gateway with a Cognito authorizer. The company wants to add a feature where authenticated users can upload profile photos directly to a specific Amazon Simple Storage Service (S3) prefix (`photos/{user_id}/`) without routing through Lambda. Users must only access their own folder. Which approach enables this with least operational complexity?

A) Create an Amazon Cognito Identity Pool that exchanges User Pool tokens for temporary AWS credentials, configure an IAM policy with `s3:PutObject` permission using `${cognito-identity.amazonaws.com:sub}` as the S3 key prefix condition
B) Generate pre-signed S3 URLs in a Lambda function behind API Gateway, including the user's Cognito sub claim as the S3 key prefix, with 15-minute expiration
C) Configure S3 bucket policy to allow authenticated Cognito User Pool users with a condition on the `cognito:sub` claim, and have the mobile app call S3 directly with the Cognito JWT token
D) Use Amazon API Gateway with an S3 proxy integration that maps the Cognito authorizer's user sub claim to the S3 key prefix in the integration request mapping template

**Your answer: A** — Correct. Cognito Identity Pools provide temporary AWS credentials for direct S3 access. IAM policy variable `${cognito-identity.amazonaws.com:sub}` enforces per-user folder access.

---

### Q10 ✓ — DAX Read Caching (lambda | dynamodb)
**Question:** A logistics company runs a serverless fleet tracking system. Thousands of IoT devices send GPS coordinates every 10 seconds to Amazon API Gateway → AWS Lambda → Amazon DynamoDB. The Lambda function writes the current position AND reads the last 5 positions to calculate speed/heading. During peak hours (8,000 devices, 800 writes/second), DynamoDB read latency increases from 5ms to 200ms due to hot partition on the most active fleet region. Write latency remains normal. Which change addresses the read latency issue with least architectural change?

A) Enable DynamoDB Accelerator (DAX) for the tracking table and update the Lambda function to read through DAX, keeping direct DynamoDB writes unchanged
B) Switch DynamoDB to On-Demand capacity mode and increase the read capacity to handle peak load without provisioned throughput limits
C) Add an Amazon ElastiCache Redis cluster with a 30-second TTL for the last-5-positions query, deploy Lambda in the VPC to access the cache
D) Redesign the DynamoDB partition key to include a random suffix for write sharding and use a Global Secondary Index (GSI) for position queries

**Your answer: A** — Correct. DAX is purpose-built for DynamoDB read caching with microsecond latency, API-compatible, minimal code change.

---

## Summary
- **Score:** 8/10 (80%)
- **Missed topics:** api-gateway-vpc-access-patterns, kms-multi-select-audit
- **Strong areas:** lambda-concurrency, api-gateway-usage-plans, sqs-write-buffer-pattern, step-functions, multi-region-serverless, step-functions-error-handling, cognito-identity-pools, dax-caching
- **Key lessons:**
  - VPC Interface Endpoint for execute-api allows internal services to reach a Regional API Gateway without internet traversal — one API serves both internal and external consumers
  - CloudTrail logs KMS management API calls by default — no additional Trail needed for basic auditability. When multi-select asks "which TWO," ensure all explicit requirements are mapped to an answer
