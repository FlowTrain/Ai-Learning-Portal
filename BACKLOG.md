# BACKLOG — Build Queue for Cowork Sessions

Ordered by leverage. Each item is sized to one or two Cowork working sessions and has acceptance criteria.

## 1. Tier 1 Monday-Morning On-Ramp (highest leverage — largest audience, weakest asset)
Rewrite the A-series openings to staircase rung 1 and add an emotional-first-win opening lab ("this saved me 20 minutes") before any pattern vocabulary.
**Accept when:** A1–A4 each tagged `staircaseRung`, open with plain-language activity, contain zero JSON/schema references at rung 1; a new `A0` first-win lab exists (15 min, one artifact, one safety rule).

## 2. Staircase audit of the full catalog
Tag every lesson with `staircaseRung` and `buildsBehaviors`; verify every rung-3 lesson has its rung-1/2 ancestors; fix gaps.
**Accept when:** all 23+ lesson frontmatters validate against `lesson.schema.json` including the new fields; a `docs/staircase-map.md` table shows every concept × three rungs with no holes.

## 3. Evolution Library entries 2 and 3
`structured-outputs` and `context-engineering` per the founding-entries list in `docs/curation-model.md`.
**Accept when:** both entries validate against the schema, include all seven required sections, and are cited via `libraryRefs` from at least two lessons each.

## 4. Placement diagnostic as intake flow
Turn the five Monday-Morning Diagnostic checks into an intake experience (app screen or facilitated worksheet) that routes a person to a course.
**Accept when:** diagnostic yields a tier + recommended course id for any answer combination; ambiguous combinations route to the lower tier by rule.

## 5. Leader literacy micro-track (3 lessons)
Tier 4 *literacy* for leaders: fund it, govern it, measure it — explicitly not the architect track.
**Accept when:** three D-prefixed lessons targeted `[leader]` exist with artifacts (an AI investment one-pager, a risk-tier policy draft, a maturity-metric dashboard spec).

## 6. Tier 4 architect track depth
Expand D1–D4 with real case studies (platform build, eval harness, governance drill) and a capstone: design an evaluation harness for one team workflow.
**Accept when:** each D lesson has a case study section and an artifact-producing assignment with rubric.
**Status 2026-07-10: deferred by owner decision** — current population is overwhelmingly Tier 1 (confirmed by field contact + diagnostic distribution). Interim: interest-gathering stubs shipped (`content/teasers.json`, 7 clickable coming-soon modules incl. topics mined from the Quantic MSAIE Nov-2027 cohort syllabus); build triggers and demand metrics defined in `docs/interest-capture.md`. Build modules in notify-me registration order from Tier 3 placements, not owner preference order.

## 7. Rebuild the app from content source
The prototype compiled content into the bundle. Re-point the app to read `content/` at build time so lessons are edited as Markdown, never in code.
**Accept when:** changing a lesson .md and rebuilding updates the app with no code edits; catalog data loads from `roles.json`/`courses.json`.
**Done 2026-07-10.** `app/build.py` + `app/template.html` → `app/dist/index.html` (single file, no server). Verified: content edit → rebuild → app updated with zero code edits; catalog from JSON; invalid frontmatter fails the build. Includes diagnostic intake, Evolution Library viewer, and architect-zone teaser cards with localStorage interest capture + export.

## 8. Cohort kit generator
A script/skill that assembles any tier-bridge course into the 4-week facilitated format (3 assignments/week + live session plan) from lesson source — the Unified Coach Guide becomes one *output* of the platform rather than a separate document.
**Accept when:** running the generator on `fluent-chains` reproduces a recognizable coach-guide structure.
**Note 2026-07-10:** borrow the Quantic MSAIE cohort rhythm — scheduled check-in weeks, an explicit break week, and a capstone showcased as a public artifact (their GitHub-repo requirement is our reuse metric in credential form).
**Done 2026-07-10.** `app/generate_cohort_kit.py <course-id>` → `cohort-kits/<course-id>-cohort-kit.md`. Verified on fluent-chains against the original bundle's structure (15-point checklist: overview/norms/not-covered, at-a-glance calendar, 2 assignments/week A+B, role-stretch notes from roles.json, biweekly 4-segment debriefs with rubric-anchored critique, facilitator prompts, showcase finale with reuse contracting, misconception-log feed). **Cadence decision recorded:** bundle DNA won over the docs' "3/week + weekly 60-min" description — 2 async assignments/week (A = opening activity on real work, B = the artifact) with peer critique inside biweekly debriefs; Quantic rhythm applied by length (check-in at 5+ content weeks, break at 6+, showcase always). Also generated: leader-literacy, aware-foundations kits.
**Accelerated profile added (owner request, 2026-07-10):** `--profile accelerated` — 4 touchpoints/week: 3 lessons as individual assignments (~45 min each: opening move + artifact) + 1 weekly 60-min session (Wins → **group activity: artifact swap** → rubric critique → next). ~3 hrs/week, for cohorts with dedicated learning time; kit itself warns to use the standard profile if the cohort only has ~1 hr/week. fluent-chains compresses to 2 weeks. Showcase finale kept in both profiles.

## 9. Product strategy strand (added 2026-07-10, owner critique)
The catalog teaches product people to *use* AI (B-series) but not how AI changes *product work itself*: discovery, business-casing, roadmapping, and shift-left economics. Development-centric drift — the same bias now named in the curation model. Candidate lessons: AI-assisted discovery without discovery cosplay (B-tier, cites `ai-product-discovery`); the AI business case (B/C-tier, cites `ai-business-cases`, feeds D5); shift-left with specs and evals — Boehm's curve for product teams (C-tier, cites `shift-left-economics`); regulated-industry AI literacy (cites `regulatory-practice`; owner's Black Box material is the case study).
**Accept when:** at least 3 lessons exist citing the second-cohort library entries, staircase-mapped with existing B/C ancestry; enabled-pm course grows or a strategy micro-track ships.
**Depends on:** second-cohort library entries graduating from Propose to Published (`specs/drafts/`).
**Progress 2026-07-11:** `shift-left-economics` and `ai-product-discovery` drafted and published (Challenge step pending), cited by B3/C5/D5 and B2/B2D respectively. Remaining entries are owner-owned: `regulatory-practice` (Black Box material) and `ai-business-cases` (client-site evidence). Lesson authoring unblocks when the owner blesses the two drafts or writes his two.

## 10. Submission & feedback loop (added 2026-07-10, restored from original scope)
The prototype had it; the rebuild dropped it: learners hand in assignment artifacts, get rubric-anchored feedback. The side effect is the real prize — submissions are the platform's own eval set. Recurring misconceptions in hand-ins are content defects found early (shift-left applied to the curriculum); patterns feed `docs/misconception-log.md`, which drives content revision.
**Waffles-and-eggs scope (the Waffle House menu trap guard):** no backend, no video, no infographics. In-app "submit" packages the artifact + the lesson's rubric into an exportable file (same localStorage/export pattern as interest capture); a coach grading worksheet renders the rubric with an emerging/working/strong picker + one free-text "misconception observed" field; graded exports accumulate in the misconception log at review cadence.
**Accept when:** a learner can package any assignment artifact for submission from the lesson page; a coach can grade it against the frontmatter rubric without leaving the worksheet; `docs/misconception-log.md` has its first three real entries and at least one has triggered a content edit (the loop demonstrably closed once).
**Explicitly out of scope until demanded:** accounts, notifications, automated/LLM grading (that's the eval-harness capstone's job, later, with a calibrated judge).
**TRIGGER FIRED 2026-07-15 — the "until demanded" clause is spent.** Cohort asked for a paste/upload box with Claude giving feedback; org constraint is **Bedrock SDK only**. This breaks two guards above: (a) **"no backend" is now impossible** — Bedrock signs with AWS creds (SigV4), which cannot live in `app/dist/index.html`; (b) LLM grading moves from "later" to "now," so the **calibrated judge** requirement becomes load-bearing rather than aspirational. Full analysis, options, judge constitution, calibration path, the A5 red-lines collision, and the owner decision log: **`docs/submission-loop-plan.md`**. **Step 1 of that plan is this item as originally scoped** (worksheet + export, no backend) — it produces the judge's calibration set and ships value even if the service is declined.

## 11. Level 1 depth expansion (added + done 2026-07-17, cohort feedback)
Learners reported "not enough Level 1 content" — and the stated reason was the finding: *they don't believe they'll make it past this stage*. Diagnosis (`docs/program-catalog.md`, Catalog Health): population is a steep pyramid, the catalog was flat, only 3 of 5 Level 1 lessons were plain-language, and **A0 was carrying the rung-1 ancestor slot for both "Safety & governance" and "Checking AI output" by itself** — the two things a nervous beginner needs most, sharing one sub-section of a 15-minute hook. Level 1 read as a waiting room; learners expect it to be a destination.
**Fix: depth at the plain rung, not more on-ramps to Level 2.**
**Done 2026-07-17** via the spec pipeline (`specs/drafts/A5–A8`): **A5** The Red Lines (safety, promoted standalone), **A6** Did It Get It Right? (checking, promoted standalone), **A7** Catching the Moment (**new concept row** — `maturity-model.md` names "often forgets AI could help" as a defining Tier 1 observable and nothing taught it; its `my-moments.md` artifact is also A2's opening activity, repairing the embedded-only prompt-reuse rung), **A8** Why It Says What It Says (the vocabulary pillar; passed its mechanism-only stop condition, so the A6 fallback was unused).
**Result:** Level 1 = 5 lessons/~110 min/3 plain → **9 lessons/~195 min/7 plain**. Both aware courses ordered `A0 → A8 → A5 → A6 → A7 → A1 → A2 → A3 → A4` (win → understand → safe → trusting → habitual → skills); `totalCredits` 4.5 → 8.5. Staircase map, catalog, and CLAUDE.md updated. Build green (32 lessons). Banned-word + JSON/schema greps clean.
**Open, not scheduled:** Level 2 has **zero** plain-language lessons — the next place this same feedback will arrive.

## 12. Rubrics for the 24 pre-convention lessons (found 2026-07-17, first real hand-in)
`CLAUDE.md` says *"rubrics live in lesson frontmatter so they version with content."* **Only 8 of 32 lessons actually have one** — and they are exactly the 8 built through the spec pipeline (A5–A8, C5, D5, D6, D7). The 24 recovered/hand-authored lessons have none, so three-quarters of the catalog **cannot be graded against criteria and cannot contribute to the judge's gold set** (`docs/submission-loop-plan.md` §4.1).
**Found the honest way:** the first real hand-in in the system was A0 — the first lesson every learner does — and it exported `"rubric": null`. The coach had nothing to grade against.
**A0 fixed 2026-07-17** (real task / time is legible / one thing they'd say differently). **23 remain.**
**Prioritize by hand-in volume, not by id order:** A1–A4 first (both aware courses, largest population, and where the Level 1 expansion just sent everyone), then B-series, then C1–C4 and D1–D4.
**Accept when:** every lesson with an assignment carries a rubric; `app/build.py` warns (not fails) on any assignment-bearing lesson without one, so this can't silently regress.
**Note the pattern — it's the argument for the pipeline:** *every* spec-built lesson has a rubric because `module-spec-template.md` §4 requires one and its Definition of Ready gates on it. Every hand-authored one lacks it. The spec pipeline isn't overhead; it's the reason the newer half of the catalog is gradeable.

## 13. Diagnostic evidence retention + coaching worksheet rework (added 2026-08-01, owner field feedback)
The placement diagnostic (#4, done) evaluates the rubric when a learner clicks "Place me," but **discards the evidence** — a coach has nothing to connect with the learner on. It should retain/package the placement evidence the way the submission loop (#10) packages artifact + rubric (localStorage + export), so a coach can pick up the conversation. Two coupled fixes on #10's coach surface: (a) the **coaching worksheet is confusing and reads like a *Coaching Session Agenda builder*** — lean into that; the owner likes the agenda-builder framing (Wins → where you are → one next step), just make it intentional; (b) **terminology: "evaluated," never "graded"** across the diagnostic and worksheet (owner preference, and truer — this is placement and coaching, not grading).
**Accept when:** clicking "Place me" persists the placement inputs + evaluated result to an exportable package a coach can open; the coach worksheet presents as a session-agenda builder rather than a grade sheet; no user-facing "grade/graded" strings remain in the diagnostic or worksheet.
**Relates to:** #4 (diagnostic intake, done) and #10 (submission loop, in flight) — this is the diagnostic half of the same coach-connection surface. App/`template.html` work; design-sensitive, so specced before edited.

## Parking lot
- Skill/SKILL.md packaging for the platform's own workflows (lesson-linter, library-entry-drafter).
- Badging/credit model review (creditHours exist in data; policy undefined).
- Analytics: which lessons produce artifacts that get *reused* — the platform's true north metric.
- **Structure View activity (owner idea, 2026-07-10).** The staircase as a UI affordance: WYSIWYG-ish mockup activity replaces the PPT — learner draws layout boxes (rung 1), drops data elements into them (rung 2), clicks a button to reveal the JSON view that was there all along (rung 3, framed as "a more precise version of what you already did"). Solves the documented "Markdown/JSON read as coded languages" reaction in the UI-surfaces track by flipping direction: produce structure spatially, *then* meet its text form. Full version = Electron app feature (owner's product roadmap); a minimal prototype (drag boxes + reveal button) is feasible in the static app as an embedded B1D/B4 activity first. **Build trigger:** misconception log shows format-layer confusion (`rung leap` / `vocabulary altitude`) clustering on B1D or B4 submissions — or the Electron Structure View ships and the class rides it. Until then: parked, per the Waffle House rule.
