---
phase: 6
title: "Polish & Integration"
status: pending
priority: P2
effort: "1h"
dependencies: [4, 5]
---

# Phase 6: Polish & Integration

## Overview

Final integration pass: follow-up menus after sessions, edge case handling, end-to-end testing of all flows, and README documentation.

## Requirements

- Functional: Follow-up menu after every session. Graceful handling of missing data. Complete flow testing.
- Non-functional: Smooth UX with clear terminal output. No dead ends.

## Related Code Files

- Modify: `.claude/skills/ai-tutor/SKILL.md` (add Step 5 follow-up menu + edge cases)
- Create: `.claude/skills/ai-tutor/README.md`

## Implementation Steps

### 1. Add Step 5 follow-up menu

After every session completion, present via AskUserQuestion:
- "Continue studying" → return to domain/mode selection
- "View progress" → show dashboard
- "Done" → end session with summary

### 2. Handle edge cases

Add guards in SKILL.md for:
- **No progress file**: Create initial `study-progress.md` with empty YAML on first run
- **No cache file + pdf-extractor fails**: Show error message, suggest `/ai-tutor refresh {domain}`
- **Empty exam history**: Weak Spot Analyzer and Exam Strategy Coach gracefully handle no data ("No exam data yet. Start with a mini-exam to track progress.")
- **Domain with 0 sessions**: Show "Not started" in dashboard, skip readiness calculation
- **Invalid args**: Show usage help with examples

### 3. Write README.md

User-facing documentation:
- What is `/ai-tutor`
- Available modes with descriptions
- Usage examples: `/ai-tutor`, `/ai-tutor progress`, `/ai-tutor aws-csa compute concept-mapper`
- How progress tracking works
- How to refresh cache: `/ai-tutor refresh compute`
- File structure explanation

### 4. End-to-end testing

Full flow test:
1. `/ai-tutor` → menu selection → concept-mapper → verify output + progress update
2. `/ai-tutor aws-csa storage mini-exam` → 5 questions → verify scoring + progress
3. `/ai-tutor progress` → verify dashboard shows both sessions
4. `/ai-tutor aws-csa compute weak-spot-analyzer` → verify it reads progress
5. `/ai-tutor refresh compute` → verify cache re-extraction
6. Verify all session files exist in `aws-csa/study-sessions/`

### 5. Terminal output polish

- Consistent formatting across all modes
- Clear section headers and spacing
- Progress bar renders correctly
- Unicode symbols (★ ◆ ▲ △ ○) display properly
- Tables align correctly

## Success Criteria

- [ ] Follow-up menu appears after every session
- [ ] "Continue studying" loops back to selection
- [ ] Edge cases handled gracefully (no crashes on missing data)
- [ ] README.md provides clear usage instructions
- [ ] E2E test: concept-mapper → mini-exam → progress → weak-spot all work in sequence
- [ ] Session files accumulate correctly in study-sessions/
- [ ] Terminal output is clean and readable

## Risk Assessment

- **Unicode rendering**: Terminal may not support ★ ◆ etc. Low risk — most modern terminals support Unicode. Fallback: use text labels only.
