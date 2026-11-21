---
number: 510
status: Open
formerly:
- QUESTION-tmp7d1ws
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

<!-- inactive-ok-file: THEORY-521 CLAIM-812 — Proposed or new, or a Deferred work registered from the exchange and not yet read -->
<!-- inactive-ok-file: THEORY-2148 THEORY-2149 CLAIM-804 — Proposed; readings and a claim of 2026-11-21 cited in the dated note -->
<!-- inactive-ok-file: THEORY-2157 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# QUESTION-510: What replaces singular learning theory's fixed-dimension asymptotics, n → ∞ with the parameter count held fixed, when width or parameter count grows in proportion to the data, and does a learning coefficient estimated in that regime still measure the singular geometry?

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
   [LIT-2995](../literature.d/LIT-2995.md), read on 2026-11-21) are made at one network size, one
   inverse temperature, β* = 1/log n, and one localizer precision γ. In the proportional regime, does a change in the estimate
   over training measure a change of singular stratum? Or is it confounded
   with sloppy directions coming into resolution, which [CLAIM-812](../claims.d/CLAIM-812.md)
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

## Note of 2026-11-21: Baik, Ben Arous and Péché, read

**Background.** The proportional-limit result this question cites, the
spiked-covariance threshold β = √γ with γ = D/N, is now read: BBP prove it
for complex Gaussian samples with D ≤ N ([LIT-2986](../literature.d/LIT-2986.md), [NOTE-2241](../notes.d/NOTE-2241.md);
[THEORY-2148](../theory.d/THEORY-2148.md)), and Baik and Silverstein for real samples at any γ
([LIT-2988](../literature.d/LIT-2988.md); [THEORY-2149](../theory.d/THEORY-2149.md)). Both hold the number of spikes fixed as
D, N → ∞: a proportional limit in which the signal's rank does not grow.
That is the regime the question asks about only if the learned structure
stays finite-rank, which [CLAIM-804](../claims.d/CLAIM-804.md)'s row 5 shows can fail. The
readings `bear_on` the question as background, not as an answer.

## Note of 2026-11-21: Lau et al., read

Read in [NOTE-2239](../notes.d/NOTE-2239.md) ([THEORY-2157](../theory.d/THEORY-2157.md)). Partial evidence on part 2, none
on part 1.

- **In one family with d > n, the estimate tracked the coefficient.** The
  deep-linear-network calibration includes runs at 10M and 100M
  parameters with n = 10⁶ (Table 1), and the estimates still track
  Aoyagi's exact values within the scatter of Fig. J.2, mostly
  underestimating by up to about 0.8 in relative error. That is a
  realizable, noiseless linear family, not a proportional limit: widths
  were not varied with d/n fixed, and the outputs carry effectively no
  noise.
- **The estimate has two cut-offs.** On a quadratic loss it is
  Σ ½·te_i/(te_i + γ) with t = n/log n ([NOTE-2239](../notes.d/NOTE-2239.md)), so both the sample
  size and the localizer decide which directions count; part 2's confound
  with sloppy directions coming into resolution ([CLAIM-812](../claims.d/CLAIM-812.md)) runs
  through both.
- **Consistency is conjectured** in the paper (App. D), at β* only, with
  the conditions on γ open; it says nothing on the d-grows-with-n regime.

The relation is written from [THEORY-2157](../theory.d/THEORY-2157.md).
