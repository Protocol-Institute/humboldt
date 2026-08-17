"""Corpus retrieval via Pinecone (direct) or c3po Worker API.

Two indexes:
  c3po index   (PINECONE_C3PO_HOST)      — PI corpus namespaces: pdfs, substack, videos, etc.
  humboldt index (PINECONE_HUMBOLDT_HOST) — Humboldt's own research artifacts (default namespace)
"""

import os
import json
import urllib.request
import urllib.parse
from typing import Optional

import voyageai
from pinecone import Pinecone

from agent.read_budget import RetrievalUnavailable  # re-exported for callers
from agent import read_budget as _budget


# Namespace groups for different retrieval tasks
NS_FORMAL = ["pdfs", "bibliography"]
NS_BROAD   = ["pdfs", "substack", "videos", "bibliography", "discord_links", "sig"]
NS_COMMUNITY = ["discord", "discord_links", "sig"]
NS_ALL = ["pdfs", "substack", "videos", "bibliography", "discord", "discord_links", "sig"]
NS_HUMBOLDT = ["humboldt"]
# PI corpus + Humboldt's own notebook/notes/laws — use for Discord responses.
# Trimmed from NS_BROAD (drops bibliography, discord_links) 2026-08-17: these two
# rarely surface in live reply context and this set is queried against c3po's
# shared Pinecone index on every composed reply, unlike the CLI-only NS_BROAD/
# NS_ALL research commands where the extra breadth is worth the cost.
NS_BROAD_PLUS = ["pdfs", "substack", "videos", "sig", "humboldt"]

_HUMBOLDT_NS = "humboldt"  # sentinel — routes to the dedicated humboldt index


def _voyage_client() -> voyageai.Client:
    return voyageai.Client(api_key=os.environ["VOYAGE_API_KEY"])


def _c3po_index():
    pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
    return pc.Index(host=os.environ["PINECONE_C3PO_HOST"])


def _humboldt_index():
    pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
    return pc.Index(host=os.environ["PINECONE_HUMBOLDT_HOST"])


# Keep old name as alias so daemon/synthesizer callsites don't break
def _pinecone_index():
    return _c3po_index()


def embed(text: str) -> list[float]:
    vc = _voyage_client()
    result = vc.embed([text], model="voyage-3", input_type="query")
    return result.embeddings[0]


def _query(idx, kwargs):
    """Run one Pinecone query, converting a monthly-quota 429 into a tripped
    breaker + RetrievalUnavailable. Other errors propagate untouched — a
    transient fault should not take the corpus offline for the rest of the month.
    """
    try:
        return idx.query(**kwargs)
    except Exception as e:  # noqa: BLE001
        if _budget.is_quota_error(e):
            until = _budget.trip(e)
            raise RetrievalUnavailable(_budget.reason(), until) from e
        raise


def query_pinecone(
    query: str,
    namespaces: list[str] = NS_FORMAL,
    top_k: int = 12,
    filter: Optional[dict] = None,
) -> list[dict]:
    """Query Pinecone indexes and return merged, ranked chunks.

    Corpus namespaces (pdfs, substack, etc.) are queried on the c3po index.
    The 'humboldt' sentinel routes to the dedicated humboldt index.

    Raises RetrievalUnavailable when corpus reads are offline — never returns an
    empty list for that case. An empty list means "the corpus has nothing on
    this"; conflating the two is what hid the 2026-08 egress outage for weeks.
    """
    # Gate before any network call: if the breaker is already tripped there is
    # no point spending a Voyage embedding on a query we cannot run.
    if _budget.is_paused():
        raise RetrievalUnavailable(_budget.reason(), _budget.paused_until())

    vector = embed(query)

    corpus_ns = [ns for ns in namespaces if ns != _HUMBOLDT_NS]
    include_humboldt = _HUMBOLDT_NS in namespaces

    all_results = []

    if corpus_ns:
        idx = _c3po_index()
        for ns in corpus_ns:
            kwargs = dict(vector=vector, top_k=top_k, include_metadata=True, namespace=ns)
            if filter:
                kwargs["filter"] = filter
            resp = _query(idx, kwargs)
            for match in resp.matches:
                all_results.append({
                    "score": match.score,
                    "namespace": ns,
                    "id": match.id,
                    "metadata": match.metadata or {},
                })

    if include_humboldt:
        hidx = _humboldt_index()
        kwargs = dict(vector=vector, top_k=top_k, include_metadata=True)
        if filter:
            kwargs["filter"] = filter
        resp = _query(hidx, kwargs)
        for match in resp.matches:
            all_results.append({
                "score": match.score,
                "namespace": _HUMBOLDT_NS,
                "id": match.id,
                "metadata": match.metadata or {},
            })

    # Sort by score descending; deduplicate by id (keep highest score)
    seen = {}
    for r in sorted(all_results, key=lambda x: x["score"], reverse=True):
        if r["id"] not in seen:
            seen[r["id"]] = r
    return list(seen.values())


def query_c3po_worker(query: str, top_k: int = 10) -> list[dict]:
    """Query c3po worker /search endpoint. Requires C3PO_WORKER_URL env var."""
    base_url = os.environ.get("C3PO_WORKER_URL", "").rstrip("/")
    if not base_url:
        raise EnvironmentError("C3PO_WORKER_URL not set")

    mcp_key = os.environ.get("C3PO_MCP_KEY", "")
    params = urllib.parse.urlencode({"q": query, "k": top_k})
    url = f"{base_url}/search?{params}"

    req = urllib.request.Request(url)
    if mcp_key:
        req.add_header("Authorization", f"Bearer {mcp_key}")

    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())

    # Normalize to same shape as query_pinecone output
    results = []
    for item in data.get("results", []):
        results.append({
            "score": item.get("score", 0.0),
            "namespace": item.get("namespace", ""),
            "id": item.get("id", ""),
            "metadata": item.get("metadata", {}),
        })
    return results


def retrieve(
    query: str,
    mode: str = "direct",
    namespaces: list[str] = NS_FORMAL,
    top_k: int = 12,
) -> list[dict]:
    """
    Unified retrieval interface.

    mode: "direct" (Pinecone) or "worker" (c3po API)
    """
    if mode == "worker":
        return query_c3po_worker(query, top_k=top_k)
    return query_pinecone(query, namespaces=namespaces, top_k=top_k)


def multi_retrieve(
    queries: list[str],
    namespaces: list[str] = NS_FORMAL,
    top_k_each: int = 8,
) -> list[dict]:
    """Run multiple queries and merge results, deduplicating by id."""
    seen = {}
    for q in queries:
        for r in query_pinecone(q, namespaces=namespaces, top_k=top_k_each):
            rid = r["id"]
            if rid not in seen or r["score"] > seen[rid]["score"]:
                seen[rid] = r
    return sorted(seen.values(), key=lambda x: x["score"], reverse=True)
