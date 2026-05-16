# Phase 02: Scenario Generator Architecture Diagram Directive

## Context
- Parent plan: `plan.md`
- Brainstorm: `plans/reports/brainstorm-260515-concept-mapper-diagrams.md`
- Target: `.claude/skills/ai-tutor/references/prompt-templates.md` lines 138-186

## Overview
- **Priority**: P3
- **Status**: pending
- **Description**: Add architecture diagram directive to scenario-generator — each scenario gets a Mermaid flowchart of the recommended solution + ASCII fallback

## Key Insights
- Each scenario already has Answer + Why Others Wrong + Key Concept sections
- Adding a diagram between Answer explanation and "Why others are wrong" is natural flow
- One diagram per scenario; keeps output proportional (scenarios already ~20 lines each)

## Requirements

### Functional
1. Add diagram step to per-scenario instructions (after step 5 "Correct Answer", before step 6 "Why Others Are Wrong")
2. Add architecture diagram to output format template
3. Add diagram quality rules specific to scenario context

### Non-Functional
- Each scenario grows by ~8-12 lines (Mermaid block + ASCII fallback)
- No changes to scenario-map.md or SKILL.md

## Related Code Files
- **Modify**: `.claude/skills/ai-tutor/references/prompt-templates.md` (lines 138-186, scenario-generator section)
- **Reference only**: `aws-csa/study-sessions/260515-1437-networking-scenario-generator.md` (example output)

## Implementation Steps

1. In `### Instructions`, add step between current steps 5 and 6:
   ```
   5.5. **Architecture Diagram**: Mermaid `graph TD` showing the recommended solution's architecture — services as nodes, connections as edges. Include ASCII fallback (3-5 lines).
   ```
   (Renumber step 6 → 7, step 7 → 8)

2. Update `### Output Format` template — add diagram block after `**Answer:**` explanation:
   ```
   **Architecture:**
   ```mermaid
   graph TD
       {recommended architecture}
   ```
   ```
   ASCII: {3-5 line text description of the architecture}
   ```

3. Add diagram quality note to Instructions:
   - Diagram shows ONLY the correct answer's architecture (not all options)
   - Max 10 nodes per scenario diagram (simpler than concept-mapper diagrams)
   - Use Mermaid `graph TD` only

## Todo
- [ ] Add architecture diagram step to per-scenario instructions
- [ ] Update output format template with diagram block
- [ ] Add diagram quality note

## Success Criteria
- Scenario generator prompt includes architecture diagram directive
- Output format template shows where diagram goes
- Diagram constrained to correct-answer architecture only
- Existing scenario structure (context, requirements, question, options, answer, why-wrong, key-concept) preserved

## Risk Assessment
- **Scenario output length**: each scenario grows ~10 lines — acceptable for 5-9 scenarios
- **Diagram redundancy with text explanation**: mitigated by keeping diagrams schematic (nodes + edges only), text provides detail

## Next Steps
- After both phases: test by running `ai-tutor networking concept-mapper` and `ai-tutor networking scenario-generator` to verify diagram output quality
