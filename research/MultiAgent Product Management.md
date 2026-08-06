# Architecture for an AI-native cross-functional product team platform

**An AI-native product team platform needs five interlocking systems: multi-model routing to match each agent to its optimal LLM, structured SKILL.md role bundles to define agent capabilities, persistent shared memory so agents build collective knowledge, learning loops that continuously improve agent performance, and an orchestration layer that ties everything together.** This report provides a production-grade blueprint for building this system in TypeScript/Node, drawing on the latest research, frameworks, and patterns available as of early 2026. The system leverages Claude API as the primary reasoning engine, Vercel AI SDK and Mastra for TypeScript-native orchestration, LangGraph.js for stateful workflows, and Azure Cosmos DB as a unified document-vector store.

---

## 1. Multi-model routing assigns each agent the right LLM for its job

The core insight from 2025-2026 research is that **intelligent model routing delivers 85% cost reduction while maintaining 95% of frontier model performance** (UC Berkeley/Canva research). Enterprise LLM spending hit $8.4 billion in 2025, with most waste coming from routing simple tasks to expensive models. The solution is a classification-first architecture where a lightweight router directs each task to the cheapest model that can handle it well.

### The production model-to-role mapping

Small models under 3B parameters achieve "superior Performance-Efficiency Ratios" over larger counterparts for classification tasks. On IMDB sentiment classification, Qwen2.5-0.5B reaches **91.7% accuracy**, while Qwen2.5-72B actually scores lower at 88.6%. This validates using nano models for routing decisions and simple classification. For a cross-functional product team, the recommended mapping is:

| Agent Role | Primary Model | Rationale |
|---|---|---|
| Router / Task Classifier | Phi-4 or Qwen3-1.7B | Classification saturates at sub-billion scale |
| Reasoning & Code Generation | Claude Sonnet/Opus 4.x | Top SWE-bench scores, strongest code quality |
| Vision & UI Analysis | GPT-4o or Gemini Pro Vision | Best multimodal comprehension |
| Fast Summarization | Gemini Flash 2.0/3.0 | Lowest latency for synthesis tasks |
| UI Component Selection | Embedding similarity + Phi-3 validation | Structured classification over finite taxonomy |
| Data Analytics SQL | Claude Sonnet | Strong structured reasoning |
| QA Test Generation | Claude Sonnet | Systematic coverage thinking |

### What Perplexity teaches about routing

Perplexity operates a **model-agnostic orchestration layer** — its core competency is not any single LLM but the orchestration system that combines models with a high-performance search backend (Vespa AI, 200B+ URLs indexed). Their ROSE inference engine uses small classifier models to determine query complexity, then routes to the cheapest model that delivers the best user experience. Simple factual queries go to their in-house Sonar model (fine-tuned Llama 3.1 70B), complex reasoning routes to frontier models like Claude or GPT, and coding tasks specifically route to Claude. The guiding principle: **"the smallest model that will still give the best possible user experience."** They A/B test model/latency tradeoff configurations on live users and use LLM-as-a-Judge for scaled evaluation.

### The nano model architecture for UI component selection

A small model can absolutely handle UI component selection from a design system gallery. ShadCN/UI has approximately 50-80 component types — this is a finite classification problem. The recommended pipeline:

1. **Encode ShadCN component descriptions + usage patterns into a vector store** (the ShadCN v4 project now exposes AI-optimized markdown via `/llm/` routes and an MCP server)
2. **Use embedding similarity** (bge-large-en-v1.5 or text-embedding-3-small) for first-pass retrieval of 3-5 candidate components
3. **Use a small model** (Phi-3 at 3.8B or Qwen3-1.7B) for final selection and validation from the shortlist
4. **Fall back to Claude** only for ambiguous or novel component needs requiring design reasoning

For the broader UI/UX design pipeline that avoids expensive Figma Make costs, the strongest alternatives are **v0.dev** (Vercel's tool, generates React/ShadCN code from text or screenshots, teams report 3x faster design-to-implementation) and **screenshot-to-code** (63K+ GitHub stars, open source, converts screenshots to HTML/Tailwind/React using GPT-4o, Claude, or Gemini). Both default to ShadCN/UI as their design system.

### TypeScript libraries for multi-model routing

The **Vercel AI SDK** (npm package `ai`, v5 stable / v6 beta, 20M+ monthly downloads) is the dominant TypeScript AI library. It provides a provider-agnostic unified API where models are referenced as simple strings like `"anthropic/claude-opus-4"` or `"openai/gpt-4o"`. The v6 `Agent` class adds agentic loop control with `stopWhen` and `prepareStep`.

**Mastra** (`@mastra/core`, from the team behind Gatsby) is the strongest TypeScript agent framework with built-in model routing. It supports **600+ models across 45 providers** with zero package installs, automatic model fallbacks, and dynamic model selection based on runtime context:

```typescript
const dynamicAgent = new Agent({
  name: 'DynamicAgent',
  model: (context) => context.complexity === 'high' 
    ? 'anthropic/claude-3-opus' 
    : 'google/gemini-3-flash'
});
```

**LiteLLM Proxy** serves as an optional gateway layer for cost tracking, rate limiting, and provider abstraction, exposing an OpenAI-compatible API that any TypeScript client can consume. For framework-level orchestration, **LangGraph.js** (`@langchain/langgraph`) supports per-node model assignment where each node in the state graph can invoke a different model.

### Mixture of Agents for quality-critical tasks

The Mixture of Agents (MoA) pattern, published as an ICLR 2025 spotlight paper by Together AI, organizes multiple LLMs in layers where each agent receives all outputs from the previous layer. Using only open-source models, MoA achieved **65.1% on AlpacaEval 2.0 versus GPT-4 Omni's 57.5%**. The key design insight: heterogeneous models contribute far more than copies of the same model, and stronger models should serve as later-layer aggregators. For a production system, reserve MoA for quality-critical tasks (architecture decisions, complex PRDs) and use single-model routing for latency-sensitive paths.

---

## 2. SKILL.md role bundles define what each agent knows and how it works

An emerging **Agent Skills Specification** (adopted by Anthropic/Claude, GitHub Copilot, OpenAI Codex) standardizes how agent capabilities are packaged as markdown files. Each SKILL.md uses YAML frontmatter for metadata and machine-readable configuration, followed by markdown instructions that serve as the agent's system prompt and behavioral guide.

### The SKILL.md file format

The recommended structure places critical constraints at the beginning and end of the file (research shows **85-95% instruction recall** at these positions versus 76-82% in the middle — the "lost-in-middle" effect). Keep each file under **5,000 tokens** (~500 lines) and use progressive disclosure: metadata loaded at startup, full body loaded on activation, reference files loaded on-demand.

```markdown
---
name: ui-ux-design
description: >-
  Select optimal UI components from design systems, synthesize user 
  research, ensure WCAG 2.1 AA accessibility, produce design tokens.
metadata:
  version: "1.2.0"
  role: "ui-ux-design"
  model-preference: "openai/gpt-4o"  # vision-capable for UI tasks
  composable-with: ["shared-accessibility", "shared-testing"]
allowed-tools: [FigmaRead, ShadcnLookup, AxeAudit, DesignTokenGen]
---

# Role: Senior UI/UX Design & Research Specialist

## Identity & Expertise
[Role persona and domain backstory — maps to CrewAI's role+backstory]

## Decision Framework
[Step-by-step chain-of-thought reasoning scaffold]

## Output Formats
[JSON schemas and structured output templates]

## Learned Patterns
[Auto-updated section from learning loops — see Topic 4]

## Common Mistakes to Avoid
[Auto-updated guardrails from error tracking]

## Examples
[2-3 few-shot input→output pairs]
```

### The seven role bundles and their critical configurations

**UI/UX Design and Research** needs access to the Figma API, ShadCN/Radix component registry, Axe-core for accessibility auditing, and Tailwind CSS IntelliSense. The most common failure mode is the **over-customization anti-pattern** — the agent creates custom components when design system primitives already exist. The fix: require the agent to enumerate available components before proposing anything custom. Always enforce accessibility checks as a mandatory step, not an afterthought.

**Data Analytics** requires SQL execution (BigQuery/Postgres/Snowflake), dbt CLI for model compilation, Segment/Mixpanel APIs for event tracking, and statistical libraries for A/B test analysis. The critical anti-pattern is **vanity metrics** — defining metrics that look good but don't drive decisions. Every metric definition must include the specific decision it informs. SQL generation must always run in read-only mode with LIMIT clauses.

**Domain-Driven Design & Multi-Cloud Architecture** needs Terraform/Pulumi CLI, cloud provider SDKs with pricing APIs, and diagram generation (Mermaid/PlantUML). The biggest risk is **premature microservices** — splitting into services before bounded contexts are validated. The SKILL.md should enforce starting with modular monoliths and extracting only when deployment independence is needed.

**Vector DB & RAG Setup** requires client libraries for Pinecone/Qdrant/Weaviate/pgvector, embedding APIs, LangChain/LlamaIndex for chain orchestration, and RAGAS/DeepEval for retrieval quality evaluation. The critical failure mode is **one-size-fits-all chunking** — using fixed 512-token chunks for all document types instead of adapting to document structure.

**Serverless Frontends** needs Next.js/Vercel CLI, edge function runtimes, Lighthouse/Web Vitals APIs, and bundle analysis tools. The common mistake is **SSR everything** — defaulting to server rendering when static generation would be cheaper and faster. The SKILL.md should include a decision tree: user-specific data → SSR, static cacheable → SSG, infrequently changing → ISR.

**Product Management** requires Linear/Jira API, Notion/Confluence for PRDs, analytics APIs (Amplitude/Mixpanel), and OKR tracking. The anti-pattern is **feature factory** mode — writing user stories disconnected from measurable outcomes. Every story must reference an OKR, and acceptance criteria must be quantified ("page load < 2s at p95" not "should be fast").

**QA / Total Quality Management** needs Playwright/Cypress for E2E, Jest/Vitest for unit tests, SonarQube for quality gates, and k6 for load testing. The critical anti-pattern is **test pyramid inversion** — too many E2E tests, not enough unit tests. Enforce the ratio: 70% unit, 20% integration, 10% E2E. Quality gates must actually block deployments, not just report.

### Composability and versioning

Skill files should be organized with shared sub-skills (accessibility, testing, security, documentation) that multiple roles compose into their context. Store skills in a git repository with semantic versioning in the YAML frontmatter. For **KV-cache optimization**, keep prompt prefixes stable across invocations — this alone can achieve 10x cost reduction per the Manus engineering team's production findings.

---

## 3. Persistent shared memory gives agents collective intelligence

The most validated architecture for multi-agent memory in 2026 combines **four memory types** drawn from the CoALA cognitive architecture framework (Princeton, 2023): working memory (current context window), episodic memory (past events and interactions), semantic memory (facts and knowledge), and procedural memory (learned skills and workflows). The critical innovation is **episodic-to-semantic consolidation** — patterns extracted from episodic event memories get distilled into general semantic knowledge, mirroring how human learning works.

### The OpenClaw pattern validates file-based memory at scale

Nader Dabit's OpenClaw architecture (145K+ GitHub stars) proves that **file-based markdown memory is production-viable**. The architecture uses append-only JSONL files for session persistence (crash-safe, lose at most one line), SOUL.md files for agent personality/behavior rules, and a `memory/` directory of markdown files for long-term memory with vector search overlay. When token count exceeds ~80% of the context window, older messages are automatically summarized and replaced with a condensed block. The key insight: the file system is the memory — no separate database required for the basic case, with vector search as a derived index that can be rebuilt anytime.

### Azure Cosmos DB genuinely works as both document store and vector store

**Azure Cosmos DB for NoSQL with DiskANN vector indexing can serve as a unified document + vector store**, eliminating the need to synchronize between separate systems. DiskANN (developed by Microsoft Research) is a state-of-the-art approximate nearest neighbor algorithm that leverages SSDs for billion-scale vector search. Key production characteristics:

- **Dimensions**: Up to 4,096 for DiskANN, 16,000 with Product Quantization on MongoDB vCore
- **Latency**: Sub-20ms query latency at scale, sub-100ms for billion-vector datasets
- **Sharded DiskANN** (2025): Splits indexes by a shard key like `tenantId`, delivering **91% faster searches, 85% lower RU cost, and 12% higher recall**
- **Hybrid search**: Combines vector similarity, BM25 full-text, and filter queries in a single operation
- **99.999% SLA** with multi-region geo-replication

The tradeoffs versus dedicated vector databases are real: Cosmos DB's RU-based cost model can escalate at high throughput, and pure vector performance at extreme scale may lag behind Qdrant or Pinecone. But the **elimination of data synchronization between document and vector stores** is a major architectural simplification. For an Azure-native stack, Cosmos DB with Sharded DiskANN using `tenantId` as the shard key is compelling for multi-agent memory.

For teams not committed to Azure, the comparison shows **Qdrant** as the best fit for TypeScript/Node multi-agent systems (open-source Rust performance, excellent multi-tenancy via payload filtering, strong TypeScript SDK), **pgvector** as sufficient for under 10M vectors when you're already running PostgreSQL, and **Pinecone** for zero-ops cloud deployment.

### Memory frameworks for TypeScript

**Mem0** is the most production-ready option with full TypeScript support via `@mem0/vercel-ai-provider`, integrating directly with Vercel AI SDK. It supports multi-dimensional scoping (`user_id`, `agent_id`, `app_id`, `run_id`, `org_id`, `project_id`) and achieved **91% latency reduction** versus full-context approaches with 90%+ token savings. **LangGraph.js PostgresStore** provides native namespace-based memory with vector search built into the orchestration framework. **Zep** offers temporal knowledge graphs for enterprise scenarios requiring relationship modeling. **Letta** (MemGPT) provides transparent agent self-managed memory with a visual development environment.

### Namespace hierarchy for multi-agent isolation

Memory should be hierarchically namespaced to prevent collision while enabling controlled sharing:

```
global/                        → Domain knowledge, SOPs (read: all agents)
├── org:{orgId}/               → Organization policies (read: org agents)
│   ├── project:{projectId}/   → Requirements, decisions, patterns (read: project agents)
│   │   ├── agent:{agentId}/   → Agent procedures, preferences (read: owning agent + supervisors)
│   │   └── session:{sessionId}/ → Working memory (read: active agent only)
```

In LangGraph.js, this maps to `PostgresStore` namespaces. In Cosmos DB, this maps to Sharded DiskANN with composite shard keys. In Qdrant, this maps to payload-filtered queries with visibility fields. The **Blackboard Pattern** — where agents post findings to a shared project namespace and all agents can read — is the most effective for cross-functional team coordination.

---

## 4. Learning loops turn agent failures into systematic improvements

The most powerful learning loop architecture is **ExpeL** (Experiential Learning, AAAI 2024), which accumulates experiences across many task runs and extracts generalized insights. Unlike Reflexion (which learns within a single retry loop), ExpeL compares successful and failed trajectories across different tasks and performs four operations on an insight set: **ADD** new insight, **EDIT** existing insight, **REMOVE** outdated insight, or **AGREE** to keep as-is. ExpeL outperforms Reflexion in ALFWorld (59% vs 54%) without repeated attempts, demonstrating genuine cross-task learning transfer.

### The three-speed learning architecture

The recommended architecture operates at three speeds simultaneously:

**Real-time (per-run)**: Reflexion-style self-reflection after each task failure. The agent generates a verbal self-critique stored in episodic memory, used immediately on the next attempt. This handles acute errors but doesn't generalize.

**Batch (every 25-50 runs)**: ExpeL-style insight extraction. Accumulate structured run results (input, output, score, errors, trace), then use Claude to compare successes versus failures and generate/update a set of max 15 insights. These insights get merged into the SKILL.md's "Learned Patterns" section.

**Strategic (weekly/monthly)**: DSPy/Ax-powered prompt optimization. When you have 30+ labeled examples per agent role, use the **Ax Framework** (`@ax-llm/ax` — the TypeScript port of DSPy, 2.4K GitHub stars) to run automated prompt optimization via MIPROv2 or GEPA optimizers. Ax bootstraps traces, proposes instruction variants, and uses Bayesian optimization to find the highest-performing prompt configuration.

### TQM principles map directly to agent quality management

The Deming PDCA cycle translates cleanly: **Plan** (define quality benchmarks per agent role, set evaluation datasets), **Do** (run agents with structured monitoring via Langfuse), **Check** (evaluate metrics, identify discrepancies, cluster failure modes), **Act** (update SKILL.md, deploy or rollback based on A/B test results). Six Sigma's DMAIC maps to: Define agent acceptance criteria → Measure error rates and quality scores per role → Analyze root causes via LLM-based failure classification → Improve SKILL.md and guardrails → Control via statistical process monitoring with alerts on regression.

Quality gates for agent outputs should layer: **schema validation** (Zod), **semantic quality** (LLM-as-judge scoring above threshold), **safety filtering**, **business rule enforcement** (symbolic guardrails, not prompt-based), and **regression testing** against a held-out evaluation set.

### Preventing learning loop degradation

The critical risks are prompt bloat (accumulated learnings make prompts too long), hallucination accumulation (self-generated insights may be wrong and compound), and overfitting to recent errors. Prevention strategies:

- **Cap accumulation**: Maximum 15 insights and 10 error corrections per SKILL.md
- **Active forgetting**: Remove learnings not triggered in the last N runs (ExpeL's REMOVE operation)
- **Periodic condensation**: Use Claude to compress accumulated learnings into concise rules
- **Git-based versioning**: Every SKILL.md update is a commit with evaluation metrics in the commit message, enabling one-click rollback
- **A/B validation**: Never deploy an updated SKILL.md without comparing against baseline on a held-out test set; require statistical significance before promotion
- **Continuous drift monitoring**: Sample production traffic, run automated evaluators, plot quality score trends daily; alert when scores drop regardless of whether SKILL.md changed (which indicates model drift from provider updates)

### Observability with Langfuse

**Langfuse** (open-source, MIT licensed, self-hostable) is the recommended observability platform for this stack. The TypeScript SDK v4 uses OpenTelemetry as its foundation (`@langfuse/tracing`, `@langfuse/otel`). It captures full traces of agent runs, supports LLM-as-judge evaluators, prompt versioning, and dataset management for evaluation. It's framework-agnostic, unlike LangSmith which is tightly coupled to LangChain.

---

## 5. The full architecture blueprint connects all five systems

### How the five components integrate

The system operates as a layered architecture where each component feeds the others:

```
┌────────────────────────────────────────────────────────────────────┐
│                        APPLICATION LAYER                           │
│              Next.js / Express / Hono API endpoints                │
├────────────────────────────────────────────────────────────────────┤
│                     ORCHESTRATION LAYER                             │
│            LangGraph.js StateGraph (supervisor pattern)             │
│    ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│    │ Router   │→ │ UI/UX    │  │Analytics │  │ Arch     │  ...    │
│    │ (Phi-4)  │  │ (GPT-4o) │  │(Claude)  │  │(Claude)  │        │
│    └──────────┘  └──────────┘  └──────────┘  └──────────┘        │
├────────────────────────────────────────────────────────────────────┤
│                    MODEL COMMUNICATION                              │
│         Vercel AI SDK v5/v6 + Mastra model router                  │
│         (600+ models, automatic fallbacks, streaming)               │
├────────────────────────────────────────────────────────────────────┤
│                    SKILL BUNDLE LAYER                               │
│    Git-versioned SKILL.md files loaded per-agent activation         │
│    Progressive disclosure: metadata → body → references             │
├────────────────────────────────────────────────────────────────────┤
│                    SHARED MEMORY LAYER                              │
│  ┌─────────────────┐  ┌───────────────┐  ┌──────────────────┐    │
│  │ Working Memory   │  │ Episodic +    │  │ Procedural       │    │
│  │ (LangGraph       │  │ Semantic      │  │ Memory           │    │
│  │  PostgresSaver)   │  │ (Cosmos DB    │  │ (SKILL.md files  │    │
│  │                   │  │  DiskANN +    │  │  + git versioning│    │
│  │                   │  │  Mem0)        │  │  )               │    │
│  └─────────────────┘  └───────────────┘  └──────────────────┘    │
├────────────────────────────────────────────────────────────────────┤
│                    LEARNING LOOP LAYER                              │
│  Langfuse tracing → Evaluation pipeline → ExpeL insight extraction │
│  → SKILL.md update → A/B validation → Git commit or rollback      │
│  Ax Framework (@ax-llm/ax) for periodic DSPy-style optimization    │
└────────────────────────────────────────────────────────────────────┘
```

### Recommended tech stack

| Layer | Technology | Package |
|---|---|---|
| **Runtime** | Node.js 22+ LTS, TypeScript 5.5+ | `typescript` |
| **Agent orchestration** | LangGraph.js | `@langchain/langgraph` |
| **Model communication** | Vercel AI SDK v5 + Mastra | `ai`, `@mastra/core` |
| **Claude API** | Anthropic SDK | `@anthropic-ai/sdk` |
| **Multi-provider** | Vercel AI SDK providers | `@ai-sdk/anthropic`, `@ai-sdk/openai`, `@ai-sdk/google` |
| **Short-term memory** | PostgresSaver | `@langchain/langgraph-checkpoint-postgres` |
| **Long-term memory** | Mem0 + Vercel AI SDK | `@mem0/vercel-ai-provider` |
| **Vector + document store** | Azure Cosmos DB (DiskANN) | `@azure/cosmos` |
| **Alternative vector store** | Qdrant | `@qdrant/js-client-rest` |
| **Relational + checkpoints** | PostgreSQL + pgvector | `pg`, `@langchain/community` |
| **Schema validation** | Zod | `zod` |
| **Observability** | Langfuse | `@langfuse/tracing`, `@langfuse/otel` |
| **Prompt optimization** | Ax Framework (DSPy for TS) | `@ax-llm/ax` |
| **UI framework** | Next.js 15 + ShadCN/UI | `next`, `shadcn` |
| **Testing** | Vitest + Playwright | `vitest`, `@playwright/test` |
| **Gateway (optional)** | LiteLLM Proxy | Self-hosted Docker container |

### Azure Cosmos DB's role in the architecture

Cosmos DB for NoSQL with DiskANN serves as the **unified persistence layer** for episodic and semantic memory. A single container holds both structured document data (agent run results, user profiles, project metadata) and vector embeddings (semantic memory, knowledge base chunks) — no synchronization between separate stores. Use **Sharded DiskANN with `/projectId`** as the vector index shard key to get automatic per-project index isolation with 91% faster searches. Store memory documents with a `memoryType` field (`episodic`, `semantic`, `procedural`) and a `visibility` array (`["global", "project:abc", "agent:ui-ux"]`) for access control via filter queries combined with vector search.

For teams not on Azure, substitute PostgreSQL + pgvector (for under 10M vectors) or Qdrant (for scale beyond that), with Mem0 managing the memory lifecycle.

### How SKILL.md files get loaded, versioned, and updated

**Loading**: At agent activation, the orchestrator reads the SKILL.md YAML frontmatter to determine model preference and allowed tools. The full markdown body is injected as the system prompt. Reference files in the `references/` directory are loaded on-demand when the agent needs domain-specific detail. This progressive disclosure keeps initial context lean.

**Versioning**: SKILL.md files live in the git repository alongside application code. The YAML `metadata.version` field tracks semantic versions. Every update from the learning loop creates a git commit with evaluation metrics in the commit message (e.g., `"ui-ux SKILL.md v1.3.0: accuracy 0.87→0.91 on eval set"`). Tags mark production-deployed versions. Rollback is `git revert`.

**Updating**: The ExpeL-inspired learning loop runs after every 25-50 agent runs per role. It extracts insights by comparing successes and failures, generates an updated SKILL.md via Claude, A/B tests the new version against the current production version on a held-out evaluation set, and only commits if the new version shows statistically significant improvement with no regression. The "Learned Patterns" and "Common Mistakes to Avoid" sections are the primary targets for automated updates; the core role definition and decision framework sections require human review to change.

### Suggested repository structure

```
ccqg-platform/
├── apps/
│   ├── web/                          # Next.js frontend
│   └── api/                          # Express/Hono API server
├── packages/
│   ├── agents/
│   │   ├── orchestrator/             # LangGraph supervisor graph
│   │   │   ├── graph.ts              # StateGraph definition
│   │   │   ├── nodes/                # Per-role agent nodes
│   │   │   ├── router.ts             # Model routing logic
│   │   │   └── types.ts              # State type definitions
│   │   ├── skills/
│   │   │   ├── shared/               # Composable sub-skills
│   │   │   │   ├── accessibility/SKILL.md
│   │   │   │   ├── testing/SKILL.md
│   │   │   │   └── security/SKILL.md
│   │   │   └── roles/                # Per-role skill bundles
│   │   │       ├── ui-ux-design/
│   │   │       │   ├── SKILL.md
│   │   │       │   └── references/
│   │   │       ├── data-analytics/SKILL.md
│   │   │       ├── ddd-architecture/SKILL.md
│   │   │       ├── vector-db-rag/SKILL.md
│   │   │       ├── serverless-frontend/SKILL.md
│   │   │       ├── product-management/SKILL.md
│   │   │       └── qa-tqm/SKILL.md
│   │   ├── memory/
│   │   │   ├── store.ts              # Memory store abstraction
│   │   │   ├── cosmos.ts             # Azure Cosmos DB adapter
│   │   │   ├── namespaces.ts         # Namespace hierarchy logic
│   │   │   └── consolidation.ts      # Episodic→semantic pipeline
│   │   └── learning/
│   │       ├── loop.ts               # ExpeL-inspired learning loop
│   │       ├── evaluator.ts          # Multi-layer evaluation pipeline
│   │       ├── error-tracker.ts      # Per-role error taxonomy
│   │       ├── skill-updater.ts      # SKILL.md auto-update logic
│   │       └── drift-monitor.ts      # Production drift detection
│   ├── tools/                        # MCP-compatible tool definitions
│   │   ├── figma/
│   │   ├── shadcn/
│   │   ├── sql-executor/
│   │   ├── terraform/
│   │   └── playwright/
│   └── shared/                       # Shared types, utils, config
│       ├── types.ts
│       ├── config.ts
│       └── logger.ts
├── evals/                            # Evaluation datasets per role
│   ├── ui-ux/test-cases.json
│   ├── analytics/test-cases.json
│   └── ...
├── infra/                            # IaC (Pulumi/Terraform)
│   ├── cosmos-db.ts
│   ├── postgres.ts
│   └── vercel.ts
└── turbo.json                        # Turborepo config
```

### Key open source projects to evaluate

- **Mastra** (`@mastra/core`) — TypeScript agent framework with model routing, workflows, memory, and eval runner; built on Vercel AI SDK
- **LangGraph.js** (`@langchain/langgraph`) — Stateful graph orchestration with checkpointing, human-in-the-loop, and persistence
- **Ax Framework** (`@ax-llm/ax`) — DSPy for TypeScript; automated prompt optimization with MIPROv2/GEPA
- **Mem0** (`@mem0/vercel-ai-provider`) — Production memory management with Vercel AI SDK integration
- **Langfuse** (`@langfuse/tracing`) — Open-source observability with OpenTelemetry, LLM-as-judge evaluators
- **screenshot-to-code** (github.com/abi/screenshot-to-code) — Open-source UI screenshot to code conversion
- **Together AI MoA** (github.com/togethercomputer/MoA) — Reference implementation of Mixture of Agents
- **Letta** (github.com/letta-ai/letta) — MemGPT-based transparent agent memory management
- **ShadCN/UI MCP Server** — AI-optimized component registry access via Model Context Protocol
- **LiteLLM** (github.com/BerriAI/litellm) — Proxy gateway for 400+ models with cost tracking
- **VoltAgent** — TypeScript agent architecture framework complementary to Vercel AI SDK

---

## Conclusion: build incrementally, measure ruthlessly

The architecture described here is comprehensive but should be built incrementally. **Start with the minimal viable stack**: LangGraph.js with PostgresSaver for orchestration and checkpointing, Claude API via Vercel AI SDK for all agent roles initially (add model routing later when cost data justifies it), SKILL.md files loaded as system prompts with manual versioning, and Langfuse for observability from day one. This alone produces a functional multi-agent product team system.

**Add complexity only when data demands it.** Multi-model routing becomes worthwhile when Langfuse traces show that 60%+ of Claude calls are for tasks a cheaper model could handle. The ExpeL learning loop becomes worthwhile when you have 50+ evaluated runs per agent role showing recurring failure patterns. Cosmos DB's vector capabilities become worthwhile when you exceed what pgvector can handle or when you need the unified document-vector model for operational simplicity.

The single most novel insight from this research: **the convergence of three separate trends — structured agent skill files (SKILL.md / AGENTS.md / CLAUDE.md), automated prompt optimization (DSPy/Ax), and ExpeL-style experiential learning — creates a closed loop where agents genuinely improve themselves over time.** The SKILL.md is both the input (defining agent behavior) and the output (updated by learning loops), versioned in git with A/B validation gates. This is the architectural pattern that transforms a static multi-agent system into one that gets measurably better with every task it completes.