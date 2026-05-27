"""
publish.py — render Humboldt lab notebook entries to the PI website.

Reads all notebook/YYYY-MM-DD.md files, converts any that are not yet
present in humboldt-notebook.html, inserts them in chronological order,
then regenerates the table of contents and commits + pushes the website repo.

Usage (CLI):
    python3 -m agent.humboldt publish              # render + push
    python3 -m agent.humboldt publish --dry-run    # render only, no git ops

Entries are inserted newest-last (chronological reading order).

Notebook markdown convention:
  Line 1:  # Lab Notebook — YYYY-MM-DD
  Line 2:  *Short tagline sentence.*
  Body:    ## Section headers, paragraphs, **bold**, *italic*, lists
  Title:   First ## heading is used as the entry h2 title.
           Override with a YAML-style comment on line 3:
             <!-- title: Custom Title Here -->
"""

import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import markdown as md_lib

from . import notebook_index as nbi

_ROOT = Path(__file__).parent.parent
_NOTEBOOK_DIR = _ROOT / "notebook"

# Path to the PI website repo (sibling directory)
_WEBSITE_REPO = _ROOT.parent / "website"
_NOTEBOOK_HTML = _WEBSITE_REPO / "humboldt-notebook.html"

# Markers
_ENTRY_MARKER_FMT = "<!-- ENTRY: {date} -->"
_TOC_START = "<!-- TOC -->"
_TOC_END = "<!-- END TOC -->"
_INSERT_BEFORE = "      </div>\n    </div>\n  </main>"


# ── Markdown → HTML ───────────────────────────────────────────────────────────

def _convert_body(body_md: str) -> str:
    """Convert notebook markdown body to HTML, demoting headings by one level."""
    html = md_lib.markdown(body_md, extensions=["tables", "fenced_code"])
    html = html.replace("<h2>", "<h3>").replace("</h2>", "</h3>")
    html = html.replace("<h3>", "\n          <h3>").replace("</h3>", "</h3>\n")
    html = html.replace("<p>", "\n          <p>").replace("</p>", "</p>\n")
    html = html.replace("<ul>", "\n          <ul>").replace("</ul>", "          </ul>\n")
    html = html.replace("<ol>", "\n          <ol>").replace("</ol>", "          </ol>\n")
    html = html.replace("<li>", "            <li>").replace("</li>", "</li>")
    html = html.replace("<hr />", "").replace("<hr>", "")
    html = re.sub(r"\n{3,}", "\n\n", html)
    return html.strip()


def render_entry(date_str: str, md_path: Path) -> tuple[str, str, str]:
    """
    Render a single notebook markdown file to a complete HTML entry block.

    Returns (entry_html, title, tagline).
    The entry div carries id="entry-{date}" for direct linking.
    """
    raw = md_path.read_text()
    lines = raw.split("\n")

    tagline = ""
    title_override = ""
    body_start = 1

    for i, line in enumerate(lines[1:], start=1):
        stripped = line.strip()
        if not tagline and stripped.startswith("*") and stripped.endswith("*") and len(stripped) > 2:
            tagline = stripped[1:-1]
            body_start = i + 1
            continue
        m = re.match(r"<!--\s*title:\s*(.+?)\s*-->", stripped)
        if m:
            title_override = m.group(1)
            body_start = i + 1
            continue
        if stripped and stripped != "---":
            body_start = i
            break

    body_md = "\n".join(lines[body_start:])

    if title_override:
        title = title_override
    else:
        m = re.search(r"^##\s+(.+)$", body_md, re.MULTILINE)
        title = m.group(1).strip() if m else f"Session {date_str}"

    dt = datetime.strptime(date_str, "%Y-%m-%d")
    display_date = dt.strftime("%B %-d, %Y")
    anchor = nbi.entry_anchor(date_str)
    permalink = f'<a href="#{anchor}" class="entry-permalink" title="Permalink to this entry">§</a>'

    body_html = _convert_body(body_md)

    entry_html = (
        f"\n        {_ENTRY_MARKER_FMT.format(date=date_str)}\n"
        f'        <div class="notebook-entry" id="{anchor}">\n\n'
        f'          <p class="entry-date">{display_date} {permalink}</p>\n'
        f"          <h2>{title}</h2>\n"
        + (f'          <p class="entry-tagline">{tagline}</p>\n' if tagline else "")
        + f"\n{body_html}\n\n"
        f"        </div>\n"
        f"        <!-- END ENTRY -->\n"
    )
    return entry_html, title, tagline


# ── TOC ───────────────────────────────────────────────────────────────────────

def _render_toc(entries: list[dict]) -> str:
    """Generate the table of contents nav block from the index."""
    if not entries:
        return ""
    items = []
    for e in reversed(entries):  # newest first in TOC
        date = e.get("date", "")
        title = e.get("title", date)
        anchor = e.get("anchor", nbi.entry_anchor(date))
        try:
            dt = datetime.strptime(date, "%Y-%m-%d")
            label_date = dt.strftime("%b %-d, %Y")
        except ValueError:
            label_date = date
        items.append(f'            <li><a href="#{anchor}">{label_date} — {title}</a></li>')
    items_html = "\n".join(items)
    return (
        f"        {_TOC_START}\n"
        f'        <nav class="notebook-toc" aria-label="Entry index">\n'
        f'          <h3 class="toc-heading">Entries</h3>\n'
        f"          <ul>\n"
        f"{items_html}\n"
        f"          </ul>\n"
        f"        </nav>\n"
        f"        {_TOC_END}"
    )


def _update_toc(html: str, entries: list[dict]) -> str:
    """Replace or insert the TOC block in the HTML."""
    toc_html = _render_toc(entries)
    if _TOC_START in html and _TOC_END in html:
        # Replace existing TOC; back up past leading whitespace on the same line
        # to avoid doubling indentation from html[:start] + indented toc_html
        start = html.index(_TOC_START)
        end = html.index(_TOC_END) + len(_TOC_END)
        line_start = html.rfind("\n", 0, start) + 1
        return html[:line_start] + toc_html + html[end:]
    # Insert TOC just before the first entry marker
    first_entry = re.search(r"        <!-- ENTRY: \d{4}-\d{2}-\d{2} -->", html)
    if first_entry:
        pos = first_entry.start()
        return html[:pos] + toc_html + "\n\n" + html[pos:]
    return html


# ── ID migration (one-time) ───────────────────────────────────────────────────

def _add_missing_ids(html: str) -> str:
    """
    Add id attributes and permalinks to existing entries that lack them.
    Idempotent — safe to run on every publish.
    """
    def patch_entry(m: re.Match) -> str:
        date = m.group(1)
        block = m.group(0)
        anchor = nbi.entry_anchor(date)
        # Add id to notebook-entry div if missing
        if f'id="{anchor}"' not in block:
            block = block.replace(
                '<div class="notebook-entry">',
                f'<div class="notebook-entry" id="{anchor}">',
                1,
            )
        # Add permalink to entry-date paragraph if missing
        permalink = f'<a href="#{anchor}" class="entry-permalink" title="Permalink to this entry">§</a>'
        if "entry-permalink" not in block:
            block = re.sub(
                r'(<p class="entry-date">)([^<]+)(</p>)',
                lambda dm: f'{dm.group(1)}{dm.group(2)} {permalink}{dm.group(3)}',
                block,
                count=1,
            )
        return block

    # Match each ENTRY block (from <!-- ENTRY --> to <!-- END ENTRY -->)
    return re.sub(
        r"<!-- ENTRY: (\d{4}-\d{2}-\d{2}) -->.*?<!-- END ENTRY -->",
        patch_entry,
        html,
        flags=re.DOTALL,
    )


# ── Website update ────────────────────────────────────────────────────────────

def _dates_in_html(html: str) -> set[str]:
    return set(re.findall(r"<!-- ENTRY: (\d{4}-\d{2}-\d{2}) -->", html))


def _insert_entries(html: str, new_entries: list[tuple[str, str]]) -> str:
    for _date, entry_html in new_entries:
        idx = html.rfind(_INSERT_BEFORE)
        if idx == -1:
            raise ValueError(f"Could not find insertion point: {_INSERT_BEFORE!r}")
        html = html[:idx] + entry_html + "\n" + html[idx:]
    return html


def publish(dry_run: bool = False, verbose: bool = True) -> list[dict]:
    """
    Main publish function.

    Returns a list of newly published entry dicts (empty if already up to date).
    Each dict has: date, title, tagline, anchor, url.
    """
    if not _NOTEBOOK_HTML.exists():
        print(f"ERROR: website HTML not found at {_NOTEBOOK_HTML}", file=sys.stderr)
        return []

    nb_files = sorted(_NOTEBOOK_DIR.glob("????-??-??.md"))
    if not nb_files:
        print("No notebook entries found.")
        return []

    current_html = _NOTEBOOK_HTML.read_text()
    existing_dates = _dates_in_html(current_html)

    new_entry_html: list[tuple[str, str]] = []
    new_entry_meta: list[dict] = []

    for nb_path in nb_files:
        date_str = nb_path.stem
        if date_str in existing_dates:
            continue
        if verbose:
            print(f"  Rendering {date_str}...")
        try:
            entry_html, title, tagline = render_entry(date_str, nb_path)
            new_entry_html.append((date_str, entry_html))
            new_entry_meta.append({
                "date": date_str,
                "title": title,
                "tagline": tagline,
                "anchor": nbi.entry_anchor(date_str),
                "url": nbi.entry_url(date_str),
            })
            # Update the notebook index
            nbi.upsert_entry(date_str, title=title, tagline=tagline,
                             anchor=nbi.entry_anchor(date_str),
                             file=f"notebook/{date_str}.md")
        except Exception as e:
            print(f"  ERROR rendering {date_str}: {e}", file=sys.stderr)

    if not new_entry_html and not dry_run:
        # Still run migrations and TOC update in case HTML is stale
        pass

    # Apply all transformations to the HTML
    updated_html = current_html
    if new_entry_html:
        updated_html = _insert_entries(updated_html, new_entry_html)
    updated_html = _add_missing_ids(updated_html)
    all_entries = nbi.load()
    updated_html = _update_toc(updated_html, all_entries)

    if updated_html == current_html and not new_entry_html:
        if verbose:
            print("Notebook is up to date — nothing to publish.")
        return []

    if dry_run:
        print("\n[dry-run] Would write updated HTML.")
        if new_entry_meta:
            print(f"New entries: {[e['date'] for e in new_entry_meta]}")
            print("\nFirst new entry preview:\n")
            print(new_entry_html[0][1][:800])
        else:
            print("(HTML migrations/TOC update only)")
        return new_entry_meta

    _NOTEBOOK_HTML.write_text(updated_html)
    if verbose:
        print(f"  Updated {_NOTEBOOK_HTML}")

    dates_str = ", ".join(e["date"] for e in new_entry_meta) if new_entry_meta else "TOC/ID migration"
    commit_msg = (
        f"Humboldt notebook: {dates_str}\n\n"
        f"Auto-published from Protocol-Institute/humboldt\n\n"
        f"Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
    )
    try:
        subprocess.run(["git", "add", str(_NOTEBOOK_HTML)],
                       cwd=_WEBSITE_REPO, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", commit_msg],
                       cwd=_WEBSITE_REPO, check=True, capture_output=True)
        subprocess.run(["git", "push", "origin", "main"],
                       cwd=_WEBSITE_REPO, check=True, capture_output=True)
        if verbose:
            print("  Pushed to website repo — GitHub Pages will deploy automatically.")
    except subprocess.CalledProcessError as e:
        print(f"  ERROR in git operation: {e.stderr.decode()}", file=sys.stderr)
        return []

    if verbose and new_entry_meta:
        print(f"  {len(new_entry_meta)} new entry(ies) published.")
    return new_entry_meta
