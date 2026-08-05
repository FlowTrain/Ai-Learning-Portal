# Module Spec — Companion Misconceptions (leader / PM-&-non-dev / designer), routed to their tiers

> Source scraps: `research/` briefs *AI Tooling: Common Misconceptions* (§2 leadership, §3 PMs/non-devs)
> and *Skills: Five Misconceptions*; plus the schema-driven-UI "gems" captured from the 2026-08-01
> conversation (UI schema, boundary object, DTCG, contract-first, Figma-as-handoff). Companion to the
> Tier-3 `tooling-misconceptions` module (C6–C8). The briefs span three tiers, so per the no-leap hard
> rule these do **not** form one course — each lands in its home tier. Log seeds M2 (passing check) and
> M3 (usage teaches it) already exist.

## The three companion lessons (each its own home)

| Lesson | Audience / misconceptions | Course | Tier | Rung |
|---|---|---|---|---|
| **D8** | **Leaders:** usage teaches the model (M3); seats deployed ≠ adoption; one tool as the front door for everything (reception desk vs workshop); "which Copilot?" | `leader-literacy` | native (leader literacy) | 2 |
| **A9** | **PMs / non-devs:** the tool feels hard because of *legibility*, not competence; you don't need their dev workflow; a passing check isn't proof (M2) | `aware-foundations` + `aware-eng` | aware | 1 |
| **B5D** | **Designers:** AI doesn't replace design — it replaces the *handoff*; declare the layout as a contract (schema-driven UI) | `enabled-design` | enabled | 3 |

**Hard dependency:** a new Evolution Library entry **`schema-driven-ui`** holding the volatile layer
(UI-schema tooling, DTCG version, the contract-first vocabulary) that B5D cites via `libraryRefs`.
Write it before B5D authors. Details at the end of this spec.

---

## Lesson D8 — "What Leaders Get Wrong About AI"

**Identity:** id `D8` · courseId `leader-literacy` · tier `native` · roleIds `[leader]` · 20 min · rung **2**.

**Concept (one sentence):** Four leadership beliefs that misdirect AI investment — that usage accrues
institutional knowledge, that deployed seats equal adoption, that one tool can be the front door for
everything, and that "Copilot" is one thing.

**Ancestry (verified in staircase-map):** rung-1 A8 (*what the model works from* — weights are frozen,
context is supplied) and A4 (tool selection & cost, leader in roleIds); rung-2 D5/D6 (leader literacy).
D8 sits at rung 2 with D5/D6 — literacy altitude, deliberately not architect vocabulary.

**Observable behaviors:** *Tier 2/4-literacy:* directs AI investment to context/standards/documents
rather than to usage volume; measures adoption by completed non-engineer work product, not seats.

**Artifact:** `ai-investment-read.md` — for one planned AI spend, a one-page read: where the value
actually accrues (docs/context vs. "the model will learn us"), the adoption measure that means
something (work finished by non-engineers), and a front-door-vs-workshop call (is this reception-desk
Q&A or artifact-building?).

**Claims & sources:** static weights / no learning loop → cite `agent-skills-format` and A8 (stable
principle). "Which Copilot?" (GitHub vs M365 differ) is **volatile** → route to an Evolution entry or
`docs/open-questions.md`; do not embed vendor specifics in the lesson.

**Sections:** Start Here (name your last AI investment and its assumed payoff) → Usage doesn't teach it
→ Seats aren't adoption → Front door vs. workshop → *Assignment*.

---

## Lesson A9 — "You're Not Behind"

**Identity:** id `A9` · courseId `aware-foundations` (+ `aware-eng`) · tier `aware` · roleIds
`[pm, coach, designer, leader, engineer, tl, data]` · 20 min · rung **1**.

**Why this lesson exists:** it answers the cohort finding head-on — *"people don't believe they'll make
it past this stage."* The blocker is usually not competence; it's that opaque tools give no signal of
state, so people read the tool's silence as their own failure.

**Concept (one sentence):** When a tool feels "too technical," the problem is almost always
legibility (no undo, no visible state, no signal of whether it's working) — not your ability — and a
check that passes is not proof the answer is right.

**Ancestry:** this is a **rung-1 lesson** (plain language, no JSON/schema). Companions A0 (first win)
and A6 (a passing/absent check isn't proof — M2). It strengthens the Level-1 "destination, not waiting
room" goal from BACKLOG 11.

**Observable behaviors:** *Tier 1:* names one state question they couldn't answer ("is it working? did
it finish? does it need me?") instead of concluding they can't use the tool; treats a clean-looking
output as a draft to check, not a verdict.

**Artifact:** `not-behind.md` — one moment a tool made them feel behind, rewritten as a *state
question* it failed to answer; plus one output they'll re-check before trusting, and how.

**Sections:** Start Here (a moment the tool made you feel dumb) → It's legibility, not you → You don't
need their workflow → A passing check isn't proof → *Assignment*. **Rung-1 guard:** zero JSON, schema,
or tooling vocabulary; the staircase rule applies to the chrome too.

---

## Lesson B5D — "AI Replaces the Handoff, Not the Design"

**Identity:** id `B5D` · courseId `enabled-design` · tier `enabled` · roleIds `[designer, pm, tl]` ·
25 min · rung **3**.

**Concept (one sentence):** AI does not replace design exploration or the shared review surface — it
replaces **Figma-as-handoff-artifact**, because handoff was always a lossy translation; declaring the
layout as a contract (a UI schema referencing a data schema, styled by tokens) removes the guess.

**The gems, made teachable (from the 2026-08-01 conversation):**
- Three named layers: **data schema** (what it is) → **UI schema** (how it's laid out, referencing the
  data schema) → **design tokens** (style). Umbrella term: **schema-driven UI**. (JSON Forms and React
  JSONSchema Form use exactly this data-schema/`uiSchema` pairing.)
- The paste is where the contract disappears: flattened markup forces the model to *re-infer intent
  from pixels* because nothing was declared. The cost isn't keystrokes; it's that the decision was
  never written down and got reconstituted by guess.
- The one artifact three roles coordinate on (spec reader, UI implementer, later API implementer) is a
  **boundary object** — a better frame than "micro-spec" because it says *why* it works.
- Keep the layers separate: domain schema canonical, UI schema references it, API contract generated
  from it — one source, three artifacts (why JSON Forms split them). A single schema serving UI *and*
  API becomes a leaky compromise.
- The "brand-new-Mac, Cmd-V" demo is a tell: a workflow that needs a freshly imaged specific machine
  is a demo under lab conditions, not a process. Worth teaching as a self-check.

**Ancestry (verified in staircase-map):** concept *Describing product surfaces* — rung-1 A1 (Stranger
Test), rung-2 B1D (component language) / B2 (structured context), rung-3 **B4 (schema-first JSON)**.
B5D is a rung-3 depth step past B4 (rung-3→rung-3, allowed), specialized to the UI-schema/handoff case.

**Observable behaviors:** *Tier 2/3:* declares a layout as a UI schema referencing a data schema
instead of pasting flattened markup; can name what the handoff paste silently drops.

**Artifact:** `ui-contract.md` — one real screen expressed as the three layers (a small data schema, a
UI schema referencing it, and which token set styles it), plus one sentence on what the old
paste-the-mockup path left to guess.

**Claims & sources (volatile → `schema-driven-ui` entry, do NOT embed):** JSON Forms / RJSF `uiSchema`;
DTCG reaching first stable version (2025.10, 24+ orgs incl. Adobe/Google/Meta/Figma); server-driven vs
build-time distinction. Stable principles (boundary object, contract-first/design-first, handoff-is-
lossy) can live in the lesson. No client/employer specifics; StructureView may be named as the owner's
tool only in general terms.

**Sections:** Start Here (where did the last design decision actually get decided?) → The handoff was
always lossy → Three layers, three names → The paste is where the contract dies → The lab-demo tell →
*Assignment*.

---

## Dependency — Evolution Library entry `schema-driven-ui`

**Practice:** Schema-Driven UI (declaring layout as a contract). **Status:** current. **Cadence:**
quarterly (the token/tooling layer moves). **Sections (the required seven):** Current guidance · Eras
(paste-the-mockup → design-system components → schema-driven contract) · Deprecated patterns
(single schema for UI+API; handoff-as-phase; pixel-inference from flattened paste) · What survived
(exploration and the review surface stay with design tools) · Boundary conditions (schema-driven fits
build-time declared layouts; runtime = server-driven UI, a different label) · Signals to watch (DTCG
version and adopters; JSON Forms/RJSF conventions; whether tokens are emitted in DTCG format) ·
Sources (W3C DTCG 2025.10 stable; JSON Forms; RJSF). **referenced_by:** [B5D].

---

## Definition of Ready (all three lessons + the entry)

- [x] Ids valid; D8/A9 join existing courses, B5D joins `enabled-design`
- [x] Ancestry verified in `docs/staircase-map.md` — no leap (D8 rung-2 w/ D5/D6; A9 rung-1; B5D rung-3 past B4)
- [x] A9 rung-1 content contains **zero** JSON/schema/tooling vocabulary (chrome included)
- [x] Each artifact is a named file; rubrics to be written per `module-spec-template` §4 at authoring
- [ ] **`schema-driven-ui` Evolution entry written and cited by B5D** (hard dependency — write first)
- [ ] "Which Copilot?" vendor specifics (D8) routed to a library entry or `open-questions.md`, not embedded
- [x] Vocabulary tiered to each lesson's audience, not the owner
