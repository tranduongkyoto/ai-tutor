# Databases — Mini Exam: Design (Phase 3)
**Date:** 2026-05-31 11:01
**Score:** 7/10 (70%)
**Scope:** design — architecture design decisions and trade-offs

---

## Questions & Results

### Q1 ✗ — DynamoDB capacity for extreme variance (dynamodb-capacity)
**Question:** Logistics company, 500K shipment updates/sec peak, 5K off-season, key-value, minimize cost without manual intervention.
A) Aurora Serverless PostgreSQL with JSON columns B) DynamoDB provisioned + auto-scaling (5K-500K WCU) C) DynamoDB on-demand capacity mode D) ElastiCache Redis cluster mode
**Your answer: B** — Incorrect. Correct: C. On-demand handles 100x variance instantly; auto-scaling has lag time causing throttling during rapid spikes.

### Q2 ✓ — Aurora Machine Learning (aurora-ml)
**Question:** Pharmaceutical company needs fraud detection via ML in Aurora MySQL without building data pipelines.
A) Glue export → S3 → SageMaker batch B) Aurora ML → SageMaker from SQL directly C) DynamoDB Streams → Lambda → SageMaker D) Aurora events → Lambda → SageMaker
**Your answer: B** — Correct. Aurora ML calls SageMaker/Comprehend directly from SQL — predictions inline with query results.

### Q3 ✓ — Babelfish migration strategy (babelfish)
**Question:** SQL Server migration with T-SQL, need cost savings + fallback for unsupported features.
A) RDS for SQL Server (full compat) B) Aurora + Babelfish primary, RDS Custom fallback C) DynamoDB rewrite D) Aurora MySQL + T-SQL conversion
**Your answer: B** — Correct. Babelfish for cost savings + RDS Custom fallback for edge cases.

### Q4 ✗ — Aurora Database Cloning (aurora-cloning)
**Question:** Create staging environment from production Aurora, available in minutes, minimize storage costs.
A) Promote Read Replica B) Snapshot → restore to new cluster C) Aurora Cloning (copy-on-write) D) DMS continuous replication
**Your answer: B** — Incorrect. Correct: C. Aurora Cloning uses copy-on-write — shares storage, fast, pay only for changed pages.

### Q5 ✓ — RDS Proxy with ECS Fargate (rds-proxy, compute:ecs-fargate)
**Question:** ECS Fargate tasks exhausting Aurora connection limit + IAM auth + faster failover.
A) Switch to EC2 launch type B) RDS Proxy (IAM + pooling + failover) C) Increase max_connections + PgBouncer D) Migrate to DynamoDB
**Your answer: B** — Correct. RDS Proxy: connection pooling + IAM auth + 66% faster failover.

### Q6 ✓ — KMS key migration for Aurora (rds-encryption, security-identity:kms)
**Question:** Change Aurora encryption from AWS-managed key to CMK for compliance.
A) Modify cluster KMS key in-place B) Snapshot → copy with CMK → restore C) Enable rotation on AWS-managed key D) New cluster + DMS
**Your answer: B** — Correct. Aurora encryption is immutable after creation; snapshot → copy with new key → restore.

### Q7 ✗ — Aurora Custom Endpoints (aurora-custom-endpoints)
**Question:** Isolate analytical workloads from OLTP on same Aurora cluster.
A) Read Replicas + Reader Endpoint B) Custom Endpoints → larger instances for analytics C) Migrate analytics to Redshift D) Aurora Serverless for analytics
**Your answer: A** — Incorrect. Correct: B. Custom Endpoints route specific query types to specific instance sizes; Reader Endpoint distributes equally across all replicas.

### Q8 ✓ — DynamoDB Streams + SNS-SQS fan-out (dynamodb-streams, integration-messaging:sns-sqs-fanout)
**Question:** Order in DynamoDB triggers 3 independent downstream systems with failure isolation.
A) Single Lambda calling all 3 sequentially B) DynamoDB Streams → Lambda → SNS → 3 SQS queues C) App writes to DynamoDB + 3 SQS simultaneously D) DynamoDB Streams → EventBridge → 3 Lambda targets
**Your answer: B** — Correct. SNS-SQS fan-out: each consumer has own queue, independent processing, failure isolation.

### Q9 ✓ — Database type matching (documentdb, neptune) [multi-select]
**Question:** Which TWO pairings correctly match data model to AWS database? (Select TWO)
A) Product catalog (JSON) → DocumentDB B) Session tokens (TTL) → Aurora + deletion jobs C) Supply chain (graph) → Neptune D) Financial reporting (SQL joins) → DynamoDB + GSI
**Your answer: A, C** — Correct. DocumentDB for JSON documents; Neptune for graph traversal.

### Q10 ✓ — DynamoDB Streams for real-time events (dynamodb-streams)
**Question:** Real-time push notifications when user pauses a show (watch history in DynamoDB).
A) On-demand backups → S3 → scheduled Lambda B) DynamoDB Streams → Lambda C) Global Tables → Lambda per region D) EventBridge polling every minute
**Your answer: B** — Correct. DynamoDB Streams captures item-level changes in real-time, triggers Lambda directly.

---

## Summary
- **Score:** 7/10 (70%)
- **Missed topics:** dynamodb-capacity (on-demand for extreme variance), aurora-cloning (copy-on-write for staging), aurora-custom-endpoints (workload isolation)
- **Strong areas:** aurora-ml, babelfish, rds-proxy, rds-encryption, dynamodb-streams, documentdb, neptune, sns-sqs-fanout
- **Key lessons:**
  - DynamoDB on-demand > provisioned+auto-scaling for 100x traffic variance — auto-scaling lags, causes throttling
  - Aurora Cloning (copy-on-write) > snapshot+restore for staging — shares storage, faster, cheaper
  - Aurora Custom Endpoints > Reader Endpoint for workload isolation — routes specific query types to specific instance sizes
