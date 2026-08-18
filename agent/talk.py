"""
talk.py — conference talk engine (plans/talk-2026-09-23.md).

Composes a talk track from Humboldt's own law records rather than retrieval, the
same freeze-immune property as ``induct`` (composition from records is not a
corpus read). Four subcommands:

    draft   brief.md + slides.yaml + law records -> track.md (Opus)
    voice   track.md -> audio/slide-NN.mp3 (macOS `say` -> ffmpeg)
    time    measure rendered audio against the slide/talk targets (ffprobe)
    check   lint word budgets and TTS hazards in track.md before voicing

The epistemic/stylistic bar for narration lives in ``prompts/talk.md`` (supervisor-
editable, same pattern as induct.md). This module is the harness.

Usage:
    python3 -m agent.humboldt talk draft
    python3 -m agent.humboldt talk draft --dry-run
    python3 -m agent.humboldt talk voice [--voice Daniel] [--rate 140]
    python3 -m agent.humboldt talk time
    python3 -m agent.humboldt talk check
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

from agent import laws as laws_mod

_ROOT = Path(__file__).parent.parent
_TALK_DIR = _ROOT / "talks" / "2026-09-23-new-nature"
_BRIEF = _TALK_DIR / "brief.md"
_SLIDES = _TALK_DIR / "slides.yaml"
_TRACK = _TALK_DIR / "track.md"
_AUDIO_DIR = _TALK_DIR / "audio"
_TIMING = _TALK_DIR / "timing.json"
_PROMPT = _ROOT / "prompts" / "talk.md"
_IDENTITY = _ROOT / "IDENTITY.md"
_OODA = _ROOT / "methods" / "M-000-ooda.md"

TALK_MODEL = "claude-opus-4-8"   # brief.md / plan: draft is a heavy-lift composition pass
TALK_MAX_TOKENS = 8000

DEFAULT_VOICE = "Daniel"
DEFAULT_RATE = 140

# TTS-hazard patterns (prompts/talk.md hard constraints) — flagged, not auto-fixed;
# a human should decide the rewrite.
_HAZARD_PATTERNS = {
    "bare law id": re.compile(r"\bL-0?\d{1,3}\b"),
    "arxiv id": re.compile(r"\barxiv[\s:-]?\d{4}\.\d{4,5}\b", re.I),
    "url": re.compile(r"https?://\S+|\b[\w-]+\.(?:org|com|io|net)\b"),
}
_LONG_PARENTHETICAL = re.compile(r"\(([^()]*)\)")
_EM_DASH = "—"


# ── Input gathering ──────────────────────────────────────────────────────────

def _load_slides() -> dict:
    return yaml.safe_load(_SLIDES.read_text())


def _identity_excerpt() -> str:
    if not _IDENTITY.exists():
        return "You are Humboldt, an artificial researcher investigating laws of the new nature."
    return _IDENTITY.read_text().strip()


def _method_excerpt() -> str:
    """Phase model + decision-gate summary for the metacognition slides (02, 03).

    Kept short and mechanical on purpose — the OODA doc itself is long and mostly
    about session-level orientation, which isn't what a 10-line stage summary needs.
    """
    ooda_gist = (
        _OODA.read_text().split("## The Core Insight", 1)[-1]
        .split("## Application History", 1)[0]
        .strip()
    ) if _OODA.exists() else ""
    phase_model = (
        "Double Freytag phase model: a law moves through exploration -> sensemaking "
        "-> valley -> heavy-lift -> retrospective. Nothing is ever 'established' — "
        "retrospective laws are unfalsified, which is a weaker and more honest claim. "
        "Confidence is tracked separately from stage: speculative -> provisional -> "
        "supported -> unfalsified, and confidence is capped by stage (a law cannot be "
        "rated more confident than its stage supports).\n\n"
        "Promotion runs on two funnel engines, not on judgment calls alone: `induct` "
        "reads the accumulated seed pool and recent reads and either drafts a new "
        "exploration-stage law, attaches evidence to an existing one, or leaves the "
        "material — zero new laws is a normal, respectable outcome of a sweep. "
        "`assess` takes one law against its own stated advance/challenge triggers "
        "(written when the law was created) and returns promote, hold, or demote. "
        "Every law ships with both triggers from the start — a law with no trigger "
        "can never be assessed, so drafting the trigger is part of drafting the law."
    )
    return phase_model + ("\n\n" + ooda_gist if ooda_gist else "")


def _law_records(slides: dict) -> str:
    ids = sorted({s["law_id"] for s in slides["slides"] if s.get("law_id")})
    parts = []
    for law_id in ids:
        law = laws_mod.load(law_id)
        parts.append(f"--- {law_id} ---\n{laws_mod.dumps(law)}")
    return "\n\n".join(parts)


def _format_slides(slides: dict) -> str:
    lines = []
    for s in slides["slides"]:
        lines.append(
            f"- {s['id']} [{s['beat']}] \"{s['title']}\" "
            f"(law: {s.get('law_id') or 'none'}, "
            f"budget: {s['word_budget']} words / {s['duration_target_s']}s)\n"
            f"    bullets: {' | '.join(s['bullets'])}\n"
            f"    notes: {s.get('notes', '').strip()}"
        )
    return "\n".join(lines)


def _build_prompt(slides: dict) -> str:
    tmpl = _PROMPT.read_text()
    return (
        tmpl.replace("{{IDENTITY_EXCERPT}}", _identity_excerpt())
            .replace("{{METHOD_EXCERPT}}", _method_excerpt())
            .replace("{{BRIEF}}", _BRIEF.read_text().strip())
            .replace("{{SLIDES}}", _format_slides(slides))
            .replace("{{LAW_RECORDS}}", _law_records(slides))
    )


# ── Model call + parse ───────────────────────────────────────────────────────

def _strip_fences(text: str) -> str:
    text = text.strip()
    m = re.match(r"^```(?:yaml)?\s*\n", text)
    if m:
        text = text[m.end():]
        text = re.sub(r"\n```\s*$", "", text)
    return text


def _parse_yaml(text: str) -> dict:
    data = yaml.safe_load(_strip_fences(text))
    if not isinstance(data, dict) or "slides" not in data:
        raise ValueError("talk draft response did not parse to {slides: {...}}")
    return data


# ── track.md read/write ──────────────────────────────────────────────────────

_SECTION_RE = re.compile(r"^## (\d{2}) — (.*)$", re.M)


def _write_track(slides: dict, narration: dict) -> None:
    lines = [
        "# Track — Some Candidate Laws of New Nature",
        "",
        "Generated by `talk draft` from slides.yaml + laws/*.yaml. This is the source of "
        "truth for narration — slides.yaml is what's projected, this is what's spoken. "
        "Edit narration directly; re-run `talk draft` only after laws or slides.yaml "
        "change, and re-check timing after any edit (plan risk 6 — do not let this drift "
        "from the records it was generated from).",
        "",
    ]
    for s in slides["slides"]:
        text = str(narration.get(s["id"], "")).strip()
        lines.append(f"## {s['id']} — {s['title']}")
        lines.append("")
        lines.append(text if text else "**MISSING — draft omitted this slide.**")
        lines.append("")
    _TRACK.write_text("\n".join(lines))


def _read_track() -> dict[str, str]:
    if not _TRACK.exists():
        raise FileNotFoundError(f"{_TRACK} does not exist — run `talk draft` first")
    text = _TRACK.read_text()
    matches = list(_SECTION_RE.finditer(text))
    out = {}
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out[m.group(1)] = text[start:end].strip()
    return out


# ── draft ─────────────────────────────────────────────────────────────────────

def draft(dry_run: bool = False) -> None:
    from dotenv import load_dotenv
    from agent import synthesizer as synth

    load_dotenv(_ROOT / ".env")

    slides = _load_slides()
    print(f"Drafting narration for {len(slides['slides'])} slides "
          f"(target {slides['meta']['speech_target_display']})...")

    prompt = _build_prompt(slides)
    text, stop_reason = synth.synthesize_full(
        system=prompt,
        user="Draft the full narration track now. Return only the YAML block.",
        model=TALK_MODEL,
        max_tokens=TALK_MAX_TOKENS,
        operation="talk-draft",
    )
    if stop_reason == "max_tokens":
        print("! warning: response hit max_tokens — track may be truncated; "
              "review before trusting it.")

    try:
        result = _parse_yaml(text)
    except Exception as e:  # noqa: BLE001
        print(f"! could not parse draft response: {e}\n\n{text[:1500]}")
        return

    narration = {str(k): v for k, v in (result.get("slides") or {}).items()}
    missing = [s["id"] for s in slides["slides"] if s["id"] not in narration]
    if missing:
        print(f"! draft omitted slide(s): {', '.join(missing)}")

    if dry_run:
        print("\n(dry-run — track.md not written)")
        for sid, txt in narration.items():
            wc = len(txt.split())
            print(f"  {sid}: {wc} words")
        return

    _TALK_DIR.mkdir(parents=True, exist_ok=True)
    _write_track(slides, narration)
    print(f"\nWrote {_TRACK}")
    print("  → run `humboldt talk check` before voicing.")


# ── check ─────────────────────────────────────────────────────────────────────

def _find_hazards(text: str) -> list[str]:
    hazards = []
    for name, pattern in _HAZARD_PATTERNS.items():
        hits = pattern.findall(text)
        if hits:
            hazards.append(f"{name}: {', '.join(sorted(set(hits))[:5])}")
    for paren in _LONG_PARENTHETICAL.findall(text):
        if len(paren.split()) > 12:
            hazards.append(f"long parenthetical ({len(paren.split())} words): ({paren[:60]}...)")
    for sentence in re.split(r"(?<=[.!?])\s+", text):
        if sentence.count(_EM_DASH) > 1:
            hazards.append(f"em-dash chain: {sentence[:80]}...")
    return hazards


def check() -> bool:
    """Returns True if the track is clean (no missing slides, no over-budget, no hazards)."""
    slides = _load_slides()
    try:
        narration = _read_track()
    except FileNotFoundError as e:
        print(f"! {e}")
        return False

    ok = True
    total_words = 0
    for s in slides["slides"]:
        sid, budget = s["id"], s["word_budget"]
        text = narration.get(sid, "")
        if not text or text.startswith("**MISSING"):
            print(f"  ✗ {sid}: no narration")
            ok = False
            continue
        wc = len(text.split())
        total_words += wc
        over = wc > budget
        marker = "✗" if over else "✓"
        if over:
            ok = False
        print(f"  {marker} {sid}: {wc}/{budget} words"
              f"{'  OVER BUDGET' if over else ''}")
        for hz in _find_hazards(text):
            print(f"      ! {hz}")
            ok = False

    target_words = slides["meta"]["speech_target_s"] * slides["meta"]["wpm_effective"] / 60
    print(f"\nTotal: {total_words} words (speech-target ballpark: {target_words:.0f} words "
          f"for {slides['meta']['speech_target_display']} at {slides['meta']['wpm_effective']} wpm)")
    print("CLEAN" if ok else "ISSUES FOUND — see above")
    return ok


# ── voice ─────────────────────────────────────────────────────────────────────

def voice(voice_name: str = DEFAULT_VOICE, rate: int = DEFAULT_RATE) -> None:
    slides = _load_slides()
    narration = _read_track()
    _AUDIO_DIR.mkdir(parents=True, exist_ok=True)

    for s in slides["slides"]:
        sid = s["id"]
        text = narration.get(sid, "").strip()
        if not text or text.startswith("**MISSING"):
            print(f"  ! {sid}: skipped, no narration")
            continue
        aiff = _AUDIO_DIR / f"slide-{sid}.aiff"
        mp3 = _AUDIO_DIR / f"slide-{sid}.mp3"
        subprocess.run(
            ["say", "-v", voice_name, "-r", str(rate), "-o", str(aiff), text],
            check=True,
        )
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-i", str(aiff), str(mp3)],
            check=True,
        )
        aiff.unlink()
        print(f"  {sid}: {mp3.name}")
    print(f"\nVoiced with '{voice_name}' at rate {rate}. Run `humboldt talk time` to measure.")


# ── time ──────────────────────────────────────────────────────────────────────

def _ffprobe_duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True, check=True,
    )
    return float(out.stdout.strip())


def time_() -> None:
    slides = _load_slides()
    if not _AUDIO_DIR.exists():
        print(f"! {_AUDIO_DIR} does not exist — run `talk voice` first")
        return

    rows = []
    running = 0.0
    for s in slides["slides"]:
        sid = s["id"]
        mp3 = _AUDIO_DIR / f"slide-{sid}.mp3"
        if not mp3.exists():
            print(f"  ✗ {sid}: no audio rendered")
            continue
        dur = _ffprobe_duration(mp3)
        running += dur
        target = s["duration_target_s"]
        delta = dur - target
        flag = "  ⚠ over target" if dur > target * 1.25 else ""
        print(f"  {sid}: {dur:5.1f}s (target {target}s, {delta:+.1f}s){flag}")
        rows.append({"id": sid, "duration_s": round(dur, 2), "target_s": target})

    speech_target = slides["meta"]["speech_target_s"]
    soft_cap = slides["meta"]["soft_cap_s"]
    hard_cap = slides["meta"]["hard_cap_s"]
    print(f"\nTotal: {running:.1f}s ({running/60:.1f} min) — "
          f"speech target {speech_target}s, soft cap {soft_cap}s, hard cap {hard_cap}s")
    if running > hard_cap:
        print("  ✗ OVER HARD CAP — must cut before this can be delivered")
    elif running > soft_cap:
        print("  ⚠ over soft target — trim if possible")
    else:
        print("  ✓ within target")

    _TIMING.write_text(json.dumps(
        {"slides": rows, "total_s": round(running, 2),
         "speech_target_s": speech_target, "soft_cap_s": soft_cap, "hard_cap_s": hard_cap},
        indent=2,
    ))
    print(f"\nWrote {_TIMING}")


# ── CLI entry points ─────────────────────────────────────────────────────────

def cmd_talk(subcmd: str, rest: list[str]) -> None:
    if subcmd == "draft":
        draft(dry_run="--dry-run" in rest)
    elif subcmd == "check":
        ok = check()
        if not ok:
            sys.exit(1)
    elif subcmd == "voice":
        v = rest[rest.index("--voice") + 1] if "--voice" in rest else DEFAULT_VOICE
        r = int(rest[rest.index("--rate") + 1]) if "--rate" in rest else DEFAULT_RATE
        voice(voice_name=v, rate=r)
    elif subcmd == "time":
        time_()
    else:
        print(f"Unknown talk subcommand: {subcmd}")
        print("Available: draft [--dry-run], check, voice [--voice NAME] [--rate N], time")
        sys.exit(1)
