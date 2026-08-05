# Assessment — Agentic PRD-to-Spec Bridge (v1.0, July 2026)

> **Status:** Owner says *"nothing final yet — starts to bridge the spike into the lineup."* This
> note is the read: what it closes, what collides, what the owner must decide. Source doc preserved
> at `research/agentic-prd-to-spec-bridge.md` (same 4-session synthesis pattern as the genesis
> paper — ChatGPT/Gemini/Perplexity/Claude + canonical outline). Keys per FLEET-REPO-BLUEPRINTS
> Part 0.5. **Nothing here is authored into a repo; this is Propose-stage reading.**

---

## 1. What it closes — "the left side of the puzzle"

FLEET-REPO-BLUEPRINTS Part 0 names the product lifecycle as *"the left side of the puzzle, still
forming"* and lists four things it needs. This draft delivers three of them:

| Blueprint's stated need | This doc's answer | Status |
|---|---|---|
| Pragmatic Marketing as the *workflow*, its artifacts as the *forms* | The **Depot** aggregating **Seven Pragmatic Tracts** (Market, Focus, Business, Planning, Programs, Enablement, Support); PRD template = the forms | Drafted |
| Venture-style **risk & funding approval gates** | The Risk Validation Matrix + **Before-SPEC Readiness Gate** (PASS / CONDITIONAL PASS / FAIL) | Drafted |
| **SOX-grade evidence out of HITL sign-offs** | **Chain of Custody**: approver ID + timestamp cryptographically bound to the spec's commit hash; 7-yr FINRA 4511 retention; HITL required for compliance-critical domains | Drafted |
| **Critical Chain Product Management** (buffer discipline remixed from projects to products) | **Absent** — no buffer/CCPM concept anywhere in the draft | **Gap** |

**Read:** the left side went from *forming* to *drafted, with one hole*. CCPM is the missing
quarter — and it's the one that would make the gates *economic* rather than just procedural
(buffers are how you decide what waits, which is the Reinertsen/Goldratt half of your kernel). Worth
naming as an explicit open question rather than letting it quietly vanish.

## 2. The catch — segment numbers collide (fix before authoring anything)

The doc proposes **S73 / S74 / S75** for bridge / workbench / agent-skills. Those numbers are
**already taken** in the QG register (`spec-instructions.md` §8):

| Doc proposes | QG register already has |
|---|---|
| S73 — prd-to-spec-bridge-and-readiness-gate | **S73 — WORM-Compliant Audit Storage & Custom RBAC Roles** |
| S74 — discovery-workbench-prd-authoring-ui | **S74 — PPTX Report Delivery Agent** |
| S75 — discovery-bench-agent-skills | **S75 — PM Presentation Intelligence Platform** |

Register says: highest = **S80**; next available = **S81**, already reserved for the TIMC Light
spec-health port (#398). So the bridge trio needs **S82 / S83 / S84** (or a decision to unreserve S81).

**Two more collisions in the same doc:**

- It calls the Discovery Agent **"S41"** and lists `S41-discovery-workbench-agentic-forms.md` — but
  the register has **S41 = QMS Controls (RCA + CAP + HITL), Complete**. Different thing entirely.
- Cross-repo: StructureView already carries its own
  `docs/S73-structureview-spec-authoring-and-quality-antagonist.md`, colliding with QG's S73.

**This is the exact failure the context keys were invented for** (Part 0.5, 2026-07-14). Renumber
the trio *and* key them — `QG-S82/83/84`, `SVD-S73` — and cross-repo collision stops being
structurally possible. The bridge doc is unintentionally the best argument for the keys yet.

## 3. Internal inconsistency — the "Four-Risk Matrix" has five rows

The matrix lists **Desirability · Viability · Feasibility · Usability · Compliance/QMS** = five. The
prose says *"All four dimensions must reach threshold."* The first four are Marty Cagan's canonical
product risks; **the fifth is the owner's addition — and it is the entire differentiator.**

**Recommendation:** rename to *"The Four Risks + the Fifth: Provable Control"*, and say plainly that
four are Cagan's and the fifth is what a regulated enterprise adds. Two wins: honest attribution
(anti-cosplay rule), and the moat stops hiding inside a table row. *Everyone* has Cagan's four. The
fifth is why FlowTrain exists.

## 4. Decisions the owner owns

- **BMAD dependency.** The draft leans hard on BMAD — named personas (Mary/John/Winston/Amelia/
  Sally/Paige), v6 scale-adaptive levels, epic sharding. **Same question as Spec Kit**, and you
  already answered that one: keep the *pattern*, drop the branded file layout. Precedent says keep
  epic-sharding + the Verifier/Implementor split (both genuinely good), drop the persona names —
  you have SOUL.md/AGENTS.md; you don't need someone else's cast.
- **"LLM Wiki" — is it new, or a rename of what's built?** Layer 1 (immutable raw sources) ≈ WORM
  storage (QG-S73) + evidence bundles. Layer 2 (compiled, agent-maintained wiki) ≈ **S70 — Fleet
  Audit Intelligence: Knowledge Base, Wiki Synthesis & Learning Loop, already Complete.** Layer 3 ≈
  the constitution (CLAUDE/AGENTS/SOUL). **Do not build a second one.** Decide whether "LLM Wiki" is
  vocabulary for S70+S73 or a genuinely new segment. (Blueprints also warn: don't rebuild Obsidian;
  keep the personal Second Brain out of the enterprise product.)
- **Depot / Turntable naming.** Turntable Hub is **S38 (Complete)**. Discovery Bench Coupler is
  **S80**. Is "the Depot" a new surface or a rename of the Discovery Bench? Third name-collision risk.
- **Home repo.** The method (enabling) → QG. The Workbench UI (stream-aligned) → Roundhouse shell or
  SVE? That's a real fleet boundary call, not a detail.

## 5. Connections to live threads (this session)

- **Intent = Marquet's clarity pillar.** The doc's core tenet — *"the PRD is the intent layer; the
  spec is the execution layer"* — plus GitHub's *"intent is the source of truth"* is exactly
  intent-based leadership rendered as artifacts. **The PRD is how you give an agent clarity before
  you give it control; the Before-SPEC Gate is the "I intend to…" checkpoint.** The kernel's Marquet
  row (Part 0) now has a concrete mechanism.
- **Artifact-driven workflow ([SY], provenance §6).** The PRD Status enum (Draft → In Discovery →
  Stakeholder Review → Approved → **Spec-Seeded** → Closed) plus gate verdicts *are* state
  transitions **earned by the artifact**, not dragged by a human. This draft operationalizes *"stop
  moving tickets, start earning transitions"* on the discovery side, and the Chain of Custody is the
  evidence exhaust falling out of it. Strong confirmation of the day-job answer.
- **The "Fireman" pattern** (business user, Git-less guided front door) = familiarity-as-distribution
  = the **Jira Trojan Horse** (Part 2.5). Same insight, different door.
- **Spec Seed = the anti-lossy-handoff artifact.** *"A Spec Seed must not invent missing PRD
  context"* is the CCQG Auditor's diagnose-only / never-fabricate posture applied **upstream**. Same
  discipline, new position on the line.
- **Shift-left economics.** The defect-cost multiplier (~$100–250 in discovery vs ~$10k–25k in
  production) is the load-bearing claim of the `shift-left-economics` EL entry.

## 6. Verification guardrail (same rule as the genesis paper)

**Source independence is compromised — the four-way convergence is an echo, not corroboration
(owner, 2026-07-15).** This doc uses the same four-session pattern *and the same shared Perplexity
Space*, which carried CCQG context in from older chats. That seepage is visible in the draft: it
already "knows" about spec-instructions.md's 10 sections, Spec Types, S-numbering, TIMC, WORM,
`observability/thresholds.yaml`, FINRA 4511. So every *"all four source documents converge"* line is
**one idea reflected four times**, not four witnesses agreeing. Strike convergence as a reason to
believe anything here; make each claim stand on its own source.

**Rule:** context persistence is a feature when building, a bug when verifying. A Space *grounds*
work; it must never *corroborate* work. Second opinions require a witness who wasn't in the room.

**Silver lining:** the seepage is also *why* this draft is usefully specific — it wrote to your
actual format instead of generic PRD advice. Grounding worked. It just can't double as validation.
(It also explains the numbering collisions in §2: it absorbed *that* S73 exists without absorbing
*which* S73 — partial context is how you get confident, wrong specifics.)

**Statistics:** this is a synthesis, not a primary source. Verify every figure against origin before
it ships in a lesson, article, or chapter — the defect-cost multiplier especially (widely repeated,
widely contested). Attribute Cagan for the four risks, BMAD for what's BMAD's. No day-job actuals.

## 7. Suggested next step (owner's call)

**Don't author S73/74/75.** Smallest useful sequence:

1. **Renumber + key** the trio (`QG-S82/83/84`), resolve the S41 reference, key `SVD-S73`.
2. **Reconcile before building:** LLM Wiki vs S70/S73-WORM; Depot vs S38/S80. Rename or absorb.
3. **Then** follow the doc's own roadmap order — it's right: *method (enabling) → UI
   (stream-aligned) → agents (platform)*. `S82 defines the method. S83 makes it usable. S84 makes
   it agentic.`
4. Decide the **CCPM gap** (§1) — in scope for the bridge, or a separate segment?
