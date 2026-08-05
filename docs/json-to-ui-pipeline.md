# The JSON→UI Pipeline — Owned, Not Rented

The demo that lands ("structured JSON prompt → working UI page") has been running on borrowed infrastructure: V0 + shadcn/Vite. This note is the sustainability decision — what replaces V0, what Storybook is actually for, where Figma fits, and why the day job's Figma Make dependency is the thing this pipeline retires. Exhibit A: `demo/json-to-ui.html` — the demo, rebuilt with zero vendors, running on the trainyard design tokens, in one file you own. Open it, edit the JSON, watch it render. Toggle the states.

## Why V0 isn't the pipeline

V0 was the right spike: it proved the *experience* — people feel the JSON become a page and something clicks. But it fails all three ownership questions (D5): who maintains it when the generator changes (Vercel does, on their schedule), what does it cost per run (their pricing, their meter), what breaks and who notices (their model updates, silently). The generation step is also *non-deterministic* — same JSON in, different page out — which quietly contradicts the entire thesis being demoed. The demo says "structure gives you control"; the tool says "roll again."

## The owned pipeline (V5's No-Figma pipeline, with the V0 tail cut)

Your V5 doc already designed this; only the last arrow changes:

```
Intent (person or vision model)
   → typed composition JSON        ← schema-validated; closed component vocabulary
   → deterministic render          ← tokens from trainyard-design-system (canonical, yours)
   → Claude Code + shadcn MCP      ← when production React is the target
   → Storybook                     ← the gallery + eval harness (below)
```

Three properties make it sustainable where V0 wasn't:

1. **The schema is closed.** The renderer/generator can only use components that exist. Unknown types render as visible errors, not inventions (the demo shows this live — structured-outputs' "valid ≠ correct" made physical).
2. **The tokens are yours and already canonical.** `trainyard-design-system/tokens/design-tokens.json` v1.0.0 — W3C draft format, cssVars declared, approved 2026-06-09. The "starving for Figma tokens" problem is solved *in your own repo*; what was missing was a consumer that proves it.
3. **The render is deterministic.** Same JSON in, same UI out, every run. Which means UI generation becomes *testable* — and that's Storybook's real job.

## What Storybook actually is in this pipeline

Not the generator — **the eval harness.** Each schema component type gets a story; each story is a visual eval fixture. Generated output gets compared against stories (visual regression, Chromatic-style or plain screenshot diff), which gives you drift detection for UI the same way eval suites give it for prompts (evaluation-practice, era 3). Storybook is where "did the generator respect the design system?" becomes a gate instead of an opinion. Start with stories for the closed vocabulary (≈8 components); that's an afternoon, not a program.

## Where Figma fits (the day-job argument)

Inverted. Figma Make's model is: *their* generator, *their* interpretation, your brand as an import. The owned pipeline's model is: **your tokens are the source of truth; Figma is a consumer** — sync `design-tokens.json` into Figma via Tokens Studio so designers see the same values the renderer uses. Figma stays what it's good at (exploration, high-fidelity moments); it stops being the bottleneck through which every screen must pass. The one-sentence version for the meeting: *"Figma Make renders their guess at our system; this renders our system."*

## "Claude design" — worth trying, in this order

1. **Claude Code + shadcn MCP** (already in V5's pipeline): live component-library access, production React out. This is the Stage-2 workhorse.
2. **Claude artifacts / chat** for the 90-second version of the demo in a room with no setup — paste schema + tokens, get a rendered page. Good theater, not the pipeline.
3. The **composition-JSON authoring step** is model-agnostic by design (BYO-AI, per V5): any vision-capable model can fill a closed schema; the schema does the quality work, not the model. That's the whole point — and it's the experiment's hypothesis (convergence under spec) applied to UI. **The codegen experiment and this pipeline are the same experiment in two domains.**

## How this connects to everything else

- **MockupCanvas (structureview plan)** is this pipeline's authoring surface: draw boxes → the same JSON → this renderer is the reveal. One data model end to end.
- **B1D/B4 lessons** teach humans to produce the JSON; this renders it — the class artifact becomes a working page, which is the strongest "why structure matters" moment the curriculum can buy.
- **The demo file** doubles as the workshop opener: edit one value in the JSON, the page changes; break the schema, the error is visible, not hallucinated. Structure → Quality → Ship, in ninety seconds, on hardware you own.

*Next steps, sized: stories for the 8-component vocabulary (one afternoon); shadcn-MCP Stage-2 spike from one composition JSON (one session); Tokens Studio sync of design-tokens.json into the day-job Figma (one sitting, high politics-to-effort ratio).*
