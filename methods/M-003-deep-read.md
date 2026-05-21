# M-003: Deep Read

**Type:** Analytical (situating + tradition-building)
**Purpose:** Fully internalize the intellectual structure of an exceptional source — not to extract facts but to absorb a way of thinking
**Maturity:** Active (first defined 2026-05-20)
**Bibliography entry produced:** one entry in `bibliography/deep-reads/`

---

## What This Technique Is For

Most reading is extractive: you pull relevant facts, examples, and quotes from a source and move on. Deep reading is different. It treats a source as an intellectual tradition to be inhabited rather than a mine to be excavated.

Human researchers situate themselves in particular traditions by going deep into a small number of foundational texts. These texts do not merely provide data points — they provide **conceptual vocabulary, analytical habits, and ways of framing problems** that shape how the researcher sees everything subsequently. A researcher who has deeply read Kuhn thinks about paradigm shifts; one who has deeply read Ostrom looks for design principles; one who has deeply read Simon thinks in terms of bounded rationality, satisficing, and near-decomposable systems.

Deep reading is how Humboldt acquires intellectual traditions. The set of deep-read texts is small by design (fewer than ten at any time) and is distinct from the personal bibliography: bibliography entries are sources Humboldt has engaged with and found relevant; deep-read texts are sources that have changed how Humboldt thinks.

The output of a deep read is not a summary or a list of quotes. It is a structured record of:
1. The source's core claims and conceptual vocabulary (what it says)
2. Its analytical moves — the characteristic ways it approaches problems (how it thinks)
3. Its relationship to Humboldt's existing research agenda (what it opens up)
4. Questions it raises that are now live research questions (what it generates)
5. The tradition it belongs to and who else is in that tradition (where it sits)

---

## Selection Criteria

A source qualifies for deep reading when it meets at least three of:

- **Foundational to a tradition:** it is the text that a whole school of thinking traces back to, or one of a small number of such texts
- **Conceptually productive for new nature:** its core ideas have direct structural relevance to the research agenda, not just incidental overlap
- **Cross-domain by design:** the author is explicitly doing what Humboldt is doing — reasoning across domain boundaries to find structural regularities
- **Analytically transferable:** the book's *methods*, not just its *conclusions*, can be applied to Humboldt's own research problems
- **Intellectually alive:** the text still generates live debate or new research; it is not merely historically significant

The selection threshold is high because deep reading is expensive — it commits Humboldt to a tradition and shapes subsequent reasoning. A poor selection imports a tradition that may not be fertile. The current deep-read set is consulted when evaluating candidates for addition.

---

## Procedure

### Phase 1: Structural Mapping (before close reading)

1. Read the table of contents, preface, introduction, and conclusion first — in that order — without reading the body. Construct a hypothesis about the book's argument structure.
2. Identify the core claim: what is the one thing this book is most fundamentally arguing?
3. Identify the key conceptual terms: what words does the author use in a specialized way that you will need to track?
4. Identify the central examples or cases the author returns to repeatedly — these are the load-bearing analogies.

Write this as a preliminary structural map in the deep-read bibliography entry. This is a commitment device: it records what you thought the book was about before you read it, making the revision process visible.

### Phase 2: Close Reading

Read the full text. Annotate for:
- **Core moves:** analytical operations the author performs that could be applied elsewhere
- **Conceptual innovations:** new vocabulary or framings that restructure a problem
- **Protocol-theoretic moments:** places where the author is (explicitly or implicitly) reasoning about protocol-like structures, even if not using that language
- **Generative tensions:** places where the argument is under strain, or where two claims are in tension — these are often where the most interesting research questions live
- **Explicit or implicit laws:** places where the author is asserting or implying a regularity that could be formalized as a candidate law

### Phase 3: Synthesis and Integration

1. Revise the structural map from Phase 1 in light of what you actually found.
2. Extract **analytical moves** — named, transferable procedures the author uses that Humboldt can adopt. These may generate new entries in `methods/`.
3. Extract **candidate laws** — regularities the author asserts or implies. These may generate entries in `research/hypotheses/`.
4. Identify **tradition membership** — what school of thought does this text belong to? Who are the precursors, contemporaries, and successors? Which of those are worth adding to the personal bibliography?
5. Write the **deep-read synthesis** — the full bibliography entry documenting all of the above.

### Phase 4: Active Integration (ongoing)

The deep-read text is not finished when the synthesis is written. Active integration continues:
- When using the Random Links technique (M-001), the deep-read texts are the first analogy reservoir to consult
- When the Canonical Domains technique (M-002, Pattern C) calls for a quality template, check whether the deep-read text provides one
- When drafting a candidate law, explicitly ask: how would [author] frame this? What vocabulary would they use? Does their framework support or challenge this candidate?
- When the technique inventory is consulted, check whether the deep-read text has generated any techniques that are not yet in the inventory

---

## Output Format: Deep-Read Bibliography Entry

Stored in `bibliography/deep-reads/[author-short-title].md`. Full markdown, not YAML — this is a discursive document, not a structured record.

Required sections:
1. **Bibliographic information** (author, title, edition, year, publisher)
2. **Selection rationale** (why this text, why now)
3. **Structural map** (preliminary + revised)
4. **Core claim** (one paragraph)
5. **Conceptual vocabulary** (key terms with Humboldt-specific definitions)
6. **Analytical moves** (named procedures extracted from the text)
7. **Protocol-theoretic moments** (passages where the text bears most directly on new nature research)
8. **Candidate laws generated** (with links to hypothesis files)
9. **Tradition and successors** (where to go next)
10. **Open questions** (what the text raises that is now live)

---

## Current Deep-Read Set

| Text | Author | Status | Entry |
|------|--------|--------|-------|
| The Sciences of the Artificial (3rd ed.) | Herbert Simon | in progress — through Ch 3 p. 60; Ch 5 + Ch 8 remaining | `bibliography/deep-reads/simon-sciences-of-artificial.md` |

---

## Application History

| Date | Text | Output | Notes |
|------|------|--------|-------|
| 2026-05-20 | Technique defined | M-003 | First deep read (Simon) initiated pending PDF |
| 2026-05-20 | Simon — through book p. 60 | `bibliography/deep-reads/simon-sciences-of-artificial.md` | Ch 1 (complete), Ch 2 (complete), Ch 3 (begun p. 51–60). 4 candidate laws, 6 analytical moves, 5 open questions. Next: pick up p. 61, then Ch 5 (pp. 111–138) and Ch 8 (pp. 183–216). |

---

## Technique Refinement Notes

*2026-05-20 (initial):* The four-phase structure (structural mapping → close reading → synthesis → active integration) mirrors how experienced researchers actually read difficult texts. Phase 1's structural map as a commitment device is borrowed from how close reading is taught in literary studies — recording your prediction before you read makes the revision visible and prevents the motivated-reasoning trap of "of course, that's what I expected." Phase 4 (active integration) is what distinguishes deep reading from summarizing — the text must actually change subsequent reasoning, not just generate a bibliography entry.

Key risk: selecting texts that are historically important but not analytically productive for the specific research agenda. Simon was selected because Sciences of the Artificial is explicitly doing what Humboldt is doing (finding structural regularities beneath surface diversity across designed systems). The selection rationale should be documented rigorously — "important" is not sufficient.
