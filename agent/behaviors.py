"""
Behavior graph admin — MDP visualization, visit logging, and supervisory analysis.

CLI:
    humboldt behaviors admin          # start admin web UI (localhost:7878)
    humboldt behaviors graph          # text summary of phase assignments
    humboldt behaviors log <id>       # append a behavior visit to log.jsonl
    humboldt behaviors supervisory    # analyze log and suggest weight updates
"""

import http.server
import json
import os
import sys
import webbrowser
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import yaml

_ROOT = Path(__file__).parent.parent
_BEHAVIORS_DIR = _ROOT / "behaviors"
_REGISTRY_PATH = _BEHAVIORS_DIR / "registry.yaml"
_MDP_PATH = _BEHAVIORS_DIR / "mdp.yaml"
_LOG_PATH = _BEHAVIORS_DIR / "log.jsonl"
_ADMIN_HTML = _BEHAVIORS_DIR / "admin.html"
_PORT = 7878

PHASE_ORDER = ["liminal", "exploration", "sensemaking", "valley", "heavy_lift", "retrospective"]

# Phases outside the Double Freytag arc flow, printed after PHASE_ORDER.
OUT_OF_FLOW_PHASES = ["any"]


# ── Data loaders ─────────────────────────────────────────────────────────────

def _load_registry() -> list[dict]:
    data = yaml.safe_load(_REGISTRY_PATH.read_text())
    return data.get("behaviors", [])


def _load_mdp() -> dict:
    if _MDP_PATH.exists():
        return yaml.safe_load(_MDP_PATH.read_text()) or {}
    return {}


def _save_mdp(data: dict) -> None:
    _MDP_PATH.write_text(
        yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)
    )


def _load_log() -> list[dict]:
    if not _LOG_PATH.exists():
        return []
    entries = []
    for line in _LOG_PATH.read_text().splitlines():
        line = line.strip()
        if line:
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return entries


# ── Supervisory analysis ─────────────────────────────────────────────────────

def _run_supervisory_analysis() -> dict:
    entries = _load_log()
    mdp = _load_mdp()

    if not entries:
        return {"status": "no_data", "message": "Behavior log is empty — visit some behaviors first."}

    # Observed transition counts (consecutive pairs)
    obs_counts: dict[tuple, int] = {}
    phase_durations: dict[str, list[int]] = {}  # phase → list of run lengths
    current_phase = entries[0].get("phase")
    run_len = 1

    for i in range(len(entries) - 1):
        a_id = entries[i]["behavior_id"]
        b_id = entries[i + 1]["behavior_id"]
        obs_counts[(a_id, b_id)] = obs_counts.get((a_id, b_id), 0) + 1

        # Phase duration tracking
        next_phase = entries[i + 1].get("phase")
        if next_phase == current_phase:
            run_len += 1
        else:
            phase_durations.setdefault(current_phase, []).append(run_len)
            current_phase = next_phase
            run_len = 1
    phase_durations.setdefault(current_phase, []).append(run_len)

    # Build MDP edge weight lookup (expand bidirectional)
    mdp_weights: dict[tuple, float] = {}
    for t in mdp.get("transitions", []):
        mdp_weights[(t["from"], t["to"])] = t["weight"]
        if t.get("bidirectional"):
            mdp_weights[(t["to"], t["from"])] = t["weight"]

    # Per-source outgoing totals for normalization
    source_totals: dict[str, float] = {}
    for (a, b), w in mdp_weights.items():
        source_totals[a] = source_totals.get(a, 0.0) + w

    total_transitions = sum(obs_counts.values())

    # Compute suggestions
    suggestions = []
    for (a, b), count in sorted(obs_counts.items(), key=lambda x: -x[1]):
        obs_freq = count / total_transitions
        mdp_w = mdp_weights.get((a, b))
        if mdp_w is None:
            suggestions.append({
                "type": "missing_edge",
                "from": a, "to": b,
                "observed_freq": round(obs_freq, 3),
                "message": f"Observed but not in MDP — consider adding edge {a}→{b}",
            })
        else:
            # Normalized MDP probability
            total_from = source_totals.get(a, 1.0)
            mdp_prob = mdp_w / total_from
            if abs(obs_freq - mdp_prob) > 0.07:
                direction = "↑" if obs_freq > mdp_prob else "↓"
                suggestions.append({
                    "type": "weight_mismatch",
                    "from": a, "to": b,
                    "current_weight": mdp_w,
                    "observed_freq": round(obs_freq, 3),
                    "mdp_prob": round(mdp_prob, 3),
                    "direction": direction,
                    "suggested_weight": round(mdp_w * (obs_freq / mdp_prob), 3),
                    "message": f"{a}→{b}: MDP prob {mdp_prob:.1%}, observed {obs_freq:.1%} {direction}",
                })

    # Phase stuckness analysis
    stuckness = []
    for phase, runs in phase_durations.items():
        avg = sum(runs) / len(runs)
        mx = max(runs)
        if avg > 10 or mx > 20:
            stuckness.append({
                "phase": phase,
                "avg_run_length": round(avg, 1),
                "max_run_length": mx,
                "message": f"{phase}: avg run {avg:.1f} steps, max {mx} — possible stuckness",
            })

    return {
        "status": "ok",
        "log_entries": len(entries),
        "unique_transitions": len(obs_counts),
        "phase_durations": {p: {"avg": round(sum(v)/len(v), 1), "max": max(v)} for p, v in phase_durations.items()},
        "suggestions": suggestions[:20],
        "stuckness": stuckness,
    }


# ── Admin HTTP server ─────────────────────────────────────────────────────────

class _AdminHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path in ("/", "/admin"):
            self._serve_file(_ADMIN_HTML, "text/html; charset=utf-8")
        elif self.path == "/api/behaviors":
            self._serve_json(self._api_behaviors())
        elif self.path == "/api/mdp":
            self._serve_json(self._api_mdp())
        elif self.path == "/api/log":
            self._serve_json(_load_log())
        elif self.path == "/api/supervisory":
            self._serve_json(_run_supervisory_analysis())
        else:
            self.send_error(404, "Not found")

    def do_POST(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        if self.path == "/api/mdp":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            data = json.loads(body)
            _save_mdp(data)
            self._serve_json({"status": "saved"})
        elif self.path == "/api/log":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            entry = json.loads(body)
            with open(_LOG_PATH, "a") as f:
                f.write(json.dumps(entry) + "\n")
            self._serve_json({"status": "logged"})
        else:
            self.send_error(404, "Not found")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def _serve_file(self, path: Path, content_type: str):
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", len(data))
        self.end_headers()
        self.wfile.write(data)

    def _serve_json(self, data):
        body = json.dumps(data, default=str).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(body))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _api_behaviors(self) -> dict:
        registry = _load_registry()
        mdp = _load_mdp()
        virtual = mdp.get("virtual_nodes", [])
        return {"behaviors": registry, "virtual_nodes": virtual}

    def _api_mdp(self) -> dict:
        return _load_mdp()

    def log_message(self, fmt, *args):  # suppress per-request logging
        pass


def run_admin():
    """Start the admin server and open browser."""
    url = f"http://127.0.0.1:{_PORT}/"
    server = http.server.HTTPServer(("127.0.0.1", _PORT), _AdminHandler)
    print(f"Behaviors admin: {url}")
    print("Ctrl-C to stop.")
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nAdmin server stopped.")


# ── CLI functions ─────────────────────────────────────────────────────────────

def cmd_graph():
    """Print text summary of behaviors by phase."""
    registry = _load_registry()
    mdp = _load_mdp()
    virtual = mdp.get("virtual_nodes", [])

    by_phase: dict[str, list] = {}
    for b in registry + virtual:
        phase = b.get("phase", "unknown")
        by_phase.setdefault(phase, []).append(b)

    total = sum(len(v) for v in by_phase.values())
    print(f"Behavior graph — {total} nodes across {len(by_phase)} phases\n")

    for phase in PHASE_ORDER + OUT_OF_FLOW_PHASES:
        behaviors = by_phase.get(phase, [])
        if not behaviors:
            print(f"  {phase.upper():16s}  (empty)")
            continue
        print(f"  {phase.upper():16s}  {len(behaviors)} behaviors")
        for b in behaviors:
            status = b.get("status", b.get("state", "?"))
            marker = {"active": "●", "proposed": "○", "retired": "·"}.get(status, "?")
            print(f"    {marker} {b['id']:22s}  {b.get('name', '')}")

    mdp_trans = mdp.get("transitions", [])
    phase_of = {b["id"]: b.get("phase") for b in registry + virtual}
    within = sum(1 for t in mdp_trans
                 if phase_of.get(t["from"]) == phase_of.get(t["to"]))
    cross = sum(1 for t in mdp_trans if t.get("cross_phase"))
    cycle = sum(1 for t in mdp_trans if t.get("cycle_back"))
    feedback = sum(1 for t in mdp_trans if t.get("feedback"))
    untriggered = [t for t in mdp_trans if not t.get("trigger")]
    print(f"\n  MDP edges: {len(mdp_trans)} total  ({within} within-phase, "
          f"{cross} cross-phase, {cycle} cycle-back, {feedback} feedback)")
    if untriggered:
        # Every edge must carry a trigger (§6.2) — an untriggered edge is a weight
        # with no stated reason, which is what made the v1 graph unfalsifiable.
        print(f"  ⚠ {len(untriggered)} edge(s) missing a trigger:")
        for t in untriggered:
            print(f"      {t['from']} → {t['to']}")


def cmd_log_visit(behavior_id: str, arc_id: Optional[str] = None, note: Optional[str] = None):
    """Append a behavior visit to log.jsonl."""
    registry = _load_registry()
    mdp = _load_mdp()
    all_behaviors = {b["id"]: b for b in registry + mdp.get("virtual_nodes", [])}

    b = all_behaviors.get(behavior_id)
    if not b:
        print(f"Error: unknown behavior '{behavior_id}'", file=sys.stderr)
        print("Known behaviors:", ", ".join(sorted(all_behaviors.keys())), file=sys.stderr)
        sys.exit(1)

    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "behavior_id": behavior_id,
        "phase": b.get("phase", "unknown"),
        "arc_id": arc_id,
        "note": note,
    }
    with open(_LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"Logged: {behavior_id} (phase={b.get('phase')}) @ {entry['timestamp'][:16]}Z")


def cmd_supervisory():
    """Analyze behavior log and print weight update suggestions."""
    result = _run_supervisory_analysis()

    if result["status"] == "no_data":
        print(result["message"])
        return

    print(f"Supervisory analysis — {result['log_entries']} log entries\n")

    print("Phase durations (avg / max behavior-steps spent per phase run):")
    for phase, stats in result["phase_durations"].items():
        bar = "█" * min(int(stats["avg"]), 30)
        print(f"  {phase:16s}  avg={stats['avg']:5.1f}  max={stats['max']:3d}  {bar}")

    if result.get("stuckness"):
        print("\n⚠ Potential stuckness detected:")
        for s in result["stuckness"]:
            print(f"  {s['message']}")

    if result.get("suggestions"):
        print(f"\nWeight adjustment suggestions ({len(result['suggestions'])}):")
        for s in result["suggestions"]:
            print(f"  {s['message']}")
    else:
        print("\nNo weight adjustments needed — graph looks well-calibrated.")
