"""
references.py — reference list management and sorting.

The reference list (bibliography/references.yaml) is the curated layer between
raw Discord captures (inbox/) and deep-read decisions (M-003).

Flow:
  inbox/discord-link-*.md → _promote_inbox_links() → references.yaml [unsorted]
  references.yaml [unsorted] → sort_references() → [read | deep_read | discard+reason]

CLI:
  humboldt references list              # show all references, grouped by status
  humboldt references list --unsorted   # show only unsorted
  humboldt references sort              # classify all unsorted references
  humboldt references sort --dry-run    # preview decisions, no writes
"""

import json
import os
import re
import sys
from datetime import date
from pathlib import Path

import yaml
from anthropic import Anthropic

_ROOT = Path(__file__).parent.parent
_REFS_FILE = _ROOT / "bibliography" / "references.yaml"
_INBOX_DIR = _ROOT / "inbox"
_FAST_MODEL = "claude-haiku-4-5-20251001"
_MAIN_MODEL = "claude-sonnet-4-6"

# Discard reasons (used in prompt and validated on save)
DISCARD_REASONS = {
    "bullshit",
    "irrelevant",
    "duplicate",
    "superseded",
    "too-thin",
    "paywalled",
    "already-known",
}


# ── File I/O ──────────────────────────────────────────────────────────────────

def load() -> list[dict]:
    """Load the full reference list. Returns [] if empty."""
    if not _REFS_FILE.exists():
        return []
    data = yaml.safe_load(_REFS_FILE.read_text()) or {}
    return data.get("references", [])


def save(refs: list[dict]) -> None:
    """Overwrite the reference list."""
    _REFS_FILE.write_text(
        "# Humboldt Reference List\n"
        "# Maintained by daemon/conversation_review.py and agent/references.py.\n"
        "# Do not edit URLs or IDs manually — use `humboldt references sort` to classify.\n"
        "#\n"
        "# Status: unsorted | read | deep_read | discard\n"
        "# Discard reasons: bullshit | irrelevant | duplicate | superseded | "
        "too-thin | paywalled | already-known\n\n"
        + yaml.dump({"references": refs}, default_flow_style=False, allow_unicode=True)
    )


def add_reference(
    title: str,
    url: str | None,
    source: str,
    snippet: str = "",
    ref_type: str = "article",
) -> dict | None:
    """
    Add a reference if not already present (deduplicates by URL).

    Returns the new reference dict, or None if it was a duplicate.
    """
    refs = load()

    # Deduplicate by URL
    if url:
        for r in refs:
            if r.get("url") == url:
                return None

    today = date.today().isoformat()
    idx = len(refs) + 1
    ref_id = f"ref-{today}-{idx:03d}"

    # Avoid ID collisions across days
    existing_ids = {r["id"] for r in refs}
    while ref_id in existing_ids:
        idx += 1
        ref_id = f"ref-{today}-{idx:03d}"

    ref = {
        "id": ref_id,
        "title": title,
        "url": url or "",
        "type": ref_type,
        "added": today,
        "source": source,
        "snippet": snippet[:300],
        "status": "unsorted",
        "sort_reason": "",
        "sort_date": None,
        "sort_notes": "",
    }
    refs.append(ref)
    save(refs)
    return ref


# ── Inbox promotion ───────────────────────────────────────────────────────────

def promote_inbox_links(since_date: str | None = None, verbose: bool = False) -> int:
    """
    Scan inbox/discord-link-*.md files and add unseen URLs to references.yaml.

    since_date: YYYY-MM-DD string; skip files older than this.
    Returns the count of new references added.
    """
    added = 0
    pattern = re.compile(r"\*\*URL:\*\*\s*(\S+)")
    title_pattern = re.compile(r"^#\s+(?:Link|Idea|link|idea)?:?\s*(.+)$", re.MULTILINE)
    relevance_pattern = re.compile(r"\*\*Relevance:\*\*\s*(.+)")
    source_pattern = re.compile(r"\*\*Source:\*\*\s*(.+)")

    for path in sorted(_INBOX_DIR.glob("discord-link-*.md")):
        # Filter by date if requested
        if since_date:
            # Filename: discord-link-YYYY-MM-DD-HHMM-slug.md
            parts = path.stem.split("-")
            if len(parts) >= 4:
                file_date = "-".join(parts[2:5])  # YYYY-MM-DD
                if file_date < since_date:
                    continue

        try:
            text = path.read_text()
            url_match = pattern.search(text)
            if not url_match:
                continue
            url = url_match.group(1).strip()

            title_match = title_pattern.search(text)
            title = title_match.group(1).strip() if title_match else path.stem

            relevance_match = relevance_pattern.search(text)
            snippet = relevance_match.group(1).strip() if relevance_match else ""

            source_match = source_pattern.search(text)
            source = source_match.group(1).strip() if source_match else "Discord"

            ref = add_reference(
                title=title,
                url=url,
                source=source,
                snippet=snippet,
            )
            if ref:
                added += 1
                if verbose:
                    print(f"  + {title[:60]}")
        except Exception as e:
            if verbose:
                print(f"  ! Error reading {path.name}: {e}", file=sys.stderr)

    return added


# ── Sorting ───────────────────────────────────────────────────────────────────

def _research_context() -> str:
    """Load active hypotheses and laws for the sort prompt."""
    hyp_dir = _ROOT / "research" / "hypotheses"
    hyp_lines = []
    for f in sorted(hyp_dir.glob("*.yaml")):
        try:
            h = yaml.safe_load(f.read_text())
            if h.get("status") == "active":
                hyp_lines.append(f"  {h.get('id')}: {h.get('question', '')[:120]}")
        except Exception:
            pass

    laws_dir = _ROOT / "research" / "laws"
    law_lines = []
    for f in sorted(laws_dir.glob("*.yaml")):
        try:
            law = yaml.safe_load(f.read_text())
            law_lines.append(f"  {law.get('id')}: {law.get('name')}")
        except Exception:
            pass

    return (
        "Active hypotheses:\n" + ("\n".join(hyp_lines) if hyp_lines else "  (none)") +
        "\n\nCurrent law inventory:\n" + ("\n".join(law_lines) if law_lines else "  (none)")
    )


_SORT_PROMPT = """\
You are Humboldt's reading prioritization system, implementing M-004.

Classify each reference into one of:
  read       — worth a light scan; may be relevant but not a deep-read candidate
  deep_read  — meets ≥3 M-003 criteria; should be queued for full deep reading
  discard    — reject; must provide a sort_reason

M-003 deep read criteria (a source qualifies for deep_read if it meets ≥3):
  1. Foundational to a tradition Humboldt could inhabit
  2. Conceptually productive for new-nature research (direct structural relevance)
  3. Cross-domain by design (author explicitly reasons across domain boundaries)
  4. Analytically transferable (methods, not just conclusions, are applicable)
  5. Intellectually alive (still generating live debate or new research)

Discard reasons (use exactly one of these strings):
  bullshit      — low epistemic quality, hype, or unfounded claims
  irrelevant    — no connection to the research agenda
  duplicate     — already covered by an existing reference in the list
  superseded    — older version; a better source already exists
  too-thin      — interesting idea but not enough substance to read
  paywalled     — inaccessible and not worth pursuing
  already-known — adds no new information to what Humboldt already holds

Be conservative with deep_read — it commits to a tradition and shapes all subsequent
reasoning. Be rigorous with discards — log the specific honest reason. When in doubt
between read and discard, prefer read.

{context}

References to sort:
{batch}

Return a JSON array with one object per reference:
[
  {{
    "id": "<ref-id>",
    "status": "read" | "deep_read" | "discard",
    "sort_reason": "<discard reason string, or empty string if not discard>",
    "sort_notes": "<1-2 sentences explaining the decision>"
  }},
  ...
]

Return only valid JSON — no markdown fences, no commentary."""


def sort_references(dry_run: bool = False, verbose: bool = True, batch_size: int = 8) -> dict:
    """
    Classify all unsorted references using Sonnet.

    Returns a summary dict: {total, classified, discarded, read, deep_read, errors}.
    """
    refs = load()
    unsorted = [r for r in refs if r.get("status") == "unsorted"]

    if not unsorted:
        if verbose:
            print("No unsorted references.")
        return {"total": len(refs), "classified": 0}

    if verbose:
        print(f"\nSorting {len(unsorted)} unsorted reference(s)...\n")

    context = _research_context()
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    today = date.today().isoformat()

    results_map: dict[str, dict] = {}
    errors = 0

    for i in range(0, len(unsorted), batch_size):
        batch = unsorted[i : i + batch_size]
        batch_text = json.dumps(
            [{"id": r["id"], "title": r["title"], "url": r.get("url", ""), "snippet": r.get("snippet", "")}
             for r in batch],
            indent=2,
        )

        prompt = _SORT_PROMPT.format(context=context, batch=batch_text)

        try:
            resp = client.messages.create(
                model=_MAIN_MODEL,
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}],
            )
            raw = resp.content[0].text.strip()
            raw = re.sub(r"^```(?:json)?\s*", "", raw)
            raw = re.sub(r"\s*```\s*$", "", raw)
            decisions = json.loads(raw)
        except Exception as e:
            print(f"  ERROR in batch {i//batch_size + 1}: {e}", file=sys.stderr)
            errors += 1
            continue

        for decision in decisions:
            ref_id = decision.get("id")
            if ref_id:
                results_map[ref_id] = decision

    # Apply decisions
    classified = read_count = deep_count = discard_count = 0

    for r in refs:
        decision = results_map.get(r["id"])
        if not decision:
            continue

        status = decision.get("status", "read")
        sort_reason = decision.get("sort_reason", "")
        sort_notes = decision.get("sort_notes", "")

        # Validate discard reason
        if status == "discard" and sort_reason not in DISCARD_REASONS:
            sort_reason = "irrelevant"  # safe fallback

        if verbose:
            icon = {"read": "📖", "deep_read": "📚", "discard": "🗑"}.get(status, "?")
            label = f"[{sort_reason}]" if status == "discard" else ""
            print(f"  {icon} {status.upper()} {label}")
            print(f"     {r['title'][:70]}")
            if sort_notes:
                print(f"     {sort_notes[:100]}")
            print()

        classified += 1
        if status == "read":
            read_count += 1
        elif status == "deep_read":
            deep_count += 1
        elif status == "discard":
            discard_count += 1

        if not dry_run:
            r["status"] = status
            r["sort_reason"] = sort_reason
            r["sort_date"] = today
            r["sort_notes"] = sort_notes

    if not dry_run and classified > 0:
        save(refs)
        if verbose:
            print(f"Saved. {classified} classified: {read_count} read, {deep_count} deep_read, {discard_count} discard.")
    elif dry_run and verbose:
        print(f"[dry-run] Would classify {classified}: {read_count} read, {deep_count} deep_read, {discard_count} discard.")

    return {
        "total": len(refs),
        "classified": classified,
        "read": read_count,
        "deep_read": deep_count,
        "discarded": discard_count,
        "errors": errors,
    }


# ── CLI display ───────────────────────────────────────────────────────────────

def cmd_list(unsorted_only: bool = False) -> None:
    """Display the reference list grouped by status."""
    refs = load()
    if not refs:
        print("Reference list is empty.")
        return

    groups: dict[str, list] = {"unsorted": [], "deep_read": [], "read": [], "discard": []}
    for r in refs:
        groups.setdefault(r.get("status", "unsorted"), []).append(r)

    order = ["unsorted", "deep_read", "read", "discard"] if not unsorted_only else ["unsorted"]

    total = 0
    for status in order:
        items = groups.get(status, [])
        if not items:
            continue
        if unsorted_only and status != "unsorted":
            continue
        print(f"\n[{status.upper()}] — {len(items)}")
        for r in items:
            reason = f" [{r.get('sort_reason')}]" if status == "discard" else ""
            print(f"  {r['id']}  {r['title'][:65]}{reason}")
            if r.get("url"):
                print(f"            {r['url'][:70]}")
        total += len(items)

    if not unsorted_only:
        print(f"\nTotal: {total}")
