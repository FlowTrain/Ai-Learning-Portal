---
id: "B2E"
courseId: "enabled-eng"
tier: "enabled"
roleIds: ["engineer", "tl", "data"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 2: anchors code-review prompts in team conventions and boundary docs"
  - "Tier 2: provides the 'why' as context when generating documentation"
---

# AI-Assisted Code Review and Documentation

> AI-assisted code review and documentation works only when the AI has architecture context. This lesson builds the workflow that gets useful, project-specific AI feedback — not generic advice that ignores your patterns.

## The Code Review Prompt Pattern

Generic code review prompt: 'Review this code.' Result: generic advice. Structured code review prompt: 'Review this code for: (1) alignment with our naming conventions [see CLAUDE.md], (2) test coverage of edge cases in the acceptance criteria [attached], (3) any missing error handling for the failure modes in our service boundary doc.' Result: specific, actionable feedback tied to your actual system.

The difference is 3 minutes of prompt structuring vs. 30 minutes of filtering irrelevant feedback.

## Documentation Generation

AI-generated documentation is only as good as the code context it receives. For function-level docs: provide the function, its callers, and the business rule it implements. For module-level docs: provide the module's service boundary doc as context. For architecture docs: provide your ADR log and let AI synthesize the narrative. Never generate docs without providing the 'why' — AI generates the 'what' fine on its own but invents the 'why' badly.

## Test Generation from Specs

The highest-ROI engineering AI workflow: write acceptance criteria in structured format → AI generates test skeletons → engineer fills in test data. The AI handles the boilerplate; the engineer handles the judgment. For this to work, acceptance criteria must include: happy path, edge cases, error conditions, and performance constraints. If your ACs don't include these, fix the AC first — the test generation will reveal the gaps.

## Assignment

Run AI-assisted code review on a real PR or code change in your current project. Use your CLAUDE.md and service boundary doc as context. Document what the AI caught that manual review would have missed, and what the AI missed that you caught.

### Deliverables

- code-review-workflow.md: the prompt pattern, context provided, AI output, your additions
- At least 2 'AI caught' items and 2 'human caught' items — with analysis of why
- A documentation draft for one function or module generated with proper context
- One test skeleton generated from structured acceptance criteria
