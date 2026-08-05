# Provenance & Mining — "Spec-Based Development with Agentic Coding" (the genesis paper)

> **What this is.** The owner's paper *Spec-Based Development with Agentic Coding: From Vague
> Prompts to Precision Engineering* (authored 2026-03-30, a synthesis of four AI research sessions
> — ChatGPT, Gemini, Claude, Perplexity — cross-validated against a canonical outline). This is the
> **genesis document** of the QG repo's `docs/specs/spec-instructions.md`. This note records the
> provenance chain, the one material divergence the owner made when implementing it, and mines the
> paper for two owner-flagged streams: **[SVD] article candidates** and **[LP] learning rungs**.
>
> Keys (see FLEET-REPO-BLUEPRINTS.md Part 0.5): **LP** learning platform · **SVD** StructureView
> Desktop · **QG** Quality Guardian · **BK** the book · **EL** Evolution Library.
> Source paper on disk: `uploads/Spec-Based-Development-Comprehensive-Paper.md`.

---

## 1. Provenance chain

```
JTBD/spec research (4 AI sessions, early 2026)
   ↓  synthesized + outlined by owner
Spec-Based Development Comprehensive Paper  (2026-03-30)
   ↓  operationalized into an authoring standard
QG  docs/specs/spec-instructions.md  (canonical spec format; ADR-2026-04-spec-pipeline-governance-overhaul)
   ↓  the format's checks made into a reader/authoring product
StructureView (SVD/SVV/SVE) — "EARS detection · TIMC scoring · BDD generation"
```

The paper's master pipeline — **Job Story → Spec → Tests → Agent Execution** — is quoted almost
verbatim at the top of `spec-instructions.md` ("Job Story → Example Map → BDD Scenarios → Formal
Spec → Tests → Agent Execution"). The paper is the *why*; the spec-instructions doc is the *how*;
StructureView is the *surface* that reads and scores the result. Three artifacts, one lineage.

**StructureView is Part VII of the paper made into a product.** The app's tagline (EARS detection,
TIMC scoring, BDD generation) maps one-to-one onto §VII.A (EARS), §IX.B (the spec-quality
hierarchy TIMC scores against), and §VII.B (BDD/Gherkin). When someone asks "why does StructureView
check *these* things," the answer is this paper.

## 2. The one material divergence — PR Strategy over Spec Kit's `tasks.md`

The paper (§VI.B / §VI.C) presents the **GitHub Spec Kit** four-phase model with **separate
artifacts**: `requirements.md` → `plan.md` → `tasks.md` → implementation. The owner **kept the
pipeline but collapsed the artifacts**: `spec-instructions.md` defines a **single 10-section spec**
whose **§6 "PR Breakdown"** plus the frontmatter field **`PR Strategy: Spec PR → N implementation
PR(s)`** does the job Spec Kit split across `plan.md` + `tasks.md`.

| Paper / Spec Kit model | What the owner implemented | Why it matters |
|---|---|---|
| Separate `requirements.md`, `plan.md`, `tasks.md` | One spec, ten sections; §3 = design, §6 = PR Breakdown | Single source of truth; fewer artifacts to drift out of sync |
| `tasks.md` checklist of granular work chunks | §6 PR Breakdown: each PR = title, branch, files, acceptance gate, commits | Work is **PR-shaped**, not task-shaped — matches the "house pattern" (small verifiable increments) |
| Four *phases* as four documents | Four ideas as *sections + gates* inside one governed doc | The governance travels with the spec, not across files |

**Kept intact from the paper** (do not mistake the divergence for a rejection): the Job Story front
door (§1, with a technology-swap test), EARS notation (§3), Example Mapping + BDD (§4), the
constitution pattern (`AGENTS.md` / `.claude/SOUL.md` / `CLAUDE.md` = the paper's
`constitution.md` + `guidelines.md` + Three-Tier Boundaries), ADRs as the decision backbone (§9),
living-spec obligation (§6 of the instructions), and CI-as-oracle (the `quality-gate` acceptance
criterion). The **Spec Type taxonomy** (stream-aligned / platform / complicated-subsystem /
enabling, S71) is an owner extension *beyond* the paper — Team Topologies mapped onto spec
artifacts.

**Teaching value of the divergence itself:** this is a clean, real example of *adapting a published
methodology to your constraints instead of cargo-culting it* — the anti-cosplay rule in action. It
belongs in the book (BK) as a sidebar and in the fluent/native curriculum as "how to adopt SDD
without adopting someone else's file layout."

## 3. [SVD] Article candidates (StructureView thought-leadership / demand signal)

Each pairs a paper finding with the StructureView feature that embodies it. These are marketing +
credibility pieces — the "marketing legs" the owner wanted. **Verify every statistic (see §5)
before publishing.**

| # | Working title | Hook (from paper §) | StructureView tie-in |
|---|---|---|---|
| A1 | **"Why your AI agent drifts: the 600-PR study"** | Alignment loss during execution beat bad task descriptions as a failure cause (§III.C) | SVD scores spec clarity *before* the agent drifts |
| A2 | **"EARS: five sentences that make a requirement machine-readable"** | The five EARS patterns from safety-critical aerospace (§VII.A) | SVD's EARS **detection** — the headline feature |
| A3 | **"19% vs 87%: the 4.5× accuracy gap is your spec"** | Multi-file AI accuracy 19.36% unstructured vs 87.2% single-function (§VIII.D) | SVD/TIMC turns "is this spec good enough" into a number |
| A4 | **"The spec *is* the test"** | Gherkin = executable spec, kills doc drift (§VII.B) | SVD's BDD **generation** from EARS |
| A5 | **"Vibe coding gets you 70%. The other 30% is the debt."** | The 70/30 structural-decay problem (§I.B) | The land-and-expand case for a spec reader |
| A6 | **"Spec review is the new code review"** | Catch problems before implementation, when cheapest (§V.B, §XI) | SVD as the spec-review surface (cross-file, TIMC) |
| A7 | **"Your JSON has a rubric now"** (ties to the TIMC-rubric backlog item) | The six-level spec-quality hierarchy (§IX.B) | TIMC Light scoring; artifact-type-aware rubric |
| A8 | **"Lost in the middle: why big specs make agents dumber"** | Attention favors head/tail; decompose specs (§X.B, §XIII.B.1) | The context-engineering EL entry; SVD's per-doc focus |

Candidate order by ease/impact: **A2, A3, A5** first (product-defining, vivid numbers), then **A1,
A4, A6**, then **A7, A8** (deeper, pair with the Evolution Library).

## 4. [LP] Learning Rungs (paper → maturity tiers → staircase)

Mapping paper concepts onto the four-tier model (Aware→Enabled→Fluent→Native) and the staircase
rung rule (1 plain / 2 patterned / 3 structured). These are **lesson candidates**, not committed
lessons — a clarify-step for the weekly review and BACKLOG grooming.

| Tier | Rung | Lesson candidate (from paper §) | Behavior it builds |
|---|---|---|---|
| **Aware (A)** | 1 | *What a spec is, and why "vibe coding" hits a wall at 70%* (§I.B) | Names the failure they've already felt; no jargon |
| **Aware (A)** | 1 | *The Job Story front door: "When… I want to… so I can…"* (§IV.B) | Writes intent as motivation, not solution |
| **Enabled (B)** | 1–2 | *EARS in five patterns* (§VII.A) | Turns a vague line into a checkable requirement |
| **Enabled (B)** | 2 | *Example Mapping in 30 minutes* (§VII.D) | Surfaces edge cases before code (red-card discipline) |
| **Enabled (B)** | 2 | *BDD: the spec that runs* (§VII.B) — pairs with B1D UI-surfaces | Given/When/Then as the bridge to tests |
| **Fluent (C)** | 2–3 | *Spec packages & the governance gate* (§V.B) | Chooses spec-review over code-review for consequential work |
| **Fluent (C)** | 3 | *The six-level spec-quality hierarchy* (§IX.B) | Self-scores a spec; knows what "good" means |
| **Fluent (C)** | 3 | *Three-tier boundaries: Always / Ask-first / Never* (§VI.D, §X.D) | Bounds agent blast radius on purpose |
| **Fluent (C)** | 3 | *Lost-in-the-middle: decomposing specs for the context window* (§X.B) | Sizes work to the model, not the wish |
| **Native (D)** | 3 | *SDD at scale: ADRs, living & adaptive specs* (§XII) | Runs specs as a closed feedback loop |
| **Native (D)** | 3 | *Governing a multi-agent team: role bundles + anti-patterns* (§XIII.B) | Designs constitutions, not prompts |
| **Native (D)** | 3 | *Learning loops for agents: PDCA / DMAIC / ExpeL* (§XIII.D) | Deming-for-agents — the kernel thesis |

Notes for grooming: the Aware/Enabled rungs (Job Story, EARS, Example Mapping, BDD) likely *already
overlap* existing A/B lessons — check for duplication before authoring, and prefer extending. The
Native-tier items are architect-track / Quantic-MSAIE-adjacent and overlap the existing
`teasers.json` interest-capture cards; wire demand signals rather than building on spec.

## 5. Guardrail — source independence, and every statistic's primary source

**Source independence is compromised — do not cite four-way convergence as validation (owner,
2026-07-15).** The paper presents itself as "four independent AI research sessions... cross-validated
against the canonical outline," and its body repeatedly leans on convergence ("all four source
documents converge on the same root cause") as if agreement were evidence. **It isn't, here.** The
sessions ran in a shared Perplexity Space carrying CCQG context from older chats; ideas seeped
across. Convergence among sources that share contaminated context is **an echo, not corroboration**
— the same claim reflected four times.

This does not falsify the claims; it removes *four-way agreement* as a reason to believe them. Each
claim must stand on its own primary source. **Rule going forward: context persistence is a feature
when building and a bug when verifying.** A Space grounds work (seepage = helpful); it must never be
used to corroborate work (seepage = manufactured consensus). A second opinion is only worth
something from a witness who wasn't in the room.

*(Corollary, and it strengthens the §XIII cold open rather than weakening it: the session that "went
rogue" and produced an architecture blueprint did so because CCQG context was **in its Space** — not
intuition. That is precisely the thesis — rich contextual grounding yields a precise spec instead of
vague guidance. Tell the honest version in the book; it's the better one, and it's self-aware.)*

### Every statistic needs its primary source before publishing

The paper is rich with numbers (McKinsey 30–40% time-to-market; GitHub 84% build-rate; UC
Berkeley/Canva 85% cost cut; the 55.8% Copilot figure; the 19.36% vs 87.2% gap; the 19% RCT
slowdown; ODI's 86% success rate; etc.). These are **cited third-party research**, not the owner's
day-job numbers — so they are usable in FlowTrain/book content **with attribution**. But per the
anti-cosplay / no-unverified-stats rule: **before any of these ship in a FlowTrain lesson, article,
or book chapter, verify each against its primary source** (the paper is a synthesis, not the
origin). Treat the paper's citations as leads to check, not facts to quote. Day-job actuals remain
out of scope entirely (delicate-dance rule).

## 6. The original intent — the 4am "why," and the day-job loop it closes

**Why this document was pulled at all.** The owner went looking for this paper at 4am to answer a
real operational ask from the day job (a large regulated enterprise, anonymized — delicate-dance
rule, no numbers): *how do we automate work management so people spend less time manually moving
tickets in Jira?*

**The answer was already in §IX.A.** The integrated pipeline (Discovery → Specification →
Governance → Agentic Implementation) is not just a build process — **every arrow is a state
transition a machine can detect.** In a mature flow, a ticket's status is a **projection of
artifact state**, not a card a human drags:

- Spec passes the **Spec Review / governance gate** → ticket → *Ready*
- **CI/CD gates** go green (SAST/DAST/tests) → ticket → *In Review*
- **HITL sign-off** recorded → ticket → *Done* (and the sign-off becomes SOX/FINRA evidence exhaust)

**The reframe:** Jira-hygiene debt is a *symptom*; the disease is that ticket state is
human-maintained instead of artifact-derived. Make status a function of the artifact reaching a
gate, and "moving tickets" stops being a category of work — the loop the owner has been chasing.

**Fleet homes (the day-job ask and the product are the same shape):**

- **SY — Switchyard** (workflow routing & arbitration): the product surface for artifact-driven
  status transitions.
- **DP — Dispatch** (planning & sprint orchestration): consumes the transitions.
- **QG** gates + the **evidence-ingestion contract** (`docs/evidence-ingestion-contract-plan.md`):
  the state signals *and* the provenance a regulator can follow.
- **The Jira Trojan Horse** (FLEET-REPO-BLUEPRINTS.md Part 2.5): distribution — live *inside* Jira
  via the Atlassian Marketplace so adoption rides existing muscle memory instead of fighting it.

**Book tie-in (BK):** this is the bridge from the cold open (§ below / the "session that proved the
thesis by ignoring the prompt") to the thesis. Governance as *artifact state*, not manual
coordination. Working line: *"Stop moving tickets. Start earning transitions."* The 4am story and
the day-job ask are the same story — the reader learns the pipeline is an answer to a problem they
have at work, not an academic diagram.

**Confidentiality:** the day-job ask is recorded here only as a generic operational goal. No client
identity, no volumes, no defect rates, no dollar figures — model with the public exemplar if this
becomes lesson/article/book content.

## 7. Homes for this material

- **QG:** the divergence (§2) is already reality in `spec-instructions.md`; if the working QG repo
  wants a provenance breadcrumb, add a one-line "Genesis" note atop that file pointing here. (Not
  done from this session — the QG copy on disk is a read-only audit clone.)
- **BK:** §2 (adapting SDD, not cargo-culting it) and §5's kernel thesis feed Part II.
- **LP:** §4 is BACKLOG grooming input.
- **SVD:** §3 is the content pipeline; top three to `inbox.md` now.
- **EL:** §3-A7/A8 pair with the token-economics and context-engineering entries.
