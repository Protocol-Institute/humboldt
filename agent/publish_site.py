"""Build and deploy the Humboldt standalone subsite to Cloudflare Pages.

Runs humboldt-site/build.py (generates dist/) then deploys via wrangler.
All pages (notebook, research, reading, architecture, about, chat) are rebuilt
and deployed in a single operation.

Usage (CLI):
    python3 -m agent.humboldt publish-site
    python3 -m agent.humboldt publish-site --dry-run   # build only, no deploy
"""

import os
import subprocess
from pathlib import Path

_ROOT = Path(__file__).parent.parent
_SITE = _ROOT / "humboldt-site"
_VENV_PYTHON = _ROOT / ".venv" / "bin" / "python3"
_PYTHON = str(_VENV_PYTHON) if _VENV_PYTHON.exists() else "/opt/homebrew/bin/python3"
_CF_ACCOUNT_ID = "7e8c7969b2464d23795c555bc6a32af8"
_CF_PROJECT = "humboldt"


def publish_site(dry_run: bool = False, verbose: bool = True) -> bool:
    """Build the subsite and deploy to CF Pages. Returns True on success."""

    def log(msg):
        if verbose:
            print(msg)

    result = subprocess.run([_PYTHON, "build.py"], cwd=_SITE)
    if result.returncode != 0:
        log(f"Build failed (exit {result.returncode})")
        return False

    if dry_run:
        log("Dry run — skipping deploy.")
        return True

    api_token = os.environ.get("CLOUDFLARE_API_TOKEN")
    if not api_token:
        log("CLOUDFLARE_API_TOKEN not set — cannot deploy.")
        return False

    env = {
        **os.environ,
        "CLOUDFLARE_API_TOKEN": api_token,
        "CLOUDFLARE_ACCOUNT_ID": os.environ.get("CLOUDFLARE_ACCOUNT_ID", _CF_ACCOUNT_ID),
    }

    log(f"Deploying to CF Pages ({_CF_PROJECT})...")
    result = subprocess.run(
        ["npx", "wrangler", "pages", "deploy", "dist", "--project-name", _CF_PROJECT],
        cwd=_SITE,
        env=env,
    )
    if result.returncode != 0:
        log(f"Deploy failed (exit {result.returncode})")
        return False

    log("Deployed → humboldt.protocol-institute.org")
    return True
