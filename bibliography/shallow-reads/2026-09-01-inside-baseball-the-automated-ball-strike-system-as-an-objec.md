# Inside Baseball: The Automated Ball-Strike System as an Object Lesson in Technological Rule Enforcement

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2605.16237
**Date read:** 2026-09-01
**Connected to:** L-004, L-008, seed-016
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary source presenting sustained empirical argument that a formally unambiguous rule (strike zone definition) resists automation due to emergent optimization surfaces created by enforcement legibility — directly extends L-008 and challenges the assumption that formalization alone solves protocol ambiguity.

## What this is

An empirical case study of MLB's seven-year attempt to automate ball-strike calls using the Automated Ball-Strike System (ABS). The paper argues that despite clear rulebook definition of the strike zone, the automated enforcement system created unanticipated optimization pressures and behavioral responses that forced iterative redesign—suggesting that rule clarity does not guarantee automation tractability.

## What I took from it

This is a grounded instance of L-008 (Proxy Optimization Under Computable Enforcement) in action: the moment a rule becomes machine-readable and enforcement becomes legible, optimizing agents (pitchers, batters, managers) can target the boundary between the formal definition and the operational measurement system. The paper appears to document not just metric capture (L-004), but the deeper phenomenon that *formalization itself creates new optimization surfaces that were invisible in the human-judgment regime*.

The stopping-rule substitution angle (seed-016) is also live here: seven years of iteration suggests that "getting the rule right" repeatedly failed because the system's legibility opened new strategic dimensions that human umpires had implicitly bounded through judgment opacity. This is not a case of the metric being wrong, but of the *automation* changing what "correct enforcement" means operationally.

## Research connections

- **L-004:** Metric capture — the strike zone is formally defined, but automated enforcement created optimization surfaces (pitcher targeting, batter adaptation) not present under human judgment.
- **L-008:** Proxy Optimization Under Computable Enforcement — the legible measurement system (camera, strike zone geometry) became an optimization target rather than a neutral arbiter.
- **seed-016:** Stopping-rule substitution — seven-year iteration cycle suggests agents learned to substitute formal rule compliance for behavioral intent, shifting the locus of "rule-following."

## Seed

**Seed title:** Formalization Opacity Collapse — Automation Legibility
**Seed type:** observation
**Seed text:** When a protocol rule transitions from human judgment (opaque, adaptive, implicit boundary conditions) to automated enforcement (legible, fixed, formally defined), the enforcement system itself becomes an optimization target. The rule does not change; the surface it presents to strategic agents does. This creates a class of "clearly-defined rules that resist automation" — not because the rule is ambiguous, but because formalization strips away the adaptive opacity that bounded optimization in the human regime. The pattern generalizes to any protocol where enforcement legibility is new.
