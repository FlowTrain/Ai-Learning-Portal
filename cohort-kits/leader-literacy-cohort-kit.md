# AI Literacy for Leaders: Fund, Govern, Measure - Cohort Kit

*Generated 2026-07-11 from `content/` by `app/generate_cohort_kit.py leader-literacy`. Regenerate, don't hand-edit.*

**AI-Native bridge** - Weeks 1-3 - 6 assignments - 2 debriefs (final = public showcase)
**For:** Engineering / Product Leader

## Program Overview

**The goal.** Tier 4 literacy for directors and VPs — fund AI workflows, set risk-tier policy, and measure maturity by behavior. Explicitly not the architect track: you write the 'what', your architects build the 'how'. By the end, these behaviors are observable in real work (this is also how completion is assessed - artifacts + behavior, never quizzes):

- Tier 4 literacy: funds AI workflows, not AI tools — every investment names the workflow it changes
- Tier 4 literacy: asks the three ownership questions before approving any AI spend
- Tier 4 literacy: governs by action risk, not by tool bans
- Tier 4 literacy: sets the risk-tier policy and delegates its enforcement to architects
- Tier 4 literacy: measures maturity by observed behaviors and reused artifacts, not tool usage
- Tier 4 literacy: reads the tier-distribution gap against the role×tier target matrix and funds against it

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
| **Week 1** | Funding AI: The Investment One-Pager | A: What Are You Already Paying For? | B: Funding AI: The Investment One-Pager - the artifact |
| **Week 2** | Governing AI: Risk Tiers Without the Architecture | A: The Undo Test | B: Governing AI: Risk Tiers Without the Architecture - the artifact |
| *-> Debrief 1* | *30-min team meeting* | *Focus: asks the three ownership questions before approving any AI spend* | |
| **Week 3** | Measuring AI Maturity: The Dashboard Spec | A: The Vanity Audit | B: Measuring AI Maturity: The Dashboard Spec - the artifact |
| *-> Debrief 2 - SHOWCASE* | *45-min, guests invited* | *Artifacts presented to people outside the cohort* | |

*Hand-off note: assignments drop Monday (A) and Thursday (B); debriefs land the Friday after each even content week. Adjust to your team's rhythm - but keep the showcase public.*

## Weekly Assignments

### Week 1 - Funding AI: The Investment One-Pager

**Lesson:** `D5` - 25 min - staircase rung 2

**Assignment A (~25 min): What Are You Already Paying For?**

Write down every AI line item your org currently pays for — licenses, subscriptions, API budgets, tool seats. Next to each, answer one question in plain words: **what specific workflow changed because of it?** Not "people use it for lots of things" — a named workflow, with a named owner, that runs differently than it did before the spend.

For most leaders, several line items have no answer. That's the problem this lesson exists to fix, and it's a funding-discipline problem, not a technology problem.

Do this on real work, then post one sentence in the cohort thread: what you picked and what surprised you. That sentence is your ticket into the next debrief.

**Assignment B (~30 min): the artifact**

Write an investment one-pager for one real AI funding decision in front of your org right now (or the one you'd most like to force to clarity). Use the five-block format. Every number must be measured or labeled as an estimate — no invented statistics.

**Deliverables**

- ai-investment-one-pager.md: all five blocks, one page
- The three ownership questions answered with names
- A review date and the artifact that will exist if the investment works

**Graded against** (see lesson rubric): Workflow specificity, Full-cost honesty, Decision clarity.

**Role-stretch notes** (optional - keep your strongest challenged)

- **Engineering / Product Leader stretch:** aim your artifact at this bar - *Org-wide AI maturity dashboard with role-specific KPIs*

### Week 2 - Governing AI: Risk Tiers Without the Architecture

**Lesson:** `D6` - 25 min - staircase rung 2

**Assignment A (~25 min): The Undo Test**

List five ways people in your org used AI this month (ask, don't guess). For each one, answer a single plain question: **if the output was wrong, could the action be undone?** A summary someone read — undone by re-reading. An email sent to a customer — not undone. A config change in production — depends entirely on what noticed it first.

You've just performed risk-tier classification. Everything else in this lesson is vocabulary for what you just did.

Do this on real work, then post one sentence in the cohort thread: what you picked and what surprised you. That sentence is your ticket into the next debrief.

**Assignment B (~30 min): the artifact**

Draft the risk-tier policy for your org. Classify at least eight real AI actions (from the Undo Test list and beyond) into the four tiers. State requirements per tier and the delegation line.

**Deliverables**

- risk-tier-policy-draft.md: four tiers, org-specific examples, requirements per tier
- At least 8 real AI actions classified, including at least 1 you'd move to a *lower* tier than current practice treats it
- One sentence naming what is deliberately not governed
- The delegation line: who builds enforcement, and the review cadence with them

**Graded against** (see lesson rubric): Risk classification, Proportionality, Delegation boundary.

**Role-stretch notes** (optional - keep your strongest challenged)

- **Engineering / Product Leader stretch:** aim your artifact at this bar - *Org-wide AI maturity dashboard with role-specific KPIs*

### Week 3 - Measuring AI Maturity: The Dashboard Spec

**Lesson:** `D7` - 25 min - staircase rung 3

**Assignment A (~25 min): The Vanity Audit**

Write down every AI number anyone has ever put in front of you: adoption rates, license utilization, prompts per week, "engagement." For each, ask the only question that matters: **if this number doubled, would anything about your org's work provably be better?** Prompts-sent can double because people are flailing. Logins can double because of a mandate. Usage is what maturity looks like from too far away to see behavior.

Do this on real work, then post one sentence in the cohort thread: what you picked and what surprised you. That sentence is your ticket into the next debrief.

**Assignment B (~30 min): the artifact**

Write the maturity-metric dashboard spec for your org: five metrics, all seven fields each, at least one per family, gap-oriented against the target matrix. Hand it to someone technical and ask them one question: "Could you build this without talking to me?" Their answer is your grade.

**Deliverables**

- maturity-dashboard-spec.md: 5 metrics × 7 fields (name, definition, source, method, cadence, owner, decision informed)
- At least one placement, one certification, and one reuse metric
- The gap view: current vs. role×tier targets, with trend
- One named vanity metric you are explicitly declining to track, and why

**Graded against** (see lesson rubric): Metric validity, Measurability, Gap orientation.

**Role-stretch notes** (optional - keep your strongest challenged)

- **Engineering / Product Leader stretch:** aim your artifact at this bar - *Org-wide AI maturity dashboard with role-specific KPIs*


## Debrief Agendas

The structure is intentionally identical each time (Wins -> Critique -> Stuck points -> Next) so the cohort learns to run it without you. Consider rotating facilitation after the first two.

### Debrief 1 (after Week 2, 30 min)

**Focus:** asks the three ownership questions before approving any AI spend

| Time | Segment | What happens |
|---|---|---|
| 0:00-0:05 | **Wins Wall** | Round-robin, 20 seconds each: one thing that clicked. No passing - if stuck, share what's still confusing. |
| 0:05-0:15 | **Live critique** | 1-2 volunteers show their artifact; cohort reviews against the lesson rubric - rubric on screen, always. |
| 0:15-0:25 | **Stuck points** | Facilitator lists 2-3 themes from the cohort thread. Group troubleshoots, teammate-to-teammate. Recurring confusions go to docs/misconception-log.md. |
| 0:25-0:30 | **Next two weeks** | Preview the coming assignments; re-anchor the ~1 hr/week timebox. |

**Facilitator prompts (pick 1-2)**

- Against "Workflow specificity" - who moved from *investment described as a tool purchase ('we need copilot licenses')* toward *names the workflow, its measured current cost, and the artifact that will prove the change*? Show us.
- Against "Risk classification" - who moved from *policy governs tools ('approved ai tools list') rather than actions* toward *every tier has org-specific examples plus an explicit escalation path between tiers*? Show us.

### Debrief 2 - SHOWCASE (after Week 3, 45 min, guests invited)

**Focus:** sets the risk-tier policy and delegates its enforcement to architects - demonstrated to people who weren't in the room.

| Time | Segment | What happens |
|---|---|---|
| 0:00-0:05 | **Wins Wall** | 20 seconds each: the artifact you're proudest of and who should reuse it. |
| 0:05-0:30 | **Showcase** | 3-4 volunteers present artifacts to invited guests (adjacent team, sponsor, next cohort). Guests ask the questions; cohort answers. |
| 0:30-0:40 | **Reuse contracting** | Each guest names ONE artifact they'll actually take. That's the metric. Log it. |
| 0:40-0:45 | **What's next** | Route to the next bridge (AI-Native track) via the placement diagnostic. |

**The point:** a public artifact is the credential. Reuse promised out loud is reuse that happens.


---

*Sources of truth: lessons in `content/lessons/`, rubrics in lesson frontmatter, current-practice claims in `library/evolution/`. Misconception patterns from debriefs feed `docs/misconception-log.md`.*
