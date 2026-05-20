"""Research prompt templates and SOUL.md loader."""

import os
from pathlib import Path

_SOUL_PATH = Path(__file__).parent.parent / "SOUL.md"

def load_soul() -> str:
    return _SOUL_PATH.read_text()


HYPOTHESIS_SYSTEM = """\
{soul}

---

You are operating in HYPOTHESIS mode.

Given a topic or domain, your task is to propose candidate laws of protocolized systems
that could plausibly emerge from that area. Each candidate should:
- Be stated precisely enough to be falsifiable
- Name the type (conservation, hardness, lifecycle, failure, scaling, evolution, interaction, equilibrium)
- Name at least one domain where the pattern might appear
- Distinguish itself from already-known named laws (Gall, Goodhart, Conway, Metcalfe, etc.)

Output a numbered list. Be generative but disciplined — propose real candidates,
not empty generalizations.
"""

EVIDENCE_ANALYSIS_SYSTEM = """\
{soul}

---

You are operating in EVIDENCE mode.

You will receive retrieved corpus excerpts and a candidate law statement.
Your task is to:
1. Identify which excerpts provide direct evidence FOR the law
2. Identify which excerpts provide evidence AGAINST or set limits on the law
3. Note any excerpts that describe a mechanism that could explain WHY the law holds
4. Identify gaps: what evidence would strengthen or weaken the case that is missing from these excerpts?

Be specific — quote the relevant passages and explain why they bear on the law.
Rate overall corpus coverage: strong / moderate / thin / absent.
"""

INVESTIGATION_SYSTEM = """\
{soul}

---

You are operating in INVESTIGATION mode.

Given a research topic and corpus excerpts, your task is to:
1. Extract the most relevant evidence and examples
2. Identify 2–4 candidate laws that the evidence supports
3. For each candidate, draft a precise statement with falsification conditions
4. Note cross-domain connections — does this pattern appear in multiple independent domains?
5. Identify what the corpus does NOT cover that would be needed to confirm or refute each candidate

Output structured YAML-ready summaries for each candidate law. Use the schema from SOUL.md.
"""

LAW_FORMULATION_SYSTEM = """\
{soul}

---

You are operating in FORMULATION mode.

You will receive a draft law candidate with evidence. Your task is to:
1. Sharpen the statement — make it precise and falsifiable
2. Identify the mechanism — WHY does this law hold?
3. Assign a confidence level: speculative / candidate / established / contested
4. Identify the closest related laws in the Protocol Institute's intellectual tradition
5. Draft the complete YAML record

Output valid YAML only — no surrounding text.
"""

THEORIZE_SYSTEM = """\
{soul}

---

You are operating in THEORIZE mode.

You will receive the current law inventory. Your task is to:
1. Identify clusters of laws that appear to be special cases of a more general principle
2. Propose a unifying statement for each cluster
3. Identify the strongest candidate for a first unified theory of protocol behavior
4. Flag laws that sit in tension with each other — apparent contradictions that need resolution
5. Propose 2–3 investigation directions that would most advance the unified theory

Output a structured analysis followed by draft theory sketches.
"""


def hypothesis_prompt(soul: str, topic: str) -> tuple[str, str]:
    system = HYPOTHESIS_SYSTEM.format(soul=soul)
    user = f"Research topic: {topic}\n\nPropose candidate laws."
    return system, user


def investigation_prompt(soul: str, topic: str, chunks: list[dict]) -> tuple[str, str]:
    system = INVESTIGATION_SYSTEM.format(soul=soul)
    context = _format_chunks(chunks)
    user = f"Research topic: {topic}\n\n--- CORPUS EXCERPTS ---\n\n{context}"
    return system, user


def evidence_prompt(soul: str, law_statement: str, chunks: list[dict]) -> tuple[str, str]:
    system = EVIDENCE_ANALYSIS_SYSTEM.format(soul=soul)
    context = _format_chunks(chunks)
    user = (
        f"Candidate law:\n{law_statement}\n\n"
        f"--- CORPUS EXCERPTS ---\n\n{context}"
    )
    return system, user


def theorize_prompt(soul: str, inventory: str) -> tuple[str, str]:
    system = THEORIZE_SYSTEM.format(soul=soul)
    user = f"Current law inventory:\n\n{inventory}"
    return system, user


def _format_chunks(chunks: list[dict]) -> str:
    parts = []
    for i, c in enumerate(chunks, 1):
        meta = c.get("metadata", {})
        source = meta.get("title") or meta.get("source") or "unknown"
        authors = meta.get("authors") or meta.get("author") or ""
        if isinstance(authors, list):
            authors = ", ".join(authors)
        header = f"[{i}] {source}"
        if authors:
            header += f" — {authors}"
        ns = c.get("namespace", "")
        if ns:
            header += f" ({ns})"
        text = meta.get("text") or c.get("text") or ""
        parts.append(f"{header}\n{text[:800]}")
    return "\n\n---\n\n".join(parts)
