# Security & Identity - AWS CSA Content Cache

## Services & Concepts

### AWS IAM (Identity and Access Management)
- **Global service** — not region-specific
- **Root account**: created by default; should never be used or shared for day-to-day work
- **Users**: people within org; can belong to multiple groups; don't have to belong to any group
- **Groups**: contain users only — groups cannot contain other groups
- **Policies**: JSON documents assigned to users or groups defining permissions
- **Least privilege principle**: never give more permissions than needed

### IAM Policy Structure
- **Version**: always "2012-10-17"
- **Id**: optional identifier for the policy
- **Statement**: one or more statements (required), each containing:
  - **Sid**: optional statement identifier
  - **Effect**: Allow or Deny
  - **Principal**: account/user/role the policy applies to
  - **Action**: list of actions allowed or denied (e.g., `s3:GetObject`)
  - **Resource**: list of resources actions apply to (e.g., `arn:aws:s3:::mybucket/*`)
  - **Condition**: optional — when this policy is in effect

### IAM Policy Inheritance
- Policies attached to groups are inherited by all group members
- Users in multiple groups inherit permissions from all groups
- Users not in any group can have **inline policies** attached directly
- Diagram: Developers group policy → Alice, Bob, Charles; Audit Team policy → Charles, David; Operations policy → David, Edward; Fred has inline policy only

### IAM Password Policy
- Set minimum password length
- Require uppercase, lowercase, numbers, non-alphanumeric characters
- Allow IAM users to change their own passwords
- Require password expiration after N days
- Prevent password re-use

### Multi-Factor Authentication (MFA)
- MFA = password (you know) + security device (you own)
- Benefit: if password stolen, account is NOT compromised
- **MFA device options**:
  - Virtual MFA device: Google Authenticator (phone only), Authy (phone only) — supports multiple tokens on single device
  - Universal 2nd Factor (U2F) Security Key: YubiKey by Yubico (3rd party) — supports multiple root and IAM users on single key
  - Hardware Key Fob: provided by Gemalto (3rd party)
  - Hardware Key Fob for GovCloud: provided by SurePassID (3rd party)

### How Users Access AWS
- **AWS Management Console**: protected by password + MFA
- **AWS CLI**: protected by access keys; open-source; direct access to public APIs
- **AWS SDK**: protected by access keys; language-specific libraries; embedded in application
  - Supports: JavaScript, Python, PHP, .NET, Ruby, Java, Go, Node.js, C++
  - Mobile SDKs: Android, iOS; IoT Device SDKs: Embedded C, Arduino
  - AWS CLI is built on AWS SDK for Python
- **Access Keys**: Access Key ID (~= username) + Secret Access Key (~= password); never share them

### IAM Roles for Services
- Assign permissions to AWS services using IAM Roles (instead of users)
- Common roles: EC2 Instance Roles, Lambda Function Roles, Roles for CloudFormation
- Diagram: IAM Role attached to EC2 instance → EC2 uses role to access AWS services

### IAM Security Tools
- **IAM Credentials Report** (account-level): lists all account users and status of their credentials
- **IAM Access Advisor** (user-level): shows service permissions granted to a user and when last accessed; use to revise policies and enforce least privilege

### IAM Best Practices
- Don't use root account except for AWS account setup
- One physical user = One AWS user; never share
- Assign users to groups; assign permissions to groups
- Create strong password policy + enforce MFA
- Use Roles for giving permissions to AWS services
- Use Access Keys for programmatic access (CLI/SDK)
- Audit with IAM Credentials Report and Access Advisor
- Never share IAM users or access keys

---

### IAM Advanced: Conditions
- **aws:SourceIp**: restrict client IP from which API calls are made
- **aws:RequestedRegion**: restrict which region API calls are made to
- **ec2:ResourceTag**: restrict based on resource tags
- **aws:MultiFactorAuthPresent**: force MFA for specific actions (e.g., deny ec2:StopInstances without MFA)

### IAM for S3
- `s3:ListBucket` applies to `arn:aws:s3:::bucket-name` (bucket-level permission)
- `s3:GetObject`, `s3:PutObject`, `s3:DeleteObject` apply to `arn:aws:s3:::bucket-name/*` (object-level permission)

### IAM Permission Boundaries
- Supported for **users and roles** (NOT groups)
- Advanced feature: set maximum permissions an IAM entity can get using a managed policy
- Effective permissions = intersection of (Permission Boundary) AND (Identity-based policy) AND (Organizations SCP)
- Use cases:
  - Delegate responsibilities to non-admins within their permission boundaries
  - Allow developers to self-assign policies without privilege escalation
  - Restrict one specific user (instead of whole account via SCP)

### IAM Policy Evaluation Logic (Priority order)
1. Explicit Deny — always wins
2. Organizations SCPs
3. Resource-based policies
4. Identity-based policies
5. IAM Permission Boundaries
6. Session policies
- Default: implicit Deny on everything

### IAM Roles vs Resource-Based Policies
- **Assuming a role**: you give up original permissions and take role permissions
- **Resource-based policy**: principal keeps their own permissions AND gains access
- Use resource-based policy when user needs permissions in BOTH accounts simultaneously (e.g., scan DynamoDB in Account A and write to S3 in Account B)
- Supported by: S3 buckets, SNS topics, SQS queues, Lambda, API Gateway, etc.

### aws:PrincipalOrgID
- Used in resource policies to restrict access to accounts that are members of an AWS Organization
- Example: S3 bucket policy that only allows member accounts of org `o-yyyyyyyyy`

### Amazon EventBridge Security
- When a rule runs, it needs permissions on the target:
  - **Resource-based policy**: Lambda, SNS, SQS, S3 buckets, API Gateway
  - **IAM role**: EC2 Auto Scaling, Systems Manager Run Command, ECS task

---

### AWS Organizations
- **Global service** — manage multiple AWS accounts
- Main account = **management account**; others = **member accounts**
- Member accounts can only be part of ONE organization
- **Consolidated Billing**: single payment method; pricing benefits from aggregated usage
- Shared reserved instances and Savings Plans discounts across accounts
- API available to automate AWS account creation

### Organizational Units (OU) — Structure
- Root OU → Management Account → child OUs → member accounts
- OU examples:
  - Business Unit: Sales OU, Retail OU, Finance OU
  - Environmental Lifecycle: Prod OU, Dev OU, Test OU
  - Project-Based: Project 1 OU, Project 2 OU, Project 3 OU

### Service Control Policies (SCP)
- IAM policies applied to OU or Accounts to restrict Users and Roles
- Do NOT apply to the management account (always full admin power)
- Must have explicit allow from root through each OU in path to target account (does not allow anything by default — like IAM)
- SCP strategies:
  - **Blocklist**: Allow `*` then explicitly Deny specific services (e.g., DenyDynamoDB)
  - **Allowlist**: Only explicitly Allow specific services (e.g., ec2:*, cloudwatch:*)

### AWS Organizations — Tag Policies
- Standardize tags across resources in an AWS Organization
- Define tag keys and allowed values
- Prevent non-compliant tagging operations on specified services
- Generate report listing all tagged/non-compliant resources
- Use EventBridge to monitor non-compliant tags
- Helps with Cost Allocation Tags and Attribute-Based Access Control

---

### AWS IAM Identity Center (successor to AWS Single Sign-On)
- One login (SSO) for all:
  - AWS accounts in AWS Organizations
  - Business cloud applications (Salesforce, Box, Microsoft 365, Slack, Dropbox)
  - SAML 2.0-enabled applications
  - EC2 Windows Instances
- Identity providers:
  - Built-in identity store in IAM Identity Center
  - 3rd party: Active Directory (AD), OneLogin, Okta
- **Permission Sets**: collection of one or more IAM Policies assigned to users/groups to define AWS access
- **Login flow**: User signs in → IAM Identity Center portal → selects account → gets access with configured permissions

### IAM Identity Center Architecture
- Browser logs into IAM Identity Center → uses Permission Sets → SSO to AWS Organization accounts, Business Cloud Apps, Custom SAML2.0 apps
- Identity store: Active Directory (on-prem or cloud) OR built-in IAM Identity Center store

### IAM Identity Center Fine-grained Permissions
- **Multi-Account Permissions**: manage access across AWS accounts in Organization using Permission Sets
- **Application Assignments**: SSO to SAML 2.0 apps (Salesforce, Box, Microsoft 365); provide URLs, certificates, metadata
- **Attribute-Based Access Control (ABAC)**: fine-grained permissions based on user attributes (cost center, title, locale); define permissions once, modify access by changing attributes

### Active Directory (AD)
- Found on any Windows Server with AD Domain Services
- Database of objects: User Accounts, Computers, Printers, File Shares, Security Groups
- Centralized security management; objects organized in trees; a group of trees is a forest

### AWS Directory Services
- **AWS Managed Microsoft AD**: create your own AD in AWS, manage users locally, supports MFA; establish trust connections with on-premises AD
- **AD Connector**: Directory Gateway (proxy) to redirect to on-premises AD, supports MFA; users managed on-premises
- **Simple AD**: AD-compatible managed directory on AWS; CANNOT be joined with on-premises AD

### IAM Identity Center — Active Directory Setup
- Connect to AWS Managed Microsoft AD: out-of-the-box integration
- Connect to Self-Managed Directory (two options):
  - Create two-way trust relationship using AWS Managed Microsoft AD
  - Create an AD Connector (proxy)

### AWS Control Tower
- Easy way to set up and govern a secure and compliant multi-account AWS environment based on best practices
- Uses AWS Organizations to create accounts
- Benefits:
  - Automate environment setup in a few clicks
  - Automate ongoing policy management using guardrails
  - Detect policy violations and remediate
  - Monitor compliance through interactive dashboard

### AWS Control Tower — Guardrails
- **Preventive Guardrail**: uses SCPs (e.g., restrict regions across all accounts)
- **Detective Guardrail**: uses AWS Config (e.g., identify untagged resources)
- Flow: AWS Config monitors member accounts → triggers SNS on NON_COMPLIANT → notifies Admin AND invokes Lambda to remediate (e.g., add tags)

---

### Encryption Fundamentals

#### Encryption in Flight (TLS/SSL)
- Data encrypted before sending, decrypted after receiving
- TLS certificates enable HTTPS
- Prevents Man-in-the-Middle (MITM) attacks
- Flow: Client → TLS Encryption → encrypted data in transit → TLS Decryption → HTTPS Website

#### Server-Side Encryption at Rest
- Data encrypted after received by server; decrypted before being sent
- Stored in encrypted form using a data key
- Encryption/decryption keys managed by the service (e.g., S3)

#### Client-Side Encryption
- Data encrypted by client; server never decrypts it
- Data decrypted only by receiving client
- Can leverage Envelope Encryption
- Could use any storage service (S3, FTP, etc.)

---

### AWS KMS (Key Management Service)
- Anytime you hear "encryption" for an AWS service → it's likely KMS
- AWS manages encryption keys; fully integrated with IAM for authorization
- Audit KMS key usage via CloudTrail
- Seamlessly integrated into: EBS, S3, RDS, SSM, and more
- Never store secrets in plaintext — especially not in code

### KMS Key Types
- **Symmetric (AES-256)**: single key for encrypt and decrypt; never accessed unencrypted (must call KMS API); all AWS-integrated services use symmetric CMKs
- **Asymmetric (RSA & ECC key pairs)**: public key (encrypt) + private key (decrypt); used for Encrypt/Decrypt or Sign/Verify; public key downloadable; private key never accessed unencrypted; use case: encryption outside AWS by users who can't call KMS API

### KMS Key Categories
- **AWS Owned Keys** (free): SSE-S3, SSE-SQS, SSE-DDB (default keys)
- **AWS Managed Key** (free): named `aws/service-name` (e.g., `aws/rds`, `aws/ebs`)
- **Customer Managed Keys created in KMS**: $1/month
- **Customer Managed Keys imported**: $1/month
- Plus: $0.03 per 10,000 API calls to KMS

### KMS Key Rotation
- **AWS-managed KMS Key**: automatic rotation every 1 year
- **Customer-managed KMS Key**: must be enabled; supports automatic AND on-demand rotation
- **Imported KMS Key**: only manual rotation possible using aliases

### KMS Key Policies
- Control access to KMS keys (similar to S3 bucket policies)
- Cannot control key access WITHOUT them — unlike most IAM resources
- **Default KMS Key Policy**: created if no specific policy provided; gives complete access to root user = entire AWS account
- **Custom KMS Key Policy**: define users/roles that can access the key; define who can administer the key; useful for cross-account access

### Copying Snapshots Across Regions (KMS)
- Diagram: EBS Volume (encrypted with KMS Key A in eu-west-2) → Snapshot (encrypted with KMS Key A) → KMS ReEncrypt with KMS Key B → Snapshot (encrypted with KMS Key B in ap-southeast-2) → new EBS Volume
- Must re-encrypt with a key in the destination region

### Copying Snapshots Across Accounts (KMS)
1. Create snapshot encrypted with Customer Managed Key
2. Attach KMS Key Policy to authorize cross-account access
3. Share the encrypted snapshot
4. In target account: copy snapshot, encrypt with CMK in target account
5. Create volume from snapshot

### KMS Multi-Region Keys
- Identical KMS keys in different AWS Regions — used interchangeably
- Same key ID, key material, automatic rotation
- Encrypt in one region → decrypt in other regions (no re-encrypt needed)
- NOT global — Primary + Replicas managed independently
- Use cases: global client-side encryption, Global DynamoDB encryption, Global Aurora encryption
- ARN format: `arn:aws:kms:REGION:ACCOUNT:key/mrk-1234abcd...`

### DynamoDB Global Tables + KMS Multi-Region Keys
- Encrypt specific attributes client-side using Amazon DynamoDB Encryption Client
- Combined with Global Tables → encrypted data replicated to other regions
- With multi-region MRK replicated same as DynamoDB Global Table region → low-latency KMS API calls to decrypt locally
- Protect specific fields even from database admins

### Global Aurora + KMS Multi-Region Keys
- Encrypt specific attributes client-side using AWS Encryption SDK
- Combined with Aurora Global Tables → encrypted data replicated to other regions
- Clients in each region use local MRK replica to decrypt — low latency

### S3 Replication + Encryption Considerations
- Unencrypted objects and SSE-S3 encrypted objects: replicated by default
- SSE-C (customer-provided key): can be replicated
- SSE-KMS: must enable the option explicitly:
  - Specify which KMS Key to use for target bucket
  - Adapt KMS Key Policy for target key
  - IAM Role with `kms:Decrypt` for source key AND `kms:Encrypt` for target key
  - May hit KMS throttling — request Service Quotas increase
  - Multi-region KMS keys treated as independent keys by S3 (still decrypts then re-encrypts)

### AMI Sharing with KMS Encryption
1. AMI in Source Account encrypted with KMS Key from Source Account
2. Modify image attribute to add Launch Permission for target account
3. Share KMS Keys used to encrypt snapshot the AMI references
4. Target account IAM Role/User needs: DescribeKey, ReEncrypt*, CreateGrant, Decrypt
5. When launching: target account can optionally specify new KMS key to re-encrypt volumes

---

### SSM Parameter Store
- Secure storage for configuration and secrets
- Optional seamless encryption using KMS
- Serverless, scalable, durable, easy SDK
- Version tracking of configurations/secrets
- Security through IAM
- Notifications with Amazon EventBridge
- Integration with CloudFormation
- Hierarchy: `/my-dept/my-app/dev/db-url`, `/my-dept/my-app/prod/db-password`
- Can reference Secrets Manager secrets: `/aws/reference/secretsmanager/secret_ID`
- Public parameters: `/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2`

### SSM Parameter Store Tiers

| Feature | Standard | Advanced |
|---|---|---|
| Max parameters | 10,000 | 100,000 |
| Max value size | 4 KB | 8 KB |
| Parameter policies | No | Yes |
| Cost | Free | $0.05/advanced param/month |

### SSM Parameter Policies (Advanced only)
- Assign TTL/expiration date to force update/delete of sensitive data
- Policy types:
  - **Expiration**: delete parameter at timestamp
  - **ExpirationNotification**: notify via EventBridge N days before expiry
  - **NoChangeNotification**: notify via EventBridge if not changed for N days
- Can assign multiple policies simultaneously

---

### AWS Secrets Manager
- Newer service, specifically for storing secrets
- Force **rotation of secrets** every X days
- Automate secret generation on rotation using Lambda
- Native integration with Amazon RDS (MySQL, PostgreSQL, Aurora)
- Secrets encrypted using KMS
- Primarily meant for RDS integration (key differentiator from SSM Parameter Store)

### Secrets Manager — Multi-Region Secrets
- Replicate secrets across multiple AWS Regions
- Read replicas kept in sync with primary secret
- Can promote read replica to standalone secret
- Use cases: multi-region apps, disaster recovery, multi-region DB

---

### AWS Certificate Manager (ACM)
- Provision, manage, deploy TLS certificates (in-flight encryption / HTTPS)
- Supports public and private TLS certificates
- **Public TLS certificates: free**
- Automatic TLS certificate renewal
- Integrations (load TLS certs on): ELB (CLB, ALB, NLB), CloudFront Distributions, APIs on API Gateway
- **Cannot use ACM with EC2** (certificates can't be extracted from ACM)

### ACM — Requesting Public Certificates
1. List domain names (FQDN: corp.example.com OR Wildcard: *.example.com)
2. Select validation method: DNS Validation (preferred, uses CNAME record in Route 53) or Email validation (sends to WHOIS contacts)
3. Takes a few hours to verify
4. Enrolled for automatic renewal — ACM renews 60 days before expiry

### ACM — Importing Certificates
- No automatic renewal — must import new certificate before expiry
- ACM sends daily expiration events starting **45 days prior** to expiration (configurable)
- Events appear in EventBridge
- AWS Config managed rule: `acm-certificate-expiration-check`

### ACM — Integration with ALB
- ALB with HTTP → HTTPS redirect rule; ACM provisions and maintains TLS certs on ALB; backend EC2 instances receive plain HTTP

### ACM — Integration with API Gateway
- Edge-Optimized: TLS certificate must be in us-east-1 (same as CloudFront); then set CNAME or A-Alias in Route 53
- Regional: TLS certificate must be in same region as API Stage; then set CNAME or A-Alias in Route 53

---

### AWS CloudHSM (Hardware Security Module)
- KMS: AWS manages software for encryption
- CloudHSM: AWS provisions encryption **hardware** (dedicated HSM device)
- You manage your own encryption keys entirely (not AWS)
- HSM device is tamper-resistant; **FIPS 140-2 Level 3** compliance
- Supports symmetric and asymmetric encryption (SSL/TLS keys)
- **No free tier**
- Must use CloudHSM Client Software
- Redshift supports CloudHSM for database encryption and key management
- Good option for SSE-C encryption
- HA: CloudHSM clusters spread across Multi-AZ

### CloudHSM vs KMS Comparison

| Feature | AWS KMS | AWS CloudHSM |
|---|---|---|
| Tenancy | Multi-Tenant | Single-Tenant |
| Standard | FIPS 140-2 Level 3 | FIPS 140-2 Level 3 |
| Master Keys | AWS Owned, AWS Managed, Customer Managed | Customer Managed only |
| Key Types | Symmetric, Asymmetric, Digital Signing | Symmetric, Asymmetric, Digital Signing & Hashing |
| Key Accessibility | Multiple regions (can't access outside creation region) | Deployed in VPC; can share across VPCs via peering |
| Cryptographic Acceleration | None | SSL/TLS Acceleration, Oracle TDE Acceleration |
| Access & Auth | AWS IAM | You create users and manage their permissions |
| High Availability | AWS Managed Service | Add multiple HSMs over different AZs |
| Audit | CloudTrail, CloudWatch | CloudTrail, CloudWatch, MFA support |
| Free Tier | Yes | No |

### CloudHSM Integration with AWS Services
- Through integration with AWS KMS: configure KMS Custom Key Store with CloudHSM
- Then EBS, S3, RDS, etc. use KMS which backs to CloudHSM
- Key usage logs → CloudTrail

---

### AWS WAF (Web Application Firewall)
- Protects web applications from common web exploits (Layer 7 = HTTP; NOT Layer 4 TCP/UDP)
- Deploy on: Application Load Balancer, API Gateway, CloudFront, AppSync GraphQL API, Cognito User Pool
- Define **Web ACL (Web Access Control List)** Rules:
  - IP Set: up to **10,000 IP addresses** (use multiple rules for more IPs)
  - HTTP headers, HTTP body, URI strings — protect from SQL injection and XSS
  - Size constraints, geo-match (block countries)
  - Rate-based rules (count events) — for DDoS protection
- Web ACL are **Regional** except for CloudFront (global)
- A **rule group** is a reusable set of rules that can be added to a Web ACL
- WAF does NOT support Network Load Balancer (Layer 4)
- For fixed IP with WAF: use Global Accelerator for fixed IP → ALB + WAF

---

### AWS Shield (DDoS Protection)
- **Shield Standard** (free, automatic for all AWS customers):
  - Protects from: SYN/UDP floods, reflection attacks, Layer 3/4 attacks
- **Shield Advanced** ($3,000/month/organization):
  - Protects EC2, ELB, CloudFront, Global Accelerator, Route 53
  - 24/7 access to AWS DDoS Response Team (DRP)
  - Protects against higher fees during usage spikes due to DDoS
  - Automatic application layer DDoS mitigation: creates, evaluates, deploys WAF rules to mitigate Layer 7 attacks

---

### AWS Firewall Manager
- Manage security rules across all accounts in an AWS Organization
- Security policies include: WAF rules (ALB, API Gateway, CloudFront), Shield Advanced (ALB, CLB, NLB, Elastic IP, CloudFront), Security Groups (EC2, ALB, ENI), AWS Network Firewall (VPC level), Route 53 Resolver DNS Firewall
- Policies created at region level
- Rules applied automatically to new resources as they are created (great for compliance)

### WAF vs Firewall Manager vs Shield
- **WAF alone**: granular protection of specific resources
- **WAF + Firewall Manager**: WAF across accounts, automate protection of new resources
- **Shield Advanced**: adds DDoS-specific features on top of WAF (dedicated SRT team, advanced reporting)
- For frequent DDoS attacks → purchase Shield Advanced

---

### DDoS Best Practices (AWS Reference Architecture)
- **BP1 — CloudFront/Global Accelerator**: Web app delivery at edge; protect from SYN floods, UDP reflection; Global Accelerator integrates with Shield
- **BP2 — AWS WAF**: filter and block malicious requests at edge or ALB
- **BP3 — Route 53**: Domain Name Resolution at edge; DDoS protection mechanism
- **BP4 — API Gateway**: protect API endpoints; edge-optimized or regional mode
- **BP5 — VPC**: use security groups and NACLs to filter traffic
- **BP6 — ELB**: scales with traffic; distributes to many EC2 instances
- **BP7 — Auto Scaling**: scale EC2 to absorb DDoS traffic surges
- **BP8 — AWS Region isolation**: segregate workloads

---

### Amazon GuardDuty
- Intelligent threat discovery using ML, anomaly detection, 3rd party data
- One-click enable; 30-day trial; no software to install
- Input data sources:
  - CloudTrail Events Logs (unusual API calls, unauthorized deployments): Management Events + S3 Data Events
  - VPC Flow Logs (unusual internal traffic, unusual IP address)
  - DNS Logs (compromised EC2 instances sending encoded data in DNS queries)
  - Optional: EKS Audit Logs, RDS & Aurora, EBS, Lambda, S3 Data Events
- Set up **EventBridge rules** to be notified of findings → target Lambda or SNS
- Protects against **CryptoCurrency attacks** (dedicated finding type)

### Amazon Inspector
- Automated Security Assessments for:
  - **EC2 instances**: via SSM agent; analyze unintended network accessibility; analyze OS against known vulnerabilities
  - **Container Images pushed to ECR**: assessment as images are pushed
  - **Lambda Functions**: identifies vulnerabilities in function code and package dependencies; assessed as deployed
- Reports to and integrates with **AWS Security Hub**
- Sends findings to **Amazon EventBridge**
- **Only for**: EC2 instances, Container Images (ECR), Lambda functions
- Continuous scanning, only when needed
- Evaluates: package vulnerabilities (CVE database), network reachability (EC2)
- Risk score associated with all vulnerabilities for prioritization

### AWS Macie
- Fully managed data security and data privacy service
- Uses ML and pattern matching to discover and protect sensitive data in AWS
- Identifies and alerts on sensitive data such as **PII (Personally Identifiable Information)**
- Flow: S3 Buckets → Macie analyzes → notifies Amazon EventBridge → integrations (downstream actions)

---

## Key Configurations

### IAM
- Policy version: always `"2012-10-17"` (never use older versions)
- Groups cannot nest (no groups within groups)
- Permission Boundaries apply to users and roles ONLY (not groups)
- SCP does not apply to management account
- Default KMS Key Policy = complete access to root user

### KMS
- Symmetric keys: never exposed unencrypted; must call KMS API
- Customer Managed Keys: $1/month storage + $0.03/10,000 API calls
- AWS-managed keys: free, named `aws/service-name`
- Multi-Region keys: same key ID/material in different regions; managed independently

### SSM Parameter Store
- Standard tier: free, 10,000 params, 4 KB max
- Advanced tier: $0.05/param/month, 100,000 params, 8 KB max, supports parameter policies

### ACM
- Public certificates: free; auto-renews 60 days before expiry
- Imported certificates: NO auto-renewal; daily expiry events start 45 days before expiry
- Edge-Optimized API Gateway: ACM cert must be in us-east-1
- Cannot install ACM certificate on EC2

---

## Architectural Patterns

### Cross-Account Access
- Option 1: IAM Role as proxy (user gives up original permissions)
- Option 2: Resource-based policy (user keeps original permissions AND gets access)
- Use resource-based policy when user needs simultaneous access in both accounts

### SSM Parameter Store vs Secrets Manager
- **SSM Parameter Store**: config AND secrets; cheaper; no automatic rotation (can use Lambda+EventBridge manually); version tracking
- **Secrets Manager**: secrets only; automatic rotation built-in (Lambda); native RDS integration; more expensive; multi-region replication

### KMS Multi-Region Key Use Cases
- Global DynamoDB table with client-side field-level encryption
- Global Aurora with client-side column-level encryption
- Protecting sensitive fields (e.g., SSN) from database admins

### DDoS Defense Architecture (Layered)
```
Users → Route 53 (BP3) → Global Accelerator (BP1) → CloudFront + WAF (BP1+BP2)
→ ALB + WAF (BP2+BP6) → API Gateway (BP4) → Auto Scaling EC2 (BP7)
Security groups/NACLs (BP5) for subnet-level filtering
```

### Complete Security Stack for Web App
- CloudFront (CDN + DDoS) + WAF (L7 filtering) + ACM (TLS) + Shield (DDoS) → ALB → EC2/Lambda in private subnets
- GuardDuty (threat detection) + Inspector (vulnerability scanning) + Macie (PII in S3)
- KMS (encryption at rest) + Secrets Manager (credentials) + SSM Parameter Store (config)

### IAM Identity Center for Multi-Account SSO
- IAM Identity Center (in Management Account) + Permission Sets → SSO to all AWS accounts via AWS Organizations
- Identity source: Active Directory (AWS Managed or on-prem via AD Connector/trust) or built-in store

---

## Important Numbers & Limits

| Service | Metric | Value |
|---|---|---|
| WAF Web ACL | Max IPs per IP Set | 10,000 |
| Shield Advanced | Cost | $3,000/month/organization |
| GuardDuty | Free trial | 30 days |
| SSM Parameter Store Standard | Max parameters | 10,000 |
| SSM Parameter Store Advanced | Max parameters | 100,000 |
| SSM Parameter Store Standard | Max value size | 4 KB |
| SSM Parameter Store Advanced | Max value size | 8 KB |
| SSM Parameter Store Advanced | Storage cost | $0.05/param/month |
| KMS Customer Managed Key | Storage cost | $1/month |
| KMS Imported Key | Storage cost | $1/month |
| KMS API calls | Cost | $0.03 per 10,000 calls |
| KMS AWS-managed key | Auto rotation | Every 1 year |
| ACM | Auto-renew trigger | 60 days before expiry |
| ACM imported cert | Expiry notifications start | 45 days before expiry |
| CloudHSM | FIPS compliance level | 140-2 Level 3 |
| KMS | FIPS compliance level | 140-2 Level 3 |

---

## Diagram Descriptions

### IAM Users & Groups Diagram
- Three overlapping groups: Developers (Alice, Bob, Charles), Audit Team (Charles, David), Operations (David, Edward)
- Fred is outside all groups (standalone user)
- Charles belongs to both Developers and Audit Team; David belongs to both Audit Team and Operations

### IAM Policy Inheritance Diagram
- Developers group policy → inherited by Alice, Bob, Charles
- Audit Team policy → inherited by Charles, David
- Operations policy → inherited by David, Edward
- Fred has inline policy attached directly

### IAM Policy Evaluation Logic Flowchart
- Decision starts with Deny → evaluate explicit Deny → check SCP → check resource-based policy → check identity-based policy → check permission boundaries → check session policies → final Allow or Deny

### KMS Copying Snapshots Across Regions
- eu-west-2: EBS Volume (KMS Key A) → Snapshot (KMS Key A)
- Snapshot travels to ap-southeast-2; KMS ReEncrypt with KMS Key B
- ap-southeast-2: Snapshot (KMS Key B) → new EBS Volume (KMS Key B)

### KMS Multi-Region Keys
- Primary key in us-east-1 (mrk-1234abcd...) syncs to replicas in us-west-2, eu-west-1, ap-southeast-2
- Same key ID in all regions; each replica managed independently
- ARN shows different region but same key suffix

### GuardDuty Architecture
- Input: VPC Flow Logs + CloudTrail Logs + DNS Logs (+ optional: S3 Logs, EBS, Lambda, RDS/Aurora, EKS Audit Logs)
- GuardDuty analyzes → findings sent to EventBridge → EventBridge triggers SNS (notify admin) or Lambda (auto-remediate)

### IAM Identity Center Architecture
- Browser logs in → IAM Identity Center (Permission Sets) → SSO to: AWS Organization accounts, Business Cloud Apps (Salesforce, Box, Slack, Microsoft 365, Dropbox), Custom SAML2.0 apps
- Identity store: Active Directory OR built-in Identity Center store

### AWS Organizations OU Hierarchy
- Root OU → Management Account + OU (Dev) + OU (Prod)
- OU (Dev): Member Accounts
- OU (Prod): direct Member Accounts + OU (HR) + OU (Finance) each with their own member accounts

### SCP Hierarchy Diagram
- Root OU: FullAWSAccess applied; Deny Athena applied
- Management Account: can do anything (SCPs don't apply)
- Sandbox OU: FullAWSAccess + Deny S3; Account A also has FullAWSAccess + Deny EC2
  - Account A result: can do everything EXCEPT S3 and EC2
  - Account B & C: can do everything EXCEPT S3
- Workloads OU: FullAWSAccess; Test OU + Prod OU inherit
  - Account D (Test OU, Allow EC2): can access EC2
  - Account E & F (Prod OU, FullAWSAccess): can do anything

### DDoS Best Practices Architecture
- Full architecture: Users → Route 53 → AWS WAF + CloudFront/Global Accelerator → Region (VPC) → ALB + WAF → Auto Scaling EC2 → AWS Transit Gateway (to corporate data center via DX/VPN)
- Defense points labeled BP1-BP8

---

## Exam-Relevant Details

### IAM Tricky Distinctions
- **Groups cannot contain other groups** — only users
- **SCP does NOT apply to management account** — always full admin
- **Permission Boundaries apply to users and roles ONLY** — not groups
- **Assuming a role = give up original permissions**; resource-based policy = keep original permissions
- **IAM is global** — not regional
- `s3:ListBucket` → bucket ARN (no wildcard); `s3:GetObject` → object ARN (with `/*`)

### KMS Tricky Distinctions
- **KMS key is REGIONAL** — cannot be directly used across regions
- **Multi-Region Keys are NOT global** — they are independent replicas; just same key material
- **SSE-S3 replicated by default**; **SSE-KMS requires explicit configuration** for replication
- **Symmetric KMS keys**: never see the key unencrypted — must use API
- **AWS Managed Keys**: free; named `aws/service-name`; auto-rotate yearly
- **Customer Managed Keys**: $1/month; rotation must be enabled
- **Imported Keys**: only manual rotation using alias
- **CloudHSM vs KMS**: CloudHSM = single-tenant hardware, you manage keys entirely; KMS = multi-tenant software, AWS manages

### SSM vs Secrets Manager
- **SSM Parameter Store**: cheaper; config + secrets; no built-in auto-rotation; version tracking
- **Secrets Manager**: secrets only; built-in auto-rotation (Lambda); native RDS integration; more expensive; multi-region replication

### ACM Critical Facts
- **Free for public certs** on ELB, CloudFront, API Gateway
- **Cannot deploy ACM certs to EC2**
- **Imported certs = no auto-renewal** (daily expiry events start 45 days before expiry)
- **ACM for Edge-Optimized API Gateway**: cert MUST be in us-east-1
- **ACM for Regional API Gateway**: cert must be in same region as API stage

### WAF vs Shield vs Firewall Manager
- **WAF**: Layer 7 protection, SQL injection, XSS, geo-blocking, rate limiting; NOT for NLB
- **Shield Standard**: free, automatic, Layer 3/4 only
- **Shield Advanced**: $3,000/month; L7 auto-mitigation; DRP team; EC2, ELB, CloudFront, Global Accelerator, Route 53
- **Firewall Manager**: multi-account WAF/Shield management via Organizations

### GuardDuty vs Inspector vs Macie
- **GuardDuty**: account-level threat detection; analyzes CloudTrail + VPC Flow Logs + DNS Logs; ML-based; finds unusual behavior
- **Inspector**: vulnerability assessment for EC2 (via SSM agent), ECR container images, Lambda functions; CVE database; network reachability
- **Macie**: S3 PII detection only; ML + pattern matching

### Common Exam Keywords
- "Rotate secrets automatically" → Secrets Manager
- "Store config and secrets, version tracking" → SSM Parameter Store
- "Encryption across regions without re-encrypt" → KMS Multi-Region Keys
- "Single-tenant hardware encryption" → CloudHSM
- "TLS certificate on EC2" → CANNOT use ACM (use third-party cert)
- "FIPS 140-2 Level 3" → both KMS and CloudHSM qualify
- "Centralized multi-account SSO" → IAM Identity Center
- "Restrict all accounts in org from using a service" → SCP
- "Management account immune to SCP" → always true
- "DDoS Layer 3/4 protection free" → Shield Standard (automatic)
- "DDoS Layer 7 protection" → Shield Advanced + WAF
- "Detect PII in S3" → Macie
- "Detect cryptocurrency mining" → GuardDuty
- "Compliance scanning, CVE vulnerabilities" → Amazon Inspector
- "Fixed IP + WAF" → Global Accelerator + ALB + WAF (WAF can't attach to NLB)
- "Block specific countries" → WAF geo-match rules
- "Inline policy" → policy attached directly to user (not via group)
- "Resource-based policy" → principal keeps own permissions (cross-account without role assumption)
