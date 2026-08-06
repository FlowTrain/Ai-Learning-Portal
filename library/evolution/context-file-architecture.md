---
id: context-file-architecture
practice: Context File Architecture (CLAUDE.md / AGENTS.md / SKILL.md across tools)
status: current
last_reviewed: 2026-08-01
review_cadence: quarterly
model_generations: [per-tool-files-era, agents-md-standard-2025, gated-skills-2026]
referenced_by: [C4]
curators: [platform-owner]
---

# Evolution Entry: Context File Architecture — Which File Owns What, Across Tools

The team question this answers: your people are on Cursor, Copilot, and Claude Code — where do the
rules live so you write them **once**, and how do the tools converge? This entry holds the volatile
who-reads-what layer. The durable idea is stable: one canonical source, thin tool-specific overlays,
and keep the always-on file lean.

## Current guidance (teach this today)

- **Three files, three loading models.**
  - **AGENTS.md** — the shared, tool-agnostic instruction file. Always-on (injected at session start).
    The emerging cross-tool standard (~30 tools read it natively).
  - **CLAUDE.md** — Claude Code's file. Always-on. Claude Code reads **this, not AGENTS.md** — Claude
    genuinely does it differently.
  - **SKILL.md** — a *gated* capability, loaded only when its description matches the task (progressive
    disclosure; see `agent-skills-format`). Not always-on.
- **One canonical source, thin overlays.** Put shared rules in AGENTS.md. Make CLAUDE.md thin: an
  `@AGENTS.md` import plus only the Claude-specific lines. (A symlink `ln -s AGENTS.md CLAUDE.md` also
  works but needs admin/Developer Mode on Windows — prefer the `@import`.) Do **not** copy AGENTS.md
  into CLAUDE.md.
- **Personal vs. project.** User-level `~/.claude/CLAUDE.md` holds *your* preferences across every
  project; the repo's AGENTS.md/CLAUDE.md holds *the project's* rules. Don't duplicate personal rules
  into the repo, or project rules into your user file.
- **Nearest-file-wins.** In a monorepo a nested AGENTS.md (e.g. `services/payments/AGENTS.md`) overrides
  the root for work in that directory — keeping each area's context tight instead of one giant file.
- **Protect the always-on budget (the "second brain" trap).** Every token in an always-on file is read
  on *every* turn and spends the model's attention. Dumping your whole knowledge base into
  CLAUDE.md/AGENTS.md is noise that degrades focus — the agent reads database lock modes while fixing a
  CSS bug. Keep always-on files lean; push situational depth into a gated SKILL.md.
- **A bridge for mixed-tool teams.** Tools that don't natively read `SKILL.md` can still benefit if a
  CI step compiles skill metadata into AGENTS.md (e.g. a "skills-to-agents" action emits a `<skills>`
  block). One source of truth; the non-Claude tools see it too.

## Eras

### Era 1 — Per-tool files (–2025)
Each tool read its own file (`.cursorrules`, `CLAUDE.md`, and whatever else). The same rules were
written several times; drift was guaranteed.

### Era 2 — AGENTS.md as the shared standard (Aug 2025 →)
OpenAI released AGENTS.md in August 2025; it was transferred to the Linux Foundation's **Agentic AI
Foundation** (late 2025, alongside MCP and goose). By mid-2026 ~30 tools read it natively and 60,000+
repos carry one — the de facto cross-tool instruction file.

### Era 3 — Gated skills alongside always-on files (Oct 2025 →)
`SKILL.md` (the agentskills.io open standard) added a *conditional* layer: capability loaded on demand,
separating "always true" (AGENTS.md / CLAUDE.md) from "true for this task" (SKILL.md).

## Deprecated patterns (stop teaching these)

- ❌ **Copying AGENTS.md into CLAUDE.md** — duplication and drift; use the `@import`.
- ❌ **One giant always-on file / "second brain" dump** — attention noise; move situational content to SKILL.md.
- ❌ **Assuming Claude Code reads AGENTS.md natively** — it doesn't (verified); it reads CLAUDE.md, and the "reads it as a fallback" claim is a myth.
- ❌ **Personal preferences in the repo file** — those belong in `~/.claude/CLAUDE.md`.
- ❌ **Hand-writing the same rule in three tools' files** — canonical source + a bridge instead.

## What survived

The core idea survived and standardized: agent behavior is governed by written, versioned files.
AGENTS.md is the era-2 generalization of CLAUDE.md; SKILL.md is its gated sibling. C4's discipline —
durable, versioned context as a contract — is the parent of all three.

## Boundary conditions (where older practice is still correct)

- **Solo / single-tool:** one CLAUDE.md is fine; the multi-file architecture earns its keep only with
  multiple tools or a monorepo.
- **Claude-only shop:** CLAUDE.md alone is enough; adopt AGENTS.md when a second tool arrives.
- **Small repo:** nested AGENTS.md is overkill until directories genuinely have different rules.

## Signals to watch (this entry will move fast)

- Whether Claude Code adds native AGENTS.md reading (currently no; `@import`/symlink required).
- AGENTS.md governance and adoption under the AAIF (170+ members, May 2026) and the native-tool count.
- SKILL.md discovery conventions (tracked in `agent-skills-format`).
- **Efficiency claims** for shared instruction files (a 2026 study reporting runtime/token reductions
  circulates in secondary posts) — **reported, not independently verified here**; cite only after
  reading the primary paper.
- "skills-to-agents"-style CI bridges as they mature.

## Sources

- AGENTS.md — OpenAI (Aug 2025); Linux Foundation **Agentic AI Foundation** stewardship (late 2025).
  https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
- agents.md — specification and native-tool list.
- Claude Code memory docs — `@import` and symlink; reads CLAUDE.md, not AGENTS.md.
  https://code.claude.com/docs/en/memory
- Agent Skills — agentskills.io (Dec 2025); see the `agent-skills-format` entry.
- Verified 2026-08-01 (AGENTS.md governance/adoption; Claude Code `@import`/symlink; the
  "reads AGENTS.md as fallback" claim debunked). Secondary-source arXiv efficiency figures are
  **deliberately not cited as fact** pending primary verification.
