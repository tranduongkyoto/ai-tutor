# Progress Tracking

Protocol for updating study progress, computing readiness scores, and displaying the dashboard.

---

## Update Protocol

Execute after EVERY study session (all modes). Read current `aws-csa/study-progress.md` (project root, NOT inside `.claude/skills/`), apply updates, write back.

### Step 1: Update YAML Frontmatter

```yaml
# Top-level fields:
started: {set to today if null}
last_session: {today's date, YYYY-MM-DD}
total_sessions: {increment by 1}

# Domain-level fields (create domain entry if not exists):
domains:
  {domain}:
    sessions_count: {increment by 1}
    modes_completed: {append mode slug if not already present}
    last_studied: {today's date, YYYY-MM-DD}
    current_phase: {1-4, advance after completing a guided phase; default 1}
    phase_scores: {p1: learn-and-test score, p2: scenario-practice score, p3: design score, p4: comprehensive score}
    modes_completed: {append mode slug} # new slugs: learn-and-test, scenario-practice
    completed: {true if Phase 4 passed ≥80%, else false/omit}
    # If mode was mini-exam, also:
    exams:
      - date: {today, YYYY-MM-DD}
        score: {correct count}
        total: {question count}
        scope: {concepts|scenarios|design|comprehensive|general}
        time_minutes: {elapsed minutes}
        time_limit_minutes: {time limit = total × 3}
        missed_topics: [{list of topic slugs from incorrect answers}]
    weak_topics: {update — see weak topic rules below}
```

```yaml
# For keyword-drill (stored at top-level, not per-domain):
keyword_drill:
  sessions_count: {increment}
  last_drilled: {date}
  exams:
    - date: {date}
      score: {correct}
      total: {pattern count}
      missed_patterns: [{pattern short-ids}]
  weak_patterns: [{cumulative missed, same removal rule as weak_topics}]
```

```yaml
# For mock-exam (stored at top-level, not per-domain):
mock_exams:
  - date: {date}
    score: {correct}
    total: 65
    time_minutes: {elapsed}
    by_exam_domain:
      secure: {score}/{total}
      resilient: {score}/{total}
      high_performing: {score}/{total}
      cost_optimized: {score}/{total}
    missed_topics: [{all missed topic slugs}]
    verdict: {PASS|BORDERLINE|FAIL}
```

### Backward Compatibility

Domains with `completed: true` retain old 6-phase format (p2/p4/p5/p6 keys). New domains use 4-phase format (p1/p2/p3/p4 keys). When displaying old completed domains: show as "4/4" in dashboard (they finished all phases).

**In-progress domain migration (case-by-case):**
- `load-balancing-scaling` (old current_phase:4, scores p2:90, p4:90): Map to new current_phase:2, phase_scores: {p1:90, p2:90}. Completed equivalent of new P1 (learn+test) and P2 (scenario+test).
- `databases` (old current_phase:1, only concept-mapper done): Reset to new current_phase:1, no scores to preserve. Will redo P1 with new learn-and-test format.

**Slug compatibility rule:** Migrated domains retain old `modes_completed` slugs (e.g., `concept-mapper`, `mini-exam:concepts`). For coverage and recommendation calculations, always use `current_phase` — never the free-mode slug fallback — for domains that have been through guided mode. Old slugs in `modes_completed` are historical records, not inputs to the coverage formula.

### Step 2: Update Weak Topics

After a mini-exam:
1. Add all `missed_topics` from the latest exam to `weak_topics`
2. Remove topics from `weak_topics` if the user answered them correctly in the **last 2 exams**
3. Deduplicate the list

### Step 3: Append Session History

Append to the `## Session History` section:

For **mini-exam** sessions:
```
### {YYYY-MM-DD} {HH:MM} | {Domain Name} | Mini Exam
- Score: {score}/{total} ({percentage}%)
- Time: {elapsed} min / {limit} min
- Missed: {comma-separated missed topics, or "none"}
- Output: study-sessions/{filename}
```

For **learn-and-test** sessions:
```
### {YYYY-MM-DD} {HH:MM} | {Domain Name} | Learn and Test
- Score: {score}/{total} ({percentage}%)
- Time: {elapsed} min / {limit} min
- Missed: {comma-separated missed topics, or "none"}
- Output: study-sessions/{filename}
```

For **scenario-practice** sessions:
```
### {YYYY-MM-DD} {HH:MM} | {Domain Name} | Scenario Practice
- Score: {score}/{total} ({percentage}%)
- Time: {elapsed} min / {limit} min
- Missed: {comma-separated missed topics, or "none"}
- Output: study-sessions/{filename}
```

For **all other modes**:
```
### {YYYY-MM-DD} {HH:MM} | {Domain Name} | {Mode Name}
- Topics: {comma-separated topics covered}
- Output: study-sessions/{filename}
```

For **keyword-drill**:
```
### {YYYY-MM-DD} {HH:MM} | Cross-Domain | Keyword Drill
- Score: {score}/{total} ({pct}%)
- Time: {elapsed} min / {limit} min
- Missed: {pattern short-ids}
- Output: study-sessions/{filename}
```

For **mock-exam**:
```
### {YYYY-MM-DD} {HH:MM} | All Domains | Mock Exam
- Score: {score}/65 ({pct}%) — {verdict}
- Time: {elapsed} min
- Weakest domain: {exam domain name}
- Output: study-sessions/{filename}
```

For **cross-domain modes** (weak-spot-analyzer, exam-strategy-coach):
```
### {YYYY-MM-DD} {HH:MM} | All Domains | {Mode Name}
- Output: study-sessions/{filename}
```

### Step 4: Get Timestamp

Use bash to get current date and time:
```bash
date +"%Y-%m-%d"     # for YAML dates
date +"%H:%M"        # for session history time
date +"%y%m%d-%H%M"  # for session filename prefix
```

---

## Readiness Formula

Compute dynamically on every dashboard view or recommendation. **Never store readiness values** — always calculate from raw data.

### Per-Domain Readiness

```
readiness = (coverage * 0.3) + (exam_avg * 0.5) + (recency * 0.2)
```

**Coverage** (30% weight):
```
coverage = (current_phase / 4) * 100
```
- 4 phases in guided path; each completed phase adds 25%
- If using free mode without guided path, fallback: `(modes_completed.length / 4) * 100` (cap at 100%)
- For old completed domains (`completed: true`): coverage = 100%

**Exam Average** (50% weight):
```
exam_avg = average of last 2 exam scores as percentage
         = 0 if no exams taken
```
- If only 1 exam: use that score
- If 2+ exams: average the last 2

**Recency** (20% weight):
```
days_since = (today - last_studied).days

recency = 100                           if days_since <= 7
        = 100 - ((days_since - 7) / 23 * 100)  if 7 < days_since <= 30
        = 0                             if days_since > 30 or never studied
```

### Overall Readiness (Exam-Weight-Adjusted)

Weighted by SAA-C03 real exam coverage. Derived from exam guide domain mapping
and community frequency reports (researched 2026-06-06).

```
Domain weights (exam-aligned):
  Tier 1 (65%): compute 12.5%, networking 12.5%, storage 12.5%,
                security-identity 12.5%, dr-architecture 15%
  Tier 2 (35%): load-balancing-scaling, databases, serverless,
                integration-messaging, dns, monitoring-audit,
                data-analytics                                         → 5% each

overall = Σ (domain_readiness × domain_weight)
```

Rationale:
- **dr-architecture in Tier 1 (15%)**: DR strategies map heavily to Domain 2 (Resilient 26%)
  + cross-domain in Domains 1/3/4. ~10-13 questions out of 65. CloudFormation,
  Well-Architected, RPO/RTO trade-offs are primary exam focus areas.
- **data-analytics in Tier 2 (5%)**: Athena/Redshift/Glue appear as options in Domain 3
  (High-Performing) and Domain 4 (Cost-Optimized). ~4-5 questions. ML services at
  awareness level only.

- Domains never studied have readiness = 0
- Tier 1 domains contribute 65% of overall readiness
- Example: 4 original Tier-1 domains at ~90% → overall ≈ 45% (DR gap drags it down)

### Status Thresholds

| Readiness | Status | Symbol |
|-----------|--------|--------|
| >= 80%    | Mastered    | ★ |
| 60-79%    | Proficient  | ◆ |
| 30-59%    | Developing  | ▲ |
| 1-29%     | Beginning   | △ |
| 0%        | Not started | ○ |

---

## Dashboard Format

Display when user runs `/ai-tutor progress`:

```
AWS CSA (SAA-C03) - Study Progress
Started: {date} | Last: {date} | Sessions: {total}
Overall Readiness: {pct}%  {progress_bar}  {studied_count}/12 domains

Domain                    Phase  Ready  Exams  Last       Status
───────────────────────── ────── ────── ────── ────────── ──────────────
Compute                    4/4    85%    3      2d ago     ★ Mastered
Storage                    3/4    62%    2      3d ago     ◆ Proficient
Databases                  1/4    45%    1      5d ago     ▲ Developing
Networking                 1/4    30%    0      7d ago     ▲ Developing
Security & Identity        -      0%     -      -          ○ Not started
Load Balancing & Scaling   -      0%     -      -          ○ Not started
DNS                        -      0%     -      -          ○ Not started
Integration & Messaging    -      0%     -      -          ○ Not started
Serverless                 -      0%     -      -          ○ Not started
Monitoring & Audit         -      0%     -      -          ○ Not started
Data & Analytics           -      0%     -      -          ○ Not started
DR & Architecture          -      0%     -      -          ○ Not started

Weak Areas: {all weak_topics across all domains, comma-separated}

Mock Exams:
  {date}: {score}/65 ({pct}%) — {verdict} — {time}min
  Weakest domain: {exam domain name}

Recommended Next: {domain} — {mode} ({reason})
```

**Progress bar**: 20 chars wide
- Filled: `█` — count = floor(percentage / 5)
- Empty: `░` — count = 20 - filled
- Example: 42% → `████████░░░░░░░░░░░░`

**"Last" column**:
- Today: `today`
- Yesterday: `1d ago`
- Within 30 days: `{N}d ago`
- Over 30 days: `30d+`
- Never: `-`

**studied_count**: Number of domains with `sessions_count > 0`

---

## Recommendation Engine

After each session AND on dashboard, suggest next action:

**Priority order:**
1. Domain in-progress with next phase available → "{domain} — Phase {N}: {mode} (continue study path)"
2. Domain with lowest non-zero readiness that is stale (>7 days) → "Stale, needs review"
3. Domain never started (pick foundational ones first: compute → networking → security-identity → storage) → "Not started yet"
4. Domain with weak_topics that hasn't had a recent mini-exam → "Retest weak topics"
5. Domain with Phase 4 failed (<80%) → "Retake final exam after reviewing weak phases"

**Format:**
```
Recommended Next: {Domain Name} — Phase {N}: {mode} ({reason})
```

Example:
```
Recommended Next: Compute — Phase 2: scenario-practice (continue study path)
Recommended Next: Networking — Phase 1: learn-and-test (not started yet)
```
