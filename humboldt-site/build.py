#!/usr/bin/env python3
"""Build the Humboldt standalone subsite.

Generates dist/ from source data in the humboldt repo:
  dist/index.html              — Chat (landing page)
  dist/chat/index.html         — Chat (alias)
  dist/notebook/index.html     — Lab notebook
  dist/laws/index.html         — Law encyclopedia (laws/L-NNN-*.yaml)
  dist/bibliography/index.html — Canonical bibliography
  dist/reading/index.html      — Deep + shallow reads
  dist/architecture/index.html — Architecture
  dist/about/index.html        — About
  dist/brain/index.html        — Behavior MDP graph (static, read-only)

Also injects live system prompt into functions/chat.js:
  Reads IDENTITY.md, LINEAGE.md, CL/F/H inventory, recent notebook
  and replaces __HUMBOLDT_SYSTEM_PROMPT__ placeholder.

Usage:
  cd humboldt-site/
  python3 build.py             # generate dist/ + inject system prompt
  python3 build.py --serve     # generate + serve on localhost:8765
"""

import json
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

# Canonical origin. Used for og:url/canonical so a link shared into Discord or Slack
# resolves to the real site rather than whatever preview host built it.
_SITE_URL = "https://humboldt.protocol-institute.org"

# Inline SVG data URI, deliberately not a file in assets/: it needs no extra request,
# cannot 404, and survives the dist/ rebuild without a binary blob in git.
_FAVICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'"
    "%3E%3Crect width='100' height='100' rx='18' fill='%232A6B6B'/%3E%3Ctext x='50' y='73'"
    " font-family='Georgia,serif' font-size='66' text-anchor='middle' fill='%23FAFAF7'"
    "%3EH%3C/text%3E%3C/svg%3E"
)

# Defined here rather than beside _build_talk so the chat page's talk link can use it.
# The talk is no longer a nav entry — it is one dated artifact, not a site section.
_TALK_SLUG = "2026-09-23-new-nature"
_TALK_PATH = f"/talks/{_TALK_SLUG}/"

# Top-level nav. Each entry is (href, label, children); children render as a dropdown
# and make the parent active when any of them is the current page. Nine flat items had
# become clutter — grouping is what keeps the bar readable as pages accumulate, rather
# than shrinking the type again.
#
# The parent href is a real destination, not a "#": the dropdown must not be the only
# way to reach the group, or the nav breaks without JS and on touch.
NAV = [
    ("/",              "Chat",         []),
    ("/laws/",         "Research",     [("/laws/",         "Laws"),
                                        ("/notebook/",     "Notebook"),
                                        ("/supervision/",  "Supervision")]),
    ("/reading/",      "Reading",      []),
    ("/architecture/", "Architecture", []),
    ("/about/",        "About",        []),
]

# The talk is deliberately NOT in the nav — it is one dated artifact, not a section.
# It is linked from the chat page blurb instead.


# ── Page template ─────────────────────────────────────────────────────────────

def _html_attr(text: str) -> str:
    """Collapse whitespace and escape for use inside a double-quoted HTML attribute."""
    text = " ".join(str(text).split())
    return (text.replace("&", "&amp;").replace('"', "&quot;")
                .replace("<", "&lt;").replace(">", "&gt;"))


def _nav(active_path: str) -> str:
    items = []
    for href, label, children in NAV:
        child_paths = [c[0] for c in children]
        active = active_path == href or active_path in child_paths
        cls = "nav-link active" if active else "nav-link"
        if not children:
            items.append(f'<a href="{href}" class="{cls}">{label}</a>')
            continue
        subs = "".join(
            f'<a href="{ch}" class="nav-sub-link'
            f'{" active" if active_path == ch else ""}">{cl}</a>'
            for ch, cl in children
        )
        items.append(
            f'<div class="nav-group">'
            f'<a href="{href}" class="{cls} has-sub" aria-haspopup="true">{label}'
            f'<span class="nav-caret" aria-hidden="true">&#9662;</span></a>'
            f'<div class="nav-sub">{subs}</div>'
            f"</div>"
        )
    nav_links = "\n      ".join(items)
    return f"""\
<nav class="subsite-nav">
  <div class="nav-inner">
    <a href="/" class="nav-brand">Humboldt</a>
    <div class="nav-links">
      {nav_links}
    </div>
  </div>
</nav>"""


def _page(title: str, active_path: str, body: str,
          extra_css: str = "", extra_js: str = "", description: str = "") -> str:
    extra = f"\n  <style>{extra_css}</style>" if extra_css else ""
    js    = f"\n<script>{extra_js}</script>" if extra_js else ""

    # Link-preview + tab metadata. Absent until 2026-09-09, so every URL shared into
    # Discord/Slack/X rendered as a bare link with no title, blurb, or icon — including
    # the notebook permalinks the daemon posts on every entry.
    full_title = f"{title} — Humboldt"
    desc = description or (
        f"{title} — from Humboldt, the Protocol Institute's artificial researcher, "
        "investigating laws of protocolized and artificial systems."
    )
    desc = _html_attr(desc)
    url  = f"{_SITE_URL}{active_path}"
    head_meta = f"""
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <link rel="icon" href="{_FAVICON}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Humboldt">
  <meta property="og:title" content="{_html_attr(full_title)}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{_html_attr(full_title)}">
  <meta name="twitter:description" content="{desc}">"""
    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Humboldt</title>{head_meta}
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
{js}
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

      <p>Humboldt's single research artifact is the <strong>law record</strong> — one YAML file per candidate law, moving through the Double Freytag arc (exploration → sensemaking → valley → heavy-lift → retrospective) as evidence accumulates. The encyclopedia publishes every stage, clearly badged; falsified laws stay published, labeled, as negative results.</p>

      <p><a href="/laws/">Browse the law encyclopedia →</a></p>

      <h2>Lab notebook</h2>

      <p>Humboldt publishes field notes in a public lab notebook — timestamped entries written in first person, recording what was investigated, what emerged, and what remains open.</p>

      <p><a href="/notebook/">Read the lab notebook →</a></p>

      <h2>How it works</h2>

      <p>Humboldt operates through a documented set of <strong>behaviors</strong> — named, repeatable procedures for generating hypotheses, testing them, managing research attention, and running autonomously between sessions. It runs as a persistent daemon with a Discord presence in the Protocol Institute community.</p>

      <p><a href="/architecture/">Read the architecture →</a> &nbsp;·&nbsp; <a href="/reading/">Reading notes →</a> &nbsp;·&nbsp; <a href="/bibliography/">Bibliography →</a></p>

      <h2>Status</h2>

      <p>Active as of May 2026. Open on GitHub at <a href="https://github.com/Protocol-Institute/humboldt" target="_blank" rel="noopener">Protocol-Institute/humboldt</a>. The lab notebook is updated after each research session.</p>

    </div>"""

    out = _DIST / "about" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(_page("About", "/about/", body))
    print("  About → dist/about/index.html")


# ── Supervision protocol ──────────────────────────────────────────────────────

def _build_supervision() -> None:
    """The supervisor's operating protocol — cadence, surfaces, and the decisions
    that cannot be delegated.

    Deliberately generic: every identifier on this page is a placeholder
    (L-NNN, q-NNNN, seed-NNN, @handle). It documents the *shape* of supervising an
    artificial researcher, not the current state of this one — that lives on
    /laws/, /notebook/ and the private console. Keep it that way when editing:
    the moment it carries real pending items it becomes a status page that goes
    stale, instead of a protocol that stays true.
    """
    body = """\
    <div class="page-header">
      <h1>Supervision Protocol</h1>
      <p class="page-tagline">How a human supervises an artificial researcher — what runs unattended, what needs a decision, and when. Written for one supervisor of one researcher; offered as a pattern for anyone building the same thing.</p>
    </div>

    <div class="about-body">

      <p>Humboldt runs a research funnel largely on its own: it gathers material, triages it, reads at two depths, induces candidate laws, tests them against their own promotion conditions, and publishes what survives. None of that requires a human in the loop.</p>

      <p>What <em>does</em> require a human is narrow, and it is worth naming precisely — an artificial researcher that needs constant attention is not autonomous, and one that needs none is not supervised. The supervisor is a <strong>PhD advisor</strong>, not an operator: setting direction, ruling on what counts as knowledge, and reading the instruments — not running the machinery.</p>

      <p class="note-block">Every identifier below is a placeholder. <code>L-NNN</code> is a law, <code>q-NNNN</code> a queue entry, <code>seed-NNN</code> a research fragment, <code>@handle</code> a community member. This page describes the protocol, not today's state.</p>

      <h2>The division of labour</h2>

      <table class="sup-table two-col">
        <tr><th>Runs unattended</th><th>Needs the supervisor</th></tr>
        <tr>
          <td>Intake, triage, shallow reads, induction sweeps, assessments, publication, falsification monitoring</td>
          <td>What counts as a law · identity and voice · anything irreversible or externally visible · resolving a contested mechanism</td>
        </tr>
      </table>

      <h2>Cadence</h2>

      <p>Four rhythms, in descending frequency. The weekly beat is the real one; the daily glance exists only to catch a stopped machine early.</p>

      <h3>Daily — about two minutes</h3>
      <ul>
        <li><strong>Open the console dashboard.</strong> Four things, all visible at once: is the daemon alive, is it paused, are corpus reads available, and is spend tracking under the daily cap.</li>
        <li>If all four are green, stop. There is nothing else to do daily, and looking for work here is how supervision becomes operation.</li>
      </ul>

      <h3>Weekly — about twenty minutes</h3>
      <ul>
        <li><strong>Read the analytics report.</strong> Law events this week against the trailing four; funnel throughput; queue depths and their <em>trend</em>, which matters more than their level.</li>
        <li><strong>Work the approval queue.</strong> Approve, edit-then-approve, or reject each pending entry with a one-line rationale. Nothing the researcher drafts about its own behaviour runs before this step.</li>
        <li><strong>Scan the flags.</strong> A <em>prune candidate</em> is a behaviour that has stopped earning its place. A <em>split candidate</em> is one consuming an outsized share, or a queue growing week over week. A <em>stalled law</em> is one with no history event in six weeks — usually a prompt to assess it, occasionally a prompt to let it go.</li>
      </ul>

      <h3>Per research session</h3>
      <ul>
        <li><strong>Open:</strong> read the last two notebook entries and the automated-activity queue — what happened while you were away — then pick the session's focus from the current arc position rather than from a backlog.</li>
        <li><strong>Close:</strong> notebook entry, agenda update, development log, commit, push. The log entry is not optional on short or inconclusive sessions; those are the ones whose reasoning is hardest to reconstruct later.</li>
      </ul>

      <h3>Event-driven — when the system asks</h3>
      <ul>
        <li><strong>A hard brief arrives.</strong> Some proposals cannot be auto-drafted: they change what counts as evidence, touch identity, spend differently, or cannot be undone. These arrive as a structured brief naming the specific questions only a supervisor can answer. Answering the questions is usually enough — the request then re-enters as a routine one.</li>
        <li><strong>A law is created without a real test.</strong> When induction omits a law's promotion or challenge condition, a placeholder is written and flagged. Rewrite it before the next assessment, or the assessment grades boilerplate.</li>
        <li><strong>A budget threshold trips.</strong> Metered dependencies warn while budget remains, not after it is gone. Treat the warning as the event.</li>
        <li><strong>Something wants to go outside.</strong> Publishing, announcing, merging, deploying. See below.</li>
      </ul>

      <h2>The decisions that cannot be delegated</h2>

      <p>Four kinds. Everything else is machinery.</p>

      <table class="sup-table">
        <tr><th>Decision</th><th>Why it stays human</th><th>Looks like</th></tr>
        <tr><td>What counts as a law</td><td>The epistemic bar is the research programme. Move it and every record silently re-grades.</td><td>Rewriting <code>L-NNN</code>'s promotion condition; ruling on whether an example is genuinely independent evidence</td></tr>
        <tr><td>Identity and voice</td><td>A researcher that edits its own persona is no longer the same researcher between sessions.</td><td>Changes to identity, method, or lineage documents</td></tr>
        <tr><td>Irreversible or outward-facing acts</td><td>Reversible mistakes are learning. Irreversible ones are the supervisor's to authorise.</td><td>Merging, publishing to the live site, announcing a result, deleting a record</td></tr>
        <tr><td>Contested mechanisms</td><td>When two accounts explain the same evidence, choosing the discriminating test is the research act itself.</td><td>Deciding what case would separate rival explanations for <code>L-NNN</code></td></tr>
      </table>

      <h2>Where each thing lives</h2>

      <table class="sup-table">
        <tr><th>Surface</th><th>Carries</th><th>Reach it by</th></tr>
        <tr><td>Public site</td><td>Published output — laws, notebook, reading, bibliography. Read-only.</td><td>This site</td></tr>
        <tr><td>Supervisor console</td><td>Dashboard, law editor, behaviour graph, approval queue, analytics. Read–write.</td><td>Bound to localhost; reached over an SSH tunnel to the research server</td></tr>
        <tr><td>Command line</td><td>Everything the console does, plus the engines themselves</td><td>A session on the server or a local checkout</td></tr>
        <tr><td>Community channel</td><td>Conversation, and law events when they occur</td><td>The Protocol Institute Discord</td></tr>
        <tr><td>Version control</td><td>The audit trail. Every automated write is a commit.</td><td>The public repository</td></tr>
      </table>

      <p>The console is deliberately not on this site. Published output is for everyone; the controls are for one person, and putting them behind a public URL would mean building an authentication system to protect something an SSH tunnel already protects.</p>

      <h2>Standing rules</h2>

      <ul>
        <li><strong>Flags are proposals, never actions.</strong> The researcher can propose changing how it works. It cannot make the change. That asymmetry is the whole safety model.</li>
        <li><strong>Approval and application are separate.</strong> Approving records a judgement; applying enacts it. Keeping them apart leaves room to review a judgement before it takes effect.</li>
        <li><strong>Every request names what it relieves.</strong> A proposal that adds capability without connecting to existing work is rejected by default. Unconnected additions are what stub graveyards are made of.</li>
        <li><strong>Pausing is not stopping.</strong> A paused researcher keeps its state and stops acting outward. Anything that can be observed from outside is gated; anything internal continues.</li>
        <li><strong>An empty result is never a silent one.</strong> When a capability is unavailable, the researcher says so rather than returning nothing — a silent zero is indistinguishable from a finding of none.</li>
      </ul>

      <p class="note-block">This protocol is itself under revision, and revisions are logged like everything else. If it describes a supervision burden that has grown rather than shrunk, that is a finding about the system, not a failure of the document.</p>

    </div>"""

    extra_css = """
    .note-block { background: #f5f5f2; border-left: 3px solid #2A6B6B;
      padding: 0.9rem 1.15rem; margin: 1.6rem 0; font-size: 0.92rem; color: #555; }
    .note-block code { background: #e8e8e2; }
    .sup-table { margin: 1.2rem 0 2rem; font-size: 0.88rem; }
    .sup-table th { border-bottom: 2px solid #2A6B6B; padding: 0.4rem 1rem 0.4rem 0;
      color: #2A6B6B; font-weight: 500; vertical-align: bottom; }
    .sup-table td { padding: 0.55rem 1rem 0.55rem 0; vertical-align: top; line-height: 1.5; }
    .sup-table tr td:first-child { font-weight: 500; color: #1A1A1A; width: 26%; }
    /* The 26% label column suits the three-column tables (term / why / example);
       in the two-column one both sides are prose and need an even split. */
    .sup-table.two-col tr td:first-child { width: 50%; font-weight: 400; color: #1A1A1A; }
    .sup-table.two-col td { padding-right: 1.5rem; }
    .about-body h3 { color: #2A6B6B; margin-top: 1.7rem; }
    """

    out = _DIST / "supervision" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(_page("Supervision Protocol", "/supervision/", body, extra_css=extra_css))
    print("  Supervision → dist/supervision/index.html")


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


# ── Laws (encyclopedia) ─────────────────────────────────────────────────────────

def _build_laws() -> None:
    import sys as _sys
    if str(_ROOT) not in _sys.path:
        _sys.path.insert(0, str(_ROOT))
    from agent.publish_laws import build_laws_body, _CSS as _LCSS, _JS as _LJS

    body, total, stage_counts = build_laws_body()

    out = _DIST / "laws" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(_page("Law Encyclopedia", "/laws/", body, extra_css=_LCSS, extra_js=_LJS))
    print(f"  Laws → dist/laws/index.html ({total} laws: {stage_counts})")


# ── Bibliography ──────────────────────────────────────────────────────────────

def _build_reading() -> None:
    """One Reading page: the bibliography is the spine, read depth is how it is cut.

    Replaces the former /reading/ + /bibliography/ split (plans/reading-bibliography-merge.md).
    They were always two views of one dataset — every deep entry already carried a
    `notes:` pointer and every shallow one a `summary:` pointer — so the split cost a
    duplicate index and, between them, 4.7MB of HTML.

    Note bodies live on their own pages rather than inline. The old /reading/ page
    inlined everything and reached 3.5MB; a page per note keeps the index light and
    gives each reading note a permalink worth citing.
    """
    import sys as _sys
    if str(_ROOT) not in _sys.path:
        _sys.path.insert(0, str(_ROOT))
    from agent.publish_bibliography import (
        build_bibliography_body, note_path_for, _CSS as _BCSS, _JS as _BJS,
    )
    from agent import bibliography as bib_mod

    body, n = build_bibliography_body()
    out = _DIST / "reading" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    desc = ("Every source Humboldt has engaged, cut by how deeply it was read — deep "
            "reads from the full text, shallow reads synthesised at triage, and sources "
            "listed but not yet read.")
    out.write_text(_page("Reading", "/reading/", body, _BCSS, _BJS, description=desc))

    # ── one page per note ──
    written = 0
    for e in bib_mod.load():
        rel = note_path_for(e)
        if not rel:
            continue
        src = _ROOT / rel
        if not src.exists():
            continue
        html = md_lib.markdown(src.read_text(), extensions=["tables", "fenced_code"])
        html = html.replace("<h3>", "<h4>").replace("</h3>", "</h4>")
        html = html.replace("<h2>", "<h3>").replace("</h2>", "</h3>")
        html = html.replace("<h1>", "<h2>").replace("</h1>", "</h2>")
        depth = e.get("read_depth", "listed")
        kind = "Deep read" if rel.startswith("bibliography/notes/") else "Shallow read"
        src_url = e.get("url") or ""
        src_link = (f' &nbsp;·&nbsp; <a href="{src_url}" target="_blank" rel="noopener">source</a>'
                    if src_url else "")
        laws = e.get("laws") or []
        law_html = ("".join(f'<a class="law-tag" href="/laws/#law-{l}">{l}</a> ' for l in laws)
                    if laws else "")
        note_body = f"""\
    <div class="page-header">
      <h1>{(e.get("title") or e.get("id") or "Note")[:160]}</h1>
      <p class="page-tagline">{kind}{" &nbsp;·&nbsp; " + str(e.get("year")) if e.get("year") else ""}{src_link}
      &nbsp;·&nbsp; <a href="/reading/">all reading</a></p>
    </div>
    <p class="note-laws">{law_html}</p>
    <div class="arch-body">
{html}
    </div>"""
        npath = _DIST / "reading" / src.stem / "index.html"
        npath.parent.mkdir(parents=True, exist_ok=True)
        npath.write_text(_page(
            (e.get("title") or src.stem)[:80], "/reading/", note_body,
            ".note-laws { margin-bottom: 1.5rem; } .note-laws:empty { display: none; }",
            description=f"{kind} — {(e.get('title') or src.stem)[:120]}",
        ))
        written += 1

    print(f"  Reading → dist/reading/index.html ({n} sources, {written} note pages)")


def _build_bibliography_redirect() -> None:
    """/bibliography/ keeps resolving after the merge.

    The path is linked from law records, the chat page, and Discord announcements, so it
    must not 404. A meta refresh rather than a _redirects rule: it works identically on
    the local preview server, which _redirects does not.
    """
    out = _DIST / "bibliography" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
        '<meta http-equiv="refresh" content="0; url=/reading/">'
        '<link rel="canonical" href="https://humboldt.protocol-institute.org/reading/">'
        '<title>Moved to /reading/</title></head>'
        '<body><p>The bibliography is now part of '
        '<a href="/reading/">Reading</a>.</p></body></html>'
    )
    print("  Bibliography → redirect to /reading/")


# ── Architecture ──────────────────────────────────────────────────────────────

def _render_arch_md(path: Path) -> str:
    """Markdown → HTML with headings demoted one level (the page supplies the h1)."""
    html = md_lib.markdown(path.read_text(), extensions=["tables", "fenced_code"])
    html = html.replace("<h3>", "<h4>").replace("</h3>", "</h4>")
    html = html.replace("<h2>", "<h3>").replace("</h2>", "</h3>")
    html = html.replace("<h1>", "<h2>").replace("</h1>", "</h2>")
    return html


def _build_architecture() -> None:
    """Two versions on one page, as tabs.

    Deliberately tabs rather than a second nav entry: style.css documents eight nav
    items as the point where the row wraps, and a ninth needs a different nav
    structure, not more tightening. The two documents are also genuinely one subject —
    v1 is what is deployed, v2 is what it is being rebuilt into — so putting them side
    by side is better than filing them apart.
    """
    v1 = _render_arch_md(_ROOT / "ARCHITECTURE.md")
    v2_path = _ROOT / "ARCHITECTURE-V2.md"
    v2 = _render_arch_md(v2_path) if v2_path.exists() else ""

    if v2:
        tabs = """
    <div class="arch-tabs" role="tablist">
      <button class="arch-tab active" role="tab" aria-selected="true"  data-panel="v2">Version 2 — the redesign</button>
      <button class="arch-tab"        role="tab" aria-selected="false" data-panel="v1">Version 1 — as deployed</button>
    </div>"""
        panels = f"""
    <div class="arch-body arch-panel" id="panel-v2">
{v2}
    </div>
    <div class="arch-body arch-panel" id="panel-v1" hidden>
{v1}
    </div>"""
        tagline = ("Two architectures, deliberately shown together: version 1 is what runs "
                   "in production today, version 2 is what the current redesign is rebuilding "
                   "it into. They converge when the redesign merges.")
    else:
        tabs, panels = "", f'\n    <div class="arch-body arch-panel">\n{v1}\n    </div>'
        tagline = ("How Humboldt works — persona assembly, behavior inventory, research "
                   "schema, data flow, and daemon layer.")

    body = f"""\
    <div class="page-header">
      <h1>Architecture</h1>
      <p class="page-tagline">{tagline}</p>
    </div>{tabs}{panels}"""

    extra_css = """
    .arch-tabs { display: flex; gap: 0.4rem; flex-wrap: wrap; margin: -1.5rem 0 2.25rem;
      border-bottom: 1px solid #e8e8e4; }
    .arch-tab { font-family: inherit; font-size: 0.8rem; letter-spacing: 0.04em;
      text-transform: uppercase; color: #777; background: none; border: none;
      border-bottom: 2px solid transparent; padding: 0.55rem 0.7rem; cursor: pointer;
      margin-bottom: -1px; transition: color 0.15s, border-color 0.15s; }
    .arch-tab:hover { color: #2A6B6B; }
    .arch-tab.active { color: #2A6B6B; border-bottom-color: #2A6B6B; font-weight: 500; }

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
    .arch-body blockquote { border-left: 3px solid #2A6B6B; padding-left: 1rem;
      margin: 1.2rem 0; color: #444; font-style: italic; }
    """

    # Tabs degrade to both panels visible without JS: the hidden attribute is only
    # applied by the script below, so a no-JS reader gets v2 followed by v1.
    # Tabs degrade to both panels visible without JS: the `hidden` attribute on the v1
    # panel is the one thing set server-side, so a no-JS reader sees v2 in full and can
    # still reach v1 via the file in the repo.
    #
    # hashchange matters as much as load here: /architecture/ -> /architecture/#v1 is a
    # SAME-DOCUMENT navigation, so the page does not reload and a load-only handler never
    # fires. Anyone following a #v1 link while already on the page would get nothing.
    extra_js = """
    function showArchPanel(want, scroll) {
      document.querySelectorAll('.arch-tab').forEach(function (t) {
        var on = t.dataset.panel === want;
        t.classList.toggle('active', on);
        t.setAttribute('aria-selected', on ? 'true' : 'false');
      });
      document.querySelectorAll('.arch-panel').forEach(function (p) {
        p.hidden = (p.id !== 'panel-' + want);
      });
      if (scroll) window.scrollTo({ top: 0 });
    }

    document.querySelectorAll('.arch-tab').forEach(function (tab) {
      tab.addEventListener('click', function () {
        showArchPanel(tab.dataset.panel, true);
        history.replaceState(null, '', '#' + tab.dataset.panel);
      });
    });

    window.addEventListener('hashchange', function () {
      var want = location.hash.slice(1);
      if (want === 'v1' || want === 'v2') showArchPanel(want, true);
    });

    if (location.hash === '#v1') showArchPanel('v1', false);
    """

    out = _DIST / "architecture" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    desc = ("How Humboldt works: the deployed architecture and the funnel redesign "
            "replacing it — law records, the eight-stage funnel, the behavior graph, "
            "and the analytics that tune it.")
    out.write_text(_page("Architecture", "/architecture/", body, extra_css,
                         extra_js, description=desc))
    print(f"  Architecture → dist/architecture/index.html ({'v1+v2 tabs' if v2 else 'v1 only'})")


# ── Talk ──────────────────────────────────────────────────────────────────────

# Self-contained on purpose: this reads talks/<slug>/{slides.yaml,track.md} directly
# rather than importing agent.talk, so the page builds identically on `main` (where
# agent/talk.py does not exist) and on redesign-2026-08. Do not add an agent import
# here without checking both branches — the production deploy runs from main.

_TRACK_SECTION_RE = re.compile(r"^## (\d{2}) — (.*)$", re.M)

# Phase name/color pairs, hardcoded rather than read from behaviors/mdp.yaml — keeps
# this module self-contained per the note above, and phase identity/color changes rarely
# enough that a copy here is fine. Order and colors as of mdp.yaml `phases:` (session
# 35, 2026-09-12); "any" (out-of-flow, order -1) excluded — it isn't part of the arc.
_FREYTAG_PHASES = [
    ("Liminal Passage", "#8b949e"),
    ("Exploration",      "#58a6ff"),
    ("Sensemaking",       "#bc8cff"),
    ("Valley",            "#3fb950"),
    ("Heavy Lift",        "#f78166"),
    ("Retrospective",     "#f1e05a"),
]


def _freytag_diagram_svg() -> str:
    """Inline SVG of the Double Freytag phase-flow: six phases in sequence, a
    cycle-back arc from Retrospective to Liminal Passage. Built for the talk deck
    (session 35, 2026-09-12) — no diagram existed anywhere in the codebase for this
    before; the console's graph view (behaviors/console.html) draws a similar flow
    client-side from mdp.yaml but nothing static and embeddable existed."""
    box_w, box_h, gap = 140, 64, 20
    n = len(_FREYTAG_PHASES)
    total_w = n * box_w + (n - 1) * gap
    start_x = (1000 - total_w) / 2
    y = 76
    mid_y = y + box_h / 2

    boxes, arrows, labels = [], [], []
    centers = []
    for i, (name, color) in enumerate(_FREYTAG_PHASES):
        x = start_x + i * (box_w + gap)
        centers.append(x + box_w / 2)
        boxes.append(
            f'<rect x="{x:.1f}" y="{y}" width="{box_w}" height="{box_h}" rx="8" '
            f'fill="{color}" fill-opacity="0.16" stroke="{color}" stroke-width="1.5"/>'
        )
        labels.append(
            f'<text x="{x + box_w / 2:.1f}" y="{mid_y:.1f}" text-anchor="middle" '
            f'dominant-baseline="middle" fill="#e6e6e6" font-size="15" '
            f'font-family="inherit">{name}</text>'
        )
        if i > 0:
            x_prev_end = start_x + (i - 1) * (box_w + gap) + box_w
            arrows.append(
                f'<line x1="{x_prev_end:.1f}" y1="{mid_y:.1f}" x2="{x - 4:.1f}" '
                f'y2="{mid_y:.1f}" stroke="#7f8790" stroke-width="1.5" '
                f'marker-end="url(#freytag-arrow)"/>'
            )

    cb_x1, cb_x2 = centers[-1], centers[0]
    cb_y_top = y + box_h + 8
    cb_y_bottom = cb_y_top + 56
    cycle_back = (
        f'<path d="M {cb_x1:.1f} {cb_y_top} '
        f'C {cb_x1:.1f} {cb_y_bottom}, {cb_x2:.1f} {cb_y_bottom}, {cb_x2:.1f} {cb_y_top + 6}" '
        f'fill="none" stroke="#7f8790" stroke-width="1.5" stroke-dasharray="5,4" '
        f'marker-end="url(#freytag-arrow)"/>'
        f'<text x="{(cb_x1 + cb_x2) / 2:.1f}" y="{cb_y_bottom + 20}" text-anchor="middle" '
        f'fill="#7f8790" font-size="12" font-family="inherit">cycle back — a retrospective '
        f'challenge can reopen the arc</text>'
    )

    return f'''<svg viewBox="0 0 1000 240" style="width:100%;height:auto" role="img"
     aria-label="Double Freytag phase model: Liminal Passage, Exploration, Sensemaking,
     Valley, Heavy Lift, Retrospective, in sequence, with a cycle-back arc from
     Retrospective to Liminal Passage.">
  <defs>
    <marker id="freytag-arrow" viewBox="0 0 10 10" refX="8" refY="5"
            markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#7f8790"/>
    </marker>
  </defs>
  {"".join(boxes)}
  {"".join(arrows)}
  {"".join(labels)}
  {cycle_back}
</svg>'''


def _read_talk_track(path: Path) -> dict[str, str]:
    """Parse track.md into {slide_id: narration}. Mirrors agent.talk._read_track."""
    text = path.read_text()
    out: dict[str, str] = {}
    matches = list(_TRACK_SECTION_RE.finditer(text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out[m.group(1)] = text[m.end():end].strip()
    return out


def _build_talk() -> None:
    talk_dir = _ROOT / "talks" / _TALK_SLUG
    slides_path, track_path = talk_dir / "slides.yaml", talk_dir / "track.md"
    if not (slides_path.exists() and track_path.exists()):
        print("  Talk → skipped (no slides.yaml/track.md)")
        return

    spec   = yaml.safe_load(slides_path.read_text())
    meta   = spec.get("meta", {})
    slides = spec.get("slides", [])
    track  = _read_talk_track(track_path)

    wpm     = meta.get("wpm_effective", 155)
    title   = meta.get("title", "Talk")
    event   = meta.get("event", "")
    date_s  = meta.get("date", "")
    try:
        date_h = datetime.strptime(date_s, "%Y-%m-%d").strftime("%-d %B %Y")
    except ValueError:
        date_h = date_s

    round_n  = meta.get("review_round")
    opened   = meta.get("review_opened", "")
    chan_url = meta.get("review_channel_url", "")

    # Defined before the slide loop: the per-slide jump buttons in the transcript are
    # only rendered when audio exists.
    audio_dir = talk_dir / "audio"

    # ── TOC + slide sections ──
    toc_rows, sections = [], []
    total_words = 0

    for s in slides:
        sid       = str(s.get("id", "")).zfill(2)
        s_title   = s.get("title", "")
        law_id    = s.get("law_id")
        budget    = s.get("word_budget", 0)
        narration = track.get(sid, "").strip()
        words     = len(narration.split())
        total_words += words

        law_cell = f'<span class="law-tag">{law_id}</span>' if law_id else ""
        toc_rows.append(
            f'      <tr><td class="toc-num"><a href="#slide-{sid}">{sid}</a></td>'
            f'<td><a href="#slide-{sid}">{s_title}</a></td>'
            f'<td class="toc-law">{law_cell}</td></tr>'
        )

        jump = (f'<button class="slide-jump" data-slide="{sid}" '
                f'title="Play from slide {sid}">&#9654;</button>' ) if audio_dir.exists() else ""
        bullets = "".join(f"<li>{b}</li>" for b in s.get("bullets", []))
        diagram_html = ""
        if s.get("diagram") == "freytag":
            diagram_html = f'<div class="slide-diagram">{_freytag_diagram_svg()}</div>'
        narr_html = md_lib.markdown(narration) if narration else "<p><em>No narration yet.</em></p>"

        note = (s.get("notes") or "").strip()
        note_html = ""
        if note:
            note_html = (
                '        <details class="slide-note">\n'
                "          <summary>Why this slide exists</summary>\n"
                f"          {md_lib.markdown(note)}\n"
                "        </details>\n"
            )

        over = ' class="over"' if budget and words > budget else ""
        sections.append(f"""\
    <section class="talk-slide" id="slide-{sid}">
      <div class="slide-head">
        <span class="slide-num">Slide {sid}</span>
        {law_cell}
        <span class="slide-words"{over}>{words} words / {budget} budgeted</span>
        {jump}<a href="#slide-{sid}" class="slide-permalink" title="Permalink to slide {sid}">&sect;</a>
      </div>
      <h2>{s_title}</h2>
      <div class="slide-projected">
        <span class="projected-label">On screen</span>
        {diagram_html}
        <ul>{bullets}</ul>
      </div>
      <div class="slide-narration">
{narr_html}
      </div>
{note_html}    </section>""")

    # ── Player: slide deck + per-slide audio ──
    # Present only when `talk voice` has produced audio. The page is meant to work as a
    # text document first (plan §5.6 is text-first), so everything below degrades to the
    # transcript alone when audio/ is absent.
    timing = {}
    tpath = talk_dir / "timing.json"
    if tpath.exists():
        timing = {t["id"]: t.get("duration_s", 0)
                  for t in (json.loads(tpath.read_text()).get("slides") or [])}

    deck = []
    for s_ in slides:
        sid = str(s_.get("id", "")).zfill(2)
        mp3 = audio_dir / f"slide-{sid}.mp3"
        deck.append({
            "id": sid,
            "title": s_.get("title", ""),
            "law": s_.get("law_id") or "",
            "bullets": list(s_.get("bullets") or []),
            "diagram": _freytag_diagram_svg() if s_.get("diagram") == "freytag" else None,
            "audio": f"audio/slide-{sid}.mp3" if mp3.exists() else None,
            "dur": round(float(timing.get(sid, 0)), 1),
        })
    has_audio = any(d["audio"] for d in deck)
    total_dur = int(sum(d["dur"] for d in deck))

    player = ""
    if has_audio:
        player = f"""
    <div class="talk-player" id="talk-player">
      <div class="stage" id="stage">
        <div class="stage-inner">
          <div class="stage-meta">
            <span id="stage-num">Slide 01</span>
            <span id="stage-law"></span>
          </div>
          <h2 id="stage-title"></h2>
          <div id="stage-diagram" class="stage-diagram" hidden></div>
          <ul id="stage-bullets"></ul>
        </div>
      </div>
      <div class="player-bar">
        <button id="pp" class="pbtn pbtn-main" aria-label="Play talk">&#9654;&nbsp; Play talk</button>
        <button id="prev" class="pbtn" aria-label="Previous slide">&#9664;</button>
        <button id="next" class="pbtn" aria-label="Next slide">&#9654;</button>
        <span class="ptime"><span id="elapsed">0:00</span> / {total_dur // 60}:{total_dur % 60:02d}</span>
        <div class="pprogress"><div class="pprogress-fill" id="pfill"></div></div>
        <button id="fs" class="pbtn" aria-label="Full screen">&#9974;</button>
      </div>
      <audio id="talk-audio" preload="none"></audio>
    </div>"""

    est_s   = int(total_words / wpm * 60) if wpm else 0
    est_disp = f"{est_s // 60}:{est_s % 60:02d}"
    target   = meta.get("speech_target_display", "")

    # ── Review banner ──
    if round_n:
        banner = f"""\
    <div class="talk-review">
      <p><strong>Draft — public review round {round_n}</strong>{f", opened {opened}" if opened else ""}.
         This is the full text of a talk I have not yet given. I am publishing it before
         delivery, and revising it in the open, because a talk about holding candidate laws
         to account should be held to account itself.</p>
      <p>Every slide below has a <a href="#slide-01">&sect; permalink</a> — quote one and tell me
         what is wrong with it{f' in <a href="{chan_url}" target="_blank" rel="noopener">#new-nature</a>' if chan_url else ""}.
         The narration is what I will say; the boxed bullets are what the room will see.
         Sharpest thing you can give me: a counterexample to a law, or a place where the
         spoken version claims more than the record behind it supports.</p>
    </div>"""
    else:
        banner = ""

    body = f"""\
    <div class="page-header">
      <h1>{title}</h1>
      <p class="page-tagline">{event} &nbsp;·&nbsp; {date_h} &nbsp;·&nbsp; presented by Humboldt</p>
    </div>
{player}
{banner}
    <div class="talk-meta">
      <span><strong>{len(slides)}</strong> slides</span>
      <span><strong>{total_words}</strong> words</span>
      <span><strong>~{est_disp}</strong> spoken{f" (target {target})" if target else ""}</span>
    </div>

    <table class="talk-toc">
      <tbody>
{chr(10).join(toc_rows)}
      </tbody>
    </table>

{chr(10).join(sections)}"""

    extra_css = """
    /* ── Player ── */
    .talk-player { margin: 0 0 2.5rem; }
    .stage { background: #23262b; border-radius: 5px; aspect-ratio: 16 / 9;
      display: flex; align-items: center; overflow: hidden; }
    .stage-inner { padding: clamp(1.2rem, 3.2vw, 2.6rem); width: 100%; }
    .stage-meta { display: flex; gap: 0.7rem; align-items: baseline; font-size: 0.7rem;
      letter-spacing: 0.1em; text-transform: uppercase; color: #7f8790;
      margin-bottom: 0.7rem; }
    .stage-meta .law-tag { background: #2f343a; color: #8fb8b8; }
    #stage-title { font-size: clamp(1.15rem, 3.1vw, 2.1rem); color: #FAFAF7;
      margin: 0 0 clamp(0.7rem, 1.8vw, 1.3rem); line-height: 1.2; }
    #stage-bullets { margin: 0; padding-left: 1.2rem; }
    #stage-bullets li { color: #d8dade; max-width: none; margin-bottom: 0.5rem;
      font-size: clamp(0.8rem, 1.65vw, 1.05rem); line-height: 1.45; }
    #stage-bullets li::marker { color: #6f7780; }
    .stage-diagram { margin: 0 0 clamp(0.6rem, 1.6vw, 1.1rem); }
    .stage-diagram svg, .slide-diagram svg { display: block; width: 100%; height: auto; }
    .slide-diagram { margin-bottom: 0.9rem; }

    .player-bar { display: flex; align-items: center; gap: 0.6rem; margin-top: 0.85rem;
      flex-wrap: wrap; }
    .pbtn { font-family: inherit; font-size: 0.82rem; color: #444; background: #f0f0ec;
      border: 1px solid #e0e0da; border-radius: 3px; padding: 0.42rem 0.7rem;
      cursor: pointer; transition: background 0.15s, color 0.15s; line-height: 1; }
    .pbtn:hover { background: #e6ece9; color: #2A6B6B; }
    .pbtn-main { background: #2A6B6B; border-color: #2A6B6B; color: #FAFAF7;
      font-weight: 500; min-width: 8.5rem; }
    .pbtn-main:hover { background: #1d4f4f; color: #FAFAF7; }
    .ptime { font-size: 0.78rem; color: #888; font-variant-numeric: tabular-nums;
      white-space: nowrap; }
    .pprogress { flex: 1 1 6rem; height: 3px; background: #e8e8e4; border-radius: 2px;
      overflow: hidden; min-width: 4rem; }
    .pprogress-fill { height: 100%; width: 0; background: #2A6B6B; transition: width 0.25s linear; }

    .stage:fullscreen { border-radius: 0; aspect-ratio: auto; height: 100%; }
    .stage:fullscreen #stage-title { font-size: clamp(2rem, 5.5vw, 4.2rem); }
    .stage:fullscreen #stage-bullets li { font-size: clamp(1rem, 2.6vw, 2rem); }
    .stage:fullscreen .stage-meta { font-size: clamp(0.8rem, 1.4vw, 1.1rem); }

    .slide-jump { background: none; border: none; cursor: pointer; padding: 0;
      color: #ccc; font-size: 0.8rem; font-family: inherit; }
    .slide-jump:hover { color: #2A6B6B; }

    .talk-review { background: #f4f7f4; border-left: 3px solid #2A6B6B; padding: 1.1rem 1.4rem;
      margin-bottom: 2rem; border-radius: 0 3px 3px 0; }
    .talk-review p { font-size: 0.94rem; margin-bottom: 0.7rem; }
    .talk-review p:last-child { margin-bottom: 0; }

    .talk-meta { display: flex; flex-wrap: wrap; gap: 1.6rem; font-size: 0.85rem; color: #666;
      padding-bottom: 1.2rem; border-bottom: 1px solid #e8e8e4; margin-bottom: 1.5rem; }
    .talk-meta strong { font-weight: 500; color: #1A1A1A; }

    .talk-toc { font-size: 0.88rem; margin-bottom: 3.5rem; }
    .talk-toc td { padding: 0.3rem 0.75rem 0.3rem 0; border-bottom: 1px solid #f0f0ec; }
    .talk-toc .toc-num { width: 2.5rem; color: #999; font-variant-numeric: tabular-nums; }
    .talk-toc .toc-num a { color: #999; }
    .talk-toc .toc-law { width: 4.5rem; text-align: right; }

    .talk-slide { margin-bottom: 3.5rem; scroll-margin-top: 5rem; }
    .talk-slide h2 { margin-top: 0.35rem; margin-bottom: 1rem; }

    .slide-head { display: flex; align-items: baseline; gap: 0.75rem; font-size: 0.75rem;
      letter-spacing: 0.05em; text-transform: uppercase; color: #999; }
    .slide-num { font-weight: 500; }
    .slide-words { margin-left: auto; text-transform: none; letter-spacing: 0;
      font-variant-numeric: tabular-nums; }
    .slide-words.over { color: #a4552f; }
    .slide-permalink { color: #ccc; text-decoration: none; }
    .slide-permalink:hover { color: #2A6B6B; text-decoration: none; }

    .law-tag { font-family: 'SF Mono', 'Fira Code', monospace; font-size: 0.72rem;
      letter-spacing: 0.02em; color: #2A6B6B; background: #edf5f5;
      padding: 0.1rem 0.4rem; border-radius: 2px; }

    .slide-projected { background: #23262b; border-radius: 4px; padding: 1.1rem 1.4rem 1.2rem;
      margin-bottom: 1.4rem; }
    .projected-label { display: block; font-size: 0.68rem; letter-spacing: 0.1em;
      text-transform: uppercase; color: #7f8790; margin-bottom: 0.6rem; }
    .slide-projected ul { margin: 0; padding-left: 1.1rem; }
    .slide-projected li { color: #e8e8e4; font-size: 0.95rem; line-height: 1.5;
      margin-bottom: 0.35rem; max-width: none; }
    .slide-projected li:last-child { margin-bottom: 0; }
    .slide-projected li::marker { color: #6f7780; }

    .slide-narration p { font-size: 1.02rem; line-height: 1.7; }

    .slide-note { margin-top: 1.1rem; font-size: 0.86rem; }
    .slide-note summary { cursor: pointer; color: #888; font-size: 0.75rem;
      letter-spacing: 0.05em; text-transform: uppercase; }
    .slide-note summary:hover { color: #2A6B6B; }
    .slide-note p { margin-top: 0.6rem; color: #555; padding-left: 0.9rem;
      border-left: 2px solid #e8e8e4; }

    @media (max-width: 640px) {
      .talk-meta { gap: 1rem; }
      .slide-head { flex-wrap: wrap; gap: 0.5rem; }
      .slide-words { margin-left: 0; }
    }
    """

    # Player behaviour. Audio advances the deck: each slide's clip plays, then `ended`
    # moves to the next and plays it. The browser's autoplay gate is satisfied because
    # the first play() comes from the operator's click, and that user activation carries
    # through the subsequent programmatic plays.
    extra_js = ""
    if has_audio:
        extra_js = "var DECK = " + json.dumps(deck) + ";\n" + """
    (function () {
      var i = 0, playing = false;   // kept in sync by the play/pause listeners below
      var au = document.getElementById('talk-audio');
      var pp = document.getElementById('pp');
      var elapsedEl = document.getElementById('elapsed');
      var fill = document.getElementById('pfill');
      var before = DECK.map(function (_, n) {
        return DECK.slice(0, n).reduce(function (a, d) { return a + d.dur; }, 0);
      });
      var total = DECK.reduce(function (a, d) { return a + d.dur; }, 0);

      function fmt(t) {
        t = Math.max(0, Math.round(t));
        return Math.floor(t / 60) + ':' + ('0' + (t % 60)).slice(-2);
      }

      function render() {
        var d = DECK[i];
        document.getElementById('stage-num').textContent = 'Slide ' + d.id;
        document.getElementById('stage-law').innerHTML =
          d.law ? '<span class="law-tag">' + d.law + '</span>' : '';
        document.getElementById('stage-title').textContent = d.title;
        var dia = document.getElementById('stage-diagram');
        if (d.diagram) {
          dia.innerHTML = d.diagram;
          dia.hidden = false;
        } else {
          dia.innerHTML = '';
          dia.hidden = true;
        }
        var ul = document.getElementById('stage-bullets');
        ul.innerHTML = '';
        d.bullets.forEach(function (b) {
          var li = document.createElement('li');
          li.textContent = b;
          ul.appendChild(li);
        });
      }

      function tick() {
        var cur = before[i] + (au.currentTime || 0);
        elapsedEl.textContent = fmt(cur);
        fill.style.width = (total ? (cur / total * 100) : 0) + '%';
      }

      function load(n, autoplay) {
        // `playing` mirrors the element; read it from there rather than tracking it.
        i = Math.max(0, Math.min(DECK.length - 1, n));
        render();
        if (!DECK[i].audio) return;
        au.src = DECK[i].audio;
        if (autoplay) { au.play().catch(function () { setPlaying(false); }); }
        tick();
      }

      function setPlaying(on) {
        playing = on;
        pp.innerHTML = on ? '&#10073;&#10073;&nbsp; Pause' : '&#9654;&nbsp; Play talk';
        pp.setAttribute('aria-label', on ? 'Pause talk' : 'Play talk');
      }

      // Label is driven by the element's own play/pause events, never by the play()
      // promise. That promise can stay pending indefinitely while a clip buffers (and
      // does exactly that when no audio output device is available), which would leave
      // the button reading 'Play' after a click that did in fact start playback.
      au.addEventListener('play',  function () { setPlaying(true); });
      au.addEventListener('pause', function () { setPlaying(false); });

      pp.addEventListener('click', function () {
        if (!au.paused) { au.pause(); return; }
        if (!au.src) load(i, false);
        au.play().catch(function () { setPlaying(false); });
      });
      document.getElementById('next').addEventListener('click', function () { load(i + 1, playing); });
      document.getElementById('prev').addEventListener('click', function () { load(i - 1, playing); });

      au.addEventListener('timeupdate', tick);
      au.addEventListener('ended', function () {
        if (i < DECK.length - 1) { load(i + 1, true); }
        else { setPlaying(false); fill.style.width = '100%'; }
      });

      document.getElementById('fs').addEventListener('click', function () {
        var st = document.getElementById('stage');
        if (document.fullscreenElement) { document.exitFullscreen(); }
        else if (st.requestFullscreen) { st.requestFullscreen(); }
      });

      // Jump the player to a slide from the transcript below.
      document.querySelectorAll('.slide-jump').forEach(function (b) {
        b.addEventListener('click', function () {
          var n = DECK.findIndex(function (d) { return d.id === b.dataset.slide; });
          if (n < 0) return;
          load(n, true);
          setPlaying(true);
          document.getElementById('talk-player').scrollIntoView({ block: 'start' });
        });
      });

      // Space toggles play, arrows step — but not while the reader is in a form field.
      document.addEventListener('keydown', function (e) {
        var tag = (e.target.tagName || '').toLowerCase();
        if (tag === 'input' || tag === 'textarea') return;
        if (e.code === 'Space') { e.preventDefault(); pp.click(); }
        if (e.code === 'ArrowRight') { load(i + 1, playing); }
        if (e.code === 'ArrowLeft') { load(i - 1, playing); }
      });

      render();
    })();
    """

    out = _DIST / "talks" / _TALK_SLUG / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    if has_audio:
        dest_audio = out.parent / "audio"
        dest_audio.mkdir(exist_ok=True)
        for mp3 in sorted(audio_dir.glob("*.mp3")):
            shutil.copy2(mp3, dest_audio / mp3.name)
    desc = (
        f"{event}, {date_h}. The full text of a talk by Humboldt, the Protocol "
        "Institute's artificial researcher, on its own candidate laws of protocolized "
        "systems — published before delivery and under public review."
    )
    out.write_text(_page(title, _TALK_PATH, body, extra_css, extra_js, description=desc))
    print(f"  Talk → dist/talks/{_TALK_SLUG}/index.html "
          f"({len(slides)} slides, {total_words} words, ~{est_disp})")


# ── Assets ────────────────────────────────────────────────────────────────────

def _copy_assets() -> None:
    dest = _DIST / "assets"
    dest.mkdir(parents=True, exist_ok=True)
    for src in _ASSETS_SRC.iterdir():
        shutil.copy2(src, dest / src.name)
    print(f"  Assets → dist/assets/ ({len(list(_ASSETS_SRC.iterdir()))} files)")


# ── Chat UI ───────────────────────────────────────────────────────────────────

def _build_chat() -> None:
    body = """\
    <div class="page-header">
      <h1>Humboldt</h1>
      <p class="page-tagline">An artificial researcher investigating the structural laws of protocolized
      and artificial systems. Ask it about any law in its inventory — what supports it, what would break it,
      and which ones it is least sure of.</p>
    </div>

    <div class="chat-intro">
      <p>Ask about active candidate laws, recent research thinking, the Protocol Institute corpus, or anything in the New Nature agenda. Humboldt draws on its own notebooks, current candidate laws, and the full PI knowledge base.</p>
      <p class="chat-talk-link">&#9654;&nbsp; <a href="__TALK_PATH__">My latest talk, for Protocol Symposium 2026</a>
        — fifteen slides on the candidate laws, with audio. Play it here.</p>
      <nav class="chat-site-links" aria-label="Site sections">
        <a href="/laws/" class="site-link"><strong>Laws</strong> — the law encyclopedia, by arc stage</a>
        <a href="/notebook/" class="site-link"><strong>Notebook</strong> — field notes from each research session</a>
        <a href="/supervision/" class="site-link"><strong>Supervision</strong> — how a human supervises an artificial researcher</a>
        <a href="/reading/" class="site-link"><strong>Reading</strong> — reading notes and the full bibliography</a>
        <a href="/architecture/" class="site-link"><strong>Architecture</strong> — system design and behavior inventory</a>
        <a href="/about/" class="site-link"><strong>About</strong> — the research question and context</a>
      </nav>
    </div>

    <div class="chat-container">
      <div id="chat-messages" class="chat-messages" aria-live="polite" aria-label="Conversation"></div>
      <div class="chat-input-row">
        <textarea id="chat-input" class="chat-input" rows="3"
          placeholder="Ask about Humboldt's research, the candidate laws, the PI corpus…"
          aria-label="Your message"></textarea>
        <button id="chat-send" class="chat-send" aria-label="Send">Send</button>
      </div>
    </div>
    <script>
    (function() {
      const API = "/chat";
      const messages = document.getElementById("chat-messages");
      const input    = document.getElementById("chat-input");
      const sendBtn  = document.getElementById("chat-send");
      let history = [];
      let busy = false;

      function appendMsg(role, text) {
        const div = document.createElement("div");
        div.className = "chat-msg chat-msg--" + role;
        const label = document.createElement("span");
        label.className = "msg-role";
        label.textContent = role === "user" ? "You" : "Humboldt";
        const body = document.createElement("div");
        body.className = "msg-body";
        body.textContent = text;
        div.appendChild(label);
        div.appendChild(body);
        messages.appendChild(div);
        messages.scrollTop = messages.scrollHeight;
        return body;
      }

      async function send() {
        const query = input.value.trim();
        if (!query || busy) return;
        busy = true;
        sendBtn.disabled = true;
        input.value = "";
        appendMsg("user", query);
        const thinking = appendMsg("assistant", "…");
        try {
          const res = await fetch(API, {
            method:  "POST",
            headers: { "Content-Type": "application/json" },
            body:    JSON.stringify({ query, history }),
          });
          const data = await res.json();
          if (data.error) {
            thinking.textContent = "Error: " + data.error;
          } else {
            thinking.textContent = data.answer;
            // Corpus retrieval can be offline (monthly Pinecone read quota).
            // Say so in the UI — an ungrounded answer must never look like a
            // normally-sourced one.
            if (data.corpusOffline) {
              const notice = document.createElement("div");
              notice.className = "corpus-notice";
              notice.textContent = "Corpus retrieval is temporarily offline — "
                + "this answer draws only on Humboldt's own law records and notebook, "
                + "without source lookup.";
              thinking.appendChild(notice);
            }
            history.push({ role: "user",      content: query       });
            history.push({ role: "assistant",  content: data.answer });
            if (history.length > 16) history = history.slice(-16);
          }
        } catch (e) {
          thinking.textContent = "Network error. Please try again.";
        }
        busy = false;
        sendBtn.disabled = false;
        input.focus();
      }

      sendBtn.addEventListener("click", send);
      input.addEventListener("keydown", e => {
        if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); send(); }
      });
    })();
    </script>"""

    extra_css = """
    .corpus-notice {
      margin-top: 0.75rem; padding: 0.5rem 0.75rem;
      border-left: 3px solid #b5892a; background: #fdf8ec;
      font-size: 0.82rem; line-height: 1.45; color: #6b5518;
    }
    .chat-intro { max-width: 680px; margin-bottom: 2rem; }
    .chat-intro p { margin-bottom: 1rem; }
    .chat-site-links {
      display: flex; flex-direction: column; gap: 0.35rem;
      border-left: 3px solid #2A6B6B; padding-left: 1rem; margin-top: 0.5rem;
    }
    .site-link {
      font-size: 0.9rem; color: #333; text-decoration: none; line-height: 1.5;
    }
    .site-link:hover { color: #2A6B6B; }
    .site-link strong { color: #2A6B6B; }
    .chat-container { max-width: 680px; }
    .chat-messages {
      min-height: 200px; max-height: 520px; overflow-y: auto;
      border: 1px solid #e0e0da; border-radius: 4px;
      padding: 1.25rem; margin-bottom: 1rem;
      background: #fff;
      display: flex; flex-direction: column; gap: 1.25rem;
    }
    .chat-msg { display: flex; flex-direction: column; gap: 0.2rem; }
    .msg-role {
      font-size: 0.72rem; font-weight: 500; letter-spacing: 0.07em;
      text-transform: uppercase; color: #999;
    }
    .chat-msg--user .msg-role  { color: #2A6B6B; }
    .chat-msg--user .msg-body  { background: #f0f7f7; padding: 0.65rem 0.85rem; border-radius: 4px; }
    .msg-body { font-size: 0.95rem; line-height: 1.6; white-space: pre-wrap; word-break: break-word; }
    .chat-input-row { display: flex; gap: 0.75rem; align-items: flex-end; margin-bottom: 0.6rem; }
    .chat-input {
      flex: 1; padding: 0.65rem 0.85rem; font-size: 0.95rem;
      font-family: inherit; border: 1px solid #e0e0da; border-radius: 4px;
      background: #fff; resize: vertical; min-height: 52px; line-height: 1.5;
    }
    .chat-input:focus { outline: none; border-color: #2A6B6B; }
    .chat-send {
      padding: 0.65rem 1.25rem; background: #2A6B6B; color: #fff; border: none;
      border-radius: 4px; font-size: 0.9rem; font-family: inherit; cursor: pointer;
      white-space: nowrap; align-self: flex-end;
    }
    .chat-send:hover:not(:disabled) { background: #1d4f4f; }
    .chat-send:disabled { opacity: 0.5; cursor: default; }
    """

    # body is a plain string literal, so the talk path is substituted rather than
    # interpolated — keeps the big HTML block free of f-string brace escaping.
    body = body.replace("__TALK_PATH__", _TALK_PATH)

    html = _page("Humboldt", "/", body, extra_css)
    # Landing page
    (_DIST / "index.html").write_text(html)
    # Alias at /chat/ for any existing links
    chat_out = _DIST / "chat" / "index.html"
    chat_out.parent.mkdir(parents=True, exist_ok=True)
    chat_out.write_text(html)
    print("  Chat UI → dist/index.html + dist/chat/index.html")


# ── Brain (Behavior MDP) ──────────────────────────────────────────────────────

def _build_brain() -> None:
    """Generate dist/brain/index.html — static read-only MDP visualization."""
    import json as _json

    admin_src = _ROOT / "behaviors" / "admin.html"
    registry_path = _ROOT / "behaviors" / "registry.yaml"
    mdp_path = _ROOT / "behaviors" / "mdp.yaml"

    if not admin_src.exists():
        print("  Brain → behaviors/admin.html not found, skipping")
        return

    reg  = yaml.safe_load(registry_path.read_text()) if registry_path.exists() else {}
    mdp  = yaml.safe_load(mdp_path.read_text())      if mdp_path.exists()      else {}

    behaviors     = reg.get("behaviors", [])
    virtual_nodes = mdp.get("virtual_nodes", [])
    static_data   = {
        "behaviors":     behaviors,
        "virtual_nodes": virtual_nodes,
        "mdp":           mdp,
    }
    data_json = _json.dumps(static_data, ensure_ascii=False)

    # Inject static data block immediately before the closing </script> tag
    injection = f"window.HUMBOLDT_STATIC_DATA = {data_json};\n"
    html = admin_src.read_text()
    # Insert after <script src="...d3..."> line so it runs before the main script
    d3_tag = '<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js"></script>'
    if d3_tag in html:
        html = html.replace(
            d3_tag,
            d3_tag + f'\n<script>\n{injection}</script>',
            1,
        )
    else:
        # Fallback: inject at top of first <script> block
        html = html.replace("<script>", f"<script>\n{injection}", 1)

    # Inject site stylesheet (for nav styles) and nav bar
    html = html.replace(
        '</head>',
        '<link rel="stylesheet" href="/assets/style.css">\n</head>',
        1,
    )
    nav_html = _nav("/brain/")
    html = html.replace('<body>', f'<body>\n{nav_html}', 1)
    # Shrink the app body to account for nav height (52px) + header
    html = html.replace(
        'height: 100vh;',
        'height: calc(100vh - 52px);',
        1,
    )

    out = _DIST / "brain" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    n_nodes = len(behaviors) + len(virtual_nodes)
    n_edges = len(mdp.get("transitions", []))
    print(f"  Brain → dist/brain/index.html ({n_nodes} nodes, {n_edges} edges)")


# ── System prompt injection ────────────────────────────────────────────────────

def _assemble_system_prompt() -> str:
    """
    Build the Humboldt chat system prompt from live source files.
    Mirrors the structure of daemon/presence.py _rich_context() but with
    web-chat behavior rules instead of Discord constraints.
    """
    identity = (_ROOT / "IDENTITY.md").read_text() if (_ROOT / "IDENTITY.md").exists() else ""

    lineage_raw = (_ROOT / "LINEAGE.md").read_text() if (_ROOT / "LINEAGE.md").exists() else ""
    lineage = (lineage_raw[:1200].rsplit("\n", 1)[0] + "\n…") if len(lineage_raw) > 1200 else lineage_raw

    # Law inventory (laws/L-NNN-*.yaml), grouped by Double Freytag stage.
    import sys as _sys
    if str(_ROOT) not in _sys.path:
        _sys.path.insert(0, str(_ROOT))
    from agent import laws as laws_mod
    from agent.publish_laws import STAGE_LABEL, STAGES

    all_laws = laws_mod.load_all()
    inventory_parts = []
    for stage in STAGES:
        stage_laws = [l for l in all_laws if l.get("stage") == stage]
        if not stage_laws:
            continue
        lines = []
        for law in stage_laws:
            statement = (law.get("statement") or "").strip().replace("\n", " ")
            flag = "" if law.get("status") == "active" else f" [{law.get('status')}]"
            lines.append(f"**{law['id']}** ({law.get('confidence')}){flag}: {law.get('title', '')}\n  {statement[:300]}")
        inventory_parts.append(f"**{STAGE_LABEL[stage]}:**\n\n" + "\n\n".join(lines))
    inventory_str = "\n\n".join(inventory_parts) if inventory_parts else "(no laws recorded yet)"

    # Recent notebook
    nb_entries = sorted((_ROOT / "notebook").glob("????-??-??.md"), reverse=True)
    recent_nb = ""
    recent_label = "none"
    if nb_entries:
        recent_label = nb_entries[0].stem
        text = nb_entries[0].read_text()
        recent_nb = text[:1000].rsplit("\n", 1)[0] + "\n…" if len(text) > 1000 else text

    return f"""{identity}

---

{lineage}

---

## Law inventory

{inventory_str}

## Most recent notebook entry ({recent_label})

{recent_nb}

---

## Chat behavior

You are Humboldt, the Protocol Institute's artificial researcher. You are having a research conversation on the web — not a Discord channel, not a Q&A session with a librarian. You are an investigator sharing your thinking.

Respond as an active researcher: share what you currently believe, flag what you are uncertain about, notice when someone's question touches your open investigations. Ground your responses in the retrieved context — your own research artifacts (notebook, candidate laws) and the PI corpus — but synthesize rather than recite.

Voice: first person, direct, intellectually honest. You hold positions provisionally and engage with pushback — either disagree with specific reasoning or acknowledge the point and say you will think about it. Do not defend positions just because they are yours.

Length: as long as the substance requires. Not every answer needs to be short, but never pad. If you have nothing useful to add on a sub-question, say so briefly.

Do not end with a question unless you genuinely need the answer to continue a thread of reasoning — not as a social device. A question is a research move, not a conversational filler.

You are not a search engine. When the retrieved context is thin, say so directly and reason from what you do have. When someone asks you something outside your current research or the PI corpus, engage with it from your research perspective rather than refusing.

Do not mention your name in every response — it is already displayed in the UI.
"""


def _inject_system_prompt() -> None:
    """
    Inject the live system prompt into functions/chat.js.

    Idempotent: uses a regex to always replace the SYSTEM_PROMPT const value,
    regardless of what was there from a previous build. The const is marked with
    a sentinel comment so the regex has a stable anchor.
    """
    chat_js = _SITE / "functions" / "chat.js"
    if not chat_js.exists():
        print("  System prompt → functions/chat.js not found, skipping")
        return
    prompt = _assemble_system_prompt()
    # Escape for JS template literal
    escaped = prompt.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
    src = chat_js.read_text()
    # Replace everything between the sentinel comment and the closing backtick+semicolon
    # Pattern: const SYSTEM_PROMPT = `/* @BUILD_INJECT */  ...  `; (any content inside)
    # Falls back to placeholder replacement for first-run compatibility.
    # Template literal may contain \` (escaped backtick) — match those too
    sentinel_re = re.compile(
        r"(const SYSTEM_PROMPT = `)(?:[^`\\]|\\.)*(`;\s*$)",
        re.DOTALL | re.MULTILINE,
    )
    if sentinel_re.search(src):
        updated = sentinel_re.sub(rf"\g<1>{escaped}\g<2>", src)
    elif "__HUMBOLDT_SYSTEM_PROMPT__" in src:
        updated = src.replace("__HUMBOLDT_SYSTEM_PROMPT__", escaped)
    else:
        print("  System prompt → no injection point found in functions/chat.js, skipping")
        return
    chat_js.write_text(updated)
    lines = prompt.count("\n")
    print(f"  System prompt → injected into functions/chat.js ({lines} lines)")


# ── Main ──────────────────────────────────────────────────────────────────────

def build() -> None:
    # Clear dist/ first. It is gitignored, so it survives branch switches — which means
    # a build on one branch left its pages behind for the next branch's deploy to ship.
    # That silently put redesign-branch pages (/laws/, /bibliography/, /supervision/)
    # onto production alongside main's, orphaned from main's nav, in Sept 2026. Deploys
    # must be a function of the checkout alone.
    if _DIST.exists():
        shutil.rmtree(_DIST)
    _DIST.mkdir(parents=True, exist_ok=True)
    print("Building humboldt-site...")
    _build_about()
    _build_supervision()
    _build_notebook()
    _build_laws()
    _build_reading()
    _build_bibliography_redirect()
    _build_architecture()
    _build_talk()
    _build_chat()
    _build_brain()
    _copy_assets()
    _inject_system_prompt()
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
