# M-004: Reading Prioritization

**Type:** Meta (controls when and how deeply Humboldt reads)
**Purpose:** Decide what to read next from the library, and whether to read shallowly or deeply
**Maturity:** Stub — heuristics to be developed from practice
**Triggers:** Any time the library contains unread documents; also at Track 1 session start when choosing what to work on

---

## What This Technique Is For

As the library grows, Humboldt cannot read everything deeply — deep reading is expensive and
commits Humboldt to a tradition. Reading prioritization governs:

1. **Selection** — which document to engage with next
2. **Depth** — whether to do a full M-003 deep read or a lighter scan
3. **Timing** — when in the research program a particular source becomes valuable

The goal is to read in service of active research needs, not to maximize coverage. A source
read at the wrong time (before the hypothesis that would make it useful has formed) produces
weaker synthesis than the same source read when Humboldt has a live question it can answer.

---

## Stub: Heuristics Under Development

*These are candidate heuristics, not yet validated through practice. Each will be marked
confirmed / revised / dropped as reading sessions accumulate.*

### Selection heuristics

**H1 — Active hypothesis pull** *(priority)*
A source that speaks directly to an active hypothesis (in `research/hypotheses/`) is
preferred over a source that is generally relevant. Hypothesis-driven reading produces
stronger evidence and sharper synthesis.

**H2 — Citation hub**
A source cited by multiple already-read sources is a candidate for deep reading. High
in-library citation count suggests foundational status in this research program.

**H3 — Domain gap**
If the current law inventory has thin evidence in a canonical domain (`methods/canonical-domains.yaml`),
prefer a source from that domain. Domain gaps are a structural weakness in cross-domain laws.

**H4 — Tradition adjacency**
After a deep read, the source's "tradition and successors" section names next candidates.
These are warm leads — the intellectual thread is live, the vocabulary is already acquired.

**H5 — Recency signal**
Recent work (last 5 years) is prioritized when an established law may have new counterexamples
or when a new empirical domain has emerged. Classical sources are preferred when building
conceptual foundations.

### Depth heuristics

**D1 — Selection criteria gate**
Apply M-003 selection criteria first. If a source meets ≥3 criteria, it is a deep-read
candidate. If it meets 1–2, scan mode. If 0, extract specific passages only.

**D2 — Hypothesis resolution**
If a source can resolve a specific active hypothesis (confirm, refute, or sharpen), read
the relevant sections deeply regardless of overall selection score. Targeted depth beats
comprehensive shallowness.

**D3 — Diminishing returns**
If the library already contains 2+ sources from the same tradition (e.g., two Simon-adjacent
organizational theory texts), prefer breadth — add a source from a different domain.

### Timing heuristics

**T1 — Inventory maturity**
Early in the research program (< 10 laws), prioritize generative sources — texts that
produce candidate laws readily. After the inventory matures, prioritize analytical and
critical sources — texts that stress-test and unify existing candidates.

**T2 — After a deep read**
A deep read opens questions and names successors. Schedule the next reading session to
follow one of those threads before the intellectual context fades (within 2–3 sessions).

---

## Future Development

This technique stub will be developed through practice. After each reading decision,
record:
- Which heuristic(s) drove the choice
- Whether the source delivered on the expectation
- Whether the depth choice was right

Over time, the heuristics will be ranked, refined, and some dropped. The goal is an
explicit, improvable model of Humboldt's reading judgment — not a fixed algorithm.

**Open design questions:**
- Should this technique produce a ranked reading queue at session start? Or is on-demand
  judgment better than a pre-committed queue?
- How should the library manifest in the system prompt so Humboldt can apply these
  heuristics automatically rather than requiring operator input?
- What is the relationship between reading prioritization and the periodic literature
  survey mechanism (future M-005)?

---

## Application History

| Date | Document chosen | Heuristic(s) applied | Depth | Outcome |
|------|----------------|---------------------|-------|---------|
| — | — | — | — | — |
