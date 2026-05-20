"""
Humboldt — Protocol Institute research agent.

Usage:
    python3 -m agent.humboldt investigate "<topic>"
    python3 -m agent.humboldt hypothesize "<topic>"
    python3 -m agent.humboldt assess <law-id>
    python3 -m agent.humboldt theorize
    python3 -m agent.humboldt inventory
"""

import sys
import os
import json
import datetime
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from . import retrieval as ret
from . import synthesizer as synth
from . import prompts

RESEARCH_DIR = Path(__file__).parent.parent / "research"
LAWS_DIR = RESEARCH_DIR / "laws"
HYPOTHESES_DIR = RESEARCH_DIR / "hypotheses"
THEORIES_DIR = RESEARCH_DIR / "theories"
DATA_DIR = Path(__file__).parent.parent / "data" / "sessions"


def _load_inventory() -> str:
    """Load all law YAML files as a single string."""
    files = sorted(LAWS_DIR.glob("*.yaml"))
    if not files:
        return "(no laws in inventory yet)"
    parts = []
    for f in files:
        parts.append(f"--- {f.name} ---\n" + f.read_text())
    return "\n\n".join(parts)


def _session_log_path(slug: str) -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    date = datetime.date.today().isoformat()
    return DATA_DIR / f"{date}-{slug}.md"


def cmd_investigate(topic: str, namespaces: list[str] = ret.NS_BROAD):
    """Open-ended investigation of a topic."""
    soul = prompts.load_soul()
    print(f"\n=== HUMBOLDT: Investigating '{topic}' ===\n")

    # Generate targeted retrieval queries
    print("Generating retrieval queries...")
    sys_q, usr_q = prompts.hypothesis_prompt(soul, topic)
    queries_raw = synth.synthesize(sys_q, f"Generate 4 targeted search queries for: {topic}. Output only the queries, one per line.")
    queries = [l.strip().lstrip("0123456789. ") for l in queries_raw.splitlines() if l.strip()][:4]
    print(f"Queries: {queries}\n")

    # Retrieve from corpus
    print(f"Retrieving from corpus (namespaces: {namespaces})...")
    chunks = ret.multi_retrieve(queries, namespaces=namespaces, top_k_each=8)
    print(f"Retrieved {len(chunks)} unique chunks.\n")

    if not chunks:
        print("No corpus results found. Corpus may be thin on this topic.")
        return

    # Synthesis
    print("Synthesizing candidate laws...\n")
    system, user = prompts.investigation_prompt(soul, topic, chunks[:20])
    output = synth.synthesize_streaming(system, user)

    # Save session log
    slug = topic.lower().replace(" ", "-")[:40]
    log_path = _session_log_path(slug)
    log_path.write_text(
        f"# Humboldt Session — {topic}\n"
        f"Date: {datetime.date.today().isoformat()}\n\n"
        f"## Retrieval queries\n"
        + "\n".join(f"- {q}" for q in queries)
        + f"\n\n## Retrieved chunks: {len(chunks)}\n\n"
        f"## Synthesis output\n\n{output}\n"
    )
    print(f"\nSession log saved: {log_path}")
    print("Next: review output, create law YAML files in research/laws/")


def cmd_hypothesize(topic: str):
    """Generate candidate law hypotheses without writing files."""
    soul = prompts.load_soul()
    print(f"\n=== HUMBOLDT: Hypothesizing on '{topic}' ===\n")
    system, user = prompts.hypothesis_prompt(soul, topic)
    synth.synthesize_streaming(system, user)


def cmd_assess(law_id: str, namespaces: list[str] = ret.NS_ALL):
    """Gather evidence for a specific law."""
    soul = prompts.load_soul()
    law_files = list(LAWS_DIR.glob(f"{law_id}*.yaml"))
    if not law_files:
        print(f"No law file found matching '{law_id}' in {LAWS_DIR}")
        sys.exit(1)

    import yaml
    law = yaml.safe_load(law_files[0].read_text())
    statement = law.get("statement", "")
    print(f"\n=== HUMBOLDT: Assessing {law.get('id')} — {law.get('name')} ===\n")

    # Build adversarial + supporting queries
    queries = [
        statement[:200],
        f"counterexample {law.get('name', '')}",
        f"mechanism {law.get('name', '')}",
    ]
    if law.get("domains"):
        for d in law["domains"][:2]:
            queries.append(f"{law.get('name', '')} {d}")

    chunks = ret.multi_retrieve(queries, namespaces=namespaces, top_k_each=10)
    print(f"Retrieved {len(chunks)} unique chunks.\n")

    system, user = prompts.evidence_prompt(soul, statement, chunks[:20])
    print("Analyzing evidence...\n")
    synth.synthesize_streaming(system, user)


def cmd_theorize():
    """Scan inventory for unification opportunities."""
    soul = prompts.load_soul()
    inventory = _load_inventory()
    if "no laws" in inventory:
        print("Inventory is empty. Run 'investigate' first.")
        return

    print("\n=== HUMBOLDT: Theorizing across inventory ===\n")
    system, user = prompts.theorize_prompt(soul, inventory)
    output = synth.synthesize_streaming(system, user)

    slug = f"theory-{datetime.date.today().isoformat()}"
    log_path = _session_log_path(slug)
    log_path.write_text(f"# Humboldt Theory Session\nDate: {datetime.date.today().isoformat()}\n\n{output}\n")
    print(f"\nSession log saved: {log_path}")


def cmd_inventory():
    """Display current law inventory."""
    files = sorted(LAWS_DIR.glob("*.yaml"))
    if not files:
        print("Law inventory is empty.")
        return

    import yaml
    print(f"\n=== HUMBOLDT Law Inventory — {len(files)} laws ===\n")
    by_confidence = {}
    for f in files:
        law = yaml.safe_load(f.read_text())
        conf = law.get("confidence", "speculative")
        by_confidence.setdefault(conf, []).append(law)

    for conf in ["established", "candidate", "contested", "speculative"]:
        laws = by_confidence.get(conf, [])
        if laws:
            print(f"[{conf.upper()}]")
            for l in laws:
                print(f"  {l.get('id')} — {l.get('name')}")
                domains = l.get("domains", [])
                if domains:
                    print(f"          domains: {', '.join(str(d) for d in domains[:3])}")
            print()


USAGE = """
Usage:
  python3 -m agent.humboldt investigate "<topic>"   # open-ended investigation
  python3 -m agent.humboldt hypothesize "<topic>"   # propose candidate laws (no files)
  python3 -m agent.humboldt assess <law-id>         # gather evidence for a law
  python3 -m agent.humboldt theorize                # find unification opportunities
  python3 -m agent.humboldt inventory               # show current law inventory
"""


def main():
    args = sys.argv[1:]
    if not args:
        print(USAGE)
        sys.exit(0)

    cmd = args[0]
    rest = args[1:]

    if cmd == "investigate":
        if not rest:
            print("Usage: humboldt investigate \"<topic>\"")
            sys.exit(1)
        cmd_investigate(" ".join(rest))
    elif cmd == "hypothesize":
        if not rest:
            print("Usage: humboldt hypothesize \"<topic>\"")
            sys.exit(1)
        cmd_hypothesize(" ".join(rest))
    elif cmd == "assess":
        if not rest:
            print("Usage: humboldt assess <law-id>  (e.g. L-001)")
            sys.exit(1)
        cmd_assess(rest[0])
    elif cmd == "theorize":
        cmd_theorize()
    elif cmd == "inventory":
        cmd_inventory()
    else:
        print(f"Unknown command: {cmd}")
        print(USAGE)
        sys.exit(1)


if __name__ == "__main__":
    main()
