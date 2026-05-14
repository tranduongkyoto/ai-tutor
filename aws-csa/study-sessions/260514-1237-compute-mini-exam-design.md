# Compute — Mini Exam: Design (Phase 5)
**Date:** 2026-05-14 12:37
**Score:** 8/10 (80%)
**Scope:** design — architecture design decisions and trade-offs

---

## Questions & Results

### Q1 ✓ — ECS Cluster Capacity Provider (elastic-container-service)
**Question:** A company runs a microservices architecture on ECS with EC2 launch type. During peak hours, new tasks fail to start because the cluster has insufficient EC2 capacity, even though ECS Service Auto Scaling has successfully increased the desired task count. What should the solutions architect implement?

A) Increase the maximum capacity of the ECS Service Auto Scaling policy
B) Configure an ECS Cluster Capacity Provider paired with the Auto Scaling Group (ASG) ✓
C) Switch all services to Fargate launch type to eliminate capacity constraints
D) Add larger EC2 instance types to the cluster manually

**Your answer: B** — Correct. ECS Cluster Capacity Provider is paired 1:1 with an ASG and automatically provisions new EC2 instances when the cluster lacks CPU/RAM capacity.

---

### Q2 ✓ — Spot Fleet for batch GPU (purchasing-options)
**Question:** A media company needs to process uploaded videos in batch. Processing is fault-tolerant, can be interrupted, and must complete within 24 hours. Minimize costs. Requires GPU instances.

A) On-Demand GPU instances in a Placement Group Cluster
B) Reserved GPU instances with a 1-year All Upfront commitment
C) Spot Fleet with GPU instances using the priceCapacityOptimized allocation strategy ✓
D) Dedicated Hosts with GPU instances

**Your answer: C** — Correct. Spot instances offer up to 90% discount. priceCapacityOptimized balances cost and availability.

---

### Q3 ✓ — Cluster PG + standby for HA (placement-groups)
**Question:** Financial services trading platform requiring ultra-low latency AND high availability across AZs.

A) Placement Group Cluster in a single AZ with a standby cluster in another AZ ✓
B) Placement Group Spread across three AZs
C) Placement Group Partition across two AZs
D) Individual instances with Enhanced Networking across AZs

**Your answer: A** — Correct. Cluster PG provides 10 Gbps inter-instance bandwidth. Standby cluster in another AZ provides HA.

---

### Q4 ✓ — Event-driven serverless containers (elastic-container-service)
**Question:** Event-driven image processing from S3, must be serverless and scale to zero. (Select TWO)

A) ECS with Fargate launch type ✓
B) ECS with EC2 launch type and Cluster Capacity Provider
C) EventBridge triggers ECS Fargate tasks on S3 events ✓
D) SQS queue + ECS Service Auto Scaling

**Your answer: A, C** — Correct. Fargate scales to zero + EventBridge triggers individual tasks per S3 event.

---

### Q5 ✗ — Dedicated Hosts vs Instances cost optimization (purchasing-options)
**Question:** Multi-tenant SaaS needing hardware isolation for compliance AND socket/core visibility for Oracle BYOL. Standard tenants can share hardware.

A) Dedicated Instances for all enterprise, On-Demand for standard
B) Dedicated Hosts (Oracle licensing) + Dedicated Instances (compliance-only) + On-Demand ✓
C) Dedicated Hosts for all enterprise, Reserved for standard
D) Capacity Reservations for enterprise, Savings Plans for standard

**Your answer: C** — Incorrect. Using Dedicated Hosts for ALL enterprise tenants is unnecessarily expensive. Only those needing socket/core visibility (BYOL licensing) need Dedicated Hosts. Compliance-only tenants can use cheaper Dedicated Instances.

---

### Q6 ✗ — App Runner fastest path (elastic-container-service)
**Question:** Startup with no Kubernetes experience, fastest path to production, needs auto scaling/LB/HTTPS and VPC access to RDS.

A) ECS Fargate + ALB
B) EKS with Managed Node Groups
C) AWS App Runner ✓
D) EC2 with Docker + ALB

**Your answer: A** — Incorrect. App Runner is designed for teams with no infra experience — auto-builds, deploys, scales, load balances, encrypts with zero config. ECS Fargate + ALB works but requires more setup. Signal: "no infrastructure experience" + "fastest path" → App Runner.

---

### Q7 ✓ — EC2 Hibernate for RAM preservation (hibernate)
**Question:** Real-time analytics app takes 8 min to load data into RAM. Stopped nightly for maintenance. Minimize restart time.

A) EC2 User Data to pre-load data
B) EC2 Hibernate to preserve in-memory state ✓
C) Custom AMI with pre-loaded data
D) Cluster Placement Group

**Your answer: B** — Correct. Hibernate saves RAM state to encrypted root EBS. User Data runs only at first boot. AMI doesn't preserve runtime memory.

---

### Q8 ✓ — EKS for Kubernetes migration (elastic-kubernetes-service)
**Question:** Migrating 200+ microservices from on-prem Kubernetes with Helm charts and kubectl scripts. Minimize migration effort, maintain cloud portability.

A) ECS Fargate
B) EKS with Managed Node Groups ✓
C) App Runner with ECR images
D) ECS with EC2 launch type

**Your answer: B** — Correct. EKS is managed Kubernetes — existing Helm/kubectl work directly. Kubernetes is cloud-agnostic for portability.

---

### Q9 ✓ — Partition PG for Cassandra (placement-groups)
**Question:** 50-node Apache Cassandra cluster, need rack-failure isolation and partition-aware replication. (Select TWO)

A) Placement Group Partition ✓
B) Placement Group Spread
C) Read partition metadata via EC2 metadata service ✓
D) Placement Group Cluster

**Your answer: A, C** — Correct. Partition PG supports 100s of instances with rack isolation. Instances access partition metadata for rack-aware replication. Spread limited to 7/AZ.

---

### Q10 ✓ — ENI failover for private IP (elastic-network-interface)
**Question:** Critical database on EC2, standby in same AZ must take over private IP within seconds. Also needs separate management interface.

A) Elastic IP reassignment
B) Secondary ENI with database IP, move on failure ✓
C) Spread Placement Group with auto IP failover
D) Same private IP via User Data

**Your answer: B** — Correct. ENIs carry private IPs and can be moved between instances in the same AZ. Also supports dual-homing for management interface.

---

## Summary
- **Score:** 8/10 (80%)
- **Missed topics:** purchasing-options (Dedicated Hosts vs Instances), elastic-container-service (App Runner)
- **Strong areas:** placement-groups, hibernate, ENI, EKS, ECS architecture patterns
- **Key lessons:**
  - Dedicated Hosts = BYOL licensing + compliance; Dedicated Instances = compliance only (cheaper)
  - "No infrastructure experience" + "fastest path" → App Runner, not ECS Fargate
