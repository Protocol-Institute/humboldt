"""
console.py — the supervisor console (redesign §7).

One web app replacing behaviors/admin.html + the admin half of agent/behaviors.py.
Python stdlib HTTP server + a single-page frontend on port 7878, reading and writing
the repo's YAML directly: every save is a file edit the next ``git diff`` shows.

Six views (§7): Dashboard, Laws, Graph, Queue, Analytics, People.

Where it runs: bound to localhost, reached over an SSH tunnel once the daemon moves
to the exe.dev server (§12) — ``ssh humboldt-console`` forwards 7878 — so approvals,
law edits and trigger tuning happen from any device without a laptop session. It also
runs locally against the laptop checkout (same code); git is the reconciliation fabric.

It does not need the daemon running: it operates on files, and the daemon re-reads
registry/laws per task, so content changes need no restart.

GIT POLICY — deliberate deviation from §7. The spec says the console commits *and
pushes* each save. This implementation commits (tagged ``[console]``) but pushes only
with ``--push``. Auto-pushing every keystroke-level save from a laptop console onto a
shared branch is a surprising outward-facing side effect; on the server, where the
console is the only writer and git is the sync fabric, ``--push`` is the intended mode.

CAUTION: a save commits *the whole file it wrote*, not a diff of the edit. That is
correct on the server (the console is the only writer there) but means that running
the console on a laptop with unrelated uncommitted changes to laws/registry/mdp will
sweep those changes into a ``[console]`` commit with a narrow message. Commit your own
work before opening the console mid-session.
"""

from __future__ import annotations

import http.server
import io
import json
import subprocess
import webbrowser
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

import yaml
from ruamel.yaml import YAML

from agent import approval_queue as queue_mod
from agent import laws as laws_mod

_ROOT = Path(__file__).parent.parent
_BEHAVIORS_DIR = _ROOT / "behaviors"
_REGISTRY_PATH = _BEHAVIORS_DIR / "registry.yaml"
_MDP_PATH = _BEHAVIORS_DIR / "mdp.yaml"
_LOG_PATH = _BEHAVIORS_DIR / "log.jsonl"
_CONSOLE_HTML = _BEHAVIORS_DIR / "console.html"
_EVENTS_PATH = _ROOT / "analytics" / "events.jsonl"
_PEOPLE_PATH = _ROOT / "daemon" / "people.json"
_INBOX_DIR = _ROOT / "inbox"
_SEEDS_DIR = _ROOT / "laws" / "seeds"
_SHALLOW_DIR = _ROOT / "bibliography" / "shallow-reads"

_PORT = 7878
_PUSH = False   # set by run_console(push=True)


def _rt_yaml() -> YAML:
    y = YAML()
    y.preserve_quotes = True
    y.width = 100
    y.indent(mapping=2, sequence=4, offset=2)
    return y


# ── Git ──────────────────────────────────────────────────────────────────────

def _git(*args: str) -> tuple[int, str]:
    proc = subprocess.run(["git", *args], cwd=_ROOT,
                          capture_output=True, text=True)
    return proc.returncode, (proc.stdout + proc.stderr).strip()


def _commit(paths: list[Path], message: str) -> str | None:
    """Commit the given paths, tagged [console]. Returns a status line, or None
    when there was nothing to commit."""
    rel = [str(p.relative_to(_ROOT)) for p in paths]
    code, _ = _git("add", *rel)
    if code != 0:
        return "git add failed"
    code, out = _git("diff", "--cached", "--quiet")
    if code == 0:
        return None  # nothing staged
    code, out = _git("commit", "-m", f"[console] {message}")
    if code != 0:
        return f"commit failed: {out[:200]}"
    if _PUSH:
        code, out = _git("push")
        if code != 0:
            return f"committed; push failed: {out[:200]}"
        return "committed and pushed"
    return "committed"


# ── Loaders ──────────────────────────────────────────────────────────────────

def _load_registry() -> list[dict]:
    data = yaml.safe_load(_REGISTRY_PATH.read_text()) or {}
    return data.get("behaviors", []) or []


def _load_mdp() -> dict:
    return yaml.safe_load(_MDP_PATH.read_text()) or {} if _MDP_PATH.exists() else {}


def _load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


def _utilization() -> dict[str, int]:
    """Visits per behavior id, from the MDP log — fills registry `utilization: auto`."""
    counts: dict[str, int] = {}
    for e in _load_jsonl(_LOG_PATH):
        bid = e.get("behavior_id")
        if bid:
            counts[bid] = counts.get(bid, 0) + 1
    return counts


_STALE_ASSESS_DAYS = 30


def _queue_depths() -> list[dict]:
    """Depth at each funnel stage boundary (§5). A boundary that grows for weeks
    flags its consuming behavior — the analytics view reads these over time.

    Only rows with ``backlog: True`` are work *waiting* on a consumer, and only those
    are flag-eligible. Cumulative totals (notes written, laws held) are reported
    alongside for context but never flagged: 1,100 shallow notes on file is throughput,
    not a queue, and flagging it would train the supervisor to ignore the flags.
    """
    inbox_n = len(list(_INBOX_DIR.glob("*.md"))) if _INBOX_DIR.exists() else 0
    seeds_n = len(list(_SEEDS_DIR.glob("seed-*.yaml"))) if _SEEDS_DIR.exists() else 0
    shallow_n = len(list(_SHALLOW_DIR.glob("[!_]*.md"))) if _SHALLOW_DIR.exists() else 0
    try:
        all_laws = laws_mod.load_all()
    except Exception:
        all_laws = []

    # Laws whose last assessment is older than the staleness window (or never
    # assessed) — this is the real assess backlog, as opposed to the law inventory.
    cutoff = (datetime.now(timezone.utc).date()
              - timedelta(days=_STALE_ASSESS_DAYS)).isoformat()
    stale = 0
    for law in all_laws:
        if law.get("status") != "active":
            continue
        assessed = [str(h.get("date", "")) for h in (law.get("history") or [])
                    if "assessment" in str(h.get("detail", "")).lower()]
        if not assessed or max(assessed) < cutoff:
            stale += 1

    return [
        {"boundary": "intake → triage", "consumer": "triage", "depth": inbox_n,
         "unit": "unprocessed inbox items", "backlog": True, "threshold": 500},
        {"boundary": "reads → induct", "consumer": "induct", "depth": seeds_n,
         "unit": "seeds in pool", "backlog": True, "threshold": 60},
        {"boundary": "induct → assess", "consumer": "assess", "depth": stale,
         "unit": f"active laws unassessed in {_STALE_ASSESS_DAYS}d",
         "backlog": True, "threshold": 10},
        {"boundary": "— total output —", "consumer": "shallow-read", "depth": shallow_n,
         "unit": "shallow notes written (cumulative)", "backlog": False},
        {"boundary": "— inventory —", "consumer": "assess",
         "depth": sum(1 for l in all_laws if l.get("status") == "active"),
         "unit": "active laws", "backlog": False},
    ]


def _daemon_status() -> dict:
    out = {"pid": None, "running": False, "paused": None, "reads": None}
    try:
        from daemon import pause as pause_mod
        out["paused"] = pause_mod.paused_until()
    except Exception:
        pass
    try:
        from agent import read_budget
        out["reads"] = read_budget.paused_until()
    except Exception:
        pass
    pid_file = _ROOT / "daemon" / "daemon.pid"   # written by daemon/discord_client.py
    if pid_file.exists():
        try:
            pid = int(pid_file.read_text().strip())
            out["pid"] = pid
            proc = subprocess.run(["ps", "-p", str(pid)], capture_output=True)
            out["running"] = proc.returncode == 0
        except (ValueError, OSError):
            pass
    try:
        from daemon import costs
        out["cost_today"] = round(costs.today_usd(), 4)
        out["cost_limit"] = costs.configured_limit()
    except Exception:
        pass
    return out


# ── API payloads ─────────────────────────────────────────────────────────────

def _api_state() -> dict:
    events = _load_jsonl(_EVENTS_PATH)
    cutoff = (datetime.now(timezone.utc) - timedelta(days=7)).isoformat()
    recent = [e for e in events if e.get("timestamp", "") >= cutoff]
    try:
        all_laws = laws_mod.load_all()
    except Exception:
        all_laws = []
    by_stage: dict[str, int] = {}
    for law in all_laws:
        by_stage[law.get("stage", "?")] = by_stage.get(law.get("stage", "?"), 0) + 1

    q = queue_mod.load().get("queue", [])
    return {
        "daemon": _daemon_status(),
        "laws_total": len(all_laws),
        "laws_by_stage": by_stage,
        "queue_pending": sum(1 for e in q if e.get("status") == "pending"),
        "queue_depths": _queue_depths(),
        "events_7d": len(recent),
        "activity": sorted(recent, key=lambda e: e.get("timestamp", ""),
                           reverse=True)[:25],
        "branch": _git("rev-parse", "--abbrev-ref", "HEAD")[1],
    }


def _api_events() -> list[dict]:
    """Law events over time — the KPI chart's series (law accumulation rate)."""
    return _load_jsonl(_EVENTS_PATH)


def _api_laws() -> list[dict]:
    try:
        all_laws = laws_mod.load_all()
    except Exception:
        return []
    out = []
    for law in all_laws:
        history = law.get("history") or []
        last = history[-1] if history else {}
        out.append({
            "id": law.get("id"),
            "title": law.get("title"),
            "stage": law.get("stage"),
            "status": law.get("status"),
            "confidence": law.get("confidence"),
            "origin": law.get("origin"),
            "last_event": last.get("event"),
            "last_date": str(last.get("date", "")),
            "counterexamples": len(law.get("counterexamples") or []),
            "examples": len(law.get("examples") or []),
        })
    return out


def _api_law(law_id: str) -> dict | None:
    path = laws_mod.path_for(law_id)
    if path is None:
        return None
    return {"id": law_id, "path": str(path.relative_to(_ROOT)),
            "yaml": path.read_text()}


def _save_law(law_id: str, text: str, note: str) -> dict:
    """Save a law record from the editor. Validates before writing — the console is
    a supervisor's instrument, but it should still refuse to write a record the
    stage machine would reject."""
    path = laws_mod.path_for(law_id)
    if path is None:
        return {"error": f"no law {law_id}"}
    try:
        parsed = _rt_yaml().load(text)
    except Exception as exc:
        return {"error": f"YAML parse failed: {exc}"}

    problems = laws_mod.validate(parsed)
    if problems:
        return {"error": "validation failed", "problems": problems}

    if note:
        laws_mod.add_history(parsed, "edited", f"console: {note}")

    buf = io.StringIO()
    _rt_yaml().dump(parsed, buf)
    path.write_text(buf.getvalue())
    status = _commit([path], f"edit {law_id}" + (f" — {note}" if note else ""))
    return {"ok": True, "git": status}


def _api_behaviors() -> dict:
    registry = _load_registry()
    util = _utilization()
    for b in registry:
        b["visits"] = util.get(b.get("id"), 0)
    return {"behaviors": registry, "mdp": _load_mdp()}


def _save_behavior(bid: str, patch: dict) -> dict:
    """Patch one registry entry — trigger, model, prompt, status are the fields the
    console is meant to tune (§7 view 3)."""
    y = _rt_yaml()
    data = y.load(_REGISTRY_PATH.read_text())
    for b in data.get("behaviors", []):
        if b.get("id") == bid:
            for key in ("trigger", "status", "phase", "name", "defined_by", "notes"):
                if key in patch:
                    b[key] = patch[key]
            if "action" in patch and isinstance(patch["action"], dict):
                b.setdefault("action", {})
                for key in ("entrypoint", "model", "prompt"):
                    if key in patch["action"]:
                        b["action"][key] = patch["action"][key]
            buf = io.StringIO()
            y.dump(data, buf)
            _REGISTRY_PATH.write_text(buf.getvalue())
            return {"ok": True, "git": _commit([_REGISTRY_PATH], f"edit behavior {bid}")}
    return {"error": f"no behavior {bid}"}


def _save_mdp(payload: dict) -> dict:
    """Save edge weights and triggers. Refuses an edge with no trigger — §6.2 makes
    the trigger mandatory, and a weight with no stated reason is what made the v1
    graph unfalsifiable."""
    y = _rt_yaml()
    data = y.load(_MDP_PATH.read_text())
    incoming = {(t["from"], t["to"]): t for t in payload.get("transitions", [])}

    missing = [f"{k[0]} → {k[1]}" for k, t in incoming.items() if not t.get("trigger")]
    if missing:
        return {"error": "every edge needs a trigger (§6.2)", "problems": missing}

    for t in data.get("transitions", []):
        key = (t["from"], t["to"])
        if key in incoming:
            if "weight" in incoming[key]:
                t["weight"] = incoming[key]["weight"]
            if "trigger" in incoming[key]:
                t["trigger"] = incoming[key]["trigger"]

    buf = io.StringIO()
    y.dump(data, buf)
    _MDP_PATH.write_text(buf.getvalue())
    return {"ok": True, "git": _commit([_MDP_PATH], "tune transition weights/triggers")}


def _api_analytics() -> dict:
    registry = _load_registry()
    util = _utilization()
    log = _load_jsonl(_LOG_PATH)

    rows = []
    for b in registry:
        bid = b.get("id")
        rows.append({
            "id": bid,
            "name": b.get("name"),
            "phase": b.get("phase"),
            "status": b.get("status"),
            "visits": util.get(bid, 0),
        })
    rows.sort(key=lambda r: -r["visits"])

    # Flags: the cheap heuristics available before Phase 4 builds the real ones.
    flags = []
    unlogged = [r["id"] for r in rows if r["status"] == "active" and r["visits"] == 0]
    if unlogged:
        # One flag, not one per behavior: the shared cause is that only induct and
        # assess call funnel_log.behavior_visit today, so utilization is blind for
        # everything else. Per-behavior flags would read as seven separate faults.
        flags.append({
            "level": "warn", "behavior": ", ".join(unlogged),
            "message": f"{len(unlogged)} active behaviors have never logged a visit — "
                       "they do not call funnel_log.behavior_visit, so utilization "
                       "cannot see them. Instrument them in Phase 4."})
    for d in _queue_depths():
        if d.get("backlog") and d["depth"] > d.get("threshold", 500):
            flags.append({"level": "warn", "behavior": d["consumer"],
                          "message": f"{d['boundary']}: {d['depth']} {d['unit']} "
                                     f"(threshold {d['threshold']}) — consumer is "
                                     "not keeping up"})

    return {
        "behaviors": rows,
        "queue_depths": _queue_depths(),
        "flags": flags,
        "log_entries": len(log),
        "note": "Phase 4 replaces these heuristics with the §8 analytics overlay "
                "(utilization trends, prune/split thresholds, weekly report).",
    }


def _api_people() -> list[dict]:
    if not _PEOPLE_PATH.exists():
        return []
    try:
        data = json.loads(_PEOPLE_PATH.read_text())
    except json.JSONDecodeError:
        return []
    people = data.values() if isinstance(data, dict) else data
    out = []
    for p in people:
        if not isinstance(p, dict):
            continue
        out.append({
            "handle": p.get("handle") or p.get("name") or "?",
            "interactions": p.get("interactions") or p.get("message_count") or 0,
            "trust": p.get("trust"),
            "model": (p.get("model") or p.get("notes") or "")[:400],
            "last_seen": p.get("last_seen") or p.get("last_interaction"),
        })
    out.sort(key=lambda p: -(p["interactions"] or 0))
    return out


# ── HTTP ─────────────────────────────────────────────────────────────────────

class _ConsoleHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        path = urlparse(self.path).path
        if path in ("/", "/console"):
            return self._file(_CONSOLE_HTML, "text/html; charset=utf-8")
        if path == "/api/state":
            return self._json(_api_state())
        if path == "/api/events":
            return self._json(_api_events())
        if path == "/api/laws":
            return self._json(_api_laws())
        if path.startswith("/api/laws/"):
            law = _api_law(path.rsplit("/", 1)[-1])
            return self._json(law) if law else self.send_error(404)
        if path == "/api/behaviors":
            return self._json(_api_behaviors())
        if path == "/api/queue":
            return self._json(queue_mod.load())
        if path == "/api/analytics":
            return self._json(_api_analytics())
        if path == "/api/people":
            return self._json(_api_people())
        self.send_error(404, "Not found")

    def do_POST(self):
        path = urlparse(self.path).path
        body = self._body()

        if path.startswith("/api/laws/"):
            law_id = path.rsplit("/", 1)[-1]
            return self._json(_save_law(law_id, body.get("yaml", ""),
                                        body.get("note", "")))
        if path.startswith("/api/behaviors/"):
            return self._json(_save_behavior(path.rsplit("/", 1)[-1], body))
        if path == "/api/mdp":
            return self._json(_save_mdp(body))
        if path.startswith("/api/queue/"):
            parts = path.strip("/").split("/")      # api queue <id> <action>
            if len(parts) == 4:
                return self._json(self._queue_action(parts[2], parts[3], body))
        self.send_error(404, "Not found")

    def _queue_action(self, qid: str, action: str, body: dict) -> dict:
        try:
            if action == "approve":
                queue_mod.approve(qid, rationale=body.get("rationale", ""),
                                  edits=body.get("edits"))
                git = _commit([_BEHAVIORS_DIR / "queue.yaml"], f"approve {qid}")
                return {"ok": True, "git": git}
            if action == "reject":
                queue_mod.reject(qid, rationale=body.get("rationale", ""))
                git = _commit([_BEHAVIORS_DIR / "queue.yaml"], f"reject {qid}")
                return {"ok": True, "git": git}
            if action == "apply":
                bid = queue_mod.apply_approved(qid)
                git = _commit([_REGISTRY_PATH, _BEHAVIORS_DIR / "queue.yaml"],
                              f"apply {qid} → behavior {bid}")
                return {"ok": True, "applied": bid, "git": git}
        except (KeyError, ValueError) as exc:
            return {"error": str(exc)}
        return {"error": f"unknown queue action {action!r}"}

    def _body(self) -> dict:
        length = int(self.headers.get("Content-Length", 0) or 0)
        if not length:
            return {}
        try:
            return json.loads(self.rfile.read(length))
        except json.JSONDecodeError:
            return {}

    def _file(self, path: Path, ctype: str):
        if not path.exists():
            return self.send_error(404, f"{path.name} not found")
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _json(self, data):
        payload = json.dumps(data, default=str).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, fmt, *args):
        pass


def run_console(port: int = _PORT, push: bool = False, open_browser: bool = True):
    global _PUSH
    _PUSH = push
    url = f"http://127.0.0.1:{port}/"
    server = http.server.HTTPServer(("127.0.0.1", port), _ConsoleHandler)
    print(f"Humboldt console: {url}")
    print(f"  branch: {_git('rev-parse', '--abbrev-ref', 'HEAD')[1]}")
    print(f"  git:    commit on save" + (" + push" if push else " (no push; --push to enable)"))
    print("  Ctrl-C to stop.")
    if open_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nConsole stopped.")
