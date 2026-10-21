"""Parse a Tutorials Dojo test result export. Two layouts are supported (Vietnamese labels).

Layout 1 — e.g. TD_SAP_Timed_Set5_Full.md, TD_SAP_Review_Set{N}_Full.md:
    **Kết quả:** 31/75 câu đúng (41.33%)
    | CSAP – <domain> | 27.78% |                 domain score rows
    ## Câu {n} — ✅ ĐÚNG | ❌ SAI                   one block per question
    ### Câu hỏi / ### Các phương án / > **Bạn chọn:** / > **Đáp án đúng:** / ### Giải thích

Layout 2 — e.g. TutorialsDojo_SAP_Timed_Mode_Set_3.md (questions grouped by domain):
    - Đúng: 42 (56.00%) | Sai/bỏ qua: 33
    ## CSAP - <domain>                           domain section heading
    ### Câu {n} (mục {k} – <domain>) — ✅ ĐÚNG | ❌ SAI · thời gian hh:mm:ss
    <stem> / - **A.** [✅|❌] [👉] text / **Đáp án đúng:** X / **Bạn chọn:** Y / **Giải thích:** ...
    Domain scores are computed from the per-question domain tags.
"""
import re
from dataclasses import dataclass, field
from pathlib import Path

QUESTION_SPLIT = re.compile(r"^## Câu (\d+) — (✅|❌).*$", re.M)
QUESTION_SPLIT_V2 = re.compile(r"^### Câu (\d+) \(mục \d+ – ([^)]+)\) — (✅|❌).*$", re.M)
OPTION_LINE = re.compile(r"^- \*\*([A-G])\.\*\* (.*)$", re.M)
MARKERS = ("👈 *(bạn chọn)*", "✅", "❌", "👉")


@dataclass
class Question:
    number: int
    correct: bool
    stem: str
    options: list = field(default_factory=list)  # [(letter, text)] with answer markers stripped
    picked: str = ""
    answer: str = ""
    explanation: str = ""
    domain: str = ""

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
    # "—" = left unanswered (e.g. time ran out in the exam page)
    picked = re.search(r"Bạn chọn:\*\* ([A-G, ]+|—)", block)
    answer = re.search(r"Đáp án đúng:\*\* ([A-G, ]+)", block)
    if not (options and picked and answer):
        raise ValueError(f"Q{number}: could not parse options/picked/answer")
    explanation = block.split("### Giải thích", 1)[1].rsplit("---", 1)[0].strip()
    return Question(number, correct, stem, options, picked.group(1).strip(),
                    answer.group(1).strip(), explanation)


def _parse_block_v2(number: int, correct: bool, domain: str, block: str) -> Question:
    if "**Giải thích:**" not in block:
        raise ValueError(f"Q{number}: missing explanation section")
    body, explanation = block.split("**Giải thích:**", 1)
    first_option = OPTION_LINE.search(body)
    if not first_option:
        raise ValueError(f"Q{number}: no options found")
    stem = body[:first_option.start()].strip()
    options = [(k, _clean(v)) for k, v in OPTION_LINE.findall(body)]
    picked = re.search(r"\*\*Bạn chọn:\*\*\s*([A-G, ]*)", body)
    answer = re.search(r"\*\*Đáp án đúng:\*\*\s*([A-G, ]+)", body)
    if not answer:
        raise ValueError(f"Q{number}: could not parse correct answer")
    # Drop the trailing separator and the next domain heading that precede the next question.
    explanation = re.sub(r"(?s)\n---\s*(\n## CSAP[^\n]*\s*)?$", "", explanation.rstrip()).strip()
    return Question(number, correct, stem, options, picked.group(1).strip() if picked else "",
                    answer.group(1).strip(), explanation, domain.strip())


def _parse_v2(text: str, path) -> TestResult:
    title = text.splitlines()[0].lstrip("# ").strip()
    parts = QUESTION_SPLIT_V2.split(text)
    questions = {}
    for i in range(1, len(parts), 4):
        n = int(parts[i])
        questions[n] = _parse_block_v2(n, parts[i + 2] == "✅", parts[i + 1], parts[i + 3])
    tally = {}
    for q in questions.values():
        right, total = tally.get(q.domain, (0, 0))
        tally[q.domain] = (right + q.correct, total + 1)
    domains = [(f"CSAP – {d}", f"{100 * r / t:.2f}%") for d, (r, t) in tally.items()]
    right = sum(q.correct for q in questions.values())
    score = f"{right}/{len(questions)} câu đúng ({100 * right / len(questions):.2f}%)"
    return TestResult(title, score, domains, questions)


def parse_result(path) -> TestResult:
    text = Path(path).read_text(encoding="utf-8")
    if QUESTION_SPLIT_V2.search(text):
        return _parse_v2(text, path)
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
