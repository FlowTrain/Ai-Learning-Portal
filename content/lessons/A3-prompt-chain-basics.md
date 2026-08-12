---
id: "A3"
courseId: "aware-foundations"
tier: "aware"
roleIds: ["pm", "coach", "designer", "leader"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 1→2: breaks one AI task into steps and checks each step's output before continuing"
  - "Tier 2: names the steps in a repeated workflow and knows which one needs human judgment"
libraryRefs: ["prompting-frameworks", "agent-orchestration"]
---

# Prompt Chain Basics

> Single prompts solve single problems. Chains solve workflows. This lesson introduces the clarify → generate → refine pattern and teaches you to identify where human judgment must stay in the loop — the skill that separates disciplined AI use from reckless automation.

## Start Here: Work You Never Do in One Sitting (5 minutes)

Think of a piece of work you never finish in one go — a status report, a meeting summary that becomes an action list, a draft that needs a second pass. Write down the sittings as steps: "First I gather the notes. Then I write the draft. Then I fix what's wrong with it." You've just described a chain in plain words. This lesson gives those steps names and shows you where AI fits into each one.

## Why Chains Beat Single Prompts

Complex tasks fail with single prompts because the model has to guess at ambiguities and make judgment calls without feedback. A chain breaks the task into steps where each output becomes the verified input for the next. You trade one long prompt (and its unpredictable output) for a series of short, inspectable steps.

The chain pattern: **Clarify** (surface assumptions), **Generate** (produce the artifact), **Critique** (identify gaps), **Refine** (improve based on critique). Most product workflows need exactly these four steps — and they map directly onto the sittings you listed above.

## Where Human Judgment Must Stay

Not every step should be automated. Human judgment is required when: (1) the decision has irreversible consequences, (2) the context involves stakeholder politics or organizational dynamics the AI cannot see, (3) the output will be attributed to a person, or (4) the criteria for 'good' involves taste, values, or priorities that change. Automation-ready steps are mechanical transformations with clear acceptance criteria.

## Capturing Chains for Reuse

A chain is reusable only if it's written down as a sequence of named steps with their prompts, expected outputs, and decision points. A chain that lives only in your head dies when you switch projects. A chain in a markdown file can be handed to a teammate, loaded into an AI context, or eventually packaged as a skill. (Chains are also the ancestor of every multi-agent system in production — how orchestration evolved from this exact pattern is tracked in the Evolution Library: see the agent-orchestration entry.)

## Assignment

Document one 3-step prompt chain for a workflow you run at least monthly. The chain must include a clarify step, a generate step, and a critique or refine step. Explicitly mark the step(s) where human judgment is required and why.

### Deliverables

- prompt-chain-[workflow-name].md
- 3 named steps with: step name, prompt template, expected output, acceptance criteria
- At least 1 step explicitly labeled as 'Human Judgment Required' with a 2-sentence rationale
- A note on when this chain would break down (missing inputs, unclear acceptance criteria, or an irreversible consequence)