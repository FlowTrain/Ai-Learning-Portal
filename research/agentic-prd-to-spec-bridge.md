# Agentic PRD-to-Spec Bridge: Comprehensive Unified Specification
### Clean Code Quality Guardian — Discovery → Specification Pipeline

> **Document Status:** Comprehensive Synthesis — All Four Source Documents + Canonical Outline  
> **Synthesis Sources:** ChatGPT (Roundhouse method & templates), Gemini (Strategic architecture & LLM Wiki), Perplexity (Templates & gate checklists), Claude (BMAD integration & policies), Canonical Outline (Cross-source reconciliation)  
> **Primary Audience:** Product Managers, Discovery Leads, Stakeholders, Executives, Developers, Compliance Reviewers, and Agentic Coding Workflows  
> **Authoring Model:** Human + Agent Collaborative  
> **Version:** 1.0 — July 2026

***

## Table of Contents

1. [Foundational Principle](#foundational-principle)
2. [Why This Bridge Is Needed](#why-this-bridge-is-needed)
3. [Cognitive Architecture of Continuous Discovery](#cognitive-architecture)
4. [The Three-Artifact Chain](#three-artifact-chain)
5. [Pre-Spec Scavenger List](#pre-spec-scavenger-list)
6. [Operational Frameworks for Human-Agent PRD Authorship](#operational-frameworks)
7. [PRD Document Structure — Canonical Sections](#prd-document-structure)
8. [TEMPLATE 1: Discovery PRD](#template-1-discovery-prd)
9. [The Before-SPEC Readiness Gate](#before-spec-gate)
10. [TEMPLATE 2: Spec Seed](#template-2-spec-seed)
11. [TEMPLATE 3: CCQG Segment Spec (PRD-Anchored)](#template-3-ccqg-segment-spec)
12. [PRD-to-Spec Bridge Mapping Table](#bridge-mapping-table)
13. [BMAD Agent Personas and Epic Sharding](#bmad-agent-personas)
14. [The Verifier / Implementor Parallel Execution Model](#verifier-implementor)
15. [Discovery Workbench and Business User Interface](#discovery-workbench)
16. [Nine Practices Validation](#nine-practices-validation)
17. [Tier 4 QMS Compliance and Chain of Custody](#tier-4-qms-compliance)
18. [Quality Gates Summary](#quality-gates-summary)
19. [Naming Conventions and File System Layout](#naming-conventions)
20. [Candidate Segment Spec Framing: S73 / S74 / S75](#candidate-segment-specs)
21. [Operating Policies](#operating-policies)
22. [Governance Decision Rules](#governance-decision-rules)
23. [Scale-Adaptive PRD Levels](#scale-adaptive-prd-levels)
24. [Brownfield vs. Greenfield PRD Mode](#brownfield-greenfield)

***

## Foundational Principle 

> **Core Tenet (shared across all four source documents):** The PRD and the Spec are distinct artifacts with different epistemic status. The PRD governs discovery — uncertainty is allowed. The Spec governs execution — certainty is required.

| Formulation | Source |
|---|---|
| *"PRD ≠ spec. The PRD is the intent layer; spec-instructions.md is the execution layer."* | Claude |
| *"The PRD acts as the ultimate bridge between ambiguous, human-led discovery efforts and highly structured, agent-executable technical constraints."* | Gemini |
| *"The PRD may contain hypotheses. The Spec may not."* | ChatGPT |
| *"The PRD is the Discovery governance artifact… The SPEC inherits from it directly."* | Perplexity |

**Shared Pipeline Mental Model (all four documents):**

```
Discovery / JTBD Research
  → PRD (intent, hypotheses, evidence)
    → PRD Lint
      → Before-SPEC Readiness Gate
        → Spec Seed
          → CCQG Segment Spec (S##)
            → BDD / EARS
              → Agentic Implementation
```

GitHub frames the paradigm shift underlying this model: *"We're moving from 'code is the source of truth' to 'intent is the source of truth.' With AI, the specification becomes the source of truth and determines what gets built."* In the agentic ecosystem, software development transitions from an exercise in syntax writing to a complex problem of **intent translation**: converting human business goals into deterministic, machine-readable specifications that govern autonomous execution.

***

## Why This Bridge Is Needed 

### The Upstream Constraint Problem

Historically, organizations allocated the majority of operational resources to raw code generation and manual quality assurance — the self-evident bottlenecks of the pre-AI era. With the maturation of LLMs and agentic coding frameworks, raw syntax generation is no longer the scarce resource. The critical constraints have migrated significantly upstream: the primary friction points now reside in **clarity of strategic intent**, the continuous synthesis of market intelligence, and rigorous adherence to complex regulatory frameworks.

This paradigm shift demands a transition from traditional, human-centric Agile methodologies to **Spec-Driven Development (SDD)** orchestrated by specialized AI agents.

### Why Traditional PRDs Fail Agentic Workflows 

All four source documents converge on the same root cause:

- **Tribal knowledge dependency:** Traditional user stories depend on implicit context that AI agents do not possess. Alignment loss during execution causes significantly more AI failures than incorrect task descriptions.
- **Single-shot prompt failure:** Single prompts fail on complex tasks because each step needs different thinking; chaining preserves context and gives each step full attention.
- **Vague PRD → Architectural drift:** When a PRD lacks deep user context, agents inevitably invent their own assumptions, leading to architectural drift, hallucinated dependencies, and misaligned functional requirements.
- **Defect-cost multiplier:** A requirement defect fixed in Discovery costs ~$100–$250; the same defect at Production costs ~$10,000–$25,000.

### The "Anterograde Amnesia" Problem 

LLMs suffer from **anterograde amnesia** — the inherent inability to natively retain, cross-reference, and compound institutional knowledge across isolated reasoning sessions. In standard "vibe-coding" workflows, agents must rediscover context with every interaction, leading directly to:

- Architectural drift
- Hallucinated dependencies
- Misaligned functional requirements

The solution is a persistent, agent-managed **LLM Wiki** (see §3 below).

***

## Cognitive Architecture of Continuous Discovery 

### The LLM Wiki — Three-Layer Memory

To resolve anterograde amnesia, enterprise architectures must deploy an LLM Wiki operating on the principle of "compile once and keep current." This architecture guarantees that when an executive, stakeholder, or product manager initiates a discovery workflow, the AI agents draw from a synchronized corporate memory rather than a vacuum.

| Layer | Name | Description | Key Property |
|---|---|---|---|
| **Layer 1** | Immutable Raw Sources | Read-only repository of unedited inputs: customer interview transcripts, support tickets, telemetry data, competitive analysis files | Forensic integrity for regulatory audits; prevents hallucination compounding |
| **Layer 2** | Compiled Wiki Codebase | Dynamic, deeply interlinked markdown files autonomously maintained by AI agents; synthesizes summary pages, entity profiles, and strategic shifts | Continuously updated without human intervention |
| **Layer 3** | Deterministic Schema | Constitutional config document (e.g., `CLAUDE.md`) establishing absolute structural constraints, workflows, and syntactic rules | Prevents model drift; enforces formatting standards |

Background linting agents act as a cognitive **immune system**, continuously scanning Layer 2 markdown for logical contradictions, orphan pages, stale claims, and evidentiary gaps. Evidence sources in the PRD template explicitly link to Layer 1 raw sources via an evidence table.

### The Depot and Turntable Hub Metaphor 

Traditional pipelines model the development lifecycle as a linear sequence — erroneously positioning product discovery as the first, transient sequential step. In advanced agentic frameworks, discovery is reimagined as a central, persistent **Depot**.

The Depot continuously aggregates raw market inputs across **Seven Pragmatic Tracts**: Market, Focus, Business, Planning, Programs, Enablement, and Support. Within it operates a central **Turntable Hub** — a routing mechanism that evaluates incoming market intelligence and routes specific, validated insights to the active execution trains (Structure, Quality, Ship, Certify).

When a business user or product manager initiates a feature request, it is evaluated in the Depot against the compiled Layer 2 market intelligence, ensuring the resulting PRD is anchored in validated customer needs rather than subjective, untested assumptions.

### Two-Plane Architecture 

```
Spec Plane (slow, human-aligned):
  PRD → Architecture → Stories/Specs/Plan files → serves as "API" for agents

Execution Plane (fast, machine):
  Pick one unit of work → implement → validate → commit → update state
```

The PRD lives entirely on the Spec Plane. It gates entry to the Spec.

***

## The Three-Artifact Chain 

> **Shared model across all four documents:** `Discovery PRD → Spec Seed → CCQG Segment Spec`

The correct operating model is **not** one giant PRD that becomes the spec. The stronger pattern is a controlled three-artifact chain.

| Artifact | Owner | Purpose | Agentic Coding Role |
|---|---|---|---|
| **Discovery PRD** | Product Manager, Discovery Bench, stakeholder, or human-agent pair | Capture problem validation, solution exploration, customer evidence, business metrics, segmentation, journeys, value streams, risks, and decision rationale | Supplies validated intent and boundaries |
| **Spec Seed** | Spec Translator Agent + human approver | Converts approved PRD content into the exact inputs needed by `spec-instructions.md` | Prevents lossy handoff from PRD to spec |
| **CCQG Segment Spec** | Product / Engineering / Agent collaboration | Formal executable governance artifact | Drives BDD, EARS requirements, tests, PR breakdown, and agent execution |

### Discovery PRD 

- Purpose: capture problem validation, solution exploration, customer evidence, business metrics, segmentation, journeys, value streams, risks, and decision rationale.
- The PRD **may contain hypotheses**; it is the discovery management artifact, not an engineering ticket or pseudo-spec.
- File naming convention: `docs/prd/PRD-##-kebab-case-title.md`. PRD numbering is independent of S## spec numbering.
- Equivalent to BMAD's Analysis + Planning phases.

### Spec Seed 

- A Spec Seed **must not invent** missing PRD context. It carries forward only approved or explicitly marked assumptions and identifies gaps that block spec generation.
- Must include candidate Example Map rules and NFR candidates (or state why none apply).
- Generated automatically by the Discovery Agent when the Before-SPEC Gate passes; contains Spec Seed ID (hash), source PRD commit reference, linked job stories, boundary constraints, and accepted open questions.

### CCQG Segment Spec 

- Formal executable governance artifact; drives BDD, EARS requirements, tests, PR breakdown, and agent execution.
- Must use the **10-section canonical structure** (see §11).
- File naming: `S##-kebab-case-focus-area-title.md`. The title describes *what* the segment delivers, never *how* it is built internally.
- Examples: `S29-business-slos-observability-thresholds` ✅ vs. `S29-improve-observability` ❌

***

## Pre-Spec Scavenger List 

The PRD cannot function as a static, narrative document in agentic coding. It must be a dense, context-rich extraction of market reality. The following discovery artifacts must be compiled **before** finalizing the PRD.

| Discovery Artifact | Definition and Operational Purpose | Downstream Impact on CCQG Spec | Primary Source |
|---|---|---|---|
| **Jobs-to-be-Done (JTBD) / Job Stories** | Identifies core motivation driving user behavior; shifts focus from feature requests to underlying human needs | Becomes Section 1 Objective anchor in the Spec | All |
| **Customer Pain Points** | Highlights current system failures, manual workarounds, and friction areas | Defines Unwanted Behavior EARS requirements and BDD edge cases | All |
| **Empathy Maps & Personas** | Deep context on user's emotional state, technical proficiency, and operating environment | Guides UX agents; informs accessibility NFRs | Gemini, ChatGPT |
| **Customer Journeys** | Maps chronological user actions to achieve a goal across multiple touchpoints | Informs Example Mapping; defines integration boundaries | All |
| **Transactional Value Streams** | Tracks explicit flow of data, money, or state changes through the business domain | Defines Domain Contracts, Stream Adapters, Anti-Corruption Layers | Gemini, ChatGPT |
| **Business Metrics & SLOs** | Establishes exact, measurable goals rather than vague aspirations | Translates into `observability/thresholds.yaml`; prevents hardcoded limits | All |
| **Competitive Analysis** | Analyzes competitor feature sets, strategic positioning, and market gaps | Justifies scope boundaries; prevents feature creep | Claude, Gemini, ChatGPT |
| **Client / Customer Segmentation** | Differentiates requirements by user tiers | Determines feature-flag requirements; enforces Optional Feature EARS constraints | All |
| **Customer Interview Evidence** | Raw Layer 1 source material, cited by Evidence ID | Grounds problem statement in empirical reality | ChatGPT, Perplexity |
| **Problem Validation Findings** | Empirical validation that the problem exists and is worth solving | Grounds PRD in market reality | ChatGPT |
| **Solution Exploration Boundaries** | Defines what is in-scope vs. out-of-scope for solution design | Prevents solution-prescription leakage into specs | ChatGPT |
| **Stakeholder Decisions & Decision Log** | Captures material decisions to prevent re-litigation | Provides audit trail for compliance | ChatGPT, Perplexity |
| **Regulatory / Compliance Requirements** | Documents regulatory obligations early | Drives compliance EARS requirements and HITL gates | Gemini, Perplexity |

### Four-Risk Validation Matrix 

All four dimensions must reach threshold before the Before-SPEC Gate passes:

| Risk Dimension | Question |
|---|---|
| **Desirability** | Do users/customers actually want this solved? |
| **Viability** | Does solving it create sustainable business value? |
| **Feasibility** | Can we build it with current or acquirable capability? |
| **Usability** | Will affected personas actually adopt the solution? |
| **Compliance / QMS** | Can we prove control and traceability? |

***

## Operational Frameworks for Human-Agent PRD Authorship 

Three dominant frameworks orchestrate the human-agent collaborative PRD authoring process, each optimizing for different complexity levels and required human oversight.

### The 7-Step PRD Blueprint 

Prevents feature creep and ensures seamless handoffs between discovery benches and development pipelines:

1. **Specific Project Definition** — avoid vague descriptions; be highly specific about context (e.g., "a time-tracking tool for freelance designers juggling multiple agency clients," not "a productivity app")
2. **SMART Goals** — establish exact, measurable outcomes (Specific, Measurable, Achievable, Relevant, Time-bound)
3. **Constraints and Assumptions** — document budgetary limits, regulatory requirements, timelines, and technical assumptions upfront
4. **Scope and Business Case** — explicitly define what is in-scope and, crucially, what is out-of-scope to actively halt agentic feature creep
5. **Context-Rich User/Job Stories** — provide deep context regarding who the user is, the specific problem they face, and environmental triggers
6. **Detailed Feature Explanation** — define the *Why*, *How*, and expected *Impact* for every requested capability
7. **Success Metrics** — define clear, quantitative metrics that downstream automated test plans can definitively measure

### The 3-Step Iterative Scaffold Workflow 

For teams leveraging conversational LLMs, a dual-agent strategy uses one model to architect the prompt and another to generate content:

1. **Scaffold Generation** — human inputs a basic project description into a pre-structured template, fed into a structural model that generates a high-level scaffold and a custom prompt optimized for a secondary model
2. **PRD Generation** — the human pastes the optimized prompt into a detail-oriented model (e.g., Claude) that expands the scaffold into a deeply detailed, production-ready PRD
3. **Review and Polish (Multi-Agent Critique)** — the PRD is fed back to the original model acting as an independent adversarial critic, identifying missing edge cases, security vulnerabilities, or logic gaps; the human reviews the critique and feeds valid points to the secondary model for final revision

### The Clarify → Execute → Refine Chain 

The multi-prompt chain approach for complex PRDs:

- **Clarify** — the model confirms its understanding and surfaces ambiguities and assumptions before drafting
- **Execute** — full PRD generation with appropriate depth
- **Refine** — human reviews and edits for intent, context, and edge cases; the PRD then seeds the CLAUDE.md/AGENTS.md agent memory

### Prompt Hub Workflows (IDE/CLI) 

Four distinct pathways for integrated development environments:

- **Single-Shot Prompt (Speed)** — comprehensive brain-dump → production-ready PRD in one inference pass; strictly reserved for minor feature additions
- **Scaffold Prompt (Quality Control)** — agent outputs concise outline for human review; human approves scaffold before full PRD expansion
- **PRD Wizard Pack (Guided CLI)** — interactive Q&A using custom slash commands; forces section-by-section progression
- **Projects Kit (Persistent Context)** — custom instructions + uploaded knowledge files tied to the LLM Wiki for ongoing enterprise-scale development

***

## PRD Document Structure — Canonical Sections 

All four documents define PRD sections. The canonical set below merges all unique sections across every source.

### PRD Frontmatter / Metadata

| Field | Source |
|---|---|
| PRD ID | All |
| Title (problem-framed, not solution-framed) | All |
| Workstream (Letter — Name) | Perplexity, Claude |
| Status (`Draft \| In Discovery \| Stakeholder Review \| Approved \| Spec-Seeded \| Closed`) | Perplexity, ChatGPT |
| Authored By / Authoring Mode (`Human \| Human+Agent Collaborative \| Discovery Bench Generated`) | All |
| Discovery Mode (`Sync Interview \| Async Workbench \| Agent-Initiated`) | Perplexity |
| Primary Owner / Approvers | ChatGPT |
| Linked Spec Seed / Linked Segment Spec | ChatGPT, Perplexity |
| Evidence Repository | ChatGPT |
| PRD Level (0–4, scale-adaptive) | Claude |
| Project Type (`greenfield \| brownfield`) | Claude |
| Source Artifacts (brief, PRFAQ, interviews) | Claude |
| Strategic Alignment Link | Claude |
| Created / Last Updated / Change Log | All |

### Section 1 — Job Story

- **Format:** *"When [situation], I want to [motivation], so I can [outcome]."*
- Must be **solution-agnostic** — no technology names, UI terms, file names, or tool names.
- **Technology-swap test:** if the implementation stack were replaced entirely, would the situation, motivation, and outcome still hold?
- Job Stories supersede User Stories for JTBD pipelines; invented by Intercom/Paul Adams, formalized by Alan Klement (2013).
- A **Solution-Prescription Filter log** captures solution-prescriptive requests and restates them as JTBD outcomes.
- Multiple job stories supported; each carries a priority (Must / Should / Could) and links to evidence.

### Section 2 — Problem Statement & Evidence

- Anchor to observable evidence: customer interview quotes, support ticket patterns, telemetry metrics, regulatory requirements.
- Evidence Sources table: Source | Signal Type | Date | Key Quote / Data Point
- Who Is Affected table: Persona | Role | How the Problem Manifests
- **Cost of Inaction** subsection with defect-cost multiplier framework (Discovery ~$100–$250 vs. Production ~$10,000–$25,000)
- Discovery Context: Trigger (why this PRD was created), Source Inputs table, Discovery Questions
- Evidence links directly to Layer 1 of the LLM Wiki for forensic traceability

### Section 3 — Outcome Hypothesis / Executive Decision Summary

- States the measurable outcome, not a feature list.
- **Format:** *"We believe [capability] will result in [outcome] for [persona], measured by [metric]."*
- Includes: Problem Statement, Recommendation (product direction decision), Decision Needed, Confidence Level (Low / Medium / High with rationale)
- Include **AI-specific metrics** alongside traditional user metrics: accuracy, hallucination rate, latency, response quality

### Section 4 — Target Customer & Segmentation Strategy

- Primary segment, secondary segments, excluded segments.
- Primary Segment fields: Name, Who they are, Context, Pain intensity (Low/Medium/High), Buying/adoption influence (User/Buyer/Recommender/Approver/Compliance Gatekeeper)
- **Excluded Segments** — explicitly name who is NOT targeted and why; AI cannot infer scope from omission
- Personas framed situation-first (not demographic-first) to align with Job Story format

### Section 5 — Jobs, Pain Points & Empathy

- Additional Job Stories table: ID | Job Story | Segment | Evidence | Priority
- Customer Pain Points table: Pain Point | Evidence | Impact | Current Workaround | Severity
- Empathy Map: Says | Thinks | Does | Feels
- Empathy Maps inform UX/UI agents and accessibility NFRs

### Section 6 — Customer Journey & Transactional Value Stream

- Current Journey table: Step | Actor | Goal | Friction | Evidence | Opportunity
- Target Journey table: Step | Actor | Desired Experience | Success Signal | Risk
- Transactional Value Stream table: Step | Input | Activity | Output | Wait/Delay | Defect/Rework Risk | Improvement Hypothesis
- Value streams define Domain Contracts, Stream Adapters, and Anti-Corruption Layers

### Section 7 — Business Metrics & Validation Plan

- Business Outcome Metrics with baseline, target, measurement method, and review cadence.
- Product / Adoption Metrics table
- Learning Metrics: Assumption | Validation Method | Evidence Needed | Decision Rule (Continue / Pivot / Stop)
- Metrics translate into `observability/thresholds.yaml` and prevent hardcoded SLOs
- Include AI-specific metrics: accuracy, hallucination rates, response quality

### Section 8 — Scope

- **In Scope** — problem space bullets in problem language (not feature language); each maps to an evidence source
- **Out of Scope** — explicit exclusions; AI cannot infer scope from omission; link to owning PRD or segment
- **Constraints & Boundary Conditions** table: Technical | Compliance | Organizational | Time constraints

### Section 9 — Stakeholder Alignment & Open Questions

- Stakeholders table: Persona | Name/Role | Alignment Status | Sign-Off Required
- Open Questions (Discovery Blockers) table: these must be resolved before Before-SPEC Gate passes

### Section 10 — Before-SPEC Gate Checklist

*(See §9 below for full specification)*

### Section 11 — Discovery Decision Log

- Append-only record of every material discovery decision: things learned, pivots made, questions resolved, scope changes

### Section 12 — Spec Seed Manifest

*(Populated automatically by Discovery Agent when Before-SPEC Gate passes)*

***

## TEMPLATE 1: Discovery PRD 

```markdown
# PRD-##: {Title — Problem-Framed, Not Solution-Framed}

**PRD ID:** PRD-##
**Workstream:** {Letter} — {Workstream Name}
**Phase:** {Number} ({Phase Name})
**Status:** {Draft | In Discovery | Stakeholder Review | Approved | Spec-Seeded | Closed}
**Authored By:** {Human | Human+Agent Collaborative | Discovery Bench Generated}
**Discovery Mode:** {Sync Interview | Async Workbench | Agent-Initiated}
**PRD Level:** {0 | 1 | 2 | 3 | 4} (scale-adaptive routing)
**Project Type:** {greenfield | brownfield}
**Primary Owner:** {Name / Role}
**Approvers:** {Product / Design / Engineering / Compliance / Executive}
**Linked Spec Seed:** {spec-seed path or TBD}
**Linked Segment Spec:** {S## path or TBD}
**Evidence Repository:** {Raw source folder / interview set / research packet}
**Strategic Alignment Link:** {OKR / roadmap ref}
**Source Artifacts:** {brief.md, prfaq.md, interview-set-##}
**Created:** {YYYY-MM-DD}
**Last Updated:** {YYYY-MM-DD}
**Change Log:**
  - {YYYY-MM-DD} — {What changed and why}

---

## 1. Job Story (Required — Open First)

> *"When [situation], I want to [motivation], so I can [outcome]."*

**Rules:**
- No technology names, file names, format names, or tool names.
- Technology-swap test: if the implementation stack were replaced entirely,
  would the actor's situation, motivation, and outcome still be true?
- This is NOT a solution statement. Fail fast if it reads like one.
- Priority: Must | Should | Could

**Example (passing):**
> *When I have a validated business problem that needs to enter the pipeline,
> I want to describe the core need using simple guided prompts, so I can
> initiate the formal specification process without technical friction.*

**Example (failing — solution-prescriptive):**
> *When I want to create a Markdown spec, I want a UI form that calls
> Claude, so I can generate EARS notation automatically.*

**Additional Job Stories (if multiple):**

| ID | Job Story | Segment | Evidence | Priority |
|----|-----------|---------|----------|----------|
| JS-01 | When..., I want..., so I can... | {Segment} | {Evidence ID} | Must |
| JS-02 | When..., I want..., so I can... | {Segment} | {Evidence ID} | Should |

**Solution-Prescription Filter Log:**
| Original Request | JTBD Reframe |
|---|---|
| {Solution-prescriptive request} | {Restated as JTBD outcome} |

---

## 2. Problem Statement & Evidence

### 2.1 The Problem

Describe the pain, gap, or opportunity in 2–4 sentences. Anchor to observable
evidence — customer interview quotes, support ticket patterns, production
metrics, or regulatory requirements. Do NOT describe the solution here.

**Evidence Sources** (link to Layer 1 raw sources where possible):

| Source | Signal Type | Date | Key Quote / Data Point |
|--------|-------------|------|------------------------|
| {Customer interview transcript} | Qualitative | {date} | "{quote}" |
| {Support ticket pattern} | Quantitative | {date} | "{N tickets/week about X}" |
| {Telemetry / DORA metric} | Quantitative | {date} | "{metric value}" |
| {Regulatory requirement} | Compliance | {date} | "{rule citation}" |

### 2.2 Who Is Affected

| Persona | Role | How the Problem Manifests |
|---------|------|--------------------------|
| {Persona 1} | {Role} | {Concrete impact} |
| {Persona 2} | {Role} | {Concrete impact} |

### 2.3 Cost of Inaction

Quantify or qualify what degrades without solving this problem. Where possible,
anchor to the defect-cost multiplier framework: a requirement defect fixed in
Discovery costs ~$100–$250; the same defect at Production costs ~$10,000–$25,000.

---

## 3. Outcome Hypothesis / Executive Decision Summary

### 3.1 Outcome Hypothesis

State the **measurable outcome** this effort pursues. This is not a feature list.

**Format:** "We believe [capability delivered] will result in [outcome]
for [persona], measured by [metric / leading indicator]."

### 3.2 Recommendation

{State the recommended product direction. Decision recommendation, not a technical
implementation plan.}

### 3.3 Decision Needed

{What decision must stakeholders make after reading this PRD?}

### 3.4 Confidence Level

**Confidence:** Low | Medium | High
**Why:** {Evidence-based rationale}

### 3.5 AI-Specific Metrics (where applicable)

| Metric | Baseline | Target | Measurement Method |
|--------|---------|--------|--------------------|
| Accuracy | {%} | {%} | {Method} |
| Hallucination Rate | {%} | {%} | {Method} |
| Response Latency | {ms} | {ms} | {Method} |
| Response Quality | {score} | {score} | {Method} |

---

## 4. Scope

### 4.1 In Scope — What This Effort Addresses

Bullet list of the problem space this PRD covers. Use problem language, not
feature language. Each bullet should map to at least one evidence source in §2.1.

- {Problem dimension 1}
- {Problem dimension 2}
- {Problem dimension 3}

### 4.2 Out of Scope — Explicit Exclusions

Bullet list of adjacent problems this PRD deliberately does NOT address.
AI cannot infer scope from omission — all exclusions must be stated positively.

- {Adjacent problem 1} — owned by {PRD-## or S##}
- {Adjacent problem 2} — deferred to Phase {N}

### 4.3 Constraints & Boundary Conditions

| Constraint Type | Description | Source |
|-----------------|-------------|--------|
| Technical | {e.g., Must not require new infrastructure in Phase 2} | {ADR or S##} |
| Compliance | {e.g., Audit trail must satisfy 7-year retention per FINRA Rule 4511} | {Regulatory ref} |
| Organizational | {e.g., Business users cannot be required to learn Git} | {Stakeholder interview} |
| Time | {e.g., Must be deliverable within 1 sprint} | {Program plan} |

---

## 5. Target Customer & Segmentation Strategy

### 5.1 Primary Segment

**Segment Name:** {Name}
**Who they are:** {Description}
**Context:** {When this problem appears}
**Pain intensity:** Low | Medium | High
**Buying / adoption influence:** User | Buyer | Recommender | Approver | Compliance Gatekeeper

### 5.2 Secondary Segments

| Segment | Problem Variation | Value Hypothesis | Evidence Strength |
|---------|-------------------|------------------|------------------|
| {Segment} | {Variation} | {Hypothesis} | Low / Medium / High |

### 5.3 Excluded Segments

{Who is explicitly not targeted by this PRD and why?}

---

## 6. Jobs, Pain Points & Empathy

### 6.1 Customer Pain Points

| Pain Point | Evidence | Impact | Current Workaround | Severity |
|-----------|---------|--------|--------------------|---------|
| {Pain} | {Evidence ID} | {Impact} | {Workaround} | H/M/L |

### 6.2 Empathy Map

| Says | Thinks | Does | Feels |
|------|--------|------|-------|
| {Quotes from interviews} | {Internal beliefs/concerns} | {Observable actions} | {Emotional state} |

---

## 7. Customer Journey & Transactional Value Stream

### 7.1 Current Journey (As-Is)

| Step | Actor | Goal | Friction | Evidence | Opportunity |
|------|-------|------|---------|---------|-------------|
| {Step} | {Actor} | {Goal} | {Friction} | {Evidence} | {Opportunity} |

### 7.2 Target Journey (To-Be)

| Step | Actor | Desired Experience | Success Signal | Risk |
|------|-------|--------------------|---------------|------|
| {Step} | {Actor} | {Experience} | {Signal} | {Risk} |

### 7.3 Transactional Value Stream

| Step | Input | Activity | Output | Wait/Delay | Defect/Rework Risk | Improvement Hypothesis |
|------|-------|----------|--------|-----------|-------------------|----------------------|
| {Step} | {Input} | {Activity} | {Output} | {Wait} | {Risk} | {Hypothesis} |

---

## 8. Business Metrics & Validation Plan

### 8.1 Business Outcome Metrics

| Metric | Baseline | Target | Measurement Method | Review Cadence |
|--------|---------|--------|--------------------|---------------|
| {Metric} | {Baseline} | {Target} | {Method} | {Cadence} |

### 8.2 Product / Adoption Metrics

| Metric | Definition | Target | Data Source |
|--------|-----------|--------|------------|
| {Metric} | {Definition} | {Target} | {Source} |

### 8.3 Learning Metrics (Hypothesis Validation)

| Assumption | Validation Method | Evidence Needed | Decision Rule |
|-----------|------------------|----------------|--------------|
| {Assumption} | {Method} | {Evidence} | Continue / Pivot / Stop |

---

## 9. Prioritization & Risk

### 9.1 Four-Risk Validation Matrix

All four must reach threshold before the Before-SPEC Gate passes.

| Risk Dimension | Question | Signal / Evidence | Status |
|----------------|---------|------------------|--------|
| **Desirability** | Do users/customers actually want this solved? | {Evidence} | ✅ / ⚠️ / ❌ |
| **Viability** | Does solving it create sustainable business value? | {Evidence} | ✅ / ⚠️ / ❌ |
| **Feasibility** | Can we build it with current or acquirable capability? | {Evidence} | ✅ / ⚠️ / ❌ |
| **Usability** | Will affected personas actually adopt the solution? | {Evidence} | ✅ / ⚠️ / ❌ |
| **Compliance / QMS** | Can we prove control and traceability? | {Evidence} | ✅ / ⚠️ / ❌ |

### 9.2 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| {Risk 1} | H/M/L | H/M/L | {Mitigation approach} |
| {Risk 2} | H/M/L | H/M/L | {Mitigation approach} |

---

## 10. Stakeholder Alignment

### 10.1 Stakeholders

| Persona | Name / Role | Alignment Status | Sign-Off Required? |
|---------|------------|-----------------|-------------------|
| {Requestor} | {Name/Role} | Aligned / Pending / Escalated | Yes/No |
| {Impacted User} | {Name/Role} | Aligned / Pending / Escalated | Yes/No |
| {Compliance Owner} | {Name/Role} | Aligned / Pending / Escalated | Yes/No |
| {Tech Lead} | {Name/Role} | Aligned / Pending / Escalated | Yes/No |

### 10.2 Open Questions (Discovery Blockers)

These must be resolved before Before-SPEC Gate passes. Each question blocks
spec seeding until answered.

| # | Question | Owner | Target Resolution Date | Status |
|---|---------|-------|----------------------|--------|
| Q1 | {Unanswered question that could change scope or design} | {Name} | {date} | Open / Resolved |
| Q2 | {Another blocker} | {Name} | {date} | Open / Resolved |

---

## 11. Before-SPEC Gate Checklist

This gate must pass before spec seeding. The Discovery Agent (S41) evaluates
these criteria programmatically; a human reviewer verifies the judgment.

- [ ] Job Story in §1 passes the technology-swap test
- [ ] Job Story contains no solution description (no tech names, UI terms, format references)
- [ ] Problem statement in §2.1 is anchored to at least one evidence source
- [ ] All four dimensions of the risk matrix in §9.1 are at ✅ or acknowledged at ⚠️ with mitigation
- [ ] All Open Questions in §10.2 are Resolved (or accepted as post-spec clarifications with documented owner)
- [ ] Stakeholders with "Sign-Off Required: Yes" have confirmed alignment
- [ ] Scope In/Out in §4 explicitly lists exclusions (not just inclusions)
- [ ] Outcome Hypothesis in §3.1 states a measurable metric (not a feature delivery)
- [ ] Constraints in §4.3 are documented (even if "No constraints identified")
- [ ] PRD Lint has been run (solution bias, missing evidence, missing metrics checks)
- [ ] Nine Practices validation passed (no prescriptive implementation requirements)

**Gate Decision:**
- `PASS` — Spec seed authorized. PRD Status → `Spec-Seeded`. Linked Spec: `S##`
- `CONDITIONAL PASS` — Specific open questions accepted for post-spec resolution;
  documented in Decision Log below
- `FAIL` — Return to Discovery. Reason: {state blocker}

**Gate Reviewer:** {Name / Agent}
**Gate Date:** {YYYY-MM-DD}

---

## 12. Discovery Decision Log

Record every material discovery decision. Append-only — never delete entries.

| Decision | Context / Options Considered | Rationale | Date |
|----------|------------------------------|-----------|------|
| {Decision made during discovery} | {What was considered} | {Why this direction} | {date} |

---

## 13. Spec Seed Manifest

*Populated automatically by the Discovery Agent when Before-SPEC Gate passes.*

```
Spec Seed ID: {hash}
Generated: {timestamp}
Source PRD: docs/prd/PRD-##-{title}.md @ {commit hash}
Linked Job Stories: {list}
Boundary Constraints: {list from §4.3}
Open Questions Accepted: {list from §10.2 with owner}
Output: docs/specs/S##-{title}.md (Draft)
```
```

***

## The Before-SPEC Readiness Gate 

The readiness gate determines whether the PRD is stable enough to generate a Spec Seed. Introduced by all four source documents and most formally specified in Perplexity, with algorithmic detail from Gemini.

### Method Flow 

```
Raw Evidence
  ↓
Discovery Memory (LLM Wiki Layer 2)
  ↓
Discovery PRD
  ↓
PRD Lint (checks: solution bias, missing evidence, missing metrics,
         missing segmentation, unbounded scope, speculative requirements,
         weak job stories, missing decision owners, conflicting intent)
  ↓
Before-SPEC Readiness Gate
  ↓ PASS              ↓ CONCERNS                  ↓ FAIL
Spec Seed         Ask clarification           Return to Discovery
```

### Gate Outcomes 

- **PASS** — Generate Spec Seed; PRD Status → `Spec-Seeded`
- **CONDITIONAL PASS** — Specific open questions accepted for post-spec resolution with documented owner
- **FAIL** — Return to discovery with stated blocker

***

## TEMPLATE 2: Spec Seed 

```markdown
# Spec Seed: {PRD Title}

**Spec Seed ID:** {hash}
**Generated:** {timestamp}
**Source PRD:** docs/prd/PRD-##-{title}.md @ {commit hash}
**PRD Gate Decision:** PASS | CONDITIONAL PASS
**Gate Date:** {YYYY-MM-DD}
**Gate Reviewer:** {Name / Agent}

---

## 1. Inherited Job Story

> *{Copy verbatim from PRD §1. Do not modify. If this must change,
> open a PRD amendment and regenerate the spec seed.}*

---

## 2. Approved Scope Boundaries

**In Scope (from PRD §4.1):**
- {Problem dimension 1}
- {Problem dimension 2}

**Out of Scope (from PRD §4.2):**
- {Exclusion 1}
- {Exclusion 2}

---

## 3. Constraints Carried Forward (from PRD §4.3)

| Constraint Type | Description | Source |
|-----------------|-------------|--------|
| {Type} | {Description} | {Source} |

---

## 4. Candidate Example Map Rules

*The Spec Seed must not invent rules. These are derived from PRD §5–§7.*

- **Rule 1:** {Plain English rule statement}
  - Happy path: {Expected behavior}
  - Edge case: {Boundary behavior}
  - Failure case: {Violation behavior}

---

## 5. NFR Candidates

*State why none apply if not present.*

| NFR Category | Candidate Requirement | Source (PRD Section) |
|---|---|---|
| Performance | {e.g., Response <200ms} | §8.1 |
| Security | {e.g., All tokens rotated on session end} | §4.3 |
| Observability | {e.g., All state transitions logged to thresholds.yaml} | §8.1 |
| Compliance | {e.g., 7-year audit retention per FINRA Rule 4511} | §4.3 |

---

## 6. Gaps That Block Spec Generation

*The Spec Seed must not invent missing context. Gaps must be surfaced here.*

| Gap | Blocking? | Clarification Owner | Target Date |
|-----|----------|--------------------|-----------:|
| {Missing information} | Yes / No | {Owner} | {date} |

---

## 7. Accepted Open Questions

*From PRD §10.2 — accepted for post-spec resolution with documented owner.*

| Question ID | Question | Owner | Resolution Deadline |
|-------------|---------|-------|---------------------|
| Q1 | {Question} | {Name} | {date} |

---

## 8. Target Spec

**Output:** `docs/specs/S##-{title}.md` (Status: Draft)
**Linked PRD:** `docs/prd/PRD-##-{title}.md`
**Spec Seed must be re-generated if PRD is amended after gate.**
```

***

## TEMPLATE 3: CCQG Segment Spec (PRD-Anchored) 

This template extends the existing `spec-instructions.md` format with explicit PRD traceability fields. All existing section rules from `spec-instructions.md` remain in force. Fields marked **[PRD Bridge]** are additions from this bridge specification.

```markdown
# S##: {Title of the Segment}

**Segment:** S##
**Workstream:** {Letter} — {Workstream Name}
**Phase:** {Number} ({Phase Name})
**Status:** {Draft | Spec Draft — Pending Review | Approved | In Progress |
            Implemented — Pending Review | Complete}
**Spec Type:** {stream-aligned | platform | complicated-subsystem | enabling}
**Depends On:** S## (Short Name), S## (Short Name)
**Estimated Effort:** {N sprint(s)}
**PR Strategy:** Spec PR → {N} implementation PR(s)

**[PRD Bridge] Source PRD:** PRD-## — {PRD Title}
**[PRD Bridge] Spec Seed ID:** {hash from PRD §13}
**[PRD Bridge] Discovery Mode:** {Human | Human+Agent Collaborative}
**[PRD Bridge] Before-SPEC Gate Date:** {YYYY-MM-DD}

---

## 1. Objective

**[PRD Bridge — Inherited Job Story]**
> *Copy the Job Story verbatim from PRD §1. Do not modify it here. If the
> implementation team discovers the Job Story must change, open a PRD amendment
> and regenerate the spec seed. The Job Story is the contract between Discovery
> and Delivery.*

**What** — What does this segment deliver? (3–5 sentences, technical now allowed)

**Why** — What gap does it close? What breaks or degrades without it?
Link to the evidence sources in PRD §2.1 rather than restating them inline.

**Measurable Outcome** — What is verifiably different once this spec is implemented?
This must be traceable to the Outcome Hypothesis in PRD §3.1.

---

## 2. Scope

#### 2.1 In Scope

Bulleted list of every deliverable: scripts, schemas, config files, documentation
files, workflow changes, and test files. Use file paths.

| PRD §4.1 Problem Dimension | Spec Deliverable (file path) |
|---------------------------|------------------------------|
| {Problem from PRD} | `path/to/deliverable` |

#### 2.2 Out of Scope

Items explicitly excluded, linked to PRD §4.2 exclusions. New exclusions
discovered during spec authoring must be added to the PRD Decision Log as well.

---

## 3. Technical Design

### 3.1 {Module / Component Architecture}

Technical design sections as required. Use named subsections, ASCII/Markdown
diagrams, and fenced code blocks with language specifiers.

**[PRD Bridge — Constraint Compliance Table]**

Every constraint in PRD §4.3 must have a named entry here confirming
how the design satisfies it.

| PRD Constraint | Design Decision That Satisfies It |
|----------------|----------------------------------|
| {Constraint from PRD §4.3} | {Technical decision} |

### 3.X Non-Functional Requirements

Cover: Performance, Security, Observability, Reliability, Tuneable Values.
If a dimension does not apply, state it explicitly.
All threshold values must reference `observability/thresholds.yaml`.

### 3.Y EARS Requirements

All functional requirements use EARS notation. Write requirements in EARS
notation before specifying implementation approach.

| Pattern | Requirement |
|---------|-------------|
| Ubiquitous | The system shall {action} |
| Event-Driven | When {trigger}, the system shall {action} |
| State-Driven | While {state}, the system shall {action} |
| Optional Feature | Where {feature is enabled}, the system shall {action} |
| Unwanted Behaviour | If {condition}, then the system shall {action} |

---

## 4. BDD Scenarios

BDD scenarios bridge the Job Story (§1 / PRD §1) and the EARS requirements (§3).
Written *before* implementation begins.

### 4.1 Example Map

**[PRD Bridge]** Every rule here must be traceable to a scope item in PRD §4.1
or a constraint in PRD §4.3. If a rule has no PRD anchor, record it in the
Decision Log (§9) and consider whether it requires a PRD amendment.

**Rule:** {State the rule in plain English}
- Happy path: {What happens when everything works}
- Edge case: {What happens at the boundary}
- Failure case: {What happens when the rule is violated}

Minimum: 2 rules × 3 examples each.

### 4.2 Gherkin Scenarios

```gherkin
Feature: {Feature name matching the spec title}

  Background:
    Given {shared context for all scenarios}

  Scenario: {Happy path — descriptive name}
    Given {precondition}
    When {action}
    Then {expected outcome}
    And {additional assertion}

  Scenario: {Edge case — descriptive name}
    Given {precondition at boundary}
    When {action}
    Then {expected boundary behaviour}

  Scenario: {Failure case — descriptive name}
    Given {failure precondition}
    When {action that triggers the rule}
    Then {system response to violation}
```

---

## 5. Test Strategy

- **BDD test wiring** — test runner, `.feature` file location, step definitions
- **Unit test approach** — framework, mocking strategy, coverage target
- **Integration / smoke test approach** — end-to-end verification needed
- **Manual verification steps** — if any remain after automation
- **Coverage target** — minimum % and TIMC quadrant mapping

---

## 6. PR Breakdown

One subsection per PR:
- PR title: `feat(S##): short description`
- Branch: `feat/s##-kebab-description`
- Depends on: list of merged PRs or segments
- Delivers: new files + modified files with paths
- Acceptance gate: numbered list of commands
- Commits: fenced commit message block

---

## 7. Dependencies

### 7.1 Hard Dependencies

| Segment | What is consumed from it |
|---------|--------------------------|
| PRD-## | Job Story, Scope Boundaries, Constraint Table, Spec Seed |
| S## | {What specifically} |

**[PRD Bridge]** PRD-## is always a hard dependency. This spec must not
reach `Approved` status unless the linked PRD is in `Spec-Seeded` status.

### 7.2 Soft Dependencies

Table of segments that improve the result but are not strictly required.

### 7.3 What Downstream Segments Depend On

Living table of segments that will consume this spec's outputs.

---

## 8. Acceptance Criteria

Binary, testable criteria. Each must be verifiable by running a command,
inspecting a file, or completing a checklist item.

- [ ] {AC-01: Binary testable criterion}
- [ ] {AC-02: Binary testable criterion}
- [ ] {AC-03: Binary testable criterion}

**[PRD Bridge]** All acceptance criteria must be traceable to the Outcome
Hypothesis in PRD §3.1.

---

## 9. Decision Log

Append-only record of spec-level decisions. PRD-level decisions belong in the
PRD §12 Decision Log; only decisions that arise after spec seeding go here.

| Decision | Options Considered | Rationale | Date |
|----------|--------------------|-----------|------|
| {Decision} | {Options} | {Why} | {date} |

---

## 10. Definition of Done (Gate 5 Matrix)

Determined by Spec Type:

| Spec Type | Done When |
|-----------|----------|
| stream-aligned | A named user can reach the change in the running product |
| platform | At least one consumer is wired through the contract |
| complicated-subsystem | Internal logic is hidden behind the facade |
| enabling | The artifact is merged and in force |

**Delivery surface is reachable:** ✅ / ❌
**Gate 5 validated by:** `validate-spec-taxonomy.mjs`
```

***

## PRD-to-Spec Bridge Mapping Table 

This table shows the deterministic translation from PRD sections to CCQG Spec targets:

| PRD Section (Business Context) | CCQG Spec Target (Engineering Contract) | Agentic Transformation Mechanism |
|---|---|---|
| §1 Job Story | Spec §1 Objective | Job Story copied verbatim; grounds the AI in the *Why* before the *How* |
| §2 Problem Statement & Evidence | Spec §3 EARS — Unwanted Behavior requirements | Architect agent translates pain points into Unwanted Behavior EARS statements |
| §3 Outcome Hypothesis | Spec §8 Acceptance Criteria | All ACs must trace to the Outcome Hypothesis; Verifier validates against PRD §3 |
| §4 Scope — In/Out | Spec §2 Scope + Spec §6 PR Breakdown | Scrum Master maps MVP scope to repository paths; shards into sequential PRs |
| §4.3 Constraints | Spec §3 Constraint Compliance Table | Every PRD constraint requires a named spec entry confirming the design satisfies it |
| §5 Customer Segmentation | Spec §8 Acceptance Criteria (segment gating) | Segment constraints dictate feature-flag logic; Verifier generates test cases validating unauthorized segments cannot access the feature |
| §6 Customer Journey & Value Stream | Spec §3 EARS requirements + Domain Contracts | Architect translates user actions into Ubiquitous/Event-Driven EARS; value stream → Stream Adapters, Anti-Corruption Layers |
| §6 Transactional Value Stream | Spec §3.Y Canonical Contract | Data flow formalized into a single canonical JSON schema; agent links repository path |
| §7 Business Metrics & SLOs | Spec §3.X Non-Functional Requirements | Metrics converted into machine-readable parameters; SLOs dynamically linked to `observability/thresholds.yaml` |
| §5.2 Pain Points / Empathy Map | Spec §4 BDD Scenarios (edge cases) | Example mapping exercises synthesized into executable Gherkin Given/When/Then |

***

## BMAD Agent Personas and Epic Sharding 

The Breakthrough Method for Agile AI-Driven Development (BMAD) provides the structural framework for translating the Scavenger List and PRD into executable code. Rather than relying on a monolithic generalist prompt, BMAD assigns tightly scoped contexts to individual agents — each receiving only the specific artifacts necessary to execute its role.

### Core BMAD Agent Roster 

| Agent | Role | PRD-Pipeline Responsibility |
|---|---|---|
| **Analyst (Mary)** | `bmad-agent-analyst` | Brainstorm, Market Research, Domain Research, Technical Research, Create Brief, PRFAQ Challenge |
| **Product Manager (John)** | `bmad-agent-pm` | Create/Update/Validate PRD, Create Epics and Stories, Implementation Readiness |
| **Architect (Winston)** | `bmad-agent-architect` | Create Architecture, Implementation Readiness, EARS translation |
| **Developer (Amelia)** | `bmad-agent-dev` | Dev Story, Quick Dev, QA test gen, Code Review, Sprint Planning |
| **UX Designer (Sally)** | `bmad-agent-ux-designer` | Create UX Design; connects to Figma MCP for exact brand colors and component rules |
| **Scrum Master** | Epic sharding role | Systematically breaks PRD into hyper-detailed, self-contained sprint story files |
| **QA Engineer** | Verifier role | Validates output against spec; generates documentation |
| **Technical Writer (Paige)** | `bmad-agent-tech-writer` | Document Project, Validate Doc, Explain Concept |

### BMAD Four-Phase Lifecycle 

1. **Analysis (optional):** brainstorming, market/domain/technical research, Product Brief, PRFAQ (Working Backwards). Produces `brief.md`, research findings, `prfaq-{project}.md`
2. **Planning:** `bmad-prd` workflow — facilitated discovery, three intents (Create/Update/Validate). Produces `prd.md`, `addendum.md`, `.memlog.md`
3. **Solutioning:** Architecture (`ARCHITECTURE-SPINE.md`), Create Epics and Stories, Implementation-Readiness gate
4. **Implementation:** sprint planning, create-story, dev-story, code-review, retrospective; tracked in `sprint-status.yaml`

**Critical structural decision:** Epics and stories belong **downstream of the PRD**, in the Solutioning phase. They are explicitly NOT in the PRD itself (BMAD v6 removed the in-PRD `epics-template.md`).

### Epic Sharding 

The Scrum Master agent executes **epic sharding**: the comprehensive PRD is systematically broken down into hyper-detailed, self-contained sprint story files. These files contain:

- Full architectural context
- Implementation guidelines
- Embedded reasoning explaining the rationale behind each requirement
- Absolute repository paths identifying specific file modifications
- Sequential PR ordering

***

## The Verifier / Implementor Parallel Execution Model 

This is one of the most critical architectural contributions, unique to the Gemini source document but adopted across all four.

When the Developer agent (Implementor) begins coding from Spec §3, a parallel QA agent (Verifier) simultaneously writes the test suite from Spec §4–§5.

**Why this works:**
- The Implementor is inherently optimistic about its own output
- The adversarial Verifier creates a significantly cleaner quality signal
- Both agents work from an identical, unambiguous baseline derived from the PRD

**What the Verifier catches:**
- Deviations from UX Figma MCP guidelines
- Unstructured logic that violates rigid EARS requirements
- Unauthorized segment access
- Domain contract violations
- Any condition that fails the localized test suite

When the Verifier detects a conflict, it **immediately fails the localized test suite and blocks the branch from merging**.

Throughout parallel execution, sub-agents continuously update the living specification in real-time, ensuring the Coordinator agent and human PM maintain a mathematically verified picture of project state.

***

## Discovery Workbench and Business User Interface 

Business stakeholders lack Git/Markdown literacy but possess strategic market intelligence critical to the PRD. The Discovery Workbench solves this tension.

### The "Fireman" Pattern 

The business stakeholder ("The Fireman") inputs plain-text intent into guided forms in the Discovery Workbench — a Git-less front door. The Discovery Agent parses the input; if overly brief, it queries the Shared Memory MCP (Layer 2) to infer missing context, **flagging all inferred sections for human verification** before they are treated as authoritative.

### Discovery Agent Evaluation (S41) 

The Discovery Agent (S41) evaluates the Before-SPEC Gate programmatically; a human reviewer verifies the judgment. The agent:

- Parses incoming PRD submissions
- Checks solution-prescription compliance
- Evaluates Nine Practices alignment
- Queries Layer 2 for context enrichment
- Generates the Spec Seed manifest on PASS
- Writes the immutable Chain of Custody record on approval

***

## Nine Practices Validation 

The Discovery Agent evaluates every submission against the **Nine Practices** of product management — derived from Total Quality Management and BPO excellence standards.

**Core rule:** Requirements must focus on business value rather than prescriptive implementation.

If a stakeholder dictates a specific UI solution (e.g., "The button must be blue and placed in the top-left corner"), the agent:

1. Flags a **Nine Practices violation**
2. **Halts spec generation**
3. Coaches the user to reframe as a JTBD outcome

This is mechanically enforced by the Solution-Prescription Filter, which captures the original request and produces a JTBD-compliant restatement in the PRD §1 filter log.

***

## Tier 4 QMS Compliance and Chain of Custody 

This section documents the regulatory compliance architecture — primarily unique to the Gemini source but referenced in all compliance-sensitive contexts.

### Compliance Targets

- FINRA Rule 4511 (7-year record retention)
- Sarbanes-Oxley
- EU AI Act

### Chain of Custody Record 

When a stakeholder clicks **Approve**, the system:

1. Merges the PR
2. Updates TIMC
3. Writes an **immutable Chain of Custody record** to the enterprise audit log

The record **cryptographically ties** the user's ID and timestamp to the exact Git commit hash of the generated spec, enforcing 7-year retention.

### Human-in-the-Loop (HITL) Gate 

For compliance-critical domains (e.g., FINRA-regulated features):

- Automated approval is **disabled**
- A **HITL prompt** requires cryptographic sign-off from a licensed individual (e.g., Series 7/21 compliance officer)
- The Developer agent cannot access the file until HITL is complete
- The compliance constraint type is explicitly referenced in PRD §4.3 table

***

## Quality Gates Summary 

| Gate | Where | What It Checks | Enforced By | Source |
|------|-------|----------------|-------------|--------|
| **Before-SPEC Gate** | PRD §11 | Problem framing, stakeholder alignment, risk matrix, open questions | Discovery Agent + Human reviewer | All |
| **PRD Lint** | Pre-gate | Solution bias, missing evidence, missing metrics, unbounded scope, weak job stories | PRD Lint agent | ChatGPT |
| **Nine Practices Gate** | Discovery Workbench | Requirements focused on business value, not prescriptive implementation | Discovery Agent | Gemini |
| **Spec Taxonomy Gate** | Spec frontmatter + §10 | Spec Type, Delivery Surface, Handoffs | `validate-spec-taxonomy.mjs` | Perplexity |
| **EARS Coverage Gate** | Spec §3 | All functional requirements in EARS notation | TIMC Light signal | All |
| **BDD Gate** | Spec §4 | Gherkin syntax valid, min 2 rules × 3 examples | `gherkin-lint` | All |
| **Acceptance Gate** | Spec §8 | All AC binary and testable; outcomes traceable to PRD §3 | PR review | All |
| **Definition of Done Gate 5** | Spec §10 | Delivery surface reachable per Spec Type rules | Taxonomy validator + PR review | Gemini, Perplexity |
| **Chain of Custody Record** | Approval step | Cryptographic tie of approver ID + timestamp to Git commit hash | TIMC + audit log | Gemini |

***

## Naming Conventions and File System Layout 

```
docs/
  prd/
    PRD-01-discovery-workbench-intent.md        ← PRD files (PRD-## independent of S##)
    PRD-02-dora-release-readiness.md
  specs/
    S41-discovery-workbench-agentic-forms.md    ← Spec files (existing CCQG convention)
    S42-test-execution-engine.md
    S73-prd-to-spec-bridge-and-readiness-gate.md
    S74-discovery-workbench-prd-authoring-ui.md
    S75-discovery-bench-agent-skills.md
.claude/
  skills/
    roundhouse-prd/
    roundhouse-spec-seed/
    ccqg-spec-auditor/
    discovery-bench/
```

### Naming Rules

- **Spec names:** `S##-kebab-case-focus-area-title.md` — describes *what* is delivered, never *how*
- **PRD names:** `PRD-##-kebab-case-title.md` — problem-framed, not solution-framed
- A PRD may seed one or multiple specs. A spec always traces to exactly one PRD.
- Valid example: `S29-business-slos-observability-thresholds` ✅
- Invalid example: `S29-improve-observability` ❌

***

## Candidate Segment Spec Framing: S73 / S74 / S75 

The UI, PRD template, Spec Seed contract, and Discovery Bench agent behavior should not be bundled into one large spec. The recommended split:

| Segment | Type | Purpose |
|---|---|---|
| **S73-prd-to-spec-bridge-and-readiness-gate.md** | `enabling` | Defines PRD template, Spec Seed template, validation rules, and promotion policy |
| **S74-discovery-workbench-prd-authoring-ui.md** | `stream-aligned` | Builds the Roundhouse UI for creating, reviewing, approving, and promoting PRDs |
| **S75-discovery-bench-agent-skills.md** | `platform` or `enabling` | Defines the agent/skill set: PRD creator, PRD validator, Spec Seed generator, Spec Auditor |

```
S73 defines the method.
S74 makes it usable.
S75 makes it agentic.
```

### Candidate S73 Objective 

```markdown
## 1. Objective

**Job Story:** *When I have validated discovery evidence that may become agentic
implementation work, I want a controlled bridge from PRD to formal spec, so I can
preserve discovery context without allowing an agent to invent requirements or
prematurely code a solution.*

This segment delivers the PRD-to-Spec Bridge method, the Discovery PRD template,
the Spec Seed template, the PRD lint checklist, and the Before-SPEC Readiness Gate.

It closes the gap between discovery artifacts and CCQG segment specifications
by creating a governed promotion path from product discovery to formal,
agent-executable requirements.

**Dependencies:** S35 (TIMC Light MVP), S39 (BDD Scenario Generator Skill),
S40 (Test Plan Composer Skill), S70 (Fleet Audit Intelligence),
S71 (Spec Taxonomy & Delivery Surface)
**Estimated Effort:** 1 sprint
**PR Strategy:** Spec PR → 1 implementation PR
```

***

## Operating Policies 

### PRD Policies

- A PRD may contain hypotheses, but they must be labeled.
- Raw evidence and agent synthesis must be distinguishable.
- Customer interviews must be cited by evidence ID or repository path.
- Business metrics must state baseline, target, and measurement method where known.
- Solution ideas must be separated from requirements.
- PRDs must not contain implementation-only instructions unless framed as constraints.
- Non-goals and "DO NOT CHANGE" boundaries must be stated positively — AI cannot infer scope from omission.
- Discovery must precede drafting — no PRD section is "Validated" until backed by a discovery artifact or an explicit, logged assumption.

### Spec Seed Policies

- A Spec Seed must not invent missing PRD context.
- A Spec Seed must carry forward only approved or explicitly marked assumptions.
- A Spec Seed must identify gaps that block spec generation.
- A Spec Seed must include candidate Example Map rules.
- A Spec Seed must include NFR candidates or state why none apply.

### Segment Spec Policies

- The first element of Section 1 must be a Job Story.
- Functional requirements must use EARS notation.
- BDD scenarios must use valid Gherkin.
- Acceptance criteria must be binary and testable.
- Delivery surfaces and integration handoffs must be explicit.
- The spec remains the authoritative governance artifact after implementation.
- This spec must not reach `Approved` status unless the linked PRD is in `Spec-Seeded` status.

***

## Governance Decision Rules 

| Situation | Required Action |
|---|---|
| PRD has no named customer or segment | Return to discovery |
| PRD has solution language but no problem statement | Run solution-bias correction |
| Job Story includes technology names | Rewrite Job Story before promotion |
| Business metric is missing | Mark CONCERNS unless metric is not applicable |
| Customer evidence is missing | Mark CONCERNS or FAIL depending on risk |
| NFR candidates are missing | Block Spec Seed if system behavior is impacted |
| Spec Seed requires invented context | Stop and ask clarification questions |
| Spec lacks delivery surface | Block spec approval |
| Agent wants to implement from PRD directly | Reject and require Spec Seed + formal spec |
| Stakeholder dictates a specific UI solution | Flag Nine Practices violation; halt spec generation; coach JTBD reframe |
| Compliance-critical domain | Disable automated approval; require HITL cryptographic sign-off |

***

## Scale-Adaptive PRD Levels 

BMAD v6's scale-adaptive routing mechanism determines how much PRD investment is required before moving to spec:

| Level | Track | Description | PRD Required? |
|---|---|---|---|
| **0–1** | Quick Flow | Bug fixes, simple features | No full PRD — lightweight intent note → spec; generates 1–2 stories max. Target: 2 hours from request to production |
| **2–3** | BMad Method | Standard feature development | Full PRD + architecture + formal quality gates |
| **4** | Enterprise | 40+ stories; major product changes | Full PRD + architecture + multiple spec segments + formal quality gates |

`workflow-init` detects the level and routes automatically. The discovery-before-drafting discipline still applies at all levels; Level 0–1 work uses a compressed intent-capture form rather than a full PRD.

***

## Brownfield vs. Greenfield PRD Mode 

| Mode | Discovery Path | PRD Approach |
|---|---|---|
| **Greenfield** | Clean Brief → PRD → Architecture → dev | Standard PRD flow |
| **Brownfield** | `document-project` → `project-context.md` → Brownfield PRD | Document the existing system first so agents follow existing patterns; run brownfield PRD/epic/story; add Test Architect (TEA) role for regression risk |

**Brownfield rule:** A brownfield PRD must include a reference to `project-context.md` in its Source Artifacts frontmatter field. No brownfield spec may be generated without a current `project-context.md` in the repository.

***

## Implementation Roadmap 

The recommended sequence for implementing this bridge in a live codebase:

1. **Author S73** — define the method (PRD template, Spec Seed template, validation rules, promotion policy) as an enabling spec
2. **Author S74** — build the Roundhouse UI for creating, reviewing, approving, and promoting PRDs (stream-aligned spec)
3. **Author S75** — define the agent/skill set: PRD creator, PRD validator, Spec Seed generator, Spec Auditor (platform spec)
4. **Instrument PRD Lint** — automate checks for solution bias, missing evidence, missing metrics, weak job stories
5. **Wire the Before-SPEC Gate** to TIMC Light signals on all PRs
6. **Deploy the LLM Wiki** — seed Layer 1, establish Layer 2 synthesis agents, configure Layer 3 constitutional schema
7. **Instrument Chain of Custody** — cryptographic commit-hash binding for compliance-critical domains
8. **Run the first brownfield PRD** against an existing segment to validate the bridge end-to-end

***

*Document synthesized from: Agentic-PRD-Spec-Bridge-chatgpt.md, Agentic-PRD-Spec-Bridge-Gemini-3.md, Agentic-PRD-Spec-Bridge-perplexity-4.md, Agentic-PRD-Spec-Bridge-Claude-2.md, and Canonical-Outline-Agentic-PRD-to-Spec-Bridge-5.md.*