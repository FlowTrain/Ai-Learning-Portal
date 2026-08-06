---
id: "C6"
courseId: "tooling-misconceptions"
tier: "fluent"
roleIds: ["coach", "tl", "engineer", "pm"]
durationMin: 25
creditHours: 1
staircaseRung: 3
buildsBehaviors:
  - "Tier 3: verifies a skill actually loads (description + discoverability) instead of assuming a file in the folder works"
  - "Tier 3: writes skill descriptions as trigger conditions, and diagnoses load → description → body in order before blaming the model"
libraryRefs: ["agent-skills-format"]
rubric:
  - criterion: "Description as trigger"
    emerging: "States what the skill is (\"a tool for X\")"
    working: "States when to use it (\"use when the user wants to …\")"
    strong: "States when, and declares negative scope (\"do NOT use for …\"), so it discriminates against the sibling skills in the same folder"
  - criterion: "Discoverability checked"
    emerging: "Didn't check whether the skill loads or where it lives"
    working: "Confirmed the file is named and placed so it can be discovered (<name>/SKILL.md)"
    strong: "Confirmed discoverable and produced evidence — a linter run, or a by-hand ranking of the description against its siblings"
  - criterion: "Diagnosis order"
    emerging: "Rewrote the body first"
    working: "Checked the description before the body"
    strong: "Checked load → description → body in order and can name what each step ruled out"
---

# Did Your Skill Even Load?

> Two coaches keep a team skill library. One keeps adding skills; half of them never fire, and the team has quietly concluded "the AI can't do that." The other keeps three, and they fire every time. Same tools, opposite results. The difference isn't the model — it's whether anyone checked that the skills load. You already know how to *write* a skill. Today you check whether the agent can *find and pick* it, which is a different question with a much quieter failure.

## Start Here: Read the Description, Cover the Body (5 minutes)

Open one skill you wrote. Cover the body — everything under the frontmatter. Read only the `description`.

Now answer honestly: for the request this skill is meant to serve, would an agent pick it over the other skills in the same folder, on that one sentence alone?

That is not a rhetorical exercise. It is exactly the decision the agent makes. When a skill is installed, the agent pre-loads only its name and description; it does not read the body until *after* it has already decided the skill is relevant — and it makes that decision on the description. (The current mechanics of selection and discovery live in the *Agent Skills* evolution entry, because they move; the habit you're building here does not.)

So the description isn't a summary of the skill. It *is* the skill, as far as getting chosen goes.

## The Description Is the Trigger, Not a Summary (6 minutes)

Most descriptions that fail are written as **identity**: "A tool for working with spreadsheets." It reads fine. It also cannot be selected, because it doesn't say *when* to reach for it, and "when" is the only thing the agent is matching against. Against five other skills that all mention spreadsheets, it discriminates against nothing.

Rewrite it as a **trigger** — a condition: "Use when the user wants to clean, edit, or chart data in an .xlsx or .csv file." Better still, add **negative scope**: "Do NOT use for scanning image-only PDFs." Negative scope is a strong signal precisely because it keeps the skill from being grabbed for an adjacent job that belongs to a sibling.

Here is the trap worth naming, because it wastes the most time. When a skill underperforms, the instinct is to open it and improve the body — add detail, add examples, add emphasis. But if the description never wins selection, **the body is never read**, and none of that work is ever seen by anything. You are tuning a file the agent never opened.

## The Failure You Can't See (6 minutes)

There's a worse version, and it has nothing to do with wording. A skill can be perfectly written and still never load because it's in the wrong shape or the wrong place — a flat file where a directory was expected, or a filename the agent doesn't scan for.

I ran a linter over a real skills directory recently. Four skills; three of them weren't loading — not because their descriptions were weak, but because they'd been saved as flat files instead of in the folder-and-file shape the format requires. Discovered by nothing. Loaded as nothing. Reported nothing. From the outside the directory looked like a working library. Most of it was empty.

Notice the shape of every failure in this lesson: **nothing errors.** No red text, no warning. The skill just isn't there, which from the outside is indistinguishable from the model being bad at the task. That silence is the entire problem — and it's why the fix is not "try harder," it's "add a check."

## Make It Loud (6 minutes)

You cannot catch a silent failure by being more careful, any more than you can hear an engine that isn't running. You need an instrument. A read-only linter for skills does for a skill library what a linter does for code: it surfaces the thing you'd never notice by rereading your own work — a description written as identity, two skills whose descriptions collide, a file that will never be discovered.

Run it on your folder before you conclude anything about the model. And build the ordering into how you work, because the order is the whole skill:

**What did you check, and in what order?** Load → description → body. Did the skill load at all? If yes, does its description win selection for the request? Only then does the body matter. Nine times out of ten the first link — did it even load? — was never examined, and the model, the last thing that could be wrong, gets blamed first.

## Assignment

Audit one real skill from a library you own, and make its status verifiable rather than assumed.

### Deliverables

- `skill-audit.md` covering one skill, with:
  - the **before/after description** — the identity version you started with, and the trigger version you rewrote (with negative scope if it earns one)
  - a **discoverability line** — confirm the skill is in the shape and place the agent actually scans, and say how you confirmed it
  - **evidence it loads** — a linter run pasted in, or, if you have no linter handy, a by-hand ranking of your description against the other skills in the folder for the request it should win
- One line naming a failure your check would still miss, and who or what you'd escalate it to
