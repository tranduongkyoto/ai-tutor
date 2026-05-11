# Quiz Flow Protocol

Interactive quiz protocol for Mini Exam mode using `AskUserQuestion`.

## Setup

1. Ask question count via `AskUserQuestion`: "How many questions for this exam?" — options: `5`, `10`, `15`
2. Determine scope:
   - Guided Phase 2: `scope=concepts`
   - Guided Phase 4: `scope=scenarios`
   - Guided Phase 6: `scope=hands-on`
   - Guided Phase 7: `scope=comprehensive`
   - Free mode: `scope=general`
3. Read inputs:
   - Cache file: `.claude/skills/ai-tutor/cache/aws-csa-{domain}.md` (domain knowledge)
   - Domain topics: `certs/aws-csa/domains.md` (topic checklist for coverage)
   - Progress: `aws-csa/study-progress.md` (weak topics to prioritize)
4. Generate questions using the Mini Exam prompt template from `references/prompt-templates.md`, passing `scope`
5. Run self-verify step: review each question for answer clarity, fix issues

## Question Generation Rules

- Exactly 5 options (A-E) per question
- Exactly ONE unambiguously correct answer
- Distractors must be plausible but definitively wrong per AWS docs
- Ground all questions in cached PDF content
- Prioritize weak topics from study-progress.md (at least 30% of questions if weak topics exist)
- Mix: 60% scenario-based, 40% fact-based
- Difficulty: 30% easy, 50% medium, 20% hard

## Presentation (one question at a time)

For each question:

1. Display the question and all 5 options as formatted terminal text:
   ```
   **Question {N}/{total}:**
   {question text}

   A) {option A}
   B) {option B}
   C) {option C}
   D) {option D}
   E) {option E}
   ```

2. Use `AskUserQuestion` with:
   - Question: "Your answer?"
   - Options: `A`, `B`, `C`, `D`
   - User types `E` via the "Other" option if needed

3. After user answers, show immediate feedback:
   ```
   ✓ Correct! / ✗ Incorrect — correct answer: {letter}
   {Brief explanation — why correct answer is right}
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
- **User selects "Other" and types "E" or "e"**: Normalize to option E (case-insensitive match)
- **User selects "Other" and types anything else**: Treat as incorrect, show correct answer
