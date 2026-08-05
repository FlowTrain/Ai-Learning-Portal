# Interest Capture — The Architect Zone as a Demand Sensor

BACKLOG 6 (architect-track depth) is deferred by owner decision (2026-07-10): the current population is overwhelmingly Tier 1, and the deep content is owner-authored material that shouldn't be built ahead of demand. But an empty zone teaches us nothing. This spec turns the zone into a sensor: clickable marketing stubs (`content/teasers.json`) that collect curiosity signals while the real content waits for its audience to climb toward it.

## What gets tracked

Per teaser card, three signal strengths (weakest to strongest):

| Signal | Event | What it means |
|---|---|---|
| **View** | Card rendered on screen | Foot traffic past the shop window. Baseline only. |
| **Open** | Card clicked/expanded | Active curiosity — they wanted the details. |
| **Notify me** | Registered with role + placed tier | A named human deferring a want. The only signal that counts toward build triggers. |

Each notify-me stores: teaser id, role, placed tier (from the diagnostic, if taken), timestamp. No free-text, no email in the stub phase — the app already knows who's logged in when there's a real backend.

## Decision rules (what the signals decide)

Signals are only worth collecting if they're wired to decisions in advance:

1. **Build trigger:** a teaser accumulating notify-me registrations from people placed **Tier 3** (or Tier 2 with fluent-chains certification underway) is a build candidate — those people can actually take the module. Review at each quarterly platform review; build in registration order, not owner preference order.
2. **Marketing signal, not build signal:** notify-me volume from **Tier 1/2** placements means the *teaser copy* is doing its job (aspiration visible from the bottom of the staircase). It informs comms and Tier 1 on-ramp motivation — it does not trigger building rung-3 content nobody can climb to yet. This distinction is the staircase rule applied to demand data.
3. **Kill/rewrite trigger:** a teaser with healthy views but near-zero opens after a quarter has a title/hook problem — rewrite the card. Near-zero views means a zone-placement problem in the app.
4. **Curriculum feed:** open-rates per topic feed the Evolution Library build order (founding entries 4–6) — e.g., heavy interest in Agentic Workflow Engineering pulls the `agent-orchestration` entry forward.

## Dashboard tie-in

These metrics join the D7 dashboard spec as the **demand family** (alongside placement, certification, reuse): "notify-me registrations by teaser × placed tier, monthly." It informs exactly one decision: what to build next in the architect zone.

## Stub-phase implementation (no backend)

The static app (BACKLOG 7) records events in browser `localStorage` and provides an **Export interest data** button (downloads JSON) in the architect zone footer. Honest limitations, documented deliberately: per-browser (not per-person), lost if storage is cleared, aggregated only when a coach collects exports (e.g., during cohort sessions or via a shared drop folder). This is acceptable for the deferral period — the point is directional signal, not analytics precision. When the platform gets a backend, the event shape here is the contract.

## Maintenance

- Review teaser set whenever BACKLOG 6 items ship (a built module's teaser retires; its accumulated registrations become the invite list).
- Quarterly: apply decision rules 1–4, note outcomes in BACKLOG.md.
