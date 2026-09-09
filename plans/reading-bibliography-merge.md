# Plan — merge `/reading/` into `/bibliography/` as one Reading page

**Status:** planned, not started. **Written:** 2026-09-09.
**Trigger:** operator, 2026-09-09 — "Reading is the notes on deep reads, which should be
naturally integrable into the bibliography as a subset with depth notes."

That reading of the data is correct, and the two pages are already views over one dataset.
This is a consolidation, not a migration.

---

## 1. The data already joins

Measured 2026-09-09 against `bibliography/bibliography.yaml`:

| | count |
|---|---|
| bibliography entries | 2,019 |
| — `read_depth: shallow` | 1,899 |
| — `read_depth: deep` | 71 |
| — `read_depth: listed` | 49 |
| deep note files (`bibliography/notes/`) | 71 |
| shallow note files (`bibliography/shallow-reads/`) | 2,009 |

**Deep reads join exactly: 71 entries ↔ 71 files**, and every one of those entries carries
a `notes:` field pointing at its file. No matching heuristic is needed — the pointer is
already in the record.

The two pointer fields are complementary rather than redundant, which is the key design
fact for the merged page:

- `summary:` → the shallow-read synthesis written at triage (present on 64 of the 71 deep
  entries — they were shallow-read first, then escalated).
- `notes:` → the full deep reading note.

So a deep entry can show *both*: what Humboldt thought on first pass, and what it thought
after reading the whole text. That is more interesting than either page shows today, and
it is the thing worth building rather than merely relocating.

## 2. Fix first: the shallow-note surplus

2,009 shallow note files against 1,899 shallow entries — **110 files with no entry.** These
are duplicates from the date-scoped resume bug (`dev-log.md` 2026-09-03: `shallow_read`'s
skip check embedded `date.today()`, so a sweep resumed after midnight re-read from item
one; 45 duplicated slugs were already on disk, most from June).

Do not merge over this. A merged page keyed on the bibliography silently drops the orphans,
which hides the problem rather than surfacing it. Dedupe first:

1. Group `bibliography/shallow-reads/*.md` by title slug, ignoring the date prefix.
2. Where a slug has several files, keep the earliest and delete the rest — the later ones
   are re-reads of the same source, not new work.
3. Re-check the count against `read_depth: shallow`. Investigate any residual gap rather
   than assuming it is more duplication.

## 3. Target design

**One page at `/reading/`.** The bibliography is the spine; read depth is how it is cut.

- **Filter chips** — All · Deep 71 · Shallow 1,899 · Listed 49 — same pattern as `/laws/`,
  which already works and needs no new interaction vocabulary.
- **Default view is Deep.** This is the substantive change and the reason to prefer chips
  over tabs: opening on 2,019 rows is a directory, opening on 71 deep reads is a reading
  list. The full set stays one click away. (Same reasoning as reversing the laws page to
  lead with heavy-lift.)
- **Entry rows** carry title, author, year, depth badge, and the laws that cite the source.
- **Deep entries expand inline** to the full reading note, with the shallow-read synthesis
  shown above it as "first pass" where one exists.
- **Shallow entries** show their one-paragraph synthesis inline — it is a paragraph, so it
  costs little — and link to the file.
- **Listed entries** are a title and a link. No note exists by definition.

### Page weight is the real constraint

`/bibliography/` is already 204 KB. Inlining 71 deep notes (full reading notes, some long)
plus 1,899 shallow paragraphs would push it past what is reasonable to ship as one static
page. Mitigations, in preference order:

1. Inline the 71 deep notes; render shallow synopses truncated with a link to the file.
2. If still too heavy, render deep notes as separate pages under `/reading/<bib-id>/` and
   link them, keeping one row per entry on the index.

Decide by measuring the built page, not in advance.

## 4. Migration

- `_build_reading` and `_build_bibliography` collapse into one builder. `agent/publish_bibliography.py`
  and the reading half of `agent/publish_reading.py` merge; keep `_current_law_ids()` and its
  `lru_cache` — that is what makes the build finish at all (see `project_site_build_perf`).
- **`/bibliography/` must keep resolving.** It is linked from law records, from the chat
  page, and from Discord announcements. Emit a redirect stub at `/bibliography/` rather than
  deleting the path; Cloudflare Pages supports `_redirects`, which is cleaner than an HTML
  meta refresh.
- Nav: the Reading group collapses from a dropdown back to a single top-level item.
- Update the cross-links in `_build_chat`'s site list and in the laws page footer.

## 5. Out of scope

- Changing `bibliography.yaml`'s schema. The merge is a presentation change; the record
  already carries everything the page needs.
- Re-reading anything. No source's depth changes because of this.
- The 49 `listed` entries. They are a real backlog signal — sources registered but never
  read — and worth surfacing on the page, but chasing them is funnel work, not site work.
