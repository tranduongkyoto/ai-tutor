# Phase 2: Update prompt-templates.md

## Context

- Parent plan: [plan.md](./plan.md)
- File: `.claude/skills/ai-tutor/references/prompt-templates.md`
- Depends on: Phase 1 (phase numbering)

## Overview

- **Priority**: High
- **Status**: complete
- **Description**: Add learn-and-test and scenario-practice mode templates

## Key Insights

- Current concept-mapper template has 7 well-defined sections — reuse as learning sections
- Current scenario-generator uses scenario-map entries — reuse as scenario items
- Existing templates must stay for free mode
- New templates define the interleaved teach→quiz→hint flow

## Requirements

### Functional
- New `Mode: Learn and Test` template with section-by-section interleaved flow
- New `Mode: Scenario Practice` template with per-scenario interactive loop
- Hint quality rules defined (directional nudge, no answer reveal)
- Scoring aggregation defined
- Session file format defined for both new modes
- Existing concept-mapper and scenario-generator templates preserved for free mode

## Related Code Files

- **Modify**: `.claude/skills/ai-tutor/references/prompt-templates.md`

## Implementation Steps

1. **Add `Mode: Learn and Test` template** (after existing Concept Mapper section):

   **Input**: domain, cache file, quiz-flow.md (hint protocol)

   **Instructions**:
   - Process domain content through 7 sections (same as concept-mapper):
     1. Service Overview
     2. Real-World Use Cases
     3. Service Integrations
     4. Architectural Patterns
     5. Cost Implications
     6. Security Considerations
     7. Exam Tips
   - Per section:
     a. Output section content (same quality as concept-mapper: tables, diagrams, bold terms)
     b. Generate 2-3 questions on that section
        - Mix: ~60% fact-based, ~40% scenario-based
        - 4 options (A-D) per question
        - Tag each with topic slug
     c. Per question: present question → show hint → collect answer → reveal explanation
   - Hint quality rules:
     - 1 sentence, directional nudge toward the concept being tested
     - NEVER mention the correct option letter
     - NEVER repeat option text verbatim
     - NEVER give away the answer — point toward the AWS concept/pattern
     - Examples: "Think about which service handles container orchestration without managing servers", "Consider the storage class optimized for infrequent access"
   - After all 7 sections: aggregate score (total correct / total questions)

   **Diagram directives**: Same as concept-mapper (diagrams embedded in section content)

   **Output format**: Section content + embedded Q&A per section

   **Session file format**:
   ```markdown
   # {Domain} — Learn and Test (Phase 1)
   **Date:** {YYYY-MM-DD HH:MM}
   **Score:** {score}/{total} ({pct}%)

   ---

   ## Section 1: Service Overview
   {full section content with diagrams}

   ### Quiz: Section 1
   **Q1** ✓/✗ — {topic-slug}
   {question text}
   A) ... B) ... C) ... D) ...
   Hint: {hint text}
   **Your answer: {letter}** — {Correct/Incorrect}. {explanation}

   ---
   ## Section 2: Real-World Use Cases
   ...
   ```

2. **Add `Mode: Scenario Practice` template** (after Learn and Test):

   **Input**: domain, cache file, scenario-map, cheat-sheet cache (if available)

   **Instructions**:
   - Read scenario-map for domain (same source as scenario-generator)
   - Generate one scenario per map entry
   - Per scenario (interactive loop):
     a. Show: Business Context + Requirements + Question + 4 Options (answer HIDDEN)
     b. Show hint: 1-2 sentence nudge toward correct AWS pattern
        - Same hint rules as learn-and-test
        - Scenario-specific: reference the architectural pattern or design principle
        - Example: "Consider a managed service that decouples producers from consumers with FIFO ordering"
     c. Collect user answer via AskUserQuestion
     d. Reveal: Correct answer + explanation + architecture diagram (Mermaid) + why-others-wrong
   - After all scenarios: aggregate score

   **Session file format**:
   ```markdown
   # {Domain} — Scenario Practice (Phase 2)
   **Date:** {YYYY-MM-DD HH:MM}
   **Score:** {score}/{total} ({pct}%)

   ---

   ### Scenario 1: {Title} — ✓/✗ ({topic-slug})
   **Context:** ...
   **Requirements:** ...
   **Question:** ...
   A) ... B) ... C) ... D) ...
   **Hint:** {hint}
   **Your answer: {letter}** — {Correct/Incorrect}
   **Correct: {letter}** — {explanation}
   **Architecture:** {mermaid diagram}
   **Why others wrong:** ...

   ---
   ### Scenario 2: ...
   ```

3. **Keep existing templates**: Mark Concept Mapper and Scenario Generator sections with a note: "Used in free mode. In guided mode, use learn-and-test / scenario-practice instead."

## Todo

- [ ] Add Mode: Learn and Test template with full section-by-section flow
- [ ] Define hint quality rules
- [ ] Define learn-and-test session file format
- [ ] Add Mode: Scenario Practice template with interactive loop
- [ ] Define scenario-practice session file format
- [ ] Add free-mode notes to existing concept-mapper and scenario-generator templates
- [ ] Verify mini-exam template unchanged (design/comprehensive scopes still work)

## Success Criteria

- learn-and-test template clearly defines 7-round section flow
- scenario-practice template clearly defines per-scenario interactive loop
- Hint rules are explicit and unambiguous
- Session file formats capture full content as study reference
- Existing templates preserved and annotated for free mode

## Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|------------|
| Template too long, confusing LLM | Medium | Keep instructions concise, use tables |
| Hint quality hard to enforce | Medium | Explicit rules + examples + "NEVER" constraints |
| Session files very large | Low | Same size as current P1+P2 combined — acceptable |
