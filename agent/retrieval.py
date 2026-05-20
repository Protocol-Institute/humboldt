"""Corpus retrieval via Pinecone (direct) or c3po Worker API."""

import os
import json
import urllib.request
import urllib.parse
from typing import Optional

import voyageai
from pinecone import Pinecone


# Namespace groups for different retrieval tasks
NS_FORMAL = ["pdfs", "bibliography"]
NS_BROAD   = ["pdfs", "substack", "videos", "bibliography", "discord_links", "sig"]
NS_COMMUNITY = ["discord", "discord_links", "sig"]
NS_ALL = ["pdfs", "substack", "videos", "bibliography", "discord", "discord_links", "sig"]


def _voyage_client() -> voyageai.Client:
    return voyageai.Client(api_key=os.environ["VOYAGE_API_KEY"])


def _pinecone_index():
    pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
    return pc.Index(host=os.environ["PINECONE_C3PO_HOST"])


def embed(text: str) -> list[float]:
    vc = _voyage_client()
    result = vc.embed([text], model="voyage-3", input_type="query")
    return result.embeddings[0]


def query_pinecone(
    query: str,
    namespaces: list[str] = NS_FORMAL,
    top_k: int = 12,
    filter: Optional[dict] = None,
) -> list[dict]:
    """Query the c3po Pinecone index and return merged, ranked chunks."""
    vector = embed(query)
    idx = _pinecone_index()

    all_results = []
    for ns in namespaces:
        kwargs = dict(vector=vector, top_k=top_k, include_metadata=True, namespace=ns)
        if filter:
            kwargs["filter"] = filter
        resp = idx.query(**kwargs)
        for match in resp.matches:
            all_results.append({
                "score": match.score,
                "namespace": ns,
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
