# The Curation Model — Evolution Libraries

## The problem this solves

AI practice has a shelf life. CREATE was the gold standard for prompting in a pre-GPT-4.5 world; today, micromanaged procedural prompts actively *hurt* frontier-model performance, while remaining essential for small local models. A learning platform that teaches practices as static truths will be quietly wrong within two model generations — and worse, learners can't tell which of their habits are current and which are 2022 fossils.

The Evolution Library treats **practices as versioned, curated entities**. Each entry shows a practice's eras, what changed between them, why (what model capability shifted), what is now deprecated, and what the current guidance is. Lessons cite library entries instead of embedding claims, so when practice evolves, the correction happens once, in the library.

## Entry anatomy

Every entry in `library/evolution/` follows this structure (schema: `content/schemas/evolution-entry.schema.json`):

```yaml
---
id: prompting-frameworks          # kebab-case, stable forever
practice: Prompt Engineering       # the practice being tracked
status: current                    # current | watch | superseded
last_reviewed: 2026-07-10
review_cadence: quarterly          # how often a curator must re-verify
model_generations: [gpt-3.5/4-era, gpt-4.5+/5.x-era, frontier-2026]
referenced_by: [A2, A3, C1]        # lesson ids that cite this entry
curators: [<owner>]
---
```

Body sections, in order:

1. **Current guidance** — what we teach *today*, first. A learner in a hurry reads only this.
2. **Eras** — one section per era: the practice as it was, the model context that made it right, and the shift that ended it.
3. **Deprecated patterns** — explicit "stop doing this" list with the reason. This section is the library's highest-value output: it names the fossils.
4. **What survived** — elements of older practice that remain valid (nothing gets strawmanned; CREATE's elements remain sound even though its procedural framing is obsolete).
5. **Boundary conditions** — where the old practice is *still* correct (e.g., rigid CREATE-style prompts remain essential for small local models that lack frontier reasoning; multi-model orchestration uses both paradigms simultaneously).
6. **Signals to watch** — what would trigger the next era (model capability, vendor guidance, measured behavior change).
7. **Sources** — dated, so staleness is visible.

## Editorial workflow

| Step | Who | What |
|---|---|---|
| Propose | Anyone | Open a stub with the practice name and the observed shift. |
| Draft | Curator | Write eras + deprecated list; every claim dated and sourced. |
| Challenge | Second Tier 3/4 reviewer | Try to break the "deprecated" claims — is the old pattern truly obsolete, or just obsolete *for frontier models*? Boundary conditions come from this step. |
| Publish | Curator | Merge; update `referenced_by` lessons if guidance changed materially. |
| Review | Curator, per `review_cadence` | Re-verify against current models. Touch `last_reviewed` even when nothing changed — an untouched date is the staleness alarm. |

## Why this is a platform feature, not a doc folder

- **Lessons stay thin and durable**: they teach the skill; the library carries the volatile "current best practice" layer.
- **Maturity signaling**: reading library entries is a Tier 2→3 behavior; *curating* them is Tier 3; *defining what gets tracked* is Tier 4. The library is itself a maturity ladder.
- **Institutional memory**: "why did we stop teaching X" has an answer with a date on it, which is exactly what an enterprise governance conversation needs.

## The entry admission test (anti-cosplay rule)

The article stream mints a new "___ Engineering" weekly (harness engineering, memory engineering, loop engineering...). A claimed discipline earns a library entry **only if it changes what a practitioner does on Monday morning**. If it renames what an existing entry already tracks, it is *absorbed* — added as an era detail or terminology note in the existing entry — never minted. Absorption is a curation act worth recording: note the rebranded term in the absorbing entry so learners who meet it in the wild can find their footing. Applied 2026-07-10: harness engineering → evaluation-practice (era 3); memory engineering → context-engineering (Write verb); loop engineering → agent-orchestration (review loops).

A second bias to curate against: the firehose is development-centric, so an unwatched library drifts toward builder practices. Product-side and governance-side practices evolve just as hard but publish quieter — they must be sourced deliberately (owner research, regulatory guidance, practitioner accounts), not skimmed from the stream.

## Founding entries (build order)

1. `prompting-frameworks` — CREATE → outcome-first / CREATE+ / context engineering. **Done** (first entry, from the founding research).
2. `structured-outputs` — prose formatting asks → JSON-mode → schema-enforced contracts; the reason-then-format trade-off. **Done** (2026-07-10; cited by B4, D1).
3. `context-engineering` — stuff-the-prompt → RAG → curated just-in-time context; U-shaped attention findings and placement rules. **Done** (2026-07-10; cited by B1, B1E, C4).
4. `agent-orchestration` — single chat → chains → multi-agent (planner/implementer/tester/reviewer); where the value moved. **Done** (2026-07-10; cited by A3, A3E, C1, D1).

**All six founding entries published as of 2026-07-10.** The "living library" claim is now credible per the 4–6 entry threshold above; the open work shifts from founding to operating — quarterly reviews per `review_cadence`, and Challenge-step second reviewers from the owner's practitioner bench (see `docs/open-questions.md`).

## Second cohort: product & governance entries (proposed 2026-07-10)

The founding six all serve the builder. These serve the product organization — the shift-left the platform's own audience needs. Propose-stage stubs in `specs/drafts/`:

7. `shift-left-economics` — Boehm's cost-of-defect curve in the AI era. **Drafted** (2026-07-11; cited by B3, C5, D5; Challenge pending — thesis confirmed by DORA 2026: specification and verification are the scarce resource; the curve twisted, it didn't flatten).
8. `ai-product-discovery` — discovery and customer centricity with AI. **Drafted** (2026-07-11; cited by B2, B2D; Challenge pending — key findings: synthetic-user sycophancy, 97% adoption vs 8% trust, "category mistake" academic position).
9. `ai-business-cases` — how AI work gets funded and justified as practice evolves: per-seat → per-workflow (D5's layer) → capability portfolios; value evidence vs. adoption theater.
10. `regulatory-practice` — technology-neutral regulators ("existing rules fully apply to AI"): HITL as a *control*, traceability/auditability (21 CFR Part 11 parallels), compliance requirements as user stories/NFRs. Founding source: `research/navigating-the-black-box.md` (owner conference material, 2026) + FINRA/SEC guidance. **Owner-authored entry — this is his domain.**
5. `evaluation-practice` — "seems right" → rubrics → eval harnesses and drift detection. **Done** (2026-07-10; cited by B3, C1, D1; the platform's own assessment design is the internal case study).
6. `token-economics` — flat pricing intuitions → caching, model-tiering, refinement-first discipline. **Done** (2026-07-10; founded on three owner research docs in `research/` + parked open-questions claims; cited by A4, A2E, C2, C5).