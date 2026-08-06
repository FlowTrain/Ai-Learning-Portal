---
id: "B1"
courseId: "enabled-pm"
tier: "enabled"
roleIds: ["pm", "coach"]
durationMin: 25
creditHours: 1
staircaseRung: 2
buildsBehaviors:
  - "Tier 2: structures workspace files so retrieval AI reliably finds them"
  - "Tier 2: writes retrieval-friendly titles and summaries as a routine habit"
libraryRefs: ["context-engineering"]
---

# AI-Ready PM Workspace

> Copilot 365 and retrieval-based AI tools are only as smart as the files they can find. This lesson redesigns your workspace so that every file is findable, every document is AI-parseable, and every retrieval query returns what you actually need.

## The Retrieval Problem

Most Microsoft 365 workspaces fail AI retrieval for the same reasons: files are named after dates instead of purpose, there are no index documents, and folders mix work types (meetings, decisions, specs, and reference material all share a folder). Copilot doesn't know what a file is for — it infers from the file name, folder path, and first paragraph. All three need to be signal-rich. (This lesson is the retrieval-tool form of a larger discipline tracked in the Evolution Library: see the context-engineering entry.)

## The AI-Ready File Structure

A product workspace that works with AI has: a **/specs** folder (PRDs, tech specs, one-pagers), a **/decisions** folder (ADRs, trade-off documents), a **/meetings** folder (structured meeting notes with clear outcome sections), a **/prompts** folder (your prompt library), and an **index.md** or **README.md** in each folder describing its purpose. The index file is the single highest-leverage 15-minute investment you can make.

## Writing Retrieval-Friendly Content

AI retrieval matches on keywords in context. Write document titles as questions or clear statements: 'Q3 2026 Checkout Redesign — Decision Log' beats 'checkout-v2-final-FINAL.docx'. Start every document with a 2-3 sentence summary. Use consistent section headings across all documents of the same type. The 5 minutes you spend on naming and structure saves 20 minutes every time you or a teammate searches.

## Assignment

Restructure one product area's SharePoint or Teams folder to follow the AI-ready file structure. Write or update the index document for that area. Demonstrate one retrieval query that now works reliably.

### Deliverables

- ai-ready-file-org.md: your actual folder structure with the new layout and naming conventions
- index.md (or equivalent) for one restructured folder — minimum 5 sections
- 3 example Copilot retrieval queries that now work reliably against this structure
- Before/after note: what queries failed before, and why they work now
