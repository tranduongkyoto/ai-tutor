# Serverless — Phase 3 Gap Analysis Report
**Date:** 2026-06-02 11:14
**Domain:** serverless
**Phase 3 Score:** 3/10 (30%)
**Purpose:** Identify content gaps in Phase 1 (learn-and-test) and Phase 2 (scenario-practice) that caused Phase 3 failures

---

## Phase 3 Results Summary

| Q# | Topic | Result | Root Cause |
|----|-------|--------|------------|
| Q1 | Lambda concurrency | ✗ | Details not preserved (partial session) |
| Q2 | API Gateway Usage Plans | ✗ | Details not preserved (partial session) |
| Q3 | Lambda Power Tuning | ✓ | — |
| Q4 | Lambda Concurrency Throttling | ✗ | Confused throttling (Regional limit) with cold starts (Provisioned Concurrency) |
| Q5 | API Gateway Usage Plans | ✗ | Chose stages (deployment environments) instead of Usage Plans (monetization) |
| Q6 | KMS + CloudTrail (cross-domain) | ✓ | — |
| Q7 | SQS Write Buffer Pattern | ✗ | Chose DAX (read cache) instead of SQS (async decoupling for writes) |
| Q8 | Step Functions Map MaxConcurrency | ✗ | Split into Express+Standard instead of single Standard with Map MaxConcurrency |
| Q9 | Multi-Region Serverless | ✗ | Chose caching instead of deploying duplicate stack + Route 53 latency routing |
| Q10 | Step Functions Error Handling | ✗ | Chose custom circuit breaker instead of native Try/Catch + Wait states |

---

## Gap Analysis: 6 Missing Concepts

### Gap 1: Regional Concurrency Limit Increase as Design Solution

**What Phase 3 tested:** Lambda throttling during peak (hitting 1,000 Regional concurrent limit) → correct answer: request limit increase + SQS buffer.

**What P1 taught:** Section 7 "Lambda Concurrency — The Hidden Exam Topic" mentions "1,000 concurrent executions per region (ALL functions share this)" and Reserved Concurrency to protect critical functions. But frames concurrency purely as function-vs-function competition.

**What P2 taught:** Scenario 2 (concurrency-limits) tested Reserved Concurrency between functions. You answered Provisioned Concurrency (wrong — that's for cold starts). Correct was Reserved Concurrency. But neither scenario covered the "request a Regional limit increase" pattern.

**The gap:** P1/P2 never taught that when ALL functions collectively exceed the Regional limit, the solution is to request a limit increase from AWS. Reserved Concurrency redistributes within the limit; limit increase raises the ceiling.

**Key concept to learn:**
- Throttling (429 errors) + no function errors = Regional concurrency limit exhausted
- Reserved Concurrency = redistribute slots within existing limit
- Request limit increase = raise the Regional ceiling (via AWS Support)
- SQS buffer = absorb spikes while limit increase processes

---

### Gap 2: API Gateway Usage Plans (Tiers, Quotas, Monetization)

**What Phase 3 tested:** Tiered API access (free/premium/enterprise) with quotas and throttling per tier → correct answer: Usage Plans + API Keys.

**What P1 taught:** Section 1 mentions "API keys, throttling" as API Gateway features. Never explains Usage Plans.

**What P2 taught:** Scenario 4 (REST vs HTTP vs WebSocket) mentions "API key usage plans" in passing context but doesn't explain the mechanism.

**The gap:** Usage Plans as a concept was never taught. Students don't know that Usage Plans are the native API Gateway feature for:
- Defining tiers (free/premium/enterprise)
- Attaching quotas (requests per day/month) and throttle limits per tier
- Distributing API keys to customers
- Tracking usage per key

**Key concept to learn:**
- Usage Plans = tiered access control attached to API keys
- API Keys = identify the caller and map to a Usage Plan
- Each Usage Plan defines: throttle rate (requests/second), burst limit, quota (requests/period)
- Stages are for deployment environments (dev/staging/prod), NOT customer tiers
- REST API supports Usage Plans; HTTP API does NOT (cheaper but fewer features)

---

### Gap 3: SQS Write Buffer Pattern (Cross-Domain: Integration-Messaging)

**What Phase 3 tested:** Cascading failures in synchronous chain (API GW → Lambda → DynamoDB) during flash sale → correct answer: SQS queue between API GW and Lambda to break the cascade.

**What P1 taught:** No mention of SQS as a decoupling or write buffer pattern.

**What P2 taught:** No scenario covers async decoupling with SQS.

**The gap:** The SQS write buffer pattern is an integration-messaging concept applied to serverless architectures. It was completely absent from P1 and P2.

**Key concept to learn:**
- Synchronous chain: API GW → Lambda → DynamoDB = single point of cascade failure
- If DynamoDB throttles → Lambda errors → API GW 502s → client retries amplify load
- SQS write buffer: API GW → SQS → Lambda (async) → DynamoDB
  - Returns HTTP 202 Accepted immediately (no client waiting)
  - SQS absorbs traffic spikes (unlimited queue depth)
  - Lambda processes at controlled rate (event source mapping batch size)
  - DynamoDB never sees the full spike
- This is the #1 pattern for breaking cascade failures in serverless
- DAX helps reads, not writes. Flash sales are write-heavy.
- Reserved Concurrency prevents Lambda throttling but doesn't fix the cascade

---

### Gap 4: Step Functions Map State + MaxConcurrency

**What Phase 3 tested:** Process 100K documents through external API with 10 req/s rate limit → correct answer: Standard Workflow + Map MaxConcurrency=10 + Retry with backoff.

**What P1 taught:** Section 1 mentions "sequence, parallel, conditions, timeouts, error handling" for Step Functions. No mention of Map state or MaxConcurrency.

**What P2 taught:** Scenario 5 (orchestration vs choreography) covered Standard vs Express, Task tokens, Catch/Retry. Never mentioned Map state.

**The gap:** Map state is a critical Step Functions feature for batch processing, and MaxConcurrency is the native rate limiting mechanism.

**Key concept to learn:**
- **Map state** = iterate over a collection, processing each item through a series of steps
- **MaxConcurrency** = limits how many items run in parallel (native rate limiter)
  - MaxConcurrency=10 → at most 10 items processed simultaneously
  - Perfect for external APIs with rate limits
- **Inline Map** = items defined in the state input (small batches)
- **Distributed Map** = items from S3 (millions of items, serverless batch processing)
- Standard Workflow: durable, up to 1 year, execution history
- Express Workflow: high-volume, max 5 min, no durable history
- For 100K items + external API rate limit: Standard + Map MaxConcurrency is the simplest solution
- No need to split workflows or build custom rate limiters

---

### Gap 5: Multi-Region Serverless Deployment (Cross-Domain: DNS)

**What Phase 3 tested:** EU users see 3s latency (API GW + Lambda in us-east-1, Global Tables replicate to eu-west-1) → correct answer: deploy second API GW + Lambda stack in eu-west-1 + Route 53 latency-based routing.

**What P1 taught:** Section 4 "Pattern 4: Global Serverless Application" describes active-active replication via Global Tables and says "same stack" in two regions, but doesn't explicitly explain:
- How to deploy the second stack
- How Route 53 latency routing connects users to nearest stack
- That API Gateway + Lambda must be duplicated per region (Global Tables alone insufficient)

**What P2 taught:** No scenario covers multi-region serverless.

**The gap:** The global pattern in P1 was too abstract. It didn't explain the concrete architecture: duplicate API GW + Lambda per region, Route 53 latency routing, Lambda reads from local DynamoDB replica.

**Key concept to learn:**
- DynamoDB Global Tables replicate data automatically (active-active)
- But API Gateway + Lambda are regional services — they don't automatically exist in multiple regions
- Multi-region serverless = deploy identical stack per region:
  - Region 1: API GW → Lambda → DynamoDB (us-east-1)
  - Region 2: API GW → Lambda → DynamoDB replica (eu-west-1)
- Route 53 latency-based routing directs users to the nearest regional API endpoint
- Caching (CloudFront, API GW cache) doesn't help for user-specific data (low hit rates)
- Lambda@Edge cannot replace full API logic (limited execution time, no VPC access)
- This is the "least architectural change" for reducing latency when Global Tables already exist

---

### Gap 6: Step Functions Try/Catch + Wait for External Service Resilience

**What Phase 3 tested:** External payment service down → Lambda retries exhaust timeout, blocking other orders → correct answer: Step Functions Try/Catch + Wait + DynamoDB conditional writes.

**What P1 taught:** Mentions "error handling" in Step Functions overview. No detail on how Try/Catch or Wait states work.

**What P2 taught:** Scenario 5 mentions "error catchers with 3 retries per state" but doesn't explain:
- Try/Catch as a state machine construct (vs Lambda code-level try/catch)
- Wait state for exponential backoff without consuming Lambda concurrency
- Advantage: Step Functions waits don't tie up Lambda instances

**The gap:** The specific pattern of Try/Catch + Wait for external service failures, and its key advantage (retries don't consume Lambda concurrency), was never taught.

**Key concept to learn:**
- Lambda retries with external services: each retry holds a Lambda instance → consumes concurrency → other functions throttled
- Step Functions Try/Catch + Wait pattern:
  - Task state calls Lambda → Lambda calls payment API
  - If fails → Catch → Wait state (exponential backoff: 5s, 10s, 20s…)
  - Wait state consumes NO Lambda concurrency (Step Functions manages the timer)
  - After wait → retry Task state → Lambda reinvoked
- DynamoDB conditional writes ensure exactly-once semantics (idempotency key)
- This is more operational than custom circuit breaker (Lambda + DynamoDB health tracking)
- Step Functions provides:
  - Native Try/Catch per state
  - Native Retry with configurable backoff (IntervalSeconds, MaxAttempts, BackoffRate)
  - Wait state (fixed, timestamp, or dynamic from input)
  - No code needed for retry logic — it's declarative in the state machine JSON/YAML

---

## Cross-Domain Patterns in Phase 3

Two of the six gaps involve concepts from other domains applied to serverless:

1. **SQS Write Buffer** (integration-messaging → serverless): Need to study SQS patterns even when focusing on serverless
2. **Route 53 Latency Routing** (dns → serverless): Multi-region deployment requires DNS knowledge

**Recommendation:** When studying any domain's design phase, expect cross-domain questions. The SAA-C03 exam tests architectural thinking, not isolated domain knowledge.

---

## Recommended Next Steps

1. **Targeted gap-fill lesson** covering all 6 concepts above with examples + quiz
2. **Retake Phase 3 design exam** with refreshed knowledge
3. Consider reviewing integration-messaging and dns domains in parallel (they feed into serverless design patterns)

---

## P1/P2 Content Quality Assessment

| Phase | Score | Content Quality | Gaps Found |
|-------|-------|----------------|------------|
| P1 (learn-and-test) | 18/18 (100%) | Good fundamentals, but missing depth on Step Functions (Map, Try/Catch/Wait) and API GW Usage Plans | 4 gaps |
| P2 (scenario-practice) | 6/8 (75%) | Good scenarios but missing SQS decoupling and multi-region patterns | 2 gaps + missed P2 concurrency question (indicator of shallow P1 coverage) |
| P3 (design exam) | 3/10 (30%) | Fair questions testing design-level thinking — failure largely due to P1/P2 gaps, not P3 difficulty | — |

**Conclusion:** Phase 3 failure was primarily a content coverage problem, not a retention problem. Phase 1 and Phase 2 need to be more comprehensive on advanced patterns (Map state, Usage Plans, cross-domain decoupling) before Phase 3 can be passed.
