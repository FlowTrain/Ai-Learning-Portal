---
id: "B2"
courseId: "enabled-pm"
tier: "enabled"
roleIds: ["pm", "coach"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 2: writes minimum viable context before prompting for PM artifacts"
  - "Tier 2: edits AI output critically — flags missing evidence, numbers, failure cases"
libraryRefs: ["ai-product-discovery"]
---

# AI-Assisted PRDs and Stakeholder Comms

> AI can accelerate PRD drafting, stakeholder email writing, and user problem synthesis — but only if the PM provides structured context first. This lesson builds the workflow that turns rough notes into polished PM artifacts without losing product substance.

## The Structured Context Pattern for PRDs

Before prompting an AI to draft a PRD, write the minimum viable context: problem statement (2 sentences), user and their goal, what success looks like, what's out of scope, and one key constraint. With this context, AI produces a solid first draft. Without it, AI produces a plausible-looking document with fabricated details that take longer to fix than starting from scratch.

## Audience Rewrites

The most underused PM AI superpower: take one set of facts and produce three versions — engineering spec, executive summary, and customer-facing announcement — without losing technical nuance in any of them. The prompt pattern: 'Rewrite the following for [audience]. Preserve all technical constraints and numbers exactly. Change only the framing and vocabulary.' This alone eliminates a large share of the time PMs spend on communication work.

## Identifying Weak AI Output

AI-generated PM artifacts fail in predictable ways: they sound authoritative but lack specifics, they omit failure modes, they invent user research that wasn't provided (the discovery-cosplay failure mode — see the ai-product-discovery Evolution Library entry), and they use vague success criteria ('improve user satisfaction'). Train yourself to flag these on first read: where is the evidence? Where is the number? Where is the failure case? If you can't find them, they need to come from you, not from a second AI prompt.

## Assignment

Use AI to draft one real PRD section (problem statement, user stories, or acceptance criteria) for a feature you're currently working on. Document the context you provided, the first AI draft, your critique of the draft, and the final version after revision.

### Deliverables

- copilot-prd-workflow.md: context provided → first draft → critique → final draft
- Critique must identify at least 2 specific weaknesses in the AI draft
- Final version must resolve all identified weaknesses
- One 'audience rewrite' demonstration: same content for two different audiences
