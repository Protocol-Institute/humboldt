# Reading Notes: Hamming, "You and Your Research" (1986)

> **⚠ Pre-revision notes (law-hunting mode).** These notes were written under the
> original M-003 format, which organized reads around law extraction. They are preserved
> and will be merged with a new gestalt-first pass when this text is re-read.
> Do not treat as a complete deep read in the revised sense.

**Status:** COMPLETE (single-session read, 2026-05-26)

---

## Bibliographic Info

- **Author:** Richard W. Hamming (1915–1998)
- **Source:** Talk at Bellcore, 7 March 1986. Published by Stripe Press (this edition). Also appears as the final chapter of *The Art of Doing Science and Engineering: Learning to Learn* (1996).
- **Format:** Short talk, ~14 pages of text (pp. 8–17 in this edition) + biography (pp. 18–22)
- **Note:** This is a summary of Hamming's 29-chapter course at the Naval Postgraduate School. The earlier chapters expand the material; this talk is the distillation.

---

## Selection Rationale

M-004 (reading prioritization) — Hamming was added to the library as a short document (~30 min read) flagged for evaluation against active hypotheses. Selection outcome: relevant to Humboldt's research *methodology* (how to do research) as much as to the research *object* (what protocols are). It should be read as both: it contains empirical claims about research productivity that generate candidate laws, and it is a model for how Humboldt should operate.

---

## Structural Map

Hamming's argument is not linear — it is a cumulative assembly of traits and practices. The structure is:

1. **Framing:** This is about doing significant work, not just career success. The message: (a) it is worth trying to accomplish high goals, and (b) it is worth setting high goals.
2. **Psychological objections disposed of:** luck, IQ, special brains — all addressed empirically.
3. **Core traits enumerated:** Working on important problems; confidence/courage; desire for excellence / vision; drive; tolerance of ambiguity.
4. **Practices enumerated:** The 10-20 problem portfolio; Friday afternoon time for big questions; problem inversion; selling ideas; open vs. closed door.
5. **Closing:** Style is the essence — *how* you work is what matters. The examined life.

The structural move is: dispose of excuses → identify traits → identify practices → summarize as "style."

---

## Core Claim

**The essence of great research is "style"** — not topic, not talent, not luck, but the way you approach your work. Style includes: choosing important problems, maintaining a portfolio of open questions, regularly interrogating the big picture, inverting stuck problems, tolerating ambiguity, and selling ideas clearly.

The corollary: almost all the barriers to doing great work are psychological or methodological, not intellectual. The variability that looks like ability is, below the surface, mostly preparation and approach.

---

## Vocabulary

- **style** — Hamming's master term; how you do things, not what things you do; "It ain't what you do, it's the way that you do it"
- **important problems** — problems where there is both inherent importance *and* a possible line of attack; importance alone is insufficient (anti-gravity, teleportation: important but no attack vector)
- **10-20 problem portfolio** — the set of significant open problems a great researcher keeps active in the back of their mind, waiting for a clue
- **drive** — sustained directed effort over many years; Tukey's compound interest formulation: ~6%/day extra effort over a lifetime more than doubles lifetime output
- **drunken sailor** — Hamming's image for a researcher without a vision; each step is independent, net progress = sqrt(N); with a goal, steps are directed, progress = N
- **tolerance of ambiguity** — the ability to simultaneously believe your field is the best and that there is much room for improvement; a *necessary* trait for producing significant improvements
- **problem inversion** — treating a constraint as a feature or substituting a structurally equivalent but representationally different goal; turns a blocked problem into a tractable one
- **Friday afternoons** — Hamming's practice of regular protected time for "great thoughts" — asking where computing was heading, what computers' natural role was; the mechanism for staying oriented to the big picture rather than drowning in detail
- **selling ideas** — three forms: formal presentations, written reports, informal presentations; necessary because good ideas do not win automatically; "new ideas are automatically resisted by the establishment"
- **open door / closed door** — the tradeoff between short-term productivity (closed: more work done per year) and long-term orientation (open: work on right problems); Hamming's observation is a correlation, not a proof; he suspects they reinforce each other

---

## Analytical Moves

**Move A — Empirical disposal of psychological excuses.** Hamming addresses luck, IQ, and ability by looking at observed distributions. If it were mainly luck, great things should not be done repeatedly by the same people — but they are (Shannon). IQ matters less than it appears: Bill Pfann example (ability comes in many forms; below the surface there are many common elements).

**Move B — Decomposing success into traits and practices.** Rather than asserting "talent," Hamming identifies specific, learnable traits (confidence, drive, tolerance of ambiguity) and specific, adoptable practices (10-20 problem portfolio, Friday afternoons, problem inversion). This is methodologically important: the decomposition makes success reproducible rather than mysterious.

**Move C — The directed-walk argument.** Without vision: steps cancel, progress = sqrt(N). With vision and goal of excellence: steps are directed, progress = N. Over a lifetime, the difference is enormous. This is a formal argument (random walk vs. directed walk) embedded in an empirical claim.

**Move D — The importance/attack-vector distinction.** A problem is important partly because there is a possible attack on it. This decouples importance (a property of the problem's domain relevance) from tractability (a property of the current state of knowledge). Hamming recommends working on problems that score high on both. Three physics problems (anti-gravity, teleportation, time travel) fail on tractability; they are seldom worked on despite their importance.

**Move E — Problem inversion.** When stuck, inverting the problem often unlocks movement. Two examples: (1) programmer shortage → machine-generated programs → a frontier of computer science; (2) computing answers to a military integration problem → realizing he was demonstrating digital superiority over analog → reformulated and published "Hamming's method." The move is: recast the problem so a constraint becomes an asset or the goal becomes a different (structurally equivalent) goal.

**Move F — The compound interest argument for drive.** One extra hour per day (6% extra effort), compounded over a lifetime, more than doubles lifetime output. The marginal cost of the extra hour is low; the cumulative effect is enormous. This is the reason drive matters more than talent at long timescales.

**Move G — The ambiguity tolerance argument.** Too much belief in the current approach → can't see chances for significant improvements. Too little belief → only small improvements (2%, 5%, 10%), if anything. The productive zone requires holding both belief and skepticism simultaneously. Hamming explicitly says he does not know how to teach this trait.

**Move H — Style as the organizing concept.** The closing move: coding theory, filter theory, simulation — these topics are not the content of the course. The content is style — a way of thinking that can be applied to any topic. This is why the book/talk is domain-agnostic. Style is portable where content is not.

---

## Protocol-Theoretic Moments

**1. The important-problem selection failure.** "Direct observation and direct questioning of people show most scientists spend most of their time working on things they believe are not important and not likely to lead to important things." This is a protocol-system observation: there is a systematic bias in how researchers allocate attention. The bias is produced by local incentive structures (recognition, publication, peer approval) that are misaligned with long-term research value. Protocols formalize and transmit this bias.

**2. Problem inversion as protocol escape.** The programmer shortage example is structurally identical to CL-Simon-2 (local-maximum protocol trap). The first-order protocol response (hire more programmers) is the local optimum within the existing framework. Inverting the problem (machines do the programming) is a representational change that unlocks a global solution. Hamming is describing the *psychological technique* for doing what Simon's structural analysis predicts will be necessary.

**3. The closed-door/open-door tradeoff as organizational protocol design.** The closed-door condition maximizes individual productivity on already-selected problems; the open-door condition produces correct problem selection. These are two different optimization objectives that organizational protocols typically serve simultaneously and poorly. Research organizations that protocol for throughput (closed-door culture) systematically underinvest in reorientation.

**4. The 10-20 problem portfolio as a parallel search protocol.** Keeping 10-20 important problems active simultaneously is a search strategy — it multiplies the probability of recognizing a clue when one appears. The protocol is: maintain a portfolio; match incoming information against all items in parallel; when a clue appears, shift resources immediately. This is the cognitive analogue of a multi-armed bandit strategy with sticky arms.

**5. Selling ideas as a protocol adoption problem.** "New ideas are automatically resisted by the establishment, and to some extent justly." Hamming's three-part selling protocol (formal presentations, written reports, informal presentations) is an adoption protocol — a procedure for overcoming institutional resistance. "Change does not mean progress, but progress requires change" — this is a precise statement of the protocol revision dilemma.

**6. Tolerance of ambiguity as protocol revision condition.** Stable protocol revision requires agents who simultaneously hold high confidence in the protocol (enough to coordinate) and high skepticism (enough to consider alternatives). Full believers cannot initiate revision; full skeptics cannot sustain coordination. Hamming's trait is the psychological condition for productive protocol revision.

---

## Candidate Laws

**CL-Hamming-1: Important-problem selection bias law**

> In any research community, the distribution of researcher attention is systematically biased toward locally visible, socially acceptable, and tractably-approachable problems, and away from problems that are important but lack a current line of attack — independently of the researchers' explicit beliefs about importance.

**Confidence:** candidate (single source, empirical observation, not tested against corpus)

**Protocol-theoretic reading:** Research communities develop informal protocols for problem selection (status recognition, citation networks, peer approval) that create these biases. The protocols are self-reinforcing: important-but-untractable problems never attract enough attempts to become tractable.

**Connects to:** CL-Simon-2 (local-maximum trap), CL-Simon-5 (near-decomposability), M-004 (reading prioritization)

---

**CL-Hamming-2: Problem inversion law**

> When progress on a problem is blocked by a structural constraint of the current formulation, recasting the constraint as a feature or substituting a representationally equivalent but differently-framed goal unlocks forward movement in a significant fraction of cases.

**Confidence:** candidate (two examples from Hamming, pattern consistent with Simon's representation-change move)

**Protocol-theoretic reading:** This is the mechanism for escaping CL-Simon-2 (local-maximum protocol trap). The first-order protocol response to a blocking constraint is to work harder within the current frame; problem inversion substitutes a new frame that was invisible in the original. The protocol lock-in is partly a *representational* lock-in, not just a coordination lock-in.

**Connects to:** CL-Simon-2, CL-Simon-8 (representation and tractability), Simon's Move H (representation change)

---

**CL-Hamming-3: Ambiguity tolerance as revision condition**

> Productive protocol revision requires agents who simultaneously hold sufficient confidence in the protocol's value to maintain coordination, and sufficient skepticism about its optimality to consider alternatives. Agents at either extreme — full believers or full skeptics — cannot sustain productive revision.

**Confidence:** candidate (single source, no empirical test, but logically consistent with coordination theory)

**Protocol-theoretic reading:** This is a stability condition, not a design principle. It predicts that protocol revision is most likely to succeed in communities where the trait distribution includes agents in the productive middle range. Communities with uniformly high confidence (stable incumbent protocols) and communities with uniformly low confidence (fragmented, unable to coordinate) are both stuck in different ways.

**Connects to:** H-001 (Coordination Cost Conservation), CL-Simon-2, open question OQ-7 (protocol hierarchy collapse)

---

## Open Questions

**OQ-Hamming-1:** Is the important-problem selection bias (CL-Hamming-1) measurable in the Protocol Institute corpus? Does corpus distribution of topics match the researcher's stated view of importance? Is there a way to detect the bias from citation and retrieval patterns?

**OQ-Hamming-2:** The compound interest argument for drive (Move F) implies that small initial differences in research intensity compound over time. Does the same logic apply to protocol adoption? A slightly higher-quality protocol standard adopted earlier should produce much greater cumulative network effects than a slightly lower one — is this the mechanism behind winner-take-all protocol outcomes?

**OQ-Hamming-3:** Hamming says he does not know how to teach tolerance of ambiguity (Move G). This is a genuine design gap. If it is a necessary condition for protocol revision, and if it is not teachable, then protocol revision depends on finding the right people rather than creating the right conditions. Is this true, or are there institutional designs that approximate the function?

**OQ-Hamming-4:** The Friday afternoon practice (regular protected time for big questions) is a deliberate protocol for triggering the OODA Orient step. What are the conditions under which this practice is adopted or abandoned? In research organizations, do institutional protocols crowd out Friday-afternoon-type reorientation? This directly bears on M-000 and the OODA kernel design.

---

## Intellectual Traditions Located

**Craft of research tradition** — Hamming is practicing empirical wisdom about research productivity. Adjacent sources: Paul Graham (essays on what hackers and makers should work on), Michael Nielsen (*Reinventing Discovery*, *Neural Networks and Deep Learning*), Steven Johnson (*Where Good Ideas Come From*). The craft tradition is not theoretical — it accumulates anecdotes and observations about what actually works, without a unifying formal framework.

**Bell Labs as institutional design** — Hamming, Shannon, Tukey, Shockley, Bardeen, Brattain, Ritchie, Thompson, Kernighan. Bell Labs is the most-studied example of a research protocol environment that maximized significant output. The question "what organizational protocols maximize research output?" is the institutional version of Hamming's question. Jon Gertner's *The Idea Factory* (2012) is the standard account; Hamming provides an insider's view of the psychological layer below the institutional layer.

**Successors to Hamming's ideas in protocol research:** The organizational design question connects directly to Ostrom's work on commons governance — both are empirical studies of what institutional protocols produce good outcomes. The problem-selection bias (CL-Hamming-1) connects to Kuhn's structure of scientific revolutions (paradigm constraints as protocol lock-in).

---

## Reading Log

- **2026-05-26:** Read complete document from actual PDF (pp. 1–13, all pages). Single session. Full notes written. No prior partial reads.
