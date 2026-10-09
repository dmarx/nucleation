---
number: 70
status: Active
formerly:
- CLAIM-tmpjl8xd
title: 'Transport induced by one global stochastic kernel carries a global extension of the source model to a global extension of the target model'
version: 1
role: thesis
defeated_if: >-
  A source model with a global extension, transported by restrictions of
  one global kernel, yields a target model with no global extension.
tags:
- mathematics
- contextuality
date: '2026-10-08'
line: pragmatic-transport
works:
- what-survives-translation
answers:
- QUESTION-022
uses:
- TERM-008
summary: >-
  Proposition II of A84, Proposition B2 of C6, the manuscript's
  Proposition 2. Without a common global kernel preservation is not
  automatic, which leaves open whether transport can create or destroy
  contextuality.
supports:
- CLAIM-100
---
<!-- inactive-ok-file: CLAIM-100 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: CLAIM-105 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-070: Transport induced by one global stochastic kernel carries a global extension of the source model to a global extension of the target model

## The claim

A84, Proposition II: global noncontextuality is preserved under local
postprocessing "induced by a common global stochastic channel". Manuscript §6:
"Suppose source e is the collection of marginals of a global distribution p, and
each K_C is the appropriate restriction of one global stochastic kernel K_X into
the target full outcome space. Then (K_X)#p has the required target marginals
and is a global extension of the transported model."

## What it does not say

C6: "Without a common global kernel or a compatible target cover, preservation
is not automatic." It gives a sufficient condition for a transport not to create
contextuality. It says nothing about transports that destroy or create it, which
is where [CLAIM-105](CLAIM-105.md) and [QUESTION-004](../questions.d/QUESTION-004.md) sit.

## What was checked

C7 Appendix A, read on 2026-10-09: "assume a source global law p and a target
global kernel K_X such that every K_C#e_C equals the marginal of K_X#p on τ(C).
Then K_X#p is an explicit global extension." As written this assumes its
conclusion: the equality of marginals is the hypothesis. The manuscript's
statement is the real one. Each K_C is "the appropriate restriction" of K_X,
which reads as naturality: the marginal of K_X on τ(C) depends only on the
source outcome's restriction to C and equals K_C applied to it. Then the
marginal of K_X#p on τ(C) is K_C#(ρ_C#p) = K_C#e_C, since p's marginal on C is
e_C. That is the one-line argument the manuscript gives ("direct by
compatibility of pushforward with marginalization"), and it holds. Active, on
that reading of "appropriate restriction"; Appendix A's own proof restates the
hypothesis and adds nothing. Appendix A also adds the right limit: "The assertion
becomes false if one assumes only local kernels with no globally compatible
realization." 

## Prior art

This proposition is a special case of Karvonen's "Categories of Empirical
Models" ([LIT-tmpes6yu](../literature.d/LIT-tmpes6yu.md)). His natural transformation σ is exactly the component on the whole measurement set, a single global kernel, and his
Lemma 3.12 states the limit that local kernels need not glue. The record's
reader drew this mapping; Karvonen does not mention translation. The
manuscript should cite it.
