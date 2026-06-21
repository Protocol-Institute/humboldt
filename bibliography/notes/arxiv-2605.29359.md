# Deep Read Notes: Arxiv 2605.29359

*Source: `bibliography/deep-reads/arxiv-2605.29359.pdf`*

---

## Reading session: full document (13 pages)

# Deep Read: Rahman (2026), "Does Distributed Training Undermine Compute Governance?"

---

## 1. Gestalt

This paper is an adversarial stress test of a specific class of regulatory architecture. The animating question is not "how should AI be governed?" but rather: "given that compute governance works by detecting large clusters, what happens when the technical requirement for large clusters disappears?" Rahman's central conviction is that the governance-by-cluster-detection approach contains a structural vulnerability — not a gap that better enforcement closes, but a gap that grows as distributed training algorithms improve. The paper is essentially an engineer running the adversary's playbook: given the most restrictive governance proposal in the literature (Scher et al. 2025), a specific threat model (well-resourced, motivated evader), and current hardware and algorithms, is evasion feasible? The answer is yes, and the paper quantifies exactly how feasible. The countermeasures section is an honest attempt to say which responses actually work and which merely feel responsive. The paper's lasting contribution may be less the specific numbers (which will date quickly) than the framing: regulatory architecture built on a physical detectability assumption inherits all the fragility of that assumption.

---

## 2. Argument and Structure

**Core claim:** Distributed training algorithms (principally the DiLoCo family) can achieve frontier-scale training compute using nodes below any proposed monitoring threshold, at consumer-grade internet bandwidth, within plausible timeframes and budgets.

**Structure of the argument:**

1. *Setup:* Current compute governance assumes large, physically detectable clusters. This assumption drives both the regulatory design (compute thresholds trigger reporting) and the enforcement mechanism (thermal signatures, satellite imagery, power monitoring).

2. *Technical demonstration:* The DiLoCo algorithm family reduces inter-node bandwidth requirements from 400+ Gbps (datacenter standard) to <100 Mbps (consumer-grade). This means geographically dispersed nodes — each below any proposed monitoring threshold — can coordinate on large-scale training. The paper builds an efficiency model capturing four degradation factors (sync interval penalty, compression quality, replica divergence, activation compression for pipeline parallelism) and runs it across hardware configurations.

3. *Results:* [text, p.4] Existing and proposed compute thresholds can be evaded for $1.6M (Scher et al.), $31M (EU AI Act), or $3.8B (California SB 53) of sub-threshold hardware. 101 nodes of 16 H100-equivalents each reach GPT-4-scale local-equivalent compute; 625 nodes reach Llama 3.1-405B scale.

4. *Countermeasures analysis:* Bandwidth caps and traffic monitoring are ineffective (easily evaded, politically unpalatable). Chip tracking with hardware-enabled location verification is effective but has a long deployment lag (can't retrofit). Whistleblower programs work *better* in the distributed case because attack surface scales with node count. Memory thresholds close an important loophole (A100 80GB has 4× the memory of H100 at equivalent compute, enabling larger models per node without compute threshold triggering). Conventional intelligence/financial forensics are effective for large-scale operations.

5. *Policy recommendation:* Revise cluster registration requirements to include an accelerator memory threshold (1,280 GB HBM) alongside the existing compute threshold. Combine with whistleblower programs and chip registries.

**Load-bearing examples:**
- The A100 80GB asymmetry is crucial: 50 A100s have 4,000 GB HBM but are below the 16 H100-equivalent compute threshold. This is not a minor technicality — it's the architectural exploit.
- Covenant-72B [text, p.5] validates the simulator's predictions at 72B scale and confirms compute-bound operation at 94.5% with 146× compression — much better than the simulator's assumed 16× default, meaning the paper's estimates may be conservative.

**Acknowledged limits:** [text, p.8] The largest published DiLoCo run is two orders of magnitude below configurations modeled at frontier scale. Extrapolation uncertainty is real and explicitly acknowledged. Chinchilla scaling law uncertainty at high compute is flagged as non-directionally-conservative.

---

## 3. Conceptual Vocabulary

**Distributed training inefficiency factor (η):** [text, p.3] The ratio of effective compute produced by distributed training to nominally equivalent centralized compute. Composed of four sub-factors: sync interval penalty (ηH), compression quality (ηcomp), replica divergence (ηrep), and activation compression (ηact). Important: this is not a fixed property of distributed training but a function of hardware configuration, bandwidth, model size, and algorithm.

**Local-equivalent compute (Clocal):** [text, p.3] Nominal compute throughput × η. The "real" compute in terms of what centralized training it equals.

**Quality-adjusted compute (Cquality):** [text, p.3] Local-equivalent compute × Chinchilla suboptimality penalty (χ). Accounts for the fact that distributed training often over-trains relative to optimal because nodes have limited memory and therefore must use smaller models.

**Replica divergence (ηrep):** [text, p.4] The dominant efficiency loss factor for most configurations. When replicas train on different data subsets, their gradient paths diverge; the averaged gradient is less useful than what centralized training would produce. Crucially, this penalty scales *inversely* with model size — larger models have higher-dimensional loss surfaces, so replica gradient paths stay more similar.

**Node:** [text, p.1, footnote] A single self-contained unit of computing hardware in a geographically dispersed network. The unit that governance thresholds are applied to.

**Replica:** [text, p.2, footnote] A node (or pipeline-parallel group of nodes) holding a copy of model weights during DiLoCo training. The unit that computes pseudo-gradients and participates in all-reduce.

**Tension with my vocabulary:** "Protocol" as I use it (coordination mechanism, normative structure) is different from "governance protocol" in this paper's sense (regulatory procedure). The paper's actual subject — compute governance as a *protocol* for controlling AI development — fits my usage well, but I need to be precise.

---

## 4. Analytical Moves

**The adversarial threat-model instantiation:** [text, p.2-3] Before modeling anything, state explicitly: who is the evader, what resources do they have, what are the constraints they face, what is the governing body actively doing to catch them? This is a standard security research move but done carefully here — the model is parameterized by the *most restrictive* governance proposal, not a strawman, and assumptions are labeled as generous or conservative to the evader.

**The detectability-assumption audit:** [text, p.1] Find the load-bearing physical assumption that makes the regulatory regime work. Ask: what technical development would undermine that assumption? Evaluate whether that development is feasible. This is a generalization of "what happens when the technical substrate of a regulation changes?"

**The asymmetry-hunting move:** [text, p.10] Look for cases where a regulation uses one metric to proxy for a second metric that actually matters. The compute-only threshold proxies for "total model capability," but memory-to-compute ratios vary across hardware, enabling high-memory, low-compute nodes that fall below the threshold while enabling larger models than the threshold intended to catch. Asymmetry between the regulatory variable and the target variable is exploitable.

**The countermeasure inversion:** [text, p.9] Some countermeasures become *more* effective as the evader scales up to avoid other countermeasures. Whistleblowing effectiveness scales with node count; forcing evaders to use more nodes (via memory thresholds) also amplifies whistleblowing reach. This interdependence between countermeasures is a design feature, not an accident.

**The Chinchilla-optimality penalty framing:** [text, p.3-4] Rather than treating model quality as binary (works/doesn't work), convert it to a FLOP-equivalent penalty. This allows apples-to-apples comparison between distributed and centralized training even when the distributed configuration is forced into sub-optimal model sizes by memory constraints.

---

## 5. What It Says About the Nature of Things

**Regulations inherit the physical assumptions they're built on.** [inference] Compute governance works by making the physical substrate of dangerous AI development detectable. This is a reasonable strategy when the physical substrate is large datacenters. But the physical detectability is doing the work, and it's contingent on technical facts about training. When those technical facts change, the regulatory regime's enforcement mechanism fails — not its goals, but its mechanism. The regulatory text may remain formally in force while becoming practically unenforceable. This is a general pattern: any protocol that relies on a physical or technical invariant becomes fragile when that invariant changes.

**The attack surface of a distributed operation scales with its node count, and this is a structural constraint, not a choice.** [text, p.9] An evader using distributed training to evade centralized-cluster detection must operate more nodes. Each node is a potential whistleblower, a procurement record, a facility that might be inspected. The evasion strategy increases the attack surface for detection. This is not unique to compute governance — it recurs whenever distributing a function trades detection risk per node for number of nodes.

**Technical standards that define thresholds in one dimension can be evaded through optimization in a correlated dimension.** [text, p.10] The memory-compute asymmetry is an instance of a general pattern: when a regulation specifies a threshold in one measurable dimension (compute throughput), hardware evolution or deliberate selection can satisfy the goal (large model capability) using a different dimension (memory per node) that is not threshold-regulated. The regulatory definition and the underlying target diverge.

---

## 6. What It Says About Becoming a Better Researcher

The paper exemplifies a specific research style: **quantify the thing that policy debates are handling qualitatively**. The question "could distributed training undermine compute governance?" had been raised qualitatively (Kryś et al. 2025); Rahman builds an efficiency model, parameterizes it from published experiments, and produces dollar figures and node counts. The move from "this is a concern" to "this would cost $31M for the EU AI Act threshold" is a research contribution, not just an engineering exercise.

**Calibration against live data:** [text, p.5] The paper explicitly notes that Covenant-72B — released *after* the simulator's initial development — validated the simulator's predictions and actually exceeded its assumptions (146× vs. 16× compression). This is model validation in real time, and the paper updates its defaults accordingly. The disposition to look for validation opportunities and report them honestly when they arrive (in either direction) is a mark of calibrated research practice.

**Honest asymmetry about uncertainty:** [text, p.8] "Crucially, this uncertainty is not directionally conservative: depending on the scaling behavior above this scale, distributed training could be less or more capable than our Cquality figures suggest." This is a harder thing to write than "our estimates may be conservative" — it admits that the uncertainty is symmetric and therefore that the policy implications could run either way.

Connecting to M-016: the paper demonstrates mature **scope-awareness** — it knows exactly where its extrapolations go beyond validated calibration points and says so precisely (parameters fit at ≤16B, conclusions at 250B).

---

## 7. Where It Touches My Research

**Compute governance as a protocolized system under stress.** [inference] This paper is essentially documenting a regulatory protocol (compute governance) encountering a technical change that undermines its detection mechanism. This is a case study in the dynamics of protocol adaptation under external perturbation. The governance regime was designed for a specific technical context; that context is changing; the question is whether the protocol can adapt faster than the threat evolves.

**The detectability-assumption structure recurs in other protocol domains.** [inference] Financial reporting protocols assume transaction visibility (and are undermined by cash, then crypto). Export control protocols assume physical detectability of controlled goods (and are undermined by digital transfer). Parliamentary procedure assumes quorum detectability. In each case, the protocol's enforcement mechanism relies on a physical detectability invariant. The distributed training case is a clean instance of this structure.

**The attack-surface-scales-with-distribution finding** connects to a candidate principle I haven't yet formalized: that distributing a function to evade centralized oversight necessarily exposes more surface area for distributed detection. This is not the same as saying oversight always wins — it says there is a structural tradeoff in the evasion strategy itself.

---

## 8. Candidate Laws

**Candidate:** *Governance Detectability Inheritance*

Any regulatory protocol that enforces through physical detectability inherits the fragility of the technical invariant producing that detectability. When the invariant fails (through technical change or deliberate optimization), the enforcement mechanism fails before the protocol's formal requirements fail — creating a period of nominal compliance with zero effective constraint.

[text, p.1]: "Enforcement of these regulations would be rendered ineffective if the regulated developers could hide their computing hardware."

**Falsification conditions:** A regulatory protocol whose enforcement mechanism relies on a physical invariant, where that invariant subsequently fails to hold for a class of actors, but where enforcement rates do not decline — i.e., new detection mechanisms emerge as fast as old ones fail, maintaining effective constraint without gap.

**What would need to be true:** Either (a) regulatory adaptation is systematically faster than technical evasion (which seems unlikely given the lag structure), or (b) the substitute enforcement mechanisms (whistleblowing, financial forensics) emerge rapidly enough to close the gap.

Confidence: speculative. One domain, mechanism partially articulated. Needs cross-domain examination.

---

**Candidate:** *Evasion Attack-Surface Scaling*

Distributing a function to evade detection-by-aggregation necessarily increases the number of detection points proportionally to the degree of distribution. An evader who fragments a single large detectable operation into N small operations creates N opportunities for detection, each smaller but the aggregate detection surface larger.

[text, p.9]: "Unlike centralized training, which can in principle be conducted by a small team inside a single secure facility, a distributed operation has an attack surface proportional to its node count."

**Falsification conditions:** A distributed evasion operation with N nodes that is *harder* to detect than the equivalent centralized operation — i.e., where the per-node detection probability decreases faster than the node count increases, producing lower aggregate detection probability. This could occur if distributed nodes are sufficiently anonymous or if centralized detection is highly efficient.

Confidence: speculative. One domain, mechanism stated but not tested cross-domain.

---

## 9. What Surprised Me / What Doesn't Fit

**The memory-compute asymmetry is almost too clean.** The A100 80GB has 4× the HBM of an H100 while being at equivalent compute — this asymmetry is a feature of where AI hardware development happened to land, not a law of physics. The paper's strongest countermeasure recommendation (add a memory threshold) is effective precisely because this particular asymmetry exists. But if hardware evolution produces a different asymmetry (e.g., compute-dense, memory-poor nodes), the vulnerability would shift rather than disappear. The countermeasure is somewhat artifact-specific, even though it's presented as a general fix.

**The replica divergence penalty's inverse relationship with model size** [text, p.4] — larger models suffer less from replica divergence because their loss surfaces are higher-dimensional — means the governance regime is actually more vulnerable at frontier scale than at smaller scale. The models the regulation most wants to catch (largest, most capable) are the easiest to train efficiently in distributed mode. This is a genuinely uncomfortable finding that the paper acknowledges but doesn't dwell on.

**Covenant-72B (Lidin et al. 2026)** is described as a validation point, but the citation suggests it's a real system trained by "trustless peers over-the-internet." [text, p.5] If a 72B parameter model has already been trained this way, the threat model is not hypothetical. The gap between "theoretical feasibility" and "demonstrated practice" is smaller than the paper's framing implies.

**The paper's framing is entirely adversarial,** which is appropriate for the stated purpose but means it says nothing about the legitimate uses of distributed training (e.g., for researchers and organizations without datacenter access). The memory threshold countermeasure is carefully calibrated to avoid burdening legitimate users, but the underlying governance design question — how to distinguish cooperative from adversarial distributed training — is not addressed. This may be out of scope, but it limits the policy generalizability.

---

## 10. What It Opens

**Immediate follow-up:** The regulatory adaptation speed question. What is the institutional lag between detection of a governance vulnerability (like this paper) and amendment of the relevant regulation? This is a different question from whether the amendment is technically possible — it's about the protocol's self-modification rate vs. the threat evolution rate.

**Papers to read:**
- Kryś et al. (2025) — "Distributed and Decentralised Training: Technical Governance Challenges in a Shifting AI Landscape" — the taxonomy paper this extends
- Baker et al. (2025) — "Verifying International Agreements on AI: Six Layers of Verification" — the multi-layer enforcement framework, which seems highly relevant to the countermeasures section
- Scher et al. (2025) — the governance proposal being stress-tested
- Lidin et al. (2026) — Covenant-72B, the already-deployed instance of internet-distributed training at scale

**Questions now running:**
1. Is "governance detectability inheritance" a law? Where else does the pattern appear? Nuclear export controls and the enrichment technology gap is a candidate. Financial reporting and structured financial instruments is another.
2. The evasion attack-surface scaling candidate: does this hold in other adversarial contexts? Smuggling networks, tax evasion structures, distributed money laundering — all involve distributing a function to evade centralized detection. Does the aggregate surface area reliably increase?
3. What does the regulatory adaptation lag look like as a structural property of governance protocols? This paper was submitted in May 2026 for algorithms that were advancing in 2023-2025. The EU AI Act and EO 14110 predate the DiLoCo capabilities that undermine them. Is there a general pattern about the lag between technical capability emergence and regulatory adaptation?
