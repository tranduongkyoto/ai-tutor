# Databases — Mini Exam: Comprehensive Final (Phase 4)
**Date:** 2026-05-31 11:31
**Score:** 10/10 (100%)
**Scope:** comprehensive — full domain exam with cross-domain integration

---

## Questions & Results

### Q1 ✓ — Aurora Database Cloning (aurora-cloning)
**Question:** Fast QA copy of production Aurora, ready in minutes, only 5% data modified, minimize storage costs.
A) Snapshot → restore B) Aurora Cloning (copy-on-write) C) Read Replica → promote D) DMS replication
**Your answer: B** — Correct. Copy-on-write shares storage, pays only for changed pages.

### Q2 ✓ — Aurora Custom Endpoints (aurora-custom-endpoints)
**Question:** Isolate BI queries on db.r5.4xlarge from OLTP on db.r5.xlarge within same Aurora cluster.
A) Reader Endpoint B) Custom Endpoint targeting large instances C) Separate Read Replicas outside cluster D) Auto Scaling with more small instances
**Your answer: B** — Correct. Custom Endpoints route specific query types to specific instance sizes.

### Q3 ✓ — Athena for serverless S3 queries (storage:athena)
**Question:** Ad-hoc SQL on S3, sporadic, no infrastructure.
A) Redshift + Spectrum B) Athena (serverless SQL on S3) C) Glue ETL → Aurora D) EMR + Hive
**Your answer: B** — Correct. Athena: serverless, standard SQL, pay-per-query, no infrastructure.

### Q4 ✓ — DynamoDB capacity + DAX for viral spikes (dynamodb-capacity, dax)
**Question:** Steady 10K reads, viral spikes to 200K, auto-scaling too slow, keep costs low.
A) On-demand mode B) Provision 200K permanently C) Provisioned 10K + DAX cache D) Adaptive capacity
**Your answer: C** — Correct. DAX absorbs viral reads from cache; provisioned handles steady baseline cheaply.

### Q5 ✓ — RDS Proxy + Lambda (rds-proxy, serverless:lambda)
**Question:** API GW + Lambda + Aurora, Lambda cold starts + TLS overhead causing timeouts.
A) Migrate to DynamoDB B) RDS Proxy (warm connection pool) C) Increase Lambda timeout D) Lambda in VPC + IAM Auth
**Your answer: B** — Correct. RDS Proxy maintains warm pre-established connections, eliminating TLS/auth overhead.

### Q6 ✓ — Aurora HA + Global (aurora-ha, aurora-global) [multi-select]
**Question:** Which TWO statements about Aurora are TRUE? (Select TWO)
A) Aurora backups can be disabled B) 6 copies across 3 AZs (4 writes, 3 reads) C) Read Replicas use SYNC D) Global DB: 10 regions, <1s lag
**Your answer: B, D** — Correct. 6 copies/3 AZs + Global DB with 10 secondary regions.

### Q7 ✓ — VPC Gateway Endpoint for DynamoDB (networking:vpc-endpoints)
**Question:** Aurora in private subnet + Lambda needs DynamoDB access without internet.
A) Private subnet + SGs + Gateway Endpoint for DynamoDB B) Public subnet + NAT C) Interface Endpoint for DynamoDB D) DynamoDB Security Group
**Your answer: A** — Correct. Gateway Endpoint: free, VPC-internal, supports S3 and DynamoDB.

### Q8 ✓ — Neptune for graph traversal (neptune)
**Question:** Social media: mutual friends, 3 degrees of separation, billions of relationships.
A) DynamoDB + GSIs B) Aurora + recursive CTEs C) Neptune (graph DB) D) OpenSearch nested docs
**Your answer: C** — Correct. Neptune: purpose-built graph DB for relationship traversal at scale.

### Q9 ✓ — Monitoring stack (monitoring-audit:cloudwatch-cloudtrail-guardduty)
**Question:** RDS audit trail + slow query alerts + unauthorized access detection.
A) CloudWatch + CloudTrail + GuardDuty B) CloudTrail only C) CloudWatch + Config + Inspector D) Performance Insights + CloudTrail + Macie
**Your answer: A** — Correct. Each service covers one requirement: monitoring, audit, threat detection.

### Q10 ✓ — Keyspaces for Cassandra migration (keyspaces)
**Question:** On-prem Cassandra → AWS, CQL queries, managed serverless, 3x AZ replication.
A) DynamoDB + CQL layer B) Keyspaces (managed Cassandra) C) DocumentDB D) Aurora + JSONB
**Your answer: B** — Correct. Keyspaces: managed Cassandra-compatible, CQL native, serverless.

---

## Summary
- **Score:** 10/10 (100%)
- **Missed topics:** none
- **Strong areas:** ALL — aurora-cloning, aurora-custom-endpoints, dynamodb-capacity+dax, rds-proxy, aurora-ha, aurora-global, neptune, keyspaces, athena, monitoring stack, vpc-endpoints
- **Key lessons:** All Phase 3 weak topics mastered (aurora-cloning, custom-endpoints, dynamodb-capacity).
