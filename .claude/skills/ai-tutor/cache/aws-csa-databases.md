# Databases - AWS CSA Content Cache

## Services & Concepts

### Amazon RDS (Relational Database Service)
- Managed SQL database service; supports Postgres, MySQL, MariaDB, Oracle, Microsoft SQL Server, IBM DB2, Aurora
- Managed: automated provisioning, OS patching, continuous backups (PITR), monitoring dashboards, maintenance windows
- Storage backed by EBS; supports vertical and horizontal scaling
- Cannot SSH into RDS instances (managed by AWS)
- **Use case**: Store relational datasets (RDBMS/OLTP), SQL queries, transactions

**RDS Storage Auto Scaling**
- Automatically scales storage when free storage < 10% of allocated
- Low-storage condition must last at least 5 minutes AND 6 hours must have passed since last modification
- Must set a Maximum Storage Threshold (upper limit)
- Supports all RDS database engines

**RDS Read Replicas**
- Up to 15 read replicas; within AZ, cross-AZ, or cross-region
- Replication is ASYNC → reads are eventually consistent
- Read replicas serve SELECT statements only (not INSERT, UPDATE, DELETE)
- Applications must update connection string to use read replicas
- Replicas can be promoted to standalone DB
- Network cost: same-region cross-AZ replication is FREE; cross-region replication incurs data transfer costs

**RDS Multi-AZ (Disaster Recovery)**
- SYNC replication to standby instance in different AZ
- One DNS name → automatic failover (no app changes needed)
- NOT used for read scaling; standby is only for failover
- Read Replicas can themselves be configured as Multi-AZ
- Converting single-AZ to Multi-AZ: zero-downtime (click modify → snapshot taken → restored in new AZ → sync established)

**RDS Backups**
- Automated: daily full backup + transaction logs every 5 minutes → restore to any point from oldest backup to 5 min ago
- Retention: 1–35 days; set to 0 to disable automated backups
- Manual snapshots: user-triggered, retained indefinitely
- Trick: stopped RDS still charges for storage — snapshot & restore instead if stopping long-term

**RDS Custom**
- For Oracle and Microsoft SQL Server only
- Full admin access to underlying OS and database
- Can SSH or use SSM Session Manager to access EC2 instance
- Must de-activate Automation Mode before customizing; take snapshot first
- RDS = AWS manages everything; RDS Custom = you manage OS/DB

**RDS Proxy**
- Fully managed, serverless, autoscaling, multi-AZ database proxy
- Pools and shares DB connections → reduces CPU/RAM stress, minimizes open connections
- Reduces RDS & Aurora failover time by up to 66%
- Supports RDS (MySQL, PostgreSQL, MariaDB, MS SQL Server) and Aurora (MySQL, PostgreSQL)
- Enforces IAM authentication; stores credentials in Secrets Manager
- RDS Proxy is NEVER publicly accessible — must be accessed from within VPC
- Key use case: Lambda functions opening many DB connections

**RDS & Aurora Security**
- At-rest encryption: KMS for master and replicas — must be defined at launch time
- If master is not encrypted, read replicas CANNOT be encrypted
- To encrypt an unencrypted DB: take snapshot → restore as encrypted
- In-flight: TLS-ready by default (AWS TLS root certificates)
- IAM Authentication: use IAM roles instead of username/password
- No SSH except on RDS Custom
- Audit logs can be sent to CloudWatch Logs for longer retention

---

### Amazon Aurora
- AWS proprietary technology (not open source); PostgreSQL and MySQL compatible
- 5x performance over MySQL on RDS; 3x performance of PostgreSQL on RDS
- Costs ~20% more than RDS but more efficient
- Failover is instantaneous; HA native
- Storage auto-grows in increments of 10 GB, up to 256 TB
- Up to 15 read replicas; replica lag < 10 ms

**Aurora High Availability**
- 6 copies of data across 3 AZs automatically
- 4 out of 6 copies needed for writes; 3 out of 6 for reads
- Self-healing with peer-to-peer replication; storage striped across 100s of volumes
- Automated failover for master in < 30 seconds
- Shared storage volume: replication + self-healing + auto-expanding

**Aurora DB Cluster Endpoints**
- Writer Endpoint: always points to master
- Reader Endpoint: connection load balancing across all read replicas
- Custom Endpoints: define subset of Aurora instances (e.g., larger instances for analytical queries); Reader Endpoint generally not used once custom endpoints defined

**Aurora Replicas Auto Scaling**
- Triggered by CPU usage on reader instances
- Extends Reader Endpoint automatically as new replicas are added

**Aurora Serverless**
- Automated instantiation and auto-scaling based on actual usage
- Good for infrequent, intermittent, or unpredictable workloads
- No capacity planning needed; pay per second
- Uses a Proxy Fleet (managed by Aurora) between client and Aurora instances

**Aurora Global Database (recommended for global)**
- 1 Primary Region (read/write)
- Up to 10 secondary (read-only) regions; replication lag < 1 second
- Up to 16 read replicas per secondary region
- Promoting a secondary region for DR: RTO < 1 minute

**Aurora Cross-Region Read Replicas**
- Useful for DR; simpler than Global Database but higher replication lag

**Aurora Backups**
- Automated: 1–35 days; CANNOT be disabled (unlike RDS)
- Manual snapshots: user-triggered, retained indefinitely
- Restore from S3 (MySQL): use Percona XtraBackup → store on S3 → restore to new Aurora cluster

**Aurora Database Cloning**
- Creates new Aurora DB Cluster from existing one using copy-on-write protocol
- Initially shares same data volume (fast, no data copying needed)
- Additional storage allocated only when clone data diverges
- Faster than snapshot & restore; great for staging from production

**Aurora Machine Learning**
- Add ML predictions via SQL using SageMaker (any ML model) or Comprehend (sentiment analysis)
- Use cases: fraud detection, ads targeting, sentiment analysis, product recommendations

**Babelfish for Aurora PostgreSQL**
- Allows Aurora PostgreSQL to understand T-SQL (MS SQL Server commands)
- MS SQL Server apps can migrate to Aurora PostgreSQL with little/no code changes
- Same client drivers (SQL Server) work with Aurora PostgreSQL

**Aurora Summary Use Case**: Same as RDS but less maintenance, more flexibility, more performance, more features

---

### Amazon ElastiCache
- Managed Redis or Memcached in-memory data store; sub-millisecond latency
- Select instance type (e.g., cache.m6g.large)
- **IMPORTANT**: Using ElastiCache requires heavy application code changes
- Use case: key/value store, frequent reads/less writes, cache DB query results, session data for websites

**ElastiCache - Redis vs Memcached**

| Feature | Redis | Memcached |
|---|---|---|
| Multi-AZ | Yes, with Auto-Failover | No |
| Read Replicas | Yes (HA scaling) | No |
| Data Durability | AOF persistence | Non-persistent |
| Backup & Restore | Yes | Yes (Serverless) |
| Data Structures | Sets, Sorted Sets | Basic |
| Architecture | Replication | Multi-node sharding |

**ElastiCache Security**
- IAM Authentication supported for Redis
- IAM policies on ElastiCache = AWS API-level security only
- Redis AUTH: password/token set at cluster creation (extra layer on top of security groups); supports SSL in-flight
- Memcached: SASL-based authentication

**ElastiCache Caching Patterns**
- **Lazy Loading**: read data cached; cache miss → read from DB → write to cache; data can become stale
- **Write Through**: update cache when DB is written; no stale data
- **Session Store**: store temporary session data using TTL features

**ElastiCache Redis Use Case — Gaming Leaderboards**
- Redis Sorted Sets: guarantee uniqueness and element ordering
- Each new element ranked in real-time and inserted in correct order

---

### Amazon DynamoDB
- AWS proprietary, managed serverless NoSQL database; millisecond latency
- Highly Available, Multi-AZ by default; reads and writes are decoupled
- Transaction capability
- Capacity modes: provisioned (with optional auto-scaling) or on-demand
- Great for rapidly evolving schemas
- Can replace ElastiCache as key/value store (TTL feature for session data)
- Security/auth/authorization through IAM only
- Use case: serverless app development (small documents, 100s KB), distributed serverless cache

**DynamoDB Accelerator (DAX)**
- In-memory cache for DynamoDB; microsecond read latency
- Fully managed, HA, seamless integration (no app code change)

**DynamoDB Streams**
- Ordered stream of item-level changes in a table
- Integrate with AWS Lambda or Kinesis Data Streams

**DynamoDB Global Tables**
- Active-active setup across multiple regions
- Must enable DynamoDB Streams first

**DynamoDB Backups**
- Automated PITR: up to 35 days (restore creates new table)
- On-demand backups: retained until explicitly deleted
- Export to S3 without using RCU (within PITR window)
- Import from S3 without using WCU

---

### Amazon DocumentDB
- AWS implementation of MongoDB (NoSQL document database)
- Used to store, query, and index JSON data
- Similar deployment concepts as Aurora
- Fully managed, highly available; replication across 3 AZs
- Storage automatically grows in increments of 10 GB
- Scales to millions of requests per second

---

### Amazon Neptune
- Fully managed graph database
- Highly available across 3 AZs; up to 15 read replicas
- Can store billions of relations and query with millisecond latency
- Use cases: knowledge graphs (Wikipedia), fraud detection, recommendation engines, social networking

**Neptune Streams**
- Real-time ordered sequence of every change to graph data; no duplicates, strict order
- Changes available immediately after writing
- Accessible via HTTP REST API
- Use cases: send notifications on graph changes, sync graph to other stores (S3, OpenSearch, ElastiCache), replicate across regions

---

### Amazon Keyspaces (for Apache Cassandra)
- Managed Apache Cassandra-compatible database service
- Serverless, scalable, fully managed, highly available
- Tables replicated 3 times across multiple AZs
- Uses Cassandra Query Language (CQL)
- Single-digit millisecond latency at any scale; 1000s of requests per second
- Capacity: on-demand mode or provisioned with auto-scaling
- PITR up to 35 days
- Use cases: IoT device info, time-series data

---

### Amazon Timestream
- Fully managed, fast, scalable, serverless time series database
- Store and analyze trillions of events per day
- 1000x faster and 1/10th the cost of relational databases for time-series data
- Data storage tiering: recent data in memory, historical in cost-optimized storage
- Built-in time series analytics functions (near real-time pattern detection)
- SQL-compatible; scheduled queries, multi-measure records
- Encryption in transit and at rest
- Use cases: IoT apps, operational applications, real-time analytics

---

### Amazon S3 (as a database type)
- Key/value store for objects; serverless, scales infinitely
- Max object size: 50 TB; versioning capability
- Great for big objects; not optimized for many small objects
- Use cases: static files, key/value store for big files, website hosting
- Tiers: Standard, Infrequent Access, Intelligent, Glacier + lifecycle policies

---

## Key Configurations

**RDS Storage Auto Scaling Triggers (all 3 must be true)**:
1. Free storage < 10% of allocated storage
2. Low-storage condition lasts ≥ 5 minutes
3. ≥ 6 hours since last storage modification

**RDS Backup Retention**:
- Automated: 1–35 days (0 = disabled)
- Manual snapshots: indefinite

**Aurora Backup Retention**:
- Automated: 1–35 days (CANNOT set to 0 — always enabled)
- Manual snapshots: indefinite

**Aurora Storage Growth**:
- Starts at 10 GB, grows in 10 GB increments up to 256 TB

**RDS Read Replica Network Cost**:
- Same region (any AZ): FREE
- Cross-region: incurs data transfer costs

**RDS Multi-AZ**:
- SYNC replication; standby NOT used for reads
- One DNS name; automatic failover; no app changes required

**Aurora Global Database**:
- Replication lag < 1 second to secondary regions
- Up to 10 secondary regions
- Up to 16 read replicas per secondary region
- DR promotion RTO < 1 minute

---

## Architectural Patterns

**ElastiCache DB Cache Pattern**:
- App queries ElastiCache first → cache hit: return data; cache miss: read from RDS → write to ElastiCache
- Cache must have invalidation strategy to ensure data freshness

**ElastiCache User Session Store Pattern**:
- User logs in → app writes session to ElastiCache → subsequent requests to any app instance retrieve session from ElastiCache → user stays logged in (stateless app)

**RDS Proxy + Lambda Pattern**:
- Lambda functions create many short-lived DB connections → RDS Proxy pools connections → reduces DB load
- Lambda → RDS Proxy (in VPC private subnet) → RDS DB instance

**Aurora Serverless Pattern**:
- Client → Proxy Fleet (managed by Aurora) → Aurora instances (auto-scale up/down based on demand)

**Aurora Custom Endpoints Pattern**:
- Separate large instances for analytical queries from smaller instances for OLTP
- Custom Endpoint → db.r5.2xlarge instances; Reader Endpoint → db.r3.large instances

**Timestream Architecture**:
- Ingestion: AWS IoT / Kinesis Data Streams / Prometheus / Telegraf / MSK → Lambda or Kinesis Data Analytics (Apache Flink) → Amazon Timestream
- Consumption: QuickSight / SageMaker / Grafana / JDBC connections

**Neptune Streams Pattern**:
- Neptune Cluster → Neptune Streams → HTTP GET (Streams API) → Reader Application (Lambda/EC2) → S3 / OpenSearch / ElastiCache

---

## Important Numbers & Limits

| Service | Metric | Value |
|---|---|---|
| RDS | Max read replicas | 15 |
| RDS | Backup retention max | 35 days |
| RDS | Transaction log backup frequency | Every 5 minutes |
| RDS | Restore granularity | Any point from oldest backup to 5 min ago |
| RDS Proxy | Failover time reduction | Up to 66% |
| Aurora | Max storage | 256 TB |
| Aurora | Storage increment | 10 GB |
| Aurora | Read replicas | Up to 15 |
| Aurora | Replica lag | Sub 10 ms |
| Aurora | Failover time | < 30 seconds |
| Aurora | Performance vs MySQL RDS | 5x |
| Aurora | Performance vs PostgreSQL RDS | 3x |
| Aurora | Cost vs RDS | ~20% more |
| Aurora Global | Secondary regions | Up to 10 |
| Aurora Global | Read replicas per secondary | Up to 16 |
| Aurora Global | Replication lag | < 1 second |
| Aurora Global | DR promotion RTO | < 1 minute |
| DynamoDB | PITR retention | Up to 35 days |
| DocumentDB | Storage increment | 10 GB |
| Keyspaces | PITR retention | Up to 35 days |
| Keyspaces | Replication | 3x across multiple AZs |
| Neptune | Read replicas | Up to 15 |
| Neptune | Relation storage | Billions of relations |
| S3 | Max object size | 50 TB |
| Timestream | Cost vs relational DB | 1/10th |
| Timestream | Speed vs relational DB | 1000x faster |

---

## Diagram Descriptions

**RDS Read Replicas Diagram**:
- Master DB (M) in center; async replication arrows to Read Replica (R) instances left and right
- Application sits above; write arrows go down to master, read arrows go up from replicas
- Shows 1 master + 2 read replicas pattern

**RDS Read Replica Network Cost Diagram**:
- Left panel: same region (us-east-1a master → us-east-1b replica) = FREE (green label)
- Right panel: cross-region (us-east-1a master → eu-west-1b replica) = $$$ (red label)
- Both use ASYNC replication

**RDS Multi-AZ Diagram**:
- Application → single DNS name → Master (AZ A) with SYNC replication → Standby (AZ B)
- Application writes/reads only from master; standby is passive

**RDS Single-AZ to Multi-AZ Migration Diagram**:
- Master (M) takes snapshot → snapshot stored → restored in new AZ as Standby (S) → SYNC replication established
- Zero downtime operation

**Aurora DB Cluster Diagram**:
- Client → Writer Endpoint (green box, points to master M) for writes
- Client → Reader Endpoint (orange box, connection load balancing) across multiple R instances with Auto Scaling
- Shared storage volume at bottom: auto-expanding from 10 GB to 256 TB

**Aurora Replicas Auto Scaling Diagram**:
- Writer Endpoint → Master; Reader Endpoint extended to cover new replicas as CPU usage rises on existing readers
- Endpoint Extended label shows automatic expansion

**Aurora Custom Endpoints Diagram**:
- Client → Writer Endpoint (master), Reader Endpoint (db.r3.large instances), Custom Endpoint (db.r5.2xlarge instances)
- Different instance types serve different query workloads

**Aurora Serverless Diagram**:
- Client → Proxy Fleet (managed by Aurora) → multiple Aurora instances on shared storage volume
- Proxy fleet manages connection routing as instances scale

**Aurora Global Database Diagram**:
- Primary region (us-east-1): Aurora cluster with Read/Write applications
- Secondary region (eu-west-1): Aurora cluster replica with Read-Only applications
- Replication arrow from primary to secondary (< 1 second lag)

**Aurora Machine Learning Diagram**:
- Application → SQL query to Aurora → Aurora sends data to SageMaker/Comprehend → predictions returned to Aurora → query results returned to application

**ElastiCache DB Cache Architecture Diagram**:
- Application → cache hit (green arrow from ElastiCache back to app) OR cache miss (orange arrow to ElastiCache then to RDS) → read from RDS → write to cache
- Shows lazy loading pattern

**ElastiCache User Session Store Diagram**:
- User → App Instance 1 → writes session to ElastiCache
- User → App Instance 2 → retrieves session from ElastiCache (already logged in)
- User → App Instance 3 → same session retrieval

**Neptune Graph Database Diagram**:
- Social graph showing two users (people icons) connected by "Friends" relationship
- Surrounding nodes (computers, mobile) connected via: Use, Like, Connect, Play, Check in, Read relationships
- Illustrates highly connected dataset pattern

**Neptune Streams Architecture Diagram**:
- Neptune Cluster (receives writes) → Neptune Streams → HTTP GET via Streams API → Streams Reader Application (Lambda + other services) → fans out to S3, OpenSearch, ElastiCache

**Timestream Architecture Diagram**:
- Left (ingestion): AWS IoT, Kinesis Data Streams, Prometheus, Telegraf → Lambda; Kinesis Data Streams + MSK → Kinesis Data Analytics for Apache Flink → Amazon Timestream
- Right (consumption): Amazon Timestream → QuickSight, SageMaker, Grafana, JDBC connections

**RDS Proxy Architecture Diagram**:
- VPC boundary: Lambda functions (many) → IAM Authentication check → RDS Proxy (in private subnet) → RDS DB instance
- Shows connection pooling and IAM enforcement

**Babelfish for Aurora PostgreSQL Diagram**:
- Left: App using SQL Server Client Driver → T-SQL → Babelfish layer inside Aurora PostgreSQL
- Right: App using PostgreSQL Driver → PL/pgSQL → PostgreSQL layer inside Aurora PostgreSQL
- Bottom: MS SQL Server → (migrate via AWS SCT+DMS) → Aurora PostgreSQL

---

## Exam-Relevant Details

### RDS vs Aurora vs DynamoDB — When to Use Which
- **RDS**: Standard relational workloads (OLTP), need SQL, specific engine (Oracle, SQL Server), moderate scale
- **Aurora**: Same as RDS but need higher performance, HA, global distribution, less maintenance overhead, MySQL/PostgreSQL compatible
- **DynamoDB**: Serverless, NoSQL, millisecond latency, unpredictable scale, simple key/value or JSON, no joins needed

### Read Replica vs Multi-AZ — Critical Distinction
- **Read Replica**: ASYNC replication; used for READ SCALING; can be cross-region; costs cross-region network fees
- **Multi-AZ**: SYNC replication; used for DISASTER RECOVERY only; standby is NOT readable; no cross-region; free for same-region

### ElastiCache Redis vs Memcached — Key Exam Points
- Need persistence/backups/HA/failover → **Redis**
- Need simple horizontal scaling/sharding, multi-threaded → **Memcached**
- Need sorted sets (leaderboards) → **Redis** (Sorted Sets)
- Memcached: NO replication, NO persistence, NO HA

### Common Exam Traps
- "Multi-AZ is for scaling reads" → FALSE; it's for DR/HA only; standby is not readable
- "ElastiCache requires no code changes" → FALSE; requires heavy application code changes
- "Aurora backup can be disabled" → FALSE; Aurora automated backups CANNOT be disabled (unlike RDS which allows setting to 0)
- "RDS Read Replicas cross-AZ same region is free" → TRUE (no cross-AZ fee for read replicas in same region)
- "RDS Custom allows SSH" → TRUE (unlike standard RDS which does NOT allow SSH)
- "RDS Proxy is publicly accessible" → FALSE; never publicly accessible, VPC only
- "DynamoDB security uses Security Groups" → FALSE; DynamoDB uses IAM only
- "To encrypt existing unencrypted RDS DB" → take snapshot → restore as encrypted (cannot encrypt in-place)

### Service-to-Use-Case Keywords
- "Social network / graph relationships / fraud detection" → **Neptune**
- "MongoDB compatible / JSON documents" → **DocumentDB**
- "Apache Cassandra / CQL / IoT time-series" → **Keyspaces**
- "Time-series / IoT metrics / operational data" → **Timestream**
- "Gaming leaderboard / real-time ranking" → **ElastiCache Redis** (Sorted Sets)
- "Session data / stateless applications" → **ElastiCache** or **DynamoDB** (TTL)
- "Migrate SQL Server to Aurora" → **Babelfish for Aurora PostgreSQL**
- "Lambda + database connection exhaustion" → **RDS Proxy**
- "Unpredictable/intermittent DB workload" → **Aurora Serverless**
- "Global low-latency reads, < 1 second replication" → **Aurora Global Database**
- "Staging database from production without impact" → **Aurora Database Cloning**
- "Free text search / unstructured search" → **OpenSearch** (not a DB type but search)
- "OLAP / BI / data warehouse" → **Redshift** (not covered in this section)

### Database Type Classification
- **RDBMS (SQL/OLTP)**: RDS, Aurora
- **NoSQL**: DynamoDB (JSON/key-value), ElastiCache (key-value), Neptune (graphs), DocumentDB (MongoDB/JSON), Keyspaces (Cassandra)
- **Object Store**: S3 (big objects), Glacier (backups/archives)
- **Data Warehouse (OLAP)**: Redshift, Athena, EMR
- **Search**: OpenSearch
- **Graph**: Neptune
- **Ledger**: Amazon QLDB (Quantum Ledger Database)
- **Time Series**: Timestream

### Choosing the Right Database — Key Questions
- Read-heavy vs write-heavy vs balanced? Throughput needs? Scale requirements?
- How much data, how long stored, object size, access patterns?
- Data durability requirements? Source of truth?
- Latency requirements? Concurrent users?
- Data model? Joins needed? Structured vs semi-structured?
- Strong schema vs flexibility? Reporting? Search? RDBMS vs NoSQL?
- License costs? Consider Cloud Native (Aurora) to avoid Oracle/SQL Server licensing
