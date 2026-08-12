---
id: model-family-tiers
practice: Model Family & Tier Naming (reading a vendor lineup)
status: current
last_reviewed: 2026-08-07
review_cadence: monthly
model_generations: [single-name-era, number-plus-suffix-era, generation-x-named-tier-era-2026]
referenced_by: [C9]
curators: [platform-owner]
---

<!-- This entry exists so lessons teach how to READ a lineup, never a snapshot list of names.
     The specific names below are dated examples, not lesson content — they will be wrong within
     months. That volatility IS the point (it's why "feel" beats memorization).
     Anthropic lineup [OFFICIAL] (platform.claude.com, fetched on last_reviewed);
     OpenAI/Google names [REPORTED] from vendor blogs + second-party roundups — confirm at §7 URLs. -->

# Evolution Entry: Model Family & Tier Naming (Single Name → Number+Suffix → Generation × Named Tier)

## 1. Current guidance (teach this today)

Teach learners to **read any lineup along three axes**, not to memorize names:

- **Family** — the vendor's model line (Claude, GPT, Gemini, Llama…). Different families = different *feel*.
- **Tier** — the capability/size class *within* a family: flagship (deep judgment) → balanced daily driver
  → fast/cheap high-volume. Every major vendor has this shape, whatever they call it.
- **Generation** — the version number that advances over time.

The durable 2026 insight: **tier and generation increasingly move on independent cadences.** A vendor can
ship a new fast-tier generation while the flagship tier sits still. So "the latest model" is ambiguous —
you have to say *which tier* and *which generation*. Read the lineup as a grid (tier × generation), pick
the **tier** by the job, then take the newest **generation** available in that tier.

**Say the confusing part out loud.** Naming clarity varies by vendor and is itself volatile:

- **Clean:** Anthropic — Opus (flagship) / Sonnet (balanced) / Haiku (fast) tiers across numbered
  generations [OFFICIAL]. Consistent tier words; the number is the generation.
- **Confusing:** OpenAI — a number line (GPT-5.x) *plus* suffixes (Instant/Thinking/Pro, mini/nano) *plus*
  a separate reasoning "o-series," and a named-tier scheme (Sol/Terra/Luna) where the name is the durable
  tier and the number is the generation [REPORTED].
- **Split-timeline:** Google — Gemini Pro / Flash / Flash-Lite tiers, but the Pro and Flash lines have
  drifted to different generation numbers (Flash ahead of a frozen Pro) [REPORTED].

Once a learner can place any new name on the family → tier × generation grid, a new release is
self-locating instead of confusing.

## 2. The observed shift (why this entry, why now)

Naming evolved from **one name per model** (early GPT-3/Claude 1) → **number + capability suffix**
(GPT-4o, mini; Claude 3.5 Sonnet) → **generation × named durable tier** (OpenAI Sol/Terra/Luna; Anthropic's
stable Opus/Sonnet/Haiku; Google's Pro/Flash on separate timelines). The driver: vendors want a *stable*
tier word customers can standardize on, while shipping generations underneath at different speeds. Result:
tier and generation decoupled — which is precisely what makes a snapshot list rot. Sources: §7.

## 3. Era table

| Era | ~Dates | Naming as it was | What made it right | What ended it |
|---|---|---|---|---|
| 1 — Single name | ~2020–2023 | One name/number per model (GPT-3, Claude 1) | Few models, one axis | Multiple sizes/speeds per generation |
| 2 — Number + suffix | 2023–2025 | Generation number + capability suffix (mini/Pro/Instant; 3.5 Sonnet) | Tiers emerge inside a family | Tiers needed to advance independently of the number |
| 3 (current) — Generation × named tier | 2026 | Durable tier name × generation number, tiers on independent cadences (Sol/Terra/Luna; Opus/Sonnet/Haiku; Pro/Flash split) | Vendors want a stable tier customers standardize on | — |

## 4. Deprecated candidates (each faces the Challenge step)

| Stop doing this | Because | Truly obsolete, or scoped? |
|---|---|---|
| Teaching a fixed list of current model names | Wrong within months; naming churns fastest of all | Obsolete in lesson bodies — names belong in this entry, dated |
| Saying "use the latest model" | Ambiguous once tier ≠ generation | Obsolete — specify tier *and* generation |
| Assuming names map across vendors | "Pro" ≠ "Opus" ≠ "Sol"; scales/meanings differ | Obsolete as a cross-vendor shortcut |
| Treating a version number as the whole identity | Misses the tier axis entirely | Obsolete — always name family + tier + generation |

## 5. What survived / boundary conditions

- **The three-tier shape is stable** even as words change: every major family has flagship / balanced /
  fast-cheap. Teach the *shape*; it's the reliable part.
- **Numbers still matter within a tier** — a newer generation of the same tier is generally the pick.
- **Snapshot lists are fine as dated examples**, never as the lesson's teaching content. This entry is
  where the dated examples live; the lesson teaches the grid.

## 6. Signals to watch (what would trigger the next era)

1. A vendor collapsing or renaming its tier words again (OpenAI already shifted to Sol/Terra/Luna).
2. Tier/generation cadences drifting further apart (Google's frozen-Pro / racing-Flash split widening).
3. Cross-vendor tier standardization (unlikely soon, but would simplify teaching).
4. Reasoning vs. non-reasoning becoming its own labeled axis (pairs with `model-sampling-parameters`).

## 7. Sources + how to re-verify (names rot fastest — always re-check)

**Confirmed by official docs on last_reviewed [OFFICIAL]:**

- Anthropic tiers Opus / Sonnet / Haiku across numbered generations — platform.claude.com.

**Reported from vendor blogs + second-party roundups, confirm before use [REPORTED]:**

- OpenAI named tiers Sol / Terra / Luna; earlier GPT-5.x Instant / Thinking / Pro, mini/nano; o-series
  reasoning (o3, o4-mini, o3-pro).
- Google Gemini Pro / Flash / Flash-Lite; Flash line ahead of a frozen Pro line (separate timelines).

**Core search terms to relocate current lineups (search fresh — never trust a cached list):**

- `OpenAI model lineup <current-year> tiers naming` → openai.com model pages
- `Anthropic Claude models overview` → platform.claude.com/docs (models)
- `Google Gemini models comparison <current-year>` → blog.google + Google Cloud model docs
- `<vendor> reasoning model vs standard model naming`

**Primary URLs to check each monthly review:**

- https://platform.claude.com/docs/en/about-claude/models/overview
- https://openai.com/ (model index / release posts)
- https://blog.google/ (Gemini model announcements) + Google Cloud Gemini model docs

<!-- Pairs with `model-sampling-parameters`: this entry = how the lineup is NAMED; that entry = how the
     controls (temperature/effort) DIFFER across those tiers. C9 cites both. -->
