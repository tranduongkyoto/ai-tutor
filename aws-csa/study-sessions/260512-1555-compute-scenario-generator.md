# Compute — Scenario Generator (Phase 3 Repeat)

Generated: 2026-05-12 15:55 | Domain: compute | Mode: scenario-generator

---

## Scenario 1: Instance Families and Sizing

**Context:** A media company runs a video transcoding pipeline that processes uploaded files into multiple formats. Peak processing involves CPU-intensive FFmpeg operations across thousands of files daily. The workload is predictable during business hours but minimal at night.

**Requirements:** Maximize transcoding throughput, minimize cost, predictable daytime workload.

**Question:** Which Elastic Compute Cloud (EC2) instance strategy best meets these requirements?

A) Use R5.4xlarge Memory Optimized instances with Reserved pricing
B) Use C5.2xlarge Compute Optimized instances with Savings Plans
C) Use M5.xlarge General Purpose instances with On-Demand pricing
D) Use T3.xlarge burstable instances with unlimited mode enabled

**Answer: B**
Video transcoding is CPU-intensive — C-family (Compute Optimized) is purpose-built for batch processing and media transcoding. Savings Plans provide up to 72% discount for the predictable daytime commitment while allowing On-Demand overflow.

**Why others are wrong:**
- A) R5 (Memory Optimized) wastes budget on RAM the workload doesn't need; transcoding is CPU-bound, not memory-bound.
- C) M5 (General Purpose) provides balanced resources but isn't optimized for CPU-heavy workloads; costs more per transcode than C5.
- D) T3 burstable instances are for variable, low-average workloads. Sustained CPU transcoding would burn credits immediately and "unlimited mode" bills at On-Demand rates, negating cost savings.

**Key Concept:** Matching instance family to workload type — C-family for CPU-intensive batch processing.

---

## Scenario 2: GPU / Compute / Memory Optimized Selection

**Context:** A biotech firm is launching a genomics analysis platform. The pipeline has two stages: (1) sequence alignment requiring massive parallel floating-point computation, and (2) variant annotation needing 384 GiB of in-memory reference genome databases.

**Requirements:** Each stage must use the most cost-effective instance type. Data stays within a single Availability Zone (AZ).

**Question:** Which combination of EC2 instance types should a solutions architect recommend?

A) P3 instances for alignment, R5.12xlarge for annotation
B) C5.9xlarge for both alignment and annotation
C) G4dn instances for alignment, X1.16xlarge for annotation
D) M5.24xlarge for both stages to simplify management

**Answer: A**
Sequence alignment is a massively parallel GPU workload — P-family provides the GPU compute. Variant annotation requires a large in-memory dataset (384 GiB) — R5.12xlarge provides 384 GiB RAM at lower cost than X1 or high-memory instances.

**Why others are wrong:**
- B) C5 tops out at 192 GiB RAM; cannot hold the 384 GiB reference genome. Also lacks GPU acceleration for alignment.
- C) G4dn is designed for ML inference and graphics, not the raw floating-point computation needed for alignment. X1 is overprovisioned (up to 1,952 GiB) and far more expensive than R5 for 384 GiB.
- D) M5.24xlarge provides only 384 GiB but has no GPU and is not optimized for either stage — suboptimal for both.

**Key Concept:** Choosing between Accelerated Compute (P/G family), Memory Optimized (R/X family), and Compute Optimized (C family) based on workload characteristics.

---

## Scenario 3: Burstable T-Instances Credit System

**Context:** A startup runs a small internal wiki application accessed by 50 employees. Average CPU usage is under 5%, but occasional document indexing spikes CPU to 40% for 2-3 minutes. The company wants the cheapest possible EC2 setup.

**Requirements:** Lowest cost, handle occasional CPU spikes, no performance degradation during spikes.

**Question:** Which EC2 configuration is most cost-effective?

A) T3.micro with unlimited mode disabled (standard mode)
B) T3.micro with unlimited mode enabled
C) M5.large with On-Demand pricing
D) C5.large with Spot pricing

**Answer: A**
T3 burstable instances are ideal for low-average CPU workloads. At <5% average, credits accumulate faster than they're consumed. Brief 2-3 minute spikes to 40% will use accrued credits without cost — standard mode is sufficient and prevents unexpected overage charges.

**Why others are wrong:**
- B) Unlimited mode would work but adds unnecessary cost risk. With 5% average usage, the instance accumulates enough credits naturally, so unlimited mode's On-Demand overflow billing is wasted insurance.
- C) M5.large is massively overprovisioned for 50 users at 5% CPU — ~4x the cost of T3.micro for no benefit.
- D) C5.large is also overprovisioned. Spot pricing adds interruption risk that's unnecessary for a persistent internal wiki.

**Key Concept:** T-family credit system — low average usage accumulates credits that cover burst periods.

---

## Scenario 4: Spot vs Reserved Decision

**Context:** An analytics company runs two workloads: (1) a production data warehouse query engine running 24/7 for 3 years, and (2) a nightly batch ETL job that can tolerate partial failures and reruns.

**Requirements:** Minimize total cost over 3 years. The batch job can be interrupted without data loss.

**Question:** Which purchasing combination is most cost-effective?

A) On-Demand for both workloads
B) 3-year All Upfront Reserved Instance for the query engine, Spot Instances for the ETL batch job
C) Savings Plan for the query engine, On-Demand for the ETL batch job
D) Spot Instances for both workloads

**Answer: B**
The 24/7 query engine is a steady-state workload — perfect for 3-year All Upfront Reserved (up to 72% discount). The ETL batch job is fault-tolerant and can be interrupted — ideal for Spot Instances (up to 90% discount).

**Why others are wrong:**
- A) On-Demand for both is the most expensive option — no discounts applied to either workload.
- C) Savings Plans would work for the query engine but On-Demand for the ETL job wastes money. Spot at 90% discount crushes On-Demand for interruptible batch work.
- D) Spot for the production query engine is dangerous — 2-minute termination notices would interrupt live user queries and violate availability requirements.

**Key Concept:** Reserved Instances for steady-state, Spot Instances for fault-tolerant batch jobs.

---

## Scenario 5: Savings Plans vs Reserved Instances

**Context:** A SaaS company runs their production API on M5 instances in us-east-1. They plan to migrate some workloads to M6g (Graviton) instances within the next year, and may change from Linux to Amazon Linux 2023. They want a 3-year commitment for maximum savings.

**Requirements:** Lock in savings now while preserving flexibility to change instance size, generation, and OS within the M-family.

**Question:** Which purchasing option provides maximum savings with the required flexibility?

A) Standard Reserved Instances for M5 in us-east-1
B) Convertible Reserved Instances for M5 in us-east-1
C) EC2 Instance Savings Plan for M5 family in us-east-1
D) Compute Savings Plan committed to a $/hour rate

**Answer: C**
EC2 Instance Savings Plans lock to instance family (M-family) + region (us-east-1) but are flexible across instance size, OS, and tenancy. This allows migration from M5 to M6g and OS changes. Discount matches Reserved Instances (up to 72%).

**Why others are wrong:**
- A) Standard RIs lock to specific instance type (M5.xlarge), region, OS, and tenancy. No flexibility for M5→M6g migration or OS change.
- B) Convertible RIs allow changes but cap at 66% discount — less savings than Instance Savings Plans at 72%.
- D) Compute Savings Plans are the most flexible (any family, any region) but provide less discount than Instance Savings Plans. The company doesn't need cross-family or cross-region flexibility.

**Key Concept:** Savings Plans (Instance) vs Reserved Instances vs Convertible RIs — flexibility and discount trade-offs.

---

## Scenario 6: Dedicated Hosts vs Dedicated Instances

**Context:** A financial services company is migrating Oracle Database to AWS. Their Oracle license agreement requires per-core licensing visibility and specific socket counts. Compliance also mandates that no other AWS customer's workloads run on the same physical hardware.

**Requirements:** Per-core/socket visibility for Oracle licensing compliance, dedicated physical hardware isolation.

**Question:** Which EC2 tenancy option meets the Oracle licensing and compliance requirements?

A) Dedicated Instances with per-instance billing
B) Dedicated Hosts with 3-year reservation
C) Default tenancy with License Manager tracking
D) Placement Group Cluster for hardware isolation

**Answer: B**
Dedicated Hosts provide visibility into physical sockets, cores, and host ID — required for per-core/per-socket Oracle licensing (BYOL). 3-year reservation provides cost savings for the long-term commitment.

**Why others are wrong:**
- A) Dedicated Instances provide dedicated hardware but NO visibility into sockets/cores — cannot satisfy per-core Oracle licensing requirements.
- C) Default tenancy shares physical hardware with other customers — violates both the licensing requirement and the hardware isolation compliance mandate.
- D) Placement Groups control instance placement strategy (cluster/spread/partition), not physical hardware dedication. Other customers may share the same host.

**Key Concept:** Dedicated Hosts for BYOL per-core/per-socket licensing; Dedicated Instances for hardware isolation without licensing needs.

---

## Scenario 7: Cluster vs Spread vs Partition Selection

**Context:** A company runs three distinct workloads: (1) a high-frequency trading system requiring sub-millisecond inter-node latency across 12 instances, (2) a primary database and its replica where each must survive independent hardware failures, and (3) an Apache Kafka cluster with 30 brokers needing rack-awareness for partition replication.

**Requirements:** Each workload must use the optimal Placement Group strategy.

**Question:** Which Placement Group configuration correctly addresses all three workloads?

A) Cluster for trading, Spread for database, Partition for Kafka
B) Spread for trading, Cluster for database, Partition for Kafka
C) Partition for all three workloads
D) Cluster for trading and database, Spread for Kafka

**Answer: A**
- Trading: Cluster Placement Group — all instances in same AZ, same rack, 10 Gbps network for lowest latency.
- Database: Spread Placement Group — each instance on separate hardware, max 7 per AZ, hardware failure of one doesn't affect the other.
- Kafka: Partition Placement Group — rack-aware distribution for 30 brokers, up to 7 partitions per AZ, 100s of instances. Kafka partition replication maps to placement partitions.

**Why others are wrong:**
- B) Spread for trading would separate instances across hardware, increasing latency — opposite of what HFT needs. Cluster for database puts both on same rack — a hardware failure takes out both primary and replica.
- C) Partition for the trading system doesn't guarantee instances land on the same rack. Partition for the database is overkill for 2 instances.
- D) Cluster for the database is risky — same rack means single hardware failure loses both. Spread for 30 Kafka brokers violates the 7-per-AZ limit.

**Key Concept:** Cluster = low latency, Spread = max HA (max 7/AZ), Partition = big data rack-awareness (100s of instances).

---

## Scenario 8: Stateful Rules and Cross-SG References

**Context:** A three-tier web application has: a public-facing Application Load Balancer (ALB), an application tier of EC2 instances, and a Relational Database Service (RDS) database. The security team requires that the app tier only accepts traffic from the ALB, and the database only accepts traffic from the app tier — without managing IP addresses.

**Requirements:** No IP-based rules. Automatically handle scaling (new app instances must immediately access the database).

**Question:** How should Security Groups (SGs) be configured?

A) Create three SGs. ALB SG allows inbound 443 from 0.0.0.0/0. App SG allows inbound 8080 from ALB SG. DB SG allows inbound 3306 from App SG.
B) Create one SG for all resources. Allow inbound 443, 8080, and 3306 from 0.0.0.0/0.
C) Create three Network Access Control Lists (NACLs) with deny rules for each tier.
D) Create three SGs with IP-range-based rules updated by a Lambda function when instances scale.

**Answer: A**
Cross-SG references allow traffic based on the source Security Group, not IP addresses. When a new app instance launches with the App SG attached, it automatically gains DB access — no IP management needed. This is the standard three-tier SG pattern.

**Why others are wrong:**
- B) Single SG with 0.0.0.0/0 opens all ports to the internet — massive security violation. No tier isolation.
- C) NACLs are stateless (must manage both inbound AND outbound rules), more complex, and applied at subnet level not instance level. SGs are stateful and instance-level — better fit.
- D) IP-based rules with Lambda updates add unnecessary complexity and latency. Cross-SG references solve this natively without any automation.

**Key Concept:** Security Groups are stateful; cross-SG references eliminate IP management in multi-tier architectures.

---

## Scenario 9: Multi-Homed Instances and ENI Failover

**Context:** A company operates a network appliance (firewall) on EC2 that must sit between a public subnet and a private subnet. If the primary appliance instance fails, traffic must failover to a standby instance within seconds — maintaining the same private IP address that route tables reference.

**Requirements:** Dual-subnet connectivity, sub-second failover preserving the IP that route tables point to, both instances in the same AZ.

**Question:** Which approach enables the fastest failover while maintaining the routing configuration?

A) Assign an Elastic IP to the primary instance and remap it to the standby on failure
B) Attach a secondary Elastic Network Interface (ENI) to the primary instance. On failure, detach it and attach to the standby instance.
C) Use an Application Load Balancer (ALB) between the two instances with health checks
D) Launch both instances in an Auto Scaling Group (ASG) with minimum capacity of 1

**Answer: B**
A secondary ENI carries the private IP that route tables reference. Detaching and re-attaching the ENI to the standby instance (both must be in the same AZ since ENIs are AZ-bound) transfers the IP in seconds — route tables don't need to change.

**Why others are wrong:**
- A) Elastic IP remaps public IP only, not the private IP that internal route tables reference. Internal traffic routing would break during failover.
- C) ALBs operate at Layer 7 — they don't work for transparent network appliance failover that needs to preserve a specific private IP in route tables.
- D) ASG replaces failed instances but creates NEW instances with NEW IPs — route tables would need updating, and launch time is minutes, not seconds.

**Key Concept:** ENIs are AZ-bound; detach/reattach enables IP-preserving failover for network appliances.

---

## Scenario 10: Hibernate Requirements, Limitations, and Use Cases

**Context:** A data science team runs long-running statistical model training on an EC2 instance. Training takes 8 hours, and the team wants to pause the instance overnight (12 hours) and resume the exact computation state in the morning — without restarting the training job from scratch.

**Requirements:** Preserve full RAM state across stop/start cycles. Instance uses 64 GiB RAM. Must work with On-Demand pricing.

**Question:** Which configuration supports EC2 Hibernate for this use case?

A) R5.2xlarge with an unencrypted 200 GiB gp3 root volume
B) R5.2xlarge with an encrypted 200 GiB gp3 root volume
C) I3.2xlarge with instance store root volume, encrypted
D) R5.2xlarge with an encrypted 200 GiB gp3 root volume, hibernated for 3 days over a long weekend

**Answer: B**
Hibernate requires: root volume must be Elastic Block Store (EBS), must be encrypted, RAM < 150 GiB. R5.2xlarge has 64 GiB RAM (within limit), encrypted EBS root, and 12-hour overnight pause is well within the 60-day maximum.

**Why others are wrong:**
- A) Root EBS volume must be **encrypted** for Hibernate — unencrypted volumes are not supported.
- C) Instance Store cannot be a root volume for Hibernate — the RAM state must be written to a **persistent** EBS volume. Instance store data is lost when the instance stops.
- D) While 3 days is within the 60-day limit, this option is a distractor. The configuration is technically valid, but B is the cleaner answer without unnecessary time constraint qualifiers.

**Key Concept:** Hibernate requires encrypted EBS root volume, RAM < 150 GiB, max 60 days.

---

## Scenario 11: ECS EC2 Launch Type vs Fargate

**Context:** A logistics company needs to run two container workloads: (1) a fleet management API handling 1,000 requests/second with steady traffic, where the team wants to fine-tune kernel parameters and use GPU instances for route optimization, and (2) an async notification microservice with unpredictable traffic that spikes during delivery windows.

**Requirements:** Workload 1: kernel-level access, GPU support. Workload 2: minimal operational overhead, auto-scale with demand.

**Question:** Which Elastic Container Service (ECS) launch type configuration best fits each workload?

A) Fargate for both workloads — it handles scaling automatically
B) EC2 Launch Type for fleet management, Fargate for notification service
C) EC2 Launch Type for both — more control and cost efficiency
D) Elastic Kubernetes Service (EKS) with Fargate for both workloads

**Answer: B**
Fleet management needs kernel parameter tuning and GPU instances — only EC2 Launch Type provides host-level access and GPU instance support. The notification service has unpredictable traffic and needs minimal ops — Fargate is serverless, auto-scales by task count, with no infrastructure to manage.

**Why others are wrong:**
- A) Fargate does NOT support GPU instances or kernel-level customization — can't satisfy fleet management requirements.
- C) EC2 Launch Type for the notification service adds unnecessary operational burden (managing EC2 instances, capacity providers, patching) when Fargate handles it automatically.
- D) EKS is for organizations already using Kubernetes. Switching to EKS adds Kubernetes complexity without addressing the GPU/kernel requirement differently than ECS EC2 Launch Type.

**Key Concept:** EC2 Launch Type for host-level access / GPU; Fargate for serverless, auto-scaling with minimal ops.

---

## Scenario 12: ECS Task Role vs Instance Profile

**Context:** An ECS cluster running on EC2 hosts two services: (1) an image processor that reads from Simple Storage Service (S3) and writes to DynamoDB, and (2) a report generator that reads from RDS and sends emails via Simple Email Service (SES). A security audit finds that both services currently share the same Identity and Access Management (IAM) permissions via the EC2 Instance Profile.

**Requirements:** Apply least-privilege access — each service should only access the AWS resources it needs. The Elastic Container Registry (ECR) pull and CloudWatch Logs permissions must remain for all tasks.

**Question:** How should IAM permissions be restructured?

A) Create two EC2 Instance Profiles with different policies, one per EC2 host
B) Keep the Instance Profile for ECR/CloudWatch. Create separate ECS Task Roles — Task Role A (S3 + DynamoDB) for image processor, Task Role B (RDS + SES) for report generator.
C) Use Security Groups to restrict which services can access S3 vs RDS
D) Create a single ECS Task Role with all permissions and assign it to both task definitions

**Answer: B**
ECS Task Roles are defined per task definition, allowing per-service IAM permissions. The Instance Profile stays on the EC2 host for ECS Agent operations (ECR pulls, CloudWatch Logs). Each service gets only the permissions it needs.

**Why others are wrong:**
- A) Instance Profiles attach to EC2 hosts, not containers. If both services run on the same host, they'd share the profile. You'd also need to guarantee service-to-host affinity, which defeats ECS scheduling.
- C) Security Groups control network access (ports/IPs), not IAM API permissions. SGs can't restrict S3 API calls or DynamoDB access.
- D) Single Task Role with all permissions violates least-privilege — the image processor could send emails via SES, and the report generator could write to DynamoDB.

**Key Concept:** Instance Profile = ECS Agent permissions (ECR, CloudWatch). Task Role = per-service application permissions (S3, DynamoDB, etc.).

---

## Scenario 13: EKS vs ECS Decision Criteria

**Context:** A multinational company operates microservices on Kubernetes clusters across Azure and on-premises data centers. They're expanding to AWS and want consistency in their container orchestration tooling, CI/CD pipelines, and monitoring dashboards across all environments.

**Requirements:** Multi-cloud/hybrid Kubernetes compatibility, reuse existing Helm charts and kubectl tooling, minimize retraining for the operations team.

**Question:** Which AWS container service should the solutions architect recommend?

A) Amazon Elastic Container Service (ECS) with Fargate — simpler and AWS-native
B) Amazon Elastic Kubernetes Service (EKS) with Managed Node Groups
C) Amazon ECS with EC2 Launch Type and custom Kubernetes-compatible API wrapper
D) Self-managed Kubernetes on EC2 instances using kops

**Answer: B**
EKS is managed Kubernetes — it uses the same Kubernetes API, Helm charts, kubectl, and monitoring tools the company already uses on Azure and on-premises. Managed Node Groups reduce operational overhead while maintaining Kubernetes compatibility. No team retraining needed.

**Why others are wrong:**
- A) ECS uses a proprietary AWS API — the team's existing Helm charts, kubectl workflows, and Kubernetes-native CI/CD pipelines would all need to be rewritten.
- C) No such thing as a "Kubernetes-compatible API wrapper" for ECS. ECS and Kubernetes are fundamentally different orchestration systems.
- D) Self-managed Kubernetes (kops) works but adds significant operational burden: patching control plane, managing etcd, handling upgrades. EKS abstracts all of this.

**Key Concept:** EKS when already using Kubernetes (multi-cloud, existing tooling). ECS when AWS-native and simpler is preferred.

---

## Scenario 14: Serverless Container Sizing and Cost (Fargate)

**Context:** A SaaS company runs an event-driven document processing pipeline. Each document takes 2 minutes to process, requiring 2 vCPU and 8 GiB memory. Volume averages 500 documents/day but spikes to 5,000 during month-end closing. The current EC2-based setup runs 10 instances 24/7 to handle peak load.

**Requirements:** Eliminate idle capacity costs, auto-scale to handle 10x spikes, pay only for actual processing time.

**Question:** Which solution eliminates idle capacity while handling variable load?

A) EC2 Auto Scaling Group with scale-in to 0 instances during off-peak
B) ECS on Fargate with task-level auto-scaling based on Simple Queue Service (SQS) queue depth
C) ECS on EC2 with Spot Instances for cost savings
D) Lambda functions with 10 GiB memory allocation

**Answer: B**
Fargate charges per vCPU-second and GB-second — zero cost when no tasks run. SQS-based scaling launches tasks proportional to queue depth: 500 tasks/day normally, 5,000 at month-end. Each task runs for 2 minutes then terminates. No idle instances.

**Why others are wrong:**
- A) EC2 ASG cannot scale to 0 — minimum capacity is 1 instance. Even with aggressive scaling, you pay for idle capacity between documents.
- C) EC2 Spot saves on per-instance cost but still runs instances 24/7 or has cold-start delays from scaling. Doesn't eliminate idle capacity — instances sit waiting between documents.
- D) Lambda has a 15-minute timeout (sufficient) but is limited to 10 GiB memory. The task needs 8 GiB which is close to the limit, and Lambda's 6 vCPU max at 10 GiB may not match the 2 vCPU deterministic sizing. Also, Lambda isn't ideal for 2-minute CPU-intensive processing at this volume.

**Key Concept:** Fargate = per-task billing with zero idle cost; SQS integration enables queue-depth-based auto-scaling.
