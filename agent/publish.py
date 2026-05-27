"""
publish.py — render Humboldt lab notebook entries to the PI website.

Reads all notebook/YYYY-MM-DD.md files, converts any that are not yet
present in humboldt-notebook.html, inserts them in chronological order,
then commits and pushes the website repo.

Usage (CLI):
    python3 -m agent.humboldt publish              # render + push
    python3 -m agent.humboldt publish --dry-run    # render only, no git ops

Entries are inserted newest-last (chronological reading order).

Notebook markdown convention:
  Line 1:  # Lab Notebook — YYYY-MM-DD
  Line 2:  *Short tagline sentence.*
  Body:    ## Section headers, paragraphs, **bold**, *italic*, lists
  Title:   First ## heading is used as the page h2 title.
           Override with a YAML-style comment on line 3:
             <!-- title: Custom Title Here -->
"""

import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import markdown as md_lib

_ROOT = Path(__file__).parent.parent
_NOTEBOOK_DIR = _ROOT / "notebook"

# Path to the PI website repo (sibling directory)
_WEBSITE_REPO = _ROOT.parent / "website"
_NOTEBOOK_HTML = _WEBSITE_REPO / "humboldt-notebook.html"

# Marker used to locate existing entries
_ENTRY_MARKER = "<!-- ENTRY: {date} -->"
_INSERT_BEFORE = "      </div>\n    </div>\n  </main>"


# ── Markdown → HTML ───────────────────────────────────────────────────────────

def _convert_body(body_md: str) -> str:
    """Convert notebook markdown body to HTML, demoting headings by one level."""
    html = md_lib.markdown(
        body_md,
        extensions=["tables", "fenced_code"],
    )
    # ## → h3, ### → h4  (h2 is reserved for the entry title on the page)
    html = html.replace("<h2>", "<h3>").replace("</h2>", "</h3>")
    html = html.replace("<h3>", "\n          <h3>").replace("</h3>", "</h3>\n")
    html = html.replace("<p>", "\n          <p>").replace("</p>", "</p>\n")
    html = html.replace("<ul>", "\n          <ul>").replace("</ul>", "          </ul>\n")
    html = html.replace("<ol>", "\n          <ol>").replace("</ol>", "          </ol>\n")
    html = html.replace("<li>", "            <li>").replace("</li>", "</li>")
    html = html.replace("<hr />", "")  # drop horizontal rules (used as section dividers)
    html = html.replace("<hr>", "")
    # Clean up multiple blank lines produced by the above
    html = re.sub(r"\n{3,}", "\n\n", html)
    return html.strip()


def render_entry(date_str: str, md_path: Path) -> str:
    """
    Render a single notebook markdown file to a complete HTML entry block.

    Returns the full string including <!-- ENTRY: date --> markers.
    """
    raw = md_path.read_text()
    lines = raw.split("\n")

    # --- Extract metadata from header lines ---
    tagline = ""
    title_override = ""
    body_start = 1  # skip line 0 (# Lab Notebook — YYYY-MM-DD)

    for i, line in enumerate(lines[1:], start=1):
        stripped = line.strip()
        # Tagline: italic line before first section
        if not tagline and stripped.startswith("*") and stripped.endswith("*") and len(stripped) > 2:
            tagline = stripped[1:-1]
            body_start = i + 1
            continue
        # Optional title override comment
        m = re.match(r"<!--\s*title:\s*(.+?)\s*-->", stripped)
        if m:
            title_override = m.group(1)
            body_start = i + 1
            continue
        # Stop scanning header on first real content or ---
        if stripped and stripped != "---":
            body_start = i
            break

    body_md = "\n".join(lines[body_start:])

    # --- Derive title ---
    if title_override:
        title = title_override
    else:
        # Use the first ## heading in the body
        m = re.search(r"^##\s+(.+)$", body_md, re.MULTILINE)
        title = m.group(1).strip() if m else f"Session {date_str}"

    # --- Format display date ---
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    display_date = dt.strftime("%B %-d, %Y")  # e.g. "May 26, 2026"

    body_html = _convert_body(body_md)

    return (
        f"\n        <!-- ENTRY: {date_str} -->\n"
        f"        <div class=\"notebook-entry\">\n\n"
        f"          <p class=\"entry-date\">{display_date}</p>\n"
        f"          <h2>{title}</h2>\n"
        + (f"          <p class=\"entry-tagline\">{tagline}</p>\n" if tagline else "")
        + f"\n{body_html}\n\n"
        f"        </div>\n"
        f"        <!-- END ENTRY -->\n"
    )


# ── Website update ────────────────────────────────────────────────────────────

def _dates_in_html(html: str) -> set[str]:
    """Return set of YYYY-MM-DD dates already present as entries in the HTML."""
    return set(re.findall(r"<!-- ENTRY: (\d{4}-\d{2}-\d{2}) -->", html))


def _insert_entries(html: str, new_entries: list[tuple[str, str]]) -> str:
    """
    Insert new (date, entry_html) tuples into the HTML in chronological order.

    Entries are added just before the closing about-body div.
    """
    for _date, entry_html in new_entries:
        # Insert before the page-closing wrapper
        idx = html.rfind(_INSERT_BEFORE)
        if idx == -1:
            raise ValueError(f"Could not find insertion point in HTML:\n  {_INSERT_BEFORE!r}")
        html = html[:idx] + entry_html + "\n" + html[idx:]
    return html


def publish(dry_run: bool = False, verbose: bool = True) -> int:
    """
    Main publish function.

    Returns the number of new entries published (0 if already up to date).
    """
    if not _NOTEBOOK_HTML.exists():
        print(f"ERROR: website HTML not found at {_NOTEBOOK_HTML}", file=sys.stderr)
        return 0

    # Discover notebook entries
    nb_files = sorted(_NOTEBOOK_DIR.glob("????-??-??.md"))
    if not nb_files:
        print("No notebook entries found.")
        return 0

    current_html = _NOTEBOOK_HTML.read_text()
    existing_dates = _dates_in_html(current_html)

    new_entries: list[tuple[str, str]] = []
    for nb_path in nb_files:
        date_str = nb_path.stem  # YYYY-MM-DD
        if date_str in existing_dates:
            continue
        if verbose:
            print(f"  Rendering {date_str}...")
        try:
            entry_html = render_entry(date_str, nb_path)
            new_entries.append((date_str, entry_html))
        except Exception as e:
            print(f"  ERROR rendering {date_str}: {e}", file=sys.stderr)

    if not new_entries:
        if verbose:
            print("Notebook is up to date — nothing to publish.")
        return 0

    if verbose:
        print(f"  {len(new_entries)} new entry(ies): {[d for d, _ in new_entries]}")

    updated_html = _insert_entries(current_html, new_entries)

    if dry_run:
        print("\n[dry-run] Would write updated HTML. First new entry preview:\n")
        print(new_entries[0][1][:800])
        return len(new_entries)

    _NOTEBOOK_HTML.write_text(updated_html)
    if verbose:
        print(f"  Updated {_NOTEBOOK_HTML}")

    # Commit and push website repo
    dates_str = ", ".join(d for d, _ in new_entries)
    commit_msg = (
        f"Humboldt notebook: add {dates_str}\n\n"
        f"Auto-published from Protocol-Institute/humboldt\n\n"
        f"Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
    )
    try:
        subprocess.run(
            ["git", "add", str(_NOTEBOOK_HTML)],
            cwd=_WEBSITE_REPO, check=True, capture_output=True,
        )
        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=_WEBSITE_REPO, check=True, capture_output=True,
        )
        subprocess.run(
            ["git", "push", "origin", "main"],
            cwd=_WEBSITE_REPO, check=True, capture_output=True,
        )
        if verbose:
            print(f"  Pushed to website repo — Netlify will deploy automatically.")
    except subprocess.CalledProcessError as e:
        print(f"  ERROR in git operation: {e.stderr.decode()}", file=sys.stderr)
        return 0

    return len(new_entries)
