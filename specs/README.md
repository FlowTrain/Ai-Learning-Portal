# specs/ — Authoring Contracts

Spec-driven content development: **research scrap → filled spec → generated artifact → validated build.** Nothing goes from idea to lesson without passing through a spec, the same way nothing goes from ticket to production without passing through acceptance criteria.

## The pipeline

```
learning_program_scraps.md          (raw research, conversations, syllabi, hunches)
        │  distill into
        ▼
specs/drafts/<name>.spec.md         (filled template — the contract)
        │  hand to a working session (Claude, or a human author)
        ▼
content/lessons/*.md                (or library/evolution/*.md, or a session plan)
        │  python app/build.py
        ▼
app/dist/index.html                 (schema-validated, or the build fails)
```

The spec is the unit of review. Approve the spec, and the artifact is mechanical; skip the spec, and you're vibing.

## The three templates

| Template | Turns scraps into | Downstream validator |
|---|---|---|
| `module-spec-template.md` | A lesson (`content/lessons/*.md`) | `lesson.schema.json` + build |
| `session-spec-template.md` | A facilitated cohort session / week plan | BACKLOG 8 generator (future); coach review today |
| `evolution-entry-spec-template.md` | An Evolution Library entry | `evolution-entry.schema.json` + the Challenge step |

Copy a template into `specs/drafts/`, rename it (`<lesson-id>.spec.md` or `<practice-id>.spec.md`), fill it. Every template ends with a **Definition of Ready** — the gates that mirror this workspace's hard rules (staircase ancestry, no invented statistics, artifact-producing, rubric attached). A spec that can't pass its own gates isn't ready to become content, and finding that out at spec time costs minutes instead of a wasted authoring session.

## How to run a spec in a working session

Open a session in this workspace (CLAUDE.md and soul.md load the rules automatically) and say:

> Build the module from `specs/drafts/D8-agentic-workflows.spec.md`. Validate and rebuild the app.

That's the whole interface. The session reads the spec, writes the lesson, runs the schema validation, rebuilds — and if the spec was honest, there's nothing to argue about in review except the writing.

## Parking-lot note

These templates are proto-skills. Once each has been run ~5 times with consistent results (C3's own packaging bar), promote them to SKILL.md form (`lesson-drafter`, `entry-drafter`) per the parking-lot item in BACKLOG.md.
