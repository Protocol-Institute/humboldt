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
    ("/",              "Chat"),
    ("/notebook/",     "Notebook"),
    ("/laws/",         "Laws"),
    ("/bibliography/", "Bibliography"),
    ("/reading/",      "Reading"),
    ("/architecture/", "Architecture"),
    ("/about/",        "About"),
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


def _page(title: str, active_path: str, body: str,
          extra_css: str = "", extra_js: str = "") -> str:
    extra = f"\n  <style>{extra_css}</style>" if extra_css else ""
    js    = f"\n<script>{extra_js}</script>" if extra_js else ""
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

def _build_bibliography() -> None:
    import sys as _sys
    if str(_ROOT) not in _sys.path:
        _sys.path.insert(0, str(_ROOT))
    from agent.publish_bibliography import build_bibliography_body, _CSS as _BCSS, _JS as _BJS

    body, total = build_bibliography_body()

    out = _DIST / "bibliography" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(_page("Bibliography", "/bibliography/", body, extra_css=_BCSS, extra_js=_BJS))
    print(f"  Bibliography → dist/bibliography/index.html ({total} entries)")


# ── Reading ───────────────────────────────────────────────────────────────────

def _build_reading() -> None:
    import sys as _sys
    if str(_ROOT) not in _sys.path:
        _sys.path.insert(0, str(_ROOT))
    from agent.publish_reading import (
        _render_note, _render_card, build_shallow_section,
        _CSS as _RCSS, _SHALLOW_CSS,
    )

    notes_dir = _ROOT / "bibliography" / "notes"
    note_paths = sorted(p for p in notes_dir.glob("*.md") if not p.name.startswith("_"))

    notes = [_render_note(p) for p in note_paths]
    notes.sort(key=lambda n: n["date_read"] or "0000")

    # TOC
    toc_items = ""
    for note in notes:
        bib = note["bib"]
        pub_title = bib["title"] or note["title_line"]
        author = bib["author"] or ""
        year = bib["year"] or ""
        slug = note["stem"]
        toc_items += f'      <li><a href="#read-{slug}">{pub_title}</a>'
        if author:
            toc_items += f' — {author}'
        if year:
            toc_items += f' ({year})'
        toc_items += "</li>\n"

    cards = "\n".join(_render_card(note, i) for i, note in enumerate(notes))
    shallow_body, shallow_n = build_shallow_section()

    body = f"""\
    <div class="page-header">
      <h1>Reading</h1>
      <p class="page-tagline">Sources that shaped Humboldt's thinking — deep reads (full text, from behavior-t5m,
      never from training memory) and shallow reads (one-paragraph triage synthesis). See also the full
      <a href="/bibliography/">bibliography</a>.</p>
    </div>
    <div class="reading-toc">
      <h3>Deep reads ({len(notes)} completed)</h3>
      <ul>
{toc_items}      </ul>
    </div>
{cards}
{shallow_body}"""

    out = _DIST / "reading" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(_page("Reading", "/reading/", body, extra_css=_RCSS + _SHALLOW_CSS))
    print(f"  Reading → dist/reading/index.html ({len(notes)} deep, {shallow_n} shallow)")


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


# ── Chat UI ───────────────────────────────────────────────────────────────────

def _build_chat() -> None:
    body = """\
    <div class="page-header">
      <h1>Humboldt</h1>
      <p class="page-tagline">An artificial researcher investigating the structural laws of protocolized and artificial systems.</p>
    </div>

    <div class="chat-intro">
      <p>Ask about active candidate laws, recent research thinking, the Protocol Institute corpus, or anything in the New Nature agenda. Humboldt draws on its own notebooks, current candidate laws, and the full PI knowledge base.</p>
      <nav class="chat-site-links" aria-label="Site sections">
        <a href="/notebook/" class="site-link"><strong>Notebook</strong> — field notes from each research session</a>
        <a href="/laws/" class="site-link"><strong>Laws</strong> — the law encyclopedia, by arc stage</a>
        <a href="/bibliography/" class="site-link"><strong>Bibliography</strong> — every source engaged past triage</a>
        <a href="/reading/" class="site-link"><strong>Reading</strong> — deep and shallow reading notes</a>
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
    _DIST.mkdir(parents=True, exist_ok=True)
    print("Building humboldt-site...")
    _build_about()
    _build_notebook()
    _build_laws()
    _build_bibliography()
    _build_reading()
    _build_architecture()
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
