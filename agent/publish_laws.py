"""
publish_laws.py — render the law encyclopedia for humboldt-site (/laws/).

The law record (``laws/L-NNN-*.yaml``) is the single research artifact type
in the 2026-08 redesign (plan §3.1/§3.3) — it replaces the old C/H/CL/T/F
typed-artifact pages. This module reads ``laws/*.yaml`` via ``agent.laws``
and ``bibliography/bibliography.yaml`` via ``agent.bibliography`` (for the
forward `laws:` index, used here in reverse — which sources cite each law)
and renders one card per law, grouped by Double Freytag stage.

Consumed by ``humboldt-site/build.py`` (``_build_laws``), which inserts the
root into ``sys.path`` before importing this module — mirrors the existing
``publish_research`` / ``publish_reading`` convention.
"""

from __future__ import annotations

import html as _html
import re
from pathlib import Path

from agent import laws as laws_mod
from agent import bibliography as bib_mod

_ROOT = Path(__file__).parent.parent

STAGES = laws_mod.STAGES  # exploration, sensemaking, valley, heavy-lift, retrospective

STAGE_LABEL = {
    "exploration":   "Exploration",
    "sensemaking":   "Sensemaking",
    "valley":        "Valley",
    "heavy-lift":    "Heavy Lift",
    "retrospective": "Retrospective",
}

STAGE_DESC = {
    "exploration":   "Law-shaped idea registered; evidence anecdotal",
    "sensemaking":   "Statement + mechanism + falsification conditions present",
    "valley":        "Evidence accumulation across domains; cruxes being worked",
    "heavy-lift":    "Evidence from 3+ independent domains; separation artifact in progress",
    "retrospective": "Published and monitored; subject to periodic challenge attempts",
}

STAGE_ICON = laws_mod._STAGE_ICON  # ○ ◔ ◑ ◕ ●

CONFIDENCE_CLASS = {
    "speculative": "conf-speculative",
    "provisional": "conf-provisional",
    "supported":   "conf-supported",
    "unfalsified": "conf-unfalsified",
}

STATUS_CLASS = {
    "active":     "",
    "challenged": "status-challenged",
    "falsified":  "status-falsified",
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def _esc(s: str) -> str:
    return _html.escape(str(s or ""), quote=False)


def _prose(text: str) -> str:
    """Folded-scalar prose → paragraphs. Blank lines are paragraph breaks."""
    text = str(text or "").strip()
    if not text:
        return ""
    paras = re.split(r"\n\s*\n", text)
    return "\n".join(f"<p>{_esc(p).replace(chr(10), ' ').strip()}</p>" for p in paras if p.strip())


def _bib_index_by_law() -> dict[str, list[dict]]:
    """law_id -> bibliography entries that cite it (bib entry's `laws:` field)."""
    idx: dict[str, list[dict]] = {}
    for e in bib_mod.load():
        for lid in (e.get("laws") or []):
            idx.setdefault(lid, []).append(e)
    for lid in idx:
        idx[lid].sort(key=lambda e: (e.get("year") or 0), reverse=True)
    return idx


def _bib_link(e: dict) -> str:
    """Link a bibliography entry to its best on-site anchor."""
    title = _esc(e.get("title", e.get("id", "")))[:90]
    depth = e.get("read_depth", "listed")
    if depth == "deep" and e.get("notes"):
        stem = Path(e["notes"]).stem
        return f'<a href="/reading/#read-{stem}">{title}</a>'
    if depth == "shallow" and e.get("summary"):
        stem = Path(e["summary"]).stem
        return f'<a href="/reading/#shallow-{stem}">{title}</a>'
    return f'<a href="/bibliography/#{e.get("id", "")}">{title}</a>'


# ── Card rendering ────────────────────────────────────────────────────────────

def _examples_html(items: list[dict], kind: str) -> str:
    if not items:
        return ""
    rows = []
    for it in items:
        if kind == "example":
            domain = _esc(it.get("domain", ""))
            desc = _esc(it.get("description", ""))
            rows.append(f"<li><strong>{domain}:</strong> {desc}</li>" if domain else f"<li>{desc}</li>")
        else:  # counterexample
            desc = _esc(it.get("description", ""))
            res = _esc(it.get("resolution", "OPEN"))
            open_flag = ' <span class="ce-open">OPEN</span>' if res.upper() == "OPEN" else ""
            rows.append(f"<li>{desc}<br><span class=\"ce-resolution\">→ {res}</span>{open_flag}</li>")
    return "<ul>" + "\n".join(rows) + "</ul>"


def _history_html(history: list[dict]) -> str:
    if not history:
        return ""
    rows = []
    for h in sorted(history, key=lambda h: h.get("date", ""), reverse=True):
        rows.append(
            f'<li><span class="hist-date">{_esc(h.get("date", ""))}</span> '
            f'<span class="hist-event">{_esc(h.get("event", ""))}</span> — '
            f'{_esc(h.get("detail", ""))}</li>'
        )
    return "<ul class=\"law-history\">" + "\n".join(rows) + "</ul>"


def _render_law_card(law, cited_by: list[dict]) -> str:
    lid = law.get("id", "?")
    slug = law.get("slug", "")
    title = _esc(law.get("title", lid))
    stage = law.get("stage", "exploration")
    status = law.get("status", "active")
    confidence = law.get("confidence", "speculative")
    origin = law.get("origin", "discovered")

    badges = [
        f'<span class="law-badge stage-badge">{STAGE_ICON.get(stage, "?")} {STAGE_LABEL.get(stage, stage)}</span>',
        f'<span class="law-badge {CONFIDENCE_CLASS.get(confidence, "")}">{_esc(confidence)}</span>',
    ]
    if status != "active":
        badges.append(f'<span class="law-badge {STATUS_CLASS.get(status, "")}">{_esc(status)}</span>')
    if origin == "imported":
        src = _esc(law.get("source") or "")
        badges.append(f'<span class="law-badge origin-badge">imported{" — " + src if src else ""}</span>')

    statement_html = _prose(law.get("statement", ""))
    mechanism_html = _prose(law.get("mechanism", ""))
    justification_html = _prose(law.get("justification", ""))
    examples_html = _examples_html(law.get("examples") or [], "example")
    counter_html = _examples_html(law.get("counterexamples") or [], "counterexample")
    open_qs = law.get("open_questions") or []
    open_qs_html = ("<ul>" + "\n".join(f"<li>{_esc(q)}</li>" for q in open_qs) + "</ul>") if open_qs else ""
    falsification_html = _prose(law.get("falsification", ""))
    history_html = _history_html(law.get("history") or [])

    refs = law.get("references") or []
    refs_html = ("<ul>" + "\n".join(f"<li>{_esc(r)}</li>" for r in refs) + "</ul>") if refs else "<p><em>None recorded.</em></p>"

    cited_html = ""
    if cited_by:
        n = len(cited_by)
        links = "".join(f"<li>{_bib_link(e)}</li>" for e in cited_by[:12])
        more = f"<li><em>+ {n - 12} more</em></li>" if n > 12 else ""
        cited_html = (
            f'<p class="section-label">Cited by {n} source{"s" if n != 1 else ""} in the bibliography</p>'
            f"<ul>{links}{more}</ul>"
        )

    related = law.get("related") or []
    related_html = ""
    if related:
        chips = " ".join(f'<a class="related-chip" href="#law-{r}">{_esc(r)}</a>' for r in related)
        related_html = f'<p class="section-label">Related laws</p><p>{chips}</p>'

    triggers = law.get("triggers") or {}
    trig_html = ""
    if triggers.get("advance") or triggers.get("challenge"):
        trig_html = '<p class="section-label">Triggers</p><ul>'
        if triggers.get("advance"):
            trig_html += f'<li><strong>Advance:</strong> {_esc(triggers["advance"]).strip()}</li>'
        if triggers.get("challenge"):
            trig_html += f'<li><strong>Challenge:</strong> {_esc(triggers["challenge"]).strip()}</li>'
        trig_html += "</ul>"

    gh_url = f"https://github.com/Protocol-Institute/humboldt/blob/main/laws/{lid}-{slug}.yaml"

    return f"""
    <div class="law-card" id="law-{lid}" data-stage="{stage}">
      <div class="law-meta">
        <span class="law-id">{lid}</span>
        <a class="entry-permalink" href="#law-{lid}" title="Link to this law">§</a>
        <a class="entry-permalink" href="{gh_url}" target="_blank" rel="noopener" title="View source YAML">↗</a>
      </div>
      <h2 class="law-title">{title}</h2>
      <div class="law-badges">{"".join(badges)}</div>
      <div class="law-statement">{statement_html}</div>
      <details class="law-details">
        <summary>Full record — mechanism, justification, evidence, history</summary>
        <div class="law-details-body">
          {"<p class='section-label'>Mechanism</p>" + mechanism_html if mechanism_html else ""}
          {"<p class='section-label'>Justification</p>" + justification_html if justification_html else ""}
          {"<p class='section-label'>Examples</p>" + examples_html if examples_html else ""}
          {"<p class='section-label'>Counterexamples</p>" + counter_html if counter_html else ""}
          {"<p class='section-label'>Open questions</p>" + open_qs_html if open_qs_html else ""}
          {"<p class='section-label'>Falsification</p>" + falsification_html if falsification_html else ""}
          {trig_html}
          {related_html}
          {cited_html}
          <p class="section-label">References (as recorded on the law)</p>
          {refs_html}
          <p class="section-label">History</p>
          {history_html}
        </div>
      </details>
    </div>"""


def _stage_header(stage: str, count: int) -> str:
    n = f"{count} law{'s' if count != 1 else ''}" if count else "none yet"
    return (
        f'<div class="stage-header" data-stage-header="{stage}">'
        f'<span class="sh-name">{STAGE_ICON.get(stage, "?")} {STAGE_LABEL.get(stage, stage)}</span>'
        f'<span class="sh-desc">{STAGE_DESC.get(stage, "")}</span>'
        f'<span class="sh-count">{n}</span></div>'
    )


# ── Page assembly ─────────────────────────────────────────────────────────────

def build_laws_body() -> tuple[str, int, dict[str, int]]:
    """Returns (body_html, total_count, stage_counts)."""
    all_laws = laws_mod.load_all()
    bib_by_law = _bib_index_by_law()

    stage_counts = {s: 0 for s in STAGES}
    for law in all_laws:
        stage_counts[law.get("stage", "exploration")] = stage_counts.get(law.get("stage", "exploration"), 0) + 1

    filter_buttons = ['<button class="stage-filter active" data-filter="all">All</button>']
    for s in STAGES:
        filter_buttons.append(
            f'<button class="stage-filter" data-filter="{s}">{STAGE_ICON.get(s, "?")} {STAGE_LABEL[s]} '
            f'<span class="fb-count">{stage_counts.get(s, 0)}</span></button>'
        )

    sections = []
    for stage in STAGES:
        laws_here = [l for l in all_laws if l.get("stage") == stage]
        sections.append(_stage_header(stage, len(laws_here)))
        if not laws_here:
            sections.append('<p class="stage-empty"><em>None currently.</em></p>')
            continue
        # Most-recently-active first within a stage.
        laws_here.sort(key=lambda l: (l.get("history") or [{}])[-1].get("date", ""), reverse=True)
        for law in laws_here:
            sections.append(_render_law_card(law, bib_by_law.get(law.get("id"), [])))

    body = f"""\
    <div class="page-header">
      <h1>Law Encyclopedia</h1>
      <p class="page-tagline">{len(all_laws)} candidate laws, one unified record type moving through the
      Double Freytag arc — exploration, sensemaking, valley, heavy-lift, retrospective. Falsified laws
      stay published, labeled, as negative results. See <a href="/about/">how the funnel works</a>.</p>
    </div>

    <div class="stage-filters">{"".join(filter_buttons)}</div>

    <div class="law-list">
{"".join(sections)}
    </div>"""

    return body, len(all_laws), stage_counts


_CSS = """
    .stage-filters {
      display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 2rem;
    }
    .stage-filter {
      font-family: 'DM Sans', sans-serif; font-size: 0.8rem; letter-spacing: 0.02em;
      color: #555; background: #f0f0ec; border: 1px solid #e0e0da; border-radius: 999px;
      padding: 0.35rem 0.85rem; cursor: pointer; transition: background 0.15s, color 0.15s;
    }
    .stage-filter:hover { background: #e5e5df; }
    .stage-filter.active { background: #2A6B6B; color: #fff; border-color: #2A6B6B; }
    .fb-count { opacity: 0.65; font-size: 0.85em; }

    .stage-header {
      display: flex; align-items: baseline; gap: 0.9rem; flex-wrap: wrap;
      border-top: 2px solid #2A6B6B; padding-top: 0.6rem; margin: 2.5rem 0 1.25rem;
    }
    .stage-header:first-child { margin-top: 0; }
    .sh-name {
      font-family: 'Cormorant Garamond', Georgia, serif; font-size: 1.4rem; font-weight: 600;
    }
    .sh-desc { color: #777; font-size: 0.85rem; font-style: italic; }
    .sh-count { margin-left: auto; color: #999; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; }
    .stage-empty { color: #999; margin-bottom: 1rem; }

    .law-card {
      border: 1px solid #e5e5df; border-radius: 6px; background: #fff;
      padding: 1.5rem 1.75rem; margin-bottom: 1.5rem;
    }
    .law-meta { font-size: 0.8rem; color: #999; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 0.2rem; }
    .law-id { font-weight: 500; }
    .law-title { margin: 0 0 0.7rem; font-size: 1.5rem; }
    .law-badges { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 1rem; }
    .law-badge {
      font-family: 'DM Sans', sans-serif; font-size: 0.75rem; padding: 0.2rem 0.6rem;
      border-radius: 3px; background: #eee; color: #444; text-transform: capitalize;
    }
    .stage-badge { background: #edf5f5; color: #1d4f4f; text-transform: none; }
    .conf-speculative { background: #f2f0e8; color: #8a7a3a; }
    .conf-provisional { background: #fdf0dd; color: #a5620a; }
    .conf-supported    { background: #e3f0ea; color: #1e6b45; }
    .conf-unfalsified  { background: #dcefe8; color: #0f5c3d; }
    .status-challenged { background: #fde3e3; color: #a5290a; }
    .status-falsified  { background: #2a2a2a; color: #fff; }
    .origin-badge { background: #ece7f5; color: #4a3a8a; }

    .law-statement p {
      font-family: 'Cormorant Garamond', Georgia, serif; font-size: 1.15rem; font-style: italic;
      color: #333; max-width: none;
    }
    .law-details { margin-top: 1.1rem; border-top: 1px solid #eee; padding-top: 0.6rem; }
    .law-details summary {
      cursor: pointer; font-size: 0.88rem; color: #2A6B6B; font-family: 'DM Sans', sans-serif;
      padding: 0.4rem 0; user-select: none;
    }
    .law-details summary:hover { color: #1d4f4f; }
    .law-details-body { padding-top: 0.5rem; font-size: 0.93rem; }
    .law-details-body .section-label { margin-top: 1.1rem; }
    .law-details-body ul { margin-bottom: 0.9rem; }
    .ce-resolution { color: #666; font-size: 0.9em; }
    .ce-open { background: #fde3e3; color: #a5290a; font-size: 0.72rem; padding: 0.05rem 0.4rem; border-radius: 2px; }
    .law-history { list-style: none; padding-left: 0; }
    .law-history li { font-size: 0.85rem; margin-bottom: 0.35rem; }
    .hist-date { color: #999; font-variant-numeric: tabular-nums; }
    .hist-event { color: #2A6B6B; font-weight: 500; text-transform: capitalize; }
    .related-chip {
      display: inline-block; background: #f0f0ec; border-radius: 3px; padding: 0.1rem 0.5rem;
      margin: 0 0.3rem 0.3rem 0; font-size: 0.85rem;
    }
"""

_JS = """
(function() {
  var buttons = document.querySelectorAll('.stage-filter');
  var cards = document.querySelectorAll('.law-card');
  var headers = document.querySelectorAll('.stage-header');
  buttons.forEach(function(btn) {
    btn.addEventListener('click', function() {
      buttons.forEach(function(b) { b.classList.remove('active'); });
      btn.classList.add('active');
      var f = btn.getAttribute('data-filter');
      cards.forEach(function(c) {
        c.style.display = (f === 'all' || c.getAttribute('data-stage') === f) ? '' : 'none';
      });
      headers.forEach(function(h) {
        h.style.display = (f === 'all' || h.getAttribute('data-stage-header') === f) ? '' : 'none';
      });
      var empties = document.querySelectorAll('.stage-empty');
      empties.forEach(function(e) {
        var prevStage = e.previousElementSibling ? e.previousElementSibling.getAttribute('data-stage-header') : null;
        e.style.display = (f === 'all' || prevStage === f) ? '' : 'none';
      });
    });
  });
})();
"""
