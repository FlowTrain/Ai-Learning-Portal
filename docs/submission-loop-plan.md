# Plan — Submission & Feedback Loop with a Bedrock-Backed Judge

> **Status:** **Decisions recorded 2026-07-15 (§8) — plan revised, approved to build.** Two owner
> answers materially changed the design: **local-first** (§1) and **the coaches are not the calibration
> source** (§4). Revises **BACKLOG 10**, whose escape clause —
> *"automated/LLM grading… explicitly out of scope **until demanded**"* — fired on **2026-07-15**
> (cohort request: a box to paste or upload an artifact and get Claude's feedback). Constraint given:
> **the only sanctioned path to Claude is the AWS Bedrock SDK.**
>
> **This request breaks two of BACKLOG 10's own scope guards.** One is negotiable. One is a wall.
> Read §1 before designing anything.

---

## 1. The wall — "no backend" cannot survive Bedrock

BACKLOG 10's Waffle-House scope guard says **"no backend."** The app today is exactly that:
`app/build.py` → `app/dist/index.html`, *"single file, no server."*

**Bedrock cannot be called from that file.** Every Bedrock SDK request is signed with AWS credentials
(SigV4). Credentials cannot go in a browser — anyone who opens the page owns them. There is no
configuration, no build flag, and no clever trick that makes a static HTML file safely call Bedrock.

So the no-backend rule and the Bedrock requirement are **mutually exclusive**. One of them has to go,
and it isn't Bedrock (that's the org's mandate, not our choice).

**The options, honestly:**

| Option | What it is | Verdict |
|---|---|---|
| **A — Thin backend** (recommended) | One small service (Lambda + API Gateway, or a container) holds an IAM role with `bedrock:InvokeModel`. The app POSTs `{lessonId, artifact}`; the service loads the rubric, calls Bedrock, returns feedback. | **Take this.** Smallest thing that works. Keeps creds, rubric, model id, and cost control server-side. Python/boto3 matches the existing toolchain (`build.py`). |
| **B — Cognito identity pool** | Browser gets temporary AWS creds, calls Bedrock directly. Technically "no server." | **No.** Anyone with the page gets model access. No cost ceiling, no abuse limit, no prompt-injection guard, and the rubric becomes client-side and therefore editable. This is a static-file rule being honored in letter while being violated in spirit. |
| **C — Keep it human** | Ship BACKLOG 10 as originally scoped: export the artifact + rubric, coach grades in the worksheet. No Bedrock. | **Viable fallback**, and it's the calibration set either way (§4). But it does not answer what the cohort asked for. |

**The real decision is not technical.** It is: *does the learning platform stop being a static build
target and become a deployed service?* That brings hosting, an AWS account, IAM, a cost line, and an
owner. It is a small service, but it is a permanent one. Say yes deliberately or say no deliberately —
don't drift into it.

### 1.1 DECIDED — Option A, but **local-first until approved** (owner, 2026-07-15)

> *"Yes — but running off the app on the desktop from the `app/dist/index.html` file till fully approved."*

**This is the right call and it dissolves the blocker.** The interim is a **local loopback service**:
a small Python process (matches the existing `build.py` toolchain) that serves `app/dist/index.html`
and exposes one local endpoint, signing Bedrock calls with **the operator's own AWS credentials/SSO
from their local AWS config**. Nothing is deployed. No hosting, no public surface, no cost line, no
on-call, nothing to approve except *"an app on my laptop calling an approved model with my own
credentials."*

**The honest consequence — and it turns out to be a feature.** Local-first means **the coach/owner
runs the judge, not each learner** (learners will never have AWS credentials). So the interim flow is:

```
learner exports artifact  (§7 step 1 — the worksheet/export, no backend)
   → coach/owner runs the judge locally over the batch
      → feedback returns through the coach, reviewed with the learner
```

That is **exactly the flow decision 6 asked for anyway** ("before coach so they have something to
review with the learner"). The interim architecture and the target experience agree — which means
**§7 step 1 is not merely calibration prep; it is the interim product.** Build it first with no
regrets: it ships value, produces the gold set, and is the delivery mechanism until the service is
approved.

**Deferred to approval:** the deployed service (§7 step 3) is the same code with the credentials
moved from a laptop to an IAM role. Design the endpoint now so that swap is the only change.

## 2. The good news — the judge's contract already exists

**Rubrics live in lesson frontmatter** (workspace convention: *"Rubrics live in lesson frontmatter so
they version with content"*). Every lesson already carries 3 criteria × emerging/working/strong.

That means the judge needs **no new evaluation criteria**. The whole call is:

```
{ the lesson's rubric, verbatim from frontmatter }
+ { the learner's artifact }
+ { the judge's constitution (§3) }
→ per criterion: emerging | working | strong
+ the evidence in the artifact that justifies it
+ exactly one next step
```

The rubric is the spec; the judge executes it. This is the same pattern as the rest of the fleet — the
contract is the artifact, the model is bounded execution. It also means **feedback can never drift
from the lesson**, because they version together in one file.

## 3. The judge needs a constitution — and this is the part that will bite

An LLM judge with no constitution will default to the smartest voice it knows, which is the **Tier 4
owner's voice**. That is the workspace's #1 documented risk (curse of knowledge), pointed directly at
the most fragile population we have.

**Remember who is standing at this box.** The cohort feedback that produced the Level 1 expansion was:
*"people don't believe they will make it past these stages."* A judge that returns **emerging /
emerging / emerging** to someone already convinced they can't do this does not give them information.
It confirms their fear, and they quit. **Feedback tone is not a nicety here; it is the retention
mechanism.**

The judge gets its own governed identity — same pattern as `soul.md`:

- **Pinned to the learner's tier**, not the owner's. A Tier 1 artifact is judged by Tier 1 standards,
  in Tier 1 vocabulary. The banned-words lists in the A5–A8 specs apply to the *feedback*, not just the
  lesson.
- **Names what works first, and specifically.** Generic praise is worse than none.
- **Exactly one next step.** Not three. One. (Waffle House rule, applied to feedback.)
- **Never a score, never a grade, never pass/fail.** Hard rule: *assessment is artifacts + observed
  behaviors, never quizzes.* Emerging is a position on a staircase, not a failure — the feedback must
  read that way or the word does damage.
- **"Emerging" always comes with the concrete move to "working."** Never a diagnosis without a next action.
- **Cites the artifact.** Every judgment quotes the learner's own words back. No unevidenced verdicts —
  the same diagnose-with-evidence posture the CCQG Auditor runs under.
- **Refuses to invent.** If the artifact is empty, off-topic, or unreadable, say so plainly and ask for
  the thing — do not hallucinate a grade.

Lives at `app/judge/soul.md`, versioned, and it is a **reviewed artifact**, not a prompt someone tweaks
in production.

## 4. Calibration — BACKLOG 10 said "calibrated judge" and meant it

An uncalibrated judge is confidently inconsistent, which is worse than no judge because it *looks*
authoritative. Do not skip this to ship faster.

### 4.1 CORRECTION — the coaches cannot be the gold set (owner, 2026-07-15)

> *"I am the regulator. Coaches are Monday morning too, and it's fake it till they make it."*

**This breaks the calibration plan as originally written, and it's the most important thing the owner
said.** The draft above assumed a coach hand-grades the gold set. **An uncalibrated grader cannot
produce a gold standard** — you'd calibrate the judge to the coaches' guesswork and then discover the
judge is confidently reproducing it at scale. Coaches who are themselves Monday-morning learners are
*consumers* of the standard, not sources of it.

**Revised: there is exactly one calibrated human in this system, and it's the owner.**

1. **The owner hand-grades the gold set** — N artifacts per lesson, against the frontmatter rubric.
   Start where volume and fragility both live: **A0 plus the new A5–A8 as each ships.** Suggested N =
   5–8 per lesson; enough to anchor, small enough to actually finish.
2. Those become the judge's few-shot anchors **and** the agreement test.
3. **Ship the judge only when it agrees with the owner** at the threshold (§8.4). Disagreements are
   the prize either way: either the judge is wrong, or **the rubric was ambiguous** — and an ambiguous
   rubric is a content defect found for free, before a cohort hits it.
4. **Coaches then learn the standard from the judge**, not the reverse.
5. Re-run the agreement test **whenever the model id changes**. Bedrock model updates are silent from
   our side; the judge can get quietly worse. That's the drift problem D1 teaches, arriving in our own
   product before we teach it.

**Suggested threshold rule** (owner to confirm, §8.4): per-criterion exact match on the gold set, and
— the hard gate — **never off by two.** Emerging-vs-working is a conversation. **Emerging-vs-strong is
disqualifying**; a judge that can't tell those apart is not calibrated, it's decorative.

### 4.2 What this reframes — the judge is the coaches' training wheels

Put decisions 4 and 6 together and the product changes shape:

> **The judge is not the learner's grader. It is the coach's scaffold.**

Coaches are faking it till they make it and are standing in front of learners anyway. The judge —
calibrated to the one Tier 4 human — gives every coach a consistent reference to review *with* the
learner. **That scales the owner's calibration into every room he isn't in**, which is a materially
better product than the box that was requested. It also means the judge's tone requirements (§3) are
doing double duty: they model *for the coach* how to give rubric-anchored feedback without crushing
someone. The coach learns coaching by watching the judge coach.

Consequence to accept: **the owner is now on the critical path.** The gold set is the gate, and nobody
else can produce it. That's real hours. It is also the highest-leverage hours available — it's the
only work here that can't be delegated, and everything downstream is mechanical once it exists.

### 4.3 Model selection folds into the same test (decision 5)

Owner reports the sanctioned options as **Opus 4.8, Sonnet, and Haiku** (exact model id / inference
profile to be pulled from the gatekeeper or local Claude config — **do not guess it; pin it**).

Don't pick a model by intuition — **the agreement test already is the model-selection test**:

1. Establish the gold set (owner, §4.1).
2. Calibrate on the **strongest** available (Opus 4.8) to prove the rubric and the judge constitution
   are sound. If Opus can't hit the threshold, the *rubric* is the problem, not the model.
3. Then test **Sonnet** and **Haiku** against the same gold set.
4. **Ship the cheapest model that agrees at threshold.** Grading is high-volume — every learner ×
   every lesson — so this is where the token bill actually lives.

This is the golf-bag lesson (`right-model-right-job`, A4/C2, the `token-economics` entry) run on the
platform itself, with a real number at the end. **That's the case study, for free, from work you had
to do anyway.**

**Dogfooding, and it's the good kind:** this *is* the eval-harness capstone (BACKLOG 6) — built on the
platform, for the platform, before it's taught. The rubric-vs-judge agreement test is a real eval set
with a real calibration story. Nobody has to invent a case study; we'll have lived one.

## 5. The A5 collision — the platform must obey its own lesson

We are about to ship **A5 — The Red Lines** ("never paste confidential data; here's your personal
card") and, on the same screens, a box that says **"paste your artifact here."**

If the platform violates the lesson it just taught, the curriculum loses credibility on contact — and
it *deserves* to. The artifacts are the learner's real work: A7's moments list names real meetings; a
B2 exercise can carry real product detail.

**Requirements, non-negotiable:**

- The submit box **shows the learner their own red-lines rule at the point of paste** — not buried in a
  policy link. A5 is the feature's copy, and the feature is A5's proof.
- **Bedrock is the answer here, not the problem** — an org-approved path that keeps the call inside the
  org's own AWS account is *why* this can be offered at all. Surface that in one plain line at the box,
  because it directly answers the fear A5 creates.
- **Do not assert AWS's data-handling policy in our own words.** Link AWS's stated Bedrock policy and
  the org's approval. (Workspace hard rule: no vendor claims. This is exactly the trap A5's spec warns
  authors about — we don't get an exemption for our own UI copy.)
- **Retention is an owner + org decision, not a default.** Submissions are the eval set, which means
  they are *stored*, which means someone owns how long and where (§8). Decide before the first paste,
  not after.

### 5.1 DECIDED — and one hard pushback (owner, 2026-07-15)

**Recorded:** AWS account = **the client's (day job)**. Retention = **2 years**. Visible to **learner,
coaches, L&D**.

**Clarified (owner, same day): L&D *are* the coach group** — support-side, quasi-level-3 escalation,
with comms duties. Non-traditional, same as the owner. **That dissolves the surveillance framing**
this section originally carried: L&D seeing artifacts *is* the coaching relationship, not a third
party watching it. The three-audience split below has been withdrawn. Two things survive the
correction, on better grounds:

**1. Name people by function in the UI, never by department.** If L&D are coaches, the submit box
says *"your coach sees this"* — never *"L&D."* This isn't spin; it's more accurate. And it matters
because **the learner's perception is what governs whether they submit honestly**, regardless of the
org chart. A Tier 1 learner who already doubts they belong reads "L&D" as HR-adjacent and starts
polishing. The word is the whole risk here; the people aren't.

**2. Retention follows the *purpose*, not the audience.** There are two purposes, and they want
different windows:

| Purpose | What it needs | Window |
|---|---|---|
| **The coaching conversation** (coaches incl. L&D, per decision 6) | The individual artifact + feedback | **As long as the engagement, plus a short tail.** Learner can delete. |
| **Curriculum repair + comms** (the misconception log, L3 support) | **Aggregate, de-identified patterns** — which criteria go emerging, which lessons cluster misconceptions, which rubrics are ambiguous | **2 years.** This is the durable asset. |

Two years on an *individual* artifact is longer than the relationship that justifies it — that's a
purpose mismatch, not a trust problem. Two years on the *corpus* is exactly right: it's the eval set
and the content-defect record.

**And the aggregate view isn't a privacy sop — it's the product their job actually needs.** L3 support
with comms duties needs *patterns*: what's breaking, what question keeps arriving, what to send out on
Monday. That's the misconception log, and it's more useful to them than a pile of transcripts. So they
get **both views for their two different jobs** — individual artifacts when coaching, patterns when
supporting. Build both; they're the same data, cut differently.

**Still worth writing down** (hygiene, not alarm): this runs in the **client's AWS** on **client
employees' real work**. Record the retention + visibility model somewhere the client can see it before
the first paste — not because anyone here is a risk, but because "we decided this on purpose in July"
is a much better sentence than reconstructing it later.

## 6. Scope fence (the Waffle House guard, re-applied)

**In:** paste-or-upload box on the lesson page → thin backend → rubric-anchored feedback (per-criterion
level + evidence + one next step) → the coach worksheet → `docs/misconception-log.md`.

**Out, until demanded the way this was:** accounts, notifications, scores, badges, leaderboards,
streaks, progress bars, video, resubmission workflows, cross-learner comparison. **Especially
leaderboards** — for a population that doesn't believe it will progress, ranking is the single most
destructive feature we could ship.

## 7. Build sequence (each step shippable, each step useful alone)

1. **The worksheet + export** — BACKLOG 10 as originally scoped. No backend, no Bedrock. Produces the
   calibration set. *Useful even if everything below is cancelled.*
2. **The judge's constitution** — `app/judge/soul.md` + the rubric→prompt assembly, runnable offline
   against saved artifacts. No UI, no deploy. Reviewable as a document.
3. **The thin backend** — Lambda/container, IAM role, one endpoint, the org's approved model id from
   their platform team. Rubric loaded server-side from lesson frontmatter. Rate limit + cost ceiling on
   day one, not later.
4. **The agreement test** — judge vs. coach on the calibration set. **Gate: no ship without it.**
5. **The box** — the smallest UI: paste/upload, red-lines reminder, feedback panel. A-series only first.
6. **The loop closes** — misconception log entries feed content edits. That was always the real prize.

## 8. Decision log — **answered 2026-07-15 (owner)**

Append-only. Reversals get a new entry, never an edit.

| # | Decision | Owner's answer | Consequence |
|---|---|---|---|
| 1 | Deployed service? | **Yes — but local-first**, running from `app/dist/index.html` on the desktop until fully approved | §1.1. Local loopback service, operator's own creds. Nothing deployed. §7 step 1 becomes the interim product. |
| 2 | Whose AWS / cost / on-call? | **The client's (day job) AWS** | §5.1 flag: platform IP + client data + employee learning records now share an account. Separate them on purpose. |
| 3 | Retention & visibility | **2 years; learner, coaches, L&D** — and **L&D *are* the coach group** (support-side, quasi-L3, comms duties; non-traditional) | §5.1 — **clarified; surveillance concern withdrawn.** Surviving asks: (a) UI names people by **function** ("your coach"), never "L&D"; (b) retention follows purpose — individual artifacts = engagement + tail, **de-identified corpus = 2 years**. |
| 4 | Agreement threshold / arbiter | **"I am the regulator. Coaches are Monday morning too — fake it till they make it."** | §4.1 — **plan corrected.** Coaches cannot produce the gold set. Owner hand-grades it. Judge becomes the coaches' scaffold (§4.2). Threshold rule proposed: exact match, **never off by two**. **Owner to confirm the number.** |
| 5 | Model id | Options: **Opus 4.8 / Sonnet / Haiku**; exact id from the gatekeeper or local Claude config | §4.3 — don't choose by intuition. Calibrate on Opus, ship the cheapest that agrees. **Pin the id; retest on change.** |
| 6 | Judge before/after/instead of coach | **Before** — "so they have something to review with the learner" | §4.2 — confirms the scaffold framing, and matches the local-first flow exactly. |
| 7 | Fallback if #1 is no | **Agreed** | Moot — #1 is yes. Local-first is a staged version of the same protection. |

**Also recorded:** leaderboards / ranking — *"the over-my-dead-body feature that will not happen."*
Promoted from §6's out-list to a standing prohibition. Nothing in this plan ranks learners against
each other, ever.

### 8.1 Still open (blocks nothing yet, blocks §7 step 5)

1. **Retention purpose-split (§5.1)** — individual artifacts scoped to the engagement, de-identified
   corpus kept 2 years? (Surveillance concern withdrawn — L&D are coaches. This is now a
   purpose-fit question, not a trust one.)
2. **The agreement number** (§4.1) — "never off by two" is the gate; what's the exact-match rate?
3. **Gold-set size** — 5–8 artifacts per lesson proposed. Owner's hours are the constraint.
4. **Written blessing** on retention + visibility from the client side (§5.1). The one item that can
   hurt a person.
