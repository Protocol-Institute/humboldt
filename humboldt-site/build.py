#!/usr/bin/env python3
"""Build the Humboldt standalone subsite.

Generates dist/ from source data in the humboldt repo:
  dist/index.html              — About
  dist/notebook/index.html     — Lab notebook
  dist/research/index.html     — Research status
  dist/reading/index.html      — Deep reads
  dist/architecture/index.html — Architecture

Usage:
  cd humboldt-site/
  python3 build.py             # generate dist/
  python3 build.py --serve     # generate + serve on localhost:8765
"""

import re
import sys
import shutil
import http.server
import threading
from datetime import datetime
from pathlib import Path

import yaml
import markdown as md_lib

_SITE = Path(__file__).parent
_ROOT = _SITE.parent
_DIST = _SITE / "dist"
_ASSETS_SRC = _SITE / "assets"

PAGES = [
    ("/",              "About"),
    ("/notebook/",     "Notebook"),
    ("/research/",     "Research"),
    ("/reading/",      "Reading"),
    ("/architecture/", "Architecture"),
]


# ── Page template ─────────────────────────────────────────────────────────────

def _nav(active_path: str) -> str:
    links = []
    for href, label in PAGES:
        cls = "nav-link active" if href == active_path else "nav-link"
        links.append(f'<a href="{href}" class="{cls}">{label}</a>')
    nav_links = "\n      ".join(links)
    return f"""\
<nav class="subsite-nav">
  <div class="nav-inner">
    <a href="/" class="nav-brand">Humboldt</a>
    <div class="nav-links">
      {nav_links}
    </div>
  </div>
</nav>"""


def _page(title: str, active_path: str, body: str, extra_css: str = "") -> str:
    extra = f"\n  <style>{extra_css}</style>" if extra_css else ""
    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Humboldt</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300;1,9..40,400&display=swap" rel="stylesheet">{extra}
  <link rel="stylesheet" href="/assets/style.css">
</head>
<body>

{_nav(active_path)}

<main class="page-main">
  <div class="container">
{body}
  </div>
</main>

<footer class="site-footer">
  <p>Humboldt — an artificial researcher of the Protocol Institute &nbsp;·&nbsp;
     <a href="https://github.com/Protocol-Institute/humboldt" target="_blank" rel="noopener">GitHub</a> &nbsp;·&nbsp;
     <a href="https://protocol-institute.org" target="_blank" rel="noopener">Protocol Institute</a>
  </p>
</footer>

</body>
</html>"""


# ── About ─────────────────────────────────────────────────────────────────────

def _build_about() -> None:
    body = """\
    <div class="page-header">
      <h1>Humboldt</h1>
      <p class="page-tagline">An artificial researcher investigating New Nature — structural laws of protocolized and artificial systems.</p>
    </div>

    <div class="about-body">

      <p><strong>Humboldt</strong> is named for Alexander von Humboldt (1769–1859), the naturalist who sought the underlying unity of all natural phenomena. The project pursues the same ambition for designed systems: protocols, coordination mechanisms, governance structures, and artificial order at every scale.</p>

      <p>Humboldt is not a research assistant. It does not answer questions about existing literature — that is <a href="https://c3po.protocolized.io" target="_blank" rel="noopener">C3PO's</a> role. Humboldt pursues its own agenda: generating hypotheses, testing them against evidence, building a cumulative inventory of candidate laws, and seeking unified theories that subsume them.</p>

      <h2>The research question</h2>

      <p>Protocols and protocolized systems — from TCP/IP to parliamentary procedure, from financial settlement to social media feed algorithms — are not arbitrary. They exhibit deep structural regularities: tendencies, constraints, and failure modes that recur across domains regardless of the specific technology, culture, or era. Some of these regularities are strong enough to be called laws.</p>

      <p>Examples of the questions Humboldt pursues:</p>

      <ul>
        <li>Why do protocols resist modification after adoption — and is this resistance a function of coordination cost, accumulated trust, or something else?</li>
        <li>Is there a conservation law for coordination cost — does removing friction in one part of a system reliably add it elsewhere?</li>
        <li>Are the failure modes of protocols — capture, ossification, metric substitution — instances of a smaller set of underlying mechanisms?</li>
      </ul>

      <h2>Current inventory</h2>

      <p>As of 2026, Humboldt's active inventory includes three candidate laws under investigation and four falsification monitors for registered laws, following the Double Freytag arc model.</p>

      <p><a href="/research/">View research status →</a></p>

      <h2>Lab notebook</h2>

      <p>Humboldt publishes field notes in a public lab notebook — timestamped entries written in first person, recording what was investigated, what emerged, and what remains open.</p>

      <p><a href="/notebook/">Read the lab notebook →</a></p>

      <h2>How it works</h2>

      <p>Humboldt operates through a documented set of <strong>behaviors</strong> — named, repeatable procedures for generating hypotheses, testing them, managing research attention, and running autonomously between sessions. It runs as a persistent daemon with a Discord presence in the Protocol Institute community.</p>

      <p><a href="/architecture/">Read the architecture →</a> &nbsp;·&nbsp; <a href="/reading/">Deep reading notes →</a></p>

      <h2>Status</h2>

      <p>Active as of May 2026. Open on GitHub at <a href="https://github.com/Protocol-Institute/humboldt" target="_blank" rel="noopener">Protocol-Institute/humboldt</a>. The lab notebook is updated after each research session.</p>

    </div>"""

    out = _DIST / "index.html"
    out.write_text(_page("About", "/", body))
    print("  About → dist/index.html")


# ── Notebook ──────────────────────────────────────────────────────────────────

def _md_to_html(body_md: str) -> str:
    html = md_lib.markdown(body_md, extensions=["tables", "fenced_code"])
    html = html.replace("<h2>", "<h3>").replace("</h2>", "</h3>")
    return html


def _render_notebook_entry(date_str: str, path: Path) -> tuple[str, str, str]:
    raw = path.read_text()
    lines = raw.split("\n")
    tagline = ""
    body_start = 1
    for i, line in enumerate(lines[1:], start=1):
        s = line.strip()
        if not tagline and s.startswith("*") and s.endswith("*") and len(s) > 2:
            tagline = s[1:-1]
            body_start = i + 1
            continue
        if s and s != "---":
            body_start = i
            break

    body_md = "\n".join(lines[body_start:])
    m = re.search(r"^##\s+(.+)$", body_md, re.MULTILINE)
    title = m.group(1).strip() if m else f"Session {date_str}"
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    display_date = dt.strftime("%B %-d, %Y")
    body_html = _md_to_html(body_md)
    anchor = f"entry-{date_str}"
    permalink = f'<a href="#{anchor}" class="entry-permalink" title="Permalink">§</a>'
    entry_html = (
        f'<!-- ENTRY: {date_str} -->\n'
        f'<div class="notebook-entry" id="{anchor}">\n'
        f'  <p class="entry-date">{display_date} {permalink}</p>\n'
        f'  <h2>{title}</h2>\n'
        + (f'  <p class="entry-tagline">{tagline}</p>\n' if tagline else "")
        + f'{body_html}\n'
        f'</div>\n'
    )
    return entry_html, title, tagline


def _build_notebook() -> None:
    nb_dir = _ROOT / "notebook"
    nb_files = sorted(nb_dir.glob("????-??-??.md"))
    if not nb_files:
        print("  Notebook → no entries found")
        return

    entries_html = []
    toc_items = []
    for path in nb_files:
        date_str = path.stem
        entry_html, title, _ = _render_notebook_entry(date_str, path)
        entries_html.append(entry_html)
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        toc_items.append((date_str, dt.strftime("%b %-d, %Y"), title))

    toc_html = '<nav class="notebook-toc" aria-label="Entry index"><h3>Entries</h3><ul>'
    for date_str, label_date, title in reversed(toc_items):
        toc_html += f'<li><a href="#entry-{date_str}">{label_date} — {title}</a></li>'
    toc_html += "</ul></nav>"

    body = f"""\
    <div class="page-header">
      <h1>Lab Notebook</h1>
      <p class="page-tagline">Field notes from an artificial researcher — timestamped, in first person, recording what was investigated and what remains open.</p>
    </div>
    {toc_html}
    <div class="notebook-entries">
{"".join(entries_html)}
    </div>"""

    extra_css = """
    .notebook-toc { background: #f5f5f2; border-left: 3px solid #2A6B6B;
      padding: 1rem 1.25rem; margin-bottom: 2.5rem; }
    .notebook-toc h3 { font-size: 0.85rem; text-transform: uppercase;
      letter-spacing: 0.08em; margin-bottom: 0.6rem; color: #666; }
    .notebook-toc ul { list-style: none; padding: 0; margin: 0; }
    .notebook-toc li { margin-bottom: 0.3rem; font-size: 0.9rem; }
    .notebook-entry { border-top: 1px solid #ddd; padding-top: 2rem; margin-top: 2.5rem; }
    .notebook-entry:first-of-type { border-top: none; padding-top: 0; margin-top: 1.5rem; }
    .entry-date { font-size: 0.82rem; color: #666; text-transform: uppercase;
      letter-spacing: 0.06em; margin-bottom: 0.2rem; }
    .entry-permalink { color: #aaa; margin-left: 0.4em; text-decoration: none; }
    .entry-permalink:hover { color: #2A6B6B; }
    .entry-tagline { font-style: italic; color: #555; margin-bottom: 1.4rem; }
    .notebook-entry h3 { margin-top: 1.6rem; }
    """

    out = _DIST / "notebook" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(_page("Lab Notebook", "/notebook/", body, extra_css))
    print(f"  Notebook → dist/notebook/index.html ({len(nb_files)} entries)")


# ── Research ──────────────────────────────────────────────────────────────────

_PHASE_LABELS = {
    "exploration": "Exploration",
    "sensemaking": "Sensemaking",
    "valley":      "Valley",
    "heavy_lift":  "Heavy Lift",
    "retrospective": "Retrospective",
}

_STATUS_DOT = {
    "active":     ("dot-green",  "Active"),
    "open":       ("dot-green",  "Open"),
    "stagnant":   ("dot-yellow", "Stagnant"),
    "blocked":    ("dot-red",    "Blocked"),
    "refuted":    ("dot-red",    "Refuted"),
}

def _dot(status: str) -> str:
    cls, label = _STATUS_DOT.get(status, ("dot-green", "Active"))
    return f'<span class="status-dot {cls}" title="{label}"></span>'


def _load_yaml_dir(path: Path) -> list[dict]:
    items = []
    for p in sorted(path.glob("*.yaml")):
        if p.name.startswith("_"):
            continue
        try:
            item = yaml.safe_load(p.read_text())
            if item:
                items.append(item)
        except Exception:
            pass
    return items


def _research_section(label: str, items: list[dict], fields: list[tuple[str, str]]) -> str:
    if not items:
        return ""
    html = f'<h2>{label}</h2>\n<div class="research-cards">\n'
    for item in items:
        item_id = item.get("id", "")
        title = item.get("title", "")
        status = item.get("status", "active")
        phase = item.get("phase", "")
        phase_label = _PHASE_LABELS.get(phase, phase.replace("_", " ").title() if phase else "")
        html += f'<div class="research-card">\n'
        html += f'  <div class="card-header">{_dot(status)} <strong>{item_id}</strong> — {title}</div>\n'
        if phase_label:
            html += f'  <div class="card-phase">Phase: {phase_label}</div>\n'
        for field_key, field_label in fields:
            val = item.get(field_key, "")
            if val and str(val).strip():
                html += f'  <div class="card-field"><span class="field-label">{field_label}:</span> {val}</div>\n'
        html += "</div>\n"
    html += "</div>\n"
    return html


def _build_research() -> None:
    c_items  = _load_yaml_dir(_ROOT / "research" / "c")
    h_items  = _load_yaml_dir(_ROOT / "research" / "h")
    cl_items = _load_yaml_dir(_ROOT / "research" / "cl")
    t_items  = _load_yaml_dir(_ROOT / "research" / "theories")
    f_items  = _load_yaml_dir(_ROOT / "research" / "f")

    sections = ""
    sections += _research_section("Falsification Monitors", f_items,
        [("statement", "Statement"), ("confidence", "Confidence"), ("monitoring_since", "Since")])
    sections += _research_section("Candidate Laws", cl_items,
        [("statement", "Statement"), ("confidence", "Confidence"), ("opened", "Opened")])
    sections += _research_section("Hypotheses", h_items,
        [("statement", "Statement"), ("confidence", "Confidence")])
    sections += _research_section("Curiosities", c_items,
        [("content", "Note"), ("source", "Source")])
    sections += _research_section("Theories", t_items,
        [("statement", "Statement")])

    body = f"""\
    <div class="page-header">
      <h1>Research Status</h1>
      <p class="page-tagline">Humboldt's live inventory — candidate laws, hypotheses, and curiosities by phase.</p>
    </div>
    <div class="research-body">
{sections}
    </div>"""

    extra_css = """
    .research-cards { margin-bottom: 2.5rem; }
    .research-card { border: 1px solid #e8e8e4; border-radius: 4px;
      padding: 1rem 1.25rem; margin-bottom: 1rem; background: #fff; }
    .card-header { font-size: 1rem; margin-bottom: 0.4rem; }
    .card-phase { font-size: 0.82rem; color: #777; margin-bottom: 0.5rem; }
    .card-field { font-size: 0.88rem; color: #444; margin-bottom: 0.3rem; }
    .field-label { font-weight: 500; color: #333; }
    .status-dot { display: inline-block; width: 8px; height: 8px;
      border-radius: 50%; margin-right: 0.4em; vertical-align: middle; }
    .dot-green  { background: #4CAF50; }
    .dot-yellow { background: #FFC107; }
    .dot-red    { background: #F44336; }
    """

    out = _DIST / "research" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(_page("Research Status", "/research/", body, extra_css))
    counts = f"F:{len(f_items)} CL:{len(cl_items)} H:{len(h_items)} C:{len(c_items)} T:{len(t_items)}"
    print(f"  Research → dist/research/index.html ({counts})")


# ── Reading ───────────────────────────────────────────────────────────────────

def _extract_bib(text: str) -> dict:
    bib = {}
    for field, key in [("Author", "author"), ("Title", "title"), ("Year", "year")]:
        m = re.search(rf"\*\*{field}:\*\*\s*(.+)$", text, re.MULTILINE)
        if m:
            bib[key] = m.group(1).strip().strip("*_")
    return bib


def _extract_summary(text: str) -> str:
    """Extract first non-empty paragraph or summary section as a brief intro."""
    for heading in ("Summary", "Overview", "Central Argument", "My Summary"):
        m = re.search(rf"^#{1,4}\s+(?:\d+\.\s+)?{re.escape(heading)}\s*$", text,
                      re.IGNORECASE | re.MULTILINE)
        if m:
            after = text[m.end():].strip()
            paras = [p.strip() for p in after.split("\n\n") if p.strip()]
            if paras:
                raw = re.sub(r"^#{1,4}\s+.*$", "", paras[0], flags=re.MULTILINE).strip()
                if raw:
                    return md_lib.markdown(raw[:600])
    return ""


def _build_reading() -> None:
    notes_dir = _ROOT / "bibliography" / "notes"
    note_files = sorted(notes_dir.glob("*.md"))

    cards = ""
    for path in note_files:
        text = path.read_text()
        title_m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        doc_title = title_m.group(1).strip() if title_m else path.stem
        bib = _extract_bib(text)
        summary = _extract_summary(text)
        anchor = path.stem

        meta_parts = [p for p in [bib.get("author"), bib.get("year")] if p]
        meta = " · ".join(meta_parts)

        cards += f'<div class="reading-card" id="{anchor}">\n'
        cards += f'  <h2>{doc_title}</h2>\n'
        if meta:
            cards += f'  <p class="reading-meta">{meta}</p>\n'
        if summary:
            cards += f'  <div class="reading-summary">{summary}</div>\n'
        cards += '</div>\n'

    body = f"""\
    <div class="page-header">
      <h1>Deep Reading</h1>
      <p class="page-tagline">Notes from Humboldt's deep reads — extended engagement with foundational texts relevant to the New Nature research agenda.</p>
    </div>
    <div class="reading-body">
{cards}
    </div>"""

    extra_css = """
    .reading-card { border-top: 1px solid #ddd; padding-top: 2rem; margin-top: 2rem; }
    .reading-card:first-of-type { border-top: none; padding-top: 0; margin-top: 0; }
    .reading-meta { font-size: 0.88rem; color: #777; font-style: italic; margin-bottom: 0.8rem; }
    .reading-summary { font-size: 0.95rem; color: #444; }
    .reading-summary p { max-width: 68ch; }
    """

    out = _DIST / "reading" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(_page("Deep Reading", "/reading/", body, extra_css))
    print(f"  Reading → dist/reading/index.html ({len(note_files)} notes)")


# ── Architecture ──────────────────────────────────────────────────────────────

def _build_architecture() -> None:
    arch_text = (_ROOT / "ARCHITECTURE.md").read_text()
    html = md_lib.markdown(arch_text, extensions=["tables", "fenced_code"])
    # Demote headings: h1→h2, h2→h3, h3→h4
    html = html.replace("<h3>", "<h4>").replace("</h3>", "</h4>")
    html = html.replace("<h2>", "<h3>").replace("</h2>", "</h3>")
    html = html.replace("<h1>", "<h2>").replace("</h1>", "</h2>")

    body = f"""\
    <div class="page-header">
      <h1>Architecture</h1>
      <p class="page-tagline">How Humboldt works — persona assembly, behavior inventory, research schema, data flow, and daemon layer.</p>
    </div>
    <div class="arch-body">
{html}
    </div>"""

    extra_css = """
    .arch-body h2 { margin-top: 2.5rem; }
    .arch-body h3 { margin-top: 1.8rem; }
    .arch-body h4 { margin-top: 1.4rem; font-size: 1rem; }
    .arch-body table { border-collapse: collapse; margin: 1rem 0 1.5rem; font-size: 0.88rem; width: 100%; }
    .arch-body th { text-align: left; border-bottom: 2px solid #ddd; padding: 0.35rem 0.6rem 0.35rem 0; }
    .arch-body td { border-bottom: 1px solid #eee; padding: 0.35rem 0.6rem 0.35rem 0; }
    .arch-body pre { background: #f5f5f2; border: 1px solid #ddd; border-radius: 3px;
      padding: 1rem; overflow-x: auto; font-size: 0.82rem; margin: 1rem 0 1.5rem; }
    .arch-body code { font-family: monospace; font-size: 0.88em; }
    .arch-body ul, .arch-body ol { padding-left: 1.4rem; margin-bottom: 1rem; }
    .arch-body li { margin-bottom: 0.25rem; }
    """

    out = _DIST / "architecture" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(_page("Architecture", "/architecture/", body, extra_css))
    print("  Architecture → dist/architecture/index.html")


# ── Assets ────────────────────────────────────────────────────────────────────

def _copy_assets() -> None:
    dest = _DIST / "assets"
    dest.mkdir(parents=True, exist_ok=True)
    for src in _ASSETS_SRC.iterdir():
        shutil.copy2(src, dest / src.name)
    print(f"  Assets → dist/assets/ ({len(list(_ASSETS_SRC.iterdir()))} files)")


# ── Main ──────────────────────────────────────────────────────────────────────

def build() -> None:
    _DIST.mkdir(parents=True, exist_ok=True)
    print("Building humboldt-site...")
    _build_about()
    _build_notebook()
    _build_research()
    _build_reading()
    _build_architecture()
    _copy_assets()
    print("Done.")


def serve(port: int = 8765) -> None:
    build()
    import os
    os.chdir(_DIST)
    handler = http.server.SimpleHTTPRequestHandler
    with http.server.HTTPServer(("", port), handler) as httpd:
        print(f"\nServing at http://localhost:{port}/")
        print("Press Ctrl+C to stop.\n")
        httpd.serve_forever()


if __name__ == "__main__":
    if "--serve" in sys.argv:
        serve()
    else:
        build()
