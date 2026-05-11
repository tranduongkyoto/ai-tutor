---
phase: 5
title: "Progress Tracking & Dashboard"
status: pending
priority: P1
effort: "2h"
dependencies: [3]
---

# Phase 5: Progress Tracking & Dashboard

## Overview

Implement the progress tracking system: update `study-progress.md` after every session, compute readiness scores dynamically, and display the progress dashboard via `/ai-tutor progress`.

## Requirements

- Functional: Track sessions, exam scores, weak topics per domain. Compute readiness with weighted formula. Display formatted dashboard.
- Non-functional: Append-only session log. YAML frontmatter for structured data. Readiness computed dynamically (never stored).

## Architecture

### study-progress.md Structure
```yaml
---
certification: aws-csa
exam_code: SAA-C03
started: 2026-05-11
last_session: 2026-05-15
total_sessions: 8
domains:
  compute:
    sessions_count: 5
    modes_completed: [concept-mapper, scenario-generator, mini-exam, hands-on-lab]
    exams:
      - date: 2026-05-11
        score: 7
        total: 10
        missed_topics: [placement-groups, spot-fleets]
    weak_topics: [hibernate]
    last_studied: 2026-05-15
  # ... remaining domains
---

## Session History

### 2026-05-15 10:30 | Compute | Mini Exam
- Score: 9/10 (90%)
- Missed: hibernate
- Output: study-sessions/260515-1030-compute-exam.md
```

### Readiness Formula
```
readiness = (coverage * 0.3) + (exam_avg * 0.5) + (recency * 0.2)

coverage  = modes_completed.length / 6 * 100
exam_avg  = average of last 2 exam scores (percentage), or 0 if no exams
recency   = 100 if last_studied <= 7 days ago
            linear decay 100→0 between day 7 and day 30
            0 if last_studied > 30 days ago or never studied
```

## Related Code Files

- Modify: `.claude/skills/ai-tutor/references/progress-tracking.md` (fill with tracking protocol)
- Modify: `.claude/skills/ai-tutor/SKILL.md` (add Step 4 save/track + progress command)
- Modify: `aws-csa/study-progress.md` (updated after each session)

## Implementation Steps

### 1. Write progress-tracking.md protocol

Fill `references/progress-tracking.md` with:

**Update Protocol (after every session):**
1. Read current `aws-csa/study-progress.md`
2. Update YAML frontmatter:
   - Increment `total_sessions`
   - Update `last_session` date
   - Update `started` if null (first session)
   - For the domain studied:
     - Increment `sessions_count`
     - Add mode to `modes_completed` if not present
     - Update `last_studied`
     - If mini-exam: append exam entry with score, total, missed_topics
     - Update `weak_topics`: merge missed topics from latest exam, remove topics scored correctly in last 2 exams
3. Append session entry to `## Session History` section:
   ```
   ### {date} {time} | {Domain} | {Mode}
   - Score: X/Y (Z%)  ← only for mini-exam
   - Topics: [list]   ← for non-exam modes
   - Output: study-sessions/{filename}
   ```

**Readiness Calculation (dynamic):**
- Parse YAML frontmatter for each domain
- Compute per-domain readiness using formula
- Compute overall readiness as average of all 12 domains
- Apply status thresholds: >=80% mastered, 60-79% proficient, 30-59% developing, 1-29% beginning, 0% not started

### 2. Implement progress dashboard

`/ai-tutor progress` displays:

```
AWS CSA (SAA-C03) - Study Progress
Started: {date} | Last: {date} | Sessions: {n}
Overall Readiness: {pct}%  {progress bar}  {studied}/{total} domains

Domain              Ready  Exams  Last     Status
────────────────── ────── ────── ──────── ──────────
Compute             85%    3      2d ago   ★ Mastered
Storage             62%    2      3d ago   ◆ Proficient
...

Weak Areas: {comma-separated list of all weak_topics}
Recommended Next: {domain} ({reason})
```

Progress bar: 20 chars wide, `█` for filled, `░` for empty.
Status symbols: ★ ◆ ▲ △ ○

### 3. Add Step 4 (Save & Track) to SKILL.md

After every mode execution:
1. Read `references/progress-tracking.md` for update protocol
2. Write session file to `aws-csa/study-sessions/`
3. Update `aws-csa/study-progress.md` (YAML + session log)
4. Show recommendation for next study action

### 4. Implement recommendation engine

After each session, suggest next action based on:
- Lowest readiness domain that has been started
- Domain not yet started (if all started domains are proficient+)
- Stale domains (>7 days since last study)
- Weak topics that need mini-exam retesting

Format: "Recommended Next: {Domain} - {Mode} ({reason})"

## Success Criteria

- [ ] progress-tracking.md contains complete update protocol and readiness formula
- [ ] YAML frontmatter updates correctly after concept-mapper session
- [ ] YAML frontmatter updates correctly after mini-exam (includes score + missed topics)
- [ ] Readiness formula produces correct values for sample data
- [ ] Recency decay works: 100% at day 0-7, decays to 0 at day 30
- [ ] `/ai-tutor progress` displays formatted dashboard with all 12 domains
- [ ] Weak topics aggregate across all domains
- [ ] Recommendation engine suggests actionable next step

## Risk Assessment

- **YAML parsing**: Claude reads/writes YAML in markdown. Complex nested structures may cause formatting issues. Mitigation: provide exact YAML format in protocol.
- **Recency calculation**: Requires current date. Use `bash -c 'date +%Y-%m-%d'` to get today's date for accurate day-diff calculation.
