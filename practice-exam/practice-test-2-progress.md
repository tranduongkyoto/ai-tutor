# Practice Test #2 — Progress Tracker
**Source:** `practice-test-2-questions.md` (65 questions)
**Started:** 2026-06-23
**Note:** Original results recovered from extracted-questions.json (Udemy attempt data)

## Domain Progress

| Domain | Questions | Score | Status |
|--------|-----------|-------|--------|
| Design Secure Architectures | 28 | 15/28 (53%) | Done |
| Design High-Performing Architectures | 15 | 11/15 (73%) | Done |
| Design Resilient Architectures | 12 | 7/12 (58%) | Done |
| Design Cost-Optimized Architectures | 10 | 5/10 (50%) | Done |

## Overall Summary

**TOTAL: 38/65 (58%)**
**Result: FAIL**

## Retake — 2026-08-05

**Retake Score: 51/65 (78%) — PASS ✓**
**Improvement: +20 points (58% → 78%)**

| Domain | Original | Retake | Change |
|--------|----------|--------|--------|
| Design Secure Architectures | 15/28 (53%) | 21/28 (75%) | +22pts |
| Design High-Performing Architectures | 11/15 (73%) | 13/15 (86%) | +13pts |
| Design Resilient Architectures | 7/12 (58%) | 10/12 (83%) | +25pts |
| Design Cost-Optimized Architectures | 5/10 (50%) | 7/10 (70%) | +20pts |

**Note:** Retake uses DIFFERENT questions than original (Udemy randomizes on retake).
Retake questions extracted to `retake-test-2-questions.md`.

### Wrong on Retake (14 questions — from retake-test-2-questions.md)

| Q# | Domain | Topic |
|----|--------|-------|
| 7 | HP | EFS Max I/O for big data processing |
| 8 | Secure | RDS encrypted snapshot sharing cross-account |
| 12 | Secure | CloudTrail org trail + IAM role for cross-account log access |
| 25 | Secure | KMS multi-Region key for cross-Region S3 encrypted data |
| 28 | Secure | S3 access points per-service prefix access |
| 40 | Resilient | ASG ELB health check not terminating unhealthy |
| 43 | Cost | CloudTrail org trail across accounts |
| 44 | Cost | Spot instances for 2hr monthly big data batch |
| 45 | Secure | SSE-C for on-prem managed encryption keys |
| 48 | Secure | Transit Gateway + RAM for hub-spoke VPC sharing |
| 54 | HP | Global Accelerator for global video conferencing |
| 55 | Cost | ASG default termination policy oldest launch config |
| 60 | Secure | API Gateway resource policy for VPC-only access |
| 61 | Resilient | Blue-green deployment with Route 53 weighted routing |

## Redo of Retake Wrong — 2026-08-06

**Redo Score: 12/14 (86%)**

| # | Q# | Domain | Topic | Redo Result |
|---|-----|--------|-------|-------------|
| 1 | 7 | HP | EFS Max I/O for big data | Correct |
| 2 | 8 | Secure | RDS encrypted snapshot sharing | Correct |
| 3 | 12 | Secure | Transfer Family SFTP + IAM roles | Wrong (picked B,D instead of B,E) |
| 4 | 25 | Secure | KMS multi-Region key for S3 CRR | Correct |
| 5 | 28 | Secure | S3 access points per-service | Correct |
| 6 | 40 | Resilient | ASG health check grace period | Wrong (extraction unclear on select-3) |
| 7 | 43 | Cost | RAM shared VPC cheapest | Correct |
| 8 | 44 | Cost | Spot Fleet for diverse batch | Correct |
| 9 | 45 | Secure | SSE-C for on-prem keys | Correct |
| 10 | 48 | Secure | Shared services VPC | Correct |
| 11 | 54 | HP | Global Accelerator for NLB endpoints | Correct |
| 12 | 55 | Cost | ASG terminates oldest launch config | Correct |
| 13 | 60 | Secure | API Gateway resource policy IP deny | Correct |
| 14 | 61 | Resilient | Global Accelerator for blue-green | Correct |

### Still Weak (wrong on redo)
1. **Transfer Family SFTP (Q12)** — B (IAM roles + IdP) + E (Transfer Family SFTP endpoint + S3 + IAM roles per vendor). D (Route 53 subdomains) is wrong — Transfer Family has its own endpoint.
2. **ASG health check troubleshooting (Q40)** — Grace period (B) is confirmed correct. Full answer for "select three" unclear from extraction.
