---
id: "C2"
courseId: "fluent-chains"
tier: "fluent"
roleIds: ["pm", "coach", "engineer", "tl", "designer", "data", "leader"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 3: owns team-level AI cost governance with documented baselines"
  - "Tier 3: calculates full ROI (time, tokens, maintenance) before certifying workflows"
libraryRefs: ["token-economics"]
---

# Token Governance and Cost Management

> AI-Fluent practitioners are accountable for AI costs — not just their own, but their team's. This lesson establishes the governance framework that keeps AI ROI positive: prompt refinement discipline, metered tool policies, and the audit habits that catch waste before it compounds.

## The Refinement-First Rule

Before opening any metered AI tool (Figma AI, Claude Code, any agentic session), run one refinement pass in a free or cheap chat window. The goal: compress vague intent into specific, structured instructions. The test: if you read your prompt aloud to a colleague and they couldn't ask a clarifying question, the prompt is specific enough. This one rule substantially reduces metered-tool token consumption.

## Team-Level Governance

Token governance at team level requires: a 'cost per workflow' baseline (how much does running this chain typically cost?), a usage anomaly threshold (what triggers a review?), and a prompt quality gate before any workflow becomes team-standard. The quality gate: the workflow must have been run at least 3 times with consistent output, and the token cost must be documented in the chain's documentation.

## The AI ROI Calculation

ROI on AI tooling is: (time saved × hourly rate) − (token cost + maintenance time). Most teams can calculate time saved. Almost no teams calculate token cost or maintenance time. A workflow that saves 2 hours per week but costs $50/month in tokens and 1 hour/week of maintenance has negative ROI at most hourly rates. Build the habit of calculating all three before certifying any workflow as 'approved.'

## Assignment

Select one AI workflow your team runs regularly. Calculate its current ROI: time saved, token cost (estimate if not tracked), and maintenance overhead. Run one refinement pass to reduce token cost by at least 20%. Document the before/after.

### Deliverables

- cost-governance-[workflow].md: ROI calculation (time saved, token cost, maintenance)
- Refinement demonstration: original prompt → refined prompt → token reduction estimate
- A 3-rule governance policy for your team's use of metered AI tools
- One workflow you would de-certify based on negative ROI, with the math
