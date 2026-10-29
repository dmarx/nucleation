---
number: 233
status: Active
formerly:
- THEORY-tmpip5os
title: "CKA and normalized Bures similarity are the Euclidean and the Bures comparison of normalized kernels, and each bounds the other only within a factor set by the kernels' ranks, so agreement in one does not carry to the other with a dimension-free constant"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Promoted from Proposed to Active at the owner's direction, carrying out
    the promotion audit's decision (record/promotion-audit/decisions/THEORY-233.yaml,
    batch 007). The promote_when asked for a close reading of App. A.3. It
    is met instead by a direct derivation of the envelope (eq. 24) and of
    eqs. 27–28, written out below and in the decision file. The owner's rule of 2026-10-19 (ADR-047): a checked step-by-step re-derivation recorded in the decision file meets a promote_when that asks for a proof the record does not hold, and the THEORY is promoted. Its
    second clause, a measurement on trained networks of how far CKA and NBS
    disagree, tests something the THEORY does not claim. It moves unchanged
    to QUESTION-140. The promote_when is removed. The claim is
    unchanged.
tags:
- representation-learning
- mathematics
date: '2026-10-14'
source:
- LIT-250
summary: >-
  Harvey, Larsen & Williams (2023), [LIT-250](../literature.d/LIT-250.md), §5 and App. A.3, read in
  [NOTE-753](../notes.d/NOTE-753.md). CKA = 1 − ½‖K_X/‖K_X‖_F − K_Y/‖K_Y‖_F‖²_F, while
  NBS = 1 − ½B²(K_X/Tr K_X, K_Y/Tr K_Y), with B the Bures distance. They
  induce the same topology, but CKA/√(r(K_X)r(K_Y)) ≤ NBS² ≤
  min[r(K_X), r(K_Y)]·CKA, saturated at rank 1. NBS bounds CKA of the
  square-root kernels, with equality for commuting kernels. Linear kernels
  only, and the discrepancy is illustrated on Wishart samples, not trained
  networks.
---
<!-- inactive-ok-file: THEORY-002 THEORY-008 — Proposed; cited for context, nothing here rests on them -->

# THEORY-233: CKA and normalized Bures similarity are the Euclidean and the Bures comparison of normalized kernels, and each bounds the other only within a factor set by the kernels' ranks, so agreement in one does not carry to the other with a dimension-free constant

## Source

Harvey, Larsen & Williams (2023), [LIT-250](../literature.d/LIT-250.md), read in [NOTE-753](../notes.d/NOTE-753.md): §5
(eqs. 21–24, 27–28), App. A.3 and Fig. 2.

## What was actually shown

**Two geometries on the same objects.** For centred linear kernels:

- CKA(K_X, K_Y) = 1 − ½‖K_X/‖K_X‖_F − K_Y/‖K_Y‖_F‖²_F (eq. 21), a Euclidean
  comparison of Frobenius-normalized kernels.
- NBS(K_X, K_Y) = 1 − ½B²(K_X/Tr K_X, K_Y/Tr K_Y) (eq. 22), the Bures
  comparison of trace-normalized kernels. NBS is the fidelity of the two
  unit-trace PSD matrices, density matrices in all but name, and by the
  paper's Theorem 1 it is the cosine of the Riemannian shape distance
  ([THEORY-004](THEORY-004.md)).

The two induce the same topology on PSD matrices.

**The envelope (eq. 24).** With r(K) the rank,

CKA/√(r(K_X) r(K_Y)) ≤ NBS² ≤ min[r(K_X), r(K_Y)]·CKA,

saturated when the kernels have rank 1. App. A.3 derives it with the
Fuchs–van de Graaf inequality applied to K/Tr K.

**Two further relations.** NBS(K_X, K_Y) ≥ CKA(K_X^½, K_Y^½), with equality
when the kernels commute (eq. 27). 1 − CKA(K_X^½, K_Y^½) is bounded above by
√(1 − NBS²) (eq. 28).

**Illustration.** On random Wishart matrices the two measures differ by
factors of two to three (Fig. 2).

What could have failed: the measures could have been monotone functions of
each other, so that one ordering of model pairs served for both. The rank
factors in eq. 24 leave room for the orderings to differ.

## What this does not say

- **Not which measure is right.** The paper prefers Bures and shape
  distances for their duality with alignment and their metric property.
  It assumes the orthogonal group as the nuisance group and does not argue
  for it.
- **Not anything about nonlinear kernels.** Everything is for linear
  kernels on finite samples.
- **Not how large the discrepancy is in trained networks.** The comparison
  is on Wishart samples only. That is [QUESTION-140](../questions.d/QUESTION-140.md).
- **Not that the envelope is tight away from rank 1.** Tightness is stated
  only at rank 1.

## Connections

- **[THEORY-002](THEORY-002.md).** Its promote_when names a stability result linking a
  distributional distance to a Bures distance, and adds that a CKA result
  does not count by itself, citing eq. 24. This account is the reason: the
  rank factors mean that a CKA bound gives a Bures bound only with a
  constant that grows with the kernels' ranks.
- **[THEORY-004](THEORY-004.md).** NBS is the kernel side of the duality held there, the
  cosine of the rotation-aligned shape distance. CKA has no such alignment
  reading.
- **[THEORY-008](THEORY-008.md).** Linear CKA is one of the readout-agreement averages
  held there. NBS, a nuclear norm of the cross-covariance, is not among the
  measures listed there.
- Kornblith et al. ([LIT-254](../literature.d/LIT-254.md)) introduced CKA for comparing networks and do
  not relate it to the Bures fidelity.

## Note of 2026-10-19: the envelope, derived directly

Write ρ = K_X/Tr K_X, σ = K_Y/Tr K_Y, A = √ρ√σ, and F = (Tr|A|)², the
fidelity. Then B² = 2 − 2√F, so NBS = √F and NBS² = F. Also
CKA = Tr(ρσ)/(‖ρ‖_F‖σ‖_F), and ‖A‖²_F = Tr(√σρ√σ) = Tr(ρσ).

- **Lower bound.** With s_i the singular values of A, (Σs_i)² ≥ Σs_i², so
  F ≥ ‖A‖²_F = CKA·‖ρ‖_F‖σ‖_F. By Cauchy–Schwarz on the eigenvalues,
  1 = Tr ρ ≤ √r(K_X)·‖ρ‖_F, so ‖ρ‖_F ≥ 1/√r(K_X), and likewise for σ. Hence
  F ≥ CKA/√(r(K_X)r(K_Y)).
- **Upper bound.** A has rank at most r = min[r(K_X), r(K_Y)], so
  (Σs_i)² ≤ r·Σs_i², and F ≤ r·CKA·‖ρ‖_F‖σ‖_F ≤ r·CKA, since
  ‖ρ‖_F ≤ Tr ρ = 1. At rank 1 every step is an equality.
- **Eq. 27.** Tr|A| ≥ |Tr A| = Tr(√ρ√σ). Because ‖K^½‖²_F = Tr K, the
  Frobenius-normalized K^½ is √ρ, so Tr(√ρ√σ) = CKA(K_X^½, K_Y^½). Equality
  holds when A ⪰ 0, in particular when the kernels commute.
- **Eq. 28.** 1 − Tr(√ρ√σ) = ½‖√ρ − √σ‖²_F ≤ ½‖ρ − σ‖₁ ≤ √(1 − F), by the
  Powers–Størmer inequality and then the Fuchs–van de Graaf upper bound.

The steps need only these textbook inequalities, so they do not depend on
the typographical slips the paper's App. A.3 contains.
