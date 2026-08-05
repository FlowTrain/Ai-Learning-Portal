# Module Spec — Catching the Moment: Where AI Fits in Your Week

> **Why this spec exists:** `docs/maturity-model.md` names *"Often forgets AI could help ('I didn't
> think of using it for that')"* as a defining Tier 1 observable, and **habit formation** as a Tier 1
> program pillar. Neither has a lesson. The staircase map's concept table has **no row** for noticing —
> this module creates the rung-1 ancestor for a concept the model names and the catalog never taught.
> It is the lesson that makes Level 1 compound instead of decay.

## 1. Identity (maps 1:1 to lesson frontmatter)

| Field | Value | Rule |
|---|---|---|
| id | A7 | aware arc, no role variant |
| courseId | aware-foundations | **also add to `aware-eng` lessonIds** |
| tier | aware | |
| roleIds | pm, coach, designer, leader, engineer, tl, data | all seven |
| durationMin | 25 | |
| staircaseRung | 1 | plain; a noticing habit, no tooling |
| creditHours | 1 | |

## 2. The concept and its staircase ancestry

**Concept in one sentence:** The moment where AI would help does not announce itself — so you attach
it to something in your week that already does.

**Where does this concept already live?** (`docs/staircase-map.md`)

- Rung 1 ancestor: **GAP — none exists.** No concept row covers noticing/triggering. Closest
  neighbours are A0 (one task, once) and A4 (which tool, once you've decided to use one). Both assume
  the learner already had the thought. **This module is the ancestor**; nothing above it is orphaned by
  building it.
- Rung 2 descendant: **A2 / A2E** — "Prompt reuse & libraries," whose rung-1 coverage is currently the
  *embedded* opening "find your repeat." A7 produces that list as a real artifact.
- This module sits at rung **1** because: the output is a list of moments from the learner's own
  calendar, in their own words. No patterns, no cards, no templates.

**Staircase note — this module repairs a known weakness.** The map flags *"Prompt reuse & libraries,
rung 1 is embedded-only."* A7's artifact **is** A2's opening activity, done properly and kept. When
this ships, update the map's rung-1 cell for that row to `A7 (standalone); A2 opening (embedded)` and
add a new concept row: **Noticing where AI fits | A7 | A2/A2E | C1**.

## 3. The learner on Monday morning

**Who walks in:** Someone who took A0, got their twenty minutes back, genuinely enjoyed it — and then
didn't open the tool again for three weeks. Not fear (that's A5). Not distrust (that's A6). They just
never had the thought again at a moment when it would have mattered. **This is the single biggest
leak at Tier 1, and it is a habit gap, not a knowledge gap.** They will not fix it with more knowledge,
which is exactly why more Level 2 on-ramps don't help them.

**Observable behavior this builds** (→ `buildsBehaviors`):

1. Tier 1: reaches for AI unprompted at least once a week — check 1 of the Monday-Morning Diagnostic
2. Tier 1: can name five recurring moments in their own week where AI fits, and what triggers each

**Opening activity** (plain, <5 min, real work): *Last Week's Repeats.* Open last week's calendar and
your sent folder. Find three things you did more than once. Not three things you'd like to automate —
three things you actually did twice.

## 4. The artifact

**Named file the learner leaves with:** `my-moments.md` — five recurring moments. Each one: the moment,
the trigger ("when I'm about to…"), and where it recurs (the meeting, the ritual, the inbox pattern).
One is flagged **this week's**.

**Who reuses it, and how would we see that?** Two clean handoffs, which is why this module isn't a
dead end:
- **The learner**, whenever the trigger fires. Reuse shows as check 1 of the diagnostic flipping to yes.
- **A2 / A2E** consume it directly — A2's opening ("find your repeat") is *already done* and on paper.
  Observable: a learner's prompt-library cards trace back to moments on this list. If they don't, A7
  didn't work.

**Rubric** (→ frontmatter):

| Criterion | Emerging | Working | Strong |
|---|---|---|---|
| Moments are recurring, not aspirational | Lists interesting or impressive tasks | Each moment demonstrably happened 2+ times last month | Each names *where* it recurs — a standing meeting, a weekly ritual, a repeating email |
| Each has a trigger, not an intention | "Use AI for emails" | "When I'm about to write the Friday update…" | The trigger is attached to a cue that already happens without willpower — it fires whether or not they remember this lesson |
| Low-stakes, honestly | Includes work that touches customers, money, or production | All five are reversible and low-risk | Names why each is low-risk, and is consistent with their own `my-red-lines.md` (A5) |

## 5. Claims and sources

| Claim the module will make | Source + date | Stable or volatile? |
|---|---|---|
| "You forget because the moment gives no cue, not because you lack knowledge" | Experiential; framed as an observation of the learner's own week, **not** as research | Stable / non-empirical |
| "Attaching a new action to an existing cue makes it fire more reliably" | **Stated as practical craft, not as science** | See guardrail |

**Hard guardrail for the author:** this lesson sits one inch from habit-formation pop science and must
not step in it. **No "studies show." No "21 days." No named researcher, no percentage, no citation to
habit literature.** The workspace rule is source-and-date or it doesn't go in, and this module does not
need it — the learner's own calendar is the evidence. If an author feels the urge to cite habit
science, that urge goes to `docs/open-questions.md` instead. `libraryRefs`: none (rung 1, no volatile
claims).

## 6. Section plan

1. **Start Here: Last Week's Repeats** — the opening activity. The list is usually boring. Boring is
   the point: boring and repeated is exactly where the twenty minutes live.
2. **Why you forget** — plain, no science: the moment doesn't announce itself. You are not
   under-informed; you are un-cued. Name it as normal, because the learner currently reads it as
   personal failure — and that reading is part of why they don't think they'll progress.
3. **Attach it to something that already happens** — the move: don't resolve to use AI more; decide
   *"when the Friday update lands in my calendar, I open the tool first."* The calendar remembers so
   you don't have to.
4. **Assignment** — Write `my-moments.md`: five moments × trigger × where it recurs. Check each against
   your red lines (A5) and cut any that cross one. Flag one as this week's. Next week, mark which
   triggers actually fired — that mark, not the list, is the lesson.

## Definition of Ready

- [x] Every identity field valid against `lesson.schema.json`
- [x] Staircase ancestry verified — this *is* the ancestor; nothing above is orphaned
- [x] Rung-1 content contains zero JSON/schema/frontmatter vocabulary
- [x] Opening activity uses the learner's real work (their actual calendar)
- [x] Artifact is a named file; rubric complete; feeds A2's opening
- [x] Every claim non-empirical or routed — habit science explicitly banned
- [x] Vocabulary tiered — "workflow," "automation," and "habit stacking" are banned words
