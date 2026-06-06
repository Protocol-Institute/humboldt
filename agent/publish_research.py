"""
publish_research.py — generate the research status page for the PI website.

Reads all typed research artifacts (C, H, CL, T, F) from research/,
generates humboldt-research/index.html in the PI website repo, and
optionally commits + pushes.

Usage:
    python3 -m agent.humboldt publish-research
    python3 -m agent.humboldt publish-research --dry-run
"""

import hashlib
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

_ROOT = Path(__file__).parent.parent
_RESEARCH = _ROOT / "research"
_WEBSITE_REPO = _ROOT.parent / "website"
_OUTPUT_DIR = _WEBSITE_REPO / "humboldt-research"
_OUTPUT_HTML = _OUTPUT_DIR / "index.html"


# ── Status ────────────────────────────────────────────────────────────────────

_STATUS = {
    "active":     ("dot-green",  "Active / ongoing"),
    "open":       ("dot-green",  "Open / collecting"),
    "stagnant":   ("dot-yellow", "Stagnant — needs attention"),
    "blocked":    ("dot-red",    "Blocked by unbuilt behavior"),
    "superseded": ("dot-yellow", "Superseded"),
    "refuted":    ("dot-red",    "Refuted by counterexample"),
}
_DEFAULT_STATUS = ("dot-green", "Active")


def _dot_cls(status: str) -> tuple[str, str]:
    return _STATUS.get(status, _DEFAULT_STATUS)


# ── Curve geometry (SVG coordinates) ─────────────────────────────────────────
#
# The Double Freytag triangle (Rao, Tempo 2011) plotted as entropy vs. time.
# Y increases downward in SVG, so high entropy = small y (near top of canvas).
#
# Phases and their curve segments:
#   Exploration : rising   (start-liminal → cheap-trick peak)
#   Sensemaking : falling  (peak → valley floor)
#   Valley      : flat     (valley floor, at baseline)
#   Heavy Lift  : rising   (valley → separation-event peak, higher than CT)
#   Retrospective: falling (separation event → new liminal, slightly above baseline)

SVG_W = 900
SVG_H = 272

_Y_BASE = 228      # entropy floor: liminal passages, valley
_Y_CT   = 110      # Cheap Trick peak — smaller than Separation Event
_Y_SE   = 26       # Separation Event peak — dominant peak, visibly taller
_Y_LEND = 198      # end Liminal Passage (staircase: above baseline)

_X0     = 58       # start of diagram
_X_EXP  = 82       # exploration begins (end of start-liminal flat)
_X_CT   = 188      # Cheap Trick — narrower exploration phase
_X_VS   = 392      # Valley start / Sensemaking end
_X_VE   = 548      # Valley end / Heavy Lift start
_X_SE   = 700      # Separation Event
_X_RE   = 842      # Retrospective end / Liminal end start
_X1     = 860      # end of diagram

# Phase segments (x1, y1, x2, y2) — linear interpolation within each
_SEG = {
    "exploration":   (_X_EXP, _Y_BASE, _X_CT,  _Y_CT),
    "sensemaking":   (_X_CT,  _Y_CT,   _X_VS,  _Y_BASE),
    "valley":        (_X_VS,  _Y_BASE, _X_VE,  _Y_BASE),
    "heavy_lift":    (_X_VE,  _Y_BASE, _X_SE,  _Y_SE),
    "retrospective": (_X_SE,  _Y_SE,   _X_RE,  _Y_LEND),
}

_DEFAULT_PCT = {"active": 0.40, "open": 0.50, "stagnant": 0.14, "blocked": 0.08}


def _curve_pos(phase: str, pct: float) -> tuple[float, float]:
    """Return (x, y) in SVG space for a phase + fraction-complete."""
    if phase not in _SEG:
        return (_X0, _Y_BASE)
    x1, y1, x2, y2 = _SEG[phase]
    return (x1 + pct * (x2 - x1), y1 + pct * (y2 - y1))


def _jitter(item_id: str) -> tuple[float, float]:
    """Deterministic jitter based on item ID hash — perpendicular to curve."""
    h = int(hashlib.md5(item_id.encode()).hexdigest(), 16)
    jx = ((h % 1000) / 1000 - 0.5) * 14   # ±7 px
    jy = ((h // 1000 % 1000) / 1000 - 0.5) * 14
    return jx, jy


# ── YAML helpers ──────────────────────────────────────────────────────────────

def _load_yamls(directory: Path) -> list[dict]:
    items = []
    for path in sorted(directory.glob("*.yaml")):
        if path.name.startswith("_"):
            continue
        with open(path) as f:
            data = yaml.safe_load(f)
        if data:
            items.append(data)
    return items


def _snippet(text: str | None, max_len: int = 200) -> str:
    if not text:
        return ""
    text = text.strip().replace("\n", " ")
    idx = text.find(". ")
    s = text[: idx + 1] if idx > 0 else text
    return (s[:max_len] + "…") if len(s) > max_len else s


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")


# ── Collect items for diagram ─────────────────────────────────────────────────

_PHASE_MAP = {
    "c":        ("exploration",   "status",          "open"),
    "h":        ("sensemaking",   "status",          "active"),
    "cl":       ("valley",        "research_status", "active"),
    "theories": ("heavy_lift",    "research_status", "active"),
    "f":        ("retrospective", "status",          "active"),
}
_SKIP_STATUSES = {"consumed", "promoted", "abandoned"}


def _all_items() -> list[dict]:
    items = []
    for subdir, (phase, status_key, default_status) in _PHASE_MAP.items():
        d = _RESEARCH / subdir
        if not d.exists():
            continue
        for raw in _load_yamls(d):
            status = raw.get(status_key, default_status)
            if status in _SKIP_STATUSES:
                continue
            pct = raw.get("phase_pct", _DEFAULT_PCT.get(status, 0.35))
            item_id = raw.get("id", "?")
            cx, cy = _curve_pos(phase, pct)
            jx, jy = _jitter(item_id)
            items.append({
                "id":       item_id,
                "name":     raw.get("name", raw.get("id", "?")),
                "phase":    phase,
                "status":   status,
                "blurb":    _snippet(raw.get("statement") or raw.get("content") or raw.get("question", "")),
                "cx":       max(12, min(SVG_W - 12, cx + jx)),
                "cy":       max(12, min(SVG_H - 12, cy + jy)),
                "cls":      _dot_cls(status)[0],
                "label":    _dot_cls(status)[1],
            })
    return items


# ── SVG diagram ───────────────────────────────────────────────────────────────

def _build_svg(items: list[dict]) -> str:
    # Main curve polyline points
    pts = " ".join(f"{x},{y}" for x, y in [
        (_X0,  _Y_BASE),
        (_X_EXP, _Y_BASE),
        (_X_CT,  _Y_CT),
        (_X_VS,  _Y_BASE),
        (_X_VE,  _Y_BASE),
        (_X_SE,  _Y_SE),
        (_X_RE,  _Y_LEND),
        (_X1,    _Y_LEND),
    ])

    # Phase mid-x for labels
    lbl_y = _Y_BASE + 18
    lbl = [
        ((_X0 + _X_EXP) // 2,     lbl_y, "Liminal"),
        ((_X_EXP + _X_CT) // 2,   lbl_y, "Exploration"),
        ((_X_CT + _X_VS) // 2,    lbl_y, "Sensemaking"),
        ((_X_VS + _X_VE) // 2,    lbl_y, "Valley"),
        ((_X_VE + _X_SE) // 2,    lbl_y, "Heavy Lift"),
        ((_X_SE + _X_RE) // 2,    lbl_y, "Retrospective"),
        ((_X_RE + _X1) // 2,      lbl_y, "Liminal"),
    ]

    labels_html = "\n      ".join(
        f'<text class="ft-lbl" x="{x}" y="{y}" text-anchor="middle">{t}</text>'
        for x, y, t in lbl
    )

    # Phase divider tick marks at transition x-positions
    ticks_x = [_X_EXP, _X_CT, _X_VS, _X_VE, _X_SE, _X_RE]
    ticks_html = "\n      ".join(
        f'<line x1="{x}" y1="{_Y_BASE}" x2="{x}" y2="{_Y_BASE + 6}" '
        f'stroke="#bbb" stroke-width="1"/>'
        for x in ticks_x
    )

    # Item dots
    dots_html = "\n      ".join(
        f'<circle class="idot {item["cls"]}" '
        f'cx="{item["cx"]:.1f}" cy="{item["cy"]:.1f}" r="8" '
        f'data-id="{_esc(item["id"])}" '
        f'data-name="{_esc(item["name"])}" '
        f'data-phase="{item["phase"].replace("_", " ").title()}" '
        f'data-status="{_esc(item["label"])}" '
        f'data-blurb="{_esc(item["blurb"][:160])}"/>'
        for item in items
    )

    return f"""\
  <div class="ft-wrap">
    <svg viewBox="0 0 {SVG_W} {SVG_H}" class="ft-svg"
         xmlns="http://www.w3.org/2000/svg"
         aria-label="Double Freytag arc — research items by phase and entropy">

      <!-- entropy axis hint -->
      <text class="ft-axis" x="10" y="{(_Y_BASE + _Y_SE) // 2}"
            transform="rotate(-90,10,{(_Y_BASE + _Y_SE) // 2})">entropy ↑</text>

      <!-- baseline dashed line -->
      <line x1="{_X0}" y1="{_Y_BASE}" x2="{_X1}" y2="{_Y_BASE}"
            stroke="#ccc" stroke-width="1.2" stroke-dasharray="5,5"/>

      <!-- main curve -->
      <polyline points="{pts}" fill="none" stroke="#2C2C2C"
                stroke-width="2" stroke-linejoin="round"/>

      <!-- named transition markers -->
      <circle cx="{_X_CT}" cy="{_Y_CT}" r="3" fill="#2C2C2C"/>
      <text class="ft-event" x="{_X_CT}" y="{_Y_CT - 9}" text-anchor="middle">Cheap Trick</text>
      <circle cx="{_X_SE}" cy="{_Y_SE}" r="3" fill="#2C2C2C"/>
      <text class="ft-event" x="{_X_SE}" y="{_Y_SE - 9}" text-anchor="middle">Separation Event</text>

      <!-- phase tick marks and labels -->
      {ticks_html}
      {labels_html}

      <!-- research items -->
      {dots_html}

    </svg>
    <div id="ft-tip" class="ft-tip" style="display:none"></div>
  </div>"""


# ── Table rows ────────────────────────────────────────────────────────────────

def _phase_header(name: str, desc: str, count: int) -> str:
    n = f"{count} item{'s' if count != 1 else ''}" if count else "none currently"
    return (f'<tr class="ph"><td colspan="4">'
            f'<span class="pn">{name}</span>'
            f'<span class="pd">{desc}</span>'
            f'<span class="pc">{n}</span></td></tr>')


def _item_row(iid: str, name: str, blurb: str, status: str, typ: str = "") -> str:
    cls, lbl = _dot_cls(status)
    badge = (f'<span class="tb tb-{typ.lower()}">{typ}</span> ') if typ else ""
    return (f'<tr>'
            f'<td class="sc"><span class="dot {cls}" title="{lbl}"></span></td>'
            f'<td class="aid">{iid}</td>'
            f'<td class="an">{badge}{name}</td>'
            f'<td class="ab">{blurb}</td></tr>')


def _empty() -> str:
    return '<tr class="er"><td colspan="4"><em>None currently.</em></td></tr>'


def _phase_rows(subdir: str, status_key: str, default_status: str,
                iid_key: str = "id", name_key: str = "name",
                type_key: str = "type", skip: set | None = None) -> tuple[int, str]:
    skip = skip or _SKIP_STATUSES
    items = [i for i in _load_yamls(_RESEARCH / subdir)
             if i.get(status_key, default_status) not in skip]
    rows = []
    for item in items:
        blurb = _snippet(item.get("statement") or item.get("content") or item.get("question", ""))
        typ = (item.get(type_key, "") or "").capitalize()
        rows.append(_item_row(
            item.get(iid_key, "?"),
            item.get(name_key, item.get("id", "?")),
            blurb,
            item.get(status_key, default_status),
            typ,
        ))
    return len(items), "\n".join(rows) if rows else _empty()


# ── HTML assembly ─────────────────────────────────────────────────────────────

_CSS = """\
    .ft-wrap { position: relative; margin: 0 0 1.8rem; }
    .ft-svg  { width: 100%; max-width: 900px; height: auto; display: block;
               overflow: visible; }
    .ft-lbl  { font-family: inherit; font-size: 13.5px; fill: #777; font-weight: 500; }
    .ft-event{ font-family: inherit; font-size: 12px; fill: #444;
               font-style: italic; }
    .ft-axis { font-family: inherit; font-size: 9px; fill: #ccc;
               text-transform: uppercase; letter-spacing: .06em; }
    .idot    { cursor: pointer; stroke: #fff; stroke-width: 2;
               transition: transform .12s ease;
               transform-box: fill-box; transform-origin: center; }
    .idot:hover { transform: scale(1.45); }
    .dot-green  { fill: #2a7a2a; }
    .dot-yellow { fill: #c8a000; }
    .dot-red    { fill: #b82222; }
    .ft-tip {
      position: fixed; background: #fff; border: 1px solid #ddd;
      border-radius: 4px; padding: .45rem .7rem; font-size: .82rem;
      color: #2C2C2C; box-shadow: 0 2px 8px rgba(0,0,0,.12);
      pointer-events: none; max-width: 260px; z-index: 100;
      line-height: 1.5;
    }
    .ft-tip strong { display: block; }
    .ft-tip .tm { color: #888; font-size: .77rem; margin-bottom: .2rem; }
    .ft-tip .tb2 { color: #444; }
    .legend { display: flex; gap: 1.5rem; font-size: .85rem; color: #555;
              margin-bottom: 1.6rem; flex-wrap: wrap; }
    .legend-item { display: flex; align-items: center; gap: .4rem; }
    .research-table { width: 100%; border-collapse: collapse;
                      margin-bottom: 2.5rem; font-size: .92rem; }
    .research-table th { text-align: left; padding: .5rem .75rem;
                         border-bottom: 2px solid #2C2C2C; font-weight: 600;
                         color: #2C2C2C; }
    .research-table td { padding: .5rem .75rem; border-bottom: 1px solid #E0E0E0;
                         color: #2C2C2C; vertical-align: top; }
    .research-table tr:last-child td { border-bottom: none; }
    .ph td { background: #f5f5f5; padding: .65rem .75rem .45rem;
             border-bottom: 1px solid #ccc; }
    .pn { font-size: .78rem; font-weight: 700; letter-spacing: .07em;
          text-transform: uppercase; color: #555; margin-right: .65rem; }
    .pd { font-size: .88rem; color: #666; margin-right: .65rem; }
    .pc { font-size: .8rem; color: #999; float: right; }
    .er td { color: #aaa; font-style: italic; padding: .35rem .75rem; }
    .sc  { width: 24px; text-align: center; }
    .aid { font-family: monospace; font-size: .82rem; white-space: nowrap;
           color: #555; width: 70px; }
    .an  { font-weight: 600; width: 220px; }
    .ab  { color: #444; font-size: .88rem; }
    .dot { display: inline-block; width: 10px; height: 10px;
           border-radius: 50%; vertical-align: middle; }
    .tb  { display: inline-block; padding: .07rem .38rem; border-radius: 3px;
           font-size: .74rem; font-weight: 600; white-space: nowrap;
           margin-right: .2rem; }
    .tb-lifecycle    { background: #e8eef8; color: #2a3a6a; }
    .tb-hardness     { background: #f0e8f8; color: #4a1a6a; }
    .tb-coordination { background: #e8f4e8; color: #1a5a2a; }
    .tb-failure      { background: #fdf0e0; color: #6a3a00; }
    .tb-evolution    { background: #f8f0e8; color: #5a3a1a; }
    .updated-note { font-size: .82rem; color: #999; margin-top: 2rem; }"""

_JS = """\
(function(){
  var tip = document.getElementById('ft-tip');
  document.querySelectorAll('.idot').forEach(function(d){
    d.addEventListener('mouseenter', function(e){
      tip.innerHTML =
        '<strong>' + d.dataset.id + ' — ' + (d.dataset.name||'') + '</strong>' +
        '<div class="tm">' + (d.dataset.phase||'') + ' · ' + (d.dataset.status||'') + '</div>' +
        '<div class="tb2">' + (d.dataset.blurb||'') + '</div>';
      tip.style.display = 'block';
      move(e);
    });
    d.addEventListener('mousemove', move);
    d.addEventListener('mouseleave', function(){ tip.style.display='none'; });
  });
  function move(e){
    var x = e.clientX + 14, y = e.clientY - 10;
    var w = tip.offsetWidth || 240;
    if(x + w > window.innerWidth - 8) x = e.clientX - w - 14;
    tip.style.left = x + 'px';
    tip.style.top  = y + 'px';
  }
})();"""


def _build_html() -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    all_items = _all_items()
    svg_html  = _build_svg(all_items)
    total     = len(all_items)

    exp_n, exp_r = _phase_rows("c",  "status",          "open",   name_key="title", type_key="type")
    sns_n, sns_r = _phase_rows("h",  "status",          "active", name_key="id")
    val_n, val_r = _phase_rows("cl", "research_status", "active")
    hlt_n, hlt_r = _phase_rows("theories", "research_status", "active")
    ret_n, ret_r = _phase_rows("f",  "status",          "active")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Humboldt — Research Status — The Protocol Institute</title>
  <meta name="description" content="Live status of Humboldt’s research inventory by arc phase.">
  <link rel="icon" href="/assets/logo-static.png" type="image/png">
  <link rel="stylesheet" href="/css/style.css">
  <style>
{_CSS}
  </style>
</head>
<body>
<div class="interior-wrapper">
  <header id="site-header"></header>
  <main class="interior-main">
    <div class="container">
      <div class="page-header">
        <h1>Humboldt — Research Status</h1>
      </div>
      <div class="about-body">

        <p>Research inventory by arc phase, following the Double Freytag model of inquiry
        (<em>Tempo</em>, Rao 2011). Each item moves through exploration, sensemaking, valley,
        heavy lift, and retrospective, producing a typed artifact at each stage. Position on
        the diagram reflects estimated progress within the current phase; vertical axis
        represents entropy in the developing mental model. Hover a dot for details.</p>

        <p><a href="/humboldt-notebook">Lab notebook →</a> &nbsp;·&nbsp;
        <a href="/humboldt-behaviors">Behavior inventory →</a> &nbsp;·&nbsp;
        <a href="/humboldt">About Humboldt →</a></p>

{svg_html}

        <div class="legend">
          <div class="legend-item"><span class="dot dot-green"></span> Active / ongoing</div>
          <div class="legend-item"><span class="dot dot-yellow"></span> Stagnant or superseded</div>
          <div class="legend-item"><span class="dot dot-red"></span> Blocked or refuted</div>
        </div>

        <table class="research-table">
          <thead>
            <tr><th style="width:24px"></th><th style="width:70px">ID</th>
            <th style="width:220px">Name / Type</th><th>Description</th></tr>
          </thead>
          <tbody>
            {_phase_header("Exploration",   "Curiosities — open provocations, awaiting cheap trick", exp_n)}
            {exp_r}
            {_phase_header("Sensemaking",   "Hypotheses — post-cheap-trick; building toward a falsifiable claim", sns_n)}
            {sns_r}
            {_phase_header("Valley",        "Candidate Laws — evidence accumulation; no external validation yet", val_n)}
            {val_r}
            {_phase_header("Heavy Lift",    "Theories — synthesis committed; approaching separation event", hlt_n)}
            {hlt_r}
            {_phase_header("Retrospective", "Falsification Monitors — registered; monitored for counterexamples", ret_n)}
            {ret_r}
          </tbody>
        </table>

        <p class="updated-note">{total} items across all phases. Generated {now}.
        Source: <a href="https://github.com/Protocol-Institute/humboldt/tree/main/research"
        target="_blank" rel="noopener noreferrer">research/ on GitHub</a>.</p>

      </div>
    </div>
  </main>
  <footer id="site-footer"></footer>
</div>
<script src="/js/components.js"></script>
<script>{_JS}</script>
</body>
</html>"""


# ── Git operations ────────────────────────────────────────────────────────────

def _git(args: list[str], cwd: Path) -> str:
    r = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed:\n{r.stderr}")
    return r.stdout.strip()


def publish_research(dry_run: bool = False) -> None:
    html = _build_html()
    _OUTPUT_DIR.mkdir(exist_ok=True)
    _OUTPUT_HTML.write_text(html)
    print(f"{'[dry-run] ' if dry_run else ''}Wrote {_OUTPUT_HTML}")

    if dry_run:
        print("[dry-run] Skipping git operations.")
        return

    _git(["add", str(_OUTPUT_HTML)], cwd=_WEBSITE_REPO)
    status = _git(["status", "--porcelain"], cwd=_WEBSITE_REPO)
    if not status:
        print("No changes to commit.")
        return

    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    _git(["commit", "-m", f"Humboldt research status update {date_str}"], cwd=_WEBSITE_REPO)
    _git(["push"], cwd=_WEBSITE_REPO)
    print("Published and pushed.")
