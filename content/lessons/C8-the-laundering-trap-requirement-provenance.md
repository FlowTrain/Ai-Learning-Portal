---
id: "C8"
courseId: "tooling-misconceptions"
tier: "fluent"
roleIds: ["pm", "coach", "tl"]
durationMin: 25
creditHours: 1
staircaseRung: 3
buildsBehaviors:
  - "Tier 3: tags each requirement by evidence tier (stated / inferred / assumed) and surfaces the coverage gap instead of letting a document's format confer unearned authority"
  - "Tier 3: can name when a document's format has outrun its source"
rubric:
  - criterion: "Every requirement carries a tier"
    emerging: "Requirements stated with no provenance"
    working: "Each requirement tagged stated / inferred / assumed"
    strong: "Stated-tier items resolve to a real source item; inferred ones show the reasoning"
  - criterion: "Coverage is disclosed"
    emerging: "No coverage block"
    working: "States what the source asked, what it didn't, the sample size and population"
    strong: "The gap is surfaced as a finding on page one, not buried"
  - criterion: "Format vs. source"
    emerging: "Lets the document format carry the authority"
    working: "Notes where the source cannot support a requirement"
    strong: "Can state the one sentence that would have stopped the laundering"
---

# When the Format Outruns the Source

> A customer sentiment survey becomes a "Voice of the Client" summary. The summary becomes a PRD. A PM asks the model to turn it into requirements, and it obliges — headers, numbered requirements, acceptance criteria, the works. By the time the document circulates, nobody remembers that the source was forty free-text comments from an instrument that never asked anyone what they needed. The format now asserts things the source was never able to support. That is laundering, and a good template makes it worse, not better.

## Start Here: Where Would This Requirement Have Come From? (5 minutes)

Take one requirement from a real document you have on hand. Ask the question you already know from checking any AI output: *where would this have come from?* Point to the specific source item — the survey question, the interview line, the ticket — that supports it.

Often you can't. The requirement reads as settled fact because it is sitting in a requirements document, but trace it back and there is nothing underneath. Hold onto that gap; the rest of the lesson is about making it visible before it ships.

## Format Confers Authority (6 minutes)

Here is the mechanism. Sentiment tells you how people feel about what already exists. A PRD asserts what to build. Those are different claims, and the first cannot support the second — but the *format* of a PRD confers authority regardless of what fed it. Numbered requirements look decided. Acceptance criteria look validated.

Three things make this worse, not better, in an AI workflow. Chaining two tools together does not fix it — a laundered input produces a laundered output with more polish. A stronger model makes it *worse*, because the unsupported requirement reads more convincingly. And a prose instruction to "ground requirements in the research" is unevidenceable — it is the written-not-operated trap from the previous lesson, wearing a PRD.

## Requirement-Level Provenance (6 minutes)

The fix is a binding control, and it is small. Every requirement carries an evidence field with a tier:

- **stated** — traceable to a specific source item (a question ID, a quote, a ticket)
- **inferred** — analyst reasoning from a stated signal, with the reasoning shown
- **assumed** — no source basis

The check is mechanical: the field exists on every requirement, the stated-tier items resolve to real source items, and the tier mix is disclosed on page one. Whether an *inference* is a good one stays advisory — that is judgment, and you don't bind judgment. But "seven of nineteen requirements have no source basis" is a fact you can print, and it is exactly the fact that disappears when the format is left to carry the authority.

## The Coverage Block (5 minutes)

One more structural requirement, because provenance per requirement isn't enough on its own. Attach a coverage block to the document: what the instrument asked, what it did not ask, the sample size, and the population. Require it to propagate into anything built downstream.

This reframes the instrument's gap as a *finding* rather than an embarrassment to smooth over. It is what stops a sentiment pass from being mistaken for the discovery that never actually happened — and it is the difference between a document that knows its own limits and one that quietly forgets them.

## Assignment

Take a real requirements or PRD section and make its evidence honest.

### Deliverables

- `provenance-check.md` covering one requirements section, with each requirement tagged **stated / inferred / assumed** — the stated ones pointing at the specific source item
- A **coverage block**: what the source asked, what it didn't, the sample size, the population
- One line naming the tier mix out loud (for example, "X of Y requirements have no source basis") — the sentence that keeps the format from outrunning the source
