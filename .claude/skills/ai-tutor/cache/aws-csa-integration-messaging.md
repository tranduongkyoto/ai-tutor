# Integration & Messaging - AWS CSA Content Cache

## Services & Concepts

### Amazon SQS (Simple Queue Service)
- Fully managed message queue service; oldest AWS offering (>10 years)
- Model: **queue model** — producers send, consumers poll
- Primary use case: **decouple applications** to handle traffic spikes independently
- Consumers: EC2 instances, on-prem servers, AWS Lambda
- Producer API: `SendMessage`; Consumer API: `ReceiveMessage`, `DeleteMessage`
- Message persisted until consumer explicitly deletes it

#### SQS Standard Queue
- Unlimited throughput, unlimited number of messages in queue
- **At-least-once delivery** (occasionally duplicates)
- **Best-effort ordering** (messages can arrive out of order)
- Default message retention: **4 days**; max: **14 days**
- Max message size: **1,024 KB (1 MB)**
- Latency: <10 ms on publish and receive

#### SQS FIFO Queue
- **First-In-First-Out** — strict message ordering guaranteed
- **Exactly-once processing** via Deduplication ID (removes duplicates)
- **Ordering by Message Group ID** — all messages in same group are ordered (mandatory parameter)
- Throughput: **300 msg/s** without batching; **3,000 msg/s** with batching
- FIFO queue name must end in `.fifo`

#### SQS Message Visibility Timeout
- After a message is polled, it becomes **invisible** to other consumers
- Default visibility timeout: **30 seconds**
- If not processed and deleted within timeout → message becomes visible again → risk of double processing
- Consumer can call `ChangeMessageVisibility` API to extend the timeout
- Too high timeout + consumer crash = long re-processing delay
- Too low timeout = duplicate processing

#### SQS Long Polling
- Consumer waits for messages if queue is empty (avoids empty responses)
- Reduces number of API calls, decreases latency
- Wait time: **1 to 20 seconds** (20 seconds preferred)
- Long Polling preferred over Short Polling
- Enable at queue level or per-API call using `WaitTimeSeconds`

#### SQS Dead Letter Queue (DLQ)
- Messages that fail processing repeatedly are moved to a DLQ
- Useful for debugging/isolating problematic messages
- Configured via `maxReceiveCount` threshold

#### SQS Security
- **In-flight encryption**: HTTPS API
- **At-rest encryption**: KMS keys
- **Client-side encryption**: client manages encryption/decryption
- **IAM policies**: regulate access to SQS API
- **SQS Access Policies** (resource-based, similar to S3 bucket policies):
  - Cross-account access to SQS queues
  - Allow other AWS services (SNS, S3) to write to an SQS queue

---

### Amazon SNS (Simple Notification Service)
- **Pub/Sub model** — event producer sends ONE message to ONE topic; all subscribers receive it
- "Push" to subscribers — no polling required
- Limits: up to **12,500,000 subscriptions per topic**; up to **100,000 topics**
- Each subscriber gets ALL messages by default (can use filter policies to limit)

#### SNS Subscribers (supported targets)
- Amazon SQS
- AWS Lambda
- Amazon Kinesis Data Firehose
- Email / Email-JSON
- SMS & Mobile Push Notifications
- HTTP(S) Endpoints

#### SNS Publishers (AWS services that send to SNS)
- CloudWatch Alarms
- AWS Budgets
- AWS Lambda
- Auto Scaling Group (notifications)
- S3 Bucket (events)
- DynamoDB
- CloudFormation (state changes)
- AWS DMS (new replication)
- RDS Events

#### SNS How to Publish
- **Topic Publish** (SDK): create topic → create subscription(s) → publish to topic
- **Direct Publish** (mobile apps SDK): create platform application → create platform endpoint → publish to platform endpoint
  - Supports: Google GCM, Apple APNS, Amazon ADM

#### SNS FIFO Topic
- Ordering by **Message Group ID**
- Deduplication using Deduplication ID or **Content-Based Deduplication**
- Can have SQS Standard and FIFO queues as subscribers
- Limited throughput — same as SQS FIFO (300/3000 msg/s)

#### SNS Message Filtering
- JSON policy attached to a subscription to filter which messages it receives
- Subscription without filter policy receives **every message**
- Use case: route "Placed" orders to one SQS queue, "Cancelled" to another — same SNS topic

#### SNS Security
- **In-flight encryption**: HTTPS API
- **At-rest encryption**: KMS keys
- **Client-side encryption**: client manages it
- **IAM policies**: regulate access to SNS API
- **SNS Access Policies** (similar to S3 bucket policies):
  - Cross-account access to SNS topics
  - Allow other services (S3) to write to an SNS topic

---

### Amazon Kinesis Data Streams (KDS)
- Collect and store streaming data in **real-time**
- Use cases: click streams, IoT devices, metrics & logs, application events
- Data producers: applications, Kinesis Agent, SDK
- Data consumers: applications, Lambda, Amazon Data Firehose, Managed Apache Flink

#### KDS Key Features
- Data retention: **1 to 365 days**
- Ability to **replay** (reprocess) data by consumers
- Data **cannot be deleted** — only expires after retention period
- Record size: up to **1 MB** per record (slide says 10MiB typical use case is "small" real-time data; max blob per record is 1 MB)
- **Ordering guarantee** for records with the same Partition Key (shard-level ordering)
- At-rest encryption: KMS; in-flight: HTTPS
- **KPL (Kinesis Producer Library)**: write optimized producer applications
- **KCL (Kinesis Client Library)**: write optimized consumer applications

#### KDS Capacity Modes

**Provisioned Mode:**
- Manually choose number of shards
- Each shard: **1 MB/s in** (or 1,000 records/s write)
- Each shard: **2 MB/s out**
- Scale manually (add/remove shards)
- Billing: per shard provisioned per hour

**On-Demand Mode:**
- No capacity provisioning needed
- Default capacity: **4 MB/s in** or **4,000 records/s**
- Scales automatically based on peak throughput in last 30 days
- Billing: per stream per hour + data in/out per GB

---

### Amazon Data Firehose (formerly Kinesis Data Firehose)
- Fully managed, **serverless**, automatic scaling
- **Near Real-Time** delivery (buffering based on size or time — NOT real-time)
- No data storage (no replay capability)
- Supports formats: CSV, JSON, Parquet, Avro, Raw Text, Binary

#### Firehose Destinations
- **AWS**: Amazon S3, Amazon Redshift, Amazon OpenSearch Service
- **3rd Party**: Splunk, MongoDB, Datadog, New Relic
- **Custom**: HTTP Endpoint

#### Native Features
- Conversions to Parquet / ORC (columnar formats)
- Compression: gzip / snappy
- Buffering: configurable by size and time before delivering batch writes
- Failed/all data backup to S3 backup bucket

#### Lambda/Custom Features
- Custom data transformations via AWS Lambda (e.g., CSV to JSON)

---

### Amazon MQ
- Managed message broker for **RabbitMQ** and **ActiveMQ**
- Use case: migrating on-premises applications to AWS that already use open protocols
- Supports open protocols: **MQTT, AMQP, STOMP, Openwire, WSS**
- Does NOT scale as much as SQS/SNS (runs on servers, not serverless)
- Runs on servers; supports **Multi-AZ with failover** for HA
- Has both queue features (~SQS) and topic features (~SNS)

#### Amazon MQ High Availability
- Active/Standby configuration across two AZs
- Both brokers share **Amazon EFS** for storage
- Client connects to active broker; fails over to standby on failure

---

## Key Configurations

### SQS
- Message visibility timeout default: **30 seconds** (configurable)
- Message retention default: **4 days**; max: **14 days**
- Max message size: **1,024 KB**
- Poll batch size: up to **10 messages** at a time
- Long polling wait time: **1–20 seconds**
- FIFO throughput: **300 msg/s** (no batch), **3,000 msg/s** (with batch)

### SNS
- Subscriptions per topic: up to **12,500,000**
- Topics per account: up to **100,000**
- SNS data is NOT persisted — lost if not delivered

### Kinesis Data Streams
- Default on-demand capacity: **4 MB/s in**, **4,000 records/s**
- Per shard provisioned: **1 MB/s in**, **2 MB/s out**
- Retention: **1–365 days** (default 24 hours)
- Scales based on last **30 days** peak in on-demand mode

### Firehose
- Record max size: **up to 1 MB**
- Near real-time (buffers before delivery — not instant)
- No storage, no replay

---

## Architectural Patterns

### SQS + ASG (Auto Scaling)
- SQS Queue → EC2 instances in ASG poll for messages
- CloudWatch Metric: **ApproximateNumberOfMessages** (queue length)
- CloudWatch Alarm triggers → ASG scale out/in
- Pattern: decouple front-end ASG (producers) from back-end ASG (consumers) via SQS queue

### SQS as Database Write Buffer
- High-traffic front-end enqueues messages to SQS
- Back-end ASG dequeues and inserts into RDS/Aurora/DynamoDB at controlled rate
- Prevents losing transactions during traffic spikes

### SNS + SQS Fan-Out
- Publish once to SNS topic → delivered to multiple SQS queues
- Each SQS queue processed independently (decoupled, no data loss)
- Enables: data persistence, delayed processing, retries
- Can add new SQS subscribers at any time without changing producer
- SQS queue access policy must allow SNS to write
- Supports **Cross-Region Delivery** (SNS → SQS in different region)

### S3 Events to Multiple Queues (Fan-Out)
- S3 allows only **one event rule per event-type + prefix combination**
- To send same S3 event to multiple targets: S3 → SNS → fan-out to multiple SQS queues + Lambda

### SNS → Kinesis Data Firehose → S3
- SNS topic subscriber = Kinesis Data Firehose
- Enables archiving SNS messages to S3 or any Firehose destination

### SNS FIFO + SQS FIFO Fan-Out
- Use when you need: fan-out + ordering + deduplication
- SNS FIFO topic → multiple SQS FIFO queues → downstream consumers

### SNS Message Filtering Fan-Out
- Single SNS topic → multiple subscriptions with filter policies
- Route "Placed" → SQS Queue A; "Cancelled" → SQS Queue B + Email; "Declined" → SQS Queue C
- One SQS queue with no filter receives all messages

### When to Use SQS vs SNS vs Kinesis
- **SQS**: task queue, decouple services, work queue (workers pull), no ordering needed (Standard), ordering needed (FIFO)
- **SNS**: fan-out notifications, one event → many receivers, fire-and-forget
- **Kinesis**: real-time analytics, streaming ETL, replay needed, multiple consumers reading same stream

### When to Use Amazon MQ
- Existing on-premises apps using MQTT/AMQP/STOMP → lift-and-shift without re-engineering
- Do NOT use MQ for new cloud-native apps (use SQS/SNS instead)

---

## Important Numbers & Limits

| Service | Parameter | Value |
|---------|-----------|-------|
| SQS Standard | Throughput | Unlimited |
| SQS Standard | Message size | 1,024 KB |
| SQS Standard | Retention (default) | 4 days |
| SQS Standard | Retention (max) | 14 days |
| SQS Standard | Visibility timeout (default) | 30 seconds |
| SQS Standard | Max messages per poll | 10 |
| SQS Standard | Long polling wait time | 1–20 seconds |
| SQS FIFO | Throughput (no batch) | 300 msg/s |
| SQS FIFO | Throughput (with batch) | 3,000 msg/s |
| SNS | Subscriptions per topic | 12,500,000 |
| SNS | Topics per account | 100,000 |
| KDS Provisioned | Write per shard | 1 MB/s or 1,000 records/s |
| KDS Provisioned | Read per shard | 2 MB/s |
| KDS On-Demand | Default write | 4 MB/s or 4,000 records/s |
| KDS | Retention | 1–365 days |
| KDS | Auto-scale lookback | 30 days peak |
| Firehose | Record size | Up to 1 MB |
| Firehose | Data storage | None (no replay) |

---

## Diagram Descriptions

### SQS Queue Diagram (p4)
- Multiple Producers (left) → send messages → SQS Queue (center) → multiple Consumers poll messages (right)
- Shows 1-to-many consumption with parallel polling

### SQS with ASG Diagram (p9)
- SQS Queue → EC2 instances poll for messages
- SQS Queue → CloudWatch Metric (ApproximateNumberOfMessages) → CloudWatch Alarm (on breach) → ASG scales EC2 instances

### SQS Decouple Application Tiers Diagram (p10, p19)
- Requests → Front-end ASG (auto-scaling) → SendMessage → SQS Queue (infinitely scalable) → ReceiveMessages → Back-end ASG (auto-scaling)
- Both tiers scale independently

### SQS as DB Buffer Diagram (p18)
- Requests → Front-end ASG → SQS Queue → Back-end ASG → inserts into RDS/Aurora/DynamoDB
- Protects database from write storms

### SNS Pub/Sub vs Direct Integration Diagram (p20)
- Left: Buying Service → directly calls Email, Fraud, Shipping, SQS (tight coupling)
- Right: Buying Service → SNS Topic → fans out to Email, Fraud, Shipping, SQS (decoupled)

### SNS Fan-Out with SQS Diagram (p26)
- Buying Service → SNS Topic → two SQS Queues → Fraud Service + Shipping Service

### S3 Events Fan-Out Diagram (p27)
- S3 object created → S3 events → SNS Topic → fan-out to 2x SQS Queues + Lambda

### SNS → Firehose → S3 Diagram (p28)
- Buying Service → SNS Topic → Kinesis Data Firehose → Amazon S3 / Any KDF Destination

### SNS FIFO + SQS FIFO Fan-Out Diagram (p30)
- Buying Service → SNS FIFO Topic → SQS FIFO Queue (Fraud) + SQS FIFO Queue (Shipping)

### SNS Message Filtering Diagram (p31)
- Buying Service → SNS Topic → 3 filter policies (State: Placed / Cancelled / Declined) → targeted SQS queues + 1 SQS queue with no filter (receives all)

### Kinesis Data Streams Architecture Diagram (p32)
- Real-time data (click streams, IoT, metrics/logs) → Producers (Applications, Kinesis Agent) → KDS → Consumers (Application, Lambda, Firehose, Managed Apache Flink)

### Amazon Data Firehose Diagram (p34)
- Producers (Applications, Client, SDK, Kinesis Agent, KDS, CloudWatch, IoT) → records up to 1 MB → Firehose → optional Lambda transformation → batch writes to S3/Redshift/OpenSearch/3rd party/HTTP; failed data → S3 backup bucket

### Amazon MQ High Availability Diagram (p38)
- Region us-east-1: ACTIVE broker in AZ us-east-1a + STANDBY broker in AZ us-east-1b
- Both brokers share Amazon EFS for storage
- Client connects to active; on failure, fails over to standby

### SQS vs SNS vs Kinesis Comparison Diagram (p36)
- Three-column comparison table (see Exam-Relevant Details section)

---

## Exam-Relevant Details

### SQS vs SNS vs Kinesis — Core Distinctions

| Feature | SQS | SNS | Kinesis |
|---------|-----|-----|---------|
| Model | Pull (consumers poll) | Push (subscribers receive) | Pull (standard) / Push (enhanced fan-out) |
| Data persistence | Yes (up to 14 days) | No (lost if undelivered) | Yes (up to 365 days) |
| Replay | No | No | Yes |
| Consumers | Many workers, each gets unique message | All subscribers get same message | Multiple consumers, each can replay |
| Ordering | FIFO queue only | FIFO topic only | Per shard (by Partition Key) |
| Throughput provisioning | Not needed | Not needed | Provisioned or On-Demand |
| Use case | Task queues, decoupling | Notifications, fan-out | Real-time analytics, ETL, big data |

### Critical Traps

- **SQS Standard duplicates**: at-least-once delivery → design consumers to be idempotent
- **Visibility timeout too low**: message re-appears before consumer finishes → duplicates
- **Visibility timeout too high**: crashed consumer causes long re-processing delays
- **SNS data is NOT persisted**: if subscriber is down when SNS publishes, message is LOST (unlike SQS)
- **Firehose ≠ real-time**: it is "near real-time" due to buffering — KDS is real-time
- **Firehose has no replay**: no data storage → cannot reprocess; KDS has replay
- **FIFO queue name must end in `.fifo`** — required naming convention
- **S3 event + multiple targets**: you can only have ONE S3 event rule per event-type+prefix — use SNS fan-out to reach multiple targets
- **Amazon MQ vs SQS/SNS**: MQ is for migrating on-prem apps using MQTT/AMQP; new cloud-native apps should use SQS/SNS
- **MQ does not scale like SQS/SNS**: runs on servers, not serverless
- **KDS Enhanced Fan-Out**: push model giving 2 MB/s per shard *per consumer* (vs standard 2 MB/s per shard shared)
- **SNS FIFO + SQS FIFO**: required when you need fan-out AND ordering AND deduplication simultaneously
- **SQS access policy required for SNS fan-out**: SQS queue must explicitly allow SNS to send messages

### Keyword-to-Service Mapping

| Keyword in question | Points to |
|--------------------|-----------|
| "decouple applications", "worker queue" | SQS |
| "exactly-once", "ordered messages", "FIFO" | SQS FIFO |
| "fan-out", "one message many receivers", "pub/sub" | SNS |
| "real-time streaming", "replay data", "click streams" | Kinesis Data Streams |
| "near real-time", "load data into S3/Redshift", "ETL sink" | Amazon Data Firehose |
| "open protocols", "MQTT", "AMQP", "migrate from on-prem MQ" | Amazon MQ |
| "buffer database writes", "absorb traffic spikes" | SQS |
| "scale EC2 based on queue depth" | SQS + CloudWatch ApproximateNumberOfMessages + ASG |
| "send S3 event to multiple queues" | S3 → SNS → SQS fan-out |
| "ordering + fan-out + deduplication" | SNS FIFO + SQS FIFO |
| "filter messages per subscriber" | SNS Message Filtering |
