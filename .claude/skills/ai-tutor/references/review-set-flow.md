# Review Set Flow (`sap review-set <N>`)

A full TD set (75q) taken in the tutor terminal in **review mode**: answer 25 questions with no feedback,
then review all 25, then the next block. At the end, results are exported in the TD timed-export format, so the
standard `test-review` pipeline (analysis + review files + redo tracker, optional `--vi`) runs unchanged.
It's for the drill-pool sets (TD1, TD2, TD5). **Never use it on TD3, TD4 or TD6.** They are reserved for timed checkpoints.
Refuse and point to the timed test on the TD website.

Script: `.claude/skills/ai-tutor/scripts/review_set_session.py`, run from `practice-exam/sap/` with
`S=../../.claude/skills/ai-tutor/scripts`. On Windows, prefix the `test-review` scripts with `PYTHONUTF8=1`
(e.g. `PYTHONUTF8=1 python3 $S/build_test_review.py ...`). Without it, they crash when printing Vietnamese text to the console.

## Rules (agreed 2026-09-28)

| Rule | Setting |
|---|---|
| Feedback | **Blocks of 25**: no correct/wrong signal or explanation until the block is done |
| Order | Shuffled (saved in the session file); show `Q{pos}` only, never the TD number, while answering |
| Multi-select | Typed answer, **all-or-nothing** scoring; the script rejects the wrong number of picks |
| Questions seen in drills | Answered and scored like any other question. `status`/`export` also show an unseen-only score for information |
| Confidence tags / keyword step | Off |
| Explanations | Not shown during a block. At reveal, show them for wrong answers only (`--all` also shows correct ones) |

## Files (`practice-exam/sap/`)

| File | Content |
|---|---|
| `td_review_set_{n}_session.json` | Shuffled order, seen-in-drills list, answers, revealed blocks (resume state) |
| `TD_SAP_Review_Set{n}_Full.md` | Export in the TD timed-export format; the `--source` for `test-review` |

## Step 0 — Start or resume

```bash
python3 $S/review_set_session.py status --set {n}
```
- If there's no session, run `init --set {n}`. It shuffles and records which questions were seen in drills
  (the `| TD{n}:Q{m} ` rows in `chapter_drill_progress.md`).
- If a session exists, resume at the reported next question. If the last full block was answered but not revealed,
  do Step 2 for it first.
- Show: `📋 TD Set {n} review mode — block {b}/3 · Q{from}–Q{to} · {answered}/75 answered`

## Step 1 — Answer a block (no feedback)

```bash
python3 $S/review_set_session.py show --set {n} --block {b}
```
For each question in the block:
1. Print the question and **all options verbatim** (same rule as practice tests: no summarizing).
2. Collect the answer:
   - Single-choice with ≤4 options: `AskUserQuestion`, with each option's full text in its description.
   - Multi-select, or more than 4 options: typed answer. State "Select {k}" and give no example format.
3. Reply only `Recorded (Q{pos}).`, with **no correct/wrong hint**. Move on to the next question.
4. Every ~5 questions, and at the end of the block, save the answers:
   `python3 $S/review_set_session.py record --set {n} --answers "1=B; 2=A,C; ..."`.
   If the script rejects an answer (wrong number of picks, invalid letter), ask that question again.

The user can type `pause` at any time. Save the answers so far and stop. `status` resumes later.

## Step 2 — Review the block

```bash
python3 $S/review_set_session.py reveal --set {n} --block {b}
```
Present:
1. Block score, then the running score, single vs multi-select, and scores by domain (from the script output).
2. Wrong answers, one at a time:
   - `❌ Q{pos} — picked X · correct Y · {domain}`
   - **Key words** (the requirement words that decide the answer)
   - **Why your pick fails** (TD's "The option that says … is incorrect" line)
   - **Rule** (one line)
   - Mark 🔁 if it repeats a known weak area from `study-progress.md` or `td_set_5_review.md`.
   - On multi-select misses where one pick was correct, say which pick broke the solution.
3. Correct answers: one line per question (`✅ Q{pos} · {domain} · rule`). Only go deeper if the user asks.
4. Short pattern note for the block (e.g. "3 of 5 misses = DIY over managed service").

Then `AskUserQuestion`: `Next block` (Recommended) / `Pause here`.

## Step 3 — Finish

After block 3 is reviewed:
```bash
python3 $S/review_set_session.py export --set {n}
```
1. Show the final score, the unseen-only score, domains vs the TD Set 5 baseline, and single vs multi-select.
2. **Gate** (from `aws-sap/study-progress.md` Plan): TD1 and TD2 must each reach **≥70%**. Migration below 50% →
   do the migrations chapter drill before TD Set 3 timed.
3. Update `aws-sap/study-progress.md`: fill in the Practice Tests row for the set, the TD question usage row
   (`all 75 (review mode)`), and weak areas.
4. Offer `test-review` on `TD_SAP_Review_Set{n}_Full.md` (see `references/test-review-flow.md`). It outputs
   `td_set_{n}_*` files plus a redo tracker, and adds the Vietnamese deep-dive when `--vi` is passed. Pass 1 of the redo happens
   the same day, Pass 2 after 3–4 days, Pass 3 after ~1 week.
