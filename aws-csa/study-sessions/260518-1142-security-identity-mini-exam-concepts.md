# Security & Identity — Mini Exam: Concepts (Phase 2)
**Date:** 2026-05-18 11:42
**Score:** 9/10 (90%)
**Scope:** concepts — test conceptual knowledge from concept-mapper

---

## Questions & Results

### Q1 ✅ — IAM Policy Structure (iam-policy-structure)
**Question:** A solutions architect needs to understand Identity and Access Management (IAM) policy structure. Which element within an IAM policy statement specifies whether access is granted or denied?

A) Principal — defines the account, user, or role the policy applies to
B) Effect — specifies Allow or Deny for the policy statement
C) Action — lists the specific API operations the policy covers
D) Condition — defines circumstances under which the policy is in effect

**Your answer: B** — Correct. The Effect element specifies either Allow or Deny. Principal identifies who the policy applies to. Action lists API operations. Condition adds optional constraints.

---

### Q2 ✅ — SCP Region Restriction (scp)
**Question:** A company wants to enforce that no AWS account in their organization can launch Amazon Elastic Compute Cloud (EC2) instances in regions outside of `us-east-1` and `eu-west-1`. The restriction must apply to all accounts except the management account. Which approach should the solutions architect use?

A) Create an Identity and Access Management (IAM) policy denying EC2 actions in other regions and attach it to all IAM users across accounts
B) Apply a Service Control Policy (SCP) with an `aws:RequestedRegion` condition to the root Organizational Unit (OU)
C) Configure AWS Config rules to detect and auto-remediate non-compliant EC2 launches in restricted regions
D) Set up an Identity and Access Management (IAM) Permission Boundary on all roles in every account restricting region access

**Your answer: B** — Correct. SCPs with aws:RequestedRegion at the root OU restrict all member accounts and by design don't apply to the management account. A is impractical at scale. C is detective not preventive. D requires manual setup per role.

---

### Q3 ✅ — KMS Symmetric Keys (kms)
**Question:** Which statement accurately describes AWS Key Management Service (KMS) symmetric encryption keys?

A) Symmetric keys consist of a public/private key pair, and the public key can be downloaded for external encryption
B) Symmetric keys use a single AES-256 key that is never exposed unencrypted — all operations require calling the KMS API
C) Symmetric keys are free for all customer-managed keys, with charges only for API calls exceeding 10,000 per month
D) Symmetric keys can only be used within the region they were created in and cannot be replicated to other regions under any configuration

**Your answer: B** — Correct. KMS symmetric keys use a single AES-256 key never accessed unencrypted. A describes asymmetric keys. C is wrong — CMKs cost $1/month. D is wrong — Multi-Region Keys allow replication.

---

### Q4 ✅ — Secrets Manager for RDS (secrets-manager)
**Question:** A developer needs to store database credentials for an Amazon Relational Database Service (RDS) instance and have them automatically rotated every 30 days. Which AWS service is the BEST fit?

A) AWS Systems Manager (SSM) Parameter Store with an Advanced tier parameter and an Amazon EventBridge rule triggering an AWS Lambda function
B) AWS Secrets Manager with native RDS integration and automatic rotation via Lambda
C) AWS Key Management Service (KMS) Customer Managed Key with automatic key rotation enabled
D) AWS Systems Manager (SSM) Parameter Store Standard tier with version tracking and manual update scripts

**Your answer: B** — Correct. Secrets Manager is purpose-built for secret rotation with native RDS integration. A requires custom setup. C rotates encryption keys not credentials. D has no auto-rotation.

---

### Q5 ❌ — ACM Certificates (acm)
**Question:** A company wants to deploy TLS certificates for their Application Load Balancer (ALB) and Amazon CloudFront distribution. They want automatic renewal and zero cost for the certificates. Which statements about AWS Certificate Manager (ACM) are correct? (Select TWO)

A) ACM public TLS certificates are free and support automatic renewal 60 days before expiry
B) ACM certificates can be deployed directly onto Amazon Elastic Compute Cloud (EC2) instances for end-to-end TLS termination
C) For an Edge-Optimized API Gateway, the ACM certificate must be provisioned in the `us-east-1` region
D) ACM imported certificates receive the same automatic renewal as ACM-issued public certificates

**Your answer: A, D** — Incorrect. Correct answers: A, C. A is correct (free public certs, auto-renew 60 days). C is correct (Edge-Optimized API GW uses CloudFront, requires us-east-1). B is wrong — cannot deploy ACM certs on EC2. D is wrong — imported certificates do NOT get auto-renewal; ACM sends expiry notifications starting 45 days before expiry.

---

### Q6 ✅ — Permission Boundaries (iam-permission-boundaries)
**Question:** An administrator is configuring Identity and Access Management (IAM) Permission Boundaries. To which IAM entities can Permission Boundaries be applied?

A) Users, roles, and groups — all IAM entity types support Permission Boundaries
B) Users and roles only — groups do NOT support Permission Boundaries
C) Roles and groups only — individual users must use inline policies instead
D) Only roles — Permission Boundaries are designed exclusively for service roles and cross-account access

**Your answer: B** — Correct. Permission Boundaries apply to users and roles only, NOT groups. Effective permissions = intersection of Permission Boundary, Identity-based policy, and SCP.

---

### Q7 ✅ — IAM Roles vs Resource-Based Policies (iam-roles-vs-resource-policies)
**Question:** What is the primary difference between assuming an Identity and Access Management (IAM) role and using a resource-based policy for cross-account access?

A) IAM roles support Multi-Factor Authentication (MFA) conditions while resource-based policies do not
B) When assuming a role, the principal gives up their original permissions; with a resource-based policy, the principal retains their original permissions AND gains access to the resource
C) Resource-based policies work only for Simple Storage Service (S3) buckets, while IAM roles work for all AWS services
D) Assuming a role is free, while resource-based policies incur additional Identity and Access Management (IAM) API charges per evaluation

**Your answer: B** — Correct. Role assumption = give up original permissions. Resource-based policy = keep original permissions AND gain access. Critical for simultaneous cross-account access.

---

### Q8 ✅ — Amazon Macie (macie)
**Question:** Which AWS service uses Machine Learning (ML) and pattern matching to discover and alert on Personally Identifiable Information (PII) stored in Amazon Simple Storage Service (S3) buckets?

A) Amazon GuardDuty — intelligent threat discovery analyzing CloudTrail, Virtual Private Cloud (VPC) Flow Logs, and Domain Name System (DNS) Logs
B) Amazon Inspector — automated security assessment for EC2 instances, container images, and Lambda functions
C) Amazon Macie — fully managed data security service using ML to identify sensitive data in S3
D) AWS Config — resource configuration tracking and compliance monitoring service

**Your answer: C** — Correct. Macie is purpose-built for PII/sensitive data detection in S3. GuardDuty detects threats. Inspector scans for CVE vulnerabilities. Config tracks resource compliance.

---

### Q9 ✅ — CloudHSM vs KMS (cloudhsm)
**Question:** A security engineer is comparing AWS CloudHSM and AWS Key Management Service (KMS). Which characteristic is unique to CloudHSM compared to KMS?

A) CloudHSM supports Symmetric and Asymmetric encryption, while KMS only supports Symmetric keys
B) CloudHSM provides single-tenant dedicated hardware where customers manage their own encryption keys entirely
C) CloudHSM integrates with CloudTrail for audit logging, while KMS does not support any audit trail
D) CloudHSM is available in the AWS Free Tier, while KMS requires a paid subscription for all key types

**Your answer: B** — Correct. CloudHSM = single-tenant dedicated hardware, customer manages keys entirely. Both support symmetric+asymmetric. Both integrate with CloudTrail. CloudHSM has NO free tier.

---

### Q10 ✅ — WAF Deployment Targets (waf)
**Question:** An organization uses AWS Web Application Firewall (WAF) to protect their web application. On which AWS resource can WAF NOT be deployed?

A) Application Load Balancer (ALB)
B) Amazon CloudFront distribution
C) Network Load Balancer (NLB)
D) Amazon API Gateway

**Your answer: C** — Correct. WAF operates at Layer 7 (HTTP) and does not support NLB (Layer 4 TCP/UDP). WAF supports: ALB, CloudFront, API Gateway, AppSync, Cognito User Pool.

---

## Summary
- **Score:** 9/10 (90%)
- **Missed topics:** acm
- **Strong areas:** iam-policy-structure, scp, kms, secrets-manager, iam-permission-boundaries, iam-roles-vs-resource-policies, macie, cloudhsm, waf
- **Key lessons:**
  - ACM imported certificates do NOT auto-renew — only ACM-issued public certificates get automatic renewal
  - For Edge-Optimized API Gateway, ACM certificate must be in us-east-1 (because it uses CloudFront under the hood)
