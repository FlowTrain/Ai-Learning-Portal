# The Four-Tier AI Maturity Model

This is the spine of the learning platform. Tiers are defined by **observable behaviors in real work**, not abstract knowledge levels — a coach should be able to watch someone work on a Monday morning and place them.

## Overview

| Tier | Name | Primary mode | Population reality |
|---|---|---|---|
| 1 | **AI-Aware** | Tries tools, low stakes | The enterprise default. Most of the workforce. |
| 2 | **AI-Enabled** | Uses AI in daily work | The broad middle every enterprise program aims to create. |
| 3 | **AI-Fluent** | Designs workflows | Coaches, senior PMs, tech leads. A minority. |
| 4 | **AI-Native** | Architects systems | A small percentage ever reach this. Not a target for everyone. |

Two design rules that follow from this table:

1. **Programs are bridges between adjacent tiers, never leaps.** A Tier 1→2 program and a Tier 2→3 program are different products with different vocabularies. Teaching JSON interface design to a Tier 1 cohort is teaching Platinum behavior to a Bronze room.
2. **Tier 4 is the reference persona, not the finish line.** The platform designer operates at Tier 4 and must treat their own baseline as explicitly out of scope for most learners — the curse of knowledge is the primary design risk of this entire platform.

---

## Tier 1 — AI-Aware (basic literacy)

"Has heard of it, maybe tried it." Many stopped at their 2022 mental model: AI is a chat box that answers.

**Observable behaviors**
- Opens an AI tool occasionally to "ask a question" or "summarize something" when prompted by a colleague or training.
- Types short, unstructured prompts with little context and no output expectations.
- Checks output informally ("seems right / seems off"); doesn't log usage or outcomes.
- Often forgets AI could help ("I didn't think of using it for that").
- Talks about AI in terms of hype, fear, or curiosity — not as a normal work tool.

**Leveling up looks like**
- Targets AI at specific low-risk tasks: draft emails, summarize docs, outline meeting notes.
- Follows at least one safety rule consistently ("never paste confidential data; always verify").

**Program design implications:** habit formation, vocabulary, safety, and emotional first wins ("this saved me 20 minutes"). No JSON. No schemas. The staircase starts with plain language.

---

## Tier 2 — AI-Enabled (regular, purposeful use)

AI is a regular tool; they're not designing systems.

**Observable behaviors**
- Uses AI multiple times per week on real work: summarizing PRDs, drafting tickets, outlining test plans, first-draft slides.
- Writes prompts with basic structure: context, task, audience.
- Reuses prompt patterns and templates from a team library rather than inventing everything.
- Routinely edits AI output before sending; treats it as a draft assistant, not a source of truth.
- Can explain in plain language when AI is and isn't appropriate.

**Leveling up looks like**
- Compares models/tools and chooses based on task.
- Tracks personal "win stories" and shares them with peers.

**Program design implications:** this is where most PMs need to land. Narrative prompt patterns (Context → Task → Constraints → Output) before any structural formats. Tables, headings, and gentle frontmatter before JSON.

---

## Tier 3 — AI-Fluent (workflow and pattern designer)

They shape how AI is used in work, even if they don't architect systems. **This is the coach-track target.**

**Observable behaviors**
- Designs repeatable AI workflows for the team ("every sprint review, these three queries produce this summary").
- Uses structured prompting consistently: CTCO patterns, explicit output schemas, simple JSON.
- Curates and maintains team prompt libraries, templates, and skills — and teaches others when to use them.
- Integrates AI into existing tools; avoids copy-paste chaos.
- Thinks in risk tiers: keeps AI on reversible/read-only tasks; demands human review where customers, regulators, or production are affected.

**Leveling up looks like**
- Experiments with light RAG or API integrations — connecting AI to data sources instead of pasting raw text.
- Defines measurable outcomes for AI-assisted workflows and reviews them.

**Program design implications:** this is where the 4-week unified coach guide sits (Tier 2→3 bridge). SKILL.md, CLAUDE.md, soul.md authoring, chain design, token governance.

---

## Tier 4 — AI-Native (system and platform architect)

Designs, deploys, and governs AI systems and agentic platforms.

**Observable behaviors**
- Architects end-to-end AI systems: model selection, orchestration, agent design, tool integration, data strategy, monitoring, governance.
- Designs structured interfaces for AI: JSON schemas, function signatures, DSLs, spec formats, test harnesses.
- Classifies AI actions by risk tier (read-only / reversible / external / high-risk) with approval flows and logging.
- Implements observability and quality: prompt/version control, evaluation harnesses, drift detection, continuous improvement loops.
- Engages with regulation and ethics: maps system behavior to regulatory frameworks; writes documentation a regulator could understand.

**Leveling up looks like**
- Moves from single systems to organizational intelligence: multiple AI systems coordinated across departments, aligned with strategy and risk appetite.

**Program design implications:** label this track explicitly as "architect / platform / regulatory leadership." Use the Tier 4 designer's own work (platform building, evaluation harnesses, governance) as case studies and aspirational material — not as the expected outcome for the cohort.

---

## Role × Tier Target Matrix

Targets, not ceilings. An individual can exceed their role's target; the program commits to getting them **to** it.

| Role | Baseline (typical) | Program target | Stretch |
|---|---|---|---|
| Product Manager | Tier 1–2 | **Tier 2** | Tier 3 |
| Product Coach | Tier 2 | **Tier 3** | Tier 4 awareness |
| Software Engineer | Tier 1–2 | **Tier 2** | Tier 3 |
| UX / Product Designer | Tier 1–2 | **Tier 2** | Tier 3 |
| Data / Analytics Engineer | Tier 2 | **Tier 2–3** | Tier 3 |
| Tech Lead / Staff Engineer | Tier 2 | **Tier 3** | Tier 4 |
| Engineering / Product Leader | Tier 1–2 | **Tier 2 + Tier 4 literacy** | — |

Leaders are a special case: they personally need Tier 2 habits plus enough Tier 4 *literacy* to fund, govern, and measure the maturity strategy — without pretending to be architects.

## Placement: the Monday-Morning Diagnostic

Place people by watching behavior, not by self-assessment (self-assessment over-places almost everyone). Five observable checks:

1. **Unprompted use:** did they reach for AI this week without being told to? (No → Tier 1)
2. **Prompt shape:** do their prompts contain context, task, and audience? (No → Tier 1; Yes → Tier 2+)
3. **Reuse:** do they use or maintain a prompt library/template? (Use → Tier 2; maintain/curate → Tier 3)
4. **Workflow design:** have they defined a repeatable AI workflow someone else runs? (Yes → Tier 3)
5. **System design:** have they built schemas, evals, or governance others operate within? (Yes → Tier 4)

Tag every lesson with the tier behaviors it builds: "By the end, Tier 1 participants can X; Tier 2 participants can Y."
