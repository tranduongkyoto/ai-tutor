---
phase: 2
title: "PDF Extractor Subagent"
status: pending
priority: P1
effort: "2h"
dependencies: [1]
---

# Phase 2: PDF Extractor Subagent

## Overview

Write the pdf-extractor subagent prompt in `references/pdf-extractor.md` and implement the cache system. The subagent uses Haiku model to read PDF sections (multimodal) and extract structured content to `.claude/skills/ai-tutor/cache/` as markdown files.

## Requirements

- Functional: Extract concepts, service details, diagram descriptions, key numbers from PDFs. One cache file per domain.
- Non-functional: Haiku model for cost efficiency. Cache files 300-600 lines max. Write-once (skip if cache exists).

## Architecture

```
Flow:
  SKILL.md checks cache/aws-csa-{domain}.md exists?
    YES → read cached content, proceed to mode
    NO  → spawn Agent(subagent_type="general-purpose", model="haiku")
          → reads mapped PDF sections via Read tool (multimodal)
          → extracts structured content
          → writes cache/aws-csa-{domain}.md
          → returns to SKILL.md flow

Cache file structure:
  cache/aws-csa-{domain}.md
    # {Domain Name} - AWS CSA Content Cache
    ## Services & Concepts
    ## Key Configurations
    ## Architectural Patterns
    ## Important Numbers & Limits
    ## Diagram Descriptions
    ## Exam-Relevant Details
```

## Related Code Files

- Modify: `.claude/skills/ai-tutor/references/pdf-extractor.md` (fill skeleton from Phase 1)
- Modify: `.claude/skills/ai-tutor/SKILL.md` (add cache-check + subagent spawn logic)
- Create: `.claude/skills/ai-tutor/cache/` (directory, auto-populated)

## Implementation Steps

### 1. Write pdf-extractor.md subagent prompt

The prompt must instruct the Haiku subagent to:
- Accept domain name and list of PDF section paths as input
- Read each PDF file using Read tool (multimodal — Haiku can read PDFs)
- Extract and organize content into structured sections:
  - **Services & Concepts**: Each service with description, use cases, key features
  - **Key Configurations**: Important settings, defaults, limits
  - **Architectural Patterns**: Common architectures using these services
  - **Important Numbers & Limits**: Quotas, thresholds, SLA numbers
  - **Diagram Descriptions**: Text descriptions of any visual diagrams in the slides
  - **Exam-Relevant Details**: Tricky distinctions, common exam traps
- Write output to `cache/aws-csa-{domain}.md`
- Handle multi-PDF domains (e.g., storage maps to 5 PDFs) by reading all and merging

### 2. Add cache-check logic to SKILL.md

In Step 2 (Load context) of SKILL.md flow:
```
cache_path = .claude/skills/ai-tutor/cache/aws-csa-{domain}.md
IF cache file exists → Read cache_path
ELSE → spawn pdf-extractor subagent with:
  - domain name
  - PDF paths from domains.md mapping
  - output path: cache_path
```

### 3. Add refresh command to SKILL.md

`/ai-tutor refresh <domain>`:
- Delete existing cache file for domain
- Re-spawn pdf-extractor subagent
- Confirm completion to user

### 4. Test with one domain

Extract `compute` domain (PDFs 03, 04, 16) as validation:
- Verify cache file is created
- Verify content covers key topics from domains.md checklist
- Verify file size is reasonable (300-600 lines)

## Success Criteria

- [ ] pdf-extractor.md contains complete subagent prompt
- [ ] Cache check logic in SKILL.md correctly detects existing/missing cache
- [ ] Subagent successfully extracts content from PDF sections
- [ ] Cache file for `compute` domain exists and contains structured content
- [ ] `/ai-tutor refresh compute` re-extracts and overwrites cache
- [ ] Cache file is under 600 lines

## Risk Assessment

- **PDF read failures**: Haiku may struggle with complex diagrams → prompt instructs to describe what it can see, skip what it can't
- **Token cost**: First extraction of all 12 domains = ~849 pages via Haiku. Acceptable one-time cost. Subsequent runs use cache.
- **Large PDFs**: Some domains map to 5 PDFs (storage). Subagent prompt must handle reading multiple files sequentially.
