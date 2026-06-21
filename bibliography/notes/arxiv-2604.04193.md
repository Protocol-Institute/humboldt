# Deep Read Notes: Arxiv 2604.04193

*Source: `bibliography/deep-reads/arxiv-2604.04193.pdf`*

---

## Reading session: full document (19 pages)

# Deep Read: Wadhwa, Yaish, Zhang, Nayak — "Perils of Parallelism: Transaction Fee Mechanisms under Execution Uncertainty" (arXiv 2604.04193)

*Full document, 19 pages. Read complete.*

---

## 1. Gestalt

This paper is fundamentally about what happens when you try to price something you cannot yet observe. The central phenomenon: parallel blockchain execution requires fees to be set *before* transactions run, but the actual resource consumption of a transaction depends on its execution path, which in turn depends on the state of the world at execution time — a state that cannot be known until other transactions have already run. The authors call this the contingency problem, and they show it is not a design failure but a structural impossibility: no fee mechanism can simultaneously protect users from overpaying and protect the protocol from under-collecting, unless it either executes transactions in advance (defeating the purpose) or collapses to constant fees (eliminating price signals entirely).

The paper is animated by a second problem running in parallel: shill attacks. When fees depend on the structure of the execution schedule, rational actors can inject fake transactions to manipulate that structure — users to reduce their fees, schedulers to inflate them. These two problems interact in a nasty way: mechanisms that protect against contingency risk often open new attack surfaces for shills, and vice versa.

What makes this work significant is that it grounds both problems in hard complexity results. The risk tradeoff is not just a game-theoretic observation; it follows from the P-completeness of determining object usage, which means no efficient shortcut exists. The parallel execution bottleneck is not going away, and the pricing problems this paper identifies are therefore permanent features of the design space.

---

## 2. Argument and Structure

**Core claims:**

1. **The risk impossibility** [text, p.1, Theorem 1]: In any fee mechanism for parallel execution with contingent transactions, user risk (overpaying for unused objects) and scheduler risk (under-collecting for unused capacity) sum to a constant. You cannot reduce one without increasing the other, unless you execute transactions pre-schedule (exponential compute) or charge constant fees.

2. **The computational foundation** [text, p.7, Theorem 2]: Determining whether a contingent object will be used by a transaction is P-complete — as hard as running the transaction itself. There is no efficient shortcut. The risk tradeoff is not an artifact of clever design; it is a consequence of Turing-completeness.

3. **Shill-proofness is incompatible with efficiency** [text, p.10, Lemma 3]: No gas computation mechanism can simultaneously satisfy scheduler shill-proofness and efficiency (total gas = schedule makespan). The proof is elegant: with n cores and n+1 parallel transactions, shill-proofness forces each transaction to consume t gas, but efficiency requires total gas = makespan = t, not (n+1)t.

4. **User-friendly mechanisms cannot price parallelism** [text, p.11-12, Theorem 3]: If user risk = 0 (users pay only for what they use), then the fee of a transaction must be independent of all other transactions in the schedule — which means the fee cannot reflect the transaction's impact on parallelism at all.

5. **OW-TFM as the bounded solution** [text, p.12-13]: The Object-Weighted TFM breaks the cyclic dependency between scheduling and fees by pricing objects based on *past* utilization (EIP-1559-style), not the current schedule. This makes shill attacks only relevant across blocks, not within them, and the shill-proofness condition becomes: α ≥ πo · η · γ/(1−γ).

**Load-bearing example:** Alice's swap throughout. Alice submits a transaction that reads an oracle price and only executes a trade if the price is favorable. The contingent objects (pool reserves, balance) are sometimes used, sometimes not. The attainable fee is 5, the baseline fee is 1, and the gap of 4 is the total risk that must be allocated. Every theorem is illustrated against this example. The example works because it is real — AMM swaps with oracle checks are extremely common in DeFi.

**Key structural moves:**
- The risk tradeoff is proven first as an algebraic identity (Lemma 1: UR + SR = fatt − fui), then lifted to an impossibility via complexity (Theorem 2).
- The shill analysis is done first on gas (Sections 6), then re-done on fees with contingency (Section 7), showing that moving from gas to fees opens new attack surfaces not captured by prior shill-proofness notions.
- OW-TFM is presented not as the optimal solution but as a mechanism that achieves the *boundary* of the tradeoff under specific parameterizations.

**Limits acknowledged:** The attainable fee concept is admitted to be an approximation — some transactions can never realize all declared contingent objects [text, p.14]. The paper does not handle off-chain collusion, denial-of-service attacks, or cross-block manipulation beyond the OW-TFM section. Probabilistic execution models are flagged as future work [text, p.14].

---

## 3. Conceptual Vocabulary

**Contingent transaction** [text, p.4, Definition 2]: A transaction is contingent if there exist two prefix schedules that produce different execution-time object access sets. Crucially: contingency is about *which* objects are accessed, not *what values* those objects hold. A transaction that always reads the same objects is not contingent even if prior transactions changed the values.

*This is a subtle and important distinction. In my own thinking I had not clearly separated "state-dependent behavior" from "access-set-dependent behavior." The authors are identifying specifically the second phenomenon.*

**User risk / Scheduler risk** [text, p.5, Definitions 3-4]: User risk = how much a user pays in excess of what they ideally would pay for actual execution. Scheduler risk = how much the scheduler fails to collect relative to the maximum it could have collected. Their sum is constant.

**Attainable fee / Baseline fee / User-ideal fee** [text, p.4-5]: Three reference points. Attainable = fee if all declared objects were used (upper bound). Baseline = fee if only deterministic objects counted (lower bound). User-ideal = fee for exactly what was used (execution-dependent). The gap between attainable and user-ideal is the total risk to be allocated.

**Shill transaction** [text, p.1-2]: A functionally useless transaction injected by a user or scheduler to manipulate the gas/fee allocation to their benefit. User shills reduce fees on the real transaction; scheduler shills inflate fees on honest transactions.

**Shill-proofness** [text, pp.9-11, Definitions 14-18]: A property requiring that no party can benefit by injecting fake transactions. The authors distinguish gas-based shill-proofness (about raw compute allocation) from fee-based shill-proofness (about actual payments, accounting for priority fees, burning, and contingent under-execution). The fee-based version is strictly harder to achieve.

**Object-Weighted TFM (OW-TFM)** [text, pp.12-13]: A mechanism that prices transactions based on the objects they declare, with prices set from previous-block utilization data (EIP-1559-style per-object price update). Fees are schedule-independent, eliminating within-block shill attacks.

**Risk division parameter α** [text, p.8]: The single parameter spanning the design space from user-friendly (α=0) to scheduler-friendly (α=1). fact = α·fatt + (1−α)·fui. Even-Steven is α=0.5.

---

## 4. Analytical Moves

**The constant-sum decomposition.** When you have two parties sharing a fixed total cost, the design question is not "can we reduce total cost?" but "who bears it?" [text, p.5-6, Lemma 1]. This move converts an optimization problem into an allocation problem. Applicable whenever a system has a conservation law (the total risk/cost is fixed) and the design question is how to distribute it.

**Complexity grounding of economic impossibility.** The authors prove an economic impossibility (Theorem 1), then strengthen it by showing the *reason* the impossibility is fundamental rather than an artifact of scheduler design: the underlying decision problem is P-complete (Theorem 2). This gives the impossibility result teeth — it rules out not just current designs but all possible designs. [text, pp.6-7]

*Transferable move: when I find an impossibility result in protocol design, ask: is this impossibility grounded in a complexity result, or is it just a feature of the design space we've explored so far? The presence of a complexity bound is what makes an impossibility law-like rather than contingent.*

**Cyclic dependency breaking via temporal separation.** The cyclic problem: fee depends on schedule, schedule depends on fee. OW-TFM breaks this by using *previous-block* data to set prices, so the fee is fixed before the current schedule is formed. [text, p.12] This is a general design move: when A and B are mutually dependent in the same time slice, introduce a lag to make them sequentially dependent across time slices.

**Parameterizing a design space between boundary conditions.** Rather than claiming one design is best, the authors characterize a linear spectrum (α ∈ [0,1]) between two theoretically pure boundary cases (user-friendly at 0, scheduler-friendly at 1), then ask what properties hold at each point and what empirical conditions determine the right parameterization. [text, pp.7-8, 13-14] This is a mature mechanism design move: scope the design space precisely before proposing solutions.

**Distinguishing gas-proofness from fee-proofness.** The authors re-run the shill analysis after noting that prior work analyzed gas only, not fees. Moving from gas to fees with priority and burning reveals new attack surfaces. [text, pp.10-11] General move: when extending an analysis to a richer setting, re-examine which properties the prior analysis guaranteed and whether they still hold in the richer setting.

---

## 5. What It Says About the Nature of Things

**Pricing deferred execution is structurally different from pricing completed execution.** The fundamental issue here is temporal: fees must be set before the outcome is known. This is not a coincidental feature of blockchain design — it is the structure of any protocol where resource consumption depends on contingent branching that happens after commitment. Insurance, options pricing, and advance booking all face the same structure. The user-scheduler risk tradeoff is a specific instance of a general problem: whenever a party commits to a price before an uncertain outcome resolves, the risk of that outcome must sit somewhere.

**Turing-completeness creates irreducible pricing complexity.** The P-completeness result says: for any protocol running Turing-complete code, there is no efficient way to predict resource consumption before execution. This is not a feature of blockchain, or of parallel execution specifically — it is a feature of any system where the execution path is determined by arbitrary computation over state. Any protocol pricing expressive computation faces this wall. [inference]

**Shill-proofness and efficiency are genuinely incompatible.** Lemma 3 is a small, clean impossibility result that deserves attention beyond blockchain: if you want gas accounting to reflect actual parallelism contribution (efficiency), you cannot simultaneously prevent a scheduler from profitably adding fake work. The incompatibility arises because efficiency requires the (n+1)th transaction to increase total measured gas (it increases the makespan), but shill-proofness requires the scheduler to be unable to profit by adding such a transaction. These requirements pull in opposite directions whenever the transaction is the marginal task that causes serialization.

**The design space of risk allocation is one-dimensional.** UR + SR = constant is a conservation law for the mechanism design space under contingency. This constrains the space of meaningful choices to a single parameter. This is a pleasing result: complex systems sometimes have low-dimensional design spaces when you find the right conservation law. [text, p.6-8]

---

## 6. What It Says About Becoming a Better Researcher

The paper is primarily technical, but several methodological commitments are visible:

**Prove what you cannot do before proposing what you can.** The paper's structure is: impossibility first (Sections 4-6), then solutions (Sections 7-8). This is sound research architecture. If you propose a solution without establishing what is impossible, reviewers can always ask "why not do X?" Proving X is impossible first forecloses that question. [inference] This connects directly to M-016 (researcher calibration): establishing the impossibility boundary before proposing solutions is a sign of research maturity.

**Running examples as proof scaffolding, not illustration.** Alice's swap appears in every section, not as a motivating story but as a concrete check on each theorem. This is more than pedagogy — the running example forces the authors to verify that their formal results produce sensible numbers in a real case. It is a calibration device. Worth adopting: when developing a formal framework, maintain a running concrete case alongside the formalism.

**Distinguish what is hard about your problem from what is contingent.** The paper carefully separates: (1) impossibilities that follow from P-completeness (fundamental — cannot be fixed by clever design), and (2) tradeoffs that reflect design choices (tunable via α). Conflating these would either make the problem seem unsolvable or hide genuine constraints. The discipline of distinguishing fundamental from contingent limits is a core research practice. [inference, connects to Hamming's "important problems" discussion]

**Acknowledge the tension between theoretical cleanness and practical deployability.** The paper notes that the attainable fee concept is an abstraction that does not correspond to any realizable execution for some transactions [text, p.14]. Rather than hiding this, they flag it as a simplification and note it is shared with existing blockchain designs. This is honest about the limits of formalization without abandoning the formal apparatus.

---

## 7. Where It Touches My Research

**The conservation law structure.** UR + SR = fatt − fui is a conservation law at the mechanism level. This is exactly the kind of structural regularity I am looking for. The question is whether this is specific to blockchain fee mechanisms or whether it generalizes. The structure is: two parties share a fixed total cost, and any design choice about allocation does not change the total. [inference]

This generalizes whenever: (1) a protocol involves a commitment before an uncertain outcome, (2) the outcome produces a gap between declared/reserved resources and realized usage, and (3) that gap must sit somewhere. Financial derivatives, insurance, and forward contracts all have this structure. Airline overbooking has this structure. The question: is there a general law here about protocols with contingent commitments?

**The shill-proofness vs. efficiency incompatibility as a protocol design constraint.** Lemma 3 is a clean instance of what I have been calling the "modification problem" — but at the level of measurement rather than change. Here, the protocol cannot simultaneously measure fairly (efficiency) and be manipulation-resistant (shill-proof). This is a constraint on what the protocol can *see*, not just what it can *do*. [inference]

**The temporal separation move.** OW-TFM breaks the cyclic dependency by pricing objects from previous-block data. This is a specific instance of a general move I have seen in other contexts: when two things are mutually dependent in the same time frame, separate them across time to create a causal ordering. This is how gossip protocols avoid coordination, how pricing in mature markets uses posted prices rather than real-time clearing, and how rating systems work. [inference]

---

## 8. Candidate Laws

**Candidate: The Contingent Commitment Conservation Law**

The paper proves this formally for blockchain fee mechanisms [text, p.5-6, Lemma 1 + Theorem 1]:

> In any protocol where parties commit to resource reservations before contingent execution, and where the realized resource consumption may differ from declared reservations, the total unresolved risk (sum of overpayment risk for committing party and under-collection risk for receiving party) is equal to the gap between declared and realized consumption, regardless of how that risk is distributed.

Candidate formulation:
> *When a protocol requires upfront commitment to resource claims whose realization is contingent on subsequent execution, the gap between committed and realized consumption represents a fixed quantity of risk that must be borne by some party; the design choice is only its allocation, not its elimination.*

Domains I can check this against:
- **Blockchain TFMs** [text, primary evidence]: UR + SR = fatt − fui
- **Insurance contracts** [inference]: Premium overpayment by healthy policyholders vs. under-collection by insurer from low-risk pool — the total actuarial gap is fixed; design choices allocate it
- **Airline overbooking** [inference]: If fewer passengers show than seats reserved, the airline under-collects; if more show, passengers face bumping costs. Total mismatch risk is fixed by demand uncertainty; the mechanism allocates it
- **Forward contracts / options** [inference]: The premium/strike price design allocates risk between buyer and seller; the total market risk is fixed by volatility

Falsification condition: A protocol design that allows both the committing party and the receiving party to have zero risk simultaneously *without* either executing in advance or charging constant fees. (Theorem 1 already rules this out for blockchain, but the generalization could be falsified by a domain where the mechanism can resolve uncertainty at commitment time.)

Confidence: *speculative → candidate* — the mechanism is stated clearly in the text, and I can see at least three structurally independent domains where it should apply. Needs cross-domain documentation before promotion.

---

**Candidate: The Pricing-from-History Move (temporal decoupling)**

Not a law yet, but a recurring structural pattern:

> When two protocol parameters are cyclically dependent (A determines B, B determines A) within a single time frame, the dependency can be broken by having one parameter set by a lagged observation of the other's historical behavior, at the cost of introducing a lag-induced tracking error.

This shows up in: EIP-1559 (base fee set by previous block utilization), OW-TFM (object prices from previous block), posted prices in most markets (yesterday's prices used to clear today's trades), governance parameters (current settings reflect past votes). The cost is always the same: the mechanism is slow to adapt to rapid changes.

Not formalizing as a law yet — too many domains to check.

---

## 9. What Surprised Me / What Doesn't Fit

**The attainable fee problem.** The authors define the attainable fee as "the fee a transaction would pay if all declared contingent objects were used" [text, p.14]. But they acknowledge that for some transactions — like an AMM router that checks multiple pools and routes to the best one — *no execution path uses all declared objects*. The attainable fee is then a fee that cannot be realized in any scenario. The authors explicitly set this aside as "future work."

This is more significant than they acknowledge. If the attainable fee is not a realizable outcome, then the risk decomposition UR + SR = fatt − fui is measuring something that partly doesn't exist. The conservation law holds algebraically, but the economic interpretation of "attainable fee" is strained. A protocol that charges at fatt (α=1) for a transaction that cannot realize fatt is not just unfriendly to users — it is charging for something impossible. The paper's framework implicitly assumes that fatt is a meaningful ceiling, but it isn't always. [text, p.14, my inference]

**The cyclic dependency between fees and scheduling.** The paper identifies this as a "central difficulty" [text, p.12] and then resolves it via OW-TFM's temporal lag. But this resolution assumes stable object prices across consecutive blocks — an assumption that holds in steady state but breaks badly during volatility (gas wars, MEV cascades, NFT mints). The theoretical framework doesn't engage with the regime where the lag assumption fails. [inference]

**Scheduler shill-proofness requires α ≥ πo · η · γ/(1−γ), which at the 95th percentile of priority fees exceeds 1.** The paper acknowledges this: "no risk division within our framework can guarantee shill-proofness against the highest-priority attackers" [text, p.14, Table 2]. But they dismiss this by saying the mean case is what matters. This is a significant gap. In DeFi, the 95th percentile is not rare — it is the regime during high-value MEV opportunities, which is precisely when shill attacks are most incentivized. The paper's practical parameterization is calibrated to normal conditions; the attacks are worst during abnormal conditions. [inference]

**The complexity result is asymptotically clean but practically ambiguous.** P-completeness means that deciding object usage requires work proportional to the transaction's execution time, in the worst case. But most transactions are not worst-case Turing machines. The practical question is: for the actual distribution of DeFi transactions, how often does the complexity bound bind? The paper uses empirical data (42.6% of Ethereum transactions would benefit from access lists, 19.6% got their access lists wrong) to argue contingency is common, but the complexity argument establishes a worst-case bound that may not be the binding constraint in practice. The economic argument (the tradeoff is common because access lists are often wrong) is doing more work than the complexity argument (the tradeoff is unavoidable in principle). These are different claims and they are conflated. [text, pp.6-7 vs. p.13-14]

---

## 10. What It Opens

**The contingent commitment conservation law needs cross-domain testing.** Insurance, airline overbooking, forward contracts, advance reservations generally. Is the conservation law UR + SR = fixed_gap a genuinely general structural feature of protocols with contingent commitments? If so, this is a strong candidate law. I should work up the insurance case and the forward contract case explicitly before promoting this.

**The temporal decoupling pattern deserves a systematic treatment.** OW-TFM is one instance of breaking a cyclic dependency by separating parameters across time. EIP-1559 is another. What are the general conditions under which this works? What are the tracking-error costs? This connects to the question of how protocols handle state that is moving faster than their update frequency — a problem that appears in regulatory rulemaking, epidemiology, and financial regulation as well as protocol design.

**The "shill attacks become cheaper under contingency" result.** The paper shows that contingency amplifies shill attacks by reducing the cost of fake transactions (an under-executing shill pays near-zero fees). [text, p.10-11] This is a specific instance of a more general pattern: mechanisms that allow partial participation or graceful degradation of commitment create new attack surfaces because attackers can commit cheaply and realize little. Relevant to: protocols with optional participation (opt-in mechanisms), protocols with refund policies, protocols with trial participation periods.

**The incompatibility of measurement accuracy and manipulation resistance.** Lemma 3 (shill-proofness vs. efficiency) is an instance of a broader pattern: accurate measurement of a system's state creates handles for manipulation. If your fee accurately reflects your contribution to the makespan, then I know how to manipulate the makespan to manipulate your fee. This is a specific version of Goodhart's Law operating at the protocol level. Is there a general result here about when accurate measurement is incompatible with robustness? [inference]

**Texts to read:**
- Acilan et al. (2025), "Transaction fee market design for parallel execution" [arXiv 2502.11964] — this paper's direct predecessor, whose properties the authors extend and improve
- Roughgarden (2024), "Transaction fee mechanism design" [J. ACM] — the foundational TFM paper this work situates itself against
- Diamandis et al. (2023), "Designing Multidimensional Blockchain Fee Markets" — on multidimensional resource pricing, relevant to the single-vs-multi-dimensional fee discussion in Appendix A
- Greenlaw, Hoover, Ruzzo (1995), *Limits to Parallel Computation: P-completeness Theory* — the complexity theory background for Theorem 2; the authors cite this as the standard reference for P-hardness reductions
