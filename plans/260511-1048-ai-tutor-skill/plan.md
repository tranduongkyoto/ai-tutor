---
title: "AI Tutor Skill for AWS Certification"
description: "Claude Code skill (/ai-tutor) for interactive AWS certification study with 6 tutor modes, PDF-based content extraction, quizzes, and progress tracking"
status: complete
priority: P1
branch: "master"
tags: [skill, aws-csa, ai-tutor]
blockedBy: []
blocks: []
created: "2026-05-11T03:50:18.852Z"
createdBy: "ck:plan"
source: skill
---

# AI Tutor Skill for AWS Certification

## Overview

Build a project-scoped Claude Code skill (`/ai-tutor`) at `.claude/skills/ai-tutor/` that helps users study for AWS SAA-C03 certification using 31 PDF course files (849 pages). The skill provides 6 tutor modes, interactive mini-exams via `AskUserQuestion`, and progress tracking with readiness scoring — all within the CLI.

**Design doc:** `plans/reports/brainstorm-260511-1040-ai-tutor-skill-design.md`

## Architecture

```
.claude/skills/ai-tutor/
├── SKILL.md                        # Orchestrator (~150 lines)
├── references/
│   ├── prompt-templates.md         # 6 tutor mode prompt templates
│   ├── progress-tracking.md        # Readiness formula + update protocol
│   ├── quiz-flow.md                # Interactive quiz protocol
│   └── pdf-extractor.md            # Subagent prompt for PDF extraction
├── cache/                          # Auto-generated domain content cache
└── certs/
    └── aws-csa/
        └── domains.md              # 12 domains + topic checklists + PDF mappings

aws-csa/                            # Runtime output at project root
├── study-progress.md               # Progress tracker (YAML + session log)
└── study-sessions/                 # Session artifacts
```

## Phases

| Phase | Name | Status | Effort | Dependencies |
|-------|------|--------|--------|--------------|
| 1 | [Skill Skeleton & Domain Config](./phase-01-skill-skeleton-domain-config.md) | Complete | 2h | None |
| 2 | [PDF Extractor Subagent](./phase-02-pdf-extractor-subagent.md) | Complete | 2h | Phase 1 |
| 3 | [Core Modes (Concept Mapper + Mini Exam)](./phase-03-core-modes-concept-mapper-mini-exam.md) | Complete | 3h | Phase 2 |
| 4 | [Remaining Modes (Scenario + Weak Spot + Lab + Arch Review + Exam Strategy)](./phase-04-remaining-modes-scenario-weak-spot-lab-arch-review-exam-stra.md) | Complete | 3h | Phase 3 |
| 5 | [Progress Tracking & Dashboard](./phase-05-progress-tracking-dashboard.md) | Complete | 2h | Phase 3 |
| 6 | [Polish & Integration](./phase-06-polish-integration.md) | Complete | 1h | Phase 4, 5 |

**Total estimated effort:** ~13h

## Key Decisions (from brainstorm)

- Only pdf-extractor as subagent (Haiku model); all 6 modes inline in main skill
- AskUserQuestion for quiz (A/B/C/D options + "Other" for E)
- User chooses quiz size: 5/10/15 questions
- Dynamic readiness: coverage(30%) + exam(50%) + recency(20%)
- Cert-specific folders: `aws-csa/study-progress.md`
- Session files: `{YYMMDD}-{HHMM}-{domain}-{mode}.md`

## Dependencies

No cross-plan dependencies. Self-contained skill creation.
