"""Build a self-study review file (wrong or correct answers) from a TD timed-test result export.

Question, options and TD explanation are copied verbatim; answers sit inside collapsed <details>.
Curated study notes (group, key words, trap/watch, rule) come from a per-test notes JSON
(schema: references/test-review-flow.md).

Usage:
  python3 build_test_review.py --source TD_..._Full.md --stats
  python3 build_test_review.py --source TD_..._Full.md --notes notes.json --mode wrong --out review.md
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from td_result_parser import parse_result  # noqa: E402

HOW_TO_USE = [
    "1. Read the question, pick your answer **before** opening the answer block.",
    "2. Open **Answer & explanation**; focus on why each wrong option fails.",
    "3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.",
]
PURPOSE = ("Confirm each correct answer was **knowledge, not a guess**. Answer again without looking; if you can't "
           "justify why every wrong option fails, tick **Guessed** and treat it as a wrong answer.")

MODES = {
    "wrong": {"title": "Wrong Answer Review", "note_icons": "🔑/🪤/🧠", "tracker": "| Group | Q | Pass 1 | Pass 2 | Pass 3 |",
              "cells": "☐ | ☐ | ☐", "trap_key": "trap", "trap_label": "🪤 **Your trap:**"},
    "right": {"title": "Correct Answer Review", "note_icons": "🔑/⚠️/🧠", "tracker": "| Group | Q | Guessed? | Pass 1 | Pass 2 |",
              "cells": "☐ | ☐ | ☐", "trap_key": "watch", "trap_label": "⚠️ **Watch:**"},
}


def stats(result) -> dict:
    """Numbers needed for the analysis file: score, single vs multi-select, per-third accuracy."""
    qs = [result.questions[n] for n in sorted(result.questions)]
    def rate(items):
        return f"{sum(q.correct for q in items)}/{len(items)}"
    thirds = [qs[i:i + len(qs) // 3 or 1] for i in range(0, len(qs), len(qs) // 3 or 1)][:3]
    wrong_multi = [q for q in qs if q.multi_select and not q.correct]
    partial = sum(1 for q in wrong_multi if set(q.picked.split(", ")) & set(q.answer.split(", ")))
    return {
        "title": result.title, "score": result.score_line, "domains": result.domains,
        "single": rate([q for q in qs if not q.multi_select]), "multi": rate([q for q in qs if q.multi_select]),
        "multi_wrong_with_partial_pick": f"{partial}/{len(wrong_multi)}",
        "thirds": [rate(t) for t in thirds],
        "wrong": [q.number for q in qs if not q.correct], "right": [q.number for q in qs if q.correct],
    }


def header(mode, notes_section, count, test_title, source_name, notes):
    cfg = MODES[mode]
    lines = [f"# {test_title} — {cfg['title']} ({count} questions)", ""]
    ref = (f" Summary: `{notes['analysis_file']}`." if mode == "wrong" and notes.get("analysis_file")
           else f" Wrong answers: `{notes['wrong_review_file']}`." if mode == "right" and notes.get("wrong_review_file")
           else "")
    lines += [f"Source: `{source_name}` (Q# = shuffled web order). Question, options and explanation are verbatim; "
              f"{cfg['note_icons']} are study notes.{ref}", ""]
    if mode == "wrong":
        lines += ["## How to use", ""] + HOW_TO_USE + [""]
    else:
        lines += ["## Purpose", "", PURPOSE, ""]
        pairs = notes_section.get("inconsistent", [])
        if pairs:
            lines += ["## ⚠️ Inconsistent concepts (right here, wrong elsewhere in this test)", "",
                      "| Right | Wrong | Concept |", "|---|---|---|"]
            lines += [f"| {r} | {w} | {c} |" for r, w, c in pairs]
            lines += ["", "These are partial knowledge — review each pair together.", ""]
    return lines


def build(result, notes, mode, source_name) -> str:
    cfg = MODES[mode]
    section = notes[mode]
    groups, meta = section["groups"], section["questions"]
    expected = {q.number for q in result.by_result(correct=(mode == "right"))}
    covered = {int(n) for n in meta}
    if expected != covered:
        raise SystemExit(f"notes/{mode} mismatch — missing {sorted(expected - covered)}, extra {sorted(covered - expected)}")
    unknown = {m["group"] for m in meta.values()} - set(groups)
    if unknown:
        raise SystemExit(f"notes/{mode}: undefined groups {sorted(unknown)}")

    order = [int(n) for g in groups for n in meta if meta[n]["group"] == g]
    out = header(mode, section, len(order), notes["title"], source_name, notes)
    out += ["## Tracker", "", cfg["tracker"], "|---|---|---|---|---|"]
    out += [f"| {meta[str(n)]['group']} | [Q{n}](#q{n}) | {cfg['cells']} |" for n in order]
    out.append("")

    for g, title in groups.items():
        qs = [n for n in order if meta[str(n)]["group"] == g]
        if not qs:
            continue
        out += ["---", "", f"# Group {g} — {title} ({len(qs)})", ""]
        for n in qs:
            q, m = result.questions[n], meta[str(n)]
            answer_line = (f"**Correct:** {q.answer} · **You picked:** {q.picked}" if mode == "wrong"
                           else f"**Correct:** {q.answer} (you answered correctly)")
            out += [f'<a id="q{n}"></a>', "", f"## Q{n}", "", q.stem, ""]
            out += [f"- **{k}.** {v}" for k, v in q.options]
            out += ["", "<details>", "<summary><b>Answer & explanation</b></summary>", "",
                    answer_line, "",
                    f"🔑 **Key words:** {m['keywords']}", "",
                    f"{cfg['trap_label']} {m[cfg['trap_key']]}", "",
                    f"🧠 **Rule:** {m['rule']}", "",
                    "### TD explanation", "", q.explanation, "", "</details>", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", required=True, help="TD result export (…_Full.md)")
    ap.add_argument("--stats", action="store_true", help="print analysis stats as JSON and exit")
    ap.add_argument("--notes", help="per-test notes JSON")
    ap.add_argument("--mode", choices=MODES, help="wrong | right")
    ap.add_argument("--out", help="output review markdown path")
    args = ap.parse_args()

    result = parse_result(args.source)
    if args.stats:
        print(json.dumps(stats(result), ensure_ascii=False, indent=2))
        return
    if not (args.notes and args.mode and args.out):
        ap.error("--notes, --mode and --out are required unless --stats")
    notes = json.loads(Path(args.notes).read_text(encoding="utf-8"))
    Path(args.out).write_text(build(result, notes, args.mode, Path(args.source).name), encoding="utf-8")
    print(f"wrote {args.mode} review to {args.out}")


if __name__ == "__main__":
    main()
