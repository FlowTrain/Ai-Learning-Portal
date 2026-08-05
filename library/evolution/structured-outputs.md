---
id: structured-outputs
practice: Structured Outputs
status: current
last_reviewed: 2026-07-10
review_cadence: quarterly
model_generations: [gpt-3.5/4-era, json-mode/function-calling-era, constrained-decoding-2026]
referenced_by: [B4, D1]
curators: [platform-owner]
---

# Evolution Entry: Structured Outputs (Prose Asks → JSON Mode → Schema-Enforced Contracts)

## Current guidance (teach this today)

Define the schema before you prompt (the B4 rule — unchanged). Then pick the enforcement level by stakes:

1. **Prompt-level formatting** ("respond as a markdown table") — fine for human-readable output a person will review anyway.
2. **Tool-use / function-calling patterns** — high reliability; pair with a code-side validator (Pydantic/Zod-style) as the safety net.
3. **Native constrained decoding** — guaranteed schema-valid output; the production default in 2026 where a machine consumes the result.

Two disciplines matter more than the enforcement level:

- **Reason first, format second.** Rigid schemas imposed on the whole generation measurably degrade reasoning. Either put a free-text reasoning field *before* the answer fields (constrained models generate fields in order), or decouple entirely: generate freeform, then reformat in a second pass. Constraining only the final answer is nearly free in quality terms.
- **Valid ≠ correct.** Constrained decoding guarantees the shape, never the content. A schema-perfect JSON can still contain invented values — the false-confidence trap. A linter catches type errors; only a human who knows the product catches invented content (B4's validation rule survives every era).

Schema design rules that hold in 2026: make fields optional when the data might not exist (forcing a required field invites hallucinated values), and split very large schemas into multiple extraction calls rather than one giant object.

## Eras

### Era 1 — Prose formatting asks (~2022–2023)

No enforcement existed. Practice was "respond only in JSON, no commentary," then regex extraction, then retry-until-it-parses loops. Reliability was a prompt-wording problem, so teams accumulated superstition ("threaten the model," "bribe it") instead of contracts. Model context: chat-era models had no format guarantees at the decoding layer; every consumer had to be defensive.

### Era 2 — JSON mode and function calling (2023–2024)

Vendors moved the guarantee into the API: function calling (OpenAI, mid-2023), then JSON mode (late 2023) guaranteed *parseable* JSON but not *your schema* — fields could still be missing, renamed, or mistyped. OpenAI's Structured Outputs (August 2024) crossed the line to schema conformance via constrained decoding. The practice shift: schemas moved from the prompt text into the API call, and "parse-and-pray" started reading as a fossil.

### Era 3 — Schema-enforced contracts and the reason-then-format discipline (2025–2026)

Constrained decoding became infrastructure: grammar backends (e.g., XGrammar) are now the default in mainstream serving stacks (vLLM, SGLang, TensorRT-LLM), and structured output is a checkbox, not an engineering project. With enforcement solved, attention moved to what enforcement *costs*: research quantified 10–30% reasoning degradation when strict format constraints are imposed too early ("the constraint tax" / "format tax"), producing the current discipline — reasoning fields first, or decoupled two-pass generation. Provider differences persist: some offer full constrained decoding; others (tool-use patterns) offer near-guarantees that still warrant a code-side validator. Schemas themselves became **interface contracts between agents and tools** — the D1 tool-inventory pattern — not just output formatting.

## Deprecated patterns (stop teaching these)

- ❌ **Prompt-and-pray JSON with regex repair** — enforcement belongs in the API/decoding layer, not in string cleanup.
- ❌ **Retry-until-it-parses loops** — a cost-multiplier that constrained decoding made obsolete.
- ❌ **One giant schema for a complex extraction** — split into multiple calls; massive single schemas degrade field accuracy.
- ❌ **Constraining the entire generation, reasoning included** — this is where the 10–30% quality loss lives; constrain the answer, not the thinking.
- ❌ **Treating schema-valid output as verified output** — validity is shape; correctness is content. The human check survives.

## What survived

The B4 workflow survives intact across all three eras: define the schema first, provide the structured description, validate before downstream use. What changed is only *who enforces the schema* — the prompt (Era 1), the API (Era 2), the decoder (Era 3). Human content validation — catching invented values a linter can't see — has never been automated away, and schema-first thinking got *more* valuable as schemas became agent-to-tool contracts.

## Boundary conditions (where older practice is still correct)

- **Small local models pay the constraint tax hardest** — they need the scratchpad most. For the local layer of a multi-model stack, always use reasoning-first fields or two-pass decoupling; naive constrained decoding quietly costs the most exactly where it looks free (the rowboat needs the most care, not the least).
- **Prompt-level formatting is still right for human-consumed output** — a table in a chat reply needs no schema; escalating every format ask to constrained decoding is over-engineering (and rung-3 thinking applied to a rung-1 task).
- **Tool-use-pattern providers** — where full constrained decoding isn't offered, Era-2 discipline (validator as safety net) remains correct practice, not a fossil.

## Signals to watch (would trigger Era 4)

- Providers eliminating the reasoning tax (extended thinking + constrained answers unified) — would retire the two-pass discipline.
- Schema negotiation between agents (schemas generated and agreed at runtime) — would move the unit of curation from "output contract" to "protocol design."
- Measured convergence of tool-use patterns to true 100% conformance — would collapse enforcement levels 2 and 3.

## Sources

- [JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models](https://arxiv.org/abs/2501.10868) (arXiv 2501, Jan 2025) — constrained-decoding efficacy/coverage across engines.
- [The Constraint Tax: Measuring Validity-Correctness Tradeoffs in Structured Outputs for Small Language Models](https://arxiv.org/pdf/2605.26128) (arXiv 2605, 2026) — small-model reasoning degradation under rigid schemas.
- [The Format Tax](https://arxiv.org/pdf/2604.03616) (arXiv 2604, 2026) and [Thinking Before Constraining: A Unified Decoding Framework](https://arxiv.org/html/2601.07525v2) (arXiv 2601, 2026) — reason-then-format findings; constraining final answers is nearly free.
- [Structured Outputs Create False Confidence](https://boundaryml.com/blog/structured-outputs-create-false-confidence) (BAML blog) — valid ≠ correct.
- [LLM Structured Output in 2026: Stop Parsing JSON with Regex](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk) (2026) — three enforcement levels, provider comparison, schema-design rules (reasoning fields first, optional fields, split schemas).
- Vendor docs (OpenAI Structured Outputs, Anthropic tool use) — re-verify enforcement guarantees at each quarterly review.
