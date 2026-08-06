#!/usr/bin/env python3
"""Generate docs/lesson-index.md from content/ — a human-readable index of every
lesson (id, title, rung, minutes, a payoff-first one-liner) plus the Evolution
Library. Run after adding or renaming lessons:  python app/build_index.py
The one-liner prefers a "you'll leave with…" payoff sentence from the lesson's
opening blockquote, falling back to its last sentence.
"""
import json, glob, re, sys, datetime, pathlib

try:
    import yaml
except ImportError:
    sys.exit("Missing dependency: pyyaml. Run: pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent


def parse(path):
    t = pathlib.Path(path).read_text(encoding="utf-8")
    # Same anchored frontmatter match as build.py, then parse it as real YAML so
    # lists, quoted colons and multi-line values are read correctly — and a '---'
    # horizontal rule in the body no longer mis-splits the file.
    fmatch = re.match(r"^\ufeff?---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n(.*)$", t, re.S)
    if not fmatch:
        raise ValueError(f"{path}: no YAML frontmatter (expected a '---' fenced block at the very top)")
    fm, body = fmatch.group(1), fmatch.group(2)
    meta = yaml.safe_load(fm) or {}
    if not isinstance(meta, dict):
        raise ValueError(f"{path}: frontmatter did not parse as a key/value mapping")
    lines = body.splitlines()
    title = next((l[2:].strip() for l in lines if l.startswith("# ")), None)
    bq, started = [], False
    for l in lines:
        s = l.strip()
        if s.startswith(">"):
            bq.append(s.lstrip(">").strip()); started = True
        elif started and s == "":
            continue
        elif started:
            break
    text = " ".join(bq).strip() or next(
        (l.strip() for l in lines if l.strip() and not l.startswith(("#", "---"))), "")
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    desc = next((s for s in sents if re.search(
        r"\b(you'?ll leave|by the end|walk away|leave with|you'?ll have|you'?ll build|you'?ll write)\b",
        s, re.I)), "")
    if not desc and sents:
        desc = sents[-1] if len(sents) > 1 else sents[0]
    desc = re.sub(r"\s+", " ", desc)
    if len(desc) > 170:
        desc = desc[:167].rstrip() + "…"
    return meta, title, desc


def main():
    lessons = {}
    for p in glob.glob(str(ROOT / "content" / "lessons" / "*.md")):
        m, title, d = parse(p)
        lessons[m.get("id", "?")] = {"title": title, "d": d,
                                     "rung": m.get("staircaseRung", "?"), "min": m.get("durationMin", "?")}
    courses = json.load(open(ROOT / "content" / "courses.json"))
    lib = []
    for p in sorted(glob.glob(str(ROOT / "library" / "evolution" / "*.md"))):
        m, _, _ = parse(p)
        ref = m.get("referenced_by", "")
        if isinstance(ref, list):  # YAML may parse this as a list; render it for the table cell
            ref = ", ".join(str(x) for x in ref)
        lib.append((m.get("id", "?"), m.get("practice", "?"), m.get("status", "?"), ref))

    tier = {"aware": "Level 1 · AI-Aware", "enabled": "Level 2 · AI-Enabled",
            "fluent": "Level 3 · AI-Fluent", "native": "Level 4 · AI-Native"}
    o = ["# Lesson & Content Index", "",
         f"> Generated from `content/` on {datetime.date.today().isoformat()} by `app/build_index.py` "
         f"(rerun after adding lessons). {len(lessons)} lessons · {len(courses)} courses · "
         f"{len(lib)} Evolution Library entries. Rung: 1 plain · 2 patterned · 3 structured.",
         "", "## Courses"]
    seen = set()
    for c in courses:
        o += ["", f"### {c['title']}  ·  {tier.get(c['tier'], c['tier'])}", "",
              c.get("description", "").strip(),
              f"*Roles: {', '.join(c.get('roleIds', []))} · {c.get('totalCredits', '?')} credits*", "",
              "| Lesson | Rung | Min | What you leave with |", "|---|---|---|---|"]
        for lid in c["lessonIds"]:
            seen.add(lid); L = lessons.get(lid, {})
            o.append(f"| **{lid}** — {L.get('title', '(missing)')} | {L.get('rung', '?')} | "
                     f"{L.get('min', '?')} | {L.get('d', '')} |")
    orphans = sorted(i for i in lessons if i not in seen)
    if orphans:
        o += ["", "### Uncatalogued lessons (not in any course)"]
        o += [f"- **{i}** — {lessons[i]['title']} (rung {lessons[i]['rung']}): {lessons[i]['d']}" for i in orphans]
    o += ["", "## Evolution Library", "",
          "Versioned 'current best practice' entries that lessons cite (via `libraryRefs`) instead of "
          "embedding claims that age.", "", "| Entry | Practice | Status | Cited by |", "|---|---|---|---|"]
    for eid, prac, st, ref in lib:
        o.append(f"| `{eid}` | {prac} | {st} | {ref} |")
    (ROOT / "docs" / "lesson-index.md").write_text("\n".join(o) + "\n", encoding="utf-8")
    print(f"OK: docs/lesson-index.md — {len(lessons)} lessons, {len(courses)} courses, "
          f"{len(lib)} entries. orphans: {orphans or 'none'}")


if __name__ == "__main__":
    main()
