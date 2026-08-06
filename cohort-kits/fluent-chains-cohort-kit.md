# AI-Fluent: Workflow Design - Cohort Kit

*Generated 2026-07-11 from `content/` by `app/generate_cohort_kit.py fluent-chains`. Regenerate, don't hand-edit.*

**AI-Fluent bridge** - Weeks 1-6 - 10 assignments - 3 debriefs (final = public showcase)
**For:** Product Manager / Product Coach / Software Engineer / Tech Lead / Staff Engineer / UX/Product Designer / Data / Analytics Engineer / Engineering / Product Leader

## Program Overview

**The goal.** Design reusable prompt chains, author skill packages, govern token costs, and build AI-ready context for agentic systems. By the end, these behaviors are observable in real work (this is also how completion is assessed - artifacts + behavior, never quizzes):

- Tier 3: designs chains others can run from documentation alone
- Tier 3: writes acceptance criteria per step before writing prompts
- Tier 3: owns team-level AI cost governance with documented baselines
- Tier 3: calculates full ROI (time, tokens, maintenance) before certifying workflows
- Tier 3: packages proven workflows as versioned, self-contained skills
- Tier 3: maintains and versions team skills as shared infrastructure
- Tier 3: authors durable context files that make AI behavior consistent across the team
- Tier 3: runs a context review cadence to prevent context decay
- Tier 3: evaluates an AI-data proposal by question cadence, full cost, and failure modes — not by tool familiarity
- Tier 3: can state the case FOR the two architectures they didn't propose

**How it's structured.** Two assignments per week (~25-30 min each): **A** puts the lesson's opening move onto your real work; **B** produces the lesson's artifact. One 30-minute debrief every two weeks - the debrief is where critique happens, so artifacts must exist before it. Final session is a **showcase with guests**: artifacts presented to people outside the cohort, because reuse is the metric that can't be gamed.

**Norms to set at kickoff.**

- Time box: ~1 hour per week total. If an assignment runs long, stop - that's data for the debrief.
- Ask in the open: one pinned cohort thread per week. "Stuck" is not a secret.
- Done beats perfect: the goal is reps and artifacts, not polish.
- Real work only: synthetic examples are re-dos. Every artifact must point at your actual product.

**What this kit will not cover (on purpose).** AI-Native-tier material - anything a rung above this course's lessons - is deliberately out. If someone asks, note the question for the coach and don't derail. The menu on the placemat is not the order.

## At-a-Glance Calendar

| Week | Theme | Assignment A (~25 min) | Assignment B (~30 min) |
|---|---|---|---|
| **Week 1** | Designing Reusable Prompt Chains | A: Prep & apply: Chain Architecture Principles | B: Designing Reusable Prompt Chains - the artifact |
| **Week 2** | Token Governance and Cost Management | A: Prep & apply: The Refinement-First Rule | B: Token Governance and Cost Management - the artifact |
| *-> Debrief 1* | *30-min team meeting* | *Focus: writes acceptance criteria per step before writing prompts* | |
| **Week 3** | Authoring AI Skills (SKILL.md) | A: Prep & apply: What a Skill Is | B: Authoring AI Skills (SKILL.md) - the artifact |
| **Week 4** | *Check-in week* | *No new assignments - catch up, finish artifacts, ask for help in the open* | |
| **Week 5** | Durable AI Context: CLAUDE.md and soul.md | A: Prep & apply: CLAUDE.md: The Project Memory File | B: Durable AI Context: CLAUDE.md and soul.md - the artifact |
| *-> Debrief 2* | *30-min team meeting* | *Focus: maintains and versions team skills as shared infrastructure* | |
| **Week 6** | Where Should the Answers Live? (Three Teams, One Question) | A: The Question Census | B: Where Should the Answers Live? (Three Teams, One Question) - the artifact |
| *-> Debrief 3 - SHOWCASE* | *45-min, guests invited* | *Artifacts presented to people outside the cohort* | |

*Hand-off note: assignments drop Monday (A) and Thursday (B); debriefs land the Friday after each even content week. Adjust to your team's rhythm - but keep the showcase public.*

## Weekly Assignments

### Week 1 - Designing Reusable Prompt Chains

**Lesson:** `C1` - 30 min - staircase rung 3 - library: prompting-frameworks, evaluation-practice, agent-orchestration

**Assignment A (~25 min): Prep & apply: Chain Architecture Principles**

Read the lesson through **Chain Architecture Principles**, then apply its core idea to one real piece of your work in a 10-line note. Excerpt to anchor you:

> A well-designed prompt chain is deterministic (the same inputs produce equivalent outputs), inspectable (every step's output can be checked before the next runs), recoverable (a failed step can be re-run without restarting), and handoff-ready (someone who didn't build it can run it from the documentation alone). These four properties separate a personal workflow hack from a team asset.

Post one sentence in the cohort thread: where it fit, or where it fought you.

**Assignment B (~30 min): the artifact**

Take one prompt chain you built in a prior lesson and redesign it to pass the handoff test. Add explicit acceptance criteria to each step. Document all failure modes and recovery paths. Give it to one teammate to run — document what they needed to ask you.

**Deliverables**

- prompt-chain-v2-[name].md: redesigned chain with acceptance criteria per step
- Failure mode register: at least 2 failure modes per step with recovery actions
- Handoff test results: what your teammate asked, what you updated as a result
- Diff: what changed from v1 to v2 and why


**Role-stretch notes** (optional - keep your strongest challenged)

- **Product Manager stretch:** aim your artifact at this bar - *PRDs generated from structured context in < 30 min*
- **Product Coach stretch:** aim your artifact at this bar - *Every PM on their roster has a maintained prompt library*
- **Software Engineer stretch:** aim your artifact at this bar - *AI-assisted PR reviews reduce review cycle by 50%*
- **Tech Lead / Staff Engineer stretch:** aim your artifact at this bar - *AI cost governance policy authored and enforced team-wide*

### Week 2 - Token Governance and Cost Management

**Lesson:** `C2` - 25 min - staircase rung 2 - library: token-economics

**Assignment A (~25 min): Prep & apply: The Refinement-First Rule**

Read the lesson through **The Refinement-First Rule**, then apply its core idea to one real piece of your work in a 10-line note. Excerpt to anchor you:

> Before opening any metered AI tool (Figma AI, Claude Code, any agentic session), run one refinement pass in a free or cheap chat window. The goal: compress vague intent into specific, structured instructions. The test: if you read your prompt aloud to a colleague and they couldn't ask a clarifying question, the prompt is specific enough. This one rule substantially reduces metered-tool token consumption.

Post one sentence in the cohort thread: where it fit, or where it fought you.

**Assignment B (~30 min): the artifact**

Select one AI workflow your team runs regularly. Calculate its current ROI: time saved, token cost (estimate if not tracked), and maintenance overhead. Run one refinement pass to reduce token cost by at least 20%. Document the before/after.

**Deliverables**

- cost-governance-[workflow].md: ROI calculation (time saved, token cost, maintenance)
- Refinement demonstration: original prompt → refined prompt → token reduction estimate
- A 3-rule governance policy for your team's use of metered AI tools
- One workflow you would de-certify based on negative ROI, with the math


**Role-stretch notes** (optional - keep your strongest challenged)

- **Product Manager stretch:** aim your artifact at this bar - *PRDs generated from structured context in < 30 min*
- **Product Coach stretch:** aim your artifact at this bar - *Every PM on their roster has a maintained prompt library*
- **Software Engineer stretch:** aim your artifact at this bar - *AI-assisted PR reviews reduce review cycle by 50%*
- **Tech Lead / Staff Engineer stretch:** aim your artifact at this bar - *AI cost governance policy authored and enforced team-wide*

### Week 3 - Authoring AI Skills (SKILL.md)

**Lesson:** `C3` - 30 min - staircase rung 3

**Assignment A (~25 min): Prep & apply: What a Skill Is**

Read the lesson through **What a Skill Is**, then apply its core idea to one real piece of your work in a 10-line note. Excerpt to anchor you:

> A skill is a named, versionable folder containing: a SKILL.md with YAML frontmatter (name, version, triggers, audience) and instructions (step-by-step workflow with prompts), plus optional supporting files (templates, examples, schemas). When an AI assistant loads a skill, it gains the ability to run that workflow reliably without the user re-explaining it.

Post one sentence in the cohort thread: where it fit, or where it fought you.

**Assignment B (~30 min): the artifact**

Package one proven workflow from your prior assignments as a complete SKILL.md. The skill must be self-contained — a colleague with the same role and a different product should be able to trigger it and get useful output without asking you any questions.

**Deliverables**

- skills/[skill-name]/SKILL.md: YAML frontmatter + step-by-step instructions + prompts
- At least 3 steps with embedded prompt templates using {{placeholders}}
- Frontmatter: name, version (1.0.0), triggers (2-3 example phrases), audience (roles)
- A test run log: what you prompted, what the skill produced, what you would improve in v1.1


**Role-stretch notes** (optional - keep your strongest challenged)

- **Product Manager stretch:** aim your artifact at this bar - *PRDs generated from structured context in < 30 min*
- **Product Coach stretch:** aim your artifact at this bar - *Every PM on their roster has a maintained prompt library*
- **Software Engineer stretch:** aim your artifact at this bar - *AI-assisted PR reviews reduce review cycle by 50%*
- **Tech Lead / Staff Engineer stretch:** aim your artifact at this bar - *AI cost governance policy authored and enforced team-wide*

### Week 4 - Durable AI Context: CLAUDE.md and soul.md

**Lesson:** `C4` - 30 min - staircase rung 3 - library: context-engineering

**Assignment A (~25 min): Prep & apply: CLAUDE.md: The Project Memory File**

Read the lesson through **CLAUDE.md: The Project Memory File**, then apply its core idea to one real piece of your work in a 10-line note. Excerpt to anchor you:

> A CLAUDE.md is the answer to the question: 'What should an AI know before doing any work in this project?' It contains the things you would tell a highly competent new engineer on their first day: what the project does, what decisions have already been made, what patterns the team uses, what the AI must not do, and where to find key artifacts.

Post one sentence in the cohort thread: where it fit, or where it fought you.

**Assignment B (~30 min): the artifact**

Write a production-quality CLAUDE.md for your primary project and a soul.md for your team. Both must be specific enough that reading them takes less than 5 minutes and leaves no questions about how the AI should behave. Get one teammate to review them and document their feedback.

**Deliverables**

- CLAUDE.md: project context, decisions made, patterns, constraints, key file locations
- .claude/soul.md: communication style, values, working agreements, 3 explicit constraints
- Teammate review: 2 things they would add, 2 things that were unclear, your revisions
- Context review schedule: when these files will be reviewed and by whom


**Role-stretch notes** (optional - keep your strongest challenged)

- **Product Manager stretch:** aim your artifact at this bar - *PRDs generated from structured context in < 30 min*
- **Product Coach stretch:** aim your artifact at this bar - *Every PM on their roster has a maintained prompt library*
- **Software Engineer stretch:** aim your artifact at this bar - *AI-assisted PR reviews reduce review cycle by 50%*
- **Tech Lead / Staff Engineer stretch:** aim your artifact at this bar - *AI cost governance policy authored and enforced team-wide*

### Week 5 - Where Should the Answers Live? (Three Teams, One Question)

**Lesson:** `C5` - 30 min - staircase rung 2 - library: prompting-frameworks, context-engineering, token-economics

**Assignment A (~25 min): The Question Census**

Before any architecture talk, take a census. Write down the last five reporting questions your team actually asked of your work-tracking data. For each one, note three things in plain words:

1. **Cadence** — was it asked once, weekly, or continuously?
2. **Asker** — a person exploring, an analyst scanning history, or a product surface that displays the answer automatically?
3. **Cost of wrong** — what happened (or would happen) if the answer was wrong?

Keep the census. It is the input to everything that follows — and here's the punchline in advance: when three teams argue past each other about architecture, it's almost always because they each did this census silently, on different questions, and don't know it.

Do this on real work, then post one sentence in the cohort thread: what you picked and what surprised you. That sentence is your ticket into the next debrief.

**Assignment B (~30 min): the artifact**

Run the pattern on your real situation. Take your question census from the opening (grow it to at least five real questions if needed). Score all three architectures against the six questions. Write a one-page decision memo.

**Deliverables**

- architecture-decision-memo-[topic].md: one page
- The question census: 5+ real questions with cadence, asker, and cost-of-wrong for each
- The six-question scoring table: three options × six questions
- A recommendation, the strongest objection to it stated fairly, and — for each option you did NOT choose — the question type it would still win

**Graded against** (see lesson rubric): Question-first framing, Steel-manning, Full-cost honesty.

**Role-stretch notes** (optional - keep your strongest challenged)

- **Tech Lead / Staff Engineer stretch:** aim your artifact at this bar - *AI cost governance policy authored and enforced team-wide*
- **Software Engineer stretch:** aim your artifact at this bar - *AI-assisted PR reviews reduce review cycle by 50%*
- **Data / Analytics Engineer stretch:** aim your artifact at this bar - *SQL generation from plain-language business questions*
- **Engineering / Product Leader stretch:** aim your artifact at this bar - *Org-wide AI maturity dashboard with role-specific KPIs*


## Debrief Agendas

The structure is intentionally identical each time (Wins -> Critique -> Stuck points -> Next) so the cohort learns to run it without you. Consider rotating facilitation after the first two.

### Debrief 1 (after Week 2, 30 min)

**Focus:** writes acceptance criteria per step before writing prompts

| Time | Segment | What happens |
|---|---|---|
| 0:00-0:05 | **Wins Wall** | Round-robin, 20 seconds each: one thing that clicked. No passing - if stuck, share what's still confusing. |
| 0:05-0:15 | **Live critique** | 1-2 volunteers show their artifact; cohort reviews against the lesson rubric - rubric on screen, always. |
| 0:15-0:25 | **Stuck points** | Facilitator lists 2-3 themes from the cohort thread. Group troubleshoots, teammate-to-teammate. Recurring confusions go to docs/misconception-log.md. |
| 0:25-0:30 | **Next two weeks** | Preview the coming assignments; re-anchor the ~1 hr/week timebox. |

**Facilitator prompts (pick 1-2)**

- Where did the tools fight you? (Some friction is tooling, not learning - name which.)
- Who ran a teammate's artifact this week? What broke?

### Debrief 2 (after Week 4, 30 min)

**Focus:** maintains and versions team skills as shared infrastructure

| Time | Segment | What happens |
|---|---|---|
| 0:00-0:05 | **Wins Wall** | Round-robin, 20 seconds each: one thing that clicked. No passing - if stuck, share what's still confusing. |
| 0:05-0:15 | **Live critique** | 1-2 volunteers show their artifact; cohort reviews against the lesson rubric - rubric on screen, always. |
| 0:15-0:25 | **Stuck points** | Facilitator lists 2-3 themes from the cohort thread. Group troubleshoots, teammate-to-teammate. Recurring confusions go to docs/misconception-log.md. |
| 0:25-0:30 | **Next two weeks** | Preview the coming assignments; re-anchor the ~1 hr/week timebox. |

**Facilitator prompts (pick 1-2)**

- Where did the tools fight you? (Some friction is tooling, not learning - name which.)
- Who ran a teammate's artifact this week? What broke?

### Debrief 3 - SHOWCASE (after Week 5, 45 min, guests invited)

**Focus:** runs a context review cadence to prevent context decay - demonstrated to people who weren't in the room.

| Time | Segment | What happens |
|---|---|---|
| 0:00-0:05 | **Wins Wall** | 20 seconds each: the artifact you're proudest of and who should reuse it. |
| 0:05-0:30 | **Showcase** | 3-4 volunteers present artifacts to invited guests (adjacent team, sponsor, next cohort). Guests ask the questions; cohort answers. |
| 0:30-0:40 | **Reuse contracting** | Each guest names ONE artifact they'll actually take. That's the metric. Log it. |
| 0:40-0:45 | **What's next** | Route to the next bridge (AI-Native track) via the placement diagnostic. |

**The point:** a public artifact is the credential. Reuse promised out loud is reuse that happens.


---

*Sources of truth: lessons in `content/lessons/`, rubrics in lesson frontmatter, current-practice claims in `library/evolution/`. Misconception patterns from debriefs feed `docs/misconception-log.md`.*
