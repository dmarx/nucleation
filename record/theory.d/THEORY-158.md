---
number: 158
status: Active
formerly:
- THEORY-tmpnp46m
title: 'For a Markov process on a finite state space, an observable commutes with the generator exactly when its mean and variance are both conserved in every state, which is exactly when it is constant on each connected component of the transition graph, so a conserved mean alone does not give a symmetry'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed to the finite state space and promoted from Proposed to Active
    at the owner's direction, carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-158.yaml, batch 008, ADR-047).
    Theorem 1's cycle of four conditions, and the Section 1 counterexample,
    are re-derived step by step in the decision. Under ADR-047 v2, the
    owner's rule of 2026-10-19, that meets the promote_when's request for a
    second, independent derivation of the finite-state equivalence. The
    title's first clause stated the moment form for Markov processes in
    general. Beyond finite X, the source's Theorems 2–3 give that form on
    σ-finite measure spaces, and they are not re-derived here. The title now
    leads with the finite case, and Theorems 2–3 are reported as the
    source's. The general-space clause of the promote_when moves to
    QUESTION-tmpnm9ml, and the promote_when is removed.
tags:
- mathematics
- probabilistic-modeling
date: '2026-10-09'
source:
- LIT-773
summary: >-
  Baez & Fong (2013), [LIT-773](../literature.d/LIT-773.md), read in [NOTE-598](../notes.d/NOTE-598.md): Theorem 1
  (finite state space, four equivalent conditions), which the record
  re-derived. Theorems 2–3 (σ-finite measure spaces, without the component
  form) are reported as the source's (QUESTION-tmpnm9ml). Unlike quantum mechanics,
  where a mean conserved in every state already implies commutation, a
  Markov process can conserve the mean of an observable it does not commute
  with. The theorem covers diagonal observables only; it says nothing about
  symmetries that permute states.
supports:
- CLAIM-094
- CLAIM-107
---

<!-- inactive-ok-file: THEORY-019 — Proposed; named as a parallel on commutants, with no relation claimed -->

# THEORY-158: For a Markov process on a finite state space, an observable commutes with the generator exactly when its mean and variance are both conserved in every state, which is exactly when it is constant on each connected component of the transition graph, so a conserved mean alone does not give a symmetry

## Source

Baez & Fong (2013), [LIT-773](../literature.d/LIT-773.md), read in full in [NOTE-598](../notes.d/NOTE-598.md): Theorem
1 with its proof, the counterexample of Section 1, and Theorems 2–3 of
Section 3.

## What was actually shown

Take a finite set X, an infinitesimal stochastic H (off-diagonal entries
≥ 0, columns summing to zero) and an observable O : X → ℝ. Theorem 1
proves that four conditions are equivalent:

- [O, H] = 0;
- every polynomial in O has a constant mean along every solution of the
  master equation;
- O and O² have constant means along every solution;
- O is constant on each connected component of the transition graph,
  where an edge j → i means Hᵢⱼ ≠ 0.

The key step is that Σᵢ (Oⱼ − Oᵢ)² Hᵢⱼ is a sum of non-negative terms,
and it equals a combination of the time derivatives of ⟨O⟩ and ⟨O²⟩ at
the point mass on j.

That the mean alone could have sufficed is ruled out by an explicit
3-state example. H moves state 2 to states 1 and 3 at equal rates, and
O = (0, 1, 2), so the mean of O is conserved but [O, H] ≠ 0. On a σ-finite
measure space the moment form (not the component form) holds for a single
stochastic operator (Theorem 3, by Chebyshev's inequality) and for Markov
semigroups (Theorem 2, stated as a consequence).

## What this does not say

- **Not Noether's theorem in its original sense.** The paper says its
  version is "somewhat removed" from the Lagrangian original. It
  generalises the commutator form, in which the observable is both the
  conserved quantity and the generator of the symmetry.
- **Not a theorem about symmetries that permute states.** Only
  multiplication operators are treated. A permutation of X commuting with
  H, which is what "symmetry" usually means for a Markov chain, is outside
  it.
- **Not that conserved means are uninteresting.** An observable with
  Hᵀ O = 0 has a conserved mean in every state without commuting with H.
  The paper does not study such observables, and their name and role
  (harmonic functions of the process) are the reader's gloss.
- **Not the general-space form, as the record's.** Beyond finite X,
  Section 3 gives only the moment and commutator forms: Theorem 3 for one
  stochastic operator, by Chebyshev, and Theorem 2 for Markov semigroups,
  stated as a consequence. Neither is re-derived here, and there is no
  component form. That is [QUESTION-tmpnm9ml](../questions.d/QUESTION-tmpnm9ml.md).
- **Not "standard deviation" in the abstract's sense.** Conservation of
  the mean and of the second moment is what is proved. That is equivalent
  to a conserved mean and variance, and so to a conserved standard
  deviation, but the proof works with ⟨O²⟩.

## Connections

The commutant described here is a block structure. H can only be
commuted with by observables that label regions it never connects. This
parallels [THEORY-019](THEORY-019.md), where operators commuting with a group respect its
isotypic components, and [THEORY-042](THEORY-042.md), where superselected observables
label sectors no observable connects. Both parallels are the record's,
not the paper's.

## Note of 2026-10-19: Theorem 1, re-derived

The promotion audit's batch 008 re-derived the finite-state cycle
(ADR-047 v2). X is finite, and H is infinitesimal stochastic: off-diagonal
Hᵢⱼ ≥ 0, and columns sum to 0. The master equation is ψ′ = Hψ, and O is a
function on X. Write d⟨f⟩/dt = Σᵢ f(i)(Hψ)ᵢ = Σⱼ ψⱼ Σᵢ f(i)Hᵢⱼ. This
vanishes along every solution iff Σᵢ f(i)Hᵢⱼ = 0 for every j, since the
starting point can be any point mass.

- **The moments give components.** If O and O² have constant means, then
  for every j,
  Σᵢ (Oⱼ − Oᵢ)² Hᵢⱼ = Oⱼ² Σᵢ Hᵢⱼ − 2Oⱼ Σᵢ OᵢHᵢⱼ + Σᵢ Oᵢ² Hᵢⱼ = 0.
  The i = j term is 0, and every other term is non-negative. So Hᵢⱼ ≠ 0
  implies Oᵢ = Oⱼ: O is constant on each connected component. It also
  gives [O, H]ᵢⱼ = (Oᵢ − Oⱼ)Hᵢⱼ = 0.
- **Commutation gives every moment.** If [O, H] = 0, then
  (Oᵢ − Oⱼ)Hᵢⱼ = 0, so O is constant on components. Then for every
  polynomial p, Σᵢ p(Oᵢ)Hᵢⱼ = p(Oⱼ)Σᵢ Hᵢⱼ = 0. Every polynomial in O has a
  constant mean, which closes the cycle.
- **The counterexample.** Let H₁₂ = H₃₂ = r and H₂₂ = −2r, with all other
  entries 0, and O = (0, 1, 2). Then Σᵢ OᵢHᵢ₂ = −2r + 2r = 0, so the mean of
  O is conserved. But [O, H]₁₂ = −r ≠ 0, and Σᵢ Oᵢ²Hᵢ₂ = 2r, so the second
  moment is not conserved.
