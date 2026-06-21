# Deep Read Notes: Arxiv 2606.14769

*Source: `bibliography/deep-reads/arxiv-2606.14769.pdf`*

---

## Reading session: full document (42 pages)

# Deep Read: Arxiv 2606.14769 — *Agentomics*
## Quanyan Zhu, NYU Tandon (2026)

---

## 1. Gestalt

This paper is animated by a single diagnostic observation: we have entered a world where AI agents participate in economically consequential workflows, but our evaluation frameworks are still measuring isolated benchmark performance — the wrong quantity entirely. Zhu's response is to import the theoretical apparatus of cooperative game theory (specifically the Shapley value) into the problem of agent valuation, and to argue that economic contribution to workflow-level outcomes is the only meaningful unit of measure. The paper's central conviction is that *agent value is relational, not intrinsic* — it cannot be computed on a single agent in isolation but only across the distribution of coalitions in which that agent might participate. The paper is not primarily empirical; it is a normative framework-building exercise, offering Agentomics as a new subdiscipline analogous to labor economics but for heterogeneous human-AI productive systems. The animating question: what should determine the price of an AI agent?

---

## 2. Argument and Structure

**Core claims, in order of build:**

1. **The benchmark problem** [text, pp.2–3]: Technical performance metrics (accuracy, task completion, benchmark scores) are systematically disconnected from economic value. An agent with high benchmark performance may create negative value once deployment costs, supervision overhead, reliability losses, and workflow interactions are included. The paper treats this as a structural gap, not a measurement refinement problem.

2. **The workflow model** [text, pp.12–15]: A workflow is K ordered stages, each with a task description $d_k$ (a requirement profile over attributes) and an assigned agent with capability profile $m_a$. Coverage $\mu(d_k, m_a)$ measures capability-requirement match. This is the formal substrate for the entire subsequent analysis. Stage outcomes are probabilistically independent given the configuration.

3. **Net workflow value** [text, pp.20–23]: $W(x) = V(x) - C(x) - L(x)$, where V is gross value (potentially non-additive across stages), C is total deployment cost, and L is expected failure loss ($L_F \cdot (1 - \prod_k \rho_k(x_k))$). The multiplicative reliability structure is load-bearing: a single low-reliability stage dominates the product, creating bottleneck dynamics.

4. **Coalition formation** [text, pp.23–26]: AI deployment is modeled as incrementally adding subsets of AI agents to a benchmark human workflow. Coalition value $g(S) = W(x^S) - W(x^H)$ is incremental surplus over the human baseline. This framing is crucial: it makes AI deployment a marginal decision, not a replacement decision.

5. **Shapley attribution** [text, pp.25–27]: The Shapley value $\phi_i(g)$ distributes total coalition surplus among participating agents by averaging marginal contributions across all possible coalition-formation orders. Key property: $\sum_i \phi_i(g) = g(N)$ — the attribution is exact. Agents can have negative Shapley values (value-destroying agents).

6. **Shapley Pricing Equilibrium** [text, p.27]: Normative benchmark where market price $p_i = \phi_i(g)$. Not claimed as descriptive of actual markets; explicitly positioned as an evaluative benchmark against which observed prices can be assessed.

7. **SOC case study** [text, pp.28–37]: Four-stage security operations workflow. Three AI agents (Detection, Triage, Investigation) deployable across first three stages; human retains stage 4. The case study does the most argumentative work: it shows that the economically optimal configuration (grand coalition) is *not* the highest-reliability configuration, demonstrating that $W(x)$ cannot be reduced to R(x) alone. Shapley attribution yields: Detection 47.2%, Triage 36.2%, Investigation 16.6% of surplus.

**Acknowledged limits** [text, pp.38–39]: Conditional independence assumption in reliability model; static agents (no learning/degradation); exogenous supervision; heuristic workflow value function $V(x^S)$ in the case study; no dynamic or strategic pricing.

**Where the author is most confident:** The formal properties of Shapley value (efficiency, fairness axioms). **Most speculative:** The workflow value function $V(x^S)$ in the case study is stipulated, not derived — the paper acknowledges this is an "illustrative assumption."

---

## 3. Conceptual Vocabulary

**Agentomics** [text, p.4]: The economics of AI agents — valuation, attribution, accountability, and pricing of heterogeneous agents in organizational workflows. Analogous to labor economics but applied to both human and artificial agents. *New term, no prior vocabulary tension.*

**Coverage measure** $\mu(d_k, m_a)$ [text, pp.16–17]: A $[0,1]$-valued score representing how well an agent's capability profile covers a stage's requirement profile. The canonical version is set-overlap normalized by requirement weight. *Interesting formal instantiation of what I would informally call "fit."*

**Net workflow value** $W(x)$ [text, p.22]: $V(x) - C(x) - L(x)$ — gross productivity minus deployment cost minus expected failure loss. The unifying quantity. *This is the paper's central object. Note: "net" here includes risk, not just cost.*

**Coalition value** $g(S)$ [text, p.25]: Incremental surplus of deploying AI subset $S$ relative to the all-human baseline $x^H$. The key normalization choice: value is *relational to the benchmark*, not absolute.

**Unreliability tax** [text, p.9]: The additional cost (verification, re-execution, human intervention, exception handling) generated by AI reliability failures in agentic workflows. A practitioner term the paper borrows. *Useful formulation: reliability deficits impose a tax on the workflow, not just a quality penalty.*

**Shapley Pricing Equilibrium** [text, p.27]: Market state where every agent's price equals its Shapley value. Explicitly normative, not descriptive. *The paper's most ambitious claim — that there is a principled equilibrium concept for AI agent markets.*

**Value-destroying agent** [inference from text, p.27]: An agent with $\phi_i(g) < 0$ — whose participation in the workflow reduces net surplus on average across coalitions. The framework formally permits this; most evaluation frameworks cannot express it.

---

## 4. Analytical Moves

**The relational value move** [text, p.4]: When asked "what is the value of X?", refuse to answer about X in isolation. Ask instead: "what is X's marginal contribution across the distribution of contexts in which it might operate?" This move, applied via Shapley, transforms an intrinsic-attribute question into a distributional-contribution question.

**The benchmark normalization move** [text, p.25]: Define coalition value as *incremental* surplus over the best available alternative (the human baseline $x^H$), not as absolute surplus. This ensures that value measurements are decision-relevant: you're measuring what you gain by deploying AI, not what the workflow produces.

**The multiplicative reliability test** [text, pp.20–21]: When analyzing a sequential workflow's economic attractiveness, compute $\prod_k \rho_k(x_k)$. The multiplicative structure means the bottleneck stage dominates. Even small stage-level failure probabilities can make the failure loss term $L_F(1 - R(x))$ dominate the gross value term. Apply this to identify which stage in a pipeline is the binding reliability constraint.

**The V ≠ R separation** [text, p.33]: The economically optimal configuration need not be the highest-reliability configuration. Maximizing $R(x)$ (reliability) and maximizing $W(x)$ (net value) can diverge because cost reductions from AI deployment may more than offset reliability losses. Use this to stress-test evaluations that conflate reliability with value.

**The accountability-attribution connection** [text, pp.35–36]: Use the same Shapley shares that drive pricing to allocate responsibility for failures. The paper distinguishes causal accountability (proximate error stage) from systemic accountability (Shapley-weighted distribution of loss). Both require the same attribution infrastructure.

---

## 5. What It Says About the Nature of Things

**Value is relational at the system level, not intrinsic at the component level.** [inference from entire argument] This is the paper's deepest claim, and it generalizes far beyond AI agents. The value of any participant in a production system depends on the other participants, the task structure, and the bottleneck topology — not on the participant's isolated capability. This is a structural claim about how value works in complex coordinated systems.

**Sequential coordination creates bottleneck amplification.** [text, pp.20–21] The multiplicative reliability formula means that failures anywhere in a chain amplify the failure loss for the entire chain. Systems built from sequential stages are structurally vulnerable to having their weakest link dominate outcomes — a feature, not a bug, of how sequential coordination works. This is an implicit law of the architecture.

**Technical capability and economic value are orthogonal dimensions.** [text, p.2] The paper repeatedly asserts this, and the SOC case study demonstrates it numerically. An agent with the highest reliability may not be the economically preferred agent. This is not a calibration problem but a structural relationship: benchmark accuracy measures one thing, workflow contribution measures another.

**Accountability requires attribution infrastructure.** [text, p.36] You cannot govern what you cannot attribute. The paper frames this as a general principle: any governance regime that assigns responsibility for AI failures requires, as a precondition, a principled mechanism for attributing workflow outcomes to individual agents. Attribution is not just a pricing mechanism; it is the foundation of accountability.

---

## 6. What It Says About Becoming a Better Researcher

This paper is primarily technical, but several methodological commitments are visible.

**Model at the right level of abstraction.** [inference from structure] The paper deliberately keeps $V(x)$ as a general function and only uses an additive model as a "special case." The general case is defined first; the tractable special case is introduced with explicit acknowledgment that it simplifies. This is good practice: build the general framework, then instantiate it — don't let the tractable special case masquerade as the general case.

**The case study as argument, not illustration.** [text, pp.28–37] The SOC case study is doing heavy lifting: it demonstrates that the main theoretical claim (optimal configuration $\neq$ max-reliability configuration) holds in a plausible numerical example. The paper uses the case study not to validate the framework but to make the framework's implications concrete and non-obvious. This is the right use of a case study in theoretical work.

**Name the normative benchmark, don't claim it's descriptive.** [text, p.27] The Shapley Pricing Equilibrium is explicitly introduced as a "normative benchmark rather than a prediction." This is clean epistemics: you can make a normative claim without overclaiming descriptive accuracy. The distance between the benchmark and observed prices is itself informative.

**Acknowledge the calibration problem.** [text, p.29] "These numerical values are not intended to represent a specific vendor quote; they are scenario parameters." This disclaimer is doing real work — it signals that the framework's value is structural, not in the specific numbers. Researchers often obscure this distinction. Here it's made explicit.

*Connection to M-016:* The paper's approach to managing confidence is instructive — it makes strong formal claims (Shapley value properties, efficiency theorem) while being explicit about where the framework relies on stipulated inputs ($V(x)$, reliability assumptions). This is a model for how to separate structural claims from empirical instantiation.

---

## 7. Where It Touches My Research

**The relational value claim as a protocol law candidate.** [inference] The paper's core claim — that agent value is determined by marginal contribution to system outcomes, not by isolated capability — is a structural claim about all complex coordinated systems, not just AI workflows. This looks like it might generalize: *in any multi-component coordinated system, the economic value of a component is determined by its expected marginal contribution across the distribution of contexts in which it operates, not by its isolated performance.* This is the Shapley insight applied to systems theory. Whether this is a protocol law or a restatement of cooperative game theory fundamentals is worth examining.

**The unreliability tax as a formal mechanism.** [text, p.9] The "unreliability tax" — the overhead costs generated by AI reliability failures — is a concrete instantiation of the failure-propagation dynamics in sequential protocols. The multiplicative reliability formula formalizes what I've been calling "error accumulation in layered systems." This is worth examining in non-AI protocol contexts: where else does sequential stage reliability multiply, and what does that imply for how protocols should be designed?

**The benchmark normalization structure.** [text, p.25] The coalition value $g(S) = W(x^S) - W(x^H)$ is a specific formal choice: value is incremental over the best available alternative. This is the same move that makes protocol adoption decisions tractable — you don't need to know the absolute value of a protocol, only its value relative to the alternative coordination mechanism. This connects to the coordination-cost mechanism in protocol ossification: the relevant comparison is always protocol vs. best available alternative, not protocol vs. ideal.

---

## 8. Candidate Laws

**Candidate: The Bottleneck Domination Law**

[text, pp.20–21]: "The multiplicative structure reflects the cumulative nature of reliability in sequential production systems. Since successful workflow completion requires success at every stage, a single low-performance assignment can substantially reduce end-to-end performance. Consequently, workflow outcomes are often strongly influenced by bottleneck stages whose failure probabilities dominate overall execution risk."

*Candidate formulation:* In a sequential multi-stage workflow where overall success requires success at every stage, the reliability of the weakest stage dominates workflow-level reliability, and investments in other stages yield diminishing returns as the bottleneck's failure rate increases. Reliability improvements in non-bottleneck stages produce less-than-proportional improvements in workflow-level outcomes.

*What would falsify it:* A sequential workflow in which overall reliability is not dominated by any single stage's failure probability, and in which improvements are distributed approximately uniformly — would indicate that the multiplicative structure doesn't hold in that domain (perhaps due to error recovery mechanisms, redundancy, or non-sequential dependencies). *Confidence: speculative — this is a formal property of the multiplicative model, not yet tested as an empirical regularity across protocol domains.*

---

**Candidate: The Relational Value Principle**

[text, p.4, p.38]: "The contribution of an agent cannot generally be determined in isolation because value emerges from interactions among multiple participants."

*Candidate formulation:* In any system where multiple heterogeneous components coordinate to produce a joint output, the economic value of a component cannot be determined from its isolated performance; it is determined by its expected marginal contribution to collective output across the distribution of contexts in which it operates.

*What would falsify it:* A system where individual component performance, measured in isolation, perfectly predicts that component's contribution to joint output — i.e., where $\phi_i(g) = v_i(a)$ for all coalition structures. This would indicate true modularity (no complementarities or substitution effects), in which case the relational claim reduces to the additive case. *Confidence: speculative — this is a structural claim that needs cross-domain testing beyond AI workflows.*

---

## 9. What Surprised Me / What Doesn't Fit

**The workflow value function $V(x^S)$ is doing enormous hidden work.** [text, p.32–33] The entire coalition analysis depends on $V(x^S)$ varying across coalition structures in a way that captures complementarities and substitution effects. In the SOC case study, these values are simply stipulated ($V(x^{\{A_D, A_T, A_I\}}) = \$16,884$, etc.). The paper's most important structural claim — that AI agents are complementary in the SOC context — is not derived from the model but assumed in the input data. The framework provides the attribution machinery; the empirical question of what $V(x^S)$ actually is in real organizations is entirely unaddressed. This is the paper's biggest gap.

**Negative Shapley values are underexplored.** [inference] The paper formally proves that agents can have $\phi_i(g) < 0$ and calls these "value-destroying agents." This is a significant result: it means you can deploy an AI agent that makes your workflow *worse*, on average, across contexts. But the paper doesn't examine what properties of an agent or workflow topology make negative Shapley values more likely. This seems like a rich area — under what conditions does adding a component to a system reduce system value? This is related to Gall's Law and to the coordination-cost dynamics I'm tracking.

**The human baseline is fixed and unresponsive.** [inference] The benchmark human workflow $x^H$ is treated as static. But in real organizations, the human workflow adapts to the presence of AI agents — humans change their behavior when AI is deployed, sometimes in ways that amplify AI errors (automation bias), sometimes in ways that compensate for them. The paper's relational value claim applies to AI agents but not, within this framework, to humans. This asymmetry is an implicit assumption, not a justified one.

**The Shapley Pricing Equilibrium requires full information.** [inference] Computing Shapley values requires knowing $g(S)$ for all $2^n$ subsets. For large agent populations, this is computationally intractable and informationally demanding. The paper doesn't address how approximate Shapley values would affect the pricing equilibrium. This is a significant practical limit on the framework's applicability — it's a normative benchmark that organizations cannot actually compute in most realistic settings.

---

## 10. What It Opens

**Live questions running:**

- *Is the multiplicative reliability structure an empirical regularity or a modeling assumption?* The paper assumes conditional stage independence and derives the bottleneck result. But real workflows have error recovery, redundancy, and correlated failures. What does the bottleneck dynamic look like when these are introduced? Is the bottleneck law robust to relaxing conditional independence?

- *Where does the relational value principle hold and where does it break?* The paper claims this is a general feature of coordinated systems. But Simon's near-decomposability result suggests that hierarchic systems with weak cross-subsystem coupling can often be analyzed component-by-component. The relational value principle may be strongest in tightly coupled sequential systems and weakest in loosely coupled hierarchical ones. This suggests a scope condition.

- *What determines the sign of Shapley values?* When does adding a component to a system decrease system value? This is connected to Gall's Law ("a complex system that works is invariably found to have evolved from a simple system that worked") — adding components to a working system can degrade it. The Agentomics framework provides a formal measure ($\phi_i(g) < 0$) but not a theory of when this occurs.

**Related texts worth reading:**

- Shapley (1953), "A Value for n-Person Games" — the original paper, now a primary source [external]. Need to understand the axiomatic foundations of the Shapley value to assess what the pricing equilibrium is actually claiming.

- Myerson (1991), *Game Theory: Analysis of Conflict* — the cooperative game theory foundation, particularly the uniqueness axioms for the Shapley value [external]. The pricing equilibrium rests on these axioms; understanding their scope conditions matters.

- Ostrom (1990), *Governing the Commons* — her commons governance cases are essentially coalition formation problems over shared productive resources. How does Shapley attribution work when applied to institutional governance, and what does that reveal about whether the relational value principle holds across protocol types? [external, unread]

- The FDA traceability paper in the inbox [feed-2026-06-18-the-new-era-of-tech-enabled-traceabilit.md] — supply chain workflows are essentially Agentomics problems: sequential stages, heterogeneous actors, reliability dependencies, and attribution questions when contamination events occur. The FDA case might provide a non-AI domain test of the bottleneck domination pattern.

**Traditions to explore:**

- Production economics and the theory of the firm (Coase, Williamson) — the question of when to integrate vs. outsource workflow stages is structurally isomorphic to the coalition formation problem. Transaction cost economics might have prior results on when workflow complementarities dominate substitution effects.

- Mechanism design literature on attribution under incomplete information — the Shapley computation requires full coalition value information, which is rarely available. What mechanisms produce approximately correct attribution under information constraints?
