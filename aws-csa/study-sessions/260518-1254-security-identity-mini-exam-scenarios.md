# Security & Identity — Mini Exam: Scenarios (Phase 4)
**Date:** 2026-05-18 12:54
**Score:** 8/10 (80%)
**Scope:** scenarios — test scenario reasoning from scenario-generator

---

## Questions & Results

### Q1 ✅ — Cross-Account Access with Resource-Based Policy (iam / cross-account-access)
**Question:** A multinational bank runs workloads across two AWS accounts. Account A hosts a central Amazon DynamoDB audit log table. Account B runs a compliance Lambda function that must read from the DynamoDB table in Account A while simultaneously writing compliance reports to an Amazon Simple Storage Service (S3) bucket in Account B. Which approach enables this?

A) Create an Identity and Access Management (IAM) role in Account A with DynamoDB read permissions; the Lambda function assumes this role to read audit logs, then uses its own execution role to write to S3 in Account B
B) Attach a resource-based policy to the DynamoDB table in Account A granting the Lambda execution role in Account B read access; the Lambda retains its Account B permissions for S3 writes
C) Create IAM users with access keys in both accounts and embed them in the Lambda function's environment variables
D) Use AWS IAM Identity Center to grant the Lambda function Single Sign-On (SSO) access to both accounts simultaneously

**Your answer: B** — Correct. Resource-based policy lets principal keep original permissions in both accounts simultaneously. Assuming a role (A) means giving up original permissions. Access keys (C) are insecure. Identity Center (D) is for human SSO, not Lambda.

---

### Q2 ✅ — Permission Boundaries for Delegated Administration (iam / permission-boundaries)
**Question:** A startup's CTO wants development team leads to create IAM roles for their teams but is concerned about privilege escalation. The security team wants to ensure any role a team lead creates cannot exceed permissions defined in `DevTeamBoundary`. Which configuration achieves this?

A) Create a Service Control Policy (SCP) at the Organizational Unit (OU) level restricting the `iam:CreateRole` action to only allow roles with specific policy ARNs
B) Require team leads to include a condition in their `iam:CreateRole` permission that mandates the `DevTeamBoundary` policy as a Permission Boundary on every new role
C) Create an AWS Config rule that detects roles without the `DevTeamBoundary` boundary and auto-deletes them
D) Replace team leads' `AdministratorAccess` with a custom policy that only allows creating roles with specific policy ARNs attached

**Your answer: B** — Correct. IAM policy condition on CreateRole requiring Permission Boundary prevents escalation preventively. SCP (A) can't control role creation parameters. Config (C) is reactive. Replacing access (D) doesn't enforce boundaries on created roles.

---

### Q3 ✅ — SCP Allowlist Inheritance (scp / inheritance)
**Question:** A company's AWS Organization has Root OU (FullAWSAccess) → Production OU (Allow: ec2, s3, rds, cloudwatch only). A new account in Production OU has IAM user with `AdministratorAccess`. Can the developer create a DynamoDB table?

A) Yes — AdministratorAccess overrides SCP
B) No — Production OU's allowlist SCP does not include DynamoDB, denied regardless of IAM policy
C) Yes — Root OU FullAWSAccess flows down through hierarchy
D) Depends on account-level SCP

**Your answer: B** — Correct. SCPs set maximum permissions ceiling. Effective permissions = intersection of SCP and IAM policy. DynamoDB not in allowlist = denied. IAM policies cannot override SCPs. Root FullAWSAccess doesn't bypass child OU restrictions.

---

### Q4 ✅ — KMS Customer Managed Key Requirements (kms / cmk-vs-managed)
**Question:** Healthcare company needs: CloudTrail audit of encryption ops, key disable on breach, annual auto-rotation. Which KMS key type?

A) AWS Managed Key (aws/s3) — free, auto-rotate, CloudTrail, can disable
B) Customer Managed Key — $1/month, configurable rotation, full control including disable/delete
C) AWS Owned Key (SSE-S3) — built-in rotation, S3 access logging, bucket policy revocation
D) Imported Key Material — CloudTrail, disable capability, auto-rotation after import

**Your answer: B** — Correct. CMK provides all three: CloudTrail audit, disable/delete capability, configurable auto-rotation. AWS Managed Keys (A) can't be disabled. AWS Owned Keys (C) are invisible to customer. Imported Keys (D) only support manual rotation.

---

### Q5 ❌ — ACM Certificate Regional Requirements (acm)
**Question:** Company needs ACM certs for ALB and Edge-Optimized API Gateway. Where must certificates be provisioned? (Select TWO)

A) ACM certificate for ALB must be in the same region as the ALB
B) ACM certificate for Edge-Optimized API Gateway must be in us-east-1
C) ACM certificate for ALB can be in any region (cross-region loading)
D) ACM certificate for Edge-Optimized API Gateway must be in same region as API stage

**Your answer: B, D** — Incorrect. Correct answers: A, B. ALB requires cert in same region (A). Edge-Optimized API GW uses CloudFront, requires us-east-1 (B). ALB does NOT support cross-region cert loading (C wrong). The "same region as stage" rule applies to Regional API Gateway, not Edge-Optimized (D wrong).

---

### Q6 ✅ — GuardDuty Cryptocurrency Detection (guardduty)
**Question:** Detect EC2 cryptocurrency mining without agents, with automated isolation. Which architecture?

A) Inspector scanning for crypto software → EventBridge → Lambda
B) GuardDuty analyzing VPC Flow Logs + CloudTrail + DNS → EventBridge → Lambda (SG isolation)
C) CloudWatch custom metrics + SSM Automation
D) Macie scanning EC2 metadata for wallet addresses

**Your answer: B** — Correct. GuardDuty has dedicated CryptoCurrency finding type, agentless (one-click enable), analyzes VPC Flow Logs + CloudTrail + DNS Logs via ML. Inspector (A) scans for CVEs not runtime behavior. CloudWatch (C) requires manual pattern definition. Macie (D) only scans S3 contents.

---

### Q7 ✅ — SSM Parameter Store vs Secrets Manager (ssm-vs-secrets-manager)
**Question:** Store RDS Aurora creds with 60-day auto-rotation + feature flags (free). Most cost-effective?

A) Everything in Secrets Manager
B) Secrets Manager (creds with rotation) + SSM Parameter Store Standard (free config)
C) Everything in SSM Advanced with Lambda rotation
D) CloudHSM (creds) + SSM Standard (config)

**Your answer: B** — Correct. Hybrid: Secrets Manager for RDS creds (native rotation), SSM Standard (free) for config/feature flags. Everything in Secrets Manager (A) is unnecessarily expensive. SSM has no built-in rotation (C). CloudHSM is encryption hardware, not secret storage (D).

---

### Q8 ❌ — Shield Standard vs Advanced (shield)
**Question:** Protect ALB web app from SQL injection, XSS, and L7 DDoS floods. Need 24/7 DDoS experts and cost protection. Which combination?

A) WAF on ALB + Shield Standard
B) WAF on ALB + Shield Advanced (L7 auto-mitigation, DRT, cost protection)
C) Network Firewall + Shield Standard
D) WAF on NLB + Shield Advanced

**Your answer: A** — Incorrect. Correct answer: B. Shield Standard only provides L3/4 protection (free, automatic) — NO L7 mitigation, NO DRT, NO cost protection. Shield Advanced ($3K/month) adds all three. WAF can't deploy on NLB (D). Network Firewall lacks WAF's HTTP rules (C).

---

### Q9 ✅ — Cognito User Pools + Identity Pools (cognito)
**Question:** Mobile app needs email/password auth + temporary AWS credentials for S3 uploads. Which Cognito configuration?

A) User Pool alone — JWT tokens exchange directly for AWS creds
B) Identity Pool alone — handles sign-up + credential vending
C) User Pool (auth → JWT) + Identity Pool (exchange JWT → temp AWS creds via IAM role)
D) User Pool + STS AssumeRoleWithWebIdentity from mobile app

**Your answer: C** — Correct. User Pools handle authentication (JWT tokens). Identity Pools handle authorization (exchange tokens for AWS credentials). User Pools alone (A) don't issue AWS creds. Identity Pools alone (B) don't handle sign-up. STS directly (D) adds unnecessary complexity.

---

### Q10 ✅ — Macie for PII Discovery (macie)
**Question:** Detect PII (credit cards, SSNs) across hundreds of S3 buckets with ongoing automated scanning and alerts. Which service?

A) GuardDuty with S3 Data Events
B) Inspector with S3 scanning
C) Macie using ML + pattern matching → EventBridge alerts
D) Config rules checking S3 encryption/policies

**Your answer: C** — Correct. Macie is purpose-built for S3 PII/sensitive data discovery using ML and pattern matching. GuardDuty (A) detects access threats, not data content. Inspector (B) scans for CVE vulnerabilities, not S3 contents. Config (D) checks bucket configuration, not object data.

---

## Summary
- **Score:** 8/10 (80%)
- **Missed topics:** acm, shield
- **Strong areas:** iam (cross-account, permission-boundaries), scp, kms, guardduty, ssm-vs-secrets-manager, cognito, macie
- **Key lessons:**
  - ACM for ALB: cert must be in same region as ALB. Edge-Optimized API GW: cert must be in us-east-1. Regional API GW: cert in same region as API stage. These are three distinct rules.
  - Shield Standard = free, automatic, L3/4 only. Shield Advanced = $3K/month, adds L7 auto-mitigation + 24/7 DRT + cost protection. Keywords "DDoS experts" or "cost protection during attacks" → always Shield Advanced.
