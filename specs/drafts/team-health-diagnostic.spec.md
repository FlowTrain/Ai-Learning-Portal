# Spec Stub — Team Health Metrics Diagnostic (PROPOSE stage, awaiting owner's artifact)

> Owner has a complete Team Health Metrics diagnostic, unshared as of 2026-07-11, unsure
> where it lives on the platform. This stub answers the placement question in advance so
> intake is mechanical when the artifact arrives.

## What it is (from owner description)

A diagnostic that prices operational health in business terms — the mine-foreman's math
applied to product teams: deferred maintenance surfacing as sev-1s, and sev-1s priced in
lost revenue per second (a customer who can't reach a savings account, process a trade, or
run tax-loss harvesting). Benchmark framing: healthy orgs convert <1% of story throughput
to defects; 10% is off the benchmark's chart entirely.

## Placement answer

The platform already has the pattern — this is the **third diagnostic in a family**:

| Diagnostic | Places | Lives at |
|---|---|---|
| Monday-Morning Diagnostic | *people* on the maturity ladder | `content/diagnostic.json` + `docs/placement-diagnostic.md` |
| Interest capture | *demand* for unbuilt content | `content/teasers.json` + `docs/interest-capture.md` |
| **Team Health Metrics** | *teams/systems* on an operational-health ladder | `content/team-health.json` + `docs/team-health-diagnostic.md` (same split: machine-readable rules + human-readable spec/worksheet) |

Consumers, already built and waiting:

- **D7 (dashboard spec lesson):** team-health metrics are a fourth metric family alongside
  placement / certification / reuse — and the one that speaks CFO (revenue-per-second).
- **D5 (funding):** the "current cost" block of the one-pager gets its numbers here.
- **Leader-literacy cohort kit:** the diagnostic is the natural pre-work for D5–D7.
- **Quality Guardian/TIMC:** the enterprise-grade home — team health as an evidence bundle
  type (see `evidence-ingestion-contract-plan.md`; likely a `bundle_type: "team-health"`).

## Why this is the Postgres/ODS justification (owner's instinct, confirmed by his own lesson)

Run C5's six questions on team-health metrics: cadence = **continuous** (sev-1 cost accrues
per second); asker = **a product surface** (dashboards leaders read without asking); cost of
wrong = **funding decisions made on bad numbers**. Three-for-three → operational data store.
The Team Health diagnostic isn't just *stored in* the Postgres ODS — it's the workload that
justifies building it. The C5 decision memo for the day-job architecture fight can cite its
own platform's diagnostic as Team Three's first tenant.

## Definition of Ready (for when the artifact lands)

- [ ] Owner shares the diagnostic (checks, scoring, thresholds)
- [ ] Same evidence-first discipline as the placement diagnostic (measured, not self-assessed)
- [ ] **Numbers discipline:** ships with the modeled exemplar + public benchmarks only;
      day-job actuals never enter platform content (see the-through-line.md, delicate-dance rule)
- [ ] Schema + exhaustive routing test, same harness as diagnostic.json
