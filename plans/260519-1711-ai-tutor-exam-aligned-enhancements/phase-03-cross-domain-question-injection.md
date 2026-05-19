---
phase: 3
title: Cross-Domain Question Injection
status: completed
priority: P1
effort: 30m
dependencies:
  - 1
---

# Phase 3: Cross-Domain Question Injection

## Overview

Modify mini-exam behavior for `scope=design` and `scope=comprehensive` to include 20-40% cross-domain questions spanning 2+ service domains. Uses cheat sheet cache for cross-cutting scenario context.

## Requirements

- Functional: cross-domain questions in design/comprehensive scopes, multi-topic tagging
- Non-functional: no change to concepts/scenarios scopes, backward compatible scoring

## Related Code Files

- Modify: `.claude/skills/ai-tutor/references/prompt-templates.md`
- Modify: `.claude/skills/ai-tutor/references/quiz-flow.md`

## Implementation Steps

### 1. Update mini-exam scope rules in `prompt-templates.md`

Replace the existing `scope=design` and `scope=comprehensive` rules:

**scope=design (replace):**
```markdown
- For `design`: Architecture decision scenarios + cross-domain integration.
  - 70% current domain questions (multi-service trade-offs within domain)
  - 30% cross-domain questions (current domain + 1-2 other domains)
  - Load cheat sheet cache for cross-cutting decision frameworks
  - Difficulty: 30% medium, 70% hard
  - Cross-domain questions MUST involve the current study domain as one component
  - Tag cross-domain questions with multiple topic slugs: `Topic: [primary-topic, secondary-domain:topic]`
```

**scope=comprehensive (replace):**
```markdown
- For `comprehensive`: Full domain exam with cross-domain integration.
  - 60% current domain questions (mix of all difficulty levels)
  - 40% cross-domain questions (current domain + 1-2 others)
  - Load cheat sheet cache for cross-cutting scenarios
  - Difficulty: 20% easy, 30% medium, 50% hard
  - Tag cross-domain questions with multiple topic slugs
```

### 2. Add cross-domain combination guide to `prompt-templates.md`

Add after the scope rules, before "### Instructions":

```markdown
### Cross-Domain Question Combinations (prioritize these pairings)

When generating cross-domain questions for design/comprehensive scopes, use these high-frequency pairings from real SAA-C03 exams:

| Current Domain | Cross With | Example Scenario |
|---------------|-----------|-----------------|
| storage | security-identity | S3 encryption (SSE-S3/KMS/C), bucket policy + VPC endpoints |
| storage | networking | CloudFront + S3 OAI, S3 gateway endpoint |
| databases | integration-messaging | SQS write buffer for DynamoDB, SNS + Lambda + RDS |
| databases | compute | ElastiCache + EC2 for session caching, Aurora + Lambda |
| compute | load-balancing-scaling | ALB + ASG + private subnet, NLB + static IP |
| compute | serverless | Lambda vs Fargate decision, API Gateway + Lambda |
| networking | security-identity | VPC endpoints + IAM policy, NACLs + WAF layering |
| load-balancing-scaling | compute | ECS dynamic port mapping + ALB, ASG + Spot |
| security-identity | monitoring-audit | GuardDuty findings → EventBridge → Lambda, CloudTrail + Config |
| data-analytics | storage | Athena + S3, Glue ETL + S3, EMR + S3 |

If the cross-domain involves a domain the user hasn't studied, use simpler factual questions about that domain (not deep architecture).
```

### 3. Update quiz-flow.md — multi-topic tag support

In the "## Scoring" section, update:

```markdown
2. List missed topics: extract topic tags from incorrect questions
   - For single-topic questions: add topic slug to missed list
   - For cross-domain questions (multiple topic tags): add ALL topic slugs to missed list
   - Format: `primary-topic` for same-domain, `domain:topic` for cross-domain
   Example: `[s3-security, networking:cloudfront]`
```

In the "## Session File Format" section, update the question header format:

```markdown
### Q{N} ✓/✗ — {Short title} ({topic-slug} | {topic-slug, cross-domain:topic-slug})
```

## Success Criteria

- [ ] `scope=design` mini-exam generates ~30% cross-domain questions
- [ ] `scope=comprehensive` mini-exam generates ~40% cross-domain questions
- [ ] `scope=concepts` and `scope=scenarios` unchanged (0% cross-domain)
- [ ] Cross-domain questions tagged with multiple topic slugs
- [ ] Missed cross-domain topics saved to study-progress correctly
- [ ] Cross-domain questions always involve the current study domain as one component

## Risk Assessment

| Risk | Mitigation |
|------|-----------|
| Cross-domain questions reference unstudied domains poorly | Rule: if cross-domain involves unstudied domain, use simpler factual questions |
| Scoring confusion with multi-topic tags | Clear format: `domain:topic` prefix for cross-domain topics |
