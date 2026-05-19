---
phase: 4
title: Full Mock Exam Mode
status: completed
priority: P2
effort: 60m
dependencies:
  - 1
  - 3
---

# Phase 4: Full Mock Exam Mode

## Overview

Add new `mock-exam` mode — 65 questions across ALL studied domains, weighted by SAA-C03 exam domain percentages. Timed experience with comprehensive post-exam analysis by exam domain.

## Requirements

- Functional: 65 questions, exam-domain weighting, timer, batched presentation (5 per block), post-exam analysis
- Non-functional: requires ≥8/12 domain caches, backward compatible

## Architecture

```
Prerequisite check (≥8 domain caches exist?)
  → Load: cheat sheet cache + all available domain caches
    → Generate 65 questions weighted by exam domain:
        Domain 1 (Secure): ~20 questions
        Domain 2 (Resilient): ~17 questions
        Domain 3 (High-Performing): ~15 questions
        Domain 4 (Cost-Optimized): ~13 questions
      → Present in blocks of 5 via AskUserQuestion
        → Track time per block
          → Post-exam analysis by exam domain + service domain
```

## Related Code Files

- Create: `.claude/skills/ai-tutor/references/mock-exam-flow.md`
- Modify: `.claude/skills/ai-tutor/references/prompt-templates.md`
- Modify: `.claude/skills/ai-tutor/references/progress-tracking.md`
- Modify: `.claude/skills/ai-tutor/SKILL.md`

## Implementation Steps

### 1. Create `references/mock-exam-flow.md`

New file defining the 65-question batched exam protocol:

```markdown
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
2. Generate all 65 questions following exam domain weights
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

**Block end:** Show running score
```
Block {B} complete: {block_correct}/5
Running total: {total_correct}/{questions_done} ({pct}%)
Target: ≥72% (47/65)
```

## Timer

- Record `date +%s` at start and after each block
- Show elapsed time at each block boundary
- At end, show total time vs 130-minute target

## Post-Exam Analysis

After all 65 questions:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MOCK EXAM RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Score: {correct}/65 ({pct}%)
Time: {elapsed} min (target: 130 min)
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
```

### 2. Add mock-exam prompt template to `prompt-templates.md`

```markdown
## Mode: Mock Exam

### Input
- All available domain caches (read each from `cache/aws-csa-*.md`)
- Cheat sheet cache: `cache/aws-csa-cheat-sheet.md`
- Progress: `aws-csa/study-progress.md` (weak topics across all domains)

### Instructions

Generate a full SAA-C03 mock exam following the protocol in `references/mock-exam-flow.md`.

Quality rules:
- Questions must be exam-realistic — match real SAA-C03 style and difficulty
- Cover ALL studied domains proportionally within each exam domain
- Prioritize weak topics from progress data (at least 20% of questions)
- Include cross-domain questions (~30%)
- Self-verify every question before presenting
```

### 3. Update `progress-tracking.md`

Add mock exam tracking:

```markdown
# For mock-exam (stored at top-level, not per-domain):
mock_exams:
  - date: {date}
    score: {correct}
    total: 65
    time_minutes: {elapsed}
    by_exam_domain:
      secure: {score}/{total}
      resilient: {score}/{total}
      high_performing: {score}/{total}
      cost_optimized: {score}/{total}
    missed_topics: [{all missed topic slugs}]
    verdict: {PASS|BORDERLINE|FAIL}
```

Add to Dashboard Format:

```markdown
Mock Exams:
  {date}: {score}/65 ({pct}%) — {verdict} — {time}min
  Weakest domain: {exam domain name}
```

### 4. Update `SKILL.md`

In mode list, add:
```
9. mock-exam — Full 65-question timed SAA-C03 mock exam (no domain needed, requires ≥8 domain caches)
```

In Argument Parsing, add:
```
| `mock-exam` | Start full mock exam (requires ≥8/12 domain caches) |
```

In Step 2 (Load Context), add mock-exam loading:
```
- mock-exam: Load ALL available domain caches + cheat sheet cache + progress data
```

In Step 3 (Execute Mode):
```
| `mock-exam` | All domain caches + cheat-sheet + mock-exam-flow.md | Yes (AskUserQuestion, batched) |
```

In Edge Cases, add:
```
- **Mock exam with <8 domain caches**: Show "Only {N}/12 domains cached. Study at least 8 domains before attempting a mock exam. Missing: {list}. Use `/ai-tutor {domain}` to start studying."
```

## Success Criteria

- [ ] `/ai-tutor mock-exam` launches successfully with ≥8 domain caches
- [ ] 65 questions generated with correct exam domain weighting (±2 questions)
- [ ] Questions presented in blocks of 5 with running score
- [ ] Timer tracks elapsed time, shown after each block
- [ ] Post-exam analysis shows breakdown by exam domain AND service domain
- [ ] Session file saved with all 65 questions + full details
- [ ] Mock exam tracked in study-progress.md under `mock_exams:`
- [ ] Prerequisite check warns if <8 domain caches

## Risk Assessment

| Risk | Mitigation |
|------|-----------|
| 65 questions = very long session (2+ hours) | Batched blocks show progress; could add save/resume in future |
| Context window pressure from loading all caches | Generate questions in exam-domain batches, loading relevant caches per batch |
| Question quality degrades at scale | Self-verify step mandatory; cross-reference with cheat sheet |
