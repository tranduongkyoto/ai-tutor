---
phase: 4
title: "Remaining Modes (Scenario + Weak Spot + Lab + Arch Review + Exam Strategy)"
status: pending
priority: P2
effort: "3h"
dependencies: [3]
---

# Phase 4: Remaining Modes

## Overview

Implement the remaining 5 tutor modes: Scenario Generator, Weak Spot Analyzer, Hands-On Lab Creator, Architecture Reviewer, and Exam Strategy Coach. All follow the same pattern: read context → generate content → display → save.

## Requirements

- Functional: Each mode generates domain-specific study content. Weak Spot Analyzer and Exam Strategy Coach use progress data instead of domain cache.
- Non-functional: All modes must save session artifacts. Architecture Reviewer requires user input (describe their architecture).

## Related Code Files

- Modify: `.claude/skills/ai-tutor/references/prompt-templates.md` (add 5 mode templates)
- Modify: `.claude/skills/ai-tutor/SKILL.md` (add mode routing for 5 modes)

## Implementation Steps

### 1. Scenario Generator template

Add to `prompt-templates.md`:
- Input: domain + cached content
- Generate 5 realistic exam scenarios with:
  - Business context (company situation, requirements)
  - Technical requirements (constraints, scale, budget)
  - 5 options (A-E) with detailed explanations
  - Why correct answer is best, why others fall short
- Output: formatted scenarios with explanations
- Save to: `{YYMMDD}-{HHMM}-{domain}-scenario-generator.md`

### 2. Weak Spot Analyzer template

Add to `prompt-templates.md`:
- Input: `study-progress.md` (all domains, not just one)
- No domain-specific cache needed — analyzes cross-domain progress
- Generate:
  - Prioritized list of weak areas (from exam scores + missed topics)
  - Targeted study plan per weak area
  - Estimated time per area
  - Specific topics to focus on with suggested mode
- AskUserQuestion for domain selection NOT needed (analyzes all)
- Save to: `{YYMMDD}-{HHMM}-weak-spot-analysis.md`

### 3. Hands-On Lab Creator template

Add to `prompt-templates.md`:
- Input: domain + cached content
- Generate progressive lab exercise:
  - **Level 1 (Basic)**: Single-service setup with step-by-step
  - **Level 2 (Intermediate)**: Multi-service integration
  - **Level 3 (Enterprise)**: Production-grade with HA, security, monitoring
  - **Troubleshooting scenarios**: Common issues and how to diagnose
  - **Cleanup procedures**: How to tear down all resources
- Include AWS CLI commands and Console instructions
- Save to: `{YYMMDD}-{HHMM}-{domain}-hands-on-lab.md`

### 4. Architecture Reviewer template

Add to `prompt-templates.md`:
- Input: domain + cached content + **user-provided architecture description**
- Flow: AskUserQuestion "Describe your architecture (services, data flow, scale)" → user types description via Other
- Evaluate against AWS Well-Architected Framework 6 pillars:
  - Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability
- Identify: single points of failure, scaling bottlenecks, cost waste, security gaps
- Provide: specific improvement recommendations with AWS service suggestions
- Save to: `{YYMMDD}-{HHMM}-{domain}-arch-review.md`

### 5. Exam Strategy Coach template

Add to `prompt-templates.md`:
- Input: `study-progress.md` + user's exam timeline (AskUserQuestion: "When is your exam?" with options like "This week", "2 weeks", "1 month", "Not scheduled")
- Generate:
  - Study schedule based on remaining time and current readiness
  - Exam day strategy (time management, question approach)
  - Common SAA-C03 traps and how to avoid them
  - Domain prioritization based on readiness scores
  - Last-minute focus areas
  - Confidence assessment based on current scores
- Save to: `{YYMMDD}-{HHMM}-exam-strategy.md`

### 6. Add mode routing to SKILL.md

Extend Step 3 mode execution with all 5 new modes. Each follows:
```
Load prompt template → Read required inputs → Generate → Display → Save
```

Special routing:
- `weak-spot-analyzer`: Skip domain selection, read all progress data
- `exam-strategy`: Skip domain selection, ask exam timeline
- `architecture-reviewer`: Ask for architecture description input

### 7. Test each mode

- Scenario Generator: verify 5 scenarios with proper structure
- Weak Spot Analyzer: verify it analyzes progress data (needs some exam history)
- Hands-On Lab: verify progressive exercise structure
- Architecture Reviewer: verify it prompts for input and evaluates
- Exam Strategy: verify timeline-aware recommendations

## Success Criteria

- [ ] All 5 mode templates written in prompt-templates.md
- [ ] SKILL.md routes to all 6 modes correctly
- [ ] Scenario Generator produces 5 scenarios with 5 options each
- [ ] Weak Spot Analyzer reads progress data and prioritizes weak areas
- [ ] Hands-On Lab has 3 progressive levels + cleanup
- [ ] Architecture Reviewer prompts for user input and evaluates against Well-Architected
- [ ] Exam Strategy Coach adapts to user's exam timeline
- [ ] All modes save session artifacts with correct naming

## Risk Assessment

- **Prompt template file size**: With 6 modes, `prompt-templates.md` may grow large (400+ lines). Acceptable — it's a reference file, not code.
- **Architecture Reviewer user input**: Free-text via AskUserQuestion "Other" may be limited. If too short, add follow-up questions.
