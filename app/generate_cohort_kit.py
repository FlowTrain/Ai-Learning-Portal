#!/usr/bin/env python3
"""Cohort Kit Generator (BACKLOG 8) - any course becomes a facilitated cohort kit.

Usage:   python app/generate_cohort_kit.py <course-id> [--profile standard|accelerated]
Output:  cohort-kits/<course-id>-cohort-kit.md  (accelerated: <course-id>-accelerated-kit.md)

Profiles:
  standard    (default) Bundle DNA: 1 lesson/week, 2 assignments/week (A = opening
              activity on real work, B = artifact), biweekly 30-min debriefs,
              check-in week at 5+ content weeks, break at 6+. ~1 hr/week.
  accelerated 4 touchpoints/week: 3 lessons/week as individual assignments
              (prep + artifact each) + 1 weekly 60-min debrief with a group
              activity (artifact swap - reuse tested live). ~3 hrs/week, for
              cohorts with dedicated learning time. No check-in/break weeks.
Both end in a public showcase (Quantic rhythm). Regenerate, don't hand-edit.
"""
import json, re, sys, glob, datetime, pathlib

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent
TIER_ORDER = ["aware", "enabled", "fluent", "native"]
TIER_NAMES = {"aware": "AI-Aware", "enabled": "AI-Enabled", "fluent": "AI-Fluent", "native": "AI-Native"}


def load_lessons():
    lessons = {}
    for p in sorted(glob.glob(str(ROOT / "content" / "lessons" / "*.md"))):
        text = pathlib.Path(p).read_text(encoding="utf-8")
        _, fm, body = text.split("---", 2)
        meta = yaml.safe_load(fm)
        title = next((l[2:].strip() for l in body.splitlines() if l.startswith("# ")), meta["id"])
        sections = re.split(r"^## ", body, flags=re.M)[1:]
        parsed = []
        for s in sections:
            head, _, stext = s.partition("\n")
            parsed.append((head.strip(), stext.strip()))
        lessons[meta["id"]] = {"meta": meta, "title": title, "sections": parsed}
    return lessons


def first_para(text):
    for chunk in text.split("\n\n"):
        c = chunk.strip()
        if c and not c.startswith(("#", "|", "-", ">")):
            return c
    return text.strip().split("\n")[0]


def assignment_pair(lesson):
    """A = opening activity operationalized; B = the artifact assignment."""
    opener = next(((h, t) for h, t in lesson["sections"] if h.lower().startswith("start here")), None)
    assign = next(((h, t) for h, t in lesson["sections"] if h.lower().startswith("assignment")), None)

    if opener:
        a_title = re.sub(r"\s*\(\d+.*?\)\s*$", "", opener[0].replace("Start Here:", "").strip())
        a_body = (opener[1] + "\n\nDo this on real work, then post one sentence in the cohort thread: "
                  "what you picked and what surprised you. That sentence is your ticket into the next debrief.")
    else:
        h, t = lesson["sections"][0]
        a_title = f"Prep & apply: {h}"
        a_body = (f"Read the lesson through **{h}**, then apply its core idea to one real piece of your "
                  f"work in a 10-line note. Excerpt to anchor you:\n\n> {first_para(t)}\n\n"
                  "Post one sentence in the cohort thread: where it fit, or where it fought you.")

    deliverables = ""
    b_body = ""
    if assign:
        parts = assign[1].split("### Deliverables")
        b_body = parts[0].strip()
        if len(parts) > 1:
            deliverables = parts[1].strip()
    return (a_title, a_body), (b_body, deliverables)


def stretch_notes(lesson, roles_by_id, course_roles):
    lines = []
    for rid in lesson["meta"]["roleIds"]:
        if rid not in course_roles:
            continue
        role = roles_by_id[rid]
        outcome = role["businessOutcomes"][0]
        lines.append(f"- **{role['title']} stretch:** aim your artifact at this bar - *{outcome}*")
    return lines[:4]


def first_behavior_focus(pair):
    for L in pair:
        b = L["meta"].get("buildsBehaviors")
        if b:
            return re.sub(r"^Tier [0-9. ]*[^:]*:\s*", "", b[-1])
    return "shared habits, demonstrated on real work"


def build_accelerated(course, week_lessons, roles_by_id):
    """3 lessons/week as individual assignments + weekly 60-min debrief w/ group activity."""
    n = len(week_lessons)
    tier = course["tier"]
    next_tier = TIER_ORDER[min(TIER_ORDER.index(tier) + 1, 3)]
    behaviors = [b for L in week_lessons for b in L["meta"].get("buildsBehaviors", [])]
    chunks = [week_lessons[i:i + 3] for i in range(0, n, 3)]
    weeks = len(chunks)

    cal, weekly, debriefs = [], [], []
    for w, chunk in enumerate(chunks, 1):
        titles = " / ".join(L["title"] for L in chunk)
        assigns = " / ".join(L["meta"]["id"] for L in chunk)
        is_final = w == weeks
        cal.append(f"| **Week {w}** | {titles} | {assigns} (individual, ~45 min each) | "
                   f"{'SHOWCASE (60 min, guests)' if is_final else 'Debrief + group activity (60 min)'} |")

        blocks = []
        for L in chunk:
            (a_title, a_body), (b_body, deliv) = assignment_pair(L)
            m = L["meta"]
            stretch = stretch_notes(L, roles_by_id, set(course["roleIds"]))
            rubric_note = ""
            if m.get("rubric"):
                rubric_note = "\n**Graded against:** " + ", ".join(r["criterion"] for r in m["rubric"]) + "."
            blocks.append(f"""#### {m['id']} - {L['title']} (individual, ~45 min)

**Step 1 - {a_title} (~10 min).** {first_para(a_body)}

**Step 2 - the artifact (~35 min).**

{b_body}

**Deliverables**

{deliv if deliv else '- See lesson assignment.'}
{rubric_note}

{chr(10).join(stretch) if stretch else ''}
""")

        swap_lines = [f"- **{L['meta']['id']}:** hand your artifact to a partner; they must *use* it "
                      f"(not read it) and report where it broke." for L in chunk]
        focus = first_behavior_focus(chunk)
        if is_final:
            session = f"""### Week {w} session - SHOWCASE (60 min, guests invited)

**Focus:** {focus} - demonstrated to people who weren't in the room.

| Time | Segment | What happens |
|---|---|---|
| 0:00-0:05 | **Wins Wall** | 20 seconds each: proudest artifact of the program and who should reuse it. |
| 0:05-0:35 | **Showcase** | Volunteers present artifacts to invited guests (adjacent team, sponsor, next cohort). Guests ask; cohort answers. |
| 0:35-0:50 | **Reuse contracting** | Each guest names ONE artifact they'll actually take. Log it - that's the metric. |
| 0:50-0:60 | **What's next** | Route to the next bridge ({TIER_NAMES[next_tier]} track) via the placement diagnostic. |
"""
        else:
            session = f"""### Week {w} session - debrief + group activity (60 min)

**Focus:** {focus}

| Time | Segment | What happens |
|---|---|---|
| 0:00-0:05 | **Wins Wall** | 20 seconds each: one thing that clicked this week. No passing. |
| 0:05-0:30 | **Group activity: artifact swap** | Pairs exchange this week's artifacts and attempt to USE them cold. Reuse friction is the finding - capture it. |
| 0:30-0:50 | **Rubric critique** | 2 volunteers' artifacts reviewed against the lesson rubrics - rubric on screen, always. Recurring confusions go to docs/misconception-log.md. |
| 0:50-0:60 | **Next week** | Preview the next 3 lessons; re-anchor the ~3 hr/week timebox. |

**Artifact swap prompts**

{chr(10).join(swap_lines)}
"""
        weekly.append(f"## Week {w} - {titles}\n\n" + "\n".join(blocks))
        debriefs.append(session)

    kit = f"""# {course['title']} - Accelerated Cohort Kit

*Generated {datetime.date.today().isoformat()} by `app/generate_cohort_kit.py {course['id']} --profile accelerated`. Regenerate, don't hand-edit.*

**{TIER_NAMES[tier]} bridge - ACCELERATED** - {weeks} week{'s' if weeks > 1 else ''} - {n} individual assignments - {weeks} live sessions (final = public showcase)
**For:** {' / '.join(roles_by_id[r]['title'] for r in course['roleIds'])} - cohorts with **dedicated learning time (~3 hrs/week)**. If your cohort has ~1 hr/week, use the standard kit instead; compression without time is how programs die politely.

## Program Overview

**The goal.** {course['description']} Observable behaviors by the end (assessment = artifacts + behavior, never quizzes):

{chr(10).join('- ' + b for b in behaviors)}

**The weekly rhythm - 4 touchpoints:** three individual assignments (one lesson each: a short opening move on your real work, then the artifact) and one 60-minute live session combining a **group activity** (artifact swap - your work gets used by someone else, cold) with rubric critique.

**Norms to set at kickoff.**

- Time box: ~3 hours/week, protected on the calendar - accelerated means denser, not "on top of everything else."
- Artifacts before the session: the group activity needs your artifact to exist. No artifact = observer seat this week.
- Ask in the open: one pinned cohort thread per week. "Stuck" is not a secret.
- Real work only: synthetic examples are re-dos.

**What this kit will not cover (on purpose).** {TIER_NAMES[next_tier]}-tier material is deliberately out. Note the questions; don't derail. The menu on the placemat is not the order.

## At-a-Glance Calendar

| Week | Lessons | Individual assignments | Live session |
|---|---|---|---|
{chr(10).join(cal)}

*Hand-off note: assignments drop Monday; the live session lands Friday. The showcase needs guests booked by week 1 - invite them at kickoff.*

{chr(10).join(weekly)}

## Live Session Agendas

{chr(10).join(debriefs)}

---

*Sources of truth: lessons in `content/lessons/`, rubrics in lesson frontmatter, current-practice claims in `library/evolution/`. Misconception patterns feed `docs/misconception-log.md`.*
"""
    out = ROOT / "cohort-kits"
    out.mkdir(exist_ok=True)
    path = out / f"{course['id']}-accelerated-kit.md"
    path.write_text(kit, encoding="utf-8")
    print(f"OK: cohort-kits/{course['id']}-accelerated-kit.md - {weeks} weeks, {n} individual assignments + {weeks} live sessions")


def build_standard(course, week_lessons, roles_by_id):
    n = len(week_lessons)
    tier = course["tier"]
    next_tier = TIER_ORDER[min(TIER_ORDER.index(tier) + 1, 3)]
    behaviors = [b for L in week_lessons for b in L["meta"].get("buildsBehaviors", [])]
    checkin_after = (n // 2) + 1 if n >= 5 else None
    break_week = n >= 6

    cal, week_no, debrief_no = [], 0, 0
    debrief_map = {}
    for i, L in enumerate(week_lessons, 1):
        week_no += 1
        (a_title, _), _ = assignment_pair(L)
        cal.append(f"| **Week {week_no}** | {L['title']} | A: {a_title} | B: {L['title']} - the artifact |")
        if i == checkin_after:
            week_no += 1
            cal.append(f"| **Week {week_no}** | *Check-in week* | *No new assignments - catch up, finish artifacts, ask for help in the open* | |")
        if break_week and i == n - 1:
            week_no += 1
            cal.append(f"| **Week {week_no}** | *Break week* | *Scheduled, not apologized for* | |")
        if i % 2 == 0 and i != n:
            debrief_no += 1
            debrief_map[i] = debrief_no
            cal.append(f"| *-> Debrief {debrief_no}* | *30-min team meeting* | *Focus: {first_behavior_focus(week_lessons[i-2:i])}* | |")
    debrief_no += 1
    debrief_map[n] = debrief_no
    cal.append(f"| *-> Debrief {debrief_no} - SHOWCASE* | *45-min, guests invited* | *Artifacts presented to people outside the cohort* | |")

    weekly = []
    for i, L in enumerate(week_lessons, 1):
        (a_title, a_body), (b_body, deliv) = assignment_pair(L)
        m = L["meta"]
        stretch = stretch_notes(L, roles_by_id, set(course["roleIds"]))
        rubric_note = ""
        if m.get("rubric"):
            crits = ", ".join(r["criterion"] for r in m["rubric"])
            rubric_note = f"\n**Graded against** (see lesson rubric): {crits}."
        refs = ", ".join(m.get("libraryRefs", []))
        weekly.append(f"""### Week {i} - {L['title']}

**Lesson:** `{m['id']}` - {m['durationMin']} min - staircase rung {m.get('staircaseRung', '-')}{' - library: ' + refs if refs else ''}

**Assignment A (~25 min): {a_title}**

{a_body}

**Assignment B (~30 min): the artifact**

{b_body}

**Deliverables**

{deliv if deliv else '- See lesson assignment.'}
{rubric_note}

**Role-stretch notes** (optional - keep your strongest challenged)

{chr(10).join(stretch) if stretch else '- (roles inherit the unified assignment this week)'}
""")

    debriefs = []
    for after_i, dnum in sorted(debrief_map.items()):
        pair = week_lessons[max(0, after_i - 2):after_i]
        focus = first_behavior_focus(pair)
        is_final = after_i == n
        prompts = []
        for L in pair:
            for r in (L["meta"].get("rubric") or [])[:1]:
                prompts.append(f"- Against \"{r['criterion']}\" - who moved from *{r['emerging'].lower()}* toward *{r['strong'].lower()}*? Show us.")
        if not prompts:
            prompts = ["- Where did the tools fight you? (Some friction is tooling, not learning - name which.)",
                       "- Who ran a teammate's artifact this week? What broke?"]
        if is_final:
            debriefs.append(f"""### Debrief {dnum} - SHOWCASE (after Week {after_i}, 45 min, guests invited)

**Focus:** {focus} - demonstrated to people who weren't in the room.

| Time | Segment | What happens |
|---|---|---|
| 0:00-0:05 | **Wins Wall** | 20 seconds each: the artifact you're proudest of and who should reuse it. |
| 0:05-0:30 | **Showcase** | 3-4 volunteers present artifacts to invited guests (adjacent team, sponsor, next cohort). Guests ask the questions; cohort answers. |
| 0:30-0:40 | **Reuse contracting** | Each guest names ONE artifact they'll actually take. That's the metric. Log it. |
| 0:40-0:45 | **What's next** | Route to the next bridge ({TIER_NAMES[next_tier]} track) via the placement diagnostic. |

**The point:** a public artifact is the credential. Reuse promised out loud is reuse that happens.
""")
        else:
            debriefs.append(f"""### Debrief {dnum} (after Week {after_i}, 30 min)

**Focus:** {focus}

| Time | Segment | What happens |
|---|---|---|
| 0:00-0:05 | **Wins Wall** | Round-robin, 20 seconds each: one thing that clicked. No passing - if stuck, share what's still confusing. |
| 0:05-0:15 | **Live critique** | 1-2 volunteers show their artifact; cohort reviews against the lesson rubric - rubric on screen, always. |
| 0:15-0:25 | **Stuck points** | Facilitator lists 2-3 themes from the cohort thread. Group troubleshoots, teammate-to-teammate. Recurring confusions go to docs/misconception-log.md. |
| 0:25-0:30 | **Next two weeks** | Preview the coming assignments; re-anchor the ~1 hr/week timebox. |

**Facilitator prompts (pick 1-2)**

{chr(10).join(prompts)}
""")

    total_weeks = week_no
    kit = f"""# {course['title']} - Cohort Kit

*Generated {datetime.date.today().isoformat()} from `content/` by `app/generate_cohort_kit.py {course['id']}`. Regenerate, don't hand-edit.*

**{TIER_NAMES[tier]} bridge** - Weeks 1-{total_weeks} - {n * 2} assignments - {debrief_no} debriefs (final = public showcase)
**For:** {' / '.join(roles_by_id[r]['title'] for r in course['roleIds'])}

## Program Overview

**The goal.** {course['description']} By the end, these behaviors are observable in real work (this is also how completion is assessed - artifacts + behavior, never quizzes):

{chr(10).join('- ' + b for b in behaviors)}

**How it's structured.** Two assignments per week (~25-30 min each): **A** puts the lesson's opening move onto your real work; **B** produces the lesson's artifact. One 30-minute debrief every two weeks - the debrief is where critique happens, so artifacts must exist before it. Final session is a **showcase with guests**: artifacts presented to people outside the cohort, because reuse is the metric that can't be gamed.

**Norms to set at kickoff.**

- Time box: ~1 hour per week total. If an assignment runs long, stop - that's data for the debrief.
- Ask in the open: one pinned cohort thread per week. "Stuck" is not a secret.
- Done beats perfect: the goal is reps and artifacts, not polish.
- Real work only: synthetic examples are re-dos. Every artifact must point at your actual product.

**What this kit will not cover (on purpose).** {TIER_NAMES[next_tier]}-tier material - anything a rung above this course's lessons - is deliberately out. If someone asks, note the question for the coach and don't derail. The menu on the placemat is not the order.

## At-a-Glance Calendar

| Week | Theme | Assignment A (~25 min) | Assignment B (~30 min) |
|---|---|---|---|
{chr(10).join(cal)}

*Hand-off note: assignments drop Monday (A) and Thursday (B); debriefs land the Friday after each even content week. Adjust to your team's rhythm - but keep the showcase public.*

## Weekly Assignments

{chr(10).join(weekly)}

## Debrief Agendas

The structure is intentionally identical each time (Wins -> Critique -> Stuck points -> Next) so the cohort learns to run it without you. Consider rotating facilitation after the first two.

{chr(10).join(debriefs)}

---

*Sources of truth: lessons in `content/lessons/`, rubrics in lesson frontmatter, current-practice claims in `library/evolution/`. Misconception patterns from debriefs feed `docs/misconception-log.md`.*
"""

    out = ROOT / "cohort-kits"
    out.mkdir(exist_ok=True)
    path = out / f"{course['id']}-cohort-kit.md"
    path.write_text(kit, encoding="utf-8")
    print(f"OK: cohort-kits/{course['id']}-cohort-kit.md - {total_weeks} weeks, {n*2} assignments, {debrief_no} debriefs")


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("course_id")
    ap.add_argument("--profile", choices=["standard", "accelerated"], default="standard")
    ns = ap.parse_args()

    courses = json.load(open(ROOT / "content" / "courses.json"))
    roles = json.load(open(ROOT / "content" / "roles.json"))
    roles_by_id = {r["id"]: r for r in roles}
    course = next((c for c in courses if c["id"] == ns.course_id), None)
    if not course:
        sys.exit(f"no course '{ns.course_id}' - have: {[c['id'] for c in courses]}")

    lessons = load_lessons()
    week_lessons = [lessons[lid] for lid in course["lessonIds"]]
    if ns.profile == "accelerated":
        build_accelerated(course, week_lessons, roles_by_id)
    else:
        build_standard(course, week_lessons, roles_by_id)


if __name__ == "__main__":
    main()
