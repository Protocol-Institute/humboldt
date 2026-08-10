"""
publish_reading.py — render Humboldt deep-read notes to the PI website.

Reads all bibliography/notes/*.md files, renders each as a reading card on
humboldt-reading/index.html in the PI website repo, then commits + pushes.

Usage:
    python3 -m agent.humboldt publish-reading
    python3 -m agent.humboldt publish-reading --dry-run
"""

import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import markdown as md_lib

_ROOT = Path(__file__).parent.parent
_NOTES_DIR = _ROOT / "bibliography" / "notes"
_SHALLOW_DIR = _ROOT / "bibliography" / "shallow-reads"
_WEBSITE_REPO = _ROOT.parent / "website"
_OUTPUT_DIR = _WEBSITE_REPO / "humboldt-reading"
_OUTPUT_HTML = _OUTPUT_DIR / "index.html"


# ── Section extraction ────────────────────────────────────────────────────────

def _extract_section(text: str, *names: str) -> str:
    """Extract the body of the first section whose heading matches any name (case-insensitive)."""
    pattern = r"^#{1,4}\s+(?:\d+\.\s+)?(" + "|".join(re.escape(n) for n in names) + r")\s*$"
    parts = re.split(r"^(#{1,4}\s+.+)$", text, flags=re.MULTILINE)
    for i, part in enumerate(parts):
        if re.match(pattern, part.strip(), re.IGNORECASE):
            body = parts[i + 1].strip() if i + 1 < len(parts) else ""
            return body
    return ""


def _count_subsections(section_body: str) -> int:
    """Count ## or ### subheadings in a section body (proxy for item count)."""
    return len(re.findall(r"^#{2,4}\s+\*\*", section_body, re.MULTILINE))


def _extract_title_line(text: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def _extract_bibliographic(text: str) -> dict:
    """Pull author, title, year from bibliographic section or filename heading."""
    bib = _extract_section(text, "Bibliographic Information", "Bibliographic Info")
    result = {"author": "", "title": "", "year": "", "publisher": ""}
    if bib:
        for field, key in [("Author", "author"), ("Title", "title"),
                           ("Year", "year"), ("Publisher", "publisher")]:
            m = re.search(rf"\*\*{field}:\*\*\s*(.+)$", bib, re.MULTILINE)
            if m:
                result[key] = m.group(1).strip().strip("*_")
    return result


def _extract_date_read(text: str) -> str:
    """Find the most recent 'Read YYYY-MM-DD' or 'YYYY-MM-DD' date in reading log."""
    m = re.search(r"\*\*(20\d\d-\d\d-\d\d)\*\*:", text)
    if m:
        return m.group(1)
    m = re.search(r"Read\s+(20\d\d-\d\d-\d\d)", text)
    if m:
        return m.group(1)
    m = re.search(r"(20\d\d-\d\d-\d\d)", text)
    return m.group(1) if m else ""


# ── HTML rendering ────────────────────────────────────────────────────────────

def _md_to_html(text: str) -> str:
    html = md_lib.markdown(text, extensions=["tables", "fenced_code"])
    html = html.replace("<h2>", "<h4>").replace("</h2>", "</h4>")
    html = html.replace("<h3>", "<h5>").replace("</h3>", "</h5>")
    html = re.sub(r"\n{3,}", "\n\n", html)
    return html.strip()


def _render_note(path: Path) -> dict:
    """Parse a notes file and return a dict of display fields."""
    text = path.read_text()
    bib = _extract_bibliographic(text)
    title_line = _extract_title_line(text)

    # Gestalt — try both numbered and unnumbered heading variants
    gestalt = _extract_section(
        text,
        "Gestalt", "Revised Gestalt",
        "3. Gestalt", "1. Gestalt",
    )
    # Strip pre-reading hypothesis sub-section if present — use revised gestalt only
    if "### Phase 1 Structural Map" in gestalt or "### Revised Gestalt" in gestalt:
        m = re.search(r"### Revised Gestalt.*?\n(.*)", gestalt, re.DOTALL)
        if m:
            gestalt = m.group(1).strip()

    # Analytical moves
    moves_body = _extract_section(
        text,
        "Analytical Moves", "6. Analytical Moves", "4. Analytical Moves",
    )
    move_items = re.findall(r"^\*\*(?:Move [A-Z]|[0-9]+\.)", moves_body, re.MULTILINE)
    n_moves = len(move_items)

    # Candidate laws
    laws_body = _extract_section(
        text,
        "Candidate Laws", "8. Candidate Laws", "10. Candidate Laws",
        "Candidate Law",
    )
    law_names = re.findall(r"^\*\*CL-[^:*]+", laws_body, re.MULTILINE)
    if not law_names:
        law_names = re.findall(r"^### (CL-[^\n]+)", laws_body, re.MULTILINE)

    # What it opens
    opens_body = _extract_section(
        text,
        "What It Opens", "What it opens",
        "9. What It Opens", "12. What It Opens", "10. What It Opens",
    )

    # Metadata
    date_read = _extract_date_read(text)

    return {
        "path": path,
        "stem": path.stem,
        "title_line": title_line,
        "bib": bib,
        "gestalt_md": gestalt[:2000] if gestalt else "",
        "n_moves": n_moves,
        "law_names": law_names,
        "opens_md": opens_body[:1500] if opens_body else "",
        "date_read": date_read,
        "full_text": text,
    }


def _render_card(note: dict, idx: int) -> str:
    bib = note["bib"]
    author = bib["author"] or "Unknown"
    year = bib["year"] or ""
    pub_title = bib["title"] or note["title_line"].replace("Reading Notes: ", "").replace("Deep Read Notes: ", "")

    date_read_str = ""
    if note["date_read"]:
        try:
            d = datetime.strptime(note["date_read"], "%Y-%m-%d")
            date_read_str = d.strftime("%-d %B %Y")
        except ValueError:
            date_read_str = note["date_read"]

    gestalt_html = _md_to_html(note["gestalt_md"]) if note["gestalt_md"] else "<p><em>See full notes.</em></p>"

    # Candidate laws badge
    law_badge = ""
    if note["law_names"]:
        law_badge = f'<span class="badge">{len(note["law_names"])} candidate law{"s" if len(note["law_names"]) != 1 else ""}</span>'
    elif note["n_moves"]:
        law_badge = ""

    # Moves badge
    moves_badge = f'<span class="badge badge-secondary">{note["n_moves"]} analytical move{"s" if note["n_moves"] != 1 else ""}</span>' if note["n_moves"] else ""

    # Opens section
    opens_html = ""
    if note["opens_md"]:
        opens_html = f"""
          <div class="opens-section">
            <p class="section-label">What it opens</p>
            {_md_to_html(note["opens_md"])}
          </div>"""

    # Full notes in collapsible
    full_html = _md_to_html(note["full_text"])
    slug = note["stem"]

    return f"""
    <div class="reading-card" id="read-{slug}">
      <div class="reading-meta">
        <span class="reading-date">{date_read_str}</span>
        <a class="entry-permalink" href="#read-{slug}" title="Link to this entry">§</a>
      </div>
      <h2 class="reading-title">{pub_title}</h2>
      <p class="reading-author">{author}{(" · " + year) if year else ""}</p>
      <div class="reading-badges">{law_badge} {moves_badge}</div>
      <div class="reading-gestalt">
        <p class="section-label">Gestalt</p>
        {gestalt_html}
      </div>{opens_html}
      <details class="full-notes">
        <summary>Full reading notes</summary>
        <div class="full-notes-body">
          {full_html}
        </div>
      </details>
    </div>"""


# ── Page assembly ─────────────────────────────────────────────────────────────

_CSS = """
    .reading-card {
      border-top: 1px solid #ddd;
      padding-top: 2rem;
      margin-top: 2.5rem;
    }
    .reading-card:first-of-type {
      border-top: none;
      padding-top: 0;
      margin-top: 1.5rem;
    }
    .reading-meta {
      font-family: 'DM Sans', sans-serif;
      font-size: 0.85rem;
      color: #666;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.3rem;
    }
    .reading-title {
      margin: 0 0 0.2rem;
      font-size: 1.35rem;
    }
    .reading-author {
      color: #555;
      font-style: italic;
      margin: 0 0 0.75rem;
    }
    .reading-badges {
      margin-bottom: 1rem;
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }
    .badge {
      background: #2A6B6B;
      color: white;
      font-size: 0.78rem;
      padding: 0.2rem 0.6rem;
      border-radius: 3px;
      font-family: 'DM Sans', sans-serif;
    }
    .badge-secondary {
      background: #666;
    }
    .reading-gestalt {
      background: #f5f5f2;
      border-left: 3px solid #2A6B6B;
      padding: 1rem 1.25rem;
      margin-bottom: 1.25rem;
    }
    .opens-section {
      margin-bottom: 1.25rem;
    }
    .section-label {
      font-family: 'DM Sans', sans-serif;
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #888;
      margin-bottom: 0.4rem;
    }
    .full-notes {
      margin-top: 1rem;
      border: 1px solid #e0e0de;
      border-radius: 4px;
    }
    .full-notes summary {
      padding: 0.6rem 1rem;
      cursor: pointer;
      font-family: 'DM Sans', sans-serif;
      font-size: 0.9rem;
      color: #2A6B6B;
      user-select: none;
    }
    .full-notes summary:hover { background: #f9f9f7; }
    .full-notes-body {
      padding: 1rem 1.25rem 1.25rem;
      border-top: 1px solid #e0e0de;
      font-size: 0.93rem;
    }
    .reading-toc {
      background: #f9f9f7;
      border: 1px solid #e0e0de;
      border-radius: 4px;
      padding: 1rem 1.25rem;
      margin-bottom: 2rem;
    }
    .reading-toc h3 {
      margin-top: 0;
      font-size: 0.9rem;
      font-family: 'DM Sans', sans-serif;
      color: #555;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .reading-toc ul {
      margin: 0;
      padding-left: 1.2rem;
    }
    .reading-toc li { margin-bottom: 0.3rem; }
    .entry-permalink {
      color: #bbb;
      text-decoration: none;
      margin-left: 0.4em;
      font-size: 0.9em;
    }
    .entry-permalink:hover { color: #2A6B6B; }
    .reading-intro {
      background: #f5f5f2;
      border-left: 3px solid #2A6B6B;
      padding: 1rem 1.25rem;
      margin-bottom: 2rem;
      font-size: 0.95rem;
    }
"""


def _build_html(notes: list[dict]) -> str:
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
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Humboldt Reading Notes — The Protocol Institute</title>
  <meta name="description" content="Humboldt's deep reading notes — sources that changed how an artificial researcher thinks.">
  <link rel="icon" href="/assets/logo-static.png" type="image/png">
  <link rel="stylesheet" href="/css/style.css">
  <style>{_CSS}
  </style>
</head>
<body>
  <header>
    <div class="container">
      <a href="/" class="logo"><img src="/assets/logo-static.png" alt="Protocol Institute" height="36"></a>
      <nav>
        <a href="/humboldt/">Humboldt</a>
        <a href="/humboldt-notebook/">Lab Notebook</a>
        <a href="/humboldt-reading/" class="active">Reading Notes</a>
        <a href="/humboldt-research/">Research</a>
        <a href="/humboldt-behaviors/">Behaviors</a>
      </nav>
    </div>
  </header>
  <main>
    <div class="container">
      <h1>Humboldt Reading Notes</h1>
      <div class="reading-intro">
        Deep reading notes from behavior-t5m — sources that changed how Humboldt thinks,
        not just sources consulted. Each read is conducted from the actual text, never
        from training memory. The gestalt paragraph describes what the work is doing on
        its own terms; the full notes record genuine engagement.
      </div>

      <div class="reading-toc">
        <h3>Sources ({len(notes)} completed)</h3>
        <ul>
{toc_items}        </ul>
      </div>

{cards}

      <p style="margin-top:3rem;font-size:0.8rem;color:#aaa;">Generated {now}</p>
    </div>
  </main>
  <footer>
    <div class="container">
      <p>The Protocol Institute · <a href="https://protocolized.io">Protocolized</a></p>
    </div>
  </footer>
</body>
</html>"""


# ── Shallow reads (humboldt-site /reading/ extension, plan §4.2) ──────────────
#
# Adds a compact, date-grouped shallow-read section alongside the existing deep-read
# cards. Kept separate from _render_note/_render_card (used by the legacy website
# publish_reading() path above) — shallow reads are lighter records (819 files) and
# get a lighter rendering: one line + a short excerpt, not the full note body.

def _parse_shallow_light(path: Path) -> dict:
    from agent import bibliography as bib_mod
    from agent import laws as laws_mod

    text = path.read_text()
    title_m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else path.stem

    source_m = re.search(r"^\*\*Source:\*\*\s*(.+)$", text, re.MULTILINE)
    source = source_m.group(1).strip() if source_m else ""
    url = bib_mod._first_url(source)

    date_m = re.search(r"^\*\*Date read:\*\*\s*(\S+)", text, re.MULTILINE)
    date_read = date_m.group(1).strip() if date_m else ""

    conn_m = re.search(r"^\*\*Connected to:\*\*\s*(.+)$", text, re.MULTILINE)
    raw_tokens = re.split(r"[,\s]+", conn_m.group(1).strip()) if conn_m else []
    current_ids = {l["id"] for l in laws_mod.load_all()}
    mapped, _raw = bib_mod.map_law_tokens(raw_tokens, current_ids)

    esc_m = re.search(r"^\*\*Escalation:\*\*\s*(\S+)", text, re.MULTILINE)
    escalation = esc_m.group(1).strip() if esc_m else ""

    took = _extract_section(text, "What I took from it")
    took = re.sub(r"\s+", " ", took).strip()
    excerpt = (took[:280].rsplit(" ", 1)[0] + "…") if len(took) > 280 else took

    return {
        "stem": path.stem,
        "title": title,
        "url": url,
        "date_read": date_read,
        "laws": mapped,
        "escalation": escalation,
        "excerpt": excerpt,
    }


def _render_shallow_item(item: dict) -> str:
    title_html = (
        f'<a href="{item["url"]}" target="_blank" rel="noopener">{item["title"]}</a>'
        if item["url"] else item["title"]
    )
    laws_html = "".join(
        f'<a class="law-chip" href="/laws/#law-{lid}">{lid}</a>' for lid in item["laws"]
    )
    star = '<span class="shallow-star" title="Escalated to deep read">★</span>' if item["escalation"] == "escalate-to-deep" else ""
    return f"""
      <div class="shallow-item" id="shallow-{item['stem']}">
        <p class="shallow-title">{title_html} {star}{laws_html}</p>
        <p class="shallow-excerpt">{item['excerpt']}</p>
      </div>"""


def build_shallow_section() -> tuple[str, int]:
    """Returns (body_html, count) — a date-grouped, collapsible shallow-read section."""
    paths = sorted((p for p in _SHALLOW_DIR.glob("*.md") if not p.name.startswith("_")), reverse=True)
    if not paths:
        return "", 0

    items = [_parse_shallow_light(p) for p in paths]
    by_date: dict[str, list[dict]] = {}
    for it in items:
        by_date.setdefault(it["date_read"] or "undated", []).append(it)

    groups_html = []
    for date_str in sorted(by_date, reverse=True):
        group_items = by_date[date_str]
        try:
            label = datetime.strptime(date_str, "%Y-%m-%d").strftime("%-d %B %Y")
        except ValueError:
            label = date_str
        rows = "".join(_render_shallow_item(it) for it in group_items)
        groups_html.append(f"""
    <details class="shallow-date-group">
      <summary>{label} <span class="shallow-date-count">({len(group_items)})</span></summary>
      <div class="shallow-items">{rows}
      </div>
    </details>""")

    body = f"""\
    <div class="shallow-section">
      <p class="section-label">Shallow reads — {len(items)} sources, one-paragraph synthesis notes from triage</p>
{''.join(groups_html)}
    </div>"""
    return body, len(items)


_SHALLOW_CSS = """
    .shallow-section { margin-top: 3rem; }
    .shallow-date-group {
      border-top: 1px solid #eee; padding-top: 0.5rem; margin-top: 0.75rem;
    }
    .shallow-date-group summary {
      cursor: pointer; font-family: 'DM Sans', sans-serif; font-size: 0.9rem;
      color: #2A6B6B; padding: 0.4rem 0; user-select: none;
    }
    .shallow-date-group summary:hover { color: #1d4f4f; }
    .shallow-date-count { color: #999; font-weight: 400; }
    .shallow-items { padding: 0.25rem 0 0.75rem 1rem; }
    .shallow-item { margin-bottom: 0.9rem; }
    .shallow-title { font-size: 0.92rem; margin-bottom: 0.15rem; }
    .shallow-star { color: #a5620a; margin: 0 0.2rem; }
    .shallow-excerpt { font-size: 0.85rem; color: #666; max-width: 68ch; margin-bottom: 0; }
    .law-chip {
      display: inline-block; background: #edf5f5; color: #1d4f4f; border-radius: 3px;
      padding: 0.05rem 0.4rem; margin-left: 0.35rem; font-size: 0.78rem;
    }
"""


# ── Entry point ───────────────────────────────────────────────────────────────

def publish_reading(dry_run: bool = False) -> None:
    notes_paths = sorted(p for p in _NOTES_DIR.glob("*.md") if not p.name.startswith("_"))
    if not notes_paths:
        print("No reading notes found in bibliography/notes/")
        return

    notes = [_render_note(p) for p in notes_paths]
    # Sort by date read, oldest first
    notes.sort(key=lambda n: n["date_read"] or "0000")

    html = _build_html(notes)

    if dry_run:
        print(f"[dry-run] Would write {len(html):,} chars to {_OUTPUT_HTML}")
        print(f"[dry-run] {len(notes)} notes: {[n['stem'] for n in notes]}")
        return

    _OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    _OUTPUT_HTML.write_text(html, encoding="utf-8")
    print(f"Written: {_OUTPUT_HTML} ({len(html):,} chars, {len(notes)} notes)")

    # Commit + push website repo
    try:
        subprocess.run(["git", "add", str(_OUTPUT_HTML)], cwd=_WEBSITE_REPO, check=True)
        msg = f"Humboldt reading notes: {len(notes)} sources ({datetime.now().strftime('%Y-%m-%d')})"
        subprocess.run(["git", "commit", "-m", msg], cwd=_WEBSITE_REPO, check=True)
        subprocess.run(["git", "push"], cwd=_WEBSITE_REPO, check=True)
        print("Pushed to website repo.")
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}", file=sys.stderr)
