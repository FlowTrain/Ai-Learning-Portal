# Work Order — AI Learning Platform: Level 1 Expansion + Submission Loop (local-first)

> **A cold-start hand-off.** A fresh agent (Claude Code, or Dispatch as a proof-point run) should be
> able to execute this without the owner in the room. **Five activities, ordered small → big, each
> independently shippable.** Every activity **must leave `python app/build.py` green.** If you can't
> keep the build green, stop and report — do not ship drift.
>
> Prepared 2026-07-17 from decisions recorded in `docs/submission-loop-plan.md` §8 and the Level 1
> expansion specs in `specs/drafts/`. Route to Claude Code, or hand to Dispatch (see §7).

## 0. How to start (context contract — read these, in this order, then stop reading)

Pin only what you need. Do not read the whole workspace; context rot is real and this repo is large.

1. **`CLAUDE.md`** + **`.claude/soul.md`** (root) — the constitution. Hard rules, persona, the
   curse-of-knowledge guardrail. **Non-negotiable and load-bearing here.**
2. **`docs/maturity-model.md`** — the spine. Required before *any* curriculum work.
3. **`specs/drafts/A5-red-lines.spec.md`, `A6-did-it-get-it-right.spec.md`,
   `A7-catching-the-moment.spec.md`, `A8-why-it-says-what-it-says.spec.md`** — Activity 1's contracts.
   Build what's specified; do not re-derive.
4. **`docs/submission-loop-plan.md`** — Activities 2–5. §1.1 (local-first), §3 (judge constitution),
   §4.1–4.3 (calibration + model selection), §5.1 (red-lines collision), §8 (decisions).
5. **`docs/program-catalog.md`** — only for the counts you'll update in Activity 1.

That's the contract. Everything else is retrieved just-in-time, per activity.

**Do NOT read `research/client-confidential/`.** It is day-job material under a publication
prohibition. Nothing in it enters content, ever. It is not context for this work order.

## 1. Guardrails (non-negotiable)

**Content integrity**
- **Source of truth is `content/lessons/*.md`.** `app/dist/` is a build target — **never edit it**.
- **`python app/build.py` green after every activity.** Invalid frontmatter must fail the build.
- **Tier 1 contains no JSON, no schemas, no code, no agentic tooling.** Each spec carries a
  **banned-words list** — honor it exactly. This is the workspace's #1 documented risk.
- **No invented statistics. No vendor claims. No "studies show" without a source and a date.**
  Unsourced claims go to `docs/open-questions.md`, not into a lesson.

**Assessment posture**
- **Assessment is artifacts + observed behaviors — never quizzes.** The judge and the worksheet emit
  **emerging / working / strong + evidence + exactly one next step.**
- **Never a score. Never a percentage. Never pass/fail.** "Emerging" is a position on a staircase.
- **NEVER build ranking, leaderboards, streaks, badges, or cross-learner comparison.** Standing
  prohibition, owner-stated: *"the over-my-dead-body feature that will not happen."* Not a backlog
  item — a prohibition.
- **Rubrics load from lesson frontmatter.** Never hardcode criteria; feedback must not be able to
  drift from the lesson it grades.

**Safety / privacy**
- **The UI names people by function, never by department.** *"Your coach sees this"* — **never
  "L&D."** (L&D *are* the coach group; the word is the risk, not the people.)
- **Show the learner their own red-lines rule at the point of paste** (A5). The platform must obey the
  lesson it teaches.
- **Nothing deploys.** Loopback (`127.0.0.1`) only. **Operator's own AWS credentials only.**
  **No AWS credentials in the browser, ever** — that's the whole reason for Activity 4's design.
- **Model id comes from config, sourced from the gatekeeper.** Do not guess it, do not hardcode it,
  pin it.

**Process**
- **Per-activity commits.** One activity = one focused commit/PR. No mega-commits.
- **If a decision is genuinely the owner's, stop and log it** (`[NEEDS OWNER]`) — don't guess.

## 2. Activity 1 — Author A5–A8 from spec · SMALL · ✅ **DONE 2026-07-17**

> **✅ COMPLETE.** Owner approved all four specs 2026-07-17; authored the same session. **A8 shipped** —
> it held to the mechanism-only stop condition (no capability claims, no era comparison; taught as
> *"it writes what plausibly comes next, based on what's in front of it"* + three consequences), so the
> A6 fallback was not needed. Build green: **32 lessons, 8 courses**. Banned-word and JSON/schema greps
> clean on all four. Level 1: **5 lessons / ~110 min / 3 plain → 9 / ~195 / 7 plain**.
>
> Retained below as the record of what was built and why. **Next agent starts at Activity 2.**

**Why first:** self-contained, proves the loop (spec → lesson → validate → build → commit), and it's
the thing the cohort actually asked for.

**~~GATE — `[NEEDS OWNER]`~~ — cleared 2026-07-17: owner approved A5–A8 and the proposed sequence.**

**Do:**
- Build **A5, A6, A7** from their specs — frontmatter exactly per each spec §1, sections per §6,
  rubric per §4, `buildsBehaviors` per §3. Validate against `content/schemas/lesson.schema.json`.
- **A8 carries its own stop condition** (spec §5): it must teach the mechanism **without any capability
  or "what changed since 2022" claim.** If the draft can't hold to mechanism-only, **cut A8** and fold
  its two mechanism sentences into A6 (A6's spec §5 already declares this fallback). **Judge at draft
  review — this is expected, not failure.**
- **Wire `content/courses.json`** — add the new ids to **both** `aware-foundations` and `aware-eng`
  `lessonIds` (these lessons are role-agnostic; same pattern as A0/A1/A4). Order:
  **`A0 → A8 → A5 → A6 → A7 → A1 → A2 → A3 → A4`** (win → understand → safe → trusting → habitual →
  existing skill-building). Ids stay stable; order is data. Update `totalCredits`: **4.5 → 8.5** with
  all four, **7.5** if A8 is cut.
- **Update `docs/staircase-map.md`** per each spec's staircase note: the rung table; Safety row rung-1
  → `A5 (standalone); A0 (embedded hook)`; Checking-output row rung-1 → `A6 (standalone); A0
  (embedded hook)`; **D1's ancestry row** (it currently traces to A0's embedded mention); prompt-reuse
  rung-1 → `A7 (standalone); A2 opening (embedded)`; **add a new concept row: Noticing where AI fits |
  A7 | A2/A2E | C1**; Context-for-AI rung 1 → `A0, A4, A8 (the why)` if A8 ships.
- **Update `docs/program-catalog.md`** — Level 1 class tables and the **Catalog Health** table
  (5 lessons/~110 min/3 plain → 9/~195/7, or 8/~175/6 without A8).
- `python app/build.py` → clean.

**Acceptance:**
- [ ] Each new lesson validates; `staircaseRung: 1`; **zero JSON/schema/technical vocabulary**; each
      spec's banned words absent (grep them)
- [ ] Opening activity uses the learner's real work, not a synthetic example
- [ ] Artifact + rubric present per spec; assignment deliverables checkable
- [ ] `courses.json` order + credits correct; both courses updated
- [ ] Staircase map + catalog updated; no rung-3 lesson left with a broken ancestor row
- [ ] `python app/build.py` green
- [ ] Commits: `feat(content): add A5 red lines`, `…A6 checking`, `…A7 moments`, (`…A8 mechanism` or
      `docs: cut A8 per spec stop condition — fold mechanism into A6`)

## 3. Activity 2 — Submission export + coach worksheet · SMALL · no backend
### ⚠️ STATUS 2026-07-17: code written, **`app/dist/index.html` needs one local rebuild**

> **Written and on disk** (`app/template.html`): the hand-in panel on every lesson page, the red-lines
> reminder wired to the learner's own A5 artifact, the coach worksheet at `#/worksheet`, nav + router,
> `store.subs()` / `store.redlines`, import/export.
>
> **NOT verified by a build.** The authoring sandbox held a stale, truncated cache of `template.html`,
> so the builds run from it compiled a corrupt `dist` — and `build.py` didn't notice, because it
> validated content and never its own template. **`build.py` now validates the template** (missing
> placeholders, missing closers, doesn't end in `</html>` → hard fail).
>
> **To finish: run `python app/build.py` locally.** It will either print `OK: 32 lessons…` (and the
> current broken `dist` is replaced with a good one) or fail loudly and tell you what's wrong. The
> source of truth — `template.html` — is correct and complete on disk.
>
> **Still unverified until that build runs:** JS syntax, and the acceptance boxes below. Treat them as
> claimed, not proven.

**This is BACKLOG 10 exactly as originally scoped — and per §1.1 of the plan it is now also the
interim product.** It ships value even if everything below is cancelled, and it produces the gold set
Activity 5 depends on.

**Do:**
- On the lesson page, a **Submit** action packages **{artifact + that lesson's frontmatter rubric +
  lessonId + date}** into an exportable file. Same `localStorage` + export pattern as the existing
  interest capture (`content/teasers.json` flow) — **no accounts, no server, no notifications.**
- **Red-lines reminder at the point of paste** — the learner's own A5 rule, inline, not a policy link.
- **Coach grading worksheet:** renders the rubric with an **emerging / working / strong** picker per
  criterion + **one** free-text *"misconception observed"* field. Graded exports accumulate.
- Copy says **"your coach"**. Never "L&D".

**Acceptance:**
- [ ] A learner can package any assignment artifact from any lesson page
- [ ] A coach can grade it against the frontmatter rubric **without leaving the worksheet**
- [ ] Rubric is read from frontmatter — not duplicated, not hardcoded
- [ ] No score/percentage/pass-fail anywhere in the UI
- [ ] Red-lines reminder present at paste
- [ ] `python app/build.py` green. Commit: `feat(app): artifact submission export + coach worksheet`

## 4. Activity 3 — The judge's constitution + offline runner · MEDIUM

**Spec:** `docs/submission-loop-plan.md` §3. **Read it before writing a prompt.**

**Do:**
- **`app/judge/soul.md`** — the judge's governed identity, versioned, reviewed as a document. It must
  encode: pinned to the **learner's** tier (not the owner's — this is the curse-of-knowledge risk
  aimed at the most fragile population); names what works **first**, specifically; **exactly one** next
  step; **never** a score/grade/pass-fail; **"emerging" never appears without the concrete move to
  "working"**; every judgment **quotes the learner's own artifact** as evidence; refuses to invent —
  if the artifact is empty/off-topic/unreadable, say so and ask, do not hallucinate a grade.
- **Rubric → prompt assembly:** loads the lesson's frontmatter rubric + the artifact + `soul.md`.
  A script, runnable **offline** against saved exports from Activity 2. **No UI, no service, no
  network required** for assembly — the model call is behind an interface and may be stubbed.
- **Output shape (fixed):** per criterion `{level, evidence_quote}` + one `next_step`. Structured,
  parseable, and the same shape the box will render in Activity 4.

**Acceptance:**
- [ ] `app/judge/soul.md` is reviewable prose a human can approve — not a prompt buried in code
- [ ] Runner consumes an Activity 2 export and emits the fixed shape with a stubbed model
- [ ] Rubric comes from frontmatter; changing a lesson's rubric changes the judge with **no code edit**
- [ ] `python app/build.py` green. Commit: `feat(judge): constitution + offline rubric-anchored runner`

## 5. Activity 4 — Local loopback service + the box · MEDIUM

**Architecture is decided** (`submission-loop-plan.md` §1.1): **local-first.** Nothing deploys.

**Do:**
- **Small Python service** (matches the `build.py` toolchain): serves `app/dist/index.html` **and**
  exposes one endpoint — `POST /api/feedback {lessonId, artifact}` → Activity 3's assembly → Bedrock →
  the fixed output shape.
- **Bind `127.0.0.1` only.** Signs with the **operator's local AWS credentials/SSO**. No credentials
  reach the browser. **`[NEEDS OWNER]` — the model id / inference profile** comes from the gatekeeper
  or the owner's Claude config; put it in config, **do not guess, do not hardcode**.
- **Rate limit + a hard cost ceiling on day one**, not later.
- **The box (smallest possible UI):** paste or upload → **red-lines reminder** → feedback panel
  rendering the fixed shape. **A-series lessons only** for the first pass.
- Design the endpoint so the **only** change for a future deployed service is moving credentials from a
  laptop to an IAM role. Nothing else should have to move.

**Acceptance:**
- [ ] Service runs locally; app loads from it; round-trip works on a real A-series artifact
- [ ] **Never binds beyond loopback**; no credential appears in any client-side asset (grep the bundle)
- [ ] Model id from config; cost ceiling + rate limit enforced and tested
- [ ] Feedback renders as level + evidence + one next step. **No score anywhere**
- [ ] `python app/build.py` green. Commit: `feat(app): local loopback judge service + submission box`

## 6. Activity 5 — Agreement test harness · GATE · **do not ship the judge**

**The judge does not go to a cohort until it agrees with the owner.** (`submission-loop-plan.md` §4.1
— coaches are Monday-morning themselves and **cannot** produce a gold standard; the owner is the only
calibrated human in the system.)

**Do:**
- **Harness:** takes the owner's hand-graded gold set + runs the judge over the same artifacts →
  **per-criterion agreement report**.
- **Gate rule:** exact-match rate per criterion **`[NEEDS OWNER]` — the owner sets the number** — plus
  the hard rule: **never off by two.** Emerging-vs-working is a conversation. **Emerging-vs-strong is
  disqualifying.**
- **Model selection is the same test** (§4.3): run **Opus 4.8**, **Sonnet**, and **Haiku** against the
  same gold set; report agreement **and token cost per artifact**; **recommend the cheapest model that
  clears the threshold.** Grading is every learner × every lesson — that's where the bill lives.
- **Report disagreements as data, not noise.** A disagreement means either the judge is wrong **or the
  rubric is ambiguous** — and an ambiguous rubric is a content defect found for free.

**Acceptance:**
- [ ] Harness runs against a gold set and emits a per-criterion agreement report + cost per artifact
- [ ] Never-off-by-two implemented as a hard fail, independent of the exact-match threshold
- [ ] Three-model comparison table produced
- [ ] **The judge is NOT enabled for any cohort.** Report only. Owner decides.
- [ ] `[NEEDS OWNER]` logged: gold set (owner-produced), threshold number, gold-set size (5–8/lesson
      proposed)
- [ ] Commit: `feat(judge): agreement test harness + model selection report`

## 7. If routed to Dispatch (proof-point framing)

Success is **not** "the code works." It's: did Dispatch **respect the context contract** (§0 — didn't
over-read, didn't touch `client-confidential/`), **honor the guardrails** (§1 — build green, no score,
no ranking, no Tier-1 JSON, no credentials in the browser), **produce per-activity commits**, and
**stop-and-log** on every `[NEEDS OWNER]` instead of guessing — especially the **spec approval gate**
(§2) and the **model id** (§5)? Five for five = passed. The feature is secondary to the governance. An
agent you can trust is one that stays inside its constitution under real work.

## 8. Definition of Done (whole work order)

- Every activity's acceptance boxes checked, or `[NEEDS OWNER]` logged with the reason.
- `python app/build.py` green on the final state.
- Per-activity commits present, each scoped.
- **The judge is not enabled anywhere.** Activity 5 produces a report; shipping is the owner's call.
- No score, no ranking, no leaderboard, no Tier-1 JSON, no credentials client-side, nothing deployed.
- Nothing from `research/client-confidential/` appears in any content or code.
- Report written back (§9).

## 9. Report-back format

```
## Work Order Report — <date> — <agent: Claude Code | Dispatch>
- Activity 1 (A5–A8 from spec): DONE <which shipped> | BLOCKED — <one line>; A8: shipped | cut per stop condition
- Activity 2 (export + worksheet): DONE | PARTIAL — <one line>
- Activity 3 (judge constitution + runner): DONE | PARTIAL — <one line>
- Activity 4 (local service + box): DONE | PARTIAL — <one line>
- Activity 5 (agreement harness): DONE — report attached | BLOCKED on gold set
- Build: GREEN | RED — <if red, why>
- [NEEDS OWNER] surfaced: <list — expect at least: spec approval, model id, threshold, gold set>
- Guardrail check: no score / no ranking / no Tier-1 JSON / no client-side creds / nothing deployed — <pass|fail each>
- Commits: <hashes/messages>
- Notes / surprises: <anything the owner should know>
```

---

*Owner note: Activities 1 and 2 ship real value on their own and depend on nothing below them. If the
week goes sideways, land those two and stop — Level 1 gets its depth, coaches get the worksheet, and
the gold set starts accumulating for whenever Activity 5 becomes worth doing.*
