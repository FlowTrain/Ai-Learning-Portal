---
id: "D6"
courseId: "leader-literacy"
tier: "native"
roleIds: ["leader"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 4 literacy: governs by action risk, not by tool bans"
  - "Tier 4 literacy: sets the risk-tier policy and delegates its enforcement to architects"
rubric:
  - criterion: "Risk classification"
    emerging: "Policy governs tools ('approved AI tools list') rather than actions"
    working: "Classifies AI actions into the four risk tiers with examples from own org"
    strong: "Every tier has org-specific examples plus an explicit escalation path between tiers"
  - criterion: "Proportionality"
    emerging: "One rule for everything (all AI use needs approval / no AI use needs approval)"
    working: "Requirements scale with tier — light touch at read-only, heavy at high-risk"
    strong: "Requirements scale with tier and the policy names what is deliberately NOT governed"
  - criterion: "Delegation boundary"
    emerging: "Policy specifies technical enforcement details the leader can't evaluate"
    working: "Policy states requirements; enforcement design is explicitly delegated"
    strong: "Requirements + delegation + a named review cadence with the architects who enforce it"
---

# Governing AI: Risk Tiers Without the Architecture

> Second lesson in the leader literacy track — still not the architect track. D1 teaches practitioners to *build* governance infrastructure: approval flows, audit logs, rollback procedures. This lesson teaches you to *set the policy* that infrastructure enforces. You write the "what"; architects build the "how."

## Start Here: The Undo Test (5 minutes)

List five ways people in your org used AI this month (ask, don't guess). For each one, answer a single plain question: **if the output was wrong, could the action be undone?** A summary someone read — undone by re-reading. An email sent to a customer — not undone. A config change in production — depends entirely on what noticed it first.

You've just performed risk-tier classification. Everything else in this lesson is vocabulary for what you just did.

## The Four Risk Tiers

AI actions — not tools, actions — fall into four tiers, and this classification is the entire technical vocabulary you need:

1. **Read-only** — the AI looked at things and produced words a human will review: summaries, drafts, analyses. Wrong output costs a person some time.
2. **Reversible** — the AI changed something that can be cleanly undone: a document edit, a ticket update, a draft commit.
3. **External** — the AI's output left the building or crossed a boundary: sent to a customer, published, fed into another team's system. Undo is no longer clean.
4. **High-risk** — customers, money, production systems, regulators, or personal data are directly affected. Wrong output has consequences a rollback doesn't fix.

The governing principle: **requirements scale with tier.** Read-only work should be nearly friction-free — over-governing it just drives usage underground and kills the Tier 1 habit-building your maturity strategy depends on. High-risk work gets human approval, logging, and a rollback plan, always.

## Govern Actions, Not Tools

The most common governance mistake at leadership level is the tool ban ("no ChatGPT") or its twin, the tool blessing ("Copilot is approved"). Both govern the wrong noun. The same tool doing read-only summarization and drafting customer emails is operating at two different risk tiers — one deserves near-zero friction, the other deserves review. Policy written against tools ages badly (tools change monthly) and invites workarounds. Policy written against action risk stays true across every tool your org will ever adopt.

## The Policy Draft and the Delegation Line

Your policy draft is one page: the four tiers with examples from your own org, what each tier requires (nothing / logging / human review / approval-plus-rollback), and one line stating what is deliberately ungoverned (say it out loud — silence reads as prohibition to a nervous Tier 1 workforce). Below that, the delegation line: enforcement design — the approval flows, audit logging, and eval pipelines that make the policy real — belongs to your D1-track architects, reviewed with you on a named cadence. If you find yourself specifying log formats, you've crossed into work you can't evaluate; step back up.

## Assignment

Draft the risk-tier policy for your org. Classify at least eight real AI actions (from the Undo Test list and beyond) into the four tiers. State requirements per tier and the delegation line.

### Deliverables

- risk-tier-policy-draft.md: four tiers, org-specific examples, requirements per tier
- At least 8 real AI actions classified, including at least 1 you'd move to a *lower* tier than current practice treats it
- One sentence naming what is deliberately not governed
- The delegation line: who builds enforcement, and the review cadence with them
