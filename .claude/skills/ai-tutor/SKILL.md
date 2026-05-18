---
name: ai-tutor
description: "Interactive AWS certification tutor with guided study paths, quizzes, and progress tracking"
argument-hint: "[domain] [mode] | guided [domain] | free [domain] [mode] | progress | refresh <domain>"
metadata:
  author: user
  version: "2.0.0"
---

# AI Tutor - AWS Certification Study Companion

Interactive tutor for AWS certification prep using PDF course materials, guided 7-phase study paths per domain, interactive quizzes, and progress tracking.

## Data Locations (project root relative)

All mutable user data lives in the **project root**, NOT inside `.claude/skills/ai-tutor/`:

| Type | Path | Purpose |
|------|------|---------|
| Progress | `aws-csa/study-progress.md` | Single source of truth for all study state |
| Sessions | `aws-csa/study-sessions/{timestamp}-{domain}-{mode}.md` | Full session output files |
| Cache | `.claude/skills/ai-tutor/cache/aws-csa-{domain}.md` | Derived PDF extraction (regeneratable) |
| Cert defs | `.claude/skills/ai-tutor/certs/aws-csa/domains.md` | Static domain/topic definitions |

## Argument Parsing

Parse `ARGUMENTS` to determine the action:

| Pattern | Action |
|---------|--------|
| _(empty)_ | Show domain selection → guided mode (default) |
| `progress` | Show progress dashboard (Load: `references/progress-tracking.md`). **Stop after displaying.** |
| `refresh <domain>` | Re-extract PDF cache for domain (Load: `references/pdf-extractor.md`). **Stop after refresh.** |
| `guided <domain>` | Start/resume guided study path for domain |
| `free <domain> <mode>` | Direct mode execution (skip guided path) |
| `<domain>` | Start/resume guided study path for domain |
| `<domain> <mode>` | Direct mode execution (skip guided path) |

## Study Path (Guided Mode — Default)

Each domain follows a 6-phase study path. Phases are completed in order — the tutor auto-recommends the next phase based on progress.

```
Phase 1: LEARN       → concept-mapper         (understand services & relationships)
Phase 2: TEST        → mini-exam:concepts     (test conceptual knowledge)
Phase 3: APPLY       → scenario-generator     (apply to real-world scenarios)
Phase 4: TEST        → mini-exam:scenarios    (test scenario reasoning)
Phase 5: DESIGN      → mini-exam:design       (architecture design decisions — MC format)
Phase 6: FINAL EXAM  → mini-exam:comprehensive (full domain exam — all topics)
```

**Optional tools** (available anytime via `free` mode or follow-up menu):
- `hands-on-lab` — build real AWS infrastructure (CLI-based, requires AWS account)
- `architecture-reviewer` — evaluate architectures against Well-Architected
- `weak-spot-analyzer` — cross-domain gap analysis (no domain needed)
- `exam-strategy-coach` — exam day strategy and study planning (no domain needed)

## Recommended Study Order (Hybrid Plan)

When suggesting the next domain in follow-up menus, use tier-based priority order instead of alphabetical:

| Tier | Domains | Min Phases | Rationale |
|------|---------|-----------|-----------|
| 1 (Core) | compute, networking, storage, security-identity | All 6 | ~60% of exam weight |
| 2 (High) | load-balancing-scaling, databases, serverless, integration-messaging, dns, monitoring-audit | P1-P4 | Solid conceptual + scenario coverage |
| 3 (Coverage) | data-analytics, dr-architecture | P1-P2 | Minimum viable, avoid zero on exam |

**Domain recommendation logic** (for Step 5 follow-up menu):
1. Suggest next unstudied domain from highest incomplete tier (Tier 1 first)
2. Within a tier, order by exam weight: compute → networking → storage → security-identity
3. After all domains reach their tier minimum, suggest: `weak-spot-analyzer` → targeted mini-exams on gaps → retry P6 on Tier 1 domains if <80%
4. Tier 2 domains can be extended to full 6 phases if user is ahead of schedule

## Step 1: Selection

**IMPORTANT:** Domain and mode are selected **sequentially**. Do NOT combine into a single `AskUserQuestion` call.

### Step 1a: Domain selection (if not provided)
Load: `certs/aws-csa/domains.md` to get the 12 domain list.
**First**, print the full domain list as numbered text:

```
📚 Available Domains:
 1. compute                 — Elastic Compute Cloud (EC2), Elastic Container Service (ECS), Elastic Kubernetes Service (EKS), Fargate
 2. storage                 — Elastic Block Store (EBS), Simple Storage Service (S3), Elastic File System (EFS), FSx, Snow Family
 3. databases               — Relational Database Service (RDS), Aurora, DynamoDB, ElastiCache
 4. networking              — Virtual Private Cloud (VPC), Subnets, NAT Gateway, Transit Gateway
 5. security-identity       — Identity and Access Management (IAM), Key Management Service (KMS), Web Application Firewall (WAF), GuardDuty, Cognito
 6. load-balancing-scaling  — Application Load Balancer (ALB), Network Load Balancer (NLB), Auto Scaling Group (ASG)
 7. dns                     — Route 53, Routing Policies
 8. integration-messaging   — Simple Queue Service (SQS), Simple Notification Service (SNS), Kinesis, Amazon MQ
 9. serverless              — Lambda, API Gateway, Step Functions
10. monitoring-audit        — CloudWatch, CloudTrail, AWS Config
11. data-analytics          — Athena, Redshift, Glue, Elastic MapReduce (EMR)
12. dr-architecture         — Disaster Recovery (DR) Strategies, CloudFormation, Well-Architected Framework
```

**Then**, use `AskUserQuestion` with 4 recommended options. User can type any domain name or number via "Other".
Rotate the 4 shown options based on study-progress.md: prioritize domains with lowest phase or least recent study. If no progress data, default to: `compute`, `storage`, `databases`, `networking`.

**Wait for user response before proceeding.**

### Step 1b: Mode selection

Read `aws-csa/study-progress.md` to determine `current_phase` for the selected domain.

**In guided mode** (default): Auto-determine the next phase. Show the user:

```
📍 {Domain} — Phase {N}/7: {phase_name}
   {phase_description}

Previous phases: ✓ Phase 1 (concept-mapper) ✓ Phase 2 (mini-exam) ...
```

Use `AskUserQuestion`:
- `Continue to Phase {N}` (Recommended)
- `Repeat Phase {N-1}`
- `Switch to free mode`

**In free mode** (if user typed `free` or chose it): Print full mode list, then `AskUserQuestion` with 4 options:

```
🎯 Study Modes:
 1. concept-mapper          — Knowledge synthesis and service relationships
 2. mini-exam               — Interactive quiz with scoring
 3. scenario-generator      — Realistic exam scenarios with explanations
 4. hands-on-lab            — Build real AWS infrastructure (optional, requires AWS account)
 5. architecture-reviewer   — Evaluate architectures against Well-Architected
 6. weak-spot-analyzer      — Identify and prioritize weak areas (no domain needed)
 7. exam-strategy-coach     — Exam day strategy and study planning (no domain needed)
```

Default shown options: `concept-mapper`, `mini-exam`, `scenario-generator`, `hands-on-lab`.

**Wait for user response before proceeding to Step 2.**

## Step 2: Load Context

1. Read `certs/aws-csa/domains.md` for topic checklist
2. Read `aws-csa/study-progress.md` for current progress (create if missing — see edge cases)
3. **If mode requires domain cache** (concept-mapper, mini-exam, scenario-generator, hands-on-lab, architecture-reviewer):
   Check cache: `.claude/skills/ai-tutor/cache/aws-csa-{domain}.md`
   - **Cache HIT**: Read cached content, proceed to Step 3
   - **Cache MISS**: Load `references/pdf-extractor.md` and spawn pdf-extractor subagent
     - Agent type: `general-purpose`, model: `haiku`
     - Input: domain name + PDF paths from domains.md
     - Output: writes cache file
     - Wait for completion, then read cache file
4. **If mode is domain-less** (weak-spot-analyzer, exam-strategy-coach): Skip cache, proceed with progress data only

## Step 3: Execute Mode

Load `references/prompt-templates.md` for the selected mode's template.

| Mode | Additional Input | Interactive? |
|------|-----------------|-------------|
| `concept-mapper` | Cache file | No |
| `mini-exam` | Cache + quiz-flow.md + **scope** | Yes (AskUserQuestion) |
| `scenario-generator` | Cache file | No |
| `hands-on-lab` | Cache file | No |
| `architecture-reviewer` | Cache + user architecture | Yes (AskUserQuestion) |
| `weak-spot-analyzer` | study-progress.md only | No |
| `exam-strategy-coach` | study-progress.md + timeline | Yes (AskUserQuestion) |

**Mini-exam scope** (guided mode phases):
- Phase 2: `scope=concepts` — test conceptual knowledge from concept-mapper
- Phase 4: `scope=scenarios` — test scenario reasoning from scenario-generator
- Phase 5: `scope=design` — test architecture design decisions and trade-offs
- Phase 6: `scope=comprehensive` — full domain exam covering all topics
- Free mode: `scope=general` — balanced mix (default behavior)

For `mini-exam`: Load `references/quiz-flow.md` for the interactive quiz protocol. Pass `scope` to the quiz generator.

Generate content following the mode's prompt template. Display output in terminal.

**Content output modes** (concept-mapper, scenario-generator, hands-on-lab):
- Check if session file already exists for this domain+mode: `aws-csa/study-sessions/*-{domain}-{mode}.md`
- **If exists AND user did NOT request regenerate**: Read and display the cached session file instead of regenerating. Show: `📄 Loading saved {mode} content. Use "Regenerate" option to create fresh content.`
- **If not exists OR user requested regenerate**: Generate fresh content, display it, and save to session file (full content, not summary)

## Step 4: Save & Track

Load `references/progress-tracking.md` for the update protocol.

1. Save session output — **write the FULL generated content** to the session file, not just a summary:
   - **Domain modes**: `aws-csa/study-sessions/{YYMMDD}-{HHMM}-{domain}-{mode}.md`
   - **Cross-domain modes**: `aws-csa/study-sessions/{YYMMDD}-{HHMM}-{mode}.md`
   - Use `bash -c 'date +%y%m%d-%H%M'` for timestamp
   - For concept-mapper, scenario-generator, hands-on-lab: the session file IS the study material — include all generated text
2. Update `aws-csa/study-progress.md` following the update protocol
   - **Guided mode**: Also update `current_phase` (advance to next phase)
   - **Mini-exam phases**: Record `phase_scores` with the exam score
3. Show phase completion status

## Step 5: Follow-Up Menu

**Guided mode** — show phase-aware next step:

```
✓ Phase {N} complete: {mode_name} ({domain})
  {score summary if mini-exam}

Next: Phase {N+1} — {next_mode_name} ({description})
```

Use `AskUserQuestion`:
- `Continue to Phase {N+1}` (Recommended) — proceed in guided path
- `Repeat Phase {N}` — redo current phase
- `Regenerate Phase {N}` — regenerate fresh content (ignores saved session file)
- `Switch domain / Done` — change domain or end session

If user selects "Other", also accept: `architecture-reviewer`, `weak-spot-analyzer`, `exam-strategy-coach`, `free`, `progress`, `done`.

**After Phase 6 (final exam)**: Show domain completion celebration + full progress dashboard.
Compute readiness using the **exact formula** from `references/progress-tracking.md` § Readiness Formula — do NOT invent ad-hoc metrics (domain coverage %, exam weight %, etc.):

```
🎉 Domain Complete: {Domain}!
   Phase scores: P2={score}% → P4={score}% → P5={score}% → P6={score}%
   Domain readiness: {readiness}% (formula: coverage×0.3 + exam_avg×0.5 + recency×0.2)
```

Then display the **full progress dashboard** (same format as `/ai-tutor progress` — see `references/progress-tracking.md` § Dashboard Format). This ensures the readiness numbers shown here match exactly what the dashboard shows.

After the dashboard, show recommendation:
```
Recommended: Start {next_unstudied_domain} or run weak-spot-analyzer
```

**Free mode** — show generic menu:
- `Continue studying` — return to Step 1
- `Switch to guided mode` — start/resume guided path
- `View progress` — show dashboard
- `Done` — end session

## Edge Cases

- **No study-progress.md**: Create initial file with empty YAML frontmatter (see `references/progress-tracking.md`)
- **PDF extraction fails**: Show error, suggest `/ai-tutor refresh {domain}`
- **No exam history**: weak-spot-analyzer and exam-strategy-coach show "No exam data yet. Start with a guided study path to build progress."
- **Resuming a domain**: If `current_phase > 1`, show completed phases and resume from next incomplete phase
- **Phase 6 passed (≥80%)**: Mark domain as "completed" in progress. User can still repeat or free-mode study.
- **Phase 6 failed (<80%)**: Recommend repeating weak phases based on `phase_scores`, then retake Phase 6.
- **Invalid args**: Show usage:
  ```
  Usage: /ai-tutor [domain]              — guided study path (default)
         /ai-tutor free [domain] [mode]  — free mode, any mode
         /ai-tutor progress              — view dashboard
         /ai-tutor refresh <domain>      — refresh PDF cache
  Example: /ai-tutor compute
           /ai-tutor free storage mini-exam
  ```
