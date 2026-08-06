---
id: "A2E"
courseId: "aware-eng"
tier: "aware"
roleIds: ["engineer", "tl", "data"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 1→2: reuses engineering prompts from a written library instead of retyping"
  - "Tier 2: writes a context file before starting a metered agentic session"
libraryRefs: ["prompting-frameworks", "token-economics"]
---

# Your First Engineering Prompt Library

> Engineers interact with AI differently than PMs — but the discipline is identical. This lesson builds your first prompt library focused on engineering tasks: code review, documentation, test generation, and query authoring.

## Engineering Prompt Patterns

The most reusable engineering prompts fall into four categories: **Transform** (convert this spec into code/tests/docs), **Explain** (summarize what this code does for X audience), **Validate** (check this against constraint Y), and **Generate** (produce Z given context A and B). The difference between useful engineering prompts and useless ones is always the same thing: how precisely you specified the input context.

## The Context File Advantage

Engineers who get the most out of agentic AI (Claude Code, GitHub Copilot Agent) do one thing consistently: they write a CLAUDE.md or AGENTS.md before starting. This file gives the agent your architecture, your naming conventions, your test patterns, and your constraints. Without it, the agent re-invents your stack every session. With it, every session picks up where the last one left off.

## Cost Discipline

Agentic sessions burn tokens fast, and a session with poor context costs several times more than one with a good CLAUDE.md — the agent spends your tokens rediscovering what you could have written down. The upfront investment in a good context file pays for itself quickly. Treat prompt refinement in a chat window as free; treat agentic sessions as metered — never start one without structured context.

## Assignment

Build 3 prompt cards focused on engineering tasks you perform at least weekly. One must be a Transform card, one must be a Validate card. Write a draft CLAUDE.md for one of your current projects — minimum 5 fields.

### Deliverables

- prompt-library-eng.md with 3 cards (Transform, Validate, + one of your choice)
- CLAUDE.md draft with: project purpose, tech stack, naming conventions, test patterns, 1 AI constraint
- Cards must reference real tasks (code review, doc generation, query writing, etc.)
