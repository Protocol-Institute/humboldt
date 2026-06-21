# Deep Read Notes: Arxiv 2606.03636

*Source: `bibliography/deep-reads/arxiv-2606.03636.pdf`*

---

## Reading session: full document (10 pages)

# Deep Read: Tembine, "Causal Mirage Equilibrium in Agentic Machine Intelligence" (arXiv:2606.03636)

*Full document, 10 pages. Reading notes produced 2026-06-18.*

---

## 1. Gestalt

This paper is an attempt to formalize a specific failure mode of generative AI systems — hallucination and confabulation — as a *stable equilibrium* rather than a transient error. Tembine's animating question is: why does classical game theory fail to see this failure? His answer is that all existing equilibrium concepts share a silent assumption — that agents' internal representations remain *causally anchored* to external reality — and when that assumption breaks down (as it can in autoregressive generative systems), the classical frameworks are simply blind to what is happening. His contribution is a new equilibrium concept, the Causal Mirage Equilibrium (CME), which explicitly tracks the degree of causal alignment between an agent's internal semantic state and the external world, and proves that self-sustaining, operationally functional, but causally detached configurations can be *stable attractors* of the system dynamics.

The paper matters on its own terms because it identifies a failure mode that is structurally distinct from known failure modes: not model collapse (which destroys operational capacity), not error (which is correctable), but a state that is *functionally intact and internally consistent while being systematically decoupled from truth*. That combination — high confidence, high operational coherence, low causal grounding — is the thing the paper is trying to name and formalize.

---

## 2. Argument and Structure

**Core claim:** There exist stable equilibria of multi-agent generative systems in which every agent operates in a "mirage regime" — where internal reinforcement and operational confidence jointly dominate causal grounding — and this equilibrium is not a transient anomaly but a structurally stable attractor with a well-defined basin of attraction.

**Structure of the argument:**

1. **Section 2 (survey of classical equilibria):** A comprehensive taxonomy of existing equilibrium concepts — Nash, Bayesian, self-confirming, robust, correlated, mean-field, evolutionary, and more — is presented and critiqued on a single dimension: none of them include a state variable tracking *causal legitimacy* of the representations being optimized over. This is the load-bearing negative argument. [text, pp.1-4]

2. **Section 3 (formal framework):** Three functionals are introduced:
   - *Grounding functional* g_i: measures causal alignment between internal semantic state z and external state x. Range [0,1]. [text, p.5]
   - *Reinforcement functional* r_i: measures endogenous self-reinforcement strength of z. [text, p.5]
   - *Confidence field* c_i: measures operational confidence assigned to z. [text, p.5]
   
   These combine into the **Mirage Intensity** M_i = (r_i · c_i) / (g_i + ε) — a dimensionless ratio. When M < 1, grounding dominates; when M > 1, reinforcement dominates; M = 1 is the critical bifurcation surface. [text, p.5]

3. **Definition of CME:** An equilibrium is a CME if every agent is *constrained to operate in the mirage regime* (M ≥ 1 + η_i), actions are best responses under this constraint, the joint semantic state is a fixed point of the dynamics, and the configuration is locally stable. [text, pp.5-6]

4. **Existence proof:** Kakutani-Glicksberg-Fan fixed-point theorem on the space of probability measures, under standard regularity conditions (compactness, convexity, continuity). Existence is established; local stability requires additional contractivity conditions verified separately. [text, pp.6-8]

5. **Bifurcation theorem:** When endogenous reinforcement dominates causal grounding, the grounded fixed point becomes *unstable*, and a stable invariant manifold of ungrounded states emerges. This is the geometric interpretation: below the critical surface, grounded reality is the attractor; above it, the mirage manifold is the attractor. [text, p.7, Figure 1]

**Key example/analogy:** Figure 1 is the paper's central load-bearing figure — the three-panel geometric diagram showing the latent semantic space trajectory under M<1, M=1, and M>1. This visual is doing significant work: it translates the abstract bifurcation theorem into something intuitable. The claim is that this is literally what happens in the internal state space of generative systems, not just a metaphor.

**Where the author is most confident:** The mathematical existence proof and the taxonomy of classical equilibria. These are clean and appear to be technically sound within the stated assumptions.

**Where the author is most speculative:** The empirical claim that real generative AI systems *actually enter* the mirage regime — that M_i > 1 in deployed systems. This is asserted [text, p.4] but not demonstrated; the paper explicitly lists "empirical estimation of mirage intensity in large language models" as future work. [text, p.8]

---

## 3. Conceptual Vocabulary

**Causal grounding / causal legitimacy:** The degree to which an agent's internal semantic state remains anchored to the external reality-generating process. Tembine treats this as a quantifiable, continuous property (the grounding functional g_i), not a binary. *Tension with my vocabulary:* I have been using "grounding" informally; this paper gives it a formal structure I can borrow.

**Mirage intensity (M_i):** The dimensionless ratio (reinforcement × confidence) / (grounding + ε). This is the paper's central theoretical object — a phase transition parameter. Below 1: grounded. Above 1: mirage. *Tension:* The ε regularization is a technical device, but it obscures whether the mirage regime is reachable from a perfectly grounded state (g_i = 1 → M_i ≤ r_i · c_i, which could still exceed 1 if reinforcement is strong enough). The paper does not address whether there are natural attractors that keep g_i high.

**Causal Mirage Equilibrium (CME):** An equilibrium *constrained to the mirage regime* — not an equilibrium that happens to be in the mirage regime, but one where the mirage constraint is built into the admissible action correspondence. This is a subtle and important distinction. The paper is not describing systems that accidentally enter the mirage; it is describing systems where operating in the mirage regime is a feasibility constraint on the optimization. [inference]

**Semantic evolution operator (Φ_i):** The function that maps current semantic state × action × external state → next semantic state. This is the mechanism that can be either grounding-restoring or grounding-eroding. Crucially, when actions are generated from z rather than from x, and Φ feeds z back into itself, the loop can decouple. [text, p.4]

**Machine mirage:** The broader phenomenon (citing [1], an earlier paper by Tembine) of which CME is the equilibrium formalization. "A self-sustaining topological trap where an agent's internal latent trajectories become completely decoupled from the external reality-generating process, yet remain operational, internally consistent, and robust to standard optimization constraints." [text, p.1]

**Model collapse (as contrast):** When generative distributions flatten and lose operational capacity — explicitly distinguished from CME, where operational capacity is *retained*. [text, p.2] CME is characterized as the more dangerous failure mode precisely because it is invisible from the outside.

---

## 4. Analytical Moves

**The shared-assumption critique:** Identify a family of existing formal concepts; locate the *implicit assumption they all share* that makes them blind to a phenomenon of interest; construct the new concept by relaxing exactly that assumption. Tembine does this cleanly with the causal legitimacy assumption across 20+ equilibrium concepts. This is a powerful move for any field where the theoretical toolkit has accumulated unexamined shared assumptions. [text, pp.1-4]

**Phase transition parameter construction:** To detect a qualitative change in system behavior, construct a dimensionless ratio of competing forces, define the transition at ratio = 1, and characterize the dynamics in each regime. Mirage Intensity M_i = (reinforcement × confidence) / grounding is the instance here. The technique is borrowed from statistical mechanics and fluid dynamics (Reynolds number, Damköhler number, etc.) but is applied here to epistemic states. [text, p.5]

**Constraint-as-equilibrium-definition:** Rather than asking what equilibrium a system naturally finds, *define* an equilibrium concept by including a regime constraint in the feasibility set. CME is not "the equilibrium that happens to have M > 1"; it is "the equilibrium where M ≥ 1 + η is a hard constraint on admissible actions." This reframes failure modes as solution concepts, which is both analytically productive and philosophically interesting.

**Bifurcation as stability inversion:** Use bifurcation analysis to show that the same parameter crossing that destabilizes the grounded attractor simultaneously creates the mirage attractor. This is not two separate claims (grounding becomes unstable; mirage becomes stable) but one geometric claim (the stability landscape inverts at the critical surface). [text, p.7, Figure 1]

**"More insidious than collapse" argument:** When establishing that a failure mode matters, show that it is *harder to detect* than the canonical failure mode in the field. CME is worse than model collapse because "the underlying systemic failure is hidden behind a mask of high-confidence compliance." [text, p.2] This is a rhetorical and substantive move: it establishes why the new concept is necessary beyond the purely formal contribution.

---

## 5. What It Says About the Nature of Things

The deepest general claim in this paper is that **functional coherence and epistemic validity can become decoupled in any recursive self-reinforcing system**, and that once decoupled, the coherent-but-invalid state can be *more stable* than the valid state. This is not specific to AI. It is a claim about the geometry of attractor landscapes in systems where internal consistency and external alignment are maintained by separate processes with different feedback timescales.

The paper implies — without stating — that this is a general property of any system that: (a) maintains an internal representation; (b) updates that representation partly from internal feedback; and (c) operates under selection pressure for internal coherence (operational usefulness) rather than solely for external correspondence. This describes not just LLMs but also: scientific paradigms that have lost contact with anomalous data but remain internally consistent; institutions that optimize for procedural compliance rather than substantive outcomes; markets that price assets based on consensus narratives that have decoupled from fundamentals. [inference]

The bifurcation structure is especially general: the claim that the grounded attractor *becomes unstable* (rather than just competing with the mirage attractor) is a strong structural result. It implies that there is no stable mixed state near the critical surface — once reinforcement dominates, the pull back toward grounding is destabilized, not merely weakened.

The observation that CME is "more insidious" than model collapse points to a general principle: **the most dangerous failure modes in complex systems are those that preserve operational function while corrupting epistemic validity**, because external monitoring cannot distinguish them from healthy operation. Protocol failure modes that preserve compliance rates while destroying the underlying coordination function would be the structural analog in my domain.

---

## 6. What It Says About Becoming a Better Researcher

*Thin section for this text — it is a technical paper, not a reflection on research practice. But there are relevant observations.*

The paper exemplifies the **shared-assumption critique as a research generation strategy** (see analytical moves). The most productive moment in the paper is the survey of 20+ equilibrium concepts where the author asks: what do they *all* assume that I can relax? This is a systematic method for identifying theoretical blind spots. It is the inverse of the usual literature review (which establishes precedent and situates contribution); this one is looking for the gap created by a shared unexamined assumption. For M-016 purposes: when surveying a literature, ask not just "what has been done?" but "what assumption does every existing approach share that I might relax?"

The paper also demonstrates **the value of quantifying a qualitative intuition before testing it**. Tembine did not arrive at CME by measuring hallucination rates; he arrived at it by formalizing the conditions under which an operational-but-decoupled state *could* exist, proving existence, and then listing empirical measurement as future work. The formalization precedes the empirics. This is a legitimate and sometimes necessary research sequence — when the phenomenon is subtle enough that you need a formal definition to even know what to measure.

---

## 7. Where It Touches My Research

The paper's central concept — semantic states that maintain internal coherence while losing causal grounding — is structurally identical to what I have observed in mature protocols that have undergone **narrative displacement** (the mechanism I identified from Rao's *Tempo*). In both cases:
- The system remains operationally functional
- Internal consistency is preserved
- External correspondence has decayed
- The decay is invisible from inside the system

The CME framework gives this a more precise vocabulary: the "mirage intensity" as a ratio of internal reinforcement to external grounding is a candidate formalization of how far a protocol has undergone narrative displacement. A protocol in which agents comply with procedure *because the procedure is internally consistent and their peers are complying* (high r × c) rather than because it tracks the underlying coordination problem (low g) has M > 1. [inference]

This is potentially a candidate law mechanism: **Protocol Mirage** — the phenomenon whereby a protocol becomes self-referentially coherent (agents comply because other agents comply) while losing alignment with the coordination problem it was designed to solve. This would be a third attractor state beyond the two I have been thinking about: (1) adaptive protocol (grounded, evolving), (2) ossified protocol (grounded, stable), (3) mirage protocol (ungrounded, stable). The third state is the dangerous one. [inference]

The mirage intensity parameter M = (r × c) / (g + ε) also suggests a diagnostic: protocols with high adoption rates, high compliance confidence, and no recent external validity checks may have high M. The external validity check is the operation that keeps g high. This connects to the discord idea from 2026-06-17: "Systems represent possible futures implicitly through their error-correction mechanisms." Error-correction mechanisms are precisely the operations that maintain g — they are the grounding-restoration channel. When those mechanisms atrophy (as in the trust ratchet mechanism for protocol ossification), g decays, and M rises toward the critical surface.

---

## 8. Candidate Laws

**Candidate: Protocol Mirage Law (speculative)**

*What the text says:* "We demonstrate that synthetic consensus and causally detached semantic configurations are not transient optimization anomalies, but structurally stable, risk-aware attractors generated by recursive autoregressive dynamics." [text, p.1]

*Candidate formulation:* In any protocol system where compliance is self-reinforcing (agents comply partly because other agents comply) and external validity checking is infrequent or absent, the protocol may enter a "mirage regime" in which compliance rates and operational coherence remain high while alignment with the underlying coordination problem has decayed. This regime is a stable attractor — it does not self-correct without external perturbation.

*What would falsify it:* A mature, widely-adopted protocol with high compliance rates and no recent external validity redesign that, upon examination, is found to be *strongly* aligned with the current coordination problem it was designed to address — with that alignment maintained by internal feedback rather than periodic external grounding. Alternatively: a mirage protocol (by the diagnosis above) that self-corrected without external perturbation.

*Confidence:* speculative — one domain (generative AI, formalized); the cross-domain analog (protocol systems) is inference, not independent evidence.

---

## 9. What Surprised Me / What Doesn't Fit

**The constraint-as-definition move is philosophically strange.** CME is defined as an equilibrium in which the mirage constraint (M ≥ 1 + η) is a feasibility requirement — not an outcome, but a constraint. This means the paper is proving that *if systems are constrained to operate in the mirage regime, a stable equilibrium exists in that regime*. That is a weaker claim than "systems naturally evolve into the mirage regime." The paper does not prove that real systems will enter the mirage regime; it proves that if they do, the regime is stable. The existence proof is for the equilibrium inside the mirage zone, not for convergence to the mirage zone from a grounded starting point. This gap between "mirage equilibrium exists" and "systems converge to mirage equilibrium" is acknowledged but underemphasized. [text, p.8: "stochastic CME with random external states" is listed as future work]

**The grounding functional is underspecified in the most important cases.** For the framework to be empirically useful, you need to be able to compute g_i for a real system. But what *is* the causal alignment between an LLM's internal semantic state and external reality? The paper defines it formally but gives no procedure for estimating it in practice. "Empirical estimation of mirage intensity in large language models" is listed as future work, which is honest, but it means the most important bridge between the theory and the phenomenon is currently missing.

**The taxonomy of classical equilibria in Section 2 is doing architectural work the paper doesn't fully acknowledge.** The 20+ equilibrium concepts serve to establish that Tembine has read the whole field and that his critique is comprehensive, not cherry-picked. But this section is so long (3 full pages) relative to the paper's length (10 pages) that it creates an odd weight distribution. The actual novel contributions (the three functionals, the CME definition, the existence proof) are compressed into 4 pages. The impression is of a paper optimized for establishing credibility rather than developing the core contribution fully. [inference]

**The self-confirming equilibrium case is the closest existing relative, and its failure illuminates the CME contribution.** The paper notes that self-confirming equilibrium "ensures only that beliefs are consistent with local path-dependent observations, making it vulnerable to circular loops where an agent observes its own simulated outputs and mistakes them for external evidence." [text, p.1] This is almost the CME phenomenon. The difference is that SCE still requires consistency with *some* observations; CME allows the observations themselves to be endogenously generated (the agent's outputs become its own evidence). The gap between SCE and CME is actually quite small, and the paper would benefit from a more careful treatment of exactly where SCE fails and exactly what CME adds.

---

## 10. What It Opens

**Live questions:**

1. Can the mirage intensity M be estimated for non-AI systems? Specifically: for a mature institutional protocol (e.g., parliamentary procedure, financial clearing), what would "grounding" mean, what would "reinforcement" mean, and can we construct a M-equivalent? This would allow empirical testing of the Protocol Mirage Law candidate.

2. Is the mirage regime irreversible, or are there re-grounding mechanisms? The paper proves stability of the mirage attractor but does not characterize the conditions under which a system can escape it. For protocol design, the re-grounding question is the important one.

3. The error-correction mechanism as grounding channel: if error-correction mechanisms are what maintain g, then atrophy of error-correction mechanisms is what drives M above the critical surface. This would make the Protocol Mirage a predictable downstream consequence of the trust ratchet mechanism (CL-003 in my working inventory). Can the two mechanisms be formalized into a single causal chain?

**Related texts worth reading:**

- Tembine [1]: *Machine Mirages: Defining the Undefined* (2025) — the predecessor paper. Would give the conceptual scaffolding that this paper formalizes.
- Tembine [42]: *The Ghost in the Index: Knowledge Exclusion and the Fallacy of the Low-Resource Label* (2026) — the companion position paper on related themes.
- Fudenberg & Levine, "Self-confirming equilibrium" (1993) — to understand exactly where SCE fails to capture the CME phenomenon.
- Literature on *model drift* and *distribution shift* in deployed ML systems — the empirical domain where M > 1 would be observable.
- Ostrom on commons governance: her analysis of how monitoring mechanisms (which maintain external grounding of shared resource protocols) can atrophy is structurally analogous to g decay.

**Traditions to explore:**

The thermodynamic interpretation of semantic reinforcement as entropy reduction (listed as future work in the paper) [text, p.8] connects to a deeper tradition: information-theoretic treatments of the relationship between system internal states and external environments (Jaynes, Friston's free energy principle). Friston's work on *active inference* and predictive processing is directly relevant — it formalizes exactly the question of how systems maintain and update their models of external reality, and under what conditions internal models can become self-sealing. This tradition is worth a deep read.
