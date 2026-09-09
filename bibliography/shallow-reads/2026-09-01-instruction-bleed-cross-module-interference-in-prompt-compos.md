# Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2606.26356
**Date read:** 2026-09-01
**Connected to:** L-011, L-012
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary empirical source documenting a mechanism (architectural non-isolation enabling silent cross-module behavioral leakage) absent from the research inventory; the pattern generalizes beyond prompt composition to any system with shared latent state and concatenated decision modules.

## What this is

An empirical probe of compositional behavioral leakage (CBL) in prompt-composed agentic systems—failure modes where editing one module silently alters behavior of others despite no shared variables or explicit dependencies. The work formalizes the mechanism: transformer self-attention provides no formal boundary between concatenated modules, enabling interference through shared context state. Testing on a deployed job-evaluation agent reveals systematic, reproducible shifts in downstream module behavior when upstream prompts are modified.

## What I took from it

This is a concrete realization of L-011 (Causal Detachment as Stable Protocol Equilibrium) in the specific domain of LLM-composed systems. The paper shows that operational functionality can mask causal dependency relationships—a module can appear to operate correctly while its behavior is actually shaped by upstream prompt state in ways that are:
1. not visible in the module's formal inputs
2. not detectable through standard testing (single-module evaluation)
3. reproducible and systematic rather than random

This directly implicates L-012 (Intervention-Layer Displacement): when a prompt module is edited with intent to change *its own* behavior, the optimization pressure actually displaces to downstream modules, which undergo silent recalibration. The system exhibits what looks like robustness but is actually latent coupling. This connects to seed-019 (embedded-explanation-opacity)—the mechanism producing interference is internal to the transformer's attention state, invisible to the protocol layer that treats modules as compositional.

The work also opens a question about protocol design under architectural non-isolation: if shared latent state is the substrate, then "module boundaries" in prompt systems are regulatory fictions rather than mechanistic truths. This may generalize to any system with shared embedding spaces or context windows.

## Research connections

- **L-011:** CBL is a mechanism by which operationally functional configurations become causally detached from their formal specification; the module works but not because of its declared inputs.
- **L-012:** Editing a prompt module displaces optimization pressure into latent state, moving the actual locus of behavioral control away from the intervention point.
- **L-013:** Protocol systems may tolerate CBL-induced malfunction for extended periods because the malfunction is distributed across module pairs and invisible to single-module auditing.
- **seed-019:** Embedded explanation opacity—the interference mechanism lives in transformer internals, unreachable by interpretability methods operating at the prompt/output level.
- **seed-026:** Incommensurability as deformalization cost—fixing CBL may require abandoning the fiction of modular composition, entailing substantial protocol restructuring.

## Seed

**Seed title:** Latent-State Coupling as Silent Protocol Violation

**Seed type:** observation

**Seed text:** In systems with shared latent state (context windows, embedding spaces, attention mechanisms), compositional modules exhibit systematic behavioral coupling despite formal independence declarations. This coupling is undetectable under single-module testing and becomes visible only under comparative intervention (editing one module, observing downstream drift). The mechanism generalizes beyond prompt systems to any architecture where decision-relevant state is not formally partitioned: the operational boundaries of a protocol module do not align with its causal scope. Systems remain functionally correct under this condition, making the coupling stable and resistant to detection until intervention occurs.
