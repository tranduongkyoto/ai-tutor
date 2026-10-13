#!/usr/bin/env python3
"""Render the SAP study notes (Markdown) into self-contained HTML pages.

The .md files stay the source of truth; re-run this after editing them:
    python3 aws-sap/build_study_pages.py

Pages (same look as new-solutions-flashcards.html):
  rule-sheet.html  — searchable, "self-test" hides every answer after "→" until clicked
  weak-areas.html  — searchable, self-test hides the "Correct" column, plus a 2-option
                     confusion-pair drill (you picked vs correct) with a final summary
"""
import json
import re
from pathlib import Path

import markdown

HERE = Path(__file__).resolve().parent
PAGES = [
    ("rule-sheet.md", "rule-sheet.html", "SAP-C02 Rule Sheet", "trigger → answer, 1 page"),
    ("weak-areas.md", "weak-areas.html", "SAP-C02 Weak Areas", "ranked, with confusion pairs"),
]

CSS = """
:root{--bg:#EDF0F3;--paper:#FFF;--ink:#1B2230;--muted:#5B6676;--line:#D5DBE3;--soft:#F5F7F9;--accent:#23507A;--accent-ink:#FFF;
--good:#1E7A46;--good-bg:#E6F4EC;--bad:#B42318;--bad-bg:#FBEAE8;--tip:#FFF6D6;--tip-line:#E8B400;--mark:#FFE27A;color-scheme:light}
@media (prefers-color-scheme: dark){:root{--bg:#141922;--paper:#1C2330;--ink:#E6EAF0;--muted:#9AA5B4;--line:#2E3848;--soft:#222A38;--accent:#86B6E6;--accent-ink:#0E1620;
--good:#5CC98A;--good-bg:rgba(92,201,138,.12);--bad:#FF8A7A;--bad-bg:rgba(255,138,122,.12);--tip:rgba(255,214,90,.10);--tip-line:#C99A12;--mark:rgba(255,214,90,.32);color-scheme:dark}}
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
button,input{font:inherit;color:inherit}button{cursor:pointer}
code{background:var(--soft);padding:1px 5px;border-radius:4px;font-size:13px}
a{color:var(--accent)}
.topbar{position:sticky;top:0;z-index:5;display:flex;align-items:center;gap:12px;padding:10px 18px;background:var(--paper);border-bottom:1px solid var(--line);flex-wrap:wrap}
.brand{font-weight:700;font-size:17px;margin-right:auto}.brand small{font-weight:500;color:var(--muted);font-size:13px;margin-left:8px}
.search{border:1px solid var(--line);background:var(--soft);border-radius:8px;padding:6px 10px;width:220px}
.btn{border:1px solid var(--line);background:var(--paper);padding:7px 14px;border-radius:8px;font-size:14px;font-weight:500}
.btn:hover{border-color:var(--muted)}.btn.primary,.btn[aria-pressed=true]{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
.btn:disabled{opacity:.45;cursor:not-allowed}
.layout{display:grid;grid-template-columns:240px 1fr;gap:20px;max-width:1180px;margin:20px auto;padding:0 16px}
.toc{position:sticky;top:70px;align-self:start;background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:12px 14px;font-size:13.5px}
.toc a{display:block;padding:3px 0;text-decoration:none;color:var(--ink)}.toc a:hover{color:var(--accent)}
.doc,.card{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:20px 26px;min-width:0}
.doc h1{font-size:22px;margin:0 0 6px}.doc h2{font-size:18px;margin:26px 0 8px;padding-top:12px;border-top:1px solid var(--line)}
.doc li{margin:4px 0}.doc table{border-collapse:collapse;width:100%;font-size:14px;margin:8px 0;display:block;overflow-x:auto}
.doc th,.doc td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top}.doc th{background:var(--soft)}
.hidden{display:none!important}
mark{background:var(--mark);color:inherit;border-radius:3px}
body.selftest .ans{filter:blur(5px);cursor:pointer;user-select:none;transition:filter .15s}
body.selftest .ans.shown{filter:none}
.muted{color:var(--muted);font-size:13.5px}
.q{font-size:17px;font-weight:600;margin:6px 0 16px}
.opt{display:flex;gap:12px;width:100%;text-align:left;border:1.5px solid var(--line);background:var(--paper);border-radius:10px;padding:12px 14px;margin-bottom:10px}
.opt:hover:not(:disabled){border-color:var(--accent)}.opt b{flex:none;width:26px;height:26px;border-radius:50%;background:var(--soft);display:grid;place-items:center;font-size:13px}
.opt.ok{border-color:var(--good);background:var(--good-bg)}.opt.no{border-color:var(--bad);background:var(--bad-bg)}.opt:disabled{cursor:default}
.fb{border-left:4px solid var(--tip-line);background:var(--tip);border-radius:6px;padding:10px 14px;margin-top:6px}
.bar{height:6px;background:var(--soft);border-radius:999px;overflow:hidden;margin:6px 0 14px}.bar i{display:block;height:100%;background:var(--accent)}
.big{font-size:40px;font-weight:800}.good{color:var(--good)}.badc{color:var(--bad)}
.row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
@media (max-width:820px){.layout{grid-template-columns:1fr}.toc{position:static}}
"""

# Shared page behaviour: TOC, search filter, self-test blur. Drill code is appended for weak-areas.
JS_COMMON = r"""
const doc = document.getElementById("doc");
const toc = document.getElementById("toc");
doc.querySelectorAll("h2").forEach((h, i) => { h.id = "s" + i; toc.insertAdjacentHTML("beforeend", `<a href="#s${i}">${h.textContent}</a>`); });
// Search: hide list items / table rows that don't match; highlight matches.
const items = [...doc.querySelectorAll("li, tbody tr, p")];
items.forEach(el => el.dataset.html = el.innerHTML);
document.getElementById("q").addEventListener("input", e => {
  const t = e.target.value.trim().toLowerCase();
  const re = t ? new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "gi") : null;
  items.forEach(el => {
    el.innerHTML = el.dataset.html;
    if (!t) { el.classList.remove("hidden"); return; }
    const hit = el.textContent.toLowerCase().includes(t);
    el.classList.toggle("hidden", !hit);
    if (hit) el.querySelectorAll("*").length || (el.innerHTML = el.innerHTML.replace(re, "<mark>$1</mark>"));
  });
});
// Self-test: blur answers; click one to reveal it.
const st = document.getElementById("selftest");
st.onclick = () => { const on = document.body.classList.toggle("selftest"); st.setAttribute("aria-pressed", on);
  doc.querySelectorAll(".ans.shown").forEach(a => a.classList.remove("shown")); };
doc.addEventListener("click", e => { const a = e.target.closest(".ans"); if (a) a.classList.toggle("shown"); });
"""

# 2-option drill over the confusion pairs; one card at a time, feedback, final summary.
JS_DRILL = r"""
const PAIRS = __PAIRS__;
const drillBtn = document.getElementById("drill");
const view = document.getElementById("view");
const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
let run = null;
drillBtn.onclick = () => run ? stop() : startDrill(PAIRS);
function stop() { run = null; drillBtn.textContent = "Pair drill"; view.innerHTML = ""; document.getElementById("main").classList.remove("hidden"); }
function startDrill(deck) {
  run = { deck: shuffle(deck), i: 0, miss: [], secs: {} };
  drillBtn.textContent = "Exit drill";
  document.getElementById("main").classList.add("hidden");
  card();
}
function card() {
  const p = run.deck[run.i];
  run.order = Math.random() < .5 ? [p.ok, p.bad] : [p.bad, p.ok];
  run.done = false;
  view.innerHTML = `<div class="card"><div class="muted">Pair ${run.i + 1} / ${run.deck.length} · ${p.sec}</div>
    <div class="bar"><i style="width:${run.i * 100 / run.deck.length}%"></i></div>
    <div class="q">Which one is correct?</div>
    ${run.order.map((t, k) => `<button class="opt" data-k="${k}"><b>${"AB"[k]}</b><span>${t}</span></button>`).join("")}
    <div id="fb"></div></div><p class="muted">Keys: <code>A</code>/<code>B</code>, <code>Enter</code> for next.</p>`;
  view.querySelectorAll(".opt").forEach(b => b.onclick = () => pick(+b.dataset.k));
}
function pick(k) {
  if (run.done) return; run.done = true;
  const p = run.deck[run.i], good = run.order[k] === p.ok;
  const s = run.secs[p.sec] = run.secs[p.sec] || [0, 0]; s[1]++; if (good) s[0]++; else run.miss.push(p);
  view.querySelectorAll(".opt").forEach((b, j) => { b.disabled = true; if (run.order[j] === p.ok) b.classList.add("ok"); else if (j === k) b.classList.add("no"); });
  document.getElementById("fb").innerHTML = `<div class="fb"><b class="${good ? "good" : "badc"}">${good ? "✅ Correct" : "❌ Trap"}</b>${p.tell ? " — Tell: " + p.tell : ""}</div>
    <div class="row" style="margin-top:12px"><button class="btn primary" id="nx">${run.i === run.deck.length - 1 ? "See summary" : "Next →"}</button></div>`;
  document.getElementById("nx").onclick = next;
}
function next() { if (!run || !run.done) return; if (++run.i < run.deck.length) card(); else summary(); }
function summary() {
  const n = run.deck.length, ok = n - run.miss.length, pc = Math.round(ok * 100 / n), miss = run.miss;
  view.innerHTML = `<div class="card"><div class="big ${pc >= 80 ? "good" : "badc"}">${ok} / ${n} <small style="font-size:20px">(${pc}%)</small></div>
    <table style="width:100%;margin:10px 0">${Object.entries(run.secs).map(([s, [a, b]]) => `<tr><td>${s}</td><td>${a}/${b}</td></tr>`).join("")}</table>
    <div class="row"><button class="btn primary" id="rm" ${miss.length ? "" : "disabled"}>Retry ${miss.length} missed</button><button class="btn" id="ag">New drill</button><button class="btn" id="ex">Back to notes</button></div></div>
    <div class="card" style="margin-top:16px"><h3 style="margin-top:0">Missed pairs</h3>${miss.map(p => `<p><span class="good">✓ ${p.ok}</span><br><span class="badc">✗ ${p.bad}</span>${p.tell ? `<br><span class="muted">Tell: ${p.tell}</span>` : ""}</p>`).join("") || '<p class="good">None — clean run.</p>'}</div>`;
  document.getElementById("rm").onclick = () => startDrill(miss);
  document.getElementById("ag").onclick = () => startDrill(PAIRS);
  document.getElementById("ex").onclick = stop;
}
document.addEventListener("keydown", e => {
  if (!run || e.target.tagName === "INPUT" || (e.target.tagName === "BUTTON" && e.key === "Enter")) return;
  const k = e.key.toLowerCase();
  if (k === "a" || k === "1") pick(0); else if (k === "b" || k === "2") pick(1); else if (k === "enter") next();
});
"""

ANSWER_IN_LI = re.compile(r"→(.*?)(?=\s·\s|</li>|<ul>|$)", re.S)


def mark_rule_answers(html: str) -> str:
    """Wrap each '→ answer' fragment inside list items so self-test can blur it."""
    def per_li(m):
        return ANSWER_IN_LI.sub(lambda a: f'→<span class="ans">{a.group(1)}</span>', m.group(0))
    return re.sub(r"<li>.*?</li>", per_li, html, flags=re.S)


def mark_correct_column(html: str):
    """In 'You picked | Correct | Tell' tables, blur the Correct cell and collect drill pairs."""
    pairs = []
    sec = ""
    out = []
    for part in re.split(r"(<h2>.*?</h2>|<table>.*?</table>)", html, flags=re.S):
        if part.startswith("<h2>"):
            sec = re.sub(r"<.*?>", "", part).split("—")[0].strip()
        elif part.startswith("<table>") and re.search(r"<th>You picked</th>\s*<th>Correct</th>", part):
            def row(m):
                cells = re.findall(r"<td>(.*?)</td>", m.group(0), re.S)
                if len(cells) >= 2:
                    pairs.append({"sec": sec, "bad": cells[0], "ok": cells[1], "tell": cells[2] if len(cells) > 2 else ""})
                return re.sub(r"(<tr>\s*<td>.*?</td>\s*<td>)(.*?)(</td>)", r'\1<span class="ans">\2</span>\3', m.group(0), count=1, flags=re.S)
            part = re.sub(r"<tr>\s*<td>.*?</tr>", row, part, flags=re.S)
        out.append(part)
    return "".join(out), pairs


def build(src: str, dst: str, title: str, sub: str) -> int:
    md_text = (HERE / src).read_text(encoding="utf-8")
    body = markdown.markdown(md_text, extensions=["tables"])
    js, extra_btn, count = JS_COMMON, "", 0
    if src == "rule-sheet.md":
        # Section 0 holds reading meta-rules (prose), so only blur the service rules from section 1 on.
        head, sep, rest = body.partition("<h2>1.")
        body = head + sep + mark_rule_answers(rest)
        count = body.count('class="ans"')
    else:
        body, pairs = mark_correct_column(body)
        count = len(pairs)
        js += JS_DRILL.replace("__PAIRS__", json.dumps(pairs, ensure_ascii=False))
        extra_btn = '<button class="btn" id="drill">Pair drill</button>'
    page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><style>{CSS}</style></head>
<body>
<!-- Generated by build_study_pages.py from {src}. Edit the .md, then re-run the script. -->
<div class="topbar"><div class="brand">{title}<small>{sub}</small></div>
<input class="search" id="q" placeholder="Search… (e.g. SCP, Kinesis)">
<button class="btn" id="selftest" aria-pressed="false">Self-test</button>{extra_btn}</div>
<div id="view" style="max-width:820px;margin:20px auto;padding:0 16px"></div>
<div class="layout" id="main"><nav class="toc" id="toc"><b>Sections</b></nav><article class="doc" id="doc">{body}</article></div>
<script>{js}</script>
</body></html>
"""
    (HERE / dst).write_text(page, encoding="utf-8")
    return count


if __name__ == "__main__":
    for src, dst, title, sub in PAGES:
        n = build(src, dst, title, sub)
        print(f"{dst}: {n} {'answers' if src == 'rule-sheet.md' else 'confusion pairs'}")
