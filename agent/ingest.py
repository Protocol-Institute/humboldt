"""Ingest Humboldt's own documents into the dedicated humboldt Pinecone index.

Covers: notebook entries, deep-read notes, shallow reads, law records, and
Discord inbox ideas. Each vector carries augmented metadata so retrieved
results are self-identifying in Claude prompts.

Incremental — a content hash per chunk (data/ingest_state.json) means only
new/changed chunks are re-embedded and upserted, and chunks whose source file
disappeared are deleted. Pass force=True to re-embed everything regardless.

Run via: python3 -m agent.humboldt ingest

Fixed 2026-09-12: the 2026-08 redesign retired the C/H/CL/T/F schema (research/c/,
research/cl/, research/h/, research/f/, research/ds/ — all archived to
research/_archive/) and replaced it with the unified law record (laws/L-*.yaml),
but nothing carried the corresponding _cl_chunks()-style embedding forward. Every
law created since the merge was therefore invisible to corpus retrieval —
agent/induct.py's own comment ("the ingest embedded it") and its post-sweep
instruction to run `humboldt ingest` were both describing behavior that had quietly
stopped happening. _law_chunks() below replaces the five now-permanently-empty
_curiosity_chunks/_cl_chunks/_h_chunks/_f_chunks/_ds_chunks functions, which read
directories that will never hold files again — deleted rather than kept as
always-empty dead weight.
"""

import hashlib
import json
import os
import re
from pathlib import Path

import voyageai
from pinecone import Pinecone

_ROOT = Path(__file__).parent.parent
_NAMESPACE = ""  # dedicated index — default namespace
_VOYAGE_MODEL = "voyage-3"
_BATCH_SIZE = 96  # voyage-3 max batch
_STATE_PATH = _ROOT / "data" / "ingest_state.json"  # chunk id -> content hash


def _voyage_client() -> voyageai.Client:
    return voyageai.Client(api_key=os.environ["VOYAGE_API_KEY"])


def _pinecone_index():
    pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
    return pc.Index(host=os.environ["PINECONE_HUMBOLDT_HOST"])


def _slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:60]


def _chunk_markdown(text: str) -> list[tuple[str, str]]:
    """Split on ## headers. Returns [(section_title, body), ...]."""
    parts = re.split(r"^(##\s+.+)$", text, flags=re.MULTILINE)
    chunks: list[tuple[str, str]] = []

    intro = parts[0].strip()
    if intro:
        title_match = re.search(r"^#\s+(.+)$", intro, re.MULTILINE)
        section_title = title_match.group(1).strip() if title_match else "Introduction"
        intro_body = re.sub(r"^#\s+.+\n?", "", intro, count=1).strip()
        if intro_body:
            chunks.append((section_title, intro_body))

    i = 1
    while i < len(parts) - 1:
        section_title = parts[i].lstrip("#").strip()
        body = parts[i + 1].strip()
        if body:
            chunks.append((section_title, body))
        i += 2

    return chunks


def _notebook_chunks() -> list[dict]:
    nb_dir = _ROOT / "notebook"
    chunks = []
    for path in sorted(nb_dir.glob("????-??-??.md")):
        date_str = path.stem
        text = path.read_text()
        title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        doc_title = title_match.group(1).strip() if title_match else f"Lab Notebook {date_str}"

        for section_title, body in _chunk_markdown(text):
            embed_text = f"Lab Notebook {date_str} — {section_title}\n\n{body}"
            chunk_id = f"humboldt-notebook-{date_str}-{_slugify(section_title)}"
            chunks.append({
                "id": chunk_id,
                "text": embed_text,
                "metadata": {
                    "type": "notebook",
                    "title": f"Lab Notebook {date_str} — {section_title}",
                    "date": date_str,
                    "doc_title": doc_title,
                    "section": section_title,
                    "source_file": f"notebook/{path.name}",
                    "text": embed_text[:2000],
                },
            })
    return chunks


def _notes_chunks() -> list[dict]:
    notes_dir = _ROOT / "bibliography" / "notes"
    chunks = []
    for path in sorted(notes_dir.glob("*.md")):
        text = path.read_text()
        title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        doc_title = title_match.group(1).strip() if title_match else path.stem

        for section_title, body in _chunk_markdown(text):
            embed_text = f"Reading Notes — {doc_title}: {section_title}\n\n{body}"
            chunk_id = f"humboldt-notes-{_slugify(path.stem)}-{_slugify(section_title)}"
            chunks.append({
                "id": chunk_id,
                "text": embed_text,
                "metadata": {
                    "type": "notes",
                    "title": f"Notes: {doc_title} — {section_title}",
                    "doc_title": doc_title,
                    "section": section_title,
                    "source_file": f"bibliography/notes/{path.name}",
                    "text": embed_text[:2000],
                },
            })
    return chunks


def _law_chunks() -> list[dict]:
    """Embed each law record (laws/L-*.yaml) — the unified research artifact
    that replaced C (Curiosity), CL (Candidate Law), H (Hypothesis), and F
    (Falsification Monitor). One chunk per law, matching the old _cl_chunks()
    granularity — a law record is short enough that splitting it by section
    would fragment the mechanism from the statement it explains."""
    from agent import laws as laws_mod

    chunks = []
    for law in laws_mod.load_all():
        law_id = law.get("id", "")
        title = law.get("title", "")
        stage = law.get("stage", "")
        confidence = law.get("confidence", "")
        statement = (law.get("statement") or "").strip()
        mechanism = (law.get("mechanism") or "").strip()
        justification = (law.get("justification") or "").strip()
        falsification = (law.get("falsification") or "").strip()
        examples = law.get("examples") or []

        embed_text = f"Law {law_id} [{stage}/{confidence}]: {title}\n\nStatement: {statement}"
        if mechanism:
            embed_text += f"\n\nMechanism: {mechanism}"
        if justification:
            embed_text += f"\n\nJustification: {justification}"
        if examples:
            ex_lines = "; ".join(
                f"{ex.get('domain', '')}: {str(ex.get('description', ''))[:200]}"
                for ex in examples[:5]
            )
            embed_text += f"\n\nExamples: {ex_lines}"
        if falsification:
            embed_text += f"\n\nFalsification condition: {falsification}"

        path = laws_mod.path_for(law_id)
        chunks.append({
            "id": f"humboldt-law-{_slugify(law_id)}",
            "text": embed_text,
            "metadata": {
                "type": "law",
                "title": f"{law_id}: {title}",
                "law_id": law_id,
                "stage": stage,
                "confidence": confidence,
                "source_file": f"laws/{path.name}" if path else f"laws/{law_id}.yaml",
                "text": embed_text[:2000],
            },
        })
    return chunks


def _inbox_idea_chunks() -> list[dict]:
    """One chunk per discord-idea file — community research inputs with hypothesis tags."""
    inbox_dir = _ROOT / "inbox"
    chunks = []
    for path in sorted(inbox_dir.glob("discord-idea-*.md")):
        text = path.read_text().strip()
        if not text:
            continue
        title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        hyp_match = re.search(r"\*\*Hypothesis:\*\*\s*(.+)$", text, re.MULTILINE)
        author_match = re.search(r"\*\*Author:\*\*\s*(.+)$", text, re.MULTILINE)
        date_match = re.search(r"\*\*Date:\*\*\s*(.+)$", text, re.MULTILINE)

        title = title_match.group(1).strip() if title_match else path.stem
        hypothesis = hyp_match.group(1).strip() if hyp_match else ""
        author = author_match.group(1).strip() if author_match else ""
        date_str = date_match.group(1).strip() if date_match else ""

        # Strip the leading "Idea: " prefix from the title for cleaner embed text
        clean_title = re.sub(r"^Idea:\s*", "", title)
        embed_text = f"Community Research Idea — {clean_title}\n\n{text}"
        chunk_id = f"humboldt-inbox-idea-{_slugify(path.stem)}"

        chunks.append({
            "id": chunk_id,
            "text": embed_text,
            "metadata": {
                "type": "inbox_idea",
                "title": f"Idea: {clean_title[:80]}",
                "hypothesis": hypothesis,
                "author": author,
                "date": date_str,
                "source_file": f"inbox/{path.name}",
                "text": embed_text[:2000],
            },
        })
    return chunks


def _shallow_read_chunks() -> list[dict]:
    """Chunk shallow-read notes by ## section, same as deep-read notes."""
    shallow_dir = _ROOT / "bibliography" / "shallow-reads"
    if not shallow_dir.exists():
        return []
    chunks = []
    for path in sorted(shallow_dir.glob("*.md")):
        if path.name.startswith("_"):
            continue  # skip format templates
        text = path.read_text()
        title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        doc_title = title_match.group(1).strip() if title_match else path.stem

        for section_title, body in _chunk_markdown(text):
            embed_text = f"Shallow Read — {doc_title}: {section_title}\n\n{body}"
            chunk_id = f"humboldt-shallow-{_slugify(path.stem)}-{_slugify(section_title)}"
            chunks.append({
                "id": chunk_id,
                "text": embed_text,
                "metadata": {
                    "type": "shallow_read",
                    "title": f"Shallow Read: {doc_title} — {section_title}",
                    "doc_title": doc_title,
                    "section": section_title,
                    "source_file": f"bibliography/shallow-reads/{path.name}",
                    "text": embed_text[:2000],
                },
            })
    return chunks


def _embed_batch(texts: list[str]) -> list[list[float]]:
    vc = _voyage_client()
    result = vc.embed(texts, model=_VOYAGE_MODEL, input_type="document")
    return result.embeddings


def _content_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def _load_state() -> dict:
    if _STATE_PATH.exists():
        return json.loads(_STATE_PATH.read_text())
    return {}


def _save_state(state: dict) -> None:
    _STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    _STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True))


def ingest_all(verbose: bool = True, force: bool = False) -> dict:
    """Ingest all Humboldt documents into the humboldt Pinecone namespace.

    Incremental by default: only chunks whose content hash differs from
    data/ingest_state.json are (re-)embedded and upserted, and chunks whose
    id is no longer produced (source file renamed/deleted) are removed from
    the index. Pass force=True to re-embed and re-upsert every chunk
    regardless of whether it changed.
    """
    all_chunks = (
        _notebook_chunks()
        + _notes_chunks()
        + _shallow_read_chunks()
        + _law_chunks()
        + _inbox_idea_chunks()
    )

    if not all_chunks:
        if verbose:
            print("No documents found to ingest.")
        return {"upserted": 0, "deleted": 0}

    type_counts: dict[str, int] = {}
    for c in all_chunks:
        t = c["metadata"]["type"]
        type_counts[t] = type_counts.get(t, 0) + 1
    breakdown = ", ".join(f"{v} {k}" for k, v in type_counts.items())

    state = _load_state()
    current_ids = {c["id"] for c in all_chunks}
    to_upsert = [
        (c, h) for c in all_chunks
        if (h := _content_hash(c["text"])) and (force or state.get(c["id"]) != h)
    ]
    to_delete = [cid for cid in state if cid not in current_ids]

    if verbose:
        unchanged = len(all_chunks) - len(to_upsert)
        print(
            f"{len(all_chunks)} chunks total ({breakdown}) — "
            f"{len(to_upsert)} changed/new, {unchanged} unchanged, "
            f"{len(to_delete)} stale to delete"
        )

    if not to_upsert and not to_delete:
        if verbose:
            print("Nothing to do — namespace already up to date.")
        return {"upserted": 0, "deleted": 0}

    idx = _pinecone_index()
    total_upserted = 0

    for i in range(0, len(to_upsert), _BATCH_SIZE):
        batch = to_upsert[i : i + _BATCH_SIZE]
        texts = [c["text"] for c, _ in batch]
        embeddings = _embed_batch(texts)
        vectors = [
            {"id": c["id"], "values": emb, "metadata": c["metadata"]}
            for (c, _), emb in zip(batch, embeddings)
        ]
        idx.upsert(vectors=vectors, namespace=_NAMESPACE)
        total_upserted += len(vectors)
        if verbose:
            print(f"  {total_upserted}/{len(to_upsert)} upserted…")

    if to_delete:
        idx.delete(ids=to_delete, namespace=_NAMESPACE)
        if verbose:
            print(f"  {len(to_delete)} stale vectors deleted.")

    for c, h in to_upsert:
        state[c["id"]] = h
    for cid in to_delete:
        del state[cid]
    _save_state(state)

    if verbose:
        print(f"Done. {total_upserted} upserted, {len(to_delete)} deleted in '{_NAMESPACE}'.")

    try:
        from agent.pre_notebook import append as pn_append
        pn_append(
            process="ingest",
            summary=(
                f"Re-indexed humboldt namespace: {total_upserted} upserted, "
                f"{len(to_delete)} deleted ({breakdown})."
            ),
            detail=type_counts,
        )
    except Exception:
        pass

    return {"upserted": total_upserted, "deleted": len(to_delete)}
