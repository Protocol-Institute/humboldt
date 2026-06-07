"""
conversation_review.py — periodic reflective synthesis of Discord conversations.

Runs daily (or on schedule). Does two things:

1. NOTEBOOK SYNTHESIS — reads recent #new-nature messages and writes a reflective
   section to the current lab notebook: what ideas emerged, what challenged current
   thinking, what is worth remembering. Not a list — a researcher's synthesis.

2. REFERENCE PROMOTION — scans inbox/discord-link-*.md files written since the last
   review and adds unseen URLs to bibliography/references.yaml with status=unsorted.
   (Sorting happens separately via `humboldt references sort`.)

The synthesis uses Sonnet (needs judgment); promotion is mechanical (no model call).
"""

import logging
import os
import subprocess
from datetime import date, datetime, timezone
from pathlib import Path

import yaml
from anthropic import AsyncAnthropic

from . import costs

logger = logging.getLogger("humboldt.conversation_review")
_ROOT = Path(__file__).parent.parent
_INBOX_DIR = _ROOT / "inbox"
_MAIN_MODEL = "claude-sonnet-4-6"


def _load_slim_context() -> str:
    """Load condensed Humboldt context for the synthesis call."""
    identity_path = _ROOT / "IDENTITY.md"
    identity = identity_path.read_text() if identity_path.exists() else ""
    if len(identity) > 400:
        identity = identity[:400].rsplit("\n", 1)[0] + "\n…"

    laws_dir = _ROOT / "research" / "laws"
    law_lines = []
    for f in sorted(laws_dir.glob("*.yaml")):
        try:
            law = yaml.safe_load(f.read_text())
            law_lines.append(f"  {law.get('id')}: {law.get('name')}")
        except Exception:
            pass

    hyp_dir = _ROOT / "research" / "hypotheses"
    hyp_lines = []
    for f in sorted(hyp_dir.glob("*.yaml")):
        try:
            h = yaml.safe_load(f.read_text())
            if h.get("status") == "active":
                hyp_lines.append(f"  {h.get('id')}: {h.get('question', '')[:100]}")
        except Exception:
            pass

    return f"""{identity}

## Active hypotheses
{chr(10).join(hyp_lines) if hyp_lines else "  (none)"}

## Law inventory
{chr(10).join(law_lines) if law_lines else "  (none)"}"""


async def generate_notebook_synthesis(messages: list[dict], date_range: str) -> str | None:
    """
    Synthesize ideas from a batch of Discord messages into a notebook section.

    Returns the markdown text (starting after the ## header), or None if nothing
    worth capturing emerged.
    """
    if not messages:
        return None

    convo = "\n".join(f"{m['author']}: {m['content'][:300]}" for m in messages[-60:])
    context = _load_slim_context()

    costs.check_budget()
    async with AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"]) as client:
        resp = await client.messages.create(
            model=_MAIN_MODEL,
            max_tokens=400,
            system=context,
            messages=[{"role": "user", "content": (
                f"You are reviewing #new-nature conversations from {date_range}.\n\n"
                f"{convo}\n\n"
                f"Write a short reflective note (3–5 sentences) for your lab notebook "
                f"capturing what you took away from these exchanges. "
                f"Not a summary or list of what was said — a researcher's synthesis: "
                f"what ideas surprised you, what challenged your current thinking, "
                f"what examples appeared that you want to remember, what new questions opened. "
                f"If nothing of research value emerged, respond with exactly: NOTHING\n\n"
                f"First person, researcher voice. Do not repeat things already in your laws "
                f"or hypotheses — only genuinely new observations."
            )}],
        )
    costs.log_call(
        "conversation_review",
        _MAIN_MODEL,
        resp.usage.input_tokens,
        resp.usage.output_tokens,
    )
    text = resp.content[0].text.strip()
    if text.upper() == "NOTHING":
        return None
    return text


def _append_to_notebook(section_title: str, content: str) -> Path:
    """Append a section to today's notebook file (create if needed)."""
    today = date.today().isoformat()
    nb_path = _ROOT / "notebook" / f"{today}.md"

    section = f"\n\n---\n\n## {section_title}\n\n{content}\n"

    if nb_path.exists():
        nb_path.write_text(nb_path.read_text().rstrip() + section)
    else:
        nb_path.write_text(
            f"# Lab Notebook — {today}\n\n"
            f"*Daemon-generated entries.*\n"
            + section
        )
    return nb_path


def _promote_inbox_links(since_date: str | None) -> int:
    """Promote unprocessed inbox link files to bibliography/references.yaml."""
    from agent.references import promote_inbox_links
    added = promote_inbox_links(since_date=since_date, verbose=False)
    return added


def _commit_review_output(nb_path: Path, refs_changed: bool) -> None:
    """Commit notebook and/or references changes after review."""
    files_to_add = []
    if nb_path.exists():
        files_to_add.append(str(nb_path))
    refs_path = _ROOT / "bibliography" / "references.yaml"
    if refs_changed and refs_path.exists():
        files_to_add.append(str(refs_path))

    if not files_to_add:
        return

    try:
        subprocess.run(
            ["git", "add"] + files_to_add,
            cwd=_ROOT, check=True, capture_output=True,
        )
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=_ROOT, capture_output=True,
        )
        if result.returncode == 0:
            return  # nothing staged
        subprocess.run(
            ["git", "commit", "-m",
             f"Conversation review {date.today().isoformat()}: "
             f"notebook synthesis + reference promotion\n\n"
             f"Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"],
            cwd=_ROOT, check=True, capture_output=True,
        )
        subprocess.run(
            ["git", "push", "origin", "main"],
            cwd=_ROOT, check=True, capture_output=True,
        )
        logger.info("Conversation review committed and pushed")
    except subprocess.CalledProcessError as e:
        logger.warning(f"Review commit failed: {e.stderr.decode()}")


async def run_review(
    messages: list[dict],
    last_review_date: str | None,
) -> dict:
    """
    Run a full conversation review pass.

    Parameters
    ----------
    messages:
        Recent Discord messages, chronological order.
    last_review_date:
        YYYY-MM-DD of last review (used to scope inbox scan). None = scan all.

    Returns
    -------
    dict with keys: notebook_written (bool), references_added (int)
    """
    today = date.today().isoformat()
    date_range = f"{last_review_date} – {today}" if last_review_date else f"through {today}"

    # 1. Synthesize ideas for notebook
    notebook_written = False
    if messages:
        synthesis = await generate_notebook_synthesis(messages, date_range)
        if synthesis:
            nb_path = _append_to_notebook(
                f"Ideas from Discord — {date_range}",
                synthesis,
            )
            logger.info(f"Conversation review: notebook section written ({nb_path.name})")
            notebook_written = True
        else:
            logger.info("Conversation review: no notebook synthesis (nothing new)")
            nb_path = _ROOT / "notebook" / f"{today}.md"
    else:
        logger.info("Conversation review: no messages to synthesize")
        nb_path = _ROOT / "notebook" / f"{today}.md"

    # 2. Promote inbox links to reference list
    refs_added = _promote_inbox_links(since_date=last_review_date)
    if refs_added:
        logger.info(f"Conversation review: {refs_added} reference(s) promoted from inbox")

    # 3. Commit if anything changed
    if notebook_written or refs_added:
        _commit_review_output(nb_path, refs_added > 0)

    # 4. Append to pre-notebook log
    try:
        from agent.pre_notebook import append as pn_append
        parts = []
        if notebook_written:
            parts.append(f"notebook section written to {nb_path.name}")
        if refs_added:
            parts.append(f"{refs_added} reference(s) promoted to bibliography/references.yaml")
        if not parts:
            parts.append("nothing new to synthesize")
        pn_append(
            process="daemon_conversation_review",
            summary=f"Daily conversation review: {'; '.join(parts)}.",
            detail={"notebook_written": notebook_written, "references_added": refs_added,
                    "last_review_date": last_review_date},
        )
    except Exception:
        pass

    return {"notebook_written": notebook_written, "references_added": refs_added}
