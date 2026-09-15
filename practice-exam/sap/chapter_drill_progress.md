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
