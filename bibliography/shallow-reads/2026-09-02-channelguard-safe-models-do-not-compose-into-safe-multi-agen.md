# ChannelGuard: Safe Models Do Not Compose into Safe Multi-Agent Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.19430
**Date read:** 2026-09-02
**Connected to:** L-001, L-012
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Demonstrates a mechanism of intervention-layer displacement across unmonitored composition boundaries in safety-critical agentic protocols — directly instantiates L-012 and exposes a generative condition for protocol ossification under safety pressure (L-001).

## What this is

An empirical study of safety composition failure in multi-agent LLM systems. The paper demonstrates that individual agents equipped with safety filters (input boundary defenses) do not compose into safe multi-agent applications because adversarial instructions can be smuggled through unmonitored inter-agent channels — the "hops" between planner, workers, verifier, and synthesizer. Defenses that guard only entry points become legible optimization targets once agents can communicate laterally.

## What I took from it

This is a direct instantiation of L-012 (Intervention-Layer Displacement in Automated Decision Protocols) applied to multi-agent composition. The safety intervention (per-model filtering) becomes legible as a localized constraint, and the optimization pressure (adversarial injection) displaces to an undefended layer — the protocol channels between agents.

More critically, this exposes a feedback loop that should feed L-001 (Protocol Ossification Under Adoption Pressure): as safety defenses become more stringent and localized, the protocol structure itself ossifies around those defenses. The system cannot be restructured to defend channels without redeploying all agents and monitors — a Gall's-Law trap. Safety interventions thus become infrastructure lock-in mechanisms. The paper's finding that "existing defenses guard only the input boundary" is not a design oversight but a symptom of how safety requirements bind to the nearest-available control surface and resist migration to deeper structural layers.

## Research connections

- **L-001:** Safety defenses applied to individual agents at adoption time become the protocol's visible joints; further modifications to defend composition channels require restructuring the entire system, making the current architecture resistant to change.
- **L-012:** Safety filtering at agent inputs is legible to adversaries; optimization pressure (jailbreak attempts) shifts to unmonitored inter-agent communication channels, a classic intervention-layer displacement.
- **L-005:** Multi-agent safety cannot be retrofitted by replacing individual defenses; it must be evolved into the composition protocol itself — but existing systems are locked into single-layer defense architecture.
- **seed-076 (Handler-Lodged Ossification in Opaque Protocols):** Safety handlers become embedded in opaque agent boundaries; the protocol hardens around this boundary placement.
- **seed-082 (Additive Intervention in Overloaded Protocols Preserves Root Pressure):** Adding per-agent defenses without restructuring channels preserves the root vulnerability to lateral injection.

## Seed

**Seed title:** Composition-Layer Safety Displacement Under Localized Defense
**Seed type:** motif
**Seed text:** In multi-agent protocols where safety obligations are enforced at individual agent boundaries (input filtering, output verification), adversarial pressure systematically displaces to undefended composition channels — inter-agent message passing, context-window smuggling, or implicit state transfer. This displacement is not random: it follows the legibility gradient of the defense architecture. The system cannot migrate defenses to deeper layers without restructuring the entire protocol, causing safety requirements themselves to ossify the composition architecture. Safety thus becomes a mechanism of protocol lock-in.
