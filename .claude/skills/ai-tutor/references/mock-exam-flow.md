# Mock Exam Flow

Full-length SAA-C03 mock exam: 65 questions, all domains, timed.

## Prerequisites
1. Check domain caches: at least 8/12 must exist in `.claude/skills/ai-tutor/cache/`
2. If <8 caches: show warning and suggest studying more domains first
3. Load all available domain caches + cheat sheet cache

## SAA-C03 Exam Domain Mapping

| Exam Domain | Weight | Questions | Service Domains (map from tutor domains) |
|-------------|--------|-----------|----------------------------------------|
| 1: Secure Architectures | 30% | 20 | security-identity, networking (VPC endpoints, NACLs), storage (S3 encryption, bucket policies) |
| 2: Resilient Architectures | 26% | 17 | compute (ASG, placement), load-balancing-scaling, databases (Multi-AZ, replicas), integration-messaging (SQS/SNS), dr-architecture |
| 3: High-Performing | 24% | 15 | databases (ElastiCache, DynamoDB perf), storage (EBS types, S3 performance), data-analytics, networking (CloudFront, Global Accelerator), serverless (Lambda) |
| 4: Cost-Optimized | 20% | 13 | compute (purchasing options, Spot), storage (lifecycle, tiers), databases (Aurora Serverless, DynamoDB on-demand), serverless (Lambda pricing), dns (Route 53) |

## Question Generation

1. Record start time: `date +%s`
2. Calculate time limit: `time_limit_minutes = 130` (matches real SAA-C03 exam: 130 min for 65 questions = 2 min each)
   Display: `⏱ Time limit: 130 min (real SAA-C03 exam time)`
3. Generate all 65 questions following exam domain weights
3. Mix question types: ~80% single-select, ~20% multi-select (select TWO)
4. Difficulty: 20% easy, 40% medium, 40% hard
5. Include cross-domain questions (~30% of total)
6. Self-verify all questions before presenting

## Batched Presentation (blocks of 5)

Present questions in blocks of 5 (13 blocks total). Each block:

**Block start:** Show block header
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Block {B}/13 — Questions {start}-{end} of 65
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Per question within block:** Follow standard quiz-flow (Step 1: text, Step 2: AskUserQuestion, Step 3: feedback)

**Block end:** Show running score with timer
```
Block {B} complete: {block_correct}/5
Running total: {total_correct}/{questions_done} ({pct}%)
Target: ≥72% (47/65)
⏱ {elapsed_min} min / 130 min limit — {remaining_min} min remaining
```

## Timer

- Record `date +%s` at start and after each block
- Show elapsed time at each block boundary
- Time limit: 130 min (matches real SAA-C03 exam). Advisory — do not force-stop.
- If elapsed exceeds 130 min, show `⚠️ TIME'S UP` warning but allow continuation
- At end, show total time vs 130-minute limit

## Post-Exam Analysis

After all 65 questions:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MOCK EXAM RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Score: {correct}/65 ({pct}%)
Time: {elapsed} min / 130 min limit {within_limit ? "✓" : "⚠️ over limit"}
Result: {PASS ≥72% | BORDERLINE 65-71% | FAIL <65%}

By Exam Domain:
  Domain 1 (Secure):          {n}/20 ({pct}%) {status_symbol}
  Domain 2 (Resilient):       {n}/17 ({pct}%) {status_symbol}
  Domain 3 (High-Performing): {n}/15 ({pct}%) {status_symbol}
  Domain 4 (Cost-Optimized):  {n}/13 ({pct}%) {status_symbol}

By Service Domain:
  {each service domain with questions}: {n}/{total} ({pct}%)

Weakest Topics: {top 5 missed topic slugs}
Strongest Topics: {top 5 perfect topic slugs}

Recommendation:
  {if FAIL: "Focus on Domain {weakest} — study {specific domains}"}
  {if BORDERLINE: "Close to passing — drill weak topics: {list}"}
  {if PASS: "Ready for the real exam. Review these edge cases: {list}"}
```

## Session File

Save to: `aws-csa/study-sessions/{YYMMDD}-{HHMM}-mock-exam.md`
Include all 65 questions with full details (same format as mini-exam session file).
