---
phase: 1
title: "Skill Skeleton & Domain Config"
status: pending
priority: P1
effort: "2h"
dependencies: []
---

# Phase 1: Skill Skeleton & Domain Config

## Overview

Create the skill directory structure, SKILL.md orchestrator, all reference files, and the AWS CSA domains configuration with 12 domains mapped to PDF sections.

## Requirements

- Functional: Skill invocable via `/ai-tutor`, parses args `[cert] [domain] [mode]`, shows menus on missing args
- Non-functional: SKILL.md under 150 lines, modularized via references/

## Architecture

```
.claude/skills/ai-tutor/
├── SKILL.md                        # Orchestrator with arg parsing + flow control
├── references/
│   ├── prompt-templates.md         # 6 tutor mode prompt templates (Phase 3-4 content)
│   ├── progress-tracking.md        # Readiness formula + update protocol (Phase 5 content)
│   ├── quiz-flow.md                # Interactive quiz protocol (Phase 3 content)
│   └── pdf-extractor.md            # Subagent prompt for PDF extraction (Phase 2 content)
└── certs/
    └── aws-csa/
        └── domains.md              # 12 domains + topic checklists + PDF mappings
```

## Related Code Files

- Create: `.claude/skills/ai-tutor/SKILL.md`
- Create: `.claude/skills/ai-tutor/references/prompt-templates.md` (skeleton, filled in Phase 3-4)
- Create: `.claude/skills/ai-tutor/references/progress-tracking.md` (skeleton, filled in Phase 5)
- Create: `.claude/skills/ai-tutor/references/quiz-flow.md` (skeleton, filled in Phase 3)
- Create: `.claude/skills/ai-tutor/references/pdf-extractor.md` (skeleton, filled in Phase 2)
- Create: `.claude/skills/ai-tutor/certs/aws-csa/domains.md`

## Implementation Steps

### 1. Create SKILL.md orchestrator

```yaml
---
name: ai-tutor
description: "Interactive AWS certification tutor with 6 study modes, quizzes, and progress tracking"
argument-hint: "[cert] [domain] [mode] | progress | refresh <domain>"
metadata:
  author: user
  version: "1.0.0"
---
```

SKILL.md must handle:
- **Arg parsing**: `/ai-tutor` (menu), `/ai-tutor progress` (dashboard), `/ai-tutor refresh <domain>` (re-extract), `/ai-tutor aws-csa compute concept-mapper` (direct)
- **Menu fallback**: Use `AskUserQuestion` for cert selection (only aws-csa for now), domain selection (12 options presented in groups of 4), mode selection (6 modes)
- **Flow control**: Load context → Execute mode → Save & track → Follow-up menu
- **Reference loading**: `Load: references/prompt-templates.md`, `Load: references/progress-tracking.md`, etc.
- Keep under 150 lines by delegating all prompt content to references/

### 2. Create domains.md for AWS CSA

Full 12-domain configuration with:
- Domain slug (kebab-case identifier)
- Display name
- PDF section numbers (mapped to `sections/*.pdf`)
- Topic checklist (exam-relevant topics per domain)

Domain list from brainstorm:
| Domain | PDFs | Key Topics |
|--------|------|------------|
| compute | 03,04,16 | instance-types, security-groups, purchasing, placement-groups, eni, hibernate, ecs, eks, fargate |
| storage | 05,10,11,12,14 | ebs-types, ebs-snapshots, efs, s3-classes, s3-lifecycle, s3-security, fsx, snow-family, storage-gateway |
| databases | 07,19 | rds, aurora, elasticache, dynamodb, rds-proxy, documentdb, neptune, keyspaces, qldb, timestream |
| networking | 25 | vpc, subnets, nacl-vs-sg, nat-gateway, vpc-peering, vpc-endpoints, dx, transit-gateway, flow-logs |
| security-identity | 02,23,24 | iam, organizations, scp, kms, ssm-params, waf, shield, guardduty, inspector, macie, cognito |
| load-balancing-scaling | 06 | alb, nlb, gwlb, asg, sticky-sessions, cross-zone, ssl-sni, connection-draining |
| dns | 08 | route53-records, routing-policies, health-checks, alias-vs-cname, hybrid-dns |
| integration-messaging | 15 | sqs, sns, kinesis-streams, kinesis-firehose, fan-out, amazon-mq |
| serverless | 17,18 | lambda, api-gateway, step-functions, cognito, lambda-edge, cloudfront-functions |
| monitoring-audit | 22 | cloudwatch, cloudtrail, config, eventbridge, insights |
| data-analytics | 20,21 | athena, redshift, glue, emr, quicksight, lake-formation, msk, ml-services |
| dr-architecture | 09,26,27,28,29 | dr-strategies, dms, backup, beanstalk, cloudformation, hpc, well-architected |

Format as YAML frontmatter for easy parsing by the skill.

### 3. Create reference file skeletons

Each reference file gets a header and placeholder sections. Content is filled in subsequent phases. This ensures SKILL.md can reference them immediately.

- `prompt-templates.md`: Header + 6 empty mode sections
- `progress-tracking.md`: Header + readiness formula placeholder
- `quiz-flow.md`: Header + quiz protocol placeholder
- `pdf-extractor.md`: Header + subagent prompt placeholder

### 4. Create runtime directories

```bash
mkdir -p aws-csa/study-sessions
```

Create initial `aws-csa/study-progress.md` with empty YAML frontmatter:

```yaml
---
certification: aws-csa
exam_code: SAA-C03
started: null
last_session: null
total_sessions: 0
domains: {}
---

## Session History
```

## Success Criteria

- [ ] `/ai-tutor` is recognized as a skill (appears in skill list)
- [ ] SKILL.md is under 150 lines
- [ ] domains.md contains all 12 domains with correct PDF mappings
- [ ] All 4 reference files exist with headers
- [ ] `aws-csa/` directory and `study-progress.md` exist
- [ ] Arg parsing handles: no args, `progress`, `refresh <domain>`, `[cert] [domain] [mode]`

## Risk Assessment

- **SKILL.md size**: If orchestration logic exceeds 150 lines, extract arg-parsing to a reference file
- **Domain mapping accuracy**: Verify PDF section numbers match actual file names in `sections/`
