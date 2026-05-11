# Compute — Concept Mapper (Repeat)

## Service Overview

| Service | Description | Primary Use Case |
|---------|-------------|-----------------|
| Amazon EC2 | IaaS virtual machines with full OS-level control | General-purpose workloads, web servers, databases |
| Amazon ECS | AWS-native container orchestration for Docker | Microservices, containerized apps (AWS-first teams) |
| Amazon EKS | Managed Kubernetes on AWS | Teams already using Kubernetes on-prem/other cloud |
| AWS Fargate | Serverless compute engine for ECS/EKS | Containers without infrastructure management |
| Amazon ECR | Docker image registry (private + public) | Store/manage container images |
| AWS App Runner | Fully managed deployment from source/container | Rapid web app/API deployment |
| AWS App2Container | CLI tool to migrate Java/.NET apps to Docker | Lift-and-shift legacy apps |

## Real-World Use Cases

- Startup with unpredictable traffic → EC2 On-Demand + ASG + ALB
- Nightly batch jobs → Spot Instances (90% discount)
- Kubernetes migration from on-prem → EKS with Managed Node Groups
- Per-core licensing compliance → Dedicated Hosts
- Serverless containers → ECS + Fargate + EFS
- Event-driven S3 processing → EventBridge → ECS Fargate Task
- Legacy Java app containerization → App2Container → ECR → ECS/EKS

## Service Integrations

- EC2 ↔ EBS, EFS, ALB/NLB, ASG, ENI
- ECS ↔ ECR, ALB/NLB, EFS, CloudWatch, EventBridge, SQS, Fargate
- EKS ↔ EBS/EFS/FSx (via CSI driver), CloudWatch Container Insights, Fargate

## Architectural Patterns

- HA: Spread Placement Group + ENI failover + ECS Fargate + EFS
- Cost: Spot Fleet (priceCapacityOptimized) + RI for steady-state + Savings Plans
- Event-driven: S3 → EventBridge → Fargate → DynamoDB
- Microservices: ECS + ALB + ECR + per-task IAM roles

## Purchasing Options

| Option | Discount | Commitment | Best For |
|--------|----------|------------|----------|
| On-Demand | 0% | None | Short-term, unpredictable |
| Reserved Instance | up to 72% | 1 or 3 yr | Steady-state |
| Convertible RI | up to 66% | 1 or 3 yr | Flexible steady-state |
| Savings Plan | up to 72% | 1 or 3 yr | Family + region locked |
| Spot Instance | up to 90% | None | Batch, fault-tolerant |
| Dedicated Host | Per-host | On-Demand/Reserved | BYOL, compliance |
| Capacity Reservation | 0% | None | Guaranteed AZ capacity |

## Key Numbers

- Elastic IP limit: 5/account
- Spread PG: max 7 instances/AZ
- Partition PG: max 7 partitions/AZ, 100s instances
- Hibernate: RAM < 150 GB, max 60 days, encrypted EBS root
- Spot termination grace: 2 minutes

## Exam Keyword Signals

- "BYOL" → Dedicated Host
- "serverless containers" → Fargate
- "Kubernetes on-prem" → EKS
- "store Docker images" → ECR
- "low latency between instances" → Cluster PG
- "HA, isolated failures" → Spread PG
- "Hadoop/Kafka/Cassandra" → Partition PG
- "timeout connecting" → Security Group issue
- "connection refused" → Application error

## Key Takeaways

1. EC2 is the foundation — know all 7 purchasing options
2. Fargate = "serverless" answer for least operational overhead
3. EKS only when Kubernetes already in use
4. Placement Groups: Cluster (perf), Spread (HA), Partition (big data)
5. Security Groups = allow-only; timeout = SG, connection refused = app
6. Spot = cheapest but interruptible; never for critical workloads
7. ECS Task Role vs Instance Profile — exam favorite distinction
