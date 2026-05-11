---
name: ai-tutor
description: "Interactive AWS certification tutor with 6 study modes, quizzes, and progress tracking"
argument-hint: "[cert] [domain] [mode] | progress | refresh <domain>"
metadata:
  author: user
  version: "1.0.0"
---

# AI Tutor - AWS Certification Study Companion

Interactive tutor for AWS certification prep using PDF course materials, 6 study modes, interactive quizzes, and progress tracking.

## Argument Parsing

Parse `ARGUMENTS` to determine the action:

| Pattern | Action |
|---------|--------|
| _(empty)_ | Show cert selection menu |
| `progress` | Show progress dashboard (Load: `references/progress-tracking.md`). **Stop after displaying — do not continue to Step 1.** |
| `refresh <domain>` | Re-extract PDF cache for domain (Load: `references/pdf-extractor.md`). **Stop after refresh — do not continue to Step 1.** |
| `<cert> <domain> <mode>` | Direct mode execution |
| Partial args | Menu fallback for missing parts |

## Step 1: Selection (menu fallback for missing args)

**Cert selection** (if not provided):
Use `AskUserQuestion` — options: `aws-csa` (only cert available now).

**Domain selection** (if not provided):
Load: `certs/aws-csa/domains.md` to get the 12 domain list.
Use `AskUserQuestion` with options grouped by category:
- `compute`, `storage`, `databases`, `networking`
- `security-identity`, `load-balancing-scaling`, `dns`, `integration-messaging`
- `serverless`, `monitoring-audit`, `data-analytics`, `dr-architecture`

NOTE: For `weak-spot-analyzer` and `exam-strategy` modes — skip domain selection entirely. These modes analyze cross-domain progress data.

**Mode selection** (if not provided):
Use `AskUserQuestion` — options:
- `concept-mapper` — Knowledge synthesis and service relationships
- `mini-exam` — Interactive quiz with scoring
- `scenario-generator` — Realistic exam scenarios with explanations
- `weak-spot-analyzer` — Identify and prioritize weak areas
- `hands-on-lab` — Progressive lab exercises
- `architecture-reviewer` — Evaluate architectures against Well-Architected
- `exam-strategy` — Exam day strategy and study planning

## Step 2: Load Context

1. Read `certs/aws-csa/domains.md` for topic checklist
2. Read `aws-csa/study-progress.md` for current progress (create if missing — see edge cases below)
3. **If mode requires domain cache** (concept-mapper, mini-exam, scenario-generator, hands-on-lab, architecture-reviewer):
   Check cache: `.claude/skills/ai-tutor/cache/aws-csa-{domain}.md`
   - **Cache HIT**: Read cached content, proceed to Step 3
   - **Cache MISS**: Load `references/pdf-extractor.md` and spawn pdf-extractor subagent
     - Agent type: `general-purpose`, model: `haiku`
     - Input: domain name + PDF paths from domains.md
     - Output: writes cache file
     - Wait for completion, then read cache file
4. **If mode is domain-less** (weak-spot-analyzer, exam-strategy): Skip cache check, proceed to Step 3 with progress data only

## Step 3: Execute Mode

Load `references/prompt-templates.md` for the selected mode's template.

| Mode | Additional Input | Interactive? |
|------|-----------------|-------------|
| `concept-mapper` | Cache file | No |
| `mini-exam` | Cache + quiz-flow.md | Yes (AskUserQuestion) |
| `scenario-generator` | Cache file | No |
| `weak-spot-analyzer` | study-progress.md only | No |
| `hands-on-lab` | Cache file | No |
| `architecture-reviewer` | Cache + user architecture | Yes (AskUserQuestion) |
| `exam-strategy` | study-progress.md + timeline | Yes (AskUserQuestion) |

For `mini-exam`: Load `references/quiz-flow.md` for the interactive quiz protocol.

Generate content following the mode's prompt template. Display output in terminal.

## Step 4: Save & Track

Load `references/progress-tracking.md` for the update protocol.

1. Save session output:
   - **Domain modes**: `aws-csa/study-sessions/{YYMMDD}-{HHMM}-{domain}-{mode}.md`
   - **Cross-domain modes**: `aws-csa/study-sessions/{YYMMDD}-{HHMM}-{mode}.md` (no domain in name)
   - Use `bash -c 'date +%y%m%d-%H%M'` for timestamp
2. Update `aws-csa/study-progress.md` following the update protocol
3. Show recommendation for next study action

## Step 5: Follow-Up Menu

After session completion, use `AskUserQuestion`:
- **Continue studying** — return to Step 1 (domain/mode selection)
- **View progress** — show progress dashboard
- **Done** — end session with brief summary

## Edge Cases

- **No study-progress.md**: Create initial file with empty YAML frontmatter (see `references/progress-tracking.md`)
- **PDF extraction fails**: Show error, suggest `/ai-tutor refresh {domain}`
- **No exam history**: Weak Spot and Exam Strategy show "No exam data yet. Start with a mini-exam to track progress."
- **Invalid args**: Show usage with examples:
  ```
  Usage: /ai-tutor [cert] [domain] [mode]
         /ai-tutor progress
         /ai-tutor refresh <domain>
  Example: /ai-tutor aws-csa compute concept-mapper
  ```
