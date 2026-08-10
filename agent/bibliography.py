"""
bibliography.py — the canonical bibliography (plan §4.1).

One entry per source Humboldt has ever engaged with past triage-discard, in
``bibliography/bibliography.yaml``. Triage-in creates a ``listed`` entry;
shallow/deep reads upgrade ``read_depth`` and link their output files; law
records cite ``bib-NNNN`` ids.

Entry schema::

    - id: bib-0042
      title: "Dilemmas in a General Theory of Planning"
      authors: [Rittel, Webber]
      year: 1973
      url: ...
      encountered: feed          # feed | discord | operator | citation-chase
      read_depth: deep           # listed | shallow | deep
      kind: content              # content | meta
      notes: bibliography/notes/rittel-webber.md      # if deep
      summary: bibliography/shallow-reads/....md       # if shallow
      laws: [L-003]              # laws citing this source
      connected_raw: [L-003, H-001]   # provenance: original connected-to tags

CLI (wired in humboldt.py):
  humboldt bib list [--depth D] [--kind K] [--year Y]
  humboldt bib show bib-0042
  humboldt bib stats
  humboldt bib migrate [--dry-run]     # one-shot migration from legacy sources
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

from agent import laws as laws_mod
from agent import references as refs_mod

_ROOT = Path(__file__).parent.parent
_BIB_FILE = _ROOT / "bibliography" / "bibliography.yaml"
_NOTES_DIR = _ROOT / "bibliography" / "notes"
_SHALLOW_DIR = _ROOT / "bibliography" / "shallow-reads"

ENCOUNTERED = {"feed", "discord", "operator", "citation-chase"}
READ_DEPTHS = ["listed", "shallow", "deep"]
KINDS = {"content", "meta"}

_FIELD_ORDER = [
    "id", "title", "authors", "year", "url", "encountered",
    "read_depth", "kind", "notes", "summary", "laws", "connected_raw",
]

# Deep reads that are about *how to do research* rather than object-level content.
_META_NOTES = {
    "hamming-you-and-your-research",
    "rao-tempo",
    "kuhn-structure-of-scientific-revolutions",
}

# Legacy artifact ids → current law ids (the unambiguous ones; §3.4).
_OLD_TO_NEW_LAW = {"CL-001": "L-003", "CL-002": "L-006", "CL-003": "L-007"}


# ── File I/O ──────────────────────────────────────────────────────────────────

def load() -> list[dict]:
    if not _BIB_FILE.exists():
        return []
    return yaml.safe_load(_BIB_FILE.read_text()) or []


def save(entries: list[dict]) -> None:
    ordered = [_reorder(e) for e in entries]
    header = (
        "# Humboldt canonical bibliography (redesign 2026-08, §4.1)\n"
        "# One entry per source engaged past triage-discard. Machine-managed by\n"
        "# agent/bibliography.py and the supervisor console; git is the audit trail.\n"
        "# read_depth: listed | shallow | deep   kind: content | meta\n\n"
    )
    _BIB_FILE.write_text(
        header + yaml.dump(ordered, default_flow_style=False,
                           allow_unicode=True, sort_keys=False, width=1000)
    )


def _reorder(e: dict) -> dict:
    out = {k: e[k] for k in _FIELD_ORDER if k in e}
    for k, v in e.items():         # keep any unexpected keys rather than dropping
        if k not in out:
            out[k] = v
    return out


# ── Ids and lookup ────────────────────────────────────────────────────────────

def next_id(entries: list[dict]) -> str:
    used = {int(m.group(1)) for e in entries
            if (m := re.match(r"bib-(\d+)", str(e.get("id", ""))))}
    n = 1
    while n in used:
        n += 1
    return f"bib-{n:04d}"


def _norm_url(url: str | None) -> str:
    if not url:
        return ""
    u = url.strip().lower().rstrip("/")
    u = re.sub(r"^https?://(www\.)?", "", u)
    # arxiv abs/pdf and version suffixes collapse to the same work
    u = re.sub(r"arxiv\.org/(abs|pdf)/", "arxiv.org/", u)
    u = re.sub(r"v\d+$", "", u)
    return u


def _norm_title(title: str | None) -> str:
    if not title:
        return ""
    return re.sub(r"[^a-z0-9]+", "", title.lower())


def _find(entries, url, title):
    """Locate an existing entry by normalised url, else normalised title."""
    nu, nt = _norm_url(url), _norm_title(title)
    if nu:
        for e in entries:
            if _norm_url(e.get("url")) == nu:
                return e
    if nt:
        for e in entries:
            if _norm_title(e.get("title")) == nt:
                return e
    return None


def _depth_rank(d: str) -> int:
    return READ_DEPTHS.index(d) if d in READ_DEPTHS else 0


# ── Upsert ────────────────────────────────────────────────────────────────────

def upsert(
    entries: list[dict],
    *,
    title: str,
    url: str | None = None,
    authors: list[str] | None = None,
    year: int | None = None,
    encountered: str = "operator",
    read_depth: str = "listed",
    kind: str = "content",
    notes: str | None = None,
    summary: str | None = None,
    laws: list[str] | None = None,
    connected_raw: list[str] | None = None,
) -> dict:
    """Add a new entry or upgrade the matching one. Deeper read_depth wins;
    laws/connected_raw unions; notes/summary paths fill in from the deeper read.
    Returns the (new or updated) entry."""
    existing = _find(entries, url, title)
    if existing is None:
        entry = {
            "id": next_id(entries),
            "title": title.strip(),
            "authors": list(authors or []),
            "year": year,
            "url": (url or "").strip(),
            "encountered": encountered if encountered in ENCOUNTERED else "operator",
            "read_depth": read_depth if read_depth in READ_DEPTHS else "listed",
            "kind": kind if kind in KINDS else "content",
            "notes": notes,
            "summary": summary,
            "laws": list(laws or []),
            "connected_raw": list(connected_raw or []),
        }
        entries.append(entry)
        return entry

    # Merge into existing, deepest-wins for read_depth and derived paths.
    if _depth_rank(read_depth) > _depth_rank(existing.get("read_depth", "listed")):
        existing["read_depth"] = read_depth
    if url and not existing.get("url"):
        existing["url"] = url.strip()
    if year and not existing.get("year"):
        existing["year"] = year
    if authors and not existing.get("authors"):
        existing["authors"] = list(authors)
    if notes:
        existing["notes"] = notes
    if summary and not existing.get("summary"):
        existing["summary"] = summary
    if kind == "meta":                       # meta tag is sticky once set
        existing["kind"] = "meta"
    for field, incoming in (("laws", laws), ("connected_raw", connected_raw)):
        if incoming:
            merged = list(dict.fromkeys((existing.get(field) or []) + list(incoming)))
            existing[field] = merged
    return existing


def link_law(bib_id: str, law_id: str) -> bool:
    """Record that ``law_id`` cites ``bib_id``. Returns True if changed.

    ``law_id`` is coerced to a plain ``str`` because callers pass ids read from
    ruamel-loaded law records (ruamel scalar subclasses). This file is dumped
    with PyYAML, which would otherwise serialise a ruamel scalar as an
    unloadable ``!!python/object`` tag and corrupt the bibliography.
    """
    bib_id, law_id = str(bib_id), str(law_id)
    entries = load()
    for e in entries:
        if e.get("id") == bib_id:
            if law_id not in (e.get("laws") or []):
                e.setdefault("laws", []).append(law_id)
                save(entries)
                return True
            return False
    return False


# ── Header parsing for legacy reads ───────────────────────────────────────────

def _first_url(text: str) -> str | None:
    m = re.search(r"https?://\S+", text)
    return m.group(0).rstrip(").,;") if m else None


def _arxiv_year(text: str) -> int | None:
    """arXiv id YYMM.NNNNN → 20YY (e.g. 2605.xxxxx → 2026)."""
    m = re.search(r"\b(\d{2})(\d{2})\.\d{4,5}\b", text)
    if m:
        return 2000 + int(m.group(1))
    return None


def _year_in(text: str) -> int | None:
    m = re.search(r"\b(19|20)\d{2}\b", text)
    return int(m.group(0)) if m else None


def year_from(*texts: str | None) -> int | None:
    """Best-effort publication year from a url/title/source string — arXiv id
    first (it is unambiguous), then a bare four-digit year. Public because the
    funnel stages create bibliography entries at triage time and have only these
    strings to work from."""
    for t in texts:
        if not t:
            continue
        y = _arxiv_year(t)
        if y:
            return y
    for t in texts:
        if t:
            y = _year_in(t)
            if y:
                return y
    return None


def map_law_tokens(raw_tokens: list[str], current_ids: set[str]):
    """Split connected-to tags into (mapped current-law ids, all raw tokens).

    Public because the funnel stages (triage, shallow read) parse the same
    free-form "Connected to:" strings out of model output and must map them the
    same way — legacy CL ids included, since the corpus and the operator still
    use them.
    """
    laws_out, raw_out = [], []
    for tok in raw_tokens:
        tok = tok.strip()
        if not tok or tok.lower().startswith("none"):
            continue
        raw_out.append(tok)
        up = tok.upper()
        if up in _OLD_TO_NEW_LAW:
            laws_out.append(_OLD_TO_NEW_LAW[up])
        elif up in current_ids:
            laws_out.append(up)
    return list(dict.fromkeys(laws_out)), list(dict.fromkeys(raw_out))


def _parse_shallow(path: Path, current_ids: set[str]) -> dict:
    text = path.read_text()
    title_m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else path.stem
    source_m = re.search(r"^\*\*Source:\*\*\s*(.+)$", text, re.MULTILINE)
    source = source_m.group(1).strip() if source_m else ""
    conn_m = re.search(r"^\*\*Connected to:\*\*\s*(.+)$", text, re.MULTILINE)
    raw_tokens = re.split(r"[,\s]+", conn_m.group(1).strip()) if conn_m else []
    mapped, raw = map_law_tokens(raw_tokens, current_ids)
    url = _first_url(source)
    year = _arxiv_year(source) or _arxiv_year(path.name) or _year_in(source)
    return {
        "title": title,
        "url": url,
        "year": year,
        "encountered": "feed",
        "read_depth": "shallow",
        "kind": "content",
        "summary": str(path.relative_to(_ROOT)),
        "laws": mapped,
        "connected_raw": raw,
    }


def _parse_deep(path: Path) -> dict:
    text = path.read_text()
    stem = path.stem
    # Prefer a "Deep Read:" title line; else the first heading that isn't the
    # "Deep Read Notes: Arxiv NNNN" wrapper.
    title = None
    dr = re.search(r"^#+\s*Deep Read:\s*(.+)$", text, re.MULTILINE)
    if dr:
        title = dr.group(1).strip().strip('"')
    else:
        for m in re.finditer(r"^#\s+(.+)$", text, re.MULTILINE):
            h = m.group(1).strip()
            if not re.match(r"(Deep Read Notes|Reading Notes?):?\s*Arxiv", h, re.I):
                title = re.sub(r"^(Deep Read|Reading Notes?)\s*[:\-—]\s*", "", h).strip().strip('"')
                break
    if not title:
        title = stem
    arxiv_m = re.match(r"arxiv-(\d{4}\.\d{4,5})", stem)
    url = f"https://arxiv.org/abs/{arxiv_m.group(1)}" if arxiv_m else _first_url(text)
    # Year from the arXiv id or the title only — a body scan picks up reading-session
    # dates (e.g. "2026-05-28"), which are not the source's publication year.
    year = _arxiv_year(stem) or _year_in(title)
    return {
        "title": title,
        "url": url,
        "year": year,
        "encountered": "feed" if arxiv_m else "operator",
        "read_depth": "deep",
        "kind": "meta" if stem in _META_NOTES else "content",
        "notes": str(path.relative_to(_ROOT)),
    }


# ── Migration ─────────────────────────────────────────────────────────────────

def migrate(dry_run: bool = False, verbose: bool = True) -> dict:
    """One-shot migration of references.yaml + reading notes + shallow-reads
    into the canonical bibliography. Idempotent: re-running upserts by url/title
    rather than duplicating."""
    entries = load()
    current_ids = {l["id"] for l in laws_mod.load_all()}
    counts = {"references": 0, "shallow": 0, "deep": 0, "skipped_discard": 0}

    # 1. references.yaml → listed (skip discards, which are past-triage-out).
    for r in refs_mod.load():
        if r.get("status") == "discard":
            counts["skipped_discard"] += 1
            continue
        src = r.get("source", "") or ""
        enc = "discord" if "discord" in src.lower() else "operator"
        upsert(
            entries,
            title=r.get("title", r.get("id", "untitled")),
            url=r.get("url") or None,
            encountered=enc,
            read_depth="listed",
            kind="content",
        )
        counts["references"] += 1

    # 2. shallow-reads → shallow (skip the _FORMAT template).
    for path in sorted(_SHALLOW_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        upsert(entries, **_parse_shallow(path, current_ids))
        counts["shallow"] += 1

    # 3. deep notes → deep (deepest, wins any prior shallow/listed match).
    for path in sorted(_NOTES_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        upsert(entries, **_parse_deep(path))
        counts["deep"] += 1

    if verbose:
        print(f"\nMigration{' (dry-run)' if dry_run else ''}:")
        print(f"  references.yaml : {counts['references']} listed "
              f"({counts['skipped_discard']} discards skipped)")
        print(f"  shallow-reads   : {counts['shallow']} shallow")
        print(f"  notes           : {counts['deep']} deep")
        print(f"  → {len(entries)} total entries after dedup")

    if not dry_run:
        save(entries)
        # Back-link: for every law a bib entry cites, ensure the law knows? No —
        # laws keep their own `references` free-text; the bib.laws field is the
        # forward index. We stop here to avoid rewriting all 7 law files.
        if verbose:
            print(f"  saved → {_BIB_FILE.relative_to(_ROOT)}")
    return counts


# ── Reference backfill ────────────────────────────────────────────────────────
#
# Law records predating the bibliography carry `references:` as free text
# ("Goodhart (1975)", "OSI vs. TCP/IP comparison literature"). Where such a
# string names a source the bibliography actually holds, it should be a bib-NNNN
# id so the encyclopedia can link it. This is a one-shot repair, deliberately
# conservative: an uncertain match stays free text. Free-text references that
# name a *literature* rather than a work ("Common law precedent literature")
# have no bibliography entry by construction and are expected to survive.

_BACKFILL_RATIO = 0.87     # difflib similarity on normalised titles
_BACKFILL_MIN_LEN = 14     # normalised chars; below this, similarity is noise


_ARXIV_TOKEN = re.compile(r"arxiv[-:\s]?(\d{4}\.\d{4,5})", re.I)
_READFILE_TOKEN = re.compile(r"([\w.-]+\.md)")


def _match_reference(ref: str, entries: list[dict]) -> tuple[dict | None, float, str]:
    """Best bibliography entry for one free-text reference or evidence source.

    Returns ``(entry|None, score, how)``. Identifier hits (arXiv id, read-file
    path, url, exact title) score 1.0; the fuzzy path requires a high title
    similarity on a reference long enough for that similarity to mean something.
    """
    from difflib import SequenceMatcher

    ref = str(ref).strip()
    if not ref:
        return None, 0.0, "empty"
    if re.match(r"seed-\d+", ref):
        # Seed provenance, not a bibliographic source — belongs in `seeds:`.
        return None, 0.0, "seed-ref"

    # 1. arXiv id — the strongest identifier the law records carry.
    am = _ARXIV_TOKEN.search(ref)
    if am:
        hit = _find(entries, f"https://arxiv.org/abs/{am.group(1)}", None)
        if hit is not None:
            return hit, 1.0, "arxiv"

    # 2. A read output path — the entry that already points at that file.
    fm = _READFILE_TOKEN.search(ref)
    if fm:
        fname = fm.group(1)
        for e in entries:
            for field in ("summary", "notes"):
                if str(e.get(field) or "").endswith(fname):
                    return e, 1.0, "read-file"

    url = _first_url(ref)
    exact = _find(entries, url, ref)
    if exact is not None:
        return exact, 1.0, "url" if url else "title"

    nref = _norm_title(ref)
    if len(nref) < _BACKFILL_MIN_LEN:
        return None, 0.0, "too-short"

    best, best_score = None, 0.0
    for e in entries:
        nt = _norm_title(e.get("title"))
        if len(nt) < _BACKFILL_MIN_LEN:
            continue
        score = SequenceMatcher(None, nref, nt).ratio()
        if score > best_score:
            best, best_score = e, score
    if best is not None and best_score >= _BACKFILL_RATIO:
        return best, best_score, "fuzzy"
    return None, best_score, "no-match"


def backfill_law_references(dry_run: bool = False, verbose: bool = True) -> dict:
    """Rewrite free-text law ``references:`` as ``bib-NNNN`` ids where a
    confident bibliography match exists. Unmatched references are left alone.

    Law files go through ``agent/laws.py`` (ruamel round-trip) so comments and
    folded scalars survive; matched pairs are also linked on the bibliography
    side so the forward index stays consistent.
    """
    entries = load()
    stats = {"laws_scanned": 0, "laws_changed": 0, "refs_seen": 0,
             "matched": 0, "already_ids": 0, "unmatched": 0, "sources_matched": 0}
    links: list[tuple[str, str]] = []

    for law in laws_mod.load_all():
        stats["laws_scanned"] += 1
        changed: list[tuple[str, str, float, str]] = []

        def resolve(raw: str, where: str):
            """Try to turn one free-text string into a bib id. Records stats."""
            raw = str(raw).strip()
            if not raw or re.fullmatch(r"bib-\d+", raw):
                if raw:
                    stats["already_ids"] += 1
                return None
            entry, score, how = _match_reference(raw, entries)
            if entry is None:
                stats["unmatched"] += 1
                if verbose and how != "seed-ref":
                    print(f"  · {law['id']} {where:<9} no match ({score:.2f}) — {raw[:62]}")
                return None
            changed.append((raw, entry["id"], score, how))
            links.append((entry["id"], str(law["id"])))
            if verbose:
                print(f"  ✓ {law['id']} {where:<9} {raw[:48]!r} → {entry['id']} "
                      f"({how} {score:.2f}) {str(entry.get('title', ''))[:40]}")
            return entry["id"]

        # 1. references: — the citation list.
        rewritten = []
        for ref in law.get("references") or []:
            stats["refs_seen"] += 1
            hit = resolve(ref, "reference")
            if hit:
                stats["matched"] += 1
            rewritten.append(hit or ref)

        # 2. examples[].source / counterexamples[].source — the schema marks these
        #    "bib-NNNN once bibliography lands; free text until then".
        source_updates: list[tuple[dict, str]] = []
        for field in ("examples", "counterexamples"):
            for ev in law.get(field) or []:
                if not isinstance(ev, dict):
                    continue
                hit = resolve(ev.get("source") or "", field[:9])
                if hit:
                    stats["sources_matched"] += 1
                    source_updates.append((ev, hit))

        # A source resolved on an example is also a citation of the law: fold it
        # into references so the encyclopedia and the bib forward index agree.
        for _, bib_id in source_updates:
            if bib_id not in rewritten:
                rewritten.append(bib_id)

        if not changed:
            continue
        stats["laws_changed"] += 1
        if dry_run:
            continue
        law["references"] = rewritten
        for ev, bib_id in source_updates:
            ev["source"] = bib_id
        detail = "sources resolved to bibliography ids: " + ", ".join(
            f"{old[:40]} → {new}" for old, new, _, _ in changed
        )
        laws_mod.add_history(law, "edited", detail)
        laws_mod.save(law)

    if not dry_run:
        for bib_id, law_id in links:
            for e in entries:
                if e.get("id") == bib_id and law_id not in (e.get("laws") or []):
                    e.setdefault("laws", []).append(law_id)
        if links:
            save(entries)

    if verbose:
        print(f"\nReference backfill{' (dry-run)' if dry_run else ''}:")
        print(f"  laws scanned    : {stats['laws_scanned']} "
              f"({stats['laws_changed']} changed)")
        print(f"  references seen : {stats['refs_seen']} "
              f"({stats['already_ids']} already bib ids)")
        print(f"  references → bib: {stats['matched']}")
        print(f"  ev. sources → bib: {stats['sources_matched']}")
        print(f"  left free text  : {stats['unmatched']}")
    return stats


# ── CLI ───────────────────────────────────────────────────────────────────────

def cmd_list(depth: str | None = None, kind: str | None = None, year: int | None = None) -> None:
    entries = load()
    if depth:
        entries = [e for e in entries if e.get("read_depth") == depth]
    if kind:
        entries = [e for e in entries if e.get("kind") == kind]
    if year:
        entries = [e for e in entries if e.get("year") == year]
    if not entries:
        print("No bibliography entries match.")
        return
    icon = {"listed": "·", "shallow": "◑", "deep": "●"}
    print(f"\nBibliography — {len(entries)} entr{'y' if len(entries)==1 else 'ies'}\n")
    for e in sorted(entries, key=lambda x: (x.get("year") or 0), reverse=True):
        mk = " [meta]" if e.get("kind") == "meta" else ""
        yr = e.get("year") or "----"
        lw = f"  → {','.join(e['laws'])}" if e.get("laws") else ""
        print(f"  {icon.get(e.get('read_depth'), '?')} {e['id']}  ({yr}) {e.get('title', '')[:66]}{mk}{lw}")
    print()


def cmd_show(bib_id: str) -> None:
    for e in load():
        if e.get("id") == bib_id:
            print(yaml.dump(_reorder(e), default_flow_style=False, allow_unicode=True, sort_keys=False))
            return
    print(f"No bibliography entry {bib_id!r}")
    sys.exit(1)


def cmd_stats() -> None:
    entries = load()
    if not entries:
        print("Bibliography is empty. Run `humboldt bib migrate`.")
        return
    by_depth = {d: 0 for d in READ_DEPTHS}
    by_kind = {"content": 0, "meta": 0}
    cited = 0
    for e in entries:
        by_depth[e.get("read_depth", "listed")] = by_depth.get(e.get("read_depth", "listed"), 0) + 1
        by_kind[e.get("kind", "content")] = by_kind.get(e.get("kind", "content"), 0) + 1
        if e.get("laws"):
            cited += 1
    print(f"\nBibliography — {len(entries)} entries")
    print(f"  depth : listed {by_depth['listed']} · shallow {by_depth['shallow']} · deep {by_depth['deep']}")
    print(f"  kind  : content {by_kind['content']} · meta {by_kind['meta']}")
    print(f"  cited by ≥1 law : {cited}\n")
