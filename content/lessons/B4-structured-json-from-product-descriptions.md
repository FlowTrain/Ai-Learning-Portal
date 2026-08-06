---
id: "B4"
courseId: "enabled-pm"
tier: "enabled"
roleIds: ["pm", "coach", "engineer", "tl", "designer", "data"]
durationMin: 25
creditHours: 1
staircaseRung: 3
buildsBehaviors:
  - "Tier 2→3: defines the schema before asking AI for structured output"
  - "Tier 2→3: validates machine-readable output before it enters a pipeline"
libraryRefs: ["structured-outputs"]
---

# Structured JSON from Product Descriptions

> Machine-readable output from AI is only useful when the structure is right. This lesson teaches you to turn product descriptions into validated JSON for Storybook configs, service inventories, and automation pipelines — without relying on AI to guess the schema.

## Define the Schema First

The fastest way to get bad JSON from AI: ask for JSON without specifying the schema. The right workflow: (1) write the target schema in a comment or example, (2) provide the structured description, (3) prompt AI to populate the schema from the description. When the schema is explicit, AI fills fields correctly. When it's implicit, AI invents fields and omits required ones.

## Validation Criteria

Before using AI-generated JSON, validate: all required fields are present and non-null, field values match the types in the schema, array values are arrays (not comma-separated strings), enum fields contain only valid values, and no invented fields appear that aren't in the schema. A JSON linter catches type errors. Only a human who knows the product can catch invented content. (How enforcement of structure has shifted from prompts to APIs to decoders — and why valid never means correct — is tracked in the Evolution Library: see the structured-outputs entry.)

## High-Value Use Cases

The highest-ROI JSON generation workflows for product teams: (1) Storybook component configs from UI descriptions, (2) service inventory JSON from service boundary docs, (3) test fixture data from acceptance criteria, (4) feature flag configs from PRD sections. Each of these drops from a substantial manual chore to minutes with AI — when the inputs are structured.

## Assignment

Define a JSON schema for one product artifact you regularly create (component config, service inventory, feature spec). Use AI to populate the schema from one of your structured descriptions. Validate the output and document what required correction.

### Deliverables

- json-output-[artifact].json: the populated, validated JSON
- json-schema-[artifact].json or inline schema definition
- json-notes.md: what the AI got right, what it invented, what required correction
- Use case note: how this JSON will be consumed downstream (Storybook, pipeline, etc.)
