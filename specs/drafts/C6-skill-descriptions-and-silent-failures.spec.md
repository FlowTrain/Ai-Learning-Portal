# Module Spec — Skill descriptions & silent failures (anchor lesson of the "Tooling Misconceptions" module)

> Source scraps: `research/` briefs *AI Tooling: Common Misconceptions* and *Skills: Five
> Misconceptions Worth Correcting* (owner, mad-at-the-day-job, 2026-08-01) + the Signalman linter
> (`trainyard-all-repos/Signalman`, MIT). This spec covers the **anchor lesson C6**; the module map
> below lists the rest. Log seeds M2–M4 already filed in `docs/misconception-log.md`.

---

## Module context — the "dedicated misconceptions module" the owner asked for

The two briefs are written for **three audiences**, and those audiences sit at **different tiers** —
so a single cross-tier course would break the no-leap hard rule. The dedicated module is therefore
scoped to the **Tier 3 (Fluent) practitioner** set — the richest, most coherent chunk (authoring
skills and specs) — and the leadership/PM misconceptions are **routed to their own tiers** as
companion lessons with their own specs.

**New course:** `tooling-misconceptions` — *"Skills & Tooling: What Actually Breaks"* (tier: fluent).
Must be added to `courses.json` when the first lesson authors.

| Lesson | Concept | Rung | Source | Status |
|---|---|---|---|---|
| **C6** *(this spec)* | The description is the trigger; a skill that isn't selected or isn't discoverable fails **silently** | 3 | AI-tooling §1.1–1.4; skills §1; Signalman SK007/SK018 | spec ready (this doc) |
| C7 | Skills as **governance, not capability** — BINDING vs ADVISORY; "writing it in the skill" is not a control (evidence it *operated*) | 3 | skills §2–§5, standards | planned (own spec) |
| C8 | The **laundering trap** — sentiment→PRD; requirement-level provenance (stated / inferred / assumed) | 3 | skills "worked failure" (genericized — no client/medical specifics) | planned (own spec) |

**Companion lessons, routed OUT of this course (different tiers):**

- **Tier 1–2 (PM / non-dev):** "the terminal problem is legibility, not aesthetics"; "you don't need
  dev workflow"; "AI replaces the *handoff*, not design"; **"a passing check isn't proof"** (already
  seeded to A6 as M2). → their own B-series/A-series specs.
- **Tier 4 literacy (leaders):** "usage teaches the model" (seeded A8/M3); "seats deployed ≠ adoption";
  "one tool as the front door for everything"; "which Copilot?" → companions in the `leader-literacy`
  course (D5–D7), their own specs.

**Hard dependency for C6/C7/C8:** an Evolution Library entry `library/evolution/agent-skills-format.md`
holding the **volatile** SKILL.md mechanics (progressive disclosure; discovery = `<name>/SKILL.md`;
cross-vendor adoption). Per the hard rule, volatile claims are cited via `libraryRefs`, never embedded.
**Write the entry before C6 ships.**

---

## 1. Identity (maps 1:1 to lesson frontmatter)

| Field | Value | Rule |
|---|---|---|
| id | C6 | `^[A-Z][0-9]+[A-Z]?$` — fluent arc |
| courseId | tooling-misconceptions | NEW course (add to courses.json) — *"Skills & Tooling: What Actually Breaks"*, tier fluent |
| tier | fluent | Tier 3 — skill authoring is the Fluent program pillar (maturity-model §Tier 3) |
| roleIds | coach, tl, engineer, pm | the people who actually author skills/specs — not "everyone" |
| durationMin | 25 | one artifact, four short sections |
| staircaseRung | 3 | works in the SKILL.md structured format + a linter |

## 2. The concept and its staircase ancestry

**Concept in one sentence:** An agent picks a skill on its `description` alone, so a vague
description (never selected) or a misplaced file (never discovered) fails **silently — nothing
errors** — and the author ends up debugging the file the agent never read.

**Ancestry (verified in `docs/staircase-map.md`):**

- Rung 1 ancestor: **A8** (mechanism — "what's in front of it": the model works from supplied text,
  not memory) and **A6** (checking — a missing/passing signal is not proof; the new M2 "verification
  gap" seed lives here).
- Rung 2 ancestor: A2 / A2E (prompt reuse patterns).
- Immediate predecessor: **C3** (rung 3 — SKILL.md packaging). C6 is a rung-3→rung-3 depth step on the
  same "prompt reuse & libraries" concept (allowed — the staircase constrains entry, not depth; same
  shape as D3→C3).
- **Sits at rung 3 because:** it operates on the structured SKILL.md contract (frontmatter description,
  filename/dir convention) and closes with a machine check (a linter).

## 3. The learner on Monday morning

**Who walks in:** a coach or tech lead who has authored a handful of skills. Some "don't seem to
work," so they've been adding detail to the bodies. They have never checked whether the skill loads
at all. Tier 3 — already curates a library; this lesson makes them *verify* it.

**Observable behavior this builds** (`buildsBehaviors`):

1. Tier 3: Curates and maintains team skills — and **verifies they actually load**, rather than
   assuming a file in the folder is a working skill.
2. Tier 3: Writes skill **descriptions as trigger conditions** ("use when…") and checks
   discoverability **before** concluding the model can't do the task.

**Opening activity** (<5 min, their real work): take one of your own skills, cover the body, and read
*only* the description. For the request it's meant to serve, would an agent pick it over the other
skills in the folder? (Then let the linter's simulator do the same in four seconds — but form the
judgment by hand first.)

## 4. The artifact

**Named file the learner leaves with:** `skill-audit.md` — a one-page audit of one real skill:
the before/after `description` (identity → trigger), a discoverability check (filename + directory),
and the linter output showing it clean.

**Who reuses it, and how would we see that?** The team skill-library owner; visible when a PR to the
skills repo cites the audit, or the linter runs in CI on the skills directory.

**Rubric** (frontmatter; 3 criteria × emerging/working/strong):

| Criterion | Emerging | Working | Strong |
|---|---|---|---|
| Description as trigger | states what the skill *is* ("a tool for X") | states *when* to use it | states when **and** declares negative scope ("do NOT use for…"), discriminating against sibling skills |
| Discoverability | didn't check load or placement | confirmed the file is named/placed to be discovered | confirmed discoverable **and** ran a linter/simulator as evidence |
| Diagnosis order | rewrote the body first | checked the description before the body | checked **load → description → body** in order and can name what each step ruled out |

## 5. Claims and sources (from the research scraps)

| Claim the module will make | Source + date | Stable or volatile? |
|---|---|---|
| An agent pre-loads only name+description; the body loads after selection | Anthropic Engineering, *Equipping agents…* (16 Oct 2025); Claude docs best-practices | **Volatile** → `agent-skills-format` entry |
| Discovery scans for `SKILL.md` in a `<name>/` dir; a flat `<name>.md` isn't discovered | Claude Code docs; agentskills.io spec (verified 2026-08-01) | **Volatile** → `agent-skills-format` entry |
| The format is read across multiple vendors' tools | agentskills.io; briefs (mid-2026) | **Volatile** → `agent-skills-format` entry |
| The description must state *when to use*, not identity | Claude docs best-practices; Signalman SK007 | Stable (principle) |

- Volatile claims → cite `library/evolution/agent-skills-format.md` (**write first — hard dependency**).
- No invented numbers. The "3 of 4 skills didn't load" observation stays an anonymized teaching
  example (no employer, no internal skill names).

## 6. Section plan (4 sections + assignment)

1. **Start Here: read your own description with the body covered** — the four-second diagnosis.
2. **The description is the trigger** — identity vs trigger; rewrite from your own words; negative scope.
3. **The failure you can't see** — the skill that never loads (wrong filename/place); nothing errors;
   the near-miss. Anonymized "3 of 4" example.
4. **Make it loud** — a linter as the check; the habit: *"what did you check, and in what order?"*
5. **Assignment** — `skill-audit.md`: (a) before/after description, (b) discoverability check,
   (c) linter output clean. Each checkable.

## Definition of Ready

- [x] Every identity field valid against `lesson.schema.json` (courseId creates a new course — noted)
- [x] Staircase ancestry verified in `docs/staircase-map.md` — no leap (A8/A6 rung-1; C3 rung-3 depth)
- [x] Not rung 1 — structured content is appropriate at Tier 3
- [x] Opening activity uses the learner's real work
- [x] Artifact is a named file; rubric complete
- [ ] **Every volatile claim routed to `agent-skills-format` Evolution Library entry — entry not yet written (hard dependency; write before authoring C6)**
- [x] Vocabulary tiered to the Tier-3 learner, not the owner
