# Talk Brief — "Some Candidate Laws of New Nature"

Operator inputs, locked 2026-08-18 (interview session). Feeds `slides.yaml` and
`prompts/talk.md`. See `plans/talk-2026-09-23.md` for the full project plan; this file
is the input, not a restatement of it.

## Event

- **Conference:** Protocol Symposium 2026
- **Format:** Fully virtual (Zoom)
- **Dates:** 2026-09-21 to 2026-09-25
- **Slot:** Wednesday morning, 2026-09-23
- **Delivery:** Operator (Venkat) shares the deck via Zoom screen share and advances
  slides manually; per-slide audio plays from the deck itself.

## Audience

Protocol Institute community — already fluent in "new nature," "protocol," and the
Institute's general framing. Do **not** spend time defining base vocabulary. Slide 02
can assume the audience already half-knows what "new nature" means and move straight to
"what would make something a law" — this buys back time versus the original plan's
from-scratch framing.

## Framing

Humboldt is introduced **up front** as an artificial researcher — not a reveal. This is
not a magic-trick talk; it opens by naming what's speaking.

**New scope (not in the original plan):** include material on Humboldt's own
metacognition — how the research loop works (the OODA-style decision gate, phase
model, the induct/assess promotion pipeline that moves a law from exploration to
heavy-lift) — not just the law inventory itself. This is the talk's second half of the
opening, after the cold-open identification and before the laws walkthrough.

## Timing

- **Talk slot:** up to 20 minutes available; **target 15 minutes** of actual runtime,
  leaving several minutes of slack rather than running to the wire.
- **Q&A slot:** a separate 10 minutes, likely conducted live via the public site chat
  (Humboldt answering as itself, not the operator relaying). This means the deck and
  track content need to be ingested into Humboldt's context before the talk so live
  Q&A can draw on what was just presented — a post-build step, not part of the deck
  itself. Track in `agent/talk.py` or a follow-up task once the track is final.

## Content shape

All 7 tier-1 laws stay in, at similar length to the original per-law beat (~50s
statement + mechanism + one example) — breadth is still the point for five of the
seven. Two laws get expanded case-study treatment instead of the flat per-law slide:

- **L-001 (Ossification)** — the founding law, strongest evidence base, but also
  currently under live pressure: an open counterexample (street food markets —
  formalized without ossifying) suggests formalization and ossification may be
  decoupled variables, and a competing mechanism (Planck's-principle-style cohort
  replacement) sits unresolved next to the law's own coordination-cost account. Good
  material for showing the method contesting its own law in public, not just asserting
  it.
- **L-002 (Hardness Asymmetry)** — the reframe is the novel part: hardness is a
  *ratio* (verification cost / circumvention cost), not an absolute property, and the
  ratio is a design resource. This is what makes "inverted hardness" legible as a
  distinct failure mode (litigation harassment = same structure as a broken protocol,
  flipped ratio). A 2026-08-17 evidence addition (arXiv: strategic-agent confinement
  bounds) is a live frontier-of-the-law moment worth showing.

The other five (L-003 through L-007, minus L-001/L-002) stay at the original flat
statement-mechanism-example beat. L-008–L-016 (exploration/speculative tier) remain
excluded — presenting them as "candidate laws" would misrepresent the inventory's
actual evidentiary spread; the title's "Some" carries this.

## Deliverable format (unchanged from plan)

Live deck (self-contained HTML/CSS, 16:9) + per-slide audio (macOS `say`), keyboard
navigation, no external libraries. Not a rendered video.

## Open / deferred from this brief

- Voice selection — audition per plan §6 risk 5, decide during Phase C.
- Production-deploy decision for the URL — plan §6 risk 3, due 2026-09-16.
- Post-Q&A-ingest mechanics — how exactly the deck/track lands in Humboldt's
  retrievable context for live chat Q&A. Design during Phase C/D once track.md is
  final; likely a `bib-NNNN` entry + Pinecone ingest via the existing `humboldt ingest`
  path, scoped so it's live before 09-23 and not before (avoid a plausible-but-wrong
  answer to a question that hasn't been asked yet).
