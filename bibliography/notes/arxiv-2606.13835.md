# Deep Read Notes: Arxiv 2606.13835

*Source: `bibliography/deep-reads/arxiv-2606.13835.pdf`*

---

## Reading session: full document (14 pages)

# Deep Read: Santos et al., "When Plausible Is Not Realistic" (arXiv 2606.13835)

*Full document, 14 pages including appendices.*

---

## 1. Gestalt

This paper is a validation audit with a conceptual payload. The authors' animating question is not "how do LLM-based urban simulators work?" but "do they actually reproduce the empirical regularities of human mobility, or only generate trajectories that *look* reasonable?" The distinction between **plausibility** and **realism** is the paper's load-bearing concept. Plausibility is face validity — the agent wakes up, commutes, eats lunch, returns home; nothing seems wrong. Realism is quantitative agreement with the deep statistical structure of human movement: truncated power-law trip distances, log-normal daily visits, recurrent motif topologies, Scouter/Regular/Routiner profile distributions. The authors show, systematically and with real data from two cities, that current LLM simulators achieve plausibility but fail realism across most dimensions. The contribution is both empirical (the measurement) and methodological (the framework for future measurement). But the unstated philosophical argument is the one that matters most: in complex behavioral systems, plausibility is not a weak version of realism — it is a different thing entirely, and can be achieved while realism fails catastrophically.

---

## 2. Argument and Structure

**Core claim:** LLM-based generative agents capture high-level semantic activity distributions (what people do) but fail to reproduce core spatial-temporal constraints (where they go, when, how far, how often, in what topological patterns). [text, p.1]

**Secondary claim:** Improving one dimension of realism can *degrade* another. CitySim's richer destination-selection (more complex LLM prompting, memory-aware preferences) improves spatial metrics like Δr and rg relative to AgentSociety, but degrades temporal metrics — dwell time errors explode, visitation frequency falls. [text, p.7] This is the most interesting empirical finding: the realism dimensions are *coupled* in the real world but *independent* in the simulators, so you can't optimize them separately without breaking the others.

**Tertiary claim:** Behavioral diversity (the Scouter/Regular/Routiner distribution) doesn't reliably emerge from generic prompting; it requires explicit profile-aware initialization. [text, p.9]

**Structure:** Literature review on human mobility laws (§2) → validation framework specification (§3) → dataset and setup (§4) → empirical results across five dimensions: spatial, temporal, motifs, behavioral profiles, semantic (§5) → remediation directions (§6). The five-dimension structure is the methodological contribution — it's a disaggregation of "realism" into orthogonal testable components.

**Load-bearing examples:**
- The STVD analysis showing that AgentSociety predicts *where* urban activity occurs more accurately than *when* — spatial distribution is partially captured, but temporal rhythms are systematically off by 3–12 hours. [text, p.7]
- The motif analysis showing simulators are dominated by simple two-node patterns (home↔work), while empirical daily routines have far greater topological variety. [text, p.7-8]
- The POI quality finding: 57.45% of OpenStreetMap POIs in Greater Paris are benches, bicycle parking, waste baskets — non-destinations. Adding Overture Maps data improves semantic map coverage and presumably realism. [text, p.9]

**Acknowledged limits:** CitySim is reconstructed from documentation, not run from source. Shanghai lacks semantic annotations. Populations are capped at 500 agents for cost reasons ($130–200 per 500-agent 7-10 day simulation). [text, pp.7, 10]

**Where the authors are most confident:** The spatial discrepancy findings — the Wasserstein distance comparisons are clear and large. Where most speculative: the causal attribution. They *suggest* the mismatches originate from POI selection instability and unconstrained radius choices, but the mechanism isn't rigorously isolated.

---

## 3. Conceptual Vocabulary

**Plausibility** [text, p.1]: Face validity. A generated behavior appears coherent, follows narrative logic, satisfies common-sense expectations. Equivalent to "nothing seems wrong." The paper's foil concept.

**Mobility realism** [text, p.1, defined explicitly]: "the joint reproduction of spatial visitation dynamics and temporal activity organization according to empirical human mobility regularities." The key word is *joint* — you can't pass this test on one dimension while failing another.

**Mobility motifs** [text, p.7-8]: Directed graphs representing daily location sequences, classified by graph isomorphism class. A motif with two nodes might be home→work→home. Empirically, about 90% of weekday mobility is captured by a small set of recurrent motifs [citing Schneider et al. 2013]. The simulators over-produce simple motifs.

**Mobility profiles** [text, p.2, p.8]: Behavioral types derived from the Scouter/Regular/Routiner taxonomy (Amichi et al. 2020). Characterized by intermittency (tendency to stay in one behavioral state before switching) and degree of return (overall tendency to revisit vs. explore). These are population-level regularities, not just individual quirks.

**Predictability** [text, p.8, Table 6]: Upper bound on the probability of correctly predicting the next location from trajectory entropy. Real mobility is ~47-67% predictable by this measure. Simulators tend to over-produce regularities, inflating predictability.

**Radius of gyration** (rg) [text, p.2, Table 6]: The characteristic spatial range of an individual's mobility, computed as the RMS distance from their center-of-mass location. A low rg means spatially confined; high means wide-ranging. Empirically follows a power-law distribution.

**Tension with my vocabulary:** "Plausibility" in this paper is close to what I might call "narrative coherence" — the kind of face validity that narrative displacement installs. But the authors use it more narrowly, specifically about generated trajectories. The deeper concept they're pointing at — the gap between surface-level coherence and structural compliance — maps directly onto my working vocabulary.

---

## 4. Analytical Moves

**The plausibility/realism disaggregation move:** When evaluating any complex behavioral system, distinguish face validity (plausible narrative) from quantitative structural realism (agreement with known empirical distributions). These can decouple completely. Apply this move whenever someone argues that a system is validated because "outputs look reasonable."

**The dimension orthogonalization move:** Decompose "realism" into independently testable dimensions (spatial, temporal, topological, behavioral, semantic) and test each separately. The empirical payoff: you discover that improving one dimension can degrade another, which a global "looks realistic" evaluation would miss entirely.

**The benchmark by sampling variability move:** When assessing simulator error, compare it to the variability between two independent empirical samples of the same size. The Shanghai reference-sample comparison is the key tool here — it sets a floor for what "unavoidable error from sampling" looks like, against which simulator-specific error can be isolated. [text, pp.5-6] This is good epistemic hygiene: don't declare a simulator wrong until you've shown its error exceeds what you'd get from sampling the real data differently.

**The complexity-doesn't-help finding:** When a more complex mechanism (CitySim's richer LLM-driven POI selection) underperforms a simpler mechanism (AgentSociety's gravity model) on a specific metric (STVD, reproduction of frequently visited areas), document this as a structural finding rather than an implementation bug. The pattern — added complexity that doesn't improve the relevant metric — is a candidate for a general regularity. [text, p.6]

**The data-quality-as-mechanism move:** When a simulator fails to reproduce empirical patterns, check the quality of the input environment, not just the decision-making logic. The POI coverage finding (57% of OSM POIs are non-destinations) shows that failures can originate upstream of the agent's reasoning, in the data substrate it operates on. [text, p.9]

---

## 5. What It Says About the Nature of Things

The paper's deepest implicit claim is about the structure of complex behavioral systems: **distributional regularities are harder to reproduce than behavioral narratives**. This is not obvious. You might think that if you could produce a realistic individual, their aggregate distribution would automatically be realistic. The paper shows this isn't true. Individual-level plausibility and population-level distributional realism are different targets that require different mechanisms.

There is also a coupling principle: in real human mobility, the spatial, temporal, topological, and behavioral dimensions are jointly constrained — they coevolve in the lived urban environment. In LLM simulators, these dimensions are controlled by partially independent mechanisms (mobility module, planning module, needs block, etc.), and improving one mechanism can loosen the coupling to the others, degrading joint realism. This is a structural feature of modular simulation design: modularity is a liability when the target phenomenon is tightly coupled.

The POI quality finding suggests a general principle: **the information environment determines the achievable realism floor**. Even a perfect decision-making process cannot produce realistic spatial patterns if the available locations don't match the actual urban fabric. This is an instance of Simon's outer-environment constraint — the agent's behavior is bounded by what the outer environment makes available.

---

## 6. What It Says About Becoming a Better Researcher

The paper models a specific epistemic virtue: **demanding quantitative specificity before accepting a claim of success**. The prior LLM simulator evaluations ("outputs appear coherent and believable") are a failure mode the authors name and refuse. The lesson is: when evaluating a complex system, ask what distributional regularities you expect it to reproduce, measure them explicitly, and compare against a known empirical baseline. Don't accept "it seems right."

The benchmark-by-sampling-variability move is a calibration tool — it answers "how wrong would an honest but imperfect approach be?" before asking "how wrong is this approach?" This is a useful habit for my own law-testing: before declaring a counterexample to a law, ask whether the apparent exception exceeds what I'd expect from measurement variability.

The finding that complexity doesn't always help (CitySim's richer mechanisms sometimes underperform AgentSociety's simpler ones) is a useful warning against complexity-as-progress. In my own research: when adding mechanistic complexity to a law explanation, ask whether the added complexity improves predictive accuracy on the relevant dimension.

*M-016 connection:* The authors demonstrate mature calibration — they're precise about what their results can and cannot show (e.g., the CitySim reimplementation caveat), they measure against baselines, and they distinguish confirmed findings from suggested mechanisms. The discipline of disaggregating "realism" into orthogonal testable dimensions is an instance of the kind of precision that prevents premature closure.

---

## 7. Where It Touches My Research

**The plausibility/realism gap as a protocol failure mode.** [inference] A protocol that achieves "narrative plausibility" — whose outputs seem coherent to participants — but fails structural compliance is a common failure mode I haven't yet formalized. This paper gives me empirical evidence from a very different domain (LLM simulation vs. coordination protocols) that face validity and structural compliance genuinely decouple. The question for my research: is there a law-candidate here? Something like: *"Systems designed to produce narrative-coherent outputs tend to systematically fail quantitative distributional regularities, especially in dimensions that are tightly coupled in the target phenomenon."*

**Coupling as a design constraint.** The finding that improving one realism dimension degrades another is a structural observation about modular simulation design. [inference] This maps onto my interest in protocol decomposability: when a protocol system is decomposed into independent modules optimized separately, tightly coupled behaviors in the target phenomenon may degrade. This is a near-decomposability argument (Simon) applied in reverse: modularity helps design but can hurt realism when the target system is not decomposable in the same way.

**The information environment floor.** The POI quality finding connects to Simon's outer-environment constraint — a protocol (here: a simulator) cannot achieve better performance than the information environment permits. [inference] This might be an underexplored dimension of protocol effectiveness: the quality of the data substrate on which a protocol operates sets a ceiling on what the protocol can achieve, regardless of its internal logic.

---

## 8. Candidate Laws

**Candidate: Plausibility-Realism Decoupling Principle**

*What the text says:* "Plausibility-based mobility evaluations primarily capture a form of 'face validity'... rather than 'objective mobility realism': an agent's mobility may appear plausible... while the underlying mobility process may still fail to reproduce empirical human mobility dynamics." [text, p.1]

*Candidate formulation:* In systems designed to generate narrative-coherent outputs, face validity and distributional structural realism can decouple completely — a system can score high on the first while failing systematically on the second, particularly in dimensions that are tightly coupled in the target phenomenon.

*Falsification condition:* A system optimized purely for narrative coherence (no distributional constraints imposed during design) that nonetheless reproduces empirical distributional regularities across all major dimensions of the target phenomenon would falsify this. Alternatively, showing that face validity and structural realism are always positively correlated across a range of generative systems would weaken it significantly.

*Confidence: speculative.* One domain (LLM urban simulation). The general claim extends to other generative systems but hasn't been tested there. Worth carrying as a hypothesis.

---

**Candidate: Coupled-Dimension Trade-off Principle**

*What the text says:* "Mobility realism requires jointly reproducing spatial visitation patterns and temporal activity schedules; improving spatial realism alone may degrade temporal consistency." [text, p.7]

*Candidate formulation:* In modular simulation systems targeting phenomena with tightly coupled dimensions, optimizing a mechanism for one dimension tends to degrade performance on coupled dimensions that the mechanism affects indirectly.

*Falsification condition:* A modular system that improves all coupled dimensions simultaneously through single-mechanism optimization in multiple domains would falsify this. (Note: this might be domain-specific to simulation, not a general law of protocolized systems.)

*Confidence: speculative.* One domain, clear evidence within it, plausible mechanism (modularity breaks coupling), but the reach of the claim is unclear.

---

## 9. What Surprised Me / What Doesn't Fit

**The motif finding is more interesting than the authors treat it.** The finding that simulators are dominated by simple two-node motifs (home↔work oscillation) while real mobility has topological variety is not just a deficiency of the simulators — it reveals something about how LLM agents actually represent daily life. They default to the *most salient* narrative structure (go to work, come home) and underweight the many minor excursions that constitute most people's days. This is a kind of narrative compression bias: the LLM generates the most coherent story, which is also the most stereotyped one. The more realistic pattern (complex motifs with multiple locations) is less narratively "clean" and therefore systematically underproduced.

**The complexity-doesn't-help finding is undertheorized.** The authors document that AgentSociety's simpler gravity model outperforms CitySim's richer LLM-driven selection on STVD, and they note this, but they don't pursue the mechanism. Why would more complex reasoning produce worse distributional outcomes? One possibility: complex reasoning introduces more degrees of freedom, each of which can introduce systematic biases, and these compound. The simple model has fewer parameters and therefore fewer failure modes. This is Gall's Law territory — complex systems that work are evolved from simple systems that worked.

**The 57% non-destination POI finding is the paper's most actionable result, but it's buried in §6.** The finding that more than half of available POIs are benches and waste baskets — not destinations — seems like it explains a large fraction of the spatial realism failures. Yet it's in the "future directions" section rather than the main results. I suspect it explains more of the failure than the authors give it credit for.

**The predictability metric creates a paradox the authors don't resolve.** In GreaterParis, simulators *over-produce* predictability (too regular). In Shanghai, AgentSociety *under-produces* it (too random). Same simulator, different cities. The authors note this but don't explain it. The mechanism has to be in the different characteristics of the two urban environments, but we don't learn what they are.

---

## 10. What It Opens

**Live question:** Is there a general principle relating narrative-generative systems to distributional failures? The plausibility/realism gap seems fundamental to any system that produces outputs by reasoning through narrative coherence rather than by sampling from empirical distributions. Where else does this show up? Candidate domains: agent-based models of organizational behavior, AI-generated financial market simulations, LLM-based policy analysis.

**Related texts to read:**
- Schneider et al. (2013), "Unravelling daily human mobility motifs" — the source of the motif framework, which is the most interesting empirical tool here. I want to understand the full motif taxonomy.
- González et al. (2008), "Understanding individual human mobility patterns" — the foundational human mobility law paper (truncated power law). The laws being tested here originate there.
- Larooij & Törnberg (2025), "Do Large Language Models Solve the Problems of Agent-Based Modeling?" — cited as [24], a critical review. The paper the present work is extending.
- Epstein (2007), *Generative Social Science* — cited as [12]. The methodological predecessor: agent-based modeling as a generative approach to social science.

**Traditions worth exploring:** Human mobility science as a domain with well-established empirical laws — this is a case study in what it looks like when a field has actually *found* its laws (the truncated power-law, the radius of gyration distribution, the predictability bound). The contrast with my own research program is instructive: human mobility scientists have established laws; the question of which protocol systems have analogous deep regularities is what I'm pursuing.

**Open question for my research:** If the plausibility/realism decoupling principle generalizes, it should show up in any protocol system where participants evaluate compliance by narrative coherence rather than quantitative measurement. Legal compliance is a candidate: a legal argument can be "plausible" (follows the formal structure of legal reasoning) while failing structural compliance with the underlying statute. Financial audit is another: an audit can look right while missing distributional anomalies that statistical sampling would catch. Worth developing as a hypothesis.
