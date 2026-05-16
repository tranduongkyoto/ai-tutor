# Prompt Templates

Mode-specific prompt templates for the AI Tutor skill. Each section defines the inputs, instructions, and output format for one study mode.

## Global Rule: Full Service Names (ALL modes)

**ALWAYS use full service/concept names on first mention, with abbreviation in parentheses.** After first mention, abbreviation alone is acceptable within the same section.

Examples:
- "Elastic Compute Cloud (EC2)" not just "EC2"
- "Elastic Block Store (EBS)" not just "EBS"
- "Application Load Balancer (ALB)" not just "ALB"
- "Virtual Private Cloud (VPC)" not just "VPC"
- "Identity and Access Management (IAM)" not just "IAM"
- "Simple Storage Service (S3)" not just "S3"
- "Relational Database Service (RDS)" not just "RDS"
- "Elastic Network Interface (ENI)" not just "ENI"
- "Auto Scaling Group (ASG)" not just "ASG"
- "Content Delivery Network (CDN)" / "CloudFront" not just "CF"
- "Key Management Service (KMS)" not just "KMS"
- "Simple Queue Service (SQS)" not just "SQS"
- "Simple Notification Service (SNS)" not just "SNS"
- "Availability Zone (AZ)" not just "AZ"
- "Network Access Control List (NACL)" not just "NACL"
- "Security Group (SG)" not just "SG"
- "Elastic File System (EFS)" not just "EFS"
- "Network Address Translation (NAT)" not just "NAT"

This applies to: concept maps, exam questions, scenario descriptions, lab instructions, architecture reviews, and all other generated content. The target audience is new AWS users preparing for their first certification.

---

## Mode: Concept Mapper

### Input
- Domain: `{domain}` (e.g., "compute")
- Cached content: loaded from `cache/aws-csa-{domain}.md`

### Instructions

Generate a comprehensive concept map for the **{domain}** domain covering:

1. **Service Overview**: Each service with 1-2 sentence description and primary use case
2. **Real-World Use Cases**: Practical scenarios — "Company X needs Y, use Z because..."
3. **Service Integrations**: How services connect (e.g., EC2 + EBS + ELB + ASG). Show relationships.
4. **Architectural Patterns**: Common architectures (e.g., 3-tier web app, microservices). Include when to use each.
5. **Cost Implications**: Pricing models per service, cost optimization tips, reserved vs on-demand decisions
6. **Security Considerations**: IAM, encryption at rest/transit, network security per service
7. **Exam Tips**: Key distinctions tested in SAA-C03, keywords that signal specific answers

### Diagram Directives

Generate **3-5 diagrams** across the concept map. Place them in the sections below — skip a diagram if the section has no visual value for the domain.

| Section | Diagram Type | Format | Guidance |
|---------|-------------|--------|----------|
| §3 Service Integrations | Service relationship flowchart | Mermaid `graph LR` | Nodes = domain services, edges = data/traffic flow direction. Show how services chain together. |
| §4 Architectural Patterns | Architecture diagram (top 2 patterns) | Mermaid `graph TD` | Layered layout: Internet → public tier → private tier → data tier. One diagram per major pattern. |
| §4 (sub) | Decision tree for pattern selection | Mermaid `graph TD` with diamond decisions | "When to use which pattern?" — branch on requirements (HA? cost? latency?) to recommended pattern. |
| §6 Security | Defense-in-depth layers | ASCII art | Stack diagram showing outer → inner layers: perimeter (NACL) → instance (SG) → service (IAM) → data (encryption). |
| §7 Exam Tips | Keyword-to-answer decision tree | Mermaid `graph TD` | Map exam trigger words (e.g., "block IP", "private S3 access") to correct service/answer via branching. |

**Diagram quality rules:**
- Mermaid: use `graph TD` or `graph LR` only — no sequence, pie, gantt, or other types
- Max 15 nodes per diagram; split into multiple diagrams if larger
- Include a 3-5 line ASCII text fallback below each Mermaid block for terminal users
- Node labels: full service name on first occurrence, abbreviation OK after
- Decision trees: condition/question at top, branches as choices, leaf = answer/recommendation

### Output Format
- Use headers (`##`, `###`) for sections
- Bullet points for details — concise, not paragraphs
- Tables for comparisons (e.g., instance type families, storage tier comparison)
- Bold key terms and service names
- Mermaid code blocks (` ```mermaid `) for architecture and decision diagrams
- ASCII blocks for terminal-friendly diagram fallbacks
- End with a "Key Takeaways" section (5-7 bullet points)

### Quality Rules
- Ground ALL content in the cached PDF material
- Include specific numbers (limits, SLAs, quotas) — not vague language
- Focus on exam-relevant details, not general AWS marketing
- Cover ALL topics from the domain's topic checklist

---

## Mode: Mini Exam

### Input
- Domain: `{domain}`
- Question count: `{count}` (5, 10, or 15)
- Scope: `{scope}` — one of: `concepts`, `scenarios`, `hands-on`, `comprehensive`, `general`
- Cached content: loaded from `cache/aws-csa-{domain}.md`
- Topic checklist: from `certs/aws-csa/domains.md`
- Weak topics: from `aws-csa/study-progress.md` (prioritize these)

### Scope Rules

| Scope | Focus | When Used |
|-------|-------|-----------|
| `concepts` | Test conceptual knowledge — service features, limits, comparisons | Guided Phase 2 (after concept-mapper) |
| `scenarios` | Test scenario reasoning — "Company X needs Y, which service?" | Guided Phase 4 (after scenario-generator) |
| `design` | Test architecture design decisions — multi-service trade-offs, Well-Architected reasoning | Guided Phase 5 (architecture design) |
| `comprehensive` | Full domain exam — mix of all scopes, harder difficulty | Guided Phase 6 (final exam) |
| `general` | Balanced mix (default) | Free mode |

- For `concepts`: 70% fact-based, 30% scenario-based. Focus on "what is", "which service", "what's the limit"
- For `scenarios`: 80% scenario-based, 20% fact-based. Focus on architecture decisions, trade-offs
- For `design`: 80% architecture decision scenarios, 20% best-practice recall. Focus on multi-service integration, Well-Architected trade-offs, service selection for complex requirements, cost vs performance vs availability decisions. Difficulty: 30% medium, 70% hard. Questions should present realistic business scenarios requiring architectural judgment — not single-service trivia.
- For `comprehensive`: 40% scenario, 30% fact, 30% practical. Difficulty: 20% easy, 40% medium, 40% hard
- For `general`: default mix (60% scenario, 40% fact). Difficulty: 30% easy, 50% medium, 20% hard

### Instructions

Generate `{count}` exam-style questions following these rules (adjusted by scope above):

**Question Types (match real SAA-C03 exam):**
- ~80% **single-select**: 4 options (A-D), pick 1 correct
- ~20% **multi-select**: 4 options (A-D), pick 2 correct. Question states "(Select TWO)"
- For 10 questions: ~8 single + ~2 multi. For 5 questions: ~4 single + ~1 multi.

**Question Quality Rules:**
1. Each question MUST have exactly 4 options (A-D) — matches real SAA-C03 exam format
2. Single-select: exactly ONE correct answer. Multi-select: exactly TWO correct answers
3. Wrong options must be plausible but clearly incorrect given AWS documentation
4. Questions must be grounded in the cached PDF content — do not invent facts
5. Cover diverse topics from the checklist; prioritize weak topics (at least 30% of questions)
6. Include scenario-based questions (60%) and fact-based questions (40%)
7. Vary difficulty: 30% easy, 50% medium, 20% hard
8. Tag each question with a topic slug from the domain's topic list

**Self-Verify Step:**
After generating all questions, review each one:
- Is the correct answer unambiguously correct based on the cached content?
- Are distractors plausible but definitively wrong?
- Does the question test real AWS knowledge (not trivia or trick wording)?
- Is the topic tag accurate?
Fix any issues before presenting to the user.

### Output Format (internal — before presenting via quiz flow)

For each question, prepare:
```
Question {N}: [scenario or question text]
Type: single | multi
A) [option]
B) [option]
C) [option]
D) [option]
Correct: [letter] (single) or [letter, letter] (multi)
Topic: [topic-slug]
Explanation: [Why correct answer(s) are right. For each wrong option: why it's wrong — 1 sentence each.]
```

Then present questions interactively using the protocol in `references/quiz-flow.md`.

---

## Mode: Scenario Generator

### Input
- Domain: `{domain}`
- Cached content: loaded from `cache/aws-csa-{domain}.md`
- Scenario map: loaded from `certs/aws-csa/scenario-map.md` — the `{domain}` section

### Instructions

Read the scenario map for the **{domain}** domain. Generate one scenario per array item in the map. Each scenario should simulate a real SAA-C03 exam question at medium-to-hard difficulty.

The scenario map defines exactly which sub-concepts need coverage. Each array item (e.g., `families-and-sizing`) becomes one scenario. Tag each scenario with its map entry.

**Per scenario:**
1. **Business Context**: Company situation, industry, scale (e.g., "A fintech startup processing 10K transactions/second...")
2. **Technical Requirements**: Specific constraints — latency, availability, budget, compliance, scale
3. **Question**: What should the solutions architect recommend?
4. **Options (A-D)**: 4 options, each a valid-sounding architecture but only one best answer
5. **Correct Answer**: Letter + detailed explanation
6. **Architecture Diagram**: Mermaid `graph TD` showing the correct answer's architecture — services as nodes, connections as edges. Include 3-5 line ASCII fallback. Max 10 nodes. Show ONLY the recommended solution (not all options).
7. **Why Others Are Wrong**: 1-2 sentences per wrong option explaining the specific flaw
8. **Key Concept**: The AWS concept being tested

### Output Format

```
### Scenario {N}: {Short Title}

**Context:** {business context}

**Requirements:** {technical requirements}

**Question:** Which solution meets these requirements?

A) {option}
B) {option}
C) {option}
D) {option}

**Answer: {letter}**
{Detailed explanation}

**Architecture:**
```mermaid
graph TD
    {recommended architecture — services as nodes, connections as edges}
```
ASCII: {3-5 line text description of the architecture flow}

**Why others are wrong:**
- A) {reason}
- B) {reason}
...

**Key Concept:** {concept being tested}
```

---

---

## Mode: Weak Spot Analyzer

### Input
- Progress data: `aws-csa/study-progress.md` (ALL domains, not domain-specific)
- No cache file needed

### Instructions

Analyze the user's study progress across all 12 domains and identify weak areas.

**Analysis steps:**
1. Parse YAML frontmatter for each domain's data
2. Identify weak spots from:
   - Domains with low/no exam scores
   - Topics appearing in `missed_topics` across multiple exams
   - Domains with low mode coverage (few modes completed)
   - Domains not studied recently (>7 days)
   - Domains never started
3. Prioritize by impact on exam readiness

**Generate:**
1. **Priority Weak Areas** (ranked list):
   - Topic/domain name
   - Why it's weak (low scores, missed repeatedly, not covered)
   - Specific sub-topics to focus on
2. **Targeted Study Plan**:
   - Per weak area: recommended mode + estimated time
   - Ordered by priority (highest impact first)
3. **Quick Wins**: Topics that need minimal study to move from "almost there" to mastered
4. **Estimated Time to Exam-Ready**: Based on current readiness and weak area count

### Output Format
- Use priority indicators: `[CRITICAL]`, `[HIGH]`, `[MEDIUM]`, `[LOW]`
- Table for domain overview
- Bulleted action items per weak area
- End with "Recommended Next Session" — specific domain + mode

### Edge Case
If no exam data exists yet: output "No exam data yet. Start with mini-exams across your weakest domains to build a progress baseline. Suggested starting order: {list 3 foundational domains: compute, networking, security-identity}."

---

## Mode: Hands-On Lab

### Input
- Domain: `{domain}`
- Cached content: loaded from `cache/aws-csa-{domain}.md`

### Instructions

Generate a progressive hands-on lab exercise for the **{domain}** domain. The lab should teach through doing — building real AWS infrastructure.

**Structure:**
1. **Lab Overview**: What you'll build, estimated time, prerequisites
2. **Level 1 — Basic** (~15 min): Single-service setup with step-by-step instructions
   - AWS Console steps AND equivalent AWS CLI commands
   - Expected output/result at each step
3. **Level 2 — Intermediate** (~30 min): Multi-service integration
   - Build on Level 1 infrastructure
   - Add monitoring, security, or HA components
4. **Level 3 — Enterprise** (~45 min): Production-grade architecture
   - HA, fault tolerance, security hardening, monitoring
   - Cost optimization considerations
5. **Troubleshooting Scenarios**: 3 common issues with symptoms, diagnosis steps, and fixes
6. **Cleanup Procedures**: Step-by-step resource teardown to avoid charges
   - Both Console and CLI cleanup commands
   - Verification that all resources are deleted

### Output Format
- Numbered steps with clear action verbs ("Create", "Configure", "Verify")
- Code blocks for CLI commands with comments
- `> Note:` callouts for important warnings (cost, security)
- Checkpoints: "At this point, you should see..." verification steps

---

## Mode: Architecture Reviewer

### Input
- Domain: `{domain}`
- Cached content: loaded from `cache/aws-csa-{domain}.md`
- User architecture: collected via `AskUserQuestion` — "Describe your architecture (services used, data flow, expected scale, any concerns):"

### Instructions

Evaluate the user's described architecture against the AWS Well-Architected Framework 6 pillars.

**Analysis per pillar:**
1. **Operational Excellence**: Monitoring, automation, incident response
2. **Security**: IAM, encryption, network isolation, data protection
3. **Reliability**: Multi-AZ, fault tolerance, backup/recovery, auto-scaling
4. **Performance Efficiency**: Right-sizing, caching, CDN, async processing
5. **Cost Optimization**: Reserved capacity, right-sizing, lifecycle policies, spot usage
6. **Sustainability**: Resource efficiency, managed services, data lifecycle

**For each pillar, provide:**
- Current assessment: what's good, what's missing
- Specific risks identified
- Actionable improvement with AWS service recommendation

**Also identify:**
- Single points of failure (SPOF)
- Scaling bottlenecks
- Cost waste opportunities
- Security gaps

### Output Format

```
## Architecture Review: {brief description}

### Summary
- Overall score: {X}/6 pillars addressed
- Critical issues: {count}
- Top recommendation: {one-liner}

### Pillar Analysis
#### 1. Operational Excellence — {Good/Needs Work/Critical}
...

### Risk Matrix
| Risk | Severity | Pillar | Recommendation |
...

### Recommended Changes (Priority Order)
1. ...
```

---

## Mode: Exam Strategy Coach

### Input
- Progress data: `aws-csa/study-progress.md` (ALL domains)
- Exam timeline: collected via `AskUserQuestion` — "When is your exam?" — options: `This week`, `2 weeks`, `1 month`, `Not scheduled`

### Instructions

Generate a personalized exam strategy based on current readiness and time remaining.

**Generate:**
1. **Current Readiness Assessment**:
   - Overall readiness percentage
   - Strongest domains (leverage these)
   - Weakest domains (focus here)
   - Confidence level: Ready / Almost Ready / Needs More Time / Not Ready
2. **Study Schedule**:
   - Based on time remaining, allocate hours per domain
   - Prioritize: weak domains with high exam weight first
   - Include specific modes to use per domain
3. **Exam Day Strategy**:
   - Time management: 130 min / 65 questions = 2 min each, flag and move on
   - Question approach: eliminate 2 options first, then evaluate remaining
   - When to guess vs spend time
4. **Common SAA-C03 Traps**:
   - "Most cost-effective" vs "most performant" — read carefully
   - "Least operational overhead" = managed services
   - Multi-AZ vs Multi-Region distinction
   - S3 storage class selection nuances
   - When they say "decouple" = SQS/SNS
5. **Last-Minute Focus Areas**:
   - Top 10 topics to review the day before
   - Quick-reference cheat sheet items
6. **Confidence Building**:
   - Based on exam scores, predict likely pass/fail
   - Areas where scores show mastery

### Output Format
- Start with a readiness summary box
- Use timeline-specific advice (don't suggest 4-week plan if exam is in 2 days)
- Actionable daily/weekly schedule
- End with motivational note based on actual progress data

### Edge Case
If no progress data: "You haven't started studying yet. Here's a recommended 4-week study plan from scratch..." with domain order and mode recommendations.
