"""Insert Vietnamese deep-dive sections (Q{n}.md fragments) into a review file.

Each fragment must start with '### 🇻🇳 Phân tích chi tiết' and use only '####' subheadings.
It is inserted inside the question's <details> block, right before '### TD explanation'.
Idempotent: re-running replaces an existing Vietnamese section.

Usage: python3 merge_vietnamese_explanations.py --review review.md --fragments /tmp/vi
"""
import argparse
import re
from pathlib import Path

HEAD = "### 🇻🇳 Phân tích chi tiết"
ANCHOR = "### TD explanation"


def merge(review: Path, fragments: Path) -> tuple:
    chunks = re.split(r'(?m)^(?=<a id="q\d+"></a>)', review.read_text(encoding="utf-8"))
    merged, missing = [], []
    for i, chunk in enumerate(chunks):
        m = re.match(r'<a id="q(\d+)"></a>', chunk)
        if not m:
            continue
        n = int(m.group(1))
        frag = fragments / f"Q{n}.md"
        if not frag.exists():
            missing.append(n)
            continue
        vi = frag.read_text(encoding="utf-8").strip()
        if not vi.startswith(HEAD):
            raise SystemExit(f"Q{n}: fragment must start with '{HEAD}'")
        if re.search(r"(?m)^#{1,2} ", vi):
            raise SystemExit(f"Q{n}: fragment contains a '#' or '##' heading (use '####')")
        if vi.count("```") % 2:
            raise SystemExit(f"Q{n}: unbalanced code fence")
        chunk = re.sub(re.escape(HEAD) + r".*?(?=^" + re.escape(ANCHOR) + ")", "", chunk, flags=re.S | re.M)
        if chunk.count(ANCHOR) != 1:
            raise SystemExit(f"Q{n}: expected exactly one '{ANCHOR}'")
        chunks[i] = chunk.replace(ANCHOR, vi + "\n\n" + ANCHOR, 1)
        merged.append(n)
    review.write_text("".join(chunks), encoding="utf-8")
    return merged, missing


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--review", required=True, type=Path)
    ap.add_argument("--fragments", required=True, type=Path, help="directory containing Q{n}.md files")
    args = ap.parse_args()
    merged, missing = merge(args.review, args.fragments)
    print(f"merged {len(merged)}; missing {missing}")


if __name__ == "__main__":
    main()
