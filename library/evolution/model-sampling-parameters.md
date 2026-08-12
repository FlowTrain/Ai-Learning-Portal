---
id: model-sampling-parameters
practice: Model Sampling & Reasoning Controls (Temperature → Effort)
status: current
last_reviewed: 2026-08-07
review_cadence: monthly
model_generations: [temperature-dial-era, single-knob-constraint-era, effort-control-era-2026]
referenced_by: [B5, C9]
curators: [platform-owner]
---

<!-- This entry is deliberately volatile — it holds the numbers and vendor rules that lessons must
     NOT hard-code. review_cadence is monthly because this moved twice in ~12 months.
     Claims tagged [OFFICIAL] were confirmed against platform.claude.com on the last_reviewed date.
     Claims tagged [REPORTED] come from vendor community/second-party sources and need a primary-doc
     confirm before they go into a lesson body — see §7. -->

# Evolution Entry: Model Sampling & Reasoning Controls (Temperature Dial → Single-Knob Constraints → Effort)

## 1. Current guidance (teach this today)

Two different worlds now exist, and which one you're in depends on the model tier:

- **Non-reasoning / general models** still expose the classic **temperature** dial — the deterministic↔creative
  control the deck describes. Set it low for repeatable/compliance work, high for ideation. This is still
  true and still worth teaching as the mental model.
- **Reasoning-tier / frontier models are moving off temperature onto an `effort` control.** You no longer
  turn a fine-grained sampling dial; you tell the model *how hard to think*. On current Claude (4.7+ and
  the 5-series) reasoning depth is set with adaptive thinking + `output_config: {effort: ...}`, not a token
  budget or a temperature value [OFFICIAL]. On OpenAI's reasoning models (o-series, GPT-5) `temperature`
  is unsupported and you use `reasoning_effort` instead [REPORTED].

**The teaching takeaway:** temperature is the *concept* (controlling output variability), but the *control
surface* is generation-dependent. Teach the concept as durable; treat the specific parameter, its range,
and its per-model rules as volatile — which is exactly why they live here and not in the lesson body.

**Ranges are not portable across vendors.** Anthropic's temperature runs **0.0–1.0**; OpenAI's ran **0–2**
(default 1.0) — the "default 1.0 / max 2.0" figure is the OpenAI/Copilot scale, not a universal one
[REPORTED]. Never teach a number without its vendor and its date.

## 2. The observed shift (why this entry, why now)

Through ~2024 the temperature dial (plus top_p, penalties) was the universal knob set. Two things changed:
first, vendors constrained *combinations* (you must pick temperature **or** top_p, not both); then the
frontier models introduced internal reasoning, and for a model that can walk itself down a bad reasoning
path, a final-token sampling temperature can't repair the path — so the control moved up a level, from
"how randomly do you pick the next word" to "how much do you deliberate." That's the era change: **from a
sampling dial to a reasoning-effort knob.** Cause: the rise of reasoning models (2025→2026). Sources: §7.

## 3. Era table

| Era | ~Dates | The practice as it was | Model context that made it right | What ended it |
|---|---|---|---|---|
| 1 — Temperature dial | ~2022–2024 | Set temperature (0–1 or 0–2) and/or top_p per use case | Single-pass generative models; sampling *was* the only lever | Combination constraints + reasoning models |
| 2 — Single-knob constraint | 2025 | One of temperature **or** top_p, not both; thinking requires temperature=1/unset | Claude 4.1 Opus+ reject both-set requests [REPORTED]; extended thinking incompatible with temp changes | Frontier reasoning models drop the dial |
| 3 (current) — Effort control | 2026 | Reasoning depth via `effort` (Claude adaptive thinking + `output_config.effort`) / `reasoning_effort` (OpenAI); temperature constrained or unsupported on reasoning tiers | Reasoning models where deliberation depth matters more than final-token randomness | — |

## 4. Deprecated candidates (each faces the Challenge step)

| Stop doing this | Because | Truly obsolete, or only for frontier models? |
|---|---|---|
| Teaching "temperature 0–2, default 1.0" as universal | That's the OpenAI/GPT-4.x scale; Anthropic is 0–1 | Obsolete as a *universal* claim; fine as a vendor-specific, dated fact |
| Setting both temperature and top_p | Rejected on current Claude; they interact unpredictably | Obsolete — pick one (temperature is the recommended primary) [REPORTED] |
| Reaching for a temperature value on a reasoning model | Unsupported / constrained; the lever is `effort` now | Frontier-only — non-reasoning models still take temperature |
| Manual extended thinking (`budget_tokens`) on Claude | Deprecated on 4.6; 400 error on 4.7+ [OFFICIAL] | Obsolete on 4.7+/5-series; migrate to adaptive thinking + `effort` |

## 5. What survived / boundary conditions

- **The concept survives intact.** "Match output variability to the job's risk and goal" is as true as
  ever — only the knob's name and shape changed. The use-case framing (compliance→low, ideation→high)
  is still the right instinct; on reasoning models it re-expresses as effort/mode choices.
- **Temperature is still correct** on non-reasoning models, small/local models, and anywhere you're
  running an older or open-weight model. The old way isn't wrong; it's scoped. This is the boundary
  condition: **general model = dial; reasoning model = effort.**
- **Determinism is never absolute.** Even at temperature 0, output isn't guaranteed identical — teach
  "more repeatable," not "deterministic."

## 6. Signals to watch (what would trigger the next era)

1. `effort`/`reasoning_effort` levels standardizing (or fragmenting) across vendors — a portable vocabulary
   would change how we teach it.
2. Temperature disappearing from the general (non-reasoning) tier too, not just the frontier.
3. New sampling controls appearing (per-request determinism seeds, etc.).
4. Anthropic publishing an explicit temperature-deprecation note for 4.7+/5-series (currently [REPORTED],
   not yet confirmed on an official page — see §7).

## 7. Sources + how to re-verify (this entry ages fast — re-run these)

**Confirmed by fetching official docs on last_reviewed [OFFICIAL]:**

- Extended thinking deprecated on Claude 4.6, 400 error on 4.7+; migrate to adaptive thinking +
  `output_config: {effort}`. — Anthropic, *Extended thinking* docs.

**Reported by second-party / community sources, confirm before putting in a lesson body [REPORTED]:**

- Claude temperature range 0.0–1.0, default 1.0; temperature XOR top_p since Claude 4.1 Opus (Aug 2025);
  thinking requires temperature=1/unset; temperature deprecated (default-only) on Claude 4.7+.
- OpenAI GPT-5 / o-series: `temperature`, `top_p`, penalties unsupported on reasoning models → use
  `reasoning_effort`; scale 0–2 on the older general models.

**Core search terms to relocate current docs (docs move — search, don't trust a bookmarked number):**

- `Anthropic Claude API temperature range docs` → platform.claude.com API reference (Create a Message)
- `Claude effort output_config adaptive thinking`
- `Claude extended thinking deprecated 4.7 400 error`
- `OpenAI GPT-5 temperature unsupported reasoning_effort`
- `Azure OpenAI reasoning models GPT-5 parameters` (Microsoft Learn — good consolidated table)

**Primary doc URLs to check on each monthly review:**

- https://platform.claude.com/docs/en/api/messages
- https://platform.claude.com/docs/en/build-with-claude/effort
- https://platform.claude.com/docs/en/build-with-claude/extended-thinking
- https://platform.openai.com/docs/guides/reasoning
- https://learn.microsoft.com/azure/foundry/openai/how-to/reasoning
