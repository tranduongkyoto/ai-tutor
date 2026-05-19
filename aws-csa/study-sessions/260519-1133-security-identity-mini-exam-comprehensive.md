# Security & Identity — Mini Exam: Comprehensive Final (Phase 6)
**Date:** 2026-05-19 11:33
**Score:** 9/10 (90%)
**Scope:** comprehensive — full domain exam covering all security & identity topics

---

## Questions & Results

### Q1 ✗ — IAM Execution Role Tag-Based Access + Deny IAM Actions (iam)
**Question:** A solutions architect needs to restrict an AWS Lambda function so it can only access Amazon Simple Storage Service (S3) objects tagged with `project=alpha` in a specific bucket. The Lambda function must also be prevented from creating IAM roles or attaching any IAM policies. Which approach enforces both requirements with least privilege?

A) Attach an IAM execution role to the Lambda function with `s3:GetObject` allowed only when `s3:ExistingObjectTag/project` equals `alpha`, and explicitly deny `iam:CreateRole` and `iam:AttachRolePolicy` in the same policy
B) Create an S3 bucket policy that allows the Lambda function's role to access only objects tagged `project=alpha`, and use an SCP to deny IAM role creation across the account
C) Attach an IAM execution role with full S3 access and use an IAM Permission Boundary that restricts `s3:GetObject` to objects tagged `project=alpha` and denies all `iam:*` actions
D) Use a resource-based policy on the Lambda function to restrict which S3 objects it can access, and deny IAM actions using a Service Control Policy (SCP) on the account

**Your answer: D** — Incorrect. Correct answer: A. Lambda resource-based policies control who can INVOKE Lambda, not what Lambda can ACCESS. The execution role with tag-based S3 condition + explicit IAM deny is the correct least-privilege approach.

---

### Q2 ✓ — KMS Multi-Region Keys Properties (kms-multi-region-keys)
**Question:** Which statement about AWS Key Management Service (KMS) Multi-Region Keys is correct?

A) Multi-Region Keys are a single global key that automatically replicates to all AWS Regions in the account, and changes to the key policy in one region instantly propagate to all replicas
B) Multi-Region Keys share the same key ID and key material across regions but are managed independently — each replica has its own key policy, grants, and can be enabled/disabled separately
C) Multi-Region Keys enable cross-region encryption by allowing a KMS key in one region to be called directly from another region via the KMS API without any latency penalty
D) Multi-Region Keys are only available as asymmetric keys and are primarily designed for cross-region digital signature verification

**Your answer: B** — Correct. MRKs share key ID and material but each replica is independently managed with separate policies, grants, and enable/disable state.

---

### Q3 ✓ — Firewall Manager Auto-Apply to New Accounts (firewall-manager)
**Question:** A company uses AWS Firewall Manager to manage WAF rules across 30 accounts. A new account is created and added to the Production OU. What happens to the Firewall Manager WAF security policy scoped to the Production OU?

A) The new account must be manually enrolled in Firewall Manager before the WAF policy takes effect
B) The WAF policy automatically applies to the new account and deploys WAF Web ACLs on all in-scope resources without administrator action
C) The WAF policy applies only after the next Firewall Manager compliance evaluation cycle (every 24 hours)
D) The new account inherits the WAF policy only if an AWS Config rule is enabled in the account

**Your answer: B** — Correct. Firewall Manager automatically discovers new accounts in scope and deploys policies without manual action — key differentiator.

---

### Q4 ✓ — Secrets Manager Rotation Cache Issue (secrets-manager)
**Question:** After a Secrets Manager rotation event, the application intermittently fails to authenticate for ~60 seconds. What is the most likely cause and fix?

A) Lambda rotation function timeout; increase Lambda timeout and memory
B) Application caching old secret; implement caching client with shorter TTL or EventBridge rotation event listener
C) Simultaneous KMS key rotation; stagger rotation schedules
D) Secret propagation delay to read replicas; reduce replica regions

**Your answer: B** — Correct. Classic rotation issue — app caches old credential. Secrets Manager caching client with shorter TTL or EventBridge listener for immediate cache invalidation.

---

### Q5 ✓ — SCP to Prevent CloudTrail Tampering (scp)
**Question:** Prevent any IAM user across 50 member accounts from disabling CloudTrail or deleting trails, while management account retains full ability.

A) Per-account IAM deny policies attached to all users/roles
B) SCP on root OU denying cloudtrail:StopLogging and cloudtrail:DeleteTrail
C) AWS Config + EventBridge to auto-re-enable CloudTrail
D) Control Tower detective guardrails to monitor CloudTrail

**Your answer: B** — Correct. SCP on root OU = preventive control for all member accounts. Management account exempt by design. Standard security pattern.

---

### Q6 ✓ — CloudFront → ALB Origin Restriction (waf / cloudfront)
**Question:** Ensure only CloudFront can reach the ALB. Which combination provides strongest protection? (Select TWO)

A) ALB SG allowing only CloudFront managed prefix list
B) Custom HTTP header in CloudFront origin + ALB listener rule validation
C) ALB with private IP in private subnet
D) WAF on ALB blocking non-CloudFront IPs

**Your answer: A, B** — Correct. SG with managed prefix list (network layer) + custom origin header (application layer) = defense-in-depth. AWS-recommended pattern.

---

### Q7 ✓ — Macie for PII Detection in S3 (macie)
**Question:** Which AWS service detects PII in S3 buckets?

A) GuardDuty
B) Inspector
C) Macie
D) AWS Config

**Your answer: C** — Correct. Macie uses ML + pattern matching to discover sensitive data (PII) in S3.

---

### Q8 ✓ — Cross-Account Secrets Manager + KMS Access (kms / secrets-manager)
**Question:** What must be configured for cross-account access to a Secrets Manager secret encrypted with a CMK?

A) Share KMS CMK via RAM + Secrets Manager resource policy
B) Secrets Manager resource policy granting access + KMS key policy granting kms:Decrypt
C) KMS MRK replica in other account + Secrets Manager MRK config
D) Export and re-create secret in other account

**Your answer: B** — Correct. Two policies needed: Secrets Manager resource-based policy for secret access + KMS key policy for decrypt permission. KMS can't be shared via RAM.

---

### Q9 ✓ — Cognito User Pool + Identity Pool for S3 Access (cognito)
**Question:** Users sign up with email/password and need temporary AWS credentials to upload photos to user-specific S3 prefix.

A) IAM policy attached directly to Cognito users
B) User Pool for auth → Identity Pool for temporary credentials → IAM role with policy variable for S3 prefix
C) Identity Pool with unauthenticated access + S3 bucket policy
D) User Pool directly issues STS credentials

**Your answer: B** — Correct. User Pool (authentication) → Identity Pool (temporary AWS credentials via STS) → IAM role with `${cognito-identity.amazonaws.com:sub}` for user-scoped S3 access.

---

### Q10 ✓ — SCP Explicit Deny Precedence (scp)
**Question:** Security OU has SCP denying ec2:TerminateInstances. User in Account X (Security OU) has IAM policy allowing ec2:*. Can user terminate instances?

A) Yes — IAM overrides SCP
B) No — SCP explicit Deny always wins
C) Yes — Root OU FullAWSAccess overrides child Deny
D) No — but only without MFA

**Your answer: B** — Correct. Explicit Deny in SCP always wins regardless of IAM policies or parent OU Allows. SCPs set maximum permissions ceiling.

---

## Summary
- **Score:** 9/10 (90%)
- **Missed topics:** iam (Lambda resource-based policy vs execution role distinction)
- **Strong areas:** kms-multi-region-keys, firewall-manager, secrets-manager, scp, waf/cloudfront, macie, cognito
- **Key lessons:**
  - Lambda resource-based policies control who can INVOKE Lambda — the execution role controls what Lambda can ACCESS. For restricting Lambda's S3 access, modify the execution role policy, not a resource-based policy.
