#!/usr/bin/env python3
"""Build the platform app from content/ — the app is a build target, content/ is the source of truth.

Usage:  python app/build.py          (from the project root, or anywhere)
Output: app/dist/index.html         (single self-contained file; open in any browser)

Requires: pyyaml, markdown, jsonschema  (pip install pyyaml markdown jsonschema)
No lesson text, catalog data, routing logic, or teaser copy lives in app code.
"""
import json, sys, glob, datetime, pathlib

try:
    import yaml, markdown
    from jsonschema import validate
except ImportError as e:
    sys.exit(f"Missing dependency: {e.name}. Run: pip install pyyaml markdown jsonschema")

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT, APP = ROOT / "content", ROOT / "app"
MD = markdown.Markdown(extensions=["tables"])


def parse_md(path):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    _, fm, body = text.split("---", 2)
    meta = yaml.safe_load(fm)
    for k, v in meta.items():
        if isinstance(v, datetime.date):
            meta[k] = v.isoformat()
    # title lives in the body's first H1, not frontmatter
    for line in body.splitlines():
        if line.startswith("# "):
            meta.setdefault("title", line[2:].strip())
            break
    MD.reset()
    return meta, MD.convert(body)


def main():
    # --- validate content before building (broken content should fail the build, not ship) ---
    required_inputs = [
        CONTENT / "schemas" / "lesson.schema.json",
        CONTENT / "schemas" / "diagnostic.schema.json",
        CONTENT / "roles.json",
        CONTENT / "courses.json",
        CONTENT / "diagnostic.json",
        CONTENT / "teasers.json",
        ROOT / "library" / "evolution",
    ]
    missing_inputs = [p for p in required_inputs if not p.exists()]
    if missing_inputs:
        print("BUILD FAILED — missing required content inputs:")
        for p in missing_inputs:
            print(" -", p.relative_to(ROOT))
        sys.exit(1)

    lesson_schema = json.load(open(CONTENT / "schemas" / "lesson.schema.json"))
    diag_schema = json.load(open(CONTENT / "schemas" / "diagnostic.schema.json"))

    lessons, errors = {}, []
    for p in sorted(glob.glob(str(CONTENT / "lessons" / "*.md"))):
        meta, html = parse_md(p)
        for key, val in meta.items():
            sub = lesson_schema["properties"].get(key)
            if sub is None:
                errors.append(f"{p}: unknown frontmatter field {key}")
                continue
            try:
                validate(val, sub)
            except Exception as e:
                errors.append(f"{p}: {key}: {e}")
        lessons[meta["id"]] = {"meta": meta, "html": html}

    library = {}
    for p in sorted(glob.glob(str(ROOT / "library" / "evolution" / "*.md"))):
        meta, html = parse_md(p)
        library[meta["id"]] = {"meta": meta, "html": html}

    roles = json.load(open(CONTENT / "roles.json"))
    courses = json.load(open(CONTENT / "courses.json"))
    diagnostic = json.load(open(CONTENT / "diagnostic.json"))
    teasers = json.load(open(CONTENT / "teasers.json"))
    validate(diagnostic, diag_schema)

    # referential integrity
    for c in courses:
        for lid in c["lessonIds"]:
            if lid not in lessons:
                errors.append(f"courses.json: {c['id']} references missing lesson {lid}")
    course_ids = {c["id"] for c in courses}
    for tier, routes in diagnostic["routing"]["tiers"].items():
        for role, cid in routes.items():
            if cid not in course_ids:
                errors.append(f"diagnostic.json: tier {tier}/{role} routes to missing course {cid}")

    if errors:
        print("BUILD FAILED — content errors:")
        for e in errors:
            print(" -", e)
        sys.exit(1)

    data = {"roles": roles, "courses": courses, "lessons": lessons,
            "library": library, "diagnostic": diagnostic, "teasers": teasers}

    template = (APP / "template.html").read_text(encoding="utf-8")

    # --- validate the template too (added 2026-07-17) ---
    # We used to validate content and then string-replace into whatever template.html happened to
    # contain. A truncated template therefore produced a silently broken app while this script
    # printed "OK". It has now happened once; it does not get to happen twice.
    tmpl_errors = []
    for placeholder in ("{{DATA_JSON}}", "{{BUILD_DATE}}"):
        if placeholder not in template:
            tmpl_errors.append(f"template.html: missing {placeholder}")
    for closer in ("</script>", "</body>", "</html>"):
        if closer not in template:
            tmpl_errors.append(f"template.html: missing {closer} — file looks truncated")
    if not template.rstrip().endswith("</html>"):
        tmpl_errors.append("template.html: does not end with </html> — file looks truncated")
    if tmpl_errors:
        print("BUILD FAILED — template errors:")
        for e in tmpl_errors:
            print(" -", e)
        sys.exit(1)

    out = (template
           .replace("{{DATA_JSON}}", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
           .replace("{{BUILD_DATE}}", datetime.date.today().isoformat()))

    # the output must close too — cheap insurance against a partial write
    if not out.rstrip().endswith("</html>"):
        sys.exit("BUILD FAILED — generated output is truncated; refusing to write app/dist/index.html")

    dist = APP / "dist"
    dist.mkdir(exist_ok=True)
    (dist / "index.html").write_text(out, encoding="utf-8")
    print(f"OK: app/dist/index.html — {len(lessons)} lessons, {len(courses)} courses, "
          f"{len(library)} library entries, {len(teasers['teasers'])} teasers")


if __name__ == "__main__":
    main()
