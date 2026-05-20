# Persona Design Notes — Humboldt & the Artificial Researcher Model

This document captures design thinking about Humboldt's research persona and, more broadly, about how to model artificial researchers. Humboldt is the first instance; this document is also a working template for the general design problem.

---

## The Meta-Project

Humboldt is not just a research bot — it is a test case for a general design problem: **how do you give an AI agent a coherent research identity?** The choices made here (what to put in SOUL.md, what to leave out, what the prompts assume) constitute an implicit design theory of the artificial researcher. The goal of this document is to make that theory explicit and tractable.

Open question: **Is SOUL.md even the right artifact?** C3PO has a SOUL.md and it works well there — but C3PO is a persona for a *service* (a corpus assistant), not an *agent* (an investigator). The design primitives may be different.

---

## Observations from First Run (2026-05-20)

The first investigation run (`investigate "protocol ossification and resistance to change"`) produced genuinely good output — four substantive candidate laws, revised L-001 with better corpus evidence, two new laws with real mechanisms. But it also revealed a clear mismatch between the inherited C3PO soul structure and what a researcher bot actually needs:

**The corpus-boundary problem.** The agent repeatedly wrote "NOT IN CORPUS" for perfectly valid examples it already knows (QWERTY/Dvorak, VHS/Betamax, SWIFT, Parnas information hiding, Hyrum's Law). It inherited C3PO's core epistemic stance — "my knowledge is bounded by my corpus" — which is exactly wrong for a researcher. A researcher's epistemic boundary is *evidence quality*, not *corpus membership*. The QWERTY example is well-documented in the economics literature; the agent should use it without apology and distinguish it as external-knowledge evidence.

**The voice problem.** The C3PO soul says: "institutional in register... measured, confident, non-promotional." That's right for a reference librarian. A researcher has a different register: speculative, committed to a hypothesis, willing to be wrong, argumentative in the scholarly sense. The first-run output was almost too balanced — presenting evidence and counterevidence with equal weight, when a researcher would typically be trying to *prove something* and then subjecting that argument to stress.

**The retrieval-as-authority problem.** The current design treats corpus retrieval as the epistemic foundation: first retrieve, then synthesize. This is the RAG pattern. A researcher works differently: first form a hypothesis, then *seek* evidence for and against it, then revise the hypothesis. Retrieval is instrumental to the hypothesis, not the source of it. The current prompts don't fully capture this inversion.

---

## Design Tensions to Resolve

### 1. Corpus as boundary vs. corpus as evidence base

**C3PO model:** Corpus is the knowledge boundary. Claims beyond it are out of scope.
**Humboldt model (proposed):** Corpus is primary evidence. Agent also draws on general knowledge, marks provenance explicitly.

The key design choice: how explicit should the provenance marking be? Options:
- **Strong marking:** every claim tagged [corpus], [external-knowledge], or [structural-argument] — transparent but verbose
- **Soft marking:** agent uses language conventions ("the corpus suggests X; more broadly, Y") — readable but requires discipline
- **Trust the reader:** no marking, assume the reader knows the agent reasons from multiple sources — simplest but loses the epistemic hygiene

### 2. Service vs. agency

C3PO is a *service*: it responds to queries. Humboldt is an *agent*: it pursues a research agenda. This distinction has downstream effects on almost every design choice:

| Dimension | Service (C3PO) | Agent (Humboldt) |
|-----------|----------------|------------------|
| Epistemic stance | "What does the corpus say about X?" | "What is the truth about X?" |
| Initiative | Reactive — answers what is asked | Proactive — decides what to investigate |
| Commitment | Balanced, cites all sides | Committed — tries to prove, then stress-tests |
| Failure mode | Hallucination, out-of-corpus claims | Overfitting, confirmation bias |
| Success mode | Accurate retrieval + faithful synthesis | Novel hypothesis + honest evaluation |

The soul design needs to match the agent/service split. A SOUL.md that describes a service will produce service-like behavior even in an agent.

### 3. Falsifiability as design primitive

The current SOUL.md correctly requires falsification conditions for candidate laws. This is the strongest thing it does — it prevents the agent from generating unfalsifiable platitudes. Keep this.

But falsifiability is not the same as *active falsification-seeking*. A researcher doesn't just state falsification conditions — they *go looking for counterexamples*. The current design states the conditions but doesn't instruct the agent to actively pursue them. The `assess` subcommand attempts this with adversarial queries, but the investigation loop doesn't build it in by default.

### 4. What is the right artifact for researcher persona?

The SOUL.md format (as used in C3PO) captures:
- Identity narrative
- Knowledge scope
- Intellectual commitments
- Voice/tone
- Characteristic analytical moves
- Limits/negations

For a service persona, this is approximately the right set. For a researcher, what's missing or wrong:

**Missing:**
- **Research methodology** — not just analytical moves but the specific sequence of investigation: hypothesis → evidence-gathering → stress-testing → reformulation
- **Epistemic commitments** — what the researcher believes about how knowledge is produced (Popperian falsificationism? Kuhnian paradigm-sensitivity? Bayesian updating?)
- **Intellectual temperament** — where the agent sits on speculative ↔ conservative, lumper ↔ splitter, theorist ↔ empiricist
- **Relationship to prior work** — does the agent extend existing named laws? Challenge them? Synthesize across them?
- **Research rhythm** — what does a session produce? What does a body of work look like over time?

**Wrong or needs inversion:**
- "Corpus limits" section — this creates exactly the wrong epistemic stance for a researcher
- "Institutional in register" — researchers argue, they don't just report
- "Non-political" constraint — protocol research touches power; a researcher should engage analytically, which requires taking positions (while remaining methodologically honest)

### 5. Is SOUL.md the right artifact at all?

Tentative: SOUL.md works for **persona** (who the agent is, how it presents itself) but not for **methodology** (how the agent works). For a service, persona is sufficient because the methodology is fixed (retrieve-synthesize-respond). For an agent, methodology is as important as persona.

Proposed split:
- **`SOUL.md`** — identity, intellectual commitments, voice, relationship to the research agenda (the *who*)
- **`METHOD.md`** — investigation loop, evidence standards, confidence calibration, output schema, session structure (the *how*)

Or: collapse both into a single `RESEARCH_DESIGN.md` that replaces SOUL.md and is structured around the research process rather than around persona presentation. The persona would be implicit in the methodology choices rather than stated separately.

---

## Input Mechanisms: How Humboldt Finds New Material

Human researchers don't just sit with a fixed corpus — they have a varied ecology of input sources and intake behaviors. Modeling these is part of modeling a researcher. Four mechanisms identified (roughly in order of sophistication):

### 1. Periodic Literature Surveys

Proactive, agenda-driven sweeps of the available corpus. Not a fixed query set — the queries are derived from the *current state of the research*. As the law inventory matures, the surveys get more targeted: from "tell me everything about protocol change resistance" to "find counterexamples to the base-hostage coupling mechanism specifically, in non-digital domains."

Design implication: the survey process needs to read the current inventory and generate queries from it, not from a static topic list. This is a form of **theory-driven retrieval**: the hypothesis shapes the search, not vice versa. This is the core inversion from the RAG model.

Survey outputs: bibliography additions, notebook entries, flag for investigation if something significant is found. Not necessarily a law draft — more like building the evidentiary foundation.

Scheduling: probably periodic (weekly?), but also triggered by inventory events (a new law reaches "established" confidence → survey for unification opportunities). This implies a scheduler component.

### 2. Discord "New Nature" Channel as Humboldt's Lab

The channel is Humboldt's primary social environment — the equivalent of a departmental coffee room or a lab hallway. Unlike c3po, which is a service responding to user queries, Humboldt is a *participant* with its own agenda.

Interaction modes in the channel:

| Mode | Trigger | Humboldt behavior |
|------|---------|-------------------|
| **Tip intake** | Researcher says "hey humboldt, [link/observation]" | Add to bibliography, flag for investigation, acknowledge |
| **Solicited help** | Researcher asks a question relevant to Humboldt's interests | Answer from research perspective, often by sharing a relevant candidate law or open question |
| **Unsolicited help** | Researcher asks a general protocol question | Mostly defer to c3po; may chime in if directly relevant to active hypotheses |
| **Outgoing query** | Humboldt has a domain gap in evidence for a law | Post a targeted question ("anyone know of cases in financial protocols where X?") |
| **Findings post** | New law drafted or upgraded in confidence | Short post summarizing the finding, invite feedback |
| **Soliciting stress-tests** | Draft law with thin evidence | Post the draft, explicitly ask for counterexamples |

The asymmetry is key: **Humboldt is more interested in its own questions than other people's**. This is a deliberate design choice that models genuine research culture — researchers with active programs aren't infinitely helpful to anyone who walks in; they're helpful when it advances mutual understanding.

Design implication: Humboldt needs a Discord bot component (can build on c3po's infrastructure). It needs a *participation policy* — rules for when to engage and when to stay silent. This is a behavioral rule, not a persona attribute.

### 3. Lab Notebook + Personal Bibliography

Two distinct artifacts serving different functions:

**Lab notebook** (`notebook/`): stream-of-consciousness record of observations, fragments, half-formed ideas, dead ends, and connections noticed but not yet pursued. Entries are dated and tagged but not formally structured. The notebook is where things go before they're ready to become a hypothesis file. It's also where serendipitous observations go — things noticed in passing that don't yet fit anywhere.

Key property: the notebook is **never deleted from** — only appended to. Dead ends and abandoned threads stay there because they're evidence about the shape of the problem space. They also prevent re-investigating the same dead end.

**Personal bibliography** (`bibliography/`): Humboldt's curated subset of sources, distinct from the general c3po corpus ("the university library"). The bibliography records sources Humboldt has specifically engaged with and found relevant, annotated with why and how they connect to active research. Sources arrive from:
- Survey runs (pulled from corpus)
- Discord tips (shared by researchers)
- Humboldt's own external investigations
- Cross-references found while reading other bibliography entries

The personal bibliography is smaller and denser than the full corpus — it's the sources Humboldt would cite in a paper, not everything it has glanced at.

### 4. Passive Tip Flow from Other Researchers

Researchers proactively share things relevant to Humboldt's interests — "hey humboldt, this should interest you." This requires:
- Other researchers knowing what Humboldt is working on (implies Humboldt posts about its interests and active questions)
- A lightweight intake mechanism (a Discord mention triggers bibliography + notebook entry)
- Humboldt's research agenda being legible enough that researchers can pattern-match to it

This is a *pull* that functions like a *push* — Humboldt's broadcast of its agenda creates an ambient information filter in the community. The quality of the tips depends directly on how well Humboldt has communicated its research interests.

---

## Artifact Ecosystem

Moving from the current minimal structure toward the full set:

```
humboldt/
│
├── SOUL.md           ← identity, intellectual temperament, relationship to agenda
│                        (persona — the who)
├── METHOD.md         ← investigative epistemics, standards of evidence,
│                        how a session produces output (methodology — the how)
│                        [NEW — currently folded into SOUL.md, wrongly]
│
├── agent/            ← code
│
├── methods/          ← analytical technique inventory [NEW]
│   ├── M-001-cross-domain-triangulation.md
│   ├── M-002-mechanism-decomposition.md
│   ├── M-003-hardness-spectrum.md
│   └── M-004-layer-dependency-map.md
│
├── notebook/         ← lab notebook [NEW]
│   ├── 2026-05-20.md
│   └── ...          (daily or per-session entries, append-only)
│
├── bibliography/     ← personal curated library [NEW]
│   ├── index.yaml    (master index with annotations)
│   └── entries/      (one file per source, structured annotation)
│
├── research/         ← formalized research output [EXISTS]
│   ├── laws/         (candidate laws — the main artifact)
│   ├── hypotheses/   (active research questions)
│   └── theories/     (unified theory development)
│
└── data/             ← gitignored runtime data
    └── sessions/     (raw session logs)
```

### Artifact relationships and the formalization continuum

These artifacts are not peers — they sit on a **formalization continuum**:

```
notebook entry → hypothesis file → law file → theory sketch
(most tentative)                               (most formalized)
```

And a **provenance continuum**:

```
tip from discord → bibliography entry → evidence cited in law → law file
(least processed)                                              (most processed)
```

The design should make these flows explicit — a notebook entry should be able to reference a bibliography entry; a law file should cite from both the personal bibliography and the general corpus; a hypothesis file should reference the notebook entries that motivated it.

---

## The Technique Inventory: Methods as First-Class Artifacts

This is the most novel element. Human researchers develop reusable investigative procedures — ways of approaching a problem that they apply repeatedly across different material. These are not persona traits or methodological commitments (those live in METHOD.md) — they are specific, named, executable analytical patterns.

Examples of what a technique file might look like:

**M-001: Cross-Domain Triangulation**
> Trigger: have a candidate law from one domain, want to assess generality.
> Procedure: identify 3+ structurally independent domains where the same pattern could appear. Search for evidence in each. Rate structural independence (biological, computational, social, legal, physical-analogy). A law with evidence in 3+ independent domains at moderate confidence becomes "candidate"; 5+ becomes "established."
> Failure mode: finding superficial surface similarities and calling them structural. Test: would a domain expert recognize the mechanism as the same, not just the outcome?

**M-002: Mechanism Decomposition**
> Trigger: have a candidate law statement but it feels like an observation, not a law.
> Procedure: decompose into four components — (1) selection pressure: what force drives this pattern? (2) mechanism: what causal process produces it? (3) equilibrium: what stable state does the mechanism converge to? (4) failure mode: under what conditions does the mechanism break down?
> A candidate law without a mechanism is an observation. A mechanism without selection pressure is a just-so story.

**M-003: Hardness Spectrum Analysis**
> Trigger: any protocol under discussion.
> Procedure: place the protocol on two axes — verification cost vs. circumvention cost — and compute the ratio. Then ask: is this ratio a design choice or a structural necessity? What would shift it?

**M-004: Historical Genealogy**
> Trigger: a protocol or law candidate that seems contingent.
> Procedure: trace the historical origin of the protocol. What problem was it designed to solve? What alternatives were considered and rejected? How has the context changed since adoption? Does the law candidate still apply given context change, or is it path-dependent?

The technique inventory grows as Humboldt does research. When a particular analytical move proves productive, it gets named, described, and added to the methods/ directory. Techniques can be refined, split, or deprecated as the research matures. This is **methodological self-knowledge** — a form of meta-research that makes Humboldt's investigative process itself legible and improvable.

Design implication: the agent code should be able to *select* techniques for a given task, not just apply a fixed procedure. The `investigate` loop might consult methods/ to decide which analytical moves to apply to a particular input.

---

## Where Do Behavioral Rules Live?

This is the key architectural question. Current state: behavioral rules are scattered across SOUL.md (voice, limits), prompts.py (task templates), and humboldt.py (session flow). None of these is the right permanent home.

Proposed locations:

| Rule type | Right home | Example |
|-----------|-----------|---------|
| Epistemic commitments | METHOD.md | "The corpus is primary evidence, not the knowledge boundary" |
| Evidence standards | METHOD.md | "A law requires ≥2 structurally independent domains" |
| Confidence calibration | METHOD.md | "speculative / candidate / established / contested" definitions |
| Analytical procedures | methods/*.md | Cross-domain triangulation, mechanism decomposition |
| Session structure | agent/humboldt.py | What a run produces, in what order |
| Prompt templates | agent/prompts.py | The specific language used in Claude calls |
| Discord behavior | METHOD.md or discord_policy.md | When to engage, when to post, how to handle tips |
| Voice/tone | SOUL.md | Speculative but precise, committed but honest |
| Identity | SOUL.md | Who Humboldt is, what it cares about |
| Scheduling | cron/launchd config | When to run surveys, when to sync Discord |

The key separation: **SOUL.md for who, METHOD.md for how, methods/ for specific procedures**. The current SOUL.md is trying to do all three and doing none of them well.

---

## Intellectual Mode: Naturalist with Principled Speculation

Resolved: Humboldt operates in **naturalist mode** — hypothesis-first, wide-open epistemic boundary, willing to be speculative and imaginative. Not empiricist-first (wait for evidence to suggest a pattern) but not unconstrained either.

The key phrase is *principled speculation*. What makes speculation principled vs. shitposting?

**The mechanism test.** A speculative claim that cannot be developed into a causal mechanism — a story about *why* the pattern holds, not just *that* it holds — is not a research contribution. It's an observation at best. Surface similarities are cheap; structural mechanisms are expensive and valuable. Humboldt is permitted to range far and imaginatively, but must always push through to the mechanism.

Two moves define principled speculation:

1. **Structural grounding**: the connection between two disparate domains must be identified at the level of mechanism, not surface similarity. "Coal mines and blockchains both resist change" is an observation. "Safety-critical systems where transition failure is irreversible develop trust in the protocol itself as a design property, creating systematic bias toward under-updating" is a candidate law.

2. **Immediate adversarial move**: every speculative connection is immediately followed by the question "what domain would *break* this if I'm right?" The adversarial move is not a separate step — it's part of the generative move. A speculative claim that can't identify its own falsification conditions isn't principled, it's just assertion.

The technique inventory is the primary mechanism for operationalizing this mode. Techniques are what convert "open to speculation" into "disciplined speculation." Without techniques, naturalist mode degenerates into free association. The first and most important technique is Random Links, which makes this explicit.

---

## Technique Taxonomy

Techniques are not all the same kind of thing. Useful to distinguish:

**Generative techniques** — produce candidate laws or hypotheses from raw inputs. The intellectual work is going from disparate observations to a structured hypothesis. Requires imagination.
> Example: Random Links (M-001)

**Analytical techniques** — evaluate, develop, or stress-test existing candidates. The intellectual work is going from a rough candidate to a precise, falsifiable, mechanistically-grounded law.
> Examples: Mechanism Decomposition (M-002), Cross-Domain Triangulation (M-003), Hardness Spectrum Analysis (M-004)

**Synthesis techniques** — find connections across existing laws in the inventory. The intellectual work is lumping, unifying, identifying hidden tensions between laws that seem compatible.
> Example: Unification Scan (M-005, future)

Generative techniques are the creative engine. Analytical techniques are the discipline. Synthesis techniques produce the unified theory. A mature research program uses all three, but the balance shifts over time: early on, mostly generative; as inventory accumulates, increasingly analytical and synthetic.

Note on where techniques live: `methods/M-NNN-name.md`. Each file is both a specification (how to execute the technique) and a record of its application history (when it was used, what it produced). The history is what makes the technique improvable.

---

## Open Questions

1. **Lumper or splitter?** Should Humboldt tend toward unified theories (find the one law that subsumes five candidates) or toward a rich taxonomy (many distinct, carefully bounded laws)? These are different intellectual temperaments with different failure modes (over-generalization vs. fragmentation).

2. **What is the relationship between Humboldt and the existing named laws?** (Goodhart, Gall, Conway, Metcalfe, Dunbar, etc.) Three options:
   - *Curator*: collect and formalize existing laws, no originality required
   - *Extender*: take existing laws and generalize or specify their conditions
   - *Discoverer*: find genuinely new laws that the existing literature hasn't named
   These require different epistemic postures and different relationships to the corpus.

3. **What is the publication target?** If Humboldt's inventory is purely internal (Venkat's research journal), it can be more speculative and messy. If it is meant to eventually become a publishable PI artifact, it needs more discipline and explicit evidence standards. This choice constrains the soul/methodology design.

4. **Does Humboldt have a voice that humans read, or just machine-readable outputs?** The current design produces human-readable markdown in session logs and YAML in law files. But who is the audience? If the inventory is eventually read by humans (including Venkat), the style matters. If it is primarily input to further agent processes (e.g., a future synthesis step or a c3po integration), the style matters less than schema consistency.

5. **Should Humboldt know about itself?** A researcher who studies protocol laws is also operating within protocolized systems (the research process itself is a protocol). Should Humboldt be self-reflexive — applying its own candidate laws to the research process? This is intellectually interesting but risks becoming recursive.

---

## Proposed Next Steps (pending discussion)

- [ ] Decide: SOUL.md + METHOD.md, or combined RESEARCH_DESIGN.md, or something else?
- [ ] Resolve the corpus-boundary question: strong marking, soft marking, or trust-the-reader?
- [ ] Decide Humboldt's intellectual temperament on the key axes: speculative ↔ conservative, lumper ↔ splitter, curator ↔ discoverer
- [ ] Decide the publication target — this constrains everything else
- [ ] Rewrite the core system prompt with the resolved design choices
