---
id: "D3"
courseId: "native-systems"
tier: "native"
roleIds: ["tl", "leader", "coach"]
durationMin: 30
creditHours: 1
staircaseRung: 3
buildsBehaviors:
  - "Tier 4: designs skill-library governance with owners, review, and health metrics"
  - "Tier 4: measures library value by reuse, not existence"
---

# AI Skill Library Design

> A skill library is organizational memory for AI workflows. This lesson designs the governance, taxonomy, and maintenance system for a team-wide skill library that scales beyond individual contributors.

## Library Architecture

A scalable skill library has: a taxonomy (skills organized by role, tier, and workflow type), a quality bar (skills must pass a review before entering the library), a versioning system (skills are versioned and changelogs maintained), and an owner model (every skill has a named owner who is responsible for maintenance). A library without an owner model collapses — skills become stale, no one updates them, and the library becomes a source of bad outputs rather than good ones.

## The Skill Review Process

Skills enter the library through a review: the skill must have been run at least 5 times with documented results, the outputs must have been validated by a domain expert, the skill's failure modes must be documented, and the skill must pass a 'handoff test' (a new user can trigger it without asking the author questions). Skills that fail review are returned with specific feedback — not rejected outright.

## Measuring Library Value

Library value is measured by: number of skill runs per month (usage), number of unique users (breadth), time saved per run vs. manual process (ROI), number of skills that have been updated (maintenance health), and number of skills deprecated after model updates (adaptability). A library with high usage but no maintenance is a technical debt liability. A library with zero usage is a vanity project.

## Assignment

Design the governance and taxonomy for your team's AI skill library. Define the review process, the owner model, and the success metrics. Package at least one skill from your prior assignments that meets the library quality bar.

### Deliverables

- skill-library-design.md: taxonomy, quality bar, review process, owner model, metrics
- Review checklist: the 5-point rubric used to evaluate skills for library admission
- One production-quality skill package (from C3 or equivalent) with review notes applied
- Library health dashboard spec: 5 metrics with measurement method
