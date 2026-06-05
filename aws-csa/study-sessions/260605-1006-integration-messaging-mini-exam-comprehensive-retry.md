# Integration & Messaging — Mini Exam: Comprehensive Final (Phase 4 Retry)
**Date:** 2026-06-05 10:06
**Score:** 10/10 (100%)
**Time:** 17 min / 30 min ✓ within limit
**Scope:** comprehensive — full domain exam covering all topics + cross-domain

---

## Questions & Results

### Q1 ✓ — sqs-visibility-timeout
**Question:** An Amazon Simple Queue Service (SQS) Standard queue has a default visibility timeout of 30 seconds. A consumer application polls a message, begins processing, but realizes mid-way that it needs more time. The processing will take an additional 90 seconds. What should the consumer do to prevent the message from becoming visible to other consumers?

A) Delete the message from the queue immediately, process it locally, and re-send it to the queue only if processing fails
B) Call the ChangeMessageVisibility API to extend the visibility timeout to 120 seconds before the current 30-second timeout expires
C) Increase the queue-level visibility timeout to 120 seconds using the SetQueueAttributes API
D) Send a new copy of the message with a delay of 120 seconds using SendMessage with DelaySeconds, then delete the original message

**Your answer: B** — Correct. ChangeMessageVisibility API extends the timeout for a specific in-flight message.

---

### Q2 ✓ — kinesis-shard-capacity-planning
**Question:** A logistics company ingests GPS tracking data from 5,000 delivery vehicles at a rate of 6 MB/s and 8,000 records per second. The architect uses Amazon Kinesis Data Streams in provisioned mode. Each shard supports 1 MB/s (or 1,000 records/s) for writes. What is the minimum number of shards required?

A) 6 shards — data throughput only
B) 8 shards — MAX of both limits (data=6, records=8)
C) 10 shards — 8 + 25% buffer
D) 5 shards — one per 1,000 vehicles

**Your answer: B** — Correct. MAX(6 MB/s ÷ 1, 8000 records/s ÷ 1000) = MAX(6, 8) = 8 shards.

---

### Q3 ✓ — sns-fanout-message-filtering
**Question:** A company processes customer support tickets. Each ticket update must be delivered to exactly three downstream services. The escalation engine should only receive tickets with priority "Critical". All services must receive messages even if one is temporarily down. Which architecture meets all requirements?

A) SNS → 3 SQS + filter on escalation sub
B) SNS → 3 direct Lambda subs + code filter
C) EventBridge → 3 rules with pattern matching
D) Producer → 3 SQS directly + consumer filter

**Your answer: A** — Correct. SNS→SQS fan-out with filter policy on escalation subscription. SQS provides durability when services are down.

---

### Q4 ✓ — kinesis-data-firehose-redshift-staging
**Question:** A data warehouse team needs to load streaming application logs into Amazon Redshift for near-real-time analytics. They also want raw logs stored in Amazon S3 in Parquet format for a data lake. Fully managed, no custom code. Which approach is most efficient?

A) 2 Firehose streams (S3 Parquet + Redshift)
B) 1 Firehose → Redshift (auto-stages S3 Parquet)
C) KDS + Lambda consumer for both
D) Firehose → S3 Parquet + Lambda COPY to Redshift

**Your answer: B** — Correct. Firehose→Redshift auto-stages in S3. One stream serves both destinations.

---

### Q5 ✓ — databases:sqs-dynamodb-throttling-retry-storm
**Question:** An e-commerce platform uses SQS to buffer order writes to DynamoDB. During Black Friday, DynamoDB throttles, causing a retry storm. Which combination resolves this without losing orders?

A) DynamoDB on-demand + more Lambda concurrency
B) DLQ maxReceiveCount=3 + manual reprocess
C) Higher visibility timeout + DynamoDB auto-scaling
D) Reduce Lambda concurrency + exponential backoff

**Your answer: C** — Correct. Addresses root causes: visibility timeout spaces out retries, auto-scaling adjusts WCU to meet demand. All messages eventually processed.

---

### Q6 ✓ — serverless:step-functions-orchestration
**Question:** A payment system must execute three steps in sequence: validate, charge, send receipt. If charge succeeds but receipt fails, must retry only the notification. Wants managed solution with visual monitoring. Which service?

A) SNS+SQS between steps + DLQs
B) Step Functions state machine + per-state retry
C) Single Lambda + try-catch + CloudWatch
D) EventBridge Pipes connecting 3 steps

**Your answer: B** — Correct. Step Functions provides per-step retry, state tracking, and visual workflow console.

---

### Q7 ✓ — amazon-mq-migration
**Question:** Migrate on-premises RabbitMQ with AMQP protocol to AWS. 20 consumer apps cannot be modified. Need HA across AZs. Which service?

A) SQS with AMQP-compatible interface
B) Amazon MQ RabbitMQ cluster multi-AZ + AMQP
C) MSK multi-AZ + AMQP bridge
D) Amazon MQ ActiveMQ single-instance + EFS

**Your answer: B** — Correct. Amazon MQ supports RabbitMQ with AMQP natively. Cluster mode provides multi-AZ HA. Zero code changes.

---

### Q8 ✓ — serverless:s3-sns-eventbridge-fanout
**Question:** S3 image upload must trigger 3 independent Lambda functions. S3 allows only one event rule per event-type+prefix. Which two solutions? (Select TWO)

A) S3 → SNS → 3 SQS → 3 Lambdas
B) 3 S3 event rules same prefix
C) S3 → EventBridge → 3 Lambda targets
D) S3 → Step Functions Parallel → 3 Lambdas

**Your answer: A, C** — Correct. SNS fan-out and EventBridge multi-target both solve the single-event-rule limitation.

---

### Q9 ✓ — kinesis-vs-firehose-decision
**Question:** Log analytics pipeline needs: replay capability, <5s latency, minimal overhead. Which service?

A) Firehose — managed + near-real-time
B) KDS — real-time + replay up to 365 days
C) Firehose — replay + sub-second latency
D) KDS on-demand + Firehose as consumer

**Your answer: B** — Correct. KDS is real-time (ms latency), supports replay (1-365 days), on-demand mode reduces overhead. Firehose has no replay and is near-real-time (buffered).

---

### Q10 ✓ — compute:sqs-asg-visibility-timeout-scaling
**Question:** ASG workers process SQS jobs taking 3-8 min. Visibility timeout=5 min. Scaling on raw queue depth. Two problems: duplicates + erratic over-scaling. Which two changes? (Select TWO)

A) Visibility timeout 10 min (> 8 min max job)
B) Custom backlog-per-instance metric + Target Tracking
C) DLQ maxReceiveCount=2
D) Switch to Kinesis for exactly-once

**Your answer: A, B** — Correct. Timeout > max job prevents duplicates. Backlog-per-instance normalizes scaling by fleet size.

---

## Summary
- **Score:** 10/10 (100%) — PASSED
- **Missed topics:** none
- **Strong areas:** all topics mastered — sqs-visibility-timeout, kinesis-shard-capacity, firehose-redshift-staging, step-functions-orchestration, sqs-dynamodb-throttling, sns-fanout, s3-eventbridge-fanout, amazon-mq-migration, kinesis-vs-firehose
- **Key achievements:**
  - All 4 previously weak topics from first P4 attempt now mastered
  - Perfect score on retry after targeted weak topic review
