# Second Brain marketplace

A Claude Code / Claude **plugin** that turns a folder of raw notes into a
structured, interlinked **second brain** — the LLM-maintained wiki pattern.

This repo is both the **plugin** and a one-plugin **marketplace**, so it can be
installed directly from GitHub.

## What you get: the `build-second-brain` plugin

When you invoke it inside a folder (e.g. `brain/`) that contains a `raw-notes/`
subfolder, it:

1. **Scaffolds** the canonical second-brain structure (`CLAUDE.md`, `HOME.md`,
   `index.md`, `hotcache.md`, `log.md`, and `projects/` /
   `people/` / `events/` templates) — byte-identical to the source schema, via a
   deterministic, idempotent script that never overwrites existing files.
2. **Restructures** your raw notes into pages — a project page per project, a
   person page per significantly-mentioned person, plus event / knowledge / idea
   pages — following the templates and frontmatter conventions.
3. **Wires up** the catalog (`index.md`), hot cache, dashboard (`HOME.md`), and
   op log so the wiki is self-consistent from day one.

Everything it needs is bundled inside the plugin — you start from an empty repo
with only a `raw-notes/` folder.

## Install

### In Claude (Cowork / desktop)

1. Open the **Cowork** tab → submenu → **Add plugin**.
2. Add this marketplace by its GitHub repo (`karena408/create-second-brain-plugin`).
3. Find **build-second-brain** in the plugin browser and install it.

### In Claude Code (CLI)

```bash
# 1. Add this repo as a marketplace (GitHub owner/repo shorthand)
/plugin marketplace add karena408/create-second-brain-plugin

# 2. Install the plugin
/plugin install build-second-brain@second-brain-marketplace
```

## Use

```text
cd path/to/brain          # a folder containing only a raw-notes/ subfolder
# then, in Claude:
"Build my second brain from these notes."
```

The skill triggers automatically on phrases like *"set up a second brain"*,
*"build an LLM wiki"*, or *"organize my notes into a wiki"*.

## Repo layout

```
build-second-brain-plugin/
├── .claude-plugin/
│   └── marketplace.json              ← marketplace manifest (lists the plugin)
└── plugins/
    └── build-second-brain/
        ├── .claude-plugin/
        │   └── plugin.json           ← plugin manifest
        ├── skills/
        │   └── build-second-brain/
        │       ├── SKILL.md          ← the skill (with the LLM-Wiki prompt inline)
        │       ├── scripts/
        │       │   └── scaffold.py   ← deterministic structure scaffolder
        │       └── assets/           ← canonical files copied into the brain repo
        └── README.md
```

## License

MIT — see [LICENSE](./LICENSE).
