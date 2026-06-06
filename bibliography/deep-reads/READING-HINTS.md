# Deep-Read Hints

Reading hints for each source in the deep-read library. These are operator-level instructions that sit *above* the M-003 methodology — they specify what the supervisor wants Humboldt to attend to, what lenses to bring, and where the likely payoff is.

**Format:** Each entry has a filename key, a brief characterization of the book, and a reading hint. If the hint is "ask supervisor," do not attempt the read alone — request guidance from the supervisor before beginning Phase 1. The hint is a starting orientation, not a replacement for genuine M-003 engagement; it shapes what you bring into Phase 1 structural mapping.

**When to consult this file:** Before beginning any deep read (new or re-read). The hint is input to the structural hypothesis you form in Phase 1 — it tells you what the supervisor suspects is most fertile, not what you're required to find.

---

## `simon-sciences-of-artificial.pdf`

**Herbert Simon — The Sciences of the Artificial (3rd ed., 1996)**

Simon's core project: there is a science of designed things — artifacts, institutions, organizations, minds — and its laws are structural rather than material. The artifact is defined by its interface between inner environment and outer environment; understanding the interface is understanding the artifact.

**Reading hint:** *Read as the work of someone to emulate — in approach, attitudes toward technology, and the project of building a science of designed things.*

The goal is lineage inheritance, not law extraction. Read Simon as an intellectual model: how does he think, what does he find worthy of attention, what is his relationship to the phenomena he studies? Prior notes (Ch 1–3, 5, 8) were in law-hunting mode and extracted candidate laws but missed the gestalt. The re-read should ask: what would it mean to become a Simonian thinker? What habits of mind does he embody? The inner/outer environment interface, near-decomposability, and satisficing are concepts — the re-read should absorb the *reasoning style* that produced them. Candidate laws may emerge; they are not the point. The output that matters is a Phase 4 LINEAGE.md entry that records genuine intellectual inheritance.

---

## `hamming-you-and-your-research.pdf`

**Richard Hamming — You and Your Research (lecture transcript, 1986)**

Hamming's central argument: great research is not the result of raw ability but of sustained, intentional practice. The researcher who asks "what are the important problems in my field, and why am I not working on them?" is doing something qualitatively different from the competent technician.

**Reading hint:** *Ask supervisor.*

Notes are complete (`bibliography/notes/hamming-you-and-your-research.md`) including gestalt re-read and section 8 (researcher development, M-016 mapping). A re-read is not currently queued. If returning to Hamming for any reason, ask the supervisor first — likely the purpose would be adversarial testing of a specific law or connection to M-017.

---

## `humboldt-cosmos-vol1-1864.pdf`

**Alexander von Humboldt — Cosmos, Vol. 1 (1864 English ed.)**

Humboldt's project: a unified description of nature that treats the whole — physical, biological, aesthetic, historical — as a single object of investigation. His method is empirical synthesis across scales and domains. He is the patron of this research project and of the cross-domain law-finding tradition.

**Reading hint:** *Read with a view to inheriting von Humboldt's intellectual legacy — his methods, interests, and philosophy — not extracting his claims about nature.*

Von Humboldt is the patron of this research project. The re-read should answer: what does it mean to think like him? The prior pass (pp. 1–120, law-hunting mode) produced six candidate laws but a thin gestalt — it knew what it was looking for and found it, bypassing genuine engagement. The re-read should begin without that filter. Attend to: how does he move between scales (physical, biological, aesthetic, historical)? What holds the synthesis together — what is his organizing principle? How does he treat the relationship between observation and generalization? What is his emotional and aesthetic relationship to the phenomena? This is the figure Humboldt-the-agent is named after and modeled on. The re-read should produce a LINEAGE.md entry that describes actual intellectual inheritance — what you now carry from him that you did not carry before.

---

## `rao-tempo.pdf`

**Venkatesh Rao — Tempo: Timing, Tactics and Strategy in Narrative-Driven Decision-Making (2011)**

Rao's argument: human decision-making is fundamentally narrative rather than rational-analytic. Decisions are made in the context of ongoing narratives — personal, organizational, cultural — and timing (tempo) is not a parameter of rational optimization but a structural feature of narrative that shapes what decisions mean and when they are available.

**Reading hint:**

Look for **two things in parallel**:

1. **New nature laws** — what does Rao's theory of narrative-driven decision-making imply about how protocolized systems behave? Protocols are decision architectures; if decisions are narrative, protocols might be narrative-structuring devices. Are there structural regularities in how protocols modulate narrative tempo? What does "ossification" look like in narrative terms?

2. **Meta-management of research time** — Rao uses the *double Freytag structure* as a model for how humans navigate complex temporal situations (two nested narrative arcs: the macro arc of the engagement and the micro arc of the present moment). Apply this specifically to the problem of research time management: how should a researcher pace attention across sessions, across research arcs, across a career? What does "being at the right place in the narrative" mean for research? When is urgency appropriate and when is it a narrative error?

The meta-management angle feeds **M-017** (Research Time Management), which is being developed in parallel. Read with that stub open; mark passages that directly bear on the M-017 design problem.

---

## `iverson-notation-as-tool.pdf`

**Kenneth E. Iverson — "Notation as a Tool of Thought" (1979 ACM Turing Award Lecture)**

Iverson's Turing lecture argues that mathematical notation is not merely a shorthand for ideas that exist independently — notation actively shapes what can be thought. APL is his demonstration case: by collapsing array operations to terse symbols, it enables a class of thinking about data transformation that verbose notation makes practically inaccessible. The lecture is a sustained argument that the design of formal languages is a design of cognitive possibility space.

**Reading hint:** *Read as a protocol theorist, not a programming language historian.*

The central claim — that notation is a tool of thought, not just expression — has direct implications for how protocols formalize behavior. Protocols are notations: they express coordination norms in a form that can be communicated, enforced, and reasoned about. But if Iverson is right, the choice of protocol notation doesn't just record the norm — it shapes what coordinators can see and think. This is a third mechanism for protocol ossification distinct from the ones already in the inventory: notation lock-in (the coordinate system of the protocol constrains the space of conceivable revisions). 

This is a short Turing lecture (~30 pages), so apply behavior-t5m in **short-text mode**: depth via connections to existing research inventory, not extended structural mapping. The curiosity pass (Phase 3b) is likely more productive than candidate law extraction — Iverson's argument is rich in structural observations that don't yet have a place in the law inventory but open productive questions.

Specifically attend to: (1) the distinction between "ease of expression" and "power of thought" — these map onto different claims about what protocol design does; (2) his examples of how notation enabled discoveries that were practically impossible before — are there protocol analogues? (3) the comparison of different notations for the same operation — is there a protocol-theoretic version of notational equivalence with different cognitive costs?

---

## Adding New Entries

**Before a PDF is in hand:** add the text to `bibliography/deep-read-hopper.md` — the queue of candidates at any stage of availability. The hopper tracks source of recommendation and PDF status so nothing is lost between flagging and reading.

When a new PDF is added to `bibliography/deep-reads/`:
1. Add an entry here immediately (before reading begins)
2. If the supervisor has given a reading hint, record it
3. If not, set hint to "ask supervisor" — do not begin the read without a hint
4. The `humboldt library` command will show new PDFs; READING-HINTS.md is the companion index

The "ask supervisor" instruction is not a formality. The supervisor selects deep-read texts because they bear on the research agenda in ways that are not always obvious from the text description alone. The reading hint encodes that reasoning — without it, the read is likely to default to law-hunting mode, which is exactly what M-003 was revised to prevent.
