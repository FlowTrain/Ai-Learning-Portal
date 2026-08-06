# Module Spec — Did It Get It Right? (Checking Without Being Technical)

> **Why this spec exists:** `docs/staircase-map.md` lists **Checking AI output rung 1 = "A0 (The One
> Rule)"** — the same overloaded slot that carries safety. Verification is the maturity model's named
> Tier 1 leveling-up behavior ("always verify") and it has no lesson of its own. This module promotes
> it to standalone rung 1. Companion to A5 (which takes the safety half of A0's One Rule).

## 1. Identity (maps 1:1 to lesson frontmatter)

| Field | Value | Rule |
|---|---|---|
| id | A6 | aware arc, no role variant — checking is universal |
| courseId | aware-foundations | **also add to `aware-eng` lessonIds** |
| tier | aware | |
| roleIds | pm, coach, designer, leader, engineer, tl, data | all seven |
| durationMin | 20 | |
| staircaseRung | 1 | plain; no eval vocabulary, no metrics, no thresholds |
| creditHours | 1 | |

## 2. The concept and its staircase ancestry

**Concept in one sentence:** You can tell whether an AI answer is good enough to use without being an
expert in what it produced — by running the same short check every time instead of going on a feeling.

**Where does this concept already live?** (`docs/staircase-map.md`, row "Checking AI output")

- Rung 1 ancestor: **A0 ("The One Rule")** — embedded, and shared with the safety row. **This module
  takes ownership of the checking half.**
- Rung 2 ancestor: B2 / B2D / B3 / B3E (critique patterns, quality criteria)
- Rung 3: D1 (eval pipelines with thresholds)
- This module sits at rung **1** because: the output is three questions in the learner's own words. No
  criteria matrix, no threshold, no eval vocabulary. The word "evaluation" does not appear.

**Staircase note:** this materially strengthens D1's ancestry — D1 currently traces its rung-1
"checking output" ancestor to A0's embedded mention. Update the map's rung-1 cell to `A6 (standalone);
A0 (embedded hook)` and D1's ancestor row accordingly when this ships.

## 3. The learner on Monday morning

**Who walks in:** Two people, same lesson. One used an AI answer, thought *"seems right,"* shipped it,
and has carried a low-grade unease ever since. The other won't touch the tool because *"I can't tell
if it's making things up."* Both are stuck on the same missing skill, and both are stuck at Tier 1
because of it. Neither is going to learn statistics.

**Observable behavior this builds** (→ `buildsBehaviors`):

1. Tier 1: checks AI output against a repeatable check instead of a feeling
2. Tier 1: can name one thing AI got wrong recently and how they caught it

**Opening activity** (plain, <5 min, real work): *How Do You Know?* Take the last useful thing AI gave
you. Without re-opening the source, write one sentence: how do you know it was right? If the honest
answer is "it sounded right" — that's the lesson, and that's most people.

## 4. The artifact

**Named file the learner leaves with:** `my-check.md` — three or four questions in their own words,
plus a **"caught it" log** with the first entry filled in.

**Who reuses it, and how would we see that?** The learner runs it on AI output. Reuse is visible when
the "caught it" log has a *second* entry a week later without prompting, or when the learner names a
catch in a standup. The log is also the honest input to a coach's Tier-1→2 placement call — check 2 of
the Monday-Morning Diagnostic is about prompt shape, but a live "caught it" log is direct evidence the
learner has stopped treating output as truth.

**Rubric** (→ frontmatter):

| Criterion | Emerging | Working | Strong |
|---|---|---|---|
| The check is runnable | Abstract ("verify accuracy," "check the facts") | Three or four concrete questions answerable in under a minute | Questions target the failure modes of *their own* work, not generic ones |
| Grounded in a real catch | No example, or a hypothetical one | One real instance of AI being wrong, and how it was noticed | The catch *changed the check* — a question exists because that catch taught it |
| Honest about the limit | Implies they can always tell | Names at least one kind of error they could not catch themselves | Names who or what they would escalate that kind of error to |

## 5. Claims and sources

| Claim the module will make | Source + date | Stable or volatile? |
|---|---|---|
| "AI can be fluent and wrong at the same time; wrongness does not announce itself" | Stable, qualitative characterization — no rate attached | Stable |
| "It produces what plausibly comes next from what you gave it — it isn't looking things up unless you gave it something to look at" | Stable mechanism; the plain-language version taught in A8 | Stable |
| ~~How often models hallucinate / any accuracy or error rate~~ | **NO SOURCE — DOES NOT GO IN** | Volatile |

**Hard guardrail for the author:** no hallucination rates, no accuracy percentages, no "studies show,"
no model-specific behavior claims. The lesson works entirely on *qualitative* mechanism and the
learner's own caught example. Any rate question a learner raises → `docs/open-questions.md`. If a
future Evolution Library entry covers error characterization, add it to `libraryRefs` then; today
**`libraryRefs`: none** — the `evaluation-practice` entry is rung-2/3 altitude and citing it here would
pull Tier-3 vocabulary into a Tier-1 lesson.

**Dependency note:** the mechanism claim in row 2 is taught plainly in **A8**. If A8 ships, sequence
A8 before A6 and let A6 refer back in one plain sentence rather than re-explaining. If A8 is cut, A6
must carry a two-sentence version of the mechanism itself.

## 6. Section plan

1. **Start Here: How Do You Know?** — the opening activity; most learners write "it sounded right."
   Name that honestly; it's the normal answer, not a personal failing.
2. **Confident and wrong is the normal failure, not a rare bug** — plain, no numbers. Why fluency is
   not evidence: it produces what usually comes next, and what usually comes next is usually — not
   always — true.
3. **Your three questions** — the check: *Where would this have come from? Does it match one thing I
   already know for certain? What would it look like if it were wrong — and can I see that from here?*
   The third is the one that does the work.
4. **Assignment** — Write `my-check.md`: three or four questions in your own words. Run it once on
   something real today. Start the "caught it" log with one entry — a real time AI was wrong, and what
   tipped you off. Name one kind of mistake your check would miss, and who you'd ask.

## Definition of Ready

- [x] Every identity field valid against `lesson.schema.json`
- [x] Staircase ancestry verified — promotion out of A0's overloaded slot, no leap
- [x] Rung-1 content contains zero JSON/schema/eval vocabulary
- [x] Opening activity uses the learner's real work
- [x] Artifact is a named file; rubric complete
- [x] Every claim sourced or qualitative-stable; all rates routed to open-questions
- [x] Vocabulary tiered — "evaluation," "hallucination," "ground truth," and "threshold" are banned words
