---
id: "D5"
courseId: "leader-literacy"
tier: "native"
roleIds: ["leader"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 4 literacy: funds AI workflows, not AI tools — every investment names the workflow it changes"
  - "Tier 4 literacy: asks the three ownership questions before approving any AI spend"
rubric:
  - criterion: "Workflow specificity"
    emerging: "Investment described as a tool purchase ('we need Copilot licenses')"
    working: "Names the workflow the investment changes and who runs it today"
    strong: "Names the workflow, its measured current cost, and the artifact that will prove the change"
  - criterion: "Full-cost honesty"
    emerging: "Only license/subscription cost appears"
    working: "Includes token/usage cost estimate"
    strong: "Includes all three ROI terms: time saved, usage cost, and maintenance ownership"
  - criterion: "Decision clarity"
    emerging: "One-pager informs but asks for nothing specific"
    working: "Asks for a specific approve/reject decision"
    strong: "Asks for a decision with explicit success criteria and a review date"
libraryRefs: ["shift-left-economics"]
---

# Funding AI: The Investment One-Pager

> This track is Tier 4 *literacy*, not the architect track (D1–D4). You will not design a system in these three lessons. You will learn to fund, govern, and measure the people who do — which is your actual job in the maturity strategy. This lesson: funding.

## Start Here: What Are You Already Paying For? (5 minutes)

Write down every AI line item your org currently pays for — licenses, subscriptions, API budgets, tool seats. Next to each, answer one question in plain words: **what specific workflow changed because of it?** Not "people use it for lots of things" — a named workflow, with a named owner, that runs differently than it did before the spend.

For most leaders, several line items have no answer. That's the problem this lesson exists to fix, and it's a funding-discipline problem, not a technology problem.

## Fund Workflows, Not Tools

A tool purchase is not an AI investment; it's a precondition for one. The unit of investment is a **workflow**: a named, repeatable piece of work that will run differently — faster, cheaper, better-evidenced — with AI in the loop. Your Tier 3 practitioners already work this way (their certification requires ROI math on real workflows); the funding process should speak the same language.

The full cost of an AI workflow has three terms, and most proposals show you only one: **time saved** (the benefit), **usage cost** (tokens are metered — cost scales with use, unlike a license), and **maintenance** (prompts, context files, and skills decay as models change; someone must own the updates). A workflow that saves hours but has no maintenance owner is a liability wearing a benefit's clothes — approve it and you'll fund its slow decay into a source of confidently wrong output.

## The Three Ownership Questions

You don't need to read a schema or understand constrained decoding. Your literacy is knowing which questions expose an unfunded liability:

1. **"Who maintains this when the model updates?"** — a name, not a team.
2. **"What does it cost per run?"** — an estimate is fine; a blank stare is a red flag.
3. **"What breaks, and who notices?"** — every AI workflow fails sometimes; funded workflows have someone who notices before customers do.

If a proposal can't answer all three, it isn't ready for money. Send it back with the questions — that act alone raises your org's maturity.

## The One-Pager Format

One page, five blocks: **the workflow** (what runs differently, who runs it), **current cost** (how the work happens today — measured or honestly estimated, never invented), **proposed change** (the AI-assisted form and the artifact that proves it works), **full cost** (all three terms), and **the decision** (what you're asking for, the success criteria, and the review date). If it doesn't fit on a page, the proposal doesn't understand itself yet. (Why the review of this page is the cheapest quality gate the investment will ever pass — see the shift-left-economics Evolution Library entry.)

## Assignment

Write an investment one-pager for one real AI funding decision in front of your org right now (or the one you'd most like to force to clarity). Use the five-block format. Every number must be measured or labeled as an estimate — no invented statistics.

### Deliverables

- ai-investment-one-pager.md: all five blocks, one page
- The three ownership questions answered with names
- A review date and the artifact that will exist if the investment works
