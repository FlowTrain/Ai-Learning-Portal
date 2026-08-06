---
id: "B5D"
courseId: "enabled-design"
tier: "enabled"
roleIds: ["designer", "pm", "tl"]
durationMin: 25
creditHours: 1
staircaseRung: 3
buildsBehaviors:
  - "Tier 2/3: declares a layout as a UI schema referencing a data schema instead of pasting flattened markup"
  - "Tier 2/3: can name what the handoff paste silently drops, and states the precise claim (AI replaces the handoff, not design)"
libraryRefs: ["schema-driven-ui"]
rubric:
  - criterion: "Layout declared, not pasted"
    emerging: "Describes the screen as a picture or a paste"
    working: "Expresses it as a UI schema that references a data schema"
    strong: "Keeps data / UI / token layers separate with one canonical source"
  - criterion: "Names what the handoff dropped"
    emerging: "Treats handoff as merely slow"
    working: "Names one decision the paste left the implementer to guess"
    strong: "Shows how the declared version makes that decision reviewable"
  - criterion: "The precise claim about design"
    emerging: "Says AI replaces design / Figma"
    working: "Says it replaces the handoff, not exploration or the review surface"
    strong: "Can name what stays with design tools, and why"
---

# AI Replaces the Handoff, Not the Design

> The fear in the room is that AI replaces designers. It doesn't — and putting it that way makes designers defensive *and* gets the claim wrong. What AI, and a declared layout, replaces is the **handoff**: the moment a design becomes a mockup someone else has to translate back into a working screen. That translation always leaked. This lesson moves the design decision out of the translation and into a contract — a file the whole team can read, diff, and be wrong in on purpose.

## Start Here: Where Did the Decision Actually Get Decided? (5 minutes)

Take one screen your team shipped recently. Pick a single specific choice — a spacing, a state, a breakpoint — and trace it back to where it was *decided*. Not where it was drawn; where it was decided.

Most of the time the honest answer is: in someone's head, then redrawn on a canvas, then guessed at in code. Hold that answer — the rest of the lesson is about closing that gap.

## The Handoff Was Always Lossy (6 minutes)

There's a whole genre of "design handoff specs," and it exists for one reason: handoff is a translation between two representations — a canvas and a codebase — and translations leak. When a mockup is pasted in as flattened markup, whatever the designer *meant* by that spacing or that state arrives as one undifferentiated blob, and the implementer (human or AI) re-infers intent from pixels because nothing was declared. Sometimes the inference is right. Nobody knows which times, because there's nothing to check it against.

That's the real cost — not the keystrokes. The design decision was never written down anywhere, so it gets reconstituted by guess.

## Three Layers, Three Names (6 minutes)

The fix is to declare it. There are three layers, and each has a real name (the current tooling specifics live in the `schema-driven-ui` library entry, because they move):

- **Data schema** — what the thing *is*: the fields, their types, their relationships.
- **UI schema** — how it's *laid out*, referencing the data schema. The standard phrasing: the data schema tells *what*, the UI schema tells *how*.
- **Design tokens** — how it's *styled*: color, spacing, type — ideally emitted in the standard token format so you inherit the tooling instead of inventing a private dialect.

Keep them separate: the domain schema is canonical, the UI schema references it, and the API contract is generated from it. One source, three artifacts. A single schema trying to serve both the screen and the API becomes a compromise that serves neither — the API wants normalized and resource-shaped, the view wants denormalized and display-shaped.

## The Paste Is Where the Contract Dies (5 minutes)

Watch the actual keystroke. Pasting a flattened mockup isn't just tedious — it's the moment the contract disappears. Before the paste, the design decision *could* have been a file. After it, it's a guess.

So declaring the layout isn't about less clipboard; it changes **who holds the intent** — from a designer's memory to a reviewable, diffable artifact that three roles (the spec reader, the UI implementer, the later API implementer) can coordinate on without a shared vocabulary. That shared artifact even has a name: a **boundary object**.

## The Lab-Demo Tell (3 minutes)

One field note worth keeping. If a slick AI-design workflow only works on a freshly imaged, specific machine — the brand-new laptop, the exact setup — you're watching a demo that survives under laboratory conditions, not a process. It's usually a sign that the thing being shown is the tool, not a workflow someone can run on a Monday. Ask which of your own pilots would pass that test.

## Assignment

Express one real screen as a contract instead of a picture.

### Deliverables

- `ui-contract.md` — one screen as the three layers: a small **data schema** (what it is), a **UI schema** that references it (how it's laid out), and which **token set** styles it
- One sentence: what the old paste-the-mockup path left the implementer to **guess**
- One line: whether this workflow would survive on a machine that isn't yours — the lab-demo test
