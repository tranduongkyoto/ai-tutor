# Brainstorm Report: AI Tutor Skill for AWS Certification

**Date:** 2026-05-11 | **Status:** Approved

---

## Problem Statement

Build a Claude Code skill (`/ai-tutor`) that helps users study for AWS certifications using PDF course material. The skill provides 6 tutor modes, interactive quizzes, and progress tracking — all within the CLI.

## Decisions

| # | Area | Decision |
|---|------|----------|
| 1 | Scope | Multi-cert structure, AWS CSA (SAA-C03) populated first |
| 2 | Content source | PDF-based via Haiku subagent + cache |
| 3 | Quiz format | 5 options (A-E) as terminal text, AskUserQuestion for answer selection |
| 4 | Quiz size | User chooses (5/10/15) per session |
| 5 | Progress storage | Cert-specific folder: `aws-csa/study-progress.md` |
| 6 | Session outputs | `aws-csa/study-sessions/{YYMMDD}-{HHMM}-{domain}-{mode}.md` |
| 7 | UX flow | Args with menu fallback (`/ai-tutor [cert] [domain] [mode]`) |
| 8 | Skill location | `.claude/skills/ai-tutor/` (project-scoped) |
| 9 | Questions | Dynamic from cached PDF extract + topic checklist per domain |
| 10 | Tutor modes | All 6 in MVP |
| 11 | Output mode | Terminal display + auto-save to .md |
| 12 | Readiness calc | Weighted: coverage(30%) + exam(50%) + recency(20%), computed dynamically |
| 13 | Recency decay | 7-day grace → linear decay to 0 at 30 days |
| 14 | Session history | Append-only log in study-progress.md |
| 15 | Recommendations | Always show after every session |
| 16 | SKILL.md | Modularized via references/ files |
| 17 | Question quality | Strict prompt guardrails + self-verify step |
| 18 | Architecture | Only pdf-extractor as subagent; all modes inline in main skill |

---

## Architecture

### File Structure

```
.claude/skills/ai-tutor/
├── SKILL.md                        # Orchestrator (~150 lines)
├── README.md                       # User docs
├── references/
│   ├── prompt-templates.md         # 6 tutor mode prompt templates
│   ├── progress-tracking.md        # Readiness formula + update protocol
│   ├── quiz-flow.md                # Interactive quiz protocol
│   └── pdf-extractor.md            # Subagent prompt for PDF extraction
├── cache/                          # Auto-generated (one .md per domain)
│   ├── aws-csa-compute.md
│   ├── aws-csa-storage.md
│   └── ...
└── certs/
    └── aws-csa/
        └── domains.md              # 12 domains + topic checklists + PDF mappings

aws-csa/                            # Cert folder at project root
├── study-progress.md               # Progress tracker (YAML frontmatter + session log)
└── study-sessions/                 # Session artifacts
    ├── 260511-1030-compute-concept-mapper.md
    ├── 260511-1400-storage-exam.md
    └── ...

sections/                           # Source PDFs (existing, 31 files, 849 pages)
```

### Flow

```
/ai-tutor [cert] [domain] [mode]
    │
    ├─ Step 1: Parse args or show menus
    │   ├─ /ai-tutor progress → skip to progress dashboard
    │   ├─ /ai-tutor refresh <domain> → re-extract PDFs
    │   └─ Normal: cert → domain → mode selection
    │
    ├─ Step 2: Load context
    │   ├─ Read certs/aws-csa/domains.md (topic checklist)
    │   ├─ Read aws-csa/study-progress.md (current progress)
    │   └─ Check cache/aws-csa-{domain}.md exists
    │       └─ Cache MISS → spawn pdf-extractor subagent (Haiku)
    │           ├─ Reads mapped PDF sections (multimodal)
    │           ├─ Extracts concepts, diagram descriptions, numbers
    │           └─ Writes cache file
    │
    ├─ Step 3: Execute mode
    │   ├─ Read references/prompt-templates.md for selected mode
    │   ├─ Read cache file for domain knowledge
    │   ├─ Generate content (concept map / scenarios / lab / etc.)
    │   ├─ For mini-exam: generate questions → self-verify → quiz via AskUserQuestion
    │   └─ Display output in terminal
    │
    ├─ Step 4: Save & track
    │   ├─ Write session output to aws-csa/study-sessions/
    │   ├─ Update aws-csa/study-progress.md (YAML + session log entry)
    │   └─ Show recommendation for next study action
    │
    └─ Step 5: Follow-up menu
        ├─ Continue with another domain/mode
        ├─ View progress dashboard
        └─ Done
```

### Why Only pdf-extractor Is a Subagent

| Component | Subagent? | Reason |
|-----------|:---------:|--------|
| pdf-extractor | Yes | Different model (Haiku, cheaper), heavy multimodal I/O (40-80 pages), write-once cache, no user interaction |
| 6 tutor modes | No | Mini-exam needs AskUserQuestion (interactive, subagents can't use it). All modes share same context (domain data, cache, progress) |
| Progress tracker | No | Simple YAML read/write + math calculation. Not worth subagent overhead |
| Question verifier | No | Single follow-up prompt within same context. Subagent would need all questions re-passed |

---

## 6 Tutor Modes

### 1. Concept Mapper
- Input: domain + cached PDF content
- Output: real-world use cases, service integrations, architectural patterns, cost implications, security considerations
- Saved to: `{YYMMDD}-{HHMM}-{domain}-concept-mapper.md`

### 2. Scenario Generator
- Input: domain + cached PDF content
- Output: 5 realistic exam scenarios with business context, technical requirements, 5 options (A-E), detailed explanations for correct and wrong answers
- Saved to: `{YYMMDD}-{HHMM}-{domain}-scenario-generator.md`

### 3. Weak Spot Analyzer
- Input: study-progress.md (all domains)
- Output: prioritized weak areas, targeted study plan, estimated time per area, specific topics to focus on
- Saved to: `{YYMMDD}-{HHMM}-weak-spot-analysis.md`

### 4. Hands-On Lab Creator
- Input: domain + cached PDF content
- Output: progressive lab exercise (basic → enterprise), troubleshooting scenarios, integration exercises, cleanup procedures
- Saved to: `{YYMMDD}-{HHMM}-{domain}-hands-on-lab.md`

### 5. Architecture Reviewer
- Input: user describes their architecture (via text or follow-up prompt)
- Output: evaluation against Well-Architected Framework, single points of failure, scaling analysis, cost optimization, security review
- Saved to: `{YYMMDD}-{HHMM}-{domain}-arch-review.md`

### 6. Exam Strategy Coach
- Input: study-progress.md + user's exam timeline/concerns
- Output: exam day strategy, time management, common traps, last-minute priorities, confidence building
- Saved to: `{YYMMDD}-{HHMM}-exam-strategy.md`

---

## Mini Exam Flow

```
1. User selects mini-exam mode
2. AskUserQuestion: "How many questions?" → 5 / 10 / 15
3. Skill reads:
   - cache/aws-csa-{domain}.md (knowledge)
   - domains.md topic checklist (coverage guide)
   - study-progress.md (weak topics to prioritize)
4. Generate N questions with 5 options each (A-E)
5. Self-verify: "Review each question. Is correct answer unambiguous? Fix issues."
6. Present questions in rounds (2 per AskUserQuestion call):
   - Display question + all 5 options as terminal text
   - AskUserQuestion with options: A, B, C, D (user types E via Other)
7. After all rounds: score, show per-question feedback
8. Update study-progress.md:
   - Append exam entry with score + missed_topics
   - Update domain's weak_topics list
9. Show recommendation for next study action
```

---

## Progress Tracking

### study-progress.md Structure

```yaml
---
certification: aws-csa
exam_code: SAA-C03
started: 2026-05-11
last_session: 2026-05-15
total_sessions: 8

domains:
  compute:
    sessions_count: 5
    modes_completed: [concept-mapper, scenario-generator, mini-exam, hands-on-lab]
    exams:
      - date: 2026-05-11
        score: 7
        total: 10
        missed_topics: [placement-groups, spot-fleets]
      - date: 2026-05-13
        score: 9
        total: 10
        missed_topics: [hibernate]
    weak_topics: [hibernate]
    last_studied: 2026-05-15

  storage:
    sessions_count: 3
    modes_completed: [concept-mapper, mini-exam]
    exams:
      - date: 2026-05-12
        score: 5
        total: 10
        missed_topics: [efs-throughput, s3-lifecycle, ebs-multi-attach, fsx-lustre, storage-gateway]
    weak_topics: [efs-throughput, fsx-lustre]
    last_studied: 2026-05-14

  # ... remaining domains (not-started domains have empty arrays)
---

## Session History

### 2026-05-15 10:30 | Compute | Mini Exam
- Score: 9/10 (90%)
- Missed: hibernate
- Output: study-sessions/260515-1030-compute-exam.md

### 2026-05-14 09:00 | Storage | Concept Mapper
- Topics: EBS types, EFS, S3 classes, FSx
- Output: study-sessions/260514-0900-storage-concept-mapper.md
```

### Readiness Formula (Computed Dynamically)

```
readiness = (coverage * 0.3) + (exam_avg * 0.5) + (recency * 0.2)

coverage = modes_completed.length / 6 * 100
exam_avg = average of last 2 exam scores (or latest if only 1)
recency  = 100 if last_studied <= 7 days ago
           linear decay from 100→0 between day 7 and day 30
           0 if last_studied > 30 days ago
```

### Status Thresholds

| Readiness | Status | Symbol |
|-----------|--------|--------|
| >= 80% | Mastered | ★ |
| 60-79% | Proficient | ◆ |
| 30-59% | Developing | ▲ |
| 1-29% | Beginning | △ |
| 0% | Not started | ○ |

### Progress Dashboard (`/ai-tutor progress`)

```
AWS CSA (SAA-C03) - Study Progress
Started: 2026-05-11 | Last: 2026-05-15 | Sessions: 8
Overall Readiness: 42%  ████████░░░░░░░░░░░░  5/12 domains

Domain              Ready  Exams  Last     Status
────────────────── ────── ────── ──────── ──────────
Compute             85%    3      2d ago   ★ Mastered
Storage             62%    2      3d ago   ◆ Proficient
Databases           45%    1      5d ago   ▲ Developing
Networking          30%    0      7d ago   ▲ Developing
Security              0%    -      -        ○ Not started
... (remaining domains)

Weak Areas: hibernate, efs-throughput, fsx-lustre, vpc-peering
Recommended Next: Networking (lowest active score, 7d stale)
```

---

## Domains & Topic Checklists (AWS CSA)

12 domains mapped to PDF sections:

| Domain | PDF Sections | ~Topics |
|--------|-------------|---------|
| Compute | 03, 04, 16 | instance-types, security-groups, purchasing, placement-groups, eni, hibernate, ecs, eks, fargate |
| Storage | 05, 10, 11, 12, 14 | ebs-types, ebs-snapshots, efs, s3-classes, s3-lifecycle, s3-security, fsx, snow-family, storage-gateway |
| Databases | 07, 19 | rds, aurora, elasticache, dynamodb, rds-proxy, documentdb, neptune, keyspaces, qldb, timestream |
| Networking | 25 | vpc, subnets, nacl-vs-sg, nat-gateway, vpc-peering, vpc-endpoints, dx, transit-gateway, flow-logs |
| Security & Identity | 02, 23, 24 | iam, organizations, scp, kms, ssm-params, waf, shield, guardduty, inspector, macie, cognito |
| Load Balancing & Scaling | 06 | alb, nlb, gwlb, asg, sticky-sessions, cross-zone, ssl-sni, connection-draining |
| DNS | 08 | route53-records, routing-policies, health-checks, alias-vs-cname, hybrid-dns |
| Integration & Messaging | 15 | sqs, sns, kinesis-streams, kinesis-firehose, fan-out, amazon-mq |
| Serverless | 17, 18 | lambda, api-gateway, step-functions, cognito, lambda-edge, cloudfront-functions |
| Monitoring & Audit | 22 | cloudwatch, cloudtrail, config, eventbridge, insights |
| Data & Analytics | 20, 21 | athena, redshift, glue, emr, quicksight, lake-formation, msk, ml-services |
| DR & Architecture | 09, 26, 27, 28, 29 | dr-strategies, dms, backup, beanstalk, cloudformation, hpc, well-architected |

---

## Problems Identified & Resolutions

| # | Problem | Resolution |
|---|---------|------------|
| 1 | PDF token cost (40-80 pages per domain) | Haiku subagent extracts to cache. First run expensive; subsequent runs read cached .md |
| 2 | AskUserQuestion max 4 options vs 5-option exam format | Display all 5 options as terminal text; use AskUserQuestion A/B/C/D + Other for E |
| 3 | Multi-cert progress file collision | Cert-specific folders: `aws-csa/study-progress.md` |
| 4 | Session file name collisions | Timestamp-based: `{YYMMDD}-{HHMM}-{domain}-{mode}.md` |
| 5 | SKILL.md too large (500+ lines) | Modularize via references/: prompt-templates.md, progress-tracking.md, quiz-flow.md |
| 6 | Readiness score staleness with recency decay | Store raw data only; compute readiness dynamically on every view |
| 7 | Dynamic question quality inconsistency | Strict prompt guardrails + self-verify step before presenting to user |

---

## Implementation Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| PDF extractor misses diagram info | Medium | Haiku is multimodal; prompt instructs to describe all visuals. User can `/ai-tutor refresh` to re-extract |
| Cache files grow too large | Low | Each domain is 40-80 pages of slides; extracted text should be 300-600 lines max |
| study-progress.md grows unbounded | Low | Append-only log; after 100+ sessions it's ~500 lines of YAML + history. Manageable for .md |
| AskUserQuestion "Other" UX for option E | Low | Rare — most AWS exam questions use 4 options. "Other" is clear fallback |
| Self-verify step adds latency | Low | Single follow-up prompt; ~5 seconds. Worth it for question quality |

---

## Success Metrics

1. User can complete a full study session (any mode) in < 15 minutes
2. Mini-exam questions are unambiguous and grounded in PDF content
3. Progress dashboard accurately reflects study state across all 12 domains
4. Weak-spot recommendations align with actual exam score patterns
5. Cache extraction preserves key concepts including diagram descriptions

---

## Next Steps

1. Create implementation plan (`/ck:plan`)
2. Phase 1: Skill skeleton (SKILL.md + references + domains.md)
3. Phase 2: PDF extractor subagent + cache system
4. Phase 3: First 2 modes (concept-mapper + mini-exam)
5. Phase 4: Remaining 4 modes
6. Phase 5: Progress tracking + dashboard
7. Phase 6: Polish (recommendations, follow-up menus, edge cases)

## Unresolved Questions

None — all design decisions resolved during brainstorm session.
