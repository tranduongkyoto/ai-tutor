#!/usr/bin/env python3
"""Build a self-contained timed exam page (HTML) from an exam-set JSON.

Exam-set JSON:
  {"title": "...", "store": "localStorage-key-prefix", "minutes": 210,
   "questions": [{"id": "T1Q5", "type": "Single Choice|Select Multiple", "stem": "...",
                  "opts": [["A", "..."], ...], "correct": ["B"], "expl": "...",
                  "domain": "ORG|NEW|CI|MIG", "note": "optional ⚠️ audit note shown after submit"}]}

Page features: countdown timer, pause, flag for review, question navigator, keyboard shortcuts,
state saved in localStorage (refresh-safe; reload resumes paused), auto-submit at time-up,
results by domain/thirds, per-question review, attempt history, and a Markdown export in the
TD layout used by .claude/skills/ai-tutor/scripts/build_test_review.py.

Usage: python3 aws-sap/build_exam_page.py --set practice-exam/sap/neal/neal_exam_A.json --out aws-sap/neal-exam-A.html
"""
import argparse
import base64
import json
from pathlib import Path

DOMAINS = {
    "ORG": "CSAP – Design Solutions for Organizational Complexity",
    "NEW": "CSAP – Design for New Solutions",
    "CI": "CSAP – Continuous Improvement for Existing Solutions",
    "MIG": "CSAP – Accelerate Workload Migration and Modernization",
}

PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
:root{--bg:#EDF0F3;--paper:#FFF;--ink:#1B2230;--muted:#5B6676;--line:#D5DBE3;--soft:#F5F7F9;--accent:#23507A;--accent-ink:#FFF;
 --good:#1E7A46;--good-bg:#E6F4EC;--bad:#B42318;--bad-bg:#FBEAE8;--flag:#C27803;--flag-bg:#FFF4D6;color-scheme:light}
@media (prefers-color-scheme:dark){:root{--bg:#141922;--paper:#1C2330;--ink:#E6EAF0;--muted:#9AA5B4;--line:#2E3848;--soft:#222A38;
 --accent:#86B6E6;--accent-ink:#0E1620;--good:#5CC98A;--good-bg:rgba(92,201,138,.12);--bad:#FF8A7A;--bad-bg:rgba(255,138,122,.12);
 --flag:#F2B84B;--flag-bg:rgba(242,184,75,.12);color-scheme:dark}}
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
button{font:inherit;color:inherit;cursor:pointer}
.topbar{position:sticky;top:0;z-index:5;display:flex;align-items:center;gap:12px;padding:10px 18px;background:var(--paper);border-bottom:1px solid var(--line);flex-wrap:wrap}
.brand{font-weight:700;font-size:16px;margin-right:auto}
.timer{font:600 18px ui-monospace,monospace;padding:4px 10px;border-radius:8px;background:var(--soft)}
.timer.low{color:var(--bad)}
/* Per-question clock: big and always visible in the sticky bar; ring fills to the 2:30 pace target. */
.qclock{display:flex;align-items:center;gap:10px;padding:4px 14px 4px 6px;border-radius:12px;background:var(--soft);border:2px solid var(--line)}
.qclock .ring{width:38px;height:38px;border-radius:50%;background:conic-gradient(var(--qc,var(--good)) var(--p,0%),var(--line) 0)}
.qclock .ring::after{content:"";display:block;width:26px;height:26px;margin:6px;border-radius:50%;background:var(--soft)}
.qclock small{display:block;font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em;line-height:1.1}
.qclock b{display:block;font:800 28px/1.05 ui-monospace,monospace;color:var(--qc,var(--ink))}
.qclock.warn{border-color:var(--flag);--qc:var(--flag)} .qclock.over{border-color:var(--bad);--qc:var(--bad);animation:qpulse 1s ease-in-out infinite alternate}
@keyframes qpulse{to{background:var(--bad-bg)}}
.wrap{max-width:900px;margin:20px auto;padding:0 16px}
.card{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:20px 22px;margin-bottom:14px}
.btn{border:1px solid var(--line);background:var(--paper);padding:7px 14px;border-radius:8px;font-size:14px;font-weight:500}
.btn:hover{border-color:var(--muted)}
.btn.primary{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
.btn.flagged{background:var(--flag-bg);border-color:var(--flag);color:var(--flag)}
.row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.muted{color:var(--muted);font-size:13.5px}
.stem{white-space:pre-wrap;margin:6px 0 14px}
.pick{font-size:13px;font-weight:600;color:var(--accent)}
.opt{display:flex;gap:12px;width:100%;text-align:left;border:1.5px solid var(--line);background:var(--paper);border-radius:10px;padding:10px 12px;margin-bottom:8px}
.opt:hover{border-color:var(--accent)}
.opt b{flex:none;width:26px;height:26px;border-radius:50%;background:var(--soft);display:grid;place-items:center;font-size:13px}
.opt.sel{border-color:var(--accent);background:var(--soft)} .opt.sel b{background:var(--accent);color:var(--accent-ink)}
.opt.ok{border-color:var(--good);background:var(--good-bg)} .opt.no{border-color:var(--bad);background:var(--bad-bg)}
.nav{display:grid;grid-template-columns:repeat(auto-fill,minmax(38px,1fr));gap:6px}
.nav button{position:relative;border:1.5px solid var(--line);background:var(--paper);border-radius:6px;padding:4px 0;font-size:13px;color:var(--muted)}
/* answered = solid accent fill + ✓ corner; flagged = thick amber border; current = outer ring (states combine) */
.nav .ans{background:var(--accent);border-color:var(--accent);color:var(--accent-ink);font-weight:700}
.nav .ans::after{content:"✓";position:absolute;top:-2px;right:3px;font-size:10px}
.nav .flg{border:2.5px solid var(--flag)} .nav .flg:not(.ans){color:var(--flag);background:var(--flag-bg)}
.nav .cur{outline:2px solid var(--ink);outline-offset:2px}
.legend{display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin:10px 0 0;font-size:13px;color:var(--muted)}
.legend i{display:inline-block;width:18px;height:14px;border-radius:4px;vertical-align:-2px;margin-right:5px;border:1.5px solid var(--line);background:var(--paper)}
.nav .ok{background:var(--good-bg);border-color:var(--good)} .nav .no{background:var(--bad-bg);border-color:var(--bad)}
.overlay{position:fixed;inset:0;background:var(--bg);display:grid;place-items:center;z-index:10}
table{border-collapse:collapse;width:100%;font-size:14px} th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line)}
.big{font-size:40px;font-weight:800;line-height:1.1}
.good{color:var(--good)} .badc{color:var(--bad)}
.expl{white-space:pre-wrap;font-size:14px;border-left:4px solid var(--line);padding:6px 12px;margin-top:8px}
.note{border-left:4px solid var(--flag);background:var(--flag-bg);padding:6px 12px;margin-top:8px;font-size:14px}
details summary{cursor:pointer;color:var(--accent);font-size:14px}
/* keyword aids: kw = constraint word, kn = negation/scope word, mark.u = user highlight, .opt.x = struck-out option */
.kw{background:rgba(242,184,75,.32);border-radius:3px;padding:0 1px;font-weight:600}
.kn{color:var(--bad);font-weight:700;text-decoration:underline}
mark.u{background:#9be7a8;color:#111;border-radius:3px;cursor:pointer}
.opt.x span{text-decoration:line-through;opacity:.45}
.opt .xb{flex:none;margin-left:auto;padding:0 6px;border-radius:6px;color:var(--muted);font-size:13px}
.opt .xb:hover{background:var(--bad-bg);color:var(--bad)}
.btn.on{background:var(--flag-bg);border-color:var(--flag)}
</style>
</head>
<body>
<div class="topbar">
  <div class="brand">__TITLE__</div>
  <span class="qclock" id="qclock" hidden><span class="ring"></span><span><small>This question · Q<span id="qnum">1</span></small><b id="qtime">0:00</b></span></span>
  <span class="timer" id="timer" hidden></span>
  <button class="btn" id="pauseBtn" hidden>Pause</button>
  <button class="btn" id="homeBtn">Home</button>
</div>
<div class="wrap" id="app"></div>
<script>
/* Question data is base64-encoded so answers are not readable in the page source by accident. */
const DATA = JSON.parse(new TextDecoder().decode(Uint8Array.from(atob("__DATA__"), c => c.charCodeAt(0))));
const QS = DATA.questions, MINUTES = DATA.minutes, DOMAINS = DATA.domains;
const SKEY = DATA.store + "-state", HKEY = DATA.store + "-history";
const app = document.getElementById("app"), timerEl = document.getElementById("timer"), pauseBtn = document.getElementById("pauseBtn");
let S = null, tick = null;

const load = (k, d) => JSON.parse(localStorage.getItem(k) || JSON.stringify(d));
const save = () => { if (S) localStorage.setItem(SKEY, JSON.stringify(S)); };
const pct = (a, b) => b ? Math.round(a * 100 / b) : 0;
const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const fmt = ms => { const s = Math.max(0, Math.round(ms / 1000)); return `${Math.floor(s / 3600)}:${String(Math.floor(s / 60) % 60).padStart(2, "0")}:${String(s % 60).padStart(2, "0")}`; };
const usedMs = () => S.elapsed + (S.running ? Date.now() - S.resumedAt : 0);
const leftMs = () => MINUTES * 60000 - usedMs();
const sameSet = (a, b) => a.length === b.length && a.every(x => b.includes(x));

/* Keyword aids. Constraint words decide between two working options; negation/scope words flip or narrow the ask.
   Auto-highlight is a practice aid, off by default (toggle K, saved per browser) — the real exam has no auto-highlight. */
const KW_CONSTRAINT = ["least operational overhead", "operational overhead", "operationally efficient", "most cost-effective", "cost-effective",
  "lowest cost", "least expensive", "minimal changes", "minimal code changes", "no code changes", "without code changes", "least amount of effort",
  "least effort", "least development effort", "quickest", "fastest", "as quickly as possible", "urgent", "urgently", "highly available",
  "high availability", "fault tolerant", "fault-tolerant", "most secure", "securely", "lowest latency", "low latency", "least latency",
  "real time", "real-time", "near real time", "near-real-time", "serverless", "fully managed", "managed service", "automatically", "automated",
  "automate", "scalable", "durable", "RPO", "RTO", "compliance", "prevent", "enforce", "block", "detect", "audit", "centrally", "centralized",
  "MOST", "LEAST", "BEST", "minimize", "reduce", "maximize", "optimize"];
const KW_NEGATION = ["NOT", "EXCEPT", "without", "must not", "should not", "cannot", "can't", "only", "existing", "current",
  "across accounts", "across multiple accounts", "cross-account", "within the Region", "multiple Regions", "another Region", "on-premises"];
const rx = w => w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const kwRe = list => new RegExp(`\\b(${[...list].sort((a, b) => b.length - a.length).map(rx).join("|")})\\b`, "g");
/* Upper-case-only words (NOT, MOST…) match case-sensitively; the rest ignore case. */
const caseful = l => l.filter(w => w === w.toUpperCase()), caseless = l => l.filter(w => w !== w.toUpperCase());
const KW_RES = [[kwRe(caseful(KW_NEGATION)), "kn"], [new RegExp(kwRe(caseless(KW_NEGATION)).source, "gi"), "kn"],
  [kwRe(caseful(KW_CONSTRAINT)), "kw"], [new RegExp(kwRe(caseless(KW_CONSTRAINT)).source, "gi"), "kw"]];
const PREF = "sap-exam-prefs";
const prefs = () => load(PREF, { autoKw: false });
/* Apply a regex only to text outside HTML tags and outside spans already inserted. */
function wrapOutsideTags(html, re, cls) {
  let depth = 0;
  return html.split(/(<[^>]+>)/).map(part => {
    if (part.startsWith("<")) { if (/^<span/.test(part)) depth++; else if (/^<\/span/.test(part)) depth--; return part; }
    return depth ? part : part.replace(re, m => `<span class="${cls}">${m}</span>`);
  }).join("");
}
/* Escape → user highlights (mark.u) → keyword spans. */
function decorate(text, qid) {
  let h = esc(text);
  for (const ph of ((S && S.hl && S.hl[qid]) || [])) {
    const e = esc(ph);
    h = h.split(e).join(`<mark class="u" data-ph="${encodeURIComponent(ph)}">${e}</mark>`);
  }
  if (prefs().autoKw) for (const [re, cls] of KW_RES) h = wrapOutsideTags(h, re, cls);
  return h;
}
/* Highlight the current text selection (stem or option) for the current question. */
function highlightSelection() {
  const sel = window.getSelection(), ph = sel ? sel.toString().trim() : "";
  if (ph.length < 2 || !sel.anchorNode || !app.contains(sel.anchorNode)) return;
  const id = QS[S.idx].id;
  S.hl = S.hl || {};
  S.hl[id] = [...new Set([...(S.hl[id] || []), ph])];
  sel.removeAllRanges(); save(); show();
}
function toggleStrike(l) {
  const id = QS[S.idx].id; S.strike = S.strike || {};
  const cur = S.strike[id] || [];
  S.strike[id] = cur.includes(l) ? cur.filter(x => x !== l) : [...cur, l];
  save(); show();
}

/* Home: start / resume / history. */
function home() {
  stopTick(); timerEl.hidden = pauseBtn.hidden = document.getElementById("qclock").hidden = true;
  S = load(SKEY, null);
  const hist = load(HKEY, []);
  const multi = QS.filter(q => q.correct.length > 1).length;
  app.innerHTML = `
  <div class="card">
    <h2 style="margin:0 0 4px">${esc(DATA.title)}</h2>
    <p class="muted">${QS.length} questions (${multi} multi-select) · ${MINUTES} minutes · multi-select is all-or-nothing.
    Progress is saved in this browser; a refresh resumes paused. Keys: <code>1–6</code> pick · <code>N</code>/<code>P</code> next/prev · <code>F</code> flag · <code>H</code> highlight selection · <code>K</code> keywords on/off · <code>Space</code> pause. ✕ strikes out an option.</p>
    <div class="row">${S ? `<button class="btn primary" id="go">Resume (${Object.keys(S.answers).length}/${QS.length} answered, ${fmt(leftMs())} left)</button>
      <button class="btn" id="reset">Discard this attempt</button>` : `<button class="btn primary" id="go">Start exam</button>`}</div>
  </div>
  <div class="card"><h3 style="margin-top:0">Attempt history</h3>${hist.length ? `<table><tr><th>#</th><th>Date</th><th>Score</th><th>Time used</th><th>By domain</th></tr>${
    hist.map((h, i) => `<tr><td>${i + 1}</td><td>${h.date}</td><td>${h.score}/${h.total} (${pct(h.score, h.total)}%)</td><td>${h.used}</td><td class="muted">${h.domains}</td></tr>`).join("")}</table>` : `<p class="muted">No attempts yet.</p>`}</div>`;
  document.getElementById("go").onclick = () => {
    if (!S) S = { answers: {}, flags: [], idx: 0, elapsed: 0, running: false, resumedAt: 0, started: new Date().toISOString() };
    resume();
  };
  const r = document.getElementById("reset");
  if (r) r.onclick = () => { if (confirm("Discard the current attempt? Answers and time will be lost.")) { localStorage.removeItem(SKEY); home(); } };
}

function resume() { S.running = true; S.resumedAt = Date.now(); save(); startTick(); show(); }
function pause() {
  if (!S || !S.running) return;
  S.elapsed = usedMs(); S.running = false; save(); stopTick(); renderTimer();
  const o = document.createElement("div"); o.className = "overlay";
  o.innerHTML = `<div class="card" style="text-align:center"><h2 style="margin-top:0">Paused</h2><p class="muted">${fmt(leftMs())} left · question hidden</p>
    <button class="btn primary" id="unpause">Resume</button></div>`;
  document.body.appendChild(o);
  document.getElementById("unpause").onclick = () => { o.remove(); resume(); };
}
function startTick() { stopTick(); timerEl.hidden = pauseBtn.hidden = false; tick = setInterval(() => { renderTimer(); if (leftMs() <= 0) submit(true); else if (Date.now() % 5000 < 1000) save(); }, 1000); renderTimer(); }
function stopTick() { if (tick) clearInterval(tick); tick = null; }
function renderTimer() {
  if (!S) return; const l = leftMs(); timerEl.textContent = fmt(l); timerEl.classList.toggle("low", l < 15 * 60000);
  /* Live per-question clock: amber past 2:30 (pace target), red past 3:00. */
  const qc = document.getElementById("qclock");
  qc.hidden = timerEl.hidden;
  if (!qc.hidden) {
    const d = liveDwell();
    document.getElementById("qtime").textContent = mmss(d);
    document.getElementById("qnum").textContent = S.idx + 1;
    qc.style.setProperty("--p", Math.min(100, d / 1500) + "%");  /* 150000 ms = 100% */
    qc.classList.toggle("warn", d > 150000 && d <= 180000); qc.classList.toggle("over", d > 180000);
  }
}

/* Timing log (exam clock, so paused time is excluded):
   S.t[id] = {dwell, visits, first, last, changes} · S.log = [{id, i, at, picks}] for every answer change. */
function noteDwell() {
  S.t = S.t || {}; S.log = S.log || [];
  const now = usedMs();
  if (S.viewId) { const t = S.t[S.viewId] || (S.t[S.viewId] = { dwell: 0, visits: 0, first: null, last: null, changes: 0 }); t.dwell += Math.max(0, now - (S.viewStart ?? now)); }
  S.viewStart = now;
}
function enterQuestion(id) {
  noteDwell();
  if (S.viewId !== id) { const t = S.t[id] || (S.t[id] = { dwell: 0, visits: 0, first: null, last: null, changes: 0 }); t.visits++; S.viewId = id; }
}
/* Time on the current question including the still-open visit. */
const liveDwell = () => { const t = S && S.t && S.viewId ? S.t[S.viewId] : null; return t ? t.dwell + Math.max(0, usedMs() - (S.viewStart ?? usedMs())) : 0; };
const mmss = ms => { if (ms == null) return "—"; const s = Math.floor(ms / 1000); return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`; };

/* One question + navigator. */
function show() {
  enterQuestion(QS[S.idx].id);
  setTimeout(renderTimer);
  const q = QS[S.idx], picked = S.answers[q.id] || [], flagged = S.flags.includes(q.id);
  const n = q.correct.length;
  const answered = Object.keys(S.answers).filter(k => S.answers[k].length).length;
  app.innerHTML = `
  <div class="card">
    <div class="row muted" style="justify-content:space-between"><span>Question ${S.idx + 1} / ${QS.length}</span><span>${answered} answered · ${S.flags.length} flagged</span></div>
    ${n > 1 ? `<div class="pick">Select ${["", "ONE", "TWO", "THREE", "FOUR"][n]}.</div>` : ""}
    <div class="row" style="margin:4px 0 2px">
      <button class="btn" id="hlBtn" title="Select text, then press H">🖍 Highlight selection (H)</button>
      <button class="btn ${prefs().autoKw ? "on" : ""}" id="kwBtn" title="Auto-highlight constraint / negation words">🔑 Keywords ${prefs().autoKw ? "on" : "off"} (K)</button>
      ${(S.hl && (S.hl[q.id] || []).length) ? `<button class="btn" id="hlClear">Clear highlights</button>` : ""}
      <span class="muted">click a green highlight to remove · ✕ strikes out an option</span>
    </div>
    <div class="stem">${decorate(q.stem, q.id)}</div>
    ${q.opts.map(([l, t], k) => `<button class="opt ${picked.includes(l) ? "sel" : ""} ${((S.strike || {})[q.id] || []).includes(l) ? "x" : ""}" data-l="${l}"><b>${l}</b><span>${decorate(t, q.id)}</span><span class="xb" data-x="${l}" title="Strike out">✕</span></button>`).join("")}
    <div class="row" style="margin-top:12px">
      <button class="btn" id="prev" ${S.idx ? "" : "disabled"}>← Prev</button>
      <button class="btn ${flagged ? "flagged" : ""}" id="flag">${flagged ? "⚑ Flagged" : "⚐ Flag for review"}</button>
      <button class="btn" id="next" ${S.idx < QS.length - 1 ? "" : "disabled"}>Next →</button>
      <span style="margin-left:auto"></span>
      <button class="btn primary" id="submit">Submit exam</button>
    </div>
  </div>
  <div class="card"><div class="nav">${QS.map((x, i) => `<button data-i="${i}" class="${(S.answers[x.id] || []).length ? "ans" : ""} ${S.flags.includes(x.id) ? "flg" : ""} ${i === S.idx ? "cur" : ""}">${S.flags.includes(x.id) ? "⚑" : ""}${i + 1}</button>`).join("")}</div>
    <div class="legend"><span><i style="background:var(--accent);border-color:var(--accent)"></i>Answered ✓</span>
      <span><i></i>Not answered</span><span><i style="border:2.5px solid var(--flag)"></i>⚑ Flagged</span>
      <span><i style="outline:2px solid var(--ink);outline-offset:1px"></i>Current</span>
      <span style="margin-left:auto">${answered}/${QS.length} answered · ${QS.length - answered} left</span></div></div>`;
  app.querySelectorAll(".opt").forEach(b => b.onclick = e => {
    const x = e.target.closest(".xb"), m = e.target.closest("mark.u");
    if (x) return toggleStrike(x.dataset.x);
    if (m) return removeHl(m.dataset.ph);
    if (String(window.getSelection())) return;  /* selecting text to highlight should not pick the option */
    choose(b.dataset.l);
  });
  app.querySelectorAll(".stem mark.u").forEach(m => m.onclick = () => removeHl(m.dataset.ph));
  document.getElementById("hlBtn").onmousedown = e => e.preventDefault();  /* keep the selection alive */
  document.getElementById("hlBtn").onclick = highlightSelection;
  document.getElementById("kwBtn").onclick = toggleKw;
  const hc = document.getElementById("hlClear"); if (hc) hc.onclick = () => { delete S.hl[q.id]; save(); show(); };
  app.querySelectorAll(".nav button").forEach(b => b.onclick = () => go(+b.dataset.i));
  document.getElementById("prev").onclick = () => go(S.idx - 1);
  document.getElementById("next").onclick = () => go(S.idx + 1);
  document.getElementById("flag").onclick = toggleFlag;
  document.getElementById("submit").onclick = () => submit(false);
}
function go(i) { if (i < 0 || i >= QS.length) return; S.idx = i; save(); show(); window.scrollTo(0, 0); }
function choose(l) {
  const q = QS[S.idx], n = q.correct.length;
  let p = S.answers[q.id] || [];
  if (n === 1) p = [l];
  else if (p.includes(l)) p = p.filter(x => x !== l);
  else if (p.length < n) p = [...p, l];
  else return alert(`Select ${n} options — unselect one first.`);
  S.answers[q.id] = p.sort();
  const t = S.t[q.id], at = usedMs();
  if (t.first == null) t.first = at; else t.changes++;
  t.last = at; S.log.push({ id: q.id, i: S.idx, at, picks: S.answers[q.id].join("") });
  save(); show();
}
function removeHl(enc) { const id = QS[S.idx].id, ph = decodeURIComponent(enc); S.hl[id] = (S.hl[id] || []).filter(x => x !== ph); save(); show(); }
function toggleKw() { const p = prefs(); p.autoKw = !p.autoKw; localStorage.setItem(PREF, JSON.stringify(p)); show(); }
function toggleFlag() { const id = QS[S.idx].id; S.flags = S.flags.includes(id) ? S.flags.filter(x => x !== id) : [...S.flags, id]; save(); show(); }

/* Submit: score, save history, show results. */
function submit(timeUp) {
  const unanswered = QS.filter(q => !(S.answers[q.id] || []).length).length;
  if (!timeUp && !confirm(`Submit now? ${unanswered} unanswered, ${S.flags.length} flagged.`)) return;
  noteDwell();
  S.elapsed = usedMs(); S.running = false; stopTick(); timerEl.hidden = pauseBtn.hidden = document.getElementById("qclock").hidden = true;
  const T = S.t || {}, LOG = S.log || [];
  const res = QS.map((q, i) => ({ q, i, mine: S.answers[q.id] || [], ok: sameSet(S.answers[q.id] || [], q.correct), flag: S.flags.includes(q.id),
    t: T[q.id] || { dwell: 0, visits: 0, first: null, last: null, changes: 0 } }));
  res.log = LOG;
  const score = res.filter(r => r.ok).length;
  const dom = Object.keys(DOMAINS).map(d => { const a = res.filter(r => r.q.domain === d); return [d, a.filter(r => r.ok).length, a.length]; }).filter(x => x[2]);
  const hist = load(HKEY, []);
  const attempt = { date: new Date().toISOString().slice(0, 16).replace("T", " "), score, total: QS.length, used: fmt(S.elapsed),
    domains: dom.map(([d, o, t]) => `${d} ${o}/${t}`).join(" · "), timeUp, timing: timingSummary(res) };
  hist.push(attempt); localStorage.setItem(HKEY, JSON.stringify(hist));
  const md = exportMd(res, score, dom, attempt);
  localStorage.removeItem(SKEY);
  results(res, score, dom, attempt, md);
  S = null;
}

/* Timing summary: averages by type/result, answered-count milestones, slowest questions, answer order. */
function timingSummary(res) {
  const avg = a => a.length ? a.reduce((x, r) => x + r.t.dwell, 0) / a.length : null;
  const firsts = res.filter(r => r.t.first != null).map(r => r.t.first).sort((a, b) => a - b);
  const mile = n => firsts.length >= n ? mmss(firsts[n - 1]) : "—";
  const single = res.filter(r => r.q.correct.length === 1), multi = res.filter(r => r.q.correct.length > 1);
  const order = [...res].filter(r => r.t.first != null).sort((a, b) => a.t.first - b.t.first).map(r => r.i + 1);
  return {
    avgAll: mmss(avg(res)), avgSingle: mmss(avg(single)), avgMulti: mmss(avg(multi)),
    avgRight: mmss(avg(res.filter(r => r.ok))), avgWrong: mmss(avg(res.filter(r => !r.ok))),
    m25: mile(25), m50: mile(50), m75: mile(Math.min(75, QS.length)),
    over3: res.filter(r => r.t.dwell > 180000).length,
    changed: res.filter(r => r.t.changes > 0).length,
    changedWrong: res.filter(r => r.t.changes > 0 && !r.ok).length,
    slowest: [...res].sort((a, b) => b.t.dwell - a.t.dwell).slice(0, 10).map(r => `Q${r.i + 1} ${mmss(r.t.dwell)}${r.ok ? "✓" : "✗"}`),
    order: order.join(" "),
  };
}

/* Markdown export in the TD layout read by build_test_review.py. */
function exportMd(res, score, dom, a) {
  const L = [`# ${DATA.title} (${a.date})`, "", `**Kết quả:** ${score}/${QS.length} câu đúng (${(score * 100 / QS.length).toFixed(2)}%)`, "",
    `**Time used:** ${a.used}${a.timeUp ? " (time up)" : ""} · **Flagged:** ${res.filter(r => r.flag).map(r => r.i + 1).join(", ") || "—"}`, "",
    "| Domain | Score |", "|---|---|", ...dom.map(([d, o, t]) => `| ${DOMAINS[d]} | ${(o * 100 / t).toFixed(2).replace(/\.00$/, "")}% |`), ""];
  const tm = a.timing;
  L.push("## ⏱ Timing", "", `- Avg per question ${tm.avgAll} · single ${tm.avgSingle} · multi ${tm.avgMulti} · right ${tm.avgRight} · wrong ${tm.avgWrong}`,
    `- Answered 25 at ${tm.m25} · 50 at ${tm.m50} · ${Math.min(75, QS.length)} at ${tm.m75} (exam clock) · >3 min: ${tm.over3} q · changed answer: ${tm.changed} q (${tm.changedWrong} ended wrong)`,
    `- Slowest: ${tm.slowest.join(" · ")}`, `- First-answer order: ${tm.order}`, "");
  res.forEach(r => {
    L.push(`## Câu ${r.i + 1} — ${r.ok ? "✅ ĐÚNG" : "❌ SAI"}`, "", `<!-- source: ${r.q.id} · domain: ${r.q.domain}${r.flag ? " · flagged" : ""} · time: ${mmss(r.t.dwell)} · first: ${mmss(r.t.first)} · visits: ${r.t.visits} · changes: ${r.t.changes} -->`, "",
      "### Câu hỏi", "", r.q.stem, "", "### Các phương án", "", ...r.q.opts.map(([l, t]) => `- **${l}.** ${t}`), "",
      `> **Bạn chọn:** ${r.mine.join(", ") || "—"}`, `> **Đáp án đúng:** ${r.q.correct.join(", ")}`, "", "### Giải thích", "",
      (r.q.note ? `> ⚠️ ${r.q.note}\n\n` : "") + r.q.expl, "");
  });
  return L.join("\n");
}

function results(res, score, dom, a, md) {
  const p = pct(score, QS.length), third = k => { const s = res.slice(k * QS.length / 3, (k + 1) * QS.length / 3); return `${s.filter(r => r.ok).length}/${s.length}`; };
  const multi = res.filter(r => r.q.correct.length > 1);
  app.innerHTML = `
  <div class="card"><div class="muted">${a.date} · time used ${a.used}${a.timeUp ? " (time up)" : ""}</div>
    <div class="big ${p >= 80 ? "good" : "badc"}">${score} / ${QS.length} <small style="font-size:20px">(${p}%)</small></div>
    <p class="muted">Gate: ≥ 80% on this bank. Multi-select ${multi.filter(r => r.ok).length}/${multi.length} · thirds ${third(0)} · ${third(1)} · ${third(2)} · flagged ${res.filter(r => r.flag).length}</p>
    <div class="row"><button class="btn primary" id="dl">Download result (.md) for test-review</button><button class="btn" id="back">Home</button></div></div>
  <div class="card"><h3 style="margin-top:0">By domain</h3><table><tr><th>Domain</th><th>Score</th><th>%</th></tr>${
    dom.map(([d, o, t]) => `<tr><td>${DOMAINS[d]}</td><td>${o}/${t}</td><td class="${pct(o, t) >= 80 ? "good" : "badc"}">${pct(o, t)}%</td></tr>`).join("")}</table></div>
  <div class="card"><h3 style="margin-top:0">⏱ Timing</h3>${(tm => `
    <p class="muted">Avg/question <b>${tm.avgAll}</b> · single ${tm.avgSingle} · multi ${tm.avgMulti} · right ${tm.avgRight} · wrong ${tm.avgWrong}<br>
    Answered 25 at <b>${tm.m25}</b> (target 60:00) · 50 at <b>${tm.m50}</b> (125:00) · all at <b>${tm.m75}</b> (185:00) · &gt;3 min: ${tm.over3} q · changed: ${tm.changed} q (${tm.changedWrong} wrong)<br>
    Slowest: ${tm.slowest.join(" · ")}<br>First-answer order: <span style="font-size:12px">${tm.order}</span></p>`)(a.timing)}
    <table><tr><th>Q</th><th>Type</th><th>Time</th><th>First answered</th><th>Visits</th><th>Changes</th><th>Result</th></tr>${
      res.map(r => `<tr><td>${r.i + 1}</td><td>${r.q.correct.length > 1 ? "multi " + r.q.correct.length : "single"}</td><td class="${r.t.dwell > 180000 ? "badc" : ""}">${mmss(r.t.dwell)}</td><td>${mmss(r.t.first)}</td><td>${r.t.visits}</td><td>${r.t.changes}</td><td>${r.ok ? '<span class="good">✓</span>' : '<span class="badc">✗</span>'}${r.flag ? " ⚑" : ""}</td></tr>`).join("")}</table></div>
  <div class="card"><h3 style="margin-top:0">Review</h3>
    <div class="row" style="margin-bottom:10px"><label><input type="checkbox" id="onlyBad" checked> Only wrong + flagged</label></div>
    <div class="nav" style="margin-bottom:12px">${res.map(r => `<button class="${r.ok ? "ok" : "no"}" data-i="${r.i}">${r.flag ? "⚑" : ""}${r.i + 1}</button>`).join("")}</div>
    <div id="rev"></div></div>`;
  const rev = document.getElementById("rev");
  const draw = () => {
    const only = document.getElementById("onlyBad").checked;
    rev.innerHTML = res.filter(r => !only || !r.ok || r.flag).map(r => `
      <div id="r${r.i}" style="border-top:1px solid var(--line);padding:12px 0">
        <b>Q${r.i + 1} ${r.ok ? '<span class="good">✓</span>' : '<span class="badc">✗</span>'}${r.flag ? " ⚑" : ""}</b> <span class="muted">${r.q.domain} · ${r.q.id} · ⏱ ${mmss(r.t.dwell)} · visits ${r.t.visits} · changes ${r.t.changes}</span>
        <div class="stem">${esc(r.q.stem)}</div>
        ${r.q.opts.map(([l, t]) => `<div class="opt ${r.q.correct.includes(l) ? "ok" : r.mine.includes(l) ? "no" : ""}"><b>${l}</b><span>${esc(t)}</span></div>`).join("")}
        <div class="muted">You: ${r.mine.join(", ") || "—"} · Correct: ${r.q.correct.join(", ")}</div>
        ${r.q.note ? `<div class="note">⚠️ ${esc(r.q.note)}</div>` : ""}
        <details><summary>Explanation</summary><div class="expl">${esc(r.q.expl)}</div></details>
      </div>`).join("") || `<p class="good">No wrong or flagged questions.</p>`;
  };
  draw();
  document.getElementById("onlyBad").onchange = draw;
  app.querySelectorAll(".nav button").forEach(b => b.onclick = () => { document.getElementById("onlyBad").checked = false; draw(); document.getElementById("r" + b.dataset.i).scrollIntoView(); });
  document.getElementById("back").onclick = home;
  document.getElementById("dl").onclick = () => {
    const a2 = document.createElement("a");
    a2.href = URL.createObjectURL(new Blob([md], { type: "text/markdown" }));
    a2.download = `${DATA.store}-${a.date.replace(/[: ]/g, "")}-results.md`; a2.click();
  };
}

document.addEventListener("keydown", e => {
  if (!S || !S.running || document.querySelector(".overlay")) return;
  const k = e.key.toLowerCase(), q = QS[S.idx];
  if (/^[1-6]$/.test(k) && q.opts[+k - 1]) choose(q.opts[+k - 1][0]);
  else if (k === "n" || e.key === "ArrowRight") go(S.idx + 1);
  else if (k === "p" || e.key === "ArrowLeft") go(S.idx - 1);
  else if (k === "f") toggleFlag();
  else if (k === "h") highlightSelection();
  else if (k === "k") toggleKw();
  else if (k === " ") { e.preventDefault(); pause(); }
});
pauseBtn.onclick = pause;
document.getElementById("homeBtn").onclick = () => { if (S && S.running) { S.elapsed = usedMs(); S.running = false; save(); } home(); };
/* Save time on tab close; a reload then resumes in the paused state. */
window.addEventListener("beforeunload", () => { if (S && S.running) { S.elapsed = usedMs(); S.running = false; save(); } });
home();
</script>
</body>
</html>
"""


def build(args):
    exam = json.loads(Path(args.set).read_text(encoding="utf-8"))
    for q in exam["questions"]:
        missing = {"id", "stem", "opts", "correct", "expl", "domain"} - q.keys()
        if missing or q["domain"] not in DOMAINS or not set(q["correct"]) <= {l for l, _ in q["opts"]}:
            raise SystemExit(f"bad question {q.get('id')}: missing {missing or '-'} / domain {q.get('domain')} / key {q.get('correct')}")
    data = {"title": exam["title"], "store": exam["store"], "minutes": exam["minutes"], "domains": DOMAINS,
            "questions": exam["questions"]}
    blob = base64.b64encode(json.dumps(data, ensure_ascii=False).encode("utf-8")).decode("ascii")
    page = PAGE.replace("__TITLE__", exam["title"]).replace("__DATA__", blob)
    Path(args.out).write_text(page, encoding="utf-8")
    print(f"wrote {args.out}: {len(exam['questions'])} questions, {exam['minutes']} min")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--set", required=True, help="exam-set JSON")
    ap.add_argument("--out", required=True, help="output HTML path")
    build(ap.parse_args())
