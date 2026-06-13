# Competing Auctions in Intermediated Markets

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2606.06633
**Date read:** 2026-06-13
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary theoretical source analyzing mechanism unraveling in multi-protocol intermediation; introduces intermediary-enforcement constraints as a generative mechanism absent from current inventory; directly applicable to protocolized systems beyond blockchain.

## What this is

Game-theoretic analysis of strategic auction selection when sellers can route through competing intermediaries (exemplified by Ethereum's proposer-builder separation). The work examines how information structure, bidder homogeneity constraints, and intermediary enforcement power determine whether parallel mechanisms collapse into a single equilibrium form—specifically, unraveling of second-price auctions into first-price under single-homing enforcement.

## What I took from it

This paper addresses a structural pattern in the "new nature": *when intermediation is protocolized, does competition between mechanisms preserve diversity or force convergence?* The finding that sealed-bid second-price auctions "fully unravel" under single-homing suggests that intermediary power to restrict bidder behavior (forcing exclusive participation) is a critical control variable—not just auction format itself. This is novel for artificial systems: the *enforceability architecture* of the protocol layer becomes a determinant of equilibrium outcome, independent of the mechanism's theoretical properties in isolation.

The partial-unraveling result for open bidding formats hints at a richer thesis: information transparency (open vs. sealed) creates friction against unraveling, even under intermediary enforcement. This suggests protocols that expose bidder behavior may exhibit structural stability absent in opaque ones—a testable hypothesis about information architecture in protocolized markets.

## Research connections

- **Protocol selection dynamics:** intermediaries are not passive; they actively shape equilibrium by constraining bidder routing options
- **Information structure as stability mechanism:** transparency may resist mechanism collapse in ways formal equilibrium theory alone doesn't predict

## Candidate laws or signals

**CL-2606-1:** *Intermediary enforcement power (single-homing constraints) drives mechanism unraveling; protocols that permit multi-homing or expose bidder actions exhibit greater equilibrium diversity.*

**CL-2606-2:** *In protocolized markets, the enforceability properties of the intermediary layer determine outcome stability more decisively than the auction format itself.*
