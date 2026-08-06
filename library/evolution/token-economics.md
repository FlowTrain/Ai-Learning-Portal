---
id: token-economics
practice: Token Economics / AI Cost Engineering
status: current
last_reviewed: 2026-07-10
review_cadence: quarterly
model_generations: [flat-pricing-era, metering-awareness-era, cost-architecture-2026]
referenced_by: [A4, A2E, C2, C5]
curators: [platform-owner]
---

# Evolution Entry: Token Economics (Flat-Pricing Intuitions → Metering Discipline → Cost Architecture)

## Current guidance (teach this today)

AI cost is an **architecture property, not a usage behavior**. Individual discipline (refine before metering, context files before agentic sessions) still matters — but as of 2026 the big money moves in design decisions made before anyone types a prompt:

- **The input tax is real and structural.** Tool schemas, context files, and conversation history are all billed input, every turn. A dense tool integration can consume tens of thousands of tokens before the first user question — statically loading a large enterprise tool suite (e.g., the 60+ tool Atlassian MCP server) costs ~47,000 tokens up front, and production agents have been observed spending up to ~79% of their context budget on their own tooling (as of 2026-07; see Sources).
- **Caching changes the math but is fragile.** Cache reads are billed at roughly 10% of the standard input rate (writes at a 1.25–2× premium), which makes persistent agents viable — but the cache is a byte-exact prefix match. Dynamic system prompts, model switching, or mid-session tool toggling silently invalidate it and restore full price.
- **Progressive disclosure beats bigger windows.** Deferring tool schemas until needed (meta-tool / dynamic discovery patterns) cuts upfront schema cost from ~47,000 to ~400–600 tokens. Filtering API payloads at a gateway strips up to ~90% of response dead weight (a raw ~30 KB Jira ticket ≈ 7,500 tokens at ~250 tokens/KB of JSON).
- **Data-layer choices dominate data-adjacent AI.** For AI-over-data architectures, storage format and partitioning move costs more than any prompt: columnar conversion (Parquet) reduces file size up to ~87% and scan-based query cost by up to ~99.7% (per AWS-published figures, 2026).
- **Model tiering is a cost tool.** Route narrow repetitive work to small/cheap models and reserve frontier models for reasoning — the rowboat/speedboat rule (see prompting-frameworks, Boundary conditions).

All specific numbers above are dated snapshots — that's this entry's job. Lessons teach the patterns; this entry holds the figures and re-verifies them quarterly.

## Eras

### Era 1 — Flat-pricing intuitions (~2022–2024)

Teams reasoned about AI spend the way they reasoned about SaaS: per-seat licenses, flat subscriptions, "we already pay for it." Chat interfaces felt free at the margin, so cost never entered workflow design. The era's legacy fossil is the license mental model applied to metered inference — budgeting AI like Office seats when consumption actually scales with architecture and usage patterns.

### Era 2 — Metering awareness and personal discipline (~2024–2025)

Token-based API pricing entered team consciousness: input/output asymmetry, context-as-cost, the discovery that agentic sessions burn tokens re-learning what nobody wrote down. Practice responded at the *individual* level: refinement-first rules (compress intent in a cheap window before opening a metered tool), context files to stop paying for re-explanation, "treat chat as free, agents as metered." This is the C2/A4 layer of the platform — still correct, still taught.

### Era 3 — Cost architecture (2025–2026)

Costs moved from the person to the platform. Prompt caching made persistent agents economically viable while making prompt *stability* an engineering requirement. The input tax of tool ecosystems (MCP-era schema injection) became a first-class design constraint, answered by progressive disclosure and gateway payload filtering. For AI-over-data systems, cost analysis expanded to the whole stack: storage format, partitioning, scan pricing, egress modeling, concurrency. The unit of optimization is no longer the prompt or even the workflow — it's the architecture, evaluated with TCO methods that finance already recognizes.

## Deprecated patterns (stop teaching these)

- ❌ **Budgeting metered AI like per-seat licenses** — consumption scales with architecture and cadence, not headcount.
- ❌ **Prompt wordsmithing as the primary cost lever** — trimming twenty tokens of phrasing while statically loading 47,000 tokens of tool schemas is bailing with a teaspoon.
- ❌ **"The window is big enough" as a cost strategy** — bigger windows raise the ceiling on waste; effective utilization degrades as they fill (see context-engineering).
- ❌ **Retry-until-it-works loops as error handling** — a cost multiplier; push error recovery into the tool/gateway layer.
- ❌ **Optimizing context mid-session at the expense of cache stability** — removing tools or mutating the system prompt to "save tokens" can trigger full-price recomputation of everything downstream.

## What survived

Era 2's personal disciplines survive intact as the rung-1/2 curriculum layer: A4's two-question test, A2E's context-file rule, C2's refinement-first rule and three-term ROI (time saved − usage cost − maintenance). Cost architecture doesn't replace them; it's what they grow into at platform scale. D5 teaches leaders the same three terms as funding questions.

## Boundary conditions (where older practice is still correct)

- **Tier 1/2 individual chat use is effectively flat-rate.** Subscription chat tools make token accounting irrelevant for personal drafting/summarizing — teaching token math to a Tier 1 learner is a staircase leap and actively harmful to habit formation. The discipline begins where metering begins: APIs, agentic tools, platform workflows.
- **Small local models invert the ledger.** Per-token cost approaches zero; the costs move to hardware, latency, and quality risk. Era-1 "it's basically free" intuitions are locally true there — the governance concern shifts from spend to output quality (see prompting-frameworks, rowboat layer).
- **Low-volume integrations may not warrant cost architecture.** A tool called weekly doesn't need progressive disclosure and a Rust gateway; Era 2 discipline plus caching defaults is proportionate. Cost architecture earns its complexity at continuous/production cadence.

## Signals to watch (would trigger Era 4)

- Flat-rate or bundled agentic pricing at enterprise scale (would partially resurrect Era-1 budgeting, legitimately).
- Vendor-managed context/caching that self-optimizes (auto-compaction, automatic prefix management) — would absorb the stability disciplines into the platform.
- Inference cost collapsing toward the edge (capable local models for most work) — would shift the entry's center of gravity from tokens to orchestration and quality economics.

## Sources

- `research/Jira MCP Token Impact Analysis.md` (owner research, 2026-07) — input tax (~47K tokens static loading; 500–1,400 tokens/schema; ~79% context-on-tooling), caching mechanics and invalidation, progressive disclosure (~400–600 tokens), payload filtering (~90%), ~250 tokens/KB JSON heuristic, latency ~0.24 ms/input token.
- `research/Jira Data Cost and Integration Analysis.md` (owner research, 2026-07) — lakehouse economics: Parquet ~87% size / up to 34× speed / ~99.7% scan-cost reduction (AWS-published), Athena scan pricing model, text-to-SQL accuracy ranges (benchmark-fragile; production-viable with schema access).
- `research/Azure PostgreSQL Jira Data Cost Analysis.md` (owner research, 2026-07) — egress modeling (first 100 GB/mo free tier; $0.09/GB first 10 TB as of writing), Delta Sharing / deep-clone patterns to minimize cross-cloud movement, ODS TCO framing.
- Parked numeric claims adopted from `docs/open-questions.md` (A4/A2E/C2 removals, 2026-07-10) — now dated and homed here.
- Vendor pricing pages (Anthropic, OpenAI, AWS, Azure) — re-verify all figures at each quarterly review; pricing is the most volatile claim class in this library.
