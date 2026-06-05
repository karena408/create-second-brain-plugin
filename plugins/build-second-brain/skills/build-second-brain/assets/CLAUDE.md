# Second Brain

This folder is Claude's workspace for acting as your executive assistant / second brain. Read this file first in every session, before any other action.

## What's here

The wiki lives at the **repo root** — the knowledge-base pages are top-level files and folders, not nested under a `wiki/` subfolder.

```
second-brain/
├── CLAUDE.md             ← this file (operating instructions — the wiki's schema/config)
├── HOME.md               ← human-facing dashboard (auto-maintained marker regions)
├── index.md              ← catalog of every page, by category
├── hotcache.md           ← sliding window of the 5–8 most recently touched pages
├── log.md                ← chronological op log
├── .claude/              ← Claude Code config (agents/, commands/, scripts/, skills/)
├── daily-intake/         ← raw daily-intake drop zone (processed by the intake agent)
├── daily-intake-archive/ ← processed intake files, kept for reference
├── digest/               ← daily intake digests + end-of-day recaps (created on first write)
├── projects/             ← active initiatives (one page each; see Template.md)
├── people/               ← person & org pages, CRM-shaped (see Template.md)
├── knowledge/            ← Courses/, Reading/, Research/ notes
├── events/               ← per-event notes (see Template.md)
└── ideas/                ← automation & product ideas backlog
```

The root dashboard files are the **fast cache** for understanding context: `HOME.md` (what's in motion), `index.md` (what pages exist), and `hotcache.md` (what changed most recently). The topic subfolders (`projects/`, `people/`, `knowledge/`, `events/`, `ideas/`) are the **deep store** — drill in for the full state of any project, person, concept, event, or idea. When the fast cache and a full page disagree, the full page wins; reconcile by updating the cache.

## Operating mode

These four rules govern the working relationship. They override generic-assistant defaults.


## Reading order at session start
1. This file (`CLAUDE.md`).
2. `HOME.md` — what's actually in motion.
3. The latest file in `daily-intake/` — what's new since last session.
4. The `Template.md` in the relevant subfolder — the page schema, if you'll be writing to the vault.
5. Drill into `projects/`, `people/`, `knowledge/`, etc. as needed for the question at hand.

## Searching the wiki (use `index.md`)
`index.md` is the catalog — your map for finding pages instead of grepping blindly. To answer any question, retrieve in this order and stop as soon as you have enough:

1. `hotcache.md` — recently touched pages; the answer is often already here.
2. `index.md` — scan the category sections and one-line summaries to pick candidate pages, then open them.
3. The relevant subfolder (`projects/`, `people/`, `knowledge/`, …) if the index points there but the entry is too thin.
4. Grep the wiki for specific phrasing — try exact phrasing first, never invent an answer. Cap at ~8 pages.

If nothing turns up, say plainly the wiki doesn't have it (or ask one crisp question) — don't guess. Keep the catalog current: add a `- [[Page-Name]] — one-line summary.` entry on every page creation, and fix the summary whenever a page's purpose changes.

## Keep the hot cache current (every interaction)
After any write — or substantial read — of a wiki page, update `hotcache.md`:
- **Prepend** the touched page(s): `- [[Page-Name]] — short reason (op + date).`
- Keep only the **5–8 most recent**; trim from the bottom. Body stays ≤500 chars.
- It's a sliding window, not a log — don't accumulate history here (chronology lives in `log.md`).

## What NOT to do
- **Don't put secrets in any file.** API keys, tokens, passwords, personal account info → environment variables or a secret store. Reference by name, not value.
- **Don't paraphrase the user's raw thoughts.** When they dump a "random thoughts" list, file it verbatim. Style edits destroy signal.
- **Don't surface stale items as if they're current.** Anything aging without progress should be flagged, not quietly carried.
- **Don't rebuild summaries from scratch each session.** The wiki is the persistent artifact — read what's already synthesized, then add to it.

## Escalation
If something is unclear, ambiguous, or the right action depends on a value judgment only the user can make (priorities, partnerships, public positioning, sensitive relationships), **ask one crisp question rather than guessing**. They prefer a quick clarifying question over a confidently wrong action.

## When this file is wrong
This file is the source of truth for how the assistant operates. When the operating mode evolves, update it here first. Log the change in `log.md` with a `decision` op.
