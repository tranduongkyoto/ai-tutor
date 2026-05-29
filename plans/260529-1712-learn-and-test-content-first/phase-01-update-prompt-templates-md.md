---
phase: 1
title: "Update prompt-templates.md"
status: pending
priority: P1
effort: "30m"
dependencies: []
---

# Phase 1: Update prompt-templates.md

## Overview

Restructure the Learn and Test template (lines 114-185) from interleaved content+quiz to a two-phase flow: generate all content first, then run quiz.

## Related Code Files

- Modify: `.claude/skills/ai-tutor/references/prompt-templates.md` (§ Mode: Learn and Test, lines 114-185)

## Implementation Steps

1. **Replace the Instructions section** (lines 123-145) with two sub-sections:

   **Phase A: Content Generation**
   <!-- Updated: Validation Session 1 - dual output (terminal + file) confirmed -->
   - Process domain content through 7 sections (same list: Service Overview → Exam Tips)
   - Generate all 7 sections with full content (diagrams, tables, bold terms — same quality as concept-mapper)
   - **Output content to terminal** as it's generated (same as concept-mapper behavior — user sees raw mermaid in CLI)
   - **Also write** complete content to session file: `aws-csa/study-sessions/{YYMMDD}-{HHMM}-{domain}-learn-and-test.md`
   - After all sections generated, display: `📄 Content saved to {file}. Open in IDEA to study with rendered diagrams.`
   - Include the Diagram Directives reference (unchanged from current)

   **Phase B: Interactive Quiz**
   - Immediately present first quiz question (no "ready?" prompt needed)
   - Per section: generate 2-3 questions on that section's material
   - Run each question through the Hint Flow Protocol (reference `quiz-flow.md`)
   - After section's questions: show `Section {N}/7 complete: {X}/{Y} correct`
   - After all 7 sections: aggregate score, list missed topics by slug
   - Append quiz results to the same session file under a `## Quiz Results` heading

2. **Update Session File Format** (lines 164-184) to match the approved layout:
   <!-- Updated: Validation Session 1 - section-grouped quiz results confirmed -->
   - Content sections first (all 7), separator `---`, then `## Quiz Results` heading
   - Each section's quiz results under `### Section {N}: {name}` (mirrors content section headers for IDEA cross-reference)
   - Per question: `**Q{N}** ✓/✗ — {topic-slug}` + question text + answer + explanation
   - Score line at top updated after quiz completes

3. **Keep unchanged**: Input section, Hint Quality Rules, Diagram Directives — these stay as-is

## Success Criteria

- [ ] Instructions clearly describe two-phase flow (content-first, quiz-after)
- [ ] Session file format shows content sections before quiz results
- [ ] Diagram Directives and Hint Quality Rules preserved unchanged
- [ ] No references to interleaved per-section content+quiz flow remain
