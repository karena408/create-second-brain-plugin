---
title: Wiki Operations Log
source:
author:
published:
created:
description: Append-only log of operations on the wiki. Newest at top.
tags: [log, system, meta]
type: synthesis
---

# Wiki Operations Log

Append-only. Newest at top. One entry per substantive operation (ingest, query, synthesis, lint, restructure, decision).

Format (grep-parseable on `^## \[`):

```
## [YYYY-MM-DD] op | Title

- One-line summary.
- Pages touched: [[Page-A]], [[Page-B]].
- Notable: anything worth remembering.
```

`op` ∈ `ingest | query | synthesis | lint | restructure | decision`.

---

*(no operations logged yet)*
