# Module Spec — Why It Says What It Says (The Plain Explanation)

> **Why this spec exists:** `docs/maturity-model.md` names **vocabulary** as a Tier 1 program pillar
> and describes Tier 1 learners as people who *"stopped at their 2022 mental model: AI is a chat box
> that answers"* and who *"talk about AI in terms of hype, fear, or curiosity — not as a normal work
> tool."* No lesson owns this. This module is the plain mental model that sits underneath A5 (why your
> data matters), A6 (why it's confidently wrong), and A7 (why context changes the answer).
>
> **This is the riskiest of the four Level 1 specs — see §5 before authoring.**

## 1. Identity (maps 1:1 to lesson frontmatter)

| Field | Value | Rule |
|---|---|---|
| id | A8 | aware arc, no role variant |
| courseId | aware-foundations | **also add to `aware-eng` lessonIds** |
| tier | aware | |
| roleIds | pm, coach, designer, leader, engineer, tl, data | all seven |
| durationMin | 20 | |
| staircaseRung | 1 | plain; the mechanism in kitchen-table language |
| creditHours | 1 | |

## 2. The concept and its staircase ancestry

**Concept in one sentence:** It writes what plausibly comes next based on what you gave it — and that
one sentence explains almost everything else, including why context matters and why it can be
completely wrong while sounding completely sure.

**Where does this concept already live?** (`docs/staircase-map.md`, row "Context for AI")

- Rung 1 ancestor: **A0 ("tell it three things")** and **A4 ("what does the tool read first?")** —
  both teach *that* context matters. **Neither teaches why.** This module supplies the why, which is
  what turns a rule into a mental model the learner can extend to cases we never taught.
- Rung 2 ancestor: B1 (workspace as context), B1E (context files intro)
- Rung 3: C4 (durable context as versioned contracts)
- This module sits at rung **1** because: the explanation uses no technical vocabulary whatsoever and
  its artifact is a paragraph the learner could say out loud to a skeptical colleague.

**Staircase note:** A8 does not add a concept row; it deepens rung 1 of "Context for AI" from *rule* to
*reason*. Update that cell to `A0, A4, A8 (the why)` when it ships.

## 3. The learner on Monday morning

**Who walks in:** Someone who is either quietly afraid of AI or quietly contemptuous of it, and both
stances come from the same place — **not knowing what the thing actually is.** They have heard it
called magic and heard it called autocomplete, and neither helps them decide whether to use it on
Tuesday. They are also, frequently, the person who says "I don't think I'll ever really get this,"
which is the exact sentence behind the cohort feedback that produced this spec.

**Observable behavior this builds** (→ `buildsBehaviors`):

1. Tier 1: talks about AI as a normal work tool rather than as hype or threat
2. Tier 1: can explain in plain words why giving it more context changes the answer

**Opening activity** (plain, <5 min, real work): *Finish the sentence.* Write down how you'd currently
finish: "AI is basically a ______." Keep it. At the end of the lesson you'll write it again, and the
gap between the two is the whole point.

## 4. The artifact

**Named file the learner leaves with:** `my-90-second-explanation.md` — a short plain-language
explanation, in the learner's own words, that they could give to a skeptical colleague without using a
single technical term.

**Who reuses it, and how would we see that?** The learner, the next time someone at their table says
"isn't that thing just making it up?" Reuse is visible when a Tier 1 learner explains AI to *another*
Tier 1 learner — which is the cheapest scaling mechanism the program has, and the clearest signal the
hype/fear framing has broken. Coaches should watch for it in cohort chat.

**Rubric** (→ frontmatter):

| Criterion | Emerging | Working | Strong |
|---|---|---|---|
| Plain language | Uses borrowed technical words ("model," "trained," "algorithm") without owning them | No technical vocabulary; a non-technical colleague would follow it | Uses an analogy from the learner's *own* domain, not one we supplied |
| Explains the "why," not just the "what" | Describes what AI does | Explains why more context changes the answer | Also explains why it can be confident and wrong — one mechanism, both consequences |
| Neither hype nor fear | Reads as sales copy or as warning | Matter-of-fact; names a real use and a real limit | A skeptic would find it fair and an enthusiast would find it honest |

## 5. Claims and sources — **read before authoring**

| Claim the module will make | Source + date | Stable or volatile? |
|---|---|---|
| "It produces text that plausibly follows from what it was given" | Stable characterization of the mechanism; no capability or performance claim attached | **Stable** |
| "It isn't looking things up unless you gave it something to look at, or connected it to something" | Stable, mechanism-level | **Stable** |
| "That's why more context changes the answer, and why it can be fluent and wrong" | Follows from the two above | **Stable** |
| ~~What models can/can't do now vs. 2022; any capability comparison~~ | **NO — DOES NOT GO IN** | **Volatile** |
| ~~Any statistic, benchmark, parameter count, or vendor capability~~ | **NO — DOES NOT GO IN** | **Volatile** |

**The risk, stated plainly:** the obvious way to write this lesson is *"here's what changed since
2022"* — and that framing is a **volatile-claims trap**. Capability comparisons age in months, and the
workspace rule is that volatile claims live in Evolution Library entries and are cited via
`libraryRefs`, never embedded. **No Evolution Library entry currently covers model-capability eras**,
and every existing entry is rung-2/3 altitude, so a rung-1 lesson cannot cite its way out of this.

**Therefore this module is scoped to the mechanism, not the timeline.** The learner's outdated 2022
mental model gets corrected by *understanding how the thing works*, which is durable, rather than by
*being told what's new*, which will be stale before the second cohort. `libraryRefs`: none.

**Author's stop condition:** if the draft cannot teach the mechanism without a capability claim, **do
not force it** — cut A8 and redistribute its two sentences into A6 (which already declares a fallback
for exactly this). A5, A6, and A7 stand alone without A8; A8 makes them cohere. It is the most
valuable of the four *and* the most likely to fail its own gate. Judge it at draft review, not now.

## 6. Section plan

1. **Start Here: Finish the sentence** — "AI is basically a ______." Collect it; don't correct it yet.
2. **The one thing it does** — plain: it writes what plausibly comes next, given what it has in front
   of it. That's the whole mechanism. No vocabulary, no diagrams, no math.
3. **Everything else follows from that** — three consequences, each one sentence: more context changes
   what "plausibly comes next" means (→ A0, A4); it can be smooth and wrong, because smooth is what
   it optimizes and true is not the same thing (→ A6); what you hand it is what it works from, so what
   you hand it matters (→ A5).
4. **Assignment** — Write `my-90-second-explanation.md` in your own words, no technical terms, using an
   analogy from your own work. Then rewrite your opening sentence. If the two are identical, the lesson
   failed and we want to know.

## Definition of Ready

- [x] Every identity field valid against `lesson.schema.json`
- [x] Staircase ancestry verified — deepens rung 1 of an existing row; nothing orphaned
- [x] Rung-1 content contains zero JSON/schema/technical vocabulary
- [x] Opening activity uses the learner's own current mental model
- [x] Artifact is a named file; rubric complete
- [ ] **Every claim sourced+dated, or routed** — ⚠️ **the gate to watch.** Passes only if the draft
      holds to mechanism-only. Any capability or era claim fails this spec. Re-check at draft review.
- [x] Vocabulary tiered — "model," "training," "parameters," "LLM," "transformer," "hallucination" are banned words
