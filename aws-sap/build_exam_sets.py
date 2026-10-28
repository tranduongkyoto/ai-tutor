#!/usr/bin/env python3
"""Build exam-set JSONs (input for build_exam_page.py) from Udemy, TD and Neal sources.

Sets:
  udemy2  — Udemy Practice Test #2, all 75 questions, shuffled order
  udemy3  — Udemy Practice Test #3, all 75 questions, shuffled order
  mix     — 75 questions: Neal Exam C (35) + TD Set 6 (16) + Udemy Practice Test #1 (24 of 30), shuffled

Question ids keep the source (U2Q14, TD6Q3, T3Q25 …) so results can be split by source later.
Udemy questions have no official domain tags: domains come from the *_unseen_source.md categories
plus a stem-based classification (practice-exam/sap/udemy_domains.json) — approximate.

Usage: python3 aws-sap/build_exam_sets.py   (writes practice-exam/sap/exam_sets/*.json)
"""
import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAP = ROOT / "practice-exam" / "sap"
OUT = SAP / "exam_sets"
sys.path.insert(0, str(ROOT / ".claude" / "skills" / "ai-tutor" / "scripts"))
from review_set_session import parse_source  # noqa: E402  TD-layout parser

QUESTION_SPLIT = re.compile(r"^## Question (\d+)\s*$", re.M)
UDEMY_OPTION = re.compile(r"^([A-G])\. ", re.M)
CORRECT_MARK = "**(Correct)**"
TD_DOMAIN = {
    "Design Solutions for Organizational Complexity": "ORG",
    "Design for New Solutions": "NEW",
    "Continuous Improvement for Existing Solutions": "CI",
    "Accelerate Workload Migration and Modernization": "MIG",
}
EXAM_WEIGHTS = {"ORG": 0.26, "NEW": 0.29, "CI": 0.25, "MIG": 0.20}


def qtype(correct):
    return "Select Multiple" if len(correct) > 1 else "Single Choice"


def parse_udemy(test_no, domains):
    """Udemy layout: '## Question N', stem, 'A. …' options (may span lines), '**(Correct)**' marks."""
    text = (SAP / f"practice_test_{test_no}.md").read_text(encoding="utf-8")
    parts = QUESTION_SPLIT.split(text)
    out = []
    for i in range(1, len(parts), 2):
        n, block = parts[i], parts[i + 1]
        body, expl = block.split("**Explanation:**", 1)
        starts = list(UDEMY_OPTION.finditer(body))
        stem = body[:starts[0].start()].strip()
        opts, correct = [], []
        for m, nxt in zip(starts, starts[1:] + [None]):
            raw = body[m.end():nxt.start() if nxt else len(body)].strip().rstrip("-").strip()
            if CORRECT_MARK in raw:
                correct.append(m.group(1))
                raw = raw.replace(CORRECT_MARK, "").strip()
            opts.append([m.group(1), raw])
        if not correct:
            raise ValueError(f"Udemy #{test_no} Q{n}: no correct option")
        qid = f"U{test_no}Q{n}"
        out.append({"id": qid, "type": qtype(correct), "stem": stem, "opts": opts, "correct": correct,
                    "expl": expl.strip().rstrip("-").strip(), "domain": domains[qid], "topic": "", "note": ""})
    return out


def parse_td6():
    out = []
    for n, q in sorted(parse_source(SAP / "SAP-Review-Mode-Set-6.md").items()):
        correct = q.answer.split(", ")
        out.append({"id": f"TD6Q{n}", "type": qtype(correct), "stem": q.stem, "opts": [list(o) for o in q.options],
                    "correct": correct, "expl": q.explanation, "domain": TD_DOMAIN[q.domain], "topic": "", "note": ""})
    return out


def load_domains():
    """Known categories from the isolated unseen sources + stem classification for the rest."""
    domains = json.loads((SAP / "udemy_domains.json").read_text(encoding="utf-8"))
    for n in (1, 2, 3):
        text = (SAP / f"udemy{n}_unseen_source.md").read_text(encoding="utf-8")
        for q, cat in re.findall(r"^## Question (\d+)\s*\n+\*\*Category:\*\* CSAP – (.+?)\s*$", text, re.M):
            domains[f"U{n}Q{q}"] = TD_DOMAIN[cat]
    return domains


def pick_udemy1(u1, fixed, keep):
    """Keep all unseen Udemy #1 questions, then fill with seen ones that move the mix toward exam weights."""
    unseen = {f"U1Q{q}" for q in re.findall(r"^## Question (\d+)", (SAP / "udemy1_unseen_source.md").read_text(), re.M)}
    chosen = [q for q in u1 if q["id"] in unseen]
    pool = [q for q in u1 if q["id"] not in unseen]
    counts = {d: sum(q["domain"] == d for q in fixed + chosen) for d in EXAM_WEIGHTS}
    while len(chosen) < keep:
        total = sum(counts.values()) + 1
        need = max(EXAM_WEIGHTS, key=lambda d: EXAM_WEIGHTS[d] - counts[d] / total)
        pick = next((q for q in pool if q["domain"] == need), pool[0])
        pool.remove(pick)
        chosen.append(pick)
        counts[pick["domain"]] += 1
    return chosen


def write(name, title, store, minutes, questions, seed):
    random.Random(seed).shuffle(questions)
    OUT.mkdir(exist_ok=True)
    path = OUT / f"{name}.json"
    path.write_text(json.dumps({"title": title, "store": store, "minutes": minutes, "questions": questions},
                               ensure_ascii=False, indent=1), encoding="utf-8")
    mix = {d: sum(q["domain"] == d for q in questions) for d in EXAM_WEIGHTS}
    multi = sum(q["type"] == "Select Multiple" for q in questions)
    print(f"{path.relative_to(ROOT)}: {len(questions)} q · multi {multi} · {mix}")


def main():
    domains = load_domains()
    write("udemy2", "Udemy Practice Test #2 — full timed, 75 questions", "sap-udemy2-full", 210,
          parse_udemy(2, domains), 1028)
    write("udemy3", "Udemy Practice Test #3 — full timed, 75 questions", "sap-udemy3-full", 210,
          parse_udemy(3, domains), 2028)
    neal_c = json.loads((SAP / "neal" / "neal_exam_C.json").read_text(encoding="utf-8"))["questions"]
    fixed = neal_c + parse_td6()
    u1 = pick_udemy1(parse_udemy(1, domains), fixed, 75 - len(fixed))
    write("mix_nealc_td6_udemy1", "Mixed mock — Neal C 35 + TD6 16 + Udemy #1 24, 75 questions",
          "sap-mix-nealc-td6-u1", 210, fixed + u1, 3028)


if __name__ == "__main__":
    main()
