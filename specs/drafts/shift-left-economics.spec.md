# Evolution Entry Spec — Shift-Left Economics (DRAFTED 2026-07-11 -> library/evolution/shift-left-economics.md; Challenge step pending)

## 1. Identity

| Field | Value |
|---|---|
| id | shift-left-economics |
| practice | Cost-of-Change / Shift-Left Economics |
| status | current (draft) |
| review_cadence | quarterly |
| model_generations | TBD (pre-AI baseline / cheap-generation era / spec-and-eval era) |
| planned referenced_by | C5 (decision memo stakes), D5 (funding), B3 (test-left) — verify at draft |

## 2. The observed shift (why this entry, why now)

Boehm's curve said a defect found after delivery costs orders of magnitude more than one found at requirements. AI complicates the curve from both ends: generation and rework got cheap (weakening the classic argument), while AI-specific failure modes (silent corruption, hallucinated behavior, compliance breaches) made *post-delivery* defects costlier than ever in regulated domains — a wrong customer communication is an enforcement action, not a bug ticket. The hypothesis to draft and challenge: **the curve didn't flatten; the cost moved from rework to review, and the "left" moved from requirements docs to specs + evals + HITL gates.** Owner's spec-driven development practice and the compliance-by-design material (`research/navigating-the-black-box.md`) are primary sources.

## 3–7. TBD at Draft stage

Era sketch: (1) Boehm-era — costly rework justifies heavy up-front process; (2) cheap-generation era — "just regenerate it" undermines the curve's rhetoric, discovery-of-defect still expensive; (3) spec/eval era — the left reconstitutes as machine-checkable artifacts (specs, eval gates, compliance NFRs) rather than documents.

## Definition of Ready

- [ ] Curve claims sourced with dates (Boehm original + AI-era critiques/confirmations)
- [ ] Challenge reviewer named
- [ ] ≥2 citing lessons confirmed
