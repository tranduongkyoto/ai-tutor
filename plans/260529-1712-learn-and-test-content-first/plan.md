---
title: "Learn-and-Test Content-First Flow"
description: "Split learn-and-test into content generation then interactive quiz so mermaid diagrams render in IDEA"
status: done
priority: P2
effort: "1h"
branch: "master"
tags: [ai-tutor, skill-update, ux]
blockedBy: []
blocks: []
created: "2026-05-29T10:29:14.484Z"
createdBy: "ck:plan"
source: skill
---

# Learn-and-Test Content-First Flow

## Overview

Mermaid diagrams in learn-and-test mode render as raw text in CLI terminal. Restructure the mode to generate full content .md file first (viewable in IntelliJ IDEA), then run quiz interactively and append results.

## Brainstorm Report

- [brainstorm-260529-1712-learn-and-test-content-first-flow-report.md](../reports/brainstorm-260529-1712-learn-and-test-content-first-flow-report.md)

## Phases

| Phase | Name | Status | Effort |
|-------|------|--------|--------|
| 1 | [Update prompt-templates.md](./phase-01-update-prompt-templates-md.md) | Done | 30m |
| 2 | [Update quiz-flow.md](./phase-02-update-quiz-flow-md.md) | Done | 15m |
| 3 | [Update SKILL.md](./phase-03-update-skill-md.md) | Done | 15m |

## Dependencies

- Phase 1 is the main change (prompt template restructure)
- Phase 2 updates the quiz cycle to reference content-first variant
- Phase 3 is a small annotation change — can run after Phase 1
- No cross-plan dependencies

## Execution Order

`Phase 1 → (Phase 2 ∥ Phase 3)`

## Validation Log

### Session 1 — 2026-05-29
**Trigger:** Pre-implementation validation
**Questions asked:** 3

#### Verification Results
- Claims checked: 10
- Verified: 10 | Failed: 0 | Unverified: 0
- Tier: Standard (3 phases)
- Failures: none — all file paths, line numbers, and content references match live codebase

#### Questions & Answers

1. **[Architecture]** Quiz results section format — section headers or flat numbered list?
   - Options: Section headers (Recommended) | Flat numbered list
   - **Answer:** Section headers — `## Quiz Results → ### Section {N}: {name} → Q1, Q2...`
   - **Rationale:** Matches content sections for easy cross-reference in IDEA side-by-side

2. **[Scope]** Any signal to user before quiz starts after content generation?
   - Options: File saved message only (Recommended) | Add 'Starting quiz...' separator
   - **Answer:** File saved message only — show `📄 Content saved to {file}. Open in IDEA.` then immediately start Q1
   - **Rationale:** Minimal friction; user can open file anytime during quiz

3. **[Tradeoffs]** Should content generation output to terminal AND file, or file-only?
   - Options: Output to terminal AND file (Recommended) | Write file silently | Summary only
   - **Answer:** Output to terminal AND file — same as concept-mapper behavior
   - **Rationale:** User sees content scrolling (raw mermaid in terminal) + file renders in IDEA. Consistent with existing modes.

#### Confirmed Decisions
- Quiz results: section-grouped under `## Quiz Results` with `### Section {N}` headers
- Quiz start: file-saved message only, no separate "ready?" prompt or separator
- Terminal output: full content displayed in terminal AND written to file (dual output)

#### Impact on Phases
- Phase 1: Session File Format must use section-grouped quiz results; Instructions must specify dual output (terminal + file)
- Phase 2: Quiz Phase description must reference section-grouped append pattern
- Phase 3: No impact (annotation-only changes)

### Whole-Plan Consistency Sweep
- Files reread: plan.md, phase-01, phase-02, phase-03
- Decision deltas checked: 3
- Reconciled stale references: 0
- Unresolved contradictions: 0
