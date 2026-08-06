---
id: context-engineering
practice: Context Engineering
status: current
last_reviewed: 2026-07-10
review_cadence: quarterly
model_generations: [stuff-the-prompt-era, rag-era, curated-jit-context-2026]
referenced_by: [B1, B1E, C4, C5]
curators: [platform-owner]
---

# Evolution Entry: Context Engineering (Stuff-the-Prompt → RAG → Curated Just-in-Time Context)

## Current guidance (teach this today)

Context engineering is deciding **what the model sees, in what order, from which authoritative sources** — and in 2026 it is a bigger quality lever than prompt wording. The working framework is four verbs:

- **Write** — persist context outside the window: durable context files (CLAUDE.md, soul.md — the C4 artifacts), decision logs, boundary docs. Written once, inherited by every session.
- **Select** — retrieve only what's relevant *now*, just-in-time, rather than front-loading everything that might matter.
- **Compress** — summarize aging history instead of carrying it verbatim; long-running sessions accumulate "context rot" where stale tokens crowd out signal.
- **Isolate** — give sub-tasks their own clean context instead of one ever-growing window.

Placement still matters: attention is U-shaped, and material buried mid-context underperforms material at the beginning or end — a finding that has survived every context-window increase to date, including million-token models. Put controlling instructions and authoritative sources at the edges; never bury the contract in the middle.

For learners below Tier 3, the practical form of all this is unchanged from the B-series: signal-rich file names and summaries so retrieval finds the right thing (B1), and a maintained context file so agentic sessions never start from zero (B1E).

## Eras

### Era 1 — Stuff the prompt (~2022–2023)

Context windows were small and the prompt was the only lever, so practice was manual curation by necessity: paste the relevant excerpt, keep it short. The era's failure mode was the opposite instinct once windows grew — "it fits, so include it." Model context: no retrieval tooling in common use; every session started from zero and ended in amnesia.

### Era 2 — RAG and placement rules (2023–2025)

Vector retrieval made external knowledge routine: chunk, embed, retrieve top-k, augment the prompt. The defining research finding was **lost-in-the-middle** (Liu et al., 2023; TACL 2024): models reliably use information at the start and end of context and degrade sharply on the middle — even explicitly long-context models. Practice acquired placement rules, reranking, and chunking discipline. The era's fossil was "bigger window beats retrieval": long windows kept getting cheaper, but position bias and cost meant *indiscriminate* stuffing still lost to *selected* context.

### Era 3 — Curated just-in-time context and agentic context management (2025–2026)

"Context engineering" became the named discipline as agents replaced single calls. What changed: agents run for many steps and accumulate history, so context became something to *manage over time*, not assemble once — hence write/select/compress/isolate, context-rot awareness, and just-in-time tool schemas (lightweight tool lists expanded on demand rather than every schema up front). Durable context files (CLAUDE.md and kin) went from power-user habit to standard infrastructure, and retrieval itself became agentic — plan, retrieve, reflect, re-retrieve — rather than single-pass. The prompt is now the smallest part of a designed information environment.

## Deprecated patterns (stop teaching these)

- ❌ **"The window is big enough, paste everything"** — position bias and context rot mean indiscriminate stuffing degrades output even when it fits.
- ❌ **Re-explaining the project at the start of every session** — that's what durable context files are for; per-session re-explanation is the single most expensive fossil in daily practice.
- ❌ **Burying instructions or authority statements mid-context** — the U-curve has not flattened; edges or nothing.
- ❌ **Single-pass retrieve-and-generate as the default for multi-step work** — agentic retrieval with reflection is the production pattern.
- ❌ **Treating context window size as a strategy** — window growth changed what's *possible*, not what's *optimal*; selection still beats volume.

## What survived

Era 1's core instinct — *manual curation of a small, relevant context* — turned out to be the whole discipline in embryo; it was right for the wrong reason (necessity) and is now right by evidence. Placement rules from Era 2 survive intact as of 2026. And the oldest rule of all survives from every era: state which sources are authoritative — models reconcile conflicting context silently unless told not to (see the prompting-frameworks entry, CREATE+ "C").

## Boundary conditions (where older practice is still correct)

- **Tier 1/2 chat-tier work needs no pipeline.** For a single question about a single document, pasting the relevant text *is* correct context engineering — teaching write/select/compress/isolate to a Tier 1 learner is a staircase leap. A0's "paste in the raw material" guidance is this entry's rung-1 form.
- **One-shot long-context dumps remain fine for single-pass tasks** (summarize this transcript) where building retrieval infrastructure is overkill — position bias matters less when the task is holistic rather than needle-finding.
- **Small local models** have small effective contexts regardless of advertised window; Era 1 discipline (short, curated, explicit) is mandatory there, mirroring the rowboat rule in prompting-frameworks.

## Signals to watch (would trigger Era 4)

- Flat attention curves on production models (placement rules retire; several vendors claim progress every cycle — verify against needle-in-haystack and LongBench-style evals, not marketing).
- Vendor-managed context (automatic compression/memory as a platform primitive) absorbing the select/compress verbs — the skill would shift to auditing what the platform chose to keep.
- Persistent cross-session memory becoming default-on in enterprise assistants — would demote CLAUDE.md from "context delivery" to "context governance" (the governance half stays).

## Sources

- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) (Liu et al., arXiv July 2023; [TACL 2024](https://aclanthology.org/2024.tacl-1.9/)) — the founding placement finding.
- [Lost-in-the-Middle Is Still Real in 2026 (Even on 1M-Token Models)](https://dev.to/gabrielanhaia/lost-in-the-middle-is-still-real-in-2026-even-on-1m-token-models-2ehj) (2026) — position bias persists on current frontier models; no production model has eliminated it.
- [Context Engineering: A Practical Guide for AI Agents](https://sourcegraph.com/blog/context-engineering) (Sourcegraph, 2026) — write/select/compress/isolate framing, context rot.
- [Context Engineering Best Practices for Agentic Systems](https://www.comet.com/site/blog/context-engineering/) (Comet, 2026) — agentic context management, JIT tool schemas, memory tools.
- [Efficient On-Device Agents via Adaptive Context Management](https://arxiv.org/pdf/2511.03728) (arXiv 2511) — just-in-time schema passing; small-model context limits.
- Founding research conversations (2026-07, `learning_program_scraps.md`) — cross-model consensus on context shaping as the successor discipline to prompt wording.
