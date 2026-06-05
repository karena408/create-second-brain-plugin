# build-second-brain (plugin)

Scaffold a personal **second brain** LLM-wiki from a folder of raw notes, then
restructure those notes into an interlinked markdown knowledge base.

See the [marketplace README](../../README.md) for install and usage. The skill
itself lives at [`skills/build-second-brain/SKILL.md`](./skills/build-second-brain/SKILL.md);
its workflow, conventions, and the LLM-Wiki pattern (reproduced verbatim) are all
documented there.

## What it does

1. **Scaffold** — runs `skills/build-second-brain/scripts/scaffold.py`, which
   creates the canonical folder tree and copies the bundled skeleton files
   (`CLAUDE.md`, `HOME.md`, `index.md`, `hotcache.md`, `log.md`, and the three
   `Template.md` files) into the target `brain/` folder.
   Idempotent and safe — it never overwrites a file that already exists, and
   never touches `raw-notes/`.
2. **Restructure** — reads every file in `raw-notes/` and files it into
   `projects/`, `people/`, `events/`, `knowledge/`, and `ideas/` pages,
   cross-linked and frontmattered per the schema.
3. **Wire up** — updates `index.md`, `hotcache.md`, `HOME.md`, and `log.md`.

## Self-contained

Everything is bundled under `skills/build-second-brain/assets/`. A user can start
from an empty repo containing only a `raw-notes/` subfolder.
