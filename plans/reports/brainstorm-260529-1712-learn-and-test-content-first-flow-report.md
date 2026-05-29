# Brainstorm: Learn-and-Test Content-First Flow

**Date:** 2026-05-29
**Status:** Approved — ready for planning

## Problem

Learn-and-test mode (Phase 1) generates mermaid diagrams in Section 3 (Service Integrations) and other sections. In Claude Code CLI terminal, mermaid renders as raw code blocks — not visually useful. IntelliJ IDEA's .md preview renders mermaid natively.

Current flow interleaves content + quiz per section, so the .md file isn't written until everything completes — user can't open it in IDEA mid-session.

## Agreed Solution: Content-First, Quiz-After

Split learn-and-test into two sequential phases within one session:

### Phase A: Content Generation
1. Generate all 7 sections with full content (diagrams, tables, bold terms, same quality as concept-mapper)
2. Write to `aws-csa/study-sessions/{YYMMDD}-{HHMM}-{domain}-learn-and-test.md`
3. Show message: `📄 Content saved to {file}. Open in IDEA to study with rendered diagrams.`

### Phase B: Interactive Quiz
4. Immediately present first quiz question (no "ready?" prompt)
5. Run 2-3 questions per section following Hint Flow Protocol
6. Show per-section scores: `Section {N}/7 complete: {X}/{Y} correct`
7. Append quiz Q&A results to same .md file after each section
8. Final aggregate score at end

### File Format (single file)
```markdown
# {Domain} — Learn and Test (Phase 1)
**Date:** {YYYY-MM-DD HH:MM}
**Score:** {score}/{total} ({pct}%)  ← updated after quiz completes

---

## Section 1: Service Overview
{full content with diagrams}

## Section 2: Real-World Use Cases
{full content}

... (all 7 sections) ...

---

## Quiz Results

### Section 1: Service Overview
**Q1** ✓/✗ — {topic-slug}
{question + answer + explanation}

### Section 2: Real-World Use Cases
...
```

## Changes Required

| File | Change |
|------|--------|
| `references/prompt-templates.md` § Learn and Test | Restructure instructions: content-first generation, then quiz loop |
| `.claude/skills/ai-tutor/SKILL.md` Step 3 | Note learn-and-test writes file before quiz |
| `references/quiz-flow.md` | Add "Section Quiz Cycle (post-content)" variant if needed |

## What Stays Same
- Session file path pattern
- Hint Flow Protocol for quizzes
- 7-section structure and content quality
- Progress tracking and scoring logic
- Diagram directives (mermaid + ASCII fallback)

## Decisions
- Single file (content + quiz results appended), not two files
- Auto-start quiz after content gen (no "ready?" pause)
- Same session naming: `{YYMMDD}-{HHMM}-{domain}-learn-and-test.md`

## Risks
| Risk | Severity | Mitigation |
|------|----------|------------|
| Content gen takes longer before any interaction | Low | Same total time, just reordered |
| User might not open IDEA before quiz starts | Low | Message clearly states to open file; quiz questions reference section content |
