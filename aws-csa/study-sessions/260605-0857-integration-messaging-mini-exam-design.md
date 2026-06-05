# Integration & Messaging — Mini Exam: Design (Phase 3)
**Date:** 2026-06-05 08:57
**Score:** 8/10 (80%)
**Time:** 20 min / 30 min ✓ within limit
**Scope:** design — architecture design decisions and trade-offs

---

## Questions & Results

### Q1 ✓ — sqs-fifo-throughput
**Question:** A financial services company processes loan applications through a multi-step pipeline. Each application must be processed exactly once and in the order received. The system currently handles 200 applications per second, but during quarter-end peaks, volume surges to 2,500 applications per second. The architecture team wants to decouple the intake service from the processing service while maintaining strict ordering guarantees. Which approach best meets these requirements?

A) Use an Amazon Simple Queue Service (SQS) Standard queue with a deduplication layer in the consumer application, and scale consumers using an Auto Scaling Group (ASG) based on the ApproximateNumberOfMessages metric
B) Use an Amazon Simple Queue Service (SQS) First-In-First-Out (FIFO) queue with batching enabled and Message Group ID set to a single constant value for all applications to ensure global ordering
C) Use Amazon Kinesis Data Streams with a partition key based on application ID, provisioned at 3 shards, and scale shards manually during peak periods
D) Use an Amazon Simple Queue Service (SQS) FIFO queue with batching enabled and Message Group ID set to a logical grouping such as loan type, distributing ordering across multiple groups to achieve the required throughput

**Your answer: D** — Correct. SQS FIFO with batching achieves up to 3,000 msg/s, and multiple Message Group IDs distribute ordering across groups while maintaining strict ordering within each group.

---

### Q2 ✓ — kinesis-vs-sqs-decision
**Question:** A media company ingests user clickstream data at 50,000 events per second for real-time analytics dashboards. They also need to archive all raw events to Amazon Simple Storage Service (S3) in Apache Parquet format for batch analysis. The solution must support data replay for up to 7 days if the analytics pipeline encounters errors. Which architecture best meets these requirements with the least operational overhead?

A) Use Amazon Simple Queue Service (SQS) Standard queue for ingestion, with one consumer writing to Amazon S3 and another feeding the real-time dashboard via Amazon OpenSearch, enabling replay by increasing the message retention to 14 days
B) Use Amazon Kinesis Data Streams for ingestion and real-time analytics consumers, with a separate Amazon Data Firehose delivery stream subscribed to the same Kinesis stream for automatic Parquet conversion and delivery to S3
C) Use Amazon Simple Notification Service (SNS) to fan out events to both an Amazon Simple Queue Service (SQS) queue for archival processing and a Kinesis Data Streams shard for real-time analytics, with S3 lifecycle policies for Parquet conversion
D) Use Amazon Managed Streaming for Apache Kafka (MSK) for ingestion with a Kafka Connect S3 sink connector for archival and a Kafka Streams application for real-time analytics, configuring 7-day log retention

**Your answer: B** — Correct. KDS supports real-time ingestion with replay (up to 365 days). Firehose natively converts to Parquet and delivers to S3 — fully managed.

---

### Q3 ✓ — sns-fifo-sqs-fanout
**Question:** An e-commerce platform processes orders through an Amazon Simple Notification Service (SNS) topic. Three downstream services must receive every order: payment processing, inventory management, and shipping notification. The payment service requires exactly-once processing with strict ordering by customer ID. The inventory service needs standard reliability. The shipping service only cares about orders with status "Shipped". Which architecture satisfies all three requirements simultaneously?

A) Use an SNS Standard topic with three Amazon Simple Queue Service (SQS) Standard queue subscriptions — apply a message filter policy on the shipping queue for status "Shipped", and implement idempotency in the payment consumer application
B) Use an SNS First-In-First-Out (FIFO) topic with an SQS FIFO queue subscription for payment (Message Group ID = customer ID), an SQS Standard queue for inventory, and an SQS Standard queue with a filter policy for shipping
C) Use an SNS Standard topic with an SQS FIFO queue for payment, an SQS Standard queue for inventory, and an SQS Standard queue with a filter policy for shipping — set the SQS FIFO deduplication scope to "queue"
D) Use Amazon EventBridge with three rules: one routing to an SQS FIFO queue for payment with ordering by customer ID, one routing to an SQS Standard queue for inventory, and one with an event pattern matching status "Shipped" routing to the shipping SQS queue

**Your answer: B** — Correct. SNS FIFO + SQS FIFO (Message Group ID = customer ID) provides exactly-once + ordering. SNS FIFO topics support both FIFO and Standard queue subscribers.

---

### Q4 ✓ — sns-firehose-archival
**Question:** A healthcare company runs a patient notification system. When a lab result is ready, the system must send an SMS to the patient, email the referring doctor, trigger a Lambda function to update the Electronic Health Records (EHR) database, and archive the event to Amazon Simple Storage Service (S3). The company wants a single publish action from the lab system. The S3 archival must be in compressed JSON format with delivery within 60 seconds. Which design achieves this with the least operational overhead?

A) Publish to an Amazon Simple Notification Service (SNS) topic with four subscriptions: SMS, Email, AWS Lambda, and an Amazon Simple Queue Service (SQS) queue with a consumer that writes to S3 in compressed JSON
B) Publish to an Amazon Simple Notification Service (SNS) topic with three subscriptions (SMS, Email, Lambda) and one subscription to Amazon Data Firehose, configured with gzip compression and JSON output format targeting S3
C) Publish to an Amazon Simple Notification Service (SNS) topic with four subscriptions: SMS, Email, Lambda, and a second Lambda function that compresses the event and writes it to S3 using the AWS SDK
D) Publish to Amazon EventBridge, which routes to four targets: Amazon SNS for SMS, Amazon Simple Email Service (SES) for email, Lambda for EHR update, and an S3 PutObject action for archival with a Lambda transform for compression

**Your answer: B** — Correct. Firehose is a supported SNS subscriber, natively handles gzip compression and JSON formatting with delivery to S3 — fully managed, no custom code.

---

### Q5 ✓ — databases:sqs-write-buffer-dynamodb-throttling
**Question:** A SaaS company has a REST API backed by Amazon Relational Database Service (RDS) Aurora PostgreSQL. During flash sales, write traffic spikes 20x and causes database connection exhaustion and timeout errors. The writes are idempotent insert operations for order records. The company needs a solution that prevents database overload while ensuring no orders are lost, with minimal changes to the existing API. Which architecture pattern best addresses this?

A) Add Amazon ElastiCache for Redis in front of the database as a write-through cache, allowing the API to write to Redis first and asynchronously flush to Aurora in controlled batches
B) Switch Aurora to Aurora Serverless v2 with auto-scaling enabled and increase the maximum Provisioned Concurrency Units (ACU) to handle the 20x spike
C) Place an Amazon Simple Queue Service (SQS) Standard queue between the API and the database — the API writes orders to SQS, and a backend consumer Auto Scaling Group (ASG) dequeues and inserts into Aurora at a controlled rate
D) Add Amazon Relational Database Service (RDS) Proxy between the API and Aurora to pool and multiplex database connections, combined with increasing the Aurora instance size to handle peak write throughput

**Your answer: C** — Correct. Classic SQS as Database Write Buffer pattern. SQS has unlimited throughput, persists messages, and the backend consumer ASG inserts at a controlled rate.

---

### Q6 ✓ — sqs-decoupling-cascading-failures
**Question:** A logistics company has 15 microservices communicating through point-to-point API calls. When the shipment-tracking service goes down, cascading failures bring down 8 other services within minutes. The company wants to redesign the communication layer so that a single service failure does not cascade. The solution must support the existing request/response patterns where downstream services need acknowledgment that a message was received. Which approach minimizes cascading failures while maintaining delivery guarantees?

A) Replace all point-to-point calls with an Amazon Simple Notification Service (SNS) topic per event type — each service subscribes to relevant topics and publishes events when state changes occur
B) Replace point-to-point calls with Amazon Simple Queue Service (SQS) queues between each pair of communicating services — producers send to the queue, consumers poll independently, and message persistence ensures no data loss during downstream outages
C) Deploy an Amazon MQ broker using RabbitMQ with topic exchanges and durable queues — services publish to exchanges and consume from their own durable queues, leveraging publisher confirms for acknowledgment
D) Implement an Amazon API Gateway with retry policies and circuit breaker patterns using AWS Step Functions, so failed calls are automatically retried with exponential backoff before falling back to a Dead Letter Queue (DLQ)

**Your answer: B** — Correct. SQS queues fully decouple producers from consumers with message persistence up to 14 days. No cascading failures — messages accumulate safely.

---

### Q7 ✓ — kinesis-enhanced-fan-out
**Question:** A gaming company processes player match events through an Amazon Kinesis Data Streams pipeline. The stream has 10 shards. Three consumer applications read from the stream: a leaderboard updater, an anti-cheat analyzer, and a replay recorder. The leaderboard updater is latency-sensitive and needs dedicated throughput, while the other two can share capacity. All consumers need to process every record. Which configuration optimizes throughput distribution across these consumers?

A) Enable Enhanced Fan-Out for the leaderboard consumer to get a dedicated 2 MB/s per shard pipe, and run the anti-cheat and replay consumers as standard shared-throughput consumers using the Kinesis Client Library (KCL)
B) Create three separate Kinesis Data Streams — one per consumer — and use AWS Lambda to copy records from the source stream to all three, ensuring each consumer gets full dedicated throughput
C) Increase the stream to 30 shards (10 per consumer) and assign each consumer a unique set of 10 shards using partition key routing to separate consumer workloads
D) Use Amazon Simple Notification Service (SNS) to fan out from Kinesis Data Streams to three separate Amazon Simple Queue Service (SQS) queues — one per consumer — giving each independent processing capacity

**Your answer: A** — Correct. Enhanced Fan-Out provides dedicated 2 MB/s per shard per consumer via HTTP/2 push. Standard consumers share the default 2 MB/s per shard.

---

### Q8 ✓ — amazon-mq-migration
**Question:** A company is migrating an on-premises order processing system to AWS. The existing system uses IBM MQ with AMQP protocol for communication between the order service and 12 downstream consumers. The migration must be completed in 4 weeks with zero application code changes to the consumers. The company plans to refactor the consumers to use cloud-native services in Phase 2, six months later. Which messaging solution best fits the Phase 1 migration constraints?

A) Amazon Simple Queue Service (SQS) Standard queues with the AWS SDK — refactor producers to use the SQS SendMessage API and consumers to use ReceiveMessage, maintaining the same message format
B) Amazon MQ with an ActiveMQ broker in Multi-Availability Zone (AZ) deployment — consumers connect using the existing AMQP protocol with no code changes, and the broker stores messages on Amazon Elastic File System (EFS) for durability
C) Amazon Simple Notification Service (SNS) with 12 SQS queue subscriptions using the fan-out pattern — producers publish to SNS, and each consumer polls its own SQS queue
D) Amazon Managed Streaming for Apache Kafka (MSK) with consumer groups — migrate from IBM MQ to Kafka protocol, which requires minimal consumer code changes due to similar pub/sub semantics

**Your answer: B** — Correct. Amazon MQ supports AMQP protocol — zero code changes for consumers. Multi-AZ with EFS provides HA.

---

### Q9 ✗ — serverless:s3-sns-eventbridge-fanout
**Question:** A retail company processes product image uploads through an Amazon Simple Storage Service (S3) bucket. Each upload must trigger three independent processing pipelines: thumbnail generation, metadata extraction, and content moderation. Currently, the S3 event notification is configured to invoke a single AWS Lambda function that calls the three pipelines sequentially. When the content moderation service is slow, it delays thumbnail availability by 30+ seconds. The company wants all three pipelines to execute in parallel with independent failure isolation. Which redesign achieves this? (Select TWO)

A) Configure the S3 bucket to send the event notification to an Amazon Simple Notification Service (SNS) topic, then create three SQS queue subscriptions — each queue triggers its own Lambda function for one pipeline
B) Configure three separate S3 event notification rules on the same bucket for the same event type and prefix, each pointing to a different Lambda function
C) Configure the S3 bucket to send the event notification to an Amazon EventBridge rule, which routes to three separate Lambda function targets for parallel execution with independent retry policies
D) Replace the single Lambda function with an AWS Step Functions Parallel state that invokes three Lambda functions simultaneously, with independent error handling per branch

**Your answer: A, D** — Incorrect. Correct answers: A, C. Step Functions Parallel state still couples all pipelines through one orchestration layer. EventBridge natively supports multiple targets per rule with independent failure isolation.

---

### Q10 ✗ — compute:sqs-asg-scaling-based-on-queue-depth
**Question:** A solutions architect is designing a system where an Auto Scaling Group (ASG) of worker instances processes jobs from an Amazon Simple Queue Service (SQS) queue. Each job takes between 30 seconds and 5 minutes to complete. The ASG must scale based on queue depth to maintain a processing latency target of under 2 minutes from when a message enters the queue to when processing begins. Workers occasionally crash mid-processing. Which combination of SQS and ASG configurations ensures reliable processing with appropriate scaling behavior?

A) Set visibility timeout to 10 minutes, use the ApproximateNumberOfMessagesVisible CloudWatch metric for ASG Target Tracking scaling, and configure a Dead Letter Queue (DLQ) with maxReceiveCount of 3
B) Set visibility timeout to 2 minutes to match the latency target, use the ApproximateNumberOfMessages metric for ASG Step Scaling, and configure a DLQ with maxReceiveCount of 5
C) Set visibility timeout to 6 minutes (slightly above max job time), use a custom CloudWatch metric of backlog-per-instance (ApproximateNumberOfMessagesVisible divided by number of running instances) for ASG Target Tracking scaling, and configure a DLQ with maxReceiveCount of 3
D) Set visibility timeout to 5 minutes (equal to max job time), use the ApproximateAgeOfOldestMessage metric for ASG Target Tracking scaling, and configure long polling with 20-second wait time and a DLQ with maxReceiveCount of 2

**Your answer: B** — Incorrect. Correct answer: C. Visibility timeout must be slightly above max job duration (6 min > 5 min). Backlog-per-instance custom metric is the AWS-recommended approach for SQS+ASG scaling.

---

## Summary
- **Score:** 8/10 (80%)
- **Missed topics:** serverless:s3-sns-eventbridge-fanout, compute:sqs-asg-scaling-based-on-queue-depth
- **Strong areas:** sqs-fifo-throughput, kinesis-vs-sqs-decision, sns-fifo-sqs-fanout, sns-firehose-archival, sqs-write-buffer, sqs-decoupling, kinesis-enhanced-fan-out, amazon-mq-migration
- **Key lessons:**
  - EventBridge supports multiple Lambda targets per rule with independent failure isolation — valid alternative to SNS fan-out for S3 events. Step Functions Parallel couples all branches through one orchestration layer.
  - For SQS+ASG scaling: use backlog-per-instance custom metric (messages ÷ instances) with Target Tracking. Visibility timeout must exceed max job duration with a safety margin to prevent duplicate processing.
