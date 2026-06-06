"""
publish_architecture.py — render ARCHITECTURE.md to the PI website.

Usage:
    python3 -m agent.humboldt publish-architecture
    python3 -m agent.humboldt publish-architecture --dry-run
"""

import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import markdown as md_lib

_ROOT = Path(__file__).parent.parent
_WEBSITE_REPO = _ROOT.parent / "website"
_OUTPUT_DIR = _WEBSITE_REPO / "humboldt-architecture"
_OUTPUT_HTML = _OUTPUT_DIR / "index.html"

_ARCH_MD = _ROOT / "ARCHITECTURE.md"


def _render(text: str) -> str:
    html = md_lib.markdown(text, extensions=["tables", "fenced_code"])
    # Demote h1→h2, h2→h3 so page h1 title stays dominant
    html = html.replace("<h1>", "<h2>").replace("</h1>", "</h2>")
    html = html.replace("<h2>", "<h3>").replace("</h2>", "</h3>")
    return html


_PAGE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Humboldt Architecture — The Protocol Institute</title>
  <meta name="description" content="How Humboldt works — persona assembly, behavior inventory, research schema, data flow, and daemon layer.">
  <link rel="icon" href="/assets/logo-static.png" type="image/png">
  <link rel="stylesheet" href="/css/style.css">
  <style>
    .arch-body h3 {{ margin-top: 2rem; margin-bottom: 0.5rem; }}
    .arch-body h4 {{ margin-top: 1.5rem; margin-bottom: 0.4rem; font-size: 1rem; }}
    .arch-body p  {{ margin-bottom: 0.9rem; color: #2C2C2C; }}
    .arch-body ul, .arch-body ol {{ padding-left: 1.4rem; margin-bottom: 1rem; color: #2C2C2C; }}
    .arch-body li {{ margin-bottom: 0.3rem; }}
    .arch-body pre {{
      background: #f5f5f2;
      border: 1px solid #ddd;
      border-radius: 4px;
      padding: 1rem 1.25rem;
      overflow-x: auto;
      font-size: 0.83rem;
      margin-bottom: 1.25rem;
    }}
    .arch-body code {{
      font-family: 'SFMono-Regular', Consolas, monospace;
      font-size: 0.84rem;
      background: #f5f5f2;
      padding: 0.1em 0.35em;
      border-radius: 3px;
    }}
    .arch-body pre code {{ background: none; padding: 0; }}
    .arch-body table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.25rem;
      font-size: 0.9rem;
    }}
    .arch-body th {{
      text-align: left;
      padding: 0.45rem 0.75rem;
      border-bottom: 2px solid #ddd;
      font-weight: 600;
    }}
    .arch-body td {{
      padding: 0.4rem 0.75rem;
      border-bottom: 1px solid #eee;
      vertical-align: top;
    }}
    .arch-body blockquote {{
      border-left: 3px solid #2A6B6B;
      padding: 0.5rem 1rem;
      margin: 1rem 0;
      background: #f5f5f2;
      color: #555;
    }}
    .arch-body hr {{ border: none; border-top: 1px solid #ddd; margin: 2rem 0; }}
    .arch-nav {{
      font-size: 0.88rem;
      margin-bottom: 2rem;
      color: #666;
    }}
    .arch-nav a {{ color: #2A6B6B; text-decoration: none; }}
    .arch-nav a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>

<div class="interior-wrapper">

  <header id="site-header"></header>

  <main class="interior-main">
    <div class="container">

      <div class="page-header">
        <h1>Humboldt Architecture</h1>
      </div>

      <p class="arch-nav">
        <a href="/humboldt/">← Humboldt</a> &nbsp;·&nbsp;
        <a href="/humboldt-notebook/">Lab Notebook</a> &nbsp;·&nbsp;
        <a href="/humboldt-reading/">Reading Notes</a> &nbsp;·&nbsp;
        <a href="/humboldt-behaviors/">Behaviors</a> &nbsp;·&nbsp;
        <a href="/humboldt-research/">Research Status</a>
      </p>

      <div class="arch-body">
        {body}
      </div>

      <p style="margin-top:3rem;font-size:0.8rem;color:#aaa;">Generated {date}</p>

    </div>
  </main>

</div>

<script src="/js/header.js"></script>
</body>
</html>
"""


def publish_architecture(dry_run: bool = False) -> None:
    arch_text = _ARCH_MD.read_text()
    # Remove the leading # Architecture heading — it's in the page h1
    import re
    arch_text = re.sub(r"^# Architecture.*\n+", "", arch_text, count=1)
    body_html = _render(arch_text)

    date = datetime.now(timezone.utc).strftime("%-d %B %Y")
    html = _PAGE.format(body=body_html, date=date)

    if dry_run:
        print(f"[dry-run] Would write {len(html):,} chars to {_OUTPUT_HTML}")
        return

    _OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    _OUTPUT_HTML.write_text(html, encoding="utf-8")
    print(f"Written: {_OUTPUT_HTML} ({len(html):,} chars)")

    try:
        subprocess.run(["git", "add", str(_OUTPUT_HTML)], cwd=_WEBSITE_REPO, check=True)
        msg = f"Humboldt architecture page ({datetime.now().strftime('%Y-%m-%d')})"
        subprocess.run(["git", "commit", "-m", msg], cwd=_WEBSITE_REPO, check=True)
        subprocess.run(["git", "push"], cwd=_WEBSITE_REPO, check=True)
        print("Pushed to website repo.")
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}", file=sys.stderr)
