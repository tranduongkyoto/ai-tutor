# Security & Identity — Scenario Generator (Phase 3)
**Date:** 2026-05-18 11:45
**Scenarios:** 11 (full scenario map coverage)

---

## Scenario 1: Cross-Account Access Pattern (iam / cross-account-access)

**Context:** A financial services company runs two AWS accounts — Account A (data warehouse with Amazon DynamoDB tables) and Account B (analytics application writing reports to Amazon Simple Storage Service / S3). A data engineer in Account B needs to scan DynamoDB tables in Account A and simultaneously write results to an S3 bucket in Account B.

**Requirements:** The engineer must retain permissions in both accounts simultaneously. Minimal operational overhead. No credential sharing.

**Question:** Which solution meets these requirements?

A) Create an Identity and Access Management (IAM) role in Account A with DynamoDB read permissions; have the engineer assume the role to scan data, then switch back to Account B to write to S3
B) Create an IAM user in Account A with access keys; embed the keys in the analytics application to access DynamoDB
C) Add a resource-based policy on the DynamoDB table in Account A granting the engineer's IAM principal in Account B access; the engineer keeps their Account B permissions
D) Set up AWS IAM Identity Center with Permission Sets for both accounts; the engineer signs in and manually switches between accounts

**Answer: C**
With a resource-based policy, the principal retains their original Account B permissions AND gains access to the DynamoDB table in Account A — enabling simultaneous access in both accounts. This is the key distinction from role assumption.

**Why others are wrong:**
- A) Assuming a role in Account A means giving up Account B permissions — can't write to S3 simultaneously
- B) Embedding access keys is insecure and violates best practices; credentials are shared and hard to rotate
- D) IAM Identity Center provides SSO portal access but doesn't enable simultaneous API-level access in both accounts within a single session

**Key Concept:** IAM role assumption vs resource-based policies for cross-account access

---

## Scenario 2: IAM Permission Boundaries for Delegated Administration (iam / permission-boundaries)

**Context:** A SaaS company wants to allow development team leads to create IAM roles for their team members. However, the security team needs to ensure no team lead can create a role with more privileges than their own — preventing privilege escalation.

**Requirements:** Team leads can self-service role creation. No privilege escalation possible. Minimal ongoing security team intervention.

**Question:** Which solution meets these requirements?

A) Create a Service Control Policy (SCP) at the Organizational Unit (OU) level restricting the `iam:CreateRole` action to only allow roles with specific policy ARNs
B) Attach an IAM Permission Boundary to each team lead's IAM user that caps the maximum permissions any role they create can have
C) Use AWS Config rules to detect overly permissive roles and automatically delete them after creation
D) Require all role creation requests to go through an approval workflow using AWS Service Catalog with predefined role templates

**Answer: B**
Permission Boundaries set the maximum permissions an IAM entity can receive. By attaching a boundary to the team lead's user, any role they create (if configured to require the same boundary) cannot exceed those limits — preventing privilege escalation without security team intervention.

**Why others are wrong:**
- A) SCPs restrict at the account/OU level, not individual IAM action parameters
- C) Detective, not preventive — overly permissive role exists briefly before remediation
- D) Works but adds significant operational overhead, blocking self-service

**Key Concept:** IAM Permission Boundaries for delegated administration without privilege escalation

---

## Scenario 3: SCP Inheritance and OU Design (organizations / scp-inheritance-and-ou-design)

**Context:** A multinational corporation has an AWS Organization: Root OU → Production OU → Regional OUs (US, EU, APAC). The security team wants Production accounts to ONLY use `ec2`, `s3`, `rds`, and `cloudwatch` services. Management account must retain full access.

**Requirements:** Strict service allowlist for Production. Management account unrestricted. New accounts automatically inherit restrictions.

**Question:** Which SCP strategy should the solutions architect implement?

A) Apply an SCP with explicit Deny statements for all services except `ec2`, `s3`, `rds`, and `cloudwatch` to the Root OU
B) Apply an Allowlist SCP that explicitly permits only `ec2`, `s3`, `rds`, and `cloudwatch` to the Production OU; keep the default FullAWSAccess on Root
C) Apply individual SCPs to each Regional OU denying specific services one by one
D) Remove the FullAWSAccess SCP from the Root OU and attach the allowlist SCP directly to each member account

**Answer: B**
An Allowlist SCP on the Production OU explicitly permits only the 4 allowed services. SCPs require explicit allows from root through each OU to the account. Management account is automatically exempt. New accounts inherit restrictions.

**Why others are wrong:**
- A) Applying to Root OU affects ALL accounts, not just Production
- C) Per-OU deny lists are error-prone and don't auto-block new services
- D) Removing FullAWSAccess from Root breaks the allow chain for all accounts

**Key Concept:** SCP allowlist strategy with OU hierarchy and management account exemption

---

## Scenario 4: SCP Deny vs Allow Strategy (scp / deny-vs-allow-strategy)

**Context:** A company's security team is debating SCP strategy. Some accounts need broad access with a few services blocked (development accounts). Other accounts need extremely restricted access with only specific services allowed (compliance-audited production accounts).

**Requirements:** Development accounts: block only DynamoDB and Redshift. Production accounts: allow only EC2, S3, RDS, Lambda. Both in same Organization.

**Question:** Which SCP approach correctly implements both requirements?

A) Apply a single Allowlist SCP to the Root OU covering both dev and prod requirements
B) Apply a Blocklist SCP (FullAWSAccess + explicit Deny for DynamoDB/Redshift) to the Dev OU; apply an Allowlist SCP (Allow only ec2/s3/rds/lambda) to the Prod OU
C) Apply Allowlist SCPs to both OUs — Dev OU allows everything except DynamoDB/Redshift, Prod OU allows only ec2/s3/rds/lambda
D) Apply Blocklist SCPs to both OUs with different deny lists — Dev denies DynamoDB/Redshift, Prod denies everything except ec2/s3/rds/lambda

**Answer: B**
Use different SCP strategies for different OUs: Blocklist (FullAWSAccess + targeted Deny) for Dev gives broad access minus specific services. Allowlist (explicit Allow only) for Prod gives strict access. Each OU gets the strategy that matches its security posture.

**Why others are wrong:**
- A) A single SCP at Root can't express different strategies for different OUs
- C) "Allow everything except X" isn't how Allowlist SCPs work — you'd need to explicitly list every other service
- D) Blocklist for Prod would require denying hundreds of services and would miss new services AWS adds

**Key Concept:** SCP Blocklist (broad access, deny specific) vs Allowlist (deny all, allow specific) — use per OU based on need

---

## Scenario 5: Customer Managed Key (CMK) vs AWS Managed Keys (kms / cmk-vs-aws-managed-keys)

**Context:** A healthcare company stores patient records in S3 and EBS. Compliance requires: annual key rotation, CloudTrail audit trail, ability to revoke access by disabling the key.

**Requirements:** Annual key rotation. CloudTrail audit. Key disable/revoke capability. Cost-effective.

**Question:** Which KMS key type meets ALL requirements?

A) AWS Owned Keys (SSE-S3) — free, managed entirely by AWS
B) AWS Managed Keys (`aws/s3`, `aws/ebs`) — free, auto-rotate yearly, CloudTrail auditable
C) Customer Managed Keys (CMK) — $1/month, configurable rotation, full access control including disable/delete
D) Imported Key Material — $1/month, manual rotation only, full lifecycle control

**Answer: C**
Customer Managed Keys meet all three: configurable automatic rotation, CloudTrail audit, and ability to disable/schedule deletion. AWS Managed Keys lack disable/revoke.

**Why others are wrong:**
- A) AWS Owned Keys — no CloudTrail visibility, no rotation control, cannot disable
- B) AWS Managed Keys — auditable and auto-rotate but CANNOT be disabled or deleted
- D) Imported keys — only manual rotation, adding operational overhead

**Key Concept:** KMS key categories — CMK provides maximum control

---

## Scenario 6: KMS Key Rotation (kms / key-rotation)

**Context:** A company uses three types of KMS keys: AWS Managed Keys for RDS, Customer Managed Keys for S3, and Imported Keys for a legacy application. The CISO wants to understand the rotation capabilities of each.

**Requirements:** Understand which keys auto-rotate, which require manual rotation, and the rotation period.

**Question:** Which statement correctly describes KMS key rotation across all three key types?

A) All three key types support automatic rotation every 1 year by default
B) AWS Managed Keys auto-rotate yearly; Customer Managed Keys support automatic and on-demand rotation (must be enabled); Imported Keys support only manual rotation using aliases
C) Customer Managed Keys auto-rotate yearly by default; AWS Managed Keys and Imported Keys require manual rotation
D) All key types support on-demand rotation triggered via the KMS API; the rotation period is configurable for all types

**Answer: B**
AWS Managed Keys auto-rotate every 1 year (mandatory, no opt-out). Customer Managed Keys must have rotation enabled — they support both automatic and on-demand rotation. Imported Keys can only be rotated manually by importing new key material and using aliases to swap.

**Why others are wrong:**
- A) Imported Keys do NOT support automatic rotation
- C) Customer Managed Keys do NOT auto-rotate by default — rotation must be explicitly enabled
- D) Imported Keys cannot be rotated via KMS API — requires manual import of new material

**Key Concept:** KMS rotation: AWS Managed (auto, yearly) → CMK (auto + on-demand, must enable) → Imported (manual only, aliases)

---

## Scenario 7: SSM Parameter Store vs Secrets Manager (ssm-parameter-store / parameter-store-vs-secrets-manager)

**Context:** A startup needs to store database credentials for RDS PostgreSQL (with 90-day auto-rotation), API keys for third-party services, and feature flags.

**Requirements:** Automatic rotation for database credentials. Cost-effective config storage. Hybrid approach if needed.

**Question:** Which approach best meets these requirements?

A) Store everything in Secrets Manager with rotation enabled
B) Store database credentials in Secrets Manager with rotation; store API keys and feature flags in SSM Parameter Store Standard
C) Store everything in SSM Parameter Store Advanced with Lambda-based rotation
D) Store credentials in CloudHSM; config in SSM Parameter Store

**Answer: B**
Hybrid: Secrets Manager handles RDS creds with built-in auto-rotation (native integration). SSM Parameter Store Standard (free) handles non-sensitive config. Matches each service's strengths.

**Why others are wrong:**
- A) Unnecessarily expensive for feature flags and non-sensitive config
- C) SSM has no built-in auto-rotation; custom Lambda+EventBridge is complex
- D) CloudHSM is for encryption hardware, not credential storage/rotation

**Key Concept:** SSM Parameter Store vs Secrets Manager — use each for its strengths

---

## Scenario 8: WAF Rules for Common Attacks (waf / waf-rules-for-common-attacks)

**Context:** An e-commerce platform on ALB experiences SQL injection and XSS attacks. Need to block specific countries and rate-limit API calls. Fixed IP requirement via Global Accelerator.

**Requirements:** Block SQL injection/XSS. Geo-block. Rate-limit. Fixed IPs.

**Question:** Which architecture meets all requirements?

A) Deploy WAF on NLB with managed rules + geo-match + rate-based rules
B) Deploy WAF on ALB with managed rules + geo-match + rate-based rules; use Global Accelerator for fixed IP → ALB
C) Deploy Shield Advanced on ALB for SQL/XSS protection; use Route 53 geolocation for country blocking
D) Deploy Network Firewall at VPC level with Suricata rules

**Answer: B**
WAF on ALB provides L7 protection with managed rule groups, geo-match, and rate-based rules. Global Accelerator provides fixed IPs. Standard pattern for "fixed IP + WAF."

**Why others are wrong:**
- A) WAF cannot deploy on NLB (Layer 4 only)
- C) Shield Advanced is DDoS protection, not SQL/XSS; Route 53 routes, doesn't block
- D) Network Firewall lacks WAF's HTTP inspection rules; doesn't integrate with Global Accelerator

**Key Concept:** WAF deployment targets (ALB, CloudFront, API GW — NOT NLB) + Global Accelerator for fixed IP

---

## Scenario 9: Shield Standard vs Advanced (shield / shield-standard-vs-advanced)

**Context:** A media streaming company on CloudFront + ALB experiences frequent DDoS attacks including L7 HTTP floods. Need 24/7 DDoS experts and cost protection during attacks.

**Requirements:** L7 DDoS mitigation. 24/7 DRT access. Cost protection. Auto WAF rule creation.

**Question:** Which solution meets these requirements?

A) Shield Standard with manually configured WAF rate-based rules
B) Shield Advanced ($3,000/month) with automatic L7 mitigation, DRT, and cost protection
C) WAF with Bot Control and IP reputation + CloudWatch alarms
D) GuardDuty for DDoS detection with Lambda auto-remediation

**Answer: B**
Shield Advanced provides automatic L7 DDoS mitigation, 24/7 DRT, cost protection, and advanced reporting. Covers EC2, ELB, CloudFront, Global Accelerator, Route 53.

**Why others are wrong:**
- A) Shield Standard only covers L3/4; no DRT; no cost protection
- C) WAF rules require manual management; no DRT; no cost protection
- D) GuardDuty is threat detection, not DDoS mitigation

**Key Concept:** Shield Standard (free, L3/4) vs Shield Advanced ($3K/month, L7, DRT, cost protection)

---

## Scenario 10: GuardDuty Threat Detection (guardduty / threat-detection-and-response)

**Context:** A fintech company suspects EC2 cryptocurrency mining. Need automatic threat detection, real-time notification, and automated instance isolation.

**Requirements:** Agentless detection. Real-time alerts. Automated remediation. Cryptocurrency mining detection.

**Question:** Which solution meets these requirements?

A) Inspector scanning EC2 for vulnerabilities → EventBridge → Lambda
B) GuardDuty analyzing VPC Flow Logs + CloudTrail → EventBridge → Lambda (isolate via SG change)
C) CloudTrail + CloudWatch Logs metric filters → CloudWatch Alarms → SNS
D) AWS Config compliance rules → SSM Automation remediation

**Answer: B**
GuardDuty uses ML to analyze VPC Flow Logs, CloudTrail, and DNS Logs with a dedicated cryptocurrency mining finding type. One-click enable, agentless. EventBridge rules trigger Lambda for automated isolation.

**Why others are wrong:**
- A) Inspector scans for CVE vulnerabilities, not runtime threats
- C) Requires manual pattern definition; no ML; won't catch crypto mining
- D) Config monitors configuration state, not runtime behavior

**Key Concept:** GuardDuty — runtime threat detection, CryptoCurrency finding, agentless, EventBridge integration

---

## Scenario 11: Cognito User Pools vs Identity Pools (cognito / user-pools-vs-identity-pools)

**Context:** A mobile gaming company needs: email/password + social login, temporary AWS credentials for S3 game save uploads, guest read-only access to DynamoDB leaderboards.

**Requirements:** Social + email sign-up. Temp AWS credentials for S3. Guest access. Single auth flow.

**Question:** Which solution meets these requirements?

A) Cognito User Pool for authentication + Cognito Identity Pool for AWS credentials (both authenticated and guest)
B) Cognito User Pool only — provides both authentication and AWS credentials
C) Cognito Identity Pool only — handles sign-up, authentication, and credential vending
D) IAM users with STS temporary credentials distributed to mobile app

**Answer: A**
User Pools handle authentication (sign-up, sign-in, social login, JWT tokens). Identity Pools handle authorization (exchange tokens for temporary AWS credentials with IAM roles). Identity Pools also support unauthenticated guest access with restricted IAM roles.

**Why others are wrong:**
- B) User Pools provide JWT tokens but do NOT issue AWS credentials
- C) Identity Pools don't handle user sign-up/management
- D) IAM users don't scale for mobile; manual STS is insecure and complex

**Key Concept:** Cognito User Pools (authentication/tokens) + Identity Pools (authorization/AWS credentials) — complementary
