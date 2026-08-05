# Roundhouse HQ — Platform Specification

**Version:** 1.0 (Founding Spec)
**Status:** Draft
**Date:** May 3, 2026
**Owner:** Roundhouse HQ Platform Team
**Primary Domain:** roundhousehq.ai
**Sister Brand:** FlowTrain HQ (flowtrain.ai)

---

## Executive Summary

Roundhouse HQ is an **agentic product-management platform** that engineers, leads, and operates a fleet of specialized AI agents across the full software delivery lifecycle — from spec authoring through code quality, orchestration, observability, and sprint dispatch. The platform is launching with **Roundhouse Quality Guardian (RQG)** as its first production agent, with four additional agents (Trainyard, Switchyard, Signalbox, Dispatch) on the roadmap, all sharing a common substrate of identity, telemetry, adapter contracts, and deployment surfaces.

This document is the **canonical platform spec** — the parent of all individual agent specs. Each agent has its own deep specification (e.g., `RQG-Unified-Spec.md`); this doc defines the shared platform that hosts them.

---

## Part I — Vision & Brand Architecture

### 1.1 Mission

> **Make agentic software delivery feel like a well-run rail yard:** every workload routed to the right specialist, every handoff observable, every track inspected, and the whole system operating on a published timetable.

Roundhouse HQ exists to solve four problems that prevent teams from running agents in production:

1. **Fragmented agent surfaces** — every agent has its own CLI, prompt format, and audit trail.
2. **Invisible work** — agent runs disappear into logs nobody reads.
3. **Quality drift** — agents ship code, specs, and tickets that bypass human gates.
4. **Coordination chaos** — multi-agent workflows are bespoke shell scripts.

Roundhouse HQ provides the **rail substrate** — typed contracts, observability, identity, gates — so individual agents can be the **specialized rolling stock** that runs on it.

### 1.2 The Rail-Systems Metaphor

The product taxonomy borrows directly from rail terminology because the metaphor is operationally precise, not just aesthetic:

| Rail concept | Platform meaning |
|---|---|
| **Roundhouse** | Central facility where engines are stored, inspected, and dispatched. The control plane. |
| **Trainyard** | Where rolling stock is assembled and broken down. Multi-agent orchestration. |
| **Switchyard** | Where tracks diverge and routes are chosen. Workflow routing & arbitration. |
| **Signalbox** | Where train movements are monitored and authorized. Observability & control. |
| **Dispatch** | Where timetables are set and trains are released. Planning & sprint orchestration. |
| **Quality Guardian (RQG)** | Track inspector. Code quality enforcement. |

Every internal name maps to a real rail role; this disciplines product scoping (no scope creep into other yards' jobs) and gives engineers a shared mental model.

### 1.3 Brand Architecture

```
FlowTrain HQ                           ← training & enablement brand
   (flowtrain.ai)                        Courses, workshops, certifications
        │
        │ (shared design language, complementary GTM)
        │
Roundhouse HQ                          ← agent platform brand
   (roundhousehq.ai)                     Production agentic systems
        │
        ├── Roundhouse Quality Guardian (RQG)   [GA — May 2026]
        ├── Trainyard                            [Planned — Q3 2026]
        ├── Switchyard                           [Planned — Q4 2026]
        ├── Signalbox                            [Planned — Q4 2026]
        └── Dispatch                             [Planned — 2027]
```

**Brand boundary rules:**

- **FlowTrain HQ** owns *teaching humans* to work with agents (curricula, certifications, conference content).
- **Roundhouse HQ** owns *running agents in production* (platform, agents, telemetry).
- Cross-brand assets (logos, color palette, typography) share design-system DNA but each brand has its own distinct accent palette and voice.
- A single GitHub org (`roundhousehq`) hosts platform code; FlowTrain content lives under `flowtrainhq`.

### 1.4 Naming Conventions

| Surface | Form | Example |
|---|---|---|
| Code, configs, paths, CLI flags | **Three-letter code** | `RQG`, `scripts/rqg/`, `--rqg-strict` |
| User-facing prose, PR comments, dashboards | **Full product name** | "Roundhouse Quality Guardian flagged 3 issues" |
| Sub-product working names | **Single word, capitalized** | `Trainyard`, `Signalbox` |
| Platform | **Roundhouse HQ** (always two words, "HQ" capitalized) |  |

> ⚠️ **Trademark watch:** *Trainyard* is a popular iOS puzzle game (Matt Rix, 2010). It is safe as an internal sub-product code name but **must not** be used as a public marketing name without legal review. The public-facing name is likely "Roundhouse Trainyard" or a successor.

---

## Part II — Platform Architecture

### 2.1 Layered Model

```
┌─────────────────────────────────────────────────────────────┐
│                      USER SURFACES                          │
│   CLI · VS Code Ext · GitHub App · Web UI · Slack/Teams     │
├─────────────────────────────────────────────────────────────┤
│                      AGENT LAYER                            │
│      RQG  ·  Trainyard  ·  Switchyard  ·  Signalbox  ·      │
│                       Dispatch                              │
├─────────────────────────────────────────────────────────────┤
│                  SHARED SUBSTRATE (HQ Core)                 │
│  Identity · Adapter Contracts · Telemetry · Quality Gates · │
│   Memory · Tool Registry · Policy Engine · Run Ledger       │
├─────────────────────────────────────────────────────────────┤
│                    EXECUTION HOSTS                          │
│  Claude Code · Codex · Local LLMs · Cloud LLMs · CI runners │
├─────────────────────────────────────────────────────────────┤
│                    INFRASTRUCTURE                           │
│      Postgres · Object Storage · Queue · OTEL Collector     │
└─────────────────────────────────────────────────────────────┘
```

Each layer has a stable contract; agents must not reach below the substrate layer except through approved adapters.

### 2.2 The Shared Substrate ("HQ Core")

**HQ Core** is the platform package every agent depends on. It is published as `@roundhousehq/core` (TypeScript) and `roundhousehq-core` (Python) with strict semver.

#### 2.2.1 Adapter Contracts

Every external system (LLM, VCS, IDE, ticket system, chat) is reached through a typed adapter:

```typescript
// @roundhousehq/core/adapters
export interface LLMAdapter {
  readonly provider: "anthropic" | "openai" | "local" | string;
  readonly model: string;
  complete(req: CompletionRequest): Promise<CompletionResult>;
  stream(req: CompletionRequest): AsyncIterable<CompletionChunk>;
}

export interface VCSAdapter {
  getDiff(ref: GitRef): Promise<UnifiedDiff>;
  postReview(pr: PRRef, review: ReviewPayload): Promise<void>;
  setStatus(sha: string, ctx: string, state: CheckState): Promise<void>;
}

export interface TicketAdapter {
  read(id: TicketId): Promise<Ticket>;
  comment(id: TicketId, body: string): Promise<void>;
  transition(id: TicketId, target: string): Promise<void>;
}
```

Agents never call vendor SDKs directly. This enables:
- Vendor swaps without agent rewrites.
- Recording all traffic for replay/forensics.
- Centralized rate-limit, retry, and credential handling.

#### 2.2.2 Identity & Authorization

- Every agent run executes as a **bot identity** (`rqg-bot`, `trainyard-bot`, …).
- Each identity has a **scoped capability set** (e.g., `rqg-bot` can comment on PRs but not merge them).
- Credentials are issued by a central **HQ Identity Service** with short-lived tokens (≤ 1 hour).
- Human delegators are recorded on every run: `acted_for: human@example.com`.

#### 2.2.3 Run Ledger

Every agent invocation produces a **Run Record** persisted to Postgres + object storage:

```json
{
  "run_id": "01J7WX...",
  "agent": "rqg",
  "agent_version": "3.0.0",
  "trigger": { "kind": "pr", "ref": "octo/repo#1234" },
  "actor": "rqg-bot",
  "delegator": "alice@example.com",
  "started_at": "2026-05-03T08:00:00Z",
  "completed_at": "2026-05-03T08:00:42Z",
  "outcome": "passed_with_warnings",
  "artifacts": ["s3://hq-runs/01J7WX/report.json"],
  "tool_calls": 14,
  "llm_tokens": { "in": 8421, "out": 1203 },
  "cost_usd": 0.087
}
```

The Run Ledger is the **single source of truth** for billing, audit, and Signalbox dashboards.

#### 2.2.4 Quality Gates

A Quality Gate is a typed predicate over a Run Record. The platform ships built-in gates:

- `gate.cost.max_usd_per_run`
- `gate.tools.allowlist`
- `gate.identity.requires_delegator`
- `gate.output.requires_human_approval` (for irreversible actions)

Agents declare which gates they require in their manifest.

#### 2.2.5 Memory

Three tiers, all addressable through HQ Core:

1. **Episodic** — per-run scratch (in-memory, dropped at run end).
2. **Project** — repo/space-scoped (Postgres + vector index).
3. **Org** — cross-project knowledge (curated, write-gated by humans).

Agents declare read/write scopes per tier in their manifest; the substrate enforces them.

#### 2.2.6 Telemetry

OpenTelemetry-native:
- Every adapter call is a span.
- Every LLM call carries `gen_ai.*` attributes.
- Every Run Record links to its trace ID.
- A standard **`hq.run.*`** semantic convention is published.

Signalbox (when GA) consumes this stream; until then, OTEL exports to any standard backend (Honeycomb, Datadog, Tempo).

### 2.3 Agent Manifest

Every agent ships a `roundhouse.agent.yaml` at the repo root:

```yaml
apiVersion: roundhousehq.ai/v1
kind: Agent
metadata:
  name: rqg
  displayName: Roundhouse Quality Guardian
  version: 3.0.0
spec:
  identity: rqg-bot
  capabilities:
    - vcs:pr.read
    - vcs:pr.review
    - vcs:status.write
  adapters:
    llm: [anthropic, openai, local]
    vcs: [github, gitlab]
  gates:
    - gate.cost.max_usd_per_run: 0.50
    - gate.tools.allowlist
  memory:
    project: read,write
    org: read
  triggers:
    - kind: pr.opened
    - kind: pr.synchronize
    - kind: cli
```

The platform refuses to launch any agent whose runtime behavior diverges from its manifest.

---

## Part III — Product Taxonomy

### 3.1 Roundhouse Quality Guardian (RQG) — GA

**Mission:** Enforce Clean Code, Clean Architecture, and the Bernstein nine practices on every change, every PR, every commit.

**Status:** General Availability, May 2026.

**Reference:** See [`RQG-Unified-Spec.md`](./RQG-Unified-Spec.md) for the full agent specification.

**Scope:**
- Pre-commit hooks (CLI).
- PR review (GitHub/GitLab).
- IDE inline review (VS Code, Claude Code, Cursor).
- Test-quality scoring across Agile Testing Quadrants Q1–Q4.
- Quality-gate enforcement in CI (`rqg-quality-gate` check).

**Why RQG is first:**
- Smallest blast radius — read-mostly, advisory comments.
- Highest-frequency execution — every PR, validates platform throughput.
- Forces the substrate to harden first (adapters, identity, run ledger).

**Dependencies on substrate:** All of HQ Core. RQG is the reference implementation.

---

### 3.2 Trainyard — Planned (Q3 2026)

**Mission:** Multi-agent orchestration. Compose RQG, Dispatch, custom agents, and human reviewers into typed workflows.

**Status:** Design — MVP target Q3 2026.

**Scope (MVP):**
- DAG-based workflow definitions in YAML.
- Typed handoffs between agents (output of A is validated against input schema of B).
- Saga-style compensation for failed multi-step runs.
- Human-in-the-loop checkpoints with timeout + escalation.

**Out of scope (MVP):**
- Real-time agent-to-agent chat (deferred — see Switchyard).
- Cross-org workflows (single tenant only).

**MVP intent:**
> Replace ad-hoc shell scripts and GitHub Actions chains with a first-class workflow runtime that respects HQ identity, gates, and the Run Ledger.

**Sample workflow (sketch):**

```yaml
apiVersion: roundhousehq.ai/v1
kind: Workflow
metadata:
  name: spec-to-pr
spec:
  steps:
    - id: draft
      agent: dispatch
      input: { ticket: "${trigger.ticket_id}" }
    - id: implement
      agent: claude-code
      input: { spec: "${steps.draft.output}" }
      requires: [draft]
    - id: review
      agent: rqg
      input: { pr: "${steps.implement.output.pr_url}" }
      requires: [implement]
    - id: human-gate
      kind: approval
      approvers: ["@team/leads"]
      timeout: 24h
      requires: [review]
```

**Dependencies:** HQ Core (full). Stable adapter contracts. Run Ledger v1.1 (multi-run linking).

**Trademark note:** Public marketing name TBD (see §1.4). Internal code name `trainyard` is fine.

---

### 3.3 Switchyard — Planned (Q4 2026)

**Mission:** Workflow routing & human-in-the-loop arbitration. Decide *which* agent should handle a given trigger and broker disagreements between agents.

**Status:** Design — MVP target Q4 2026.

**Scope (MVP):**
- **Router:** classify incoming triggers (PRs, tickets, alerts) and dispatch to the right agent or workflow.
- **Arbitrator:** when two agents produce conflicting outputs (e.g., RQG says "block," another linter says "ship"), present a structured diff to a human or fall through to a tiebreaker policy.
- **Policy DSL:** declarative rules for routing/arbitration, evaluable offline.

**Out of scope (MVP):**
- ML-based routing (rules first, ML later).
- Cross-agent negotiation (agents do not "argue" — humans arbitrate).

**MVP intent:**
> Be the *control plane decision layer* sitting between triggers and Trainyard workflows.

**Dependencies:** Trainyard GA, RQG GA, at least one second agent (Dispatch alpha).

---

### 3.4 Signalbox — Planned (Q4 2026)

**Mission:** Observability, telemetry, and forensics for every agent run. The "single pane of glass" for agentic operations.

**Status:** Design — MVP target Q4 2026.

**Scope (MVP):**
- **Run Explorer** — searchable, filterable view of every Run Record.
- **Trace viewer** — OTEL waterfall for any run, including LLM token attribution.
- **Cost dashboards** — per-agent, per-team, per-repo cost rollups.
- **Replay** — re-execute a past run against a new agent version (regression testing).
- **Alerts** — anomaly detection on run failure rates, cost spikes, gate violations.

**Out of scope (MVP):**
- Custom dashboard builder (use Grafana for now).
- Cross-tenant benchmarking.

**MVP intent:**
> Make every agent action *legible* — to engineers debugging, to leaders evaluating ROI, to auditors verifying controls.

**Dependencies:** HQ Core Run Ledger + OTEL pipeline. Postgres + ClickHouse for analytics.

**Why deferred:** RQG ships with raw OTEL export to standard backends. Signalbox adds polish, not capability.

---

### 3.5 Dispatch — Planned (2027)

**Mission:** Spec authoring, sprint planning, and ticket orchestration. The agent that turns business intent into well-formed engineering work.

**Status:** Design — MVP target 2027.

**Scope (MVP):**
- Read product PRDs / Slack threads / meeting transcripts.
- Draft well-formed spec docs (acceptance criteria, test plans, architecture notes).
- Decompose specs into Jira tickets with dependencies.
- Estimate, prioritize, and propose sprint compositions.
- Detect spec drift during implementation (via Trainyard hooks).

**Out of scope (MVP):**
- Performance review or HR analytics.
- Direct cost/budget approval (Dispatch *recommends*, humans *decide*).

**MVP intent:**
> Be the spec-driven counterpart to RQG: just as RQG enforces code quality, Dispatch enforces *spec quality* before code is written.

**Dependencies:** Trainyard GA, Switchyard alpha (for human approval steps), org memory tier.

---

### 3.6 Roadmap Summary

| Quarter | Milestone |
|---|---|
| **Q2 2026** | RQG GA. HQ Core v1.0. Run Ledger v1.0. |
| **Q3 2026** | Trainyard MVP. HQ Core v1.1 (multi-run linking). RQG v3.1 (Trainyard-aware). |
| **Q4 2026** | Signalbox MVP. Switchyard MVP. HQ Core v1.2. |
| **Q1 2027** | Dispatch alpha. Cross-agent end-to-end demo: ticket → spec → code → review → merge. |
| **Q2 2027** | Dispatch GA. Platform 2.0 — multi-tenant, marketplace for third-party agents. |

---

## Part IV — Integration Surfaces

Every Roundhouse HQ agent must be reachable from the surfaces engineers already use.

### 4.1 GitHub / GitLab

- **GitHub App:** `Roundhouse HQ` — single app, dispatches to individual agents via webhook router.
- Per-agent permissions are scoped through HQ Identity, not raw app permissions.
- Status checks namespaced: `roundhouse/rqg-quality-gate`, `roundhouse/dispatch-spec-check`, etc.

### 4.2 Claude Code / Codex / Cursor

- HQ Core ships an **MCP server** (`@roundhousehq/mcp`) exposing every agent as MCP tools.
- Adapter normalizes MCP tool calls to HQ Run Records — invocations from Claude Code or Cursor get the same audit trail as PR-triggered runs.
- A `claude.md` snippet template ships with each agent for opt-in IDE behavior.

### 4.3 Perplexity Spaces

- Each Roundhouse HQ agent has a **Perplexity Space** that mirrors its docs and exposes its CLI semantics for design-time exploration.
- Spaces are read-mostly; production work happens through GitHub/IDE/CLI surfaces.
- The `Clean Code Quality Guardian` Space (this conversation's parent Space) becomes the **RQG Space** with the rebrand.

### 4.4 VS Code Extension

- Single extension: `Roundhouse HQ for VS Code`.
- Auto-detects which agents the current workspace declares (`roundhouse.agent.yaml` files in repos / `.roundhouse/` config).
- Inline reviews from RQG; future: inline ticket creation from Dispatch, run inspection from Signalbox.

### 4.5 CLI

```bash
# unified entrypoint
roundhouse <agent> <command> [flags]

# examples
roundhouse rqg review --pr 1234
roundhouse rqg gate --strict
roundhouse trainyard run spec-to-pr --ticket ENG-742
roundhouse signalbox tail --agent rqg --since 1h
```

CLI is a thin wrapper over the same adapter contracts; nothing the CLI does is unavailable to other surfaces.

### 4.6 Slack / Teams

- Out of scope for MVP.
- Planned with Switchyard (Q4 2026) — chat is a natural arbitration surface.

---

## Part V — Domain & Infrastructure Plan

### 5.1 Domain Strategy

| Domain | Role | Status | Action |
|---|---|---|---|
| `roundhousehq.ai` | Primary platform marketing + docs | **Available** | **Acquire (Porkbun, $82.70/yr)** |
| `flowtrain.ai` | Sister training brand | **Available** | **Acquire (Porkbun, $82.70/yr)** |
| `roundhouse.ai` | Defensive (taken — owner since 2018) | Unavailable | Park watch; do not pursue broker. |
| `theroundhouse.ai` | Defensive secondary | Available ($82.70/yr) | Optional — register if budget allows. |
| `signalbox.ai` | Sub-product (aftermarket $9,888) | Aftermarket | **Defer** — too expensive for unshipped product. |

**Subdomain plan under `roundhousehq.ai`:**

```
www.roundhousehq.ai          → marketing site
docs.roundhousehq.ai         → unified docs (all agents)
app.roundhousehq.ai          → web UI (post-MVP)
api.roundhousehq.ai          → public API gateway
status.roundhousehq.ai       → status page
rqg.roundhousehq.ai          → RQG product page (redirect to /rqg)
```

Sub-products do **not** get their own apex domains until they are GA and have demonstrated independent traction.

### 5.2 Infrastructure

| Concern | Choice | Rationale |
|---|---|---|
| Cloud | Azure (primary) | User's existing platform expertise + GitHub Actions integration. |
| Compute | Azure Container Apps + AKS for stateful | Spin to zero for low-traffic; AKS for OTEL collectors and Postgres. |
| Database | Azure Postgres (Flexible Server) | Run Ledger, identity, project memory. |
| Object storage | Azure Blob | Run artifacts, large diffs, replay corpora. |
| Vector store | pgvector (initially) | Avoid premature dependency on Pinecone/Weaviate. |
| Queue | Azure Service Bus | Trigger fan-out, agent task distribution. |
| Telemetry | OpenTelemetry → Honeycomb (dev) / Azure Monitor (prod) | Vendor-portable. |
| Secrets | Azure Key Vault | Short-lived tokens issued via HQ Identity. |
| CI/CD | GitHub Actions | Quality-gated by RQG against itself. |

**Eat your own dogfood rule:** every Roundhouse HQ repo must pass `rqg-quality-gate` before merge. RQG enforces RQG.

### 5.3 Repo Layout

```
github.com/roundhousehq/
├── core              # HQ Core packages (TS + Py)
├── rqg               # Roundhouse Quality Guardian
├── trainyard         # Workflow runtime (planned)
├── switchyard        # Routing/arbitration (planned)
├── signalbox         # Observability (planned)
├── dispatch          # Planning agent (planned)
├── platform          # Infra-as-code (Bicep/Terraform)
├── docs              # docs.roundhousehq.ai source
└── examples          # Reference workflows, sample agents
```

---

## Part VI — Operating Principles

These are the inviolable principles that govern how Roundhouse HQ ships agents.

### 6.1 Spec-Driven, Always

Every agent is shipped with a Unified Spec that follows the structure of `RQG-Unified-Spec.md`:
1. Theoretical framework (the books/practices it embodies).
2. Cognitive architecture (perception → reasoning → memory → planning → action → learning).
3. Quality model (how it tests itself + Agile Testing Quadrants).
4. Implementation surfaces.
5. Goals & metrics.

Agents without a Unified Spec do not enter Trainyard workflows. Period.

### 6.2 Read Before Write

Every new agent ships in **read-only / advisory mode** for at least one quarter before being granted write capabilities. This applies even to internal agents.

### 6.3 Reversibility

- All agent writes must be **reversible by a single human action** (revert PR, undo ticket transition, etc.).
- Irreversible actions require a `gate.output.requires_human_approval` gate, no exceptions.

### 6.4 Cost Transparency

- Every Run Record carries `cost_usd`.
- Cost dashboards are visible to the team that triggered the run.
- Cost gates are mandatory; default cap is **$0.50 per run**.

### 6.5 Observability is Table Stakes

- An agent with no OTEL spans is a bug, not a feature.
- Every adapter call is a span; every LLM call has `gen_ai.*` attributes.
- The Run Ledger is queryable in <2s for any run in the last 90 days.

### 6.6 Identity is Non-Negotiable

- No agent runs without a delegating human.
- No human delegates to more than one agent per trigger without an explicit Trainyard workflow.
- Bot identities never share credentials.

### 6.7 Memory is Scoped

- Episodic > Project > Org, with strictly increasing write-gates.
- No agent writes to org memory without a human merge step.

### 6.8 Quadrant Coverage for the Platform

The platform itself must satisfy all four Agile Testing Quadrants:

| Quadrant | Platform application |
|---|---|
| Q1 — Tech-facing, support programming | Unit + integration tests for HQ Core, every adapter. |
| Q2 — Business-facing, support programming | BDD scenarios for each agent's user-visible behavior. |
| Q3 — Business-facing, critique product | Usability testing of CLI/IDE/PR-comment surfaces. |
| Q4 — Tech-facing, critique product | Load tests, chaos tests, cost regression tests. |

This is enforced by — what else — RQG.

---

## Part VII — Goals & Metrics

### 7.1 Platform Goals (12-month)

| Goal | Metric | Target |
|---|---|---|
| Ship RQG to GA | RQG runs per week | 1,000+ |
| Land Trainyard MVP | Workflows defined | 25+ |
| Adapter stability | Breaking changes in HQ Core | ≤ 1 per quarter |
| Cost discipline | Median run cost | < $0.10 |
| Reliability | Run Ledger write durability | 99.99% |
| Observability | Runs with full OTEL trace | 100% |
| Safety | Reverted agent writes | < 0.5% of all writes |

### 7.2 Per-Agent Goals

Each agent spec carries its own metrics. The platform requires every agent to publish:
- **Adoption:** weekly active triggers.
- **Outcome quality:** task-specific (e.g., RQG: % of flagged issues acknowledged by human).
- **Cost:** median + p95 run cost.
- **Reliability:** error rate, p95 latency.

### 7.3 Anti-Goals

The platform explicitly does **not** pursue:
- Replacing engineers.
- Approving its own writes.
- Hosting third-party agents (until 2027 marketplace).
- Cross-tenant data sharing.
- Becoming a generic LLM gateway (use the adapter; we're not LiteLLM).

---

## Part VIII — Open Questions

Tracked here so they don't get lost. These are platform-level; agent-specific opens live in agent specs.

1. **Multi-tenant strategy** — single-tenant SaaS, BYO-cloud, or both? (Decision target: Q3 2026.)
2. **Pricing model** — per-run, per-seat, or per-repo? (Decision target: Q3 2026.)
3. **Agent marketplace governance** — what gates does a third-party agent pass to enter the registry? (Decision target: Q1 2027.)
4. **`Trainyard` public name** — legal review pending; candidate alternates: "Roundhouse Workflows," "Roundhouse Yard."
5. **Local-only mode** — can the entire platform run on a developer's workstation against local LLMs? Strategic question, not just technical.
6. **FlowTrain HQ ↔ Roundhouse HQ revenue split** — same legal entity, but training vs. platform have very different unit economics. (Decision target: Q4 2026.)

---

## Appendix A — Glossary

| Term | Definition |
|---|---|
| **Agent** | A specialized AI workflow with its own manifest, identity, and Unified Spec. |
| **Adapter** | A typed interface to an external system (LLM, VCS, ticketing, etc.). |
| **HQ Core** | The shared substrate package (`@roundhousehq/core`). |
| **Manifest** | `roundhouse.agent.yaml` — the contract between agent and platform. |
| **Quality Gate** | A typed predicate evaluated against a Run Record. |
| **Run Record** | The canonical, persisted record of one agent invocation. |
| **Run Ledger** | The Postgres + object-storage system holding Run Records. |
| **Substrate** | Synonym for HQ Core in prose. |
| **Workflow** | A Trainyard-defined DAG of agents and human steps. |

---

## Appendix B — Migration from CCQG Era

For artifacts created before the rebrand, the following table governs migration:

| CCQG-era name | Roundhouse-era name |
|---|---|
| Clean Code Quality Guardian | Roundhouse Quality Guardian |
| CCQG | RQG |
| `scripts/ccqg/` | `scripts/rqg/` |
| `docs/ccqg/` | `docs/rqg/` |
| `ccqg-quality-gate` (CI check) | `rqg-quality-gate` |
| `CCQG_*` env vars | `RQG_*` (with one-release alias) |
| CCQG Space | RQG Space (within Roundhouse HQ) |

The CCQG name is preserved only in:
- Migration notes.
- Changelog entries dated before May 3, 2026.
- Quoted historical text (do not modify in-place).

---

## Appendix C — References

- **RQG agent spec:** `RQG-Unified-Spec.md` (this directory).
- **Books grounding the platform's quality philosophy:**
  - Robert C. Martin, *Clean Code* and *Clean Architecture*.
  - David Scott Bernstein, *Beyond Legacy Code* (the nine practices).
  - Michael Feathers, *Working Effectively with Legacy Code*.
  - Jez Humble & David Farley, *Continuous Delivery*.
  - Lisa Crispin & Janet Gregory, *Agile Testing* (the quadrants).
- **Standards:**
  - OpenTelemetry semantic conventions for GenAI (`gen_ai.*`).
  - Model Context Protocol (MCP) — agent ↔ IDE bridge.

---

*End of Roundhouse HQ Platform Specification v1.0.*
