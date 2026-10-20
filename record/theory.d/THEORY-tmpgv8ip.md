---
status: Proposed
promote_when: 'A proof that, for some non-Gaussian ensemble in the paper''s class, such as random signs, the ℓ₁ recovery transition converges to the Gaussian ρ(δ; C) as N → ∞; or simulations at problem sizes an order of magnitude beyond N = 1600 in which the gap to the Gaussian curve keeps shrinking as N^(−1/2) for an ensemble not used to choose that exponent. More simulations at the same sizes do not settle it.'
title: 'As dimension grows with the undersampling and sparsity ratios fixed, the ℓ₁ phase transition for recovering sparse vectors from random measurements sits at the same curve for a broad class of random-matrix ensembles, those with a kind of orthogonality or weak independence, as for Gaussian matrices, while differing at finite size'
version: 1
tags:
- mathematics
- mathematical-statistics
date: '2026-10-20'
source:
- LIT-1160
summary: >-
  The general reading that [THEORY-391](THEORY-391.md) held before the
  promotion audit narrowed it to what 2,948,000 optimizations at three
  problem sizes showed. Donoho and Tanner (2009),
  [LIT-1160](../literature.d/LIT-1160.md), read in
  [NOTE-933](../notes.d/NOTE-933.md), state it as the hypothesis of "weak
  universality" and pose the class of ensembles it holds for as an open
  problem. Nothing about non-Gaussian ensembles is proved. Filed under
  [ADR-047](../decisions.d/ADR-047.md) v4 so the wide form stays a thesis
  evidence can confirm or reject.
extends:
- THEORY-391
answers:
- QUESTION-168
---

# THEORY-tmpgv8ip: As dimension grows with the undersampling and sparsity ratios fixed, the ℓ₁ phase transition for recovering sparse vectors from random measurements sits at the same curve for a broad class of random-matrix ensembles, those with a kind of orthogonality or weak independence, as for Gaussian matrices, while differing at finite size

## Source

Donoho and Tanner (2009), [LIT-1160](../literature.d/LIT-1160.md), read in [NOTE-933](../notes.d/NOTE-933.md): Findings 1 and 3 and claim C2 ("weak universality", moderate), with the class left undelineated (§3.7: ensembles with "a certain air of 'orthogonality' or 'weak independence'"). The analogy to a new limit theorem (C7) is weak and is not part of this thesis.

## What is asserted, and by whom

The thesis is weak universality: for the two decoders studied, the large-N location of the ℓ₁ transition does not depend on the measurement ensemble within a broad class that includes the eight non-Gaussian ensembles tried. Strict, finite-N universality is not claimed; the authors reject it.

## What the record holds toward it

- [THEORY-391](THEORY-391.md) (Active): the eight ensembles approach the Gaussian curve at N = 200, 400 and 1600, consistent with gaps shrinking as N^(−1/2), an exponent fitted on the same data.
- The Gaussian curve itself is a theorem, by the authors' earlier face-counting results.

## What would confirm or reject it

A proof of convergence to the Gaussian curve for some non-Gaussian ensemble in the class, or simulations an order of magnitude larger with the gap still shrinking for an ensemble not used to fit the exponent, would confirm it. An ensemble of the class whose large-N transition sits elsewhere would reject it. [QUESTION-168](../questions.d/QUESTION-168.md) asks this as a question; this entry is the answer Donoho and Tanner propose.
