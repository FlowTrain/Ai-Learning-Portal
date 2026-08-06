---
id: "C1"
courseId: "fluent-chains"
tier: "fluent"
roleIds: ["pm", "coach", "engineer", "tl", "designer", "data", "leader"]
durationMin: 30
creditHours: 1
staircaseRung: 3
buildsBehaviors:
  - "Tier 3: designs chains others can run from documentation alone"
  - "Tier 3: writes acceptance criteria per step before writing prompts"
libraryRefs: ["prompting-frameworks", "evaluation-practice", "agent-orchestration"]
---

# Designing Reusable Prompt Chains

> AI-Fluent practitioners don't just use prompt chains — they design them for others to run without explanation. This lesson teaches chain architecture: step decomposition, failure mode handling, human-in-the-loop design, and documentation standards that make chains handoff-ready.

## Chain Architecture Principles

A well-designed prompt chain is deterministic (the same inputs produce equivalent outputs), inspectable (every step's output can be checked before the next runs), recoverable (a failed step can be re-run without restarting), and handoff-ready (someone who didn't build it can run it from the documentation alone). These four properties separate a personal workflow hack from a team asset.

## Failure Mode Engineering

Every chain step has two failure modes: the AI produces wrong output, or the AI produces no output. Build explicit gates: before triggering step N+1, verify that step N's output meets the acceptance criteria for that step. Write the acceptance criteria before you write the prompt — this forces you to define 'good' before you see what AI produces, which is the only honest way to evaluate it. (This criteria-first ordering is the through-line of the evaluation-practice Evolution Library entry.)

## The Handoff Test

A chain is ready to share when: you can give the documentation to a teammate with your same role (but without your product context), and they can run the chain on their own product surface and get equivalent-quality output within one try. If they need to ask you questions, the chain is underspecified. If the quality depends on your personal context, the chain hasn't been generalized enough.

## Assignment

Take one prompt chain you built in a prior lesson and redesign it to pass the handoff test. Add explicit acceptance criteria to each step. Document all failure modes and recovery paths. Give it to one teammate to run — document what they needed to ask you.

### Deliverables

- prompt-chain-v2-[name].md: redesigned chain with acceptance criteria per step
- Failure mode register: at least 2 failure modes per step with recovery actions
- Handoff test results: what your teammate asked, what you updated as a result
- Diff: what changed from v1 to v2 and why
