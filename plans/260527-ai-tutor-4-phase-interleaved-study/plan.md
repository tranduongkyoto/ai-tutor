---
title: "AI Tutor 4-Phase Interleaved Study Path"
description: "Merge 6-phase study path into 4 interleaved phases for better retention"
status: complete
priority: P2
effort: 2h
branch: master
tags: [ai-tutor, skill-update, learning-design]
created: 2026-05-27
---

# AI Tutor: 4-Phase Interleaved Study Path

## Summary

Merge current 6-phase guided study into 4 phases by interleaving learning with testing. P1+P2 → learn-and-test (section-by-section teach+quiz with hints), P3+P4 → scenario-practice (per-scenario interactive loop with hints). P5/P6 → P3/P4 (unchanged).

## Brainstorm Report

- [brainstorm-report.md](./brainstorm-report.md)

## Phases

| # | Phase | Status | Files | Effort |
|---|-------|--------|-------|--------|
| 1 | [Update SKILL.md](./phase-01-update-skill-md.md) | complete | SKILL.md | 30m |
| 2 | [Update prompt-templates.md](./phase-02-update-prompt-templates.md) | complete | prompt-templates.md | 45m |
| 3 | [Update quiz-flow.md](./phase-03-update-quiz-flow.md) | complete | quiz-flow.md | 25m |
| 4 | [Update progress-tracking.md](./phase-04-update-progress-tracking.md) | complete | progress-tracking.md | 20m |

## Dependencies

- Phase 2 and 3 can run in parallel (independent files)
- Phase 4 depends on phase 1 (needs final phase numbering)
- Phase 1 should go first (defines the source-of-truth phase table)

## Execution Order

`Phase 1 → (Phase 2 ∥ Phase 3) → Phase 4`

## Validation Log

### Session 1 — 2026-05-27
**Trigger:** Pre-implementation validation
**Questions asked:** 4

#### Verification Results
- Claims checked: 8
- Verified: 6 | Failed: 1 | Unverified: 1
- Tier: Standard (4 phases)
- Failures: SKILL.md:115 says `Phase {N}/7` — should be `/6`, plan fixes to `/4`

#### Questions & Answers

1. **[Migration]** load-balancing-scaling at old Phase 4 (p2:90, p4:90). How to handle?
   - Options: Map to new P2 complete | Reset to P1 | Keep as-is
   - **Answer:** Map to new P2 complete — set current_phase:2, phase_scores: {p1:90, p2:90}
   - **Rationale:** Domain completed the equivalent of new P1+P2; no reason to lose progress

2. **[Scope]** Write migration rules for ALL in-progress domains or case-by-case?
   - Options: Add migration rules for all | Handle case-by-case
   - **Answer:** Case-by-case — only load-balancing-scaling and databases are in-progress
   - **Rationale:** Only 2 domains affected; generic migration rules add unnecessary complexity

3. **[Architecture]** Should scenario-practice load scenario-map in Step 2 or Step 3?
   - Options: Step 2 (with other inputs) | Step 3 (current pattern)
   - **Answer:** Step 2 — consistent with "load all inputs in Step 2, execute in Step 3"
   - **Rationale:** Cleaner separation of concerns

4. **[Bug fix]** SKILL.md line 115 has `/7` typo. Fix as part of this plan?
   - Options: Yes, fix to /4 | Fix separately
   - **Answer:** Yes, fix to /4 — include in Phase 1
   - **Rationale:** Trivial fix, no reason to create separate work

#### Confirmed Decisions
- In-progress migration: case-by-case, not generic rules
- Scenario-map: load in Step 2
- Bug fix: include in Phase 1

#### Impact on Phases
- Phase 1: Add bug fix step (line 115 `/7` → `/4`), update Step 2 for scenario-map
- Phase 4: Add case-by-case migration for load-balancing-scaling and databases

### Whole-Plan Consistency Sweep
- All phase files reference 4-phase numbering consistently
- No stale references to 6-phase system in plan files
- Phase 2 and Phase 3 correctly reference hint flow protocol (DRY)
- Unresolved contradictions: 0
