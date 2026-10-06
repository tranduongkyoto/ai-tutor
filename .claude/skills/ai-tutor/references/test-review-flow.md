# Test Review Flow (`sap test-review <result-file> [--vi]`)

Post-test pipeline for a timed test taken on the Tutorials Dojo website and exported as markdown
(e.g. `practice-exam/sap/TD_SAP_Timed_Set{N}_Full.md`). Produces analysis + self-study review files
+ redo tracker. Reference run: TD Set 5 (2026-09-25).

Scripts: `.claude/skills/ai-tutor/scripts/` (run with `python3`, from `practice-exam/sap/`).
Below, `S=../../.claude/skills/ai-tutor/scripts` and `SRC=<result-file>`.

## Outputs (all in `practice-exam/sap/`, `{n}` = set number)

| File | Content |
|---|---|
| `td_set_{n}_analysis.md` | Score, domains, single vs multi, pattern groups, 10 rules, next actions |
| `td_set_{n}_review_notes.json` | Curated per-question notes (source of truth for review builds) |
| `td_set_{n}_review.md` | Wrong answers: verbatim Q/options, collapsed answer + notes + TD explanation, tracker |
| `td_set_{n}_review_correct.md` | Correct answers: same layout, "Guessed?" tracker, inconsistent-concept table |

Question numbers = shuffled web order in the export (not Review-Mode numbering). Always read questions
from the export file, never from `SAP-Review-Mode-Set-{N}.md`.

Two export layouts are parsed by `td_result_parser.py` (auto-detected):
- `TD_SAP_Timed_Set{N}_Full.md` / `TD_SAP_Review_Set{N}_Full.md` — `## Câu N — ✅/❌` blocks, shuffled web order
- `TutorialsDojo_SAP_Timed_Mode_Set_{N}.md` — `### Câu N (mục k – <domain>) — ✅/❌` blocks grouped by domain,
  inline ✅/❌/👉 option markers; domain scores are computed from the per-question tags. Question order is by
  domain, so per-third accuracy is not a fatigue signal for this layout.

## Step 1 — Stats

```bash
python3 $S/build_test_review.py --source $SRC --stats
```
Gives score, domains, single vs multi-select, multi-select misses with ≥1 correct pick, per-third accuracy,
wrong/right question lists. Ask the user for time taken if not in the export.

## Step 2 — Diagnose wrong answers

Extract per wrong question: stem, correct option(s), learner's pick, and the TD "The option that says … is
incorrect" line for the pick. Group misses by **pattern**, not by service (Set 5 groups: DIY over managed
service / multi-account governance / DR & Route 53 / migration / serverless + DB / networking & S3).
Cross-check weak areas in `chapter_drill_progress.md` and `aws-sap/study-progress.md` → flag repeats (🔁).

## Step 3 — Write notes JSON

`td_set_{n}_review_notes.json` schema (key order = display order):

```json
{
  "title": "TD Set 5",
  "analysis_file": "td_set_5_analysis.md",
  "wrong_review_file": "td_set_5_review.md",
  "wrong": {
    "groups": {"A": "DIY over managed service", "B": "..."},
    "questions": {"1": {"group": "A", "keywords": "...", "trap": "...", "rule": "..."}}
  },
  "right": {
    "groups": {"A": "..."},
    "questions": {"11": {"group": "A", "keywords": "...", "watch": "...", "rule": "..."}},
    "inconsistent": [["Q44", "Q16", "CUR in management account + QuickSight"]]
  }
}
```
- `keywords`: requirement words that decide the answer · `trap`: why the learner's pick failed ·
  `watch` (right mode): distractor to watch / link to a wrong question on the same concept · `rule`: one-line exam rule
- `inconsistent`: concepts answered right in one question but wrong in another (partial knowledge)
- Build fails fast if notes don't cover exactly the wrong (or right) question set

## Step 4 — Build + verify review files

```bash
python3 $S/build_test_review.py --source $SRC --notes td_set_{n}_review_notes.json --mode wrong --out td_set_{n}_review.md
python3 $S/build_test_review.py --source $SRC --notes td_set_{n}_review_notes.json --mode right --out td_set_{n}_review_correct.md
python3 $S/verify_test_review.py --source $SRC --review td_set_{n}_review.md --mode wrong
python3 $S/verify_test_review.py --source $SRC --review td_set_{n}_review_correct.md --mode right
```
⚠️ Rebuilding overwrites tracker marks and Vietnamese sections — only rebuild fresh files, or re-run
the merge (Step 6) and restore tracker marks afterwards.

## Step 5 — Analysis file + progress

Write `td_set_{n}_analysis.md` (scores, why drill vs timed gap, pattern tables with correct answer + why
pick was wrong, multi-select lesson, 10 rules, next actions). Update `aws-sap/study-progress.md`
(timed test row, domains, forecast, weak areas). Present summary to user; do not print the full files.

## Step 6 — Vietnamese deep-dive (`--vi` only)

Only when the user passes `--vi` (or asks later). Default: wrong answers only; correct answers only on request.

1. Style + exemplar: `references/vietnamese-explanation-style.md`
2. Spawn parallel `general-purpose` subagents (≤6, ~6–9 questions each, split by pattern group). Each gets:
   the style file path, the review file path, its question list, output dir `/tmp/td-set{n}-vi/`,
   group context (e.g. repeat mistakes → `⚠️ Lỗi lặp lại`), and "create only Q{n}.md files, modify nothing else"
3. After all finish, merge + verify:
   ```bash
   python3 $S/merge_vietnamese_explanations.py --review td_set_{n}_review.md --fragments /tmp/td-set{n}-vi
   python3 $S/verify_test_review.py --source $SRC --review td_set_{n}_review.md --mode wrong
   ```
4. Spot-check the highest-risk questions (repeat mistakes, questions the user missed twice) against the TD
   explanation; add `📝 Ghi chú kỹ thuật` where exam wording differs from real behavior; re-run merge (idempotent)

## Redo sessions

`redo group X[,Y]` → shuffle that group's questions, present verbatim via `AskUserQuestion` with **full option
text in each option description** (single-choice) or typed answer (multi-select, no example formats), short
feedback per answer. At the end, mark the tracker column in `td_set_{n}_review.md`
(`✅ MM-DD` / `❌ MM-DD`) — Pass 1 same day after study, Pass 2 after 3–4 days, Pass 3 after ~1 week.
