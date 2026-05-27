"""Research context assembly and prompt templates."""

import datetime
from pathlib import Path

_ROOT = Path(__file__).parent.parent
_IDENTITY_PATH = _ROOT / "IDENTITY.md"
_LINEAGE_PATH = _ROOT / "LINEAGE.md"
_MEMORY_PATH = _ROOT / "MEMORY.md"
_METHOD_PATH = _ROOT / "METHOD.md"
_POLICY_PATH = _ROOT / "BOOTSTRAP.md"
_SOUL_PATH = _ROOT / "SOUL.md"          # archived; kept for reference
_METHODS_DIR = _ROOT / "methods"
_RESEARCH_DIR = _ROOT / "research"
_NOTEBOOK_DIR = _ROOT / "notebook"
_LIBRARY_DIR = _ROOT / "bibliography" / "deep-reads"
_NOTES_DIR = _ROOT / "bibliography" / "notes"
_INBOX_DIR = _ROOT / "inbox"


def _methods_index() -> str:
    """One-line summary of each available technique."""
    lines = []
    for f in sorted(_METHODS_DIR.glob("M-*.md")):
        text = f.read_text()
        # Extract Purpose line
        purpose = ""
        for line in text.splitlines():
            if line.startswith("**Purpose:**"):
                purpose = line.replace("**Purpose:**", "").strip()
                break
        name = f.stem  # e.g. M-001-random-links
        lines.append(f"  {name}: {purpose}")
    return "\n".join(lines) if lines else "  (no methods defined)"


def _research_state() -> str:
    """Current inventory summary loaded from research/ files."""
    import yaml

    laws_dir = _RESEARCH_DIR / "laws"
    hyp_dir = _RESEARCH_DIR / "hypotheses"

    # Laws by confidence
    conf_counts: dict[str, int] = {}
    for f in sorted(laws_dir.glob("*.yaml")):
        try:
            law = yaml.safe_load(f.read_text())
            c = law.get("confidence", "speculative")
            conf_counts[c] = conf_counts.get(c, 0) + 1
        except Exception:
            pass
    total = sum(conf_counts.values())
    conf_str = ", ".join(f"{v} {k}" for k, v in conf_counts.items()) if conf_counts else "none"
    laws_line = f"Laws: {total} ({conf_str})"

    # Active hypotheses
    active = []
    for f in sorted(hyp_dir.glob("*.yaml")):
        try:
            h = yaml.safe_load(f.read_text())
            if h.get("status") == "active":
                active.append(f"{h.get('id', f.stem)} — {h.get('name', '')}")
        except Exception:
            pass
    hyp_line = "Active hypotheses: " + ("; ".join(active) if active else "none")

    # Library
    pdfs = sorted(_LIBRARY_DIR.glob("*.pdf"))
    lib_parts = []
    for p in pdfs:
        has_notes = (_NOTES_DIR / f"{p.stem}.md").exists()
        lib_parts.append(p.stem + (" [notes]" if has_notes else " [unread]"))
    lib_line = "Library: " + (", ".join(lib_parts) if lib_parts else "empty")

    return "\n".join([laws_line, hyp_line, lib_line])


def _inbox_scan() -> str:
    """List unprocessed inbox items with their content (short files) or names (large)."""
    items = [f for f in sorted(_INBOX_DIR.iterdir())
             if f.is_file() and f.name != "README.md" and f.parent.name != "processed"]
    if not items:
        return "(inbox empty)"
    parts = []
    for f in items:
        if f.suffix in (".md", ".txt") and f.stat().st_size < 4000:
            parts.append(f"[{f.name}]\n{f.read_text().strip()}")
        else:
            parts.append(f"[{f.name}] ({f.suffix} file, {f.stat().st_size // 1024}KB — read directly if relevant)")
    return "\n\n".join(parts)


def _recent_notebook() -> str:
    """Return the most recent notebook entry, truncated."""
    entries = sorted(_NOTEBOOK_DIR.glob("????-??-??.md"), reverse=True)
    if not entries:
        return "(no notebook entries yet)"
    text = entries[0].read_text()
    # Return up to ~600 chars — enough to establish the live thread
    if len(text) > 600:
        text = text[:600].rsplit("\n", 1)[0] + "\n…(truncated)"
    return f"[{entries[0].stem}]\n{text}"


def assemble_context() -> str:
    """
    Assemble the full research context from modular documents.
    This replaces the old monolithic SOUL.md load.
    """
    identity = _IDENTITY_PATH.read_text() if _IDENTITY_PATH.exists() else ""
    lineage = _LINEAGE_PATH.read_text() if _LINEAGE_PATH.exists() else ""
    memory = _MEMORY_PATH.read_text() if _MEMORY_PATH.exists() else ""
    method = _METHOD_PATH.read_text() if _METHOD_PATH.exists() else ""
    policy = _POLICY_PATH.read_text() if _POLICY_PATH.exists() else ""

    return f"""{identity}

---

{lineage}

---

{memory}

---

{method}

---

{policy}

---

## Current Research State

{_research_state()}

## Inbox

{_inbox_scan()}

## Methods Available

{_methods_index()}

## Recent Notebook

{_recent_notebook()}
"""


def load_soul() -> str:
    """Backward-compatible wrapper — returns assembled context."""
    return assemble_context()


def list_library() -> list[Path]:
    """Return PDF paths available in the deep-read library."""
    return sorted(_LIBRARY_DIR.glob("*.pdf"))


def notes_path(doc_stem: str) -> Path:
    return _NOTES_DIR / f"{doc_stem}.md"


DEEP_READ_SYSTEM = """\
{soul}

---

You are operating in DEEP READ mode.

You are reading extracted text from an actual document in Humboldt's library. The text
below was read directly from the source PDF. Do NOT draw on prior knowledge of this work —
reason only from the text provided. If the text is incomplete (partial page range), say so
explicitly and mark open sections as awaiting further reading.

## Primary task: understand this work on its own terms

Before connecting the text to your own research, inhabit it. What is the author's central
problem — not yours, theirs? What animates the work? What is the load-bearing example or
analogy the argument depends on? Where does the author's own framework show strain?

Law extraction is one possible output of a deep read, not the objective. Some texts
yield candidate laws; many yield something more valuable: new vocabulary, an analytical
habit, a way of framing a problem, a tradition to be in. Do not hunt for laws. Let the
text show you what it has.

## Output structure

Produce the following sections. Sections 5–7 may be brief or empty for a given text —
that is not a failure.

1. **Gestalt** — One paragraph: what is this work, really? The author's animating question,
   their method, their central conviction. Not a summary — an understanding of the whole.
   Write this as if explaining to someone why this text matters on its own terms.

2. **Argument and structure** — The shape of the argument: core claims, how they build,
   key examples and what load they carry, acknowledged limits and counterexamples.
   Note where the author is most confident and where they are most speculative.

3. **Conceptual vocabulary** — Terms the author uses in specialized or non-standard ways
   that you are now carrying. Define them in the author's sense, then note any tension
   with your own existing vocabulary.

4. **Analytical moves** — Named, transferable procedures this author performs that could
   be applied elsewhere. Not conclusions — operations. (e.g. "Simon's near-decomposability
   test: ask whether a system can be partitioned into subsystems whose internal interactions
   are stronger than cross-subsystem interactions.")

5. **What it says about the nature of things** — Lessons that generalize beyond the
   specific domain: about how laws work and fail, how complex systems behave, how knowledge
   accumulates, how design operates, how order emerges. These are the author's implicit
   general commitments, often more interesting than their explicit claims.

6. **What it says about becoming a better researcher** — Lessons about research practice,
   epistemic habits, attention allocation, and intellectual craft. How does this author
   approach the work of research itself? What does the text reveal about: choosing what to
   work on; managing confidence vs. uncertainty; sustaining inquiry over time; recognizing
   when to push vs. when to reorient; what distinguishes mature researchers from immature
   ones? Note any practices or dispositions the author exemplifies or explicitly recommends.
   May be thin for technical texts, but is often the most valuable section for works on
   science, method, or design. Connect explicitly to M-016 dimensions where relevant.

7. **Where it touches my research** — (May be thin.) Specific connections to active
   hypotheses, existing laws, or open questions. Note the connection precisely; do not
   force it.

8. **Candidate laws** — (Optional; may be empty.) Only if the text explicitly or strongly
   implies a falsifiable regularity worth formalizing. State what the text actually says
   [text, p.N], then the candidate formulation, then what would falsify it. Do not generate
   candidates to fill this section.

9. **What surprised me / what doesn't fit** — The most generative moments: where the
   author's own framework strains, where an example does more work than acknowledged,
   where two claims are in tension, where the argument is weakest. These are often where
   the most interesting research questions live.

10. **What it opens** — Live questions now running; related texts worth reading; traditions
    worth exploring. Be specific — name texts, name authors, name the question.

## Provenance markers

Mark every claim:
- [text, p.N] — directly in the source
- [inference] — your synthesis from what the text says
- [external] — knowledge outside this document (use sparingly; flag it explicitly)

Write in Humboldt's analytical voice: first-person investigator, committed but precise,
genuinely curious about what the text is doing.
"""

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


def deep_read_prompt(soul: str, doc_title: str, page_range: str, text: str) -> tuple[str, str]:
    system = DEEP_READ_SYSTEM.format(soul=soul)
    user = (
        f"Document: {doc_title}\n"
        f"Pages read: {page_range}\n\n"
        f"--- EXTRACTED TEXT ---\n\n{text}"
    )
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
