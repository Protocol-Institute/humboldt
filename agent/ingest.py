"""Ingest Humboldt's own documents into the 'humboldt' Pinecone namespace.

Covers: notebook entries, deep-read notes, shallow reads, C/H/CL/F research
artifacts, DS arc files, and Discord inbox ideas. Each vector carries augmented
metadata so retrieved results are self-identifying in Claude prompts.

Run via: python3 -m agent.humboldt ingest
"""

import os
import re
from pathlib import Path

import yaml
import voyageai
from pinecone import Pinecone

_ROOT = Path(__file__).parent.parent
_NAMESPACE = "humboldt"
_VOYAGE_MODEL = "voyage-3"
_BATCH_SIZE = 96  # voyage-3 max batch


def _voyage_client() -> voyageai.Client:
    return voyageai.Client(api_key=os.environ["VOYAGE_API_KEY"])


def _pinecone_index():
    pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
    return pc.Index(host=os.environ["PINECONE_C3PO_HOST"])


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


def _curiosity_chunks() -> list[dict]:
    """Embed each C (Curiosity) YAML — exploration phase artifacts."""
    c_dir = _ROOT / "research" / "c"
    chunks = []
    for path in sorted(c_dir.glob("C-*.yaml")):
        try:
            item = yaml.safe_load(path.read_text())
        except Exception:
            continue
        item_id = item.get("id", path.stem)
        title = item.get("title", "")
        content = (item.get("content") or "").strip()
        source = item.get("source", "")
        connections = item.get("connections") or []

        embed_text = f"Curiosity {item_id}: {title}\n\n{content}"
        if connections:
            embed_text += "\n\nConnections: " + ", ".join(str(c) for c in connections)

        chunks.append({
            "id": f"humboldt-curiosity-{_slugify(item_id)}",
            "text": embed_text,
            "metadata": {
                "type": "curiosity",
                "title": f"{item_id}: {title}",
                "item_id": item_id,
                "source": source,
                "source_file": f"research/c/{path.name}",
                "text": embed_text[:2000],
            },
        })
    return chunks


def _cl_chunks() -> list[dict]:
    """Embed each CL (Candidate Law) YAML — valley phase artifacts."""
    cl_dir = _ROOT / "research" / "cl"
    chunks = []
    for path in sorted(cl_dir.glob("CL-*.yaml")):
        try:
            item = yaml.safe_load(path.read_text())
        except Exception:
            continue
        item_id = item.get("id", path.stem)
        name = item.get("name", "")
        statement = (item.get("statement") or "").strip()
        mechanism = (item.get("mechanism") or "").strip()
        domains = item.get("domains") or []

        embed_text = f"Candidate Law {item_id}: {name}\n\nStatement: {statement}"
        if mechanism:
            embed_text += f"\n\nMechanism: {mechanism}"
        if domains:
            embed_text += "\n\nDomains: " + "; ".join(str(d) for d in domains[:4])

        chunks.append({
            "id": f"humboldt-cl-{_slugify(item_id)}",
            "text": embed_text,
            "metadata": {
                "type": "candidate_law",
                "title": f"{item_id}: {name}",
                "item_id": item_id,
                "name": name,
                "source_file": f"research/cl/{path.name}",
                "text": embed_text[:2000],
            },
        })
    return chunks


def _h_chunks() -> list[dict]:
    """Embed each H (Hypothesis) YAML — sensemaking phase artifacts."""
    h_dir = _ROOT / "research" / "h"
    chunks = []
    for path in sorted(h_dir.glob("H-*.yaml")):
        try:
            item = yaml.safe_load(path.read_text())
        except Exception:
            continue
        item_id = item.get("id", path.stem)
        question = (item.get("question") or "").strip()
        cheap_trick = (item.get("cheap_trick") or "").strip()
        working_statement = (item.get("working_statement") or "").strip()

        embed_text = f"Hypothesis {item_id}: {question}"
        if cheap_trick:
            embed_text += f"\n\nCheap trick: {cheap_trick}"
        if working_statement:
            embed_text += f"\n\nWorking statement: {working_statement}"

        chunks.append({
            "id": f"humboldt-h-{_slugify(item_id)}",
            "text": embed_text,
            "metadata": {
                "type": "hypothesis",
                "title": f"{item_id}: {question[:80]}",
                "item_id": item_id,
                "source_file": f"research/h/{path.name}",
                "text": embed_text[:2000],
            },
        })
    return chunks


def _f_chunks() -> list[dict]:
    """Embed each F (Falsification Monitor) YAML — retrospective phase artifacts."""
    f_dir = _ROOT / "research" / "f"
    chunks = []
    for path in sorted(f_dir.glob("F-*.yaml")):
        try:
            item = yaml.safe_load(path.read_text())
        except Exception:
            continue
        item_id = item.get("id", path.stem)
        name = item.get("name", "")
        statement = (item.get("statement") or "").strip()
        falsification_conditions = (item.get("falsification_conditions") or "").strip()

        embed_text = f"Falsification Monitor {item_id}: {name}\n\nStatement: {statement}"
        if falsification_conditions:
            embed_text += f"\n\nFalsification conditions: {falsification_conditions}"

        chunks.append({
            "id": f"humboldt-f-{_slugify(item_id)}",
            "text": embed_text,
            "metadata": {
                "type": "falsification_monitor",
                "title": f"{item_id}: {name}",
                "item_id": item_id,
                "source_file": f"research/f/{path.name}",
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


def _ds_chunks() -> list[dict]:
    """Chunk each DS (Deep Story arc) markdown file by section."""
    ds_dir = _ROOT / "research" / "ds"
    chunks = []
    for path in sorted(ds_dir.glob("DS-*.md")):
        text = path.read_text()
        title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        doc_title = title_match.group(1).strip() if title_match else path.stem

        for section_title, body in _chunk_markdown(text):
            embed_text = f"Deep Story Arc — {doc_title}: {section_title}\n\n{body}"
            chunk_id = f"humboldt-ds-{_slugify(path.stem)}-{_slugify(section_title)}"
            chunks.append({
                "id": chunk_id,
                "text": embed_text,
                "metadata": {
                    "type": "deep_story",
                    "title": f"{path.stem} — {section_title}",
                    "doc_title": doc_title,
                    "section": section_title,
                    "source_file": f"research/ds/{path.name}",
                    "text": embed_text[:2000],
                },
            })
    return chunks


def _embed_batch(texts: list[str]) -> list[list[float]]:
    vc = _voyage_client()
    result = vc.embed(texts, model=_VOYAGE_MODEL, input_type="document")
    return result.embeddings


def ingest_all(verbose: bool = True) -> dict:
    """Ingest all Humboldt documents into the humboldt Pinecone namespace.

    Safe to re-run — upserts by deterministic IDs, so re-ingest updates
    existing vectors rather than creating duplicates.
    """
    all_chunks = (
        _notebook_chunks()
        + _notes_chunks()
        + _shallow_read_chunks()
        + _curiosity_chunks()
        + _h_chunks()
        + _cl_chunks()
        + _f_chunks()
        + _ds_chunks()
        + _inbox_idea_chunks()
    )

    if not all_chunks:
        if verbose:
            print("No documents found to ingest.")
        return {"upserted": 0}

    type_counts: dict[str, int] = {}
    for c in all_chunks:
        t = c["metadata"]["type"]
        type_counts[t] = type_counts.get(t, 0) + 1
    breakdown = ", ".join(f"{v} {k}" for k, v in type_counts.items())

    if verbose:
        print(f"Ingesting {len(all_chunks)} chunks ({breakdown}) → namespace '{_NAMESPACE}'")

    idx = _pinecone_index()
    total_upserted = 0

    for i in range(0, len(all_chunks), _BATCH_SIZE):
        batch = all_chunks[i : i + _BATCH_SIZE]
        texts = [c["text"] for c in batch]
        embeddings = _embed_batch(texts)
        vectors = [
            {"id": c["id"], "values": emb, "metadata": c["metadata"]}
            for c, emb in zip(batch, embeddings)
        ]
        idx.upsert(vectors=vectors, namespace=_NAMESPACE)
        total_upserted += len(vectors)
        if verbose:
            print(f"  {total_upserted}/{len(all_chunks)} upserted…")

    if verbose:
        print(f"Done. {total_upserted} vectors upserted to '{_NAMESPACE}'.")

    try:
        from agent.pre_notebook import append as pn_append
        pn_append(
            process="ingest",
            summary=f"Re-ingested humboldt namespace: {total_upserted} vectors ({breakdown}).",
            detail=type_counts,
        )
    except Exception:
        pass

    return {"upserted": total_upserted}
