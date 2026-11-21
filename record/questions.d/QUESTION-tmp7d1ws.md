---
status: Open
title: 'What replaces singular learning theory''s fixed-dimension asymptotics, n → ∞ with the parameter count held fixed, when width or parameter count grows in proportion to the data, and does a learning coefficient estimated in that regime still measure the singular geometry?'
version: 1
tags:
- learning-theory
- model-comparison
- mathematical-statistics
date: '2026-11-21'
line:
- learned-structure
summary: >-
  A37 §9 of the exchange "Rich Get Richer Power Laws" (2026-11-21):
  "classical RLCT asymptotics cannot be directly transplanted into a regime
  where network width or parameter count grows proportionally with the
  amount of data", so a combined theory "may need to track at least three
  scales", γ = D/N, an effective dimension and a local learning
  coefficient. A flags the mismatch and gives no theory for it; every
  combined test A proposes depends on it. The wording is A's (the other
  assistant in the exchange "Rich Get Richer Power Laws", A37); adopting it
  is the owner's call.
---

<!-- inactive-ok-file: THEORY-521 CLAIM-tmpcg4uu LIT-tmpnbl2d — Proposed or new, or a Deferred work registered from the exchange and not yet read -->

# QUESTION-tmp7d1ws: What replaces singular learning theory's fixed-dimension asymptotics, n → ∞ with the parameter count held fixed, when width or parameter count grows in proportion to the data, and does a learning coefficient estimated in that regime still measure the singular geometry?

## The question

Watanabe's free energy F_n = nL + λ log n − (m − 1) log log n + O(1)
([THEORY-087](../theory.d/THEORY-087.md)) is an expansion in n with the model fixed. The exchange's
other results are in proportional limits: the spiked-covariance threshold
at β = √γ, γ = D/N, and the concentration of high-dimensional embeddings.
A37 §9: "These are not interchangeable." The record holds a proportional
limit in which generalization error jumps with the load ([THEORY-521](../theory.d/THEORY-521.md), in
perceptrons), but nothing that connects such a limit to a learning
coefficient.

Two parts.

1. **Theory.** When d grows with n, is there an expansion of the free
   energy whose leading complexity term is still governed by a
   singularity invariant, and what plays λ's role?
2. **Measurement.** Local learning-coefficient estimates (Lau et al.,
   [LIT-tmpnbl2d](../literature.d/LIT-tmpnbl2d.md), unread) are made at one network size and one inverse
   temperature. In the proportional regime, does a change in the estimate
   over training measure a change of singular stratum? Or is it confounded
   with sloppy directions coming into resolution, which [CLAIM-tmpcg4uu](../claims.d/CLAIM-tmpcg4uu.md)
   shows can mimic a coefficient below d/2 at fixed n?

A37 also asks "whether a feature becomes spectrally detectable before,
after, or simultaneously with a change in the local learning
coefficient". That ordering is one use of an answer.

## What would count as an answer

For part 1, a derivation or a citation that gives the free energy's
complexity term in a proportional limit for a singular model class, or
shows that none of singular-learning form exists. For part 2, a model in
which both the coefficient and the stratum structure are known, run at
several widths with d/n fixed, showing whether the estimate tracks the
stratum.
