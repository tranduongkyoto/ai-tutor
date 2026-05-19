# Security & Identity — Mini Exam: Design (Phase 5)
**Date:** 2026-05-19 09:53
**Score:** 7/10 (70%)
**Scope:** design — architecture design decisions and multi-service trade-offs

---

## Questions & Results

### Q1 ✓ — ACM Certificate Placement for ALB + Edge-Optimized API Gateway (acm)
**Question:** A financial services company runs a multi-region application with an Application Load Balancer (ALB) in eu-west-1 and an edge-optimized Amazon API Gateway in front of a microservices backend. They need Transport Layer Security (TLS) certificates managed through AWS Certificate Manager (ACM) for both endpoints. The security team requires centralized certificate management with automatic renewal. How should the solutions architect configure the TLS certificates?

A) Provision one ACM certificate in eu-west-1 with both domain names; attach it to the ALB and the API Gateway
B) Provision an ACM certificate in eu-west-1 for the ALB and a separate ACM certificate in us-east-1 for the edge-optimized API Gateway
C) Provision an ACM certificate in us-east-1 for both the ALB and the edge-optimized API Gateway since edge-optimized requires us-east-1
D) Import a third-party wildcard certificate into ACM in us-east-1 and attach it to both the ALB and the API Gateway for centralized management

**Your answer: B** — Correct. Edge-optimized API Gateway uses CloudFront, requiring ACM cert in us-east-1. ALB cert must be in ALB's region (eu-west-1). Two separate certs needed.

---

### Q2 ✓ — Shield Advanced + WAF for L7 DDoS (shield)
**Question:** A SaaS company hosts a public-facing web application behind an Application Load Balancer (ALB). They experience frequent Layer 7 Distributed Denial of Service (DDoS) attacks that bypass AWS Shield Standard protections. The CTO wants automated Layer 7 mitigation, cost protection during attack-related traffic spikes, and access to a dedicated AWS response team. The company also uses Amazon CloudFront and Amazon Route 53. Which combination provides the required protections?

A) Enable AWS Shield Advanced on the ALB, CloudFront, and Route 53; attach AWS Web Application Firewall (WAF) Web Access Control Lists (ACLs) to CloudFront and the ALB for rate-based rules
B) Enable AWS Shield Standard (already active) and add AWS WAF with rate-based rules on the ALB; use Amazon CloudWatch alarms to notify the operations team during attacks
C) Deploy AWS Network Firewall in front of the ALB for Layer 7 inspection; enable AWS Shield Standard for Layer 3/4 protection
D) Enable AWS Shield Advanced on CloudFront only; use AWS Firewall Manager to propagate WAF rules across all accounts in the organization

**Your answer: A** — Correct. Shield Advanced on ALB, CloudFront, Route 53 provides automated L7 DDoS mitigation, cost protection, and 24/7 DRT access. WAF Web ACLs add granular L7 filtering.

---

### Q3 ✓ — CloudHSM-backed KMS for FIPS 140-2 Level 3 (kms / cloudhsm)
**Question:** A healthcare company stores patient records in Amazon Simple Storage Service (S3). Regulatory compliance requires that: (1) encryption keys must be managed exclusively by the company with full control over key lifecycle, (2) the encryption solution must meet FIPS 140-2 Level 3, and (3) the company must be able to audit all key usage. The application team wants to use server-side encryption with Amazon S3. Which encryption approach satisfies all requirements?

A) Use Server-Side Encryption with AWS Key Management Service (SSE-KMS) with an AWS managed key (`aws/s3`) and enable AWS CloudTrail for key usage auditing
B) Use Server-Side Encryption with customer-provided keys (SSE-C) where the application manages keys in an on-premises Hardware Security Module (HSM)
C) Use Server-Side Encryption with AWS KMS (SSE-KMS) using a Customer Managed Key (CMK) stored in an AWS CloudHSM-backed KMS Custom Key Store
D) Use Server-Side Encryption with Amazon S3 managed keys (SSE-S3) and enable S3 server access logging for audit compliance

**Your answer: C** — Correct. KMS Custom Key Store backed by CloudHSM = company-exclusive key control, FIPS 140-2 Level 3, CloudTrail auditing. Best of both worlds: SSE-KMS simplicity + CloudHSM security.

---

### Q4 ✓ — SCP + Permission Boundaries for Multi-Account Control (scp / permission-boundaries)
**Question:** A multinational company with 200+ AWS accounts uses AWS Organizations. The security team needs to: (1) enforce a policy preventing any account from launching resources outside approved regions (us-east-1, eu-west-1), (2) allow the management account to operate without restriction, and (3) ensure new accounts automatically inherit the restriction. A junior administrator should be allowed to create IAM roles for their team but cannot escalate permissions beyond what they've been granted. Which combination of controls achieves this? (Select TWO)

A) Attach a Service Control Policy (SCP) to the root Organizational Unit (OU) with an explicit Deny on all actions where `aws:RequestedRegion` is not us-east-1 or eu-west-1
B) Create an IAM policy in each account that denies actions outside approved regions and attach it to all IAM users and roles
C) Assign the junior administrator an IAM Permission Boundary that limits the maximum permissions they can grant when creating new roles
D) Use AWS Control Tower preventive guardrails to restrict regions, which applies SCPs that automatically exclude the management account

**Your answer: A, C** — Correct. SCP on root OU restricts all member accounts (management account exempt by design). Permission Boundary limits what the junior admin can delegate.

---

### Q5 ✓ — IAM Identity Center with AWS Managed AD (iam-identity-center)
**Question:** A company is migrating to a multi-account AWS environment. They need single sign-on for 500 employees accessing 15 AWS accounts and 3 SaaS applications (Salesforce, Slack, Microsoft 365). Employee identities are managed in an on-premises Microsoft Active Directory (AD). The solution must minimize operational overhead while supporting attribute-based access control for fine-grained permissions. Which architecture should the solutions architect recommend?

A) Create IAM users in each AWS account mapped to Active Directory users; use SAML 2.0 federation directly between Active Directory Federation Services (ADFS) and each account
B) Set up AWS IAM Identity Center with AWS Managed Microsoft Active Directory (AD), establish a two-way trust with the on-premises AD, and configure Permission Sets with attribute-based access control (ABAC)
C) Deploy an AD Connector in AWS to proxy authentication to the on-premises AD and create individual IAM roles in each account for each employee
D) Set up AWS IAM Identity Center with a built-in identity store, manually sync all 500 users from on-premises AD, and configure Permission Sets for each account

**Your answer: B** — Correct. IAM Identity Center + AWS Managed AD with two-way trust to on-prem AD provides SSO to AWS accounts + SaaS apps, ABAC support, and minimal overhead.

---

### Q6 ✗ — KMS Multi-Region Keys + DynamoDB Global Tables (kms-multi-region-keys)
**Question:** A company runs a global e-commerce application with Amazon DynamoDB Global Tables storing customer data including Social Security Numbers (SSNs) encrypted client-side. The application must: (1) encrypt SSN fields before writing to DynamoDB, (2) decrypt SSN fields locally in each region without cross-region KMS API calls, and (3) ensure database administrators cannot read SSN values even with full DynamoDB access. Which encryption design meets all requirements?

A) Enable DynamoDB encryption at rest with an AWS managed KMS key (`aws/dynamodb`) and restrict DynamoDB table access using IAM policies that deny `GetItem` on the SSN attribute
B) Use the Amazon DynamoDB Encryption Client with KMS Multi-Region Keys (MRK) to encrypt SSN fields client-side before writing to DynamoDB; replicate the MRK to all Global Table regions
C) Use Server-Side Encryption (SSE) with a Customer Managed Key (CMK) in KMS for DynamoDB table encryption and create separate CMKs in each region for the Global Table replicas
D) Encrypt SSN values in the application using AWS CloudHSM before writing to DynamoDB; deploy CloudHSM clusters in every region where Global Tables are replicated

**Your answer: C** — Incorrect. Correct answer: B. SSE with CMK encrypts entire table server-side — DynamoDB decrypts transparently on read, so admins still see plaintext. DynamoDB Encryption Client + MRK provides client-side field-level encryption with local decryption in each region.

---

### Q7 ✓ — GuardDuty for Cryptocurrency Detection + Auto-Remediation (guardduty)
**Question:** A media company needs to detect and respond to potential security threats across 50 AWS accounts in their Organization. They require: (1) centralized threat detection across all accounts, (2) automatic notification when cryptocurrency mining is detected on any EC2 instance, and (3) automated remediation that isolates compromised instances. Which architecture provides this?

A) Enable Amazon Inspector across all accounts via AWS Organizations delegated administrator; configure Amazon EventBridge rules to trigger AWS Lambda functions that modify Security Groups (SGs) on compromised instances
B) Enable Amazon GuardDuty with a delegated administrator account; configure EventBridge rules in the admin account to match GuardDuty cryptocurrency findings and trigger a Lambda function that replaces the instance's Security Group with an isolation SG allowing no inbound/outbound traffic
C) Deploy Amazon Macie across all accounts to detect unusual API activity; use AWS Step Functions to orchestrate remediation workflows that terminate compromised instances
D) Enable AWS CloudTrail in all accounts with centralized logging to an S3 bucket; use Amazon Athena queries scheduled via EventBridge to detect cryptocurrency-related API patterns and trigger SNS notifications

**Your answer: B** — Correct. GuardDuty has dedicated cryptocurrency finding type, supports multi-account via delegated admin, EventBridge triggers Lambda to isolate via SG replacement.

---

### Q8 ✓ — Secrets Manager + SSM Parameter Store Hybrid (ssm-parameter-store / secrets-manager)
**Question:** A company stores sensitive configuration data and database credentials for a microservices application. Requirements: (1) database credentials for Amazon RDS must rotate automatically every 30 days, (2) non-sensitive configuration values (feature flags, endpoint URLs) need version tracking at minimal cost, (3) the application runs in 3 AWS Regions for disaster recovery. Which design optimally addresses all three requirements?

A) Store all configuration and credentials in AWS Secrets Manager with automatic rotation enabled; replicate secrets to all 3 regions using Secrets Manager multi-region secrets
B) Store database credentials in AWS Secrets Manager with automatic rotation via Lambda; store configuration values in AWS Systems Manager (SSM) Parameter Store Standard tier with version tracking
C) Store everything in SSM Parameter Store Advanced tier with parameter policies for expiration-based rotation; use EventBridge to trigger Lambda for credential rotation
D) Store database credentials in AWS Secrets Manager with rotation; store configuration in SSM Parameter Store Advanced tier with parameter policies for change notifications across regions

**Your answer: B** — Correct. Secrets Manager for RDS auto-rotation (native integration). SSM Parameter Store Standard (free) for config with version tracking. Optimal cost split.

---

### Q9 ✗ — CloudFront → ALB Origin Restriction Pattern (waf / cloudfront)
**Question:** A company is designing a defense-in-depth security architecture for a web application. The application uses Amazon CloudFront, an Application Load Balancer (ALB) in a public subnet, and Amazon EC2 instances in private subnets. They need to: (1) block requests from specific countries, (2) rate-limit requests to prevent abuse, (3) protect against SQL injection, and (4) ensure only CloudFront can reach the ALB. Which layered architecture provides these protections?

A) Attach AWS WAF to CloudFront with geo-match rules, rate-based rules, and SQL injection rules; configure the ALB Security Group (SG) to only allow traffic from CloudFront's managed prefix list; add a custom HTTP header in CloudFront origin settings and validate it in the ALB listener rules
B) Attach AWS WAF to both CloudFront and the ALB with identical rule sets for geo-match, rate-limiting, and SQL injection; restrict the ALB SG to CloudFront IP ranges updated via Lambda
C) Use AWS Network Firewall in front of the ALB for geo-blocking and SQL injection inspection; attach AWS WAF to CloudFront for rate-limiting; restrict the ALB SG to the Network Firewall's Elastic Network Interfaces (ENIs)
D) Attach AWS WAF to CloudFront for all protections (geo-match, rate-limiting, SQL injection); use a Network Access Control List (NACL) on the ALB subnet to block non-CloudFront IP ranges

**Your answer: D** — Incorrect. Correct answer: A. NACLs can't handle CloudFront's dynamic, constantly-changing IP ranges (rule limit of 20). Use ALB SG with AWS-managed prefix list (`com.amazonaws.global.cloudfront.origin-facing`) + custom origin header for defense-in-depth.

---

### Q10 ✗ — Firewall Manager for Multi-Account WAF/Shield (firewall-manager)
**Question:** A company with a multi-account AWS Organization wants to ensure comprehensive security visibility. They need: (1) continuous compliance monitoring with automatic remediation for non-compliant resources, (2) centralized WAF rule management across all accounts, and (3) protection of all ELBs with AWS Shield Advanced. The solution must automatically apply security policies to newly created accounts. Which service should the solutions architect primarily use to orchestrate these requirements?

A) AWS Security Hub with AWS Config conformance packs for compliance, and manual WAF rule deployment per account via AWS CloudFormation StackSets
B) AWS Firewall Manager with security policies for WAF rules, Shield Advanced protections, and AWS Config rules — configured with automatic remediation and auto-applied to new Organization accounts
C) AWS Control Tower with preventive guardrails for WAF and Shield, and detective guardrails backed by AWS Config for compliance monitoring
D) AWS Organizations SCPs to enforce WAF attachment on all ALBs, combined with AWS Config rules in each account for compliance and EventBridge rules for remediation

**Your answer: C** — Incorrect. Correct answer: B. Firewall Manager is purpose-built for centralized multi-account WAF/Shield/SG policy management — auto-applies to new accounts and new resources. Control Tower manages governance (SCPs/Config guardrails), not WAF/Shield deployment.

---

## Summary
- **Score:** 7/10 (70%)
- **Missed topics:** kms-multi-region-keys, waf (CloudFront origin restriction), firewall-manager
- **Strong areas:** acm, shield, kms/cloudhsm, scp, permission-boundaries, iam-identity-center, guardduty, ssm-parameter-store, secrets-manager
- **Key lessons:**
  - KMS Multi-Region Keys + DynamoDB Encryption Client = client-side field-level encryption with local decryption per region; SSE encrypts server-side (admins still see plaintext)
  - CloudFront → ALB restriction uses AWS-managed prefix list + custom origin header; NACLs can't handle dynamic CloudFront IPs
  - Firewall Manager orchestrates multi-account WAF/Shield/SG policies with auto-apply to new accounts; Control Tower is governance, not security policy deployment
