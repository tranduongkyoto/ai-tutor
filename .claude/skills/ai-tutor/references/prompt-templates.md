# Prompt Templates

Mode-specific prompt templates for the AI Tutor skill. Each section defines the inputs, instructions, and output format for one study mode.

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

### Output Format
- Use headers (`##`, `###`) for sections
- Bullet points for details — concise, not paragraphs
- Tables for comparisons (e.g., instance type families, storage tier comparison)
- Bold key terms and service names
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
- Cached content: loaded from `cache/aws-csa-{domain}.md`
- Topic checklist: from `certs/aws-csa/domains.md`
- Weak topics: from `aws-csa/study-progress.md` (prioritize these)

### Instructions

Generate `{count}` exam-style questions following these rules:

**Question Quality Rules:**
1. Each question MUST have exactly 5 options (A-E)
2. Exactly ONE correct answer per question
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
A) [option]
B) [option]
C) [option]
D) [option]
E) [option]
Correct: [letter]
Topic: [topic-slug]
Explanation: [Why correct answer is right. For each wrong option: why it's wrong — 1 sentence each.]
```

Then present questions interactively using the protocol in `references/quiz-flow.md`.

---

## Mode: Scenario Generator

### Input
- Domain: `{domain}`
- Cached content: loaded from `cache/aws-csa-{domain}.md`

### Instructions

Generate 5 realistic exam-style scenarios for the **{domain}** domain. Each scenario should simulate a real SAA-C03 exam question at medium-to-hard difficulty.

**Per scenario:**
1. **Business Context**: Company situation, industry, scale (e.g., "A fintech startup processing 10K transactions/second...")
2. **Technical Requirements**: Specific constraints — latency, availability, budget, compliance, scale
3. **Question**: What should the solutions architect recommend?
4. **Options (A-E)**: 5 options, each a valid-sounding architecture but only one best answer
5. **Correct Answer**: Letter + detailed explanation
6. **Why Others Are Wrong**: 1-2 sentences per wrong option explaining the specific flaw
7. **Key Concept**: The AWS concept being tested

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
E) {option}

**Answer: {letter}**
{Detailed explanation}

**Why others are wrong:**
- A) {reason}
- B) {reason}
...

**Key Concept:** {concept being tested}
```

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
