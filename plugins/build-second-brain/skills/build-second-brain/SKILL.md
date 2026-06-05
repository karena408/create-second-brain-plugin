---
name: build-second-brain
description: >-
  Scaffold a personal "second brain" LLM-wiki from a folder of raw notes, then
  restructure those notes into an interlinked markdown knowledge base (a project
  page per project, a person page per significant person, plus events / knowledge
  / ideas). Use this whenever the user wants to turn a pile of raw notes,
  braindumps, meeting notes, or a `raw-notes/` folder into an organized second
  brain / personal wiki / knowledge base / Obsidian vault — or asks to "set up a
  second brain", "build an LLM wiki", "scaffold the brain structure", or
  "organize my notes into a wiki". Triggers even when they describe the outcome
  (an executive-assistant knowledge base, a CRM-shaped people store, a structured
  vault) without naming the structure. Produces a CLAUDE.md/HOME.md/index.md
  skeleton identical to the canonical schema, so do not hand-roll the layout —
  use this skill.
---

# Build a Second Brain (LLM Wiki)

This skill turns a folder of raw notes into a structured, interlinked **second
brain** — the LLM-maintained wiki pattern. It does two things:

1. **Scaffold** the exact canonical folder structure with a deterministic script
   (so `CLAUDE.md` and the rest of the skeleton are byte-identical to the source
   schema — no drift, no hand-rolling).
2. **Restructure** the user's raw notes into the wiki: a project page per
   project, a person page per significantly-mentioned person, and event /
   knowledge / idea pages as the material warrants — following the page
   templates and conventions, then wiring up the index, hot cache, and log.

## The mental model (read this first)

The pattern is Andrej Karpathy's *LLM Wiki*: instead of re-deriving knowledge
from raw documents on every query (RAG), the LLM **incrementally builds and
maintains a persistent, interlinked wiki** that sits between the user and their
raw sources. The wiki is a compounding artifact — cross-references already
exist, contradictions are already flagged, summaries stay current. The user
curates and asks; the LLM does all the reading, filing, and bookkeeping.

The full pattern is reproduced **verbatim at the end of this skill** — see
[Appendix: The LLM Wiki pattern](#appendix-the-llm-wiki-pattern-verbatim).
**Read it before restructuring** to absorb the *why* (the three layers: raw
sources → wiki → schema; the ingest / query / lint operations; why a compounding
wiki beats re-deriving from raw docs each time). It's reproduced inline so you
never have to depend on a file being present. The appendix is intentionally
abstract — it describes the idea, not a specific layout.

The **concrete conventions** for this particular instantiation live in the files
the scaffold script drops in, and those are authoritative:

- `CLAUDE.md` — the operating schema: the flat layout, frontmatter rules, naming,
  retrieval order, the hot-cache/index/log discipline, and the do's & don'ts.
- The three `Template.md` files (`projects/`, `people/`, `events/`) — the exact
  section structure and frontmatter each page type must follow.

## Workflow

Work through these in order. Track them as todos so none gets dropped.

### 1. Scaffold the structure

Confirm where the brain lives. By default it's the current working directory (a
`brain/` folder that already contains `raw-notes/`). If the user named a
different folder, use that. Then run:

```bash
python3 <skill-dir>/scripts/scaffold.py [TARGET_DIR]
```

`<skill-dir>` is this skill's directory; `TARGET_DIR` defaults to the cwd. The
script is **idempotent and never overwrites** an existing file — safe to re-run
on a partially-built brain. It creates this flat tree and copies the canonical
skeleton files in verbatim:

```
brain/
├── CLAUDE.md              ← operating instructions + wiki schema (identical to source)
├── HOME.md                ← human-facing dashboard (auto-maintained marker regions)
├── index.md               ← catalog of every page, by category
├── hotcache.md            ← sliding window of the 5–8 most recently touched pages
├── log.md                 ← chronological op log
├── wiki-fixes.md          ← lint/fix notes (starts empty)
├── daily-intake/          ← raw drop zone for new intake (.gitkeep)
├── daily-intake-archive/  ← processed intake (.gitkeep)
├── projects/Template.md   ← active initiatives
├── people/Template.md     ← person/org CRM pages
├── events/Template.md     ← per-event notes
├── knowledge/             ← Courses/ · Reading/ · Research/ (.gitkeep placeholders)
├── ideas/                 ← automation/product backlog (.gitkeep)
└── .claude/               ← Claude Code config
```

`raw-notes/` is the **input** and is never touched by the script. If the script
reports no `raw-notes/`, ask the user where their raw notes are before going on.

### 2. Absorb the schema

Read, in this order, so you restructure to the right conventions:

1. The **LLM Wiki pattern** — reproduced verbatim in the
   [appendix](#appendix-the-llm-wiki-pattern-verbatim) below (the *why*:
   persistent compounding wiki, the three layers, ingest/query/lint).
2. The scaffolded `brain/CLAUDE.md` — the operating schema this wiki runs on
   (flat layout, frontmatter rules, naming, retrieval order, do's & don'ts).
3. The three `Template.md` files (`projects/`, `people/`, `events/`) — the exact
   section structure each page type must follow.

### 3. Restructure the raw notes into pages — the heart of the job

Read **every** file in `raw-notes/` carefully first; build a mental map of what's
there before writing anything. Then create pages:

- **One project page per project.** Anything that reads like an initiative,
  effort, or ongoing piece of work → `projects/<Title-Case-With-Hyphens>.md`
  using `projects/Template.md`. Sort action items into the Urgent / Do / Do
  eventually buckets per the template's priority rule (default to **Do** when
  unclear).
- **One person page per significantly-mentioned person.** Someone who recurs, is
  tied to a project, or has follow-ups/touchpoints → `people/<Firstname>.md`
  (promote to `Firstname Lastname.md` on a collision) using `people/Template.md`.
  A name mentioned once in passing does **not** need a page — use judgment;
  significance, not mere appearance, is the bar.
- **Events** (a conference, meetup, offsite) → `events/<Name>.md` via
  `events/Template.md`.
- **Knowledge** (a concept, a course, a paper/article read) →
  `knowledge/Research|Courses|Reading/<Name>.md`.
- **Ideas** (automation or product ideas, "wouldn't it be cool if…") →
  `ideas/<Name>.md`.

While writing pages, hold to these conventions (full detail in `CLAUDE.md` and
the `Template.md` files):

- **Frontmatter** — every page opens with the seven mandatory fields (title,
  source, author, published, created, description, tags) plus the per-type
  extras (`type`, `status`, `updated`; person adds `org`/`relationship`; event
  adds `event_date`/`role`). YAML gotcha: wrap any string containing `: `
  (colon-space) in double quotes or rephrase to drop the colon.
- **Cross-link aggressively.** Every project page links the `[[People]]` on it;
  every person page links the `[[Projects]]` they touch. Bare-filename wikilinks
  (`[[Project-Name]]`). Cross-links are as valuable as the pages themselves.
- **Preserve the user's words.** When a note is a raw braindump or "random
  thoughts," file the user's wording **verbatim** — do not paraphrase. Style
  edits destroy signal. (This is a hard rule in `CLAUDE.md`.)
- **Never invent facts.** If a note is ambiguous (who owns this? is this a
  project or just an idea?), capture what's there and flag the question rather
  than guessing. Don't auto-promote a loose idea into a project.
- **Flag contradictions** rather than silently overwriting — note both claims
  with dates.
- **Bias toward more, smaller, well-linked pages** over a few sprawling ones.

Set `created`/`updated` frontmatter dates to today's date (ask or infer from
context if unknown — don't fabricate a specific date if you truly can't tell).

### 4. Wire up the catalog, cache, and log

Once the pages exist, make the system self-consistent:

- **`index.md`** — add a `- [[Page-Name]] — one-line summary.` entry for every
  page you created, under the right category section.
- **`hotcache.md`** — prepend the most-recently-touched pages (keep 5–8, trim the
  bottom, body ≤500 chars).
- **`HOME.md`** — fill the Active-projects and People-in-motion tables **inside**
  the `<!-- vault:* -->` marker pairs only.
- **`log.md`** — prepend one `## [YYYY-MM-DD] restructure | …` entry recording
  the build (one-line summary, `Pages touched:` list, `Notable:`).

### 5. Report and hand back

Print the tree you created and a short "here's what each piece does." Then
**stop** and hand back — surface any contradictions or ambiguities you flagged,
and ask the user to (a) confirm the project/person split looks right and (b)
share their project categories / domain vocabulary so the schema can be tuned to
them. The wiki is meant to be co-evolved, not finished in one shot.

## What NOT to do

- Don't hand-roll `CLAUDE.md` or the skeleton files — the script copies the
  canonical versions; that's the whole point of byte-identical scaffolding.
- Don't build the old nested `knowledge-base/wiki/` layout — this is the flat
  layout.
- Don't overwrite or delete anything in `raw-notes/` — it's the immutable source.
- Don't put secrets (API keys, tokens) in any file — reference by name.
- Don't paraphrase raw user thoughts, invent facts, or auto-promote ideas to
  projects.

---

## Appendix: The LLM Wiki pattern (verbatim)

Reproduced verbatim below so it is always available inline — do not
assume any external file is present. This is the *why* behind the skill.

<!-- BEGIN andrej-llm-wiki.md (verbatim) -->

# LLM Wiki

A pattern for building personal knowledge bases using LLMs.

This is an idea file, it is designed to be copy pasted to your own LLM Agent (e.g. OpenAI Codex, Claude Code, OpenCode / Pi, or etc.). Its goal is to communicate the high level idea, but your agent will build out the specifics in collaboration with you.

## The core idea

Most people's experience with LLMs and documents looks like RAG: you upload a collection of files, the LLM retrieves relevant chunks at query time, and generates an answer. This works, but the LLM is rediscovering knowledge from scratch on every question. There's no accumulation. Ask a subtle question that requires synthesizing five documents, and the LLM has to find and piece together the relevant fragments every time. Nothing is built up. NotebookLM, ChatGPT file uploads, and most RAG systems work this way.

The idea here is different. Instead of just retrieving from raw documents at query time, the LLM **incrementally builds and maintains a persistent wiki** — a structured, interlinked collection of markdown files that sits between you and the raw sources. When you add a new source, the LLM doesn't just index it for later retrieval. It reads it, extracts the key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting where new data contradicts old claims, strengthening or challenging the evolving synthesis. The knowledge is compiled once and then *kept current*, not re-derived on every query.

This is the key difference: **the wiki is a persistent, compounding artifact.** The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read. The wiki keeps getting richer with every source you add and every question you ask.

You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions. The LLM does all the grunt work — the summarizing, cross-referencing, filing, and bookkeeping that makes a knowledge base actually useful over time. In practice, I have the LLM agent open on one side and Obsidian open on the other. The LLM makes edits based on our conversation, and I browse the results in real time — following links, checking the graph view, reading the updated pages. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

This can apply to a lot of different contexts. A few examples:

- **Personal**: tracking your own goals, health, psychology, self-improvement — filing journal entries, articles, podcast notes, and building up a structured picture of yourself over time.
- **Research**: going deep on a topic over weeks or months — reading papers, articles, reports, and incrementally building a comprehensive wiki with an evolving thesis.
- **Reading a book**: filing each chapter as you go, building out pages for characters, themes, plot threads, and how they connect. By the end you have a rich companion wiki. Think of fan wikis like [Tolkien Gateway](https://tolkiengateway.net/wiki/Main_Page) — thousands of interlinked pages covering characters, places, events, languages, built by a community of volunteers over years. You could build something like that personally as you read, with the LLM doing all the cross-referencing and maintenance.
- **Business/team**: an internal wiki maintained by LLMs, fed by Slack threads, meeting transcripts, project documents, customer calls. Possibly with humans in the loop reviewing updates. The wiki stays current because the LLM does the maintenance that no one on the team wants to do.
- **Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives** — anything where you're accumulating knowledge over time and want it organized rather than scattered.

## Architecture

There are three layers:

**Raw sources** — your curated collection of source documents. Articles, papers, images, data files. These are immutable — the LLM reads from them but never modifies them. This is your source of truth.

**The wiki** — a directory of LLM-generated markdown files. Summaries, entity pages, concept pages, comparisons, an overview, a synthesis. The LLM owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. You read it; the LLM writes it.

**The schema** — a document (e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex) that tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow when ingesting sources, answering questions, or maintaining the wiki. This is the key configuration file — it's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot. You and the LLM co-evolve this over time as you figure out what works for your domain.

## Operations

**Ingest.** You drop a new source into the raw collection and tell the LLM to process it. An example flow: the LLM reads the source, discusses key takeaways with you, writes a summary page in the wiki, updates the index, updates relevant entity and concept pages across the wiki, and appends an entry to the log. A single source might touch 10-15 wiki pages. Personally I prefer to ingest sources one at a time and stay involved — I read the summaries, check the updates, and guide the LLM on what to emphasize. But you could also batch-ingest many sources at once with less supervision. It's up to you to develop the workflow that fits your style and document it in the schema for future sessions.

**Query.** You ask questions against the wiki. The LLM searches for relevant pages, reads them, and synthesizes an answer with citations. Answers can take different forms depending on the question — a markdown page, a comparison table, a slide deck (Marp), a chart (matplotlib), a canvas. The important insight: **good answers can be filed back into the wiki as new pages.** A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history. This way your explorations compound in the knowledge base just like ingested sources do.

**Lint.** Periodically, ask the LLM to health-check the wiki. Look for: contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, important concepts mentioned but lacking their own page, missing cross-references, data gaps that could be filled with a web search. The LLM is good at suggesting new questions to investigate and new sources to look for. This keeps the wiki healthy as it grows.

## Indexing and logging

Two special files help the LLM (and you) navigate the wiki as it grows. They serve different purposes:

**index.md** is content-oriented. It's a catalog of everything in the wiki — each page listed with a link, a one-line summary, and optionally metadata like date or source count. Organized by category (entities, concepts, sources, etc.). The LLM updates it on every ingest. When answering a query, the LLM reads the index first to find relevant pages, then drills into them. This works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure.

**log.md** is chronological. It's an append-only record of what happened and when — ingests, queries, lint passes. A useful tip: if each entry starts with a consistent prefix (e.g. `## [2026-04-02] ingest | Article Title`), the log becomes parseable with simple unix tools — `grep "^## \[" log.md | tail -5` gives you the last 5 entries. The log gives you a timeline of the wiki's evolution and helps the LLM understand what's been done recently.

## Optional: CLI tools

At some point you may want to build small tools that help the LLM operate on the wiki more efficiently. A search engine over the wiki pages is the most obvious one — at small scale the index file is enough, but as the wiki grows you want proper search. [qmd](https://github.com/tobi/qmd) is a good option: it's a local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking, all on-device. It has both a CLI (so the LLM can shell out to it) and an MCP server (so the LLM can use it as a native tool). You could also build something simpler yourself — the LLM can help you vibe-code a naive search script as the need arises.

## Tips and tricks

- **Obsidian Web Clipper** is a browser extension that converts web articles to markdown. Very useful for quickly getting sources into your raw collection.
- **Download images locally.** In Obsidian Settings → Files and links, set "Attachment folder path" to a fixed directory (e.g. `raw/assets/`). Then in Settings → Hotkeys, search for "Download" to find "Download attachments for current file" and bind it to a hotkey (e.g. Ctrl+Shift+D). After clipping an article, hit the hotkey and all images get downloaded to local disk. This is optional but useful — it lets the LLM view and reference images directly instead of relying on URLs that may break. Note that LLMs can't natively read markdown with inline images in one pass — the workaround is to have the LLM read the text first, then view some or all of the referenced images separately to gain additional context. It's a bit clunky but works well enough.
- **Obsidian's graph view** is the best way to see the shape of your wiki — what's connected to what, which pages are hubs, which are orphans.
- **Marp** is a markdown-based slide deck format. Obsidian has a plugin for it. Useful for generating presentations directly from wiki content.
- **Dataview** is an Obsidian plugin that runs queries over page frontmatter. If your LLM adds YAML frontmatter to wiki pages (tags, dates, source counts), Dataview can generate dynamic tables and lists.
- The wiki is just a git repo of markdown files. You get version history, branching, and collaboration for free.

## Why this works

The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else.

The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that.


## Note

This document is intentionally abstract. It describes the idea, not a specific implementation. The exact directory structure, the schema conventions, the page formats, the tooling — all of that will depend on your domain, your preferences, and your LLM of choice. Everything mentioned above is optional and modular — pick what's useful, ignore what isn't. For example: your sources might be text-only, so you don't need image handling at all. Your wiki might be small enough that the index file is all you need, no search engine required. You might not care about slide decks and just want markdown pages. You might want a completely different set of output formats. The right way to use this is to share it with your LLM agent and work together to instantiate a version that fits your needs. The document's only job is to communicate the pattern. Your LLM can figure out the rest.
<!-- END andrej-llm-wiki.md (verbatim) -->
