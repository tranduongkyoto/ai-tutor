---
phase: 3
title: "Core Modes (Concept Mapper + Mini Exam)"
status: pending
priority: P1
effort: "3h"
dependencies: [2]
---

# Phase 3: Core Modes (Concept Mapper + Mini Exam)

## Overview

Implement the first two tutor modes: Concept Mapper (knowledge synthesis) and Mini Exam (interactive quiz with scoring). These are the core study experiences — one for learning, one for testing.

## Requirements

- Functional: Concept Mapper generates structured knowledge maps. Mini Exam presents interactive 5-option questions via AskUserQuestion with scoring.
- Non-functional: Questions must be unambiguous and grounded in PDF content. Self-verify step before presenting questions.

## Architecture

### Concept Mapper Flow
```
Read cache → Read prompt template → Generate concept map with:
  - Real-world use cases per service
  - Service integrations and architectural patterns
  - Cost implications
  - Security considerations
→ Display in terminal → Save to study-sessions/
```

### Mini Exam Flow
```
AskUserQuestion("How many questions?") → 5/10/15
Read cache + domains.md topics + study-progress.md weak topics
Generate N questions (5 options A-E each)
Self-verify: "Review each question. Is correct answer unambiguous? Fix issues."
Present in rounds (2 questions per AskUserQuestion call):
  - Display question + 5 options as terminal text
  - AskUserQuestion with options: A, B, C, D (user types E via Other)
Score → per-question feedback → save results
```

## Related Code Files

- Modify: `.claude/skills/ai-tutor/references/prompt-templates.md` (add concept-mapper + mini-exam templates)
- Modify: `.claude/skills/ai-tutor/references/quiz-flow.md` (fill quiz protocol)
- Modify: `.claude/skills/ai-tutor/SKILL.md` (add mode execution in Step 3)

## Implementation Steps

### 1. Write Concept Mapper prompt template

In `prompt-templates.md`, add the concept-mapper section:

```markdown
## Mode: Concept Mapper

### Input
- Domain: {domain}
- Cached content: (loaded from cache file)

### Instructions
Generate a comprehensive concept map for the {domain} domain covering:

1. **Service Overview**: Each service with 1-2 sentence description
2. **Real-World Use Cases**: Practical scenarios for each service
3. **Service Integrations**: How services connect (e.g., EC2 + EBS + ELB)
4. **Architectural Patterns**: Common architectures (e.g., 3-tier web app)
5. **Cost Implications**: Pricing models, cost optimization tips
6. **Security Considerations**: IAM, encryption, network security per service
7. **Exam Tips**: Key distinctions tested in SAA-C03

### Output Format
Use headers, bullet points, and tables. Keep concise but comprehensive.
```

### 2. Write Mini Exam prompt template

In `prompt-templates.md`, add the mini-exam section:

```markdown
## Mode: Mini Exam

### Input
- Domain: {domain}
- Question count: {count} (5/10/15)
- Cached content: (loaded from cache file)
- Topic checklist: (from domains.md)
- Weak topics: (from study-progress.md, prioritize these)

### Instructions
Generate {count} exam-style questions following these rules:

**Question Quality Rules:**
1. Each question MUST have exactly 5 options (A-E)
2. Exactly ONE correct answer per question
3. Wrong options must be plausible but clearly incorrect given AWS docs
4. Questions must be grounded in the cached PDF content
5. Cover diverse topics from the checklist; prioritize weak topics
6. Include scenario-based questions (60%) and fact-based questions (40%)
7. Vary difficulty: 30% easy, 50% medium, 20% hard

**Self-Verify Step:**
After generating all questions, review each one:
- Is the correct answer unambiguously correct?
- Are distractors plausible but definitively wrong?
- Does the question test real AWS knowledge (not trivia)?
Fix any issues before presenting.

### Output Format (per question)
Question N: [scenario or question text]
A) [option]
B) [option]
C) [option]
D) [option]
E) [option]
Correct: [letter]
Explanation: [why correct + why each wrong option is wrong]
```

### 3. Write quiz-flow.md protocol

Fill `references/quiz-flow.md` with the interactive quiz protocol:

```markdown
# Quiz Flow Protocol

## Setup
1. AskUserQuestion: "How many questions?" with options: "5", "10", "15"
2. Read inputs: cache file, domains.md topics, study-progress.md weak topics
3. Generate questions using mini-exam prompt template
4. Run self-verify step

## Presentation (2 questions per round)
For each pair of questions:
1. Display both questions with all 5 options as formatted terminal text
2. For question 1: AskUserQuestion with options A, B, C, D
   - User selects A-D directly, or "Other" to type E
3. For question 2: Same AskUserQuestion pattern
4. After each round: show immediate feedback (correct/wrong + explanation)

## Scoring
After all rounds:
1. Display score: X/{total} ({percentage}%)
2. Show per-question breakdown: question summary, user answer, correct answer
3. List missed topics (extract topic tags from missed questions)
4. Return score data for progress tracking (Phase 5)

## Edge Cases
- Odd number of questions: last round has 1 question
- User selects "Other" and types invalid input: treat as wrong, show correct answer
```

### 4. Add mode execution logic to SKILL.md

In SKILL.md Step 3 (Execute mode), add routing:

```
IF mode == "concept-mapper":
  Load: references/prompt-templates.md (concept-mapper section)
  Read: cache/aws-csa-{domain}.md
  Generate concept map content
  Display in terminal
  Save to aws-csa/study-sessions/{YYMMDD}-{HHMM}-{domain}-concept-mapper.md

IF mode == "mini-exam":
  Load: references/quiz-flow.md
  Load: references/prompt-templates.md (mini-exam section)
  Execute quiz flow protocol
  Save results to aws-csa/study-sessions/{YYMMDD}-{HHMM}-{domain}-exam.md
```

### 5. Test both modes

- Run `/ai-tutor aws-csa compute concept-mapper` → verify structured output + saved file
- Run `/ai-tutor aws-csa compute mini-exam` → verify interactive quiz + scoring + saved file

## Success Criteria

- [ ] Concept Mapper generates structured domain knowledge with all 7 sections
- [ ] Mini Exam generates questions with exactly 5 options each
- [ ] Self-verify step catches and fixes ambiguous questions
- [ ] AskUserQuestion correctly presents A/B/C/D options with E via Other
- [ ] Scoring calculates correctly and shows per-question feedback
- [ ] Session files saved to `aws-csa/study-sessions/` with correct naming
- [ ] Weak topics from progress are prioritized in question generation

## Risk Assessment

- **AskUserQuestion option E via Other**: User experience slightly clunky. Mitigation: most AWS questions use 4 options, E is rare. Display clear instruction "Type E for option E".
- **Self-verify adds latency**: ~5s per question set. Worth it for quality.
- **Question quality**: Prompt guardrails are critical. If quality is poor, add explicit examples of good/bad questions to the prompt template.
