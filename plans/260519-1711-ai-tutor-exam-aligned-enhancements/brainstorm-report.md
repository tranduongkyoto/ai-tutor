# AI Tutor v2.1 — Exam-Aligned Enhancements

**Date:** 2026-05-19
**Status:** Approved for planning
**Context:** 3 practice exam analyses + AWS SAA Master Cheat Sheet (48 pages)

## Problem

Real exam score (37.5%) far below domain-specific mini-exam scores (80-90%).

Root causes from 3 exam analyses:
1. ~25% of real exam questions span 2+ service domains — tutor tests one domain at a time
2. Exam uses keyword triggers ("minimal effort" → managed, "decouple" → SQS) — no systematic drill
3. No full-length mock exam (real: 65 questions, 130 min, all domains)
4. 48-page cheat sheet with exam-focused decision frameworks unused as knowledge source
5. 7/12 domains unstudied (database, integration, serverless, analytics, DNS, monitoring, DR) account for ~34% of exam questions

## Design

### Phase 1 — Quick Wins (immediate exam prep value)

#### 1A. Cheat Sheet Integration

Register cheat sheet PDF as shared secondary knowledge source. Full extraction into cache.

**Changes:**
- `domains.md`: add `cheat-sheet-pdf: sections/AWS-SAA-Master-Cheat-Sheet.pdf`
- `pdf-extractor.md`: add cheat-sheet-specific extraction protocol (full 48 pages, organized by exam domain sections)
- `prompt-templates.md`: for `scope=design` and `scope=comprehensive`, load cheat sheet cache alongside domain cache
- Auto-generate: `cache/aws-csa-cheat-sheet.md` (~800-1200 lines, full content)

**Knowledge loading per mode:**
| Mode | Domain Cache | Cheat Sheet Cache |
|------|-------------|-------------------|
| concept-mapper | Yes | No |
| mini-exam (concepts/scenarios) | Yes | No |
| mini-exam (design/comprehensive) | Yes | Yes (full) |
| scenario-generator | Yes | Yes (relevant sections) |
| keyword-drill | No | Yes (full) |
| mock-exam | Sampled from all | Yes (full) |

#### 1B. Keyword Pattern Drill Mode

New mode: `keyword-drill` — quick-fire flash-card format. Present exam trigger phrases → user maps to correct service/pattern.

**Format:**
```
Pattern 3/25: "Company needs to decouple components, handle traffic spikes,
              messages must be processed at least once"
→ Your answer? [SQS Standard | SNS | Kinesis | EventBridge]
✓ Correct! SQS Standard — "decouple" + "at least once" = SQS Standard Queue
```

**New reference file:** `references/keyword-patterns.md` — ~80 curated trigger-word → service mappings from cheat sheet + 3 exam analyses. Organized by exam domain.

**Sample patterns:**
| Trigger | Answer | Exam Domain |
|---------|--------|-------------|
| "minimal operational effort/overhead" | Managed/serverless service | All |
| "static IP + high throughput" | NLB + Elastic IP | Resilient |
| "decouple writes to database" | SQS as write buffer | Resilient |
| "SMB + NFS file shares" | FSx for NetApp ONTAP | High-Performing |
| "RabbitMQ/ActiveMQ migration" | Amazon MQ | Resilient |
| "unpredictable OLTP workload" | Aurora Serverless | Cost-Optimized |
| "encryption with audit trail" | SSE-KMS | Secure |
| "restrict S3 to CloudFront only" | Origin Access Identity (OAI) | Secure |
| "key-value + flexible schema" | DynamoDB | High-Performing |
| "query S3 data without loading" | Athena | High-Performing |
| "serverless ETL" | AWS Glue | High-Performing |
| "multi-region VPC connectivity" | Direct Connect Gateway | Resilient |
| "UDP traffic load balancing" | NLB | High-Performing |
| "crypto mining detection" | GuardDuty | Secure |
| "cross-region failover DNS" | Route 53 failover routing | Resilient |

**Session config:** 25 patterns per session (configurable 10/25/all). Scoring + missed pattern tracking.
**No domain required** — cross-cutting by nature. Added to optional tools in SKILL.md.

#### 1C. Cross-Domain Question Injection

Modify mini-exam for `scope=design` and `scope=comprehensive`:

```
scope=design:
  70% current domain questions
  30% cross-domain questions (current domain + 1-2 others)
  Load cheat sheet cache for cross-cutting scenarios

scope=comprehensive:
  60% current domain questions
  40% cross-domain questions
  Tag with multiple topic slugs: topic: [s3-security, cloudfront]
```

Cross-domain combinations to prioritize (from exam analyses):
- S3 + CloudFront + security (OAI, signed URLs)
- SQS + DynamoDB (write buffering)
- ALB + EC2 + VPC (private subnet architecture)
- RDS + ElastiCache (read performance)
- Lambda + API Gateway + DynamoDB (serverless stack)
- Direct Connect + VPN (hybrid connectivity)
- CloudFront + S3 + WAF (content delivery security)
- ECS + ALB (dynamic port mapping)

### Phase 2 — Full Mock Exam (after more domains studied)

#### 2A. Mock Exam Mode

New `mock-exam` mode — 65 questions across ALL studied domains.

**SAA-C03 Exam Domain Weighting:**
| Exam Domain | Weight | ~Questions | Service Domains |
|-------------|--------|-----------|-----------------|
| 1: Secure | 30% | 20 | security-identity, networking (VPC/endpoints), storage (encryption) |
| 2: Resilient | 26% | 17 | compute, load-balancing, databases (HA), integration-messaging, DR |
| 3: High-Performing | 24% | 15 | databases (perf), storage (EBS/S3), data-analytics, networking (CDN/GA) |
| 4: Cost-Optimized | 20% | 13 | compute (purchasing), storage (lifecycle), databases (serverless), serverless |

**Prerequisite:** ≥8/12 domain caches must exist.

**Quiz flow:** Present in blocks of 5 questions (13 blocks). Show running score between blocks. Track elapsed time.

**Post-exam report:**
```
Mock Exam Results — 45/65 (69%)
Time: 112 min (target: 130 min)

By Exam Domain:
  Domain 1 (Secure):          14/20 (70%) ▲
  Domain 2 (Resilient):       12/17 (71%) ▲
  Domain 3 (High-Performing): 10/15 (67%) △
  Domain 4 (Cost-Optimized):   9/13 (69%) ▲

Weakest: data-analytics (0/3), elasticache (0/2)
Strongest: VPC/subnets (4/4), EC2 instances (3/3)
Verdict: BORDERLINE — need 47/65 (72%). Focus on Domain 3.
```

**New reference:** `references/mock-exam-flow.md` — batched 65-question protocol with timer + exam-domain analysis.

## File Change Summary

| File | Phase | Change Type |
|------|-------|-------------|
| `SKILL.md` | 1+2 | Modify — add keyword-drill + mock-exam modes, register cheat sheet |
| `certs/aws-csa/domains.md` | 1 | Modify — add cheat sheet PDF path |
| `references/prompt-templates.md` | 1+2 | Modify — add keyword-drill + mock-exam templates, cross-domain rules |
| `references/quiz-flow.md` | 1+2 | Modify — add keyword-drill flow, multi-topic tags, batched mock flow |
| `references/pdf-extractor.md` | 1 | Modify — add cheat sheet extraction protocol |
| `references/progress-tracking.md` | 1+2 | Modify — add keyword-drill + mock-exam tracking |
| `references/keyword-patterns.md` | 1 | **New** — ~80 trigger-word → service mappings |
| `references/mock-exam-flow.md` | 2 | **New** — 65-question batched exam protocol |
| `cache/aws-csa-cheat-sheet.md` | 1 | **Auto-generated** — full cheat sheet extraction |

## Constraints

- Backward compatible — all existing modes and progress data unchanged
- No changes to session file format or study-progress.md YAML schema (just new mode slugs)
- Cheat sheet cache extracted in full — no trimming
- Keyword patterns curated from real exam analyses, not invented

## Success Metrics

- Phase 1: keyword drill score >80% within 3 sessions; cross-domain mini-exam questions match real exam feel
- Phase 2: mock exam score ≥72% (pass threshold)
- Overall: real SAA-C03 exam pass (≥720/1000)
