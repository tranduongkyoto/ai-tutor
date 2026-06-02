---
phase: 1
title: Implement Fix A+B+C
status: completed
priority: P1
effort: 1h
dependencies: []
---

# Phase 1: Implement Fix A+B+C

## Overview

Close P3/P4 asymmetry with three changes: (A) gate cross-domain questions on studied domains, (B) ground all questions in loaded cache content, (C) add cross-domain topic mapping + cheat sheet to P1 so patterns are taught before tested.

## Principle

**Everything testable in P3/P4 must have been teachable in P1/P2.**

## Validated Decisions

- **Filtering:** Explicit cross-domain topic mapping in `scenario-map.md` (not LLM filtering of whole cheat sheet)
- **Studied threshold:** `current_phase >= 2` (completed P1) — no minimum score required
- **Context loading:** Load all paired domain caches for mini-exam cross-domain (no cap)

## Related Code Files

- Modify: `.claude/skills/ai-tutor/certs/aws-csa/scenario-map.md` — add `cross-domain-topics` per domain
- Modify: `.claude/skills/ai-tutor/references/prompt-templates.md` — P1 cheat sheet usage, P3/P4 gating + grounding rules
- Modify: `.claude/skills/ai-tutor/SKILL.md` — P1 cheat sheet loading, mini-exam cross-domain cache loading

## Implementation Steps

### Step 1: Add cross-domain topic mappings to `scenario-map.md`

After each domain's existing scenario entries, add a `### cross-domain-topics` section. Each entry maps: source domain → topics → cheat sheet section reference.

Priority: start with domains that have known gaps from the serverless P3 analysis. Cover all 12 domains.

**Example for serverless:**
```markdown
### cross-domain-topics
- from: integration-messaging
  topics: [sqs-write-buffer-pattern, sqs-lambda-async-decoupling, sns-fan-out-to-lambda]
  cheat-sheet-ref: "§2.1 Services for Loose Coupling, §Quick Ref: Messaging"
- from: dns
  topics: [route53-latency-routing, multi-region-serverless-deployment]
  cheat-sheet-ref: "§3.4 Network Topologies for Global Architectures"
- from: security-identity
  topics: [kms-lambda-encryption, cognito-api-gateway-auth]
  cheat-sheet-ref: "§1.2 Key Security Services, §1.3 Encrypting Data at Rest"
- from: monitoring-audit
  topics: [cloudwatch-lambda-metrics, xray-distributed-tracing]
  cheat-sheet-ref: "§2.2 Automation Strategies"
```

**For all 12 domains:** Use the Cross-Domain Question Combinations table from `prompt-templates.md` as the starting point. Add 2-5 cross-domain entries per domain based on known SAA-C03 exam pairings.

### Step 2: Add cheat sheet to P1 (learn-and-test) in `SKILL.md`

**2a.** In `## Step 2: Load Context`, item 3, update the `learn-and-test` bullet:

Current:
```
- **learn-and-test** also needs: `references/quiz-flow.md` (hint flow protocol)
```

Change to:
```
- **learn-and-test** also needs: `references/quiz-flow.md` (hint flow protocol) + cheat-sheet cache (see item 4) + cross-domain topics from `certs/aws-csa/scenario-map.md` (the `### cross-domain-topics` section for this domain)
```

**2b.** In item 4, add `learn-and-test` to the modes list:

Current:
```
- **Modes that use cheat sheet**: mini-exam (design/comprehensive/general), scenario-practice, scenario-generator, keyword-drill, mock-exam
```

Change to:
```
- **Modes that use cheat sheet**: learn-and-test, mini-exam (design/comprehensive/general), scenario-practice, scenario-generator, keyword-drill, mock-exam
```

### Step 3: Update P1 prompt template in `prompt-templates.md`

**3a.** In `## Mode: Learn and Test` → `### Input`, add:
```
- Cheat sheet cache (supplementary): `.claude/skills/ai-tutor/cache/aws-csa-cheat-sheet.md`
- Cross-domain topics: from `certs/aws-csa/scenario-map.md` → `### cross-domain-topics` section for this domain
  - Only reference cheat sheet sections listed in the mapping
```

**3b.** In `### Quality Rules` (currently 4 rules), add rule 5:
```
- Supplement domain cache with cross-domain topics from scenario-map.md.
  For each mapped topic, reference the specified cheat sheet section to enrich
  the relevant P1 section (typically §4 Architectural Patterns or §7 Exam Tips).
  Only include cross-domain content where this domain is a primary component.
```

### Step 4: Add Cross-Domain Gating Rule to `prompt-templates.md`

Insert after the "Cross-Domain Question Combinations" table and before `### Instructions` in the Mini Exam section:

```markdown
### Cross-Domain Gating Rule

Before generating cross-domain questions for `design` or `comprehensive` scopes:

1. Read `aws-csa/study-progress.md`
2. Build a list of **studied domains** = domains where `current_phase >= 2` (completed at least P1)
3. Cross-domain questions may ONLY reference domains in the studied list
4. Scale cross-domain percentage based on studied domain count:
   - 0-2 studied domains → 0% cross-domain (all questions from current domain only)
   - 3-5 studied domains → 15% cross-domain
   - 6+ studied domains → use normal scope percentage (30% design, 40% comprehensive)
5. Tag each cross-domain question: `Requires: [domain1, domain2]` — both must be in studied list
6. If a pairing from the Cross-Domain Question Combinations table involves an unstudied domain, skip that pairing entirely
7. Cross-domain topics must match entries in `scenario-map.md` → `### cross-domain-topics` for the current domain
```

### Step 5: Add Content Grounding Rule to `prompt-templates.md`

In Mini Exam "Question Quality Rules" (rules 1-8), add rule #9:

```markdown
9. **Content grounding:** Every question (including cross-domain) must be answerable
   from the loaded caches only. For current domain: use domain cache + cheat sheet.
   For cross-domain: also load the paired domain's cache file
   (`cache/aws-csa-{paired-domain}.md`) and verify the tested concept appears in it.
   If a concept exists in NO loaded cache, do NOT generate a question about it.
```

### Step 6: Add mini-exam cross-domain cache loading to `SKILL.md`

In `## Step 2: Load Context`, item 3, after existing cache logic, add:

```markdown
   - **Mini-exam cross-domain cache loading** (design/comprehensive scopes only):
     After loading the current domain cache, read `aws-csa/study-progress.md` to identify
     studied domains (current_phase >= 2). Read `certs/aws-csa/scenario-map.md` →
     `### cross-domain-topics` for the current domain. For each mapped domain that is
     in the studied list, also load `cache/aws-csa-{paired-domain}.md`.
     These caches provide content grounding for cross-domain questions.
     Do NOT load caches for unstudied domains.
```

### Step 7: Update Self-Verify Step in `prompt-templates.md`

In the existing "Self-Verify Step", add:

```markdown
- Does every cross-domain question reference only studied domains (per Gating Rule)?
- Is every tested concept present in at least one loaded cache file?
- Does every cross-domain topic match an entry in scenario-map.md cross-domain-topics?
```

## Success Criteria

- [ ] `scenario-map.md` has `### cross-domain-topics` for all 12 domains
- [ ] `SKILL.md` Step 2 adds cheat sheet + cross-domain topics loading for learn-and-test
- [ ] `SKILL.md` Step 2 adds cross-domain cache loading for mini-exam design/comprehensive
- [ ] `prompt-templates.md` P1 Input includes cheat sheet + cross-domain mapping
- [ ] `prompt-templates.md` P1 Quality Rules reference cross-domain topics from scenario-map
- [ ] `prompt-templates.md` contains "Cross-Domain Gating Rule" with studied-domain check
- [ ] `prompt-templates.md` Question Quality Rule #9 enforces cache grounding
- [ ] `prompt-templates.md` Self-Verify includes 3 new verification bullets
- [ ] No existing rules/sections broken by additions

## Risk Assessment

- **Low risk**: All changes additive — new sections/rules, no removals
- **Mapping maintenance**: New cross-domain-topics entries needed when gaps discovered. Mitigated: gap analysis reports identify exactly what's missing.
- **P1 length increase**: Cheat sheet content filtered through explicit mapping, so only mapped topics added (not entire cheat sheet dump)
- **Edge case**: Free-mode `scope=general` unaffected by gating rule (design/comprehensive only)
- **Edge case**: A mapped topic exists in scenario-map but its source domain has no cache → skip that topic (cache miss = can't ground)
