# Misconception Log — Submissions as the Platform's Eval Set

Graded assignment artifacts are the platform's drift-detection data (see `library/evolution/evaluation-practice.md` — this is that entry applied to the curriculum itself). When the same misunderstanding shows up in multiple hand-ins, that's not a learner problem; it's a content defect found early. Log it here, fix the lesson, date the fix. Boehm's curve, pointed at ourselves: a misconception caught in a cohort costs one lesson edit; the same one caught after "graduates" spread it across an org costs a re-training program.

## How to log

One row per *pattern* (not per submission). A pattern earns a row at 2+ independent occurrences. Guard against the Waffle House menu trap in the fix column: the fix is a lesson edit, a rung re-check, or a library-entry pointer — never "add a video."

Curated seeds (a known trap logged *ahead* of a cohort) are allowed and marked as such — occurrences `0 (seed)` — but they don't trigger a fix until real hand-ins corroborate them. Promote a seed to a real pattern when it hits 2+ occurrences.

| Date spotted | Lesson | Misconception observed | Occurrences | Root cause hypothesis | Fix + date | Status |
|---|---|---|---|---|---|---|
| 2026-07-17 | A8 / A6 | **"The model knows our users."** Believes the AI understands current/specific customers, board, or domain because it "read everything." Owner's line: *"It knows the internet's past. Training-data drift is structural; your current customer is not in the weights."* | 0 (curated seed) | Mechanism gap — parametric (frozen, general) vs supplied (context) knowledge not understood | Add A8 callout: *"it knows the internet's past; your customer is not in the weights unless you put them there."* Confirm A6 lists "assumes the model knows current/specific facts" as a catchable error class. — *pending* | Open (seed) |
| 2026-08-01 | A6 / misconceptions module | **"If the AI produced it and the checks passed, it's right."** A green gate is read as proof of correctness. Owner's line: *"The gate checks what you specified. It can't check what you didn't think of."* | 0 (curated seed) | Verification gap — a passing check trusted as proof; doesn't grasp the gate only tests what was specified | Add A6 error class *"a passing check is not proof — name what it could not see"*; full treatment in the misconceptions module. — *pending* | Open (seed) |
| 2026-08-01 | A8 / misconceptions module | **"The AI learns our organization the more we use it."** Believes usage volume accrues institutional knowledge. Owner's line: *"You're not training a colleague. You're writing very good onboarding docs for a fast contractor with no memory — the docs are the asset."* | 0 (curated seed) | Mechanism gap — static weights, no learning loop from usage; improvement lives in the supplied documents | Confirm A8 states weights are frozen between sessions and improvement lives in the docs; leadership framing in the module. — *pending* | Open (seed) |
| 2026-08-01 | misconceptions module (Tier 2–3) | **"If the skill isn't working, add more detail to the instructions."** Rewrites the body of a skill that never loads; selection happens on the `description` alone. Owner's line: *"The body is what it does. The description is whether it gets asked. You've been rewriting the first one."* | 0 (curated seed) | Mechanism gap — skill selection reads only the description; the body is read after selection, or never | Module lesson (skill authoring) + the SKILL.md linter (Signalman) as the artifact check. — *pending* | Open (seed) |
| 2026-08-01 | C4 / context-file-architecture | **"Put everything in CLAUDE.md — more context is always better."** Dumps a whole "second brain" into the always-on file; the agent then spends attention on irrelevant rules every turn. Owner's line: *"Always-on context isn't free — it's read on every turn."* | 0 (curated seed) | Mechanism gap — treats always-on context as free; doesn't grasp it spends the attention budget each turn | Confirm C4 teaches the lean-file + gated-SKILL split; cite `context-file-architecture`. — *pending* | Open (seed) |

## Root-cause vocabulary (pick one, add if needed)

- **Rung leap** — lesson assumes a rung the learner hasn't climbed (check `docs/staircase-map.md` ancestry).
- **Vocabulary altitude** — Tier 3 words in a Tier 1/2 room (the curse-of-knowledge check failed).
- **Stale claim** — content contradicts current library guidance (check `libraryRefs`; the entry may have moved).
- **Ambiguous assignment** — deliverable checkable two ways; learners optimized the wrong one.
- **Internet contamination** — learner imported a pattern from the article firehose that the library deprecates (log which fossil; consider naming it in the entry's absorption notes).
- **Mechanism gap** — learner misunderstands *how* the model produces output (parametric/frozen weights vs supplied context), so they trust or distrust it for the wrong reasons. A8 is the rung-1 fix. (Added 2026-07-17 with M1.)
- **Verification gap** — trusts a passing check, gate, or "it looks right" as proof of correctness, without grasping that the check only tests what was specified. Distinct from mechanism gap: the learner understands the model fine but over-trusts the *guardrail*. (Added 2026-08-01 with M2.)

## Review cadence

At each quarterly library review: scan the log for lessons with 2+ open rows (content smell), and for root causes clustering on one vocabulary item (systemic smell). Closed rows are history — never delete them; they're the evidence the loop works.
