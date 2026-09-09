# Mostly Automatic Translation of Language Interpreters from C to Safe Rust

**Source:** cs.MA updates on arXiv.org
**URL:** https://arxiv.org/abs/2606.27122
**Date:** 2026-06-26
**Relevance:** Addresses formalization and safety constraints in translating unsafe systems code (C interpreters) to provably safe language (Rust), directly instantiating CL-001's thesis about formalizing informal systems.

## Summary

arXiv:2606.27122v1 Announce Type: cross 
Abstract: Translating C programs to safe Rust is challenging owing to significant differences in typing constraints, ownership, and borrowing rules. Interpreter programs are particularly important targets for such translation, as they often handle untrusted inputs and suffer from memory-related vulnerabilities. We present Reboot, a mostly-automatic technique that translates real-world interpreter programs from C to safe Rust. Using Reboot, we have translated six interpreters ranging from 6k to 23k lines of C code to safe Rust, with each translation requ
