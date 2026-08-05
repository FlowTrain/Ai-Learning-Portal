# StructureView Viability Assessment — Shipping the Class With It

Assessed 2026-07-11 against `trainyard-all-repos/structureview`. Two questions: (A) can the class ship with StructView as its artifact tool, and (B) what would the Structure Mockup activity (boxes → data elements → JSON reveal) take. Short version: **A is nearly free, B is one spike PR away, and the hard parts are already built.**

## What verifiably exists today

- **Milestone 1 viewer, done and packaged.** Markdown (GFM + highlighting) and JSON (collapsible interactive tree) viewing, multi-tab, sidebar with cross-file search, live file watching, raw-source toggle, drag & drop, OS file associations. A Windows build (`out/structureview-win32-x64`, squirrel maker) exists dated 2026-07-02; electron-builder config covers nsis + **appx** (Microsoft Store path — relevant for enterprise distribution) and Linux targets.
- **Quality infrastructure that most 0.1.0 apps don't have:** jest suite across parsers/components/main/auth, coverage, `quality-gate` script (lint + coverage), prettier/eslint.
- **TIMC Light** (`src/timc-light/`, `@trainyard/timc-light`): zero-dep ESM scoring engine — **55/55 selftests passed in a Linux sandbox during this assessment**, confirming the S69 claim that it's the clean, portable win.
- **S73 spec** (governed, 4-sprint estimate): WYSIWYG spec authoring (TipTap/ProseMirror, CCQG 10-section template, EARS/Gherkin blocks, Markdown⇄ADF) + dual-LLM quality antagonist. **PR1 spike is already built** — `ui/src/pages/SpecAuthor.tsx` (live TIMC scoring as you type, autosave, Download .md), verified clean Vite build per the PR doc. The editor-engine decision is de-risked with working code, not a document.
- **Dual shell, sensible default:** desktop main process loads the built React UI (`src/renderer-dist`) when present, falls back to the vanilla renderer. Login exists as a route, **not a gate** — the viewer works without auth. Good news for Tier 1 classrooms.
- **S69 disposition** already maps what's reusable vs. prototype debris (token remap to `trainyard-design-system`, mock data flagged for discard).

## A. Shipping the class with StructView: viable now, small checklist

The viewer role needs no new code. Learners open their `.md` artifacts and any `.json` in a tool that renders both beautifully — and the JSON tree viewer is already a *soft* version of the reveal (collapse the tree = rung 2; expand = rung 3). SpecAuthor is a bonus for fluent-tier cohorts: write the C-series artifacts in-tool with live quality scores.

Classroom-build checklist (the actual gap):

1. **Distribution decision:** nsis installer vs. appx vs. plain zip of `out/`. For a client site, unsigned nsis may trip SmartScreen/endpoint policy — the appx/Store path or IT-pushed zip avoids it. (This is a client-IT conversation, not engineering.)
2. **First-run sanity pass at Tier 1 altitude:** hide/park the Login and Antagonist nav items behind a flag for the classroom build; strip the S69-flagged mock data (`Documents 5`, corpus stats) so nothing invites questions the course doesn't answer.
3. **A 1-page "install + open your first artifact" handout** — which is candidate idea #51 turned respectable: *clone/download, open folder, watch your artifact render*. A0-adjacent, zero Git ceremony required (Git can wait for the aware-eng track).

Sizing: one focused session, mostly configuration and pruning. No architecture.

## B. The Structure Mockup activity: one spike PR, pattern already proven

**The insight that makes this cheap: the canvas state IS the JSON.** The activity's data model should mirror B1D's deliverable exactly — layout regions → components → data elements → states — so the "Reveal JSON" button isn't a converter, it's a *view toggle* on state that was structured all along. The app already knows how to render JSON gorgeously; the canvas just has to produce it.

Spike shape (follow the PR1 SpecAuthor pattern precisely — it's the house style for spikes):

- **`ui/src/pages/MockupCanvas.tsx`** — new lazy-loaded route. Click-to-add region boxes on a simple grid (name + type from B1D vocabulary: header/sidebar/content/footer/overlay), click a box to add data-element chips and state tags. **No drag-drop library needed for the spike** — click-to-add + arrow-key nudge avoids new dependencies; @dnd-kit is a fast-follow if the feel demands it.
- **The reveal:** button flips the pane to the existing JSON tree renderer fed by the canvas state, with the staircase line as the caption: *"a more precise version of what you already drew."* Optional second reveal: the same state as HTML skeleton (`ui-layout-[screen].html`) — the B1D deliverable, generated.
- **Persistence:** the SpecAuthor patterns verbatim — localStorage autosave, `Download .json` / `Download .html`.
- **Deliverable alignment:** output validates against the B1D assignment (3+ regions, 3+ states, data elements per region) — meaning the class artifact and the product feature are the same object.

Sizing, honestly: **spike PR = 1–2 working sessions** (comparable to PR1, which is 266 lines + route + docs); **class-ready = one more** (empty/error states, the B1D deliverable check, tests to pass `quality-gate`). It slots into the S73 family without disturbing the 4-sprint plan — it consumes the same UI shell and ships value while the antagonist waits.

## Risks, named

- **Scope gravity.** S73 is already 4 sprints; the canvas must stay a spike-sized sibling, not become Milestone 3. The B1D data model is the scope fence — if a feature isn't needed to produce the B1D deliverable, it's placemat.
- **Dual-shell divergence.** Classic renderer and React UI both exist; the classroom build should commit to the React UI and treat the vanilla renderer as the fallback it already is.
- **Brand/token drift** (S69's blue-vs-yellow note) is cosmetic and already has a remediation plan; don't let it block a classroom build.
- **The antagonist and auth are not classroom features.** They're product roadmap. The classroom build flag should make that boundary physical.

## Recommendation

Two moves, in order: (1) cut the **classroom build** of the viewer — it's a pruning exercise on a working app, and it puts StructView in learners' hands with the B-series; (2) run the **MockupCanvas spike** as the next working session in this repo, PR1-style, with the B1D deliverable as its acceptance test. When the misconception log's build trigger fires (format-layer confusion on B1D/B4), the fix will already exist as a product feature — which is the platform eating its own cooking one more time.

*Cross-references: BACKLOG parking lot (Structure View activity, build trigger), B1D lesson (data model source), `docs/misconception-log.md` (trigger), S73/S69/PR1 docs in the structureview repo (verified sources).*
