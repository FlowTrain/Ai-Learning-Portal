---
id: "A4"
courseId: "aware-foundations"
tier: "aware"
roleIds: ["pm", "coach", "engineer", "tl", "designer", "data", "leader"]
durationMin: 20
creditHours: 1
staircaseRung: 1
buildsBehaviors:
  - "Tier 1: picks a tool deliberately instead of using the same AI for everything"
  - "Tier 1→2: can explain in plain language when AI is and isn't appropriate for a task"
libraryRefs: ["token-economics"]
---

# Right Tool, Right Task

> The most expensive AI mistake teams make is reaching for the most powerful tool for every task. Some AI tools cost far more per use than others, and the powerful ones do worse — not better — on tasks that aren't prepared for them. This lesson builds the habit of matching the tool to the job.

## Start Here: Your Last Five (5 minutes)

Write down the last five times you used an AI tool for work. Next to each one, answer in plain words: did you get what you needed on the first try? If not, how many tries did it take? Keep this list — it's the raw material for the assignment, and the pattern in it is usually visible immediately: the frustrating ones were the wrong tool, the wrong preparation, or both.

## The AI Tool Stack

**Search-and-summarize tools (Copilot 365, Notion AI):** Best for finding and condensing content that already exists in your workspace. Cheapest to run. They can't invent what they can't find — which for this job is a feature.

**Chat tools (Claude, ChatGPT, Gemini):** Best for single-transformation tasks — take this input, produce this output. Ideal for drafting, rewriting, changing format, and refining your own requests.

**Agentic tools (Claude Code, Cursor, GitHub Copilot Agent):** Best for multi-step tasks that require reading and writing files across a project. Most expensive per session. Only worth it when the tool has a written project description to read before it starts.

## The Two-Question Test

Before opening one of the expensive tools, ask: (1) "What file will exist when I'm done that someone else will reuse?" If you can't name it, this belongs in a chat window. (2) "What does the tool get to read about my project before it starts?" If the answer is nothing, you're about to pay for the tool to guess at your entire project.

If you can't answer both questions, the task isn't ready for an agentic session.

## Cost Reality

The expensive tools are metered: every session costs real money, and an unprepared session costs several times more than a prepared one while producing worse output. You don't need to know the pricing tables — you need one habit: treat chat as cheap and agentic sessions as metered, and never start a metered session without something written down for the tool to read first.

## Assignment

Take your "last five" list from the opening activity. For each entry, identify: which tool you used, which tool was the best fit, and what written context (if any) you gave it before starting. Then write a "tool selection rule" for your specific role that you would share with a new teammate.

### Deliverables

- right-tool-audit.md with 5 real task entries (task, tool used, best-fit tool, context provided)
- A 3-5 rule 'tool selection guide' for your role — written to be handed to a new team member
- One example of a task where you'd switch tools based on this lesson
