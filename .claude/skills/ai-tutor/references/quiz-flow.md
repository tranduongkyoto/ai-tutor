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

## Presentation (one question at a time)

For each question:

1. **CRITICAL: Print ALL 4 options as plain text FIRST.** Every option (A-D) MUST appear in the terminal output above the answer prompt. Never rely on `AskUserQuestion` descriptions to show option text.
   ```
   **Question {N}/{total}:**
   {question text}

   A) {option A}
   B) {option B}
   C) {option C}
   D) {option D}
   ```

2. **After** all options are printed, use `AskUserQuestion`:
   - **Single-select**: Question: "Your answer?" — Options: `A`, `B`, `C`, `D` — `multiSelect: false`
   - **Multi-select**: Question: "Your answers? (Select TWO)" — Options: `A`, `B`, `C`, `D` — `multiSelect: true`

3. After user answers, show immediate feedback:
   - **Single-select**:
     ```
     ✓ Correct! / ✗ Incorrect — correct answer: {letter}
     {Brief explanation — why correct answer is right}
     ```
   - **Multi-select**: User must select BOTH correct answers to score. Partial = incorrect.
     ```
     ✓ Correct! (selected A, C) / ✗ Incorrect — correct answers: {letter}, {letter}
     {Brief explanation — why each correct answer is right}
     ```

4. Proceed to next question

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

## Edge Cases

- **Odd question count**: Works fine — one question at a time
- **User selects "Other" and types anything**: Treat as incorrect, show correct answer
