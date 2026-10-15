# TD Set 5 — Timed retake — Analysis

**Date:** 2026-10-15 · **Mode:** TD website timed mode (retake) · **Time:** 21 min 08 s (~17 s/question) · multi-select all-or-nothing
**Score:** 66/75 (**88%**) 🟢 — first attempt 09-25: 31/75 (41.3%) → **+47 pts**
**Source:** `Retake-AWS_SAP_Timed_Mode_Set_5_Results.md` (raw TD export) → normalized to `td5_retake_export.md`
**Review file:** `td5_retake_review.md` (9 wrong + tracker + 🇻🇳) · flashcards: `aws-sap/td5-flashcards.html`

## Scores

| Domain | Score |
|---|---|
| Design Solutions for Organizational Complexity | 94.44% 🟢 |
| Continuous Improvement for Existing Solutions | 94.12% 🟢 |
| Accelerate Workload Migration and Modernization | 83.33% 🟢 |
| Design for New Solutions | 81.82% 🟡 lowest |

| Slice | Score |
|---|---|
| Single-choice | 48/54 (89%) |
| Multi-select | 18/21 — all 3 misses had 1 of 2 correct picks |
| Per third | 22/25 · 21/25 · 23/25 |

## Old misses vs regressions

| | Count |
|---|---|
| 09-25 misses now right | **41/44** (still wrong: Q17 DX gateway, Q48 PrivateLink NLB, Q70 EKS multi-cloud) |
| 09-25 right answers now wrong | **6/31** (Q8, Q22, Q38, Q39, Q44, Q55) |

⚠️ **21 minutes for 75 questions = recall speed.** The real exam allows ~2.8 min/question. Retakes measure memory; TD4 (unseen, 10-19) is the real signal — read every stem fully there.

## Wrong answers by pattern (9)

| Group | Q | Correct | Why the pick failed |
|---|---|---|---|
| A. Networking & routing | 48 🔁 | NLB-backed endpoint service | ALB can't back PrivateLink (5th miss) |
| A | 17 🔁 | 2nd DX + one DX gateway | Transit gateway per Region = extra parts |
| A | 55 | Allowed prefixes ≥ VPC CIDR + advertise VPC prefixes | MACsec / bandwidth don't fix routing |
| A | 38 | Private subnets + DynamoDB endpoint or NAT | VPC Lambda never gets a public IP |
| B. Cheapest / least overhead | 22 | S3 Transfer Acceleration + edge-optimized API GW | Multi-Region stack = overbuilt |
| B | 39 | Lambda functions + API Gateway | ASG + ALB still runs EC2 |
| B | 70 🔁 | EKS on Fargate | ECS is AWS-only; multi-cloud → Kubernetes |
| B | 44 | Hash on-chain, PII in DynamoDB | Name + ID are still PII |
| C. Least privilege | 8 | Trust the caller's role ARN | Trusting Account B root = any identity |

**Pattern:** networking/routing is now the main weak area (4/9 + 5 public-VIF misses + Pair drill 7/10).

## 5 rules
1. PrivateLink service → **NLB** (or GWLB). Never ALB.
2. Many Regions over one DX → **one Direct Connect gateway**; TGW ↔ DX gateway needs **allowed prefixes ≥ VPC CIDRs**.
3. VPC Lambda → **private subnets** + endpoint/NAT for AWS APIs.
4. "Other cloud providers" + containers → **EKS**.
5. Cross-account trust → the **specific role ARN**, edited in the role's own account.

## Next actions
1. Read 🇻🇳 sections (🔁 first: Q48, Q17, Q70).
2. Redo Pass 1 tonight: `/ai-tutor sap test-review td5_retake redo A, B, C`.
3. TD5 flashcards round 1 (`aws-sap/td5-flashcards.html`).
4. 10-16: TD2 retake — target 60–90 min, not 21.
