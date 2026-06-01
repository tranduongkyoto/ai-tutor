# AWS SAA-C03 Master Cheat Sheet — Content Cache
> Source: SkillCertPro AWS Solutions Architect Associate Master Cheat Sheet (54 pages)

---

## Domain 1: Design Secure Architectures (30%)

### 1.1: Design Secure Access to AWS Resources

#### IAM Users and Root User — Security Best Practices
- **Root User:** Complete, unrestricted access to all services/resources. Use only for initial setup (creating the first IAM user). Lock away securely after that.
- **IAM Users:** Represent individual people or applications. Use for day-to-day operations.
- **Principle of Least Privilege:** Grant only the permissions required for the specific task. Avoid broad policies like AdministratorAccess.
- **MFA (Multi-Factor Authentication):** Enable for ALL users, especially root. Requires second factor (authenticator app, security key) in addition to password. Significantly reduces unauthorized access risk.
- **Strong Passwords:** Enforce minimum length, complexity requirements, and regular rotation.
- **Credential Rotation:** Rotate access keys regularly. Never embed credentials in code — use IAM roles instead.
- **Monitor Activity:** Use AWS CloudTrail to log API calls and monitor for suspicious activity.

#### IAM Authorization Model: Users, Groups, Roles, Policies
- **IAM Users:** Individual identities. Directly attaching policies is possible but not scalable.
- **IAM Groups:** Collections of IAM users. Attach policies to the group; all users inherit those permissions. Best practice for managing permissions for users with similar job functions.
- **IAM Roles:** Identities designed for entities needing temporary access to AWS resources. No long-term credentials (access keys). Use temporary credentials via AWS STS.
  - **AWS Services (EC2, Lambda):** Preferred way for applications to access AWS resources — application assumes a role, receives temporary credentials.
  - **Federated Users (corporate directories):** Enables users from existing identity systems (Active Directory) to access AWS without separate IAM users.
  - **Cross-Account Access:** Allows users in one AWS account to access resources in another.
- **IAM Policies:** JSON documents defining permissions. Specify:
  - **Actions:** What is allowed (e.g., s3:GetObject, ec2:RunInstances)
  - **Resources:** Which resources the actions apply to
  - **Effect:** Allow or Deny
- **Types of Policies:**
  - **AWS Managed Policies:** Predefined by AWS; cover common use cases; good starting point
  - **Customer Managed Policies:** Created and managed by you; more granular control; recommended for specific requirements
  - **Inline Policies:** Embedded directly within an IAM user/group/role; deleted when entity is deleted; generally less preferred than customer managed

#### AWS STS and Role-Based Access Control
- **AWS Security Token Service (STS):** Provides temporary security credentials (access key ID, secret access key, session token) with limited lifespan.
  - **Role Assumption:** IAM user or AWS service assumes a role; STS provides temporary credentials
  - **Federation:** Grant AWS access to users from external IdPs (Active Directory, SAML, web identity). IdP authenticates user; STS provides temporary AWS credentials.
  - **Cross-Account Access:** Grant access to resources in one account to users/services in another
- **Role Switching:** AWS Management Console feature allowing IAM users to easily switch between roles within same account or across accounts.
- **Cross-Account Access Setup:**
  1. In resource account (B): create IAM role with permissions to access the resource
  2. In resource account (B): add trust policy allowing the principal in accessing account (A) to assume the role
  3. User in Account A assumes the role in Account B and gets temporary credentials

#### Multi-Account Strategy: AWS Control Tower and SCPs
- **AWS Control Tower:** Sets up and governs secure multi-account AWS environment. Automates creation of new accounts (using AWS Organizations) and implements best-practice security baselines (guardrails). Uses Organizations, SCPs, AWS Config, and other services.
- **Service Control Policies (SCPs):** Feature of AWS Organizations that centrally manages permissions for all accounts.
  - Define the **maximum** permissions that can be granted to IAM users and roles in member accounts
  - Act as guardrails — prevent actions even if an IAM policy would otherwise allow them
  - **Inheritance:** Inherited down the hierarchy (root → OUs → accounts)
  - **Deny by Default:** Use deny-by-default approach; explicitly grant using Allow statements
  - **Impact on IAM:** SCPs do not directly grant permissions; they limit what IAM policies can grant
  - **Use Cases:** Prevent disabling CloudTrail/Config; restrict specific services or regions; enforce encryption
  - **Example:** SCP at root denying ec2:RunInstances overrides any member account IAM policy allowing it

#### Resource Policies
- JSON documents attached directly to a resource defining who has access and what they can do
- **Amazon S3:** Bucket policies control access; grant public read for static website hosting; allow specific accounts to upload
- **AWS IAM:** Roles can have resource policies (trust policies) for fine-grained control over who can assume the role
- **AWS KMS:** Key policies determine who can use the key for encryption/decryption
- **Amazon SQS/SNS:** Resource policies on queues and topics control who can send/receive messages

#### Federation with IAM Roles
- **Federation:** Allows users authenticated in an external IdP to access AWS without separate IAM users
- **How it works:**
  1. Establish trust: create trust relationship between AWS account and external IdP (Active Directory, Okta, Ping Identity)
  2. Define IAM role with permissions federated users will have
  3. User authenticates with external IdP using existing credentials
  4. IdP provides temporary credentials; user assumes the pre-defined IAM role
  5. User accesses AWS resources based on role permissions
- **When to use:** Existing directory service; enforce consistent auth policies; provide access to external users/partners
- **Benefits:** Simplified user management; improved security (leverage existing auth); centralized access control

---

### 1.2: Design Secure Workloads and Applications

#### VPC Architecture with Security Components
- **Security Groups:** Virtual firewalls for EC2 instances. Define inbound/outbound rules at instance level. **Stateful** — if inbound allowed, corresponding outbound automatically allowed.
- **Route Tables:** Determine where network traffic from subnets is directed. Control flow within VPC and to external networks.
- **Network ACLs (NACLs):** Additional security layer at subnet level. **Stateless** — must define rules for both inbound and outbound. Broader control compared to security groups.
- **NAT Gateways:** Allow instances in private subnets to connect to internet/AWS services, but prevent internet from initiating connections to those instances.

#### Network Segmentation Strategies
- **Public Subnets:** Have a route to internet via Internet Gateway. Resources can be directly accessed from internet. Place web servers, load balancers here.
- **Private Subnets:** No direct route to internet. Resources cannot be directly accessed from internet. Place databases, application servers, backend systems here.
- **3-tier example:** Web servers in public subnet (Security Group: allow HTTP/HTTPS) → App servers in private subnet → Database servers in private subnet (Security Group: allow only DB traffic from app servers)

#### Key Security Services for Applications
- **AWS Shield:** DDoS protection.
  - **Standard:** Always-on protection against common infrastructure-level attacks (Layer 3/4). Free.
  - **Advanced:** Sophisticated detection/mitigation; 24/7 access to AWS DDoS response team. Paid.
- **AWS WAF (Web Application Firewall):** Protects web applications from common exploits (SQL injection, XSS). Pre-configured or custom rules to filter malicious traffic. Deploy on CloudFront, ALB, or API Gateway.
- **IAM Identity Center (formerly AWS SSO):** Manage user access to multiple AWS accounts/applications from central location. Supports Active Directory, Okta, Azure AD. Enforces consistent access policies.
- **AWS Secrets Manager:** Securely store and manage secrets (DB credentials, API keys, OAuth tokens). Encrypts at rest and in transit. Provides automatic rotation.

#### Securing External Network Connections
- **AWS VPN (Virtual Private Network):**
  - **Site-to-Site VPN:** Connects on-premises network to VPC
  - **Client VPN:** Individual users securely connect to AWS resources
- **AWS Direct Connect:** Dedicated network connections between on-premises and AWS. Higher bandwidth, lower latency than VPN. Suitable for high performance and consistent connectivity.

---

### 1.3: Determine Appropriate Data Security Controls

#### Compliance and Governance Services
- **AWS Artifact:** On-demand access to AWS compliance reports (SOC, PCI DSS attestations) and agreements. Understand how AWS infrastructure/services comply with standards.
- **AWS Audit Manager:** Continuously audit AWS usage to simplify risk assessment and compliance auditing. Automates evidence collection; pre-built frameworks for compliance standards.
- **AWS Config:** Detailed view of configuration of AWS resources. Track changes and ensure compliance with internal policies and regulatory requirements.

#### Encrypting Data at Rest
- **AWS Key Management Service (KMS):** Managed service for creating and managing encryption keys. Integrates with S3, EBS, RDS, and other services. Key types: AWS-managed keys, customer-managed keys, imported keys.
  - Supports automatic key rotation for customer master keys (CMKs)
- **Server-Side Encryption (SSE):**
  - **SSE-S3:** Encryption with S3-managed keys
  - **SSE-KMS:** Encryption with KMS-managed keys
  - **SSE-C:** Encryption with customer-provided keys
- **Client-Side Encryption:** Encrypt data before sending to AWS using your own libraries and keys. Maximum control but more management overhead.
- **AWS CloudHSM:** Dedicated hardware security modules (HSMs) for customers requiring highest level of security and compliance.

#### Encrypting Data in Transit
- **TLS/SSL:** Standard protocol for encrypting communication. ELB, CloudFront, API Gateway support TLS/SSL.
- **AWS Certificate Manager (ACM):** Provision, manage, and deploy SSL/TLS certificates for use with AWS services. Automatic renewal for certificates used with AWS services.
- **VPN and Direct Connect:** Encrypt data in transit over these connections.

#### Key Management Considerations
- **Key management:** KMS simplifies key management and provides options for controlling key access
- **Performance:** Encryption can impact performance; consider trade-offs
- **Cost:** Different encryption options have different costs

#### Data Backups and Replication
- **Amazon S3:** Highly durable and scalable object storage for backups. Versioning and cross-region replication for enhanced protection.
- **Amazon EBS:** EBS snapshots for backup of volumes.
- **AWS Backup:** Centralized backup service for EC2, EBS, RDS, DynamoDB, EFS. Define backup policies and schedules. Cost optimization through lifecycle policies.

#### Data Access, Lifecycle, and Protection Policies
- **Data access:** IAM policies and access control mechanisms define who can access what data
- **Data lifecycle:** S3 lifecycle policies define retention and deletion/archival rules
- **Data protection:** Encryption, access control, data loss prevention (DLP) measures

#### Encryption Key Rotation and Certificate Renewal
- **Why rotate keys:** Limits exposure if a key is compromised; meet compliance requirements
- **KMS:** Supports automatic key rotation for customer master keys (CMKs)
- **ACM:** Automatically renews SSL/TLS certificates used with AWS services

---

## Domain 2: Design Resilient Architectures (26%)

### 2.1: Design Scalable and Loosely Coupled Architectures

#### Architecture Patterns: Multi-tier, Microservices, Event-Driven

**Multi-tier Architectures:**
- Traditional approach: presentation (UI), application logic (business logic), data storage layers
- AWS services by tier:
  - **Presentation Tier:** S3 (static website), CloudFront (CDN), ELB
  - **Application Tier:** EC2, Elastic Beanstalk, ECS/EKS
  - **Data Tier:** RDS, DynamoDB, S3

**Microservice Architectures:**
- Small, independent services communicating over network; changes to one service don't require changes to others
- AWS services:
  - **API Gateway:** Manages API requests; routes to appropriate microservices
  - **AWS Lambda:** Serverless compute for individual functions
  - **ECS/EKS:** Container orchestration for deploying and managing microservices
  - **SQS/SNS:** Messaging for asynchronous communication

**Event-Driven Architectures:**
- Services communicate by producing and consuming events (not direct point-to-point)
- Significantly improves loose coupling and scalability
- AWS services:
  - **Amazon SQS:** Message queuing; decouples producers and consumers
  - **Amazon SNS:** Pub/sub messaging; broadcasts events to multiple subscribers
  - **Amazon EventBridge:** Serverless event bus; receives events from various sources (AWS services, custom apps, SaaS); routes to targets (Lambda, SQS)
  - **AWS Lambda:** Processes events

#### Scaling Strategies
- **Vertical Scaling (Scale Up):** Increase resources of single instance (CPU, memory, storage). Limited by max instance size. In AWS: choose larger EC2 instance type.
- **Horizontal Scaling (Scale Out):** Add more instances. Preferred for cloud — better fault tolerance and scalability.
  - **ELB:** Distributes traffic across multiple instances
  - **Auto Scaling:** Automatically adds/removes instances based on demand
  - **ECS/EKS:** Orchestrates containers across multiple instances

**Scaling strategies by component:**
- **Compute (EC2, Lambda, containers):** Auto Scaling based on CPU utilization, memory usage, request count
- **RDS:** Read replicas for scaling reads; scale up instance for increased performance
- **DynamoDB:** Scales automatically based on provisioned or on-demand capacity
- **SQS:** Scales automatically to handle any volume of messages
- **ElastiCache:** Scale by adding more cache nodes or choosing larger cache node type

#### Services for Loose Coupling
- **Amazon SQS:** Asynchronous messaging; decouples sender and receiver; messages stored until receiver is available
- **Amazon SNS:** Pub/sub; publisher sends to topic; multiple subscribers receive notifications
- **Amazon EventBridge:** Serverless event bus for event-driven architectures at scale
- **Amazon API Gateway:** Front door for applications; decouples frontend from backend; backend can evolve independently
- **Microservices pattern:** ECS, EKS, Lambda support small independent services

#### Containers: When to Use
- **Use containers when:**
  - Application portability required (consistent across dev/test/prod)
  - Implementing microservices
  - Consistent runtime environments needed
  - Optimizing resource utilization (containers share host OS kernel; more efficient than VMs)
- **AWS Container Services:**
  - **Amazon ECS (Elastic Container Service):** Fully managed container orchestration; supports Docker
  - **Amazon EKS (Elastic Kubernetes Service):** Managed Kubernetes; for orgs already using Kubernetes
  - **AWS Fargate:** Serverless compute engine for containers; removes need to manage EC2 instances

#### Serverless Technologies: When to Use
- **Benefits:**
  - Automatic scaling based on demand
  - Pay-per-use pricing (only pay for compute time consumed)
  - Reduced operational overhead (no server/OS/patching management)
- **Key serverless services:**
  - **AWS Lambda:** Run code without servers; triggered by events; ideal for event-driven apps and microservices
  - **Amazon API Gateway:** Create serverless APIs triggering Lambda
  - **Amazon S3:** Store static content or trigger Lambda on object uploads
- **Key considerations:**
  - Loose coupling can introduce complexity in inter-service communication and distributed tracing
  - Robust monitoring and observability crucial for distributed systems
  - Understand pricing model; optimize code for performance

#### Technology Selection: Compute, Storage, Networking, Database

**Compute:**
- **EC2:** Virtual servers; various instance types (compute-intensive, memory-intensive, etc.); use Auto Scaling
- **Lambda:** Serverless; ideal for event-driven and microservices
- **ECS/EKS:** Container orchestration; ECS is AWS-native; EKS allows Kubernetes on AWS

**Storage:**
- **S3:** Object storage for any amount of data; highly scalable, durable, cost-effective; use cases: backups, media, data lakes
- **EBS:** Block storage volumes for EC2 instances; persistent storage attached as virtual hard drives
- **EFS:** Network file system shared by multiple EC2 instances; ideal for shared file storage (CMS, web apps)

**Networking:**
- **VPC:** Isolated networks in AWS Cloud; control IP ranges, subnets, route tables
- **ELB:** Distributes traffic across EC2, containers, IP addresses
- **Route 53:** Highly available DNS; route traffic based on latency, geography, health checks

**Database:**
- **RDS:** Managed relational DB; MySQL, PostgreSQL, Oracle, SQL Server, MariaDB; automatic backups, patching, scaling
- **DynamoDB:** Managed NoSQL; fast and predictable performance; ideal for high throughput, low latency (gaming, mobile, web)
- **Aurora:** MySQL/PostgreSQL-compatible; combines performance/availability of commercial DBs with cost-effectiveness of open-source

**Purpose-built services:**
- **SQS:** Decouple application components; send, store, receive messages
- **SNS:** Pub/sub; send notifications to email, mobile, other AWS services
- **Step Functions:** Serverless orchestration; coordinate multiple services into workflows; visual designer and built-in error handling
- **ElastiCache:** Caching service; stores frequently accessed data in memory; supports Redis and Memcached

---

### 2.2: Design Highly Available and/or Fault-Tolerant Architectures

#### Automation Strategies for Infrastructure Integrity
- **Infrastructure as Code (IaC):** CloudFormation, CDK, Terraform — define and manage infrastructure through code; version control; automate deployments; replicate environments
- **Configuration Management:** Systems Manager, Ansible, Chef — automate configuration and management; consistent configurations; simplify patching
- **Automated Deployments:** CodeDeploy, CodePipeline — automate application deployment; reduce deployment time and errors
- **Automated Monitoring and Alerting:** CloudWatch — monitor health and performance; set alerts for corrective action
- **Automated Recovery:** Auto Scaling + automated failover — automatically recover from failures

#### Services for High Availability and Fault Tolerance
- **Availability Zones (AZs):** Distinct locations within an AWS Region; isolated from failures in other AZs; deploy across multiple AZs for continued operation if one fails
- **Elastic Load Balancing (ELB):** Distributes incoming traffic across multiple instances; improves availability and fault tolerance
  - Types: Application Load Balancer (ALB), Network Load Balancer (NLB), Classic Load Balancer (CLB)
- **Auto Scaling:** Automatically adjusts instance count based on demand; handles varying traffic loads; recovers from instance failures
- **Amazon S3:** 99.999999999% (11 nines) data durability; multiple storage classes with different availability and durability
- **Amazon RDS:** Multi-AZ deployments for built-in high availability and fault tolerance
- **Amazon DynamoDB:** Fully managed NoSQL; inherent high availability and scalability
- **Route 53:** DNS service; route traffic to healthy instances; perform health checks

#### Key Metrics for High Availability
- **RTO (Recovery Time Objective):** Maximum acceptable time for application to be unavailable after failure
- **RPO (Recovery Point Objective):** Maximum acceptable amount of data loss in case of failure
- **Availability:** Percentage of time application is available for use
- **MTBF (Mean Time Between Failures):** Average time between system failures
- **MTTR (Mean Time To Recovery):** Average time to recover from failure

#### Strategies for High Availability and Fault Tolerance
- **Redundancy:** Multiple instances across different AZs; multiple copies of data; multiple storage locations
- **Failover:** Mechanisms to automatically switch traffic to healthy instances
- **Health Checks:** Regularly monitor instance health; auto-remove unhealthy instances
- **Stateless Applications:** Don't store session state locally; use separate data store; easier to scale and replace
- **Data Replication:** Replicate across multiple AZs or Regions; S3 cross-region replication; RDS multi-AZ

#### Eliminating Single Points of Failure (SPOFs)
- **Multiple AZs:** Physically separate data centers with independent power, cooling, networking
- **Load Balancing:** Distribute traffic; if one instance fails, traffic redirected to remaining healthy instances (ALB, NLB, CLB)
- **Data Replication:** If one storage location fails, data still available
- **Auto Scaling:** Automatically launch new instance to replace failed instance
- **Stateless applications:** Store data in separate data store, not on instances

#### Disaster Recovery Strategies (ranked by RTO/RPO)
1. **Backup and Restore:** Back up data; restore to new environment in disaster. Simplest but longest RTO/RPO.
2. **Pilot Light:** Minimal environment in different region (core services: databases, networking). Scale up to full capacity in disaster.
3. **Warm Standby:** Fully functional but scaled-down version in different region. Constantly running; ready to take over.
4. **Multi-Region Active/Active:** Run application in multiple regions simultaneously. Traffic distributed; if one region fails, traffic automatically redirected. Lowest RTO/RPO.

#### Legacy Application Reliability Services
- **EC2 Auto Scaling:** Automatically scale instances; launch new instances to replace failures; useful for legacy apps without built-in scaling
- **ELB:** Distributes traffic; stops sending to failed instances; no significant code changes required
- **Route 53:** DNS failover capabilities; route to healthy instances or different regions
- **AWS Application Discovery Service:** Gather information about on-premises servers and apps; plan migration to AWS; understand dependencies and requirements

---

## Domain 3: Design High-Performing Architectures (24%)

### 3.1: Determine High-Performing and/or Scalable Storage Solutions

#### Storage Performance Metrics
- **Throughput:** Amount of data read/written per second
- **IOPS (Input/Output Operations Per Second):** Number of read/write operations per second
- **Latency:** Time to complete a read/write operation

#### AWS Storage Services and Performance

**Amazon S3:**
- Object storage; high durability, availability, scalability
- Wide range of use cases: backups, media files, application data, data lakes
- Storage classes with varying performance and cost:
  - **S3 Standard:** High performance for frequently accessed data; most expensive
  - **S3 Glacier:** Designed for long-term archival; lower performance

**Amazon EBS (Elastic Block Storage):**
- Block storage volumes attached to EC2 instances
- Volume types:
  - **gp3 (General Purpose SSD):** Balance of price and performance for wide variety of workloads
  - **io2 Block Express (Provisioned IOPS SSD):** Highest performance; consistent IOPS and low latency; mission-critical applications
  - **st1 (Throughput Optimized HDD):** High throughput for frequently accessed data with large sequential I/O
  - **sc1 (Cold HDD):** Lowest cost storage for infrequently accessed data

**Amazon EFS (Elastic File System):**
- Scalable and elastic file system shared by multiple EC2 instances
- Suitable for shared file storage (web servers, CMS)
- Performance modes: General Purpose and Max I/O

**Amazon FSx:**
- Fully managed file systems compatible with Windows File Server and Lustre
- High performance and scalability for demanding workloads

#### Storage Scalability
- **S3:** Inherently scalable; virtually unlimited data; automatically scales to handle increasing traffic
- **EBS:** Volumes can be resized; performance characteristics changeable; RAID configurations for increased performance
- **EFS:** Automatically scales capacity as files added/removed; can increase throughput as needed
- **FSx:** Can be scaled in terms of storage capacity and throughput

#### Key Considerations for Performance and Scalability
- Understand workload read/write patterns, throughput requirements, IOPS needs
- Determine data access frequency; choose appropriate storage class/service
- Conduct performance testing to validate configuration
- Monitor storage performance and utilization; identify bottlenecks

---

### 3.2: Design High-Performing and Elastic Compute Solutions

#### Decoupling Workloads for Independent Scaling
- **Decoupling benefits:**
  - Improved scalability: scale each component based on specific needs
  - Increased resilience: if one component fails, others continue
  - Enhanced maintainability: changes to one component less likely to affect others
- **Decoupling techniques:**
  - **Message queues (SQS, Amazon MQ):** Asynchronous communication; components don't need to wait for each other
  - **Event-driven architecture (SNS, EventBridge):** React to events; notification sent to interested components
  - **API Gateway:** Decouples frontend from backend services

#### Auto Scaling: Metrics and Conditions
- **Key metrics for Auto Scaling:**
  - CPU utilization
  - Memory utilization
  - Network traffic
  - Request count
- **Scaling policies:**
  - **Target tracking scaling:** Maintain specific metric value
  - **Step scaling:** Add/remove specific number of instances based on metric thresholds
  - **Scheduled scaling:** Scale based on predefined schedule
- **AWS Auto Scaling services:**
  - **EC2 Auto Scaling:** Automatically scale EC2 instance count
  - **Application Load Balancer:** Auto-distribute traffic and scale instances
  - **Lambda:** Automatically scales functions based on incoming request count

#### EC2 Instance Types and Selection
- **General Purpose (M instances):** Balanced compute, memory, networking. Web servers, small/medium databases. Examples: m5.large, m6g.medium
- **Compute Optimized (C instances):** High CPU. Batch processing, media transcoding, HPC. Examples: c5.xlarge, c6i.2xlarge
- **Memory Optimized (R, X instances):** Large memory. In-memory databases, data analytics, high-performance databases. Examples: r5.2xlarge, x2gd.large
- **Storage Optimized (I, D instances):** High disk throughput and IOPS. NoSQL databases, data warehousing, distributed file systems. Examples: i3.xlarge, d2.8xlarge
- **Accelerated Computing (P, G, F instances):** GPUs, FPGAs. Machine learning, graphics rendering, video encoding. Examples: p3.2xlarge, g4dn.xlarge

#### Instance Size Selection Approach
1. Start with benchmark: begin small; monitor under typical workload
2. Monitor resource utilization: CloudWatch metrics (CPU, memory, network, disk I/O)
3. Right-size based on utilization: downsize if underutilized; upsize if overutilized
4. Consider burstable performance: T instances offer burstable performance for variable CPU demands

#### Key Design Considerations for Elastic Compute
- **Scalability:** Design to scale automatically using Auto Scaling (EC2) or Lambda's automatic scaling
- **Performance:** Choose right compute options and resource sizes; consider CPU, memory, storage, networking
- **Cost-efficiency:** Use right pricing models (On-Demand, Reserved, Spot); right-size resources
- **Monitoring:** Monitor performance to identify and address bottlenecks

---

### 3.3: Determine High-Performing Database Solutions

#### Read Replicas
- Copies of primary database instance used to handle read traffic
- **Benefits:**
  - Increased read throughput: offload read operations from primary instance
  - Improved availability: read replica can be promoted to new primary if primary fails
  - Disaster recovery: replicas in different AZs or Regions
- **Use cases:** E-commerce, CMS with heavy read traffic; reporting and analytics with large data queries
- **Considerations:**
  - Asynchronous — slight delay between write to primary and availability on replica
  - Can create multiple read replicas for a single primary
  - Read replicas can have their own read replicas (multi-tier architecture)

#### Database Architecture Patterns
- **Single DB instance:** Small applications with low traffic
- **Multi-AZ deployment:** High availability by replicating DB instance across multiple AZs
- **Read replicas:** Improve read performance and availability
- **Database sharding:** Distribute data across multiple DB instances to improve scalability

#### Database Engine Selection

**MySQL vs PostgreSQL:**
| Feature | MySQL | PostgreSQL |
|---------|-------|------------|
| Ease of use | Easier to set up and use | More complex to configure |
| Performance | Generally faster for simple reads | Better performance for complex queries |
| Features | Fewer advanced features | More advanced features and extensions |
| Data integrity | Less strict data integrity checks | Strong data integrity checks |
| Scalability | Good scalability for read-heavy workloads | Good scalability with careful tuning |
| Community | Large and active community | Strong and active community |

**MySQL:** Popular open-source RDBMS; ease of use, performance, scalability; web apps, e-commerce, CMS
**PostgreSQL:** Advanced features, data integrity, extensibility; complex transactions, data warehousing, geospatial
**Amazon Aurora:** MySQL/PostgreSQL-compatible; improved performance and availability; good for demanding applications
**Oracle:** Commercial; enterprise-grade features and scalability
**SQL Server:** Commercial from Microsoft; commonly used in enterprise environments
**Amazon DynamoDB:** NoSQL; high performance and scalability; high traffic, low latency requirements
**Amazon Redshift:** Data warehouse optimized for large-scale data analytics

#### Database Type Selection
- **Relational (Row-based):** Structured schema with ACID properties; financial transactions, inventory management
  - **RDS:** MySQL, PostgreSQL, MariaDB, Oracle, SQL Server
  - **Aurora:** MySQL/PostgreSQL-compatible; higher performance; serverless options (v1 and v2)
- **NoSQL (Non-relational):** Flexible schema; high scalability and performance; web apps, mobile, IoT
  - **DynamoDB:** Key-value and document; extremely low latency; high scalability
- **Data Warehousing (Columnar):** Optimized for analytical queries on large datasets
  - **Redshift:** Columnar storage; efficient compression; faster query performance; use Redshift Spectrum to query S3 directly
- **Time Series:** Optimized for time-stamped data
  - **Amazon Timestream:** Automatic scaling; serverless options
- **Graph Databases:** Highly connected datasets
  - **Amazon Neptune:** Property graph and RDF data models

**Decision table: choosing database type by data format:**
- **Time Series Format:** Amazon Timestream
- **Columnar Format (Analytical):** Amazon Redshift (large-scale); Amazon Athena (smaller-scale, query S3 directly)
- **Relational Data (Transactional):** Amazon RDS or Amazon Aurora; Aurora Serverless for variable workloads
- **Key-Value/Document (High Throughput, Low Latency):** Amazon DynamoDB
- **Graph Data (Relationships between data):** Amazon Neptune

#### Caching Strategies
- **Read-Through Caching:** Application checks cache first; on miss, retrieves from DB, stores in cache, returns to user
- **Write-Through Caching:** Application writes to both cache and DB simultaneously; cache always consistent with DB
- **Lazy Loading/Cache-Aside:** Application checks cache first; on miss, fetches from DB, stores in cache, returns it; subsequent requests served from cache
- **Amazon ElastiCache engines:**
  - **Memcached:** Simple and fast in-memory caching; session data, web page fragments
  - **Redis:** Advanced in-memory data store; supports lists, sets, hashes; leaderboards, real-time analytics, complex caching

---

### 3.4: Determine High-Performing and/or Scalable Network Architectures

#### Network Topologies for Global, Hybrid, Multi-tier Architectures

**Global Architectures (spanning multiple AWS Regions):**
- **Latency:** Route 53 (DNS based on geolocation/latency), CloudFront (CDN for caching content closer to users), Global Accelerator (direct traffic to optimal endpoints)
- **Data Replication/Synchronization:** S3 cross-region replication; database replication features
- **Disaster Recovery:** Global architectures serve as DR solutions for each other

**Hybrid Architectures (on-premises + AWS):**
- **Connectivity:** AWS Direct Connect (dedicated connection) or AWS VPN (encrypted over internet)
- **Network Segmentation:** Properly segment network between on-premises and AWS for security
- **Consistent Management:** Tools for managing both on-premises and AWS resources

**Multi-Tier Architectures (3-tier):**
- **Security:** Each tier isolated using Security Groups and NACLs
- **Scalability:** Each tier scales independently
- **Load Balancing:** Distribute traffic across multiple instances in each tier

#### Scalable Network Configurations
- **Elasticity:** Auto Scaling groups for EC2; ELB for traffic distribution; SQS/SNS for decoupling
- **Subnet Sizing:** CIDR blocks providing enough IP addresses for future growth
- **Avoid SPOFs:** Multiple AZs, multiple VPN connections
- **Automation:** IaC tools (CloudFormation, Terraform) for network provisioning

#### Resource Placement Considerations
- **Latency:** Place resources close to users or dependent systems
- **Data Residency:** Place data in specific Regions for regulatory compliance
- **Cost Optimization:** Choose most cost-effective services and Regions
- **Availability and DR:** Distribute across multiple AZs or Regions

#### Load Balancing Strategy Selection
- **Application Load Balancer (ALB):** Best for HTTP/HTTPS traffic; application-level routing (path-based, host-based routing)
- **Network Load Balancer (NLB):** Best for TCP/UDP traffic; high performance, low latency; operates at Layer 4 (Transport)
- **Classic Load Balancer (CLB):** Older generation; generally less preferred than ALB and NLB
- **Global Accelerator:** Improves performance for global applications; routes traffic through AWS global network backbone; provides static IP addresses

---

### 3.5: Determine High-Performing Data Ingestion and Transformation Solutions

#### Building and Securing Data Lakes
- **Data lake:** Centralized repository for structured, semi-structured, unstructured data at any scale
- **Amazon S3:** Foundation of most data lakes on AWS; highly scalable and durable object storage
- **AWS Lake Formation:** Simplifies building, securing, and managing data lakes; automates data discovery, cataloging, and fine-grained access control
- **AWS Glue:** Fully managed ETL service; data catalog, ETL jobs, crawler for automatically discovering data
- **Security for data lakes:**
  - Access control: IAM roles and policies
  - Encryption: S3 SSE or client-side encryption
  - Data masking and tokenization: protect sensitive data
  - Auditing: log and monitor access

#### Data Streaming Architectures
- **Amazon Kinesis family:**
  - **Kinesis Data Streams:** Capture and store streams of data (real-time)
  - **Kinesis Data Firehose:** Load streaming data into data stores and analytics tools
  - **Kinesis Data Analytics:** Process streaming data with SQL or Java applications
- **Amazon MSK (Managed Streaming for Apache Kafka):** Fully managed Apache Kafka clusters; popular open-source distributed streaming platform

#### Data Transfer Solutions
- **AWS Snow Family:** Physical devices for transferring large amounts of data offline
  - **Snowcone:** Small, ruggedized device for edge computing and data transfer
  - **Snowball Edge:** Larger device with more storage and compute capabilities
  - **Snowmobile:** Truck-sized exabyte-scale data transfer service
- **AWS DataSync:** Automates transfer of data between on-premises storage and AWS storage services
- **AWS Transfer Family:** Managed file transfer using SFTP, FTPS, and FTP protocols

#### Data Visualization
- **Amazon QuickSight:** Cloud-based BI service; create interactive dashboards and visualizations from various data sources
- Can also integrate with Tableau, Power BI, and Looker

#### Big Data Processing: Amazon EMR
- **Amazon EMR (Elastic MapReduce):** Managed service running Apache Hadoop, Spark, Hive, Presto
- Process vast amounts of data using distributed computing
- **Use cases:** Log analysis, data warehousing, machine learning, ETL
- **EMR selection considerations:**
  - Instance types: choose appropriate EC2 types (memory-optimized, compute-optimized)
  - Cluster size: number of nodes based on data volume and processing needs
  - EMR releases: select appropriate release version
  - Storage options: S3 for persistent storage, HDFS for temporary within cluster

**Other compute options for data processing:**
- **Lambda:** Serverless; event-driven processing of smaller datasets or triggered transformations
- **AWS Glue:** Serverless ETL; schema discovery; simpler transformations
- **EC2:** More customized control; more management overhead

#### Data Ingestion Configurations
- **Amazon S3:** Landing zone for raw data; use AWS CLI, SDKs, third-party tools
- **AWS Kinesis:** Real-time streaming ingestion; ingest high-velocity data
- **AWS Glue Crawlers:** Automatically discover schemas from S3 or other data stores
- **AWS DataSync:** Efficient and secure transfer from on-premises to AWS
- **AWS Snow Family:** Offline transfer for large datasets

#### Data Format Transformation
- **CSV:** Simple and widely used; not efficient for large datasets
- **Parquet:** Columnar format optimized for analytical queries; significant storage savings; faster query times; recommended format
- **JSON:** Semi-structured; common for web apps and APIs
- **Avro:** Row-based with rich schema support; often used in Hadoop ecosystems

**Tools for format transformation:**
- **EMR (Spark, Hive):** Complex transformations including format conversions; Spark ideal for large-scale
- **AWS Glue:** Simpler transformations and format conversions
- **Lambda:** Smaller-scale or event-driven transformations

---

## Domain 4: Design Cost-Optimized Architectures (20%)

### 4.1: Design Cost-Optimized Storage Solutions

#### Storage Strategies: Batch vs Individual Uploads to S3
- **Batch Uploads:** Upload multiple files in single operation; use AWS CLI, SDKs, S3 Transfer Acceleration
  - Advantages: Reduced overhead (fewer requests), improved performance for many files
  - Disadvantages: More complex implementation; larger failure domain
- **Individual Uploads:** Upload one file at a time
  - Advantages: Simpler implementation; smaller failure domain
  - Disadvantages: Higher overhead (more requests); slower for many files
- **When to use which:**
  - **Batch:** Large numbers of small files, frequent uploads, performance critical
  - **Individual:** Small number of files, infrequent uploads, simplicity paramount
- **Other strategies:**
  - Data lifecycle management: move from S3 Standard to Glacier based on access frequency
  - Data compression: compress before storing to reduce costs

#### S3 Storage Classes — Decision Framework
| Storage Class | Use Case | Key Characteristics |
|---------------|----------|---------------------|
| S3 Standard | Frequently accessed data | High durability, availability, performance. Most expensive. |
| S3 Intelligent-Tiering | Unknown/changing access patterns | Auto-moves objects between frequent/infrequent tiers. Small monthly monitoring fee. |
| S3 Standard-IA | Less frequently accessed, rapid access needed | Lower storage cost than Standard; retrieval fees apply. |
| S3 One Zone-IA | Less frequently accessed, single AZ OK | Lower than Standard-IA; less resilient to AZ failures; not for critical data. |
| S3 Glacier Instant Retrieval | Archival, millisecond access needed | Lower storage cost than Standard-IA; retrieval fee. |
| S3 Glacier Flexible Retrieval | Archival, minutes-to-hours retrieval | Lower storage cost than Glacier Instant; retrieval times: minutes to hours. |
| S3 Glacier Deep Archive | Long-term archival, rarely accessed | Lowest storage cost; retrieval times 12-48 hours. |

**Factors for storage class selection:**
- Access frequency: how often will data be accessed?
- Retrieval time: how quickly does data need to be retrieved?
- Durability and availability requirements
- Cost budget

#### S3 Lifecycle Policies
- Define rules for transitioning objects between storage classes or deleting them
- Rules based on: object age, object prefix, object tags
- **Example lifecycle policy:**
  - Move to S3 Standard-IA after 30 days
  - Move to S3 Glacier Flexible Retrieval after 90 days
  - Permanently delete after 365 days

#### Storage Size and Right-Sizing
- **Factors to consider:**
  - Current data volume
  - Data growth rate
  - Data retention policies
  - Data access patterns
- Use CloudWatch to track storage usage and identify trends

#### Cost-Effective Data Transfer to AWS
- **Internet:** Simplest, often cheapest for small datasets; slow and expensive for large datasets
- **AWS Direct Connect:** Higher bandwidth, lower latency; recurring costs; suitable for high volumes
- **AWS Snow Family:** Physical devices; cost-effective for very large datasets or limited bandwidth
- **AWS DataSync:** Online transfer; cost-effective for large datasets with frequent changes

#### Backup and Archival Solution Selection
- **AWS Backup:** Centralized backup for EC2, EBS, RDS, DynamoDB, EFS; define backup policies; cost optimization through lifecycle policies; best for frequent backups and fast restores
- **Amazon S3 Glacier:** Long-term archival; lowest cost for infrequently accessed data; use lifecycle policies or direct uploads; best for long-term archival with less stringent recovery requirements
- **AWS Storage Gateway:** Connects on-premises to cloud-based storage; useful for hybrid cloud backup
- **Selection factors:** RTO, RPO, data retention requirements, cost

#### Data Migration to Storage Services
- **Snow Family (Snowcone, Snowball Edge, Snowmobile):** Large data transfers offline; physically shipped devices; when bandwidth is limited/unavailable
- **AWS DataSync:** Online transfer between on-premises and AWS storage; uses software agent
- **AWS Transfer Family (SFTP, FTPS, FTP):** Secure file transfers using standard protocols
- **AWS Storage Gateway:** Hybrid cloud storage scenarios including data migration
- **Selection factors:** Data volume, network bandwidth, migration timeline, security requirements

#### Most Cost-Effective Storage Service Selection
- **S3:** Object storage; various tiers for cost optimization; backups, archives, media, data lakes
- **EBS:** Block storage for EC2; high performance and low latency; different volume types for varying performance/cost
- **EFS:** Shared file storage accessed by multiple instances concurrently
- **FSx:** Managed file systems for specific workloads (Windows File Server, Lustre for HPC)
- **Storage Gateway:** Hybrid cloud connecting on-premises to AWS storage
- **Selection considerations:** Data access patterns (random vs sequential), performance requirements, durability/availability needs, cost

---

### 4.2: Design Cost-Optimized Compute Solutions

#### Load Balancer Selection for Cost Optimization
- **ALB (Application Load Balancer — Layer 7):** Best for HTTP/HTTPS, content-based routing, path-based, host-based routing, WebSockets; ideal for web apps and APIs
- **NLB (Network Load Balancer — Layer 4):** Best for TCP/UDP traffic; high performance, low latency; static IP addresses; Elastic IPs supported
- **GWLB (Gateway Load Balancer — Layer 3/4):** Deploy and manage virtual appliances (firewalls, IDS/IPS, DPI); transparent bump-in-the-wire; centralized management

**Choosing the right load balancer:**
- HTTP/HTTPS + content-based routing → **ALB**
- TCP/UDP + high performance + low latency → **NLB**
- Virtual appliances (firewalls, IDS/IPS) → **GWLB**

#### Scaling Methods for Elastic Workloads
- **Horizontal Scaling (Scale Out/In):** Add or remove instances; most common and preferred in cloud
  - High availability: distributes traffic across multiple instances
  - Elasticity: easily scales up or down based on demand
  - Cost-effective: only pay for resources you use
- **Vertical Scaling (Scale Up/Down):** Change size of existing instance (e.g., t3.medium → t3.large)
  - Use cases: applications that cannot be easily distributed; short-term performance boosts

**Auto Scaling Strategies:**
- **Manual Scaling:** Manually adjust instance count or size
- **Automatic Scaling:** Based on metrics (CPU, network traffic, request count)
  - **Target tracking scaling:** Maintain target value for specific metric
  - **Step scaling:** Add/remove specific number of instances based on metric thresholds
  - **Scheduled scaling:** Scale based on predefined schedule

#### EC2 Hibernation
- Stop and start EC2 instances while preserving in-memory state (RAM)
- **Use cases:** Long-running processes (pause/resume without losing progress); cost savings (only pay for storage while hibernated)

#### EC2 Pricing Models — Cost Optimization
- **On-Demand:** Pay by hour or second; no commitments; short-term, unpredictable, initial development
- **Reserved Instances (RIs):** Significant discount for 1-year or 3-year commitment; steady-state workloads with predictable usage
- **Savings Plans:** Flexible pricing; lower costs than On-Demand; commitments for 1 or 3 years; apply to EC2, Lambda, and Fargate; more flexible than RIs (apply to various instance families and regions)
- **Spot Instances:** Up to 90% off On-Demand prices for spare EC2 capacity; fault-tolerant workloads that can be interrupted (batch processing, data analysis, testing)
- **Dedicated Hosts:** Dedicated physical servers; workloads with strict regulatory or licensing requirements

#### EC2 Instance Families for Cost Optimization
- **General Purpose (M):** Balanced; web servers, app servers, small DBs. m5.large, m6g.medium
- **Compute Optimized (C):** High CPU; batch processing, media transcoding, HPC. c5.xlarge, c6i.2xlarge
- **Memory Optimized (R, X):** Large memory; in-memory DBs, data analytics, high-perf DBs. r5.2xlarge, x2gd.large
- **Storage Optimized (I, D):** High disk throughput/IOPS; NoSQL DBs, data warehousing. i3.xlarge, d2.8xlarge
- **Accelerated Computing (P, G, F):** GPUs/FPGAs; ML, graphics rendering, video encoding. p3.2xlarge, g4dn.xlarge

#### Cost-Effective Compute Service Selection
- **Lambda:** Serverless; pay only for compute time consumed; no idle costs; event-driven, background tasks, APIs with variable traffic; Use cases: data upload processing, DynamoDB changes, serverless APIs, scheduled tasks
- **EC2:** Virtual servers; various pricing options (On-Demand, RI, Savings Plans, Spot, Dedicated Hosts)
- **Fargate:** Serverless containers; pay for vCPU and memory consumed; no infrastructure management; running containerized apps, microservices, batch jobs

#### Availability vs Cost Trade-offs
| Workload Type | Availability Requirement | Cost Implications |
|---------------|--------------------------|-------------------|
| Production | High (e.g., 99.99%) | Higher costs: redundancy, multiple AZs, load balancing, more expensive instances |
| Non-Production | Low to Moderate (95-99.9%) | Lower costs: Spot Instances, single AZ, less expensive instances, scheduling |
| Batch Processing | Variable (tolerant to interruptions) | Use Spot Instances; design for fault tolerance and restart capabilities |

#### Cost Optimization Strategies Summary
- **Right-sizing:** Choose appropriate instance types/sizes for workloads
- **Reserved Instances (RIs):** Significant discounts for steady-state workloads (1 or 3 year commitment)
- **Savings Plans:** Flexible pricing for EC2, Lambda, Fargate (1 or 3 year commitment)
- **Spot Instances:** Up to 90% discount for fault-tolerant, interruptible workloads
- **Auto Scaling:** Automatically adjust instance count; only pay for what you need
- **Stop unused instances:** Terminate instances not in use
- **Use AWS Cost Explorer:** Analyze spending; identify opportunities for optimization

---

### 4.3: Design Cost-Optimized Database Solutions

#### Backup and Retention Policies
- **Snapshots:** Incremental backups; point-in-time copies; stored in S3
- **Backup frequency:** More frequent = finer recovery points but higher storage costs; balance with RPO
- **Retention policy:** Longer retention = more recovery options but higher costs; balance with regulatory requirements
- **Cost optimization strategies:**
  - Automated backups: use AWS database automated backup features
  - Snapshot lifecycle management: use lifecycle policies to auto-delete old snapshots
  - Copy snapshots to lower-cost storage: move infrequent snapshots to S3 Glacier

#### Cost-Effective Database Service Selection
- **RDS vs DynamoDB:**
  - **RDS:** Relational data, ACID properties → appropriate choice
  - **DynamoDB:** High throughput, low latency, flexible schema → appropriate choice
  - **Serverless options:** Variable workloads → Aurora Serverless, DynamoDB On-Demand

**All database types and cost characteristics:**
- **RDS:** Cost based on instance size, storage, I/O, data transfer; use reserved instances or savings plans for steady-state
- **Aurora:** MySQL/PostgreSQL-compatible; significantly improved performance; Aurora Serverless v1/v2 for variable workloads
- **DynamoDB:** Cost based on read/write capacity units, storage, data transfer; On-demand for unpredictable; provisioned for predictable (with auto scaling); cost-optimize with auto scaling
- **DocumentDB (MongoDB-compatible):** Instance size, storage, I/O based cost
- **Amazon Keyspaces (Apache Cassandra-compatible):** Read/write capacity units, storage, data transfer
- **Redshift:** Node type, number of nodes, storage; use Redshift Spectrum to query data in S3 without loading into Redshift
- **Amazon Timestream:** Time series; writes, storage, queries based cost; automatic scaling, serverless options
- **Amazon Neptune:** Graph database; instance size, storage, I/O based cost

**Choosing database type by data format — cost perspective:**
- **Time Series Format:** Amazon Timestream (most cost-effective)
- **Columnar Format (Analytical):** Redshift for large-scale; Athena for smaller-scale (query S3 directly)
- **Relational Data:** RDS or Aurora; Aurora Serverless for variable
- **Key-Value/Document (High Throughput, Low Latency):** DynamoDB
- **Graph Data:** Neptune

#### Database Migration for Cost Optimization
- **AWS DMS (Database Migration Service):** Migrate databases quickly and securely; supports relational and NoSQL; homogeneous (Oracle→Oracle) and heterogeneous (Oracle→Aurora) migrations
- **AWS SCT (Schema Conversion Tool):** Convert database schemas from one engine to another (Oracle, SQL Server, MySQL → Aurora, Redshift)
- **Cost considerations during migration:**
  - DMS costs: based on data transferred and migration duration
  - Storage costs: both source and target during migration
  - Compute costs: EC2 instances for migration tasks
  - Downtime costs: minimize downtime to avoid business disruption

#### Database Cost Optimization Strategies
- **Right-sizing:** Choose appropriate instance size based on workload
- **Reserved Instances or Savings Plans:** Significant savings for steady-state workloads
- **Spot Instances (non-critical):** Cost savings but can be interrupted
- **Serverless options:** Aurora Serverless, DynamoDB On-Demand for variable workloads
- **Storage optimization:** Appropriate storage types and compression techniques
- **Monitor database performance:** Regularly monitor and identify areas for optimization

---

### 4.4: Design Cost-Optimized Network Architectures

#### NAT Gateway Cost Considerations
- **Single shared NAT gateway:** Simplest and often cheapest for smaller workloads; single point of failure; all traffic routes through single NAT gateway (bottleneck for high-traffic)
- **NAT gateway per AZ:** High availability and fault tolerance; more expensive (paying for multiple); recommended for production workloads
- **NAT Instance:** Older method; EC2 instance configured for NAT; more control but more management; generally less cost-effective and less performant than NAT Gateways
- **NAT gateway cost components:**
  - Hourly usage: charged for each hour gateway is provisioned
  - Data processing: charged per GB of data processed
  - Data transfer out: charged for data transferred to internet

#### Network Connection Cost Comparison
- **Internet:** Simplest, often cheapest for smaller workloads/dev environments; less reliable/secure than dedicated connections
- **VPN (Virtual Private Network):** Secure encrypted connections; good for secure connectivity without extremely high bandwidth; more expensive than internet but less than Direct Connect
- **AWS Direct Connect:** Dedicated network connections; highest bandwidth, lowest latency, most consistent performance; most expensive; suitable for mission-critical apps requiring high performance and reliability
- **Cost considerations:**
  - Data transfer: charged for data in and out of AWS
  - Port hours (Direct Connect): hourly rate per Direct Connect port
  - VPN connection hours: hourly rate per VPN connection
- **Choosing right network connection:**
  - Low bandwidth, low security need → Internet
  - Secure connectivity, moderate bandwidth → VPN
  - High bandwidth, low latency, mission-critical → Direct Connect

#### Minimizing Network Transfer Costs
- **Region-to-Region:** Data transfer between Regions incurs costs; keep resources that communicate within same Region
- **AZ-to-AZ:** Lower than cross-region costs; place resources that communicate frequently in same AZ
- **Private to public:** Private IP to public IP incurs costs; use NAT gateways or VPC endpoints
- **VPC Endpoints:** Connect to S3, DynamoDB, and other AWS services privately without traversing public internet; avoids data transfer costs; improves security
  - **Interface endpoints:** ENIs within subnets; private connectivity to services
  - **Gateway endpoints:** Attached to route tables; private connectivity to S3 and DynamoDB
- **AWS Global Accelerator:** Routes traffic through AWS global network; can reduce latency; reduce data transfer costs by optimizing routing across the AWS network

#### CDN and Edge Caching for Cost Reduction
- **CDNs (Amazon CloudFront):** Store copies of content at edge locations worldwide; serve from closest location; reduce latency; reduce data transfer costs
- **Edge caching:** Cache content at edge locations; reduces need to retrieve from origin servers; especially beneficial for frequently accessed static content
- **When to use CDN:**
  - Users distributed globally
  - Static content that doesn't change frequently
  - Content accessed frequently

#### Reviewing Workloads for Network Optimization
- **Data transfer costs:** Analyze patterns; reduce by co-locating resources in same AZ/Region; use VPC endpoints; compress data
- **Elastic IP addresses:** Release unused Elastic IPs to avoid charges
- **Network traffic patterns:** Use VPC Flow Logs for insights; identify bottlenecks/inefficient routing
- **VPN connections:** If consistently underutilized, consider downsizing or consolidating
- **Direct Connect:** If underutilized, consider downsizing or using VPN instead
- **NAT Gateway usage:** NAT Gateways charge per GB; evaluate if NAT Instances might be more cost-effective for predictable traffic

#### Throttling Strategies
- **Identify bottlenecks:** Network devices, connections, applications
- **Throttling mechanisms:**
  - **NACLs:** Block/allow traffic based on IP addresses and ports
  - **Security Groups:** Virtual firewalls for EC2 instances
  - **AWS WAF:** Protect web apps from malicious traffic; rate limiting
  - **API Gateway throttling:** Control rate of API requests
- Throttling prevents unexpected cost spikes from sudden traffic increases

#### Bandwidth Allocation: VPN vs Direct Connect
- **Single VPN:** Sufficient for low-to-medium bandwidth; single point of failure
- **Multiple VPNs:** Higher bandwidth and redundancy; more expensive
- **Direct Connect speeds:** 1 Gbps to 100 Gbps; choose based on bandwidth requirements
- **Direct Connect locations:** Choose geographically close to on-premises to minimize latency
- **Direct Connect redundancy:** Multiple connections in different locations for high availability
- **Example decision:** If consistent 500 Mbps need — two 500 Mbps VPN connections might be more cost-effective than single 1 Gbps Direct Connect if utilization consistently below 1 Gbps; but if growth anticipated beyond 1 Gbps, Direct Connect might be better long-term strategy

---

## Quick Reference: Key Service Decision Frameworks

### Compute: When to Use Which
| Scenario | Service |
|----------|---------|
| Event-driven, short-duration tasks | Lambda |
| Containerized microservices | ECS/EKS + Fargate |
| Long-running, stateful workloads | EC2 |
| Steady-state, predictable load | EC2 Reserved Instances |
| Fault-tolerant, interruptible batch | EC2 Spot Instances |
| Variable containerized workloads | Fargate |

### Database: When to Use Which
| Scenario | Service |
|----------|---------|
| Structured data + ACID transactions | RDS (MySQL, PostgreSQL, Aurora) |
| High throughput + low latency + flexible schema | DynamoDB |
| Large-scale data warehousing + analytics | Redshift |
| Time-series data | Amazon Timestream |
| Highly connected data (social networks, graphs) | Amazon Neptune |
| Document data + MongoDB compatibility | Amazon DocumentDB |
| Apache Cassandra compatibility | Amazon Keyspaces |
| Variable workloads, pay-per-use | Aurora Serverless, DynamoDB On-Demand |

### Storage: When to Use Which
| Scenario | Service |
|----------|---------|
| Object storage (backups, media, data lakes) | S3 |
| Block storage for EC2 instances | EBS |
| Shared file storage for multiple EC2 instances | EFS |
| Windows File Server | FSx for Windows |
| High-performance computing (Lustre) | FSx for Lustre |
| Hybrid cloud storage | Storage Gateway |
| Long-term archival | S3 Glacier |

### Load Balancer: When to Use Which
| Scenario | Service |
|----------|---------|
| HTTP/HTTPS + content-based routing | ALB (Layer 7) |
| TCP/UDP + high performance + low latency | NLB (Layer 4) |
| Third-party virtual appliances (firewalls, IDS/IPS) | GWLB (Layer 3/4) |
| Global traffic optimization | Global Accelerator |

### Messaging: When to Use Which
| Scenario | Service |
|----------|---------|
| Decouple producers and consumers (queue) | SQS |
| Fan-out notifications (pub/sub) | SNS |
| Complex event routing from many sources | EventBridge |
| Real-time streaming data ingestion | Kinesis Data Streams |
| Load streaming data into storage/analytics | Kinesis Firehose |
| Managed Apache Kafka | Amazon MSK |
| Complex workflow orchestration | Step Functions |

### Network Connection: When to Use Which
| Scenario | Service |
|----------|---------|
| Secure connection over internet (low cost) | AWS VPN |
| Dedicated connection (high bandwidth, low latency) | AWS Direct Connect |
| Reduce latency for global users | CloudFront (CDN) |
| Private connectivity to S3/DynamoDB | VPC Gateway Endpoints |
| Private connectivity to other AWS services | VPC Interface Endpoints |
| Optimize global application performance | AWS Global Accelerator |

### DR Strategy: When to Use Which
| Strategy | RTO/RPO | Cost | Use Case |
|----------|---------|------|----------|
| Backup and Restore | Highest | Lowest | Non-critical; cost-sensitive |
| Pilot Light | Hours | Low-medium | Core systems must be recoverable |
| Warm Standby | Minutes | Medium-high | Business-critical with some downtime tolerance |
| Multi-Region Active/Active | Near-zero | Highest | Mission-critical; no downtime acceptable |

---

## Exam Tips and Common Traps

### Domain 1 (Security)
- **Trap:** Confusing Security Groups (stateful, instance-level) with NACLs (stateless, subnet-level)
- **Tip:** SCPs do NOT grant permissions — they only restrict; always need IAM policies too
- **Tip:** For cross-account access: role in resource account + trust policy + principal from accessing account assumes role
- **Tip:** KMS customer-managed keys support automatic rotation; AWS-managed keys rotated annually automatically
- **Trap:** SSE-C = customer provides key at upload/download time; AWS doesn't store the key
- **Tip:** AWS Shield Standard is free; Shield Advanced costs money but provides 24/7 DDoS response team

### Domain 2 (Resilient)
- **Tip:** Multi-AZ RDS = synchronous replication (HA); Read Replicas = asynchronous replication (performance)
- **Trap:** Read Replicas are NOT automatically promoted — you must manually promote
- **Tip:** S3 has 99.999999999% (11 nines) durability; S3 One Zone-IA is lower because single AZ
- **Tip:** For lowest RTO/RPO: Multi-Region Active/Active; for most cost-effective DR: Backup and Restore
- **Trap:** Stateful applications are harder to scale horizontally — always prefer stateless design

### Domain 3 (Performance)
- **Tip:** EBS io2 Block Express for highest consistent IOPS; gp3 for balanced price/performance
- **Tip:** Use read replicas to offload read traffic; DynamoDB DAX for microsecond caching of DynamoDB reads
- **Tip:** CloudFront caches content at edge locations; reduces origin load and latency
- **Tip:** ALB for HTTP/HTTPS; NLB for TCP/UDP with ultra-low latency; GWLB for network appliances
- **Trap:** EFS automatically scales; EBS requires manual resizing

### Domain 4 (Cost)
- **Tip:** Reserved Instances = commitment to instance type in Region; Savings Plans = more flexible commitment to spend amount per hour
- **Tip:** Spot Instances up to 90% discount — but can be interrupted with 2-minute notice
- **Tip:** S3 Intelligent-Tiering adds small monthly monitoring fee — not always cheapest if access pattern is predictable
- **Tip:** VPC endpoints (Gateway for S3/DynamoDB, Interface for others) save data transfer costs AND improve security
- **Trap:** NAT Gateway per AZ costs more but provides high availability; single NAT Gateway is cheaper but is a SPOF
- **Tip:** Fargate = no need to manage EC2 instances; pay per vCPU/memory used; good for variable container workloads
