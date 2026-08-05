# Fleet Middle-Tier Architecture (transcribed from owner diagram, 2026-07-11)

Transcription of the architecture image shared 2026-07-11 — the connective tissue between the shipped entry product and the in-dev platform. Legend on the original: CCQG Auditor and Dependency Graph were designed "this thread" (a separate working session); StructureView and Quality Guardian are existing fleet.

## ENTRY — SHIPPED v1.0

**StructureView · EMD SD70ACe**
File viewer · EARS detection · TIMC Light signal layer
**The mechanism line:** *Document opens → quality signal fires → upgrade CTA appears.*

Flows out: `audit trigger` → CCQG Auditor; `dep discovery` → Dependency Graph.

## MIDDLE TIER

**CCQG Auditor** (variant agent · UP 844 lineage)
- Read-only posture · **never commits**
- Domain record · cross-repo dep map
- 4-quadrant finding classification
- Segment-close artefact emission
- Outputs: `findings.json` + `.md` + `.mermaid`
- **"Not a fixer — diagnoses only"**

**Dependency Graph** (cross-repo · cross-product map)
- Upstream libs · APIs · databases
- Downstream consumers · contracts
- Shared infra · IaC · observability
- **Blast radius analysis**
- Output: `dependency-risk-map.md`
- Feeds Quality Guardian context

Auditor `feeds` → Dependency Graph.

## PLATFORM — IN DEV Q3 2026

**Quality Guardian · UP 844 · TIMC Platform**
- Q1 Traceability · Q2 Impact · Q3 Measurability · Q4 Completeness
- Release readiness · HITL sign-off · RCA/CAP · **FINRA 4511 records**
- **The evidence line:** *findings.json + dependency map → TIMC ingested as evidence.*

Flows in: `findings feed` (from Auditor) · `risk map feed` (from Dependency Graph).

## Why this diagram matters (analysis)

1. **The funnel has a mechanism now.** V5's upgrade path (StructureView → Quality Guardian) read as marketing; this diagram makes it physics: a document opening *fires a quality signal*, the signal *triggers an audit*, the audit *emits artifacts*, the artifacts *become platform evidence*. Every arrow is a file format, not a sales motion.
2. **The Auditor is D6's risk-tier governance shipped as product constitution.** "Read-only posture, never commits, not a fixer — diagnoses only" is the read-only risk tier implemented as an agent's identity. This is the strongest possible answer to enterprise AI fear: the agent *cannot* be the incident. Book Part IV/VI material, verbatim.
3. **The evidence pipeline is the Black Box talk, operationalized.** findings.json + dependency map ingested into TIMC as FINRA 4511 records = traceability-as-artifact, exactly what the conference material promises. The demo and the compliance story are the same pipeline.
4. **The Dependency Graph's killer first mission already exists: the DB2 mainframe retirement.** 12,500 batch jobs, tables, and service requests to retire is precisely a blast-radius / upstream-downstream / contracts problem. The owner's automation instinct for that program (spec-driven + auditor + daily HITL sign-off) runs *through this box*. The mainframe program isn't a distraction from the fleet — it's the Dependency Graph's proving ground and the auditor's first enterprise case study.
5. **Mermaid output → StructView renders it.** The Auditor emits `.mermaid`; the fleet's own viewer displays it. The fleet eats its own artifacts — reuse as architecture.

Cross-references: `docs/the-through-line.md` (machine layer), `docs/structureview-viability.md` (entry tier), `research/Quality-Guardian-Research-Expansion-V5.md` §13 (fleet), owner remarks 2026-07-10 on the auditor working without the DB and the discovery bench wiki/graph being partially auditor-fed.

## Addendum: the Auditor build session, summarized (from owner-shared transcript, 2026-07-11)

The "this thread" session that designed the middle tier produced a complete audit system across four versions:

- **v0 — Foundation artifacts:** `AGENTS.md` v1.0.0 (seven non-negotiable constraints incl. read-only posture, evidence required, quadrant attribution mandatory; domain-record YAML schema with `commit_frequency_90d`/`active_contributors_90d` so unmaintained codebases surface as findings before code is read; Planning Mode triggers; severity escalation table), `SOUL.md` v1.0.0 (measured, evidence-first voice; "I will not issue a clean bill of health unless every segment is inspected"), audit-plan template (worked example: 14,200 LOC Node/Express, 5 segments/7 passes), `findings-SEG-01.json` sample (CRITICAL hardcoded credentials → INFO good-pattern-worth-preserving), four Mermaid diagram templates, React planning dashboard (later retired).
- **v1.0.0 — Paste-only protocol:** relay-baton pattern, six confirmation signals, bash extraction commands, tool compatibility incl. Copilot workaround.
- **v2.0.0 — Clone access protocol + Prompt 2c dependency map:** upstream/downstream/shared-infra/risk-summary sections; documented rationale that blast radius cannot be answered from one repo alone (hence the Dependency Graph as a distinct box).
- **v3.0.0 — Segment-close fix:** three files per segment, CRITICAL escalation file, Mermaid fragment spec making consolidation merge-mechanical (seven-step, merge-only).
- **Viewer:** standalone HTML (JSX retired), seven views, three-format findings normalization; bugs fixed in a follow-up session (domain YAML/JSON export, segment scope-matching with UNASSIGNED bucket).

**Outstanding items carried from that thread:** (1) consolidation prompt must embed merged diagram as `architecture_mermaid` in findings.json (one-line fix, identified); (2) SKILL.md tertiary layer unwritten; (3) Agent Roster entry; (4) Cowork plugin spec; (5) **the evidence ingestion contract into TIMC — the spec that turns middle-tier files into fleet product. Drafted 2026-07-11 as a Propose-stage spec: `structureview/docs/evidence-ingestion-contract-plan.md`.**

**Pattern note for the book:** the Auditor's three-layer governance (AGENTS.md constitution / SOUL.md identity / SKILL.md capability) is the same pattern this learning platform runs on (CLAUDE.md / soul.md / skills) and that C4 teaches. One constitution pattern, three deployments: agent, workspace, curriculum. Owner's formulation (2026-07-11, verbatim): *"CLAUDE.md is the Quality Management System. SOUL.md is the code of conduct. SKILL.md is how they manifest — walk them out — in day-to-day activities. It's almost like it's alive."* That's the Part II chapter thesis: institutions have always been constituted this way — law, character, practice — and agents built this way inherit the institutional property of persisting through change of parts.
