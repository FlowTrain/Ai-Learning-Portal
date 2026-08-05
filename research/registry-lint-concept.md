# Registry-lint — one read-only referee for every fleet registry

> **Concept, for the monorepo-teardown / fleet-packaging spec (owner, 2026-07-21).** Not a spec-number
> linter — a *framework*. The fleet has many `.md`/`.json` registries with real invariants; their checks
> are scattered (some in `build.py`, some in `inbox-lint.py`, some in the staircase audit, some
> nowhere). Consolidate into one config-driven referee each registry declares its contract to. Rationale:
> **attestation ≠ compliance** — agents keep asserting registry entries (a spec number, a key) without
> validating against the register. Three incidents prove it (PRD-bridge S73/74/75 taken; SVD-S73
> collision; the phantom **S87**). Rules aren't enough; the register needs a guard the writer can't route
> past. Same lesson as the inbox linter, generalized.

## The registries and their invariants

| Registry | Canonical source | Invariant to enforce | Guard today |
|---|---|---|---|
| Spec register | `spec-instructions.md §8` | S-numbers unique, sequential, no gaps; frontmatter fields present; status valid | **none** ← S87 |
| Context keys | `FLEET-REPO-BLUEPRINTS Part 0.5` | keys unique; 2–3 char; every inbox/spec key exists here | none |
| Inbox | `inbox.md` | ≤N lines; one key; no secrets | `inbox-lint.py` ✅ |
| Evolution Library | `library/evolution/*` | **`libraryRefs ↔ referenced_by` symmetry** (bidirectional) | partial (manual) |
| Staircase map | `docs/staircase-map.md` | every rung-3 concept has a rung-1/2 **ancestor** | manual audit |
| Catalog | `courses.json`/`roles.json` | referential integrity (lessonIds exist; roleIds valid) | `build.py` (some) ✅ |
| Misconception log | `docs/misconception-log.md` | entry shape; root-cause vocab from the enum | none |
| Evidence / disposition | `*.schema.json` | payload validates; the disposition rules (no kill-on-assumption) | `ajv` (per-artifact) |
| Skill corpus | `.claude/skills/*/SKILL.md` | discoverable filename (`SKILL.md`, not flat `<name>.md`); `name`+`description` present; description states a *trigger*, not an identity; names unique; no trigger collision | **Signalman** ✅ (public, MIT) |

**Two invariant classes beyond uniqueness** — worth naming because they're where the value is:
- **Symmetry** (Evolution Library): if A cites B, B must list A as `referenced_by`. A one-sided ref is a
  broken registry, invisible today.
- **Ancestry** (staircase): a rung-3 lesson with no rung-1/2 ancestor is premature — a real content
  defect the map is supposed to catch but only a human currently does.

## The shape

One small checker; each registry ships a `registry.lint.yaml` declaring:
```yaml
source: docs/specs/spec-instructions.md   # canonical register
entries: docs/specs/S*.md                 # what it registers
id_pattern: '^S\d+$'                       # + sequential | unique | no-gaps
required_fields: [Segment, Workstream, Status, "Spec Type"]
invariants: [unique, sequential]          # or: symmetry(libraryRefs, referenced_by) | ancestry(staircaseRung)
forbid: [secrets, confidential]
```
The referee reads the config, checks the entries against the register, and **rejects** violations with a
teaching message (the `inbox-lint.py` pattern: the error *is* the instruction). Read-only — it flags,
never fixes.

## Home & rollout

- **Home:** the monorepo-teardown / fleet-packaging spec — a shared `@trainyard/registry-lint` package +
  an org `.github` reusable workflow every repo's registries opt into. Same "extract shared config,
  collapse per-repo checks to stubs" move as `@trainyard/eslint-config`.
- **Rollout:** three read-only-referee instances exist now — `inbox-lint.py` (#1, done), `spec-lint.mjs`
  (#2, closes the S87 class), and **Signalman** (#3, the skill corpus; public MIT repo, `trainyard-all-repos/Signalman`).
  Signalman is the same pattern generalized to a *set*: the skill-description corpus is a registry, its
  `description` frontmatter is the only trigger surface, SK101/SK102 are the uniqueness/collision invariants,
  and it flags-but-never-fixes. **Live-validated 2026-08-01** against a real corpus (`Quality and Testing/.claude/skills`):
  it correctly found that three "skills" were flat `<name>.md` files that don't load at all (silent vaporware —
  nothing errored), and flagged a canonical skill's non-portable custom keys. Discovery convention re-checked
  against current Claude Code + Agent Skills docs and confirmed. Two pre-release fixes noted (SK007 fix-text
  mangling; add near-miss detection for flat files under a skills dir). Evolution Library symmetry is the
  obvious #4 — highest-value invariant, still zero guard.

> **Public-product face:** the productization of this framework is captured in
> `trainyard-all-repos/AGENTIC-LINT-LIBRARY.md` — "The Lint Trap," with Signalman as the seed of a
> public `@trainyard/agentic-lint` core + per-artifact rule packs. Each registry-lint instance here
> (inbox #1, spec #2, Signalman #3, EL-symmetry #4) is one **rule pack** there.
- **Not now:** this is a captured concept feeding a future spec, not a build. `spec-lint.mjs` can be
  built standalone first to close the S87 incident; the framework waits for the teardown spec.
