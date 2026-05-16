# Brainstorm: Concept Mapper & Scenario Generator Diagrams

**Date:** 2026-05-15 | **Status:** Approved | **Scope:** ai-tutor skill prompt templates

---

## Problem

Concept mapper outputs are text-only. Service relationships, architecture patterns, and decision logic are hard to internalize without visuals. Scenario generator lacks architecture diagrams for recommended solutions.

## Requirements

- **Output**: updated prompt templates in `references/prompt-templates.md`
- **Diagram types**: Mermaid flowcharts (`graph TD/LR`) + decision trees + ASCII fallbacks
- **Volume**: 3-5 diagrams per concept-mapper session
- **Modes affected**: concept-mapper, scenario-generator

## Agreed Design

### Concept Mapper — 5 diagram insertion points

| Section | Diagram | Format | Purpose |
|---------|---------|--------|---------|
| §3 Service Integrations | Service relationship flowchart | Mermaid `graph LR` | Show how services connect (traffic flow, data paths) |
| §4 Architectural Patterns | Architecture diagram per pattern | Mermaid `graph TD` | Visualize 3-tier, HA NAT, hybrid patterns |
| §4 (sub) | Decision tree | Mermaid `graph TD` with branches | "When to use what" — VPN vs DX vs TGW vs Peering |
| §6 Security | Security layers | ASCII | Defense-in-depth layering: NACL → SG → IAM → Encryption |
| §7 Exam Tips | Keyword decision tree | Mermaid `graph TD` | Map exam keywords to answer signals |

**Target**: 3-5 per session, not every section. Only where visual genuinely aids comprehension.

### Scenario Generator — 1 diagram per scenario

Each scenario's answer section gets a Mermaid flowchart showing recommended architecture + ASCII fallback.

### Quality Rules

- Mermaid `graph TD` or `graph LR` only — no exotic types
- Max 15 nodes per diagram; split if larger
- ASCII fallback below each Mermaid block
- Node labels use full service names on first appearance
- Decision trees: question at top, branches as options, leaf = answer

## Scope Boundary

- **In**: prompt template updates (concept-mapper + scenario-generator sections)
- **Out**: other modes, SKILL.md, rendering tooling, cache files

## Touchpoints

- `references/prompt-templates.md` — Concept Mapper (lines 33-63), Scenario Generator section

## Acceptance Criteria

1. Concept mapper prompt instructs 3-5 diagrams (Mermaid + ASCII)
2. Scenario generator prompt instructs 1 architecture diagram per scenario
3. Existing output structure (7 sections, headers, tables) preserved
4. Diagrams render in GitHub/VS Code markdown preview

## Risks

- **Output length inflation**: mitigated by 3-5 cap and "only where visual helps" rule
- **Mermaid rendering inconsistency**: mitigated by sticking to `graph TD/LR` only + ASCII fallbacks

## Next Steps

Hand off to `/ck:plan` for implementation planning.
