# Evidence Audit — Context Switching, High WIP, and the Churn Calculator

> **Why this exists:** the churn cost model's assumptions (20% context-switching impact, "up to 35%
> cost / 4–10x lead time") were flagged as the calculator's attack surface. Owner's answer: the
> never-released **High WIP essay** (Nov 2023) and the **Neurodivergent Context Switching Burnout
> series**. Both now in `research/`. This is the honest read on whether they close the gap.
>
> **Verdict up front: partly — and not the way you'd expect.** The essay doesn't source the numbers.
> The series does have real research in it, but its own headline number is sourced to a vendor blog.
> Fixable in an afternoon; fatal if published without fixing.

---

## 1. The High WIP essay (Nov 2023) — good argument, zero numbers

It's a Weinberg-lineage thought piece. Four claims, all qualitative, all sound:

1. **The myth of multitasking** — *"Time lost in context switching increases as the number of
   processes increases."* (Weinberg)
2. **Quality takes a back seat** — the woodpecker line.
3. **Burnout and productivity decline** — high WIP → burnout → more post-release fixes → more strain.
4. **Ripple effect on team dynamics** — *"No matter how it looks at first, it's always a people
   problem."* (Weinberg)

**It contains no statistics at all.** So it does **not** source the churn calculator's 20%. It's a good
essay and it should be released — but not as evidence.

**However — it points at the actual source, and you should go get it.** The framework's **20% context-
switching impact almost certainly descends from Weinberg's own model** (*Quality Software Management,
Vol. 1: Systems Thinking*, 1992 — the widely-reproduced table where 1 project = 100% of time on task,
2 projects = 40% each + 20% lost to switching, 3 = 20% each + 40% lost, and so on).

**Cite that table, with book and edition, and the 20% stops being folklore and becomes a named,
30-year-old model from a named authority.** That alone survives most of the room.

**But be honest about what it is** — and this is the part that protects you: **Weinberg presented it as
a model, not a measurement.** It is illustrative arithmetic, not an empirical study. Anyone who knows
the literature knows that. So:

> Don't claim it's measured. Claim it's Weinberg's model, name it, and **hand them the dial** — let
> them set the switching cost themselves. It's still millions at 10%.

Claiming measurement you don't have is the only way to actually lose this argument.

## 2. The Neurodivergent series — genuinely strong, with one load-bearing crack

This is a serious piece of work: 43 sources, real structure, and an argument that lands. It's also
**80% publishable as-is**. The problem is concentrated and specific.

### 2.1 The crack: your headline number is sourced to a blog

**"Up to 40% of productive time"** carries the entire economic argument — it appears in §I, Table 1,
§V, and twice in the Conclusions. It is currently cited to **[1] a corporate vendor blog**.

**And you don't need that blog — you already cite the real source two footnotes later.** Source **[2]
is the APA's own page on multitasking switch costs**, which is where the "up to 40%" figure actually
comes from (Rubinstein, Meyer & Evans, 2001). **Swap [1] → [2] on every instance of the 40% claim** and
the number goes from attackable to institutional. That's a find-and-replace, and it's the single
highest-value edit in the document.

### 2.2 Source triage — what to fix before publishing

| Claim | Currently cited to | Strength | Do this |
|---|---|---|---|
| **"Up to 40% of productive time"** (headline) | [1] Tyfoom blog | ❌ Vendor blog | **Re-cite to [2] APA** — you already have it |
| "Interrupted every 3 min; 20+ min to recover" | [10] Shelidon blog | ❌ Blog | This is **Gloria Mark (UC Irvine)**, *The Cost of Interrupted Work* (2008) — the real figure is ~23 min 15 s. Cite Mark directly |
| **"HBR: neurodivergent teams up to 30% more productive"** (your ROI headline) | [38] galtstaffing, [39] hrfuture | ❌❌ **Two aggregators, neither is HBR** | **Verify against the actual HBR piece** — Austin & Pisano, *"Neurodiversity as a Competitive Advantage"* (HBR, 2017). My strong suspicion: HBR reports **specific company results (SAP, HPE)**, not a blanket 30%. If so, this claim as written is an aggregator's paraphrase and it is **the most attackable sentence in the series** |
| Burnout $4k–$21k/employee | [7] CUNY SPH → *Am. J. Preventive Medicine* | ⚠️ Secondary but traceable | Cite the AJPM study directly |
| 40% of turnover from stress; 120–200% replacement cost | [8] UMass Lowell CPH-NEW | ✅ Academic center | Fine; note the date |
| 57% ad-hoc meetings; 48%/52% chaotic | [15] Microsoft Work Trend Index | ✅ Strong primary | Keep, date it |
| $1 → $4–6 safety ROI | [22] OECS blog | ❌ Vendor blog | Trace or cut — it's decorative, not load-bearing |
| Dyslexia task-switching difficulty | **[33] Reddit** | ❌❌❌ | **Cut it.** A public series cannot cite r/Dyslexia. The GMB dyspraxia toolkit [34] is real; lead with that |
| Switch-cost mechanism, ADHD/ASD executive function | [2] APA, [4][5][24][31][36][37] Frontiers / PMC / T&F / PubMed | ✅ Peer-reviewed | **This is your spine.** It's excellent |

**The pattern:** the *science* is well-sourced (APA, Frontiers, PMC, Taylor & Francis, PubMed, Microsoft).
The *business numbers* are blog-sourced. A five-part public series invites exactly the scrutiny the
churn meeting does — and the business numbers are what a skeptic attacks, because they're the ones that
cost them money.

### 2.3 The unit collision — and yes, it's the same bug again

**Weinberg's 20% and the APA's 40% are not the same number, and they don't measure the same thing:**

| | Weinberg 20% | APA 40% |
|---|---|---|
| **Unit** | Productivity lost **per additional concurrent project** | Percentage of **an individual's productive time** lost to task switching |
| **Scope** | Organizational WIP allocation | Individual cognition |
| **Type** | A **model** (illustrative arithmetic, 1992) | An **experimental finding** (2001) |

They support each other rhetorically; **they cannot be added, averaged, or substituted.** If the churn
calculator uses 20% and the series says 40%, someone will ask which one is right and the honest answer
is "neither — they're different questions." **Declare the unit and the scope for both.**

*(For the record: this is the **third** instance today of the same disease — org sums graded against
team benchmarks in Product Family Health, "Churn Rate 121%" graded against a `<20%` scale, and now a
1992 model sitting next to a 2001 experiment. **A number graded against a rubric that was never built
for it.** That's not sloppiness — that's an entire career's worth of evidence that the unit/scope
contract is the load-bearing idea in your book.)*

## 3. What's genuinely excellent — and what to lead with

**"The fragility of hyperfocus" (§IV, final paragraph) is the best idea in the series and it is buried.**

The argument: many neurodivergent people can enter intense, sustained deep work — the single
highest-value cognitive state available to an organization. **That state is inherently fragile.** When
an external interruption shatters it, the switch cost is *amplified far beyond* the fractional penalty
a neurotypical colleague pays.

Which means:

> **A high-WIP environment doesn't just tax everyone a little. It systematically destroys the best deep
> work in the building, in exactly the people most capable of producing it.**

That's not an inclusion footnote on an efficiency argument. **It's a better explanation of the same
data**, and it's the thesis. Lead Part 1 with it.

**Two more strengths:**

- **"Neuroinclusive Design as Universal Best Practice" (§V) is the un-arguable frame.** Every
  accommodation — written instructions, protected focus time, clear priorities, no-meeting blocks — is
  just good management. Nobody can oppose it without opposing competence. This is how the series avoids
  being filed under "DEI initiative" and gets filed under "operating model," which is where it belongs
  and where it has teeth.
- **The distribution insight is confirmed.** A flat "20% switch cost" is exactly the kind of average
  §2B of Product Family Health warns about — it hides where the harm lands. The series *is* the
  distribution behind that average.

## 4. The three artifacts are one argument — that's the series

Separate, each is attackable. Combined, the chain is hard to break:

| Piece | Role | Source of authority |
|---|---|---|
| **High WIP essay** (2023) | **Mechanism** — why WIP causes switching causes defects and burnout | Weinberg, qualitative |
| **Neurodivergent series** | **Evidence + stakes** — the cost is real, quantified, and lands unevenly on your best people | APA, Frontiers, PMC, Microsoft |
| **Churn calculator** | **Local proof** — here's what it costs *this* org, in dollars | Your own data, their dials |

**This is how the never-happy conversation gets won** — not with a bigger number, but with mechanism →
evidence → local cost → *and it's burning out the people who do your deep work.* The dollar figure is
arguable. The chain isn't.

**Suggested 5-part shape:**

1. **The fragility of hyperfocus** — lead with the strongest idea, not the definitions
2. **The switch cost is real and it isn't evenly distributed** — APA + the neurotype detail; the average hides the harm
3. **The architecture of distraction** — how *we* built this (meetings, tools, reactive leadership); no villains, systems
4. **High WIP is the upstream cause** — the Weinberg essay, finally released, as the bridge to delivery
5. **What it costs and what to do** — neuroinclusive design as universal practice + the churn model with the dials in their hands

## 5. Publishing gate (do these first)

- [ ] **Re-cite the 40% to APA [2]**, not the blog [1] — every instance
- [ ] **Verify the HBR 30% claim** against Austin & Pisano (2017) directly. If HBR doesn't say it, **cut
      it or restate what HBR actually reported.** This is the one that ends your credibility if wrong
- [ ] **Cut the Reddit citation [33]**; use the GMB dyspraxia toolkit [34]
- [ ] **Cite Gloria Mark directly** for the interruption/recovery figures
- [ ] **Cite Weinberg's QSM Vol. 1 (1992)** for the 20% — and say plainly that it's a model, not a study
- [ ] **Declare unit + scope** wherever 20% and 40% appear near each other
- [ ] Trace or cut the $1→$4–6 safety ROI [22]
- [ ] **No day-job data anywhere in the public series** — the churn model appears with the *modeled*
      exemplar and reader-set dials only (`research/client-confidential/README.md`)
