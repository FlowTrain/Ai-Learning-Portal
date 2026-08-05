# Program Architecture — How the Pieces Fit

## The realization this platform is built on

The original 4-week coach upskilling program was pitched at the wrong level — not because the content was wrong, but because it assumed the audience's floor was higher than it is. JSON interface design read as "really advanced" to a cohort where many hadn't touched AI since 2022. The fix is not to dumb anything down; it is to **build the staircase** and place every program on the right step:

```
Tier 4  AI-Native      ── Architect track (systems, evals, governance)
                          ▲
Tier 3  AI-Fluent      ── The 4-week Unified Coach Guide lives HERE (2→3 bridge)
                          ▲
Tier 2  AI-Enabled     ── Role-based enablement tracks (PM / Eng / Design)
                          ▲
Tier 1  AI-Aware       ── Monday-Morning On-Ramp (habits, vocabulary, safety)
```

## The content staircase rule

Every concept enters the curriculum three times, in escalating structure. This is the antidote to the curse of knowledge:

| Rung | Form | Example (describing a product surface) |
|---|---|---|
| 1. Plain language | Narrative description, bullets | "The screen has a header, a table of invoices, and a side panel." |
| 2. Patterned language | Named patterns, templates, headings | Layout-areas / components / data-elements / states template |
| 3. Structured format | Schemas, JSON, frontmatter, contracts | `shared-ui-schema.json`-conformant UX JSON |

A Tier 1 lesson lives on rung 1. A Tier 2 lesson moves 1→2. A Tier 3 lesson moves 2→3. The **same skill**, three altitudes — and the rung 3 version is always framed as "a more precise version of what you already did in bullets last week."

The full concept × rung ancestry table lives in `docs/staircase-map.md` (audited 2026-07-10; re-run the audit whenever a lesson is added or a rung changes).

## Where existing assets map

| Asset | Tier bridge | Status |
|---|---|---|
| Prototype course `aware-foundations` / `aware-eng` (A0–A4) | 1 → 2 | Rung-1 rewrite done (2026-07): A0 first-win lab added; A1/A4 rewritten to rung 1; A2/A3/A2E/A3E tagged rung 2 with plain-language openings; unsourced stats parked in `docs/open-questions.md`. |
| Prototype courses `enabled-pm` / `enabled-eng` / `enabled-design` (B-series) | 2 | Extracted. Role-based, correct altitude. |
| Prototype course `fluent-chains` (C-series: chains, token governance, SKILL.md, CLAUDE.md/soul.md) | 2 → 3 | Extracted. This is the compressed lesson form of the 4-week guide. |
| **Unified Coach Guide** (cohort format) | 2 → 3, coach cohort format | **Now a generated output** (2026-07-10): `python app/generate_cohort_kit.py fluent-chains` → `cohort-kits/`. The original document remains the reference DNA; kits regenerate from lesson source whenever content changes. |
| Prototype course `native-systems` (D-series) | 3 → 4 | Extracted. Thinnest tier — expand with real case studies (platform work, eval harnesses, governance). |
| Evolution Library | All tiers (curation layer) | Founded — first entry: `library/evolution/prompting-frameworks.md`. |

## The two products

The platform manages two distinct things and should not blur them:

1. **Learning programs** — tier-bridge curricula, delivered as self-paced lessons (the prototype app) or facilitated cohorts (the 4-week guide format). Versioned, role-tagged, tier-tagged, with assignments and grading.
2. **The Evolution Library** — curated, living reference entries showing how core practices change as models change (see `docs/curation-model.md`). Lessons *reference* library entries; library entries *outlive* any lesson version. This is what keeps the platform honest as the field moves: when prompting practice shifts again, the library entry gets a new era section and every lesson pointing at it inherits the correction.

## Delivery model per tier

| Tier bridge | Format | Rationale |
|---|---|---|
| 1 → 2 | Self-paced micro-lessons (15–25 min) + one drop-in clinic | Tier 1 learners won't commit to cohorts; wins must come in the first session. |
| 2 (role tracks) | Self-paced lessons + optional weekly debrief | Habit consolidation; role-specific artifacts. |
| 2 → 3 | **Cohort program** (the 4-week guide format: 3 assignments/week + 60-min live session) | Fluency requires critique, sharing, and joint artifacts — the live session is the product. |
| 3 → 4 | Studio/apprenticeship: real platform work, case reviews, governance drills | Architecture is learned on real systems, not exercises. |

## Assessment = artifacts + observed behavior

Consistent with the maturity model: completion is evidenced by named artifacts (prompt cards, chains, SKILL.md, CLAUDE.md, soul.md, schemas) plus the Monday-Morning Diagnostic behaviors, never by quiz scores. The prototype's submission/grading flow should grade **artifacts against rubrics**, and rubrics live with the lesson content so they version together. (Restored to scope 2026-07-10 as BACKLOG 10; graded submissions double as the platform's own eval set — misconception patterns land in `docs/misconception-log.md` and drive content revision.)

## Known gaps (build order lives in BACKLOG.md)

1. **Tier 1 on-ramp is the weakest asset and the largest audience.** The aware-tier lessons exist but need the rung-1 rewrite and an emotional-first-win opening lab.
2. **Placement flow.** The diagnostic exists on paper; the platform needs it as an intake experience that routes people to the right course.
3. **Tier 4 track depth.** D-series lessons are outlines; they need case studies, an eval-harness lab, and a governance simulation.
4. **Library velocity.** One evolution entry exists; the model needs 4–6 entries before the "living library" claim is credible (candidates: context engineering, structured outputs, agent orchestration, evaluation practice, token economics).
5. **Leader literacy micro-track.** Leaders need a 3-lesson Tier 4 *literacy* strand (fund/govern/measure) distinct from the architect track.
