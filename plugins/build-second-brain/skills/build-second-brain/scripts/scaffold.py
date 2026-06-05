#!/usr/bin/env python3
"""Scaffold the flat "second brain" LLM-wiki structure into a target folder.

Creates the exact directory tree and copies the canonical skeleton files
(CLAUDE.md, HOME.md, index.md, hotcache.md, log.md, wiki-fixes.md, the three
Template.md files, and the helper-prompts) from this skill's assets/ directory.

Design goals:
- Idempotent and SAFE: never overwrites a file that already exists. Re-running
  on a partially-built brain only fills in what's missing, so it can't clobber a
  wiki you've started populating. Skipped files are reported.
- Byte-identical skeleton: the files are copied verbatim from assets/, so the
  produced CLAUDE.md (and everything else) matches the canonical source exactly.

Usage:
    python3 scaffold.py [TARGET_DIR]

TARGET_DIR defaults to the current working directory (meant to be the `brain/`
folder that already contains your `raw-notes/`). raw-notes/ is never touched.
"""

import os
import shutil
import sys

# Folders that should exist and stay in git even while empty -> get a .gitkeep.
GITKEEP_DIRS = [
    "daily-intake",
    "daily-intake-archive",
    "raw-files",
    "ideas",
    "knowledge/Courses",
    "knowledge/Reading",
    "knowledge/Research",
    ".claude/skills",
]

# Folders that will hold their Template.md (no .gitkeep needed).
TEMPLATE_DIRS = ["projects", "people", "events"]

# Every file copied verbatim from assets/ -> its destination path under TARGET.
# (relative path is identical in assets/ and in the destination)
ASSET_FILES = [
    "CLAUDE.md",
    "HOME.md",
    "index.md",
    "hotcache.md",
    "log.md",
    "wiki-fixes.md",
    "helper-prompts/andrej-llm-wiki.md",
    "helper-prompts/daily-brew.md",
    "helper-prompts/granola-intake.md",
    "projects/Template.md",
    "people/Template.md",
    "events/Template.md",
]


def main():
    target = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.getcwd())
    assets = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
    assets = os.path.abspath(assets)

    if not os.path.isdir(assets):
        sys.exit(f"ERROR: assets directory not found at {assets}")

    os.makedirs(target, exist_ok=True)

    created, skipped = [], []

    # 1. Directory tree + .gitkeep placeholders.
    for d in GITKEEP_DIRS:
        os.makedirs(os.path.join(target, d), exist_ok=True)
        keep = os.path.join(target, d, ".gitkeep")
        if not os.path.exists(keep):
            open(keep, "w").close()
            created.append(os.path.join(d, ".gitkeep"))
    for d in TEMPLATE_DIRS:
        os.makedirs(os.path.join(target, d), exist_ok=True)
    os.makedirs(os.path.join(target, "helper-prompts"), exist_ok=True)

    # 2. Copy skeleton files verbatim (never overwrite).
    for rel in ASSET_FILES:
        src = os.path.join(assets, rel)
        dst = os.path.join(target, rel)
        if not os.path.exists(src):
            sys.exit(f"ERROR: missing asset {src}")
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if os.path.exists(dst):
            skipped.append(rel)
            continue
        shutil.copy2(src, dst)
        created.append(rel)

    # 3. Note whether raw-notes/ is present (the input the wiki is built from).
    raw_notes = os.path.join(target, "raw-notes")
    has_raw = os.path.isdir(raw_notes)

    print(f"Scaffolded second-brain structure into: {target}\n")
    print(f"Created ({len(created)}):")
    for c in sorted(created):
        print(f"  + {c}")
    if skipped:
        print(f"\nSkipped — already existed, left untouched ({len(skipped)}):")
        for s in sorted(skipped):
            print(f"  = {s}")
    print()
    if has_raw:
        n = sum(len(f) for _, _, f in os.walk(raw_notes))
        print(f"raw-notes/ found ({n} file(s)) — ready to restructure into pages.")
    else:
        print("NOTE: no raw-notes/ folder found. Create one with your source notes, "
              "or point the restructuring step at wherever the raw notes live.")


if __name__ == "__main__":
    main()
