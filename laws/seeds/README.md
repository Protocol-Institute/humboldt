# Seeds — the law holding pen

A seed is a law-shaped fragment not yet worth its own record: an idea, observation,
motif, or question. Seeds are **cheap and unmanaged** — no schema ceremony, no lifecycle.

The induction sweep (`induct`, plan §5 stage 5) samples seeds and either promotes them
into exploration-stage law records, attaches them to existing laws as evidence, or
leaves them. Shallow and deep reads emit new seeds.

## Convention — `seed-NNN-<slug>.yaml`

```yaml
id: seed-031
title: short name
text: |
  the fragment itself — one paragraph is plenty
source: bibliography/shallow-reads/....md   # where it came from, or "inbox" / "operator"
origin: C-031            # provenance if migrated from a legacy C item; else omit
surfaced: 2026-06-06     # date it first appeared
type: insight            # insight | observation | question | motif (free-form, advisory)
connections: [L-003]     # optional: related law ids (legacy C/H/CL tags kept raw)
status: open             # open | promoted | attached | dropped
```

Only `id`, `title`, `text`, `source` are load-bearing. Everything else is advisory.

Migrated 2026-08-01 from the 47 `research/c/` curiosity items (redesign §3.2).
