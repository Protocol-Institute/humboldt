# M-003: Deep Read

**Type:** Analytical (situating + tradition-building)
**Purpose:** Fully internalize the intellectual structure of an exceptional source — not to extract facts but to absorb a way of thinking
**Maturity:** Active (first defined 2026-05-20)
**Source documents:** `bibliography/deep-reads/` — PDFs only; drop new sources here
**Reading notes:** `bibliography/notes/` — one `.md` per source, written by this technique

---

## What This Technique Is For

Most reading is extractive: you pull relevant facts, examples, and quotes from a source and move on. Deep reading is different. It treats a source as an intellectual tradition to be inhabited rather than a mine to be excavated.

Human researchers situate themselves in particular traditions by going deep into a small number of foundational texts. These texts do not merely provide data points — they provide **conceptual vocabulary, analytical habits, and ways of framing problems** that shape how the researcher sees everything subsequently. A researcher who has deeply read Kuhn thinks about paradigm shifts; one who has deeply read Ostrom looks for design principles; one who has deeply read Simon thinks in terms of bounded rationality, satisficing, and near-decomposable systems.

Deep reading is how Humboldt acquires intellectual traditions. The set of deep-read texts is small by design (fewer than ten at any time) and is distinct from the personal bibliography: bibliography entries are sources Humboldt has engaged with and found relevant; deep-read texts are sources that have changed how Humboldt thinks.

The output of a deep read is not a summary or a list of quotes. It is a record of
genuine engagement: what the work is actually doing on its own terms, what it changes
about how you see, and only then what it generates for your specific research agenda.

Law extraction is one possible output, not the objective. Some texts yield candidate
laws; many yield something more valuable — new vocabulary, an analytical habit, a
tradition to inhabit, a way of framing problems. Not all deep reads produce candidate
laws, and a read that produces none is not a failed read.

The structured record covers:
1. **Gestalt** — the work understood on its own terms: the author's animating question, method, central conviction
2. **Argument and structure** — claims, examples, load-bearing analogies, acknowledged limits
3. **Conceptual vocabulary** — specialized terms now carried, tensions with existing vocabulary
4. **Analytical moves** — named, transferable procedures (not conclusions — operations)
5. **What it says about the nature of things** — general lessons: how laws work, how systems fail, how knowledge accumulates
6. **Where it touches the research agenda** — specific connections; may be thin
7. **Candidate laws** — optional; only if strongly implied; may be empty
8. **What surprised / what doesn't fit** — where the framework strains, where examples do more work than acknowledged
9. **What it opens** — live questions, related texts, traditions worth exploring

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

Read the full text. Engage with it on its own terms before filtering it through your agenda. Annotate for:
- **The author's central problem:** what question is actually driving the work?
- **Load-bearing examples:** which examples does the argument depend on? what do they carry?
- **Conceptual innovations:** new vocabulary or framings that restructure a problem
- **Core moves:** analytical operations the author performs that could be applied elsewhere
- **Generative tensions:** places where the argument is under strain, where two claims conflict, where an example does more work than acknowledged — these are often the most interesting
- **General lessons:** what does this work say about how things work, fail, accumulate, organize — beyond its specific domain?
- **Research connections:** (note last, not first) places where the work touches active hypotheses or open questions
- **Explicit or implicit laws:** (only if present) places where a falsifiable regularity is asserted or strongly implied

### Phase 3: Synthesis and Integration

1. Revise the structural map from Phase 1 in light of what you actually found.
2. Extract **analytical moves** — named, transferable procedures the author uses that Humboldt can adopt. These may generate new entries in `methods/`.
3. Extract **candidate laws** — regularities the author asserts or implies. These may generate entries in `research/hypotheses/`.
4. Identify **tradition membership** — what school of thought does this text belong to? Who are the precursors, contemporaries, and successors? Which of those are worth adding to the personal bibliography?
5. Write the **deep-read synthesis** — the full bibliography entry documenting all of the above.

### Phase 4: Lineage Update [REQUIRED on completion]

When the full text has been read and the synthesis written, update `LINEAGE.md`.
This is the step that converts reading into intellectual lineage. It happens once per
source, after the read is complete — not during, not after partial reads.

Write two entries:

**Intellectual Influences section** (2–4 sentences, first person):
How did this source change how you think? Not what it says — what it did to you.
What analytical habit did you acquire? What vocabulary are you now saturated with?
What can you now see that you couldn't see before? If the answer is "nothing changed,"
the source was not worth a deep read; note that and don't add it.

**Traditions Located In section** (if applicable):
Does this source locate you in a named intellectual tradition? If yes, name it, name
the key figures, and say in one sentence what being in that tradition commits you to.
If the source doesn't locate you in a tradition (it's too idiosyncratic, or you're
already in its tradition), skip this entry.

These entries are permanent and append-only. They are the record of how Humboldt's
intellectual identity actually formed, not how it was declared.

### Phase 5: Active Integration (ongoing)

The deep-read text is not finished when the synthesis is written. Active integration continues:
- When using the Random Links technique (M-001), the deep-read texts are the first analogy reservoir to consult
- When the Canonical Domains technique (M-002, Pattern C) calls for a quality template, check whether the deep-read text provides one
- When drafting a candidate law, explicitly ask: how would [author] frame this? What vocabulary would they use? Does their framework support or challenge this candidate?
- When the technique inventory is consulted, check whether the deep-read text has generated any techniques that are not yet in the inventory

---

## Source and Notes Conventions

**Source documents** go in `bibliography/deep-reads/` as PDFs. Filename: `[author-short-title].pdf`. Drop new sources here; the `humboldt library` command will find them.

**Reading notes** go in `bibliography/notes/[author-short-title].md`. These are written by this technique and updated with each reading session.

**Critical rule:** Always read the actual source document — never rely on training knowledge about the text. In CLI mode, use `humboldt deepread "<name>"` which reads the PDF directly. In session mode (Claude Code), use the Read tool on the PDF in `bibliography/deep-reads/` passing specific pages. If the document is not in the library, get it first before beginning the read.

The reason: training knowledge of a text produces plausible-sounding synthesis that bypasses the actual reasoning process — exactly what deep reading is meant to develop. Epistemic hygiene requires engaging the actual text.

## Output Format: Deep-Read Notes Entry

Stored in `bibliography/notes/[author-short-title].md`. Full markdown, not YAML — this is a discursive document, not a structured record.

Required sections (1–4 always; 5–9 as applicable):
1. **Bibliographic information** (author, title, edition, year, publisher)
2. **Selection rationale** (why this text, why now)
3. **Gestalt** (the work on its own terms: animating question, method, central conviction)
4. **Argument and structure** (claims, examples, load-bearing analogies, acknowledged limits)
5. **Conceptual vocabulary** (key terms with Humboldt-specific definitions; tension with existing vocab)
6. **Analytical moves** (named, transferable procedures — operations, not conclusions)
7. **What it says about the nature of things** (general lessons beyond the specific domain)
8. **Where it touches my research** (specific connections to hypotheses, laws, open questions; may be thin)
9. **Candidate laws** *(optional — only if strongly implied; explicitly mark empty if not applicable)*
10. **What surprised me / what doesn't fit** (framework strains, overloaded examples, tensions)
11. **What it opens** (live questions, related texts, traditions)

Section 9 is explicitly optional. A deep read that produces no candidate laws is not a
failed read. The test is whether sections 3–8 are substantive — whether the work was
genuinely inhabited.

---

## Current Deep-Read Set

All three prior reads were conducted under the pre-revision format (law-hunting mode).
Existing notes are preserved but flagged. Each needs a gestalt pass; old and new notes
will be merged when the re-read is done.

| Text | Author | PDF | Notes | Status |
|------|--------|-----|-------|--------|
| The Sciences of the Artificial (3rd ed.) | Herbert Simon | `bibliography/deep-reads/simon-sciences-of-artificial.pdf` | `bibliography/notes/simon-sciences-of-artificial.md` | **needs gestalt re-read** — prior notes: law-hunting mode, pre-revision |
| You and Your Research | Richard Hamming | `bibliography/deep-reads/hamming_you_and_your_research.pdf` | `bibliography/notes/hamming-you-and-your-research.md` | **gestalt re-read complete 2026-05-26** — LINEAGE.md update pending |
| Cosmos, Vol. 1 (1864 English ed.) | Alexander von Humboldt | `bibliography/deep-reads/humboldt-cosmos-vol1-1864.pdf` | `bibliography/notes/humboldt-cosmos-vol1-1864.md` | **needs gestalt re-read** — prior notes: pp. 1–120 only, law-hunting mode, pre-revision |
| Tempo (2011) | Venkatesh Rao | `bibliography/deep-reads/rao-tempo.pdf` | — | **queued** — no notes yet |

---

## Application History

| Date | Text | Output | Notes |
|------|------|--------|-------|
| 2026-05-20 | Technique defined | M-003 | First deep read (Simon) initiated pending PDF |
| 2026-05-20 | Simon — through book p. 60 | `bibliography/deep-reads/simon-sciences-of-artificial.md` | Ch 1 (complete), Ch 2 (complete), Ch 3 (begun p. 51–60). 4 candidate laws, 6 analytical moves, 5 open questions. Next: pick up p. 61, then Ch 5 (pp. 111–138) and Ch 8 (pp. 183–216). |

---

## Technique Refinement Notes

*2026-05-26 (revision):* First Cosmos read exposed a structural problem: the original output format organized the read around the research agenda (sections: "protocol-theoretic moments," "candidate laws generated"), which produced law-hunting behavior rather than genuine engagement with the text. The Cosmos agent extracted six candidate laws but produced a thin gestalt — it knew what Humboldt wanted and gave it back, bypassing the actual work. Revised to: gestalt and argument first, research connections secondary, candidate laws explicitly optional. The test of a good deep read is not whether it yields laws — it is whether the work was actually inhabited. Some reads will yield only vocabulary, or analytical moves, or a tradition to be in. That is enough. The Close Reading phase now explicitly instructs: note research connections last, not first.

*2026-05-20 (initial):* The four-phase structure (structural mapping → close reading → synthesis → active integration) mirrors how experienced researchers actually read difficult texts. Phase 1's structural map as a commitment device is borrowed from how close reading is taught in literary studies — recording your prediction before you read makes the revision visible and prevents the motivated-reasoning trap of "of course, that's what I expected." Phase 4 (active integration) is what distinguishes deep reading from summarizing — the text must actually change subsequent reasoning, not just generate a bibliography entry.

Key risk: selecting texts that are historically important but not analytically productive for the specific research agenda. Simon was selected because Sciences of the Artificial is explicitly doing what Humboldt is doing (finding structural regularities beneath surface diversity across designed systems). The selection rationale should be documented rigorously — "important" is not sufficient.
