# CCQG Self-Audit — the Guardian audits the Guardian (2026-06-29)

The CCQG Auditor was run — via manual prompt chain, mid-Fable-shutdown glitchiness, and a mid-run model swap to Haiku ("ran out of steam toward the end but found enough for me to go *well, crap*") — against **its own namesake repo**, `FlowTrain/Clean_Code_Quality_Guardian`. Owner note for the record: hasn't written software professionally since 2013; this was a manual relay-baton run, not a polished harness. Raw artifacts in `research/` uploads: domain-record.yaml, audit-plan.md, dependency-map-initial.yaml, RISK-ASSESSMENT.md, CONSOLIDATION.md, diagram-CONSOLIDATED-RISK-MAP.mermaid, README.md.

## What it found

Scope: 9 segments, 109 files, 15,259 LOC (partial — Haiku faded before full coverage). **176 findings: 5 CRITICAL, 9 HIGH, 162 MEDIUM/LOW/INFO.** Verdict: *"architecturally sound but operationally unready for FINRA-regulated data."* The 5 production blockers:

1. **CRITICAL-1 — Cosmos DB single-region.** No zone redundancy, no failover. A regional Azure outage = total loss of audit evidence = FINRA 4511 (7-year retention) violated. Est. fine framing: $500K–$10M+.
2. **CRITICAL-2 — Audit storage lock deferred** (`enableAuditStorageLock=false` default). Evidence deletable before the CanNotDelete lock is applied; 7-year immutability void.
3. **CRITICAL-3 — Signal scoring inversion.** Empty specs and EARS `total=0` score **100%**. The release gate green-lights on false signals — a spec with no requirements reports "complete." (Already known internally: GH-#398 parked it for Phase 3.)
4. **CRITICAL-4 — `maxDepth()` DOS.** Crashes on circular JSON refs; scorer stack-overflows with no graceful degradation.
5. **CRITICAL-5 — Evidence data loss (3 linked).** Malformed JSONL lines silently skipped (no recovery); HTTP error-handling bypass; encryption key with no rotation.

Plus HIGH: no private endpoints (all Azure services public-facing), no Managed Identity (connection-string auth), and a compliance violation where the dashboard hardcodes thresholds instead of reading the YAML config (S35 AC11).

## Why this is the most important artifact of the build

1. **The read-only auditor worked, and its diagnoses-only posture is now proven under fire.** It found five ways its own platform could lose regulated evidence and *touched nothing*. That's the D6 read-only risk tier and the "not a fixer" SOUL.md, validated on the highest-stakes possible target: itself. This is `t-case-platform` and Book Part IV/VI, written by events.

2. **It's brutal, honest dogfooding.** A quality platform that audited itself and came back clean would be suspicious. One that came back with 5 CRITICALs — including a *scoring inversion in its own signal engine*, the exact "valid ≠ correct / a green light on a false signal" failure the evaluation-practice and structured-outputs entries warn about — is credible. The platform caught its platform lying green. That story sells more than any clean bill of health could.

3. **The findings are self-consistent with the whole corpus:** single-region audit store (C5's "who owns the store, where does it live"), deferred maintenance as unfunded liability (D5, the coal mine), inverted signal = false green (evaluation-practice era 3, the drift/calibration failure), key-rotation gap (the Black Box compliance material). The platform's own defects are a live-fire exam of its own curriculum.

## Why this forces the Postgres/ODS decision (owner's read, confirmed)

The audit *is* the C5 decision, run for real on the platform's own reporting substrate:

- **CRITICAL-1 and CRITICAL-5 are both "the evidence store is wrong."** Cosmos single-region with silent JSONL skips is the *lakehouse-tail* answer (append files, hope) applied to data that has FINRA's continuous, product-surface, catastrophic-cost-of-wrong profile. Run C5's six questions on audit evidence: cadence = continuous (findings accrue per segment, per CI run); asker = a product surface + a regulator (TIMC dashboard, audit data room); cost of wrong = **destruction of evidence = regulatory violation**. Three-for-three → **governed operational data store**, with immutability, retention lock, and georeplication as first-class properties — not a bucket of JSONL behind a single-region NoSQL default.
- The **evidence ingestion contract** (`structureview/docs/evidence-ingestion-contract-plan.md`) is the *product* answer to exactly CRITICAL-5: content-hash, append-only supersession, validation-gate-or-quarantine, attestation. The self-audit is that spec's first real requirement set — F1 (silent skip) is precisely what the contract's "reject-with-reasons, never silently accept" rule prevents.
- So the Postgres/ODS is no longer a preference argument. **The platform's own audit says the current evidence store fails the compliance profile the platform sells.** That is the forcing function: build the governed store, or the Quality Guardian can't pass its own gate for regulated data. The dogfood bit back, which is the best thing that could have happened before a client's did.

## What this needs next (not now — recording only)

- **Re-run under a stable model with the rules-engine context assembler** (LemonAid finding): Haiku fading mid-run is the accumulation-collapse curve again; per-segment context contracts would let a small/cheap model finish the 9 segments without steam loss.
- **Triage the 5 CRITICALs as real backlog** on the CCQG repo (separate engagement from this platform — audit ≠ remediation, per the auditor's own SOUL.md).
- **The self-audit becomes the case study**: `t-case-platform` teaser's demand trigger just fired from the owner's own hand. When it's built, this is the opening — "we ran our own auditor on ourselves and found five ways to lose a regulator's evidence."
