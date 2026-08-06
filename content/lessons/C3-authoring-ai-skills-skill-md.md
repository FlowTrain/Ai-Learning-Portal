---
id: "C3"
courseId: "fluent-chains"
tier: "fluent"
roleIds: ["pm", "coach", "engineer", "tl", "designer", "data", "leader"]
durationMin: 30
creditHours: 1
staircaseRung: 3
buildsBehaviors:
  - "Tier 3: packages proven workflows as versioned, self-contained skills"
  - "Tier 3: maintains and versions team skills as shared infrastructure"
---

# Authoring AI Skills (SKILL.md)

> Skills are the packaging format that turns personal workflows into organizational infrastructure. An AI-Fluent practitioner can take any proven prompt chain and package it as a SKILL.md that an AI assistant loads on-demand. This lesson builds your first real skill.

## What a Skill Is

A skill is a named, versionable folder containing: a SKILL.md with YAML frontmatter (name, version, triggers, audience) and instructions (step-by-step workflow with prompts), plus optional supporting files (templates, examples, schemas). When an AI assistant loads a skill, it gains the ability to run that workflow reliably without the user re-explaining it.

A skill is not a prompt card. A prompt card is for a person to copy. A skill is for a workflow to run the same way, every time, by the AI. The distinction matters because skills are consumed differently — they need to be self-contained, context-independent, and AI-parseable.

## When a Workflow Deserves to Be a Skill

Package a workflow as a skill when: (1) it has been run at least 5 times with consistent results, (2) it produces an artifact that other people reuse, (3) it requires the same setup context every time (which can be encoded in the skill), and (4) a teammate with the same role could trigger it without knowing your specific product context. If any of these aren't true, the workflow isn't stable enough to package.

## Skill Versioning and Maintenance

Skills must be versioned. When the underlying AI model changes, the product domain changes, or a new failure mode is discovered, the skill must be updated and the version bumped. A skill that hasn't been reviewed in 6 months is suspect. A skill library without an owner is a liability. The discipline is the same as maintaining any shared codebase: it's not done when it's written, it's done when it's maintained.

## Assignment

Package one proven workflow from your prior assignments as a complete SKILL.md. The skill must be self-contained — a colleague with the same role and a different product should be able to trigger it and get useful output without asking you any questions.

### Deliverables

- skills/[skill-name]/SKILL.md: YAML frontmatter + step-by-step instructions + prompts
- At least 3 steps with embedded prompt templates using {{placeholders}}
- Frontmatter: name, version (1.0.0), triggers (2-3 example phrases), audience (roles)
- A test run log: what you prompted, what the skill produced, what you would improve in v1.1
