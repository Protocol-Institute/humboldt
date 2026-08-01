"""
publish_bibliography.py — render the canonical bibliography for humboldt-site
(/bibliography/), plan §4.2.

Reads ``bibliography/bibliography.yaml`` via ``agent.bibliography`` (929
entries as of the 2026-08 migration) and renders a filterable table: each
entry links to its own read summary/notes on ``/reading/`` when it has one
(deep → ``#read-<stem>``, shallow → ``#shallow-<stem>``), else to its source
URL, and shows the laws that cite it linked into ``/laws/``.

Consumed by ``humboldt-site/build.py`` (``_build_bibliography``), which
inserts the repo root into ``sys.path`` before importing — same convention
as ``publish_research`` / ``publish_reading`` / ``publish_laws``.
"""

from __future__ import annotations

import html as _html
from pathlib import Path

from agent import bibliography as bib_mod

DEPTH_ICON = {"listed": "·", "shallow": "◑", "deep": "●"}
DEPTH_LABEL = {"listed": "Listed", "shallow": "Shallow read", "deep": "Deep read"}


def _esc(s) -> str:
    return _html.escape(str(s or ""), quote=True)


def _title_link(e: dict) -> str:
    title = _esc(e.get("title") or e.get("id", "untitled"))[:140]
    depth = e.get("read_depth", "listed")
    if depth == "deep" and e.get("notes"):
        stem = Path(e["notes"]).stem
        return f'<a href="/reading/#read-{stem}">{title}</a>'
    if depth == "shallow" and e.get("summary"):
        stem = Path(e["summary"]).stem
        return f'<a href="/reading/#shallow-{stem}">{title}</a>'
    url = e.get("url")
    if url:
        return f'<a href="{_esc(url)}" target="_blank" rel="noopener">{title}</a>'
    return title


def _laws_html(e: dict) -> str:
    laws = e.get("laws") or []
    if not laws:
        return ""
    return " ".join(f'<a class="law-chip" href="/laws/#law-{_esc(l)}">{_esc(l)}</a>' for l in laws)


def _row(e: dict) -> str:
    depth = e.get("read_depth", "listed")
    kind = e.get("kind", "content")
    year = e.get("year") or ""
    authors = ", ".join(e.get("authors") or []) or ""
    eid = _esc(e.get("id", ""))
    meta_badge = f'<span class="kind-badge">meta</span>' if kind == "meta" else ""
    return (
        f'<tr id="{eid}" data-depth="{depth}" data-kind="{kind}" '
        f'data-search="{_esc((e.get("title") or "") + " " + authors).lower()}">'
        f'<td class="bib-year">{year}</td>'
        f'<td class="bib-title">{_title_link(e)} {meta_badge}</td>'
        f'<td class="bib-authors">{_esc(authors)}</td>'
        f'<td class="bib-depth" title="{DEPTH_LABEL.get(depth, depth)}">{DEPTH_ICON.get(depth, "?")}</td>'
        f'<td class="bib-laws">{_laws_html(e)}</td>'
        f"</tr>"
    )


def build_bibliography_body() -> tuple[str, int]:
    entries = bib_mod.load()
    entries_sorted = sorted(
        entries,
        key=lambda e: (e.get("year") or -1, (e.get("title") or "")),
        reverse=True,
    )

    by_depth = {"listed": 0, "shallow": 0, "deep": 0}
    by_kind = {"content": 0, "meta": 0}
    cited = 0
    for e in entries:
        by_depth[e.get("read_depth", "listed")] = by_depth.get(e.get("read_depth", "listed"), 0) + 1
        by_kind[e.get("kind", "content")] = by_kind.get(e.get("kind", "content"), 0) + 1
        if e.get("laws"):
            cited += 1

    rows_html = "\n".join(_row(e) for e in entries_sorted)

    body = f"""\
    <div class="page-header">
      <h1>Bibliography</h1>
      <p class="page-tagline">{len(entries)} sources engaged past triage-discard — feeds, Discord links,
      operator drops, and citation chases. {cited} cited by at least one law. See also
      <a href="/reading/">deep and shallow reading notes</a>.</p>
    </div>

    <div class="bib-stats">
      <span><strong>{by_depth['listed']}</strong> listed</span>
      <span><strong>{by_depth['shallow']}</strong> shallow-read</span>
      <span><strong>{by_depth['deep']}</strong> deep-read</span>
      <span><strong>{by_kind['meta']}</strong> meta (research-methodology sources)</span>
    </div>

    <div class="bib-controls">
      <input id="bib-search" class="bib-search" type="text" placeholder="Filter by title or author…">
      <div class="bib-filter-group">
        <span class="bfg-label">Depth</span>
        <button class="bib-filter active" data-filter-type="depth" data-filter="all">All</button>
        <button class="bib-filter" data-filter-type="depth" data-filter="listed">Listed</button>
        <button class="bib-filter" data-filter-type="depth" data-filter="shallow">Shallow</button>
        <button class="bib-filter" data-filter-type="depth" data-filter="deep">Deep</button>
      </div>
      <div class="bib-filter-group">
        <span class="bfg-label">Kind</span>
        <button class="bib-filter active" data-filter-type="kind" data-filter="all">All</button>
        <button class="bib-filter" data-filter-type="kind" data-filter="content">Content</button>
        <button class="bib-filter" data-filter-type="kind" data-filter="meta">Meta</button>
      </div>
      <span id="bib-count" class="bib-count"></span>
    </div>

    <table class="bib-table">
      <thead>
        <tr><th style="width:64px">Year</th><th>Title</th><th style="width:180px">Authors</th>
        <th style="width:40px">Depth</th><th style="width:110px">Laws</th></tr>
      </thead>
      <tbody id="bib-tbody">
{rows_html}
      </tbody>
    </table>
    <p class="updated-note">Source: <a href="https://github.com/Protocol-Institute/humboldt/blob/main/bibliography/bibliography.yaml"
    target="_blank" rel="noopener">bibliography.yaml on GitHub</a>.</p>"""

    return body, len(entries)


_CSS = """
    .bib-stats {
      display: flex; flex-wrap: wrap; gap: 1.5rem; margin-bottom: 1.5rem;
      font-size: 0.88rem; color: #555;
    }
    .bib-stats strong { color: #2A6B6B; }

    .bib-controls {
      display: flex; flex-wrap: wrap; align-items: center; gap: 0.9rem;
      margin-bottom: 1rem; position: sticky; top: 52px; background: #FAFAF7;
      padding: 0.75rem 0; border-bottom: 1px solid #e8e8e4; z-index: 10;
    }
    .bib-search {
      font-family: 'DM Sans', sans-serif; font-size: 0.88rem; padding: 0.4rem 0.7rem;
      border: 1px solid #ddd; border-radius: 4px; min-width: 220px; background: #fff;
    }
    .bib-search:focus { outline: none; border-color: #2A6B6B; }
    .bib-filter-group { display: flex; align-items: center; gap: 0.3rem; }
    .bfg-label { font-size: 0.75rem; color: #999; text-transform: uppercase; letter-spacing: 0.05em; margin-right: 0.2rem; }
    .bib-filter {
      font-family: 'DM Sans', sans-serif; font-size: 0.78rem; color: #555; background: #f0f0ec;
      border: 1px solid #e0e0da; border-radius: 999px; padding: 0.25rem 0.7rem; cursor: pointer;
    }
    .bib-filter:hover { background: #e5e5df; }
    .bib-filter.active { background: #2A6B6B; color: #fff; border-color: #2A6B6B; }
    .bib-count { margin-left: auto; font-size: 0.8rem; color: #999; }

    .bib-table { font-size: 0.85rem; }
    .bib-table th { position: sticky; top: 106px; background: #FAFAF7; }
    .bib-year { color: #999; font-variant-numeric: tabular-nums; }
    .bib-title a { word-break: break-word; }
    .bib-authors { color: #666; font-size: 0.85em; }
    .bib-depth { text-align: center; color: #2A6B6B; }
    .kind-badge {
      background: #666; color: #fff; font-size: 0.68rem; padding: 0.05rem 0.4rem;
      border-radius: 2px; margin-left: 0.3rem; text-transform: uppercase; letter-spacing: 0.03em;
    }
    .law-chip {
      display: inline-block; background: #edf5f5; color: #1d4f4f; border-radius: 3px;
      padding: 0.05rem 0.4rem; margin: 0 0.2rem 0.2rem 0; font-size: 0.8rem;
    }

    @media (max-width: 640px) {
      .bib-controls { position: static; }
      .bib-table th { position: static; }
      .bib-authors { display: none; }
    }
"""

_JS = """
(function() {
  var rows = Array.prototype.slice.call(document.querySelectorAll('#bib-tbody tr'));
  var search = document.getElementById('bib-search');
  var countEl = document.getElementById('bib-count');
  var state = { depth: 'all', kind: 'all', q: '' };

  function apply() {
    var visible = 0;
    rows.forEach(function(r) {
      var okDepth = state.depth === 'all' || r.getAttribute('data-depth') === state.depth;
      var okKind = state.kind === 'all' || r.getAttribute('data-kind') === state.kind;
      var okQ = !state.q || r.getAttribute('data-search').indexOf(state.q) !== -1;
      var show = okDepth && okKind && okQ;
      r.style.display = show ? '' : 'none';
      if (show) visible++;
    });
    countEl.textContent = visible + ' of ' + rows.length + ' shown';
  }

  document.querySelectorAll('.bib-filter').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var type = btn.getAttribute('data-filter-type');
      document.querySelectorAll('.bib-filter[data-filter-type="' + type + '"]').forEach(function(b) {
        b.classList.remove('active');
      });
      btn.classList.add('active');
      state[type] = btn.getAttribute('data-filter');
      apply();
    });
  });

  search.addEventListener('input', function() {
    state.q = search.value.trim().toLowerCase();
    apply();
  });

  apply();
})();
"""
