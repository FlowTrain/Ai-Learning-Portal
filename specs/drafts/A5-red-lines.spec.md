# Module Spec — The Red Lines: What Never Goes In

> **Why this spec exists:** Tier 1 cohort feedback (2026-07-15) — "not enough Level 1 content,
> people don't believe they'll get past this stage." Diagnosis in `docs/program-catalog.md`
> (Catalog Health): Level 1 holds most of the workforce on 3 plain-rung lessons. `docs/staircase-map.md`
> shows **Safety & governance rung 1 = "A0 (The One Rule)"** — embedded in a 15-min hook lesson.
> This module promotes safety to a standalone rung-1 lesson. Pillar: **safety** (maturity-model.md,
> Tier 1 program design implications).

## 1. Identity (maps 1:1 to lesson frontmatter)

| Field | Value | Rule |
|---|---|---|
| id | A5 | `^[A-Z][0-9]+[A-Z]?$` — aware arc, no role variant (safety is universal) |
| courseId | aware-foundations | home course; **also add to `aware-eng` lessonIds** (same pattern as A0/A1/A4) |
| tier | aware | |
| roleIds | pm, coach, designer, leader, engineer, tl, data | all seven — matches A0 |
| durationMin | 20 | |
| staircaseRung | 1 | plain language; zero JSON/schema/policy vocabulary |
| creditHours | 1 | matches A4 (20 min) |

## 2. The concept and its staircase ancestry

**Concept in one sentence:** There are a few things you will never put into an AI tool, you can say
what they are without being told, and you know what to do instead.

**Where does this concept already live?** (`docs/staircase-map.md`, row "Safety & governance")

- Rung 1 ancestor: **A0 ("The One Rule")** — embedded only, and A0 shares that slot with the
  *checking-output* concept row. Overloaded. **This module takes ownership of the safety half.**
- Rung 2 ancestor: C2 (team governance policy), D6 (risk-tier policy)
- This module sits at rung **1** because: the output is a personal card in the learner's own words —
  not a policy, not a risk tier, not an approval flow. No tooling, no vocabulary they don't already have.

**Staircase note:** A0 keeps a one-line safety mention as its hook ("the one rule"); A5 is where it
becomes a habit with an artifact. Update the staircase map's Safety row rung-1 cell to `A5
(standalone); A0 (embedded hook)` when this ships.

## 3. The learner on Monday morning

**Who walks in:** Someone who got one useful thing out of an AI tool and then quietly stopped. Not
because it failed — because a colleague said "careful what you put in that" and they had no idea
where the line was, so they drew it at *everything*. Fear is doing more to cap Tier 1 than ignorance is.

**Observable behavior this builds** (→ `buildsBehaviors`):

1. Tier 1: follows at least one safety rule consistently, without being reminded
2. Tier 1: can state out loud what they will never paste into an AI tool, and what they do instead

**Opening activity** (plain, <5 min, real work): *The Elevator Test.* Open the last thing you pasted
into an AI tool — or the last thing you almost pasted and backed out of. Read it and mark anything
you would not read aloud in a crowded elevator.

## 4. The artifact

**Named file the learner leaves with:** `my-red-lines.md` — 3–5 lines. Each line: the thing that
never goes in + "instead, I…".

**Who reuses it, and how would we see that?** The learner, weekly, at the moment of hesitation. Reuse
is visible when a learner cites their own card in a channel ("that's a red line for me — I'll
summarize it by hand") or when A7's moments list is filtered against it. It is also the personal-tier
ancestor a coach points at when C2 (team governance) asks for the team's rules.

**Rubric** (→ frontmatter):

| Criterion | Emerging | Working | Strong |
|---|---|---|---|
| Red lines are specific | Generic restatement ("no confidential data") | Names actual document types or systems from their own work | Names the *rule that generates* the list ("anything with a customer's name in it"), so new cases resolve themselves |
| The alternative is real | Says only "don't" | Every red line has an "instead, I…" | Each alternative is something they would actually do on a Monday, not a theoretical workaround |
| It survives without the card | Long prose; needs re-reading | Short and scannable, fits one screen | Short enough to recall from memory at the moment of hesitation |

## 5. Claims and sources

| Claim the module will make | Source + date | Stable or volatile? |
|---|---|---|
| "Your organization has rules about where data may go" | The learner's own company policy — **the lesson points, never states** | Org-specific |
| "Some mistakes can't be taken back once sent" | Stable, non-empirical (no statistic attached) | Stable |
| ~~What any named vendor does with your inputs~~ | **NO SOURCE — DOES NOT GO IN** | Volatile |

**Hard guardrail for the author:** this module makes **zero claims about what any AI vendor does with
submitted data** — retention, training, or otherwise. That is volatile, vendor-specific, and unsourced;
stating it would violate the workspace's no-vendor-claims rule and would age badly inside a lesson.
The module teaches the learner to *find and follow their own org's rule*, and routes the underlying
question to `docs/open-questions.md`. No statistics of any kind. `libraryRefs`: none (rung 1, no
volatile claims by construction).

## 6. Section plan

1. **Start Here: The Elevator Test** — the opening activity above; name what they marked.
2. **The three questions that draw your lines** — plain language: *Is it someone else's to share?
   Would a leak be impossible to take back? Would I be embarrassed to be quoted?* Any "yes" is a red line.
3. **What to do instead** — the swap, not the ban: strip the names; describe the shape instead of
   pasting the content; ask about the *kind* of problem, not the case. (This is what keeps A5 from
   turning Tier 1 learners into abstainers.)
4. **Assignment** — Write `my-red-lines.md`: 3–5 red lines, each with an "instead, I…". Find and link
   your organization's actual policy (one line — where it lives). Name the one line you'd have crossed
   last month if nobody had said anything.

## Definition of Ready

- [x] Every identity field valid against `lesson.schema.json`
- [x] Staircase ancestry verified in `docs/staircase-map.md` — promotion, no leap
- [x] Rung-1 content contains zero JSON/schema/frontmatter vocabulary
- [x] Opening activity uses the learner's real work
- [x] Artifact is a named file; rubric complete
- [x] Every claim sourced+dated, or routed (vendor data-handling → open-questions)
- [x] Vocabulary tiered to the learner — no "governance," "risk tier," or "policy" as learner-facing words
