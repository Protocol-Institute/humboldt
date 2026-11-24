"""Shared helpers for the site-chat probe and A/B harness (admin-gated endpoint)."""
from __future__ import annotations

import json
import os
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL = os.environ.get("HUMBOLDT_CHAT_URL", "https://humboldt.protocol-institute.org/chat")
# Cloudflare answers urllib's default User-Agent with error 1010.
UA = "humboldt-probe/1.0"


def admin_key() -> str:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
    key = os.environ.get("CHAT_ADMIN_KEY", "")
    if len(key) < 32:
        raise SystemExit("CHAT_ADMIN_KEY missing from .env (see .env.template).")
    return key


def ask(query: str, *, key: str, variant: str | None = None, now: str | None = None,
        sources_only: bool = False, history: list | None = None, timeout: int = 120) -> dict:
    body = {"query": query, "history": history or []}
    if variant:
        body["variant"] = variant
    if now:
        body["now"] = now
    if sources_only:
        body["mode"] = "sources"
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), method="POST",
                                 headers={"Content-Type": "application/json",
                                          "User-Agent": UA, "X-Admin-Key": key})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as r:
        out = json.loads(r.read())
    out["_wall_s"] = round(time.time() - t0, 2)
    return out
