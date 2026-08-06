---
id: "B3"
courseId: "enabled-pm"
tier: "enabled"
roleIds: ["pm", "coach", "engineer", "designer"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 2: writes Given/When/Then acceptance criteria including unhappy paths"
  - "Tier 2: rejects AI test plans that invent behavior"
libraryRefs: ["evaluation-practice", "shift-left-economics"]
---

# User Stories to AI-Assisted Test Plans

> AI can generate manual test plans from user stories — but only if the stories have proper acceptance criteria. This lesson builds both: the story format that enables AI test generation, and the test plan structure that catches what AI misses. (Why catching it here is cheap and catching it in production isn't — the economics of the left — is tracked in the shift-left-economics Evolution Library entry.)

## The Acceptance Criteria Format That Works

User stories that AI can convert to tests have acceptance criteria in this format: 'Given [context], When [action], Then [observable outcome].' Each criterion must describe something observable (not an internal system state), include the unhappy path, and specify the data. 'The form should validate correctly' is not a criterion. 'Given an empty email field, when the user clicks Submit, then a red error message appears below the email field reading \"Email is required\"' is a criterion.

## Test Categories

AI generates test scenarios in predictable categories: happy path (everything works), edge cases (boundary values, empty inputs, max lengths), error handling (system failures, network errors, permission denials), permissions (role-based access), accessibility (keyboard, screen reader), and regression (things that must not break). For backend work, add: dependency failures, observability checkpoints (is the event logged?), and SLA validation.

AI reliably generates the first three categories. Human judgment is required for permissions, accessibility, regression scope, and backend observability.

## Quality Criteria for AI-Generated Test Plans

Before accepting an AI-generated test plan, check: (1) Does every test have a specific expected result — not 'it should work correctly'? (2) Are dependency failures tested for backend scenarios? (3) Are edge cases based on the actual data constraints in the acceptance criteria, not invented by the AI? (4) Are there any invented behaviors — tests for features not described in the story? Reject and return tests that invent behavior. (How evaluation practice itself has evolved — from eyeballing to rubrics like these to production eval harnesses — is tracked in the Evolution Library: see the evaluation-practice entry.)

## Assignment

Take one real user story from your current sprint. Improve its acceptance criteria to the Given/When/Then format. Use AI to generate a test plan. Evaluate the output against the quality criteria and produce a final test plan with your revisions noted.

### Deliverables

- manual-test-plan-[story].md: original AC → improved AC → AI draft → critique → final plan
- Improved AC: minimum 3 Given/When/Then criteria including at least 1 unhappy path
- Critique: categories AI got right, at least 1 invented behavior caught, at least 1 missing category added
- Final test plan: 5+ test scenarios, each with explicit expected result
