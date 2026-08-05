---
id: agent-orchestration
practice: Agent Orchestration
status: current
last_reviewed: 2026-07-10
review_cadence: quarterly
model_generations: [single-chat-era, chain-era, multi-agent-2026]
referenced_by: [A3, A3E, C1, D1]
curators: [platform-owner]
---

# Evolution Entry: Agent Orchestration (Single Chat → Chains → Multi-Agent)

## Current guidance (teach this today)

Decompose first, delegate second, multiply agents last — and only against evidence:

- **The chain is still the backbone.** Break multi-step work into named steps with verified outputs between them (the A3/C1 layer). Every orchestration pattern in production is this idea with more machinery.
- **Multiply agents only against a measured ceiling.** The 2026 correction to multi-agent enthusiasm: coordination is not free. Multi-agent topologies carry substantial token overhead (reported ~58% for independent setups to ~285% for centralized ones, as of 2026), and compute-normalized comparisons show a single well-contexted agent often *matches* a multi-agent system on reasoning tasks. Reach for multiple agents when you can name the single-agent ceiling you're escaping: a recurring failure mode a specialist would catch, a latency wall parallelism would break, or a quality bar a critic measurably raises — which means you need an eval before you need a second agent (see evaluation-practice).
- **When you do orchestrate, use the boring topology.** Orchestrator-worker — a planner that decomposes and dispatches to specialized workers (researcher / implementer / tester / reviewer), then merges — accounts for the large majority (~70%) of production deployments. The exotic patterns (debate, swarm) are for named problems, not defaults.
- **Every agent gets a contract.** Bounded scope, explicit tool inventory with input/output schemas, a failure protocol (never silent), and an audit log — D1's four properties. An agent without a contract is a liability with initiative.
- **The reviewer agent is the cheapest win.** One agent checking another's output against criteria measurably reduces hallucinated and unsafe output — it's the critique step of the A3 chain, given a permanent seat.

## Eras

### Era 1 — Single chat (~2022–2023)

One conversation did everything: research, drafting, revision, formatting, in a single thread with a single context. The human *was* the orchestrator — copy-pasting between windows, carrying state in their head, re-explaining after every context overflow. Model context: no tool use, no memory, weak planning; there was nothing to orchestrate but the person's patience.

### Era 2 — Chains (2023–2025)

Decomposition became the practice: clarify → generate → critique → refine, each step's output verified before becoming the next step's input. The value was inspectability — one long prompt's unpredictable output traded for short steps a human could gate. Human judgment stayed at the joints, explicitly placed where consequences were irreversible (the A3 rule). Chains written down became team assets, then skills (C3). This era's discipline — acceptance criteria per step, before the prompt — is what made everything after it possible.

### Era 3 — Multi-agent orchestration (2025–2026)

Models got planning, tool use, and long-running autonomy; the chain's stations got staffed. Orchestrator-worker became the production default, with a recognized pattern vocabulary (fan-out, pipeline, debate, supervisor, swarm) and reviewer/critic agents as standard quality machinery. Where the value moved: from prompt wording (era 1) to decomposition (era 2) to **coordination design** — agent interfaces, tool contracts, review loops, and failure protocols are now where the engineering lives. And era 3 promptly generated its own correction: compute-normalized studies showing single agents matching multi-agent systems forced the discipline of justifying every added agent with a measured ceiling rather than architectural fashion.

## Deprecated patterns (stop teaching these)

- ❌ **One giant prompt for multi-step work** — era-1 practice; decompose into inspectable steps (also deprecated in prompting-frameworks).
- ❌ **Multi-agent by default** — agent count is not sophistication; unjustified topology buys 58–285% token overhead for quality a better-contexted single agent often matches.
- ❌ **Unbounded agents** — no scope, no tool contract, no failure protocol means no production. "It usually behaves" is not a contract.
- ❌ **Silent failure handling** — an agent that can't complete its task must say so through a defined protocol; swallowed failures surface as confident wrong answers downstream.
- ❌ **Removing the human gate from irreversible steps** — era-2's judgment rule survives every topology; autonomy is granted per risk tier (D6), not per capability.

## What survived

The chain survived wholesale — a multi-agent system is a chain whose stations have been delegated, and the A3 pattern (clarify/generate/critique/refine) is visibly the planner/implementer/reviewer topology in embryo. C1's acceptance-criteria-per-step became inter-agent contracts. The human-judgment placement rule survived as risk-tiered autonomy. Nothing from era 2 was wrong; it was staffing that changed.

## Boundary conditions (where older practice is still correct)

- **A single agent with good context is correct for most team workflows.** Below production cadence, multi-agent is over-engineering — the Tier 2–3 curriculum (chains + context files) is not a lesser version of orchestration; it *is* the right architecture at that scale.
- **Era-2 human-gated chains remain mandatory where stakes are high** regardless of how capable agents get — the gate placement rule is a governance decision (D6), not a capability question.
- **Single chat is still right for single transformations** — orchestrating a one-step task is the same fossil as schema-enforcing a chat reply (see structured-outputs, boundary conditions).
- **The critic pattern needs an eval to earn its seat** — without a measured quality bar, a reviewer agent is cost without evidence (evaluation-practice, era 3).

## Signals to watch (would trigger Era 4)

- Coordination overhead collapsing (framework-managed state, shared KV/context between agents) — would weaken the compute-normalized argument for single agents.
- Reliable self-organizing topologies (swarms that don't need designed contracts) — would move the skill from topology design to constraint design.
- Vendor platforms absorbing orchestration entirely (declare the outcome, get a managed team) — prompts became specs; workflows would become intents, and this entry's unit of curation shifts again.

## Sources

- [Single-Agent vs Multi-Agent AI: When to Scale](https://www.augmentcode.com/guides/single-agent-vs-multi-agent-ai) (Augment Code, 2026) — compute-normalized parity finding; token overhead figures (~58% / ~285%); "measurable single-agent ceiling" trigger.
- [Multi-Agent Orchestration Guide](https://www.codebridge.tech/articles/mastering-multi-agent-orchestration-coordination-is-the-new-scale-frontier) (Codebridge, 2026) — orchestrator-worker at ~70% of production deployments; coordination as the new frontier.
- [Multi-Agent Orchestration: 5 Patterns That Work](https://www.digitalapplied.com/blog/multi-agent-orchestration-5-patterns-that-work) (2026) — fan-out / pipeline / debate / supervisor / swarm vocabulary.
- [Multi-agent orchestration patterns and best practices](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/multi-agent-patterns) (Microsoft Learn, 2026) — reviewer/fact-checker loops reducing hallucination; enterprise topology guidance.
- [The Code Agent Orchestra](https://addyosmani.com/blog/code-agent-orchestra/) (Osmani, 2026) — practitioner account of planner/implementer/tester/reviewer coding workflows.
- Founding research conversations (2026-07, `learning_program_scraps.md`) — multi-agent as production default for non-trivial tasks; where prompt skill moved.
