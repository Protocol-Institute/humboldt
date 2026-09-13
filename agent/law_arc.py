"""
law_arc.py — the Double Freytag arc, plotted with one dot per law record.

Restores the diagram that ``agent/publish_research.py`` drew for the old research
status page (session 14). The *geometry* here is a faithful port of that module —
the arc is the Double Freytag triangle (Rao, *Tempo* 2011) as entropy vs. time,
and its proportions are load-bearing: the Separation Event peak is visibly taller
than the Cheap Trick peak, and the trailing Liminal Passage lands above the
baseline rather than on it (the staircase).

What changed is the *data*. The original read ``research/{c,h,cl,theories,f}/``,
all of which the 2026-08 redesign archived, so it would now plot an empty arc —
the same stale-path failure class session 35 found in ``ingest.py``. This module
reads ``laws/L-NNN-*.yaml`` instead, where one law record replaces the five typed
artifacts and the ``stage`` field replaces the per-directory phase mapping.

Two encoding notes:

* **Colour is confidence, not status.** Every law record is currently
  ``status: active``, so status has no variance to show. ``confidence``
  (speculative / provisional / supported / unfalsified) is what actually moves.
* **Position within a phase is rank, not an absolute coordinate.** Law records
  carry no ``phase_pct`` field (the old C/H/CL ones did), so laws are spread
  evenly across their stage's segment in confidence order, with an alternating
  perpendicular row offset once a stage holds five or more. Exploration currently
  holds 13 of the 20 laws on the shortest segment of the arc, so the spread has
  to use the whole segment — anchoring each confidence level to a fixed fraction
  smears them into one clump.

Consumed by ``agent.publish_laws.build_laws_body``. Takes an already-loaded law
list — never call ``laws.load_all()`` per item, it is a ruamel round-trip.
"""

from __future__ import annotations

import hashlib

# ── Curve geometry (SVG coordinates) ─────────────────────────────────────────
#
# Y increases downward in SVG, so high entropy = small y (near top of canvas).
#
#   Exploration  : rising   (start-liminal -> cheap-trick peak)
#   Sensemaking  : falling  (peak -> valley floor)
#   Valley       : flat     (valley floor, at baseline)
#   Heavy Lift   : rising   (valley -> separation-event peak, higher than CT)
#   Retrospective: falling  (separation event -> new liminal, above baseline)

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

# Phase segments (x1, y1, x2, y2) — linear interpolation within each.
# Keyed by the law record's `stage` value, so "heavy-lift" is hyphenated here
# where the old module used "heavy_lift".
_SEG = {
    "exploration":   (_X_EXP, _Y_BASE, _X_CT,  _Y_CT),
    "sensemaking":   (_X_CT,  _Y_CT,   _X_VS,  _Y_BASE),
    "valley":        (_X_VS,  _Y_BASE, _X_VE,  _Y_BASE),
    "heavy-lift":    (_X_VE,  _Y_BASE, _X_SE,  _Y_SE),
    "retrospective": (_X_SE,  _Y_SE,   _X_RE,  _Y_LEND),
}

# Confidence ordering. Within a stage, laws are laid out along the segment in this
# order — a `supported` exploration law sits nearer its Cheap Trick than a
# `speculative` one does.
#
# An earlier version pinned each confidence level to a fixed fraction of the segment
# and fanned ties around it. That misjudged the real distribution: 13 of 20 laws are
# `speculative`, so they all fanned around one point and smeared into an unreadable
# clump on the shortest segment on the arc. Spreading the whole stage across the whole
# segment is what actually fits the data — position now reads as rank within the stage
# rather than an absolute confidence coordinate, which the colour already carries.
_CONF_RANK = {
    "speculative": 0,
    "provisional": 1,
    "supported":   2,
    "unfalsified": 3,
}

_CONF_CLS = {
    "speculative": ("dot-speculative", "Speculative"),
    "provisional": ("dot-provisional", "Provisional"),
    "supported":   ("dot-supported",   "Supported"),
    "unfalsified": ("dot-unfalsified", "Unfalsified"),
}
_DEFAULT_CONF = ("dot-speculative", "Speculative")

# Laws in a stage spread across this fraction of its segment, inset from both ends
# so no dot sits exactly on a phase boundary or a named transition marker.
_SPREAD_LO, _SPREAD_HI = 0.09, 0.91
# Perpendicular offset (px), applied alternately once a stage holds enough laws that
# one row would collide. Two rows double the effective spacing.
_ROW_OFFSET = 9.0
# Above this count, a stage switches from one row to two.
_TWO_ROW_AT = 5
_DOT_R = 6


def _esc(s: str) -> str:
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def _snippet(text: str | None, max_len: int = 165) -> str:
    """First sentence of a statement, trimmed for a tooltip."""
    if not text:
        return ""
    text = " ".join(str(text).split())
    idx = text.find(". ")
    s = text[: idx + 1] if idx > 0 else text
    return (s[: max_len].rstrip() + "…") if len(s) > max_len else s


def _seg_geometry(stage: str) -> tuple[float, float, float, float, float, float]:
    """Return (x1, y1, x2, y2, perp_x, perp_y) for a stage's segment.

    perp is the unit normal, so row offsets stay perpendicular to the arc
    instead of always being vertical (which looks wrong on the steep segments).
    """
    x1, y1, x2, y2 = _SEG[stage]
    dx, dy = x2 - x1, y2 - y1
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    return x1, y1, x2, y2, -dy / length, dx / length


def _jitter(law_id: str) -> float:
    """Small deterministic wobble so a fan doesn't look mechanically ruled."""
    h = int(hashlib.md5(law_id.encode()).hexdigest(), 16)
    return ((h % 1000) / 1000 - 0.5) * 3.0


def _place(laws: list[dict]) -> list[dict]:
    """Assign an (x, y) to every law with a plottable stage."""
    placed: list[dict] = []

    by_stage: dict[str, list[dict]] = {}
    for law in laws:
        stage = law.get("stage", "exploration")
        if stage in _SEG:
            by_stage.setdefault(stage, []).append(law)

    for stage, group in by_stage.items():
        x1, y1, x2, y2, px, py = _seg_geometry(stage)

        # Least- to most-confident along the segment; id breaks ties so the layout
        # is stable across builds and a rebuild produces no spurious diff.
        group = sorted(group, key=lambda l: (_CONF_RANK.get(l.get("confidence", "speculative"), 0),
                                             str(l.get("id", ""))))
        n = len(group)
        two_row = n >= _TWO_ROW_AT

        for i, law in enumerate(group):
            # A single law sits mid-segment; otherwise spread evenly across it.
            frac = 0.5 if n == 1 else i / (n - 1)
            pct = _SPREAD_LO + frac * (_SPREAD_HI - _SPREAD_LO)
            cx = x1 + pct * (x2 - x1)
            cy = y1 + pct * (y2 - y1)

            row = (1 if i % 2 else -1) if two_row else 0
            cx += px * row * _ROW_OFFSET + _jitter(str(law.get("id", "")))
            cy += py * row * _ROW_OFFSET

            conf = law.get("confidence", "speculative")
            cls, conf_label = _CONF_CLS.get(conf, _DEFAULT_CONF)
            placed.append({
                "id":    law.get("id", "?"),
                "title": law.get("title", law.get("id", "?")),
                "stage": stage,
                "conf":  conf_label,
                "blurb": _snippet(law.get("statement")),
                "cx":    max(_DOT_R + 2, min(SVG_W - _DOT_R - 2, cx)),
                "cy":    max(_DOT_R + 2, min(SVG_H - _DOT_R - 2, cy)),
                "cls":   cls,
            })

    placed.sort(key=lambda d: str(d["id"]))
    return placed


def arc_svg(laws: list[dict], interactive: bool = True) -> str:
    """Render the arc with one dot per law. `laws` is an already-loaded list.

    ``interactive=False`` is for embedding the arc somewhere that is not the laws
    page — currently talk slide 02. It drops the ``#ft-tip`` tooltip div and the
    "click a dot to jump to its record" note. Both are wrong off-page: the talk
    deck renders each diagram TWICE (once in the static slide list, once inside
    the player's JS deck data), so a hardcoded element id would be duplicated in
    one document, and there are no ``#law-NNN`` anchors to jump to. The confidence
    legend is kept either way — it is what decodes the dot colours."""
    items = _place(laws)
    tip_html = ('<div id="ft-tip" class="ft-tip" style="display:none"></div>'
                if interactive else "")
    legend_note = ('<span class="ft-legend-note">One dot per law · click a '
                   'dot to jump to its record</span>'
                   if interactive else
                   '<span class="ft-legend-note">One dot per law</span>')

    pts = " ".join(f"{x},{y}" for x, y in [
        (_X0,    _Y_BASE),
        (_X_EXP, _Y_BASE),
        (_X_CT,  _Y_CT),
        (_X_VS,  _Y_BASE),
        (_X_VE,  _Y_BASE),
        (_X_SE,  _Y_SE),
        (_X_RE,  _Y_LEND),
        (_X1,    _Y_LEND),
    ])

    lbl_y = _Y_BASE + 20
    labels = [
        ((_X0 + _X_EXP) // 2,   lbl_y, "Liminal"),
        ((_X_EXP + _X_CT) // 2, lbl_y, "Exploration"),
        ((_X_CT + _X_VS) // 2,  lbl_y, "Sensemaking"),
        ((_X_VS + _X_VE) // 2,  lbl_y, "Valley"),
        ((_X_VE + _X_SE) // 2,  lbl_y, "Heavy Lift"),
        ((_X_SE + _X_RE) // 2,  lbl_y, "Retrospective"),
        ((_X_RE + _X1) // 2,    lbl_y, "Liminal"),
    ]
    labels_html = "\n      ".join(
        f'<text class="ft-lbl" x="{x}" y="{y}" text-anchor="middle">{t}</text>'
        for x, y, t in labels
    )

    ticks_html = "\n      ".join(
        f'<line x1="{x}" y1="{_Y_BASE}" x2="{x}" y2="{_Y_BASE + 6}" '
        f'stroke="#bbb" stroke-width="1"/>'
        for x in (_X_EXP, _X_CT, _X_VS, _X_VE, _X_SE, _X_RE)
    )

    # Each dot is a link to its own card further down the page — the arc is a
    # navigation control, not just a picture.
    dots_html = "\n      ".join(
        f'<a class="ft-dot-link" href="#law-{_esc(it["id"])}" '
        f'data-stage="{_esc(it["stage"])}">'
        f'<circle class="idot {it["cls"]}" '
        f'cx="{it["cx"]:.1f}" cy="{it["cy"]:.1f}" r="{_DOT_R}" '
        f'data-id="{_esc(it["id"])}" '
        f'data-title="{_esc(it["title"])}" '
        f'data-phase="{_esc(it["stage"].replace("-", " ").title())}" '
        f'data-conf="{_esc(it["conf"])}" '
        f'data-blurb="{_esc(it["blurb"])}"/></a>'
        for it in items
    )

    return f"""\
  <div class="ft-wrap">
    <svg viewBox="0 0 {SVG_W} {SVG_H}" class="ft-svg"
         xmlns="http://www.w3.org/2000/svg" role="img"
         aria-label="Double Freytag arc — {len(items)} candidate laws plotted by stage and confidence">

      <!-- rotate(-90) turns the glyph with the text, so the arrow that reads as
           "up" on screen has to be authored as a right-arrow. -->
      <text class="ft-axis" x="10" y="{(_Y_BASE + _Y_SE) // 2}"
            transform="rotate(-90,10,{(_Y_BASE + _Y_SE) // 2})">entropy &#8594;</text>

      <line class="ft-base" x1="{_X0}" y1="{_Y_BASE}" x2="{_X1}" y2="{_Y_BASE}"
            stroke="#ccc" stroke-width="1.2" stroke-dasharray="5,5"/>

      <polyline class="ft-curve" points="{pts}" fill="none" stroke="#2C2C2C"
                stroke-width="2" stroke-linejoin="round"/>

      <circle class="ft-event-dot" cx="{_X_CT}" cy="{_Y_CT}" r="3" fill="#2C2C2C"/>
      <text class="ft-event" x="{_X_CT}" y="{_Y_CT - 9}" text-anchor="middle">Cheap Trick</text>
      <circle class="ft-event-dot" cx="{_X_SE}" cy="{_Y_SE}" r="3" fill="#2C2C2C"/>
      <text class="ft-event" x="{_X_SE}" y="{_Y_SE - 9}" text-anchor="middle">Separation Event</text>

      {ticks_html}
      {labels_html}

      {dots_html}
    </svg>
    {tip_html}
  </div>
  <div class="ft-legend">
    <span class="ft-legend-item"><span class="ft-key key-speculative"></span> Speculative</span>
    <span class="ft-legend-item"><span class="ft-key key-provisional"></span> Provisional</span>
    <span class="ft-legend-item"><span class="ft-key key-supported"></span> Supported</span>
    <span class="ft-legend-item"><span class="ft-key key-unfalsified"></span> Unfalsified</span>
    {legend_note}
  </div>"""


_CSS = """
    .ft-wrap { position: relative; margin: 0 0 0.9rem; }
    .ft-svg  { width: 100%; max-width: 900px; height: auto; display: block;
               overflow: visible; margin: 0 auto; }
    .ft-lbl  { font-family: inherit; font-size: 13.5px; fill: #777; font-weight: 500; }
    .ft-event{ font-family: inherit; font-size: 12px; fill: #444; font-style: italic; }
    .ft-axis { font-family: inherit; font-size: 9px; fill: #ccc;
               text-transform: uppercase; letter-spacing: .06em; }
    .idot    { cursor: pointer; stroke: #fff; stroke-width: 2;
               transition: transform .12s ease, opacity .12s ease;
               transform-box: fill-box; transform-origin: center; }
    .idot:hover { transform: scale(1.5); }
    .ft-dot-link.dimmed .idot { opacity: .17; pointer-events: none; }
    /* `fill` paints the SVG circles; the legend keys are HTML spans and need
       `background` — one palette, two properties, or the legend renders blank. */
    .dot-speculative { fill: #b9b09a; }
    .dot-provisional { fill: #c8a000; }
    .dot-supported   { fill: #2A6B6B; }
    .dot-unfalsified { fill: #2a7a2a; }
    .key-speculative { background: #b9b09a; }
    .key-provisional { background: #c8a000; }
    .key-supported   { background: #2A6B6B; }
    .key-unfalsified { background: #2a7a2a; }
    .ft-tip {
      position: fixed; background: #fff; border: 1px solid #ddd;
      border-radius: 4px; padding: .45rem .7rem; font-size: .82rem;
      color: #2C2C2C; box-shadow: 0 2px 8px rgba(0,0,0,.12);
      pointer-events: none; max-width: 280px; z-index: 100; line-height: 1.5;
    }
    .ft-tip strong { display: block; }
    .ft-tip .tm  { color: #888; font-size: .77rem; margin-bottom: .2rem; }
    .ft-tip .tb2 { color: #444; }
    .ft-legend { display: flex; gap: 1.1rem; flex-wrap: wrap; align-items: center;
                 font-size: .82rem; color: #666; margin: 0 0 2rem; }
    .ft-legend-item { display: flex; align-items: center; gap: .38rem; }
    .ft-key { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
    .ft-legend-note { color: #999; font-style: italic; }
    .law-card.ft-target { animation: ft-flash 1.6s ease-out; }
    @keyframes ft-flash {
      0%   { box-shadow: 0 0 0 3px rgba(42,107,107,.55); }
      100% { box-shadow: 0 0 0 3px rgba(42,107,107,0); }
    }
    @media (prefers-reduced-motion: reduce) {
      .law-card.ft-target { animation: none; }
      .idot { transition: none; }
    }
    @media (max-width: 700px) {
      .ft-lbl { font-size: 17px; }
      .ft-event { font-size: 15px; }
      .ft-legend { gap: .8rem; }
      .ft-legend-note { display: none; }
    }
"""

# Tooltip + filter-sync. The stage chips already filter the cards below; the arc
# has to follow them or the two halves of the page disagree about what is shown.
_JS = """
(function(){
  var tip = document.getElementById('ft-tip');
  if (!tip) return;
  document.querySelectorAll('.idot').forEach(function(d){
    d.addEventListener('mouseenter', function(e){
      tip.innerHTML =
        '<strong>' + (d.dataset.id||'') + ' — ' + (d.dataset.title||'') + '</strong>' +
        '<div class="tm">' + (d.dataset.phase||'') + ' · ' + (d.dataset.conf||'') + '</div>' +
        '<div class="tb2">' + (d.dataset.blurb||'') + '</div>';
      tip.style.display = 'block';
      move(e);
    });
    d.addEventListener('mousemove', move);
    d.addEventListener('mouseleave', function(){ tip.style.display = 'none'; });
  });
  function move(e){
    var x = e.clientX + 14, y = e.clientY - 10;
    var w = tip.offsetWidth || 260;
    if (x + w > window.innerWidth - 8) x = e.clientX - w - 14;
    tip.style.left = x + 'px';
    tip.style.top  = y + 'px';
  }

  document.querySelectorAll('.stage-filter').forEach(function(btn){
    btn.addEventListener('click', function(){
      var f = btn.getAttribute('data-filter');
      document.querySelectorAll('.ft-dot-link').forEach(function(a){
        a.classList.toggle('dimmed', f !== 'all' && a.getAttribute('data-stage') !== f);
      });
      tip.style.display = 'none';
    });
  });

  // The jump itself is left to the browser. The wrapping <a href="#law-NNN"> is a
  // real fragment link and the site already sets `html { scroll-behavior: smooth }`,
  // so the native anchor navigation is both correct and animated with no script at
  // all. An earlier version called preventDefault() and drove scrollIntoView by
  // hand, which only added a way for the jump to break while removing the working
  // fallback. This handler therefore does no navigation — it only flashes the
  // destination, so a reader thrown several thousand pixels down the page can see
  // where they landed, and clears the tooltip, which would otherwise be stranded
  // on screen after the viewport moves out from under the cursor.
  document.querySelectorAll('.ft-dot-link').forEach(function(a){
    a.addEventListener('click', function(){
      tip.style.display = 'none';
      var card = document.querySelector(a.getAttribute('href'));
      if (!card) return;
      card.classList.remove('ft-target');
      void card.offsetWidth;          // restart the animation on a repeat click
      card.classList.add('ft-target');
      setTimeout(function(){ card.classList.remove('ft-target'); }, 1600);
    });
  });
})();
"""
