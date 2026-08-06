# Module Spec — Right Model, Right Job (the Golf Bag) — PROPOSE stage

<!-- Owner idea, 2026-07-11 ("token-a-nomics"). Captured to the spec lane, not built. -->

## 1. Identity (draft)

| Field | Value |
|---|---|
| id | C6 (proposed — fluent sibling to A4; confirm) |
| courseId | fluent-chains |
| tier | fluent |
| roleIds | ["pm","coach","engineer","tl","data","leader"] |
| durationMin | 25 |
| staircaseRung | 2 |
| libraryRefs | ["token-economics", "prompting-frameworks"] |

## 2. Concept + ancestry

**One sentence:** choose the *model* by the job's required capability and cost-of-wrong, not by
this week's discount — the golf-bag discipline for a metered world.

- Rung-1 ancestor: **A4 (Right Tool, Right Task)** — picks the tool *tier* (chat/agentic). This
  is the level up: picking a *model* within/across tiers.
- Rung-2 sibling: **C2 (token governance)**; cites **token-economics** for the volatile numbers.
- Not a leap: A4 → this is the same decision, finer grain.

## 3. The learner Monday morning

Someone with 4+ models available (Fable 5, Opus 4.8, GPT-5.x, a small local model) who reaches
for the biggest one every time "to be safe" — and is quietly torching budget, or is paralyzed by
this week's pricing promo. They think the *sale* is the decision. It isn't.

**Behaviors built:**
- "Tier 3: routes a task to the cheapest model that clears the job's quality bar, and can say why."
- "Tier 3: treats promo pricing as noise; the job's cost-of-wrong picks the model."

**Opening activity — Build Your Bag (5 min):** list the 5 AI tasks you did this week. Next to
each, name the *club*: putter (small/fast/cheap — classification, formatting, structured JSON),
wedge (mid — a category of drafting/analysis), driver (frontier — hard reasoning, architecture,
high-stakes), or the pond-club (disposable/local — throwaway lies you won't risk good clubs on).

## 4. The golf metaphor (the spine)

- **Putter = a job.** High-frequency precision, cheap model, used constantly. Not glamorous.
- **Wedge = a role.** Situational specialist, mid model, a *class* of shots.
- **Driver = frontier model.** Max power tee-shot; expensive swing; wrong club for a 2-ft putt
  (= burning Opus to reformat a CSV).
- **Pond-club = small/local model.** The banged-up club for cart-path/asphalt lies — used
  *because* you won't risk or pay for the good clubs on a throwaway. (The rowboat, from the
  prompting-frameworks boundary condition.)
- **The discount is a club sale.** 33% off GPT-5.5, 1.5× Opus, wallet-on-fire-next-to-Fable-5 —
  the sale doesn't change the shot. Don't buy a wedge on sale when the lie calls for a putter.
  *Deprecated pattern to name: chasing this week's promo instead of matching model to job.*

### 4a. Content hooks — openers (HEADLINE register · NOT lesson body · NOT paper evidence)

Candidate opener for the lesson / a `token-economics` blog, owner-coined 2026-07-21:

> **"The 200K underdog that went 1.5 million tokens."** Haiku — the cheapest club in the bag,
> a 200K window — went ten rounds with a Mike-Tyson-like long-running session before taking the KO
> at over 1.5M tokens.

Why it earns a spot: it's the golf-bag lesson made vivid in two beats. **The distance it went** =
"spend freely, the cheap club punches above its price" (the token *business* lens — value/cost fit,
not penny-pinching). **The KO** = the round where the bag says *swap to a bigger club, or put a
read-only referee on it* (ties Paper One's separation-of-context: the fix for long-run collapse is a
fresh-window referee holding the standard, not just a pricier model).

**⚠️ Guardrail — this is a HEADLINE, not a citation.** The 1.5M is *cumulative across the session*
(many turns/compactions), **not** 1.5M in a single 200K window. Great for a blog/talk opener; it must
**never** appear in Paper One as evidence of "context rot" — that misreads the window and a sharp
reviewer catches it. The accurate, load-bearing version: "a long agentic session degraded and
abandoned its task after ~1.5M cumulative tokens" (long-run coherence decay / the context-*contract*
problem). Headline for the click; the precise version for anything that has to survive scrutiny. Same
split as instruction-vs-linter.

## 5. Claims/sources

Volatile (prices, discounts, which model is "best" this week) → **all routed to token-economics**,
dated. The lesson teaches the *durable* pattern (match by capability + cost-of-wrong); the entry
holds the shifting numbers. No model name or price is asserted as current in the lesson body.

## 6. Section plan

1. **Start Here: Build Your Bag** (activity above).
2. **A club has a job, not a ranking.** Capability-vs-cost, not "which is smartest."
3. **The sale is noise.** Cost-of-wrong picks the club; promo pricing never does. (Ties C5's
   cost-of-wrong question + token-economics model-tiering.)
4. **Assignment.**

## 7. Assignment (owner's design)

Read the current model-quality/pricing landscape (link to token-economics + one dated external
source), then map your real weekly task list to a personal model bag: task → club → one-line why.
**Deliverable:** `my-model-bag.md` — 5+ real tasks, each with model tier + rationale + cost-of-wrong.
**Fallback prompt-practice (if stuck):** paste your task list into an AI and prompt it to
categorize each by *required capability* (not "which is best"); then you assign the club. Teaches
capability-first thinking via the exercise itself.

## Definition of Ready
- [ ] Confirm id/course placement (C6 vs a new "fluent-economics" micro-track)
- [ ] token-economics entry carries all live pricing/quality claims (it does)
- [ ] Golf metaphor stays a metaphor — no real model named as "the driver" in body (names date badly)
