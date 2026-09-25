"""Verify a review file against its TD result source. Exits non-zero on any failure.

Checks: question set matches mode, answers/picks match source, option letters match,
<details> balanced, no answer markers (✅/👈) outside answer blocks except tracker rows,
code fences balanced, at most one Vietnamese section per question.

Usage: python3 verify_test_review.py --source TD_..._Full.md --review review.md --mode wrong|right
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from td_result_parser import parse_result  # noqa: E402


def check(source: Path, review: Path, mode: str) -> list:
    result = parse_result(source)
    text = review.read_text(encoding="utf-8")
    errors = []
    expected = {q.number for q in result.by_result(correct=(mode == "right"))}
    blocks = dict((int(n), b) for n, b in re.findall(r"(?ms)^## Q(\d+)\n(.*?)(?=^<a id=|\Z)", text))
    if set(blocks) != expected:
        errors.append(f"question set mismatch: missing {sorted(expected - set(blocks))}, extra {sorted(set(blocks) - expected)}")
    for n, block in blocks.items():
        q = result.questions.get(n)
        if not q:
            continue
        head = block.split("<details>")[0]
        if re.findall(r"(?m)^- \*\*([A-G])\.\*\*", head) != [k for k, _ in q.options]:
            errors.append(f"Q{n}: option letters differ from source")
        want = (f"**Correct:** {q.answer} · **You picked:** {q.picked}" if mode == "wrong"
                else f"**Correct:** {q.answer} (you answered correctly)")
        if want not in block:
            errors.append(f"Q{n}: answer line missing or wrong ({want})")
        if block.count("### 🇻🇳 Phân tích chi tiết") > 1:
            errors.append(f"Q{n}: duplicate Vietnamese section")
    if text.count("<details>") != text.count("</details>"):
        errors.append("unbalanced <details>")
    if text.count("```") % 2:
        errors.append("unbalanced code fences")
    outside, inside = [], False
    for line in text.splitlines():
        if line.startswith("<details>"):
            inside = True
        elif line.startswith("</details>"):
            inside = False
        elif not inside and re.search("✅|👈", line) and not re.match(r"^\| [A-Z] \| \[Q\d+\]", line):
            outside.append(line[:80])
    if outside:
        errors.append(f"answer markers outside answer blocks: {outside[:3]}")
    return errors


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", required=True, type=Path)
    ap.add_argument("--review", required=True, type=Path)
    ap.add_argument("--mode", required=True, choices=["wrong", "right"])
    args = ap.parse_args()
    errors = check(args.source, args.review, args.mode)
    vi = args.review.read_text(encoding="utf-8").count("### 🇻🇳 Phân tích chi tiết")
    if errors:
        print("FAIL\n- " + "\n- ".join(errors))
        sys.exit(1)
    print(f"PASS ({args.mode}; Vietnamese sections: {vi})")


if __name__ == "__main__":
    main()
