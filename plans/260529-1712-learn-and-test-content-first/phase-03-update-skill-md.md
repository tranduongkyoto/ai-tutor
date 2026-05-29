---
phase: 3
title: "Update SKILL.md"
status: pending
priority: P2
effort: "15m"
dependencies: [1]
---

# Phase 3: Update SKILL.md

## Overview

Add a note in Step 3 (Execute Mode) that learn-and-test writes the content file before starting the quiz, so the user can open it in IDEA for rendered mermaid diagrams.

## Related Code Files

- Modify: `.claude/skills/ai-tutor/SKILL.md` (Step 3 section, around line 199)

## Implementation Steps

1. **Add content-first note after the mode table** (after line 199, before "Guided mode scope mapping"):

   Add a brief note:
   ```
   **learn-and-test content-first flow:** This mode writes full content (all 7 sections with diagrams) to the session file BEFORE starting the interactive quiz. This lets the user open the .md in IntelliJ IDEA to see rendered mermaid diagrams while answering quiz questions. Quiz results are appended to the same file after completion.
   ```

2. **Update the Guided mode scope mapping** Phase 1 description (line 191):
   - From: `section-by-section teach + quiz with hints (no scope param — sections defined by template)`
   - To: `content-first: generates all sections to .md file, then runs quiz with hints (no scope param)`

## Success Criteria

- [ ] Step 3 explains content-first flow for learn-and-test
- [ ] Guided mode scope mapping Phase 1 description updated
- [ ] No other sections affected
