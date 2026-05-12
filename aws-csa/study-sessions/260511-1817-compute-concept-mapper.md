# Compute — Concept Mapper (Repeat)
**Date:** 2026-05-11 18:17
**Domain:** compute
**Mode:** concept-mapper (Phase 1 repeat)

## Topics Covered
- EC2 (instance types, security groups, purchasing options, placement groups, ENI, hibernate)
- ECS (EC2 launch type, Fargate, task roles, auto scaling, integration patterns)
- EKS (managed node groups, Fargate, CSI drivers)
- ECR (image storage, IAM access control)
- App Runner (fully managed deployment)
- App2Container (Java/.NET migration)

## Key Concepts Reviewed
- 7 EC2 purchasing options with discount tiers and use cases
- 3 placement group strategies (Cluster/Spread/Partition)
- ECS vs EKS decision criteria
- Task Role vs Instance Profile distinction
- Security Group behavior (allow-only, timeout vs connection refused)
- Hibernate requirements (encrypted EBS, <150GB RAM, 60 days max)
- Event-driven container patterns (EventBridge, SQS, Schedule)
- Cost optimization patterns (Spot Fleet, RI, Savings Plans)

## Exam Signals
- BYOL/compliance → Dedicated Host
- Steady-state → Reserved Instance
- Fault-tolerant batch → Spot Instance
- Serverless containers → Fargate
- Kubernetes migration → EKS
- Low latency → Cluster Placement Group
