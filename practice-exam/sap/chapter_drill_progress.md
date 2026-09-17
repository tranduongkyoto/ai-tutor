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

## vpc — 2026-09-16 (30 of 34 answered, skipped 4 non-VPC: T1:Q29, T3:Q40, T3:Q57, T3:Q64)
Score: 23/30 (77%)

| Q Ref | Topic | Your | Correct | Result |
|-------|-------|------|---------|--------|
| T3:Q1 | QuickSight VPC connection (private subnet + SG + ENI) | C | C | Correct |
| T3:Q5 | Route53 Resolver inbound + private zone + CNAME for EFS | C | C | Correct |
| T2:Q4 | Multi-DC hybrid (DX per DC from different providers) | B | D | Wrong |
| T3:Q8 | Cross-VPC load balancer access (VPC peering, cost-effective) | B | B | Correct |
| T3:Q9 | Encrypted DX (public VIF + Site-to-Site VPN) | C | D | Wrong |
| T3:Q11 | Storage Gateway to S3 private (Gateway + Interface endpoints) | B,A | B,D | Wrong |
| T3:Q14 | Private IP S3 access over DX (private VIF + interface endpoint) | A | A | Correct |
| T2:Q13 | S3 access restricted to VPC endpoint only | A | A | Correct |
| T3:Q20 | Encrypted DX to VPC (public VIF + VPG + IPsec) | D,A,F | C,D,F | Wrong |
| T3:Q21 | Move EC2 to different subnet (AMI + new instance + Route53) | C | B | Wrong |
| T3:Q25 | Isolated VPCs via PrivateLink (NLB + endpoint service + ALB) | B | C | Wrong |
| T3:Q28 | Automated VPC CIDR (CloudFormation custom resource + IPAM) | C | A | Wrong |
| T2:Q17 | Hub-spoke shared services (Centralized VPC Endpoints) | C | C | Correct |
| T2:Q31 | Private hosted zone not resolving (enable DNS hostnames+resolution) | D | D | Correct |
| T2:Q32 | Lambda VPC best practices (Layers, NAT, CloudWatch alarms) | E,A,F | A,E,F | Correct |
| T2:Q42 | Bidirectional DNS (inbound + outbound R53 Resolver endpoints) | B,C | B,C | Correct |
| T2:Q51 | Multi-site communication (VPN CloudHub) | D | D | Correct |
| T2:Q55 | Shared VPCs (VPC sharing = share subnets via RAM) | A | A | Correct |
| T2:Q57 | Default SG vs new SG (self-referencing inbound vs no inbound) | D | D | Correct |
| T2:Q64 | VPC peering + routes both directions (172.20 ↔ 172.30) | A,B | A,B | Correct |
| T2:Q72 | 140TB archive over DX (public VIF to S3) | D | A | Wrong |
| T3:Q46 | Same-CIDR peered VPCs (/28 subnets + 2 route tables) | A,E | A,E | Correct |
| T3:Q52 | Flow logs ACCEPT/REJECT (NACL outbound on subnet) | D | D | Correct |
| T3:Q61 | Lambda in VPC no internet (NAT Gateway needed) | A | A | Correct |
| T3:Q70 | Direct client access bypassing ELB (SG restrict to ELB only) | A | A | Correct |
| T1:Q2 | VPC Flow Logs NAT gateway (CloudWatch + dstAddr filter) | D | D | Correct |
| T1:Q12 | Security groups EC2↔RDS (outbound EC2 + inbound DB, port 3306) | E,B | B,E | Correct |
| T1:Q24 | Interface VPC endpoint for Kinesis (not Gateway) | C | C | Correct |
| T1:Q25 | Secrets Manager rotation timeout (VPC interface endpoint for SM) | A | A | Correct |
| T1:Q26 | DX + VPN for encrypted high-throughput connection | D | B | Wrong |

### Weak Areas — VPC
1. **Public VIF for encrypted DX** — VPN over Direct Connect requires PUBLIC VIF (VPN endpoint has public IP). Private VIF = private IP access to VPC only. Pattern: encryption over DX = public VIF + VPN
2. **Public VIF for S3 over DX** — on-premises → S3 directly over DX = public VIF (S3 is a public service). Only use private VIF + interface endpoint when bucket policy denies public IPs
3. **S3 supports both Gateway AND Interface VPC endpoints** — Private Virtual Interface is for Direct Connect only, not Storage Gateway to S3
4. **Can't move EC2 to different subnet** — must create AMI → launch new instance in target subnet → update DNS → terminate old
5. **PrivateLink for isolated cross-VPC** — NLB as endpoint service + interface VPC endpoint. VPC peering opens bidirectional traffic. NLB doesn't support host-based routing (ALB only)
6. **Fn::Cidr vs Custom Resource** — Fn::Cidr splits existing CIDRs, can't ensure global uniqueness. Use CloudFormation custom resource + external IPAM for unique CIDR allocation
7. **Multiple DCs need separate DX connections** — one DX per data center from different service providers for max resiliency. Can't share one DX across multiple distant DCs
8. **Minimum subnet CIDR is /28** — AWS doesn't allow /29 or smaller
9. **DX alone is not encrypted** — DX + VPN combo needed for encrypted + low-latency + high-throughput; VPN alone lacks throughput guarantees

## storage — 2026-09-17 (IN PROGRESS: 5/51 answered, resume from T1:Q16)
Score so far: 3/5 (60%)

| Q Ref | Topic | Your | Correct | Result |
|-------|-------|------|---------|--------|
| T1:Q3 | FSx Multi-AZ failover test + monitoring (throughput, not ENI) | C,B | D,E | Wrong |
| T1:Q7 | VOD storage (S3 Intelligent-Tiering + CloudFront) | B | B | Correct |
| T1:Q9 | CloudFront S3 HTTP 307 (24h propagation + Regional endpoint) | A,B | A,D | Wrong |
| T1:Q10 | On-prem NAS to S3 (DataSync + Lambda + Step Functions + Batch) | C | C | Correct |
| T1:Q15 | Storage Gateway cache stale (RefreshCache, not ResetCache) | C | C | Correct |

### Remaining questions (resume from here)
T1:Q16, T1:Q17, T1:Q22, T2:Q2, T2:Q5, T2:Q7, T2:Q11, T2:Q12, T2:Q13, T2:Q26, T2:Q27, T2:Q30, T2:Q35, T2:Q41, T2:Q44, T2:Q52, T2:Q54, T2:Q56, T2:Q61, T2:Q62, T2:Q63, T2:Q67, T2:Q68, T2:Q70, T2:Q72, T2:Q73, T3:Q3, T3:Q4, T3:Q11, T3:Q15, T3:Q27, T3:Q29, T3:Q31, T3:Q34, T3:Q35, T3:Q41, T3:Q42, T3:Q47, T3:Q48, T3:Q49, T3:Q50, T3:Q53, T3:Q62, T3:Q72, T3:Q73, T3:Q75

### Weak Areas (so far)
1. **FSx failover test** — modify THROUGHPUT CAPACITY to trigger failover; NEVER modify ENIs (permanent loss of connection)
2. **FSx monitoring** — CloudWatch for metrics, CloudTrail for API calls only, CloudWatch Logs + Firehose for file access auditing
3. **S3 HTTP 307** — new bucket takes 24h to propagate; use Regional endpoint (s3.us-west-2.amazonaws.com) instead of default s3.amazonaws.com
