---
id: "C5"
courseId: "fluent-chains"
tier: "fluent"
roleIds: ["tl", "engineer", "data", "leader", "coach"]
durationMin: 30
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 3: evaluates an AI-data proposal by question cadence, full cost, and failure modes — not by tool familiarity"
  - "Tier 3: can state the case FOR the two architectures they didn't propose"
libraryRefs: ["prompting-frameworks", "context-engineering", "token-economics", "shift-left-economics"]
rubric:
  - criterion: "Question-first framing"
    emerging: "Compares tools by features"
    working: "Scores options against the team's actual question census"
    strong: "Census includes cadence, asker, and cost-of-wrong-answer per question"
  - criterion: "Steel-manning"
    emerging: "Own option praised, others strawmanned"
    working: "Each option's legitimate best-fit case stated"
    strong: "Each option scored by a question type it wins — including the two not chosen"
  - criterion: "Full-cost honesty"
    emerging: "License/compute costs only"
    working: "Includes token economics and maintenance ownership"
    strong: "All three cost terms plus failure modes (write-back risk, context exhaustion, egress) with sources"
---

# Where Should the Answers Live? (Three Teams, One Question)

> Three teams want AI-powered reporting from the same data. One says "just give everyone a chatbot connected to the source system." One says "build a data lake and let AI write the queries." One says "stand up a central operational data store and put AI on top." All three are right — about different questions. This lesson teaches the comparison pattern that turns an unwinnable architecture argument into a decision.

## Start Here: The Question Census (5 minutes)

Before any architecture talk, take a census. Write down the last five reporting questions your team actually asked of your work-tracking data. For each one, note three things in plain words:

1. **Cadence** — was it asked once, weekly, or continuously?
2. **Asker** — a person exploring, an analyst scanning history, or a product surface that displays the answer automatically?
3. **Cost of wrong** — what happened (or would happen) if the answer was wrong?

Keep the census. It is the input to everything that follows — and here's the punchline in advance: when three teams argue past each other about architecture, it's almost always because they each did this census silently, on different questions, and don't know it.

## Three Teams, Three Answers

Each answer below is presented the way its own team would present it — best case first. Your job in this section is not to pick a winner. It's to be able to argue *for* each one. (In a cohort, these are three separate sittings: one team's world at a time.)

### Team One: Chat With Your Data

Connect the AI assistant directly to the source system and let everyone ask their own questions. The case for it is real: fastest possible adoption, zero infrastructure to build, no waiting on a platform team, and every person gets answers in their own words on day one. For occasional, low-stakes, personal questions — "summarize what my team shipped this sprint" — this is the *correct* architecture, and heavier options are over-engineering.

What its advocates undercount: every user pays the machinery cost on every question. Connecting an AI to a rich enterprise tool means loading the tool's entire vocabulary into the AI's working memory before the first question — an input tax that can consume most of the AI's attention before any work happens — and raw responses from enterprise APIs arrive bloated with metadata the question never needed. Worse, letting the AI *write back* to the source system crosses a risk boundary: round-tripping rich content through the AI's plain-text world can silently destroy formatting, with no error raised. The patterns and current numbers behind all of this live in the Evolution Library (see the token-economics and context-engineering entries); the durable lesson is that per-person convenience has a per-question price, and it compounds with cadence.

### Team Two: The Lakehouse

Land the raw data in cheap object storage, project a schema over it, and let the AI translate plain-language questions into SQL that a serverless engine executes. The case for it is real: it's built for scanning the world — years of history, millions of records, questions nobody predicted. Storage is nearly free, you pay per scan, and smart storage formatting cuts scan costs by orders of magnitude. For analyst-shaped work — "how has cycle time trended across all projects since 2022?" — this architecture wins outright, and a chat tool pointed at the live system simply cannot do the job.

What its advocates undercount: the audience. AI-generated SQL is production-viable but not infallible — it needs schema access, semantic help, and an error-recovery loop, which means it needs an owner. The architecture is shaped like its builder: an analyst who scans history. The PM who needs the same three numbers every Monday morning, delivered to a dashboard without asking, is not the user this system was designed for — and retrofitting that cadence onto per-scan pricing has its own bill.

### Team Three: The Operational Data Store

Stand up one governed database that holds the operational data in query-ready form — relational tables for the structured facts, flexible document storage for the messy custom fields, semantic search for the unstructured text — and point both AI and dashboards at it. The case for it is real: continuous questions get continuous answers, product surfaces get a stable contract to display, one store gets governed once (access, compliance, retention), and it can align with where the organization's data platform is already heading. For product operational reporting — answers that appear on screens without anyone asking — this is the architecture the other two eventually grow into.

What its advocates undercount: it's the biggest commitment on the table. Someone must own the pipeline, the schema, the sync from source systems, and the platform bill — before the first user sees value. It is the right third step taken confidently; taken as a first step by a team without platform ownership, it's an expensive way to discover that.

## The Six Questions

The census resolves the argument, because architecture follows questions. Score every option against these six — this is the whole pattern:

1. **What cadence are the questions?** Once → chat. Exploratory-over-history → lakehouse. Continuous → data store. (This is A4's two-question test at enterprise scale.)
2. **Who asks?** A person → chat. An analyst → lakehouse. A product surface → data store.
3. **What does a wrong answer cost?** Personal drafts tolerate errors; a dashboard executives read does not. Stakes set the review and governance burden (the cost curve behind this question lives in the shift-left-economics Evolution Library entry).
4. **Who maintains it when the model or API updates?** A name, not a team. An architecture nobody owns decays into confidently wrong answers.
5. **What breaks, and who notices?** Every option fails differently: silent formatting corruption, a mis-joined query, a stale pipeline. Name the failure and its detector before choosing.
6. **Where is the org already going?** Platform direction is a legitimate scoring question, not a bias. An option aligned with the data platform's roadmap inherits support; an option fighting it inherits friction.

Questions 4 and 5 are the leader track's ownership questions (D5); questions 1–3 are your question census, formalized. Notice what the pattern does to the three teams: it stops asking "which is right?" and starts asking "which questions does each one win?" — and suddenly there are answerable sub-decisions instead of one unwinnable fight. Most real organizations end up running two of the three on purpose. The failure mode is running all three by accident.

## Assignment

Run the pattern on your real situation. Take your question census from the opening (grow it to at least five real questions if needed). Score all three architectures against the six questions. Write a one-page decision memo.

### Deliverables

- architecture-decision-memo-[topic].md: one page
- The question census: 5+ real questions with cadence, asker, and cost-of-wrong for each
- The six-question scoring table: three options × six questions
- A recommendation, the strongest objection to it stated fairly, and — for each option you did NOT choose — the question type it would still win
