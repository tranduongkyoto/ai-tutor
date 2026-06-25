# Practice Exam Wrong Answers — Security Knowledge Review

**Date:** 2026-06-23 | **Errors:** 20/56 (36% of all errors)
**Source:** Udemy Practice Exams 1 & 2

---

## Topic A: IAM Scoping — SCP vs Permission Boundary vs IAM Policy (4 errors)

### 3-Layer Permission Model

| Layer | Scope | Who sets it | What it does |
|-------|-------|-------------|-------------|
| **SCP** | Account/OU level | Org admin | Maximum permissions for ENTIRE account |
| **Permission Boundary** | Per IAM user/role | Delegated admin | Maximum permissions for ONE user/role |
| **IAM Policy** | Per user/role/group | Anyone with IAM access | Actual granted permissions |

**Effective permission = SCP ∩ Permission Boundary ∩ IAM Policy**

### Decision Rule
- Restrict entire account/OU → **SCP**
- Restrict one specific user/role → **Permission Boundary**
- Grant actual access → **IAM Policy**

### Wrong Answers
- **E1-Q18**: Cross-account access → Create IAM role in target account + trust policy. Source account users assume via STS.
- **E2-Q12**: Restrict developer accounts → **SCP on OU** (not IAM policy on root user)
- **E2-Q18**: Limit individual developer → **Permission Boundary** (not SCP)
- **E2-Q65**: `ListBucket` → `arn:aws:s3:::mybucket`, `GetObject` → `arn:aws:s3:::mybucket/*` — different Resource ARNs

---

## Topic B: Cognito User Pools vs Identity Pools (1 error)

| Feature | User Pools | Identity Pools |
|---------|-----------|---------------|
| Purpose | Authentication (who?) | Authorization (what AWS?) |
| Output | JWT tokens | Temp AWS credentials (STS) |
| Use with | ALB, API Gateway | S3, DynamoDB, AWS services |

- **E2-Q19**: ALB auth → **User Pools** (not Identity Pools)

---

## Topic C: S3 Object Lock, Versioning & Retention (2 errors)

- Versioning = prerequisite for Object Lock
- Different versions CAN have different retention modes/periods
- Governance mode: some override | Compliance mode: nobody overrides

- **E1-Q17**: Versions have independent retention settings
- **E1-Q32**: Compliance protection → enable Versioning FIRST

---

## Topic D: Network Security — WAF, SG, CloudFront (3 errors)

| Scenario | Correct | Wrong Alternative |
|----------|---------|-------------------|
| Block countries on ALB | AWS WAF geo rules | CF Geo Restriction (CF-only) |
| Control EFS network | Security Groups | IAM (IAM=who mounts, SG=network) |
| Restrict API to IPs | API GW Resource Policy | Public subnet + SG |

- **E1-Q27**: Country block on ALB → **WAF geo rules**
- **E1-Q39**: EFS network → **Security Groups**
- **E2-Q41**: IP allowlist for API → **API GW Resource Policy**

---

## Topic E: Cross-Account & Private Connectivity (2 errors)

- NLB + PrivateLink = private cross-account connectivity (no public internet)
- Encrypted snapshot sharing = cross-account DB sharing + KMS key access

- **E1-Q62**: Partner private RDS access → **NLB + PrivateLink**
- **E2-Q23**: Auditor cross-account DB → **encrypted snapshot + KMS key**

---

## Topic F: Encryption & Certificate Management (2 errors)

- SSE-KMS automatic rotation: AWS handles it yearly
- SSE-KMS manual rotation: you create new CMK, update refs
- ACM-issued certs: auto-renew. Imported certs: NO auto-renew, use Config rule

- **E2-Q16**: KMS rotation → **automatic** (not manual)
- **E2-Q6**: Cert expiry check → **imported third-party certs** need Config rule

---

## Topic G: VPC Sharing & Isolation (1 error)

- Shared Services VPC: centralize shared resources, connect via peering/TGW
- Transit VPC: legacy pattern, replaced by Transit Gateway

- **E2-Q22**: Share resources across accounts → **Shared Services VPC**

---

## Topic H: EKS Security & On-Prem (2 errors)

- IRSA: pod-level IAM roles per K8s service account (granular)
- Outposts + EKS Anywhere: run EKS on-premises

- **E1-Q1**: EKS pod-level → **IRSA** (not instance profile)
- **E1-Q14**: Containers on-prem → **Outposts + EKS Anywhere**

---

## Topic I: Dedicated Instances vs Hosts (1 error)

| Feature | Dedicated Instance | Dedicated Host |
|---------|-------------------|----------------|
| Isolation | Single-tenant | Single-tenant |
| Host visibility | No | Yes (sockets, cores) |
| BYOL | No | Yes |
| Cost | Lower | Higher |

- **E2-Q37**: Single-tenant, no BYOL → **Dedicated Instances**

---

## Topic J: Conditional IAM & S3 Access Points (2 errors)

- `aws:SourceIp` checks caller's IP, not instance metadata
- S3 Access Points: per-app access with prefix-scoped policies

- **E2-Q31**: Condition on IP → check **user's source IP**
- **E2-Q54**: Multi-service S3 access → **S3 Access Points** per service
