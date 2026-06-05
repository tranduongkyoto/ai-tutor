# Integration & Messaging — Mini Exam: Comprehensive Final (Phase 4)
**Date:** 2026-06-05 09:24
**Score:** 6/10 (60%) — FAILED (below 80%)
**Time:** 15 min / 30 min ✓ within limit
**Scope:** comprehensive — full domain exam covering all topics + cross-domain

---

## Questions & Results

### Q1 ✓ — sqs-visibility-timeout
**Question:** A development team is troubleshooting an Amazon Simple Queue Service (SQS) Standard queue where consumers occasionally process the same message twice. The visibility timeout is set to 30 seconds, and some messages take up to 45 seconds to process. The team wants to eliminate duplicate processing without changing the queue type. Which action resolves this issue?

A) Enable long polling with a 20-second wait time to reduce the number of empty responses and prevent duplicate message delivery
B) Increase the visibility timeout to 60 seconds so messages remain invisible long enough for consumers to finish processing and delete them
C) Configure a Dead Letter Queue (DLQ) with maxReceiveCount set to 1 so each message is only attempted once before being moved to the DLQ
D) Add a Content-Based Deduplication ID to each message so SQS automatically filters duplicate deliveries to consumers

**Your answer: B** — Correct. Visibility timeout (30s) < processing time (45s) causes duplicates. Increasing to 60s keeps messages invisible until processing completes.

---

### Q2 ✗ — kinesis-shard-capacity-planning
**Question:** An IoT platform ingests sensor data from 10,000 devices at a combined rate of 8 MB/s. The architect chooses Amazon Kinesis Data Streams in provisioned mode. Each sensor reading is approximately 0.5 KB. How many shards are required to handle the write throughput, and what is the limiting factor?

A) 4 shards — each shard supports 2 MB/s write throughput, so 4 shards handle 8 MB/s
B) 8 shards — each shard supports 1 MB/s write throughput, so 8 shards handle 8 MB/s
C) 16 shards — each shard supports 1,000 records/s write, and 10,000 devices at 1 reading/s = 10,000 records/s, requiring at least 10 shards, rounded up to 16 for headroom
D) 10 shards — each shard supports 1,000 records/s and 1 MB/s, so both limits (8 MB/s data and 10,000 records/s) require 10 shards

**Your answer: B** — Incorrect. Correct answer: D. Must check BOTH shard limits: data (8 MB/s ÷ 1 = 8 shards) AND records (10,000 ÷ 1,000 = 10 shards). Take higher value = 10 shards. Read throughput is 2 MB/s per shard, write is 1 MB/s.

---

### Q3 ✓ — serverless:s3-sns-eventbridge-fanout
**Question:** A video processing platform uses Amazon Simple Storage Service (S3) to receive uploaded videos. Each upload must trigger three independent pipelines: transcoding, thumbnail extraction, and content moderation. The architect knows that S3 only allows one event notification rule per event-type and prefix combination. Which two approaches correctly solve this fan-out requirement? (Select TWO)

A) Configure the S3 event notification to publish to an Amazon Simple Notification Service (SNS) topic, then subscribe three separate Amazon Simple Queue Service (SQS) queues to the topic — each queue triggers its own Lambda function
B) Configure three S3 event notification rules with the same s3:ObjectCreated:* event type but different prefixes (/transcode/, /thumbnail/, /moderate/) to route uploads to different Lambda functions
C) Enable Amazon EventBridge integration on the S3 bucket, then create an EventBridge rule matching Object Created events that targets three separate Lambda functions for parallel execution
D) Configure the S3 event notification to invoke a single Lambda function that uses the AWS SDK to publish the event to three separate SQS queues in parallel

**Your answer: A, C** — Correct. SNS fan-out and EventBridge multi-target both solve the single-event-rule limitation with independent failure isolation.

---

### Q4 ✓ — sns-message-filtering
**Question:** A company uses Amazon Simple Notification Service (SNS) to broadcast order events to multiple downstream services. The SNS topic currently has 5 SQS queue subscriptions. The team wants the "returns processing" queue to receive only orders where the status field equals "Returned", while a "catch-all" analytics queue should continue receiving every message. How should this be configured?

A) Create two separate SNS topics — one for returned orders and one for all orders
B) Apply an SNS message filter policy {"status": ["Returned"]} to the returns processing subscription. Leave the analytics subscription with no filter policy
C) Configure the returns processing SQS queue with a message filter that drops non-returned messages after they are received from SNS
D) Use Amazon EventBridge instead of SNS, creating two rules

**Your answer: B** — Correct. SNS filter policies are per-subscription. No filter = receives everything.

---

### Q5 ✗ — kinesis-data-firehose-redshift-staging
**Question:** A data engineering team needs to load streaming clickstream data into Amazon Simple Storage Service (S3) in Apache Parquet format and simultaneously into Amazon Redshift for real-time dashboards. The source data arrives as JSON at approximately 2 GB/hour. They want a fully managed solution with no custom consumer code. Which service and configuration meets these requirements?

A) Amazon Kinesis Data Streams with two consumer Lambda functions — one converting JSON to Parquet and writing to S3, another using the Redshift Data API to insert rows
B) Amazon Data Firehose with an S3 destination configured for Parquet format conversion, and a separate Firehose delivery stream for the Redshift destination
C) Amazon Data Firehose with Amazon Redshift as the primary destination — Firehose automatically stages data in S3 in Parquet format before COPY-ing into Redshift, serving both requirements from a single delivery stream
D) Amazon Managed Streaming for Apache Kafka (MSK) with Kafka Connect S3 sink for Parquet output and a Kafka Connect Redshift sink for the dashboard data

**Your answer: A** — Incorrect. Correct answer: C. Firehose with Redshift destination automatically stages data in S3 before COPY-ing into Redshift — one stream serves both S3 archival and Redshift loading. Lambda consumers require custom code, violating the requirement.

---

### Q6 ✓ — compute:sqs-asg-scaling-backlog-per-instance
**Question:** A solutions architect is designing a system where an Auto Scaling Group (ASG) of worker instances processes messages from an Amazon Simple Queue Service (SQS) queue. The target is to keep per-instance backlog under 50 messages. Currently there are 4 instances and 800 messages visible in the queue. The architect needs to configure Auto Scaling to maintain this target. Which metric and scaling policy combination is correct?

A) Use the built-in CloudWatch metric ApproximateNumberOfMessagesVisible with Target Tracking scaling set to a target value of 50
B) Publish a custom CloudWatch metric that calculates ApproximateNumberOfMessagesVisible ÷ NumberOfRunningInstances, then use Target Tracking scaling with a target value of 50
C) Use the built-in CloudWatch metric ApproximateNumberOfMessagesVisible with Step Scaling
D) Use the built-in CloudWatch metric ApproximateAgeOfOldestMessage with Target Tracking scaling set to a target of 120 seconds

**Your answer: B** — Correct. Backlog-per-instance custom metric is the AWS-recommended approach. Target Tracking does NOT auto-divide by fleet size.

---

### Q7 ✗ — serverless:step-functions-orchestration
**Question:** A company is building a serverless order processing system. When an order is placed, an AWS Lambda function must process the payment and, if successful, send a confirmation email via Amazon Simple Notification Service (SNS) and update the inventory in Amazon DynamoDB. If the Lambda function fails after sending the email but before updating DynamoDB, the system could end up in an inconsistent state. Which architecture prevents this partial execution problem?

A) Configure the Lambda function with a Dead Letter Queue (DLQ) so that failed executions are retried automatically
B) Use Amazon Simple Queue Service (SQS) between the Lambda function and both downstream services
C) Use AWS Step Functions to orchestrate the workflow — sequence the payment, email, and inventory update as separate Lambda functions with error handling and retry logic per step
D) Enable Lambda Provisioned Concurrency to prevent cold start failures that cause the partial execution

**Your answer: B** — Incorrect. Correct answer: C. Step Functions provides per-step retry and state tracking — if email succeeds but inventory fails, only inventory is retried. SQS decoupling doesn't solve atomic orchestration — if Lambda crashes after publishing to email queue but before inventory queue, you still have inconsistency.

---

### Q8 ✓ — sqs-visibility-timeout
**Question:** An Amazon Simple Queue Service (SQS) Standard queue receives messages from a web application. The consumer Lambda function processes each message in approximately 2 minutes. The Lambda concurrency limit is set to 100. During peak hours, the queue grows to 50,000 messages. The team notices that some messages are processed twice. The current visibility timeout is 90 seconds. Which change resolves the duplicate processing while maintaining throughput?

A) Switch to an SQS FIFO queue to guarantee exactly-once processing
B) Increase the visibility timeout to 3 minutes (180 seconds) so it exceeds the 2-minute processing time
C) Enable long polling with a 20-second wait time and reduce the Lambda batch size to 1
D) Add a DynamoDB table to track processed message IDs and check for duplicates

**Your answer: B** — Correct. Visibility timeout (90s) < processing time (120s) = duplicates. Increase to 180s provides safe margin.

---

### Q9 ✓ — amazon-mq-migration
**Question:** A retail company needs to migrate its on-premises order management system to AWS. The existing system uses ActiveMQ with the MQTT protocol for communication between IoT point-of-sale devices and the backend. The company has a 6-week migration window and cannot modify the point-of-sale device firmware. Which messaging architecture meets the Phase 1 migration requirement?

A) Deploy Amazon Managed Streaming for Apache Kafka (MSK) with Kafka Connect MQTT source connector
B) Deploy Amazon MQ with an ActiveMQ broker in Multi-Availability Zone (AZ) configuration
C) Deploy Amazon Simple Queue Service (SQS) with the AWS IoT Core MQTT bridge
D) Deploy Amazon Simple Notification Service (SNS) with MQTT endpoint support

**Your answer: B** — Correct. Amazon MQ supports MQTT protocol natively — zero firmware changes. Multi-AZ provides HA.

---

### Q10 ✗ — databases:sqs-dynamodb-throttling-retry-storm
**Question:** A company runs an event-driven architecture where an Amazon Simple Queue Service (SQS) Standard queue buffers database write operations to an Amazon DynamoDB table. During a traffic spike, DynamoDB throttles write requests. The consumer Lambda function catches these errors but messages are returned to the queue and reprocessed, creating a retry storm. Which combination of changes resolves the retry storm while ensuring no messages are lost?

A) Switch DynamoDB to on-demand capacity mode and increase Lambda concurrency
B) Configure a Dead Letter Queue (DLQ) with maxReceiveCount of 3 and increase visibility timeout
C) Increase the SQS visibility timeout to allow more time between retries and enable DynamoDB auto-scaling on the provisioned table
D) Reduce Lambda concurrency and configure exponential backoff

**Your answer: B** — Incorrect. Correct answer: C. DLQ isolates failed messages but doesn't ensure timely processing — messages sit in DLQ until separately handled. Addressing root cause (auto-scaling capacity + spacing retries via visibility timeout) resolves without message loss risk.

---

## Summary
- **Score:** 6/10 (60%) — FAILED
- **Missed topics:** kinesis-shard-capacity-planning, kinesis-data-firehose-redshift-staging, serverless:step-functions-orchestration, databases:sqs-dynamodb-throttling-retry-storm
- **Strong areas:** sqs-visibility-timeout (2/2), sns-message-filtering, s3-sns-eventbridge-fanout, sqs-asg-scaling-backlog-per-instance, amazon-mq-migration
- **Key lessons:**
  - Kinesis shard sizing: always calculate BOTH data throughput AND record count limits — take the higher
  - Firehose→Redshift automatically stages in S3 — one stream serves both destinations
  - Step Functions solves multi-step orchestration with per-step retry — SQS decoupling doesn't solve atomic orchestration
  - DLQ isolates but doesn't resolve root cause — prefer auto-scaling + visibility timeout for DynamoDB throttling
