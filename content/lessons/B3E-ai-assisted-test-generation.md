---
id: "B3E"
courseId: "enabled-eng"
tier: "enabled"
roleIds: ["engineer", "tl", "data"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 2: assembles the full input chain (ACs, boundary doc, context file) before test generation"
  - "Tier 2: reviews generated tests for realistic data and contract-aligned mocks"
---

# AI-Assisted Test Generation

> AI can generate test skeletons from acceptance criteria faster than any engineer can write boilerplate — but the quality of the tests is entirely determined by the quality of the input. This lesson builds the input discipline that makes AI test generation reliable.

## The Test Generation Input Chain

Quality test generation requires: structured acceptance criteria (Given/When/Then), the service boundary doc (so the AI knows what dependencies to mock), and the CLAUDE.md (so the AI knows your test patterns and framework). When all three are present, AI generates test skeletons that match your actual patterns. When any one is missing, AI invents patterns that require manual correction.

## What AI Generates Well vs. Poorly

AI generates reliably: happy path tests, input validation tests, simple integration stubs. AI generates poorly: tests that require understanding of organizational context (what 'premium user' means in your specific system), tests for non-functional requirements (performance, security), and tests that depend on production data patterns. Engineer judgment is always required for test data selection and environment configuration.

## The Review Loop

After AI generates test skeletons, run this review: (1) Do the test names describe the behavior being tested? (2) Are the test data values realistic, or did AI use placeholder values that would never occur in production? (3) Does the test actually test what the acceptance criterion says? (4) Are mocks aligned with the actual service contract? Catch these in review, not in CI.

## Assignment

Generate test skeletons for a real feature in your current sprint using AI. Provide your CLAUDE.md, service boundary doc, and structured ACs as context. Document the review loop: what you changed, what you kept, and why.

### Deliverables

- test-generation-[feature].md: context provided → AI output → review loop results
- At least 5 test skeletons generated
- Review loop: 2 changes made (with rationale), 2 things kept (with rationale)
- One test the AI could not generate without your judgment — explain why
