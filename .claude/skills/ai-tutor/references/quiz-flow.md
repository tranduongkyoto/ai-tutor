# Quiz Flow Protocol

Interactive quiz protocol for Mini Exam mode using `AskUserQuestion`.

## Setup

1. Ask question count via `AskUserQuestion`: "How many questions for this exam?" — options: `5`, `10`, `15`
2. Determine scope:
   - Guided Phase 2: `scope=concepts`
   - Guided Phase 4: `scope=scenarios`
   - Guided Phase 5: `scope=design`
   - Guided Phase 6: `scope=comprehensive`
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

### Q{N} ✓/✗ — {Short title} ({topic-slug})
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
