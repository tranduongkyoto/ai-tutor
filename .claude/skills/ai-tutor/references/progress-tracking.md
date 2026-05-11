# Progress Tracking

Protocol for updating study progress, computing readiness scores, and displaying the dashboard.

---

## Update Protocol

Execute after EVERY study session (all modes). Read current `aws-csa/study-progress.md`, apply updates, write back.

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
    # If mode was mini-exam, also:
    exams:
      - date: {today, YYYY-MM-DD}
        score: {correct count}
        total: {question count}
        missed_topics: [{list of topic slugs from incorrect answers}]
    weak_topics: {update — see weak topic rules below}
```

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
- Missed: {comma-separated missed topics, or "none"}
- Output: study-sessions/{filename}
```

For **all other modes**:
```
### {YYYY-MM-DD} {HH:MM} | {Domain Name} | {Mode Name}
- Topics: {comma-separated topics covered}
- Output: study-sessions/{filename}
```

For **cross-domain modes** (weak-spot-analyzer, exam-strategy):
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
coverage = (modes_completed.length / 6) * 100
```
- 6 total modes; each completed mode adds ~16.7%

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

### Overall Readiness

```
overall = average of all 12 domain readiness scores
```
- Domains never studied have readiness = 0
- This means overall readiness is diluted by unstudied domains (intentional — you need all 12)

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

Domain                    Ready  Exams  Last       Status
───────────────────────── ────── ────── ────────── ──────────────
Compute                    85%    3      2d ago     ★ Mastered
Storage                    62%    2      3d ago     ◆ Proficient
Databases                  45%    1      5d ago     ▲ Developing
Networking                 30%    0      7d ago     ▲ Developing
Security & Identity         0%    -      -          ○ Not started
Load Balancing & Scaling    0%    -      -          ○ Not started
DNS                         0%    -      -          ○ Not started
Integration & Messaging     0%    -      -          ○ Not started
Serverless                  0%    -      -          ○ Not started
Monitoring & Audit          0%    -      -          ○ Not started
Data & Analytics            0%    -      -          ○ Not started
DR & Architecture           0%    -      -          ○ Not started

Weak Areas: {all weak_topics across all domains, comma-separated}
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
1. Domain with lowest non-zero readiness that is stale (>7 days) → "Stale, needs review"
2. Domain with lowest non-zero readiness → "{mode} to improve score"
3. Domain never started (pick foundational ones first: compute → networking → security-identity → storage) → "Not started yet"
4. Domain with weak_topics that hasn't had a recent mini-exam → "Retest weak topics"

**Format:**
```
Recommended Next: {Domain Name} — {mode} ({reason})
```

Example:
```
Recommended Next: Networking — mini-exam (lowest active score, 7d stale)
```
