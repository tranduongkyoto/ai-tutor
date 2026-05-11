# Code Review: ai-tutor Skill Implementation

**Date:** 2026-05-11
**Reviewer:** code-reviewer subagent
**Scope:** `.claude/skills/ai-tutor/` — all 8 files (markdown-only skill)
**Score: 8/10**

---

## Summary

The skill is well-structured, modular, and aligned with the brainstorm design doc. All 6 phases from the plan are implemented. Core flows are coherent. A few correctness issues exist — one HIGH (mode slug mismatch), one MEDIUM (quiz option gap), and several LOW quality improvements. No blocking issues prevent functionality.

---

## Critical Issues

None.

---

## High Priority

### H1 — Mode Slug Mismatch: `hands-on-lab` vs `Hands-On Lab Creator`

**File:** `SKILL.md` line 47 vs `prompt-templates.md` line 182

- SKILL.md mode option: `hands-on-lab`
- prompt-templates.md header: `## Mode: Hands-On Lab Creator`
- progress-tracking.md session log format: references mode by "Mode Name" (implied slug)
- Brainstorm doc: "Saved to: `{YYMMDD}-{HHMM}-{domain}-hands-on-lab.md`"

There is no `hands-on-lab` slug in `SKILL.md`'s mode table (Step 3); the table shows only `hands-on-lab` as an option but the template title is different. More critically: the brainstorm doc in "Architecture Reviewer" section says the mode is `architecture-reviewer` (matches), but `exam-strategy` brainstorm says saved as `exam-strategy.md` while SKILL.md option is `exam-strategy`. These are OK. The one real mismatch: **prompt-templates.md uses "Hands-On Lab Creator" as header** while slug is `hands-on-lab`. This is cosmetic for display but could confuse an agent matching slugs to template sections. **Fix:** Standardize — either rename header to `## Mode: Hands-On Lab` or document the mapping.

### H2 — `weak-spot-analyzer` and `exam-strategy` Skip Domain but Still Trigger Cache Load

**File:** `SKILL.md` Step 2, lines 52-60 vs Step 3 table lines 70-74

- SKILL.md notes these modes skip domain selection (line 38-39)
- But Step 2 still performs cache check unconditionally (lines 53-60): "Check cache: `.claude/skills/ai-tutor/cache/aws-csa-{domain}.md`"
- prompt-templates.md correctly states "No cache file needed" for Weak Spot Analyzer and exam-strategy uses only `study-progress.md`
- If domain was skipped, `{domain}` is undefined — cache path becomes malformed, triggering unnecessary PDF extraction

**Fix:** In Step 2, gate cache check: "If mode requires domain cache (not `weak-spot-analyzer` or `exam-strategy`): check cache..." The Step 3 table already correctly marks these as not needing cache but Step 2 doesn't branch.

---

## Medium Priority

### M1 — Quiz AskUserQuestion Has Only 4 Options (A-D), Option E Relies on "Other"

**File:** `quiz-flow.md` lines 41-44

- The design decision (brainstorm #3) explicitly accepts this: "AskUserQuestion with A/B/C/D + Other for E"
- But quiz-flow.md line 42 says options: `A`, `B`, `C`, `D` — then "User types E via the Other option"
- Problem: `AskUserQuestion` "Other" prompts the user to type free-text. If user types lowercase `e` instead of `E`, line 80 handles it ("type invalid input → treat as incorrect"). But lowercase `e` is a valid intent, not invalid.
- **Fix:** Add: "If user types 'e' (lowercase), normalize to 'E' before evaluation."

### M2 — Session Filename: `mode` slug inconsistency for cross-domain modes

**File:** `progress-tracking.md` Step 3 vs SKILL.md Step 4

- SKILL.md line 84: `{YYMMDD}-{HHMM}-{domain}-{mode}.md` for all modes
- progress-tracking.md has separate format for cross-domain modes: "All Domains | {Mode Name}"
- But the session filename formula still uses `{domain}` — what value does `{domain}` hold for `weak-spot-analyzer`?
- Brainstorm specifies: "Saved to: `{YYMMDD}-{HHMM}-weak-spot-analysis.md`" (no domain) and `{YYMMDD}-{HHMM}-exam-strategy.md` (no domain)
- SKILL.md line 84 doesn't account for domain-less session files

**Fix:** In Step 4, add: "For cross-domain modes (`weak-spot-analyzer`, `exam-strategy`): filename = `{timestamp}-{mode}.md` (no domain prefix)."

### M3 — `progress` and `refresh` commands skip Steps 3/4/5 but SKILL.md doesn't explicitly say so

**File:** `SKILL.md` Argument Parsing table (lines 18-25)

- The table shows `progress` → "Show progress dashboard" and `refresh <domain>` → "Re-extract PDF cache"
- But the subsequent steps (1-5) don't mention early-exit for these commands
- An agent reading linearly might proceed to Step 1 (domain/mode selection) after handling `progress`
- **Fix:** Add explicit early-return note: "After handling `progress` or `refresh`, stop — do not proceed to Steps 1-5."

---

## Low Priority

### L1 — `README.md` Lists 7 Modes in Table, Skill Has 6

**File:** `README.md` lines 18-25

```
| exam-strategy | ... |
```

The README table shows 7 rows (concept-mapper, mini-exam, scenario-generator, weak-spot-analyzer, hands-on-lab, architecture-reviewer, exam-strategy). That is 7. The skill is described as "6 study modes" on line 3 of README and line 3 of SKILL.md. Count is actually 7 modes implemented (prompt-templates.md has 7 `## Mode:` headers).

**Clarify:** Either update description to "7 study modes" or confirm `exam-strategy` was intended as a bonus beyond the core 6. The brainstorm lists 6 (does not count exam-strategy in the top 6 but then describes it as one of the modes). The brainstorm "## 6 Tutor Modes" section lists exactly 6: concept-mapper, scenario-generator, weak-spot-analyzer, hands-on-lab, architecture-reviewer, exam-strategy — **no mini-exam listed as one of the 6**. Mini-exam is treated separately as the quiz engine. This is confusing. SKILL.md correctly lists 7 in the mode selection menu. **Fix:** Update all "6 study modes" references to "7 study modes" or restructure to call mini-exam the quiz engine separately.

### L2 — PDF mapping correctness: two files not domain-mapped

**File:** `certs/aws-csa/domains.md` vs actual `sections/` directory

PDFs in `sections/` but NOT in any domain mapping:
- `00-intro-and-toc.pdf` — intro, intentionally excluded ✓
- `01-getting-started-with-aws.pdf` — AWS basics, not mapped to any domain
- `13-cloudfront-and-global-accelerator.pdf` — **not mapped to any domain**
- `30-exam-preparation-and-congratulations.pdf` — exam prep content, not mapped

`13-cloudfront-and-global-accelerator.pdf` is notable: CloudFront is a real exam topic (CDN, caching, signed URLs, OAC). The `serverless` domain lists `cloudfront-functions` as a topic but doesn't map the CloudFront PDF. The `networking` domain would be the natural home.

**Fix:** Either add `13-cloudfront-and-global-accelerator.pdf` to `networking` or `load-balancing-scaling` domain, or document the intentional exclusion.

### L3 — `progress-tracking.md` Recommendation Engine Priority #4 Conflicts with #2

**File:** `progress-tracking.md` lines 179-183

- Priority 2: "Domain with lowest non-zero readiness → improve score"
- Priority 4: "Domain with weak_topics that hasn't had a recent mini-exam → retest weak topics"

A domain can match both #2 and #4. Priority 2 will always fire first, so priority 4 is unreachable when lowest-readiness domain also has weak_topics (common case). This is minor logic order issue — not wrong, but the recommendation "Retest weak topics" will rarely surface.

### L4 — `pdf-extractor.md` cache path is relative; SKILL.md cache path format differs slightly

**File:** `pdf-extractor.md` line 80 vs `SKILL.md` line 54

- pdf-extractor.md says: "Check if file exists using Bash: `test -f {cache_path} && echo "HIT" || echo "MISS"`"  
- SKILL.md says check cache at `.claude/skills/ai-tutor/cache/aws-csa-{domain}.md`
- pdf-extractor.md line 84: "Construct full PDF paths: `sections/{pdf_filename}`"
- All paths look consistent, but `sections/` is a relative path. If Claude's working directory is not the project root, this fails silently.
- **Fix:** Document that all paths assume cwd = project root, or use absolute path construction.

### L5 — No timeout/fallback if pdf-extractor subagent silently fails

**File:** `SKILL.md` lines 56-60

- SKILL.md says "Wait for completion, then read cache file"
- Edge case: subagent completes but writes a malformed/empty cache file
- Only error case handled: "PDF extraction fails → show error, suggest refresh" (line 99)
- But no check after cache MISS flow: "does cache file now exist and is non-empty?"
- **Fix:** After spawning subagent, verify: `test -s {cache_path}` (non-zero size). If empty, show extraction failure error.

---

## Positive Observations

1. **Modular design**: SKILL.md at 107 lines is clean. References files do heavy lifting. Correct architectural choice.
2. **Self-verify step**: Mini exam prompt explicitly includes quality review before presenting — good guardrail against hallucinated answers.
3. **Dynamic readiness**: Correct decision to never store computed scores — always recalculate from raw data.
4. **Edge cases covered**: Empty progress file, no exam history, invalid args — all handled explicitly.
5. **Cache check protocol**: Bash `test -f` for cache HIT/MISS is clean and deterministic.
6. **study-progress.md structure**: YAML frontmatter + append-only session log is simple and works well.
7. **PDF mappings accuracy**: 27 of 31 PDFs correctly mapped to domains. The 4 unmapped are edge cases (intro, getting-started, cloudfront, exam-prep) — 3 are defensible omissions.
8. **Brainstorm alignment**: All 18 design decisions from the brainstorm doc are reflected in the implementation.

---

## Completeness Check (6 Plan Phases)

| Phase | Description | Status |
|-------|-------------|--------|
| 1 | Skill skeleton (SKILL.md + references + domains.md) | Complete |
| 2 | PDF extractor subagent + cache system | Complete |
| 3 | Core modes: concept-mapper + mini-exam | Complete |
| 4 | Remaining modes: scenario, weak-spot, lab, arch-review, exam-strategy | Complete |
| 5 | Progress tracking + dashboard | Complete |
| 6 | Polish: recommendations, follow-up menus, edge cases | Complete |

All 6 phases implemented.

---

## Cross-Reference Integrity

| Check | Result |
|-------|--------|
| Mode slugs in SKILL.md match AskUserQuestion options | Pass |
| Mode slugs in SKILL.md match prompt-templates.md headers | Partial fail — "Hands-On Lab Creator" vs `hands-on-lab` slug |
| Domain slugs in SKILL.md match domains.md keys | Pass — all 12 match |
| Reference file names in SKILL.md match actual files | Pass |
| Cache path format consistent across files | Pass |
| Session filename format consistent (SKILL.md vs progress-tracking.md) | Partial fail — domain-less modes not handled |

---

## Recommended Actions (Priority Order)

1. **[HIGH]** Fix Step 2 in SKILL.md to skip cache check for `weak-spot-analyzer` and `exam-strategy`
2. **[HIGH]** Standardize `Hands-On Lab Creator` header in prompt-templates.md to `Hands-On Lab` to match slug
3. **[MEDIUM]** Add early-exit note in SKILL.md for `progress` and `refresh` commands
4. **[MEDIUM]** Fix session filename formula in SKILL.md Step 4 for domain-less modes
5. **[MEDIUM]** Add lowercase `e` normalization in quiz-flow.md edge cases
6. **[LOW]** Add `13-cloudfront-and-global-accelerator.pdf` to networking domain
7. **[LOW]** Update "6 study modes" → "7 study modes" in README.md and SKILL.md description
8. **[LOW]** Add post-spawn cache file size check in SKILL.md after PDF extraction

---

## Unresolved Questions

1. Is `exam-strategy` counted as one of the "6 modes" or a 7th bonus mode? The brainstorm's "6 Tutor Modes" section includes it but excludes mini-exam — inconsistent framing.
2. Should `01-getting-started-with-aws.pdf` content (IAM basics, regions, AZs) be added to `security-identity` or a new `foundations` domain?
3. Is `13-cloudfront-and-global-accelerator.pdf` intentionally excluded or an oversight? CloudFront appears in serverless topics list (`cloudfront-functions`) but PDF isn't mapped.
