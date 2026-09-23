"""Behavior-graph diagram for the conference talk — a projected-slide rendering.

WHY THIS EXISTS, and why it is not the /brain/ page. `/brain/` draws the same data
with D3, client-side, in a force-ish layout tuned for *inspection*: you hover a node,
you read a tooltip, you pan around. Session 36 put a browser capture of that page on
a slide (images/behavior-graph.png, 1400x712). On a projector it is unreadable —
the nodes occupy a narrow central ribbon, roughly half the frame is empty margin, the
HTML legend eats a fifth of the width, and the node labels land at about 4px of
projected type. Operator called it: "unreadable graphic."

So this is a SECOND, DELIBERATELY DIFFERENT drawing of the same records, built for a
different job: seen once, from twenty feet, for about forty seconds. It reads the same
`behaviors/registry.yaml` + `behaviors/mdp.yaml` the /brain/ page does, so it cannot
drift from them the way a checked-in screenshot did — the s36 note "regenerate it if
registry.yaml or mdp.yaml change" is now automatic.

Design consequences of "projected, once, from twenty feet":
  · Phase structure is the message. Columns in phase order, left to right, each headed
    by its phase name — the arc is legible before any single node is read.
  · Rectangles, not circles: a 13-character id like `shallow-read` fits a rect at
    readable type and does not fit a circle.
  · Edge WEIGHT is not drawn as a number. 23 numeric labels is what made the capture
    illegible; weight maps to stroke opacity instead, which survives projection.
  · Cycle-back edges (to an earlier phase) are dashed and routed below the columns, so
    they read as "returns" without crossing the forward flow.

Dark-first palette: this diagram is only ever embedded by the talk page, on the #23262b
stage and in its transcript, both of which already dark-skin the law_arc diagram. Unlike
law_arc — which is shared with the light /laws/ page and therefore needs a scoped
re-skin — this one has no light-background consumer, so it is coloured for the stage
directly. If it ever lands on a light page, add a scoped override rather than repainting
these values.
"""

from __future__ import annotations

import html
from pathlib import Path

import yaml

_ROOT = Path(__file__).parent.parent
_REGISTRY = _ROOT / "behaviors" / "registry.yaml"
_MDP = _ROOT / "behaviors" / "mdp.yaml"

SVG_W = 1000
SVG_H = 470

_COL_Y = 214           # vertical centre of the column band
_ROW_GAP = 62
_NODE_W = 138
_NODE_H = 42
_FLOW_Y = 424          # the out-of-flow band


def _esc(s: str) -> str:
    return html.escape(str(s or ""), quote=True)


def _load() -> tuple[list[dict], dict]:
    reg = yaml.safe_load(_REGISTRY.read_text()) or {}
    mdp = yaml.safe_load(_MDP.read_text()) or {}
    return reg.get("behaviors", []), mdp


def _layout(behaviors: list[dict], mdp: dict) -> tuple[dict, list[dict]]:
    """Place every behavior. Returns {id: node} and the ordered phase columns."""
    phases = [p for p in (mdp.get("phases") or []) if p.get("id") != "any"]
    phases.sort(key=lambda p: p.get("order", 0))

    # Columns are evenly spread, but the first and last are inset so a 138-wide node
    # cannot overhang the viewBox.
    n = len(phases)
    left, right = 78, SVG_W - 78
    step = (right - left) / max(n - 1, 1)
    for i, p in enumerate(phases):
        p["cx"] = left + i * step

    by_phase: dict[str, list[dict]] = {}
    for b in behaviors:
        by_phase.setdefault(b.get("phase", "any"), []).append(b)

    nodes: dict[str, dict] = {}
    for p in phases:
        col = by_phase.get(p["id"], [])
        for i, b in enumerate(col):
            cy = _COL_Y + (i - (len(col) - 1) / 2) * _ROW_GAP
            nodes[b["id"]] = {
                "id": b["id"], "cx": p["cx"], "cy": cy,
                "phase": p["id"], "order": p.get("order", 0),
                "color": p.get("color", "#8b949e"),
                "proposed": b.get("status") != "active",
            }

    # Out-of-flow behaviors sit in their own band, centred under the middle columns.
    loose = by_phase.get("any", [])
    for i, b in enumerate(loose):
        cx = SVG_W / 2 + (i - (len(loose) - 1) / 2) * (_NODE_W + 34)
        nodes[b["id"]] = {
            "id": b["id"], "cx": cx, "cy": _FLOW_Y, "phase": "any", "order": -1,
            "color": "#6e7681", "proposed": b.get("status") != "active",
        }
    return nodes, phases


def _edge_path(a: dict, b: dict) -> tuple[str, bool]:
    """Path from node `a` to node `b`, plus whether it is a cycle-back.

    Forward edges leave the right face and enter the left face, bowed by the vertical
    gap so parallel runs separate. Cycle-backs are routed under the whole column band
    instead of retracing the forward corridor — with 23 edges over 13 nodes, sharing
    the corridor is what turns the picture into a thicket.
    """
    # Classified GEOMETRICALLY, not just by phase order. The out-of-flow behaviors
    # (`respond`, `review`) carry order -1, so by order alone every edge leaving them
    # counts as forward — including `review -> orient`, which then gets drawn as a
    # forward edge that has to loop rightward all the way around to reach a node on
    # the far left. It is a return; drawing it as one is both truer and legible.
    back = b["cx"] < a["cx"] - 1 or b["order"] < a["order"]
    if back:
        y = _FLOW_Y - 78
        return (f"M {a['cx']:.0f} {a['cy'] + _NODE_H/2:.0f} "
                f"C {a['cx']:.0f} {y:.0f}, {b['cx']:.0f} {y:.0f}, "
                f"{b['cx']:.0f} {b['cy'] + _NODE_H/2:.0f}"), True

    x1, x2 = a["cx"] + _NODE_W / 2, b["cx"] - _NODE_W / 2
    if x2 <= x1:                      # same column — bow out to the right
        x1, x2 = a["cx"] + _NODE_W / 2, b["cx"] + _NODE_W / 2
        bow = max(34.0, abs(b["cy"] - a["cy"]) * 0.5)
        return (f"M {x1:.0f} {a['cy']:.0f} "
                f"C {x1 + bow:.0f} {a['cy']:.0f}, {x2 + bow:.0f} {b['cy']:.0f}, "
                f"{x2:.0f} {b['cy']:.0f}"), False
    mid = (x1 + x2) / 2
    return (f"M {x1:.0f} {a['cy']:.0f} "
            f"C {mid:.0f} {a['cy']:.0f}, {mid:.0f} {b['cy']:.0f}, "
            f"{x2:.0f} {b['cy']:.0f}"), False


def graph_svg() -> str:
    behaviors, mdp = _load()
    nodes, phases = _layout(behaviors, mdp)
    transitions = mdp.get("transitions") or []

    parts: list[str] = []

    # ── phase columns: tint band + header ────────────────────────────────────
    for p in phases:
        x = p["cx"] - (SVG_W / len(phases)) / 2 + 4
        w = SVG_W / len(phases) - 8
        parts.append(
            f'<rect class="bg-band" x="{x:.0f}" y="46" width="{w:.0f}" height="330" '
            f'rx="6" fill="{p.get("color", "#8b949e")}" />')
        parts.append(
            f'<text class="bg-phase" x="{p["cx"]:.0f}" y="32" text-anchor="middle" '
            f'fill="{p.get("color", "#8b949e")}">{_esc(p.get("name", p["id"])).upper()}</text>')

    # ── edges under the nodes ───────────────────────────────────────────────
    weights = [float(t.get("weight", 0.3) or 0.3) for t in transitions] or [1.0]
    wmax = max(weights) or 1.0
    for t in transitions:
        a, b = nodes.get(t.get("from")), nodes.get(t.get("to"))
        if not a or not b:
            continue
        d, back = _edge_path(a, b)
        # Weight -> opacity: the one visual channel that still reads at projector size.
        op = 0.28 + 0.52 * (float(t.get("weight", 0.3) or 0.3) / wmax)
        cls = "bg-edge bg-edge-back" if back else "bg-edge"
        parts.append(f'<path class="{cls}" d="{d}" opacity="{op:.2f}" />')

    # ── nodes ───────────────────────────────────────────────────────────────
    for nd in nodes.values():
        x = nd["cx"] - _NODE_W / 2
        y = nd["cy"] - _NODE_H / 2
        cls = "bg-node bg-node-proposed" if nd["proposed"] else "bg-node"
        parts.append(
            f'<rect class="{cls}" x="{x:.0f}" y="{y:.0f}" width="{_NODE_W}" '
            f'height="{_NODE_H}" rx="7" stroke="{nd["color"]}" />')
        parts.append(
            f'<text class="bg-label" x="{nd["cx"]:.0f}" y="{nd["cy"] + 6:.0f}" '
            f'text-anchor="middle">{_esc(nd["id"])}</text>')

    # ── out-of-flow band label ──────────────────────────────────────────────
    loose = [n for n in nodes.values() if n["phase"] == "any"]
    if loose:
        lx = min(n["cx"] for n in loose) - _NODE_W / 2
        parts.append(
            f'<text class="bg-phase bg-phase-loose" x="{lx:.0f}" '
            f'y="{_FLOW_Y - _NODE_H/2 - 10:.0f}" fill="#6e7681">OUT OF FLOW</text>')

    # ── legend ──────────────────────────────────────────────────────────────
    # Below the out-of-flow nodes, not beside them: at _FLOW_Y - 34 the legend's last
    # key collided with the OUT OF FLOW label.
    ly = SVG_H - 8
    parts.append(
        f'<g class="bg-legend" transform="translate(28 {ly})">'
        f'<line class="bg-edge" x1="0" y1="0" x2="34" y2="0" opacity="0.8" />'
        f'<text class="bg-key" x="42" y="4">forward</text>'
        f'<line class="bg-edge bg-edge-back" x1="126" y1="0" x2="160" y2="0" opacity="0.8" />'
        f'<text class="bg-key" x="168" y="4">cycle-back</text>'
        f'<rect class="bg-node bg-node-proposed" x="264" y="-8" width="22" height="16" '
        f'rx="3" stroke="#8b949e" />'
        f'<text class="bg-key" x="294" y="4">proposed (not built)</text>'
        f'</g>')

    return (f'<svg viewBox="0 0 {SVG_W} {SVG_H}" class="bg-svg" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-label="Humboldt\'s behavior graph: {len(nodes)} behaviors placed in '
            f'the Double Freytag phase columns, connected by {len(transitions)} weighted '
            f'transitions, with dashed cycle-back edges returning to earlier phases.">'
            + "".join(parts) + "</svg>")


_CSS = """
    .bg-svg { width: 100%; max-width: 1000px; height: auto; display: block; margin: 0 auto; }
    .bg-band  { opacity: 0.055; }
    .bg-phase { font-family: inherit; font-size: 14px; font-weight: 600;
                letter-spacing: 0.1em; }
    .bg-node  { fill: #2b2f35; stroke-width: 1.6; }
    .bg-node-proposed { fill: #24272c; stroke-dasharray: 5 3; opacity: 0.72; }
    .bg-label { font-family: inherit; font-size: 15.5px; font-weight: 500; fill: #e9ecef; }
    .bg-node-proposed + .bg-label { fill: #9aa3ad; }
    .bg-edge  { fill: none; stroke: #c3cad2; stroke-width: 1.7; }
    .bg-edge-back { stroke-dasharray: 6 4; stroke: #b9ad7e; }
    .bg-key   { font-family: inherit; font-size: 12.5px; fill: #8d959e; }
    .bg-phase-loose { font-size: 12px; letter-spacing: 0.08em; }
"""
