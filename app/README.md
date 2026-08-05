# The App — a Build Target, Not a Source

Content lives in `content/` and `library/`. This folder turns it into a browsable app. Never edit lessons here; edit the Markdown and rebuild.

## Build

```
pip install pyyaml markdown jsonschema
python app/build.py
```

Output: `app/dist/index.html` — one self-contained file, no server, open it in any browser (double-click works). Share it by sending the file.

## What the app includes

- **Role picker → placement diagnostic** — the Monday-Morning Diagnostic as an intake flow, driven entirely by `content/diagnostic.json` (the app implements the conjunctive-ladder rule type; questions, flags, and routing are data).
- **Course catalog + lesson viewer** — from `roles.json`, `courses.json`, `lessons/*.md`.
- **Evolution Library viewer** — from `library/evolution/*.md`.
- **Architect Zone** — teaser cards from `content/teasers.json` with interest capture (views/opens/notify-me in browser localStorage, exportable as JSON — see `docs/interest-capture.md` for the decision rules the signals feed).

## Guardrails

- The build **validates before it ships**: lesson frontmatter against `lesson.schema.json`, diagnostic against its schema, course→lesson and routing→course referential integrity. Broken content fails the build with a list of errors.
- Lesson titles come from each file's first `# ` heading; everything else from frontmatter.

## Verified acceptance (BACKLOG 7, 2026-07-10)

Editing a lesson `.md` and rebuilding updates the app with zero code edits; catalog data loads from JSON; invalid content fails the build.
