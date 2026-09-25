"""Parse a Tutorials Dojo timed-test result export (e.g. TD_SAP_Timed_Set5_Full.md).

Expected source layout (Vietnamese labels from the TD export):
    **Kết quả:** 31/75 câu đúng (41.33%)
    | CSAP – <domain> | 27.78% |                 domain score rows
    ## Câu {n} — ✅ ĐÚNG | ❌ SAI                   one block per question
    ### Câu hỏi / ### Các phương án / > **Bạn chọn:** / > **Đáp án đúng:** / ### Giải thích
"""
import re
from dataclasses import dataclass, field
from pathlib import Path

QUESTION_SPLIT = re.compile(r"^## Câu (\d+) — (✅|❌).*$", re.M)
OPTION_LINE = re.compile(r"^- \*\*([A-G])\.\*\* (.*)$", re.M)
MARKERS = ("👈 *(bạn chọn)*", "✅")


@dataclass
class Question:
    number: int
    correct: bool
    stem: str
    options: list = field(default_factory=list)  # [(letter, text)] with answer markers stripped
    picked: str = ""
    answer: str = ""
    explanation: str = ""

    @property
    def multi_select(self) -> bool:
        return "," in self.answer


@dataclass
class TestResult:
    title: str
    score_line: str
    domains: list  # [(domain, pct)]
    questions: dict  # number -> Question

    def by_result(self, correct: bool) -> list:
        return [q for q in self.questions.values() if q.correct == correct]


def _clean(text: str) -> str:
    for marker in MARKERS:
        text = text.replace(marker, "")
    return text.strip()


def _parse_block(number: int, correct: bool, block: str) -> Question:
    if "### Các phương án" not in block or "### Giải thích" not in block:
        raise ValueError(f"Q{number}: missing options or explanation section")
    stem = block.split("### Các phương án")[0].replace("### Câu hỏi", "").strip()
    option_section = block.split("### Các phương án")[1].split("> **Bạn chọn")[0]
    options = [(k, _clean(v)) for k, v in OPTION_LINE.findall(option_section)]
    picked = re.search(r"Bạn chọn:\*\* ([A-G, ]+)", block)
    answer = re.search(r"Đáp án đúng:\*\* ([A-G, ]+)", block)
    if not (options and picked and answer):
        raise ValueError(f"Q{number}: could not parse options/picked/answer")
    explanation = block.split("### Giải thích", 1)[1].rsplit("---", 1)[0].strip()
    return Question(number, correct, stem, options, picked.group(1).strip(),
                    answer.group(1).strip(), explanation)


def parse_result(path) -> TestResult:
    text = Path(path).read_text(encoding="utf-8")
    title = text.splitlines()[0].lstrip("# ").strip()
    score = re.search(r"\*\*Kết quả:\*\* (.+)", text)
    domains = re.findall(r"^\| (CSAP – [^|]+?) \| ([\d.]+%) \|", text, re.M)
    parts = QUESTION_SPLIT.split(text)
    questions = {}
    for i in range(1, len(parts), 3):
        n = int(parts[i])
        questions[n] = _parse_block(n, parts[i + 1] == "✅", parts[i + 2])
    if not questions:
        raise ValueError(f"{path}: no '## Câu N — ✅/❌' question blocks found")
    return TestResult(title, score.group(1).strip() if score else "", domains, questions)
