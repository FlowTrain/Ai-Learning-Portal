---
id: "B1E"
courseId: "enabled-eng"
tier: "enabled"
roleIds: ["engineer", "tl", "data"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 2: maintains a CLAUDE.md and service boundary docs for owned projects"
  - "Tier 2→3: gives agentic tools durable context instead of re-explaining each session"
libraryRefs: ["context-engineering"]
---

# Engineering AI Context Files

> Agentic AI tools are only as good as the context they start with. This lesson builds the context files that turn generic AI assistants into domain-aware engineering collaborators: CLAUDE.md, architecture decision records, and service boundary docs.

## The CLAUDE.md Pattern

A CLAUDE.md (or AGENTS.md, or COPILOT.md — the name matters less than the habit) is a project-level context file that the AI reads at the start of every agentic session. It contains: project purpose (2 sentences), tech stack (exact versions), architectural patterns (what the team agreed on), naming conventions, test patterns, things the AI must not do, and pointers to where key files live.

Without it, every agentic session starts from zero. With it, the AI inherits months of team decisions instantly. (Why durable context files became standard practice — and how context management evolved past prompt-stuffing — is tracked in the Evolution Library: see the context-engineering entry.)

## Architecture Decision Records

ADRs are the highest-leverage documents an AI-native engineering team can maintain. They record: the context, the decision, the alternatives considered, the consequences, and the status. An AI with access to your ADR log can explain any architectural choice, flag when new work violates an existing decision, and synthesize tradeoffs across decisions. A team without ADRs asks the AI to make architectural choices without knowing the history — the worst possible input.

## Service Boundary Documents

Every service or module should have a 1-page boundary doc: what it does, what it doesn't do, who calls it, what it calls, its SLA, and its failure modes. These docs feed directly into AI-assisted code review, incident response, and onboarding. A team that maintains them gets AI assistance that knows the system. A team that doesn't gets generic advice that must be manually filtered for applicability.

## Assignment

Write a complete CLAUDE.md for your primary current project. Write a service boundary doc for one service you own. Demonstrate how the two documents together enable a more specific and accurate AI response on a real engineering task.

### Deliverables

- CLAUDE.md: all required sections filled, no placeholder text
- service-boundary-[name].md: capabilities, consumers, contracts, dependencies, SLA, failure modes
- A before/after prompt demonstration: same engineering question, with and without these context files
