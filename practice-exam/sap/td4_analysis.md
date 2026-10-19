# TD Set 4 — Timed (Gate 2) — Analysis

**Date:** 2026-10-19 · **Mode:** TD website timed mode · **first attempt, unseen** · **Time:** 180 min (all of it) · multi-select all-or-nothing
**Score:** 50/75 (**66.7%**) 🔴 — below the 70% gate → **keep exam on 11-02** (no earlier reschedule)
**Source:** `AWS-SAP-Timed-Mode-Set-4-results.md` (TD export) → normalized to `td4_export.md`
**Review file:** `td4_review.md` (25 wrong + tracker + 🇻🇳) · flashcards: `aws-sap/td4-flashcards.html` (75 cards, 25 🔁)

## Scores

| Domain | Score |
|---|---|
| Accelerate Workload Migration and Modernization | 100% 🟢 |
| Design Solutions for Organizational Complexity | 100% 🟢 |
| Design for New Solutions | 68% 🔴 |
| Continuous Improvement for Existing Solutions | **56%** 🔴 lowest |

| Slice | Score |
|---|---|
| Single-choice | 41/59 (69%) |
| Multi-select | 9/16 — **all 7 misses were partial** (1 right pick + 1 wrong) |
| Per third | 18/25 · 18/25 · **14/25** — fatigue / time pressure at the end |

## Why this differs from the retakes

TD1/TD5/TD2 retakes scored 88–89%, but those questions were seen before (TD5 took 21 min = recall speed). TD4 is the only unseen full test → **~67% is the honest baseline**. The real exam gives 210 min (ESL +30) — use the extra time on the last third.

## Wrong answers by pattern (25)

| Group | Q | Correct | Why the pick failed |
|---|---|---|---|
| A. Known rule, new wording | 5 🔁 | EventBridge rule + Step Functions + SNS | CloudTrail filter alone doesn't notify |
| A | 28 🔁 | RDS Proxy + Aurora + Aurora Replicas | Cache doesn't queue writes / speed failover |
| A | 58 🔁 | DX Gateway + VGW per VPC | Already-known DX rule missed (3rd time) |
| A | 64 🔁 | Redshift automated snapshot + cross-Region copy | No cross-Region "replication" for Redshift |
| A | 57 | Stop → modify placement group → start | Terminate / ENA don't fix placement |
| A | 62 | CFN SSM parameter type for latest AMI | Service Catalog / Config don't resolve AMIs |
| B. Storage & performance fit | 13 | Table per week + sensor PK + timestamp SK | Concatenated key / one big table |
| B | 38 | EFS + ASG EC2 + CloudFront | Lambda burst limits |
| B | 51 | EFS Provisioned Throughput | Max I/O adds latency |
| B | 66 | Replicas + ElastiCache + sharding | Bigger instance / PIOPS = costly |
| C. Cost choice | 15 | Fargate web + Spot workers | S3 can't host a dynamic app |
| C | 21 | DynamoDB reserved capacity + drop old table | Wrong cost lever |
| C | 40 | Spot Fleet On-Demand + Spot across AZs + ALB | All-Spot risks interruption |
| C | 54 | DEV benefits (same AZ zonal RI) | RI sharing needs same AZ + type |
| D. Near-identical options | 14 | CodePipeline + change set + CodeBuild | Extra "CodeDeploy" clause |
| D | 41 | S3 origin + path-pattern behavior | ALB can't forward to S3 |
| D | 63 | Parallel state + orchestration workflow | SQS isn't a direct Step Functions input |
| E. Service fit | 17 | AppSync subscriptions | Caching/polling isn't real-time push |
| E | 19 | Client VPN + one endpoint in main VPC | TGW rework not needed |
| E | 29 | MGN replication agent | Wrong migration tool |
| E | 34 | ENI pool + Parameter Store | Licenses bind to MAC → ENI |
| E | 44 | Cert in IAM, Security-team-only policy | Cert on EC2 breaks separation of duties |
| E | 56 | IPsec VPN + external MySQL replica | SSL endpoint alone ≠ replication |
| E | 65 | NLB + NACL deny non-UDP | WAF/ALB are Layer 7 |
| E | 74 | WorkDocs | Sharing keys with customers |

**Pattern:** 4 🔁 misses were rules already on the rule sheet → recall under new wording is the gap, not knowledge. Partial multi-select picks cost 7 points (meta-rule 5).

## 6 rules
1. Same AWS rule, new words → name the **trigger** first (one DX → many VPCs = DX Gateway; DR Redshift = cross-Region snapshot copy).
2. Multi-select: after picking, **re-check each pick completes the same solution** — 7/7 multi misses were half right.
3. Twin options → judge only the differing clause (meta-rule 7).
4. "Cheapest + resilient" → mix On-Demand baseline + Spot; never all-Spot for prod.
5. Read-heavy DB on budget → replicas + cache + sharding, not bigger/PIOPS.
6. Last third: slow down, re-read the constraint word; budget ~2.5 min/question with 210 min.

## Next actions
1. Read 🇻🇳 sections (🔁 first: Q5, Q28, Q58, Q64).
2. 10-20 redo Pass 1: `/ai-tutor sap test-review td4 redo A, B, C, D, E`.
3. TD4 flashcards round 1 (`aws-sap/td4-flashcards.html`).
4. Rewrite the 11-02 plan: Continuous Improvement focus, multi-select discipline, one more unseen timed test ~10-28 (target ≥72%).
