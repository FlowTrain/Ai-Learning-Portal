---
id: "A2"
courseId: "aware-foundations"
tier: "aware"
roleIds: ["pm", "coach", "designer", "leader"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 1→2: reuses a prompt that worked instead of retyping from memory"
  - "Tier 2: maintains a small personal prompt library with known failure modes"
libraryRefs: ["prompting-frameworks"]
---

# Your First Prompt Library

> A prompt you use once is a tool. A prompt you write down and improve is an asset. This lesson establishes the habit that separates AI-Aware individuals from AI-Enabled teams: treating prompts as reusable artifacts rather than one-off queries.

## Start Here: Find Your Repeat (5 minutes)

Scroll back through your AI chat history from the last two weeks. Find one request you've typed more than once — different words, same intent ("summarize this doc for my boss," "turn these notes into an email"). That repeat is your first library entry. You've already done the hard part: discovering a prompt worth keeping.

## The Prompt Card Format

Now give that repeat a home. Every prompt card has five fields: **Intent** (one sentence: what is this prompt for?), **Inputs** (what context does the prompt need — what does the caller provide?), **Prompt** (the actual template, with {{placeholders}} for variable content), **Expected Output** (what good looks like), and **Failure Modes** (what bad looks like, and why). The failure modes field is what separates a prompt library from a notes file.

## When to Write a Card

Write a card when: (1) you've used the same prompt pattern more than twice, (2) you got a result good enough to repeat, or (3) you discovered a failure mode worth warning teammates about. Don't write cards for one-off queries. The test: would a teammate on your team benefit from this card without further explanation from you?

## Library Governance

A prompt library is a living document. Treat it like a changelog: when a prompt stops working well (model update, product change, new constraint), update the card and note what changed and why. A prompt library that isn't maintained becomes worse than no library — it breeds false confidence in stale patterns. (How prompt-writing advice itself changes over time is tracked in the Evolution Library: see the prompting-frameworks entry.)

## Assignment

Build the first 3 cards of your personal prompt library. At least one card must come from a real prompt you've used in your actual work — not a synthetic example. At least one card must include a documented failure mode from real experience.

### Deliverables

- personal-prompt-library.md with exactly 3 cards
- Each card: Intent, Inputs, Prompt (with placeholders), Expected Output, Failure Modes
- One card must reference a real product artifact you own
- One card must document a real failure mode you observed
