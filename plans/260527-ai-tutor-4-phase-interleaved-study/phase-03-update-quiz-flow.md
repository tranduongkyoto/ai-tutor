# Phase 3: Update quiz-flow.md

## Context

- Parent plan: [plan.md](./plan.md)
- File: `.claude/skills/ai-tutor/references/quiz-flow.md`
- Can run in parallel with Phase 2

## Overview

- **Priority**: Medium
- **Status**: complete
- **Description**: Add hint flow protocol and section/scenario quiz cycles

## Key Insights

- Current quiz flow uses a strict 2-step cycle (question → answer → feedback) — works well
- New hint flow adds a step: question → hint → answer → feedback (3-step)
- Standard quiz flow stays for design/comprehensive exams (P3, P4)
- Keyword Drill flow stays unchanged

## Requirements

### Functional
- Hint Flow Protocol: defines how hints are presented between question and answer
- Section Quiz Cycle: how learn-and-test mode interleaves sections with quizzes
- Scenario Practice Cycle: how scenario-practice mode runs per-scenario loops
- No changes to standard quiz flow or keyword drill flow

## Related Code Files

- **Modify**: `.claude/skills/ai-tutor/references/quiz-flow.md`

## Implementation Steps

1. **Add "Hint Flow Protocol" section** (before Keyword Drill Flow):

   ```markdown
   ## Hint Flow Protocol

   Extended quiz cycle used by learn-and-test and scenario-practice modes.
   Adds a hint step between question presentation and answer collection.

   ### Per-Question Cycle (4 steps, 3 turns)

   **Step 1 — Present question (TEXT ONLY, no AskUserQuestion):**
   Show question text + all 4 options (A-D). NEVER reveal answer.

   **Step 2 — Show hint (TEXT ONLY, same turn as Step 1):**
   Show hint immediately after options:
   ```
   💡 Hint: {1-sentence directional nudge}
   ```

   Hint rules:
   - 1 sentence, points toward the AWS concept being tested
   - NEVER mention the correct option letter
   - NEVER repeat any option text verbatim
   - NEVER give away the answer directly
   - Focus on the architectural pattern, service category, or design principle

   **Step 3 — Collect answer (AskUserQuestion):**
   Same as standard flow: "Your answer?" with A, B, C, D options.

   **Step 4 — Feedback (TEXT ONLY, new turn):**
   Same as standard flow: ✓/✗ + explanation.
   ```

2. **Add "Section Quiz Cycle" section** (for learn-and-test):

   ```markdown
   ## Section Quiz Cycle (learn-and-test mode)

   Flow for Phase 1 guided mode. Processes 7 concept sections sequentially.

   ### Per-Section Flow
   1. Output full section content (same quality as concept-mapper)
   2. Generate 2-3 questions on that section's material
   3. Run each question through the Hint Flow Protocol (above)
   4. After section's questions: brief "Section {N}/7 complete: {X}/{Y} correct"
   5. Proceed to next section

   ### After All 7 Sections
   - Aggregate score: {total_correct}/{total_questions} ({pct}%)
   - List missed topics by topic slug
   - No separate "question count" prompt — count is determined by sections (2-3 per section)
   ```

3. **Add "Scenario Practice Cycle" section** (for scenario-practice):

   ```markdown
   ## Scenario Practice Cycle (scenario-practice mode)

   Flow for Phase 2 guided mode. Processes scenarios from scenario-map.

   ### Per-Scenario Flow
   1. Show: Business Context + Requirements + Question + 4 Options (answer HIDDEN)
   2. Show hint (same turn): 💡 Hint: {nudge toward correct pattern}
   3. Collect answer via AskUserQuestion
   4. Reveal (new turn):
      - ✓/✗ + correct answer letter
      - Detailed explanation
      - Architecture diagram (Mermaid `graph TD`, max 10 nodes)
      - Why each wrong option fails (1 sentence each)
   5. Proceed to next scenario

   ### After All Scenarios
   - Aggregate score: {correct}/{total} ({pct}%)
   - List missed topics
   ```

4. **Update Setup section**: Add note that learn-and-test and scenario-practice skip the "question count" prompt (count determined by content, not user choice).

## Todo

- [ ] Add Hint Flow Protocol section
- [ ] Add Section Quiz Cycle section
- [ ] Add Scenario Practice Cycle section
- [ ] Update Setup section with skip-count note
- [ ] Verify standard quiz flow and keyword drill unchanged

## Success Criteria

- Hint flow clearly defines the 4-step cycle
- Section quiz cycle references hint flow (DRY)
- Scenario practice cycle references hint flow (DRY)
- Standard quiz flow for design/comprehensive exams untouched

## Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|------------|
| LLM skips hint step | Low | Bold "MANDATORY" on hint step, same pattern as existing "HARD RULE" |
| Hint shown in same turn as question | Low | Explicit "same turn" instruction in protocol |
