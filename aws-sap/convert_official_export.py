#!/usr/bin/env python3
"""Convert an AWS Skill Builder Official Practice Exam result export (Vietnamese layout) into the
TD timed-export layout read by .claude/skills/ai-tutor/scripts/td_result_parser.py.

Input blocks look like:
  ## Câu N — ✅ Đúng | ❌ Sai
  *Multiple Choice · Thời gian làm: 1 minutes 43 seconds*
  **Đề bài:** … **Đáp án bạn chọn:** C **Đáp án đúng:** C
  **Các lựa chọn và giải thích:**  - **A. option text** … *Giải thích:* per-option rationale

Per-option rationales are merged into one explanation (✔ marks the correct options).
Domain scores come from the companion domain-score file (optional).

Usage: python3 aws-sap/convert_official_export.py <result.md> <out.md> [--domains <domain-scores.md>]
"""
import argparse
import re
from pathlib import Path

BLOCK = re.compile(r"^## Câu (\d+) — (✅|❌)[^\n]*\n(.*?)(?=^## Câu \d+ — |\Z)", re.M | re.S)
OPTION = re.compile(r"^- \*\*([A-G])\. (.*?)\*\*[ \t]*\n(.*?)(?=^- \*\*[A-G]\. |\Z)", re.M | re.S)
DOMAIN_ROW = re.compile(r"^\| Content Domain \d: (.+?) \| (\d+) \| (\d+) \| (\d+) \|", re.M)


def convert_block(n, ok, body):
    meta = re.search(r"^\*([^*]+?) · Thời gian làm: ([^*]+)\*", body, re.M)
    stem = body.split("**Đề bài:**", 1)[1].split("**Đáp án bạn chọn:**", 1)[0].strip()
    picked = re.search(r"\*\*Đáp án bạn chọn:\*\* ([^\n]*)", body).group(1).strip() or "—"
    answer = re.search(r"\*\*Đáp án đúng:\*\* ([^\n]*)", body).group(1).strip()
    opts_part = body.split("**Các lựa chọn và giải thích:**", 1)[1].rsplit("\n---", 1)[0]
    options, expl = [], []
    for letter, text, rest in OPTION.findall(opts_part):
        options.append(f"- **{letter}.** {text.strip()}")
        why = re.search(r"\*Giải thích:\*\s*(.*)", rest, re.S)
        mark = " ✔" if letter in answer else ""
        expl.append(f"{letter}{mark}. {re.sub(r'[ \t]+\n', '\n', why.group(1).strip()) if why else ''}")
    note = f"{meta.group(1)} · {meta.group(2).strip()}" if meta else ""
    return "\n".join([f"## Câu {n} — {'✅ ĐÚNG' if ok == '✅' else '❌ SAI'}", "",
                      f"<!-- source: OFF1Q{n} · {note} -->", "", "### Câu hỏi", "", stem, "",
                      "### Các phương án", "", *options, "", f"> **Bạn chọn:** {picked}",
                      f"> **Đáp án đúng:** {answer}", "", "### Giải thích", "", "\n\n".join(expl), ""])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src"); ap.add_argument("out"); ap.add_argument("--domains")
    a = ap.parse_args()
    text = Path(a.src).read_text(encoding="utf-8")
    blocks = BLOCK.findall(text)
    right = sum(ok == "✅" for _, ok, _ in blocks)
    score = re.search(r"\*\*Điểm:\*\* (\d+)", text)
    head = [f"# AWS Official Practice Exam SAP-C02 — attempt 1 (scaled {score.group(1) if score else '?'})", "",
            f"**Kết quả:** {right}/{len(blocks)} câu đúng ({right * 100 / len(blocks):.2f}%)", ""]
    if a.domains:
        rows = DOMAIN_ROW.findall(Path(a.domains).read_text(encoding="utf-8"))
        head += ["| Domain | Score |", "|---|---|"] + [f"| CSAP – {d} | {int(c) * 100 / int(t):.2f}% |" for d, t, c, _ in rows] + [""]
    Path(a.out).write_text("\n".join(head + [convert_block(int(n), ok, b) for n, ok, b in blocks]), encoding="utf-8")
    print(f"wrote {a.out}: {len(blocks)} questions, {right} right")


if __name__ == "__main__":
    main()
