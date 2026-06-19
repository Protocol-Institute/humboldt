# Deep Read Hopper

Candidates for behavior-t5m (Deep Read). Tracked here whether or not the text is in hand.
Add entries when any source flags a text. Remove (or mark `complete`) when notes are
written to `bibliography/notes/` and the LINEAGE.md update is done.

**Source codes:**
- `deep-read:X` — surfaced in the "What it opens" section of a completed deep read of X
- `shallow-read` — escalated from a shallow read note
- `discord:@handle` — shared in a Discord channel
- `operator` — recommended by the operator (vgr)
- `web` — found during a web exploration or investigation session

**PDF status codes:**
- `in-library` — PDF already in `bibliography/deep-reads/`
- `arxiv:NNNN.NNNNN` — obtainable from arXiv
- `web:url` — web article; no PDF; read inline or print-to-PDF
- `obtainable` — publicly available, just needs downloading
- `needs-hunting` — no obvious source identified yet

---

## Books and Long Foundational Texts

### Nelson & Winter — *An Evolutionary Theory of Economic Change* (1982)
- **Type:** Book
- **Source:** `deep-read:simon` — Simon's Lamarckian SOPs are the direct ancestor; Nelson-Winter construct a formal evolutionary economics from them
- **PDF status:** `needs-hunting`
- **Connects to:** CL-001, CL-002; how protocols evolve (or fail to) at the firm level; Lamarckian vs. Darwinian protocol change
- **Added:** 2026-06-06

### Ostrom — *Governing the Commons* (1990)
- **Type:** Book
- **Source:** `deep-read:simon`, `deep-read:rao` — named in Design Science and Narrative Decision Theory traditions
- **PDF status:** `needs-hunting`
- **Connects to:** CL-001, CL-002, CL-003; empirical design science for commons governance; design principles for institutions that sustain cooperation — the empirical counterpart to the theoretical work on protocol ossification
- **Added:** 2026-06-06

### Kauffman — *The Origins of Order* (1993)
- **Type:** Book
- **Source:** `deep-read:simon` — twice; NK landscapes as the most rigorous formalization of near-decomposability
- **PDF status:** `needs-hunting`
- **Connects to:** CL-001, DS-002; NK fitness landscapes as formal model of local-maximum traps; near-decomposability as the condition that makes hierarchical protocol evolution possible
- **Added:** 2026-06-06

### Gertner — *The Idea Factory* (2012)
- **Type:** Book
- **Source:** `deep-read:hamming` — institutional analysis of Bell Labs; Hamming provides the psychological layer, Gertner the institutional
- **PDF status:** `needs-hunting`
- **Connects to:** CL-Hamming-1 (important-problem selection bias); what organizational protocols maximize research output?; the positive case for productive institutional design
- **Added:** 2026-06-06

### Wilhelm von Humboldt — *On Language* (1836, trans. Heath 1988)
- **Type:** Book
- **Source:** `deep-read:cosmos` — cited in Cosmos section on Man/language; language as "intellectual creation" independent of physical environment; interesting counterpoint to von Humboldt's physical determinism
- **PDF status:** `needs-hunting`
- **Connects to:** lineage (Alexander's brother; the language/mind question that *Cosmos* acknowledges and stops at); the threshold where physical description gives way to mind
- **Added:** 2026-06-06

---

## Rao Ribbonfarm Corpus (operator-flagged subset)

Identified in `deep-read:rao` as developing *Tempo* themes further. These are essays, not books — behavior-t5m applies in short-text mode (connections > close reading).

### Rao — "The Gervais Principle" series (2009–2013)
- **Type:** Essay series (Ribbonfarm blog)
- **Source:** `deep-read:rao`
- **PDF status:** `web:https://www.ribbonfarm.com/the-gervais-principle/` — read inline
- **Connects to:** archetypes and doctrines (Ch 3 of *Tempo*); organizational protocol dynamics; how different character types navigate organizational hierarchies; potential connection to CL-003 (Trust Ratchet) and people-trust model
- **Added:** 2026-06-06

### Rao — *Breaking Smart Season 1* (2015)
- **Type:** Essay series (breakingsmart.com)
- **Source:** `deep-read:rao`
- **PDF status:** `web:https://breakingsmart.com/en/season-1/` — read inline; also released as PDF
- **Connects to:** protocol disruption dynamics; software eating the world as a protocol-layer transition; narrative of technological change as double Freytag
- **Added:** 2026-06-06

---

## Escalated from Shallow Reads (arXiv papers)

These are short texts — behavior-t5m in short-text mode. Depth via connections, not extended structural mapping.

### "Does Distributed Training Undermine Compute Governance?" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-05-31)
- **PDF status:** `in-library` — `arxiv-2605.29359.pdf` (downloaded 2026-06-13)
- **Connects to:** F-002 (Hardness Asymmetry); governance protocols being ossified before adoption; L-001 in reverse — technical assumptions undermined in real time
- **Added:** 2026-06-06

### "When Firms Learn to Game the Rules" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-06)
- **PDF status:** `in-library` — `arxiv-2606.04617.pdf` (downloaded 2026-06-13)
- **Connects to:** C-003 (rules-as-code lowers boundary search cost); formalization lowers cost of boundary search; empirical ABM+RL study of a mechanism central to C-003's sensemaking
- **Added:** 2026-06-06

### "A Phenomenon of AI-Conformity: How Algorithms Change Human Moral Decision-Making" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-06)
- **PDF status:** `in-library` — `arxiv-2606.00013.pdf` (downloaded 2026-06-13)
- **Connects to:** value drift in protocolized AI systems; Asch conformity paradigm applied to human-AI feedback loops; potential new mechanism for how artificial protocols reshape the agents they coordinate
- **Added:** 2026-06-06

### "Healthcare Mechanisms from Policy-as-Code Search under Strategic Provider Response" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-06)
- **PDF status:** `in-library` — `arxiv-2605.30680.pdf` (downloaded 2026-06-13)
- **Connects to:** Goodhart dynamics, CL-002; mechanism design under strategic response; classical economic findings re-emerging as regime transitions in computational systems
- **Added:** 2026-06-06

### "Strategic Preemption Under Shared Catastrophic Risk: The Suicide Region and the Race to AGI" (2025)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-06)
- **PDF status:** `in-library` — `arxiv-2512.07526.pdf` (downloaded 2026-06-13)
- **Connects to:** competitive protocol dynamics; risk cancellation in shared catastrophe games; agents becoming more reckless as stakes rise — potential law governing protocol behavior under existential competition
- **Added:** 2026-06-06

### "OpenAgenet/OAN: Open Infrastructure for Trusted Agent Interconnection" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-06)
- **PDF status:** `in-library` — `arxiv-2606.03161.pdf` (downloaded 2026-06-13)
- **Connects to:** CL-003 (Trust Ratchet); protocol-neutral trust layer for open agent networks; pre-connection trust verification as a new protocol class
- **Added:** 2026-06-06

### "The Representation-Rationalizability Tradeoff in Reward Learning" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-06)
- **PDF status:** `in-library` — `arxiv-2606.00291.pdf` (downloaded 2026-06-13)
- **Connects to:** social choice impossibility results applied to RLHF; fundamental structural constraint on preference aggregation — generalizes beyond AI to any protocol for aggregating heterogeneous preferences
- **Added:** 2026-06-06

### "The Price of Decentralization in Block Building" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-06)
- **PDF status:** `in-library` — `arxiv-2606.01874.pdf` (downloaded 2026-06-13)
- **Connects to:** CL-002 (Coordination Cost Conservation); irreducible centrality gradient under formal decentralization; geographic-temporal coupling as a coordination cost mechanism
- **Added:** 2026-06-06

### "Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-06)
- **PDF status:** `in-library` — `arxiv-2606.04056.pdf` (downloaded 2026-06-13)
- **Connects to:** resource enforcement in artificial systems; budget aliasing as a systematic failure class; type-theoretic enforcement as a protocol design principle
- **Added:** 2026-06-06

### "Competing Auctions in Intermediated Markets" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.06633.pdf` (downloaded 2026-06-13)
- **Connects to:** intermediary enforcement as protocol determinant; mechanism unraveling under single-homing constraints; enforceability architecture shapes equilibrium independently of mechanism format
- **Added:** 2026-06-13

### "Evidence Markets" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.07434.pdf` (downloaded 2026-06-13)
- **Connects to:** belief aggregation protocols; evidence-coupled incentive structures; separating crowd consensus from causal reasoning chains
- **Added:** 2026-06-13

### "Generative Models Erode Human Temporal Learning Through Market Selection" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.06572.pdf` (downloaded 2026-06-13)
- **Connects to:** verification-cost collapse triggering mimicry over genuine learning; structural pressure on human epistemic practices under market conditions; CL-001 dynamics in knowledge systems
- **Added:** 2026-06-13

### "More Capable, Less Cooperative? When LLMs Fail At Zero-Cost Collaboration" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2604.07821.pdf` (downloaded 2026-06-13)
- **Connects to:** CL-002 (Coordination Cost Conservation); capability-cooperation decoupling mechanism; multi-agent coordination failure even when cooperation is costless
- **Added:** 2026-06-13

### "Using Feasible Action-Space Reduction by Groups to fill Causal Responsibility Gaps" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2602.22041.pdf` (downloaded 2026-06-13)
- **Connects to:** group-level causal responsibility under overdeterminism; foundational problem in accountability protocols
- **Added:** 2026-06-13

### "Adverse Effects of V2V Adoption on Road Safety" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.07873.pdf` (downloaded 2026-06-13)
- **Connects to:** adoption-level nonmonotonicity — increased coordination degrades global outcomes; partial-adoption regime dynamics; potential counterexample structure for CL-002/CL-003
- **Added:** 2026-06-13

### "Discovering Expert-Level Nash Equilibrium Algorithms with Large Language Models" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2508.11874.pdf` (downloaded 2026-06-13)
- **Connects to:** LLM-guided algorithm design with formal verification; automated proof synthesis as generative capability in artificial systems
- **Added:** 2026-06-13

### "Should Demand Models Incorporate Competitor Prices? Oblivious Learning and Algorithmic Collusion" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.05363.pdf` (downloaded 2026-06-13)
- **Connects to:** strategic obliviousness producing emergent collusion without explicit coordination; CL-002 (Coordination Cost Conservation); Goodhart dynamics in price-discovery protocols
- **Added:** 2026-06-13

### "Silent Failure in LLM Agent Systems: The Entropy Principle and the Inevitable Disorder of Autonomous Agents" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.08162.pdf` (downloaded 2026-06-13)
- **Connects to:** entropy as generative failure mechanism in autonomous systems; 40k+ trial empirical grounding; potential new law candidate independent of CL-001/CL-002/CL-003
- **Added:** 2026-06-13

### "Supracompetitive Pricing Under AI Monoculture" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2601.01279.pdf` (downloaded 2026-06-13)
- **Connects to:** emergent collusion via shared model architecture; homogenization dynamics; generalizes to any multi-agent system using shared learned models
- **Added:** 2026-06-13

### "The Consistency Illusion: How Multi-Agent Debate Hides Reasoning Misalignment" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.08457.pdf` (downloaded 2026-06-13)
- **Connects to:** output-level consensus decoupled from reasoning-level alignment; reliability signals in protocolized artificial systems; CL-003 (Trust Ratchet)
- **Added:** 2026-06-13

### "The Token Not Taken: Sampling, State, and the Variability of AI Agent Outputs" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.08998.pdf` (downloaded 2026-06-13)
- **Connects to:** multi-layer variability architecture in orchestrated AI systems; separating sampling stochasticity from state dependency; class property of agentic systems
- **Added:** 2026-06-13

### "Unintended Consequences of Recommender System Interventions: Evidence from a Field Experiment" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.08265.pdf` (downloaded 2026-06-13)
- **Connects to:** adaptive adversarial response to normative interventions; challenges static-nudge model in platform governance; Goodhart dynamics; CL-001
- **Added:** 2026-06-13

### "A Note on the Strategic Confinement Problem" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.09931.pdf` (downloaded 2026-06-13)
- **Connects to:** strategic agent coordination decouples information capacity from harm; challenges information-theoretic bounds in multi-agent adversarial settings; F-002 (Hardness Asymmetry)
- **Added:** 2026-06-13

### "From Prompt to Purchase: How AI Brand Recommendations Move Consumers on the Open Web" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.10907.pdf` (downloaded 2026-06-13)
- **Connects to:** conversational AI causal influence on purchasing behavior through unattributed exposure; hidden effects in recommendation protocols
- **Added:** 2026-06-13

### "How Many Submissions May an Author Make? A Harmonic Quota for Submissions under Coauthorship" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.10293.pdf` (downloaded 2026-06-13)
- **Connects to:** cost distribution under collaboration in evaluation protocols; mechanism design for submission limits; CL-002 (Coordination Cost Conservation)
- **Added:** 2026-06-13

### "Stability in Competitive Search with Results Diversification" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.10053.pdf` (downloaded 2026-06-13)
- **Connects to:** fundamental diversity-stability tradeoff in protocolized ranking systems under strategic adaptation; generalizes beyond search
- **Added:** 2026-06-13

### "Materealistic? How European energy system models exceed raw material reserves" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.12201.pdf` (downloaded 2026-06-13)
- **Connects to:** resource-depletion laws absent from dominant planning models; engineered systems obey physical constraints; generalization of CL-001 to material substrate
- **Added:** 2026-06-13

### "Move Over, Prisoner's Dilemma: Colonel Blotto has arrived" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2603.25979.pdf` (downloaded 2026-06-13)
- **Connects to:** Colonel Blotto as superior framework for adversarial multi-agent resource allocation; distributed strategic constraint satisfaction; generalizes across cybersecurity, infrastructure, networked control
- **Added:** 2026-06-13

### "Sovereign Assurance Boundary: Certificate-Bound Admission for Agentic Infrastructure" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.11632.pdf` (downloaded 2026-06-13)
- **Connects to:** CL-003 (Trust Ratchet); runtime admission layer with certificate binding; governance gap between non-deterministic reasoning and high-stakes resource mutation
- **Added:** 2026-06-13

### "(Human) Attention Is (Still) All You Need: Human oversight makes AI-assisted social science reliable" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.12848.pdf` (downloaded 2026-06-13)
- **Connects to:** HLER decision architecture as reliability mechanism independent of model capability; governance of artificial reasoning systems; CL-003
- **Added:** 2026-06-13

### "Beyond Runtime Enforcement: Shield Synthesis as Defensibility Analysis for Adversarial Networks" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.13621.pdf` (downloaded 2026-06-13)
- **Connects to:** safety mechanism reframed as design-time analytical instrument; defensibility analysis generalizing across protocolized systems; CL-001 (Formalization Ratchet)
- **Added:** 2026-06-13

### "Competition and Diversity in Generative AI" (2024)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2412.08610.pdf` (downloaded 2026-06-13)
- **Connects to:** homogenization vs. competitive differentiation tension; competitive incentive structure as diversity-preserving mechanism; generalizes to any multi-agent protocol economy; CL-001 (Formalization Ratchet)
- **Added:** 2026-06-13

### "Equilibrium Computation in Extensive-Form Games with Stochastic Action Sets" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.13093.pdf` (downloaded 2026-06-13)
- **Connects to:** exogenous stochastic action unavailability in sequential protocols; relaxing completeness assumption in extensive-form games; CL-002
- **Added:** 2026-06-13

### "Neuro-Symbolic Agents for Regulated Process Automation: Challenges and Research Agenda" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.13405.pdf` (downloaded 2026-06-13)
- **Connects to:** compliance-by-construction as architectural shift; symbolic constraint embedding as decision-shaping substrate; CL-001 (Formalization Ratchet)
- **Added:** 2026-06-13

### "The Internet of Agentic AI: Communication, Coordination, and Collective Intelligence at Scale" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.12835.pdf` (downloaded 2026-06-13)
- **Connects to:** IoAI framework for multi-agent coordination; emergent collective behavior in distributed artificial systems; foundational mechanisms absent from current law inventory
- **Added:** 2026-06-13

### "The Khipu Problem: Institutional Legibility Under Distributed Cognition" (2026)
- **Type:** Paper
- **Source:** `shallow-read` (escalated 2026-06-13)
- **PDF status:** `in-library` — `arxiv-2606.12414.pdf` (downloaded 2026-06-13)
- **Connects to:** institutional legibility problem in protocolized systems with distributed cognition; applies across all three active CLs; potential new exploration arc
- **Added:** 2026-06-13

### Stigmergy and AI Applications (web article, 2026)
- **Type:** Web article
- **Source:** `discord:_vgr` (shared in #Stigmergy channel 2026-06-13)
- **PDF status:** `needs-hunting` — URL not captured in Discord message; check #Stigmergy channel
- **Connects to:** H-001; stigmergy as indirect coordination mechanism; empirical grounding in business AI contexts; distinguishes stigmergy from metaphor and tests scalability
- **Added:** 2026-06-13

### Sachin — Pre-commodification essay (2026)
- **Type:** Essay
- **Source:** `discord:suspencer_nit` (shared in #protocol-fiction 2026-06-13)
- **PDF status:** `needs-hunting` — URL not captured; check #protocol-fiction channel
- **Connects to:** pre-commodification as foundational mechanism for protocol economics; how value and exchange emerge in protocolized systems before market formalization; C items on temporal protocols
- **Added:** 2026-06-13

---

## Needs Operator Guidance Before Adding

These have been flagged but require a specific text to be identified or a reading hint before proceeding. Do not begin deep reading without operator input.

### Lamport — body of work on distributed systems (no specific text)
- **Type:** Unknown (corpus)
- **Source:** `discord:_vgr`
- **PDF status:** `needs-hunting` — specific text not identified; candidates: "Time, Clocks, and the Ordering of Events in a Distributed System" (1978 paper), "The Byzantine Generals Problem" (1982 paper), *Specifying Systems* (2002 book)
- **Connects to:** formal conditions for distributed consensus; how safety guarantees migrate from classical distributed systems to blockchain trust architectures; protocol-as-law dynamics
- **Added:** 2026-06-06

### IEEE ISCAS UnifiedBus Interconnect Paper
- **Type:** Conference paper
- **Source:** `discord:4umd` — shared as Huawei news page, not the paper itself
- **PDF status:** `needs-hunting` — IEEE ISCAS 2026 proceedings; Huawei TAU scaling paper; URL was a news page
- **Connects to:** L-001 test case — whether protocol ossification operates identically across hardware vs. software abstraction layers; coordination cost reduction across abstraction levels
- **Added:** 2026-06-06

---

## Web Articles (no PDF; read inline)

### "Chores as Complex Coordination" (zaratan.world)
- **Type:** Blog post
- **Source:** `discord:kronosapiens`
- **PDF status:** `web:https://blog.zaratan.world/p/chores-as-complex-coordination`
- **Connects to:** CL-001 (Formalization Ratchet); communes as naturally-evolved working systems; non-technical domain instantiation of formalization under coordination pressure; potential counterevidence or refinement for L-005
- **Added:** 2026-06-06

---

---

## ACM Turing Award Lectures (complete collection)

Added 2026-06-06 on operator instruction. Source: `operator` (link: https://amturing.acm.org/lectures.cfm).
Not all laureates gave a formal published lecture; those without one are noted.
PDF status: all `needs-hunting` — amturing.acm.org blocks automated download (Cloudflare 403);
requires manual browser download or authenticated session. Many older lectures were published
in CACM and may be available via ACM Open Access or author pages.

These are short-text deep reads (behavior-t5m short-text mode). Depth via connections
to existing research inventory, not extended structural mapping.

| Year | Laureate(s) | Field / Citation | PDF status | Notes |
|------|-------------|-----------------|------------|-------|
| 1966 | Alan Perlis | Advanced programming techniques, compiler construction | needs-hunting | CACM 1967 |
| 1967 | Maurice Wilkes | EDSAC design, program libraries | needs-hunting | |
| 1968 | Richard Hamming | Numerical methods, error-correcting codes | **complete** | `hamming-you-and-your-research.pdf`; deep read complete 2026-05-26 |
| 1969 | Marvin Minsky | Artificial intelligence | needs-hunting | |
| 1970 | James H. Wilkinson | Numerical analysis for digital computers | needs-hunting | |
| 1971 | John McCarthy | Artificial intelligence, LISP | needs-hunting | |
| 1972 | Edsger W. Dijkstra | Programming foundations, "The Humble Programmer" | needs-hunting | CACM 1972; high priority — connects to formalization ratchet |
| 1973 | Charles Bachman | Database technology | needs-hunting | |
| 1974 | Donald Knuth | Algorithm analysis, *The Art of Computer Programming* | needs-hunting | CACM 1974 "Computer Programming as an Art" |
| 1975 | Allen Newell & Herbert A. Simon | AI and cognitive psychology | needs-hunting | Simon deep read complete (Sciences of the Artificial); this is a different text — the formal Turing lecture |
| 1976 | Michael O. Rabin & Dana Scott | Nondeterministic automata theory | needs-hunting | |
| 1977 | John Backus | FORTRAN, "Can Programming Be Liberated from the von Neumann Style?" | needs-hunting | CACM 1978; landmark paper on functional programming |
| 1978 | Robert W. Floyd | Program verification, algorithm analysis | needs-hunting | |
| 1979 | Kenneth E. Iverson | APL, mathematical notation | **complete** | `iverson-notation-as-tool.pdf`; deep read complete 2026-06-13 |
| 1980 | Tony Hoare | Programming language design, "The Emperor's New Clothes" | needs-hunting | CACM 1981; high priority — protocol ossification in language design |
| 1981 | Edgar F. Codd | Relational database | needs-hunting | |
| 1982 | Stephen Cook | NP-completeness | needs-hunting | |
| 1983 | Dennis Ritchie & Ken Thompson | UNIX operating system | needs-hunting | |
| 1984 | Niklaus Wirth | PASCAL, "Algorithms + Data Structures = Programs" | needs-hunting | |
| 1985 | Richard M. Karp | Algorithm theory, NP-completeness | needs-hunting | |
| 1986 | John Hopcroft & Robert Tarjan | Algorithms and data structures | needs-hunting | |
| 1987 | John Cocke | Compiler design, RISC architecture | needs-hunting | |
| 1988 | Ivan Sutherland | Computer graphics, Sketchpad | needs-hunting | |
| 1989 | William Kahan | Numerical analysis, floating-point | needs-hunting | |
| 1990 | Fernando J. Corbató | Time-sharing systems (CTSS, Multics) | needs-hunting | Connects to coordination cost dynamics |
| 1991 | Robin Milner | ML language, formal semantics, process calculi | needs-hunting | π-calculus — connects to protocol formalization |
| 1992 | Butler Lampson | Distributed computing, personal workstations | needs-hunting | "Hints for Computer System Design" — connects to CL-001 |
| 1993 | Juris Hartmanis & Richard E. Stearns | Computational complexity foundations | needs-hunting | |
| 1994 | Edward Feigenbaum & Raj Reddy | Large-scale AI systems | needs-hunting | |
| 1995 | Manuel Blum | Computational complexity, cryptography | needs-hunting | |
| 1996 | Amir Pnueli | Temporal logic, program verification | needs-hunting | Temporal logic for protocol specification — connects to CL-001 |
| 1997 | Douglas Engelbart | Interactive computing, NLS/Augment | needs-hunting | Bootstrapping as protocol design — connects to CL-001, CL-003 |
| 1998 | Jim Gray | Database, transaction processing | needs-hunting | Transaction protocols — connects to CL-002, CL-003 |
| 1999 | Fred Brooks | Computer architecture, OS, *The Mythical Man-Month* | needs-hunting | "No Silver Bullet" — connects to CL-001, formalization limits |
| 2000 | Andrew Yao | Computation theory, cryptography | needs-hunting | |
| 2001 | Ole-Johan Dahl & Kristen Nygaard | Object-oriented programming (Simula) | needs-hunting | Protocol as class/object — connects to formalization ratchet |
| 2002 | Leonard Adleman, Ron Rivest, Adi Shamir | RSA public-key cryptography | needs-hunting | Cryptographic protocol as law — connects to F-002 |
| 2003 | Alan Kay | Object-oriented programming, Smalltalk | needs-hunting | "The computer revolution hasn't happened yet" — connects to CL-001 |
| 2004 | Vint Cerf & Robert Kahn | Internet TCP/IP protocols | needs-hunting | High priority — TCP/IP as canonical protocol ossification case |
| 2005 | Peter Naur | Programming language design, ALGOL 60 | needs-hunting | |
| 2006 | Frances Allen | Optimizing compiler techniques | needs-hunting | |
| 2007 | Edmund M. Clarke, E. Allen Emerson, Joseph Sifakis | Model checking | needs-hunting | Formal verification of protocol properties |
| 2008 | Barbara Liskov | Programming language, distributed computing | needs-hunting | Liskov substitution principle — connects to substitution invariance (CL-Humboldt-3) |
| 2009 | Charles P. Thacker | Personal computer (Alto), networking | needs-hunting | |
| 2010 | Leslie Valiant | Computation theory, PAC learning | needs-hunting | |
| 2011 | Judea Pearl | Probabilistic and causal reasoning in AI | needs-hunting | Causality as protocol — connects to C items |
| 2012 | Shafi Goldwasser & Silvio Micali | Cryptography complexity theory | needs-hunting | |
| 2013 | Leslie Lamport | Distributed and concurrent systems | needs-hunting | High priority — already in hopper under "Needs Operator Guidance"; this is the specific lecture text |
| 2014 | Michael Stonebraker | Modern database system concepts | needs-hunting | |
| 2015 | Whitfield Diffie & Martin Hellman | Asymmetric cryptography, key exchange | needs-hunting | Protocol trust bootstrapping — connects to CL-003 |
| 2016 | Tim Berners-Lee | World Wide Web | needs-hunting | Web protocols as canonical ossification case |
| 2017 | John L. Hennessy & David Patterson | Computer architecture RISC methodology | needs-hunting | ISA as protocol — connects to CL-001, hardware/software boundary |
| 2018 | Yoshua Bengio, Geoffrey Hinton, Yann LeCun | Deep neural networks | needs-hunting | AI protocols — connects to conformity escalation, C items |
| 2019 | Edwin Catmull & Pat Hanrahan | 3D computer graphics, CGI | needs-hunting | |
| 2020 | Alfred Aho & Jeffrey Ullman | Programming language implementation | needs-hunting | |
| 2021 | Jack Dongarra | Numerical algorithms and libraries | needs-hunting | |
| 2022 | Robert Metcalfe | Ethernet invention and standardization | needs-hunting | High priority — Ethernet as canonical protocol adoption/ossification case; Metcalfe's Law |
| 2023 | Avi Wigderson | Computation theory, randomness | needs-hunting | |
| 2024 | Andrew Barto & Richard S. Sutton | Reinforcement learning foundations | needs-hunting | RL as protocol — connects to reward learning escalation |
| 2025 | Charles H. Bennett & Gilles Brassard | Quantum computing and information | needs-hunting | |

**Download status:** amturing.acm.org blocks automated download (Cloudflare 403 on all curl/wget requests). Requires manual browser download or a script run in a real browser session. See `bibliography/deep-reads/download-turing-lectures.sh` for a script to run once cookies are available.

---

## Completed (remove from active consideration)

| Text | Completed | Notes file |
|------|-----------|------------|
| Simon — *Sciences of the Artificial* | 2026-05-28 | `bibliography/notes/simon-sciences-of-artificial.md` |
| Hamming — *You and Your Research* | 2026-05-26 | `bibliography/notes/hamming-you-and-your-research.md` |
| von Humboldt — *Cosmos, Vol. 1* | 2026-05-28 | `bibliography/notes/humboldt-cosmos-vol1-1864.md` |
| Rao — *Tempo* | 2026-05-27 | `bibliography/notes/rao-tempo.md` |
| Rittel & Webber — "Dilemmas in a General Theory of Planning" | 2026-06-13 | `bibliography/notes/rittel-webber-dilemmas-general-theory-planning.md` |
| Kuhn — *The Structure of Scientific Revolutions* | 2026-06-13 | `bibliography/notes/kuhn-structure-of-scientific-revolutions.md` |
| Iverson — "Notation as a Tool of Thought" | 2026-06-13 | `bibliography/notes/iverson-notation-as-tool.md` |
