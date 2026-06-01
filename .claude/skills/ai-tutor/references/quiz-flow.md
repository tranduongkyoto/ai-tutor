# Quiz Flow Protocol

Interactive quiz protocol for Mini Exam mode using `AskUserQuestion`.

**HARD RULE — Never reveal answers before user responds.** Each question's correct answer and explanation MUST be hidden until Step 3 (after the user submits). Showing "Answer: B" or any correct-answer hint alongside the question defeats the entire purpose of the exam. The internal question data (Correct, Explanation fields) is for scoring only — never output it during question presentation.

## Setup

1. Ask question count via `AskUserQuestion`: "How many questions for this exam?" — options: `5`, `10`, `15`
   - **Skip for learn-and-test and scenario-practice modes** — question count is determined by content (2-3 per section or per scenario), not user choice.
2. Determine scope:
   - Guided Phase 3: `scope=design`
   - Guided Phase 4: `scope=comprehensive`
   - Free mode: `scope=general`
3. Read inputs:
   - Cache file: `.claude/skills/ai-tutor/cache/aws-csa-{domain}.md` (domain knowledge)
   - Domain topics: `certs/aws-csa/domains.md` (topic checklist for coverage)
   - Progress: `aws-csa/study-progress.md` (weak topics to prioritize)
4. Generate questions using the Mini Exam prompt template from `references/prompt-templates.md`, passing `scope`
5. Run self-verify step: review each question for answer clarity, fix issues

## Question Types (match real SAA-C03 exam)

**Two types — mix ~80% single / ~20% multi per exam:**

1. **Single-select** (type: `single`): 4 options (A-D), pick 1 correct answer
2. **Multi-select** (type: `multi`): 4 options (A-D), pick 2 correct answers. Question states: *"(Select TWO)"*

For a 10-question exam: ~8 single + ~2 multi. For 5-question: ~4 single + ~1 multi.

## Question Generation Rules

- Exactly 4 options (A-D) per question — matches real SAA-C03 exam format
- Single-select: exactly ONE correct answer
- Multi-select: exactly TWO correct answers, question must say "(Select TWO)"
- Distractors must be plausible but definitively wrong per AWS docs
- Ground all questions in cached PDF content
- Prioritize weak topics from study-progress.md (at least 30% of questions if weak topics exist)
- Mix: 60% scenario-based, 40% fact-based
- Difficulty: 30% easy, 50% medium, 20% hard

## Option Balance Rule

- All 4 options (A-D) MUST be similar in length (within 2x of each other)
- If option A is 15 words, option D cannot be 5 words
- Longest option should NOT always be the correct answer
- Apply this during question generation AND self-verify step

## Presentation (one question at a time)

Each question follows a strict 2-step cycle. **Never combine steps into one turn.**

**Step 1 — Draft (MANDATORY). Do NOT call AskUserQuestion in this step:**

Write a complete text block with the question and ALL 4 options. Output this and STOP:

```
**Question {N}/{total}:**
{question text}

A) {option A full text}
B) {option B full text}
C) {option C full text}
D) {option D full text}
```

**CRITICAL: Do NOT reveal the answer in this step.** The output MUST contain ONLY the question text and options A-D. Never include: the correct answer letter, "Answer:", "Correct:", explanations, or any hint about which option is right. The answer is revealed ONLY in Step 3 after the user responds.

**Step 2 — Tool call (ONLY after Step 1 text is fully output):**

Call `AskUserQuestion` with short labels only:
- **Single-select**: Question: "Your answer?" — Options: `A`, `B`, `C`, `D` — `multiSelect: false`
- **Multi-select**: Question: "Your answers? (Select TWO)" — Options: `A`, `B`, `C`, `D` — `multiSelect: true`

**Step 3 — Feedback (TEXT-ONLY turn. Do NOT call AskUserQuestion for the next question in this turn):**

Show immediate feedback and STOP. The next question starts in a new turn.

- **Single-select**:
  ```
  ✓ Correct! — {letter} is right.
  {Why correct answer is right. Why each wrong option is wrong — 1 sentence each.}
  ```
  or
  ```
  ✗ Incorrect — correct answer: {letter}
  {Why correct answer is right. Why each wrong option is wrong — 1 sentence each.}
  ```
- **Multi-select**:
  ```
  ✓ Correct! (selected {letters}) / ✗ Incorrect — correct answers: {letter}, {letter}
  {Why each correct answer is right. Why each wrong option is wrong.}
  ```

**Step 4 — Next question:** Return to Step 1 for the next question (new turn).

## Multi-select Scoring

- `AskUserQuestion` with `multiSelect: true` returns an ARRAY of selected options
- User must select EXACTLY 2 options
- Score as correct ONLY if both selected options match both correct answers
- Order does not matter: `["A","C"]` equals `["C","A"]`
- Selecting 1 or 3+ options = incorrect

## Fallback

If `AskUserQuestion` tool is unavailable or fails:
- Print the question with all 4 options as text
- Ask user to type their answer letter(s) directly in chat
- Parse the response (accept: `A`, `a`, `A)`, `Option A`, `a,c`, `A and C`)

## Scoring

After all questions answered:

1. Display summary:
   ```
   ## Exam Results: {Domain} — {scope} — {score}/{total} ({percentage}%)

   | # | Result | Your Answer | Correct | Topic |
   |---|--------|-------------|---------|-------|
   | 1 | ✓      | B           | B       | ebs-types |
   | 2 | ✗      | A           | C       | s3-lifecycle |
   ...
   ```

2. List missed topics: extract topic tags from incorrect questions
   - For single-topic questions: add topic slug to missed list
   - For cross-domain questions (multiple topic tags): add ALL topic slugs to missed list
   - Format: `primary-topic` for same-domain, `domain:topic` for cross-domain
   Example: `[s3-security, networking:cloudfront]`
3. Return data for progress tracking:
   - `score`: number correct
   - `total`: number of questions
   - `missed_topics`: list of topic slugs from incorrect answers
   - `percentage`: score/total * 100

## Session File Format (ALL scopes)

**CRITICAL:** Every mini-exam session file MUST save full question details — not just a summary table. This applies to ALL scopes (concepts, scenarios, design, comprehensive, general).

Write the session file to `aws-csa/study-sessions/{YYMMDD}-{HHMM}-{domain}-mini-exam-{scope}.md` with this format:

```markdown
# {Domain} — Mini Exam: {Scope Title} (Phase {N})
**Date:** {YYYY-MM-DD HH:MM}
**Score:** {score}/{total} ({percentage}%)
**Scope:** {scope} — {scope description}

---

## Questions & Results

### Q{N} ✓/✗ — {Short title} ({topic-slug} | {topic-slug, cross-domain:topic-slug})
**Question:** {Full question text}

A) {option A text}
B) {option B text}
C) {option C text}
D) {option D text}

**Your answer: {letter(s)}** — Correct/Incorrect. {Explanation of why correct answer is right. If incorrect, state the correct answer.}

---

{repeat for all questions}

## Summary
- **Score:** {score}/{total} ({percentage}%)
- **Missed topics:** {comma-separated topic slugs, or "none"}
- **Strong areas:** {topics answered correctly}
- **Key lessons:**
  - {lesson from each missed question — what to remember}
```

**Rules:**
- Always include ALL 4 choices (A-D) with full text — never abbreviate
- Always record the user's actual answer letter(s)
- Mark each question with ✓ (correct) or ✗ (incorrect)
- For multi-select questions, show both selected and correct answers
- Include the explanation after each question — not just at the end
- The "Key lessons" section summarizes takeaways from missed questions only

## Edge Cases

- **Odd question count**: Works fine — one question at a time
- **User selects "Other" and types anything**: Treat as incorrect, show correct answer

---

## Hint Flow Protocol

Extended quiz cycle used by learn-and-test and scenario-practice modes. Adds a hint step between question presentation and answer collection.

### Per-Question Cycle (4 steps, 3 turns)

**Step 1 — Present question (TEXT ONLY, no AskUserQuestion):**
Show question text + all 4 options (A-D). NEVER reveal answer.

**Step 2 — Show hint (TEXT ONLY, same turn as Step 1):**
Show hint immediately after options:
```
💡 Hint: {1-sentence directional nudge}
```

Hint rules:
- 1 sentence, points toward the AWS concept being tested
- NEVER mention the correct option letter
- NEVER repeat any option text verbatim
- NEVER give away the answer directly
- Focus on the architectural pattern, service category, or design principle

**Step 3 — Collect answer (AskUserQuestion):**
Same as standard flow: "Your answer?" with A, B, C, D options. `multiSelect: false`.

**Step 4 — Feedback (TEXT ONLY, new turn):**
Same as standard flow: ✓/✗ + explanation. Then proceed to next question or section.

---

## Section Quiz Cycle — Content-First (learn-and-test mode)

Flow for Phase 1 guided mode. Two-phase: generate all content to .md file first, then teach + quiz section-by-section.

### Content Phase (runs first, all sections)
1. Generate all 7 sections with full content (same quality as concept-mapper — diagrams, tables, bold terms)
2. Write complete content to session file (NOT to terminal — terminal output happens per-section in quiz phase)
3. Show: `📄 Content saved to {file}. Open in IDEA to study with rendered diagrams.`

### Resume Detection (before starting quiz phase)
Check for an existing partial session file (`*-{domain}-learn-and-test.md` with `[PARTIAL]` in title or sections missing `### Quiz: Section {N}`):
- If found: read file, identify sections with quiz results, skip completed sections
- Show: `📍 Resuming from Section {N}/7 — Sections 1-{N-1} already completed.`
- If not found: start from Section 1

### Quiz Phase (section-by-section — teach then quiz)
For each section (1-7), in order:
1. **Teach**: Read section content from the .md file and output it to terminal
2. **Quiz**: Generate 2-3 questions on that section's material
3. Run each question through the Hint Flow Protocol (above)
4. After section's questions: `Section {N}/7 complete: {X}/{Y} correct`
5. **Save inline**: Append quiz results to the session file as `### Quiz: Section {N}` at the end of that section (before the `---` separator and next section). This keeps content + quiz together.
6. **Update header**: Update running score and section progress in the file header. Mark `[PARTIAL]` until all 7 sections are done.

### After All 7 Sections
- Aggregate score: `{total_correct}/{total_questions} ({pct}%)`
- List missed topics by topic slug
- Remove `[PARTIAL]` from session file title; update final score in header
- No separate "question count" prompt — count is determined by sections (2-3 per section)

---

## Scenario Practice Cycle (scenario-practice mode)

Flow for Phase 2 guided mode. Two-phase: generate all scenarios to .md file first, then practice scenario-by-scenario.

### Content Phase (runs first, all scenarios)
1. Generate all scenarios with full content (context, requirements, question, options, answer, architecture diagram, wrong-option analysis, key concept)
2. Write complete content to session file (NOT to terminal — terminal output happens per-scenario in practice phase)
3. Show: `📄 {N} scenarios saved to {file}. Open in IDEA to study with rendered diagrams.`

### Resume Detection (before starting practice phase)
Check for an existing partial session file (`*-{domain}-scenario-practice.md` with `[PARTIAL]` in title or scenarios missing `**Your answer:**`):
- If found: read file, identify scenarios with answer results, skip completed scenarios
- Show: `📍 Resuming from Scenario {N}/{total} — Scenarios 1-{N-1} already completed.`
- If not found: start from Scenario 1

### Practice Phase (scenario-by-scenario — teach then quiz)
For each scenario, in order:
1. **Teach**: Read scenario from the .md file. Output to terminal: Context + Requirements + Question + Options (answer HIDDEN — do NOT show correct answer, explanation, diagram, or wrong-option analysis)
2. Show hint (same turn): `💡 Hint: {nudge toward correct pattern}`
3. Collect answer via AskUserQuestion
4. Reveal (new turn):
   - ✓/✗ + correct answer letter
   - Detailed explanation
   - Architecture diagram (Mermaid `graph TD`, max 10 nodes)
   - Why each wrong option fails (1 sentence each)
5. **Save inline**: Update the scenario in the session file — add `**Your answer: {letter}** — {Correct/Incorrect}` line
6. **Update header**: Update running score and scenario progress. Mark `[PARTIAL]` until all scenarios are done.
7. Proceed to next scenario

### After All Scenarios
- Aggregate score: `{correct}/{total} ({pct}%)`
- List missed topics
- Remove `[PARTIAL]` from session file title; update final score in header

---

## Keyword Drill Flow

Variant of the standard quiz flow optimized for quick-fire pattern recognition.

### Setup
1. Ask count via AskUserQuestion: "How many patterns?" — options: `10`, `25`, `All (~80)`
2. Load `references/keyword-patterns.md`
3. Read progress for previously missed patterns
4. Select patterns: prioritize missed (40%), random from remaining (60%)
5. Shuffle order

### Per-Pattern Cycle (same 2-step as standard quiz)

**Step 1 — Present pattern (TEXT ONLY, no AskUserQuestion):**
```
**Pattern {N}/{total}:**
"{trigger phrase from the pattern}"

A) {answer or distractor — shuffled}
B) {answer or distractor — shuffled}
C) {answer or distractor — shuffled}
D) {answer or distractor — shuffled}
```

**Step 2 — Collect answer:**
AskUserQuestion: "Your answer?" — Options: A, B, C, D — multiSelect: false

**Step 3 — Feedback (TEXT ONLY):**
```
✓ Correct! / ✗ Incorrect — correct answer: {letter}
{explanation from pattern data}
```

### Scoring
Same as standard quiz: score/total, missed patterns list.
Save missed patterns as `weak_topics` with prefix `kw:` (e.g., `kw:aurora-serverless`).
