#!/usr/bin/env python3
"""Build the platform app from content/ — the app is a build target, content/ is the source of truth.

Usage:  python app/build.py          (from the project root, or anywhere)
Output: app/dist/index.html         (single self-contained file; open in any browser)

Requires: pyyaml, markdown, jsonschema  (pip install pyyaml markdown jsonschema)
No lesson text, catalog data, routing logic, or teaser copy lives in app code.
"""
import json, sys, glob, re, datetime, pathlib

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
    # Anchor the frontmatter to the very top of the file. Splitting on the literal
    # '---' misparses a file that has no frontmatter but a '---' horizontal rule in
    # its body (three parts, wrong ones); the anchored match rejects that instead.
    m = re.match(r"^\ufeff?---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n(.*)$", text, re.S)
    if not m:
        raise ValueError(f"{path}: no YAML frontmatter (expected a '---' fenced block at the very top)")
    fm, body = m.group(1), m.group(2)
    meta = yaml.safe_load(fm) or {}
    if not isinstance(meta, dict):
        raise ValueError(f"{path}: frontmatter did not parse as a key/value mapping")
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


def load_json(path):
    """Read a required JSON file, failing with a clear message instead of a traceback."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        sys.exit(f"BUILD FAILED — missing required file: {path}")
    except json.JSONDecodeError as e:
        sys.exit(f"BUILD FAILED — invalid JSON in {path}: {e}")


def main():
    # --- fail fast with the full list of missing inputs, not a one-at-a-time traceback ---
    required_inputs = [
        CONTENT / "schemas" / "lesson.schema.json",
        CONTENT / "schemas" / "diagnostic.schema.json",
        CONTENT / "roles.json", CONTENT / "courses.json",
        CONTENT / "diagnostic.json", CONTENT / "teasers.json",
    ]
    missing_inputs = [str(p) for p in required_inputs if not p.exists()]
    if missing_inputs:
        sys.exit("BUILD FAILED — missing required content files:\n"
                 + "\n".join(f" - {mi}" for mi in missing_inputs))

    # --- validate content before building (broken content should fail the build, not ship) ---
    lesson_schema = load_json(CONTENT / "schemas" / "lesson.schema.json")
    diag_schema = load_json(CONTENT / "schemas" / "diagnostic.schema.json")

    lessons, errors = {}, []
    for p in sorted(glob.glob(str(CONTENT / "lessons" / "*.md"))):
        try:
            meta, html = parse_md(p)
        except Exception as e:
            errors.append(str(e))
            continue
        missing_req = [r for r in lesson_schema.get("required", []) if r not in meta]
        if missing_req:
            errors.append(f"{p}: missing required frontmatter field(s): {', '.join(missing_req)}")
        if "id" not in meta:
            continue  # id keys the lesson map — cannot proceed without it
        for key, val in meta.items():
            sub = lesson_schema["properties"].get(key)
            if sub is None:
                errors.append(f"{p}: unknown frontmatter field {key}")
                continue
            try:
                validate(val, sub)
            except Exception as e:
                errors.append(f"{p}: {key}: {e}")
        if meta["id"] in lessons:
            errors.append(f"{p}: duplicate lesson id '{meta['id']}'")
            continue
        lessons[meta["id"]] = {"meta": meta, "html": html}

    library = {}
    for p in sorted(glob.glob(str(ROOT / "library" / "evolution" / "*.md"))):
        try:
            meta, html = parse_md(p)
        except Exception as e:
            errors.append(str(e))
            continue
        if "id" not in meta:
            errors.append(f"{p}: missing required frontmatter field 'id'")
            continue
        library[meta["id"]] = {"meta": meta, "html": html}

    roles = load_json(CONTENT / "roles.json")
    courses = load_json(CONTENT / "courses.json")
    diagnostic = load_json(CONTENT / "diagnostic.json")
    teasers = load_json(CONTENT / "teasers.json")
    validate(diagnostic, diag_schema)

    # referential integrity (tolerate malformed rows — report, don't crash)
    for c in courses:
        for lid in c.get("lessonIds", []):
            if lid not in lessons:
                errors.append(f"courses.json: {c.get('id', '(no id)')} references missing lesson {lid}")
    course_ids = {c.get("id") for c in courses}
    for tier, routes in diagnostic.get("routing", {}).get("tiers", {}).items():
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
          f"{len(library)} library entries, {len(teasers.get('teasers', []))} teasers")


if __name__ == "__main__":
    main()
