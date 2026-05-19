---
title: AI Tutor v2.1 — Exam-Aligned Enhancements
description: >-
  Add cheat sheet integration, keyword pattern drills, cross-domain questions,
  and full mock exam mode to close the gap between domain-specific study
  (80-90%) and real exam performance (37.5%)
status: pending
priority: P1
branch: master
tags:
  - ai-tutor
  - aws-csa
  - exam-prep
blockedBy: []
blocks: []
created: '2026-05-19T10:19:02.922Z'
createdBy: 'ck:plan'
source: skill
---

# AI Tutor v2.1 — Exam-Aligned Enhancements

## Overview

Enhance the AI tutor skill with 4 features to bridge the gap between domain-specific mini-exam scores (80-90%) and real exam performance (37.5%). Based on analysis of 3 practice exams and the AWS SAA Master Cheat Sheet (48 pages).

**Brainstorm report:** `plans/260519-1711-ai-tutor-exam-aligned-enhancements/brainstorm-report.md`

## Key Insights from Exam Analysis

- ~25% of real exam questions span 2+ service domains — tutor tests one at a time
- 48-page cheat sheet with exam-focused decision frameworks sits unused
- No full-length exam simulation (real: 65 questions, 130 min, all domains)
- Exam uses keyword triggers the tutor doesn't drill systematically

## Phases

| Phase | Name | Status | Priority | Effort | Dependencies |
|-------|------|--------|----------|--------|-------------|
| 1 | [Cheat Sheet Integration](./phase-01-cheat-sheet-integration.md) | Pending | P1 | 30m | Completed |
| 2 | [Keyword Pattern Drill Mode](./phase-02-keyword-pattern-drill-mode.md) | Pending | P1 | 45m | Completed |
| 3 | [Cross-Domain Question Injection](./phase-03-cross-domain-question-injection.md) | Pending | P1 | 30m | Completed |
| 4 | [Full Mock Exam Mode](./phase-04-full-mock-exam-mode.md) | Pending | P2 | 60m | Completed |

## Phasing Strategy

**Phase 1-3 = immediate exam prep** (ship together, ~1.5h total)
**Phase 4 = after more domains studied** (needs ≥8/12 domain caches)

## File Change Matrix

| File | P1 | P2 | P3 | P4 |
|------|----|----|----|----|
| `SKILL.md` | ✓ | ✓ | — | ✓ |
| `certs/aws-csa/domains.md` | ✓ | — | — | — |
| `references/pdf-extractor.md` | ✓ | — | — | — |
| `references/prompt-templates.md` | ✓ | ✓ | ✓ | ✓ |
| `references/quiz-flow.md` | — | ✓ | ✓ | — |
| `references/progress-tracking.md` | — | ✓ | — | ✓ |
| `references/keyword-patterns.md` | — | ✓ (new) | — | — |
| `references/mock-exam-flow.md` | — | — | — | ✓ (new) |

## Dependencies

No cross-plan dependencies. Original AI tutor plan (`260511-1048`) is complete.
