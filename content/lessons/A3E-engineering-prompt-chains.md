---
id: "A3E"
courseId: "aware-eng"
tier: "aware"
roleIds: ["engineer", "tl", "data"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 1→2: breaks an engineering task into chain steps with validation between them"
  - "Tier 2: distinguishes automation candidates from judgment-required steps"
libraryRefs: ["prompting-frameworks", "agent-orchestration"]
---

# Engineering Prompt Chains

> Engineering workflows are ideal candidates for prompt chains because they have clear inputs (specs, PRDs, existing code) and clear outputs (tests, docs, code). This lesson builds your first engineering chain and identifies automation candidates vs. judgment-required steps.

## The Engineering Chain Pattern

The most common high-value engineering chain: **Spec → Test Plan → Test Code → Review Checklist**. Each step has a clear input (the prior step's output), a clear transformation (what the LLM adds), and a clear validation (what 'good enough to proceed' looks like). This chain alone eliminates the most common bottleneck in sprint delivery: writing tests before code is merged.

## Chains vs. One-Shot Generation

One-shot generation (give the model a spec, get back code) fails on anything complex because there's no feedback loop. Chains succeed because each step can be validated before proceeding. The key insight: the validation step is where the human adds the most value — checking the output of step N before triggering step N+1 is far cheaper than fixing a bad final artifact.

## Identifying Automation Candidates

A step is ready for automation when: it runs the same way every time, its inputs are always available in structured form, its success criteria can be checked programmatically, and a bad output is safe to retry without consequences. Most documentation generation, test skeleton creation, and code comment tasks meet this bar. Architecture decisions, stakeholder tradeoffs, and acceptance criteria definition never do.

## Assignment

Document a 3-step engineering chain for a workflow in your current sprint or project. Identify which steps are automation candidates and which require human review. Estimate the weekly time saving if this chain were consistently applied.

### Deliverables

- eng-chain-[workflow].md with 3 named steps
- Each step: prompt template, expected output, validation criteria
- Each step labeled: 'Automation Candidate' or 'Human Review Required' with rationale
- Time-saving estimate: current manual effort vs. chain-assisted effort (weekly minutes saved)