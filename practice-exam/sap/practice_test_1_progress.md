# Practice Test #1 — SAP-C02 Progress Tracker
**Source:** `practice_test_1.md` (30 questions)
**Started:** 2026-09-10

## Domain Progress

| Domain | Questions | Score | Status |
|--------|-----------|-------|--------|
| Organizational Complexity (26%) | — | — | Not started |
| Design New Solutions (29%) | — | — | Not started |
| Continuous Improvement (25%) | — | — | Not started |
| Migration & Modernization (20%) | — | — | Not started |

**Status:** In Progress (Q3/30) — 0/3 correct (0%) — paused 2026-09-11

## All Questions

| Q# | Topic | Your | Correct | Result |
|----|-------|------|---------|--------|
| 1 | Cross-account CW Logs aggregation | C | A | Wrong |
| 2 | VPC Flow Logs analysis tool + filter | B | D | Wrong |
| 3 | FSx Multi-AZ + monitoring | B,C | D,E | Wrong |

### Weak Areas (so far)
1. **CloudWatch vs CloudTrail** — CW Logs for Flow Logs analysis, CloudTrail for API audit only
2. **Subscription Filters** — CW Logs → Subscription Filter → Kinesis Firehose (not CW agent → Firehose)
3. **FSx failover testing** — modify throughput capacity, NEVER touch ENIs
4. **FSx monitoring** — CloudWatch for metrics, CW Logs + Firehose for file access auditing
