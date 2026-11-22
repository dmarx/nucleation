---
number: 2151
status: Proposed
formerly:
- THEORY-tmp3gj1j
title: 'Bialek, Nemenman and Tishby: the predictive information of a stationary series is the subextensive part of its entropy; when the data come from a model with K parameters drawn once from a prior it grows as (K/2) log N, with K replaced by a smaller dimension when the parameterization is degenerate, and when the density of models at small divergence from the target has an essential singularity exp(−B/D^μ) it grows, in the annealed approximation, as N^(μ/(μ+1)), as N^(1/2) for a smooth density under a field-theory prior'
promote_when: >-
  A reading of a later rigorous treatment confirming, under the stated
  conditions, the logarithmic coefficient for regular parametric families
  (Clarke and Barron 1990, or a successor) and, for some nonparametric
  Bayesian problem, power-law growth of I(θ; X_{1:N}) with exponent
  μ/(μ+1) computed exactly rather than in the annealed approximation. The
  record's own linear-Gaussian computation (CLAIM-849, NOTE-2243)
  gives the exponent for one family and shows the annealed coefficient too
  large; it is the filer's and does not by itself meet this.
version: 1
tags:
- information-theory
- learning-theory
- complex-systems
date: '2026-11-21'
source:
- LIT-3008
corroborates:
- CLAIM-805
- CLAIM-825
bears_on:
- QUESTION-517
- QUESTION-507
summary: >-
  Bialek, Nemenman and Tishby (2001), [LIT-3008](../literature.d/LIT-3008.md), read in [NOTE-2243](../notes.d/NOTE-2243.md).
  The source of the three regimes of predictive information the record's
  [TERM-141](../terms.d/TERM-141.md) carries. Their I_pred(T) has an infinite future. The
  power-law class is annealed and its essential singularity posited, then
  derived for one prior; the statements about criticality are asserted,
  not shown.
---
<!-- inactive-ok-file: CLAIM-849 TERM-141 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->
<!-- inactive-ok-file: THEORY-tmpl7rgc — Proposed; the reading of Crutchfield and Feldman, 2026-11-22 -->

# THEORY-2151: Bialek, Nemenman and Tishby: the predictive information of a stationary series is the subextensive part of its entropy; when the data come from a model with K parameters drawn once from a prior it grows as (K/2) log N, with K replaced by a smaller dimension when the parameterization is degenerate, and when the density of models at small divergence from the target has an essential singularity exp(−B/D^μ) it grows, in the annealed approximation, as N^(μ/(μ+1)), as N^(1/2) for a smooth density under a field-theory prior

## Source

Bialek, Nemenman and Tishby, "Predictability, complexity and learning",
[LIT-3008](../literature.d/LIT-3008.md), read from arXiv physics/0007070v3 in [NOTE-2243](../notes.d/NOTE-2243.md).

## What was actually shown

- **Definition and identity.** I_pred(T) = lim_{T′→∞} I_pred(T, T′) = S₁(T),
  the subextensive entropy (Eq. 9); and the information the data carry
  about the parameters "is easily shown to be equal to the predictive
  information about all of the future".
- **Logarithmic class.** For linear regression with Gaussian noise
  (§4.1, Eq. 41) and for any K-parameter family through the density of
  divergences (§4.2, Eq. 63), S₁ → (K/2) log₂ N, "independent even of the
  prior"; a degenerate Fisher matrix gives a phase-space dimension in
  place of K (Eq. 64). Valid for N well above the VC dimension.
- **Power-law class.** If ρ(D → 0) ≈ A exp[−B/D^μ], the annealed
  S₁^(a) ∝ N^(μ/(μ+1)) (Eq. 84); the field-theory prior of §4.6 gives μ = 1
  and √N, "directly proportional to the number of bins that can be put in
  the range of x".
- **Uniqueness.** Under coordinate changes and temporally local
  transformations, only the divergent subextensive part survives as a
  complexity measure (§5.3).

What could have failed: the coefficient could have depended on the prior
or the basis; it does not, in the annealed calculation.

## What this does not say

- **That the power-law coefficients are exact.** They are annealed. In a
  linear-Gaussian model with eigenvalues j^(−p) the annealed coefficient is
  too large by about 1 + 1/p, while the exponent 1/p is right
  ([NOTE-2243](../notes.d/NOTE-2243.md)).
- **That every power law needs an essential singularity of this form.**
  The authors know of no complete Bayesian family of power-law scalings
  (p. 32).
- **That predictive information diverges at critical points.** "At
  critical points the predictive information will diverge with the size
  of the system" is stated with details "to be worked out" (§6, fn. 9).
- **That a growing I_pred implies criticality.** Logarithmic growth comes
  from learning with no transition.
- **Its value for a finite future.** I_pred(T, T) is a case of Eq. 6, not
  the headline quantity; for S₁ = cT^μ it is (2 − 2^μ)cT^μ.

## Note of 2026-11-22: Crutchfield and Feldman, read

**A parallel, with a stated contrast**, no edge (LIT-3010, read in
NOTE-tmpe86ty; THEORY-tmpl7rgc). Crutchfield and Feldman treat excess
entropy and this paper's predictive information as one quantity (their
alias list), report its Ising exponents, and say its parameter-count
result "holds in a slightly different context than ours": an observer
learning a distribution by successive sampling, not one reading block
histograms. They add that logarithmic growth of the excess entropy also
comes from the Thue–Morse sequence, which has no parameter at all
(TERM-141, version 2). They do not take up the assertion that predictive
information diverges at critical points. Status unchanged.
