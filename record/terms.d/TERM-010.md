---
number: 10
status: Active
formerly:
- TERM-tmp9qq3b
title: 'fidelity, as a weighted three-term directed distortion'
version: 1
tags:
- philosophy-of-language
- information-theory
date: '2026-10-08'
line: pragmatic-transport
summary: >-
  A100's "mathematical centerpiece": minimize observational, decision
  and structural distortion subject to a rate budget I(U;V) ≤ R. The
  manuscript §6 keeps the three terms, drops the rate constraint, swaps
  the weights and demotes it to "a flexible directed fidelity
  functional".
used_by:
- CLAIM-048
superseded_by:
- TERM-043
---

# TERM-010: fidelity, as a weighted three-term directed distortion

## Definition

A100: min_T D_obs(T) + λ D_decision(T) + γ D_structure(T) subject to
I(U;V) ≤ R, "where U and V are source and target realizations, R is the
information-rate budget, and the three distortion terms measure complementary
aspects of fidelity. This is the mathematical centerpiece. The translation,
diffusion, and telephone-game cases become different ways of instantiating the
same construction."

Manuscript §6: L = L_obs + λL_str + γL_dec, "a flexible directed fidelity
functional; there is no universal choice of weights or observational tasks."

## What changed silently

Three things, none argued for in the exchange, on the chunk-6 reader's reading
(the manuscript's form is later than U37):

- the rate budget left the objective and went to §5's rate–distortion function;
- the weights swapped, so that λ now weighs structure and γ decision;
- "centerpiece" became "flexible".

Its terms are [TERM-021](TERM-021.md) (observational) and [TERM-028](TERM-028.md) (decision); the structural term is
the restriction defect of C6 Appendix B.

## Why it is still Active

[TERM-043](TERM-043.md) replaced the weighted scalar as the foundation of fidelity on
2026-10-10. Under it, transports are compared component by component, and a
scalar exists only once a task fixes the weights. The weighted sum survives in
that role, as the scalar a task-fixed weighting gives. It is also what the
manuscript §6 states, as "a flexible directed fidelity functional", and no draft
has yet changed that.
