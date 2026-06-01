# Databases — Scenario Practice (Phase 2)
**Date:** 2026-05-30 11:21
**Score:** 13/14 (93%)

---

### Scenario 1: Multi-AZ vs Read Replicas — ✓ (read-replicas, multi-az)
**Context:** Healthcare patient records on RDS MySQL, high read load + 99.95% uptime SLA.
**Your answer: B** — Correct. Read Replicas (reads) + Multi-AZ (failover) are independent complementary features.

### Scenario 2: Engine Selection — ✓ (rds-custom)
**Context:** Oracle migration needing full OS access + managed benefits.
**Your answer: C** — Correct. RDS Custom for Oracle: full OS/DB admin + managed backups.

### Scenario 3: Aurora vs RDS Decision — ✗ (aurora)
**Context:** Fintech trading platform, 100K TPS, 15 replicas, auto-growing storage.
**Your answer: C** — Incorrect. Correct: B. Aurora PostgreSQL provides all requirements natively. Aurora Serverless is for intermittent workloads, not high-throughput trading.

### Scenario 4: Aurora Serverless Use Cases — ✓ (aurora-serverless)
**Context:** University exam system, used 12 weeks/year, zero traffic otherwise.
**Your answer: C** — Correct. Aurora Serverless scales to zero, pay per ACU-second.

### Scenario 5: Aurora Global Database — ✓ (aurora-global)
**Context:** Streaming company, 200M users across 3 continents, DR RTO < 1 min.
**Your answer: B** — Correct. Aurora Global Database: <1s replication, <1 min DR promotion.

### Scenario 6: Redis vs Memcached — ✓ (elasticache-redis)
**Context:** Gaming leaderboard + session store needs.
**Your answer: B** — Correct. Redis: Sorted Sets + TTL + Multi-AZ + AOF persistence.

### Scenario 7: Caching Strategies — ✓ (elasticache-caching)
**Context:** E-commerce flash sale, 100x read:write ratio, stale pricing concern.
**Your answer: C** — Correct. Write-Through + TTL: fresh data + memory efficiency.

### Scenario 8: Partition Key Design — ✓ (dynamodb-partition-key)
**Context:** Ride-sharing app, query by driver+month and city+date.
**Your answer: A** — Correct. driver_id PK + trip_date SK + GSI(city, trip_date).

### Scenario 9: Capacity Modes — ✓ (dynamodb-capacity, dax)
**Context:** News app, 2K steady reads + unpredictable viral 50K spikes.
**Your answer: D** — Correct. Provisioned 2K RCU + DAX absorbs instant viral spikes.

### Scenario 10: DAX Acceleration — ✓ (dax)
**Context:** Product recommendation engine, hot partition key throttling.
**Your answer: B** — Correct. DAX: microsecond reads, zero code change, reduces RCU.

### Scenario 11: Global Tables — ✓ (dynamodb-global-tables)
**Context:** Multinational e-commerce, active-active read/write in 3 regions.
**Your answer: B** — Correct. DynamoDB Global Tables: active-active, last-writer-wins.

### Scenario 12: RDS Proxy — ✓ (rds-proxy)
**Context:** 500 Lambda functions exhausting Aurora connection limit + IAM auth requirement.
**Your answer: B** — Correct. RDS Proxy: connection pooling + IAM auth + 66% faster failover.

### Scenario 13: DocumentDB vs DynamoDB — ✓ (documentdb)
**Context:** MongoDB migration with nested JSON, aggregation pipelines.
**Your answer: B** — Correct. DocumentDB: MongoDB-compatible API, minimal code changes.

### Scenario 14: Specialty Databases — ✓ (neptune, timestream, qldb, keyspaces)
**Context:** Fraud (graph), IoT (time-series), audit (immutable), device registry (Cassandra).
**Your answer: C** — Correct. Neptune + Timestream + QLDB + Keyspaces.

---

## Summary
- **Score:** 13/14 (93%)
- **Missed topics:** aurora (confused Aurora Serverless with standard Aurora for high-throughput)
- **Strong areas:** rds-custom, aurora-global, aurora-serverless, elasticache-redis, caching-strategies, dynamodb (partition key, capacity, DAX, global tables), rds-proxy, documentdb, specialty-databases
- **Key lessons:**
  - Aurora Serverless = intermittent/unpredictable workloads (scales to zero). Standard Aurora = high-throughput with fixed replicas and auto-growing storage.
