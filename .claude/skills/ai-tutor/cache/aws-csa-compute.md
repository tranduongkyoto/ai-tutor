# Compute - AWS CSA Content Cache

## Services & Concepts

### Amazon EC2 (Elastic Compute Cloud)
- IaaS — rent virtual machines, store data on EBS, distribute load via ELB, scale via ASG
- Config options: OS (Linux/Windows/macOS), CPU, RAM, storage (EBS/EFS/Instance Store), network card, security group, User Data script
- **EC2 User Data**: bootstrap script run ONLY ONCE at first start, runs as root user; used for installs, updates, file downloads

### EC2 Instance Types
Naming convention: `m5.2xlarge` → m=class, 5=generation, 2xlarge=size

| Family | Use Cases | Example Types |
|---|---|---|
| General Purpose | Web servers, code repos; balanced compute/memory/network | Mac, T4g, T3, T3a, T2, M6g, M5, M5a, M4, A1 |
| Compute Optimized | Batch processing, media transcoding, HPC, ML, gaming servers | C6g, C6gn, C5, C5a, C5n, C4 |
| Memory Optimized | In-memory DBs, BI, real-time big data processing, distributed cache | R6g, R5, R5a, R5b, R5n, R4, X1e, X1, High Memory, z1d |
| Storage Optimized | OLTP, NoSQL/relational DBs, Redis cache, data warehousing, distributed file systems | I3, I3en, D2, D3, D3en, H1 |
| Accelerated Computing | GPU workloads | P-family, G-family |

Example specs:
- t2.micro: 1 vCPU, 1 GiB RAM, EBS-Only, Low-to-Moderate network
- r5.16xlarge: 64 vCPU, 512 GiB RAM, EBS-Only, 20 Gbps network, 13,600 Mbps EBS BW
- m5.8xlarge: 32 vCPU, 128 GiB RAM, EBS-Only, 10 Gbps network, 6,800 Mbps EBS BW

### Security Groups
- Fundamental of network security in AWS; act as firewall on EC2 instances
- Contain **allow rules only** (no deny rules); reference by IP or by security group
- Regulate: port access, authorized IP ranges (IPv4/IPv6), inbound/outbound traffic
- **Defaults**: all inbound blocked, all outbound authorized
- Locked down to a region/VPC combination
- Lives "outside" EC2 — blocked traffic never reaches the instance
- One SG can be attached to multiple instances
- Timeout error → SG issue; "Connection refused" → application error
- Best practice: maintain a separate SG for SSH access

Classic ports: 22=SSH/SFTP, 21=FTP, 80=HTTP, 443=HTTPS, 3389=RDP (Windows)

### Elastic IPs
- Fixed public IPv4 address that you own until deleted
- Attach to one instance at a time; can remap to mask instance failure
- Limit: **5 Elastic IPs per account** (can request increase)
- Best practice: avoid Elastic IPs — use DNS name or Load Balancer instead

### EC2 Instance Networking
- By default, EC2 gets: private IP (internal AWS network) + public IP (internet)
- Public IP **changes** when instance is stopped and started
- SSH into EC2: must use public IP (private IP only works from within same network)

### Elastic Network Interfaces (ENI)
- Logical component in a VPC representing a virtual network card
- Attributes: primary private IPv4, one or more secondary IPv4, one Elastic IP per private IPv4, one public IPv4, one or more SGs, MAC address
- Can create ENIs independently and attach/move them between EC2 instances for failover
- **Bound to a specific AZ** — cannot move across AZs

### EC2 Placement Groups
Three strategies:
- **Cluster**: all instances in single AZ on same rack; 10 Gbps network between instances; high risk (AZ fails = all fail); use for Big Data / low-latency / high-throughput
- **Spread**: instances across different hardware, max **7 instances per AZ per group**; spans multiple AZs; use for critical apps requiring HA
- **Partition**: up to **7 partitions per AZ**, spans multiple AZs, scales to **100s of instances**; each partition = separate rack; partition failure doesn't affect others; instances get partition metadata; use for HDFS, HBase, Cassandra, Kafka

### EC2 Hibernate
- Preserves in-memory (RAM) state; much faster boot (OS not restarted)
- RAM state written to encrypted root EBS volume
- Requirements: root volume must be EBS, encrypted, not instance store
- Supported families: C3, C4, C5, I3, M3, M4, R3, R4, T2, T3, …
- RAM limit: **less than 150 GB**
- Not supported for bare metal instances
- Available for On-Demand, Reserved, and Spot instances
- **Maximum hibernate duration: 60 days**
- AMI support: Amazon Linux 2, Linux AMI, Ubuntu, RHEL, CentOS, Windows

### EC2 Instance Connect
- Browser-based SSH; AWS uploads temporary key to instance
- Works out-of-the-box only with **Amazon Linux 2**
- Port 22 must still be open in security group

---

## EC2 Purchasing Options

### On-Demand
- Pay per second (Linux/Windows); per hour (all other OS)
- Highest cost, no upfront, no commitment
- Use for: short-term, unpredictable workloads

### Reserved Instances
- Up to **72% discount** vs On-Demand; 1 or 3 year terms
- Reserve: Instance Type, Region, Tenancy, OS
- Payment: No Upfront (+), Partial Upfront (++), All Upfront (+++)
- Scope: Regional or Zonal (reserves AZ capacity)
- Can buy/sell in Reserved Instance Marketplace
- **Convertible RI**: can change instance type/family/OS/scope/tenancy; up to **66% discount**
- Use for: steady-state workloads (databases)

### EC2 Savings Plans
- Up to **72% discount**; commit to $/hour for 1 or 3 years
- Locked to instance family + region (e.g., M5 in us-east-1)
- Flexible across: instance size, OS, tenancy
- Usage beyond commitment billed at On-Demand price

### Spot Instances
- Up to **90% discount** — most cost-efficient in AWS
- Can lose instance when spot price exceeds your max price
- **2-minute grace period** before termination when outbid
- Use for: batch jobs, data analysis, image processing, distributed workloads, flexible start/end
- Not suitable for: critical jobs, databases
- Spot Request types: one-time or persistent
- To terminate: must first cancel Spot Request (open/active/disabled), then terminate instances
- Cancelling request does NOT terminate running instances

### Spot Fleets
- Set of Spot Instances + optional On-Demand instances
- Define launch pools (instance type, OS, AZ); fleet picks from pools
- Allocation strategies:
  - **lowestPrice**: cost optimization, short workloads
  - **diversified**: spread across pools, best availability for long workloads
  - **capacityOptimized**: pool with best capacity for count needed
  - **priceCapacityOptimized** (recommended): highest capacity first, then lowest price

### Dedicated Hosts
- Physical server fully dedicated to your use
- Addresses compliance requirements, BYOL (per-socket/per-core/per-VM licensing)
- Purchase: On-Demand (per second) or Reserved (1 or 3 years)
- Most expensive option
- Visibility of sockets, cores, host ID; affinity between host and instance

### Dedicated Instances
- Instances on hardware dedicated to you; may share with other instances in same account
- No control over instance placement
- Per-instance billing (+ $2/region fee)

### Capacity Reservations
- Reserve On-Demand capacity in specific AZ for any duration
- No time commitment; no billing discounts
- Charged at On-Demand rate whether or not instances run
- Combine with Regional RIs or Savings Plans for discounts
- Use for: short-term, uninterrupted workloads in a specific AZ

---

## Containers on AWS

### Docker
- Apps packaged in containers; run identically on any OS/machine
- Use cases: microservices, lift-and-shift on-premises apps to AWS
- Images stored in Docker Repositories: Docker Hub (public) or Amazon ECR (private + public gallery)
- Docker vs VMs: containers share host OS via Docker Daemon (no Guest OS per container); more lightweight, many containers per server

### Amazon ECR (Elastic Container Registry)
- Store and manage Docker images on AWS
- Supports private and public repositories (Public Gallery: gallery.ecr.aws)
- Fully integrated with ECS; backed by S3
- Access controlled via IAM (permission errors = check IAM policy)
- Features: vulnerability scanning, versioning, image tags, lifecycle policies

### Amazon ECS (Elastic Container Service)
- Launch Docker containers = launch ECS Tasks on ECS Clusters
- **EC2 Launch Type**: you provision and maintain EC2 instances; each instance runs ECS Agent to register in cluster; AWS manages start/stop of containers
- **Fargate Launch Type**: serverless — no EC2 instances to manage; define task definitions (CPU/RAM); AWS runs tasks; scale by increasing task count

**ECS IAM Roles:**
- **EC2 Instance Profile** (EC2 launch type only): used by ECS agent; makes API calls to ECS, ECR, CloudWatch Logs, Secrets Manager/SSM Parameter Store
- **ECS Task Role**: each task gets specific role; defined in task definition; allows tasks to access different AWS services (e.g., Task A → S3, Task B → DynamoDB)

**ECS Load Balancer Integration:**
- ALB: supported, works for most use cases
- NLB: recommended for high throughput or with AWS PrivateLink
- Classic LB: supported but not recommended (no Fargate support)

**ECS Data Volumes (EFS):**
- Mount EFS onto ECS tasks; works for both EC2 and Fargate launch types
- Tasks in any AZ share same data; Fargate + EFS = fully serverless
- S3 cannot be mounted as a file system

**ECS Service Auto Scaling:**
- Uses AWS Application Auto Scaling; scales ECS task count
- Metrics: ECS Service Average CPU, Average Memory, ALB Request Count Per Target
- Policies: Target Tracking, Step Scaling, Scheduled Scaling
- ECS Service Auto Scaling (task level) ≠ EC2 Auto Scaling (instance level)
- Fargate auto scaling is simpler (serverless)

**EC2 Launch Type — Auto Scaling EC2 Instances:**
- Auto Scaling Group: scale ASG based on CPU Utilization
- ECS Cluster Capacity Provider: paired with ASG; adds EC2 instances when missing capacity (CPU, RAM)

**ECS Integration Patterns:**
- EventBridge: trigger ECS tasks on S3 upload events (event-driven batch processing)
- EventBridge Schedule: run tasks on schedule (e.g., every 1 hour for batch processing to S3)
- SQS Queue: ECS service polls SQS; auto scales based on queue depth
- Intercept stopped tasks: EventBridge captures ECS Task State Change → SNS → admin notification

### Amazon EKS (Elastic Kubernetes Service)
- Managed Kubernetes clusters on AWS; alternative to ECS with different API
- Kubernetes is open-source, cloud-agnostic (Azure, GCP, AWS)
- Supports EC2 worker nodes or Fargate for serverless containers
- Use case: companies already using Kubernetes on-prem or another cloud
- One EKS cluster per region for multi-region setups
- Logs and metrics via CloudWatch Container Insights

**EKS Node Types:**
- **Managed Node Groups**: AWS creates/manages nodes (EC2); nodes in ASG managed by EKS; supports On-Demand or Spot
- **Self-Managed Nodes**: you create and register to cluster; managed by ASG; can use prebuilt Amazon EKS Optimized AMI; supports On-Demand or Spot
- **AWS Fargate**: no maintenance, no nodes managed

**EKS Data Volumes:**
- Requires StorageClass manifest + CSI (Container Storage Interface) driver
- Supports: Amazon EBS, Amazon EFS (works with Fargate), Amazon FSx for Lustre, Amazon FSx for NetApp ONTAP

### AWS App Runner
- Fully managed service for web apps and APIs at scale; no infrastructure experience required
- Input: source code or container image
- Auto builds, deploys, scales, load balances, encrypts
- VPC access support; can connect to databases, caches, message queues
- Use cases: web apps, APIs, microservices, rapid production deployments

### AWS App2Container (A2C)
- CLI tool for migrating Java and .NET web apps into Docker containers
- Lift-and-shift from on-premises bare metal, VMs, or any cloud
- Workflow: Discover & Analyze → Extract & Containerize → Create Deployment Artifacts → Deploy to AWS
- Generates CloudFormation templates, registers images to ECR, deploys to ECS/EKS/App Runner
- Supports pre-built CI/CD pipelines; no code changes required

---

## Key Configurations

- **EC2 User Data**: runs at first start only, runs as root, bootstraps instance
- **Security Groups**: inbound blocked by default, outbound allowed by default; allow rules only
- **Elastic IP limit**: 5 per account (soft limit)
- **ENI**: bound to AZ; can be detached and reattached for failover
- **Hibernate**: RAM < 150 GB; root volume EBS encrypted; max 60 days
- **Placement Group Spread**: max 7 instances per AZ per group
- **Placement Group Partition**: max 7 partitions per AZ; 100s of instances total
- **Spot Instance termination**: 2-minute grace period; must cancel request before terminating instances
- **ECS Task Role**: defined per task definition; different role per service
- **EKS**: one cluster per region; CSI driver required for persistent storage

---

## Architectural Patterns

### High Availability Pattern
- Spread Placement Group: instances across multiple AZs on different hardware
- ENI failover: move ENI from failed to standby instance
- ECS Fargate + EFS: serverless containers with shared persistent storage across AZs

### Cost Optimization Pattern
- Spot Instances + Spot Fleet with priceCapacityOptimized strategy
- Reserved Instances for steady-state workloads + On-Demand for spikes
- Savings Plans for flexible long-term commitments

### Event-Driven Container Workloads
- S3 event → EventBridge rule → ECS Fargate Task → process data → DynamoDB
- SQS queue → ECS Service polling → auto-scale tasks based on queue depth
- EventBridge Schedule → ECS Task → batch processing → S3

### Microservices on AWS
- ECS (EC2 or Fargate) + ALB for HTTP routing
- ECR for image storage; ECS Task Roles for per-service IAM permissions
- ECS Service Auto Scaling with Target Tracking on CPU or ALB request count

### Kubernetes Migration
- Use EKS when company already uses Kubernetes on-prem
- EKS Managed Node Groups + Fargate for mixed workloads
- CloudWatch Container Insights for observability

### Compliance / Licensing
- Dedicated Host for BYOL (per-socket/per-core licensing) or strong compliance needs
- Dedicated Instances when hardware isolation needed but placement control not required

---

## Important Numbers & Limits

| Item | Value |
|---|---|
| Elastic IP per account | 5 (soft limit, can request increase) |
| Placement Group Spread — max instances per AZ | 7 |
| Placement Group Partition — max partitions per AZ | 7 |
| Placement Group Cluster — network bandwidth | 10 Gbps (with Enhanced Networking) |
| EC2 Hibernate — max RAM | < 150 GB |
| EC2 Hibernate — max duration | 60 days |
| Spot Instance termination grace period | 2 minutes |
| Reserved Instance discount vs On-Demand | up to 72% |
| Convertible Reserved Instance discount | up to 66% |
| Spot Instance discount vs On-Demand | up to 90% |
| Dedicated Host Reservation discount | up to 70% |
| IPv4 address space (public) | ~3.7 billion |
| On-Demand billing granularity (Linux/Windows) | per second after first minute |
| On-Demand billing granularity (other OS) | per hour |
| EC2 Instance Connect — requires port open | 22 |
| ECS Cluster Capacity Provider | paired 1:1 with ASG |

---

## Diagram Descriptions

**Private vs Public IP Diagram**: Two company private networks (192.168.0.1/22 each) connect to internet via their own Internet Gateways (public IPs). Public web servers accessible directly via their public IPs. Private machines use NAT through gateway to reach WWW.

**Security Groups Diagram**: EC2 instance has two SG layers — Inbound filter (allows Port 22 from specific IP, blocks from others) and Outbound filter (allows all traffic to WWW). Blocked traffic never reaches EC2.

**Security Groups Cross-Reference Diagram**: EC2 instance A allows inbound on Port 123 from SG1 and SG2 (instances with those SGs pass through), but blocks traffic from SG3 instances. Useful for service-to-service authorization without IP management.

**Placement Group Cluster Diagram**: 6 EC2 instances in 3x2 grid, all in same AZ, all interconnected, labeled "low latency 10 Gbps network."

**Placement Group Spread Diagram**: 3 AZs (us-east-1a/b/c), each AZ has 2 EC2 instances on separate hardware racks (Hardware 1-6). Each instance on unique hardware.

**Placement Group Partition Diagram**: 2 AZs (us-east-1a/b); AZ-a has 2 partitions (4 EC2 each), AZ-b has 1 partition (4 EC2). Partitions don't share racks.

**ENI Diagram**: AZ contains 2 EC2 instances. EC2-1 has primary ENI (eth0, 192.168.0.31) and secondary ENI (eth1, 192.168.0.42). Secondary ENI can be moved to EC2-2 for failover.

**EC2 Hibernate Flow Diagram**: Running (RAM + EBS) → Hibernate → Stopping (RAM saved to EBS) → Shutdown → Stopped (RAM on EBS) → Start → Running (RAM restored from EBS). RAM state preserved across stop/start cycle.

**Docker vs VM Diagram**: VMs stack: Infrastructure → Host OS → Hypervisor → Guest OS per app. Docker stack: Infrastructure → Host OS (EC2 instance) → Docker Daemon → many containers sharing daemon. Containers far more lightweight.

**Docker Getting Started Diagram**: Dockerfile → Build → Docker Image ↔ Push/Pull → Docker Repository (Docker Hub or ECR) → Run → Docker Container.

**ECS EC2 Launch Type Diagram**: ECS Cluster contains 3 EC2 instances, each running Docker + ECS Agent + multiple ECS Tasks (containers).

**ECS Fargate Launch Type Diagram**: ECS Cluster managed by Fargate; tasks run directly without visible EC2 instances underneath.

**ECS IAM Roles Diagram**: EC2 Instance Profile used by ECS Agent (accesses ECS, ECR, CloudWatch). Each task (A, B) has separate Task Role (A→S3, B→DynamoDB).

**ECS Load Balancer Diagram**: Users → ALB (port 80/443) → ECS Tasks spread across EC2 instances in ECS Cluster.

**ECS EFS Data Volume Diagram**: EC2 instances and Fargate tasks in ECS Cluster both mount same Amazon EFS file system, enabling shared persistent storage across AZs.

**ECS Scaling Diagram**: CloudWatch Metric (CPU Usage) → CloudWatch Alarm → ECS Auto Scaling → new tasks; optionally triggers ECS Capacity Provider to scale underlying EC2 ASG.

**ECS EventBridge Diagram**: Client uploads to S3 → EventBridge rule triggers → new Fargate task runs with ECS Task Role (access S3 + DynamoDB) → saves result to DynamoDB.

**ECS SQS Diagram**: Messages → SQS Queue → ECS Service A polls queue → auto-scales tasks (Task 1, 2, 3) based on queue depth.

**EKS Diagram**: VPC with 3 AZs; each AZ has public subnet (ELB + NAT Gateway) and private subnet (EKS worker nodes with pods). EKS nodes span AZs in Auto Scaling Group. Public and private service load balancers for different access patterns.

**App Runner Diagram**: Container Image or Source Code → Configure Settings (vCPU, RAM, Auto Scaling, Health Check) → Create & Deploy → Access using URL.

**A2C Workflow Diagram**: Discover & Analyze → Extract & Containerize → Create Deployment Artifacts (ECS/EKS task definitions, CloudFormation templates, CI/CD) → Deploy to AWS (ECR + ECS/EKS/App Runner).

---

## Exam-Relevant Details

### Key Distinctions

**Dedicated Instances vs Dedicated Hosts**
- Both use dedicated physical hardware
- Dedicated Instances: per-instance billing, no socket/core visibility, no placement control
- Dedicated Hosts: per-host billing, socket/core visibility, affinity control, BYOL licensing support
- Signal: "BYOL" or "compliance" or "per-core licensing" → Dedicated Host

**Reserved vs Savings Plans**
- RI: locked to instance type + region + OS; Zonal RI reserves AZ capacity
- Savings Plans: locked to instance family + region, flexible on size/OS/tenancy
- Both offer ~72% max discount; both 1 or 3 year terms

**ECS EC2 Launch Type vs Fargate**
- EC2: you manage infrastructure; use when you need control or cost optimization
- Fargate: serverless; use when simplicity and auto-scaling matter
- Fargate auto scaling is "much easier to setup"

**ECS vs EKS**
- ECS: AWS-proprietary, simpler; EKS: Kubernetes (open-source, cloud-agnostic)
- Use EKS when already using Kubernetes on-premises or in another cloud
- Both support EC2 and Fargate launch types

**Placement Group Cluster vs Spread vs Partition**
- Cluster: performance (low latency, 10 Gbps) but all eggs in one basket (same AZ)
- Spread: max HA, max 7/AZ, spans AZs
- Partition: big data workloads (Hadoop/Kafka/Cassandra), 100s of instances, rack isolation

**ECS Task Role vs EC2 Instance Profile**
- Instance Profile: used by ECS Agent on EC2 host (access to ECS API, ECR, CloudWatch)
- Task Role: used by the application inside the container; defined in task definition
- Both needed for EC2 launch type; only Task Role relevant for Fargate

### Common Exam Traps

- Public IP **changes** on stop/start — use Elastic IP or DNS/Load Balancer for stability
- Cancelling a Spot Request does NOT terminate the instance — must terminate separately
- Capacity Reservations have NO billing discount — billed at On-Demand rate even if unused
- Security Groups only have **allow** rules — no explicit deny
- EC2 Instance Connect works out-of-the-box only with **Amazon Linux 2**, requires port 22 open
- ENIs are **AZ-bound** — cannot move an ENI to a different AZ
- Hibernate requires root EBS volume to be **encrypted**
- ECS Service Auto Scaling ≠ EC2 Auto Scaling (task level vs instance level)
- **S3 cannot be mounted as a file system** — use EFS for ECS shared storage
- Spot Fleet cancelling does not stop instances already running
- EKS requires **one cluster per region** for multi-region deployments

### Keyword Signals for Exam

| Keyword | Service/Option |
|---|---|
| "BYOL", "per-socket/per-core licensing" | Dedicated Host |
| "compliance", "regulatory isolation" | Dedicated Host or Dedicated Instances |
| "steady-state", "database", "predictable" | Reserved Instances |
| "batch jobs", "fault tolerant", "flexible timing" | Spot Instances |
| "short-term, uninterrupted, specific AZ" | Capacity Reservations |
| "serverless containers" | Fargate |
| "migrate from Kubernetes on-prem" | EKS |
| "Amazon-native containers" | ECS |
| "store Docker images" | ECR |
| "rapid deployment, no infra knowledge" | App Runner |
| "low latency between instances" | Placement Group Cluster |
| "HA, isolated failures" | Placement Group Spread |
| "Hadoop/Cassandra/Kafka" | Placement Group Partition |
| "fixed public IP" | Elastic IP |
| "virtual network card", "failover IP" | ENI |
| "preserve RAM on stop" | EC2 Hibernate |
| "run once at first boot" | EC2 User Data |
| "time out connecting" | Security Group issue |
| "connection refused" | Application not running (not SG) |
| "Java/.NET app to containers" | App2Container (A2C) |
| "event-driven container task" | ECS + EventBridge |
| "scheduled container batch job" | ECS + EventBridge Scheduler |
| "queue-based container scaling" | ECS + SQS |
