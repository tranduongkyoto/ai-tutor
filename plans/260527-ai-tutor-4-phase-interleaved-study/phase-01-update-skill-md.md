# Phase 1: Update SKILL.md

## Context

- Parent plan: [plan.md](./plan.md)
- Brainstorm: [brainstorm-report.md](./brainstorm-report.md)
- File: `.claude/skills/ai-tutor/SKILL.md`

## Overview

- **Priority**: High (defines source-of-truth phase table)
- **Status**: complete
- **Description**: Update the main skill file to reflect 4-phase structure

## Key Insights

- SKILL.md is the entry point — all other files reference its phase definitions
- Free mode must still list concept-mapper and scenario-generator as standalone modes
- Guided mode uses the new merged modes only
- Existing completed domains unaffected (completed: true skips phase tracking)

## Requirements

### Functional
- Phase table shows 4 phases instead of 6
- Step 1b shows correct phase progression for guided mode
- Step 3 routes to new modes (learn-and-test, scenario-practice)
- Step 5 follow-up menu uses P1-P4 numbering
- Free mode retains all original modes

### Non-functional
- Backward compat with existing progress data
- Clear distinction between guided vs free mode availability

## Related Code Files

- **Modify**: `.claude/skills/ai-tutor/SKILL.md`

## Implementation Steps

1. **Fix existing bug**: Line 115 says `Phase {N}/7` — fix to `Phase {N}/4`

2. **Update Study Path table** (line ~43-53):
   Replace 6-phase table with:
   ```
   Phase 1: LEARN + TEST  → learn-and-test        (section-by-section: teach → quiz with hints)
   Phase 2: APPLY + TEST  → scenario-practice      (per-scenario: context → hint → answer → explain)
   Phase 3: DESIGN        → mini-exam:design        (architecture design decisions — MC format)
   Phase 4: FINAL EXAM    → mini-exam:comprehensive  (full domain exam — all topics)
   ```

2. **Update Recommended Study Order** (line ~63-77):
   Change `Min Phases` column: Tier 1 → "All 4", Tier 2 → "P1-P2", Tier 3 → "P1"
   Update domain recommendation logic: references to P6 become P4

3. **Update Step 1b — Mode selection** (line ~108-141):
   - Guided mode: show `Phase {N}/4` instead of `/6`
   - Phase descriptions match new mode names
   - Free mode: add learn-and-test and scenario-practice to the full mode list alongside concept-mapper and scenario-generator

4. **Update Step 2 — Load Context** (line ~146-166):
   - Add learn-and-test and scenario-practice to the list of modes requiring domain cache
   - learn-and-test also needs quiz-flow.md (for hint protocol)
   - scenario-practice needs scenario-map loaded in Step 2 (not Step 3) + cheat-sheet cache
   - Move scenario-map loading from Step 3 to Step 2 for scenario-practice mode

5. **Update Step 3 — Execute Mode** (line ~168-199):
   - Add learn-and-test to mode table: Input = "Cache + quiz-flow.md", Interactive = "Yes (AskUserQuestion)"
   - Add scenario-practice to mode table: Input = "Cache + scenario-map + cheat-sheet", Interactive = "Yes (AskUserQuestion)"
   - Update guided mode scope mapping:
     - Phase 1: learn-and-test (no scope param — sections defined by template)
     - Phase 2: scenario-practice (no scope param)
     - Phase 3: mini-exam scope=design
     - Phase 4: mini-exam scope=comprehensive

6. **Update Step 5 — Follow-Up Menu** (line ~216-248):
   - Phase references: `Phase {N}/4`, `Phase {N+1}`
   - After Phase 4 (was Phase 6): show domain completion celebration
   - Phase 4 pass threshold remains ≥80%

7. **Update Edge Cases** (line ~255-276):
   - Phase 4 passed → mark completed (was Phase 6)
   - Phase 4 failed → recommend weak phases (was Phase 6)
   - Update all `current_phase` references from max 6 to max 4

## Todo

- [ ] Update phase table (6→4)
- [ ] Update tier min-phases
- [ ] Update Step 1b guided mode display
- [ ] Update Step 2 cache loading for new modes
- [ ] Update Step 3 mode table and scope mapping
- [ ] Update Step 5 follow-up menu
- [ ] Update edge cases
- [ ] Verify free mode still lists all modes

## Success Criteria

- Guided mode shows 4 phases, correct mode names
- Free mode still offers all modes (including standalone concept-mapper, scenario-generator)
- Phase completion and advancement logic uses P1-P4
- No references to old P5/P6 numbering remain in guided mode context

## Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|------------|
| Breaking free mode by removing old modes | Medium | Keep concept-mapper/scenario-generator in free mode list |
| Inconsistent phase refs | Low | Search-and-replace all `/6` → `/4` in guided sections |

## Next Steps

After this phase: Phase 2 (prompt-templates) and Phase 3 (quiz-flow) can proceed in parallel.
