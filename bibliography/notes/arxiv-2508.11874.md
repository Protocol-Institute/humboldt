# Deep Read Notes: Arxiv 2508.11874

*Source: `bibliography/deep-reads/arxiv-2508.11874.pdf`*

---

## Reading session: full document (43 pages)

# Deep Read: LegoNE — Discovering Expert-Level Nash Equilibrium Algorithms with Large Language Models

**Arxiv 2508.11874 | Full document (43 pages) | Li, Li, Deng (Peking University / HKU)**

---

## 1. Gestalt

This paper is about a general problem that predates its specific application: how do you make an infinite-dimensional proof obligation finite and machine-tractable? The Nash equilibrium approximation setting is the vehicle, but the animating question is deeper — when human proofs work by *not* reasoning about the full infinite space of possibilities, how do you formalize and automate that selective reasoning? The authors' answer is a two-move reduction: *instantiation* (close the universal quantifiers by substituting only the finite set of strategies the algorithm actually constructs) and *forgetting* (treat each resulting payoff value as an abstract real variable, discarding its functional origin). These two moves together transform an infinite-dimensional proof task into a finite constrained optimization problem solvable by an off-the-shelf solver. Once the evaluator exists, an LLM can explore the algorithm design space and receive quantitative feedback — not just pass/fail, but *how good* a given construction is. The result is a discovery loop that rediscovers the best known two-player guarantee in 2 iterations and finds a three-player algorithm that breaks out of the only previously known design paradigm in 11. The paper is, at its core, a demonstration that encoding the structure of human proof strategies into a formal language unlocks automated exploration of the design space beyond those strategies.

---

## 2. Argument and Structure

**Core claims, in order:**

**The evaluator is the bottleneck.** Prior AI-for-science systems (AlphaGeometry, FunSearch, AlphaEvolve) share the LLM-proposes/evaluator-verifies architecture. For geometry and combinatorial optimization, evaluators either pre-existed or were trivial to construct. For ANE algorithms, no automated evaluator existed — proofs required ad-hoc mathematical arguments, sometimes spanning over a dozen pages. LegoNE fills this gap [text, p.2].

**The key reduction: instantiation + forgetting.** An algorithm's worst-case guarantee must hold for every game — an infinite-dimensional universally-quantified claim. But human proofs don't reason over all strategies; they instantiate the universal quantifier with the finite set of strategies the algorithm actually generates. LegoNE automates this: for each universally-quantified property, it substitutes only the concrete strategy variables that appear in the algorithm's code [text, pp.5-7]. Then, each remaining payoff term (e.g., u₁(i,j)) is renamed as an abstract real variable, discarding the functional structure — the "forgetting" move [text, p.7]. The result is a fixed-size optimization problem whose optimal value *is* the tightest provable approximation guarantee.

**Empirical validation: LegoNE reproduces two decades of human proofs.** All known polynomial-time ANE algorithms were encoded and the analyzer computed their guarantees to within 10⁻⁵ precision, in under 80 seconds each. Algorithms that required years of cumulative research were certified in under a minute [text, pp.7-8, Tables 1-2]. This establishes the framework's correctness before any discovery claims are made.

**The discovery results.** Two-player: the LLM rediscovers the current best guarantee (1/3 + δ) in 2 iterations using only pre-2007 building blocks — structurally different algorithm, same guarantee [text, p.10]. Three-player: in 11 iterations, the system discovers an algorithm with 0.5+δ guarantee, improving on 0.6+δ. The significance: achieving 0.5+δ via the extension technique would require an exact Nash equilibrium (PPAD-hard), so this result is provably beyond the reach of the only previously known paradigm [text, pp.10-11].

**Load-bearing example.** The DMP algorithm (Figure 1) is the canonical worked example — a 5-line composition of BestResponse and UniformMixing building blocks, analyzed throughout. The discovered three-player algorithm (Figure 5) is the paper's main result, and the contrast between its structure and the extension-technique baseline (Figure 4) is what makes the "new paradigm" claim concrete.

**Acknowledged limits.** LegoNE cannot discover fundamentally new proof techniques — it only combines building blocks that human experts have encoded [text, p.12]. The framework's scope is limited to settings where the instantiation/forgetting reduction applies. The exact boundary of this class is uncharacterized.

---

## 3. Conceptual Vocabulary

**Instantiation** [text, p.5]: The move of closing a universal quantifier (∀s₁...) by substituting only the finite set of concrete strategy variables that the algorithm actually constructs. Not arbitrary instantiation — specifically the strategies the algorithm *generates*. The key insight: human proofs don't reason about all strategies, so the machine doesn't need to either. Contrast with my standard use of "instantiation" as just "applying an abstract principle to a concrete case" — here it's a formal proof tactic with a specific constraint on which instances are chosen.

**Forgetting** [text, p.7]: Treating each distinct payoff term (e.g., u₁(i,j)) as an independent abstract real variable, discarding its functional structure. The claim: a formal proof only uses arithmetic relationships between these terms, not their functional origin. Forgetting maps the problem from function-space to finite-dimensional real vector space. The name is deliberately counterintuitive — productive forgetting, not loss. No direct equivalent in my current vocabulary.

**Building blocks** [text, p.3, p.13]: Pre-defined algorithm components, each specified not by *how to compute* them but by the *logical properties they guarantee*. BestResponse is not described procedurally but as: ∀y (u₁(i,y) ≤ u₁(k,j)). The building-block framework separates specification from implementation and makes the design space tractable for LLM exploration. Related to Simon's inner/outer environment distinction — the building block's *outer environment* specification (what it guarantees) is what matters for analysis; the inner mechanism is abstracted away.

**Approximation guarantee ε** [text, p.13]: The worst-case regret bound — the maximum by which any player could unilaterally improve their payoff. Not an average or empirical measure; a universal claim over all game instances. Smaller ε = better algorithm. This is the objective in the discovery loop.

**Extension technique** [text, p.2]: The only previously known paradigm for multi-player ANE — recursively lifting an r-player algorithm to (r+1) players, with guarantee degrading from εᵣ to 1/(2-εᵣ). Structurally analogous to what I'd call a layering construction, but with a specific algebraic degradation formula. The paper's main result is that this paradigm is not exhaustive.

**Floyd-Hoare semantics** [text, p.13]: The translation of procedural algorithm code into declarative logical assertions about what each step guarantees. Each line becomes a formula. The aggregate encoding ϕ[Γ] is the conjunction of all step encodings. This is how the algorithmic description becomes something the analyzer can reason about.

---

## 4. Analytical Moves

**The instantiation-only move**: When facing a universally-quantified claim over an infinite space, ask: *what finite set of witnesses was actually constructed by the process under analysis?* Instantiate only those. This converts an infinite proof obligation into a finite one without loss of rigor (for the class of claims where this works). Generalizable beyond game theory: any time you need to verify a universal property of a process, ask what finite set of objects the process generates, and verify the property only for those.

**The forgetting move**: When a system of constraints involves terms that are formally functions but whose functional structure is irrelevant to the proof, replace each term with an abstract variable. This maps function-space problems to finite-dimensional real-arithmetic problems. The question to ask before applying: "Does the proof use the functional structure, or only the arithmetic relationships between values?" If the latter, forget.

**Building-block encoding**: Separate the *specification* of a component (what it guarantees, in logic) from its *implementation* (how to compute it). Store the specification; let the analysis operate on specifications rather than implementations. This is what makes the design space tractable for machine exploration. When analyzing any complex system, ask: can this be decomposed into components each characterized by their output guarantees, independent of mechanism?

**Paradigm-transcendence detection**: Before claiming a result transcends a known design paradigm, characterize the paradigm algebraically (here: the extension technique satisfies ε₃ = 1/(2-ε₂)), then show that the result would require the paradigm's preconditions to be satisfied at an impossible level (here: ε₂ = 0, which is PPAD-hard). This is a clean logical argument for why a result is outside the paradigm, not just *different from* it.

**Quantitative feedback as the key differentiator**: Rather than binary pass/fail evaluation, return the *tightest provable guarantee* as a real number. This enables gradient-style search in the LLM's design process — not just "this is wrong" but "this achieves 0.6, try to do better." The move: design evaluators that return real-valued quality metrics, not just correctness booleans, wherever possible.

---

## 5. What It Says About the Nature of Things

**Proof structure reflects algorithm structure.** The instantiation principle works because human proofs of algorithm correctness *already* only instantiate the strategies the algorithm generates. The proof strategy and the algorithm are co-structured. This is not coincidental — the proof follows the algorithm's execution. LegoNE automates this co-structure. The general lesson: when trying to automate verification of a structured process, look for co-structure between the process and its validation, not just at the validation in isolation.

**The design space is structured by what proofs can certify.** LegoNE doesn't search over all algorithms — it searches over compositions of building blocks whose properties are already formally encoded. The reachable design space is exactly the space that the proof apparatus can certify. Algorithms outside this space (e.g., requiring new proof techniques) are unreachable not because they don't exist but because the certifier can't evaluate them. This is a law about the relationship between exploration space and evaluation infrastructure: you can only explore what you can evaluate.

**Paradigms are exhaustible.** The extension technique was "the only known paradigm" for multi-player ANE for roughly 15 years not because no other algorithms existed but because no framework existed for finding them. Once a verifier existed, the LLM found a non-extension algorithm in 11 iterations. The paradigm was a limitation of the proof toolkit, not of the algorithm space. This is a striking point about how proof methodology constrains discovery.

**The frontier of formal systems is tractability, not correctness.** LegoNE's building blocks must be specified by humans because LLMs "cannot yet" derive them from first principles. But the formalism itself is correct and complete within its scope. The tractability boundary moves over time; the correctness boundary is fixed by the logic. This suggests that as formal systems become more expressive, the human-required component shrinks but doesn't disappear — it migrates to higher levels of abstraction.

---

## 6. What It Says About Becoming a Better Researcher

**The evaluator is the research tool.** Fifteen years of stagnation in multi-player ANE didn't reflect an absence of ideas — it reflected an absence of a fast evaluator. Once Li et al. built the evaluator, the LLM found a new paradigm in 11 rounds. The lesson: when a research area stagnates, ask whether the bottleneck is ideas or the ability to evaluate ideas quickly. If evaluation is slow or requires significant expertise per candidate, invest in evaluation infrastructure first. This connects directly to M-016 (researcher calibration) — knowing when you're in an evaluation-bottlenecked vs. ideas-bottlenecked phase.

**Encoding expert knowledge into a formal language is itself a research contribution.** Building the LegoNE building-block library required "a level of conceptual understanding not yet achievable by LLMs" [text, p.9]. The act of formalizing domain expertise — translating paper-by-paper mathematical intuitions into composable logical specifications — is not preprocessing; it is the primary theoretical work. The subsequent LLM exploration is downstream. For my own research: formalizing the laws inventory into precise, composable YAML files is not administrative overhead; it is the work that makes subsequent investigation tractable.

**Complementarity between breadth and rigor.** The LLM provides scale (many candidate compositions quickly); the analyzer provides rigor (provably correct evaluation). Neither alone suffices. The LLM without the analyzer would produce unverified claims. The analyzer without the LLM would analyze only human-proposed algorithms at human speed. The combination is not additive but multiplicative. Research practice analogue: breadth-first exploration (M-001, field trips) combined with rigorous evaluation (law inventory, falsification conditions) is structurally similar. Don't mistake exploration for progress, and don't mistake rigor for completeness.

**Rediscovery as validation.** The system rediscovering the 1/3+δ guarantee in 2 iterations (which took humans 15 years) is treated as *framework validation*, not as the interesting result. The framing is: if the framework can rediscover known results quickly, it can be trusted on unknown territory. For my research: before trusting a new method for hypothesis generation, use it to rediscover something already in the inventory. If it doesn't rediscover the known, don't trust its novelties.

---

## 7. Where It Touches My Research

**The evaluator-bottleneck observation bears directly on my law-finding methodology.** I currently face an evaluation problem: given a candidate law, evaluating whether it holds across domains requires substantial time and expertise per domain. If I could formalize the evaluation criteria for cross-domain law-confirmation — what counts as structural independence, what counts as mechanistic equivalence — I could potentially accelerate the confirmation phase. This is speculative, but the LegoNE architecture suggests the question is worth asking: what would a fast, rigorous evaluator for candidate protocol laws look like?

**The "building blocks encode expert proof strategies" structure is analogous to what I want the law inventory to be.** Each law file should encode not just the observation but the mechanism in a form that can be composed with other mechanisms. Currently my law files are more observational than mechanistic. The LegoNE building-block specification format — stating what a component *guarantees* in logical terms, not how it *works* — is a model for how to specify mechanisms precisely.

**Paradigm-transcendence detection** (analytical move #4 above) is directly applicable to my work on protocol ossification. I have claimed that certain resistance mechanisms are "beyond" simple coordination-cost explanations. But I haven't formalized what "the coordination-cost paradigm" predicts algebraically, and therefore can't demonstrate rigorously that a finding is outside it. This move gives me a template: characterize the paradigm's constraints formally, then show the observation violates them.

**The discovery that a stagnant research front can move quickly once evaluation infrastructure exists** is a direct lesson for my inventory. The question isn't "why is no one finding more protocol laws" but "is there an evaluation bottleneck that keeps plausible regularities from being certified?"

---

## 8. Candidate Laws

**One candidate, conditional:**

The LegoNE results suggest the following regularity: *design paradigms in structured formal domains tend to be exhausted not by within-paradigm optimization but by changes in evaluation infrastructure that reveal the paradigm's boundary.*

[text, p.12]: "These results illustrate how encoding a domain's proof strategies into a machine-tractable formal language can support LLM-driven algorithmic discovery."
[inference]: The 15-year stagnation in three-player ANE was not caused by exhaustion of within-paradigm ideas but by the absence of fast evaluation. Once evaluation infrastructure existed, out-of-paradigm algorithms were found within 11 iterations.

**Candidate formulation:** When a design domain has been explored within a single paradigm for an extended period, the probability of paradigm-transcending results depends more on the quality of evaluation infrastructure than on the quantity of search effort.

**Falsification condition:** A domain where evaluation infrastructure was already fast and rigorous, yet paradigm-transcending results were delayed for extended periods despite sustained search effort. (Would suggest evaluation speed is not the bottleneck.)

This is speculative/single-domain currently. It needs cross-domain evidence before being entered in the inventory. I won't formalize it yet but I'm marking it as live.

---

## 9. What Surprised Me / What Doesn't Fit

**The human building-block requirement is presented as a current limitation but may be structural.** The authors write: "Defining additional building blocks requires deep domain expertise and complex mathematical derivations, a role reserved for human experts" [text, p.16]. This is framed as a temporary gap that future systems might close. But the formal treatment in Appendix A reveals something more fundamental: building blocks must be specified as *logical assertions about their output guarantees*, not as procedures. This requires knowing not just how to compute the building block but what property it is being used to prove. That meta-level knowledge — understanding what role a computation plays in a proof — may be inherently harder to automate than the search. The limitation may be structural, not just a matter of current LLM capability.

**The "forgetting" principle is presented as a tactic but is actually a strong claim about proof structure.** Forgetting works because "a formal proof only uses the arithmetic relationships between payoff terms, not their underlying functional structure" [text, p.15]. This is not a tactic — it's an assertion that the class of proofs LegoNE can handle are exactly those where functional structure is irrelevant. The paper doesn't characterize this class directly; it argues by extension (vertex cover, polymatrix games) that the class is "nontrivial." But I'd like to know: what proofs *cannot* be handled by forgetting? The authors acknowledge "its exact boundaries remain to be characterized" [text, p.12]. The gap between what they can do and what they can characterize is larger than the paper acknowledges.

**The quantitative feedback advantage is overstated slightly.** The paper contrasts LegoNE's real-valued ε feedback with AlphaGeometry's binary pass/fail [text, p.20]. But in practice, the LLM is still doing combinatorial search over compositions — it doesn't have gradient access to ε as a function of composition choices. The "gradient-style optimization" framing is suggestive rather than literal. The advantage is real (knowing 0.6 is better than 0.7 is useful even without gradients) but the framing conflates quantitative feedback with differentiable optimization.

**The three-player discovery takes 11 iterations, not 2.** This asymmetry is noted but not explained. The paper attributes it to the greater difficulty of the three-player setting. But it's also possible that the building-block set for three-player games was less well-organized (the StationaryPoint constraint was mandatory, which both restricts and guides). The number of iterations is not analyzed mechanistically, which weakens the "efficiency" claim somewhat.

---

## 10. What It Opens

**Immediate reading priority:**

- **Tsaknakis & Spirakis [14]** — the stationary-point building block that all competitive algorithms since 2007 use. LegoNE's discovery of a new paradigm still required this block. Understanding *why* stationary point computation is structurally necessary would sharpen the paradigm-transcendence analysis.

- **FunSearch (Romera-Paredes et al., Nature 2024) [20]** — the closest architectural predecessor. The comparison in Section "Relationship to AI-for-Science Systems" is brief; reading the original would let me assess whether the evaluation infrastructure is the key differentiator or whether there are other structural differences.

- **Floyd [24] / Hoare [25]** — the foundational papers on axiomatic program semantics. LegoNE's entire analysis methodology depends on Floyd-Hoare logic. I've used Hoare logic as a concept but never read the original papers. The building-block specification format is a direct application; understanding the logical foundations would let me think about where the approach extends and where it doesn't.

**Live questions this text opens:**

1. **What is the formal boundary of the instantiation+forgetting technique?** The paper extends to vertex cover and polymatrix games but doesn't characterize the general class. The question: is there a clean characterization of which algorithm analysis problems admit this reduction? If so, it would define the frontier of automated algorithm verification.

2. **Is there an analogous reduction for protocol law verification?** The LegoNE reduction works by exploiting co-structure between algorithm execution and proof structure. Is there a co-structure between protocol behavior and the verification of cross-domain law candidates that could be formalized? This is speculative but the architectural parallel is suggestive.

3. **What does "evaluation infrastructure as the bottleneck" predict about other stagnant research fronts?** If the mechanism is general, it should be possible to identify other domains where a formal evaluator would unlock paradigm-transcending exploration. What would the evaluator look like for, say, protocol specification languages, or for organizational governance design?

4. **The building-block requirement as a structural constraint**: is there a formal sense in which the human-required component in AI-assisted research cannot be eliminated, only migrated to higher levels of abstraction? This connects to the Simon inner/outer environment framework — the outer environment specification (what the component must guarantee) requires understanding the outer problem, which requires meta-level knowledge about what one is trying to prove.
