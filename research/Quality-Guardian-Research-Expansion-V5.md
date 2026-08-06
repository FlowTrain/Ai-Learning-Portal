# QUALITY GUARDIAN & The Train Yard Fleet
## Total Quality Management Across the Full Product Lifecycle

*Structure → Quality → Ship → Certify*
*From Clean Code Agent to Enterprise Quality Platform*

**James Gifford**
FlowTrain HQ
April 2026 | **Version 5.0**

---

## Table of Contents

1. Executive Summary
2. Section 1: The Quality Guardian Vision
3. Section 2: TQM as the Foundation
4. Section 3: Product Discovery Integration
5. Section 4: The Expanded Agent Architecture
6. Section 5: Multi-Modal Agent Orchestration
7. Section 6: Spec-Based Development with Agentic Coding
8. Section 7: Skill Bundles, Shared Memory, and Learning Loops
9. Section 8: Design System Strategy
10. Section 9: Skills Roadmap
11. Section 10: Recommended Technology Stack
12. Section 11: Implementation Roadmap
13. Section 12: Strategic Positioning
14. Section 13: The Train Yard — Fleet Architecture
15. Appendix A: Full Mapping Matrix
16. Appendix B: shadcn/ui Token Mapping
17. Appendix C: Architecture & Technology Glossary
18. Appendix D: Source Document Reference

---

## Executive Summary

The Quality Guardian began as the Clean Code Quality Guardian (CCQG) — an AI-powered agent designed to enforce engineering standards and eliminate legacy-code patterns across financial trading systems. Its value proposition was clear: stop generating technical debt at the source. But the ambition was always larger than code.

This document charts the evolution from a code-level quality agent into a full-lifecycle quality platform spanning Product Discovery, Development, Testing, Deployment, Operations, and Continuous Improvement. The strategic foundation rests on three pillars: Total Quality Management (TQM) principles, Product Discovery methodologies, and Engineering Excellence practices.

The TIMC (Testing Information & Management Centre) UI realignment — completed in March 2026 — was the first tangible proof of this vision. The TIMC was transformed from developer scaffolding into a business-visible Quality Hub with stakeholder-facing navigation, regulatory compliance cards, stage-gate release progression, and a domain configuration wizard. This realignment demonstrated that quality tooling can and should serve the entire organisation, not just engineers.

**The financial imperative is stark.** In organisations spending $780 million across 260 development teams, 35% ($273 million) goes to technical debt, production support, and defect remediation — an average of $3 million per team. Breaking that down for a single $3M team: planning dysfunction waste accounts for approximately $1.65M/year (60% plan failure rate), while quality and defect remediation accounts for approximately $1.05M/year (35% TQM benchmark). Total identifiable waste: ~$2.7M/year — nearly equal to the team's entire annual cost. The Quality Guardian's mission is to drastically reduce this waste by embedding quality at every stage of the product lifecycle.

Version 5.0 of this research expansion integrates and fully incorporates the following bodies of work:

- **CCQG Expansion Paper** (Multi-Modal Agent Orchestration, Skill Bundles, Shared Memory, Learning Loops)
- **Spec-Based Development with JTBD** (Job Stories, 6-Step Translation Pipeline, EARS Notation, Spec Packages, Living Specs)
- **Train Yard Fleet Briefs** (StructureView, StructureView Lite, Q2 Release, Tier 4, Turntable Hub)
- **Time-Dimensional Testing** (S29–S31 specs for SLO observability, synthetic monitoring, AI model governance)

Together these form the complete intellectual foundation for the Quality Guardian's next phase. A key insight from the Time-Dimensional Testing work: there will be a need for greater configurability in the UI, especially since product metrics often change and depend on the dance between the problem and solution spaces. This configurability requirement shapes the design system strategy and the dashboard architecture described in later sections.

> **Note on agent count:** The CCQG Expansion Paper describes "seven cross-functional role bundles." Section 4 of this document defines eight new agents, which supersedes the earlier framing. The eight-agent mesh is the current target architecture.

---

## Section 1: The Quality Guardian Vision

### Mission

The Quality Guardian exists to be the antonym of legacy-code generators AND legacy product processes. Where traditional organisations accumulate technical debt through rushing, cutting corners, and disconnecting quality from business outcomes, the Quality Guardian embeds quality as a first-class concern across every stage of the product lifecycle.

### From CCQG to Quality Guardian

The Clean Code Quality Guardian (CCQG) was the genesis — a multi-agent AI system focused on enforcing coding standards, running automated quality gates, and managing domain-specific testing requirements for financial trading platforms. Its architecture on Azure (Function App, Static Web App, Cosmos DB) proved the viability of AI-powered quality enforcement.

> *"You can't ship a PR unless they all pass. I even jam you up if you've got lint in your pocket."*

The current CCQG enforces a minimum of 3 gates (simple changes) up to 15 gates (full quality push). Every PR is blocked until gates pass. This is not advisory — it is enforcement.

The evolution to "Quality Guardian" represents a deliberate expansion of scope:

- **CCQG (Code-Focused):** Static analysis, unit test enforcement, code review quality gates, clean code patterns
- **Quality Guardian (Full Lifecycle):** Product Discovery validation, development quality, testing orchestration, release readiness, operational monitoring, continuous improvement feedback loops

### The Three Pillars

**1. Total Quality Management (TQM) — The philosophical and strategic foundation.**
TQM's 8 principles provide the framework for quality across all organisational activities, from customer focus to continuous improvement.

**2. Product Discovery — The upstream extension.**
Product Discovery methodologies (risk management, continuous discovery, opportunity solution trees) ensure quality begins before a single line of code is written.

**3. Engineering Excellence — The execution layer.**
Clean code practices, BDD, shift-left testing, CI/CD quality gates, and DORA metrics ensure quality is maintained through development and into production.

### Bring Your Own AI

Quality Guardian has an abstraction layer on top of AI providers. It is bring-your-own-AI by design. When a pharma company or financial services organisation sees "you can point this at your own Azure OpenAI endpoint" — procurement friction drops significantly. The architecture targets the system prompt / SKILL.md abstraction layer, making it provider-agnostic across Anthropic, OpenAI, Google, and self-hosted models.

### The TIMC Realignment as Proof of Concept

The TIMC UI realignment (completed March 2026) serves as the foundational proof that Quality Guardian's vision is executable. The realignment delivered five major changes:

- Navigation Restructure: From developer-centric labels to business-facing language (e.g., "Auditable Artifacts" → "Compliance & Traceability")
- Test Plan Enhancement: Quadrant health bars, regulatory tag filtering, domain-specific test case browser with Gherkin details
- Domain Configuration Wizard: A 5-step guided form enabling non-engineers to register and configure domain agents
- Product Lifecycle & Release Gates: Visual stage-gate progression (Alpha → Closed Beta → Open Beta → GA) with rollback trigger monitoring
- Compliance & Traceability View: Six regulatory compliance status cards (SEC 17a-4, SEC 613/CAT, IRC §1091, WCAG 2.2 AA, Reg S-P, OWASP ASVS)

All P0 and P1 bug fixes were resolved. 40+ integration tests were added. TIMC moved from being an internal developer tool to a stakeholder-visible quality hub.

### Platform Upgrade Path

The upgrade path between products follows this sequence:

```
StructureView Lite (TIMC Light signal)
    ↓  upgrade trigger fires
Quality Guardian Team
    ↓  quality data feeds release readiness
Q2 Release
    ↓  compliance mode activates
Tier 4 Compliance
```

---

## Section 2: TQM as the Foundation

Total Quality Management provides the strategic backbone for the Quality Guardian platform. Each of TQM's 8 principles maps directly to specific platform capabilities and specialised agents.

| TQM Principle | Quality Guardian Capability | Agent/Skill Needed |
|---|---|---|
| Customer Focus | Product Discovery agent, customer insights dashboard, desirability risk validation | Discovery Agent |
| Total Employee Involvement | Cross-functional quality scorecards, shared quality ownership metrics, collaborative BDD workshops | Collaboration Agent |
| Process-Centered | CI/CD quality gates, workflow automation, shift-left testing integration, pipeline orchestration | Pipeline Agent |
| Integrated System | Unified metrics dashboard, traceability matrix (requirements → tests → results → compliance), 4-quadrant test management | TIMC Core |
| Strategic & Systematic Approach | Release readiness gates, DORA metrics tracking, stage-gate progression (Alpha → GA) | Release Agent |
| Continuous Improvement | Learning events, trend analysis, AI-driven recommendations, anomaly detection, retrospective insights | Learning Agent |
| Fact-Based Decision Making | Metrics dashboard, data-driven quality assessments, coverage analytics, defect trend visualisation | Analytics Agent |
| Communication | Living documentation generation, stakeholder reports, compliance artifacts, audit-ready evidence packages | Documentation Agent |

### The Financial Case for Quality

| Metric | Value | Implication |
|---|---|---|
| Total Annual Technology Budget | $780 Million | Significant organisational investment in technology capability |
| Amount Spent on Technical Debt, Production Support & Defect Remediation | $273 Million (35%) | Over one-third of the budget consumed by non-value-adding activities |
| Number of Development Teams | 260 teams | Scale demands systematic, automated quality enforcement |
| Average Cost Per Team | $3 Million | Each team's debt burden is quantifiable and addressable |
| Planning Dysfunction Waste (per team) | ~$1.65M/year | 60% plan failure rate — the largest single waste category |
| Quality/Defect Remediation (per team) | ~$1.05M/year | 35% TQM benchmark applied to team cost |
| Total Identifiable Waste (per team) | ~$2.7M/year | Nearly equal to the team's entire annual cost |
| Opportunity Cost | $273M redirectable to innovation | Quality improvement directly funds competitive advantage |

The Quality Guardian platform targets this $273M expenditure by embedding quality at the source — preventing defects rather than remediating them, automating compliance rather than auditing after the fact, and providing continuous feedback rather than end-of-cycle discoveries.

### Competitive Pricing Context

Quality Guardian competes in the DevOps/infrastructure tools category, where median ARPU is **$847/month** (the highest category in SaaS). Direct comparisons:

- **SonarQube Enterprise:** $15,000–$500,000/year for comparable organisations
- **GitHub Copilot Enterprise:** $39/user/month for a subset of what Quality Guardian delivers

The right pricing conversation is not per-seat — it is fraction-of-waste-recovered. At 35% quality waste on a $3M team ($1.05M recoverable), a platform fee of 10–15% of recovery yields $105k–$157k/year per team. At 85 teams (Jira 20k-seat reference), that is **$9M–$13M ARR from a single enterprise relationship**.

*[PLACEHOLDER: Formal pricing tiers and numbers — pending closed beta data to anchor recovery percentages]*

### TQM Across the Product Management Lifecycle

| Lifecycle Stage | TQM Principles Applied | Quality Guardian Automation |
|---|---|---|
| Idea Generation & Concept Development | Customer Focus, Continuous Improvement | Discovery Agent surfaces customer pain points; AI generates opportunity trees |
| Market Analysis & Strategy | Data-Driven Decision Making, Process-Centered | Analytics Agent provides market signal dashboards; automated competitive scanning |
| Product Design & Development | Quality Design, Employee Involvement | Quality at Source Agent enforces TDD/BDD; UX Quality Agent runs accessibility audits |
| Testing & Validation | Continuous Improvement, Fact-Based Decisions | TIMC Core orchestrates 4-quadrant test execution; automated coverage analysis |
| Production / Implementation | Process-Centered, Employee Involvement | Pipeline Agent manages CI/CD quality gates; automated deployment validation |
| Launch & Market Introduction | Customer Focus, Integrated System | Release Agent evaluates stage gates; DORA metrics track deployment frequency |
| Monitoring & Feedback | Continuous Improvement, Fact-Based Decisions | Continuous Improvement Agent detects anomalies; customer feedback integration |
| Iteration / Discontinuation | Strategic Approach, Continuous Improvement | Documentation Agent generates lifecycle reports; trend analysis informs pivot decisions |

---

## Section 3: Product Discovery Integration

Product Discovery represents the upstream extension of the Quality Guardian — ensuring that quality begins before development starts.

### The Four Risks as Automated Quality Checkpoints

Silicon Valley product teams identify four fundamental risks during discovery. These four risk areas are particularly valued by risk professionals in regulated industries and form the backbone of the Quality Guardian's discovery validation system.

| Risk | Definition | Quality Guardian Checkpoint | Automation |
|---|---|---|---|
| Desirability Risk | Will customers find it attractive and worth using? | Customer signal validation gate | Discovery Agent analyses feedback sentiment, market signals, and survey data to generate a desirability score |
| Viability Risk | Can it be profitable and sustainable? | Business model validation gate | Analytics Agent runs cost-benefit models and revenue projections against market sizing data |
| Feasibility Risk | Can we build it with current capabilities? | Technical feasibility assessment | Quality at Source Agent evaluates tech stack compatibility, team capacity, and architectural constraints |
| Usability Risk | Will users find it easy to use? | UX quality gate | UX Quality Agent runs automated accessibility audits, heuristic evaluations, and design system compliance checks |

Each risk checkpoint generates artifacts that feed into the traceability matrix, linking discovery decisions to downstream test coverage and compliance evidence.

### Continuous Discovery Loops Fed by Quality Metrics

The Quality Guardian feeds the continuous discovery loop established by Teresa Torres:

- Quality metrics from production (defect trends, performance degradation, user drop-off points) become inputs to the next discovery cycle
- Automated anomaly detection triggers discovery investigations when quality signals deviate from baselines
- Customer satisfaction correlations link quality metrics to business outcomes, informing prioritisation

### Jobs-to-be-Done as the Discovery Front Door

Jobs-to-be-Done (JTBD) theory, pioneered by Clayton Christensen and Anthony Ulwick, posits that people do not buy products — they hire products to accomplish a job in their lives. Outcome-Driven Innovation (ODI) operationalises JTBD theory into a measurable process, reporting an **86% success rate** in product innovation — more than five times the industry average of approximately 17%.

For the Quality Guardian, JTBD integration means:

- Discovery Agent can process raw transcripts of customer discovery calls and automatically output validated Job Stories from unstructured data
- Job Stories replace traditional user stories as the front door for specification creation, grounding every feature in documented customer motivation
- The situation clause in Job Stories captures the precise context and trigger conditions that determine which solution will work

### Job Stories as the Bridge to Specifications

Alan Klement's Job Story format: *"**When [situation/context], I want to [motivation], so I can [expected outcome]**"*

| Dimension | User Story | Job Story |
|---|---|---|
| Format | As a [role], I want [feature] so that [benefit] | When [situation], I want to [motivation], so I can [outcome] |
| Focus | Product feature | Customer progress |
| Implementation Bias | High — often implies solution | Low — deliberately withholds solution |
| Contextual Richness | Low | High — situation includes multiple contextual layers |
| AI Suitability | Poor (too vague for machine reasoning) | Moderate (richer context, requires spec elaboration) |

A critical clarification: Job Stories are not yet specifications — they are high-quality starting points for specification creation.

### Opportunity Solution Trees Driven by Defect/Trend Data

The Quality Guardian enhances the Opportunity Solution Tree (OST) by:

- Auto-populating opportunity branches from production defect clusters and support ticket analysis
- Scoring solution candidates against feasibility data from the codebase analysis
- Tracking experiment outcomes and linking them back to quality metrics for closed-loop learning

### BDD as the Bridge Between Discovery and Development

Behaviour-Driven Development serves as the critical translation layer between Product Discovery artifacts and development deliverables:

- Discovery outputs (Job Stories, acceptance criteria) translate to Gherkin scenarios (Given/When/Then)
- Gherkin scenarios become automated test scripts that validate expected behaviours
- BDD scenarios serve as living documentation that stays synchronised with the codebase
- The BDD Scenario Generator skill automates the translation from Job Stories to Gherkin format

### Zero-Based Design for Quality Process Reimagination

Applied to the Quality Guardian itself, Zero-Based Design drives:

- Reimagining quality processes from first principles rather than automating broken workflows
- Questioning every existing quality gate: does it prevent defects or just create friction?
- Designing the Quality Guardian UX without assuming that quality dashboards must look like traditional testing tools

### Human-Centered Design Applied to Quality Guardian UX

HCD principles apply directly to the Quality Guardian's own design:

- **Empathise** with all stakeholders: developers want fast feedback, PMs want visibility, compliance officers want evidence
- **Define** quality personas: the developer, the test lead, the product manager, the compliance officer, the executive
- **Design** Quality Guardian interfaces that serve each persona's specific needs and mental models

### UI Configurability for Product Metrics

A key insight from the Time-Dimensional Testing work: product metrics often change and depend on the dance between the problem and solution spaces. This creates a fundamental requirement for greater UI configurability — metrics displays, thresholds, and visualisations must be easily reconfigurable as teams iterate through discovery cycles **without requiring engineering changes**.

### When Discovery Is NOT Needed — The Pragmatic Filter

Full discovery is unnecessary for:

- Obvious problems with clear solutions (e.g., a missing button preventing task completion)
- Low-risk situations (minor design tweaks, repositioning a menu item)
- Keep-the-lights-on activities (bug fixes, infrastructure upgrades)
- Backlog refinement scenarios where the problem is validated and the solution is decided

The Quality Guardian incorporates this pragmatism by classifying incoming work and recommending appropriate levels of discovery effort.

---

## Section 4: The Expanded Agent Architecture

> **Agent count clarification:** This section defines eight new agents. This supersedes the "seven bundles" language used in the CCQG Expansion Paper, which reflected an earlier architectural framing. The eight-agent mesh is the current target.

### Existing Agents (CCQG Core)

The current CCQG architecture provides the foundation:

- **Clean Code Quality Guardian (Orchestrator):** The central coordination agent managing quality workflows across all sub-agents
- **Domain Sub-Agents:** Specialised agents with cognitive architectures for specific domains (e.g., financial trading expert with 6 capabilities, 4 frameworks, 2 regulatory calendars)
- **Coordination Agent:** Manages inter-agent communication, task routing, and conflict resolution

### New Agents Needed

#### 1. Product Discovery Agent

**Mission: Analyse customer feedback, map opportunity trees, and generate BDD scenarios from Job Stories to ensure quality begins at the point of product conception.**

**Key Capabilities:**
- Customer feedback sentiment analysis and trend detection across support tickets, surveys, and usage data
- Automated Opportunity Solution Tree generation from defect clusters and customer pain points
- BDD scenario generation from Job Stories and acceptance criteria using Gherkin format
- Desirability and viability risk scoring for new feature proposals
- Continuous discovery loop integration — feeding production quality signals back into discovery

**Data Sources:** Customer support ticket databases, user survey responses and NPS data, product analytics (usage patterns, drop-off points), market research and competitive intelligence feeds

**Outputs:** Opportunity Solution Trees with quality-signal annotations, risk assessment scorecards (desirability, viability, feasibility, usability), generated BDD scenarios in Gherkin format, discovery-to-delivery artifact packages

**Integration Points:** Quality at Source Agent (handoff of BDD scenarios), Analytics Agent (quality metrics as discovery inputs), TIMC Core (traceability from discovery to test coverage)

#### 2. Quality at Source Agent

**Mission: Enforce shift-left quality practices by embedding automated quality checks at every stage of the development process, from code commit to deployment.**

**Key Capabilities:**
- Shift-left testing recommendations based on code change analysis and risk profiling
- Code review quality gate enforcement with automated pattern detection
- TDD coaching — identifies untested code paths and suggests test strategies
- Static analysis orchestration and finding prioritisation
- Integration test gap analysis across system boundaries

**Data Sources:** Git repositories (commit history, PR data, code coverage reports), CI/CD pipeline telemetry, static analysis tool outputs (ESLint, SonarQube, etc.), code review platform data

**Outputs:** Quality gate pass/fail decisions with evidence, test coverage gap reports with prioritised recommendations, developer coaching notifications, code quality trend reports

**Integration Points:** Pipeline Agent (CI/CD integration), TIMC Core (test coverage data for traceability matrix), Release Agent (quality gate status for release decisions)

#### 3. TQM Compliance Agent

**Mission: Map TQM principles to team practices, identify gaps in quality management adoption, and generate actionable improvement plans aligned with organisational quality standards.**

**Key Capabilities:**
- TQM principle adherence assessment across teams and projects
- Gap analysis between current practices and TQM best practices
- Improvement plan generation with prioritised recommendations and timelines
- Quality culture metrics tracking (employee involvement, feedback loop effectiveness)

**Outputs:** TQM compliance scorecards per team and project, improvement plans with specific actions and owners, quality culture assessment reports, benchmarking comparisons across teams

**Integration Points:** Analytics Agent (quality metrics data), Documentation Agent (compliance documentation generation), Continuous Improvement Agent (improvement plan tracking)

#### 4. UX Quality Agent

**Mission: Ensure every user interface meets accessibility standards, design system compliance, and usability heuristics through automated auditing and continuous monitoring.**

**Key Capabilities:**
- Accessibility auditing (WCAG 2.2 AA compliance, colour contrast, keyboard navigation, screen reader compatibility)
- Design system compliance validation against FlowTrain component library
- Usability heuristic evaluation based on Nielsen's 10 usability heuristics
- Cross-browser and responsive design validation
- Accessibility regression detection in CI/CD pipelines

**Data Sources:** Rendered UI snapshots and DOM analysis, design system token definitions and component registry, user session recordings and heatmap data, accessibility tool outputs (axe-core, Lighthouse)

**Outputs:** Accessibility audit reports with WCAG compliance scores, design system violation reports with remediation guidance, usability heuristic scorecards, UI regression alerts

**Integration Points:** Quality at Source Agent (accessibility checks in CI/CD), Documentation Agent (accessibility compliance evidence), TIMC Core (Q4 non-functional test results)

#### 5. Omnichannel Quality Agent

**Mission: Ensure consistent quality and experience parity across all customer touchpoints — web, mobile, chat, IVR, and call centre channels.**

**Key Capabilities:**
- Cross-channel experience consistency checks (brand messaging, service levels, interaction patterns)
- IVR/web/mobile experience parity validation
- Channel-specific quality metrics aggregation and comparison
- Customer journey continuity validation across channel transitions
- Digital containment and deflection effectiveness tracking

**Outputs:** Cross-channel consistency reports, channel-specific quality scorecards, journey continuity gap analysis, digital containment effectiveness reports

**Integration Points:** Discovery Agent (customer journey insights), Analytics Agent (unified metrics), Documentation Agent (omnichannel quality reports)

#### 6. Release Readiness Agent

**Mission: Evaluate stage-gate criteria, track DORA metrics, and monitor rollback triggers to ensure every release meets quality thresholds before reaching customers.**

**Key Capabilities:**
- Stage-gate evaluation (Alpha → Closed Beta → Open Beta → GA) with configurable criteria
- DORA metrics tracking: deployment frequency, lead time for changes, change failure rate, mean time to restore
- Rollback trigger monitoring (error rate thresholds, settlement failure rates, latency degradation)
- Release evidence package compilation for audit and compliance
- Deployment risk scoring based on change scope, test coverage, and historical patterns

**Outputs:** Release readiness scorecards with go/no-go recommendations, DORA metrics dashboards and trend reports, rollback trigger alerts with severity classification, release evidence packages for compliance auditing

**Integration Points:** Quality at Source Agent, TIMC Core (test execution results), Continuous Improvement Agent (post-release learning events), Documentation Agent

#### 7. Continuous Improvement Agent

**Mission: Detect quality trends, identify anomalies, and generate AI-driven improvement recommendations that evolve the organisation's quality practices over time.**

**Key Capabilities:**
- Quality trend analysis across all metrics (defect rates, test coverage, build success rates, deployment frequency)
- Anomaly detection using statistical models to identify emerging quality issues before they escalate
- AI-driven improvement recommendations based on pattern analysis across teams and projects
- Learning event generation from production incidents, linking root causes to preventive actions
- Retrospective insight aggregation across teams to identify systemic improvement opportunities

**Outputs:** Improvement recommendation reports with expected impact scoring, anomaly detection alerts with context and suggested investigations, quality trend dashboards with predictive indicators, learning event summaries

**Integration Points:** TQM Compliance Agent (improvement plan input), Analytics Agent (data feeds), all agents (improvement recommendations distributed across the ecosystem)

#### 8. Documentation Agent

**Mission: Generate living documentation, compliance artifacts, and stakeholder reports that stay synchronised with the codebase and quality state of the system.**

**Key Capabilities:**
- Living documentation generation from code, tests, and BDD scenarios that auto-updates with each deployment
- Compliance artifact production (audit evidence, regulatory documentation, traceability matrices)
- Stakeholder reporting (executive dashboards, team quality summaries, release readiness reports)
- API documentation validation against actual implementation
- Knowledge base maintenance and quality playbook generation

**Outputs:** Living documentation packages (auto-updated HTML/PDF), compliance evidence bundles (per regulation), executive quality summary reports, quality playbooks and best practice guides

**Integration Points:** All agents (documentation generated from their outputs), TIMC Core (traceability matrix data), Release Agent (release documentation packages)
---

## Section 5: Multi-Modal Agent Orchestration

*Source: CCQG Expansion Paper — Multi-Modal Agent Orchestration, Skill Bundles, Shared Memory, and Self-Improving Learning Loops (March 2026)*

### The Paradigm Shift to Agent Mesh

The CCQG v2.0 specification established a single-agent architecture: an autonomous AI coding agent governed by Clean Code principles, TDD, SOLID, the Agile Testing Quadrants, and CI/CD quality gates. That foundation is sound and immutable. The expansion moves from a single guardian agent to a coordinated agent mesh that covers the full cross-functional product team — UI/UX designers, data analysts, domain architects, knowledge engineers, product managers, and QA leads — all operating under a unified quality management framework.

This architectural philosophy directly aligns with TQM: organisation-wide participation, customer-focused improvement culture, and data-driven decision-making across cross-functional teams. The expansion propagates these principles across every product lifecycle phase: Discovery → Scoping → Build → Test → Deploy → Measure → Learn.

### Three-Tier Model Hierarchy

Enterprise LLM spending hit $8.4 billion in 2025, with most waste attributable to routing simple tasks to expensive frontier models. Intelligent routing delivers **85% cost reduction** while maintaining 95% of frontier model performance.

| Tier | Models | Role | Rationale |
|---|---|---|---|
| Tier 1 — Staff Principal | Claude Opus 4.5 | Architecture reviews, catastrophic bugs, legacy refactoring | >80% SWE-bench score |
| Tier 2 — Daily Workhorses | Claude Sonnet 4.5, Gemini 3.1 Pro | Code-heavy tasks, sustained multi-step tool loops, visual composition | 77.2% SWE-bench; 15–20% faster on visual tasks |
| Tier 3 — Sub-Agents | Gemini 3 Flash, Claude Haiku, Phi-4, Qwen3-1.7B | Fast lookups, simple scaffolding, routing decisions | Qwen2.5-0.5B achieves 91.7% accuracy for classification |

> **Model name update:** The brief previously referenced "Gemini 3 Pro" — this model was shut down March 2026 and replaced by Gemini 3.1 Pro. "Gemini Flash 3.0" is now correctly identified as Gemini 3 Flash (released December 2025). Gemini Flash 2.0 is deprecating with a June 2026 shutdown. All model references in this document use current identifiers.

### Production Model-to-Role Mapping

| Agent Role | Primary Model | Fallback | Rationale |
|---|---|---|---|
| Router / Task Classifier | Phi-4 / Qwen3-1.7B | Claude Haiku | Classification saturates at sub-billion scale |
| Orchestrator / Architect | Claude Opus 4.5 | Claude Sonnet 4.5 | >80% SWE-bench; deep cross-file reasoning |
| Code Generation | Claude Sonnet 4.5 | GPT-4o | 77.2% SWE-bench; most reliable for tool loops |
| UI/UX Composition | Gemini 3.1 Pro | GPT-4o | Native screen understanding; 15–20% faster |
| Data Analytics / SQL | Claude Sonnet | GPT-4o | Strong structured reasoning |
| Fast Summarisation | Gemini 3 Flash | Claude Haiku | Lowest latency |
| QA / Test Generation | Claude Sonnet | — | Systematic coverage thinking |
| UI Component Selection | bge-large-en-v1.5 + Phi-4 | Claude Haiku | Finite ~50–80 component taxonomy |

### Mixture of Agents (MoA) for Quality-Critical Tasks

The Mixture of Agents pattern (ICLR 2025, Together AI) organises multiple LLMs in layers where each agent receives all outputs from the previous layer. Using only open-source models, MoA achieved **65.1% on AlpacaEval 2.0** versus GPT-4 Omni's 57.5%. Heterogeneous models contribute more than copies of the same model.

Reserve MoA for quality-critical tasks only (architecture decisions, complex PRDs, multi-service refactoring). Use single-model routing for latency-sensitive paths.

### The No-Figma UI Pipeline

The Quality Guardian eliminates Figma Make dependency through a two-stage composition pipeline:

- **Stage 1 — Visual Planning:** A vision-capable model (Gemini 3.1 Pro or GPT-4o) outputs a typed composition JSON — a schema-validated structure listing templates and component slots. The LLM cannot hallucinate a component that does not exist in the schema.
- **Stage 2 — Code-Centric Implementation:** The composition JSON is handed to Claude Code with the shadcn/ui MCP server mounted. The agent has live access to the actual component library, producing production-ready React/Tailwind code.

Complete workflow: Designer describes intent → Gemini 3.1 Pro generates typed composition JSON → Schema validated against shadcn component library (Zod) → Claude Code + shadcn MCP generates React/Next.js code → V0 by Vercel for rapid iteration → Deploy.

### OpenClaw Architecture Patterns

The OpenClaw architecture (247,000+ GitHub stars, fastest-growing repo in 2025/26) validates the construction sequence: Sessions → SOUL.md → Tools → Permissions → Compaction → Memory → Multi-agent. Key patterns that translate directly to the Quality Guardian:

- Append-only JSONL session transcripts for crash-safe durability
- Compaction at ~80% context window, replacing old messages with structured summaries
- Semantic snapshots (structured text of UI accessibility trees) for lower-token UI control
- **Heartbeats and scheduled cron tasks** for proactive quality routines — these drive background agent behaviours such as nightly DORA metric aggregation, weekly quality trend reports, and scheduled ExpeL learning batch runs
- Per-session locks with async mutex and atomic writes for concurrent agent safety

---

## Section 6: Spec-Based Development with Agentic Coding

*Source: Spec-Based Development Comprehensive Paper (March 2026)*

### The Central Thesis

In an era where AI can generate code faster than a human can type, code is no longer the scarce resource. The bottleneck has shifted decisively upstream, from the mechanics of implementation to the clarity of intent. Spec-Based Development (SDD) treats specifications as the authoritative source of truth, with AI agents as bounded execution engines rather than autonomous architects.

"Vibe coding" — rapid, conversational AI-assisted development — produces approximately 70% of a functional application almost instantaneously. But the remaining 30% reveals severe structural decay: bug regressions, brittle architecture, credential leakage, and unmaintainable code. The master pipeline — **Job Story → Spec → Tests → Agent Execution** — transforms AI from an unpredictable conversational novelty into a deterministic engineering accelerator.

### Why User Stories Fail for AI Agents

Research identifies at least fourteen limitations of user stories as a specification mechanism. AI agents amplify every one of them. Key failure modes:

- User stories describe work, not the system — they contain no rules, flows, edge cases, or constraints
- User stories depend on invisible tribal knowledge that LLMs do not possess unless made explicit
- A study of 600 rejected pull requests found that alignment loss during execution caused more failures than incorrect task descriptions
- A 2025 randomised controlled trial found AI tools actually slowed experienced developers by 19% — the path to AI as a force multiplier runs through specification quality

### The Six-Step Translation Pipeline

| Step | Action | Output |
|---|---|---|
| 1 — JTBD Research | Conduct switch interviews and outcome interviews | Jobs being hired, customer motivations |
| 2 — Job Story Authoring | Capture situation, motivation, expected outcome with contextual forces and anxieties | Job Stories |
| 3 — Impact Mapping | Decompose the job into actors, impacts, and deliverables | Prioritised opportunity space |
| 4 — Example Mapping | Use concrete examples to elaborate rules and surface ambiguities | Validated rules and edge cases |
| 5 — Formal Specification | Convert validated examples into EARS notation, BDD scenarios, or use case specs | Machine-readable requirements |
| 6 — Living Spec Maintenance | Keep specifications synchronised with implementation | Bidirectionally updated specs |

The complete traceability chain: stakeholder intent → Job Story → Example Map → Gherkin → agentic code. Every line of AI-generated code is traceable back through a verifiable artifact chain to a documented stakeholder need.

### EARS Notation for Machine-Readable Requirements

The Easy Approach to Requirements Syntax (EARS), developed at Rolls-Royce for safety-critical systems and adopted by Amazon Kiro, provides five deterministic sentence patterns:

| Pattern | Template | Example |
|---|---|---|
| Ubiquitous | The [system] shall [action] | The system shall display the user's full name in the navigation bar |
| Event-Driven | When [trigger], the [system] shall [action] | When the user clicks "Save", the system shall persist form data |
| State-Driven | While [state], the [system] shall [action] | While offline, the system shall queue pending write operations locally |
| Unwanted Behavior | If [condition], then the [system] shall [action] | If the connection times out after 30s, the system shall retry three times |
| Optional Feature | Where [feature is enabled], the [system] shall [action] | Where dark mode is enabled, the system shall apply dark colour scheme |

### Spec Packages and Governance

The highest-leverage governance artifact is the spec package — a structured replacement for story-only backlog items. A spec package contains: goals and non-goals, functional requirements, non-functional requirements (security, reliability, performance, observability), acceptance criteria with examples, a verification plan, and a decision log.

Spec review replaces code review as the primary governance mechanism for consequential changes. Rather than catching problems after implementation, spec review catches them before implementation begins — when they are cheapest to fix.

### The Three-Tier Boundary System

| Boundary Tier | Definition | Practical Application |
|---|---|---|
| Always Do | Unconditional actions the agent must execute | Always run linting and unit tests before proposing a Git commit |
| Ask First | High-impact modifications requiring human authorisation | Modifying database schemas; altering CI/CD pipeline configurations |
| Never Do | Absolute prohibitions representing hard stops | Never commit API secrets; never modify production configuration; never bypass failing tests |

### The Four-Phase SDD Workflow

| Phase | Developer Role | AI Output | Validation Question |
|---|---|---|---|
| 1 — Specify | Define business goals, user journeys, success definitions | Structured requirements.md | Are edge cases and business motivations captured? |
| 2 — Plan | Provide tech stack, architectural boundaries | Comprehensive plan.md with architecture decisions | Does the architecture adhere to security and compliance? |
| 3 — Tasks | Review decomposition for logical progression | Granular tasks.md with test-driven chunks | Are tasks small enough for agent context windows? |
| 4 — Implement | Steer, verify, and critique incrementally | Application code and automated tests | Does generated code pass the automated tests? |

### Flow Efficiency Evidence

Flow efficiency is the ratio of active work time to total elapsed time. Traditional agile teams average 15–25% flow efficiency. In one documented case study, replacing user stories with structured engineering specifications increased flow efficiency from **32% to 85%** — improvement coming entirely from collapsing requirement clarification overhead.

### Productivity Evidence

- GitHub Copilot controlled experiment: **55.8% faster** task completion
- Microsoft field study: **12.92–21.83% PR throughput lift** per developer per week
- McKinsey (50+ companies): **30–40% time-to-market reduction** with comprehensive SDD
- Azure internal: A two-week feature delivered in two days using AI-augmented SDD
- Multi-file AI accuracy without structured specifications: only **19.36% vs 87.2%** for single-function tasks — a 4.5× gap attributable entirely to specification quality

---

## Section 7: Skill Bundles, Shared Memory, and Learning Loops

*Source: CCQG Expansion Paper — Parts 2, 3, and 4 (March 2026)*

### The SKILL.md Standard

The transition from rigid system prompts to portable, versionable skill definitions is the foundational shift enabling cross-functional agent teams. Plain-text Markdown artifacts are diff-able, reviewable, version-controlled, and easy to audit. The Agent Skills open standard (adopted by Anthropic/Claude, GitHub Copilot, OpenAI Codex) formalises this: each SKILL.md uses YAML frontmatter for metadata followed by Markdown instructions serving as the agent's system prompt.

#### Three-Layer Context Architecture

- **Layer 1 — AGENTS.md (Always-On):** Injected every turn. Carries non-inferable project specifics. Vercel 2026 evals showed AGENTS.md achieved 100% agent pass rate vs. 79% for skills alone. AGENTS.md must be human-authored. Keep under 8KB.
- **Layer 2 — SOUL.md (Agent Identity):** One per agent role. Injected at session start. Defines personality, behaviour rules, boundaries, role-specific priorities, and escalation paths.
- **Layer 3 — SKILL.md (On-Demand Expertise):** Triggered by semantic match to task. Progressive disclosure: metadata loaded first (~100 tokens), full body on match, reference files on demand. Each file stays under 5,000 tokens.

### The Seven Role Skill Bundles

| Bundle | Model Preference | Key Anti-Pattern | Notable Skill Files |
|---|---|---|---|
| 1. UI/UX Design & Research | Gemini 3.1 Pro | Over-customisation — require enumeration of available components before proposing custom | component-composition.md, ux-research-synthesis.md, jtbd-canvas.md, accessibility-audit.md |
| 2. Data Analytics | Claude Sonnet | Vanity metrics — every metric must reference the specific decision it informs | metric-definition.md, sql-analytics-patterns.md, experiment-design.md, dashboard-requirements.md |
| 3. DDD & Multi-Cloud Architecture | Claude Opus | Premature microservices — enforce modular monolith first | ddd-tactical-patterns.md, multi-cloud-decision-framework.md, architecture-decision-record.md |
| 4. Vector DB & RAG Setup | Claude Sonnet | One-size-fits-all chunking — adapt strategy to document structure | vector-db-selection.md, chunking-strategies.md, agentic-rag-patterns.md, rag-evaluation.md |
| 5. Serverless Frontend Engineering | Claude Sonnet | SSR everything — enforce decision tree: SSR/SSG/ISR | nextjs-app-router.md, shadcn-design-system.md, security-auditor.md |
| 6. Product Management | Claude Sonnet | Feature factory mode — every story must reference an OKR | PM agent becomes mesh orchestrator, not direct contributor |
| 7. QA / Total Quality Management | Claude Sonnet | Test pyramid inversion — enforce 70% unit / 20% integration / 10% E2E | Extends CCQG Part III; quality gates must block, not just report |

### Persistent Shared Memory Architecture

Without shared memory, agents rediscover context, make contradictory decisions, and cannot build on each other's work. The CCQG expansion implements the CoALA cognitive architecture framework (Princeton, 2023) with four memory types:

| Memory Type | Infrastructure | Role in CCQG |
|---|---|---|
| Working Memory | In-context token window | Real-time reasoning — active SOUL.md + loaded skill |
| Episodic Memory | Session JSONL files / vector DB with temporal tagging | Recall historical events, avoid repeating errors |
| Semantic Memory | Graph DB or dense document stores via RAG | Organisational knowledge, domain facts, architectural decisions |
| Procedural Memory | Version-controlled SKILL.md files | Procedural knowledge, continuously updated via learning loops |

The critical innovation is episodic-to-semantic consolidation: patterns from episodic events are distilled into general semantic knowledge, mirroring how human expertise develops.

#### Three-Layer Memory Architecture

- **Layer 1 — Always-On Context:** SOUL.md + AGENTS.md. Role identity, project conventions, quality gates. Injected every turn. ~2–8KB, stays lean.
- **Layer 2 — Long-Term Memory:** MEMORY.md + knowledge/. Decisions, patterns, user preferences, ADRs. Agents write here; loaded via semantic search.
- **Layer 3 — Session Memory:** sessions/YYYY-MM-DD.jsonl. Active conversation, tool call history. Per-session, compacted when >80% context window.

#### Memory Namespace Hierarchy

Hierarchical namespace prevents collision while enabling controlled sharing: `global/` → `org:{orgId}/` → `project:{projectId}/` → `agent:{agentId}/` → `session:{sessionId}/`. The **Blackboard Pattern** — agents post findings to shared project namespace, all agents read — is the most effective pattern for cross-functional coordination.

#### MCP as Integration Layer

Model Context Protocol (MCP) provides the open standard for secure, two-way connections between AI tools and data. The CCQG memory tools (save_learning, search_learnings) are exposed via MCP with hybrid search: 70% vector weight + 30% BM25/SQLite FTS5. Start file-based under ~500 entries, graduate to LanceDB, then to Qdrant or MongoDB Atlas at production multi-tenant scale.

### Self-Improving Learning Loops

#### The Learnings.md + Wrap-Up Skill Pattern

The single highest-leverage learning mechanism. At session end, the Wrap-Up Skill analyses the session transcript and writes learnings back to Learnings.md. Each entry includes dated metadata, confidence scores, and session references. Every session without a wrap-up loses learning data.

#### Three-Speed Learning Architecture

- **Speed 1 — Real-time (per-run): Reflexion.** After each task failure, generate verbal self-critique stored in episodic memory. Used immediately on next attempt within the same session.
- **Speed 2 — Batch (every 25–50 runs): ExpeL.** Accumulate run results, use Claude to compare successes vs. failures, generate/update max 15 insights. Merge into SKILL.md "Learned Patterns" section. Requires A/B validation before committing.
- **Speed 3 — Strategic (weekly/monthly): DSPy/Ax Prompt Optimisation.** When 30+ labelled examples per role are available, run the Ax Framework (@ax-llm/ax, TypeScript port of DSPy) with MIPROv2 or GEPA optimisers for Bayesian prompt optimisation.

#### PDCA/DMAIC Governance for Agent Quality

PDCA governs the agent capability stack on a weekly cadence: Plan (define quality benchmarks, create evaluation datasets) → Do (run agents with Langfuse monitoring) → Check (evaluate metrics, cluster failure modes, run ExpeL batch if 25–50 runs accumulated) → Act (update SKILL.md, A/B test, deploy or rollback).

Six Sigma DMAIC maps directly: Define (agent acceptance criteria) → Measure (error rates per role via Langfuse traces) → Analyse (root causes via LLM-based failure classification) → Improve (SKILL.md updates) → Control (statistical process monitoring with regression alerts).

#### Learning Degradation Prevention

- Cap accumulation: max 15 insights + 10 error corrections per SKILL.md
- Active forgetting: remove learnings not triggered in last N runs (ExpeL REMOVE)
- Periodic condensation: compress accumulated learnings monthly
- Git-based versioning: every update is a commit with eval metrics; rollback is git revert
- A/B validation gate: require p < 0.05 statistical significance before promotion
- Continuous drift monitoring: alert when quality scores drop regardless of SKILL.md changes

> **The immutable constraint: Learning loops update heuristics only. They never lower quality gates, relax TDD requirements, or reduce coverage thresholds.**

---

## Section 8: Design System Strategy

The FlowTrain Quality Guardian Design System provides a unified visual language across all Quality Guardian interfaces and the broader Train Yard fleet.

### Technology Foundation

| Layer | Technology | Purpose |
|---|---|---|
| Component Library | shadcn/ui (50+ Radix primitives) | Accessible, composable UI components with CSS variable theming |
| Styling | Tailwind CSS | Utility-first CSS with design token integration |
| Framework | React + TypeScript | Type-safe component development with modern hooks API |
| Theming | CSS custom properties (variables) | Semantic token system for light/dark mode and brand customisation |
| AI Integration | shadcn/ui MCP Server | AI-assisted UI development with component awareness |
| Distribution | Custom Registry | Quality Guardian-specific component distribution and versioning |

### Brand Color Mapping to shadcn/ui Tokens

| Brand Element | Hex Value | shadcn/ui Token | Usage |
|---|---|---|---|
| FlowTrain Blue | #2BAEE4 | --primary | Primary CTAs, active states, links, navigation highlights |
| FlowTrain Black | #231F20 | --background (dark) | Dark mode background, high-contrast surfaces |
| Purple Accent | #5A4FCF | Phase banners, accent | Phase progression indicators, accent highlights |
| Blue-to-Cyan Gradient | #2BAEE4 → #00D4FF | Accent surfaces | Hero areas, feature cards, data visualisation highlights |
| White | #FFFFFF | --background (light) | Light mode background, card surfaces |
| Light Blue | #E8F6FD | --accent | Hover states, secondary highlights, table alternating rows |
| Dark Slate | #1A3A4F | --foreground (dark) | Dark mode headings, high-emphasis text |

### Fleet-Wide Color Extension

These tokens are established by the StructureView and Turntable Hub visual identity and apply across the entire suite:

| Token Name | Hex Value | Origin Product | Fleet-Wide Usage |
|---|---|---|---|
| Gold | #F0C050 | StructureView (syntax accent) | JSON highlighting, syntax accents, "steam" particle effects in Turntable, premium feature indicators |
| Steam Red | #D44030 | StructureView (warnings) | Warnings, alerts, unavailable tool states in Turntable Hub, error states requiring immediate attention |
| Deep Background | #0a0a0f | StructureView dark base | Fleet dark mode primary background — load-bearing for suite cohesion, Turntable night yard |
| Roundhouse Surface | #12121a | Turntable Hub | Secondary dark surface for the roundhouse structure, card surfaces over Deep Background |

These four tokens, combined with the existing FlowTrain Blue (#2BAEE4), form the complete fleet dark theme palette. Every product in the Train Yard should use this palette as the foundation.

### Light and Dark Mode Strategy

**Light Mode (Stakeholder-Facing):** Clean, professional, optimised for executive dashboards, compliance reports, and presentations. White backgrounds, subtle blue accents, high readability.

**Dark Mode (Developer-Facing):** Dashboard-optimised with Deep Background (#0a0a0f) as the fleet-wide dark base, Roundhouse Surface (#12121a) for elevated surfaces, FlowTrain Blue for active states, Gold (#F0C050) for syntax and accent highlights, and Steam Red (#D44030) for warnings.

### Component Categories

| Component Category | Examples | Primary Use |
|---|---|---|
| Quality Metric Cards | KPI cards, DORA metric tiles, coverage percentage displays | Dashboard surfaces showing real-time quality state |
| Test Quadrant Visualisations | 4-quadrant matrix, quadrant health bars, test distribution charts | TIMC test plan views and quality overview |
| Traceability Matrix Tables | Requirements-to-tests mapping, compliance evidence linking | Compliance & traceability views |
| Release Gate Steppers | Stage-gate progression (Alpha → GA), criteria checklists | Product lifecycle and release readiness views |
| Agent Activity Timelines | Agent execution logs, inter-agent communication traces | CCQG Quality Engine monitoring |
| Compliance Status Badges | Covered/Partial/Gap indicators, regulatory status icons | Compliance views and audit dashboards |
| Discovery Workflow Components | Opportunity trees, assumption maps, risk scorecards | Product Discovery integration views |
| Steam Pressure Gauges | Release readiness percentage dial, team green-up progress, rollout population controls | Q2 Release departure decision UI and feature flag management |
| Domain Dependency Graphs | Organisational topology visualisation, dependency edge annotations, Team Topologies classification indicators | Q2 Release domain model views and release readiness graphs |
| Certificate of Conformity Cards | Immutable compliance records with regulatory framework badges, HITL sign-off status, timestamp chains | Tier 4 audit trail views and compliance certificate displays |
| Turntable Navigation | Rotating hub interface, track selection, locomotive dispatch animation, roundhouse layout | Turntable Hub central launcher — the fleet navigation paradigm |

### shadcn/ui MCP Server Integration

The shadcn/ui MCP Server enables AI-assisted development of Quality Guardian interfaces. When integrated with the Quality Guardian agent ecosystem, the MCP Server allows agents to:

- Generate UI components programmatically based on data schemas and quality requirements
- Validate generated interfaces against the FlowTrain design system automatically
- Maintain design system consistency across all agent-generated views
- Access the custom Quality Guardian component registry for domain-specific UI elements

Storybook enables building, testing, and documenting components in isolation. Playwright ARIA snapshots provide structured accessibility tree representations for lower-token, semantically meaningful UI testing.

---

## Section 9: Skills Roadmap

Skills are composable, AI-invokable capabilities that accelerate Quality Guardian development. Each skill encapsulates domain-specific knowledge and tooling.

### 1. quality-dashboard-builder
**Description:** Builds interactive quality metric dashboards with shadcn/ui components and Recharts visualisations.
**Trigger Patterns:** "Build a quality dashboard", "Show DORA metrics", "Create coverage report view"
**Tech Stack:** React + TypeScript + shadcn/ui + Recharts + Tailwind CSS
**Outputs:** Single-page dashboard applications with KPI cards, trend charts, and drill-down tables

### 2. bdd-scenario-generator
**Description:** Generates Gherkin BDD scenarios from Job Stories and acceptance criteria for automated testing. Integrates with the 6-step translation pipeline from Section 6.
**Trigger Patterns:** "Generate BDD scenarios", "Create Gherkin tests", "Convert Job Story to test"
**Tech Stack:** Gherkin syntax + Cucumber integration + TypeScript step definition scaffolding
**Outputs:** Feature files (.feature), step definition templates, test execution configuration

### 3. test-plan-composer
**Description:** Creates TIMC-structured test plans across 4 quadrants with regulatory tag mapping.
**Trigger Patterns:** "Create test plan", "Map tests to quadrants", "Generate TIMC test strategy"
**Tech Stack:** YAML/JSON schema + TIMC quadrant model + regulatory tag taxonomy
**Outputs:** Structured test plan documents, quadrant distribution reports, regulatory coverage matrices

### 4. compliance-artifact-builder
**Description:** Generates audit-ready compliance documents with traceability evidence and regulatory mapping.
**Trigger Patterns:** "Generate compliance report", "Build audit evidence", "Create traceability matrix"
**Tech Stack:** Document generation (DOCX/PDF) + TIMC traceability schema + regulatory requirements registry
**Outputs:** Compliance evidence packages, traceability matrices, regulatory audit reports

### 5. agent-card-creator
**Description:** Domain agent registration and configuration with capability mapping and calendar integration.
**Trigger Patterns:** "Register domain agent", "Configure agent capabilities", "Create agent card"
**Tech Stack:** JSON schema + agent-card.json format + capability/framework/calendar taxonomies
**Outputs:** Agent card JSON files, capability manifests, framework configuration documents

### 6. design-system-enforcer
**Description:** Validates UI implementations against FlowTrain design system tokens, components, and patterns.
**Trigger Patterns:** "Check design system compliance", "Validate UI tokens", "Audit component usage"
**Tech Stack:** CSS variable analysis + shadcn/ui component validation + Tailwind CSS linting
**Outputs:** Design system compliance reports, token usage audits, remediation guidance

### 7. discovery-to-delivery
**Description:** Bridges product discovery artifacts (Job Stories, OSTs) to development backlog items with quality traceability.
**Trigger Patterns:** "Convert discovery to backlog", "Bridge discovery to delivery", "Map opportunities to stories"
**Tech Stack:** Opportunity Solution Tree parser + Job Story templates + BDD integration
**Outputs:** Backlog items with discovery provenance, BDD scenario links, risk annotations

### 8. traceability-mapper
**Description:** Maps requirements to tests to results to compliance evidence in a unified traceability matrix.
**Trigger Patterns:** "Map requirements to tests", "Build traceability matrix", "Link tests to compliance"
**Tech Stack:** Requirements registry (YAML) + TIMC test results + compliance requirements database
**Outputs:** Full traceability matrices, coverage gap reports, compliance evidence chains

---

## Section 10: Recommended Technology Stack

*Source: CCQG Expansion Paper — Part 5 (March 2026)*

### Full Five-Layer Architecture Blueprint

| Layer | Technology | Package |
|---|---|---|
| Runtime | Node.js 22+ LTS, TypeScript 5.5+ | typescript |
| Agent Orchestration | LangGraph.js (stateful graph with supervisor pattern) | @langchain/langgraph |
| Model Communication | Vercel AI SDK v5 + Mastra | ai, @mastra/core |
| Claude API | Anthropic SDK | @anthropic-ai/sdk |
| Multi-Provider | Vercel AI SDK providers | @ai-sdk/anthropic, @ai-sdk/openai, @ai-sdk/google |
| Short-Term Memory | LangGraph PostgresSaver | @langchain/langgraph-checkpoint-postgres |
| Long-Term Memory | Mem0 (91% latency reduction) | @mem0/vercel-ai-provider |
| Vector + Document Store | MongoDB Atlas (multi-cloud) or Qdrant | mongodb, @qdrant/js-client-rest |
| Relational + Checkpoints | PostgreSQL + pgvector | pg |
| Schema Validation | Zod | zod |
| Observability | Langfuse (open-source, self-hostable) | @langfuse/tracing, @langfuse/otel |
| Prompt Optimisation | Ax Framework (DSPy for TypeScript) | @ax-llm/ax |
| UI Framework | Next.js 15 + shadcn/ui | next, shadcn |
| Testing | Vitest + Playwright | vitest, @playwright/test |
| Gateway (optional) | LiteLLM Proxy (400+ models) | Self-hosted Docker |

> **Database note:** The original brief specified Azure Cosmos DB (DiskANN) as the primary vector and document store. Version 5 replaces this recommendation with **MongoDB Atlas** as the primary option for new deployments, on the basis of multi-cloud portability. See Appendix C (Architecture Glossary) for a full comparison. If the architecture is Azure-native and multi-cloud failover is not a requirement, Cosmos DB remains a valid choice; it is retained as an alternative in the infrastructure graduation triggers below.

### Infrastructure Graduation Triggers

| Current State | Trigger | Target |
|---|---|---|
| File-based keyword search | Memory corpus > 500 entries | LanceDB vector search |
| LanceDB | Production multi-tenant scale | Qdrant or MongoDB Atlas |
| No learning loop | 25–50 accumulated runs per role | ExpeL batch learning loop |
| ExpeL only | 30+ labelled examples per role | Ax/DSPy strategic optimisation |
| Single model for all roles | Langfuse shows 60%+ of calls could use cheaper model | Multi-model routing (Mastra + LiteLLM) |
| Manual Learnings.md | Wrap-Up Skill reliable over 10+ sessions | Autonomous PR commits via learning agent |

### What Not to Build Prematurely

- MoA for every decision: Reserve for architecture reviews and complex PRDs only
- Cosmos DB DiskANN or MongoDB Atlas Vector Search from day one: Start with pgvector or LanceDB
- Ax/DSPy optimisation on day one: Requires 30+ labelled examples; build eval datasets first
- Full eight-agent mesh from day one: Start with Code Guardian + Wrap-Up Skill + one new bundle (UI/UX recommended)

### Current Build Status (April 2026)

| Deliverable | Status | Notes |
|---|---|---|
| TIMC UI Realignment (5 major changes) | **DONE** | All 37 line items complete |
| P0/P1 Bug Fixes | **DONE** | 3 P0s, 6 P1s resolved, 80+ tests |
| Dashboard Data Pipeline | **DONE** | generate-timc-summary.mjs, 25 tests |
| Shared UI Components (Stepper, TagFilterRow) | **DONE** | Reusable components in UIComponents.jsx |
| 28 Specs Implemented | **DONE** | ~60,000 lines, ~60 tracked issues |
| Design System Token Definitions | **IN PROGRESS** | FlowTrain brand mapped; formal token file pending |
| MCP Server (Docker/WSL) | **BLOCKED** | Docker/WSL configuration issue; resolved manually for now |
| StructureView Phase 1 | **DONE** | Core viewer, FlowTrain brand, three view modes shipped |
---

## Section 11: Implementation Roadmap

The roadmap reflects the multi-product fleet architecture. Quality Guardian remains the platform core, but the build sequence now accounts for StructureView as the acquisition entry point, TIMC Light as the conversion bridge, Q2 Release as the release coordination expansion, and Tier 4 as the compliance layer.

### Phase 1: Foundation (Q1 2026) — Complete

| Deliverable | Status | Notes |
|---|---|---|
| TIMC UI Realignment (5 changes) | DONE | All 37 line items complete |
| P0/P1 Bug Fixes | DONE | 3 P0s resolved, 6 P1s resolved with 80+ tests |
| Dashboard Data Pipeline | DONE | generate-timc-summary.mjs populates timc-summary.json via CI (25 tests) |
| Shared UI Components (Stepper, TagFilterRow) | DONE | Reusable components in UIComponents.jsx |
| Design System Token Definitions | IN PROGRESS | FlowTrain brand mapped to shadcn/ui tokens; formal token file pending |
| StructureView Core (file viewer) | DONE | Phase 1 shipped — core viewer, FlowTrain brand, three view modes |

### Phase 2: Design System, Skills & Acquisition Funnel (Q2 2026) — Planned

| Deliverable | Target | Dependencies |
|---|---|---|
| Fleet-Wide Design System on shadcn/ui | April 2026 | Token definitions covering all 4 products; #0a0a0f dark base, Gold #F0C050, Steam Red #D44030 |
| AGENTS.md authoring | April 2026 | Human-authored project-level rules — applies across all products |
| Wrap-Up Skill (/wrap-up) | April 2026 | Highest-leverage learning loop — applies across all products |
| TIMC Light MVP (StructureView Lite) | May 2026 | Spec completeness signals, JSON structural quality — the conversion bridge |
| Shared Memory MCP primitives | May 2026 | JSONL storage + keyword search (Step 1) — foundation for enterprise bundle |
| quality-dashboard-builder skill | May 2026 | Design system tokens; Recharts integration |
| Turntable Hub static (no animation) | June 2026 | Validate metaphor and navigation with 2 tracks (StructureView + Quality Guardian) |
| bdd-scenario-generator skill | June 2026 | Gherkin template library; Cucumber integration |
| test-plan-composer skill | June 2026 | TIMC quadrant model formalisation |

### Phase 3: Agent Expansion & Fleet Growth (Q3 2026) — Planned

| Deliverable | Target | Dependencies |
|---|---|---|
| Product Discovery Agent | July 2026 | Customer feedback pipeline; OST data model; BDD generator |
| Quality at Source Agent | August 2026 | CI/CD pipeline integration; static analysis connectors |
| UX Quality Agent | August 2026 | axe-core; design system enforcer; Lighthouse pipeline |
| UI/UX Skill Bundle | July 2026 | shadcn MCP server; ARIA snapshot testing |
| TIMC Light Phase 2 (config validation, AI output signals) | July 2026 | Expands StructureView Lite conversion funnel |
| Q2 Release domain model wizard prototype | August 2026 | Organisational topology capture — first Q2 Release deliverable |
| Turntable Hub basic rotation animation | September 2026 | Establishes the signature interaction paradigm |
| First ExpeL batch run | September 2026 | 25–50 accumulated runs per role |
| Tier 4 regulatory framework documentation | September 2026 | 3-tier accountability framework for regulatory configuration design |

> **Q2 Release dates in Phase 3–4 are assumed, not confirmed.** The Q2 Release standalone roadmap vs. phased Quality Guardian integration requires an explicit sequencing decision before Q3 build starts.

### Phase 4: Enterprise Platform & Fleet Completion (Q4 2026) — Planned

| Deliverable | Target | Dependencies |
|---|---|---|
| Full Agent Orchestration (8-agent mesh) | October 2026 | All Phase 3 agents operational; shared memory across fleet |
| Omnichannel Quality Agent | October 2026 | Cross-channel data pipeline; feeds Q2 Release patterns |
| Release Readiness Agent → Q2 Release integration | November 2026 | DORA metrics pipeline; Q2 Release domain model wizard |
| Q2 Release closed beta orchestration | November 2026 | Feature flag management; population routing |
| Tier 4 Compliance Mode Phase 1 | November 2026 | Audit log; basic Certificate of Conformity; requires QG agents |
| Documentation Agent for Living Docs & Compliance | December 2026 | All agent output schemas; Certificate of Conformity depends on this |
| Full Turntable Hub dispatch animation | December 2026 | Ships with Q2 Release or enterprise bundle |
| Multi-model routing (Mastra + LiteLLM) | December 2026 | Langfuse data showing routing optimisation potential |
| Ax/DSPy strategic prompt optimisation | December 2026 | 30+ labelled examples per role |
| TQM Compliance Agent | December 2026 | TQM assessment framework; Tier 4 subsumes at enterprise scale |

### Strategic Decision Points

- **Q2 Release sequencing** — standalone roadmap vs. phased Quality Guardian integration needs an explicit decision before Q3 build starts
- **Tier 4 regulatory framework priority order** — recommendation: FINRA first, given existing financial services research depth
- **StructureView Pro tier feature set** — determines free vs. paid boundary for acquisition funnel

---

## Section 12: Strategic Positioning

### The Train Yard as FlowTrain's Product Architecture

"Quality Guardian" remains the platform core, but FlowTrain HQ's market position is now the **Train Yard** — a fleet of purpose-built tools that compose into an enterprise quality platform. The brand promise: Structure → Quality → Ship → Certify. Every locomotive, a step in the journey.

Each Train can be sold individually. Each can be adopted by a single team. Each delivers immediate value. But the enterprise bundle — all four Trains with shared memory, unified traceability, and organisational intelligence — is the moat. The acquisition path is individual Trains. The retention is the bundle.

### Can Each Train Stand Alone?

**Yes. Explicitly yes.** Each Train is designed with:

- A clear standalone mission that doesn't require the rest of the fleet
- A pricing model accessible without enterprise commitment
- A value proposition that makes sense to a team of 5, not just a company of 5,000
- A natural upgrade trigger that creates desire for the next Train without requiring a sales conversation

**StructureView** is useful the moment a developer opens a JSON file. No other Train required.

**Q2 Release** solves the release coordination problem for 5 teams without Quality Guardian. It becomes dramatically more powerful with Quality Guardian feeding release readiness data — but it doesn't require it to deliver day-one value.

**Tier 4** is the one exception — it requires Quality Guardian as a foundation. It is a compliance mode, not a standalone tool. The compliance conversation leads to Quality Guardian adoption, not the other way around.

### Competitive Moat

| Moat Component | Description | Differentiation |
|---|---|---|
| Regulatory Expertise | Deep domain knowledge in FINRA, SEC (17a-4, 613/CAT), IRC §1091, WCAG 2.2 AA, FDA 21 CFR Part 11 | Most quality tools are domain-agnostic; Tier 4 is built for regulated industries |
| Clean Code Foundation | AI-powered code quality enforcement with domain-specific cognitive architectures | Goes beyond linting to enforce domain patterns and architectural standards |
| TQM Integration | Full TQM principle mapping across the product lifecycle | Uniquely bridges management philosophy with engineering automation |
| Product Discovery Bridge | Quality metrics feed discovery loops; discovery artifacts trace to test coverage | No competitor bridges the gap between discovery and quality |
| Spec-Based Development | Job Story → Spec → Tests → Agent Execution pipeline | Deterministic engineering accelerator vs. probabilistic vibe coding |
| Self-Improving Agent Mesh | ExpeL + Reflexion + DSPy/Ax learning loops with PDCA governance | Agents measurably improve with every task completed |
| Fleet Architecture | Four standalone products composing into an enterprise bundle with shared memory | Land-and-expand from free file viewer to enterprise compliance platform |
| Organisational Intelligence | Release pattern data, dependency risk profiles, and bottleneck detection built from actual release cycles | No competitor instruments the release coordination problem at this depth |

### Revenue Streams

- **SaaS Subscriptions — The Core Revenue:** StructureView (free → Pro $4.99/mo → Team $9.99/user/mo), StructureView Lite (conversion bridge), Quality Guardian (Team → Division → Enterprise), Q2 Release (Observer → Coordinator → OS), Tier 4 (Viewer → Monitor → OS), Enterprise Bundle (all Trains + shared memory + organisational intelligence).

- **Training & Certification:** TQM-for-engineering workshops, BDD mastery courses, Quality Guardian certification programs. Target: engineering managers, QA leads, product managers in regulated industries.

- **Consulting Services:** Quality assessment engagements, TQM adoption roadmaps, TIMC implementation, SDD adoption consulting, regulatory compliance gap analysis. Leveraging the financial case ($273M in addressable waste).

- **Workshop Revenue ($10K/day):** AI Compliance in Regulated Industries workshop → Tier 4 closed beta funnel. Release Coordination workshop → Q2 Release early adopters. The pharma platform story, the 3-tier accountability framework, the 5-mile release walk — practitioner content that commands premium pricing while products build.

- **Content Pipeline:** LinkedIn posts (individual stories) → long-form essays (chapter-length case studies) → workshops ($10K/day) → book (trust accelerator for enterprise sales). Each workshop audience is top-of-funnel for one or more Trains.

### The Hackathon-to-Enterprise Pipeline

The acquisition funnel operates at two levels — the product funnel (individual Train adoption) and the content funnel (workshop → beta customer):

1. Hackathon Showcase: Demonstrate the platform at internal and external hackathons
2. Open Source Core: Release foundational components (design system, BDD generator, traceability mapper) as open source
3. StructureView Free → Lite Conversion: Food court strategy — real quality signal, zero commitment
4. Team Adoption: Individual teams adopt Quality Guardian agents to solve immediate quality pain
5. Q2 Release Expansion: Teams coordinating releases adopt Q2 Release for orchestration
6. Tier 4 Enterprise: Regulated industries activate compliance mode for audit-ready delivery
7. Enterprise Bundle: All Trains, shared memory, unified traceability, organisational intelligence

**The story is the product. The products are the story, made executable.**

---

## Section 13: The Train Yard — Fleet Architecture

*Source: Train Yard Fleet Overview, StructureView Brief, StructureView Lite Brief, Q2 Release Brief, Tier 4 Compliance Brief, Turntable Hub Brief (April 2026)*

### The Fleet Narrative

The Train Yard is not four separate products that happen to share a brand. It is one complete narrative about how software gets from idea to auditable, certified delivery.

**StructureView** is where the documents live. Specs, configs, AI outputs, evidence packages — all the structured artifacts that make up modern software delivery, made navigable and readable for everyone on the team, not just developers.

**Quality Guardian** is where quality is enforced. Continuously, automatically, across every phase of the product lifecycle — from product discovery through code to deployment and operations. The UP 844 never retires. Neither does quality.

**Q2 Release** is where the train departs. The orchestration layer that takes 86 teams across 4 continents from individual readiness to coordinated release — with two crews in every cab, organisational intelligence building with every cycle, and a steam pressure gauge that tells you when you're truly ready.

**Tier 4** is where compliance is certified. The layer that makes everything that came before *provable* — to a regulator, in a courtroom, in a board meeting, on demand.

**Structure → Quality → Ship → Certify. Every locomotive, a step in the journey.**

| Locomotive | Product | Mission | Tagline |
|---|---|---|---|
| EMD SD70ACe | StructureView | Haul your structured documents with precision | *The modern workhorse* |
| UP 844 | Quality Guardian | Total quality management across the full product lifecycle | *Never retired. Always on guard.* |
| PRR Q2 | Q2 Release | Release coordination operating system for complex organisations | *Two seats in the cab. One train to ship.* |
| Metrolink Tier 4 | Tier 4 | Provably compliant software delivery for regulated industries | *Certificate of conformity. Every run.* |

### Pricing Architecture

> **Note:** Tier 4 Compliance OS (Tier 3) requires a Quality Guardian Team or Enterprise licence as foundation. This dependency applies at the fleet level, not just within the Tier 4 product section.

| Tier | Capability | Products | Notes |
|---|---|---|---|
| Tier 1 — Read | View, observe, analyse individual artifacts | StructureView (free/low cost), Q2 Release Observer | — |
| Tier 2 — Aggregate | Aggregate signals, light quality analysis, closed beta entry | StructureView Lite (+ TIMC Light), Q2 Release Coordinator | — |
| Tier 3 — Author | Full platform, agent orchestration, compliance certification | Quality Guardian, Q2 Release OS, Tier 4 OS | Tier 4 OS requires QG licence |
| Enterprise Bundle | All Trains, shared memory, unified traceability, organisational intelligence | Full Train Yard | — |

---

### StructureView — The Entry Point

*Locomotive: EMD SD70ACe — reliable, precise, handles any load. The SD70ACe doesn't just haul freight — it opens the yard.*

StructureView exists to give developers, product managers, and technical writers a single precision instrument for viewing, navigating, and understanding structured files — without losing the thread of what the document *means*, not just what it *contains*. **There is no precision instrument for the middle ground** — the moment when someone needs to *understand* a file, not *edit* it. StructureView fills that gap.

#### Core Capabilities

**File Viewing Engine**
- Multi-format support: MD, JSON, XML, YAML, TOML (v1.0 shipped); CSV, JSONL (v1.1 — planned)
- Three view modes: **Preview** (rendered), **Raw** (syntax-highlighted source), **Outline** (navigable structure tree)
- Format-aware rendering — Markdown prose gets serif typography, JSON gets collapsible tree, XML gets schema-aware display
- **Note: XML support is read-only in this version**

**Navigation & Organisation**
- Sidebar file browser with format-coded indicators (colour-coded by file type)
- Sidebar sections: **"On Track"** (open files) and **"Siding"** (recent files) — railroad vocabulary, earned not forced
- Tab-based multi-file workspace

**Visual Identity**
- FlowTrain brand pulled all the way through: #2BAEE4 blue for active states, #F0C050 gold for syntax accents and JSON highlighting, #D44030 steam red for warnings and alerts
- SD70ACe silhouette in toolbar chrome — `{ }` curly braces at the nose, `</>` on the windshield, document/file icons as train windows
- Rail accent stripe (blue → gold → blue) at top — nod to locomotive livery
- **Format badge** (MD / JSON / XML) displayed in the toolbar, right-aligned next to the view mode tabs
- JetBrains Mono for all technical labels; serif (Georgia) for document prose
- **Status bar reads: `DISPATCHED · EMD SD70ACe`** — mechanical satisfaction in every session
- Dark theme primary: #0a0a0f deep background, #12121a card background — load-bearing for suite cohesion

#### Standalone Value

- **For developers:** The fastest way to understand an unfamiliar structured file without opening an IDE.
- **For PMs and technical writers:** A reading environment for technical documents that respects the document's structure — not just its text.
- **For QA and compliance teams:** A clean, auditable viewer for test artifacts, compliance evidence, and specification packages — without needing engineering tooling.

#### Upgrade Trigger

The moment TIMC Light finds a quality signal it cannot fully resolve — a missing EARS notation in a spec, a WCAG flag in a UI config, a structural gap in a JSON API response — a callout appears:

> **"Full analysis available in Quality Guardian."**

That is the moment. The customer has seen the problem. They know you can solve more of it. The ask is natural.

#### StructureView Roadmap

| Phase | Target | Deliverable |
|---|---|---|
| Phase 1 | Complete | Core file viewer, FlowTrain brand, three view modes |
| Phase 2 | Q2 2026 | TIMC Light integration, StructureView Lite bundle |
| Phase 3 | Q3 2026 | YAML/TOML support (v1.0), outline deep-linking, agent output rendering |
| Phase 4 | Q4 2026 | Full Quality Guardian suite integration, traceability linking |

---

### StructureView Lite — The Conversion Bridge

*The food court sample. Real quality signal. Zero commitment required.*

In 2016, a pharma ecommerce platform went live across 25 teams and 4 continents with flip charts and walkie-talkies. The people who bought the tools that replaced that process didn't do it because a salesperson told them they needed it. They did it because they *felt* the problem, *saw* a better way, and the ask was natural. StructureView Lite is engineered for that moment.

A developer opens a spec. A PM reviews an AI output. A compliance officer looks at an evidence package. StructureView Lite renders it beautifully — and then surfaces *one real quality signal* they didn't know to look for. Not a demo. Not a gesture at quality. **Real work, on their real document.** The upgrade writes itself.

TIMC Light is designed to demonstrate that understanding **in the first 60 seconds of use**.

#### TIMC Light — Document-Type Aware Signals

| Document Type | TIMC Light Signal |
|---|---|
| Requirements / Spec (MD) | EARS notation coverage — are requirements machine-readable? |
| JSON API Response | Structural quality score — schema compliance, null handling, consistency |
| Configuration File (XML/YAML) | Schema validation — required fields, type correctness, deprecated keys |
| AI Output (MD/JSON) | Hallucination indicators — confidence markers, source references, structural completeness |
| Test Plan / BDD Scenario | Gherkin coverage — Given/When/Then completeness, missing edge cases |
| Compliance Artifact | Regulatory tag presence — SEC, WCAG, FINRA markers |

Signals appear **inline** in the StructureView interface — not in a separate panel, not as a modal, not as a notification badge. Examples: `⚠ 2 requirements missing EARS notation`, `Schema gap detected — 'settlement_date' field undocumented`, or a document-level health bar: `Spec completeness: 73%`.

#### The Upgrade Trigger

When TIMC Light finds a signal it cannot fully resolve, a single callout appears: *"Full analysis available in Quality Guardian — traceability matrix, coverage mapping, and compliance evidence generation."* This appears **once per session**, at the moment of maximum relevance. It is never a banner. It earns its place.

#### What Lite Deliberately Omits

These are the reasons to upgrade. They are visible as locked capabilities when TIMC Light surfaces a signal:

- Full traceability matrix (requirements → tests → results → compliance)
- Multi-file aggregate quality analysis
- Agent-driven improvement recommendations
- Compliance artifact generation
- Team-level quality dashboards
- Release readiness integration

#### Acquisition Funnel

```
StructureView (free / Tier 1)
    ↓  user opens a spec or compliance doc
StructureView Lite (Tier 2)
    ↓  TIMC Light surfaces a real quality signal
    ↓  user sees the locked full-analysis callout
Quality Guardian Team (Tier 3)
    ↓  team adopts quality dashboards, agent checks
Quality Guardian Enterprise (Tier 3 full)
    ↓  full 8-agent mesh, DORA metrics, compliance artifacts
```

The funnel is pull-based at every stage. Each step creates the desire for the next.

#### Roadmap

| Phase | Target | Notes |
|---|---|---|
| Phase 2 | Q2 2026 | TIMC Light MVP — spec completeness, JSON structural quality |
| Phase 2.5 | Q3 2026 | Config validation, AI output signals |
| Phase 3 | Q3 2026 | BDD/Gherkin coverage, compliance artifact signals |
| Phase 4 | Q4 2026 | Full Quality Guardian upgrade flow, traceability preview |

#### Success Metrics

| Metric | Target |
|---|---|
| % of Lite users who encounter a TIMC Light signal | > 80% within first session |
| % of signal encounters that lead to upgrade CTA view | > 60% |
| % of CTA views converting to Quality Guardian trial | TBD — establish baseline in closed beta |
| Time from first Lite session to upgrade conversation | < 14 days |

---

### Q2 Release — The Release Coordination OS

*Locomotive: PRR Q2 — the most powerful high-quality steam freight locomotive in America. Demands a two-person crew. Cannot be operated alone.*

> **Origin note:** The PRR Q2 slot was originally conceived as a PR/comms tool — "the PRR in the name is too good to ignore." The concept evolved during product development into release coordination and closed beta orchestration, which is a significantly stronger and more defensible product position. The locomotive metaphor carries even more cleanly in the evolved concept.

#### The Two-Person Crew

A Pennsylvania Railroad Q2 locomotive required two people in the cab:
- **The Engineer** — controlled speed, starting, and stopping
- **The Fireman** — maintained the fire, steam pressure, and water levels

Neither could run a Q2 alone. **That's not a limitation. That's the point.**

- **The Engineer (Developer):** Sets the route, controls speed, configures feature flags, sets population splits, defines rollout logic.
- **The Fireman (Business Stakeholder):** Maintains the pressure. Monitors burn rate, manages business conditions, provides go/no-go sign-off.

**Q2 Release is a collaboration tool disguised as a release tool.**

#### The Problem It Solves

In 2016, that problem was solved with a 40-foot story map, a sticker chart outside the team pods, and a person walking 5 miles in an office with a walkie-talkie. PA was always the last to green up. Q2 Release is what should have existed then. And what exists now.

Every organisation running a complex release cycle is currently doing one of three things:

1. **The flip chart approach** — manual status, walkie-talkies, a person walking the floor. Doesn't scale past 10 teams.
2. **The JIRA board approach** — visible but not actionable. Shows you the problem after it's already late.
3. **The nothing approach** — hope, coordination meetings, and a tense Tuesday morning.

None of them capture the shape of the dependencies. None learn the org's release fingerprint over time. **Q2 Release does.**

#### Core Capabilities

**Domain Model Wizard**
A structured form — or AI-guided wizard — capturing organisational topology: teams, domains, ownership, dependency edges with boundary annotations, Team Topologies classifications (stream-aligned, complicated-subdomain, platform, enabling), cross-domain integration points and load-bearing dependencies. Once captured, **release readiness is computable, not a meeting.**

**Release Readiness Dashboard**
Team-by-team, domain-by-domain, geography-by-geography status. Dependency graph view showing blocked domains. Real-time green-up progress with steam pressure metaphor:
- At 0%: *cold iron. The train isn't moving.*
- At 50%: *building pressure. Some cohorts live, pattern data accumulating.*
- At 100%: *full steam. Departure authorised.*

The two-person crew model: engineering status separate from business sign-off, both required for departure.

**Feature Flag & Population Routing**
Multi-PR stacked A/B testing configuration. Population routing and cohort management for closed beta phases. Feature flag lifecycle (create, target, graduate, retire) via business-facing interface.

**Closed Beta Orchestration**
Participant management for closed beta cohorts. Feedback capture tied to release artifacts. Scope voting workflows. Configurable release cadence (6-week default) with planning integration.

**Pattern Detection & Organisational Intelligence**
- Which domains are statistically always the last to go green
- Which team topologies create release bottlenecks
- Which dependency edges are chronically risky
- Where the fireman (business sign-off) is always the constraint vs. where it's always the engineer

**Quality Guardian Integration**
Quality gate status feeds the release readiness graph. DORA metrics flow into the departure decision. Release evidence packages satisfy Certificate of Conformity requirements.

#### Standalone Value

- **For engineering leaders:** The first tool that makes cross-team release coordination observable, learnable, and improvable — without adding another meeting.
- **For PMs and business stakeholders:** A seat in the cab, not a report after the fact.
- **For CTOs/VPs Engineering:** The organisational intelligence layer that turns 86 release cycles into a pattern dataset.
- **For regulated industries:** The HITL layer satisfying regulatory requirements for human oversight, with immutable audit trail.

#### Pricing Tier Model

| Tier | Name | Capability |
|---|---|---|
| Tier 1 — Read | Release Observer | View release status, domain graph, team progress |
| Tier 2 — Aggregate | Release Coordinator | Manage feature flags, population routing, closed beta |
| Tier 3 — Author | Release OS | Full domain model, pattern detection, organisational intelligence, Quality Guardian integration |

#### Target Customer

Q2 Release is relevant to any organisation with taggable goods and services, living in the tail of two products — the product being built, and all the digital products used for servicing and customer interaction. The MVP needs one organisation running a closed beta release cycle that feels the pain — even 5–10 teams with real domain dependencies proves the value.

#### Taglines

- *"The Q2 was quality personified. Your releases should be too."*
- *"Two seats in the cab. One train to ship."*

---

### Tier 4 — The Compliance Engine

*Locomotive: Metrolink Tier 4 — EPA-certified, 70% pollutant reduction, Positive Train Control. The compliance engine meets the standard before it moves, every time.*

| Tier 4 Locomotive | Tier 4 Product |
|---|---|
| 70% reduction in pollutants | 70%+ reduction in compliance violations, audit findings, escaped defects |
| Positive Train Control (PTC) | HITL layer — human approval gate that cannot be bypassed |
| Certificate of Conformity | Immutable quality gate pass artifact — the audit trail |
| Replacing Tier 0 with Tier 4 | Replacing manual compliance processes with instrumented, agentic ones |
| California Air Resources Board | FINRA, SEC, FDA, DEA — the pattern of controls is identical |

#### The Regulatory Context

FINRA and FDA are on different ends of the regulatory spectrum, but the controls at the kernel are nearly identical. Tier 4 is built on that kernel — one compliance engine, configurable for any regulator.

- **FINRA Rule 3110:** AI systems must be supervised like humans. Every agent decision requires an audit trail — not a log, but a chain of accountability.
- **FDA 21 CFR Part 11:** Quality gates function as validation evidence. A 15-gate quality pass is a validation protocol artifact in regulated contexts.
- **The HITL Requirement:** No automated system can make a release decision alone. Documented human sign-off required.
- **3-Tier Accountability Framework** (introduced at the testing conference, November 2024):
  - Tier 1: The Agent Execution Layer — what the AI did
  - Tier 2: The Human Oversight Layer — what the engineer approved
  - Tier 3: The Organisational Accountability Layer — what leadership is responsible for

#### The Two-Person Crew in Regulated Industries

The Q2 Release two-person crew model applies directly here:
- **The Engineer** configures the Tier 4 engine. Sets the quality gates, defines the compliance profiles, manages the agent execution.
- **The Fireman** — the compliance officer — **certifies it meets the standard before it moves.**

In regulated industries, this isn't a product metaphor. **It's a legal requirement.**

#### Core Capabilities

**Compliance Mode** — Not a standalone product from day one, but a compliance mode activating on top of Quality Guardian. When active: every agent action written to immutable audit log, every quality gate pass/fail recorded with timestamp + agent ID + human reviewer, every release decision requires HITL sign-off.

**Regulatory Configuration Layer** — Select applicable frameworks (FINRA, SEC 17a-4, SEC 613/CAT, IRC §1091, FDA 21 CFR Part 11, WCAG 2.2 AA, HIPAA, SOC 2, DEA). Configure domain-specific controls (e.g., T+1 settlement windows). Generate framework-specific evidence packages.

**Certificate of Conformity** — Every quality gate pass generates an immutable, signed record. This is not a report — it is an artifact a regulator can examine.

**Positive Train Control Layer** — HITL enforcement between automated quality gate passage and deployment authorisation. Neither the engineer nor the compliance officer can be bypassed in Compliance Mode.

**Audit Trail Architecture** — Append-only event log. Cryptographic integrity verification (tampering detectable). Temporal query capability (reconstruct compliance state at any point in time). Regulatory export formats per regulatory body.

#### Pricing

| Tier | Name | Capability |
|---|---|---|
| Tier 1 — Read | Compliance Viewer | View audit logs, compliance status, certificate history |
| Tier 2 — Aggregate | Compliance Monitor | Real-time compliance dashboard, alert configuration, report generation |
| Tier 3 — Author | Compliance OS | Full regulatory configuration, Certificate of Conformity generation, HITL enforcement, immutable audit architecture |

*Note: Tier 3 requires Quality Guardian Team or Enterprise licence as foundation.*

#### Target Customer

Financial services, pharma and life sciences, healthcare, deposit systems, brokerage platforms, trading systems — any regulated industry where the question is: *"Can we prove software quality to a regulator?"*

The entry conversation: **"You have AI agents writing code. Your regulator is going to ask how you supervise them. We have the answer."**

#### Workshop & Consulting Connection

The 3-tier accountability framework introduced at the November 2024 testing conference — which received shock from the room — is the content foundation for Tier 4's go-to-market. The "AI Compliance in Regulated Industries: What Your Agentic Coding Tools Don't Know Yet" workshop ($10,000/day) is the direct top-of-funnel. Workshop participants become the first Tier 4 closed beta customers.

#### Taglines

- *"Tier 4 locomotives produce 90% less pollutant. Your releases should too."*
- *"Certificate of conformity. Every run."*

---

### The Turntable Hub — Central Launcher

*Dispatch your tools from the roundhouse.*

In real railroad yards, the turntable sits at the centre of a roundhouse and rotates to align with different tracks — dispatching locomotives in any direction. In FlowTrain, the turntable is the launcher. Each track leads to a different tool. Select a tool, watch the turntable rotate, and your engine rolls out. This is not a dashboard. This is a **dispatch event** — a moment of commitment with mechanical weight and satisfaction behind it.

#### Why the Turntable Works

- **Memorable:** Trains are visceral, mechanical, iconic. Users remember choosing a locomotive, not clicking a menu item. Early adopters remember when there were only two tracks — that's retention storytelling built into the UI.
- **Scalable:** New tool? New train. Add a track to the roundhouse. The metaphor never runs out of room.
- **Narratable:** Every tool has a backstory — a real locomotive with real engineering history. Built-in marketing copy baked into the product. The research process of finding the perfect locomotive analogy becomes part of the product development ritual.
- **Distinctive:** No other software company navigates like this. Instantly recognisable and unreplicable without wholesale adoption of the metaphor.

#### Track Assignments

| Track | Locomotive | Tool | Status |
|---|---|---|---|
| Track 1 | EMD SD70ACe | StructureView | Shipped |
| Track 2 | UP 844 | Quality Guardian | In development |
| Track 3 | PRR Q2 | Q2 Release | Planned |
| Track 4 | Metrolink Tier 4 | Tier 4 Compliance | Planned |
| Track 5+ | TBD | Future Tools | Expandable |

#### Turntable States

| State | Description |
|---|---|
| Idle | Turntable centred, all locomotives visible at their tracks |
| Selecting | User hovering a track — locomotive at that track illuminates, subtle steam effect |
| Rotating | Turntable bridge swinging to alignment — weighted mechanical motion |
| Locked | Bridge aligned, locomotive ready — brief settle animation |
| Dispatched | Locomotive rolls forward, tool launches, turntable returns to idle |

#### The Animation

The turntable rotation is the product's signature interaction. It must be engineered, not designed.

**What it should feel like:** Mechanical and satisfying — gears turning, bridge swinging, deliberate. Conveying weight and momentum. The moment of commitment. Think: a real turntable with mass rotating on a pivot, decelerating into position.

**What it must NOT feel like:**
- A CSS spinner
- A snappy page transition
- A loading indicator
- Anything that says "app" instead of "yard"

**Five animation beats:**
1. User selects a tool (clicks a track or locomotive)
2. Turntable bridge begins to rotate — weighted easing, not linear
3. Bridge locks into alignment with selected track — slight mechanical settle
4. Locomotive rolls forward along the bridge — weight and momentum in the motion
5. Tool launches — the locomotive has departed

> **Do not ship the turntable hub with a CSS spinner pretending to be a turntable. The animation is the product.**

**Implementation sequencing:**
1. Static hub with clickable tracks — validates the metaphor and navigation
2. Basic rotation animation — establishes the paradigm
3. Full weighted mechanical animation — the signature version, launches with Q2 Release or enterprise bundle
4. Locomotive dispatch animation — the complete experience

#### Visual Language

- **Active/shipped tools:** Full colour locomotive, illuminated track
- **In-development tools:** Desaturated locomotive, dimmed track, subtle "under construction" indicator
- **Planned/future slots:** Empty track with ghost placeholder — visible but not actionable

Hub brand colours: `#0a0a0f` deep background (the night yard), `#12121a` roundhouse structure, `#2BAEE4` active track illumination, `#F0C050` gold accent and "steam" particle effects, `#D44030` steam red for warnings and unavailable tools.

#### Expansion Model

The turntable hub is architecturally infinite. Tool taxonomy by locomotive class:

- **Freight locomotives** → developer tools (heavy lifting, precision, load-bearing)
- **Steam locomotives** → legacy/heritage tool integrations
- **Tier 4 / modern** → compliance and governance tools
- **Passenger locomotives** → [PLACEHOLDER — user-facing, experience tools]

**Special editions:**
- "Night Express" dark mode livery — seasonal or premium
- "Heritage" retro UI treatment for anniversary events
- Limited-run locomotive liveries for conference appearances

#### Community & Lore

Each tool's "About" page tells the story of its locomotive namesake. Users learn actual railroad engineering while using developer tools. This is brand depth that cannot be manufactured. The research process — finding the perfect locomotive analogy for each new tool — becomes part of the product development ritual. It is brand-building baked into the roadmap.

*"Add a train. Add a track. The yard never fills up."*

#### Core Taglines

- *"Your code rides the rails."*
- *"Every tool, its own engine."*
- *"Dispatch quality from the roundhouse."*
- *"Full steam ahead on clean code."*
- *"Switch tracks. Switch tools."*

#### Railroad Vocabulary Reference

| Railroad Term | FlowTrain Meaning |
|---|---|
| Dispatch | Launch a tool |
| Haul | Process / handle |
| Consist | Tool combination / suite |
| Coupling | Integration / connection |
| Mainline | Primary workflow |
| Switching | Changing tools |
| Siding | Staging / secondary workflow |
| Full steam | Maximum effort / speed |
| On track | On schedule / correct |
| Roundhouse | Tool hub / dashboard |
| Gauge | Metrics / measurement |
| Terminal | Endpoint / completion |
---

## Appendix A: Full Mapping Matrix

| TQM Principle | Lifecycle Stage | QG Feature | Agent | Skill |
|---|---|---|---|---|
| Customer Focus | Idea Generation | Customer insights dashboard | Discovery Agent | discovery-to-delivery |
| Customer Focus | Market Analysis | Market signal analysis | Discovery Agent | quality-dashboard-builder |
| Customer Focus | Launch | Customer satisfaction tracking | Analytics Agent | quality-dashboard-builder |
| Employee Involvement | Design & Dev | Cross-functional quality scorecards | Collaboration Agent | quality-dashboard-builder |
| Employee Involvement | Testing | Collaborative BDD workshops | Quality at Source Agent | bdd-scenario-generator |
| Process-Centered | Design & Dev | CI/CD quality gates | Pipeline Agent | test-plan-composer |
| Process-Centered | Production | Automated deployment validation | Pipeline Agent | compliance-artifact-builder |
| Integrated System | All Stages | Unified traceability matrix | TIMC Core | traceability-mapper |
| Integrated System | Testing | 4-quadrant test management | TIMC Core | test-plan-composer |
| Strategic Approach | Launch | Stage-gate progression | Release Agent | compliance-artifact-builder |
| Strategic Approach | Monitoring | DORA metrics tracking | Release Agent | quality-dashboard-builder |
| Continuous Improvement | Monitoring | Anomaly detection | CI Agent | quality-dashboard-builder |
| Continuous Improvement | Iteration | AI-driven recommendations | CI Agent | discovery-to-delivery |
| Fact-Based Decisions | Market Analysis | Data-driven quality assessments | Analytics Agent | quality-dashboard-builder |
| Fact-Based Decisions | Testing | Coverage analytics | Analytics Agent | test-plan-composer |
| Communication | All Stages | Living documentation | Documentation Agent | compliance-artifact-builder |
| Communication | Launch | Stakeholder reports | Documentation Agent | quality-dashboard-builder |

---

## Appendix B: shadcn/ui Token Mapping

Complete CSS variable mapping for FlowTrain brand in both light and dark mode.

### Light Mode Tokens

| Token | CSS Variable | HSL Value | Hex Equivalent | Usage |
|---|---|---|---|---|
| Background | --background | 0 0% 100% | #FFFFFF | Page and card backgrounds |
| Foreground | --foreground | 0 3% 12% | #231F20 | Primary text |
| Primary | --primary | 196 76% 53% | #2BAEE4 | CTAs, links, active nav items |
| Primary Foreground | --primary-foreground | 0 0% 100% | #FFFFFF | Text on primary backgrounds |
| Secondary | --secondary | 196 76% 95% | #E8F6FD | Secondary buttons, hover states |
| Secondary Foreground | --secondary-foreground | 0 3% 12% | #231F20 | Text on secondary backgrounds |
| Muted | --muted | 210 10% 96% | #F5F5F7 | Disabled states, subtle backgrounds |
| Muted Foreground | --muted-foreground | 0 0% 45% | #737373 | Placeholder text, captions |
| Accent | --accent | 196 76% 93% | #D0EEFC | Hover highlights, table alt rows |
| Accent Foreground | --accent-foreground | 200 30% 16% | #1A3A4F | Text on accent backgrounds |
| Destructive | --destructive | 0 84% 60% | #EF4444 | Error states, delete actions |
| Border | --border | 0 0% 80% | #CCCCCC | Card borders, dividers |
| Input | --input | 0 0% 80% | #CCCCCC | Input field borders |
| Ring | --ring | 196 76% 53% | #2BAEE4 | Focus rings |
| Chart 1 | --chart-1 | 196 76% 53% | #2BAEE4 | Primary data series |
| Chart 2 | --chart-2 | 180 60% 40% | #29A399 | Secondary data series |
| Chart 3 | --chart-3 | 210 50% 35% | #2D5A8E | Tertiary data series |
| Chart 4 | --chart-4 | 35 90% 55% | #E8A230 | Quaternary data series |
| Chart 5 | --chart-5 | 340 60% 55% | #CC4477 | Quinary data series |

### Dark Mode Tokens

| Token | CSS Variable | HSL Value | Hex Equivalent | Usage |
|---|---|---|---|---|
| Background | --background | 0 3% 12% | #231F20 | Page background (FlowTrain Black) |
| Foreground | --foreground | 0 0% 95% | #F2F2F2 | Primary text |
| Primary | --primary | 196 76% 53% | #2BAEE4 | CTAs, links (unchanged) |
| Primary Foreground | --primary-foreground | 0 3% 12% | #231F20 | Text on primary backgrounds |
| Secondary | --secondary | 200 20% 18% | #253742 | Secondary surfaces |
| Secondary Foreground | --secondary-foreground | 0 0% 90% | #E6E6E6 | Text on secondary surfaces |
| Muted | --muted | 0 2% 18% | #2E2C2C | Disabled states, subtle surfaces |
| Muted Foreground | --muted-foreground | 0 0% 55% | #8C8C8C | Placeholder text |
| Accent | --accent | 200 30% 16% | #1A3A4F | Hover highlights |
| Accent Foreground | --accent-foreground | 196 76% 75% | #7ECEF0 | Text on accent backgrounds |
| Destructive | --destructive | 0 72% 51% | #DC2626 | Error states |
| Border | --border | 0 2% 25% | #3F3D3D | Card borders |
| Input | --input | 0 2% 25% | #3F3D3D | Input borders |
| Ring | --ring | 196 76% 53% | #2BAEE4 | Focus rings |
| Chart 1–5 | (same hues, +15% lightness) | Adjusted for dark backgrounds | Brighter variants | Enhanced contrast on dark surfaces |

### Fleet-Wide Token Extensions

| Token Name | CSS Variable | Hex Value | HSL Value | Usage |
|---|---|---|---|---|
| Gold | --fleet-gold | #F0C050 | 43 84% 63% | Syntax accents, JSON key highlighting, steam particle effects |
| Steam Red | --fleet-steam-red | #D44030 | 8 64% 51% | Warnings, alerts, unavailable states |
| Deep Background | --fleet-deep-bg | #0a0a0f | 240 25% 6% | Fleet dark mode base — primary background for all dark-theme products |
| Roundhouse Surface | --fleet-roundhouse | #12121a | 240 20% 9% | Elevated dark surfaces: cards, sidebars, nav drawers over Deep Background |

### Sidebar Tokens

| Token | Light Mode | Dark Mode | Usage |
|---|---|---|---|
| --sidebar-background | #FAFAFA | #1A1A1A | Sidebar container background |
| --sidebar-foreground | #231F20 | #E6E6E6 | Sidebar text |
| --sidebar-primary | #2BAEE4 | #2BAEE4 | Active nav item, selected state |
| --sidebar-primary-foreground | #FFFFFF | #231F20 | Text on active nav items |
| --sidebar-accent | #E8F6FD | #1A3A4F | Hover state background |
| --sidebar-accent-foreground | #231F20 | #7ECEF0 | Hover state text |
| --sidebar-border | #E5E5E5 | #333333 | Sidebar section dividers |
| --sidebar-ring | #2BAEE4 | #2BAEE4 | Focus rings in sidebar |

### Radius Scale

| Token | Value | Usage |
|---|---|---|
| --radius | 0.5rem | Base border radius for cards, buttons, inputs |
| --radius-sm | calc(var(--radius) - 4px) | Small elements (badges, tags) |
| --radius-md | calc(var(--radius) - 2px) | Medium elements (input fields) |
| --radius-lg | var(--radius) | Large elements (cards, dialogs) |
| --radius-xl | calc(var(--radius) + 4px) | Extra large elements (hero cards) |

---

## Appendix C: Architecture & Technology Glossary

This glossary covers every technology and design pattern named in the Quality Guardian architecture. It is intended for both non-technical readers (what does this do?) and technical readers (how does it work, where does it run, what are the trade-offs?). Columns: **Plain-English Purpose · Technical Description · Cloud Affinity · Managed Equivalents · Licence**.

> **Cloud key:** ✅ = natively available as managed service. ⚠️ = available but not native. ❌ = not available.

---

### Runtime, Language, and Schema

| Tool | Plain-English Purpose | Technical Description | Cloud Affinity | Managed Equivalents | Licence |
|---|---|---|---|---|---|
| **Node.js 22+ LTS** | The engine that runs the server-side code — JavaScript outside the browser. | Open-source, cross-platform JS runtime on Chrome's V8 engine. v22 entered Active LTS Oct 2024 ("Jod"). Features built-in WebSocket client, stable Watch Mode, native ESM `require()`, native TypeScript type-stripping (v22.18.0+). Node 24 is now current Active LTS. | Cloud-agnostic | AWS Lambda ✅, Azure Functions ✅, GCP Cloud Functions ✅ | MIT |
| **TypeScript 5.5+** | JavaScript with a spell-checker for code — catches bugs before they run. | Statically-typed JS superset by Microsoft. v5.5 (Jun 2024): inferred type predicates, `isolatedDeclarations`, regex syntax checking, 33% smaller package. Current stable: 5.9. TS 7.0 (Go-based rewrite, ~10× faster builds) announced Mar 2025. | Cloud-agnostic | Supported via Node.js runtimes on all clouds | Apache 2.0 |
| **Zod** | A data bouncer — only lets correctly shaped data through. | TypeScript-first schema declaration and validation with automatic static type inference via `z.infer<>`. v4.0.0 released Jul 2025 with `z.xor()`, `z.fromJSONSchema()`, Standard Schema compliance. Zero runtime dependencies. | Cloud-agnostic | No cloud equivalent (application-level library) | MIT |

---

### Agent Orchestration

| Tool | Plain-English Purpose | Technical Description | Cloud Affinity | Managed Equivalents | Licence |
|---|---|---|---|---|---|
| **LangGraph.js** | A flowchart engine for AI agents — defines sequences, loops, human approval points, and state persistence. | JS/TS library for stateful, multi-actor agent workflows modelled as directed graphs. Nodes = functions (LLM calls, tool invocations, logic); edges = control flow (static, conditional, Command-based). State managed via `Annotation` schemas. Supports cycles, checkpointing, human-in-the-loop, streaming, supervisor/swarm patterns. | Cloud-agnostic. LangGraph Platform (proprietary) provides managed deployment. | No native AWS/Azure/GCP equivalent. AWS Step Functions and Azure Durable Functions are workflow tools but lack LLM agent primitives. | MIT (core). Platform is proprietary. |
| **Mastra** | An all-in-one TypeScript toolkit for building AI agents — created by the Gatsby.js team. Covers workflows, memory, RAG, and evals. | TypeScript-native agent framework built on Vercel AI SDK. Declarative Agent, Workflow (graph-based state machines with suspend/resume), RAG pipeline, Memory, and Eval primitives. Model routing supports 40+ providers via unified `"provider/model-name"` syntax. MCP server authoring, Langfuse observability integration. YC W25, 10K+ GitHub stars. | Cloud-agnostic + Mastra Cloud (managed) | No native AWS/Azure/GCP equivalent | Apache 2.0 (core). Enterprise features under Mastra Enterprise Licence. |

---

### Model Communication SDKs

| Tool | Plain-English Purpose | Technical Description | Cloud Affinity | Licence |
|---|---|---|---|---|
| **Vercel AI SDK v5** | A universal translator for AI models — write code once and it works with OpenAI, Anthropic, Google, and dozens of others. 20M+ monthly npm downloads. | Unified TS API for LLM interaction: `generateText`, `streamText`, `generateObject`, `streamObject`. UI hooks: `useChat`, `useCompletion`. **v5 released Jul 31, 2025** (typed UIMessage/ModelMessage, SSE streaming, agentic loop control). v6 beta adds Agent abstraction and DevTools. | Cloud-agnostic (Vercel-optimised) | Apache 2.0 |
| **Anthropic SDK** (`@anthropic-ai/sdk`) | Anthropic's official library for calling Claude models. Handles auth, streaming, errors, and retries. v0.82.0, 12M+ weekly downloads. | Typed `Anthropic` client with `messages.create()`, full SSE streaming, error hierarchy, tool use, vision, extended thinking. Runs on Node 18+, Deno, Bun, Workers. Companion packages: `@anthropic-ai/bedrock-sdk` (AWS Bedrock ✅), `@anthropic-ai/vertex-sdk` (GCP Vertex ✅). | Claude available on AWS Bedrock ✅, Azure AI Foundry ✅, GCP Vertex AI ✅ | MIT |
| **@ai-sdk/anthropic** | A plug-in connecting Vercel AI SDK to Claude models — swap providers with one line. | Provider package implementing AI SDK Language Model Spec. `anthropic()` factory with extended thinking, effort levels, speed modes, prompt caching. v3.0.x. | Cloud-agnostic | Apache 2.0 |
| **@ai-sdk/openai** | A plug-in connecting Vercel AI SDK to OpenAI GPT models and any OpenAI-compatible endpoint. | Provider package for OpenAI Chat Completions and Responses APIs. Supports structured output, tool use with streaming, embeddings. | Cloud-agnostic | Apache 2.0 |
| **@ai-sdk/google** | A plug-in connecting Vercel AI SDK to Google's Gemini models. Separate `@ai-sdk/google-vertex` for GCP-native deployment. | Provider package for Google Generative AI API. Maps grounding (Gemini 2.0+), Vertex RAG Store, file search (Gemini 2.5+). | GCP-native via Vertex package | Apache 2.0 |

---

### AI Models Referenced

> ⚠️ **Important model name updates:** "Gemini 3 Pro" was shut down March 2026 and replaced by **Gemini 3.1 Pro**. "Gemini Flash 3.0" is officially **Gemini 3 Flash** (released December 2025). Gemini Flash 2.0 is deprecating June 2026. All references in this document use current identifiers.

| Model | Plain-English Purpose | Key Technical Facts | Cloud Availability | Licence |
|---|---|---|---|---|
| **Claude Opus 4.5** | Anthropic's most powerful model at release — for complex coding, research, and multi-step projects. | 200K context (1M beta). 64K max output. SWE-bench 80.9%. $5/$25 per M tokens. Released Nov 2025. Succeeded by Opus 4.6 (Feb 2026). | Anthropic API, AWS Bedrock ✅, Azure AI Foundry ✅, GCP Vertex AI ✅ | Proprietary |
| **Claude Sonnet 4.5** | Best balance of power and cost. "Best coding model in the world" at release. | 200K context (1M beta). 64K max output. SWE-bench 77.2%. $3/$15 per M tokens. Released Sep 2025. ASL-3 safety classification. | Anthropic API, AWS Bedrock ✅, Azure AI Foundry ✅, GCP Vertex AI ✅ | Proprietary |
| **Gemini 3.1 Pro** | Google's most capable model — text, images, code, audio, video with advanced reasoning. (Previously listed as "Gemini 3 Pro" in earlier brief versions.) | MoE architecture. 1M context, 65K max output. GCP Vertex AI only. | GCP Vertex AI ✅ only. Not on AWS ❌ or Azure ❌. | Proprietary |
| **Gemini 3 Flash** | Google's fast, everyday workhorse model — near-Pro intelligence at low cost. (Previously "Gemini Flash 3.0".) | 1M context. ~65K output. $0.50/$3.00 per M tokens. Released Dec 2025. | GCP Vertex AI ✅ only | Proprietary |
| **GPT-4o** | OpenAI's multimodal model — processes text, images, and audio in one model. "o" = omni. | 128K context, 16K max output. MMLU 88.7%. $2.50/$10 per M tokens. Available via API. | OpenAI API, Azure OpenAI ✅. Not on AWS Bedrock ❌ or GCP Vertex ❌. | Proprietary |
| **Phi-4** | Microsoft's small-but-mighty model — beats larger models on math and science reasoning. Runs on modest hardware. | 14B parameters. 16K context. MIT licence (open weights). Variants: mini, multimodal, reasoning, reasoning-plus. | Azure AI Foundry ✅ (native). Also Hugging Face, Ollama (self-hostable anywhere). | **MIT** (open weights) |
| **Qwen3-1.7B** | A compact model from Alibaba for phones and modest hardware — switches between fast response and deep thinking modes. | 1.7B parameters. 32K context. Dual-mode inference. 36T training tokens, 119 languages. Released Apr 2025. | Cloud-agnostic (self-hostable). Hugging Face, Ollama, Alibaba DashScope. | **Apache 2.0** (open weights) |
| **bge-large-en-v1.5** | Converts text into numbers that capture meaning — for semantic search. Does not generate text. | 335M parameters (BERT-family). 1024-dim embeddings. 512 token max. MTEB score 64.23. Succeeded by BGE-M3 (multilingual, 8K tokens). | Cloud-agnostic. Cloudflare Workers AI. Self-hostable anywhere. | **MIT** (open weights) |

---

### Memory and Storage

| Tool | Plain-English Purpose | Technical Description | Cloud Affinity | Managed Equivalents | Licence |
|---|---|---|---|---|---|
| **LangGraph PostgresSaver** | An "auto-save" for AI agents — snapshots every step in PostgreSQL so agents can resume exactly where they left off. | PostgreSQL-backed `BaseCheckpointSaver` for LangGraph. Serialises full graph state into PG tables at every superstep using Psycopg 3. Sync + async modes, connection pooling, cursor pagination. v3.0.5. | Cloud-agnostic (any PostgreSQL) | AWS RDS/Aurora ✅, Azure DB for PostgreSQL ✅, GCP Cloud SQL ✅, Neon, Supabase | MIT |
| **Mem0** | An intelligent memory layer that extracts and stores important facts from AI conversations — the AI remembers users across sessions. ⚠️ Not the same as MemGPT/Letta. | Hybrid datastore: vector stores (19 backends) + graph stores (Neo4j, Neptune) + KV stores. LLM-powered extraction pipeline deduplicates memories. 186M+ API calls processed by Q3 2025. Official memory provider for AWS Agent SDK. YC-backed, $24M raised. | Cloud-agnostic + Mem0 Cloud (managed SaaS) | No native AWS/Azure/GCP equivalent. AWS Agent SDK integration. | Apache 2.0 (core). Cloud is commercial. |
| **MongoDB Atlas** | A globally distributed document database with built-in vector search — the recommended primary store for new Quality Guardian deployments. Runs across AWS, Azure, and GCP simultaneously. | Multi-cloud document database. HNSW-based vector search supporting up to 8,192 dimensions, cosine/euclidean/dot-product, scalar and binary quantisation. Full MQL aggregation pipeline, multi-document ACID transactions, Change Streams. True multi-cloud replica sets (nodes distributed across AWS, Azure, GCP) with 10–30 second failover. $1.43B annual Atlas revenue, 54,500+ customers. | **AWS ✅, Azure ✅, GCP ✅** — genuine multi-cloud failover | No direct equivalent at this capability level | **Proprietary** (MongoDB Inc.) / Community Edition is SSPL |
| **Azure Cosmos DB (DiskANN)** | Microsoft's globally distributed database with an SSD-optimised vector search algorithm. Azure-native; valid choice for Azure-primary architectures. | Multi-model DB with DiskANN vector indexing. SSD-optimised graph-based ANN search. <20ms query latency over 10M vectors. Supports up to 4,096 dims (NoSQL) / 16,000 dims (vCore + PQ). **Azure-only** — no multi-cloud failover. 99.999% SLA for multi-region writes within Azure. | **Azure only ✅**. AWS ❌, GCP ❌. | AWS: DynamoDB + OpenSearch. GCP: Spanner + Vertex AI Vector Search. | **Proprietary** (Azure service). DiskANN library is MIT. |
| **Qdrant** | A purpose-built vector search engine — finds items by meaning rather than keywords. Written in Rust for high performance. | HNSW-based ANN with filterable metadata. Dense + sparse vectors, hybrid search, rich JSON payload filtering, scalar/product/binary quantisation. Qdrant Edge (beta Jul 2025) for embedded deployment. 25K+ GitHub stars. | Cloud-agnostic. Qdrant Cloud on AWS ✅, Azure ✅, GCP ✅. | AWS: OpenSearch. Azure: AI Search. GCP: Vertex AI Vector Search. | Apache 2.0 |
| **LanceDB** | An embedded AI database storing text, images, and their embeddings together — runs inside the app with no server needed at development scale. | Serverless/embedded vector DB on Lance columnar format. Rust core on Apache Arrow. IVF-PQ, IVF-Flat, HNSW-PQ indexes. BM25 full-text search. Git-like data versioning. 200M+ vector scale. | Cloud-agnostic (S3, GCS, Azure Blob backends) | LanceDB Cloud and Enterprise (commercial). YC-backed, $30M Series A. | Apache 2.0 (OSS). Cloud/Enterprise commercial. |
| **pgvector** | An add-on for PostgreSQL that stores and searches AI embeddings — no separate vector database needed. | PostgreSQL extension: `vector` type (up to 16K dims for HNSW), `halfvec`, `sparsevec`, `bit`. HNSW + IVFFlat indexes. L2, cosine, inner product distances. Full ACID, JOINs, transactions. v0.8.2. | Cloud-agnostic. Pre-installed on most managed PG services. | AWS RDS/Aurora PG ✅, Azure DB for PG ✅, GCP Cloud SQL/AlloyDB ✅. De facto standard. | PostgreSQL Licence (permissive) |
| **SQLite FTS5** | A built-in keyword search engine for SQLite — finds documents by text without a separate search server. | Virtual table module with inverted index, BM25 ranking, AND/OR/NOT/NEAR queries, phrase search. Pre-installed in most SQLite builds. Used in Quality Guardian for hybrid memory search (BM25 30% weight). | Cloud-agnostic (embedded, runs everywhere) | AWS: OpenSearch. Azure: AI Search. GCP: Vertex AI Search. None are equivalent — FTS5 is uniquely local-first. | Public domain |

#### MongoDB Atlas vs Azure Cosmos DB — Decision Summary

The single biggest architecture portability question is the database layer. The summary:

| Criterion | MongoDB Atlas | Azure Cosmos DB (DiskANN) |
|---|---|---|
| Multi-cloud failover | ✅ AWS + Azure + GCP simultaneously | ❌ Azure only |
| Vector search algorithm | HNSW (industry standard) | DiskANN (SSD-optimised, Microsoft Research) |
| Max vector dimensions | 8,192 | 4,096 (NoSQL) / 16,000 (vCore + PQ) |
| Document size limit | 16 MB | 2 MB |
| Aggregation capability | Full MQL pipeline (GROUP BY, $lookup, $graphLookup) | Limited SQL-like; no native GROUP BY |
| Change capture | Change Streams — captures inserts, updates, AND deletes | Change Feed — inserts and updates only (no native deletes) |
| Enterprise procurement (AWS/GCP shops) | Available on AWS Marketplace and GCP Marketplace | Azure subscription required |
| Multi-region write SLA | 99.995% | 99.999% (within Azure) |
| Failover time | ~30 seconds (replica election) | <15 minutes for regional; ~0 for node failures |

**Recommendation:** Use MongoDB Atlas for new deployments where multi-cloud portability or AWS/GCP-primary procurement is a requirement. Retain Cosmos DB for Azure-native architectures where DiskANN's extreme-scale memory efficiency is needed (datasets >10M vectors) and cross-cloud failover is not required.

---

### Prompt Optimisation, Gateway, and Observability

| Tool | Plain-English Purpose | Technical Description | Cloud Affinity | Licence |
|---|---|---|---|---|
| **Ax Framework** (`@ax-llm/ax`) | Instead of writing prompts by hand, describe what goes in and comes out — Ax finds the best prompt automatically. The TypeScript version of Stanford's DSPy. | TS framework implementing DSPy concepts. Core abstraction: signatures (typed I/O declarations compiled into optimised prompts). Supports MIPROv2, ACE, GEPA optimisers. ReAct agent loops, RAG, multi-modal. 15+ LLM providers. OpenTelemetry tracing. Zero runtime deps. | Cloud-agnostic. AWS Bedrock provider via `@ax-llm/ax-ai-aws-bedrock`. | MIT |
| **MIPROv2** | An automatic prompt-improvement system — uses Bayesian search to find the best combination of instructions and examples. Part of DSPy. | DSPy's primary optimiser. Three phases: bootstrap (collect high-scoring traces), grounded proposal (LLM-generated instruction candidates), Bayesian search (Optuna TPE over instruction × demo-set combinations). Available in Python (DSPy) and TypeScript (Ax `AxMiPRO`). | Cloud-agnostic | MIT (part of DSPy) |
| **GEPA** | A smarter prompt optimiser that reads full reasoning traces, diagnoses failures, and rewrites prompts. Prompts are 9.2× shorter than MIPROv2 outputs. Accepted as Oral at ICLR 2026. | Reflective evolutionary optimiser. Captures execution traces, uses LLM to diagnose failures, mutates prompts with accumulated lessons. Pareto frontier selection prevents local optima. Outperforms MIPROv2 by 10%+. Integrated into MLflow, Comet Opik, Google ADK. | Cloud-agnostic | MIT |
| **LiteLLM Proxy** | A universal traffic controller for AI models — one format for 100+ providers, with cost tracking, key management, load balancing, and fallbacks. 33K+ GitHub stars. | Self-hosted OpenAI-compatible API gateway (Python). Virtual key management with budget tracking, load balancing, rate limiting, caching, guardrails. Architecture: proxy + PostgreSQL + Redis. Available on AWS Marketplace. | Cloud-agnostic (self-hosted) | MIT (core). Enterprise licence for SSO/SCIM/RBAC. |
| **Langfuse** | A monitoring dashboard for AI apps — records every interaction, tracks cost/latency/quality, manages prompt versions, and enables debugging. 24K+ GitHub stars. Acquired by ClickHouse 2025/2026. | Open-source LLM engineering platform: tracing (hierarchical spans), prompt management (versioning, A/B), evaluations (LLM-as-judge, user feedback), datasets, metrics dashboards. Architecture: Web + Worker + PostgreSQL + ClickHouse + Redis + S3. Integrates with Vercel AI SDK, LiteLLM, Mastra. | Cloud-agnostic (self-host via Docker/K8s) + Langfuse Cloud (SaaS) | MIT |

---

### UI Framework and Testing

| Tool | Plain-English Purpose | Technical Description | Cloud Affinity | Licence |
|---|---|---|---|---|
| **Next.js 15** | A framework for building websites using React — handles server rendering, code splitting, and routing. | Full-stack React meta-framework by Vercel. App Router with React Server Components. v15 (Oct 2024): Turbopack Dev stable, React 19, async request APIs. Next.js 16 (Oct 2025) adds Deployment Adapters API for non-Vercel platforms. | Cloud-agnostic (Vercel-optimised) | MIT |
| **shadcn/ui** | Beautiful, ready-to-use interface components you copy into your project and own entirely — like professional blueprints you can freely modify. | Component distribution platform (not npm package). Copy-paste React components on Radix UI + Tailwind CSS via CLI. Supports Tailwind v4, React 19, dark mode. Now supports Base UI alongside Radix. | Cloud-agnostic | MIT |
| **Radix UI** | The invisible behaviour layer for UI components — accessibility, keyboard navigation, and interactions without dictating visual style. | Unstyled, headless React component library. WAI-ARIA compliant. 30+ primitives: Dialog, Popover, Select, Tabs, Tooltip, etc. Maintained by WorkOS. Unified `radix-ui` package (Jun 2025). | Cloud-agnostic | MIT |
| **Tailwind CSS** | A styling toolkit using small utility classes directly in HTML — faster to build, smaller production bundles. | Utility-first CSS framework. v4 (early 2025): ground-up rewrite as standalone CSS tool (no config file), CSS layers, `oklch` colours, container queries. 93K+ GitHub stars. | Cloud-agnostic | MIT |
| **Vitest** | A fast testing tool for JS/TS — shares the same build engine as the app, so tests reuse existing configuration. | Vite-native unit/integration test framework with Jest-compatible API. Native ESM, TS/JSX, snapshot testing, coverage (v8/istanbul), browser mode (Playwright), concurrent execution. v4.1.2. Backbone of Storybook 9's component testing. | Cloud-agnostic | MIT |
| **Playwright** | Automates web browsers — clicks buttons, fills forms, navigates pages like a real user across Chrome, Firefox, and Safari. Maintained by Microsoft. | Cross-browser E2E testing. Chromium, Firefox, WebKit. Auto-waiting, Trace Viewer, codegen, parallel execution, network interception, API testing. v1.58.0. | Cloud-agnostic | **Azure: Microsoft Playwright Testing ✅** (managed cloud). No AWS/GCP native equivalent. | Apache 2.0 |
| **Storybook** | A workshop for building and testing UI components in isolation — shows each component in various states. | Component development tool. v9 (Jun 2025): deep Vitest integration, built-in component testing, test widget, 48% leaner core, Vite-powered. Chromatic for visual testing. | Cloud-agnostic | MIT |
| **axe-core** | The engine behind most automated accessibility testing — scans pages for WCAG problems. 3B+ downloads. Powers Lighthouse a11y audits. | JS accessibility engine by Deque. Evaluates DOM against WCAG 2.0/2.1/2.2 (A/AA/AAA). Zero false positives guarantee. Used in Storybook a11y addon. | Cloud-agnostic | MPL-2.0 |
| **Lighthouse** | Google's free website grader — scores performance, accessibility, SEO, and best practices. | Automated auditing tool (Google). Measures Core Web Vitals (LCP, CLS, INP). A11y audits powered by axe-core. v13 (Oct 2025) restructured into "Insights" + "Diagnostics." CLI, Node.js, Chrome DevTools, PageSpeed Insights. | GCP-associated but tool is cloud-agnostic | Apache 2.0 |

---

### Design Patterns and Architectures

| Pattern | Plain-English Purpose | Technical Description | Open Source? |
|---|---|---|---|
| **CoALA** | A blueprint for thinking about how AI agents should be built — every agent needs memory, actions, and a decision-making loop. A design reference, not software. | Conceptual taxonomy (Sumers, Yao et al., Princeton, 2023) mapping agents onto cognitive architectures. Three dimensions: memory (working + long-term), action space (internal + external), decision procedure (retrieve → reason → plan → act). Unifies 300+ agent works under one framework. Published TMLR 2024. | Academic/open-access |
| **Mixture of Agents (MoA)** | Multiple AI models work in layers — each round, models read prior answers and refine them. Achieves 65.1% on AlpacaEval 2.0 using only open-source models vs. GPT-4o's 57.5%. | Layered multi-agent inference (Wang et al., Together AI, 2024; ICLR 2025). N proposer agents per layer; aggregator agents refine using all prior outputs. Heterogeneous models outperform homogeneous ones. Best for offline/batch quality maximisation. | Apache 2.0 |
| **Blackboard Pattern** | Experts around a shared whiteboard — each watches and contributes when they spot something relevant. Multi-agent coordination without tight coupling. | Classic AI pattern (Hearsay-II, 1980). Three components: shared data store (blackboard), specialised knowledge sources (agents), control component (scheduler). Modern LLM adaptations show 13–57% improvement over master-slave baselines. | Public domain pattern |
| **OpenClaw** | A local-first AI agent gateway connected to all messaging apps (WhatsApp, Telegram, Slack, etc.) — 247K+ GitHub stars, fastest-growing repo in 2025/26. Validates the agent construction sequence used in this architecture. | Local-first AI agent gateway (Node.js). Gateway + Channel Adapters (20+ protocols) + Agent Runtime + Skills System (markdown-based). Browser automation via CDP. Multi-agent routing with isolated sessions. Founded by Peter Steinberger (Nov 2025); renamed from Clawdbot. | Open source (Apache-style) |
| **Reflexion** | An AI that learns from mistakes by reflecting on failures in plain English — like a student reviewing a failed exam. Achieves 91% on HumanEval vs. GPT-4's 80%. | Verbal reinforcement learning (Shinn et al., NeurIPS 2023). Actor generates actions; evaluator judges success; self-reflection model produces linguistic diagnosis. Reflections stored in episodic buffer (≤3) and injected into retry prompts. "Semantic gradients" without weight updates. | Open source |
| **ExpeL** | An AI that keeps a journal across many tasks, distilling general rules of thumb for future use. | Experiential learning (Zhao et al., Tsinghua, AAAI 2024). Three stages: experience gathering (ReAct + Reflexion), insight extraction (LLM reviews success/failure pairs → ADD/UPVOTE/DOWNVOTE/EDIT rules), evaluation (kNN episodic recall + insights for single-attempt inference). | Open source |
| **DSPy** | Build AI apps by writing structured code instead of fragile prompts — DSPy's compiler automatically finds the best prompts and examples. "PyTorch for LLM applications." 24K+ GitHub stars. | Programming framework (Khattab et al., Stanford, 2023). Signatures (typed I/O specs), Modules (ChainOfThought, ReAct, Retrieve), Optimisers (MIPROv2, GEPA, BootstrapFewShot) that compile programs by tracing, filtering, and optimising. | MIT |

---

## Appendix D: Source Document Reference

| Document | Key Contributions | Date |
|---|---|---|
| TQM Strategic Application | 8 TQM principles, financial case ($273M), lifecycle mapping | January 2026 |
| Product Discovery Comprehensive Guide | 4 risk areas, continuous discovery, OSTs, BDD bridge, HCD, Zero-Based Design | January 2026 |
| TIMC UI Realignment Plan | 5 major UI changes, 37 line items, navigation restructure | March 2026 |
| CCQG Expansion Paper (MMA/SKB/SMM/Loop) | Multi-modal agent orchestration, 7 skill bundles, CoALA memory, ExpeL/Reflexion/DSPy learning loops, PDCA/DMAIC governance, OpenClaw patterns | March 2026 |
| Spec-Based Development with JTBD | Job Stories, 6-step pipeline, EARS notation, spec packages, Three-Tier Boundary, living specs, SDD workflow, productivity evidence | March 2026 |
| Time-Dimensional Testing with Observability | Source for S29–S31 specs (SLO observability, synthetic monitoring, AI model governance); UI configurability insight | March 2026 |
| CCQG Unified Specification v2.0 | Foundation spec — all architectural decisions remain canonical and immutable | January 2026 |
| Train Yard Fleet Overview | Full fleet architecture, four-locomotive model (Structure → Quality → Ship → Certify), land-and-expand strategy, enterprise bundle model | April 2026 |
| StructureView Brief | File viewer architecture, multi-format support (MD/JSON/XML/YAML/TOML), three view modes, FlowTrain brand visual identity, Gold/Steam Red/Deep Background tokens | April 2026 |
| StructureView Lite Brief | TIMC Light integration, document-type aware quality signals, acquisition funnel mechanics, upgrade trigger design | April 2026 |
| Q2 Release Brief | Two-person crew model, domain model wizard, release readiness dashboard, steam pressure gauge metaphor, PRR Q2 locomotive analogy | April 2026 |
| Tier 4 Compliance Brief | 3-tier accountability framework, regulatory kernel (FINRA/FDA), Certificate of Conformity, Positive Train Control layer, Metrolink Tier 4 analogy | April 2026 |
| Turntable Hub Brief | Central launcher design, turntable animation specification, railroad vocabulary, track assignment model, visual language for fleet states | April 2026 |

---

*FlowTrain HQ • Quality Guardian & The Train Yard Fleet • April 2026 | Version 5.0*
