# They'll Verify. They Just Won't Act. How Authority Framing and Laundered Code Turn a Trusted Agentic CI/CD Pipeline Into an Attack Surface

**Source:** cs.MA updates on arXiv.org
**URL:** https://arxiv.org/abs/2607.19267
**Date:** 2026-07-22
**Relevance:** Directly supports CL-003 (Trust Ratchet in Safety-Critical Protocols)—demonstrates how formal verification stages in multi-agent pipelines create false confidence without corresponding action constraints, enabling adversarial exploitation through authority framing.

## Summary

arXiv:2607.19267v1 Announce Type: cross 
Abstract: We study a five-agent CI/CD pipeline (triage -> developer -> security-scan -> review -> approve/deploy), built from five distinct production LLMs across three providers, behind an LLM firewall in shadow mode. A single untrusted input - an external issue requesting a "usage-telemetry" feature - asks for code that exfiltrates process secrets (dict(os.environ)) to an attacker URL, laundered as observability. Across a pre-registered A x B (x C) factorial (N=20; naive arm N=60) we find: (1) the entry agent does not leak its system prompt (0/40); (2
