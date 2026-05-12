# Compute — Scenario Generator (Phase 3)
**Date:** 2026-05-12 12:35 | **Domain:** compute | **Mode:** scenario-generator

## Scenarios Covered

### 1. Genomics Research Batch Processing
- **Concept tested:** Spot Instances + Spot Fleet allocation strategies
- **Answer:** Spot Fleet with priceCapacityOptimized for fault-tolerant batch workloads
- **Key fact:** Spot = up to 90% discount; RI/Savings Plans max 72%

### 2. Multi-Tier Application High Availability
- **Concept tested:** Cluster Placement Group limitations + multi-AZ HA
- **Answer:** Separate Cluster Placement Groups per AZ + ALB + Route 53 failover
- **Key fact:** Cluster Placement Group cannot span AZs

### 3. Container Migration Decision
- **Concept tested:** ECS vs EKS + Fargate + EFS
- **Answer:** ECS Fargate + EFS for serverless shared storage (no K8s needed)
- **Key fact:** S3 cannot be mounted as file system; EFS works with Fargate

### 4. License Compliance Migration
- **Concept tested:** Dedicated Hosts vs Dedicated Instances (BYOL)
- **Answer:** Dedicated Hosts for per-core/per-socket licensing visibility
- **Key fact:** Only Dedicated Hosts expose socket/core info + placement control

### 5. Event-Driven Image Processing Pipeline
- **Concept tested:** S3 → EventBridge → ECS Fargate pattern
- **Answer:** Event-driven Fargate tasks triggered by S3 upload events
- **Key fact:** EventBridge direct trigger is simpler than SQS polling

## Topics Exercised
- purchasing-options (Spot, RI, Savings Plans, Dedicated Hosts)
- placement-groups (Cluster, Spread, Partition)
- ECS, EKS, Fargate, EFS, S3
- ENI, security-groups (indirectly)
- hibernate (not directly tested)
