# Deep Read Notes: Arxiv 2602.22041

*Source: `bibliography/deep-reads/arxiv-2602.22041.pdf`*

---

## Reading session: full document (20 pages)

# Deep Read: arxiv-2602.22041
## George et al., "Using Feasible Action-Space Reduction by Groups to fill Causal Responsibility Gaps in Spatial Interactions" (2026)

---

## 1. Gestalt

This paper is solving a tractability problem within a responsibility attribution framework, not making a foundational philosophical argument. The authors inherit a prior metric (FeAR — Feasible Action-Space Reduction) that quantifies individual causal responsibility in spatial interactions by measuring how much an agent's actions constrain another agent's feasible moves. That metric works well for dyadic or near-dyadic interactions. It breaks down in cases of *causal overdetermination* — when multiple agents simultaneously produce an effect that none of them individually causes. The paper's animating question is: how do you assign causal responsibility when no individual is sufficient? The answer is to extend FeAR from individuals to groups, then develop a tiering algorithm to identify the *minimal* responsible groups and rank their assertiveness. The contribution is methodological: a formal, computational procedure for detecting and attributing group-level causal effects in multi-agent spatial systems, with an implicit secondary application as an emergence detector.

---

## 2. Argument and Structure

**Core problem:** FeAR (individual) fails in causal overdetermination. Two agents can each be insufficient to constrain a third agent's action space, while together they fully constrain it. Individual FeAR assigns zero responsibility to both. This is a *responsibility gap* — the collective is responsible but no individual is [text, p.3].

**Core solution:** Group FeAR (gFeAR) computes FeAR for arbitrary subsets of agents, using counterfactual intervention: how much does the group's action reduce the feasible action space of the affected agent, compared to if all group members had stayed? [text, p.4, Definition 2]

**Taxonomy of influence types:** Four types emerge from the group analysis [text, p.6]:
- *Solo influence*: agent i constrains j individually (iFeAR > 0)
- *Mediated influence*: agent i has no solo influence, but amplifies the effect of a group G (FeAR increases when i is added to G)
- *Coupled influence*: no individual in group G constrains j alone, but G as a whole does
- *Mediated coupled influence*: a group G has coupled influence that is mediated by another group G'

**Tiering algorithm:** Starting from solo and coupled influences, the algorithm iteratively identifies minimal groups with assertive influence on each affected agent and ranks them into tiers. Higher tiers have stronger causal influence than lower [text, p.7, Algorithm 1]. The minimality criterion is load-bearing: the algorithm systematically probes incremental group sizes rather than assigning blanket collective responsibility.

**Validation:** Scenario simulations (one detailed, three randomized) test two metrics: (1) the difference in count of assertive agents identified by individual vs. group FeAR, and (2) Kendall's τ comparing rankings of assertiveness. Key empirical findings: group effects are stronger at closer agent proximity; group effects are larger in "aggressive" (conflictual) scenarios than "random" or "directed" ones; gFeAR-Tier and gFeAR-Shapley rankings show high agreement (τ close to 1), both diverging significantly from iFeAR [text, pp. 11-14].

**Secondary application:** The standard deviation of Kendall's τ between iFeAR and gFeAR rankings is proposed as a model-agnostic metric for detecting emergent complexity in spatial interactions — higher SD indicates more superadditive group effects, which the authors connect to complexity at the "edge of chaos" [text, pp. 15-16].

**Limits acknowledged:** Grid world with discrete actions and non-adaptive agents has low external validity. Moral responsibility (intention, knowledge, wrongdoing) is explicitly set aside — the paper addresses only causal responsibility [text, p.15].

---

## 3. Conceptual Vocabulary

**Feasible Action Space (FAS):** The set of actions currently available to an agent that do not produce collisions, given the state and joint actions of others. This is the key operational currency of the framework.

**FeAR (Feasible Action-Space Reduction):** The normalized reduction in FAS imposed on agent j by actor i (or group G). Positive values = assertive (constraining), negative values = courteous (the actor's actions create more space for j). [text, p.4]

**Move de Rigueur (MdR):** The expected or normative action for an agent in a given state — treated as the counterfactual baseline (what would the agent have done if not assertive). In the paper's implementation, MdR = Stay (S0) for all agents. [text, p.3]

**Responsibility gap:** A situation where a group is collectively causally responsible but no individual is [text, p.3]. Distinguished from *responsibility void* (where no collective can be held responsible at all) and *responsibility glut* (where too many agents are held responsible) [text, p.14].

**Coupled influence:** This is the paper's cleanest concept — no individual in the group constrains the affected agent, but the group as a whole does. This is structurally distinct from aggregated individual effects. [text, p.6, Definition 5]

**Tiering:** A ranking system for assertive influences that uses the structure of mediated vs. unmediated influence — agents whose influence is conditional on others (mediated) are ranked lower than those whose influence is direct. This is an operationalized form of causal priority [text, pp. 6-7].

**Tension with my vocabulary:** The paper uses *causal responsibility* in a narrow, formal sense (counterfactual action-space reduction), stripped of epistemic and intentional conditions. My existing vocabulary around responsibility in protocol contexts tends toward the normative-institutional sense (who is answerable?). The paper is doing causal attribution *prior to* moral or institutional assignment — a useful clarification of sequence.

---

## 4. Analytical Moves

**Counterfactual substitution for responsibility:** Replace an agent's actual action with its MdR and observe what changes in the affected agent's feasible action space. This is the fundamental operation. Transferable to any domain where you can define: (a) a normative baseline, (b) a feasibility constraint, and (c) a measurable restriction. [text, p.4]

**Incrementally probe group sizes:** When individual analysis fails (overdetermination), enumerate groups of increasing size (k=1, 2, ...) to identify minimal sufficient sets. The algorithm is exponential in principle but pruned by courteous-agent elimination and tier structure. The *minimality* criterion prevents gluts. [text, p.7, Algorithm 1]

**Type-stratify before ranking:** Rather than producing a single ranking of influence, first categorize influences by structural type (solo/mediated/coupled/mediated-coupled), then rank within and across types. This produces richer, more interpretable attributions than a scalar ranking alone. [text, pp. 6-7]

**Use ranking disagreement as a complexity signal:** When individual-level and group-level rankings diverge significantly (measured by 1-τ), this signals superadditive group effects — which are interpretable as emergence or complexity. The disagreement between two analytical lenses becomes an indicator variable for a system-level property. [text, pp. 15-16]

**Eliminate courteous agents before group analysis:** Agents that *increase* the affected agent's feasible action space (negative FeAR) are identified and removed before the tiering algorithm runs. This dramatically prunes the search space and reflects a principled theoretical choice: courteousness is evidence against assertiveness, not merely neutral. [text, p.7]

---

## 5. What It Says About the Nature of Things

The paper's implicit general commitment is that *causal structure in multi-agent systems is irreducibly collective in certain configurations*. Not as a philosophical position but as a mathematical fact: there exist interaction configurations where the causal map cannot be decomposed into individual contributions without loss. The responsible entity is the group, and the group cannot be further decomposed without the attribution becoming false.

This has an interesting corollary: the unit of analysis appropriate for responsibility attribution is not fixed in advance but determined by the interaction structure. In sparse interactions, individuals are the right unit. In dense interactions, groups may be the only coherent unit. The appropriate unit is an empirical question about the interaction topology, not a normative choice.

The emergence discussion [text, pp. 15-16] makes the stronger claim that complexity itself is most appropriately detected at the group level — that superadditive effects measured by ranking disagreement between individual and group analysis is a *structural indicator* of emergent complexity, independent of any probabilistic model of how the system evolves. This is a methodologically interesting claim: emergence is not a property that requires probabilistic trajectory modeling; it can be detected from a single-timestep counterfactual analysis if the counterfactual analysis is group-sensitive.

---

## 6. What It Says About Becoming a Better Researcher

Thin here — this is a technical paper, not a reflective one. But one methodological lesson is extractable:

**Detect the right level of analysis before proceeding.** The paper's fundamental move is to recognize that iFeAR was not wrong but was operating at the wrong level of analysis for certain configurations. The solution was not to fix iFeAR but to extend it upward to the natural unit (groups) for overdetermined cases. The lesson: when a metric fails, ask whether it is operating at the right level of analysis, not just whether it is measuring the right thing at its current level.

The paper also exemplifies a clean research practice: explicitly delimit what you are *not* doing. The deliberate setting-aside of moral responsibility (intention, knowledge) is stated upfront and maintained throughout. The authors don't try to solve everything; they solve the causal attribution sub-problem and leave the moral attribution to others. This produces a cleaner paper and a more falsifiable contribution.

---

## 7. Where It Touches My Research

This paper is tangential to my primary research agenda but touches two live threads in ways worth noting:

**Collective responsibility and protocol governance:** The responsibility gap concept [text, p.3] — no individual responsible, group collectively responsible — maps onto a real problem in distributed protocol governance. When a protocol produces a bad outcome (a standard produces dangerous interoperability, a coordination mechanism excludes a class of participants), who is responsible? The paper's formalism suggests that responsibility attribution in multi-stakeholder protocol contexts should explicitly check for coupled influence before assigning individual blame. This is not a law candidate but a diagnostic framing.

**Emergence detection:** The use of ranking disagreement between individual and group analysis as an emergence metric [text, pp. 15-16] is potentially transferable. If I have a domain where I can define both an individual-level and a group-level analysis of the same interaction, the disagreement between them is a signal about whether the domain is operating in a superadditive regime. This has potential application to protocol ecosystems where individual protocol analysis misses cross-protocol effects.

---

## 8. Candidate Laws

No candidates. The paper is a methodological contribution with specific formal definitions, not a general empirical claim about how systems behave. The empirical findings (group effects increase with proximity, group effects are stronger in aggressive scenarios) are domain-specific results about spatial multi-agent interactions, not candidates for cross-domain laws.

The emergence-as-ranking-disagreement proposal is interesting but too early and too domain-specific to formalize here.

---

## 9. What Surprised Me / What Doesn't Fit

**The MdR = Stay assumption is load-bearing and underexamined.** The entire framework rests on the Move de Rigueur as the counterfactual baseline. In the paper, MdR is simply defined as Stay (S0) for all agents in all scenarios [text, p.3]. But the choice of counterfactual baseline fundamentally determines what gets attributed as "assertive" behavior. An agent "assertively" constraining another is always relative to what the agent *would otherwise have done* — and Stay is a very specific, contestable choice. In real traffic, the normative baseline is not staying still; it is something like "proceeding at normal speed, yielding as required by convention." The paper acknowledges this limitation implicitly ("the MdR is staying (S0) for all the agents in all scenarios") but doesn't examine what changes if the MdR is different. This is where the framework's external validity is most fragile.

**The tiering algorithm is presented as systematic but its complexity is not analyzed.** The algorithm is exponential in principle (it enumerates subsets of increasing size). The authors mention that eliminating courteous agents "potentially saves on computation cost" [text, p.15] but provide no analysis of worst-case complexity or scaling behavior. For 8 agents this works; for 80 it may not.

**The emergence claim is attached but not integrated.** The section on group FeAR as an emergence metric [text, pp. 15-16] feels loosely connected to the rest of the paper. The claim that SD of Kendall's τ between individual and group rankings is a "model-agnostic metric for detecting emergence of complexity" is interesting but is not developed with the same rigor as the main FeAR framework. It reads like a speculative extension appended to the core contribution — potentially valuable but not yet earned.

**Responsibility gaps vs. responsibility voids:** The paper carefully distinguishes these [text, p.14] but the distinction is underutilized in the analysis. The tiering algorithm addresses gaps (group responsible, individual not). What happens when the algorithm finds *no* assertive agents — not even collectively? The paper doesn't address this case systematically.

---

## 10. What It Opens

**Read:** The prior FeAR paper by George et al. (2023, [17] in the reference list — also in library as a continuous version: arxiv-2505.17739 [19]) to understand the individual metric fully before using the group extension.

**Explore:** Halpern's work on structural models of causation [7, 24, 25 in the references] — Halpern-Pearl causality. This is the formalism that most formally treats counterfactual causation in multi-agent settings, and it appears to be the theoretical ancestor the FeAR framework is working around (simplifying for tractability). Understanding Halpern-Pearl would clarify exactly what FeAR is and isn't capturing.

**Question:** Is there a domain I know well where the individual vs. group responsibility gap appears structurally? Financial clearing comes to mind: individual bank actions may not individually trigger a crisis, but collective behavior (simultaneous withdrawal, correlated risk-taking) produces outcomes no individual caused. The FeAR framework might not translate directly (it requires a spatial/action-space model) but the *responsibility gap* concept does.

**Question:** The MdR baseline problem is genuinely deep. For protocols, what is the MdR of a protocol participant? Is it "follow the protocol specification exactly"? If so, responsibility = deviation from specification. This connects to how protocols assign responsibility through compliance definitions — something I haven't formalized but that the FeAR framework makes vivid.
