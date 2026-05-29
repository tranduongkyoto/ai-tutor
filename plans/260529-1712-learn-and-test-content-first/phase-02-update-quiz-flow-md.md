---
phase: 2
title: "Update quiz-flow.md"
status: pending
priority: P2
effort: "15m"
dependencies: [1]
---

# Phase 2: Update quiz-flow.md

## Overview

Update the Section Quiz Cycle (lines 221-236) to reflect content-first flow — quiz runs after all content is generated and written to file.

## Related Code Files

- Modify: `.claude/skills/ai-tutor/references/quiz-flow.md` (§ Section Quiz Cycle, lines 221-236)

## Implementation Steps

1. **Rename section** from "Section Quiz Cycle (learn-and-test mode)" to "Section Quiz Cycle — Content-First (learn-and-test mode)"

2. **Replace Per-Section Flow** (lines 225-229) with:

   **Content Phase (runs first, all sections):**
   1. Generate all 7 sections with full content (same quality as concept-mapper — diagrams, tables, bold terms)
   2. Write to session file
   3. Show: `📄 Content saved to {file}. Open in IDEA to study with rendered diagrams.`

   **Quiz Phase (runs after content is written):**
   <!-- Updated: Validation Session 1 - section-grouped append pattern confirmed -->
   For each section (1-7):
   1. Generate 2-3 questions on that section's material
   2. Run each question through the Hint Flow Protocol
   3. After section's questions: `Section {N}/7 complete: {X}/{Y} correct`
   4. Append quiz results to session file under `## Quiz Results → ### Section {N}: {name}` (section headers mirror content sections for cross-reference)

3. **Keep "After All 7 Sections" unchanged** (lines 232-235) — aggregate score logic stays the same

## Success Criteria

- [ ] Section Quiz Cycle describes content-first, quiz-after flow
- [ ] Hint Flow Protocol reference preserved
- [ ] Aggregate scoring logic unchanged
- [ ] No references to interleaved content+quiz per section remain
