#!/usr/bin/env python3
"""make_preview.py — one command to build the app and package an emailable preview.

    python app/make_preview.py

Rebuilds app/dist/index.html (via build.py — fails loudly if content is broken),
then writes an email-safe zip (index.html + a tester READ-ME) to app/dist/.
Raw .html attachments get stripped by many mail servers; a zip sails through.
"""
import subprocess, sys, glob, json, zipfile, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = ROOT / "app"
DIST = APP / "dist"


def main():
    # 1. Build — a broken build must NOT ship a stale preview.
    if subprocess.run([sys.executable, str(APP / "build.py")], cwd=ROOT).returncode != 0:
        sys.exit("make_preview: build failed — refusing to package a stale preview.")

    index = DIST / "index.html"
    if not index.exists():
        sys.exit("make_preview: app/dist/index.html missing after build.")

    lessons = len(glob.glob(str(ROOT / "content" / "lessons" / "*.md")))
    with open(ROOT / "content" / "courses.json", encoding="utf-8") as f:
        courses = len(json.load(f))
    today = datetime.date.today().isoformat()

    readme = f"""AI Maturity Learning Platform — Preview build ({today})

HOW TO OPEN
  1. Unzip this folder.
  2. Double-click  index.html  — it opens in your web browser. That's the whole app, one file.

GOOD TO KNOW
  - It runs entirely on your computer. Nothing you type or click is uploaded anywhere.
  - It will not save progress between sessions (this is a preview).
  - Best first path: click "Place me" (the quick diagnostic) to get routed, or jump to
    Level 1 and start with "The First Win: Get 20 Minutes Back."

WHAT I'D LOVE FEEDBACK ON
  - Did a "first win" actually land in the first lesson?
  - Anywhere the wording felt like it assumed you already knew something?
  - Did you ever feel "behind"? (there is a lesson about exactly that — did it help?)

This build: {lessons} lessons, {courses} courses.
"""

    zip_path = DIST / f"ai-maturity-learning-platform-preview-{today}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(index, "index.html")
        z.writestr("READ-ME-FIRST.txt", readme)

    kb = zip_path.stat().st_size // 1024
    print(f"OK: {zip_path}")
    print(f"    {kb} KB - {lessons} lessons / {courses} courses. Attach this zip to your test email.")


if __name__ == "__main__":
    main()
