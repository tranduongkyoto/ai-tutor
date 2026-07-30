# AI Tutor — AWS Certification Study Skill

Interactive study companion for AWS SAA-C03 certification. Uses 31 PDF course sections (849 pages) as knowledge source.

## Usage

```
/ai-tutor                                    # Interactive menu
/ai-tutor aws-csa compute concept-mapper     # Direct mode
/ai-tutor practice-test                      # Udemy practice test
/ai-tutor progress                           # View dashboard
/ai-tutor refresh compute                    # Re-extract PDF cache
```

## 7 Study Modes + Practice Tests

| Mode | What It Does |
|------|-------------|
| **concept-mapper** | Synthesizes domain knowledge: services, integrations, patterns, exam tips |
| **mini-exam** | Interactive quiz (5/10/15 questions) with scoring and per-question feedback |
| **scenario-generator** | 5 realistic exam scenarios with detailed explanations |
| **weak-spot-analyzer** | Analyzes progress across all domains, prioritizes weak areas |
| **hands-on-lab** | Progressive lab exercises (basic → enterprise) with CLI commands |
| **architecture-reviewer** | Evaluates your architecture against Well-Architected Framework |
| **exam-strategy** | Personalized study plan and exam day strategy |
| **practice-test** | Udemy practice tests (6 tests × 65 Qs) with answer tracking, domain filter, redo wrong, weakness report |

## 12 Domains

compute, storage, databases, networking, security-identity, load-balancing-scaling, dns, integration-messaging, serverless, monitoring-audit, data-analytics, dr-architecture

## How It Works

1. First run on a domain extracts PDF content via Haiku subagent → cached for future use
2. Study modes use cached content to generate domain-specific material
3. Mini-exam tracks scores and missed topics in `aws-csa/study-progress.md`
4. Readiness score computed dynamically: coverage (30%) + exam scores (50%) + recency (20%)

## File Structure

```
.claude/skills/ai-tutor/
├── SKILL.md              # Orchestrator
├── references/           # Prompt templates, quiz flow, tracking protocol
├── cache/                # Auto-generated PDF extracts (one per domain)
└── certs/aws-csa/        # Domain configuration

aws-csa/
├── study-progress.md     # Progress tracker (YAML + session log)
└── study-sessions/       # Session output files
```
