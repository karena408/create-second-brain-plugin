# Daily Brew — scheduled morning task

Run these steps **in order, one at a time**. Finish each before starting the next, and print a short progress line after each (e.g. `3/8 done — intake notes read`).

Read `CLAUDE.md` first for the wiki conventions. Paths are flat at the repo root (`index.md`, `hotcache.md`, `people/`, `projects/`, `daily-intake/`, `daily-intake-archive/`, etc.).

1. **Read my calendar** — events from today through the next 3 days.
2. **Read my email** — new/unread mail from the last 24h. Read only; don't reply or draft.
3. **Read my daily-intake notes** — everything currently in `daily-intake/`.
4. **Update the knowledge base** — fold the intake notes, calendar, and email into the right `people/` and `projects/` pages (create pages as needed). Use my exact words; don't paraphrase.
5. **Update `index.md` and `hotcache.md`** to reflect the pages you just changed.
6. **Summarize what changed** — a short "since yesterday" list of new/updated pages, new people, and new follow-ups.
7. **Send me the Daily Brew on Slack** (`python3 .claude/scripts/post_to_slack.py <file> dm --only-marked`) with: today's schedule, emails worth a look, things to keep top of mind, and follow-ups.
8. **Archive and reset** — move the processed note from `daily-intake/` into `daily-intake-archive/`, then create today's new `daily-intake/<YYYY-MM-DD>.md` seeded with top-of-mind, to-dos, and follow-ups.

When done, append a one-line entry to `log.md` and reply with a short summary of what you did.

## Never
- Never paraphrase my raw words when routing into pages, or edit anything I wrote.
- Never send or draft email; never Slack anyone but my own DM; never post to a channel.
- Never delete an intake note — archive it. Never archive before Step 4 is done cleanly.
- Never overwrite a `daily-intake/<today>.md` I already started — prepend instead.
- Never grow `hotcache.md` past 8 entries. Never auto-promote a loose idea to a project — flag it.
- Never invent facts. If a name, event, or note is ambiguous, flag it instead of guessing.
- Never write a webhook URL anywhere but `.claude/scripts/slack-channels.json`.
