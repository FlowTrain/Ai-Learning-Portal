---
id: agent-skills-format
practice: Agent Skills (SKILL.md) — Authoring & Discovery
status: current
last_reviewed: 2026-08-01
review_cadence: quarterly
model_generations: [prompt-era, context-files-era, skills-era-2025]
referenced_by: [C6, C7]
curators: [platform-owner]
---

# Evolution Entry: Agent Skills — the SKILL.md Format (Prompt → Context Files → Portable Skills)

The volatile mechanics of how skills are written, selected, and discovered live here so lessons can
cite them instead of embedding claims that move. The **durable habit** (verify a skill loads; write a
description that gets selected) is taught in C6; the **current specifics** below are re-checked each
review.

## Current guidance (teach this today)

- **A skill is a directory, not a file.** The unit is `<name>/SKILL.md` — a folder named for the
  skill, containing a file named exactly `SKILL.md`. A flat `<name>.md` dropped in a skills folder is
  discovered by nothing and loads as nothing.
- **The description is the trigger, not a summary.** At startup the agent pre-loads only each skill's
  name and description (~100 tokens); the body loads *only after* the skill is selected, and selection
  is decided on the description alone. Write it as a condition — "use when the user wants to…" — not an
  identity — "a tool for…".
- **Progressive disclosure is the design.** Metadata always → body on selection → bundled files on
  demand. Keep the body focused; push reference detail to linked files.
- **Silent failure is the characteristic risk.** A vague description (never selected) or a
  misplaced/misnamed file (never discovered) fails with no error and no warning. Verify; don't assume.
- **The format is cross-vendor.** SKILL.md is an open format (agentskills.io) read by Claude and, from
  conventional directories, by GitHub Copilot, Codex, and others. Skill discipline is portable, not
  one vendor's lock-in.
- **Lint the corpus.** A read-only linter (e.g., Signalman, MIT) catches the silent failures human
  review misses — description-as-identity, trigger collisions, and flat-file near-misses.

## Eras

### Era 1 — The prompt (~2022–2023)

Capability lived in the sentence you typed. Reuse meant copy-paste; there was no artifact, no
discovery, no portability. "It works if you word it right" was the whole craft.

### Era 2 — Context files (2023–2025)

CLAUDE.md / AGENTS.md / soul.md made context durable and versioned (the C4 layer). Capability moved
from wording to written, reviewable context — but these files loaded wholesale, with no selective,
on-demand capability.

### Era 3 — Portable skills (2025–2026)

The SKILL.md format packaged a capability as a discoverable, model-invoked unit with progressive
disclosure and optional bundled code. Anthropic published the format (Oct 2025); an open standard
(agentskills.io) and cross-vendor adoption followed. Capability moved again — from "what's in my
context file" to "what the agent selects, on its own, from a library." The new engineering surface is
the **description** (the trigger) and the **discovery convention** (the filename and directory).

## Deprecated patterns (stop teaching these)

- ❌ **Description as identity** ("a tool for spreadsheets") — it cannot be selected; write a trigger.
- ❌ **Debugging the body of a skill that never fires** — the body is not read until selection; fix the
  description first.
- ❌ **Flat `<name>.md` files in a skills folder** — not discovered; use `<name>/SKILL.md`.
- ❌ **"More skills = more capability"** — overlapping descriptions collide; a bloated corpus can be
  net-negative.
- ❌ **Assuming a skill loaded** — nothing errors when it doesn't. Verify.
- ❌ **Padding a skill body with what a capable model already knows** — spend the context budget on what
  it can't derive: your conventions, your environment, post-cutoff facts.

## What survived

Era 2's core lesson survived wholesale: capability is a written, reviewable artifact, not a knack. A
skill is a context file given a trigger and a loader. C4's durable-context discipline is the parent of
skill authoring; C3's packaging is the direct ancestor. What changed is selectivity and portability —
not the principle that you write the capability down.

## Boundary conditions (where older practice is still correct)

- **A one-off task still wants a plain prompt** — packaging a single transformation as a skill is
  over-engineering.
- **Always-on project rules still belong in a context file** (CLAUDE.md), not a skill — skills are for
  selectable, triggerable capabilities, not ambient context.
- **"Author a spec" is a standard, not a skill** — a document you cite, because it has no single moment
  of activation. Not everything worth standardizing is a triggerable action.

## Signals to watch (this entry will move)

- **Discovery conventions and frontmatter keys are vendor-current and shift** — re-verify the
  filename/directory rules and which agent reads which directory against live docs before relying on
  them. (Verified 2026-08-01: discovery scans for `SKILL.md`; required frontmatter is `name` +
  `description`.)
- **Deterministic invocation is evolving** — `disable-model-invocation`, commands-as-skills; the
  "model-invoked by default" mechanic may gain more explicit-invocation paths.
- **Marketplaces / third-party skills** raise a code-intake security surface (skills can bundle
  executable code) — treat a third-party skill as third-party code.
- **BINDING vs ADVISORY governance framing** (a skill claimed as a control needs evidence it
  *operated*, not just that it was documented) — likely to formalize; feeds the planned C7.

## Sources

- Anthropic Engineering, "Equipping agents for the real world with Agent Skills" (16 Oct 2025).
- Claude Docs, "Skill authoring best practices" (context budget; description states *when* to use;
  per-model testing).
- Claude Code Docs, "Extend Claude with skills" (`.claude/skills` scanned for `SKILL.md`;
  `disable-model-invocation`; commands merged into skills).
- Agent Skills open standard — agentskills.io (format specification; cross-vendor).
- Signalman (MIT) — read-only SKILL.md linter; SK007 (description-as-trigger), SK018 (flat-file
  near-miss).
- Live-docs verification 2026-08-01 (discovery = `<name>/SKILL.md`; required frontmatter `name` +
  `description`).
