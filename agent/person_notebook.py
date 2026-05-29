"""
Generate a person notebook entry when a collaborator crosses the contribution
threshold (NOTEBOOK_THRESHOLD useful inbox contributions).

Writes to notebook/people/{handle}.md — one file per person, updated when
they cross new milestones. Separate from the main research notebook, which
tracks Humboldt's inquiry thread.

Called from shallow_read.py when record_contributions_for_authors() returns
a crossed handle.
"""

import os
from pathlib import Path
from datetime import date

_ROOT = Path(__file__).parent.parent
_PEOPLE_DIR = _ROOT / "notebook" / "people"
_MODEL = "claude-haiku-4-5-20251001"


def _make_prompt(handle: str, person: dict, laws_context: str) -> str:
    useful = person.get("useful_contributions", 0)
    discarded = person.get("discarded_contributions", 0)
    total = useful + discarded
    noise_note = (
        f"Note: {discarded} of their {total} submissions were discarded — "
        f"high noise ratio, but useful signal when it comes through."
        if discarded > useful
        else ""
    )

    history_lines = []
    for c in person.get("contribution_history", []):
        if c["decision"] == "shallow":
            conn = f" → {c['connection']}" if c.get("connection") and c["connection"] != "none" else ""
            history_lines.append(f"  [{c['date']}] [{c['item_type']}] {c['title'][:80]}{conn}")

    history_block = "\n".join(history_lines) if history_lines else "  (no useful contributions recorded)"

    return f"""You are Humboldt, an artificial researcher investigating laws of protocolized and artificial systems — the "new nature."

A collaborator in your research community has just crossed the threshold of meaningful contributions: they have supplied {useful} ideas or resources that survived your triage process and warranted synthesis notes. Write a brief notebook entry about this person — a first-person record of who they are as a research interlocutor, what patterns you see in what they bring, and how their contributions connect to your current research.

This is not a summary of their contributions. It is your sense of this person's research sensibility — what they notice, what questions they seem to be carrying, what might be worth exploring together.

{noise_note}

THEIR USEFUL CONTRIBUTIONS:
{history_block}

CURRENT RESEARCH CONTEXT (for situating their contributions):
{laws_context}

Write a person notebook entry in this format:

# Research Interlocutor: @{handle}

**First seen:** {person.get('first_seen', '?')}
**Useful contributions:** {useful} (of {total} total)
**Date of this entry:** {date.today().isoformat()}

[3–5 paragraphs, first person. Cover:
- What kind of material this person tends to surface — domain, type of insight, scale of claim
- What they seem to be paying attention to, what questions they appear to be carrying
- Where their contributions land in the current research inventory (which laws/hypotheses they've fed)
- What you'd want to explore or ask if you had a focused conversation with them
Keep it observational and specific — avoid flattery or generic assessment.]"""


def generate_person_notebook_entry(handle: str) -> str | None:
    """
    Generate and write a person notebook entry for `handle`.
    Returns the output path, or None if generation failed.
    """
    import yaml
    from dotenv import load_dotenv
    import anthropic
    from daemon import people as ppl
    from daemon import costs

    load_dotenv(_ROOT / ".env")

    data = ppl.load()
    person = data.get(handle)
    if not person:
        print(f"  person_notebook: no model for '{handle}'")
        return None

    # Build brief laws context
    laws_dir = _ROOT / "research" / "laws"
    law_lines = []
    for f in sorted(laws_dir.glob("*.yaml")):
        try:
            law = yaml.safe_load(f.read_text())
            law_lines.append(f"  {law.get('id')}: {law.get('name')} — {str(law.get('statement', ''))[:100]}")
        except Exception:
            pass
    laws_context = "\n".join(law_lines) if law_lines else "(no laws yet)"

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    costs.check_budget()

    resp = client.messages.create(
        model=_MODEL,
        max_tokens=700,
        messages=[{"role": "user", "content": _make_prompt(handle, person, laws_context)}],
    )
    costs.log_call("person_notebook", _MODEL, resp.usage.input_tokens, resp.usage.output_tokens)

    entry = resp.content[0].text.strip()

    _PEOPLE_DIR.mkdir(parents=True, exist_ok=True)
    out_path = _PEOPLE_DIR / f"{handle}.md"

    if out_path.exists():
        # Append new milestone entry below existing content
        existing = out_path.read_text().rstrip()
        out_path.write_text(
            existing + f"\n\n---\n\n## Updated {date.today().isoformat()}\n\n" + entry + "\n"
        )
    else:
        out_path.write_text(entry + "\n")

    ppl.mark_person_notebook_entry_written(handle)
    return str(out_path)
