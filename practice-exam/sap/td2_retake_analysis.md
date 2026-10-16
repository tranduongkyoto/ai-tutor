# TD Set 2 — Timed retake — Analysis

**Date:** 2026-10-16 · **Mode:** TD website timed mode (retake) · multi-select all-or-nothing
**Score:** 67/75 (**89.3%**) 🟢 — first attempt: 43/75 (57.3%) → **+32 pts**
**Source:** `Retake-AWS_SAP_TimedModeSet2_ketqua.md` (raw TD export) → normalized to `td2_retake_export.md`
**Review file:** `td2_retake_review.md` (8 wrong + **Group D: 5 answered-right-but-unsure — Q13, 34, 39, 68, 72** + tracker + 🇻🇳 on all 13) · flashcards: `aws-sap/td2-flashcards.html`

⚠️ **Export defects fixed:** 6 questions (15, 26, 42, 45, 53, 62) had an empty "Đáp án đúng" and 2 multi-selects (17, 58) listed only one of two answers. Answers were recovered from the TD explanation text ("Hence/Therefore, the correct answer…", "… is correct") — all exact text matches.

| Slice | Score |
|---|---|
| Single-choice | 51/57 (89%) |
| Multi-select | 16/18 — both misses had 1 of 2 correct picks |
| Per third | 23/25 · 22/25 · 22/25 |

## Old misses vs regressions

| | Count |
|---|---|
| First-attempt misses now right | **31/32** (still wrong: Q26 IAM role vs SCP) |
| First-attempt right answers now wrong | **7/43** (Q15, Q17, Q42, Q45, Q53, Q58, Q62) |

Retake caveat: seen questions → treat 89% as ~80% on unseen material. TD4 (10-19) is the real signal.

## Wrong answers by pattern (8)

| Group | Q | Correct | Why the pick failed |
|---|---|---|---|
| A. Identity & directory | 42 | Directory Service + AD trust → SSO | Identity Center alone can't use the existing AD |
| A | 26 🔁 | IAM role with resource-level permissions | SCPs never grant |
| B. DNS & edge protection | 17 | Resolver **outbound** endpoint + forwarding rule | Inbound = into the VPC, wrong direction |
| B | 58 | OAC + custom header/WAF **on the ALB** | NACL can't allow "CloudFront only" |
| C. Read the deciding detail | 15 | SNS **Mobile Push** | SNS SMS = text messages, not app push |
| C | 45 | CloudFormation + CloudFront | Beanstalk isn't infrastructure as code |
| C | 53 | Multi-AZ failover flips the **CNAME** | The IP isn't moved |
| C | 62 | Stateless ASG + ElastiCache + read replicas + Multi-AZ | Stateful + Multi-AZ only (twin options) |

## 5 rules
1. Existing Microsoft AD → **Directory Service** (trust) → SSO; don't recreate users.
2. Resolver: queries **leaving** the VPC → **outbound** endpoint + forwarding rule.
3. ALB origin behind CloudFront → custom header + **WAF on the ALB**; S3 origin → OAC.
4. App push → **SNS Mobile Push** (not SMS) · IaC → **CloudFormation**.
5. Multi-AZ failover = **CNAME** switch · scale reads = read replicas + cache, stateless tiers.

## Next actions
1. Read 🇻🇳 sections (Q26 🔁 first).
2. Redo Pass 1 tonight: `/ai-tutor sap test-review td2_retake redo A, B, C`.
3. 10-17: TD3 retake.
