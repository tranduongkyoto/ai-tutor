# AI Tutor: 4-Phase Interleaved Study Path

## Problem Statement

Current 6-phase study path separates learning from testing — user reads a full concept map (P1), then takes a separate quiz (P2), then reads scenarios (P3), then quizzes again (P4). This breaks the feedback loop: by the time the quiz happens, retention of early material has faded.

**Goal**: Merge learn+test phases into interleaved sessions for tighter feedback loops and better retention.

## Requirements

- **Expected output**: Modified SKILL.md, prompt-templates.md, quiz-flow.md, progress-tracking.md
- **Acceptance criteria**: 4-phase guided path works end-to-end; existing completed domains unaffected; new domains use new flow
- **Scope boundary**: P3 (design exam) and P4 (final exam) unchanged. No migration of old progress data.
- **Constraints**: Must work within Claude context window; session files remain study reference material
- **Touchpoints**: SKILL.md, references/prompt-templates.md, references/quiz-flow.md, references/progress-tracking.md

## Design

### Phase Structure: 6 → 4

| Phase | Name | Mode Key | Description |
|-------|------|----------|-------------|
| P1 | LEARN + TEST | `learn-and-test` | Section-by-section: teach section → 2-3 Qs with hints → next section. 7 rounds, ~15-20 Qs total |
| P2 | APPLY + TEST | `scenario-practice` | Per-scenario: show context + options → hint → user answers → reveal + explain → next |
| P3 | DESIGN | `mini-exam:design` | Unchanged — architecture design MC exam |
| P4 | FINAL EXAM | `mini-exam:comprehensive` | Unchanged — full domain comprehensive exam |

### P1: learn-and-test — Detailed Flow

```
For each section in concept-mapper template (7 sections):
  1. Output section content (Service Overview, Use Cases, etc.)
  2. Generate 2-3 questions on that section
     - Mix: ~60% fact-based, ~40% scenario-based
     - 4 options (A-D) per question
  3. Per question:
     a. Show question + options (answer hidden)
     b. Show hint: 1-sentence nudge toward the right concept (NOT the answer)
     c. User picks via AskUserQuestion
     d. Reveal: correct/incorrect + explanation
  4. Move to next section
After all 7 sections:
  - Show aggregate score: X/Y (Z%)
  - List missed topics
  - Save session file with full content + Q&A
  - Update progress: advance to P2
```

**Hint quality rules**:
- Hint = directional nudge, not answer. E.g., "Think about which service handles container orchestration without EC2 management"
- Never mention the correct option letter
- Never repeat option text verbatim
- Reference the AWS concept/pattern being tested

**Session file format**: Full concept material + embedded Q&A per section — serves as combined study reference.

### P2: scenario-practice — Detailed Flow

```
Load scenario-map for domain (8-15 scenarios)
For each scenario:
  1. Show: Business Context + Requirements + Question + 4 Options (answer hidden)
  2. Show hint: 1-2 sentence nudge toward correct pattern
     E.g., "Consider how to decouple the write path from the processing"
  3. User picks via AskUserQuestion
  4. Reveal:
     - Correct answer + detailed explanation
     - Architecture diagram (Mermaid)
     - Why others wrong (1 sentence each)
  5. Next scenario
After all scenarios:
  - Score: X/Y (Z%)
  - Missed topics
  - Save session file with all scenarios + user answers
  - Update progress: advance to P3
```

### Progress Tracking

**New schema** (for domains started after this change):
```yaml
current_phase: 2  # out of 4
phase_scores: {p1: 85, p2: 80, p3: 70, p4: 90}
modes_completed: [learn-and-test, scenario-practice]
```

**Old domains** (completed: true): keep existing format, no migration needed. `completed: true` domains skip phase tracking anyway.

**In-progress domains** (e.g., databases at current_phase: 1): Reset to new P1 since only concept-mapper done (no exam score to preserve).

**Readiness formula**: unchanged — still uses coverage, exam_avg, recency.

### Files to Modify

| File | Changes |
|------|---------|
| `SKILL.md` | Phase table (6→4), guided mode flow in Step 1b, mode names in Step 3, session naming, follow-up menu phase numbers |
| `references/prompt-templates.md` | Replace concept-mapper + mini-exam sections with `learn-and-test` template. Replace scenario-generator section with `scenario-practice` template. Keep mini-exam for design/comprehensive scopes. |
| `references/quiz-flow.md` | Add "Hint Flow Protocol" section for interleaved Q&A. Add section-by-section quiz cycle. |
| `references/progress-tracking.md` | New phase numbering (4 phases), backward compat note, update dashboard format |

### Risks & Mitigations

| Risk | Severity | Mitigation |
|------|----------|------------|
| Session length (P1: ~20 interactive Qs) | Medium | Allow mid-session save/resume at section boundaries |
| Context window pressure | Low | Each section is moderate; total similar to current P1+P2 combined |
| Hint quality inconsistent | Medium | Strict prompt rules: directional nudge only, never mention answer letter |
| Breaking existing progress | Low | No migration; completed domains unaffected; in-progress domains reset to new P1 |

### Success Metrics

- Domains studied with new flow should show equal or better P3/P4 scores vs old flow (hypothesis: interleaved learning improves retention)
- Session count per domain drops from 6 to 4 (fewer context switches)
- User subjective preference: new flow feels more engaging

## Next Steps

Implement via `/ck:plan` — modify the 4 skill reference files.
