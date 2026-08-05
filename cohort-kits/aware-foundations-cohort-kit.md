# AI Foundations for Product Teams - Cohort Kit

*Generated 2026-07-11 from `content/` by `app/generate_cohort_kit.py aware-foundations`. Regenerate, don't hand-edit.*

**AI-Aware bridge** - Weeks 1-6 - 10 assignments - 3 debriefs (final = public showcase)
**For:** Product Manager / Product Coach / UX/Product Designer / Engineering / Product Leader

## Program Overview

**The goal.** Build the vocabulary and mental models to work effectively with AI tools. No prior AI experience required. By the end, these behaviors are observable in real work (this is also how completion is assessed - artifacts + behavior, never quizzes):

- Tier 1: targets AI at one specific low-risk task and finishes it
- Tier 1: follows one safety rule consistently
- Tier 1: describes a screen or service in plain, complete sentences before asking AI for anything
- Tier 1: recognizes that vague requests produce made-up answers, and says what was missing
- Tier 1→2: reuses a prompt that worked instead of retyping from memory
- Tier 2: maintains a small personal prompt library with known failure modes
- Tier 1→2: breaks one AI task into steps and checks each step's output before continuing
- Tier 2: names the steps in a repeated workflow and knows which one needs human judgment
- Tier 1: picks a tool deliberately instead of using the same AI for everything
- Tier 1→2: can explain in plain language when AI is and isn't appropriate for a task

**How it's structured.** Two assignments per week (~25-30 min each): **A** puts the lesson's opening move onto your real work; **B** produces the lesson's artifact. One 30-minute debrief every two weeks - the debrief is where critique happens, so artifacts must exist before it. Final session is a **showcase with guests**: artifacts presented to people outside the cohort, because reuse is the metric that can't be gamed.

**Norms to set at kickoff.**

- Time box: ~1 hour per week total. If an assignment runs long, stop - that's data for the debrief.
- Ask in the open: one pinned cohort thread per week. "Stuck" is not a secret.
- Done beats perfect: the goal is reps and artifacts, not polish.
- Real work only: synthetic examples are re-dos. Every artifact must point at your actual product.

**What this kit will not cover (on purpose).** AI-Enabled-tier material - anything a rung above this course's lessons - is deliberately out. If someone asks, note the question for the coach and don't derail. The menu on the placemat is not the order.

## At-a-Glance Calendar

| Week | Theme | Assignment A (~25 min) | Assignment B (~30 min) |
|---|---|---|---|
| **Week 1** | The First Win: Get 20 Minutes Back | A: Prep & apply: Pick the Chore (2 minutes) | B: The First Win: Get 20 Minutes Back - the artifact |
| **Week 2** | Describing Your Product Surface for AI | A: The Stranger Test | B: Describing Your Product Surface for AI - the artifact |
| *-> Debrief 1* | *30-min team meeting* | *Focus: follows one safety rule consistently* | |
| **Week 3** | Your First Prompt Library | A: Find Your Repeat | B: Your First Prompt Library - the artifact |
| **Week 4** | *Check-in week* | *No new assignments - catch up, finish artifacts, ask for help in the open* | |
| **Week 5** | Prompt Chain Basics | A: Work You Never Do in One Sitting | B: Prompt Chain Basics - the artifact |
| *-> Debrief 2* | *30-min team meeting* | *Focus: maintains a small personal prompt library with known failure modes* | |
| **Week 6** | Right Tool, Right Task | A: Your Last Five | B: Right Tool, Right Task - the artifact |
| *-> Debrief 3 - SHOWCASE* | *45-min, guests invited* | *Artifacts presented to people outside the cohort* | |

*Hand-off note: assignments drop Monday (A) and Thursday (B); debriefs land the Friday after each even content week. Adjust to your team's rhythm - but keep the showcase public.*

## Weekly Assignments

### Week 1 - The First Win: Get 20 Minutes Back

**Lesson:** `A0` - 15 min - staircase rung 1

**Assignment A (~25 min): Prep & apply: Pick the Chore (2 minutes)**

Read the lesson through **Pick the Chore (2 minutes)**, then apply its core idea to one real piece of your work in a 10-line note. Excerpt to anchor you:

> Choose one small, dull task that's already on your plate this week. Good candidates: summarizing a long document you have to read anyway, turning messy meeting notes into a tidy email, drafting a first version of something you'd normally stare at a blank page for. Pick something low-stakes — nothing confidential, nothing where a mistake would embarrass you.

Post one sentence in the cohort thread: where it fit, or where it fought you.

**Assignment B (~30 min): the artifact**

Do the chore for real — the output should be something you actually use this week, not an exercise.

**Deliverables**

- The finished chore itself (the summary, the email, the draft — whatever you made)
- first-win.md with three sentences: what the task was, roughly how much time it saved, and one thing you'd say differently to the AI next time


**Role-stretch notes** (optional - keep your strongest challenged)

- **Product Manager stretch:** aim your artifact at this bar - *PRDs generated from structured context in < 30 min*
- **Product Coach stretch:** aim your artifact at this bar - *Every PM on their roster has a maintained prompt library*
- **UX/Product Designer stretch:** aim your artifact at this bar - *Design specs generated from user research in Storybook-ready format*
- **Engineering / Product Leader stretch:** aim your artifact at this bar - *Org-wide AI maturity dashboard with role-specific KPIs*

### Week 2 - Describing Your Product Surface for AI

**Lesson:** `A1` - 25 min - staircase rung 1

**Assignment A (~25 min): The Stranger Test**

Pick one screen or one service you know well. Now describe it — out loud or in writing — to an imaginary new coworker who has never seen it. Could they sketch it from your words alone?

Most first attempts sound like this: "It's the invoices page." A description that passes the stranger test sounds like this: "The screen has a header with the customer's name, a table of invoices with dates and amounts, and a side panel showing payment status."

That second sentence is the whole skill. Nothing more advanced is required in this lesson.

Do this on real work, then post one sentence in the cohort thread: what you picked and what surprised you. That sentence is your ticket into the next debrief.

**Assignment B (~30 min): the artifact**

Choose one screen you own (or one service, if that's your world). Write a plain-language description that passes the stranger test: someone who has never seen your product could sketch or summarize it from your words alone.

**Deliverables**

- A markdown document (my-screen.md or my-service.md)
- At least 3 areas of the screen, or 3 jobs of the service, each described in complete sentences
- One "when it goes wrong" moment explicitly described (empty, loading, failed, wrong input)
- One rule the thing must always follow, in plain words


**Role-stretch notes** (optional - keep your strongest challenged)

- **Product Manager stretch:** aim your artifact at this bar - *PRDs generated from structured context in < 30 min*
- **Product Coach stretch:** aim your artifact at this bar - *Every PM on their roster has a maintained prompt library*
- **UX/Product Designer stretch:** aim your artifact at this bar - *Design specs generated from user research in Storybook-ready format*
- **Engineering / Product Leader stretch:** aim your artifact at this bar - *Org-wide AI maturity dashboard with role-specific KPIs*

### Week 3 - Your First Prompt Library

**Lesson:** `A2` - 25 min - staircase rung 2 - library: prompting-frameworks

**Assignment A (~25 min): Find Your Repeat**

Scroll back through your AI chat history from the last two weeks. Find one request you've typed more than once — different words, same intent ("summarize this doc for my boss," "turn these notes into an email"). That repeat is your first library entry. You've already done the hard part: discovering a prompt worth keeping.

Do this on real work, then post one sentence in the cohort thread: what you picked and what surprised you. That sentence is your ticket into the next debrief.

**Assignment B (~30 min): the artifact**

Build the first 3 cards of your personal prompt library. At least one card must come from a real prompt you've used in your actual work — not a synthetic example. At least one card must include a documented failure mode from real experience.

**Deliverables**

- personal-prompt-library.md with exactly 3 cards
- Each card: Intent, Inputs, Prompt (with placeholders), Expected Output, Failure Modes
- One card must reference a real product artifact you own
- One card must document a real failure mode you observed


**Role-stretch notes** (optional - keep your strongest challenged)

- **Product Manager stretch:** aim your artifact at this bar - *PRDs generated from structured context in < 30 min*
- **Product Coach stretch:** aim your artifact at this bar - *Every PM on their roster has a maintained prompt library*
- **UX/Product Designer stretch:** aim your artifact at this bar - *Design specs generated from user research in Storybook-ready format*
- **Engineering / Product Leader stretch:** aim your artifact at this bar - *Org-wide AI maturity dashboard with role-specific KPIs*

### Week 4 - Prompt Chain Basics

**Lesson:** `A3` - 25 min - staircase rung 2 - library: prompting-frameworks, agent-orchestration

**Assignment A (~25 min): Work You Never Do in One Sitting**

Think of a piece of work you never finish in one go — a status report, a meeting summary that becomes an action list, a draft that needs a second pass. Write down the sittings as steps: "First I gather the notes. Then I write the draft. Then I fix what's wrong with it." You've just described a chain in plain words. This lesson gives those steps names and shows you where AI fits into each one.

Do this on real work, then post one sentence in the cohort thread: what you picked and what surprised you. That sentence is your ticket into the next debrief.

**Assignment B (~30 min): the artifact**

Document one 3-step prompt chain for a workflow you run at least monthly. The chain must include a clarify step, a generate step, and a critique or refine step. Explicitly mark the step(s) where human judgment is required and why.

**Deliverables**

- prompt-chain-[workflow-name].md
- 3 named steps with: step name, prompt template, expected output, acceptance criteria
- At least 1 step explicitly labeled as 'Human Judgment Required' with a 2-sentence rationale
- A note on when this chain would break down (mod


**Role-stretch notes** (optional - keep your strongest challenged)

- **Product Manager stretch:** aim your artifact at this bar - *PRDs generated from structured context in < 30 min*
- **Product Coach stretch:** aim your artifact at this bar - *Every PM on their roster has a maintained prompt library*
- **UX/Product Designer stretch:** aim your artifact at this bar - *Design specs generated from user research in Storybook-ready format*
- **Engineering / Product Leader stretch:** aim your artifact at this bar - *Org-wide AI maturity dashboard with role-specific KPIs*

### Week 5 - Right Tool, Right Task

**Lesson:** `A4` - 20 min - staircase rung 1 - library: token-economics

**Assignment A (~25 min): Your Last Five**

Write down the last five times you used an AI tool for work. Next to each one, answer in plain words: did you get what you needed on the first try? If not, how many tries did it take? Keep this list — it's the raw material for the assignment, and the pattern in it is usually visible immediately: the frustrating ones were the wrong tool, the wrong preparation, or both.

Do this on real work, then post one sentence in the cohort thread: what you picked and what surprised you. That sentence is your ticket into the next debrief.

**Assignment B (~30 min): the artifact**

Take your "last five" list from the opening activity. For each entry, identify: which tool you used, which tool was the best fit, and what written context (if any) you gave it before starting. Then write a "tool selection rule" for your specific role that you would share with a new teammate.

**Deliverables**

- right-tool-audit.md with 5 real task entries (task, tool used, best-fit tool, context provided)
- A 3-5 rule 'tool selection guide' for your role — written to be handed to a new team member
- One example of a task where you'd switch tools based on this lesson


**Role-stretch notes** (optional - keep your strongest challenged)

- **Product Manager stretch:** aim your artifact at this bar - *PRDs generated from structured context in < 30 min*
- **Product Coach stretch:** aim your artifact at this bar - *Every PM on their roster has a maintained prompt library*
- **UX/Product Designer stretch:** aim your artifact at this bar - *Design specs generated from user research in Storybook-ready format*
- **Engineering / Product Leader stretch:** aim your artifact at this bar - *Org-wide AI maturity dashboard with role-specific KPIs*


## Debrief Agendas

The structure is intentionally identical each time (Wins -> Critique -> Stuck points -> Next) so the cohort learns to run it without you. Consider rotating facilitation after the first two.

### Debrief 1 (after Week 2, 30 min)

**Focus:** follows one safety rule consistently

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

**Focus:** maintains a small personal prompt library with known failure modes

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

**Focus:** names the steps in a repeated workflow and knows which one needs human judgment - demonstrated to people who weren't in the room.

| Time | Segment | What happens |
|---|---|---|
| 0:00-0:05 | **Wins Wall** | 20 seconds each: the artifact you're proudest of and who should reuse it. |
| 0:05-0:30 | **Showcase** | 3-4 volunteers present artifacts to invited guests (adjacent team, sponsor, next cohort). Guests ask the questions; cohort answers. |
| 0:30-0:40 | **Reuse contracting** | Each guest names ONE artifact they'll actually take. That's the metric. Log it. |
| 0:40-0:45 | **What's next** | Route to the next bridge (AI-Enabled track) via the placement diagnostic. |

**The point:** a public artifact is the credential. Reuse promised out loud is reuse that happens.


---

*Sources of truth: lessons in `content/lessons/`, rubrics in lesson frontmatter, current-practice claims in `library/evolution/`. Misconception patterns from debriefs feed `docs/misconception-log.md`.*
