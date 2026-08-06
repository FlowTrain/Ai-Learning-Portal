---
id: "B2D"
courseId: "enabled-design"
tier: "enabled"
roleIds: ["designer"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 2: structures research notes before asking AI to synthesize"
  - "Tier 2: distinguishes AI-found patterns from fabricated findings"
libraryRefs: ["ai-product-discovery"]
---

# AI-Assisted UX Research Synthesis

> Research synthesis is the highest-volume cognitive task in design. AI can compress synthesis work to a fraction of its manual time — if you provide structured notes rather than raw transcripts. This lesson builds the workflow.

## The Structured Research Note Format

Raw transcripts fail AI synthesis because the signal-to-noise ratio is too low. The fix: turn transcripts into structured notes before prompting. Format: participant label, task they were performing, observation (what happened), and interpretation (what it might mean). When every note has this structure, AI can cluster themes, identify contradictions, and surface patterns that would take hours to find manually.

## From Synthesis to Design Brief

AI can transform a structured research synthesis into a design brief in one step — if the synthesis is specific enough. The prompt: 'Given these research findings, identify: (1) the top 3 user goals, (2) the top 3 friction points, (3) one design principle that should guide this feature.' The output becomes the first section of your design spec. Review it for accuracy; don't fabricate findings that aren't in your research. (Where AI acceleration ends and evidence substitution begins — including why synthetic users flatter concepts real users reject — is tracked in the Evolution Library: see the ai-product-discovery entry.)

## Design System Language

Before engaging Figma AI or any AI design tool, translate your design intent into design-system language: component names (not visual descriptions), token names (not hex values), state names (not visual behaviors). 'A button that turns blue when hovered' costs Figma AI credits to interpret. 'A Button component, variant=primary, state=hover' is processed in one shot. The translation step belongs in a chat window before you open Figma.

## Assignment

Take research notes from a real usability study or user interview (use sanitized data if needed). Structure them in the observation/interpretation format. Run synthesis through AI and produce a design brief. Evaluate what the AI got right and what required your judgment.

### Deliverables

- research-synthesis-[feature].md: structured notes (min 8 observations) → AI synthesis → design brief
- Design brief: top 3 user goals, top 3 friction points, 1 design principle
- Critique: 2 AI synthesis points you kept, 2 you revised, 1 it missed entirely
- One component description in design-system language ready for Figma AI
