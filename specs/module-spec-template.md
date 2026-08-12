# Module Spec — {working title}

<!-- Copy to specs/drafts/<lesson-id>.spec.md and fill every field.
     Delete guidance comments as you go. "TBD" is allowed while drafting;
     a spec with any TBD left fails Definition of Ready. -->

## 1. Identity (maps 1:1 to lesson frontmatter)

| Field | Value | Rule |
|---|---|---|
| id | TBD | `^[A-Z][0-9]+[A-Z]?$`; letter = tier arc, suffix = role variant |
| courseId | TBD | must exist in courses.json (or name the new course this creates) |
| tier | TBD | aware / enabled / fluent / native |
| roleIds | TBD | who is this actually for — not "everyone" |
| durationMin | TBD | 15–30; if it wants more, it's two modules |
| staircaseRung | TBD | 1 plain / 2 patterned / 3 structured |

## 2. The concept and its staircase ancestry

**Concept in one sentence:** TBD

**Where does this concept already live?** (check `docs/staircase-map.md`)

- Rung 1 ancestor: TBD (lesson id, or "embedded in X's opening", or **GAP — build the ancestor first**)
- Rung 2 ancestor: TBD
- This module sits at rung ___ because: TBD

<!-- Hard rule: a rung-3 module with no rung-1 ancestor is premature. Full stop. -->

## 3. The learner on Monday morning

**Who walks in:** TBD — describe the real person at the target tier, not the aspirational one.

**Observable behavior this builds** (2 items, phrased per the maturity model — these become `buildsBehaviors`):

1. Tier N: TBD
2. Tier N: TBD

**Opening activity** (plain-language, ≤5 min, uses their real work): TBD

## 4. The artifact

**Named file the learner leaves with:** TBD
**Who reuses it, and how would we see that?** TBD  <!-- reuse is the true-north metric -->

**Rubric** (becomes frontmatter; 3 criteria × emerging/working/strong):

| Criterion | Emerging | Working | Strong |
|---|---|---|---|
| TBD | TBD | TBD | TBD |
| TBD | TBD | TBD | TBD |
| TBD | TBD | TBD | TBD |

## 5. Claims and sources (from the research scraps)

| Claim the module will make | Source + date | Stable or volatile? |
|---|---|---|
| TBD | TBD | TBD |

- Volatile claims → cite an Evolution Library entry via `libraryRefs` (name it: TBD). If no entry exists, either write the entry first or move the claim to `docs/open-questions.md`.
- Numbers with no source → they don't go in. No exceptions; this is the workspace's most-violated recovered-content rule.

## 6. Section plan (3–4 sections + assignment)

1. **Start Here: {opening activity}** — TBD
2. TBD
3. TBD
4. **Assignment** — deliverables list, each one checkable: TBD

## Definition of Ready (all boxes or it doesn't ship to authoring)

- [ ] Every identity field valid against `lesson.schema.json`
- [ ] Staircase ancestry verified in `docs/staircase-map.md` — no leap
- [ ] Rung-1 content contains zero JSON/schema/frontmatter vocabulary (if rung 1)
- [ ] Opening activity uses the learner's real work, not a synthetic example
- [ ] Artifact is a named file; rubric complete
- [ ] Every claim sourced+dated, or routed to library/open-questions
- [ ] Vocabulary tiered to the learner, not the owner (curse-of-knowledge check: read section 3 again, then section 6)
