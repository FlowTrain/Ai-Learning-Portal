---
id: "D7"
courseId: "leader-literacy"
tier: "native"
roleIds: ["leader"]
durationMin: 25
creditHours: 1
staircaseRung: 3
buildsBehaviors:
  - "Tier 4 literacy: measures maturity by observed behaviors and reused artifacts, not tool usage"
  - "Tier 4 literacy: reads the tier-distribution gap against the role×tier target matrix and funds against it"
rubric:
  - criterion: "Metric validity"
    emerging: "Metrics count tool usage (logins, prompts sent, licenses active)"
    working: "Metrics track behaviors and artifacts (diagnostic placements, certified workflows)"
    strong: "Includes at least one reuse metric — artifacts consumed by someone other than their author"
  - criterion: "Measurability"
    emerging: "Metrics lack a measurement method ('track AI fluency')"
    working: "Every metric has a source, method, and cadence"
    strong: "Every metric has source, method, cadence, owner, and a stated decision it informs"
  - criterion: "Gap orientation"
    emerging: "Dashboard reports absolutes with no target"
    working: "Reports current tier distribution against the role×tier target matrix"
    strong: "Reports the gap, its trend, and ties each funded investment (D5) to the gap it closes"
---

# Measuring AI Maturity: The Dashboard Spec

> Last lesson in the leader literacy track. You've funded workflows (D5) and set the risk policy (D6); this lesson builds the instrument that tells you whether any of it is working. You will not build the dashboard — you will write the spec that makes it buildable, which is a rung-3 artifact: precise enough that someone else can implement it without asking you what you meant.

## Start Here: The Vanity Audit (5 minutes)

Write down every AI number anyone has ever put in front of you: adoption rates, license utilization, prompts per week, "engagement." For each, ask the only question that matters: **if this number doubled, would anything about your org's work provably be better?** Prompts-sent can double because people are flailing. Logins can double because of a mandate. Usage is what maturity looks like from too far away to see behavior.

## Measure Behaviors, Not Usage

Your platform already defines maturity behaviorally — the Monday-Morning Diagnostic places people by five observable checks, and every lesson tags the behaviors it builds. So the measurement layer is already designed; the dashboard just reads it. The three metric families that mean something:

- **Placement:** tier distribution by role, from real diagnostic intakes — not self-assessment, which over-places almost everyone.
- **Certification:** artifacts graded against lesson rubrics — prompt libraries, chains, skills, context files. An artifact is evidence; a completed video is not.
- **Reuse:** the true-north family. A prompt library *used by someone other than its author*, a skill run by a second team, a chain handed off. Reuse is the only metric that can't be gamed by enthusiasm, because it requires someone else to have found the artifact worth picking up.

## The Gap Is the Dashboard

An absolute number ("34% Tier 2") is trivia. The dashboard's job is the **gap**: current tier distribution per role versus the role×tier target matrix in the maturity model, and the trend of that gap. This is also where D5 and D7 connect — every investment one-pager should name the gap it closes, and the dashboard should show whether it did. A leader reading this dashboard makes exactly three kinds of decision: fund something (a gap isn't closing), govern something (a risk metric moved), or celebrate something specific (a reuse number earned it).

## The Spec Format

A dashboard spec is a contract, so it's structured: for each of five metrics — **name, definition, source, measurement method, cadence, owner, and the decision it informs**. If any field is blank, the metric isn't real yet. Two constraints: at least one metric from each family (placement, certification, reuse), and no metric that a tool vendor could report for you — if it comes free with a license, it's measuring the license, not your people.

## Assignment

Write the maturity-metric dashboard spec for your org: five metrics, all seven fields each, at least one per family, gap-oriented against the target matrix. Hand it to someone technical and ask them one question: "Could you build this without talking to me?" Their answer is your grade.

### Deliverables

- maturity-dashboard-spec.md: 5 metrics × 7 fields (name, definition, source, method, cadence, owner, decision informed)
- At least one placement, one certification, and one reuse metric
- The gap view: current vs. role×tier targets, with trend
- One named vanity metric you are explicitly declining to track, and why
