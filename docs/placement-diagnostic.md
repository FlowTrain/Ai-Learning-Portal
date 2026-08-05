# Placement Diagnostic — Intake Flow Spec

The Monday-Morning Diagnostic (`docs/maturity-model.md`) as a working intake experience. Machine-readable form: `content/diagnostic.json` (validates against `content/schemas/diagnostic.schema.json`). This document is the human-readable spec plus the facilitated worksheet.

## Design commitments

1. **Behavior, not self-assessment.** Every check pairs its question with an evidence prompt ("show me"). Self-assessment over-places almost everyone; the evidence prompt is what makes the score honest. In app form, evidence is a required free-text field the coach reviews; in facilitated form, it's the follow-up the coach actually asks.
2. **Ambiguity routes down.** Placement uses a conjunctive ladder: a tier is awarded only when its gate *and every lower gate* passes. A "yes" on a higher check with a failed lower gate never raises placement — it becomes a flag for the coach instead. This is the BACKLOG-mandated rule, and it's also the safe error: an under-placed person breezes through a course and gains confidence; an over-placed person hits "JSON felt really advanced" and disengages.
3. **Deterministic and total.** Every one of the 48 possible answer combinations yields exactly one tier; every (tier × role) pair yields exactly one course id. No combination dead-ends.

## The ladder

| Gate | Requires | Grants |
|---|---|---|
| Tier 2 | Q1 = yes AND Q2 = yes | AI-Enabled placement |
| Tier 3 | Tier 2 gate AND Q3 = maintain AND Q4 = yes | AI-Fluent placement |
| Tier 4 | Tier 3 gate AND Q5 = yes | AI-Native placement |
| (else) | — | Tier 1, AI-Aware |

Q3 has three values: `none` / `use` / `maintain`. `use` is consistent with Tier 2 but not required for it (checks 1–2 govern the Tier 2 gate, per the maturity model); only `maintain` counts toward Tier 3.

**Worked ambiguity examples** (the rule in action):

| Answers (Q1–Q5) | Placement | Why |
|---|---|---|
| no, yes, maintain, yes, yes | **Tier 1** | Q1 fails the Tier 2 gate; everything above is disregarded and flagged (`orphan_curation`, `orphan_workflow_design`, `orphan_system_design`). |
| yes, yes, use, yes, no | **Tier 2** | Q4 = yes but Q3 ≠ maintain — the Tier 3 gate needs both. Flag `orphan_workflow_design`: ask who actually runs that workflow. |
| yes, yes, maintain, no, yes | **Tier 2** | Q5 = yes but the Tier 3 gate fails on Q4. Flag `orphan_system_design`: verify the artifact. |
| yes, yes, maintain, yes, no | **Tier 3** | Clean fluent placement. |

Flags never change placement. They tell the coach where the interview and the answers disagree — which is usually the most informative part of the intake.

## Routing (tier × role → course)

The recommended course is the bridge that *starts* at the placed tier:

| Placed | pm | coach | designer | leader | engineer | tl | data |
|---|---|---|---|---|---|---|---|
| Tier 1 | aware-foundations | aware-foundations | aware-foundations | aware-foundations | aware-eng | aware-eng | aware-eng |
| Tier 2 | enabled-pm | enabled-pm | enabled-design | leader-literacy † | enabled-eng | enabled-eng | enabled-eng |
| Tier 3 | fluent-chains ‡ | native-systems | fluent-chains ‡ | native-systems | fluent-chains ‡ | native-systems | fluent-chains ‡ |
| Tier 4 | native-systems § | native-systems | native-systems § | native-systems | native-systems § | native-systems | native-systems § |

† **Leader at Tier 2 routes to the literacy strand.** Per the role×tier target matrix, a leader's target is "Tier 2 + Tier 4 literacy" — a leader placed at Tier 2 has the habits half; the remaining program is leader-literacy (D5–D7: fund, govern, measure). The interim enabled-pm route was retired 2026-07-10 when BACKLOG 5 shipped.

‡ **Tier 3 for non-coach-track roles routes to fluent-chains, not native-systems.** Placement is behavioral; tier *standing* requires artifacts (assessment = artifacts + observed behavior). A PM who behaves fluent but has never produced a SKILL.md certifies through fluent-chains. tl/leader/coach — the roles native-systems serves — route to their 3→4 bridge directly.

§ **Tier 4 for roles outside native-systems' roleIds** (pm/designer/engineer/data): the course id is still native-systems, but the coach should enroll them as case-study contributors and Evolution Library curator candidates rather than ordinary cohort members. Someone who genuinely passes all five gates is a curation asset (see `docs/curation-model.md` — curating is Tier 3, defining what gets tracked is Tier 4).

## Facilitated worksheet (coach script)

Ten minutes, one-on-one, ideally with the person's laptop open. Ask in order; score only what you see evidence for.

1. *"Did you reach for an AI tool this week without being told to?"* — then: **"Tell me about the last time. What was the task?"** A concrete task within the week = yes. "I use it all the time" with no specific = no.
2. *"When you prompt, do you routinely give context, task, and audience?"* — then: **"Show me a recent prompt you actually used."** Score the prompt on the screen, not the description of it.
3. *"Do you use a prompt library or shared templates? Maintain one?"* — then: **"Show me. When was it last updated, and by whom?"** Using someone else's = `use`. An update history with their name in it = `maintain`. A library they own but haven't touched in months = `use`, and note it.
4. *"Have you defined a repeatable AI workflow someone else runs?"* — then: **"Who runs it? Show me what they run it from."** If the answer is "well, I run it" — that's a no for this check (it's Tier 2 behavior done well).
5. *"Have you built schemas, evals, or governance others operate within?"* — then: **"Show me the artifact, and name one person constrained by it."** Both halves required.

Then: read the tier off the ladder, read the course off the table, and review any flags out loud with the person — the flags are conversation starters, not accusations.

**Coach overrides:** a coach may override routing *downward* freely (e.g., visible gaps despite passed gates). Upward overrides require the evidence the check asked for — never the person's self-report. Record overrides with a one-line reason; override frequency per check is the diagnostic's own quality signal (a check that's constantly overridden is mis-worded — fix it here and in `diagnostic.json`).

## App intake flow (for BACKLOG 7's rebuild)

Screen 1: role picker (from `roles.json`). Screens 2–6: one check per screen — question, options, required evidence text field. Screen 7: placement result — tier with its maturity-model description, recommended course card, flags rendered as "things to discuss with your coach." Store answers + evidence + flags with the learner record; a coach reviews evidence async and confirms or overrides. The router is pure data (`diagnostic.json`), so the app implements no placement logic of its own.

## Maintenance

- Re-verify routing whenever a course is added/retired or course `roleIds` change (the exhaustive router test in the validation harness catches dead routes).
- Review question wording quarterly against override frequency.
