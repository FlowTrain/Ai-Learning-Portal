---
id: schema-driven-ui
practice: Schema-Driven UI (declaring layout as a contract)
status: current
last_reviewed: 2026-08-01
review_cadence: quarterly
model_generations: [paste-the-mockup-era, design-system-era, schema-driven-era]
referenced_by: [B5D]
curators: [platform-owner]
---

# Evolution Entry: Schema-Driven UI (Paste-the-Mockup → Design-System Components → Declared Contract)

The volatile tooling and standards layer for describing a UI as a *contract* lives here, so B5D can
cite it instead of embedding claims that move. The durable idea — declare the layout so intent is a
reviewable file, not a guess reconstructed from pixels — is taught in the lesson.

## Current guidance (teach this today)

- **Three layers, three names.** *Data schema* says what the thing is; *UI schema* says how it's laid
  out, referencing into the data schema; *design tokens* say how it's styled. The umbrella is
  **schema-driven UI**. JSON Forms uses exactly this data-schema/UI-schema pairing; react-jsonschema-
  form calls the layout object `uiSchema` and mirrors the data schema's structure. "JSON Schema tells
  *what*; uiSchema tells *how*."
- **Keep the layers separate, one source.** Domain schema is canonical; the UI schema references it;
  the API contract is generated from it. One source, three artifacts. A single schema serving both UI
  and API becomes a leaky compromise — the API wants normalized/resource-shaped, the view wants
  denormalized/display-shaped. (This is why JSON Forms split them rather than annotating one blob.)
- **Emit tokens in the DTCG format.** The Design Tokens Community Group spec reached its first stable
  version (2025.10, 28 Oct 2025) — vendor-neutral, 20+ contributing orgs (Adobe, Google, Meta,
  Microsoft, Figma, Salesforce, Shopify…), with Style Dictionary v4 support. Target it and you inherit
  the transformation ecosystem instead of inventing a private dialect.
- **It replaces the handoff, not design.** Exploration of visual alternatives and the shared review
  surface stay with design tools. What schema-driven UI replaces is **Figma-as-handoff-artifact** —
  which was always a lossy translation between two representations.
- **The artifact is a boundary object.** One declared layout lets the spec reader, the UI implementer,
  and the later API implementer coordinate without a shared vocabulary — a *boundary object* (design-
  research term), a more useful frame than "micro-spec" because it says *why* it works.

## Eras

### Era 1 — Paste the mockup (~2022–2024)
A design is exported as flattened markup and pasted in; the agent (or the developer) re-infers intent
from pixels because nothing was declared. Sometimes the inference is right; nobody knows which times,
because there's no artifact to check it against. The design decision was never written down.

### Era 2 — Design-system components (2023–2025)
Component libraries and tokens reduced the guesswork by standardizing the pieces, but the *layout* of a
given screen still lived in a canvas and got handed off by translation. The handoff remained a phase.

### Era 3 — Declared contract / schema-driven UI (2025–2026)
The layout itself becomes a declared artifact — a UI schema referencing a data schema, styled by
tokens in a now-stable interchange format (DTCG 2025.10). Intent moves from a designer's head → canvas
→ serialized markup → guessed-back, to a file that is reviewable, diffable, and wrong in ways someone
can point at. Handoff stops being a phase rather than merely getting faster.

## Deprecated patterns (stop teaching these)

- ❌ **Paste flattened markup and let the model infer intent** — the contract disappears at the paste.
- ❌ **One schema serving UI and API** — a leaky compromise that satisfies neither.
- ❌ **Handoff as a phase** — if the layout is the contract, there is nothing to translate.
- ❌ **Private token dialects** — a bespoke token format forfeits the DTCG transformation ecosystem.
- ❌ **The lab-conditions demo** — a workflow that only survives on a freshly imaged, specific machine
  (the brand-new-Mac, Cmd-V demo) is demonstrating a *tool*, not a *process*. Treat it as a tell.

## What survived

Design's real work survived wholesale: divergent exploration and the stakeholder review surface are
things a schema does not do and a design tool still should. Tokens survived and got a standard. What
changed is where *intent* lives — from a canvas that gets translated to a contract that gets referenced.

## Boundary conditions (where older practice is still correct)

- **Exploration still belongs on a canvas** — schema-driven UI is for the layout you've *decided*, not
  the ten you're weighing.
- **Build-time vs runtime matters.** Schema-driven UI here is *build-time* declared layout. If the
  layout is delivered and interpreted at runtime, that's **Server-Driven UI** — a different label with
  different tradeoffs; don't conflate them.
- **Small static screens may not need it** — the contract earns its keep when a UI, an API, and a spec
  reader must stay in sync over time.

## Signals to watch (this entry will move)

- DTCG version and adopter list; whether your design tool emits DTCG-format tokens natively.
- JSON Forms / react-jsonschema-form conventions (the `uiSchema` shape) as they evolve.
- Whether "UI schema" consolidates around one cross-tool spec or stays library-specific.
- StructureView's own JSON layout activity (owner tooling) as a producer of these artifacts.

## Sources

- W3C Design Tokens Community Group — "Design Tokens specification reaches first stable version"
  (2025.10, 28 Oct 2025). https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/
- JSON Forms — data schema + UI schema pairing (jsonforms.io).
- react-jsonschema-form — `uiSchema` API (rjsf-team.github.io).
- Boundary object — Star & Griesemer (design/CSCW research term).
- Contract-first / design-first — OpenAPI practice.
- Verified 2026-08-01 (DTCG stable version + the JSON-Schema/uiSchema pairing).
