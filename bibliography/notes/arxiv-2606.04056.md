# Deep Read Notes: Arxiv 2606.04056

*Source: `bibliography/deep-reads/arxiv-2606.04056.pdf`*

---

## Reading session: full document (26 pages)

# Deep Read: arxiv-2606.04056 — Token Budgets: An Empirical Catalog of LLM-Agent Budget-Overrun Incidents

---

## 1. Gestalt

This paper is, at its core, an empirical artifact: a carefully constructed failure catalog. Khan has done something methodologically unusual in the ML/systems engineering space — he built a qualitative coding study in the grounded-theory tradition and subjected it to independent inter-rater reliability verification, applied to a phenomenon (LLM agent budget overruns) that the field mostly treats as an annoyance rather than a structured failure class. The animating question is not "how do we prevent cost overruns?" — that question is almost too simple. The deeper question is: *what is the structure of this failure class, and what does that structure imply about where enforcement should live?*

The paper's central conviction is that the right place to enforce resource constraints is the earliest point at which a violation can be detected — and that the dominant existing mitigations are all reactive (software-layer callbacks, transport-layer 402s) because they catch problems after API calls are already committed. The affine-typed Rust crate is less a product and more a demonstration that compile-time enforcement is achievable for this resource class. Khan is honest that the crate applies to a minority deployment context (new Rust agents, not the Python-dominated ecosystem); the catalog is the result he wants reviewers to weigh.

What makes this paper matter on its own terms: it is one of the few empirical treatments of a *protocol-level failure mode in AI agent systems* — not capability failure, not safety failure, but coordination-and-resource-accounting failure across 21 independently-developed frameworks. That structural finding — same failure class recurring across 18 ecosystems — is significant regardless of the Rust crate.

---

## 2. Argument and Structure

**Core claims, in order of weight:**

**Claim 1 (Primary, empirical): LLM-agent budget overruns constitute a documented, recurring failure class.** [text, pp.1-8]
The 63 confirmed production incidents (plus 47 supplementary structural entries) across 21 frameworks establish *recurrence*, not prevalence. Khan is explicit and disciplined about this distinction throughout — he never says "X% of deployments fail," only that the failure pattern appears across independently-developed projects. The eight-cluster mechanism taxonomy (M-retry-loop, M-cost-observability, M-context-amplification, M-storage-amplification, M-budget-primitive-missing, M-delegation-fanout, providerOptions-silently-dropped, M-multimodal-cost-amplification) is explicitly labeled exploratory (κ=0.44 for cluster assignment), while the four-class confirmation labeling (bug_fixed, bug_unfixed, maintainer_framing, feature_request) is IRR-validated at κ=0.837.

The load-bearing example: DNSW-001 ($2,150 in unintended spend by a single user). Claude-code itself has the same compaction-loop signature. These are not fringe libraries.

**Claim 2 (Mechanism): Runtime mitigations share a structural limitation — they can only enforce after a call commits.** [text, pp.2-3, 7-8]
The three-layer taxonomy (compile-time, software-layer, transport-layer) is the paper's conceptual spine. Every existing mitigation sits at layer 2 or 3. Layer 2 (AgentGuard-style callbacks, LiteLLM proxies) catches spend after the API call returns — always admits one overshooting call. Layer 3 (ATXP HTTP 402) catches at the network boundary — call is already in flight.

**Claim 3 (Demonstration): Affine ownership in Rust can enforce budget integrity at compile time.** [text, pp.8-14, 21-23]
The distinguishing contribution is *non-bypassability*, not the cap-respecting outcome. The forgetful-operator experiment (§4.3) is the key: racy Python overshoots 30/30, locked Python reaches 0/30, Rust affine reaches 0/30 — but the racy pattern *cannot be written* in the Rust affine version (rejected by the borrow checker). This is a structural difference, not a marginal improvement. Runtime alternatives achieve the same outcome when the operator writes correct lock discipline; the affine type removes that operator-discipline requirement.

**Acknowledged limits (unusually candid):** [text, Table 2, pp.3-4, 18-20]
- Binary-level cap soundness is Conjecture 1, deliberately unproven
- Estimator soundness (A1) is the real load-bearing dependency; the type system doesn't help if A1 fails
- Reasoning models violate A6 structurally (hidden thinking tokens)
- A7 (provider usage truthfulness) is a shared trust assumption — the A7 fault injection table at k=5 shows 100% overshoot
- Capital cost: static estimator reserves 4-6× actual; meaningful on prepay accounts
- Deployment context: minority of ecosystem (Python dominates)

**Most confident:** the catalog's existence and inter-rater reliability; the forgetful-operator mechanism split (30/30 vs. 0/30 is categorical, not marginal); single-agent cap parity between Rust affine and a 4-line Python counter.

**Most speculative:** the eight-cluster taxonomy (κ=0.44); the claim that the approach generalizes to non-retry-loop workloads; binary-level properties.

---

## 3. Conceptual Vocabulary

**Affine type / affine ownership** [text, p.9, A.3]: A type that can be used *at most once* — consumed by the operation that "moves" it. Weaker than linear (which requires exactly-one-use); a dropped Budget can under-spend but cannot double-spend. Khan's crucial point: dropping is cap-safe; duplication is not. The Rust borrow checker enforces this structurally.

*In my vocabulary:* I have "conservation law" and "type system" as concepts but not affine typing specifically. This introduces a more precise vocabulary for one class of protocol-level constraint enforcement — the class where a resource is fundamentally *consumable* and *non-duplicable*.

**M-delegation-fanout** [text, pp.6-7]: The specific failure mode where a parent agent delegates budget to multiple children concurrently, each checks the shared budget before any debit, and multiple children proceed past the check simultaneously. This is a classic check-then-act race under concurrency, applied to resource accounting.

*Note: this is a domain-specific instantiation of a general concurrent protocol failure. The name is useful for my purposes.*

**Budget-primitive-missing** [text, pp.7, 20-21]: Not a bug in an existing primitive but the *absence* of a first-class aggregate-budget primitive. Frameworks shipping without a native budget capability (or with one that silently regresses) fall into this cluster. The distinction between "absent primitive" and "buggy primitive" is analytically important.

**Conservative reservation** [text, pp.9-10]: The pattern of debiting an *upper-bound estimate* before the API call rather than actual cost after. Requires an estimator (A1) that over-reserves but never under-reserves. Cap soundness depends on A1, not on the type system. The type system makes A1 violations *structural* rather than accidental — but cannot prevent A1 from being wrong.

**Three-layer enforcement taxonomy** [text, pp.7-8, 15]: Compile-time / software-layer / transport-layer. The taxonomy is the author's conceptual contribution to organizing the space of mitigations, independent of the specific crate. I find this framing potentially generalizable.

**Non-bypassability** [text, pp.9, 11-13]: The property that correct-looking code cannot accidentally defeat the enforcement mechanism. Distinguished from the *outcome* (cap-respecting) — runtime alternatives achieve the same outcome when written correctly; affine types achieve the outcome *without requiring correctness from the operator*.

---

## 4. Analytical Moves

**The layer-taxonomy move:** When analyzing a class of enforcement mechanisms, ask where in the system enforcement occurs, and what the latency is from violation to detection. Compile-time catches before deployment; software-layer catches after API call returns; transport-layer catches at network boundary. *Each layer can only catch violations that have not yet committed resources at that layer.* This move generalizes: any protocol with an enforcement mechanism can be analyzed by its *earliest detection point*.

**The mechanism-isolation experiment:** Khan's forgetful-operator experiment (§4.3) is exemplary. To isolate what compile-time integrity *uniquely adds* over runtime alternatives, he constructs five conditions varying independently: allocation strategy (shared vs. split), language (Python vs. Rust), integrity layer (none vs. runtime discipline vs. compile-time). Condition E — Rust with shared `Arc<Mutex<Budget>>` and operator-written lock discipline — reaches 0/30 like the affine Conditions C and D, isolating the integrity-layer contribution from language choice. The result: the distinguishing property is non-bypassability, not the outcome, not the language.

**The recurrence-not-prevalence framing:** When sampling from biased data (failure-confirming selection frame), do not claim prevalence — claim recurrence across independently-developed projects. "The failure class exists and recurs across N=21 independently-developed frameworks" is a defensible claim from the data; "X% of deployments fail" is not. This move is a model for how to scope empirical claims honestly when your sampling frame selects on the dependent variable.

**The dependency-chain decomposition:** The cap-respecting property decomposes into (1) integrity property — type-system enforced, unconditional within trust boundary; (2) cap-respecting property — estimator-dependent, runtime arithmetic. These are *independent*, and the weaker chain is A1. Explicitly mapping which properties are enforced where (Table 2) is a powerful analytical move — it makes the trust model auditable and clarifies exactly what guarantees are being claimed.

**The decision-matrix approach:** Rather than arguing "use this tool," map the full deployment context × mechanism space, identify where the approach is strictly better, and explicitly name where it is the wrong choice. Table 3 is an exemplar of this move. This prevents scope-inflation and makes the contribution honest.

---

## 5. What It Says About the Nature of Things

The most general lesson here is about **where enforcement mechanisms can live in relation to the resources they govern.** Khan's three-layer taxonomy implies a general principle: *enforcement at layer N catches violations that have not yet consumed resources at layers N+1 through K, but cannot prevent violations that already occurred at layers 1 through N-1.* This is a structural claim about enforcement architectures, not a claim about LLM cost specifically.

A second lesson: **the existence of a correct implementation does not prevent incorrect implementations.** Runtime alternatives achieve cap-respecting when written correctly (Conditions B and E both reach 0/30). The problem is that incorrect implementations (Condition A) compile and run — they just race. Type systems are valuable not because they achieve better outcomes but because they *eliminate the incorrect-implementation possibility space*. This is a general principle about formal constraints in protocol systems.

A third lesson: **the failure class can be stable across organizational boundaries.** The same failure cluster (M-delegation-fanout, M-budget-primitive-missing) appears in LangChain, AutoGen, CrewAI, Claude-code, Pydantic AI, OpenAI Agents SDK — independently developed, different design philosophies, different authors. When a failure mode survives across organizational boundaries and implementation choices, it is structural, not accidental.

**The estimator as load-bearing element:** The entire edifice of compile-time enforcement depends on A1 (estimator soundness). The type system cannot help when A1 fails. This is a general lesson about formal protocol enforcement: formal guarantees are always conditional on the correctness of the empirical layer that feeds them. A well-specified formal system can still fail catastrophically if its inputs are wrong.

---

## 6. What It Says About Becoming a Better Researcher

Khan demonstrates **claim scope management** at a high level. Every claim in this paper is explicitly scoped to its evidence. The distinction between "recurrence" and "prevalence" is maintained throughout. Binary-level soundness is labeled Conjecture 1 and "deliberately unproven." The eight-cluster taxonomy is labeled "exploratory." The forgetful-operator experiment's claim is bounded to "mechanism demonstration" rather than "statistical effect." This discipline is not timid — it is precise. Khan claims less, but what he claims is defensible.

The **Table 2 guarantee map** (which property, enforced where, with what status, under what trust assumption) is a research practice worth adopting. Every law and hypothesis I develop has an implicit analogous structure: which domains, what mechanism, what trust assumptions, what remains open. Making this table explicit rather than implicit in prose is a discipline improvement.

**Calibrated negative results.** Khan's finding that a 4-line Python counter with the same estimator achieves identical cap-respecting outcomes on single-agent workloads (0/30 overshoot, matching the Rust affine) is a negative result about the affine discipline's distinguishing value in the single-agent case. He reports it prominently. The affine discipline earns its place on the narrower claim — multi-agent non-bypassability. Researchers who suppress negative results leave their claims over-extended.

The **pre-committed stopping rules** in §5.1 (the Agent Contracts head-to-head protocol) are notable. When an experiment encounters unexpected conditions (API drift in v0.3.2), the response is to report a null result per the pre-committed protocol, not to retroactively reinterpret the data. This is methodological honesty that matters especially in empirical CS where experiment conditions change rapidly.

*M-016 connection:* Khan's explicit, numbered "expensive follow-ups" section (§7.3, items E1-E5) is a model for distinguishing "revision items" from "research projects." E1 (binary-level refinement proof) is explicitly a different paper, not a weakness of this one. Knowing the boundary of your contribution — what you have established vs. what you have not attempted — is a mature research disposition.

---

## 7. Where It Touches My Research

**Direct connection to protocol ossification (CL-001 and related):** The paper documents a specific failure class that occurs precisely because LLM agent frameworks *lack* first-class budget primitives. The M-budget-primitive-missing cluster (12 of 110 rows) is not a bug in existing code — it is the absence of a primitive. This is a protocol-design failure: the protocol specification (LLM agent framework interface) was designed without this resource type as a first-class element. The formalization ratchet (if I have anything like CL-001) would predict that once frameworks shipped without budget primitives, retrofitting them becomes harder as the surrounding code patterns ossify around their absence. The catalog's temporal distribution (18/25/52/15 across 2023-2026) is consistent with this — the failure persists across all four years, not absorbed as a solved problem.

**Three-layer enforcement taxonomy as a candidate law structure:** The compile-time/software-layer/transport-layer framing has structural parallels to other layered enforcement systems. Legal enforcement (constitutional constraint / statutory law / regulatory enforcement) has a similar layer structure. Network protocol enforcement (packet-level / connection-level / application-level) has a similar layer structure. The generalization would be: *in any layered system, enforcement at layer N cannot prevent resource consumption that occurred at layers below N.* This is closer to a physical constraint than a social regularity.

**Affine types as protocol constraint:** The affine Budget type is itself a *protocol constraint made structural* — the rules of the budget-delegation protocol (no duplication, no double-spend, no use-after-delegation) are encoded in the type system such that violations fail to compile. This is a very clean example of what I might call "protocol-as-type" — where the protocol's invariants become the type invariants of the resource representation. The question this opens: in what domains does this move become possible, and what prevents it from being adopted everywhere that it would be beneficial?

**The A7 fault injection result:** When the provider under-reports usage by 2×, 666/1000 sessions overshoot. When it under-reports by 5×, all 1000 sessions overshoot. The formal guarantee evaporates completely when the input layer is untrusted. This is a case of protocol failure propagating *upward* through an enforcement layer — the outer layer (type system) is sound, but the inner layer (provider usage reporting) is not, and there is no recovery. This connects to whatever I eventually develop about protocol trust hierarchies.

---

## 8. Candidate Laws

**Candidate 1: Earliest Enforcement Point determines the minimum resource consumed under violation.**

[text, p.7, §2.7]: "None catches the spend before the API call commits: the agent either pays for the call and then notices, or has the call rejected at the network boundary after the request is already in flight."

*Candidate formulation:* In any layered resource-enforcement system, the minimum resource consumed before a violation is detected equals the cost of the transaction that first crosses the enforcement threshold at layer N, where N is the highest layer at which enforcement exists.

*What this text says:* compile-time layer catches before any resource is consumed; software-layer catches after one call returns; transport-layer catches after the request is in flight.

*What would falsify it:* An enforcement mechanism that is "software-layer" but catches the violation before the API call commits (not merely checking after a return). This would be a software-layer mechanism that achieves compile-time latency — possible in principle (e.g., a sufficiently tight pre-flight check at the application layer). Khan's own pre-call reservation pattern is arguably this — a software-layer mechanism operating before the call. The taxonomy needs sharper boundaries.

*Assessment:* This is a candidate worth formalizing, but the layer taxonomy needs to be more precisely defined. The move from "three layers" to a general law requires more work. Mark as speculative; one domain (LLM agent infrastructure) with mechanism stated.

**Candidate 2: Absence of a first-class primitive is structurally stable once coordination overhead develops.**

[text, §2.4, A.1]: M-budget-primitive-missing appears across 6 frameworks; maintainer-acknowledged structural gaps persist for 13+ months in some cases (SMAG-002). The failure class persists across all four catalog years.

*Candidate formulation:* Once a framework ships without a first-class resource-accounting primitive and user code patterns develop around its absence, adding the primitive retroactively requires either breaking changes or a dual-path architecture — making absence self-reinforcing.

*What would falsify it:* A framework that shipped without a budget primitive, acquired significant user code patterns around its absence, and successfully added a first-class budget primitive with backward compatibility and rapid adoption.

*Assessment:* This is a coordination-cost account of why M-budget-primitive-missing persists. It is consistent with my existing work on protocol ossification. One domain only (LLM agent frameworks), though it recurs across 6 frameworks within that domain. Mark as speculative; needs cross-domain verification.

---

## 9. What Surprised Me / What Doesn't Fit

**The A7 fault injection table is quietly devastating.** [text, Table 7, p.19] Khan proves that at k=2 (provider under-reports by 2×), 66.6% of sessions overshoot. At k=5, all 1000 sessions overshoot. The formal guarantee — which Khan builds with considerable care — evaporates *completely* if the provider is not honest. He acknowledges this as "a trust assumption shared with every client-side cost-accounting mechanism." This is true, but it also means the entire system is only as secure as the weakest actor in the trust chain — the external provider. The compile-time integrity property, which is the paper's distinctive contribution, provides *zero* protection against this failure mode. I find it striking that this result — which essentially sets an outer bound on the approach's reliability — is in §6 rather than the abstract.

**The temporal distribution doesn't accelerate predictably.** [text, p.7] The catalog shows 18/25/52/15 incidents across 2023-2026 (where 2026 is a partial year through April). Khan is careful not to interpret this as acceleration. But the jump from 25 to 52 between 2024 and 2025 is notable. He attributes it to ecosystem expansion (new frameworks, growing GitHub activity, methodology refinements). This is honest but incomplete — it's possible that the failure class *is* accelerating as agent systems become more complex. The catalog can't distinguish these hypotheses.

**The honest scope claim creates a puzzle.** Khan argues the Rust affine discipline applies to "new Rust agent deployments" — a minority (roughly 2-3 of every 10 retained incidents are Rust-relevant by his estimates). The Python ecosystem dominates failures, but the formal contribution doesn't apply there. The Python port provides "runtime discipline only" — which is functionally equivalent to existing mitigations. So the paper's formal contribution is narrowly scoped to a deployment context that currently represents a small fraction of production incidents. Khan is honest about this, but it means the gap between the failure class established by the catalog and the failure class addressed by the crate is substantial.

**The eight-cluster taxonomy has moderate IRR but the paper builds significant narrative structure on it.** [text, §6.6] κ=0.44 for cluster assignment means moderate agreement — better than chance, but two raters substantially disagree on the cluster structure. Yet the entire Section 2.6 ("Patterns") and much of the paper's narrative is organized around the eight clusters. Khan acknowledges this in §6.6 but the tension between "exploratory taxonomy" and "organizing device for significant discussion" is real.

**Why not a capability-typed approach rather than budget-per-agent?** The paper doesn't consider whether a different design philosophy — e.g., requiring all LLM calls to pass through a capability-typed interface that carries budget information — might address more than one cluster. The current design adds a Budget type alongside existing agent code; an alternative would make Budget a required argument to any LLM-calling function at the framework level. This would address M-budget-primitive-missing by construction. Khan discusses why the 12-row cluster is the "cleanest fit" for type-level discipline [text, Appendix A], but doesn't fully explore the alternative of making the type system load-bearing at the *interface* level rather than just within an agent.

---

## 10. What It Opens

**Live questions:**

1. Is the "enforcement layer determines minimum resource consumption" principle general? Does it hold in financial clearing (where T+2 settlement creates the same structure — you can catch fraud faster or slower, but the minimum consumed resource is bounded by the enforcement latency)? In legal enforcement? This is the candidate law I want to develop.

2. What is the mechanism by which M-budget-primitive-missing becomes self-reinforcing? The catalog shows it persists across 6 frameworks, often with maintainer acknowledgment but no fix. This is protocol ossification in a very specific, recent, well-documented case. I want to trace the mechanism here.

3. The affine type as "protocol-as-type" move — where else has this occurred in protocol history? EVM gas metering is one case (intrinsic cost pre-computable). Linear types in session types is another. The general question: in which protocol domains is it possible to encode the protocol invariants in the type system of the implementation language, and what determines whether this is feasible?

4. The A7 trust boundary is a general problem: any resource-accounting system that depends on an external party's honest reporting is only as reliable as that party's honesty. What are the structural conditions under which this trust relationship can be eliminated, and what are the costs?

**Related texts to read:**
- [25] Ye and Tan, "Agent Contracts" (arXiv:2601.08815) — concurrent work, the runtime alternative that achieves the same outcome through different machinery. Referenced in the library as `arxiv-2601.01279`; check if this is the same paper.
- The blockchain gas metering lineage: KEVM, GASTAP, MadMax — for the comparison case where cost is intrinsic and pre-computable rather than post-hoc external.
- Wadler, "Linear types can change the world" [1] — the founding document of the substructural types tradition Khan places himself in.
- The Saga pattern literature (Garcia-Molina and Salem [57]) — Khan's §6.7 connects the multi-tenant extension to Sagas; this tradition has protocol-ossification implications I haven't explored.

**Traditions worth exploring:** The substructural and resource-aware typing tradition (RAML, AARA, Linear Haskell, quantitative type theory) as a tradition that has been trying to put resource constraints into types for 30+ years, with limited adoption. The adoption failure might itself be evidence for a protocol ossification law.
