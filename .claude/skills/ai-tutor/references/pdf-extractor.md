# PDF Extractor Subagent

Prompt and protocol for the Haiku-model subagent that extracts structured content from PDF course sections into cache files.

## Subagent Configuration

- **Agent type**: `general-purpose`
- **Model**: `haiku`
- **Purpose**: Read PDF sections (multimodal), extract structured content, write cache file

## Subagent Prompt Template

Use this prompt when spawning the pdf-extractor subagent:

```
You are a PDF content extractor for AWS certification study material.

**Task:** Read the following PDF files and extract structured study content for the "{domain_name}" domain.

**PDF files to read** (use Read tool for each):
{pdf_paths_list}

**Instructions:**
1. Read each PDF file using the Read tool (you can read PDFs — they contain slide content)
2. Extract ALL educational content including:
   - Service names, descriptions, and key features
   - Configuration options, defaults, and limits
   - Architectural patterns and best practices
   - Important numbers (quotas, SLAs, thresholds)
   - Descriptions of any diagrams or visual content in the slides
   - Exam-relevant distinctions and common traps
3. Merge content from all PDFs into a single organized document
4. Write the output to: {cache_path}

**Output format — use these exact sections:**

# {Domain Name} - AWS CSA Content Cache

## Services & Concepts
For each service/concept:
- **Service Name**: Description, use cases, key features
- Include sub-services and variants

## Key Configurations
- Important settings, defaults, and configurable limits
- Default behaviors that differ from expectations

## Architectural Patterns
- Common architectures using these services
- Multi-service integration patterns
- When to use which service

## Important Numbers & Limits
- Quotas, thresholds, SLA numbers
- Size limits, throughput limits, timeout values
- Use a table format for easy scanning

## Diagram Descriptions
- Text descriptions of any visual diagrams in the slides
- Architecture diagrams, flow charts, comparison tables

## Exam-Relevant Details
- Tricky distinctions (e.g., "X vs Y — when to use which")
- Common exam traps and misconceptions
- Keywords that signal specific services in exam questions

**Quality rules:**
- Be comprehensive — this cache is the ONLY source of domain knowledge for study modes
- Use concise bullet points, not paragraphs
- Include specific numbers (not "large" — say "up to 64 TiB")
- Preserve technical accuracy from the source PDFs
- Target 300-600 lines total
```

## Cache Check Protocol (for SKILL.md)

Before executing any study mode that requires domain knowledge:

1. Construct cache path: `.claude/skills/ai-tutor/cache/aws-csa-{domain}.md`
2. Check if file exists using Bash: `test -f {cache_path} && echo "HIT" || echo "MISS"`
3. **HIT**: Read cache file directly, proceed to mode execution
4. **MISS**: Spawn pdf-extractor subagent:
   - Read `certs/aws-csa/domains.md` to get PDF file list for the domain
   - Construct full PDF paths: `sections/{pdf_filename}`
   - Spawn Agent with the prompt template above (filled with domain name, PDF paths, cache path)
   - After subagent completes, read the cache file

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
```
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

## Refresh Protocol

For `/ai-tutor refresh <domain>`:

1. Delete existing cache file: `rm -f .claude/skills/ai-tutor/cache/aws-csa-{domain}.md`
2. Spawn pdf-extractor subagent (same as cache MISS flow)
3. Confirm to user: "Cache refreshed for {domain}. Extracted from {N} PDF sections."
