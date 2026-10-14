# TD Set 1 — Timed retake — Analysis

**Date:** 2026-10-14 · **Mode:** TD website timed mode (retake) · multi-select all-or-nothing
**Score:** 66/75 (**88%**) 🟢 — first attempt 09-28: 46/75 (61.3%) → **+27 pts**
**Source:** `Retake-AWS-SAP-Timed-Mode-Set-1-Results.md` (raw TD export) → normalized to `td1_retake_export.md` for the review scripts
**Review file:** `td1_retake_review.md` (9 wrong + tracker + 🇻🇳). Right answers: see `td_set_1_review_correct.md` (same questions).

## Scores

| Domain | Score |
|---|---|
| Continuous Improvement for Existing Solutions | 92% 🟢 |
| Design for New Solutions | 85.71% 🟢 (first attempts were 50–58%) |
| Design Solutions for Organizational Complexity | 84.62% 🟢 |
| Accelerate Workload Migration and Modernization | 77.78% 🟡 lowest |

| Slice | Score |
|---|---|
| Single-choice | 60/67 (90%) |
| Multi-select | 6/8 — both misses had 1 of 2 correct picks |
| Per third | 22/25 · 23/25 · 21/25 — no fatigue drop |

## Old misses vs regressions

| | Count |
|---|---|
| 09-28 misses now right | **27/29** (still wrong: Q21 AMI compliance, Q53 car registration) |
| 09-28 right answers now wrong | **7/46** (Q10, Q22, Q39, Q45, Q59, Q68, Q70) |

Retake caveat: questions were seen before → treat 88% as roughly 80% on unseen material. Gate 2 (TD4, 10-26) is the real check.

## Wrong answers by pattern (9)

| Group | Q | Correct | Why the pick failed |
|---|---|---|---|
| A. Read the real need | 53 🔁 | 2 NGINX EC2 + DMS + ELB + alias | S3 can't run an interactive app; option points at an ELB it never creates |
| A | 70 | Bucket lacks public read | "Wait 12 h for propagation" — Route 53 propagates in ~60 s |
| A | 10 | ASG On-Demand + ALB + Aurora Multi-AZ | Spot for the always-on prod web tier |
| A | 39 | Patched AMI + CodeDeploy + EFS for dataset | 500 GB download in user data at every boot |
| B. Edge & DNS | 68 🔁 | CloudFront geo restriction | Route 53 geolocation routes, doesn't block |
| B | 59 | GA + Route 53 public alias | Resolver inbound endpoint is for on-prem private DNS (twin options) |
| C. Hybrid networking | 22 🔁 | DX + DX Gateway + private VIF | VPN = internet, not dedicated |
| D. Governance & identity | 21 🔁 | Patch Manager + Config approved-AMI rule | GuardDuty detects threats, not compliance |
| D | 45 | Custom SAML + IAM, or custom OIDC + Cognito Identity Pools | Identity Center isn't for mobile app federation |

**Pattern:** 4/9 misses (Q53, Q68, Q22, Q21) were already on the weak-areas / pair-drill lists — known rules, not yet applied under time pressure.

## 6 rules
1. Interactive app + DB → compute + DB migration; **S3 hosts static files only**.
2. Static site shows nothing → **public read** on the bucket; never "wait for propagation".
3. Always-on production tier → **On-Demand/RI**, not Spot.
4. Slow boot / big static data → **bake AMI + EFS**, not user-data downloads.
5. **Block** countries → CloudFront geo restriction / WAF; Route 53 geolocation only routes.
6. "Dedicated private network" → **Direct Connect** (+ DX Gateway for many Regions), never VPN.

## Next actions
1. Read 🇻🇳 sections in `td1_retake_review.md` (🔁 ones first).
2. Redo Pass 1 today/tomorrow: `/ai-tutor sap test-review td1_retake redo A, B, C, D`.
3. TD5 full retake moves up to 10-16.
