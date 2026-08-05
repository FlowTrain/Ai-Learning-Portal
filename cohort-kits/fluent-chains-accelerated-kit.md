# AI-Fluent: Workflow Design - Accelerated Cohort Kit

*Generated 2026-07-11 by `app/generate_cohort_kit.py fluent-chains --profile accelerated`. Regenerate, don't hand-edit.*

**AI-Fluent bridge - ACCELERATED** - 2 weeks - 5 individual assignments - 2 live sessions (final = public showcase)
**For:** Product Manager / Product Coach / Software Engineer / Tech Lead / Staff Engineer / UX/Product Designer / Data / Analytics Engineer / Engineering / Product Leader - cohorts with **dedicated learning time (~3 hrs/week)**. If your cohort has ~1 hr/week, use the standard kit instead; compression without time is how programs die politely.

## Program Overview

**The goal.** Design reusable prompt chains, author skill packages, govern token costs, and build AI-ready context for agentic systems. Observable behaviors by the end (assessment = artifacts + behavior, never quizzes):

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

**The weekly rhythm - 4 touchpoints:** three individual assignments (one lesson each: a short opening move on your real work, then the artifact) and one 60-minute live session combining a **group activity** (artifact swap - your work gets used by someone else, cold) with rubric critique.

**Norms to set at kickoff.**

- Time box: ~3 hours/week, protected on the calendar - accelerated means denser, not "on top of everything else."
- Artifacts before the session: the group activity needs your artifact to exist. No artifact = observer seat this week.
- Ask in the open: one pinned cohort thread per week. "Stuck" is not a secret.
- Real work only: synthetic examples are re-dos.

**What this kit will not cover (on purpose).** AI-Native-tier material is deliberately out. Note the questions; don't derail. The menu on the placemat is not the order.

## At-a-Glance Calendar

| Week | Lessons | Individual assignments | Live session |
|---|---|---|---|
| **Week 1** | Designing Reusable Prompt Chains / Token Governance and Cost Management / Authoring AI Skills (SKILL.md) | C1 / C2 / C3 (individual, ~45 min each) | Debrief + group activity (60 min) |
| **Week 2** | Durable AI Context: CLAUDE.md and soul.md / Where Should the Answers Live? (Three Teams, One Question) | C4 / C5 (individual, ~45 min each) | SHOWCASE (60 min, guests) |

*Hand-off note: assignments drop Monday; the live session lands Friday. The showcase needs guests booked by week 1 - invite them at kickoff.*

## Week 1 - Designing Reusable Prompt Chains / Token Governance and Cost Management / Authoring AI Skills (SKILL.md)

#### C1 - Designing Reusable Prompt Chains (individual, ~45 min)

**Step 1 - Prep & apply: Chain Architecture Principles (~10 min).** Read the lesson through **Chain Architecture Principles**, then apply its core idea to one real piece of your work in a 10-line note. Excerpt to anchor you:

**Step 2 - the artifact (~35 min).**

Take one prompt chain you built in a prior lesson and redesign it to pass the handoff test. Add explicit acceptance criteria to each step. Document all failure modes and recovery paths. Give it to one teammate to run — document what they needed to ask you.

**Deliverables**

- prompt-chain-v2-[name].md: redesigned chain with acceptance criteria per step
- Failure mode register: at least 2 failure modes per step with recovery actions
- Handoff test results: what your teammate asked, what you updated as a result
- Diff: what changed from v1 to v2 and why


- **Product Manager stretch:** aim your artifact at this bar - *PRDs generated from structured context in < 30 min*
- **Product Coach stretch:** aim your artifact at this bar - *Every PM on their roster has a maintained prompt library*
- **Software Engineer stretch:** aim your artifact at this bar - *AI-assisted PR reviews reduce review cycle by 50%*
- **Tech Lead / Staff Engineer stretch:** aim your artifact at this bar - *AI cost governance policy authored and enforced team-wide*

#### C2 - Token Governance and Cost Management (individual, ~45 min)

**Step 1 - Prep & apply: The Refinement-First Rule (~10 min).** Read the lesson through **The Refinement-First Rule**, then apply its core idea to one real piece of your work in a 10-line note. Excerpt to anchor you:

**Step 2 - the artifact (~35 min).**

Select one AI workflow your team runs regularly. Calculate its current ROI: time saved, token cost (estimate if not tracked), and maintenance overhead. Run one refinement pass to reduce token cost by at least 20%. Document the before/after.

**Deliverables**

- cost-governance-[workflow].md: ROI calculation (time saved, token cost, maintenance)
- Refinement demonstration: original prompt → refined prompt → token reduction estimate
- A 3-rule governance policy for your team's use of metered AI tools
- One workflow you would de-certify based on negative ROI, with the math


- **Product Manager stretch:** aim your artifact at this bar - *PRDs generated from structured context in < 30 min*
- **Product Coach stretch:** aim your artifact at this bar - *Every PM on their roster has a maintained prompt library*
- **Software Engineer stretch:** aim your artifact at this bar - *AI-assisted PR reviews reduce review cycle by 50%*
- **Tech Lead / Staff Engineer stretch:** aim your artifact at this bar - *AI cost governance policy authored and enforced team-wide*

#### C3 - Authoring AI Skills (SKILL.md) (individual, ~45 min)

**Step 1 - Prep & apply: What a Skill Is (~10 min).** Read the lesson through **What a Skill Is**, then apply its core idea to one real piece of your work in a 10-line note. Excerpt to anchor you:

**Step 2 - the artifact (~35 min).**

Package one proven workflow from your prior assignments as a complete SKILL.md. The skill must be self-contained — a colleague with the same role and a different product should be able to trigger it and get useful output without asking you any questions.

**Deliverables**

- skills/[skill-name]/SKILL.md: YAML frontmatter + step-by-step instructions + prompts
- At least 3 steps with embedded prompt templates using {{placeholders}}
- Frontmatter: name, version (1.0.0), triggers (2-3 example phrases), audience (roles)
- A test run log: what you prompted, what the skill produced, what you would improve in v1.1


- **Product Manager stretch:** aim your artifact at this bar - *PRDs generated from structured context in < 30 min*
- **Product Coach stretch:** aim your artifact at this bar - *Every PM on their roster has a maintained prompt library*
- **Software Engineer stretch:** aim your artifact at this bar - *AI-assisted PR reviews reduce review cycle by 50%*
- **Tech Lead / Staff Engineer stretch:** aim your artifact at this bar - *AI cost governance policy authored and enforced team-wide*

## Week 2 - Durable AI Context: CLAUDE.md and soul.md / Where Should the Answers Live? (Three Teams, One Question)

#### C4 - Durable AI Context: CLAUDE.md and soul.md (individual, ~45 min)

**Step 1 - Prep & apply: CLAUDE.md: The Project Memory File (~10 min).** Read the lesson through **CLAUDE.md: The Project Memory File**, then apply its core idea to one real piece of your work in a 10-line note. Excerpt to anchor you:

**Step 2 - the artifact (~35 min).**

Write a production-quality CLAUDE.md for your primary project and a soul.md for your team. Both must be specific enough that reading them takes less than 5 minutes and leaves no questions about how the AI should behave. Get one teammate to review them and document their feedback.

**Deliverables**

- CLAUDE.md: project context, decisions made, patterns, constraints, key file locations
- .claude/soul.md: communication style, values, working agreements, 3 explicit constraints
- Teammate review: 2 things they would add, 2 things that were unclear, your revisions
- Context review schedule: when these files will be reviewed and by whom


- **Product Manager stretch:** aim your artifact at this bar - *PRDs generated from structured context in < 30 min*
- **Product Coach stretch:** aim your artifact at this bar - *Every PM on their roster has a maintained prompt library*
- **Software Engineer stretch:** aim your artifact at this bar - *AI-assisted PR reviews reduce review cycle by 50%*
- **Tech Lead / Staff Engineer stretch:** aim your artifact at this bar - *AI cost governance policy authored and enforced team-wide*

#### C5 - Where Should the Answers Live? (Three Teams, One Question) (individual, ~45 min)

**Step 1 - The Question Census (~10 min).** Before any architecture talk, take a census. Write down the last five reporting questions your team actually asked of your work-tracking data. For each one, note three things in plain words:

**Step 2 - the artifact (~35 min).**

Run the pattern on your real situation. Take your question census from the opening (grow it to at least five real questions if needed). Score all three architectures against the six questions. Write a one-page decision memo.

**Deliverables**

- architecture-decision-memo-[topic].md: one page
- The question census: 5+ real questions with cadence, asker, and cost-of-wrong for each
- The six-question scoring table: three options × six questions
- A recommendation, the strongest objection to it stated fairly, and — for each option you did NOT choose — the question type it would still win

**Graded against:** Question-first framing, Steel-manning, Full-cost honesty.

- **Tech Lead / Staff Engineer stretch:** aim your artifact at this bar - *AI cost governance policy authored and enforced team-wide*
- **Software Engineer stretch:** aim your artifact at this bar - *AI-assisted PR reviews reduce review cycle by 50%*
- **Data / Analytics Engineer stretch:** aim your artifact at this bar - *SQL generation from plain-language business questions*
- **Engineering / Product Leader stretch:** aim your artifact at this bar - *Org-wide AI maturity dashboard with role-specific KPIs*


## Live Session Agendas

### Week 1 session - debrief + group activity (60 min)

**Focus:** writes acceptance criteria per step before writing prompts

| Time | Segment | What happens |
|---|---|---|
| 0:00-0:05 | **Wins Wall** | 20 seconds each: one thing that clicked this week. No passing. |
| 0:05-0:30 | **Group activity: artifact swap** | Pairs exchange this week's artifacts and attempt to USE them cold. Reuse friction is the finding - capture it. |
| 0:30-0:50 | **Rubric critique** | 2 volunteers' artifacts reviewed against the lesson rubrics - rubric on screen, always. Recurring confusions go to docs/misconception-log.md. |
| 0:50-0:60 | **Next week** | Preview the next 3 lessons; re-anchor the ~3 hr/week timebox. |

**Artifact swap prompts**

- **C1:** hand your artifact to a partner; they must *use* it (not read it) and report where it broke.
- **C2:** hand your artifact to a partner; they must *use* it (not read it) and report where it broke.
- **C3:** hand your artifact to a partner; they must *use* it (not read it) and report where it broke.

### Week 2 session - SHOWCASE (60 min, guests invited)

**Focus:** runs a context review cadence to prevent context decay - demonstrated to people who weren't in the room.

| Time | Segment | What happens |
|---|---|---|
| 0:00-0:05 | **Wins Wall** | 20 seconds each: proudest artifact of the program and who should reuse it. |
| 0:05-0:35 | **Showcase** | Volunteers present artifacts to invited guests (adjacent team, sponsor, next cohort). Guests ask; cohort answers. |
| 0:35-0:50 | **Reuse contracting** | Each guest names ONE artifact they'll actually take. Log it - that's the metric. |
| 0:50-0:60 | **What's next** | Route to the next bridge (AI-Native track) via the placement diagnostic. |


---

*Sources of truth: lessons in `content/lessons/`, rubrics in lesson frontmatter, current-practice claims in `library/evolution/`. Misconception patterns feed `docs/misconception-log.md`.*
