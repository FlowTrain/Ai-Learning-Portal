# CLAUDE.md — AI Maturity Learning Platform Workspace

## What this workspace is
The source-of-truth for a four-tier AI upskilling platform (AI-Aware → AI-Enabled → AI-Fluent → AI-Native) serving a DPE organization: learning programs that bridge adjacent tiers, plus a curated Evolution Library that tracks how AI practices change as models change. Owner is the platform designer (Tier 4 reference persona); primary audiences are product coaches, PMs, engineers, designers, and leaders at Tiers 1–3.

## Where things live
- `docs/maturity-model.md` — the four tiers with observable behaviors, role×tier targets, placement diagnostic. **The spine; read before any curriculum work.**
- `docs/program-architecture.md` — staircase rule, asset map, delivery models, known gaps.
- `docs/curation-model.md` — Evolution Library anatomy and editorial workflow.
- `content/roles.json`, `content/courses.json` — catalog data (recovered from the app prototype).
- `content/lessons/*.md` — one file per lesson, YAML frontmatter + sections + assignment. **This is the editable source of truth; the compiled app is a build target, not a source.**
- `content/schemas/` — lesson and evolution-entry schemas. Frontmatter must validate.
- `library/evolution/*.md` — Evolution Library entries.
- `BACKLOG.md` — prioritized build queue with acceptance criteria.
- `specs/` — authoring contracts: research scraps become filled specs before becoming modules, sessions, or library entries. Templates + workflow in `specs/README.md`. Drafts live in `specs/drafts/`.
- `app/` — the build target. `python app/build.py` compiles `content/` → `app/dist/index.html`. Never edit content here.

## Conventions
- Lesson ids: letter = tier arc (A=aware, B=enabled, C=fluent, D=native), suffix = role variant (E=engineering, D=design). Keep stable; the app links on them.
- Every lesson is 15–30 min, artifact-producing, and tagged with `staircaseRung` (1 plain language, 2 patterned, 3 structured). A concept must exist at rung 1 before a rung 3 lesson may cite it as prerequisite.
- Volatile "current best practice" claims go in Evolution Library entries; lessons cite entries via `libraryRefs`, never embed the claims.
- Rubrics live in lesson frontmatter so they version with content.
- Filenames: `<id>-<kebab-title>.md`; evolution entries: `<practice-id>.md`.

## Hard rules
- Never design a lesson that leaps more than one tier. Tier 1 content contains no JSON, no schemas.
- **The staircase rule applies to the app chrome, not just the lessons.** UI copy, empty states, and prompts must not use vocabulary from a lesson the learner hasn't reached yet, and must never scold them for not having an artifact they haven't been taught to make. (Found the hard way 2026-07-17: the hand-in panel greeted a learner on lesson 1 with "You haven't saved your red lines yet" — a concept first taught in lesson 3. The curriculum honored the staircase; the chrome broke it.)
- Never treat the platform owner's level as the learner baseline — the curse of knowledge is this project's #1 documented risk (see maturity-model.md, design rule 2).
- Never delete an Evolution Library era or deprecated-pattern item; supersede with a new dated section. History is the product.
- Assessment is artifacts + observed behaviors, never quizzes.
- Do not invent maturity statistics, vendor claims, or model behaviors; unsourced claims go to `docs/open-questions.md`.

## Current focus
- ~~Tier 1 Monday-Morning On-Ramp rewrite~~ Done 2026-07-10 (A0 added; A-series rewritten/tagged).
- ~~Full-catalog staircase audit~~ Done 2026-07-10 (all 24 lessons tagged; see `docs/staircase-map.md`).
- ~~Evolution Library entries 2–3~~ Done 2026-07-10 (structured-outputs, context-engineering published and cited).
- ~~Placement diagnostic as an intake flow~~ Done 2026-07-10 (`content/diagnostic.json` + `docs/placement-diagnostic.md`; router verified exhaustively).
- ~~Leader literacy micro-track~~ Done 2026-07-10 (D5–D7, `leader-literacy` course; leader@Tier-2 route retargeted).
- BACKLOG 6 (architect depth) **deferred by owner decision** — interest-gathering teaser stubs shipped instead (`content/teasers.json`, `docs/interest-capture.md`); build in demand order.
- ~~Rebuild the app from content source (BACKLOG 7)~~ Done 2026-07-10 (`app/build.py` → `app/dist/index.html`; see `app/README.md`).
- ~~Evolution Library founding entries~~ **All six published 2026-07-10** (library complete; Challenge-step reviews pending from curator bench).
- C5 "Where Should the Answers Live?" shipped via the spec pipeline (`specs/` — first full spec→module run).
- ~~**Level 1 depth expansion (A5–A8)**~~ **Done 2026-07-17.** Cohort feedback ("not enough Level 1 content — people don't believe they'll make it past this stage") → diagnosis in `docs/program-catalog.md` (Catalog Health): population is a pyramid, the catalog was flat, and **A0 was carrying the rung-1 ancestor slot for *both* Safety and Checking-output by itself**. Fix was depth at the plain rung, not more on-ramps to Level 2. Shipped via spec pipeline: **A5** red lines (safety, standalone), **A6** did-it-get-it-right (checking, standalone), **A7** catching-the-moment (**new concept row** — "often forgets AI could help" had no lesson; its artifact is also A2's opening), **A8** why-it-says-what-it-says (the vocabulary pillar; held to mechanism-only per its stop condition). Order in both aware courses: `A0 → A8 → A5 → A6 → A7 → A1 → A2 → A3 → A4`. Level 1: 5 lessons/~110 min/3 plain → **9/~195/7**. Staircase map + catalog updated; build green (32 lessons).
- **Level 2 has zero plain-language lessons** — the next place this same feedback will come from. Noted, not scheduled.
- ~~BACKLOG 8 cohort kit generator~~ Done 2026-07-10 (`app/generate_cohort_kit.py`; kits in `cohort-kits/`).
- **Next: BACKLOG 10 (submission & feedback loop) — in flight.** Plan + recorded owner decisions: `docs/submission-loop-plan.md`. Work order: `docs/HANDOFF-level1-and-submission-loop.md` (Activity 1 done; **start at Activity 2**). Key decisions: **local-first** (loopback service, operator's creds, nothing deployed); **Bedrock/Azure-OpenAI model id from the gatekeeper — pin it, don't guess**; **the judge is the coaches' scaffold, not the learner's grader**; **the owner is the only calibrated human — he hand-grades the gold set and the judge cannot ship without passing the agreement test**; **no scores, no ranking, ever**.
- Then: BACKLOG 9 (product strategy strand, gated on second-cohort library entries), or architect-zone modules per teaser demand.

## Persona
@.claude/soul.md
