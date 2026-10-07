"""Run a TD set in review mode (blocks of 25) and export results in the TD timed-export format.

Source: practice-exam/sap/SAP-Review-Mode-Set-{N}.md (answers marked with bold + ✅).
Session state: practice-exam/sap/td_review_set_{N}_session.json (shuffled order + answers).
Export: practice-exam/sap/TD_SAP_Review_Set{N}_Full.md — same layout as TD_SAP_Timed_Set{N}_Full.md, so
build_test_review.py / verify_test_review.py work unchanged. Q numbers = shuffled position.

A named set (e.g. `--set mixed_unseen_mock_1`) reads `{name}_source.md` (same TD layout), keeps state in
`{name}_session.json` and exports `{name}_export.md`; it has no drill-seen list.

Usage (run from practice-exam/sap/):
  python3 review_set_session.py init   --set 1 [--seed 7] [--force]
  python3 review_set_session.py show   --set 1 --block 1
  python3 review_set_session.py record --set 1 --answers "1=B; 2=A,C; 3=D"
  python3 review_set_session.py reveal --set 1 --block 1
  python3 review_set_session.py status --set 1
  python3 review_set_session.py export --set 1
"""
import argparse
import json
import random
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path

BLOCK = 25
RESERVED_SETS = {3, 4, 6}  # timed checkpoints only (aws-sap/study-progress.md)
QUESTION_SPLIT = re.compile(r"^## Question (\d+)\s*$", re.M)
OPTION_START = re.compile(r"^- (\*\*)?([A-G])\. ", re.M)  # option text may span lines (numbered steps)
CATEGORY = re.compile(r"^\*\*Category:\*\* CSAP – (.+?)\s*$", re.M)
JUNK_LINES = {"Correct", "Incorrect"}


@dataclass
class Question:
    number: int
    domain: str
    stem: str
    options: list  # [(letter, text)]
    answer: str  # "A, C"
    explanation: str

    @property
    def picks_needed(self) -> int:
        return len(self.answer.split(", "))


def _clean_option(text: str) -> str:
    text = text.replace("✅", "").strip()
    if text.endswith("**"):
        text = text[:-2].strip()
    return text


def _clean_explanation(text: str) -> str:
    lines = [ln.strip() for ln in text.splitlines()]
    kept = [ln for ln in lines if ln not in JUNK_LINES]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip()


def parse_source(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    parts = QUESTION_SPLIT.split(text)
    questions = {}
    for i in range(1, len(parts), 2):
        n, block = int(parts[i]), parts[i + 1]
        if "### Explanation" not in block:
            raise ValueError(f"Q{n}: missing ### Explanation")
        body, explanation = block.split("### Explanation", 1)
        cat = CATEGORY.search(body)
        starts = list(OPTION_START.finditer(body))
        if not (cat and starts):
            raise ValueError(f"Q{n}: missing category or options")
        stem = body[cat.end():starts[0].start()].strip()
        options, correct = [], []
        for m, nxt in zip(starts, starts[1:] + [None]):
            raw = body[m.end():nxt.start() if nxt else len(body)].strip()
            options.append((m.group(2), _clean_option(raw)))
            if m.group(1) or "✅" in raw:
                correct.append(m.group(2))
        if not correct:
            raise ValueError(f"Q{n}: no correct option marked")
        explanation = explanation.rsplit("---", 1)[0] if explanation.rstrip().endswith("---") else explanation
        questions[n] = Question(n, cat.group(1), stem, options, ", ".join(correct), _clean_explanation(explanation))
    return questions


def seen_in_drills(set_no, progress: Path) -> list:
    if not isinstance(set_no, int) or not progress.exists():
        return []
    found = re.findall(rf"^\| TD{set_no}:Q(\d+) ", progress.read_text(encoding="utf-8"), re.M)
    return sorted({int(x) for x in found})


class Session:
    def __init__(self, set_no: int, base: Path):
        self.set_no = set_no
        self.base = base
        named = not isinstance(set_no, int)
        self.label = set_no if named else f"TD{set_no}"
        self.path = base / (f"{set_no}_session.json" if named else f"td_review_set_{set_no}_session.json")
        self.export_path = base / (f"{set_no}_export.md" if named else f"TD_SAP_Review_Set{set_no}_Full.md")
        self.questions = parse_source(base / (f"{set_no}_source.md" if named else f"SAP-Review-Mode-Set-{set_no}.md"))
        self.data = json.loads(self.path.read_text(encoding="utf-8")) if self.path.exists() else None

    def require(self):
        if self.data is None:
            sys.exit(f"No session: run `init --set {self.set_no}` first")

    def save(self):
        self.path.write_text(json.dumps(self.data, indent=1, ensure_ascii=False), encoding="utf-8")

    def question_at(self, pos: int) -> Question:
        return self.questions[self.data["order"][pos - 1]]

    def block_positions(self, block: int) -> range:
        total = len(self.data["order"])
        start = (block - 1) * BLOCK + 1
        if start > total:
            sys.exit(f"Block {block} out of range ({total} questions)")
        return range(start, min(start + BLOCK, total + 1))

    def is_correct(self, pos: int) -> bool:
        return self.data["answers"].get(str(pos)) == self.question_at(pos).answer

    def seen(self, pos: int) -> bool:
        return self.question_at(pos).number in self.data["seen"]


def cmd_init(s: Session, args):
    if s.set_no in RESERVED_SETS and not args.allow_reserved:
        sys.exit(f"TD Set {s.set_no} is reserved for a clean timed checkpoint — take it timed on the TD website")
    if s.data is not None and not args.force:
        sys.exit(f"{s.path.name} exists — use --force to restart (answers will be lost)")
    order = sorted(s.questions)
    random.Random(args.seed).shuffle(order)
    s.data = {"set": s.set_no, "created": date.today().isoformat(), "seed": args.seed, "order": order,
              "seen": seen_in_drills(s.set_no, s.base / "chapter_drill_progress.md"), "answers": {},
              "revealed_blocks": []}
    s.save()
    blocks = (len(order) + BLOCK - 1) // BLOCK
    print(f"Session created: {s.label}, {len(order)} questions, {blocks} blocks, "
          f"{len(s.data['seen'])} seen in drills: {s.data['seen']}")


def cmd_show(s: Session, args):
    s.require()
    for pos in s.block_positions(args.block):
        q = s.question_at(pos)
        picks = f" · **Select {q.picks_needed}**" if q.picks_needed > 1 else ""
        print(f"## Q{pos}{picks}\n\n{q.stem}\n")
        for letter, text in q.options:
            print(f"- **{letter}.** {text}")
        print("\n---\n")


def parse_answers(raw: str) -> dict:
    out = {}
    for item in filter(None, (x.strip() for x in raw.split(";"))):
        pos, _, letters = item.partition("=")
        picks = sorted({x.strip().upper() for x in re.split(r"[,\s]+", letters) if x.strip()})
        if not pos.strip().isdigit() or not picks:
            sys.exit(f"Bad answer item: {item!r} (expected like 3=A,C)")
        out[int(pos)] = picks
    return out


def cmd_record(s: Session, args):
    s.require()
    total = len(s.data["order"])
    for pos, picks in parse_answers(args.answers).items():
        if not 1 <= pos <= total:
            sys.exit(f"Q{pos} out of range 1–{total}")
        q = s.question_at(pos)
        valid = {letter for letter, _ in q.options}
        if not set(picks) <= valid:
            sys.exit(f"Q{pos}: invalid option(s) {sorted(set(picks) - valid)}; valid {sorted(valid)}")
        if len(picks) != q.picks_needed:
            sys.exit(f"Q{pos}: needs {q.picks_needed} pick(s), got {len(picks)}")
        s.data["answers"][str(pos)] = ", ".join(picks)
    s.save()
    print(f"Recorded. {len(s.data['answers'])}/{total} answered.")


def rate(items) -> str:
    items = list(items)
    right = sum(items)
    return f"{right}/{len(items)} ({right / len(items):.0%})" if items else "—"


def cmd_reveal(s: Session, args):
    s.require()
    positions = list(s.block_positions(args.block))
    missing = [p for p in positions if str(p) not in s.data["answers"]]
    if missing:
        sys.exit(f"Block {args.block} not finished — unanswered: {missing}")
    print(f"# Block {args.block} (Q{positions[0]}–Q{positions[-1]}): {rate(s.is_correct(p) for p in positions)}\n")
    for pos in positions:
        q, ok = s.question_at(pos), s.is_correct(pos)
        seen = " 🔁seen" if s.seen(pos) else ""
        print(f"## Q{pos} ({s.label}:Q{q.number}) — {'✅' if ok else '❌'}{seen} · {q.domain}")
        print(f"Picked: {s.data['answers'][str(pos)]} · Correct: {q.answer}")
        if not ok or args.all:
            print(f"\n{q.explanation}\n")
        print("---")
    if args.block not in s.data["revealed_blocks"]:
        s.data["revealed_blocks"].append(args.block)
        s.save()
    print()
    cmd_status(s, args)


def cmd_status(s: Session, args):
    s.require()
    answered = sorted(int(p) for p in s.data["answers"])
    total = len(s.data["order"])
    print(f"Answered {len(answered)}/{total}; next question: Q{next((p for p in range(1, total + 1) if str(p) not in s.data['answers']), '—')}")
    if not answered:
        return
    unseen = [p for p in answered if not s.seen(p)]
    single = [p for p in answered if s.question_at(p).picks_needed == 1]
    multi = [p for p in answered if s.question_at(p).picks_needed > 1]
    partial = sum(1 for p in multi if not s.is_correct(p)
                  and set(s.data["answers"][str(p)].split(", ")) & set(s.question_at(p).answer.split(", ")))
    print(f"Score (all): {rate(s.is_correct(p) for p in answered)} · unseen only: {rate(s.is_correct(p) for p in unseen)}"
          f" · seen: {rate(s.is_correct(p) for p in answered if s.seen(p))}")
    print(f"Single: {rate(s.is_correct(p) for p in single)} · Multi: {rate(s.is_correct(p) for p in multi)}"
          f" (wrong multi with ≥1 correct pick: {partial})")
    by_domain = defaultdict(list)
    for p in answered:
        by_domain[s.question_at(p).domain].append(s.is_correct(p))
    for domain in sorted(by_domain):
        print(f"  {domain}: {rate(by_domain[domain])}")


def cmd_export(s: Session, args):
    s.require()
    total = len(s.data["order"])
    if len(s.data["answers"]) != total:
        sys.exit(f"Not finished: {len(s.data['answers'])}/{total} answered")
    positions = range(1, total + 1)
    right = sum(s.is_correct(p) for p in positions)
    by_domain = defaultdict(list)
    for p in positions:
        by_domain[s.question_at(p).domain].append(s.is_correct(p))
    unseen = [p for p in positions if not s.seen(p)]
    lines = [f"# Review Mode {'Set ' + str(s.set_no) if isinstance(s.set_no, int) else s.label} – AWS Certified Solutions Architect Professional (Tutorials Dojo)", "",
             f"**Kết quả:** {right}/{total} câu đúng ({right / total:.2%}) — {'✅ Đạt' if right / total >= 0.75 else '❌ Chưa đạt'}",
             "", f"**Unseen only:** {rate(s.is_correct(p) for p in unseen)} · **Mode:** review, blocks of {BLOCK} · "
             f"**Date:** {s.data['created']}", "", "## Điểm theo domain", "", "| Domain | Tỉ lệ đúng |", "|---|---|"]
    for domain in sorted(by_domain):
        lines.append(f"| CSAP – {domain} | {sum(by_domain[domain]) / len(by_domain[domain]) * 100:.2f}% |")
    lines += ["", "## Bảng tổng hợp", "", "| Câu | TD Q | Kết quả | Bạn chọn | Đáp án đúng |", "|---|---|---|---|---|"]
    for p in positions:
        q = s.question_at(p)
        mark = "✅ Đúng" if s.is_correct(p) else "❌ Sai"
        lines.append(f"| {p} | Q{q.number}{' 🔁' if s.seen(p) else ''} | {mark} | {s.data['answers'][str(p)]} | {q.answer} |")
    lines += ["", "---", ""]
    for p in positions:
        q, ok, picked = s.question_at(p), s.is_correct(p), s.data["answers"][str(p)].split(", ")
        lines += [f"## Câu {p} — {'✅ ĐÚNG' if ok else '❌ SAI'}", "", "### Câu hỏi", "", q.stem, "", "### Các phương án", ""]
        correct = q.answer.split(", ")
        for letter, text in q.options:
            tags = (" 👈 *(bạn chọn)*" if letter in picked else "") + (" ✅" if letter in correct else "")
            flat = " ".join(ln.strip() for ln in text.splitlines())  # export parser reads one line per option
            lines.append(f"- **{letter}.** {flat}{tags}")
        lines += ["", f"> **Bạn chọn:** {', '.join(picked)}  ", f"> **Đáp án đúng:** {q.answer}  ",
                  f"> **Kết quả:** {'✅ Đúng' if ok else '❌ Sai'}", "", "### Giải thích", "", q.explanation, "", "---", ""]
    out = s.export_path
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out.name}: {right}/{total}; next: test-review on this file")


def main():
    for stream in (sys.stdout, sys.stderr):  # emoji/Vietnamese output on Windows consoles
        stream.reconfigure(encoding="utf-8")
    ap =argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("init", "show", "record", "reveal", "status", "export"):
        p = sub.add_parser(name)
        p.add_argument("--set", type=lambda v: int(v) if v.isdigit() else v, required=True,
                       help="TD set number, or a named set with a {name}_source.md file")
        p.add_argument("--base", type=Path, default=Path("."), help="folder with the TD source files")
        if name == "init":
            p.add_argument("--seed", type=int, default=None)
            p.add_argument("--force", action="store_true")
            p.add_argument("--allow-reserved", action="store_true")
        if name in ("show", "reveal"):
            p.add_argument("--block", type=int, required=True)
        if name == "reveal":
            p.add_argument("--all", action="store_true", help="also print explanations of correct answers")
        if name == "record":
            p.add_argument("--answers", required=True)
    args = ap.parse_args()
    s = Session(args.set, args.base)
    {"init": cmd_init, "show": cmd_show, "record": cmd_record, "reveal": cmd_reveal,
     "status": cmd_status, "export": cmd_export}[args.cmd](s, args)


if __name__ == "__main__":
    main()
