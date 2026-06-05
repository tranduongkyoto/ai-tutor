# Monitoring & Audit - AWS CSA Content Cache

## Services & Concepts

### Amazon CloudWatch

Core monitoring service for every AWS service. Provides metrics, logs, alarms, dashboards, and events.

#### CloudWatch Metrics
- **Metric**: variable to monitor (CPUUtilization, NetworkIn, etc.)
- **Namespace**: logical grouping of metrics (e.g., AWS/EC2)
- **Dimension**: attribute of a metric (instance id, environment) — up to **30 dimensions per metric**
- All metrics have **timestamps**
- Can create **CloudWatch Dashboards** of metrics
- Can create **Custom Metrics** (e.g., RAM utilization — not available by default)

#### CloudWatch Metric Streams
- Continually stream metrics to a destination with **near-real-time delivery** and low latency
- Destinations: **Kinesis Data Firehose** → S3, Redshift, OpenSearch, Athena
- Third-party: Datadog, Dynatrace, New Relic, Splunk, Sumo Logic
- Option to **filter metrics** to stream only a subset

#### CloudWatch Logs
- **Log group**: arbitrary name, usually representing an application
- **Log stream**: instances within application / log files / containers
- Log expiration policies: never expire, **1 day to 10 years**
- Logs **encrypted by default**; can use KMS-based encryption with own keys
- **Destinations** (where CW Logs can send):
  - Amazon S3 (exports — batch, up to 12 hours delay)
  - Kinesis Data Streams
  - Kinesis Data Firehose
  - AWS Lambda
  - OpenSearch

#### CloudWatch Logs — Sources
- SDK, CloudWatch Logs Agent, CloudWatch Unified Agent
- Elastic Beanstalk: collection from application
- ECS: collection from containers
- Lambda: collection from function logs
- VPC Flow Logs: VPC-specific logs
- API Gateway
- CloudTrail (based on filter)
- Route 53: DNS query logs

#### CloudWatch Logs for EC2
- **By default, no logs from EC2 go to CloudWatch** — must install agent
- Need to run **CloudWatch Logs Agent** on EC2; IAM permissions required
- Agent can also run on **on-premises servers**

#### CloudWatch Logs Agent vs Unified Agent
| Feature | Logs Agent (old) | Unified Agent (new) |
|---|---|---|
| Sends logs | Yes | Yes |
| System-level metrics (RAM, processes) | No | Yes |
| Centralized config | No | SSM Parameter Store |

**Unified Agent metrics collected**: CPU (active/guest/idle/system/user/steal), Disk (free/used/total), Disk IO (writes/reads/bytes/iops), RAM (free/inactive/used/total/cached), Netstat (TCP/UDP connections, packets, bytes), Processes (total/dead/blocked/idle/running/sleep), Swap Space (free/used/%)

**EC2 out-of-the-box metrics** (without agent): disk, CPU, network — only high-level

#### CloudWatch Logs Insights
- Search and analyze log data stored in CloudWatch Logs
- Purpose-built query language; automatically discovers fields from AWS services and JSON logs
- Can: fetch fields, filter by conditions, calculate aggregate stats, sort events, limit results
- Can query **multiple Log Groups across different AWS accounts**
- Save queries and add to CloudWatch Dashboards
- **It's a query engine, NOT a real-time engine**
- Queries can run up to **15 minutes**

#### CloudWatch Logs — S3 Export
- Log data can take **up to 12 hours** to become available for export
- API call: `CreateExportTask`
- **Not near-real-time** — use Logs Subscriptions for real-time needs

#### CloudWatch Logs Subscriptions
- Get **real-time** log events for processing and analysis
- Send to: Kinesis Data Streams, Kinesis Data Firehose, or Lambda
- **Subscription Filter** — filter which logs are delivered to destination
- **Cross-Account Subscription**: send log events to resources in a different AWS account (KDS, KDF)
  - Requires IAM Role (cross-account) + Destination Access Policy on recipient side

#### CloudWatch Logs Aggregation (Multi-Account & Multi-Region)
- Pattern: Multiple accounts/regions → each has Subscription Filter → feeds central Kinesis Data Streams → Kinesis Data Firehose → Amazon S3 (near-real-time)

#### CloudWatch Alarms
- Trigger notifications for any metric
- Evaluation options: sampling, %, max, min, etc.
- **Alarm States**: OK | INSUFFICIENT_DATA | ALARM
- **Period**: length of time in seconds to evaluate metric
  - High-resolution custom metrics: **10 sec, 30 sec, or multiples of 60 sec**
- **Alarm Targets**:
  - Stop, Terminate, Reboot, or Recover an EC2 instance
  - Trigger Auto Scaling Action
  - Send notification to SNS
- Alarms can be created based on **CloudWatch Logs Metrics Filters**
- Test alarms via CLI: `aws cloudwatch set-alarm-state --alarm-name "myalarm" --state-value ALARM --state-reason "testing purposes"`

#### CloudWatch Alarms — Composite Alarms
- Standard alarms are on a **single metric**
- **Composite Alarms** monitor the states of **multiple other alarms**
- Support AND / OR conditions
- Reduces "alarm noise" by creating complex conditions

#### EC2 Instance Recovery via CloudWatch Alarm
- **Status Checks**: Instance status (EC2 VM), System status (underlying hardware), Attached EBS status
- Alarm: `StatusCheckFailed_System` triggers **EC2 Instance Recovery**
- Recovery preserves: **same Private IP, Public IP, Elastic IP, metadata, placement group**

#### CloudWatch Network Synthetic Monitor
- Monitor and detect network issues between AWS apps and on-premises data center
- Identifies packet loss, latency, jitter — **no agents required**
- Tests ICMP or TCP traffic to IPv4 destinations via **Direct Connect** or **S2S VPN**
- Publishes data to CloudWatch Metrics

#### CloudWatch Container Insights
- Collect, aggregate, summarize metrics and logs from containers
- Available for: ECS, EKS, Kubernetes on EC2, Fargate (ECS and EKS)
- For EKS/Kubernetes: uses **containerized version of CloudWatch Agent** to discover containers

#### CloudWatch Lambda Insights
- Monitoring and troubleshooting for serverless applications on Lambda
- Collects system-level metrics: CPU time, memory, disk, network
- Collects diagnostic info: cold starts, Lambda worker shutdowns
- Provided as a **Lambda Layer**

#### CloudWatch Contributor Insights
- Analyze log data and create time series showing **top-N contributors**
- Find heaviest network users, bad hosts, URLs generating most errors
- Works on any AWS-generated logs (VPC Flow Logs, DNS, etc.)
- Build rules from scratch or use AWS sample rules
- AWS also provides built-in rules for other AWS service metrics

#### CloudWatch Application Insights
- Automated dashboards showing potential problems with monitored applications
- Supports EC2 with: Java, .NET, IIS Web Server, databases
- Integrates with: EBS, RDS, ELB, ASG, Lambda, SQS, DynamoDB, S3, ECS, EKS, SNS, API Gateway
- Powered by **SageMaker**
- Findings and alerts sent to **Amazon EventBridge** and **SSM OpsCenter**

---

### Amazon EventBridge (formerly CloudWatch Events)

#### Core Features
- **Schedule**: Cron jobs (e.g., trigger Lambda every hour)
- **Event Pattern**: Rules to react to a service action (e.g., IAM Root User Sign-in → SNS email)
- Trigger Lambda functions, send SQS/SNS messages

#### Event Buses
- **Default Event Bus**: AWS Services (EC2, Lambda, S3, etc.)
- **Partner Event Bus**: AWS SaaS partners (Zendesk, Datadog, etc.)
- **Custom Event Bus**: Custom applications
- Event buses accessible by other AWS accounts via **Resource-based Policies**
- Can **archive events** (all or filtered) sent to an event bus — indefinitely or set period
- Ability to **replay archived events**

#### EventBridge Rules — Sources & Destinations
- **Sources**: EC2, CodeBuild, S3, Trusted Advisor, CloudTrail (any API call), Schedule/Cron
- **Destinations**:
  - Compute: Lambda, AWS Batch, ECS Task
  - Integration: SQS, SNS, Kinesis Data Streams
  - Orchestration: Step Functions, CodePipeline, CodeBuild
  - Maintenance: SSM, EC2 Actions
- Events delivered as **JSON format**
- Optional filter on events before delivery

#### EventBridge Schema Registry
- Analyzes events in your bus and **infers the schema**
- Generates **code bindings** for your application so it knows data structure in advance
- Schemas can be **versioned**

#### EventBridge Resource-based Policy
- Manage permissions for a specific Event Bus
- Allow/deny events from another AWS account or region
- Use case: aggregate all events from AWS Organization into a single account/region

#### EventBridge + CloudTrail Integration
- Pattern: API call → CloudTrail logs it → EventBridge generates event → SNS alert
- Example 1: User calls `DeleteTable` on DynamoDB → CloudTrail → EventBridge → SNS
- Example 2: User `AssumeRole` via IAM → CloudTrail → EventBridge → SNS
- Example 3: User edits EC2 Security Group (`AuthorizeSecurityGroupIngress`) → CloudTrail → EventBridge → SNS

---

### AWS CloudTrail

#### Core Concepts
- Provides **governance, compliance, and audit** for AWS Account
- **Enabled by default**
- Records history of events / API calls made within account by: Console, SDK, CLI, AWS Services
- Can send logs to **CloudWatch Logs** or **S3**
- Trail can be applied to **All Regions (default)** or a **single Region**
- **Investigate CloudTrail first** if a resource is deleted

#### CloudTrail Event Types
| Type | Default Logged | Description |
|---|---|---|
| Management Events | Yes | Operations on resources (AttachRolePolicy, CreateSubnet, CreateTrail) |
| Data Events | No (high volume) | S3 object-level (GetObject, DeleteObject, PutObject), Lambda Invoke API |
| Insights Events | No (must enable) | Unusual activity detection |

- Management Events: can separate **Read Events** (no resource modification) from **Write Events** (may modify)
- Data Events: can separate Read and Write

#### CloudTrail Insights
- Detects **unusual activity**: inaccurate resource provisioning, hitting service limits, bursts of IAM actions, gaps in periodic maintenance
- Analyzes normal management events to create a **baseline**
- Continuously analyzes **write events** to detect unusual patterns
- Anomalies appear in: CloudTrail console, S3, EventBridge event (for automation)

#### CloudTrail Events Retention
- Events stored for **90 days** in CloudTrail
- For longer retention: **log to S3 → analyze with Athena**

---

### AWS Config

#### Core Concepts
- Helps with auditing and recording **compliance** of AWS resources
- Records configurations and **changes over time**
- Per-region service (but can be aggregated across regions and accounts)
- Configuration data can be stored in S3 (analyzed by Athena)
- Receive SNS notifications for any changes
- Does **NOT prevent** actions — it only records and evaluates (no deny capability)

#### Use Cases
- Is there unrestricted SSH access to my security groups?
- Do my S3 buckets have public access?
- How has my ALB configuration changed over time?

#### Config Rules
- **AWS Managed rules**: over 75 available
- **Custom rules**: must be defined in AWS Lambda
  - Example: evaluate if each EBS disk is gp2 type
  - Example: evaluate if each EC2 instance is t2.micro
- Rules triggered: on each config change, and/or at regular time intervals
- **Config Rules do NOT prevent actions** (no deny)
- **Pricing**: no free tier — $0.003 per config item recorded/region, $0.001 per rule evaluation/region

#### Config Rules — Remediations
- Automate remediation of non-compliant resources via **SSM Automation Documents**
- Use AWS-Managed Automation Documents or custom (can invoke Lambda functions)
- Set **Remediation Retries** if resource is still non-compliant after auto-remediation

#### Config Rules — Notifications
- Use **EventBridge** to trigger notifications when resources are non-compliant → Lambda, SNS, SQS
- Also: send all config changes and compliance state notifications directly to **SNS** (use SNS Filtering or filter client-side)

#### AWS Config Resource View
- View compliance of a resource over time (Compliant / Noncompliant status per resource)
- View configuration changes of a resource over time (timestamped timeline)
- View CloudTrail API calls for a resource over time

---

## Key Configurations

### CloudWatch Logs
- **Default retention**: never expires (must set explicitly)
- **Retention range**: 1 day to 10 years
- **Encryption**: enabled by default; KMS-CMK optional
- **EC2 logs**: NOT sent to CloudWatch by default — requires agent installation + IAM role

### CloudWatch Alarms
- **High-resolution alarm periods**: 10 sec, 30 sec, or multiples of 60 sec
- **Three states**: OK, INSUFFICIENT_DATA, ALARM
- Composite alarms can combine multiple alarms with AND/OR logic

### CloudTrail
- **Default**: enabled for all regions, logs management events only
- **Data events**: disabled by default (high volume = extra cost)
- **Insights**: disabled by default (must enable separately)
- **Retention in service**: 90 days; use S3 + Athena for longer

### AWS Config
- **Not enabled by default** — must be turned on per region
- **No free tier** for Config rules
- Rules evaluate on config change or scheduled interval
- Cannot block/deny — detection and notification only

---

## Architectural Patterns

### Real-Time Log Processing
```
CloudWatch Logs → Subscription Filter → Lambda → OpenSearch (real-time)
CloudWatch Logs → Subscription Filter → Kinesis Data Firehose → S3/Redshift (near-real-time)
CloudWatch Logs → Subscription Filter → Kinesis Data Streams → KDF/KDA/EC2/Lambda
```

### Log Aggregation (Multi-Account/Region)
```
Account A/B/C Logs → Subscription Filters → Central Kinesis Data Streams → Kinesis Data Firehose → Amazon S3
```

### Batch Log Export (Not Real-Time)
```
CloudWatch Logs → CreateExportTask → Amazon S3 (up to 12 hours delay)
```

### CloudWatch Metrics Streaming
```
CloudWatch Metrics → Kinesis Data Firehose → S3/Redshift/OpenSearch/Athena (near-real-time)
CloudWatch Metrics → 3rd party (Datadog, Splunk, New Relic, etc.)
```

### CloudTrail Long-Term Audit
```
CloudTrail (90-day) → S3 Bucket → Athena (SQL queries for analysis)
```

### Security Alerting via CloudTrail + EventBridge
```
Any API Call → CloudTrail → EventBridge rule → SNS/Lambda/SQS
Use case: root user login, security group change, DynamoDB table deletion
```

### Config Compliance Auto-Remediation
```
AWS Resource (non-compliant) → AWS Config detects → triggers SSM Automation Document → remediation action
Example: expired IAM key → Config → SSM RevokeUnusedIAMUserCredentials (retries: 5)
```

### Config Compliance Notification
```
Option 1: AWS Config → EventBridge → Lambda/SNS/SQS (specific non-compliant events)
Option 2: AWS Config → SNS (all events — config changes + compliance state)
```

### EC2 Instance Recovery
```
EC2 (StatusCheckFailed_System) → CloudWatch Alarm → EC2 Instance Recovery action
Result: same Private IP, Public IP, Elastic IP, metadata, placement group preserved
```

### Elastic Load Balancer — Combined Monitoring
- **CloudWatch**: Incoming connections metric, error codes % over time, dashboards
- **Config**: Track SG rules, config changes, ensure SSL cert assigned (compliance)
- **CloudTrail**: Track who made changes via API calls

---

## Important Numbers & Limits

| Item | Value |
|---|---|
| Max dimensions per metric | 30 |
| Log retention range | Never expire OR 1 day to 10 years |
| S3 export delay (CW Logs) | Up to 12 hours |
| Alarm high-resolution periods | 10 sec, 30 sec, multiples of 60 sec |
| CloudTrail event retention | 90 days |
| Logs Insights query max runtime | 15 minutes |
| Config managed rules available | 75+ |
| Config pricing per item | $0.003/config item recorded/region |
| Config pricing per rule eval | $0.001/rule evaluation/region |
| Config remediation retries | Configurable (example showed 5) |

---

## Diagram Descriptions

### CloudWatch Metric Streams Flow
CloudWatch Metrics → (near-real-time stream) → Kinesis Data Firehose → Amazon S3 / Amazon Redshift / Amazon OpenSearch → (S3 also) → Athena. Optionally direct to 3rd-party providers.

### CloudWatch Logs Subscriptions Flow
CloudWatch Logs → Subscription Filter → (three paths):
1. Lambda → OpenSearch Service (real-time)
2. Kinesis Data Firehose → S3 (near-real-time)
3. Kinesis Data Streams → KDF / KDA / EC2 / Lambda / ...

### Multi-Account Log Aggregation
Three separate (Account A Region 1, Account B Region 2, Account B Region 3) each with CloudWatch Logs → Subscription Filter → all feed into central Kinesis Data Streams → Kinesis Data Firehose → Amazon S3 (near real-time)

### Cross-Account Subscription
Sender account: CloudWatch Logs → Subscription Filter → (cross-account) → Recipient account: Subscription Destination → Kinesis Data Streams. Requires: IAM Role (assumable by sender) + Destination Access Policy on KDS.

### CloudWatch Logs for EC2/On-Premises
EC2 Instance (CloudWatch Logs Agent) → CloudWatch Logs. On-Premise Server (CloudWatch Logs Agent) → CloudWatch Logs. Agent needed; IAM permissions required.

### Composite Alarm Flow
EC2 Instance → (monitors CPU) CW Alarm-A (ALARM) + (monitors IOPS) CW Alarm-B (ALARM) → Composite Alarm → triggers Amazon SNS

### EC2 Instance Recovery Flow
EC2 Instance → (monitored by) CloudWatch Alarm (StatusCheckFailed_System) → (alert to) SNS Topic + (recovery action back to) EC2 Instance

### CloudWatch Network Synthetic Monitor
CloudWatch Metrics (in AWS Cloud with EC2 in private subnet) → DX Connection or VPN Connection → Corporate Data Center Server

### EventBridge Rules Diagram
Sources (EC2/CodeBuild/S3/Trusted Advisor/CloudTrail/Schedule) → optional filter → EventBridge (JSON event) → Destinations split into: Compute (Lambda/Batch/ECS), Integration (SQS/SNS/KDS), Orchestration (Step Functions/CodePipeline/CodeBuild), Maintenance (SSM/EC2 Actions)

### EventBridge Event Bus Types
AWS Services → Default Event Bus | AWS SaaS Partners (Zendesk, Datadog) → Partner Event Bus | Custom Apps → Custom Event Bus

### EventBridge Resource-based Policy
AWS Account 2 (Lambda function) → PutEvents → EventBridge Bus in Account 1 (central-event-bus). Policy on bus allows specific account principal to call events:PutEvents.

### CloudTrail Diagram
SDK + CLI + Console + IAM Users/Roles → CloudTrail Console → (Inspect & Audit) + exports to CloudWatch Logs + S3 Bucket

### CloudTrail Insights Flow
Management Events → (continuous analysis) → CloudTrail Insights → generates Insights Events → CloudTrail Console + S3 Bucket + EventBridge event

### CloudTrail Events Retention Flow
Management Events + Data Events + Insights Events → CloudTrail (90-day retention) → S3 Bucket (long-term retention) → Athena (analyze)

### EventBridge Intercept API Calls
User (DeleteTable API call) → DynamoDB → CloudTrail (logs API call) → EventBridge (event) → SNS (alert)

### EventBridge + CloudTrail Integration Flows
Flow 1: User AssumeRole → IAM → CloudTrail → EventBridge → SNS
Flow 2: User edits SG Inbound Rules (AuthorizeSecurityGroupIngress) → EC2/Security Group → CloudTrail → EventBridge → SNS

### AWS Config Resource View
Three-panel view: (1) compliance list per resource (Compliant/Noncompliant), (2) configuration change timeline with timestamps, (3) CloudTrail events timeline linked to resource

### Config Remediations Flow
IAM Access Key (expired, NON_COMPLIANT) → monitored by AWS Config → triggers Auto-Remediation Action (SSM Document: AWSConfigRemediation-RevokeUnusedIAMUserCredentials, Retries: 5) → deactivate key

### Config Notifications — Two Patterns
Pattern 1: AWS Resources (non-compliant) → AWS Config → EventBridge → Lambda/SNS/SQS
Pattern 2: AWS Resources → AWS Config (all events: config changes + compliance state) → SNS → Admin

### CloudWatch Insights Comparison Summary
- Container Insights: ECS/EKS/K8s/Fargate → metrics and logs
- Lambda Insights: serverless → detailed Lambda metrics (provided as Lambda Layer)
- Contributors Insights: find "Top-N" contributors through CW Logs
- Application Insights: automated dashboard for app + related AWS services (powered by SageMaker)

---

## Exam-Relevant Details

### CloudWatch vs CloudTrail vs Config — Key Distinction
| Service | Purpose | Key Phrase |
|---|---|---|
| CloudWatch | Performance monitoring, metrics, logs, alerting | "monitor metrics", "dashboards", "alarms" |
| CloudTrail | API call history, who did what | "audit", "API calls", "who deleted", "governance" |
| Config | Resource configuration compliance over time | "compliance rules", "configuration change history", "drift detection" |

### Common Exam Traps

- **RAM not in EC2 default metrics** — must use CloudWatch Unified Agent (Custom Metric)
- **EC2 logs not automatic** — must install CloudWatch Logs Agent + correct IAM permissions
- **S3 export is NOT real-time** — up to 12-hour delay; use Subscriptions for real-time
- **Logs Insights is NOT real-time** — it's a query engine (historical analysis)
- **Config Rules cannot DENY actions** — they only record and alert (not preventive like SCP/IAM)
- **CloudTrail Data Events NOT logged by default** — must enable explicitly (extra cost)
- **CloudTrail Insights NOT enabled by default** — must enable
- **CloudTrail retention is 90 days** — for longer, must ship to S3
- **Config is per-region** — CloudTrail is global service
- **Composite Alarms** reduce alarm noise by combining multiple alarms with AND/OR
- **Old Logs Agent** can only send logs; **Unified Agent** sends logs AND system metrics (RAM, etc.)
- **EC2 recovery** preserves same Private/Public/Elastic IP and metadata
- **EventBridge = CloudWatch Events** (renamed) — they are the same service

### Keyword Signals
- "detect who deleted a resource" → **CloudTrail**
- "monitor RAM on EC2" → **CloudWatch Unified Agent / Custom Metric**
- "ensure SSH port not open on security groups" → **AWS Config**
- "alert when CPU > 80%" → **CloudWatch Alarm**
- "schedule Lambda to run every hour" → **EventBridge (schedule/cron)**
- "react to IAM root login" → **EventBridge event pattern**
- "stream metrics to Splunk/Datadog" → **CloudWatch Metric Streams**
- "analyze logs across multiple accounts" → **CloudWatch Logs Insights (cross-account)**
- "find top IP addresses making most requests" → **CloudWatch Contributor Insights**
- "troubleshoot Lambda cold starts" → **CloudWatch Lambda Insights**
- "auto-remediate non-compliant resources" → **AWS Config + SSM Automation**
- "near-real-time log delivery to S3" → **CloudWatch Logs Subscriptions → Kinesis Firehose → S3**
- "real-time log processing" → **CloudWatch Logs Subscriptions → Lambda or KDS**
- "batch export logs to S3" → **CreateExportTask (up to 12 hours)**
- "detect unusual API patterns" → **CloudTrail Insights**
- "archive and replay events" → **EventBridge event archiving**
- "aggregate events from entire AWS Organization" → **EventBridge Resource-based Policy**
