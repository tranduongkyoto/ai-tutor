# Keyword Patterns

Quick-fire exam trigger phrases → correct AWS service/pattern mappings for the SAA-C03 exam. Used by the `keyword-drill` mode.

---

## Domain 1: Design Secure Architectures (30%)

### Pattern: iam-cross-account
- trigger: "cross-account access + simultaneous access needed"
- answer: "Resource-based policy"
- distractors: ["IAM role with AssumeRole", "AWS Organizations SCP", "IAM user in each account"]
- explanation: "Resource-based policies allow cross-account access without switching roles, enabling simultaneous access to resources in both accounts"
- exam-domain: 1
- source: cheat-sheet

### Pattern: iam-permission-boundary
- trigger: "delegated admin IAM — limit max permissions"
- answer: "Permission Boundaries"
- distractors: ["Service Control Policies (SCPs)", "IAM inline policies", "AWS Organizations OUs"]
- explanation: "Permission Boundaries set the maximum permissions an IAM entity can have, allowing delegation without granting unlimited power"
- exam-domain: 1
- source: cheat-sheet

### Pattern: encryption-audit-trail
- trigger: "encryption with audit trail of key usage"
- answer: "SSE-KMS (Server-Side Encryption with Key Management Service)"
- distractors: ["SSE-S3", "SSE-C (customer-provided keys)", "Client-side encryption"]
- explanation: "SSE-KMS integrates with CloudTrail to log every use of the encryption key, providing an audit trail"
- exam-domain: 1
- source: exam-1

### Pattern: encryption-cheapest
- trigger: "cheapest server-side encryption for S3"
- answer: "SSE-S3 (Server-Side Encryption with S3 managed keys)"
- distractors: ["SSE-KMS", "SSE-C", "Client-side encryption with AWS SDK"]
- explanation: "SSE-S3 is free with no per-request charges, while SSE-KMS incurs API call costs"
- exam-domain: 1
- source: exam-1

### Pattern: s3-cloudfront-restrict
- trigger: "restrict S3 access to CloudFront only"
- answer: "Origin Access Identity (OAI) / Origin Access Control (OAC)"
- distractors: ["S3 bucket policy with IP whitelist", "VPC endpoint for S3", "AWS WAF on CloudFront"]
- explanation: "OAI/OAC creates a special CloudFront identity that S3 recognizes, blocking direct S3 access"
- exam-domain: 1
- source: exam-1

### Pattern: signed-url-vs-cookie
- trigger: "signed URLs vs signed cookies — when to use which"
- answer: "Signed URLs for individual files, signed cookies for multiple files/streaming"
- distractors: ["Signed URLs for streaming", "Signed cookies for single files", "Both are interchangeable"]
- explanation: "URLs are per-file; cookies apply to all matching paths — use cookies for video streaming or multi-file access"
- exam-domain: 1
- source: exam-1

### Pattern: shield-advanced
- trigger: "L7 DDoS protection + cost protection from DDoS scaling"
- answer: "AWS Shield Advanced"
- distractors: ["AWS WAF alone", "AWS Shield Standard", "CloudFront with rate limiting"]
- explanation: "Shield Advanced provides L7 DDoS protection, 24/7 DRT access, and cost protection for scaling during attacks"
- exam-domain: 1
- source: cheat-sheet

### Pattern: firewall-manager
- trigger: "multi-account WAF policy management"
- answer: "AWS Firewall Manager"
- distractors: ["AWS WAF with rules", "AWS Organizations SCP", "AWS Config rules"]
- explanation: "Firewall Manager centrally configures WAF rules, Shield Advanced, and security groups across multiple accounts"
- exam-domain: 1
- source: cheat-sheet

### Pattern: config-compliance
- trigger: "compliance audit automation — check resource configurations"
- answer: "AWS Config rules"
- distractors: ["AWS CloudTrail", "AWS Trusted Advisor", "Amazon Inspector"]
- explanation: "Config rules continuously evaluate resource configurations against compliance requirements"
- exam-domain: 1
- source: cheat-sheet

### Pattern: cloudtrail-api
- trigger: "API activity logging — who did what when"
- answer: "AWS CloudTrail"
- distractors: ["Amazon CloudWatch Logs", "AWS Config", "VPC Flow Logs"]
- explanation: "CloudTrail records all API calls in your account, providing a complete audit trail of actions"
- exam-domain: 1
- source: cheat-sheet

### Pattern: macie-sensitive-data
- trigger: "sensitive data discovery in S3 — PII, financial data"
- answer: "Amazon Macie"
- distractors: ["Amazon Inspector", "AWS Config", "Amazon GuardDuty"]
- explanation: "Macie uses ML to discover and classify sensitive data (PII, financial) stored in S3 buckets"
- exam-domain: 1
- source: cheat-sheet

### Pattern: inspector-vuln
- trigger: "vulnerability scanning for EC2 instances and containers"
- answer: "Amazon Inspector"
- distractors: ["Amazon GuardDuty", "AWS Config", "Amazon Macie"]
- explanation: "Inspector scans EC2 instances, container images, and Lambda functions for software vulnerabilities and network exposure"
- exam-domain: 1
- source: cheat-sheet

### Pattern: guardduty-threat
- trigger: "crypto mining detection / threat detection across AWS accounts"
- answer: "Amazon GuardDuty"
- distractors: ["Amazon Inspector", "AWS Config", "Amazon Detective"]
- explanation: "GuardDuty uses ML to detect threats including crypto mining, compromised instances, and unusual API calls"
- exam-domain: 1
- source: exam-2

### Pattern: cognito-user-pool
- trigger: "user authentication for web/mobile app — sign-up, sign-in, MFA"
- answer: "Amazon Cognito User Pools"
- distractors: ["Cognito Identity Pools", "IAM users", "AWS SSO (IAM Identity Center)"]
- explanation: "User Pools provide sign-up/sign-in, MFA, and token-based auth for web/mobile apps"
- exam-domain: 1
- source: common

### Pattern: cognito-identity-pool
- trigger: "temporary AWS credentials for mobile app users"
- answer: "Amazon Cognito Identity Pools (Federated Identities)"
- distractors: ["Cognito User Pools", "IAM roles with AssumeRole", "AWS STS directly"]
- explanation: "Identity Pools exchange identity tokens for temporary AWS credentials, enabling direct access to AWS services"
- exam-domain: 1
- source: common

### Pattern: kms-key-rotation
- trigger: "automatic encryption key rotation — annual compliance requirement"
- answer: "AWS KMS automatic key rotation"
- distractors: ["Manual key rotation with re-encryption", "SSE-S3 with new key", "CloudHSM key rotation"]
- explanation: "KMS automatic key rotation rotates the backing key annually while keeping the same key ID — transparent to applications"
- exam-domain: 1
- source: common

### Pattern: secrets-manager
- trigger: "rotate database credentials automatically"
- answer: "AWS Secrets Manager"
- distractors: ["SSM Parameter Store SecureString", "AWS KMS", "IAM user access keys"]
- explanation: "Secrets Manager supports automatic rotation of RDS, Redshift, and DocumentDB credentials via Lambda"
- exam-domain: 1
- source: common

### Pattern: ssm-parameter-store
- trigger: "store configuration values and secrets — free tier available"
- answer: "AWS Systems Manager (SSM) Parameter Store"
- distractors: ["AWS Secrets Manager", "AWS AppConfig", "S3 encrypted bucket"]
- explanation: "Parameter Store is free for standard parameters; Secrets Manager costs $0.40/secret/month but adds rotation"
- exam-domain: 1
- source: common

### Pattern: nacl-vs-sg
- trigger: "stateless firewall at subnet level — explicit deny rules"
- answer: "Network Access Control List (NACL)"
- distractors: ["Security Group", "AWS WAF", "AWS Network Firewall"]
- explanation: "NACLs are stateless, operate at subnet level, and support explicit deny rules — unlike Security Groups which are stateful and allow-only"
- exam-domain: 1
- source: common

---

## Domain 2: Design Resilient Architectures (26%)

### Pattern: multi-az-standby
- trigger: "Multi-AZ failover — can the standby serve read traffic?"
- answer: "No — Multi-AZ standby is for failover only, use Read Replicas for reads"
- distractors: ["Yes, standby handles reads automatically", "Yes, with connection string change", "Only during failover events"]
- explanation: "RDS Multi-AZ standby is synchronous replication for HA — it cannot serve traffic until promoted during failover"
- exam-domain: 2
- source: exam-1

### Pattern: sqs-decouple
- trigger: "decouple writes to DynamoDB / handle write spikes"
- answer: "Amazon Simple Queue Service (SQS) as a write buffer"
- distractors: ["DynamoDB Accelerator (DAX)", "DynamoDB Auto Scaling", "Amazon Kinesis Data Streams"]
- explanation: "SQS buffers writes during spikes, allowing consumers to process at a steady rate to DynamoDB"
- exam-domain: 2
- source: exam-1

### Pattern: rabbitmq-migration
- trigger: "RabbitMQ or ActiveMQ migration to AWS"
- answer: "Amazon MQ"
- distractors: ["Amazon SQS", "Amazon SNS", "Amazon Kinesis"]
- explanation: "Amazon MQ is a managed message broker compatible with RabbitMQ and ActiveMQ protocols — no code changes needed"
- exam-domain: 2
- source: exam-1

### Pattern: asg-target-tracking
- trigger: "auto-scale based on CPU/request count target"
- answer: "Auto Scaling Group (ASG) with target tracking scaling policy"
- distractors: ["ASG with simple scaling", "ASG with step scaling", "Manual scaling"]
- explanation: "Target tracking automatically adjusts capacity to maintain a target metric value (e.g., 70% CPU)"
- exam-domain: 2
- source: common

### Pattern: dr-backup-restore
- trigger: "cheapest Disaster Recovery strategy — highest RTO/RPO acceptable"
- answer: "Backup & Restore"
- distractors: ["Pilot Light", "Warm Standby", "Multi-Region Active/Active"]
- explanation: "Backup & Restore is the lowest cost DR strategy but has the highest RTO/RPO (hours)"
- exam-domain: 2
- source: cheat-sheet

### Pattern: dr-pilot-light
- trigger: "minimal core infrastructure running in DR region"
- answer: "Pilot Light"
- distractors: ["Backup & Restore", "Warm Standby", "Multi-Region Active/Active"]
- explanation: "Pilot Light keeps minimal critical components running (e.g., DB replication) — scale up on failure"
- exam-domain: 2
- source: cheat-sheet

### Pattern: dr-warm-standby
- trigger: "scaled-down but fully functional environment in DR region"
- answer: "Warm Standby"
- distractors: ["Pilot Light", "Backup & Restore", "Multi-Region Active/Active"]
- explanation: "Warm Standby runs a scaled-down copy of the full environment — scale up quickly on failure"
- exam-domain: 2
- source: cheat-sheet

### Pattern: dr-active-active
- trigger: "lowest RTO/RPO — zero downtime DR — highest cost acceptable"
- answer: "Multi-Region Active/Active"
- distractors: ["Warm Standby", "Pilot Light", "Backup & Restore"]
- explanation: "Active/Active runs full production in multiple regions simultaneously — near-zero RTO/RPO, highest cost"
- exam-domain: 2
- source: cheat-sheet

### Pattern: route53-failover
- trigger: "cross-region DNS failover — automatic traffic rerouting"
- answer: "Route 53 failover routing policy"
- distractors: ["Route 53 weighted routing", "Route 53 latency routing", "Global Accelerator"]
- explanation: "Failover routing with health checks automatically routes traffic to a healthy region when the primary fails"
- exam-domain: 2
- source: cheat-sheet

### Pattern: route53-latency
- trigger: "route users to lowest-latency AWS region"
- answer: "Route 53 latency-based routing policy"
- distractors: ["Route 53 geolocation routing", "Route 53 weighted routing", "CloudFront"]
- explanation: "Latency routing directs users to the region with the lowest network latency, not geographic proximity"
- exam-domain: 2
- source: cheat-sheet

### Pattern: global-tables
- trigger: "multi-region active-active database — sub-millisecond reads globally"
- answer: "DynamoDB Global Tables"
- distractors: ["Aurora Global Database", "RDS Cross-Region Read Replicas", "ElastiCache Global Datastore"]
- explanation: "Global Tables provide multi-region active-active replication with single-digit millisecond reads in any region"
- exam-domain: 2
- source: cheat-sheet

### Pattern: aurora-global
- trigger: "cross-region relational database disaster recovery — RPO under 1 second"
- answer: "Amazon Aurora Global Database"
- distractors: ["RDS Multi-AZ", "RDS Cross-Region Read Replicas", "DynamoDB Global Tables"]
- explanation: "Aurora Global Database replicates to secondary regions with <1 second RPO and <1 minute RTO for failover"
- exam-domain: 2
- source: common

### Pattern: sqs-fifo
- trigger: "guaranteed message ordering + exactly-once processing"
- answer: "Amazon SQS FIFO queue"
- distractors: ["SQS Standard queue", "Amazon Kinesis", "Amazon MQ"]
- explanation: "FIFO queues guarantee message ordering and exactly-once delivery — Standard queues offer best-effort ordering only"
- exam-domain: 2
- source: common

### Pattern: sns-sqs-fanout
- trigger: "send same event to multiple processing pipelines simultaneously"
- answer: "SNS topic → multiple SQS queues (fan-out)"
- distractors: ["SQS with multiple consumers", "EventBridge with multiple targets", "Kinesis with multiple consumers"]
- explanation: "SNS fan-out to SQS ensures each subscriber queue gets an independent copy for parallel processing"
- exam-domain: 2
- source: common

### Pattern: elb-health-check
- trigger: "automatically replace unhealthy EC2 instances behind load balancer"
- answer: "Auto Scaling Group (ASG) with Elastic Load Balancer (ELB) health checks"
- distractors: ["CloudWatch alarm + Lambda", "Route 53 health checks", "EC2 Auto Recovery"]
- explanation: "ASG with ELB health checks terminates instances that fail load balancer health checks and launches replacements"
- exam-domain: 2
- source: common

### Pattern: s3-versioning-protection
- trigger: "protect S3 objects from accidental deletion"
- answer: "S3 Versioning + MFA Delete"
- distractors: ["S3 Object Lock", "S3 Cross-Region Replication", "S3 Lifecycle policy"]
- explanation: "Versioning preserves all object versions; MFA Delete requires MFA to permanently delete versions"
- exam-domain: 2
- source: common

---

## Domain 3: Design High-Performing Architectures (24%)

### Pattern: aurora-serverless
- trigger: "unpredictable OLTP workload — auto-scaling relational database"
- answer: "Amazon Aurora Serverless"
- distractors: ["Aurora Provisioned", "RDS with Auto Scaling", "DynamoDB on-demand"]
- explanation: "Aurora Serverless automatically scales compute capacity based on demand — ideal for variable/unpredictable workloads"
- exam-domain: 3
- source: exam-1

### Pattern: elasticache-redis-vs-memcached
- trigger: "Redis vs Memcached — which to choose"
- answer: "Redis for persistence/replication/complex types; Memcached for simple multi-threaded caching"
- distractors: ["Redis is always better", "Memcached for persistence", "Both are identical"]
- explanation: "Redis supports snapshots, replication, pub/sub, sorted sets; Memcached is simpler, multi-threaded, no persistence"
- exam-domain: 3
- source: exam-1

### Pattern: nlb-static-ip
- trigger: "static IP address + TCP/UDP load balancing"
- answer: "Network Load Balancer (NLB) with Elastic IP"
- distractors: ["Application Load Balancer (ALB)", "Classic Load Balancer", "Global Accelerator"]
- explanation: "NLB supports Elastic IP per AZ for static IPs and operates at L4 for TCP/UDP traffic"
- exam-domain: 3
- source: cheat-sheet

### Pattern: gwlb-appliance
- trigger: "third-party virtual appliances — firewall, IDS/IPS inline inspection"
- answer: "Gateway Load Balancer (GWLB)"
- distractors: ["Network Load Balancer (NLB)", "Application Load Balancer (ALB)", "AWS Network Firewall"]
- explanation: "GWLB transparently routes traffic through third-party virtual appliances for inline inspection"
- exam-domain: 3
- source: cheat-sheet

### Pattern: placement-cluster
- trigger: "HPC / high-performance cluster — lowest network latency between instances"
- answer: "Cluster placement group"
- distractors: ["Spread placement group", "Partition placement group", "Dedicated Hosts"]
- explanation: "Cluster placement groups pack instances close together in one AZ for lowest latency inter-node communication"
- exam-domain: 3
- source: cheat-sheet

### Pattern: dynamodb-kv
- trigger: "key-value store + flexible schema + single-digit ms latency"
- answer: "Amazon DynamoDB"
- distractors: ["Amazon RDS", "Amazon ElastiCache", "Amazon DocumentDB"]
- explanation: "DynamoDB is a serverless key-value/document database with single-digit millisecond performance at any scale"
- exam-domain: 3
- source: cheat-sheet

### Pattern: neptune-graph
- trigger: "graph data / highly connected relationships / social network"
- answer: "Amazon Neptune"
- distractors: ["Amazon DynamoDB", "Amazon DocumentDB", "Amazon RDS"]
- explanation: "Neptune is a managed graph database optimized for storing and querying highly connected datasets"
- exam-domain: 3
- source: cheat-sheet

### Pattern: timestream-ts
- trigger: "time series data — IoT metrics, application metrics"
- answer: "Amazon Timestream"
- distractors: ["Amazon DynamoDB", "Amazon RDS", "Amazon Redshift"]
- explanation: "Timestream is purpose-built for time series data with automatic tiering from memory to magnetic storage"
- exam-domain: 3
- source: cheat-sheet

### Pattern: qldb-ledger
- trigger: "immutable ledger — cryptographically verifiable transaction log"
- answer: "Amazon Quantum Ledger Database (QLDB)"
- distractors: ["Amazon DynamoDB", "Amazon Aurora", "Amazon Managed Blockchain"]
- explanation: "QLDB provides an immutable, cryptographically verifiable transaction log — not a blockchain, but a centralized ledger"
- exam-domain: 3
- source: cheat-sheet

### Pattern: keyspaces-cassandra
- trigger: "Cassandra migration to AWS"
- answer: "Amazon Keyspaces (for Apache Cassandra)"
- distractors: ["Amazon DynamoDB", "Amazon DocumentDB", "Amazon RDS"]
- explanation: "Keyspaces is a managed Cassandra-compatible service — same CQL API, no cluster management"
- exam-domain: 3
- source: cheat-sheet

### Pattern: documentdb-mongodb
- trigger: "MongoDB migration to AWS / MongoDB-compatible"
- answer: "Amazon DocumentDB"
- distractors: ["Amazon DynamoDB", "Amazon Keyspaces", "Amazon RDS"]
- explanation: "DocumentDB is MongoDB-compatible, supporting MongoDB drivers and tools with managed infrastructure"
- exam-domain: 3
- source: cheat-sheet

### Pattern: fsx-ontap
- trigger: "SMB and NFS file shares — multi-protocol access"
- answer: "Amazon FSx for NetApp ONTAP"
- distractors: ["Amazon FSx for Windows", "Amazon EFS", "Amazon FSx for Lustre"]
- explanation: "FSx ONTAP supports both NFS and SMB protocols simultaneously, ideal for mixed Linux/Windows environments"
- exam-domain: 3
- source: cheat-sheet

### Pattern: fsx-windows
- trigger: "Windows file server — Active Directory integration"
- answer: "Amazon FSx for Windows File Server"
- distractors: ["Amazon EFS", "Amazon FSx for NetApp ONTAP", "Amazon S3"]
- explanation: "FSx for Windows provides fully managed Windows-native file storage with AD integration, SMB protocol, and DFS"
- exam-domain: 3
- source: cheat-sheet

### Pattern: global-accelerator
- trigger: "static anycast IPs + global traffic optimization over AWS backbone"
- answer: "AWS Global Accelerator"
- distractors: ["Amazon CloudFront", "Route 53 latency routing", "NLB with Elastic IP"]
- explanation: "Global Accelerator provides 2 static anycast IPs and routes traffic through AWS global network for consistent performance"
- exam-domain: 3
- source: common

### Pattern: cloudfront-cache
- trigger: "cache static content globally — reduce origin load"
- answer: "Amazon CloudFront"
- distractors: ["AWS Global Accelerator", "ElastiCache", "S3 Cross-Region Replication"]
- explanation: "CloudFront caches content at 400+ edge locations worldwide, reducing latency and origin server load"
- exam-domain: 3
- source: common

### Pattern: efs-shared-storage
- trigger: "shared file storage across multiple EC2 instances — POSIX-compliant"
- answer: "Amazon Elastic File System (EFS)"
- distractors: ["Amazon EBS", "Amazon S3", "Amazon FSx for Lustre"]
- explanation: "EFS provides shared NFS file system accessible from multiple EC2 instances across AZs — EBS is single-instance only"
- exam-domain: 3
- source: common

### Pattern: fsx-lustre-hpc
- trigger: "high-performance parallel file system — ML training / HPC workloads"
- answer: "Amazon FSx for Lustre"
- distractors: ["Amazon EFS", "Amazon FSx for Windows", "Amazon S3"]
- explanation: "FSx for Lustre provides sub-millisecond latency parallel file system integrated with S3 for HPC/ML workloads"
- exam-domain: 3
- source: common

### Pattern: dax-dynamodb
- trigger: "microsecond read latency for DynamoDB — in-memory cache"
- answer: "DynamoDB Accelerator (DAX)"
- distractors: ["ElastiCache Redis", "ElastiCache Memcached", "DynamoDB Global Tables"]
- explanation: "DAX is a DynamoDB-specific in-memory cache providing microsecond read latency with no application changes"
- exam-domain: 3
- source: common

### Pattern: s3-transfer-acceleration
- trigger: "speed up S3 uploads from distant geographic locations"
- answer: "S3 Transfer Acceleration"
- distractors: ["S3 Multipart Upload", "CloudFront with S3 origin", "AWS DataSync"]
- explanation: "Transfer Acceleration uses CloudFront edge locations to speed up uploads over long distances"
- exam-domain: 3
- source: common

### Pattern: redshift-warehouse
- trigger: "petabyte-scale data warehouse — complex analytics queries"
- answer: "Amazon Redshift"
- distractors: ["Amazon Athena", "Amazon RDS", "Amazon DynamoDB"]
- explanation: "Redshift is a columnar data warehouse optimized for complex analytical queries on petabytes of structured data"
- exam-domain: 3
- source: common

---

## Domain 4: Design Cost-Optimized Architectures (20%)

### Pattern: athena-query-s3
- trigger: "query S3 data without loading into a database — serverless SQL"
- answer: "Amazon Athena"
- distractors: ["Amazon Redshift", "Amazon EMR", "AWS Glue"]
- explanation: "Athena runs SQL queries directly on S3 data — serverless, pay-per-query, no infrastructure to manage"
- exam-domain: 4
- source: exam-1

### Pattern: glue-etl-spark
- trigger: "Spark/ETL on AWS — minimal operational overhead / serverless"
- answer: "AWS Glue"
- distractors: ["Amazon EMR", "AWS Lambda", "Amazon Redshift"]
- explanation: "Glue is serverless ETL with Apache Spark — no cluster management, auto-scales, includes schema discovery"
- exam-domain: 4
- source: exam-1

### Pattern: kinesis-streams
- trigger: "real-time streaming — custom processing with multiple consumers"
- answer: "Amazon Kinesis Data Streams"
- distractors: ["Kinesis Data Firehose", "Amazon SQS", "Amazon MSK"]
- explanation: "Kinesis Data Streams provides real-time data streaming with custom consumer applications and replay capability"
- exam-domain: 4
- source: cheat-sheet

### Pattern: kinesis-firehose
- trigger: "near-real-time ETL/delivery to S3, Redshift, or OpenSearch"
- answer: "Amazon Kinesis Data Firehose"
- distractors: ["Kinesis Data Streams", "AWS Glue", "AWS Data Pipeline"]
- explanation: "Firehose is the easiest way to load streaming data — fully managed, auto-scales, delivers to S3/Redshift/OpenSearch"
- exam-domain: 4
- source: cheat-sheet

### Pattern: lake-formation
- trigger: "data lake access control — fine-grained permissions on S3 data"
- answer: "AWS Lake Formation"
- distractors: ["S3 bucket policies", "IAM policies", "AWS Glue Data Catalog"]
- explanation: "Lake Formation provides centralized governance with column/row-level security for data lake data"
- exam-domain: 4
- source: cheat-sheet

### Pattern: spot-instances
- trigger: "fault-tolerant batch jobs — cheapest compute option"
- answer: "EC2 Spot Instances"
- distractors: ["On-Demand Instances", "Reserved Instances", "Savings Plans"]
- explanation: "Spot Instances offer up to 90% discount for interruptible workloads — ideal for batch, data analysis, CI/CD"
- exam-domain: 4
- source: common

### Pattern: reserved-vs-savings
- trigger: "predictable steady-state workload — commit for 1-3 years"
- answer: "Reserved Instances or Savings Plans"
- distractors: ["Spot Instances", "On-Demand Instances", "Dedicated Hosts"]
- explanation: "Both offer up to 72% savings for committed usage; Savings Plans are more flexible across instance families"
- exam-domain: 4
- source: common

### Pattern: s3-lifecycle
- trigger: "automatically move S3 objects to cheaper storage over time"
- answer: "S3 Lifecycle policies"
- distractors: ["S3 Intelligent-Tiering", "S3 Replication rules", "S3 Inventory"]
- explanation: "Lifecycle policies automate transitions between storage classes (e.g., Standard → IA → Glacier) based on age"
- exam-domain: 4
- source: common

### Pattern: s3-intelligent-tiering
- trigger: "unpredictable S3 access patterns — automatic cost optimization"
- answer: "S3 Intelligent-Tiering"
- distractors: ["S3 Lifecycle policies", "S3 Standard", "S3 One Zone-IA"]
- explanation: "Intelligent-Tiering automatically moves objects between access tiers based on usage patterns — no retrieval fees"
- exam-domain: 4
- source: common

### Pattern: lambda-cost
- trigger: "event-driven / short-duration / infrequent execution — cheapest compute"
- answer: "AWS Lambda"
- distractors: ["EC2 Spot Instances", "Fargate", "EC2 On-Demand"]
- explanation: "Lambda charges per invocation and duration — cheapest for sporadic, short workloads with no idle cost"
- exam-domain: 4
- source: common

### Pattern: minimal-ops
- trigger: "minimal operational effort / least operational overhead"
- answer: "Managed/serverless service (Lambda, Fargate, Aurora Serverless, DynamoDB)"
- distractors: ["Self-managed EC2", "ECS on EC2", "RDS on EC2"]
- explanation: "When the exam says 'minimal operational effort', it means choose the most managed/serverless option available"
- exam-domain: 4
- source: cheat-sheet

### Pattern: ebs-gp3-vs-io2
- trigger: "cost-effective SSD storage vs high IOPS requirement"
- answer: "gp3 for general workloads (up to 16K IOPS), io2 Block Express for high IOPS (up to 256K)"
- distractors: ["gp2 for everything", "io1 for all databases", "st1 for all workloads"]
- explanation: "gp3 is cheaper than gp2 with configurable IOPS; io2 is for sustained high IOPS like databases"
- exam-domain: 4
- source: common

### Pattern: storage-gateway
- trigger: "hybrid cloud storage — on-premises access to S3"
- answer: "AWS Storage Gateway"
- distractors: ["AWS DataSync", "AWS Transfer Family", "S3 Cross-Region Replication"]
- explanation: "Storage Gateway provides on-premises applications with access to cloud storage via NFS/SMB/iSCSI protocols"
- exam-domain: 4
- source: common

### Pattern: datasync-transfer
- trigger: "one-time or scheduled data migration to AWS — large dataset transfer"
- answer: "AWS DataSync"
- distractors: ["AWS Storage Gateway", "S3 Transfer Acceleration", "AWS Transfer Family"]
- explanation: "DataSync automates large-scale data transfers between on-premises and AWS with built-in scheduling and verification"
- exam-domain: 4
- source: common

### Pattern: transfer-family
- trigger: "SFTP/FTPS/FTP access to S3 or EFS"
- answer: "AWS Transfer Family"
- distractors: ["AWS DataSync", "AWS Storage Gateway", "S3 presigned URLs"]
- explanation: "Transfer Family provides managed SFTP/FTPS/FTP endpoints backed by S3 or EFS for legacy file transfer workflows"
- exam-domain: 4
- source: common

### Pattern: compute-savings-plan
- trigger: "flexible commitment discount — works across EC2, Fargate, Lambda"
- answer: "Compute Savings Plans"
- distractors: ["EC2 Instance Savings Plans", "Reserved Instances", "Spot Instances"]
- explanation: "Compute Savings Plans apply to EC2, Fargate, and Lambda across any region/family — most flexible commitment"
- exam-domain: 4
- source: common

### Pattern: s3-requester-pays
- trigger: "share large datasets without paying for download costs"
- answer: "S3 Requester Pays"
- distractors: ["S3 Cross-Region Replication", "CloudFront distribution", "S3 presigned URLs"]
- explanation: "Requester Pays shifts download/request costs to the data consumer rather than the bucket owner"
- exam-domain: 4
- source: common

### Pattern: nat-gateway-cost
- trigger: "reduce NAT Gateway costs for private subnet internet access"
- answer: "Use VPC Gateway Endpoints for S3/DynamoDB (free) + consolidate NAT Gateways"
- distractors: ["Use NAT Instance instead", "Use VPN connection", "Use AWS Direct Connect"]
- explanation: "Gateway Endpoints for S3/DynamoDB are free, eliminating NAT Gateway data processing charges for those services"
- exam-domain: 4
- source: common

---

## Cross-Domain Patterns

### Pattern: eventbridge-integration
- trigger: "event-driven automation — react to AWS service state changes"
- answer: "Amazon EventBridge"
- distractors: ["Amazon SNS", "Amazon SQS", "AWS Step Functions"]
- explanation: "EventBridge routes events from AWS services, SaaS apps, and custom sources to targets based on rules"
- exam-domain: 2
- source: common

### Pattern: step-functions-orchestrate
- trigger: "orchestrate multiple Lambda functions / long-running workflow"
- answer: "AWS Step Functions"
- distractors: ["Amazon SQS", "Amazon EventBridge", "AWS Batch"]
- explanation: "Step Functions coordinates multiple services into serverless workflows with visual state machines and error handling"
- exam-domain: 3
- source: common

### Pattern: ecs-fargate-vs-ec2
- trigger: "containers without managing servers"
- answer: "Amazon Elastic Container Service (ECS) with Fargate"
- distractors: ["ECS on EC2", "EKS on EC2", "Self-managed Docker on EC2"]
- explanation: "Fargate is serverless compute for containers — no EC2 instance management, pay per vCPU/memory used"
- exam-domain: 4
- source: common

### Pattern: api-gateway-lambda
- trigger: "serverless REST API — no infrastructure management"
- answer: "Amazon API Gateway + AWS Lambda"
- distractors: ["ALB + EC2", "NLB + Fargate", "CloudFront + EC2"]
- explanation: "API Gateway + Lambda is fully serverless — auto-scales, pay-per-request, no servers to manage"
- exam-domain: 3
- source: common

### Pattern: sns-fanout
- trigger: "one message → multiple subscribers / fan-out pattern"
- answer: "Amazon Simple Notification Service (SNS) fan-out to SQS queues"
- distractors: ["SQS with multiple consumers", "EventBridge", "Kinesis with multiple shards"]
- explanation: "SNS publishes to multiple SQS queues simultaneously — each queue processes the message independently"
- exam-domain: 2
- source: common

### Pattern: vpc-endpoint-gateway
- trigger: "private access to S3/DynamoDB without internet — no NAT Gateway cost"
- answer: "VPC Gateway Endpoint"
- distractors: ["VPC Interface Endpoint", "NAT Gateway", "VPN connection"]
- explanation: "Gateway Endpoints for S3/DynamoDB are free and route traffic within the AWS network without NAT Gateway"
- exam-domain: 1
- source: common

### Pattern: vpc-endpoint-interface
- trigger: "private access to AWS services via private IP in VPC"
- answer: "VPC Interface Endpoint (AWS PrivateLink)"
- distractors: ["VPC Gateway Endpoint", "NAT Gateway", "VPC Peering"]
- explanation: "Interface Endpoints create ENIs in your VPC with private IPs for accessing AWS services privately"
- exam-domain: 1
- source: common

### Pattern: waf-rate-limit
- trigger: "block IP addresses / rate limiting on web application"
- answer: "AWS Web Application Firewall (WAF)"
- distractors: ["Security Groups", "NACLs", "AWS Shield Standard"]
- explanation: "WAF provides IP blocking, rate limiting, and SQL injection/XSS protection at the application layer"
- exam-domain: 1
- source: common
