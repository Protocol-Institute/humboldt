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
from agent import read_cache as _cache
from agent import read_egress as _egress


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

# top_k for the Discord reply path (the highest-frequency retrieval in the
# system). Egress is `namespaces x top_k x queries` and every match carries up
# to 2000 chars of chunk text, so over-fetching here is what spends the monthly
# cap. `presence.generate_mention_response` formats at most 4 own + 4 PI chunks,
# so 5 namespaces x 3 = 15 candidates already leaves ~2x headroom for the merge
# and dedup; the old top_k of 5 returned 25 and discarded 17 of them.
REPLY_TOP_K = 3

# Same reasoning for the assessment sweep: `assess` formats chunks[:10], and ran
# 2 queries x 6 namespaces x 8 = 96 matches to fill them.
ASSESS_TOP_K = 4

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


def _ns_query(idx_fn, query, vector_fn, ns, top_k, filter, op) -> list[dict]:
    """One namespace query, through the full read path: cache → network →
    egress accounting → cache.

    Kept at namespace granularity so callers with different namespace *sets*
    still share cached answers for the namespaces they have in common.
    """
    hit = _cache.get(query, ns, top_k, filter)
    if hit is not None:
        _egress.record(ns, len(hit), _egress.measure(hit), op=op, cached=True)
        return hit

    kwargs = dict(vector=vector_fn(), top_k=top_k, include_metadata=True)
    if ns != _HUMBOLDT_NS:
        kwargs["namespace"] = ns  # humboldt index uses the default namespace
    if filter:
        kwargs["filter"] = filter

    resp = _query(idx_fn(), kwargs)
    results = [{
        "score": m.score,
        "namespace": ns,
        "id": m.id,
        "metadata": m.metadata or {},
    } for m in resp.matches]

    _egress.record(ns, len(results), _egress.measure(resp.matches), op=op)
    _cache.put(query, ns, top_k, results, filter)
    return results


def query_pinecone(
    query: str,
    namespaces: list[str] = NS_FORMAL,
    top_k: int = 12,
    filter: Optional[dict] = None,
    op: str = "query",
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

    # Embedded lazily and once: a query answered entirely from the read cache
    # should not spend a Voyage call either.
    _vector: list[float] | None = None

    def vector_fn() -> list[float]:
        nonlocal _vector
        if _vector is None:
            _vector = embed(query)
        return _vector

    # Indexes are built lazily for the same reason — an all-cache-hit call
    # should touch no client at all.
    _clients: dict = {}

    def c3po_fn():
        return _clients.setdefault("c3po", _c3po_index())

    def humboldt_fn():
        return _clients.setdefault("humboldt", _humboldt_index())

    all_results = []
    for ns in namespaces:
        idx_fn = humboldt_fn if ns == _HUMBOLDT_NS else c3po_fn
        all_results.extend(_ns_query(idx_fn, query, vector_fn, ns, top_k, filter, op))

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
    op: str = "retrieve",
) -> list[dict]:
    """
    Unified retrieval interface.

    mode: "direct" (Pinecone) or "worker" (c3po API)
    """
    if mode == "worker":
        return query_c3po_worker(query, top_k=top_k)
    return query_pinecone(query, namespaces=namespaces, top_k=top_k, op=op)


def multi_retrieve(
    queries: list[str],
    namespaces: list[str] = NS_FORMAL,
    top_k_each: int = 8,
    op: str = "multi",
) -> list[dict]:
    """Run multiple queries and merge results, deduplicating by id.

    ``op`` labels the calling path in the egress ledger — egress scales as
    queries x namespaces x top_k_each, so per-path attribution is what makes a
    runaway consumer findable before it exhausts the monthly cap.
    """
    seen = {}
    for q in queries:
        for r in query_pinecone(q, namespaces=namespaces, top_k=top_k_each, op=op):
            rid = r["id"]
            if rid not in seen or r["score"] > seen[rid]["score"]:
                seen[rid] = r
    return sorted(seen.values(), key=lambda x: x["score"], reverse=True)
