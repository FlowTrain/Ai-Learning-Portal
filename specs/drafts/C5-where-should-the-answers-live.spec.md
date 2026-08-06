# Module Spec — Where Should the Answers Live? (Three Teams, One Question)

> **BUILT 2026-07-10** → `content/lessons/C5-where-should-the-answers-live.md`. Dependency resolved first: `library/evolution/token-economics.md` (founding entry 6). Spec retained as the authoring record.

<!-- Filled from research/: the three Jira reporting analyses (MCP-direct, Athena
     lakehouse, Azure PostgreSQL ODS), 2026-07. First real run of the module
     spec template. -->

## 1. Identity (maps 1:1 to lesson frontmatter)

| Field | Value | Rule |
|---|---|---|
| id | C5 | fluent-tier arc |
| courseId | fluent-chains | extends the existing Tier 2→3 course |
| tier | fluent | |
| roleIds | ["tl", "engineer", "data", "leader", "coach"] | the people in the three meetings |
| durationMin | 30 | |
| staircaseRung | 2 | patterned comparison — the full reference architecture stays in the architect zone |

## 2. The concept and its staircase ancestry

**Concept in one sentence:** Matching an AI-and-data architecture to the *cadence and stakes of the questions being asked* — not to the preferences of the team proposing it.

**Where does this concept already live?** (verified in `docs/staircase-map.md`, "Tool selection & cost" row)

- Rung 1 ancestor: **A4 — Right Tool, Right Task.** The two-question test ("what artifact, what does the tool read first?") is this exact decision at personal scale.
- Rung 2 ancestor: **C2 — token governance** (three-term cost), **D5 — three ownership questions** (for the leader segment).
- This module sits at rung 2 because: it teaches a named comparison pattern (six questions × three options). The rung-3 form — the actual reference architecture, schemas, gateway specs — is architect-zone material (`t-intelligent-infrastructure`, `t-foundation-integration` teasers).

## 3. The learner on Monday morning

**Who walks in:** Someone who has sat in (or run) one of the three meetings. They know *their* proposal's strengths and the other two teams' weaknesses, and they are sincerely confused why the decision hasn't been made yet. Some are Tier 2 practitioners with strong tool loyalty; the leaders among them are being asked to fund one of three things they can't compare.

**Observable behavior this builds** (→ `buildsBehaviors`):

1. "Tier 3: evaluates an AI-data proposal by question cadence, full cost, and failure modes — not by tool familiarity"
2. "Tier 3: can state the case FOR the two architectures they didn't propose"

**Opening activity** (plain-language, <5 min, real work): *The Question Census.* Write down the last five reporting questions your team actually asked of Jira data. For each: how often does it get asked (once / weekly / continuously), who asked (a person exploring, an analyst scanning, a product surface displaying), and what happened when the answer was wrong?

## 4. The artifact

**Named file:** `architecture-decision-memo-[topic].md` — one page, the three options scored against the six questions, with a recommendation *and* the strongest objection to it.

**Who reuses it:** the annual-planning decision forum; also feeds the discovery bench wiki. Reuse signal: the memo cited in a funding decision (D5's one-pager can attach it).

**Rubric:**

| Criterion | Emerging | Working | Strong |
|---|---|---|---|
| Question-first framing | Compares tools by features | Scores options against the team's actual question census | Census includes cadence, asker, and cost-of-wrong-answer per question |
| Steel-manning | Own option praised, others strawmanned | Each option's legitimate best-fit case stated | Each option scored by a question type it *wins* — including the two not chosen |
| Full-cost honesty | License/compute costs only | Includes token economics and maintenance ownership | All three D5 terms + failure modes (write-back risk, context exhaustion, egress) with sources |

## 5. Claims and sources (from research/)

| Claim the module will make | Source + date | Stable or volatile? |
|---|---|---|
| Direct MCP integration carries a schema "input tax" (tens of thousands of tokens before the first question) and consumes most of the context budget on tooling | `research/Jira MCP Token Impact Analysis.md`, 2026-07 | **Volatile** → `token-economics` entry (founding entry 6); teach the *pattern* (input tax exists), route the numbers (47K, 79%) to the entry |
| Markdown↔ADF write-back is lossy: an agent appending a sentence can silently destroy ticket formatting, with no error raised | same, 2026-07 | Semi-stable (vendor-specific) → teach as a *failure-mode category* (lossy round-trips at write boundaries); vendor specifics dated in module |
| Gateway payload filtering (fields/expand, jq) cuts ~90% of response dead weight | same, 2026-07 | Volatile numbers → entry; stable pattern (filter at the boundary, not in the prompt) |
| Columnar formats + partitioning cut lakehouse scan costs by orders of magnitude; text-to-SQL accuracy is benchmark-fragile but production-viable with schema access + semantic models | `research/Jira Data Cost and Integration Analysis.md`, 2026-07 | Volatile (benchmarks) → cite dated in module body; candidates for `evaluation-practice` entry |
| A multi-model ODS (relational + JSONB + vector in one engine) serves product operational reporting and RAG from a single store; cross-cloud egress is a modelable, often-negligible cost at this volume | `research/Azure PostgreSQL Jira Data Cost Analysis.md`, 2026-07 | Stable pattern / volatile prices → prices stay in research doc, pattern in module |
| Org platform direction (Fabric migration, 18 mo) legitimately weights the decision | owner field knowledge, 2026-07 | Stable principle: "where the org is going" is a scoring question, not a bias |

- `libraryRefs`: ["prompting-frameworks", "context-engineering"] — context exhaustion and placement findings already live there. Add "token-economics" when entry 6 ships (these three research docs are its founding sources — note added to curation model's founding-entries list).
- No unsourced numbers enter the lesson body; the six-questions pattern carries the teaching, the library carries the numbers.

## 6. Section plan

1. **Start Here: The Question Census** — (activity above). The census is the input to everything; the punchline lands later: *the architecture argument is unresolvable because the three teams did three different censuses without knowing it.*
2. **Three Teams, Three Answers** — each proposal presented in its own team's voice, best case first (steel-man discipline): chat-with-your-data (fastest adoption, zero infrastructure, per-person cost and write-back risk), the lakehouse (scan-the-world analytics, cheapest per-TB questions, analyst-shaped), the operational data store (product surfaces and continuous questions, one governed store, biggest up-front commitment). **Deliberately delivered as three standalone segments — one team's world per sitting. This is the anti-head-explosion design: nobody sees the whole map until they've stood in all three rooms.**
3. **The Six Questions** — the comparison pattern: (1) What cadence are the questions? (2) Who asks — person, analyst, or product surface? (3) What does a wrong answer cost? (4) Who maintains it when the model/API updates? (5) What breaks, and who notices? (6) Where is the org already going? Questions 4–5 are D5's ownership questions; question 1–2 is A4's two-question test grown up.
4. **Assignment** — run your real question census, score all three options, write the decision memo. Deliverables: census (5+ real questions), six-question scoring table, one-page memo with recommendation + strongest objection + the question type each *losing* option would still win.

## Definition of Ready

- [x] Identity fields valid against `lesson.schema.json` (C5 pattern-valid; fluent-chains exists)
- [x] Staircase ancestry verified — A4 (rung 1) → C2/D5 (rung 2); no leap. Rung-3 continuation lives in architect-zone teasers.
- [x] N/A rung-1 vocabulary gate (this is rung 2)
- [x] Opening activity uses learners' real reporting questions
- [x] Artifact named; rubric complete; reuse consumer identified (annual planning / discovery bench)
- [x] Every claim sourced + dated; volatile numbers routed to `token-economics` (pending entry) or kept dated in research/
- [x] Curse-of-knowledge check: the module never shows the unified map as a diagram to be admired — the learner *assembles* it via the census and six questions. The owner's full architecture (CCQG, auditor graph, mainframe program) is explicitly out of scope; it is the case study material for the architect zone, not this lesson.

**Ready.** One dependency worth sequencing: drafting the `token-economics` Evolution Library entry before (or alongside) authoring C5 — these three research docs are its founding sources, and C5 becomes its third citing lesson.
