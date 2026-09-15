# SAP-C02 Chapter Drill Progress

## security — 2026-09-15
Score: 10/13 (77%)

| Q Ref | Topic | Your | Correct | Result |
|-------|-------|------|---------|--------|
| T1:Q6 | WAF rules across multi-account (Config+SSM+CF StackSets) | B | B | Correct |
| T1:Q20 | WAF+Inspector+GuardDuty roles (monitor vs block) | B | B | Correct |
| T1:Q25 | Secrets Manager rotation in VPC (interface endpoint) | C | A | Wrong |
| T1:Q30 | KMS client-side encryption (GenerateDataKey) | A | C | Wrong |
| T2:Q6 | WAF geo match + IP set (block country, allow dev team) | C,E | C,E | Correct |
| T2:Q14 | ACM certs are Region-specific (multi-Region ALB) | C | C | Correct |
| T2:Q18 | Redshift KMS cross-Region snapshots (grant in dest) | D | B | Wrong |
| T2:Q34 | DDoS defense (Route53 + CloudFront + WAF + S3) | C,E | C,E | Correct |
| T3:Q16 | CloudFront 502 (expired origin SSL cert, need trusted CA) | A | A | Correct |
| T3:Q29 | Redshift audit logs (SSE-S3 + Spectrum, cost-effective) | A | A | Correct |
| T3:Q38 | KMS key access restriction (PrincipalOrgID + Org ID) | C | C | Correct |
| T3:Q54 | Country restriction (WAF geo match on ALB) | D | D | Correct |
| T3:Q60 | Vulnerability scanning (Inspector, not SSM) | D | D | Correct |

### Weak Areas — Security
1. **VPC endpoints for Secrets Manager** — Lambda timeout in private subnet = needs VPC interface endpoint for Secrets Manager (not Lambda, not SSL issue)
2. **kms:GenerateDataKey** — client-side envelope encryption requires GenerateDataKey for uploads, Decrypt for downloads. kms:Encrypt alone is NOT sufficient
3. **Redshift cross-Region snapshots** — snapshot copy grant in DESTINATION Region, KMS key in DESTINATION Region, configure in SOURCE Region. No "cross-Region replication" exists for Redshift

## identity-federation — 2026-09-15
Score: 8/15 (53%)

| Q Ref | Topic | Your | Correct | Result |
|-------|-------|------|---------|--------|
| T3:Q33 | Confused deputy (external ID from partner) | A | C | Wrong |
| T1:Q27 | Centralized RI purchasing (Orgs all-features + SCP) | C,B | A,B | Wrong |
| T2:Q47 | SCP behavior (root user, service-linked roles) | B,F,E | B,D,E | Wrong |
| T3:Q18 | SCP true statements (root user, deny overrides) | C,E | C,E | Correct |
| T2:Q38 | SAML federation + RDS Region restriction | B | D | Wrong |
| T1:Q28 | Multi-account OUs + Budget alerts + GuardDuty delegated admin | A,C,E | A,C,D | Wrong |
| T3:Q17 | API Gateway throttle (no Lambda logs = blocked before Lambda) | C | C | Correct |
| T1:Q6 | WAF rules across multi-account (Config+SSM+CF StackSets) | B | B | Correct |
| T3:Q19 | SCP JSON syntax (Statement as array) | C | C | Correct |
| T3:Q37 | Cross-account Lambda (execution role + AssumeRole) | C,D | C,D | Correct |
| T3:Q38 | KMS key access restriction (PrincipalOrgID + Org ID) | C | C | Correct |
| T3:Q58 | Region restriction (SCP deny non-core at root OU) | A | A | Correct |
| T3:Q13 | CodePipeline cross-account (KMS+S3 in A, role+CF in B) | C,B,A | A,D,E | Wrong |
| T2:Q75 | SNS→Lambda throttling (Lambda concurrency quota) | A | A | Correct |
| T3:Q66 | ABAC session tags (STS tag + IAM deny StringNotEquals) | A | D | Wrong |

### Weak Areas — Identity & Federation
1. **External ID direction** — external ID comes FROM the third-party partner (they generate it for uniqueness), not created by you
2. **AWS Organizations all features vs consolidated billing** — SCPs require all features mode; consolidated billing mode does NOT support SCPs
3. **SCPs affect root user** — SCPs affect ALL identities in member accounts INCLUDING root; they do NOT affect service-linked roles or the management account root
4. **PowerUserAccess vs AdministrativeAccess** — PowerUserAccess = AdministrativeAccess minus IAM management; use PowerUser for least privilege when IAM access not needed
5. **OUs vs SCPs as containers** — accounts are organized into OUs, not into SCPs; SCPs are attached TO OUs
6. **Cross-account CodePipeline direction** — pipeline in account A: KMS key + S3 bucket + AssumeRole permission in A; cross-account role + CF service role in target account B
7. **ABAC with STS session tags** — for shared accounts, use SAML session tags + IAM deny with StringNotEquals on aws:PrincipalTag; can't use separate OUs for a single shared account
