# Bibliography Pattern

The bibliography (`bibliography/`) is the researcher's personal curated library — a subset of sources that have been engaged with and found relevant, distinct from the general corpus the researcher queries.

## Distinction from the research corpus

| | Research corpus | Personal bibliography |
|---|---|---|
| Contents | All indexed sources | Sources the researcher has specifically engaged with |
| Purpose | Retrieval target | Active reference set |
| Curation | Automated ingestion | Manual, high-threshold |
| Depth | Uniform (all indexed equally) | Variable (some sources are "deep-read") |

## Directory structure

```
bibliography/
├── personal-bib.md         Curated reference list with annotations
└── deep-reads/             Full M-003 deep-read entries (one file per source)
    └── [author-title].md
```

## Personal bibliography format

`personal-bib.md` is a curated list of sources the researcher has directly engaged with and found valuable. Each entry includes:
- Bibliographic information
- Why this source was selected
- What it contributes (key concepts, examples, or findings)
- Relationship to the research inventory (which laws or hypotheses it informs)

The personal bibliography is a living document. Sources are added when engaged with; they are not removed if they become less relevant, but their status can be updated.

## Deep reads

A deep read (`bibliography/deep-reads/`) is a full M-003 entry for a source that has been internalized rather than merely consulted. The format is prescribed in `methods/M-003-deep-read.md`. The deep-read set is small by design — fewer than 10 sources at any time. Depth beats breadth.

## Selection threshold

Adding a source to the personal bibliography requires direct engagement (reading, not retrieval). The threshold is lower than for deep reads: any source that was read and found relevant qualifies. Deep reads require meeting 3 of 5 selection criteria defined in M-003.
