---
id: prompting-frameworks
practice: Prompt Engineering
status: current
last_reviewed: 2026-07-10
review_cadence: quarterly
model_generations: [gpt-3.5/4-era, gpt-4.5+/5.x-era, frontier-2026]
referenced_by: [A2, A2E, A3, A3E, C1, C5]
curators: [platform-owner]
---

# Evolution Entry: Prompting Frameworks (CREATE → Outcome-First → Context Engineering)

## Current guidance (teach this today)

Use the smallest prompt that adequately defines:

> **Outcome + context + constraints + evidence + output + validation**

Add roles, examples, and procedural instructions only when testing demonstrates they improve performance. Good prompting today looks like writing a crisp ticket or spec — not a long incantation. The leverage has moved from prompt wording to **context shaping** (what the model can see, in what order, from which authoritative sources) and **workflow design** (chains, agents, quality gates enforced outside the prompt).

For the coach cohort, the practical frame is the updated **CREATE+**:

| Element | Current interpretation |
|---|---|
| **C** — Context and source authority | Only relevant context; state which sources control. "Use the attached policy as authoritative; flag conflicts rather than reconciling silently." |
| **R** — Result and audience | Define the outcome, not a generic persona. "Produce a decision memo the committee can approve, reject, or conditionally approve." |
| **E** — Evidence and examples | Set the evidentiary threshold; examples only where they clarify judgment, as boundary-setters. |
| **A** — Actions, tools, and autonomy | What the model may do and where approval is required. "Search and analyze; do not send, modify, or commit." |
| **T** — Tests and trade-offs | How the work will be judged. "Optimize traceability over breadth; verify citations before finalizing." |
| **E** — Expression and output contract | Format, depth, tone, constraints — as a contract, not vibes. |
| **+** — Execution loop | Gather → draft → test against acceptance criteria → revise defects → stop when criteria met or evidence insufficient. |

## Eras

### Era 1 — Procedural frameworks (GPT-3.5/4, ~2022–2024)

Models needed verbose, step-by-step scaffolding to behave reliably. CREATE (Context, Role, Examples, Action, Tone, Expectations) and its cousins were the gold standard: encode a fixed meta-workflow, micromanage the reasoning, wordsmith heavily. "Act as an expert X…" personas measurably helped. Clever phrasing mattered because the model's internal planner was weak.

### Era 2 — Outcome-first delegation (GPT-4.5+ / 5.x, ~2024–2026)

Frontier models arrived with strong internal planners. Vendor guidance flipped: tell the model what success looks like (goal, audience, quality bar) rather than enumerating internal steps — detailed procedural scripts became **distractor tokens** that actively hurt performance. The working metaphor shifted from "instruct every step" to "delegate an objective to a capable intern with clear acceptance criteria." Structure beat eloquence: schemas, XML-ish scaffolding, and explicit output contracts outperformed baroque roleplay.

### Era 3 — Context and workflow engineering (frontier, 2026–)

The locus of control moved out of the prompt text entirely:

- **Context engineering** became the recognized discipline: just-in-time retrieval, source hierarchies, and *placement* — the U-shaped attention curve means instructions buried mid-context suffer >30% accuracy drops, so where information sits matters more than how it's worded.
- **Multi-agent workflow design** (planner / implementer / tester / reviewer) became the default for non-trivial production tasks; prompt skill now shows up as defining agent roles, interfaces, tool-call policies, and review loops.
- **Iteration got cheap**: self-critique loops and meta-prompting (have the model design its own prompt/workflow) replaced one-shot perfection.
- Prompts became **product surfaces**: versioned, short, maintained — one part of a larger contract among agents, tools, and specs.

## Deprecated patterns (stop teaching these)

- ❌ **Fixed meta-workflow frameworks as universal practice** — encoding CREATE-style step scripts into every prompt adds drag to frontier models.
- ❌ **"Act as my prompt engineer, interview me, then rewrite" loops** — the model understands the task earlier than the ritual assumes.
- ❌ **Persona-first prompting as a quality lever** — roles only where perspective or decision authority genuinely changes the output.
- ❌ **Burying format requirements deep in prose** — use explicit output contracts / schemas, externally validated where stakes are high.
- ❌ **One giant prompt for multi-step work** — decompose into staged workflows with inspectable intermediate outputs.

## What survived from CREATE

The *elements* remain sound even though the procedural framing is obsolete: curated context, meaningful perspective, boundary-setting examples, a clear action, audience-appropriate tone, explicit expectations. CREATE taught people to communicate clearly with a model; it is incomplete rather than wrong. What it never addressed — source grounding, tool use, uncertainty handling, validation, workflow decomposition, permissions, evaluation, memory, stopping conditions — is exactly what CREATE+ adds.

## Boundary conditions (where Era-1 practice is still correct)

Rigid, locked-down, CREATE-style prompts remain **essential for small local models** (limited internal reasoning; they drift and hallucinate without explicit personas and heavily constrained steps). Modern multi-model orchestration uses both paradigms simultaneously:

- **Local layer:** highly specific, constrained prompts driving small models for narrow repetitive tasks (classification, formatting, structured JSON) — cheap and reliable.
- **Frontier layer:** broad, outcome-first prompts for heavy reasoning, architecture, and strategy.

The engineering judgment has shifted from "write the perfect prompt" to "know where the rowboat is more efficient than the speedboat."

## Signals to watch (would trigger Era 4)

- Vendor guidance deprecating explicit output contracts in favor of learned intent (would weaken the schema-first rule).
- Long-context attention becoming flat (would weaken placement rules).
- Agent frameworks absorbing prompt authoring entirely (prompts become generated artifacts, and this entry's unit of curation shifts to workflow specs).

## Sources

- Founding research conversations (Perplexity, Gemini, ChatGPT synthesis), captured 2026-07 in `learning_program_scraps.md` — cross-model consensus on outcome-first, context engineering, structure-over-cleverness, multi-agent defaults, and the CREATE+ reformulation.
- Vendor prompting guides (OpenAI GPT-5-era guidance; Anthropic prompt-engineering docs) — re-verify at each quarterly review.
- U-shaped attention / lost-in-the-middle findings — re-verify against current long-context evals at each review.
