# Databases — Learn and Test (Phase 1) [PARTIAL]
**Date:** 2026-05-29 18:02
**Score:** 5/5 (100%) — Sections 1-2 complete, Section 3+ pending
**Status:** Partial — session interrupted after Section 2

---

## Section 1: Service Overview

### Amazon Relational Database Service (RDS)
Managed SQL database supporting PostgreSQL, MySQL, MariaDB, Oracle, Microsoft SQL Server, IBM DB2, and Aurora. AWS handles provisioning, OS patching, continuous backups (PITR), and monitoring.

| Feature | Detail |
|---------|--------|
| Storage | Backed by Elastic Block Store (EBS) |
| Scaling | Vertical (instance resize) + horizontal (read replicas) |
| SSH access | **Not allowed** (managed service) — except RDS Custom |
| Use case | Relational datasets, Online Transaction Processing (OLTP), SQL queries |

**RDS Custom** — available for Oracle and Microsoft SQL Server only. Full OS/DB admin access (SSH or SSM Session Manager). Must deactivate Automation Mode before customizing.

### Amazon Aurora
AWS proprietary; PostgreSQL and MySQL compatible.
- 5x MySQL on RDS performance; 3x PostgreSQL on RDS
- Storage auto-grows: 10 GB increments → up to 256 TB
- Up to 15 read replicas with sub-10 ms lag
- 6 copies of data across 3 AZs automatically
- Failover in < 30 seconds
- Costs ~20% more than standard RDS

### Amazon ElastiCache
Managed in-memory data store — Redis or Memcached. Sub-millisecond latency.

| | Redis | Memcached |
|---|---|---|
| Multi-AZ + failover | Yes | No |
| Read replicas | Yes | No |
| Persistence | AOF | None |
| Data structures | Sets, Sorted Sets | Basic key-value |

**Important:** Requires heavy application code changes.

### Amazon DynamoDB
Serverless NoSQL — millisecond latency, Multi-AZ by default. Uses IAM only for security. Capacity: provisioned (with auto-scaling) or on-demand.

### Specialty Databases
| Service | Type | Trigger Keyword |
|---------|------|----------------|
| DocumentDB | MongoDB-compatible document DB | "JSON documents", "MongoDB" |
| Neptune | Graph database | "social network", "fraud detection" |
| Keyspaces | Cassandra-compatible | "CQL", "Cassandra", "IoT device info" |
| Timestream | Time-series DB | "IoT metrics", "time-series analytics" |
| QLDB | Ledger/immutable | "immutable journal", "financial ledger" |

### Quiz: Section 1
**Q1** ✓ — rds-custom
Oracle DB with full OS access + managed benefits → which service?
A) RDS for Oracle with Multi-AZ B) RDS Custom for Oracle C) Oracle on EC2 D) Aurora with Oracle compatibility
💡 Hint: Which RDS variant gives managed benefits while allowing OS access?
**Your answer: B** — Correct. RDS Custom for Oracle gives full OS/DB admin access with managed backups.

**Q2** ✓ — dynamodb
Mobile gaming app, JSON documents, unpredictable traffic (100-10K req/s), zero capacity planning → which DB?
A) Aurora Serverless B) RDS MySQL Auto Scaling C) DynamoDB on-demand D) ElastiCache Redis cluster
💡 Hint: Serverless, handles JSON/key-value natively, auto-scales based on traffic.
**Your answer: C** — Correct. DynamoDB on-demand scales instantly with zero capacity planning for JSON/key-value workloads.

**Q3** ✓ — elasticache
Which statement about ElastiCache is TRUE?
A) Memcached supports Multi-AZ + persistence B) No app code changes needed C) Redis Sorted Sets for leaderboards D) Redis has no auth beyond SGs
💡 Hint: Which engine supports sorted sets and rankings?
**Your answer: C** — Correct. Redis Sorted Sets guarantee uniqueness and automatic ordering for real-time leaderboards.

---

## Section 2: Real-World Use Cases

### When to Use Which Database
- SQL + joins + transactions + highest perf → Aurora
- SQL + specific engine (Oracle, SQL Server) → RDS
- Key-value / JSON + serverless → DynamoDB
- Graph relationships → Neptune
- MongoDB-compatible → DocumentDB
- Cassandra-compatible → Keyspaces
- Time-series → Timestream
- In-memory cache / sessions → ElastiCache

### Real-World Scenarios
1. E-commerce: Aurora (catalog/orders) + DynamoDB/ElastiCache (sessions) + OpenSearch (search)
2. Social Media: Aurora (profiles) + Neptune (connections) + ElastiCache (feed cache)
3. IoT: DynamoDB (device state) + Timestream (metrics) + Neptune (device relationships)
4. Financial: Aurora (transactions) + QLDB (audit trail) + Neptune (fraud detection)
5. Migration: Oracle → RDS Custom; SQL Server → Babelfish; MongoDB → DocumentDB; Cassandra → Keyspaces

### Quiz: Section 2
**Q1** ✓ — rds-custom
Healthcare EHR Oracle migration, need custom patches + OS scripts + minimal app changes → which target?
A) Aurora PostgreSQL + Babelfish B) RDS for Oracle (standard) C) RDS Custom for Oracle D) DynamoDB with DMS
💡 Hint: "Oracle" + "custom OS patches" + "minimal app changes"
**Your answer: C** — Correct. RDS Custom for Oracle keeps Oracle engine with full OS access.

**Q2** ✓ — elasticache
Real-time leaderboard, millions of players, instant ranking → which solution?
A) DynamoDB with GSI B) Aurora PostgreSQL ORDER BY C) ElastiCache Redis Sorted Sets D) Memcached custom ranking
💡 Hint: In-memory data structure guaranteeing uniqueness + automatic ordering.
**Your answer: C** — Correct. Redis Sorted Sets purpose-built for real-time rankings.

---

## Section 3: Service Integrations [INCOMPLETE]
Session interrupted. Key patterns covered in teaching:
- ElastiCache + RDS (caching layer with Lazy Loading / Write Through)
- RDS Proxy + Lambda (connection pooling, up to 66% faster failover)
- DynamoDB Accelerator (DAX) — microsecond reads, no code change
- DynamoDB Streams + Lambda (event-driven, required for Global Tables)
- Aurora Machine Learning (SageMaker/Comprehend via SQL)
- Neptune Streams → fan-out to S3/OpenSearch/ElastiCache
- Timestream ingestion (IoT → Kinesis → Timestream → QuickSight)

Quiz not completed for this section.

---

## Summary
- **Score:** 5/5 (100%) — Sections 1-2 only
- **Missed topics:** none
- **Strong areas:** rds-custom, dynamodb, elasticache
- **Status:** Resume from Section 3 quiz onwards
