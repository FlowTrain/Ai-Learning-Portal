---
id: "D1"
courseId: "native-systems"
tier: "native"
roleIds: ["tl", "leader", "coach"]
durationMin: 30
creditHours: 1
staircaseRung: 3
buildsBehaviors:
  - "Tier 4: designs the eval pipeline before the prompt"
  - "Tier 4: specifies bounded, auditable agentic workflows with failure protocols"
libraryRefs: ["structured-outputs", "evaluation-practice", "agent-orchestration"]
---

# AI System Architecture

> AI-Native practitioners don't use AI — they architect it into systems. This lesson covers the design principles for AI-first product systems: evaluation pipelines, agentic workflow design, and the governance structures that make AI production-safe at scale.

## Evaluation-First Design

Any AI capability that ships to production needs an evaluation pipeline before it ships. An eval pipeline answers: does this AI behavior meet the quality bar, consistently, across the range of inputs the system will encounter? The eval design comes before the prompt design — define what 'good' looks like, build the eval, then iterate prompts until the eval passes.

Teams that skip eval design ship AI capabilities that work on demos and break in production. Teams that build evals first discover failure modes before users do. (Current harness practice — calibrated judges, sampled production scoring, drift monitoring — is tracked in the evaluation-practice Evolution Library entry.)

## Agentic Workflow Design Patterns

Production-grade agentic workflows are designed with: a bounded scope (the agent knows exactly what it is and isn't allowed to do), a tool inventory (explicit list of tools the agent can call, with input/output contracts — schema-enforced; see the structured-outputs Evolution Library entry), a failure protocol (what the agent does when it can't complete a task — it never silently fails), and an audit log (every action the agent takes is logged with rationale). Agentic workflows without these properties are not production-ready. (Topology guidance — when one agent beats many, and what each added agent must justify — is tracked in the agent-orchestration Evolution Library entry.)

## Organizational AI Governance

At the AI-Native level, governance is a system design problem: who approves new AI capabilities before they're deployed? Who owns the eval pipelines? Who is alerted when a model update changes behavior? What's the rollback procedure when an AI workflow degrades? These questions have engineering answers — not just policy answers. AI-Native organizations have the infrastructure to answer them operationally, not just in documentation.

## Assignment

Design the architecture for one AI capability your team wants to ship to production. Include the eval pipeline design, the agentic workflow design (if applicable), and the governance structure. This document should be reviewable by a principal engineer or VP of Engineering.

### Deliverables

- ai-system-design-[capability].md: capability description, eval pipeline, governance structure
- Eval pipeline: at least 3 test categories with success criteria and failure thresholds
- Agentic workflow (if applicable): scope, tool inventory, failure protocol, audit log spec
- Governance: approval process, owner, rollback procedure, review cadence
