---
title: Fix P3 Cross-Domain Asymmetry in AI Tutor Skill
description: >-
  Gate cross-domain questions on studied domains (Fix A) and ground questions in
  loaded caches (Fix B)
status: completed
priority: P1
branch: master
tags:
  - ai-tutor
  - bug-fix
blockedBy: []
blocks: []
created: '2026-06-02T04:28:30.445Z'
createdBy: 'ck:plan'
source: skill
---

# Fix P3 Cross-Domain Asymmetry in AI Tutor Skill

## Overview

P3 design mini-exam can test cross-domain concepts (SQS buffer, Route 53 latency routing, Step Functions Map state) that P1/P2 never taught because: (1) P1/P2 are grounded in domain-specific cache, (2) P3 questions draw from LLM general knowledge, (3) cross-domain concepts belong to domains the user may not have studied.

Three changes applied together:
- **Fix A** — Gate cross-domain questions on actually-studied domains via study-progress.md
- **Fix B** — Ground ALL P3/P4 questions in loaded cache content only
- **Fix C** — Add cheat sheet to P1 (learn-and-test) so cross-domain patterns are taught before tested

**Principle:** Everything testable in P3/P4 must have been teachable in P1/P2.

## Root Cause

See: `plans/reports/serverless-phase3-gap-analysis.md`

## Files Modified

| File | Change |
|------|--------|
| `.claude/skills/ai-tutor/certs/aws-csa/scenario-map.md` | Add `### cross-domain-topics` mapping per domain |
| `.claude/skills/ai-tutor/references/prompt-templates.md` | P1 cheat sheet usage + P3/P4 gating rule + content grounding rule |
| `.claude/skills/ai-tutor/SKILL.md` | P1 cheat sheet loading + mini-exam cross-domain cache loading |

## Phases

| Phase | Name | Status |
|-------|------|--------|
| 1 | [Implement Fix A+B](./phase-01-implement-fix-a-b.md) | Completed |
