---
phase: 1
title: Cheat Sheet Integration
status: completed
priority: P1
effort: 30m
dependencies: []
---

# Phase 1: Cheat Sheet Integration

## Overview

Register the 48-page AWS SAA Master Cheat Sheet PDF as a shared secondary knowledge source. Extract full content into a dedicated cache file. Update prompt templates to load it alongside domain caches for design/comprehensive scopes.

## Requirements

- Functional: cheat sheet extractable via `/ai-tutor refresh cheat-sheet`, loadable by mini-exam and scenario-generator
- Non-functional: full extraction (no trimming), backward compatible with existing modes

## Architecture

```
PDF (sections/AWS-SAA-Master-Cheat-Sheet.pdf)
  → Haiku pdf-extractor subagent
    → cache/aws-csa-cheat-sheet.md (~800-1200 lines)
      → loaded by mini-exam (design/comprehensive), scenario-generator, keyword-drill, mock-exam
```

## Related Code Files

- Modify: `.claude/skills/ai-tutor/certs/aws-csa/domains.md`
- Modify: `.claude/skills/ai-tutor/references/pdf-extractor.md`
- Modify: `.claude/skills/ai-tutor/references/prompt-templates.md`
- Modify: `.claude/skills/ai-tutor/SKILL.md`
- Auto-create: `.claude/skills/ai-tutor/cache/aws-csa-cheat-sheet.md`

## Implementation Steps

### 1. Update `domains.md` — add cheat sheet reference

Add at top level (after frontmatter, before `## Domains`):

```yaml
cheat-sheet:
  name: "SAA-C03 Master Cheat Sheet"
  pdf: sections/AWS-SAA-Master-Cheat-Sheet.pdf
  description: "Cross-domain exam-focused decision frameworks, organized by SAA-C03 exam domains (Secure 30%, Resilient 26%, High-Performing 24%, Cost-Optimized 20%)"
```

### 2. Update `pdf-extractor.md` — add cheat sheet extraction protocol

Add new section after "## Refresh Protocol":

```markdown
## Cheat Sheet Extraction

For cheat sheet extraction (triggered by `/ai-tutor refresh cheat-sheet` or on first use):

1. Read the cheat sheet PDF: `sections/AWS-SAA-Master-Cheat-Sheet.pdf` (all pages)
2. Extract into: `.claude/skills/ai-tutor/cache/aws-csa-cheat-sheet.md`

**Subagent prompt additions:**
- Organize by SAA-C03 exam domain sections (Domain 1-4)
- Preserve decision frameworks and "when to use which" tables
- Extract all service comparisons and selection criteria
- Include exam tips and common traps per domain
- Target 800-1200 lines (full content, no trimming)

**Output sections:**
# AWS SAA-C03 Master Cheat Sheet — Content Cache

## Domain 1: Design Secure Architectures (30%)
{all content from Domain 1 sections}

## Domain 2: Design Resilient Architectures (26%)
{all content from Domain 2 sections}

## Domain 3: Design High-Performing Architectures (24%)
{all content from Domain 3 sections}

## Domain 4: Design Cost-Optimized Architectures (20%)
{all content from Domain 4 sections}
```

### 3. Update `prompt-templates.md` — add cheat sheet loading rules

In the Mini Exam "### Input" section, add:

```markdown
- Cheat sheet cache (conditional): `.claude/skills/ai-tutor/cache/aws-csa-cheat-sheet.md`
  - Load for scope=design, scope=comprehensive, scope=general
  - Skip for scope=concepts, scope=scenarios
```

In the Scenario Generator "### Input" section, add:

```markdown
- Cheat sheet cache (supplementary): `.claude/skills/ai-tutor/cache/aws-csa-cheat-sheet.md`
  - Load if available; use for cross-cutting decision frameworks
```

### 4. Update `SKILL.md` — register cheat sheet in context loading

In "## Step 2: Load Context", add after step 3:

```markdown
4. **Cheat sheet cache** (for modes that use it):
   Check cache: `.claude/skills/ai-tutor/cache/aws-csa-cheat-sheet.md`
   - **Cache HIT**: Read cached content, add to context
   - **Cache MISS**: Load `references/pdf-extractor.md` § Cheat Sheet Extraction
     - Spawn pdf-extractor subagent for cheat sheet
     - Wait for completion, then read cache file
   - **Modes that use cheat sheet**: mini-exam (design/comprehensive/general), scenario-generator, keyword-drill, mock-exam
```

In "## Argument Parsing", add pattern:

```markdown
| `refresh cheat-sheet` | Re-extract cheat sheet PDF cache |
```

### 5. Trigger initial extraction

After all file changes, run `/ai-tutor refresh cheat-sheet` to generate the initial cache file.

## Success Criteria

- [ ] `cache/aws-csa-cheat-sheet.md` generated with full content (~800-1200 lines)
- [ ] Mini-exam `scope=design` loads both domain cache + cheat sheet cache
- [ ] Mini-exam `scope=concepts` does NOT load cheat sheet (no regression)
- [ ] `/ai-tutor refresh cheat-sheet` works from argument parser
- [ ] Existing domain caches and modes unaffected

## Risk Assessment

| Risk | Mitigation |
|------|-----------|
| Cheat sheet + domain cache exceeds context | Both together ~1500-2000 lines; well within LLM context. Monitor for Haiku extraction quality. |
| Extraction misses key content | Full extraction mandate — no trimming. Verify manually after first run. |
