---
id: "B5"
courseId: "enabled-pm"
tier: "enabled"
roleIds: ["pm", "engineer", "leader"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 2: sets model output constraints deliberately per use case — chooses a temperature range with a stated reason rather than accepting the platform default"
  - "Tier 2: writes AI behavior as a testable requirement (a threshold with a check) instead of a vague ask like 'make it consistent'"
libraryRefs: ["model-sampling-parameters"]
rubric:
  - criterion: "Range fits the use case"
    emerging: "Picks one setting for everything"
    working: "Differentiates low from high by broad category"
    strong: "Each use case has a range justified by its risk and its goal"
  - criterion: "Stated as a requirement"
    emerging: "Asks to 'make it consistent'"
    working: "Names a number"
    strong: "Writes a testable NFR — a threshold and the check that catches drift"
  - criterion: "Governance awareness"
    emerging: "No mention of who owns the setting"
    working: "Notes that sensitive cases need review"
    strong: "Names sign-off plus monitoring for out-of-range drift, and links the team risk-tier policy"
---

# Temperature: Setting the Dial as a Requirement

> You have been shipping AI features on a dial you never touched. Temperature is the control between repeatable and inventive output on a *single* model — and in a product it is not a default you inherit, it is a requirement you set. By the end you'll leave with a `temperature-policy.md` for one real feature: each use case matched to a range, with a reason and an owner.

## Start Here: Run It Twice (5 minutes)

Take a prompt you actually use at work — a status summary, a first-draft email, a bit of copy — and run it twice, unchanged, at whatever setting your tool opened with. Put the two outputs side by side.

Something changed between them. Maybe a little, maybe a lot. That variance is the whole lesson: the model samples its answer rather than looking it up, so the same prompt can land differently each time. You have been living with that variance without deciding how much of it you want. Hold those two outputs — we're about to make that a choice instead of an accident.

## The Dial (6 minutes)

Every general-purpose model produces text by choosing the next word from a ranked list of possibilities. Temperature governs how far down that list it is willing to reach. Turned low, it keeps taking the safest, most likely next word, so output is tight and repeatable. Turned high, it ranges further into less-likely choices, so output is more varied and more inventive — and less predictable.

Neither end is "better." Low is not more correct; high is not more creative in a way that helps every task. They are two settings for two kinds of job. The skill is not memorizing a number — it's knowing which end of the dial the job in front of you actually needs, and why.

One caution worth saying plainly: even at the lowest setting, output is not guaranteed to be identical every time. The honest claim is "more repeatable," not "deterministic." Teach yourself to want repeatability, not to expect a photocopy.

## Ranges by Use Case (7 minutes)

Here is the pattern to carry away: **match the setting to the job's goal *and* its risk.**

Work that has to be repeatable and defensible — anything that lands in an audit record, a regulated disclosure, a safety warning, a compliance-sensitive flow — wants the low end. You are buying consistency you can stand behind when someone asks why the system said what it said. Routine business communication sits in the middle, where a little variation reads as natural rather than robotic. Idea generation — brainstorming features, naming, exploring onboarding concepts — wants the high end, where you *want* the model to surprise you and you will curate the results yourself.

The specific numbers — vendor defaults, the exact range each scale runs, which use case maps to which value — are deliberately **not** written into this lesson, because they change and they differ by vendor. They live in the `model-sampling-parameters` Evolution Library entry, dated and sourced, so this lesson doesn't quietly teach a number that went stale six months ago. When you build your policy, pull the current figures from there. And note the era shift that entry tracks: on the newest reasoning-tier models the control is moving off temperature entirely onto an "effort" setting — the *concept* here (deciding how much variability the job should tolerate) survives, even as the knob changes shape.

## The Dial Is a Requirement (5 minutes)

Here is the move that makes this a Level-2 skill rather than a tip: temperature is a **Non-Functional Requirement**. It defines *how* the system behaves, not *what* it produces — the same category as latency, uptime, or accessibility.

That reframing changes how you write it down. "Make the output consistent" is not a requirement; nobody can test it and nobody owns it. "Responses in the disclosure flow must run at or below this range, checked in the PR" is a requirement — it has a threshold and a check, an engineer can implement it, and a reviewer can catch it when it drifts. The difference between those two sentences is the difference between hoping and governing.

The deeper governance work — how token cost and policy interact, how to set risk tiers across a whole product — is not this lesson's job to duplicate. It lives in C2 (token governance) and D6 (governing AI risk tiers without the architecture). What you own here is the literacy: knowing the dial is yours, and writing it as a requirement someone can check.

## Assignment (2 minutes to read, ~20 to do)

**Part A — feel the ends.** Take one real scenario with a clear stake. (A worked example: a SaaS onboarding flow loses most of its users at the payment step.) Run the same prompt twice — once at a compliance-mode low setting, once at a creative-mode high setting (use the current values from `model-sampling-parameters`). Write down what actually changed: the language, the structure, the *kinds* of solutions offered, and the risk each carried.

**Part B — write the policy.** Produce a `temperature-policy.md` for one feature you actually work on. A simple table: each AI use case in that feature × its approved range × a one-line rationale tied to the use case's risk and goal × who signs off. That last column is not decoration — a requirement without an owner is a wish.

You'll know it worked when the policy gets *cited* — referenced in a PR, a spec, or a review — rather than filed and forgotten. That is the signal that the dial stopped being an accident and became a decision your team can stand behind.
