---
number: 8
status: Active
formerly:
- TERM-tmp6szt9
title: 'transport'
version: 3
history:
- version: 3
  date: '2026-10-08'
  note: >-
    The crystallized argument (A108 §13) gave transport four components,
    the fourth "Criteria determining which observable and decision
    structures are preserved". The manuscript (§6) moves the criteria out
    into the fidelity functional and lets the transport "also specify task
    correspondences and decoder side information". Unremarked.
- version: 2
  date: '2026-10-08'
  note: >-
    A81 §5.2 (U30) made transport context-indexed: a context map τ and
    outcome-level Markov kernels K_C, compatible with restriction,
    "formulate[d] as a morphism or lax morphism between observational
    systems". C6 Appendix B kept the kernels and called compatibility a
    "naturality-like law"; the lax-morphism framing was dropped. Version 1
    was the utterance-level map of U20 and A50.
tags:
- mathematics
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
summary: >-
  The owner's word at U20 for the map Φ from source to target
  communicative states: directed, possibly stochastic and non-
  invertible, required only to get within ε. Renames A48's "state
  correspondence" and A49's "admissible correspondence". The
  manuscript's central term (§6).
used_by:
- CLAIM-101
- CLAIM-106
- CLAIM-070
- CLAIM-121
---
<!-- inactive-ok-file: CLAIM-101 — Superseded; replaced, and cited as the history this entry answers or replaces -->
<!-- inactive-ok-file: CLAIM-106 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# TERM-008: transport

## Definition

U20: "there should be some transport map that at least gets to within some
eps". A50: "There is no requirement that the transport be invertible or
symmetric ... transporting the communicative structure of a nineteenth-century
poem into contemporary slang need not be equivalent to transporting the modern
version back." A50 §6 made translation itself a stochastic reconstruction
kernel T(v | u, c), not a map u ↦ v; A52 §4.1 called these "stochastic transport
kernels".

## What it is not

Not a correspondence witnessing equivalence, which is what Φ was from A34 to
A49. Manuscript §6: "A transport from source C_o to target C_t consists of a
correspondence τ between appropriate source and target contexts and local
stochastic kernels ... It is intentionally directed: compression and
interpretation need not be invertible." That definition arrived at A81 §5.2:
K_C : E_o(C) ⇝ E_t(τ(C)), "Require appropriate compatibility with restriction
maps when a transport is intended to preserve observational structure. Formulate
the resulting construction as a morphism or lax morphism between observational
systems." C6 Appendix B: "restrict_tau(D) K_C = K_D restrict_D, interpreted as
equality of kernels. This naturality-like law means that transporting and
forgetting observations agrees with forgetting and transporting." The
lax-morphism framing, which would have named the approximate case
categorically, did not reach C6 or the manuscript. A86 also modelled translation
as an utterance-level channel T(v | u); the two levels are never formally
related, and the manuscript uses both.
