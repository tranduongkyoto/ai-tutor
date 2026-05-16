# Phase 01: Concept Mapper Diagram Directives

## Context
- Parent plan: `plan.md`
- Brainstorm: `plans/reports/brainstorm-260515-concept-mapper-diagrams.md`
- Target: `.claude/skills/ai-tutor/references/prompt-templates.md` lines 33-63

## Overview
- **Priority**: P3
- **Status**: pending
- **Description**: Add diagram generation directives to the concept-mapper prompt template — Mermaid flowcharts/decision trees + ASCII fallbacks across 5 sections

## Key Insights
- Current concept mapper has 7 sections, only §3 has a basic ASCII block in practice
- Mermaid `graph TD/LR` renders in GitHub, VS Code, Obsidian — widely supported
- ASCII fallback ensures terminal users still benefit
- 3-5 diagrams per session prevents output bloat

## Requirements

### Functional
1. Add `### Diagram Directives` subsection to concept-mapper Instructions
2. Define 5 diagram insertion points with format + purpose
3. Add diagram quality rules (max nodes, naming, fallbacks)
4. Preserve existing 7-section structure and Output Format section

### Non-Functional
- Output length increase: ~40-60 lines of template additions
- No changes to how SKILL.md invokes concept-mapper

## Related Code Files
- **Modify**: `.claude/skills/ai-tutor/references/prompt-templates.md` (lines 33-63, concept-mapper section)
- **Reference only**: `aws-csa/study-sessions/260515-0851-networking-concept-mapper.md` (example output)

## Implementation Steps

1. In the concept-mapper `### Instructions` section (after the 7-item list, before `### Output Format`), add a new `### Diagram Directives` subsection with:

2. **Diagram placement table** — 5 insertion points:
   | Section | Diagram Type | Format | Guidance |
   |---------|-------------|--------|----------|
   | §3 Service Integrations | Service relationship flowchart | Mermaid `graph LR` | Show traffic/data paths between domain services. Nodes = services, edges = data flow direction |
   | §4 Architectural Patterns | Architecture diagram (top 2 patterns) | Mermaid `graph TD` | Layered layout: Internet → public tier → private tier → data tier |
   | §4 (sub) | Decision tree for pattern selection | Mermaid `graph TD` with diamond branches | "When to use which pattern?" — branching on requirements |
   | §6 Security | Defense-in-depth layers | ASCII art | Stack diagram: outer (NACL) → inner (SG) → service (IAM) → data (encryption) |
   | §7 Exam Tips | Keyword-to-answer decision tree | Mermaid `graph TD` | Map exam trigger words to correct service/answer |

3. **Diagram quality rules** (append to existing Quality Rules):
   - Mermaid: `graph TD` or `graph LR` only — no sequence, pie, gantt, etc.
   - Max 15 nodes per diagram; split into multiple if larger
   - Include ASCII text fallback below each Mermaid block (3-5 line summary)
   - Node labels: full service name on first occurrence, abbreviation OK after
   - Decision trees: question/condition at top, branches as options, leaf = answer/recommendation
   - Target 3-5 diagrams per session — skip if a section has no visual value for the domain

4. **Update Output Format** section — add bullet:
   - Mermaid code blocks (` ```mermaid `) for architecture and decision diagrams
   - ASCII blocks for terminal-friendly fallbacks

## Todo
- [ ] Add `### Diagram Directives` subsection with placement table
- [ ] Add diagram quality rules
- [ ] Update Output Format bullet list
- [ ] Verify no disruption to existing 7-section structure

## Success Criteria
- Concept mapper prompt includes diagram directives for 5 insertion points
- Quality rules specify Mermaid-only types, node limits, ASCII fallbacks
- Output Format section mentions Mermaid + ASCII
- Existing sections 1-7 and their instructions unchanged

## Risk Assessment
- **Output bloat**: mitigated by 3-5 cap and "skip if no visual value" escape clause
- **Mermaid syntax errors in AI output**: mitigated by constraining to `graph TD/LR` only

## Next Steps
- After this phase: proceed to Phase 02 (scenario-generator diagrams)
