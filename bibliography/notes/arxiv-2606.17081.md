# Deep Read Notes: Arxiv 2606.17081

*Source: `bibliography/deep-reads/arxiv-2606.17081.pdf`*

---

## Reading session: full document (38 pages)

# Deep Read: Georgiou, "The Price of Anarchy in Disaggregated Inference" (arXiv 2606.17081)

---

## 1. Gestalt

This paper is doing something methodologically unusual: it is applying game-theoretic vocabulary to a production engineering system not to *compute* game-theoretic quantities at runtime (which is computationally infeasible) but to *name and measure* what the system is already doing. The animating problem is this: disaggregated inference—where LLM prefill and decode phases run on separate GPU pools—creates a natural multi-agent resource allocation problem, and the engineering community has been characterizing it with Pareto frontier analysis without realizing they were computing equilibrium properties. Georgiou's contribution is to name the three games hidden inside NVIDIA's Dynamo architecture, derive their equilibrium structure, and then measure an empirical Price of Anarchy index across two production-scale models. The central conviction is that *game theory's value for inference systems is analytical, not algorithmic*—it provides vocabulary, metrics, and regime analysis, not runtime computation. The paper's deepest result is not an optimization; it's a diagnosis: the PoA is stable below saturation and explodes above it, and this regime transition is the correct signal for adaptive control.

---

## 2. Argument and Structure

**Core architecture of the argument:**

The paper identifies three coupled games in Dynamo [text, p.1–2]:
- **Game 1 (Γ_PD):** Prefill and decode pools compete for a shared GPU budget. Modeled as a Generalized Nash Equilibrium Problem (GNEP) with shared constraint G_P + G_D ≤ G. Unique variational equilibrium exists where marginal SLO improvements are equal across pools [text, p.9].
- **Game 2 (Γ_KV):** GPU workers choose whether and where to cache KV blocks across a four-tier hierarchy (HBM → DRAM → SSD → networked). Selfish caching game with hierarchical topology. PoA = 1 on complete-graph (NVLink within node), potentially O(√n) on sparse topologies (InfiniBand across nodes) [text, p.10].
- **Game 3 (Γ_R):** Requests are routed to decode workers. Congestion game with a positive externality from KV cache overlap that breaks the potential game structure [text, p.11].

**Load-bearing example:** The routing game's cost function (Eq. 7) includes both a congestion term (latency as function of co-routed requests) and a cache externality benefit (overlap score × weight). The sign inversion between Dynamo's implementation and the paper's formulation is acknowledged—mathematically equivalent for argmin selection but conceptually revealing about what the system is trading off [text, p.11].

**The saturation analysis** is the empirical heart. Below saturation, latency functions are approximately linear; above saturation, they acquire a singular term at capacity (Eq. 9) that drives PoA divergence. This is not a discontinuity in the physical sense but a "rapid, practically significant degradation" [text, p.13]. The saturation proposition (Proposition 4) claims: (i) PoA is stable below saturation; (ii) PoA grows rapidly at saturation via two mechanisms—routing inefficiency amplified by superlinear latency, and resource allocation failure (prefill bottleneck); (iii) the transition is detectable via the second derivative of aggregate latency with respect to load [text, p.14].

**Key empirical findings:**
- Three-regime PoA structure (artifact → stable plateau → explosive growth) reproduced across both a 70B and 340B model, across three P/D topologies, despite 4.9× model size difference [text, p.24].
- Below saturation: PoA is *invariant* to router parameters (τ, ω). The cross-configuration spread is ≤ ±0.10 for the 340B and ±0.08 for the 70B across 16 parameter combinations [text, p.26].
- At saturation: parameter sensitivity emerges. Cross-configuration variance increases ~37–58× [text, p.27].
- The same first post-knee grid point (C = 128) appears for both models—explained plausibly by both using a single prefill worker on identical hardware with identical input lengths [text, p.33].
- Adaptive controller (detecting regime, switching parameters) reduces PoA 3.1× and achieves 29× TTFT improvement post-switch on 70B 1P/5D [text, p.29].

**Acknowledged limits:**
- Game 1 is analyzed analytically but never empirically validated (fixed P/D splits throughout)
- Workload is homogeneous (5 templates, 128 input tokens, deterministic generation) which may make Game 2 degenerate
- KV cache tier spillover never exercised (blocks always in HBM)
- PoA estimator uses uncalibrated cost model; values are regime indicators, not absolute efficiency ratios [text, p.19]
- Single-run measurements for Experiments 1, 2, 4a, 4b; only Experiment 3 has n=3 trials [text, p.23]

---

## 3. Conceptual Vocabulary

**Price of Anarchy (PoA):** Standard: ratio of social cost at worst Nash equilibrium to social cost at social optimum. Here applied mechanistically—the router is a *mechanism* whose greedy assignment mirrors best-response dynamics; PoA measures mechanism efficiency, not agent rationality [text, p.2, p.34].

**ˆPoA (empirical PoA estimator):** Distinguished explicitly from classical PoA bounds. Computed via Hungarian algorithm on frozen-latency cost matrix against actual routing outcomes. An *upper bound* on true PoA (because OPT is underestimated from frozen latencies), calibrated as a *relative regime indicator* rather than absolute efficiency ratio [text, p.19]. The paper is unusually careful here: "a PoA of 19 does not mean '19× worse than optimal' in system terms."

**Saturation knee:** The concurrency level at which latency transitions from approximately linear (stable PoA) to superlinear (growing PoA). Located in (96, 128] for both tested models—not resolvable at their grid spacing [text, p.25].

**Disaggregated inference:** Physical separation of LLM prefill (compute-bound) and decode (memory-bandwidth-bound) phases onto distinct GPU pools. Creates structural multi-agent dynamics because the pools optimize different objectives—TTFT vs. ITL [text, p.3].

**Regime transition:** The paper uses this term for what is technically a continuous but practically sharp change in the game's payoff structure at saturation. The latency function's singular term (Eq. 9) drives this. [text, p.13, with explicit caveat about continuity]

**Congestion game with positive externalities:** The routing game's enrichment over standard congestion games—KV cache overlap creates *identity-dependent* costs (request prefix matters), not just *count-dependent* costs. This breaks the anonymous-cost assumption and the potential game structure [text, p.11].

**GNEP (Generalized Nash Equilibrium Problem):** Nash equilibrium with shared strategy constraints. The P/D game is a GNEP because G_P + G_D ≤ G couples the feasible sets. The standard solution concept is the *variational equilibrium* [text, p.9].

**Variational equilibrium:** The standard selection for GNEPs with shared constraints—equalizes shadow prices across players. Here: equilibrium where marginal SLO improvement per GPU is equal for prefill and decode [text, p.9, Proposition 1].

*Tension with my vocabulary:* I use "protocol" loosely for coordination mechanisms. This paper distinguishes sharply between the *centralized mechanism* (the Smart Router) and the *game structure* it implements. The router is not a decentralized agent—it is a mechanism designer who happens to use best-response dynamics. This is a cleaner framing than I typically apply.

---

## 4. Analytical Moves

**Move 1: Naming the games hidden in existing architecture.**
Georgiou doesn't design a new system. He takes an existing architecture (Dynamo) and identifies the game-theoretic structure it already implements. The move: for each component (Planner, KVBM, Smart Router), ask: who are the players, what are the resources, what is the mechanism? This re-description is not cosmetic—it makes visible properties (PoA, equilibrium structure, coupling) that engineering analysis misses. Applicable anywhere: take an existing protocol/mechanism and ask what game it is implementing.

**Move 2: Analytical-not-algorithmic game theory.**
The move: use game theory to *characterize behavior and bound inefficiency* without computing equilibria at runtime. The resolution to PPAD-hardness is not approximation but reframing: "game theory provides the analytical vocabulary and fairness guarantees, but the runtime algorithm must be a tractable approximation" [text, p.2]. This licenses applying game theory to systems where real-time equilibrium computation is infeasible.

**Move 3: Regime detection as a proxy for equilibrium computation.**
Rather than computing Nash equilibria, classify which *regime* the system is in (below/transition/saturated) using observable metrics (EWMA of TTFT P99). Regime classification is a tractable approximation to the intractable problem of equilibrium computation. The controller then applies pre-computed regime-specific parameters. Applicable to any complex system where equilibrium computation is infeasible but regime transitions are detectable.

**Move 4: Decomposing a complex PoA into contributing mechanisms.**
At deep saturation, ˆPoA of 284 is not "284× suboptimal routing." It decomposes into: (a) routing inefficiency (bounded, manageable) and (b) resource allocation failure (dominant—prefill bottleneck that no routing decision can fix) [text, p.25]. The move: when a composite metric explodes, ask which component is driving it and whether that component is addressable at the current level of intervention.

**Move 5: Coupling topology as a source of cascade risk.**
The three games are not independent. Cache state changes overlap scores → routing decisions → cache pressure → Planner reallocation → changed routing game → potential oscillation [text, p.12, Figure 3]. The move: for any multi-component system, identify the coupling arrows between components and ask which direction the cascades flow and which cascade amplifies vs. dampens inefficiency.

**Move 6: Pareto frontier deformation at regime transitions.**
Below saturation, the frontier is flat and smooth (parameter configurations are nearly equivalent). At saturation, the frontier steepens and becomes parameter-sensitive ("rugged") [text, p.16]. The move: characterize not just where the Pareto frontier is but how it *deforms* as operating conditions change. A static deployment-time Pareto analysis is sufficient only when the frontier doesn't move.

---

## 5. What It Says About the Nature of Things

**Regime transitions are the productive unit of analysis, not steady states.** The paper's main contribution is not steady-state equilibrium analysis but characterization of the transition between regimes. The system spends time in transient states; designing for steady-state equilibrium misses where the action is. [inference from text, p.32: "Design for regime transitions, not steady state."]

**Greedy sequential assignment is best-response dynamics.** The equivalence between a centralized greedy mechanism and decentralized best-response play [text, p.2] is a general result (cited to Roughgarden [31]). This means: any greedy sequential allocation mechanism can be analyzed as a game, even if no agents are consciously playing. The mechanism-design framing is the correct lens for centralized protocols that implement resource allocation.

**Structural inefficiency from greedy routing is irreducible at the protocol level.** Below saturation, no parameter configuration reduces ˆPoA—the ~7-19× inefficiency relative to Hungarian-optimal is a structural cost of greedy routing, recoverable only by changing to batch assignment [text, p.26–27]. This is a specific instance of a general pattern: some inefficiencies are not addressable by tuning parameters of a fixed protocol; they require changing the protocol class.

**The topology of interconnects determines the PoA of caching games.** NVLink (near-complete graph within node) → PoA ≈ 1. InfiniBand (sparse across nodes) → potentially O(√n) [text, p.10]. This is a concrete instance of how physical infrastructure topology constrains the best achievable coordination efficiency—the game's PoA is bounded by the network topology.

**Saturation cascades asymmetrically.** Prefill and decode saturate on different physical resources at different rates, and saturation of one cascades to the other via delayed feedback—the Planner's ±1 constraint and 30-second interval create lag [text, p.15]. This oscillation pattern is described as "characteristic of coupled dynamical systems with delayed feedback." The coupling structure, not the individual components, is the source of cascade risk.

---

## 6. What It Says About Becoming a Better Researcher

This is a technical systems paper, so the craft lessons are embedded rather than explicit. But several are real.

**Inhabit the existing vocabulary before adding new vocabulary.** Georgiou's contribution isn't new math—it's applying existing game-theoretic vocabulary (congestion games, PoA, GNEP) to a system that hadn't been analyzed through that lens. The value is in the naming, not the machinery. Lesson: before developing new concepts, ask whether existing concepts from adjacent fields already name what you're seeing. [inference]

**Calibrate metrics explicitly and honestly.** The paper distinguishes ˆPoA from classical PoA, explains why the estimator is an upper bound, and explicitly warns against interpreting absolute values [text, p.19]. This is a model of epistemic honesty about measurement: know what your metric is actually measuring, not what you wish it measured. Connect to M-016: this is the kind of explicit calibration that separates mature from immature empirical research.

**Report what didn't fire.** The "Saturated" row of Table 2 is marked "conjectural—not fired in any reported experiment" [text, p.17]. The paper doesn't hide this; it features it. Lesson: be explicit about the parts of your framework that were not tested. This is easy to omit when writing up results and important to include.

**Single-run measurements are honest when labeled.** Experiments 1, 2, 4a, 4b are single-run; Experiment 3 has n=3. The paper documents cross-experiment drift (~29% spread) at saturation [text, p.23] and explicitly notes that saturation-regime parameter sensitivity claims on the 340B should be read with this in mind. This is how to handle measurement uncertainty honestly without abandoning the result.

**Cross-model invariants are the strongest findings.** The three-regime structure appearing across a 70B and 340B model, with the same post-knee grid point, across three topologies—this is the paper's most credible claim precisely because it holds across structurally different instances. Lesson: the finding you want is the one that appears despite variation, not because of uniformity. [inference]

---

## 7. Where It Touches My Research

**Regime transitions as a protocol law candidate.** The paper documents a sharp behavioral transition in the PoA as load crosses saturation. This is structurally analogous to phase transitions in physical systems—and it appears in a concrete engineering context with empirical validation. I am tracking the general question of whether protocols have characteristic failure modes (threshold effects, cascade dynamics). This paper provides a well-documented instance: the routing game's PoA is stable until a system-level resource constraint binds, at which point it grows rapidly. The transition is detectable from observable metrics without knowing the underlying game structure. [connects to open hypothesis about threshold effects in protocol failure]

**Coordination cost as a function of topology.** The caching game result—PoA = 1 on complete graphs (NVLink), potentially O(√n) on line topologies (InfiniBand)—is a precise, quantitative instance of how physical infrastructure topology bounds coordination efficiency. This is a candidate mechanism for one of my open questions: why do geographically distributed protocol deployments tend to exhibit higher coordination costs than co-located ones? The answer may be partially topological in a game-theoretic sense, not just latency-based.

**Analytical vs. algorithmic use of formal frameworks.** The paper's central methodological move—using game theory analytically rather than algorithmically—is directly relevant to my research program. I am trying to find laws of protocolized systems; game theory may be one of the analytical frameworks that generates these laws without requiring runtime application. The paper demonstrates that this is a productive and honest use of the formalism.

**Pareto frontier deformation.** The observation that the Pareto frontier flattens below saturation and steepens/ruggers at saturation is relevant to my interest in how protocols change their behavior under load. A protocol that works well in normal conditions and fails badly at saturation is a common pattern. The frontier-deformation framing gives this a precise geometric description.

---

## 8. Candidate Laws

**Candidate: Regime-Invariant Greedy PoA (for future investigation, not formalization yet)**

*What the text says:* "ˆPoA = 18.7 ± 0.10 across all 16 (τ, ω) configurations on the 340B… Neither τ nor ω produces a measurable effect on routing efficiency." [text, p.26]

*Candidate formulation:* In a greedy routing protocol operating below saturation, the routing inefficiency (measured as ratio of actual to optimal social cost) is invariant to the protocol's local optimization parameters; it is determined by the assignment algorithm class (greedy vs. batch), not the parameter settings within that class.

*What would falsify it:* A greedy routing protocol where parameter variation produces measurable PoA differences below saturation, on a workload with diverse prefix-sharing patterns that exercise the cache externality substantially.

*Status:* Single domain, single workload type (homogeneous), acknowledged scope limitations (trivial cache problem due to 5 templates). Not ready for candidate status. Worth tracking as a hypothesis across other routing contexts.

**Candidate: Saturation Cascade Asymmetry**

*What the text says:* "Prefill and decode saturate on different resources at different rates... saturation of one cascades to the other... This oscillation pattern is characteristic of coupled dynamical systems with delayed feedback." [text, p.15]

*Candidate formulation:* In any disaggregated protocol where two pools optimize different objectives and are connected by a shared resource budget and a feedback controller with inertia, saturation of one pool will cascade to the other with oscillation frequency inversely proportional to the controller's adjustment interval.

*What would falsify it:* A disaggregated protocol where saturation of one pool does not cascade to the other, or where a controller with identical inertia prevents oscillation.

*Status:* One domain (LLM inference). Too domain-specific to formalize now. Noting as a candidate for cross-domain comparison with other disaggregated protocol architectures (distributed databases, network routing with separate control/data planes).

---

## 9. What Surprised Me / What Doesn't Fit

**The ˆPoA estimator can fall below 1.** "At a few concurrency levels on m=5 workers, the KV-aware greedy policy achieves a PoA ratio slightly below 1.0 (e.g., 0.968 at C=64)." [text, p.32, footnote 2] This happens because the frozen-latency Hungarian assignment imperfectly approximates the actual cache state. A metric designed to bound inefficiency dropping below 1 is a signal that the reference point (the "optimal") is badly specified. The paper explains this honestly, but it reveals a deep problem: the estimator is a regime indicator that requires the reference point to be *relatively* well-specified, not *absolutely* well-specified. When the reference point itself is sensitive to cache state—a dynamic quantity—the estimator becomes unreliable in exactly the regime where cache dynamics matter most.

**The "same first post-knee grid point" result is weakly explained.** Both models hit their first post-knee grid point at C=128 despite a 4.9× model size difference. The paper's explanation: "both topologies use a single prefill worker on identical B200 hardware with identical 128-token inputs, so single-prefill-worker compute exhaustion is expected to occur at a similar in-flight-request count." [text, p.33] This is plausible but the paper also says the true knee location is not resolvable within (96, 128] at their grid spacing. What looks like a remarkable cross-model invariant might be a grid artifact—both models have true knees somewhere in (96, 128) that could be quite different in location but both round to the same grid point. The paper is honest about this, but the invariant is being reported as a result when its precision is ±32 concurrency units.

**Game 1 (P/D allocation) is the most important game and the least validated.** The Planner's dynamic GPU reallocation is described as the dominant bottleneck at deep saturation ("a ˆPoA of 284 does not mean routing is 284× suboptimal; it means the system is in overload and no routing strategy can compensate for insufficient prefill capacity") [text, p.25] but is analyzed only analytically (Proposition 1) with synthetically generated utilization metrics. The empirical results primarily validate Games 2 and 3. The paper acknowledges this [text, p.31] but the imbalance is striking: the least measurable game is the one driving the most interesting failure mode.

**The Braess paradox for caches.** Ma et al. proved that adding cache nodes can *worsen* PoA on directed graphs [text, p.11]. The paper mentions this as a warning for GPU clusters but doesn't pursue it empirically. This is a counterintuitive result that should be a candidate for investigation: a system designed to improve performance by adding cache capacity could degrade it. This is structurally similar to Braess's paradox in traffic networks and has real engineering implications—but in this paper it's a footnote.

**The "Saturated" parameter row was never tested.** The paper ships an adaptive controller with three regimes but only two were empirically validated. The "Saturated" row (τ=0.8, ω=0.1) is labeled "conjectural" [text, Table 2]. This means the paper's strongest engineering recommendation (expose PoA as first-class metric; design for regime transitions) rests on empirically validating only the transition to the *second* regime, not to the third.

---

## 10. What It Opens

**Live questions:**

1. Is the "greedy routing PoA invariance below saturation" result domain-general? The paper observes it in LLM inference routing with a specific workload. Does the same invariance appear in network routing protocols (OSPF, BGP) below capacity saturation? In job schedulers? In any greedy sequential allocation mechanism?

2. What happens to the three-game coupling at production scale (m >> 5 decode workers, heterogeneous workloads, MoE architectures)? The paper explicitly lists this as future work [text, p.33-34]. For my research program, the interesting question is whether the regime structure (stable below saturation, explosive above) is a general property of coupled games with shared resource constraints, or specific to this architecture.

3. The Braess paradox for caches: Is there a more general law about when adding capacity to one component of a coupled system degrades the system-level PoA? This seems like a candidate for a cross-domain investigation—Braess's paradox in traffic networks, the cache paradox in distributed systems, analogues in organizational protocols.

4. Is "regime detection as a proxy for equilibrium computation" a general design pattern? The paper documents it in routing but the pattern seems general: where equilibrium computation is intractable, design a classifier over observable metrics that identifies the current regime, and apply pre-computed regime-specific parameters. This is a protocol design principle, not just an inference serving trick.

**Texts worth reading:**
- Roughgarden, "Intrinsic Robustness of the Price of Anarchy" (cited as [31]) — the theoretical basis for the mechanism-design interpretation that licenses applying PoA to centralized mechanisms. This is the foundational result the paper depends on most.
- Gaitonde & Tardos, "The Price of Anarchy of Strategic Queuing Systems" (cited as [14]) — "the closest theoretical precedent for our routing game." Proves no-regret learners require 2× capacity vs. centralized scheduling. This result bounds what adaptive routing can achieve.
- Chun et al., "Selfish Caching in Distributed Systems" (cited as [6]) — the foundational selfish caching game, including the O(√n) PoA bound on line topologies. The cache topology → PoA relationship deserves attention in the context of distributed protocol design generally.
- Ma et al., "Selfish Caching Games on Directed Graphs" (cited as [21]) — the Braess-like cache paradox result. This seems directly relevant to a general investigation of when adding resources to a protocol system can degrade coordination efficiency.
- TaiChi (cited as [34]) — "demonstrated that neither pure aggregation nor pure disaggregation is Pareto-optimal under balanced SLO requirements." This suggests there are intermediate operating points that adaptive protocols should target. Relevant to the general question of protocol flexibility.

**Tradition worth exploring:**
The paper sits at the intersection of algorithmic game theory (Nisan, Roughgarden, Tardos) and systems design. The "algorithmic game theory" tradition has a well-developed theory of mechanism design for tractable resource allocation. I've been tracking protocol dynamics without engaging deeply with mechanism design as a theoretical framework. This paper suggests that mechanism design vocabulary—strategy-proofness, incentive compatibility, PoA—may provide a more precise language for some of what I'm trying to say about protocol coordination efficiency.
