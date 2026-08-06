---
id: "C4"
courseId: "fluent-chains"
tier: "fluent"
roleIds: ["pm", "coach", "engineer", "tl", "designer", "data", "leader"]
durationMin: 30
creditHours: 1
staircaseRung: 3
buildsBehaviors:
  - "Tier 3: authors durable context files that make AI behavior consistent across the team"
  - "Tier 3: runs a context review cadence to prevent context decay"
libraryRefs: ["context-engineering", "context-file-architecture"]
---

# Durable AI Context: CLAUDE.md and soul.md

> The most expensive AI sessions are the ones that start from zero. CLAUDE.md prevents this for project context. soul.md prevents this for team persona and values. Together, they are the two files that turn a generic AI assistant into a domain-aware, values-aligned team collaborator. This lesson authors both.

## CLAUDE.md: The Project Memory File

A CLAUDE.md is the answer to the question: 'What should an AI know before doing any work in this project?' It contains the things you would tell a highly competent new engineer on their first day: what the project does, what decisions have already been made, what patterns the team uses, what the AI must not do, and where to find key artifacts.

The test of a good CLAUDE.md: a senior engineer new to the project could get to first meaningful contribution in one day using only this file and the codebase. If it takes more, the file is incomplete.

## soul.md: The Team's AI Persona

A soul.md defines how the AI collaborator should behave on this team: its communication style (formal or casual?), its values (prefer explicit tradeoffs over confident recommendations?), its constraints (never suggest deleting tests to pass CI), and its working agreements (always ask one clarifying question before generating long artifacts).

Without a soul.md, AI behavior varies session to session and practitioner to practitioner — which makes AI outputs inconsistent and harder to review. With one, AI becomes a consistent team member with predictable behavior.

## Context Hygiene

Context files are living documents. They decay as the project evolves. Establish a context review cadence: CLAUDE.md reviewed at the start of each quarter, soul.md reviewed at the start of each new team member's onboarding. The review question: 'Is there anything in this file that's no longer true, or anything true that's not in this file?' The answer tells you the maintenance cost of your context files — which is always cheaper than the cost of AI working from outdated context. (The evolution of context practice — and the placement and curation rules these files implement — is tracked in the Evolution Library: see the context-engineering entry.)

## Assignment

Write a production-quality CLAUDE.md for your primary project and a soul.md for your team. Both must be specific enough that reading them takes less than 5 minutes and leaves no questions about how the AI should behave. Get one teammate to review them and document their feedback.

### Deliverables

- CLAUDE.md: project context, decisions made, patterns, constraints, key file locations
- .claude/soul.md: communication style, values, working agreements, 3 explicit constraints
- Teammate review: 2 things they would add, 2 things that were unclear, your revisions
- Context review schedule: when these files will be reviewed and by whom
