---
id: "C7"
courseId: "tooling-misconceptions"
tier: "fluent"
roleIds: ["coach", "tl", "pm", "engineer"]
durationMin: 25
creditHours: 1
staircaseRung: 3
buildsBehaviors:
  - "Tier 3: classifies each team skill as BINDING or ADVISORY and can state the mechanical check that evidences a binding one"
  - "Tier 3: distinguishes shaping output (governance) from claiming a control without evidence it operated"
libraryRefs: ["agent-skills-format"]
rubric:
  - criterion: "Binding vs advisory, labeled"
    emerging: "Skills unlabeled; \"it's written in the skill\" is treated as a control"
    working: "Each skill is labeled BINDING or ADVISORY"
    strong: "The label matches reality — every BINDING skill has a mechanical check; the advisory ones make no control claim"
  - criterion: "Evidence it operated"
    emerging: "Points to the skill's text as proof"
    working: "Names the check that would fail the artifact"
    strong: "Produces what the check emits — a log line, a rejected item — sampleable evidence, not documentation"
  - criterion: "The line is drawn in the right place"
    emerging: "Tries to make a judgment call binding"
    working: "Binds structure, leaves semantics advisory"
    strong: "Can name a case where forcing a binding check would manufacture false confidence"
---

# It's In the Skill. Is It a Control?

> A coach ships a skill that tells the model to "always include a control-ID column." Months later, audit season: can you prove that happened on every artifact? "The skill says to" is not evidence. Two teams run the same library — one can produce the log of what the check rejected, the other can only produce the skill file. Same instruction, and only one of them has a control. This lesson is about which one you are, and how to choose it on purpose.

## Start Here: Why Does Your Best Skill Exist? (5 minutes)

Pick the skill your team relies on most. Write one sentence: *why does this skill exist?*

If the answer is "to make the model better at the task," notice that the ground is shifting under it. On a strong model, "make it smarter" is a weak and shrinking justification — the model is often already competent. The answer that holds up is different: the skill exists so that twenty people doing the same job produce the *same shape* of output, every time. That is not capability. That is governance, and it is the durable reason to own a skill library at all.

## Governance, Not Capability (6 minutes)

Here is the reframe worth internalizing, because it inverts the usual pitch. A stronger model makes governance skills *more* valuable, not less. Undertrained models fail visibly — the output is obviously wrong and review catches it. Strong models produce competent-looking *variation*, and plausible variation is far harder to catch in review than bad output. Twenty people prompting twenty different ways, each getting something reasonable-but-different, is precisely the problem a control exists to prevent.

That also changes the measure of success. The question is not "did this task go well." It is: *how much variation did this remove across everyone who does the job?* Dispersion reduction is measurable in a way "helpfulness" is not.

## Written Is Not Operated (6 minutes)

Now the most expensive misconception, because it produces the *appearance* of a control without the substance: believing that writing something into a skill makes it a control.

It does not. A control is something you can demonstrate *operated* — not something you can show was *documented*. "The skill instructed the model to include a control-ID column" is not sampleable. "The validator rejected four artifacts for missing control IDs, and here is the log" is. If you have ever worked under an audit, you know the difference is the whole game: evidence of operation, not evidence of intent.

## BINDING vs ADVISORY (6 minutes)

So label every skill as one of two kinds, explicitly, in the skill itself.

**BINDING** — scripted, enforceable, and citable as a control. It has a deterministic check (bundled or downstream) that *fails the artifact* when violated. It has an owner, a version, and a review date, because it is a controlled document. (Skills can carry executable code, not just prose — the current mechanics of that live in the Agent Skills library entry.)

**ADVISORY** — prose that shapes output but is explicitly *not* claimed as a control. This is where judgment lives.

Draw the line in one place: **structure is mechanically checkable; semantics are not.** Column presence, an ID format, every risk having at least one mapped control — that is a schema check, maybe thirty lines of code, and it should be binding. Whether the identified risk is the *right* risk, whether the control genuinely addresses it — that stays advisory, because a binding check on a judgment call manufactures false confidence. Mixing the two tiers without labels is how a team ends up claiming a control it cannot evidence.

## Assignment

Take a real skill library you own and make its control claims honest.

### Deliverables

- `skill-control-register.md` listing each skill labeled **BINDING** or **ADVISORY**
- For one BINDING skill: its **owner, version, review date**, and the **mechanical check** that fails the artifact when the skill is violated (name the check; if it doesn't exist yet, that's your finding)
- One line: a check you deliberately left **ADVISORY**, and why binding it would create false confidence
