---
phase: 2
title: Keyword Pattern Drill Mode
status: completed
priority: P1
effort: 45m
dependencies:
  - 1
---

# Phase 2: Keyword Pattern Drill Mode

## Overview

Add new `keyword-drill` mode — quick-fire flash-card format that drills exam trigger phrases → correct service/pattern mappings. ~80 curated patterns from cheat sheet + 3 exam analyses.

## Requirements

- Functional: interactive drill with scoring, 10/25/all patterns per session, tracks missed patterns
- Non-functional: no domain required (cross-cutting), patterns grounded in real exams

## Architecture

```
keyword-patterns.md (static, ~80 patterns)
  + cheat-sheet cache (supplementary context)
    → AskUserQuestion per pattern (4 options, single-select)
      → score + missed patterns → progress tracking
```

## Related Code Files

- Create: `.claude/skills/ai-tutor/references/keyword-patterns.md`
- Modify: `.claude/skills/ai-tutor/references/prompt-templates.md`
- Modify: `.claude/skills/ai-tutor/references/quiz-flow.md`
- Modify: `.claude/skills/ai-tutor/references/progress-tracking.md`
- Modify: `.claude/skills/ai-tutor/SKILL.md`

## Implementation Steps

### 1. Create `references/keyword-patterns.md`

New file with ~80 trigger-word → service mappings. Organized by SAA-C03 exam domain.

Structure per pattern:
```markdown
### Pattern: {short-id}
- trigger: "{exam phrase or keyword combination}"
- answer: "{correct AWS service or pattern}"
- distractors: ["{wrong1}", "{wrong2}", "{wrong3}"]
- explanation: "{why this is correct — 1 sentence}"
- exam-domain: {1|2|3|4}
- source: {cheat-sheet|exam-1|exam-2|exam-3|common}
```

**Pattern sources to include (minimum):**

From exam analyses:
- "decouple writes to DynamoDB" → SQS as buffer
- "RabbitMQ migration to AWS" → Amazon MQ
- "unpredictable OLTP workload" → Aurora Serverless
- "Multi-AZ failover — can standby serve reads?" → No (Read Replicas for reads)
- "Redis vs Memcached" → Redis for persistence/replication/complex types; Memcached for simple/multi-threaded
- "encryption with audit trail" → SSE-KMS
- "cheapest encryption" → SSE-S3
- "Spark on AWS, minimal ops" → AWS Glue (serverless)
- "restrict S3 to CloudFront only" → OAI
- "signed URLs vs signed cookies" → URLs for individual files, cookies for multiple
- "query S3 data without loading" → Athena
- "crypto mining detection" → GuardDuty

From cheat sheet exam domains:
- "minimal operational effort" → managed/serverless
- "static IP + TCP/UDP" → NLB + Elastic IP
- "third-party virtual appliances" → GWLB
- "SMB/NFS file shares" → FSx ONTAP
- "Windows file server" → FSx for Windows
- "HPC cluster" → placement group (cluster)
- "key-value + flexible schema" → DynamoDB
- "graph data / relationships" → Neptune
- "time series data" → Timestream
- "immutable ledger" → QLDB
- "Cassandra migration" → Keyspaces
- "MongoDB migration" → DocumentDB
- "multi-region active-active" → DynamoDB Global Tables
- "data lake access control" → Lake Formation
- "real-time streaming" → Kinesis Data Streams
- "near-real-time ETL to S3" → Kinesis Data Firehose
- "serverless ETL / schema discovery" → AWS Glue
- "cross-account access + simultaneous" → resource-based policy
- "delegated admin IAM" → Permission Boundaries
- "L7 DDoS protection + cost protection" → Shield Advanced
- "multi-account WAF policy" → Firewall Manager
- "compliance audit automation" → AWS Config rules
- "API activity logging" → CloudTrail
- "sensitive data discovery in S3" → Macie
- "vulnerability scanning" → Inspector
- "cross-region DNS failover" → Route 53 failover routing
- "latency-based routing" → Route 53 latency policy
- "Backup & Restore DR" → cheapest, highest RTO/RPO
- "Pilot Light DR" → minimal core services running
- "Warm Standby DR" → scaled-down full environment
- "Multi-Region Active/Active DR" → lowest RTO/RPO, highest cost

Target: 80+ patterns across all 4 exam domains.

### 2. Add keyword-drill prompt template to `prompt-templates.md`

Append new section:

```markdown
## Mode: Keyword Drill

### Input
- Keyword patterns: loaded from `references/keyword-patterns.md`
- Cheat sheet cache: `.claude/skills/ai-tutor/cache/aws-csa-cheat-sheet.md`
- Pattern count: `{count}` (10, 25, or all)
- Progress: `aws-csa/study-progress.md` (prioritize previously missed patterns)

### Instructions

Run a quick-fire drill testing the user's ability to map exam trigger phrases to correct AWS services/patterns.

1. Load patterns from `references/keyword-patterns.md`
2. If user has previous keyword-drill sessions, prioritize missed patterns (at least 40%)
3. Shuffle selected patterns randomly
4. Present each pattern using the quiz flow from `references/quiz-flow.md` § Keyword Drill Flow
5. Score and save results

### Output Format (per pattern)
Present trigger phrase as the "question", correct service + 3 distractors as options.
After user answers, show: correct/incorrect + explanation (1 sentence).
```

### 3. Add keyword drill flow to `quiz-flow.md`

Add new section:

```markdown
## Keyword Drill Flow

Variant of the standard quiz flow optimized for quick-fire pattern recognition.

### Setup
1. Ask count via AskUserQuestion: "How many patterns?" — options: `10`, `25`, `All (~80)`
2. Load `references/keyword-patterns.md`
3. Read progress for previously missed patterns
4. Select patterns: prioritize missed (40%), random from remaining (60%)
5. Shuffle order

### Per-Pattern Cycle (same 2-step as standard quiz)

**Step 1 — Present pattern (TEXT ONLY, no AskUserQuestion):**
```
**Pattern {N}/{total}:**
"{trigger phrase from the pattern}"

A) {answer or distractor — shuffled}
B) {answer or distractor — shuffled}
C) {answer or distractor — shuffled}
D) {answer or distractor — shuffled}
```

**Step 2 — Collect answer:**
AskUserQuestion: "Your answer?" — Options: A, B, C, D — multiSelect: false

**Step 3 — Feedback (TEXT ONLY):**
```
✓ Correct! / ✗ Incorrect — correct answer: {letter}
{explanation from pattern data}
```

### Scoring
Same as standard quiz: score/total, missed patterns list.
Save missed patterns as `weak_topics` with prefix `kw:` (e.g., `kw:aurora-serverless`).
```

### 4. Update `progress-tracking.md`

In "### Step 1: Update YAML Frontmatter", add to domain-level fields:

```markdown
# For keyword-drill (stored at top-level, not per-domain):
keyword_drill:
  sessions_count: {increment}
  last_drilled: {date}
  exams:
    - date: {date}
      score: {correct}
      total: {pattern count}
      missed_patterns: [{pattern short-ids}]
  weak_patterns: [{cumulative missed, same removal rule as weak_topics}]
```

In Session History format, add:

```markdown
For keyword-drill:
### {YYYY-MM-DD} {HH:MM} | Cross-Domain | Keyword Drill
- Score: {score}/{total} ({pct}%)
- Missed: {pattern short-ids}
- Output: study-sessions/{filename}
```

### 5. Update `SKILL.md`

In mode list (Step 1b, free mode), add:
```
8. keyword-drill — Quick-fire exam keyword → service mapping drill (no domain needed)
```

In Argument Parsing table, add:
```
| `keyword-drill` | Start keyword pattern drill (no domain needed) |
```

In optional tools list, add `keyword-drill`.

In Step 2 (Load Context), add keyword-drill to modes that need cheat-sheet cache but NOT domain cache.

In Step 3 (Execute Mode) table, add:
```
| `keyword-drill` | keyword-patterns.md + cheat-sheet cache | Yes (AskUserQuestion) |
```

## Success Criteria

- [ ] `references/keyword-patterns.md` contains ≥80 patterns across 4 exam domains
- [ ] `/ai-tutor keyword-drill` launches without requiring a domain
- [ ] Pattern count selection works (10/25/all)
- [ ] Missed patterns tracked in `study-progress.md` under `keyword_drill:`
- [ ] Previously missed patterns prioritized in subsequent sessions

## Risk Assessment

| Risk | Mitigation |
|------|-----------|
| Distractor options too easy | Self-verify: each distractor must be a real AWS service that could plausibly answer the trigger |
| Patterns become outdated | Grounded in real exam analyses; easy to extend by adding to keyword-patterns.md |
