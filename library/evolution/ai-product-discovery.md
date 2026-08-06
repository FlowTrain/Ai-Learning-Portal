---
id: ai-product-discovery
practice: Product Discovery & Customer Centricity with AI
status: current
last_reviewed: 2026-07-11
review_cadence: quarterly
model_generations: [manual-discovery-era, ai-accelerated-synthesis-era, synthetic-substitution-contested-2026]
referenced_by: [B2, B2D]
curators: [platform-owner]
---

# Evolution Entry: AI Product Discovery (Manual Synthesis → AI-Accelerated Evidence → The Synthetic-User Boundary)

## Current guidance (teach this today)

One question draws the line through everything: **did a real customer generate this signal?**

- **AI accelerating the handling of real evidence is the durable win.** Structured research notes synthesized in minutes instead of hours (the B2D workflow), interview guides drafted, screeners generated, themes clustered across studies — all of it legitimate, all of it conditional on the inputs being real observations of real customers.
- **Synthetic users are instruments, not evidence.** As of 2026 the field's own numbers make the boundary vivid: ~97% of researchers have AI in their workflow while only ~8% trust AI-generated participants as participants. Legitimate uses cluster where a false positive is cheap: piloting an interview guide before burning real recruits on it, stress-testing screener wording, triaging obviously-bad concepts. Illegitimate use is one step further: presenting the synthetic session's output as customer evidence.
- **Know the failure mechanism by name: sycophancy.** Head-to-head studies found synthetic users praised concepts that real users went on to question or reject, and predicted real behavior poorly. A fake user that tells you yes is worse than no user — it manufactures the confidence that discovery exists to destroy. This is **discovery cosplay**: shipping faster while learning nothing, with artifacts that look like learning.
- **Training-data drift makes it structural, not fixable by prompting.** A model reflects its training text — the past, and the general public's past at that. Asking it about your 2026 product yields a 2023 internet's idea of your customer. Grounded approaches (personas built from your own VoC data, with verifiable citations back to real quotes) are the research frontier, not the shipping practice — watch, don't teach.

The 80/20 division emerging as best practice: synthetic for the cheap front of the funnel (instrument piloting, screening), real humans for everything that becomes evidence — emotional insight, edge cases, cultural nuance, and every final decision.

## Eras

### Era 1 — Manual discovery (pre-2023)

Continuous-discovery habits fought a mechanical bottleneck: synthesis. Transcripts piled up; affinity-mapping ate the calendar; the interview→insight lag was measured in weeks. The era's discipline — small-n qualitative depth, direct customer contact as a weekly habit — was correct and survives untouched. What didn't survive was the assumption that synthesis cost is fixed.

### Era 2 — AI-accelerated synthesis (2023–2025)

The bottleneck broke. Structured notes (participant / task / observation / interpretation) fed to a model produced theme clusters, contradiction lists, and draft briefs in minutes — the B2D layer of this platform. Discovery cadence accelerated without changing its epistemology: every insight still traced to a real observed human. The era's boundary rule, already in the B2D lesson: AI finds patterns in your evidence; it must never *add* findings that aren't in it.

### Era 3 — Synthetic substitution, contested (2025–2026)

Vendors shipped "user research without the users": LLM personas you interview. Adoption ran far ahead of trust (97% touch / 8% trust), and the validity evidence arrived negative — sycophancy, poor behavioral prediction, training-data drift — capped by academic judgment (a 182-study systematic review converging on the same concerns; a January 2026 ACM *Interactions* piece calling AI-generated participants "a category mistake that undermines the purpose of research"). Meanwhile ~45% of researchers flagged the organizational risk: synthetic users invoked to justify cutting research contact with real customers. The era's live frontier is the middle path — VoC-grounded, citation-verifiable personas — promising for instruments, unproven as evidence.

## Deprecated patterns (stop teaching these)

- ❌ **Synthetic interviews as validation evidence** — the sycophancy finding makes this actively worse than skipping research: it manufactures false confidence with professional-looking artifacts.
- ❌ **"The model knows our users"** — it knows the internet's past. Training-data drift is structural; your current customer is not in the weights.
- ❌ **Cutting real customer contact because personas are cheaper** — the cost being saved is the product's connection to reality; that invoice arrives later, at C5's "cost of a wrong answer" scale.
- ❌ **AI-added findings in synthesis** — already the B2D rule; restated here because era 3 industrialized the temptation.
- ❌ **Speed as the discovery metric** — interviews-per-week was never the point; validated-learning-per-decision was. Acceleration that skips the customer optimizes the wrong term.

## What survived

Everything that made discovery discovery: continuous cadence, small-n depth, direct contact, evidence traceability. Era 2's structured-notes discipline survives as the compatibility layer — it's what makes AI synthesis safe (structured inputs of real observations) and what exposes synthetic substitution (no real observation, no structure to trace). The oldest instinct — *watch a real person attempt a real task* — remains the one activity no era has automated, because it's where the surprises live, and surprises are the product of discovery.

## Boundary conditions (where synthetic practice is legitimately correct)

- **Instrument piloting:** running an interview guide against a synthetic persona to find confusing questions before spending real recruits — cheap, low-stakes, honest.
- **Screener and survey pre-tests:** wording checks, logic-path walks, comprehension smoke tests.
- **Concept triage at the very top of the funnel** — screening obviously-broken ideas where a false "keep exploring" costs one more cheap iteration, not a roadmap commitment.
- **Never** in regulated, safety, health, or accessibility contexts — there the participant's reality is the entire point, and a synthetic stand-in isn't a shortcut, it's a category error with consequences.

## Signals to watch (would trigger Era 4)

- VoC-grounded persona systems (PersonaCite-class: interviewable personas with verifiable citations to real customer data) demonstrating predictive validity in longitudinal head-to-heads — would move grounded synthetics from instrument to limited evidence.
- IRB/regulatory rulings on synthetic participants — would draw the legal boundary this entry currently draws editorially.
- Measured behavioral-prediction parity on narrow task classes — would justify a scoped exception list, one task class at a time, never wholesale.

## Sources

- [Synthetic Users in 2026: 97% use, 8% trust](https://developmentcorporate.com/product-management/synthetic-users-in-2026-why-97-of-researchers-use-ai-but-only-8-trust-ai-generated-participants/) (2026) — adoption/trust gap, legitimacy-by-task survey, headcount-risk flag.
- [Synthetic Users vs Real Participants: What the 2026 Research Actually Shows](https://userevaluation.com/post/synthetic-users-vs-real-participants/) (2026) — sycophancy and behavioral-prediction failures; training-data drift; the 80/20 division of labor.
- Kuric, Demcak & Krajcovic — systematic review spanning 182 studies (cited in the above; obtain primary at Challenge step); ACM *Interactions*, Jan 2026 — "category mistake" position.
- [PersonaCite: VoC-Grounded Interviewable Synthetic Personas](https://arxiv.org/pdf/2601.22288) (arXiv 2601, 2026) — the grounded middle path; watch-list, not guidance.
- [Synthetic Users (vendor)](https://www.syntheticusers.com/) — the advocate position, for Challenge-step steel-manning.
- B2D lesson + `docs/misconception-log.md` root-cause vocabulary — this platform's internal boundary rules.
