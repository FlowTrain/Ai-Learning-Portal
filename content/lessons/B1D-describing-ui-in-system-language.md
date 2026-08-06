---
id: "B1D"
courseId: "enabled-design"
tier: "enabled"
roleIds: ["designer"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 2: describes screens in component/variant/state language, not visual language"
  - "Tier 2: includes accessibility constraints in every UI description"
---

# Describing UI in System Language

> Design tools powered by AI work best when designers speak the same language as the system. This lesson teaches you to describe any screen in terms that feed directly into Storybook, engineering specs, and AI design tools — eliminating the translation layer that currently sits between design and engineering.

## Component Language vs. Visual Language

Designers naturally describe what they see: 'a blue button with rounded corners and a shadow.' Engineers and AI tools need to know what the thing is: 'Button, variant=primary, size=md, state=default, with icon-left.' The shift from visual to component language is the single most impactful change a designer can make for AI-assisted workflows.

Component language maps to: component name (from your design system), variant (from the component's variant set), state (default, hover, focus, disabled, loading, error), and props (the data it displays).

## Layout Regions and Hierarchy

Before describing individual components, describe the layout: what regions exist (header, sidebar, content, footer, overlay), what the primary content hierarchy is (what's most important on this screen), and how the regions relate (which regions are fixed, which scroll, which collapse). This layout map is the skeleton that makes the component descriptions meaningful.

## Accessibility as a Specification Constraint

Accessibility requirements belong in the description, not in a separate doc. Every component description should note: keyboard navigation behavior, screen reader label, focus order, and any WCAG constraint that affects the implementation. AI tools that receive these constraints generate implementations that don't require accessibility retrofits — the most expensive design debt a team can accumulate.

## Assignment

Choose one screen from your current product. Write a complete structured description: layout regions, component inventory with system language, data elements, states, and accessibility constraints. This document should be reviewable by an engineer without any verbal explanation from you.

### Deliverables

- ui-layout-[screen].md: layout regions → component inventory → data elements → states → accessibility
- All components described using design-system names and variant/state language
- At least 3 states documented (including one error or empty state)
- 2 accessibility constraints explicitly called out
