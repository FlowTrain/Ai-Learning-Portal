---
id: evaluation-practice
practice: Evaluation Practice
status: current
last_reviewed: 2026-07-10
review_cadence: quarterly
model_generations: [seems-right-era, rubric-era, harness-and-drift-2026]
referenced_by: [B3, C1, D1]
curators: [platform-owner]
---

# Evolution Entry: Evaluation Practice ("Seems Right" → Rubrics → Eval Harnesses and Drift Detection)

## Current guidance (teach this today)

Define what "good" looks like **before** generating anything — then enforce it at the altitude the stakes demand:

- **Personal work (Tier 1–2):** the author reads the output like a colleague's draft before it leaves their hands (A0's One Rule). This is a complete evaluation practice at personal stakes. Teaching harnesses here is a staircase leap.
- **Team workflows (Tier 2–3):** written acceptance criteria *before* the prompt (C1's rule), quality checklists for AI output (B3's pattern), and a small **golden set** — 10–20 real examples with known-good answers, re-run when the prompt, model, or context changes. A golden set is the cheapest eval that actually works.
- **Production systems (Tier 4):** a versioned eval harness wired into deployment — eval regressions block the ship, the way failing tests do. Current practice (as of 2026-07): deterministic checks on 100% of traffic, sampled LLM-as-judge scoring on ~5–10% of production requests, judges calibrated to ~85–90% agreement with a human-labeled reference set, and drift monitoring on both the outputs and the *case set itself* — production usage drifts, and a static test suite quietly diverges from reality.

Two principles hold at every altitude. **Eval-first ordering:** define good → build the check → then iterate the prompt until it passes (D1's rule — the eval comes before the prompt, not after the incident). **Human ground truth:** every automated judge is calibrated against, and periodically audited by, human judgment; a judge nobody has checked is a vibe with a dashboard.

## Eras

### Era 1 — "Seems right" (~2022–2023)

Evaluation was the author reading the output and nodding. Demos stood in for validation; a good anecdote shipped a workflow. Model context: outputs were low-stakes drafts, tooling didn't exist, and the novelty was the point. The era's honest core — human judgment on real output — was never wrong; it just doesn't scale past the author.

### Era 2 — Rubrics and review patterns (2023–2025)

As AI output entered real workflows, teams wrote down what "good" meant: checklists, acceptance criteria authored before generation, golden examples, structured critique passes (the B2/B3 pattern layer of this platform). Public benchmarks proliferated — and immediately taught their own limits: contamination, gaming, and metrics that disagree with human judgment (the BIRD text-to-SQL benchmark's strict execution-accuracy metric agrees with human experts only ~62% of the time, generating false negatives on functionally correct answers). LLM-as-judge emerged as the scaling move, arriving with documented biases — position, verbosity, self-preference — that made uncalibrated judging a new way to be confidently wrong.

### Era 3 — Harnesses and drift detection (2025–2026)

Evaluation industrialized into engineering infrastructure: versioned eval suites run in CI on every prompt/model/context change, with regressions gating deployment ("eval without gates is decoration"). LLM-as-judge matured from a trick into a calibrated instrument — human-agreement targets, multi-method scoring with disagreement detection, sampled scoring economics. The frontier problem moved twice: from *scoring* to *drift* (models update, usage shifts, and the eval set itself goes stale — the dominant failure mode is now operational cadence, not technique), and from single calls to *agent trajectories* (evaluating multi-step tool use, not just final text). The eval set became the durable asset — more valuable than the prompts it tests, because it survives every model migration.

## Deprecated patterns (stop teaching these)

- ❌ **Shipping on demo** — an anecdote is a sample size of one, selected by the person with the most to gain.
- ❌ **Benchmark-number worship** — public benchmark scores are contaminated, gameable, and only loosely correlated with human judgment on your task; build task-specific evals instead.
- ❌ **Uncalibrated LLM-as-judge** — a judge without a measured human-agreement rate inherits every bias of the model plus false authority.
- ❌ **Evaluate-once-at-launch** — models update under you and usage drifts; an eval that ran once is a photograph, not a monitor.
- ❌ **Eval as post-build QA** — defining "good" after seeing the output means the output defines "good"; the ordering is the discipline (criteria → check → generate).

## What survived

Era 1's core — a human reading real output with judgment — survives as both the Tier 1 practice (the One Rule) and the ground-truth anchor of every Tier 4 harness: calibration sets are human-labeled, drift audits are human-in-the-loop. Era 2's rubrics survive *inside* the harness as the judge's scoring criteria. This platform is itself the pattern at organizational scale: rubrics version with lessons, assessment is artifacts plus observed behavior (never quizzes), and the Monday-Morning Diagnostic is a behavioral eval with evidence prompts — evaluation-practice applied to humans learning AI.

## Boundary conditions (where older practice is still correct)

- **Personal, reversible work needs no harness.** The One Rule is the correct and complete practice for Tier 1–2 drafts; harness overhead there kills the habit formation the maturity strategy depends on.
- **Low-volume team workflows** are properly served by Era 2: a golden set of 10–20 real cases re-run on change beats both "seems right" and a premature harness. Build the harness when the workflow reaches production cadence or external stakes (D6's risk tiers make the trigger explicit).
- **Deterministic properties don't need judges.** Schema validity, format conformance, and referential integrity are exact checks (see structured-outputs) — spending judge tokens on them is waste; the judge is for qualities only judgment can score.

## Signals to watch (would trigger Era 4)

- Models whose self-evaluation is trusted natively at production stakes (would collapse the judge/calibration layer).
- Vendor-managed drift detection and auto-updating eval sets as platform primitives (would absorb the cadence discipline — the skill shifts to auditing the vendor's evals).
- Regulatory frameworks mandating documented evaluation for deployed AI (would convert this practice from engineering discipline to compliance artifact — governance implications land in D1/D6 territory).

## Sources

- [Evaluating LLM Outputs: Internal Eval Harness for 2026](https://logiciel.io/blog/llm-eval-harness-internal-build-2026) (2026) — harness operating cadence as the dominant failure mode; versioning, CI integration, regression gates.
- [LLM-as-a-Judge in 2026](https://deepeval.com/blog/llm-as-a-judge) (DeepEval, 2026) — calibration to ~85–90% human agreement; multi-method scoring with disagreement detection; judge bias catalog.
- [The Complete Guide to LLM & AI Agent Evaluation in 2026](https://www.adaline.ai/blog/complete-guide-llm-ai-agent-evaluation-2026) (Adaline, 2026) — sampled production scoring (~5–10% judge, 100% heuristic), agent-trajectory evaluation, drift monitoring.
- `research/Jira Data Cost and Integration Analysis.md` (owner research, 2026-07) — BIRD benchmark's ~62% human-agreement rate; benchmark fragility vs. production accuracy with schema access.
- This platform's own assessment design (`docs/maturity-model.md`, rubrics-in-frontmatter convention, placement diagnostic) — evaluation-practice applied to human learning; the internal case study.
