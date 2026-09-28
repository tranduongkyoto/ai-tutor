---
name: ai-tutor
description: "Interactive AWS certification tutor with guided study paths, quizzes, and progress tracking"
argument-hint: "[sap] [domain] [mode] | practice-test [sap] | sap test-review <result-file> [--vi] | sap review-set <N> | guided [domain] | free [domain] [mode] | progress | refresh <domain>"
metadata:
  author: user
  version: "2.2.0"
---

# AI Tutor - AWS Certification Study Companion

Interactive tutor for AWS certification prep using PDF course materials, guided 4-phase study paths per domain, interactive quizzes, and progress tracking.

Supports: **SAA-C03** (Associate) and **SAP-C02** (Professional).

## Cert Selection

Detect cert from arguments:
- `sap`, `SAP`, `SAP-C02`, `professional` → load `certs/aws-sap/domains.md`
- Default (no cert keyword) → load `certs/aws-csa/domains.md` (SAA-C03)
- `practice-test sap` → SAP practice tests from `practice-exam/sap/`

SAP-specific notes:
- SAP has 4 domains (not 12), 75 questions (not 65), 180 minutes (not 130)
- SAP pass threshold: 80% on practice tests (vs 72% for SAA)
- SAP practice tests are in `practice-exam/sap/practice_test_{N}.md`
- SAP study pipeline & labs defined in `certs/aws-sap/domains.md`
- SAP questions have detailed `**Explanation:**` sections — show AFTER user answers

## Data Locations (project root relative)

All mutable user data lives in the **project root**, NOT inside `.claude/skills/ai-tutor/`:

### SAA-C03 (Associate)
| Type | Path | Purpose |
|------|------|---------|
| Progress | `aws-csa/study-progress.md` | Single source of truth for all study state |
| Sessions | `aws-csa/study-sessions/{timestamp}-{domain}-{mode}.md` | Full session output files |
| Cache | `.claude/skills/ai-tutor/cache/aws-csa-{domain}.md` | Derived PDF extraction (regeneratable) |
| Cert defs | `.claude/skills/ai-tutor/certs/aws-csa/domains.md` | Static domain/topic definitions |

### SAP-C02 (Professional)
| Type | Path | Purpose |
|------|------|---------|
| Progress | `aws-sap/study-progress.md` | SAP study state |
| Sessions | `aws-sap/study-sessions/{timestamp}-{domain}-{mode}.md` | SAP session files |
| Practice tests (Udemy) | `practice-exam/sap/practice_test_{N}.md` | 3 tests (30q + 75q + 75q) |
| Practice tests (TD) | `practice-exam/sap/SAP-Review-Mode-Set-{N}.md` | 6 sets (75q x5 + 16q) = 391q |
| Practice progress | `practice-exam/sap/practice_test_{N}_progress.md` | Per-test progress tracking |
| TD timed results | `practice-exam/sap/TD_SAP_Timed_Set{N}_Full.md` | Exported TD timed test (shuffled order) — input to `test-review` |
| TD review-mode results | `practice-exam/sap/td_review_set_{N}_session.json` → `TD_SAP_Review_Set{N}_Full.md` | `review-set` session state, then an export in the timed-export format (input to `test-review`) |
| Test review | `practice-exam/sap/td_set_{n}_{analysis.md,review.md,review_correct.md,review_notes.json}` | Output of `test-review` (see `references/test-review-flow.md`) |
| Review scripts | `.claude/skills/ai-tutor/scripts/*.py` | Build/verify review files, merge Vietnamese sections |
| Cert defs | `.claude/skills/ai-tutor/certs/aws-sap/domains.md` | SAP domains, labs, pipeline |
| Pipeline report | `.claude/skills/ai-tutor/certs/aws-sap/study-pipeline.md` | Full study timeline |

## Argument Parsing

Parse `ARGUMENTS` to determine the action:

| Pattern | Action |
|---------|--------|
| _(empty)_ | Show domain selection → guided mode (default, SAA) |
| `sap` | Show SAP domain selection → guided mode |
| `sap practice-test` or `practice-test sap` | Start SAP practice test (Load: `references/practice-test-flow.md` with SAP cert) |
| `sap chapter-drill <chapter>` | Quiz Udemy practice questions for a chapter (Load: `certs/aws-sap/chapter-question-map.md` + `references/practice-test-flow.md`) |
| `sap chapter-drill <chapter> dojo` | Quiz Tutorials Dojo questions for a chapter (Load: `certs/aws-sap/chapter-question-map-td.md` + `references/practice-test-flow.md`) |
| `sap test-review <result-file> [--vi]` | Analyze a TD timed-test export → analysis + wrong/correct review files + redo tracker (Load: `references/test-review-flow.md`). `--vi` adds Vietnamese deep-dive per question (Load: `references/vietnamese-explanation-style.md`) |
| `sap test-review <set> redo <group>[,<group>]` | Redo a review group's questions, record tracker pass (Load: `references/test-review-flow.md` § Redo sessions) |
| `sap review-set <N>` | Full TD set in review mode, in blocks of 25 (answer 25 with no feedback, then review), with resume support. Exports in the timed-export format for `test-review`. Only TD1, TD2 and TD5; TD3, TD4 and TD6 stay timed-only (Load: `references/review-set-flow.md`) |
| `progress` | Show progress dashboard (Load: `references/progress-tracking.md`). **Stop after displaying.** |
| `refresh <domain>` | Re-extract PDF cache for domain (Load: `references/pdf-extractor.md`). **Stop after refresh.** |
| `refresh cheat-sheet` | Re-extract cheat sheet PDF cache (Load: `references/pdf-extractor.md` § Cheat Sheet Extraction). **Stop after refresh.** |
| `keyword-drill` | Start keyword pattern drill (no domain needed) |
| `mock-exam` | Start full mock exam (requires ≥8/12 domain caches) |
| `practice-test` | Start SAA practice test (Load: `references/practice-test-flow.md`). Interactive test from `practice-exam/` questions. |
| `guided <domain>` | Start/resume guided study path for domain |
| `free <domain> <mode>` | Direct mode execution (skip guided path) |
| `<domain>` | Start/resume guided study path for domain |
| `<domain> <mode>` | Direct mode execution (skip guided path) |

## Study Path (Guided Mode — Default)

Each domain follows a 4-phase study path. Phases are completed in order — the tutor auto-recommends the next phase based on progress.

```
Phase 1: LEARN + TEST  → learn-and-test         (content to .md first, then per-section: teach → quiz → save, with resume)
Phase 2: APPLY + TEST  → scenario-practice       (content to .md first, then per-scenario: teach → hint → answer → reveal, with resume)
Phase 3: DESIGN        → mini-exam:design        (architecture design decisions — MC format)
Phase 4: FINAL EXAM    → mini-exam:comprehensive  (full domain exam — all topics)
```

**Optional tools** (available anytime via `free` mode or follow-up menu):
- `concept-mapper` — standalone knowledge synthesis and service relationships
- `scenario-generator` — standalone realistic exam scenarios with explanations
- `hands-on-lab` — build real AWS infrastructure (CLI-based, requires AWS account)
- `architecture-reviewer` — evaluate architectures against Well-Architected
- `weak-spot-analyzer` — cross-domain gap analysis (no domain needed)
- `exam-strategy-coach` — exam day strategy and study planning (no domain needed)
- `keyword-drill` — quick-fire exam keyword → service mapping drill (no domain needed)
- `mock-exam` — full 65-question timed SAA-C03 mock exam (no domain needed, requires ≥8 domain caches)
- `practice-test` — Udemy practice test with answer tracking, domain filter, redo wrong, weakness report (no domain needed)

## Recommended Study Order (Hybrid Plan)

When suggesting the next domain in follow-up menus, use tier-based priority order instead of alphabetical:

| Tier | Domains | Min Phases | Weight | Rationale |
|------|---------|-----------|--------|-----------|
| 1 (Core) | compute, networking, storage, security-identity, dr-architecture | All 4 | 65% (12.5% each + DR 15%) | Foundation + DR heavily tested (~16-20% of real exam) |
| 2 (High) | load-balancing-scaling, databases, serverless, integration-messaging, dns, monitoring-audit, data-analytics | P1-P2 | 35% (5% each) | Solid learn + scenario coverage |

**Domain recommendation logic** (for Step 5 follow-up menu):
1. Suggest next unstudied domain from highest incomplete tier (Tier 1 first)
2. Within a tier, order by exam weight: compute → networking → storage → security-identity
3. After all domains reach their tier minimum, suggest: `weak-spot-analyzer` → targeted mini-exams on gaps → retry P4 on Tier 1 domains if <80%
4. Tier 2 domains can be extended to full 4 phases if user is ahead of schedule

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
📍 {Domain} — Phase {N}/4: {phase_name}
   {phase_description}

Previous phases: ✓ Phase 1 (learn-and-test) ✓ Phase 2 (scenario-practice) ...
```

Use `AskUserQuestion`:
- `Continue to Phase {N}` (Recommended)
- `Repeat Phase {N-1}`
- `Switch to free mode`

**In free mode** (if user typed `free` or chose it): Print full mode list, then `AskUserQuestion` with 4 options:

```
🎯 Study Modes:
 1. learn-and-test          — Section-by-section: teach → quiz with hints (guided P1)
 2. scenario-practice       — Content to .md first, then per-scenario: teach → hint → answer → reveal → save (guided P2)
 3. concept-mapper          — Standalone knowledge synthesis and service relationships
 4. mini-exam               — Interactive quiz with scoring
 5. scenario-generator      — Standalone realistic exam scenarios with explanations
 6. hands-on-lab            — Build real AWS infrastructure (optional, requires AWS account)
 7. architecture-reviewer   — Evaluate architectures against Well-Architected
 8. weak-spot-analyzer      — Identify and prioritize weak areas (no domain needed)
 9. exam-strategy-coach     — Exam day strategy and study planning (no domain needed)
10. keyword-drill            — Quick-fire exam keyword → service mapping drill (no domain needed)
11. mock-exam                — Full 65-question timed SAA-C03 mock exam (no domain needed, requires ≥8 domain caches)
12. practice-test            — Udemy practice test with answer tracking, redo wrong, weakness report (no domain needed)
```

Default shown options: `concept-mapper`, `mini-exam`, `scenario-generator`, `hands-on-lab`.

**Wait for user response before proceeding to Step 2.**

## Step 2: Load Context

1. Read `certs/aws-csa/domains.md` for topic checklist
2. Read `aws-csa/study-progress.md` for current progress (create if missing — see edge cases)
3. **If mode requires domain cache** (learn-and-test, scenario-practice, concept-mapper, mini-exam, scenario-generator, hands-on-lab, architecture-reviewer):
   Check cache: `.claude/skills/ai-tutor/cache/aws-csa-{domain}.md`
   - **Cache HIT**: Read cached content, proceed to Step 3
   - **Cache MISS**: Load `references/pdf-extractor.md` and spawn pdf-extractor subagent
     - Agent type: `general-purpose`, model: `haiku`
     - Input: domain name + PDF paths from domains.md
     - Output: writes cache file
     - Wait for completion, then read cache file
   - **learn-and-test** also needs: `references/quiz-flow.md` (hint flow protocol) + cheat-sheet cache (see item 4) + cross-domain topics from `certs/aws-csa/scenario-map.md` (the `### cross-domain-topics` section for this domain)
   - **scenario-practice** also needs: `certs/aws-csa/scenario-map.md` (loaded here in Step 2, not Step 3) + cheat-sheet cache (see item 4)
4. **Cheat sheet cache** (for modes that use it):
   Check cache: `.claude/skills/ai-tutor/cache/aws-csa-cheat-sheet.md`
   - **Cache HIT**: Read cached content, add to context
   - **Cache MISS**: Load `references/pdf-extractor.md` § Cheat Sheet Extraction
     - Spawn pdf-extractor subagent for cheat sheet
     - Wait for completion, then read cache file
   - **Modes that use cheat sheet**: learn-and-test, mini-exam (design/comprehensive/general), scenario-practice, scenario-generator, keyword-drill, mock-exam
   - **Mini-exam cross-domain cache loading** (design/comprehensive scopes only):
     After loading the current domain cache, read `aws-csa/study-progress.md` to identify
     studied domains (current_phase >= 2). Read `certs/aws-csa/scenario-map.md` →
     `### cross-domain-topics` for the current domain. For each mapped domain that is
     in the studied list, also load `cache/aws-csa-{paired-domain}.md`.
     These caches provide content grounding for cross-domain questions.
     Do NOT load caches for unstudied domains.
5. **If mode is keyword-drill**: Skip domain cache. Load `references/keyword-patterns.md` + cheat sheet cache (step 4). No domain selection needed.
6. **If mode is mock-exam**: Load ALL available domain caches + cheat sheet cache + `references/mock-exam-flow.md`. No domain selection needed. Prerequisite: ≥8/12 domain caches must exist.
8. **If mode is practice-test**: Load `references/practice-test-flow.md`. No domain cache needed — questions come from `practice-exam/practice-test-{N}-questions.md`. No domain selection needed (handled inside the flow).
7. **If mode is domain-less** (weak-spot-analyzer, exam-strategy-coach): Skip cache, proceed with progress data only

## Step 3: Execute Mode

Load `references/prompt-templates.md` for the selected mode's template.

| Mode | Additional Input | Interactive? |
|------|-----------------|-------------|
| `learn-and-test` | Cache + quiz-flow.md + cheat-sheet + cross-domain topics | Yes (AskUserQuestion) |
| `scenario-practice` | Cache + scenario-map + cheat-sheet | Yes (AskUserQuestion) |
| `concept-mapper` | Cache file | No |
| `mini-exam` | Cache + quiz-flow.md + **scope** + paired domain caches (design/comprehensive) + scenario-map cross-domain-topics | Yes (AskUserQuestion) |
| `scenario-generator` | Cache file | No |
| `hands-on-lab` | Cache file | No |
| `architecture-reviewer` | Cache + user architecture | Yes (AskUserQuestion) |
| `weak-spot-analyzer` | study-progress.md only | No |
| `exam-strategy-coach` | study-progress.md + timeline | Yes (AskUserQuestion) |
| `keyword-drill` | keyword-patterns.md + cheat-sheet cache | Yes (AskUserQuestion) |
| `mock-exam` | All domain caches + cheat-sheet + mock-exam-flow.md | Yes (AskUserQuestion, batched) |
| `practice-test` | practice-exam/practice-test-{N}-questions.md + progress file | Yes (AskUserQuestion + typed input) |

**learn-and-test section-by-section flow:** This mode writes full content (all 7 sections with diagrams) to the session file first, then teaches and quizzes one section at a time. Per section: output content to terminal → quiz with hints → save quiz results inline in the .md file → next section. Supports resume — if interrupted, detects `[PARTIAL]` in the session file and picks up at the next unquizzed section.

**Guided mode scope mapping** (4 phases):
- Phase 1: `learn-and-test` — content-first: generates all sections to .md file, then teaches + quizzes section-by-section with resume support (no scope param)
- Phase 2: `scenario-practice` — content-first: generates all scenarios to .md file, then practices scenario-by-scenario with hints and resume support (no scope param)
- Phase 3: `mini-exam` with `scope=design` — architecture design decisions and trade-offs
- Phase 4: `mini-exam` with `scope=comprehensive` — full domain exam covering all topics
- Free mode mini-exam: `scope=general` — balanced mix (default behavior)

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
   - For learn-and-test, scenario-practice, concept-mapper, scenario-generator, hands-on-lab: the session file IS the study material — include all generated text
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

**After Phase 4 (final exam)**: Show domain completion celebration + full progress dashboard.
Compute readiness using the **exact formula** from `references/progress-tracking.md` § Readiness Formula — do NOT invent ad-hoc metrics (domain coverage %, exam weight %, etc.):

```
🎉 Domain Complete: {Domain}!
   Phase scores: P1={score}% → P2={score}% → P3={score}% → P4={score}%
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
- **Phase 4 passed (≥80%)**: Mark domain as "completed" in progress. User can still repeat or free-mode study.
- **Phase 4 failed (<80%)**: Recommend repeating weak phases based on `phase_scores`, then retake Phase 4.
- **Mock exam with <8 domain caches**: Show "Only {N}/12 domains cached. Study at least 8 domains before attempting a mock exam. Missing: {list}. Use `/ai-tutor {domain}` to start studying."
- **Invalid args**: Show usage:
  ```
  Usage: /ai-tutor [domain]              — guided study path, SAA (default)
         /ai-tutor sap                  — guided study path, SAP-C02
         /ai-tutor sap practice-test    — SAP practice test (3 tests: 30q + 75q + 75q)
         /ai-tutor sap test-review <result-file> [--vi] — review a TD timed test (Vietnamese deep-dive with --vi)
         /ai-tutor sap review-set <N>   — TD set in review mode, blocks of 25 (TD1/TD2/TD5)
         /ai-tutor practice-test        — SAA practice test (6 tests, 65 Qs each)
         /ai-tutor free [domain] [mode] — free mode, any mode
         /ai-tutor keyword-drill        — keyword pattern drill
         /ai-tutor mock-exam            — full 65-question mock exam (SAA)
         /ai-tutor progress             — view dashboard
         /ai-tutor refresh <domain>     — refresh PDF cache
         /ai-tutor refresh cheat-sheet  — refresh cheat sheet cache
  Example: /ai-tutor compute
           /ai-tutor sap practice-test
           /ai-tutor sap chapter-drill security
           /ai-tutor sap chapter-drill storage dojo
           /ai-tutor sap test-review practice-exam/sap/TD_SAP_Timed_Set3_Full.md --vi
           /ai-tutor sap review-set 1
           /ai-tutor free storage mini-exam
           /ai-tutor practice-test
  ```
