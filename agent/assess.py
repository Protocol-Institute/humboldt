"""
assess.py — the assessment pass (funnel stage 6, and stage 8 challenge mode).

Assessment is the promotion gate. Where induction is generous (turn material into
laws), assessment is deliberately harsh: it resists promotion until the law's
``advance`` trigger is literally met with cited evidence, and it actively hunts
for reasons to demote. A funnel that promotes on rhetorical momentum produces an
encyclopedia nobody should trust — so the default verdict is HOLD, and the value
it emits on a HOLD is a *gap*: the specific, executable missing thing that becomes
the law's work queue.

The epistemic standard lives in ``prompts/assess.md`` (Fable, supervisor-editable).
This module is the harness: assemble the law record plus new evidence (a corpus
retrieval on the law), call the model — Sonnet for routine laws, Opus for
heavy-lift and retrospective laws — parse the verdict, and apply PROMOTE / HOLD /
DEMOTE through the ``agent/laws.py`` stage machine.

Retrospective laws are assessed in *challenge mode*: the pass skips the promotion
step and only hunts for disconfirmation; a surviving challenge demotes and flags
the law ``challenged``.

Usage:
    python3 -m agent.humboldt assess L-003
    python3 -m agent.humboldt assess L-003 --dry-run    # call the model, apply nothing
    python3 -m agent.humboldt assess --all               # sweep every active law
    python3 -m agent.humboldt assess --all --dry-run
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from agent import funnel_log
from agent import law_notify
from agent import laws as laws_mod
from agent import retrieval as ret

_ROOT = Path(__file__).parent.parent
_METHOD = _ROOT / "METHOD.md"
_PROMPT = _ROOT / "prompts" / "assess.md"

ASSESS_MODEL_ROUTINE = "claude-sonnet-4-6"      # §5 stage 6 routine tier
ASSESS_MODEL_HARD = "claude-opus-4-8"           # heavy-lift + retrospective laws
_HARD_STAGES = {"heavy-lift", "retrospective"}


def _model_for(law) -> str:
    return ASSESS_MODEL_HARD if law.get("stage") in _HARD_STAGES else ASSESS_MODEL_ROUTINE


# ── Input gathering ───────────────────────────────────────────────────────────

def _method_excerpt() -> str:
    if not _METHOD.exists():
        return ""
    return _METHOD.read_text().strip()[:2500]


def _retrieve_new_evidence(law) -> str:
    """A corpus retrieval on the law — the 'material accumulated since the last
    assessment' the pass weighs. Every excerpt is citable as a corpus retrieval."""
    title = str(law.get("title", "")).strip()
    stmt = str(law.get("statement", "")).strip().replace("\n", " ")
    queries = [q for q in (title, stmt[:200]) if q]
    if not queries:
        return "(no query could be formed from the law record)"
    try:
        chunks = ret.multi_retrieve(queries, namespaces=ret.NS_BROAD, top_k_each=8)
    except ret.RetrievalUnavailable as e:
        # Only reachable under --no-corpus; assess() refuses up front otherwise.
        # Stated flatly so the verdict prompt cannot mistake it for a thin corpus.
        return (f"(NO CORPUS ACCESS — {e}. This assessment is running on the law "
                f"record alone. Do not treat the absence of new evidence as "
                f"evidence of absence, and do not promote on this basis.)")
    except Exception as e:  # noqa: BLE001 — a transient fault must not crash the pass
        return f"(corpus retrieval failed: {e})"
    if not chunks:
        return "(corpus retrieval returned nothing on this law)"
    parts = []
    for i, c in enumerate(chunks[:10], 1):
        meta = c.get("metadata", {}) or {}
        source = meta.get("title") or meta.get("source") or c.get("id", "unknown")
        ns = c.get("namespace", "")
        text = (meta.get("text") or c.get("text") or "").strip()
        parts.append(f"[corpus:{ns}:{source}]\n{text[:700]}")
    return "\n\n---\n\n".join(parts)


# Stage-appropriate fallback triggers. Step 1 of the assessment prompt evaluates
# the law's `advance` trigger; a law whose trigger is empty — as every law created
# by an induction sweep before 2026-08-10 was — gives the model nothing to
# evaluate and can never be promoted. These defaults restate the schema's own
# stage-entry criteria (laws/_schema.yaml, STAGE MACHINE RULES) so assessment
# degrades to "does this law meet the bar for the next stage" rather than failing.
# They are used for the prompt only and are never written to the record: the
# supervisor owns trigger wording.
_DEFAULT_ADVANCE = {
    "exploration":
        "Statement, causal mechanism, and falsification condition are all present "
        "and mutually consistent, with at least one concrete checkable example.",
    "sensemaking":
        "Supporting evidence from at least two independent domains, and the "
        "mechanism survives the sharpest counterexample currently on the record.",
    "valley":
        "Evidence from 3+ genuinely independent domains, with the open cruxes "
        "either resolved or explicitly scoped out of the statement.",
    "heavy-lift":
        "A separation artifact — a publishable writeup of the law, its evidence, "
        "and its boundary conditions — is complete.",
    "retrospective":
        "Terminal stage: no advance. Assess in challenge mode only.",
}
_DEFAULT_CHALLENGE = (
    "A documented case meeting the law's stated conditions in which the predicted "
    "regularity does not hold, which survives one assessment pass."
)


def _record_for_prompt(law) -> tuple[str, list[str]]:
    """The law record as YAML for the prompt, with empty triggers defaulted.

    Normally the file text is used verbatim so hand-authored comments and folded
    scalars reach the model as the supervisor wrote them. Only when a trigger is
    blank is a patched copy dumped instead. Returns ``(yaml_text, warnings)``.
    """
    path = laws_mod.path_for(law["id"])
    record_yaml = path.read_text()
    triggers = law.get("triggers") or {}
    advance = str(triggers.get("advance") or "").strip()
    challenge = str(triggers.get("challenge") or "").strip()
    if advance and challenge:
        return record_yaml, []

    import copy

    warnings = []
    patched = copy.deepcopy(law)
    filled = dict(patched.get("triggers") or {})
    if not advance:
        filled["advance"] = _DEFAULT_ADVANCE.get(
            law.get("stage"), _DEFAULT_ADVANCE["exploration"])
        warnings.append("advance")
    if not challenge:
        filled["challenge"] = _DEFAULT_CHALLENGE
        warnings.append("challenge")
    patched["triggers"] = filled
    return laws_mod.dumps(patched), warnings


def _build_prompt(law, new_evidence: str) -> str:
    record_yaml, warnings = _record_for_prompt(law)
    if warnings:
        print(f"  ! {law['id']}: empty {'/'.join(warnings)} trigger — assessing "
              "against the stage-default condition. Supervisor should write a real "
              "trigger on this record.")
    tmpl = _PROMPT.read_text()
    return (
        tmpl.replace("{{METHOD_EXCERPT}}", _method_excerpt())
            .replace("{{LAW_RECORD}}", record_yaml)
            .replace("{{NEW_EVIDENCE}}", new_evidence)
    )


# ── Parse ─────────────────────────────────────────────────────────────────────

def _strip_fences(text: str) -> str:
    text = text.strip()
    m = re.match(r"^```(?:yaml)?\s*\n", text)
    if m:
        text = text[m.end():]
        text = re.sub(r"\n```\s*$", "", text)
    return text


def _parse_yaml(text: str) -> dict:
    data = yaml.safe_load(_strip_fences(text))
    if not isinstance(data, dict):
        raise ValueError("assessment response did not parse to a mapping")
    return data


def _parse_stage_change(raw: str | None) -> str | None:
    """'valley -> heavy-lift' → 'heavy-lift'."""
    if not raw:
        return None
    m = re.search(r"->\s*([a-z-]+)", str(raw))
    return m.group(1).strip() if m else None


def _parse_confidence_target(raw: str | None) -> str | None:
    if not raw:
        return None
    m = re.search(r"->\s*([a-z]+)", str(raw))
    tgt = m.group(1).strip() if m else None
    return tgt if tgt in laws_mod.CONFIDENCE else None


# ── Verdict application ───────────────────────────────────────────────────────

def _apply_counterexamples(law, added: list) -> None:
    for ce in added or []:
        if not isinstance(ce, dict):
            continue
        item = {"domain": ce.get("domain", ""), "description": ce.get("description", ""),
                "source": ce.get("source", ""),
                "resolution": ce.get("resolution") or "OPEN"}
        law.setdefault("counterexamples", []).append(item)
        laws_mod.add_history(law, "counterexample",
                             str(item["description"])[:120] or "counterexample added")
        funnel_log.law_event("counterexample", law["id"], detail=str(item["description"])[:100])


def _apply_verdict(law, v: dict) -> str:
    verdict = str(v.get("verdict", "HOLD")).strip().upper()
    challenge = v.get("strongest_challenge") or {}
    resolution = str(challenge.get("resolution", "")).strip()
    if challenge.get("outcome") == "resolved" and resolution:
        laws_mod.add_history(law, "resolved", resolution[:150])

    if verdict == "PROMOTE":
        detail = str(v.get("trigger_evaluation", "advance trigger met")).strip()[:200]
        pre = law["stage"]
        laws_mod.advance(law, detail)
        tgt_conf = _parse_confidence_target(v.get("confidence_change"))
        if tgt_conf:
            try:
                laws_mod.set_confidence(law, tgt_conf,
                                        str(v.get("confidence_change", "")).strip()[:120])
            except ValueError as e:
                print(f"    ! confidence change skipped: {e}")
        funnel_log.law_event("promoted", law["id"], detail=f"{pre} -> {law['stage']}",
                             stage=law["stage"], confidence=law.get("confidence"))
        return f"PROMOTE {pre} → {law['stage']}"

    if verdict == "DEMOTE":
        pre = law["stage"]
        target = _parse_stage_change(v.get("stage_change"))
        if not target or laws_mod.stage_index(target) >= laws_mod.stage_index(pre):
            # fall back to one stage down
            target = laws_mod.STAGES[max(0, laws_mod.stage_index(pre) - 1)]
        detail = (challenge.get("description") or v.get("trigger_evaluation")
                  or "challenge survived").strip()[:200]
        laws_mod.cycle_back(law, target, detail)
        if pre == "retrospective":
            laws_mod.mark_challenged(law, "challenge survived retrospective assessment")
        funnel_log.law_event("demoted", law["id"], detail=f"{pre} -> {law['stage']}",
                             stage=law["stage"])
        return f"DEMOTE {pre} → {law['stage']}"

    # HOLD (default)
    gap = str(v.get("gap", "")).strip()
    if gap:
        oq = law.setdefault("open_questions", [])
        if gap not in [str(q) for q in oq]:
            oq.append(gap)
    laws_mod.add_history(law, "edited", f"assessment HOLD — gap: {gap[:150]}")
    funnel_log.law_event("assessed-hold", law["id"], detail=gap[:120])
    return f"HOLD — gap: {gap[:80]}"


# ── Entry points ──────────────────────────────────────────────────────────────

def _assess_one(law, dry_run: bool) -> str:
    from agent import synthesizer as synth

    model = _model_for(law)
    mode = "challenge" if law.get("stage") == "retrospective" else "promotion"
    print(f"\nAssessing {law['id']} [{law.get('stage')}/{law.get('status')}] "
          f"via {model} ({mode} mode)…")

    new_evidence = _retrieve_new_evidence(law)
    prompt = _build_prompt(law, new_evidence)

    # One retry on a malformed verdict. A dropped fence or a stray preamble is a
    # sampling accident, not a property of the law — and a PARSE-ERROR costs the
    # whole pass (retrieval included) for nothing. Two attempts, then give up.
    v = None
    for attempt in (1, 2):
        text, stop_reason = synth.synthesize_full(
            system=prompt,
            user="Run the assessment pass now. Return only the YAML block.",
            model=model,
            max_tokens=4000,
            operation="assess",
        )
        if stop_reason == "max_tokens":
            print("  ! warning: response hit max_tokens — verdict may be truncated.")
        try:
            v = _parse_yaml(text)
            break
        except Exception as e:  # noqa: BLE001
            if attempt == 1:
                print(f"  ! could not parse assessment ({e}) — retrying once.")
                continue
            print(f"  ! could not parse assessment on retry: {e}\n{text[:1200]}")
            return "PARSE-ERROR"

    verdict = str(v.get("verdict", "HOLD")).upper()
    ch = v.get("strongest_challenge") or {}
    print(f"  verdict: {verdict}"
          + (f"  ({v.get('stage_change')})" if v.get("stage_change") else ""))
    print(f"  trigger: {str(v.get('trigger_evaluation', ''))[:120]}")
    print(f"  challenge: {str(ch.get('outcome', 'n/a'))} — {str(ch.get('description', ''))[:100]}")
    if verdict == "HOLD":
        print(f"  gap: {str(v.get('gap', ''))[:140]}")

    if dry_run:
        print("  (dry-run — not applied)")
        return f"{verdict} (dry-run)"

    _apply_counterexamples(law, v.get("counterexamples_added"))
    outcome = _apply_verdict(law, v)
    laws_mod.save(law)

    if outcome.startswith("PROMOTE"):
        law_notify.queue("promoted", law)
    elif outcome.startswith("DEMOTE"):
        law_notify.queue("demoted", law)

    problems = laws_mod.validate(law)
    if problems:
        print("  ! post-assessment validation warnings:")
        for p in problems:
            print(f"      {p}")
    return outcome


def _corpus_gate(no_corpus: bool) -> bool:
    """False when the pass must not run. Assessment is the promotion gate: a
    verdict reached without the corpus is not a cheap verdict, it is a different
    and much weaker claim. Refuse by default rather than emit one that looks
    normal in the law's history."""
    from agent import read_budget as rb

    if not rb.is_paused():
        return True
    if no_corpus:
        print(f"  ! {rb.status_line()}\n  ! proceeding on --no-corpus: "
              f"records-only assessment, no new evidence will be weighed.")
        return True
    print(f"Assessment refused — {rb.status_line()}.\n"
          f"The promotion gate weighs new corpus evidence; with reads offline it "
          f"would verdict on an empty evidence slot.\n"
          f"Re-run after the quota resets, or pass --no-corpus to assess on the "
          f"law record alone (deliberately weaker).")
    return False


def assess(law_id: str, dry_run: bool = False, no_corpus: bool = False) -> None:
    from dotenv import load_dotenv

    load_dotenv(_ROOT / ".env")
    if not _corpus_gate(no_corpus):
        return
    try:
        law = laws_mod.load(law_id)
    except FileNotFoundError:
        print(f"No law record for {law_id!r}. See `humboldt laws list`.")
        return

    outcome = _assess_one(law, dry_run)

    if not dry_run:
        law_notify.flush()
        funnel_log.behavior_visit("assess", "valley", note=f"{law_id}: {outcome}")
        from agent.pre_notebook import append as pn_append
        pn_append(process="assess", summary=f"Assessed {law_id}: {outcome}",
                  detail={"law": law_id, "outcome": outcome})
    print(f"\n{law_id}: {outcome}")


def assess_all(dry_run: bool = False, no_corpus: bool = False) -> None:
    from dotenv import load_dotenv

    load_dotenv(_ROOT / ".env")
    if not _corpus_gate(no_corpus):
        return
    laws = [l for l in laws_mod.load_all() if l.get("status") != "falsified"]
    if not laws:
        print("No assessable laws.")
        return

    print(f"Assessment sweep — {len(laws)} law(s){' (dry-run)' if dry_run else ''}")
    outcomes = {}
    for law in laws:
        outcomes[law["id"]] = _assess_one(law, dry_run)

    print("\n── Sweep summary ──")
    for lid, out in outcomes.items():
        print(f"  {lid}: {out}")

    if not dry_run:
        law_notify.flush()
        promoted = [l for l, o in outcomes.items() if o.startswith("PROMOTE")]
        demoted = [l for l, o in outcomes.items() if o.startswith("DEMOTE")]
        summary = (f"Assessment sweep of {len(laws)} laws: "
                   f"{len(promoted)} promoted, {len(demoted)} demoted, "
                   f"{len(laws) - len(promoted) - len(demoted)} held.")
        funnel_log.behavior_visit("assess", "valley", note=summary)
        from agent.pre_notebook import append as pn_append
        pn_append(process="assess", summary=summary,
                  detail={"promoted": promoted, "demoted": demoted, "outcomes": outcomes})
        print(f"\n{summary}")
