# Phase 4: Update progress-tracking.md

## Context

- Parent plan: [plan.md](./plan.md)
- File: `.claude/skills/ai-tutor/references/progress-tracking.md`
- Depends on: Phase 1 (final phase numbering confirmed)

## Overview

- **Priority**: Medium
- **Status**: complete
- **Description**: Update progress tracking to 4-phase numbering

## Key Insights

- Existing completed domains keep old format — no migration
- Only in-progress and new domains use new numbering
- Readiness formula coverage calculation changes: `/4` instead of `/6`
- Dashboard phase column changes from `X/6` to `X/4`

## Requirements

### Functional
- Phase numbering: P1-P4 (was P1-P6)
- phase_scores keys: p1, p2, p3, p4
- modes_completed values: learn-and-test, scenario-practice, mini-exam:design, mini-exam:comprehensive
- Coverage formula: `current_phase / 4` (was `/6`)
- Dashboard: `X/4` in Phase column
- Backward compat note for old data
- Recommendation engine uses P1-P4

### Non-functional
- Readiness formula weights unchanged (0.3 coverage + 0.5 exam + 0.2 recency)

## Related Code Files

- **Modify**: `.claude/skills/ai-tutor/references/progress-tracking.md`

## Implementation Steps

1. **Update YAML schema** (Step 1):
   - `current_phase: {1-4, advance after completing a guided phase; default 1}`
   - `phase_scores: {p1: learn-and-test score, p2: scenario-practice score, p3: design score, p4: comprehensive score}`
   - `modes_completed: {append mode slug}` — new slugs: learn-and-test, scenario-practice

2. **Add backward compatibility note**:
   ```
   ## Backward Compatibility
   Domains with `completed: true` retain old 6-phase format (p2/p4/p5/p6 keys).
   New domains use 4-phase format (p1/p2/p3/p4 keys).
   When displaying old completed domains: show as "4/4" in dashboard (they finished all phases).
   ```

   **In-progress domain migration (case-by-case)**:
   - `load-balancing-scaling` (old current_phase:4, scores p2:90, p4:90): Map to new current_phase:2, phase_scores: {p1:90, p2:90}. It completed the equivalent of new P1 (learn+test) and P2 (scenario+test).
   - `databases` (old current_phase:1, only concept-mapper done): Reset to new current_phase:1, no scores to preserve. Will redo P1 with new learn-and-test format.
   - Update `study-progress.md` directly during implementation.

3. **Update Readiness Formula — Coverage**:
   ```
   coverage = (current_phase / 4) * 100
   ```
   - Each phase adds 25% (was ~16.7%)
   - Fallback for free mode: `(modes_completed.length / 4) * 100` (cap at 100%)
   - For old completed domains: coverage = 100%

4. **Update Dashboard Format**:
   - Phase column: `X/4` instead of `X/6`
   - Example rows updated accordingly

5. **Update Recommendation Engine**:
   - All phase references: P1-P4
   - Phase 4 passed ≥80% → completed (was Phase 6)
   - Phase 4 failed → recommend weak phases + retake

6. **Update Session History format**:
   - learn-and-test sessions: `| {Domain} | Learn and Test`
   - scenario-practice sessions: `| {Domain} | Scenario Practice`

## Todo

- [ ] Update YAML schema (current_phase 1-4, phase_scores p1-p4)
- [ ] Add backward compatibility note
- [ ] Update coverage formula (/4 instead of /6)
- [ ] Update dashboard format (X/4)
- [ ] Update recommendation engine (P1-P4)
- [ ] Update session history format for new modes
- [ ] Verify readiness formula weights unchanged

## Success Criteria

- New domains tracked with P1-P4 numbering
- Old completed domains display correctly as 4/4
- Coverage formula uses /4
- Dashboard shows correct phase column
- Recommendation engine references correct phase numbers

## Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|------------|
| Old p2/p4/p5/p6 keys confuse readiness calc | Low | Completed domains → coverage=100%, skip phase calc |
| In-progress domain (databases, current_phase:1) | Low | Reset to new P1 — only concept-mapper done, no exam score to lose |
