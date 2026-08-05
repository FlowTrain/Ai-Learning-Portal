---
id: shift-left-economics
practice: Cost-of-Change / Shift-Left Economics
status: current
last_reviewed: 2026-07-11
review_cadence: quarterly
model_generations: [boehm-era, agile-cheap-change-era, spec-and-eval-era-2026]
referenced_by: [B3, C5, D5]
curators: [platform-owner]
---

# Evolution Entry: Shift-Left Economics (Boehm's Curve → Cheap Change → Specs and Evals as the New Left)

## Current guidance (teach this today)

The curve didn't flatten — **the cost moved from rework to review, and "the left" moved from documents to machine-checkable artifacts.** Current working rules:

- **Detection timing still dominates cost.** 2026 industry figures hold the classic shape: a defect caught at unit/coding stage costs on the order of $25; the same defect in production runs $10,000+ — and in regulated domains the right end of the curve isn't a bug ticket at all, it's an enforcement action (a misleading AI-generated customer communication is a FINRA 2210 problem, not a hotfix).
- **Generation is cheap; validation is the scarce resource.** The DORA 2026 finding, stated plainly: as AI accelerates code generation, the bottleneck shifts to specification and verification — they are no longer overhead but the constraint. Teams measuring the full picture report AI-assisted first-year costs running ~12% *higher* than baseline once review overhead (~9%), a ~1.7× testing burden, and ~2× code churn are counted (as of 2026 — see Sources; re-verify, these are young numbers).
- **The new left is specs, evals, and HITL gates.** Requirements documents were never machine-checkable; tests checked code after it existed. The current form: specs precise enough to generate and judge against (the spec pipeline this platform runs on), eval gates that block shipment (evaluation-practice, era 3), and human-in-the-loop review placed by risk tier (D6) where stakes demand it. Approve the spec and the artifact is mechanical; skip the spec and you're paying the validation tax with interest, later, in production.
- **Spend review effort where regeneration can't save you.** "Just regenerate it" is a real strategy for reversible, low-stakes work (see Boundary conditions) and a cost multiplier everywhere else — churn data says regenerated code that was never specified gets regenerated again.

## Eras

### Era 1 — Boehm's curve (~1981–2000s)

The founding empirical result: cost-to-fix grows dramatically with each lifecycle phase between introduction and detection. The practice consequence was heavy front-loading — big requirements documents, formal reviews, change control — because *change itself* was expensive and late change was ruinous. Right conclusion, heavy instrument: the left was paper.

### Era 2 — Agile's cheap-change critique (2000s–2023)

Iterative delivery, automated tests, CI, and refactoring tooling genuinely flattened the middle of the curve for reversible software — the "cost of change curve is outdated" position had real evidence behind it. The left migrated from documents to *executable* checks: TDD, CI gates, trunk-based flow. The era's honest core: when change is cheap and reversible, betting on adaptation beats betting on prediction. Its overreach: treating the flattening as universal — it never applied to the irreversible right end (data loss, customer harm, compliance), and it assumed a human wrote and understood every line.

### Era 3 — AI generation and the validation squeeze (2024–2026)

Code became nearly free to produce and the curve responded by *twisting*, not flattening: writing cost collapsed while validation cost grew to absorb it. Measured 2026 reality: higher defect and churn rates in AI-generated code with problems surfacing disproportionately *after* release; net first-year costs above baseline once review and testing burdens are counted; DORA naming specification and verification as the new constraint. The response is the reconstituted left — specs as quality gates (generate *from* the spec, judge *against* it), eval harnesses in CI, compliance requirements entering sprints as explicit user stories/NFRs (compliance by design — the owner's Black Box material is the regulated-industry playbook for exactly this). Boehm's insight survives translated: **the cheapest place to catch a defect is now the spec review, because everything downstream of the spec is generated volume.**

## Deprecated patterns (stop teaching these)

- ❌ **Heavy documents as the shift-left instrument** — paper isn't machine-checkable; a 40-page requirements doc shifts blame left, not defects.
- ❌ **"Just regenerate it" as a universal defect strategy** — 2× churn is the measured cost of regenerating unspecified work; regeneration without a spec re-rolls the dice, it doesn't fix them.
- ❌ **Code-volume and speed metrics as productivity** — generation speed measures the cheap part; unvalidated velocity is inventory, not throughput.
- ❌ **Skipping the spec because the code is cheap** — inverts the actual economics; the spec is now the highest-leverage artifact precisely *because* the code is cheap.
- ❌ **Treating the flattened curve as universal** — Agile's flattening applied to reversible change; the irreversible right end (production data, customers, regulators) is steeper than the 1981 original in consequence terms.

## What survived

Boehm's core finding survives fully: detection later costs more, and 2026 production-defect figures still trace his shape. Agile's contribution survives as a boundary condition rather than a refutation: cheap reversibility genuinely flattens the middle for low-stakes work, and iterative delivery remains the right default. The through-line across all three eras: **move the checkable thing as early as possible** — it was reviews, then tests, now specs and evals. This platform is its own case study: the module spec's Definition of Ready catches a mis-pitched lesson at spec time (minutes) instead of after an authoring session (hours) or a confused cohort (weeks).

## Boundary conditions (where older practice is still correct)

- **Reversible, low-stakes, internal work:** regenerate-and-move-on is legitimately fine; imposing spec ceremony on a throwaway script is Era-1 cosplay. The curve is genuinely flat where undo is genuinely free (D6's read-only/reversible tiers make the boundary operational).
- **Prototypes and spikes** are exempt by purpose — their deliverable is learning, not artifact durability. Mark them as spikes and never promote them silently (the S69-style disposition step is the promotion gate).
- **Agile-era test-first practice remains the correct left for human-written code** — the spec-and-eval left is *additive* where generation enters, not a replacement for TDD where it doesn't.

## Signals to watch (would trigger Era 4)

- Validation itself becoming reliably automatable (self-verifying generation with trusted evals) — would collapse the review bottleneck and genuinely flatten the middle again.
- Measured AI defect/churn rates converging to human baselines (vendor-claimed every quarter; verify against DORA-class longitudinal data, not marketing).
- Regulatory regimes pricing post-delivery AI defects explicitly (fines schedules) — would let the right end of the curve be modeled in dollars instead of argued.

## Sources

- Boehm, *Software Engineering Economics* (1981) — the founding curve; [historical cost-to-fix adaptation](https://www.researchgate.net/figure/Historical-cost-to-fix-curve-Adapted-from-Boehm-1981-p-40_fig11_308264787).
- [The Cost of Change Curve Is Outdated](https://www.mountaingoatsoftware.com/blog/the-cost-of-change-curve-is-outdated) (Mountain Goat Software) — the era-2 critique, pre-AI.
- [The Cost of a Production Bug in 2026](https://getautonoma.com/blog/cost-of-production-bug) (2026) — $25 unit → $10K+ production escalation, current figures.
- [The Hidden Costs of AI-Generated Code in 2026](https://www.codebridge.tech/articles/the-hidden-costs-of-ai-generated-software-why-it-works-isnt-enough) and [AI-Generated Code Quality Metrics 2026](https://www.secondtalent.com/resources/ai-generated-code-quality-metrics-and-statistics-for-2026/) — ~12% net first-year cost increase, ~9% review overhead, ~1.7× testing burden, ~2× churn.
- [2025 was the year of AI speed; 2026 will be the year of AI quality](https://www.coderabbit.ai/blog/2025-was-the-year-of-ai-speed-2026-will-be-the-year-of-ai-quality) (CodeRabbit, citing DORA 2026) — specification and verification as the scarce resource.
- [The Specification as Quality Gate](https://arxiv.org/pdf/2603.25773) (arXiv 2603, 2026) — spec-anchored review hypotheses for AI-assisted development.
- `research/navigating-the-black-box.md` (owner conference material, 2026) — regulated-domain right end of the curve: HITL as control, compliance as user stories/NFRs.
