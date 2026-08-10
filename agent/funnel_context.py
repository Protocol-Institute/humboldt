"""
funnel_context.py — the research context the early funnel stages think against.

Triage (stage 2) and shallow read (stage 3) both need the same orientation: what
laws currently exist, which of them are still open lines of inquiry, and what is
sitting in the seed pool. Before the 2026-08 redesign each module hand-rolled its
own loader against ``research/laws/`` and ``research/hypotheses/`` — directories
that no longer exist. This module is the single replacement, reading the live
sources: ``laws/L-*.yaml`` (via ``agent/laws.py``) and ``laws/seeds/``.

There is no separate "hypothesis" artifact post-redesign. The nearest equivalent
is a law still at ``exploration``/``sensemaking`` stage: registered, mechanism
not yet settled, actively being worked. Those are presented to the models as the
open questions; ``valley`` and beyond are presented as the standing inventory.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from agent import laws as laws_mod

_ROOT = Path(__file__).parent.parent
_SEEDS_DIR = _ROOT / "laws" / "seeds"

# Stages at which a law is still an open line of inquiry rather than a standing
# claim — the post-redesign analogue of "active hypotheses".
OPEN_STAGES = {"exploration", "sensemaking"}


def load_open_seeds() -> list[dict]:
    """Seeds still in the pool (status ``open`` or unset), newest surfaced first."""
    seeds = []
    for f in sorted(_SEEDS_DIR.glob("seed-*.yaml")):
        try:
            s = yaml.safe_load(f.read_text()) or {}
        except Exception:  # noqa: BLE001 — a malformed seed must not block the funnel
            continue
        if s.get("status", "open") == "open":
            seeds.append(s)
    seeds.sort(key=lambda s: str(s.get("surfaced", "")), reverse=True)
    return seeds


def next_seed_id() -> str:
    """One past the highest ``seed-NNN`` ever issued.

    Deliberately *not* lowest-unused: the migrated pool (seed-001..057, 47 files)
    has gaps, and law records cite seed ids in their ``seeds:`` field. Refilling
    a gap would silently re-point an existing citation at unrelated material.
    Law ids referenced by law records are counted as issued for the same reason.
    """
    highest = 0
    for f in _SEEDS_DIR.glob("seed-*.yaml"):
        m = re.match(r"seed-(\d+)", f.stem)
        if m:
            highest = max(highest, int(m.group(1)))
    for law in laws_mod.load_all():
        for cited in law.get("seeds") or []:
            m = re.match(r"seed-(\d+)", str(cited))
            if m:
                highest = max(highest, int(m.group(1)))
    return f"seed-{highest + 1:03d}"


def current_law_ids() -> set[str]:
    return {str(law.get("id")) for law in laws_mod.load_all() if law.get("id")}


def research_context(
    *,
    statement_chars: int = 110,
    max_seeds: int = 25,
    laws: list | None = None,
) -> str:
    """Render the law inventory + seed pool as prompt context.

    ``laws`` may be passed in when the caller already loaded them (the sweeps do,
    to avoid re-parsing every record per batch).
    """
    laws = laws_mod.load_all() if laws is None else laws
    open_laws, standing = [], []
    for law in laws:
        stmt = str(law.get("statement", "")).strip().replace("\n", " ")
        line = (f"  {law.get('id')} [{law.get('stage')}] {law.get('title', '')} — "
                f"{stmt[:statement_chars]}")
        (open_laws if law.get("stage") in OPEN_STAGES else standing).append(line)

    seeds = load_open_seeds()
    seed_lines = [f"  {s.get('id')}: {str(s.get('title', '')).strip()[:90]}"
                  for s in seeds[:max_seeds]]

    parts = [
        "LAWS UNDER ACCUMULATION (valley and beyond — statements the funnel is "
        "gathering evidence for or against):",
        "\n".join(standing) or "  (none yet)",
        "",
        "OPEN LINES OF INQUIRY (exploration/sensemaking-stage laws — mechanism not "
        "yet settled; the live questions):",
        "\n".join(open_laws) or "  (none yet)",
        "",
        f"SEED POOL ({len(seeds)} open law-shaped fragments awaiting induction"
        + (f"; {max_seeds} most recent shown" if len(seeds) > max_seeds else "")
        + "):",
        "\n".join(seed_lines) or "  (empty)",
    ]
    return "\n".join(parts)
