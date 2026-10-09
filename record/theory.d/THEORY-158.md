---
number: 158
status: Proposed
formerly:
- THEORY-tmpnp46m
promote_when: >-
  A second, independent derivation of the finite-state equivalence. A
  textbook or later paper that proves "[O, H] = 0 iff O is constant on the
  connected components of the transition graph" would do, as would one
  that proves the moment form, or a checked extension of the component
  form to general state spaces. Refuted by an infinitesimal stochastic H
  and a diagonal O on a finite set with both moments conserved in every
  state but [O, H] ≠ 0, or with O non-constant on a component and still
  commuting.
title: 'In a Markov process, an observable commutes with the generator exactly when its mean and variance are both conserved in every state; on a finite state space this means it is constant on each connected component of the transition graph, so a conserved mean alone does not give a symmetry'
version: 1
tags:
- mathematics
- probabilistic-modeling
date: '2026-10-09'
source:
- LIT-773
summary: >-
  Baez & Fong (2013), [LIT-773](../literature.d/LIT-773.md), read in [NOTE-598](../notes.d/NOTE-598.md): Theorem 1
  (finite state space, four equivalent conditions) and Theorems 2–3 (σ-finite
  measure spaces, without the component form). Unlike quantum mechanics,
  where a mean conserved in every state already implies commutation, a
  Markov process can conserve the mean of an observable it does not commute
  with. The theorem covers diagonal observables only; it says nothing about
  symmetries that permute states.
supports:
- CLAIM-094
- CLAIM-107
---

<!-- inactive-ok-file: THEORY-019 — Proposed; named as a parallel on commutants, with no relation claimed -->

# THEORY-158: In a Markov process, an observable commutes with the generator exactly when its mean and variance are both conserved in every state; on a finite state space this means it is constant on each connected component of the transition graph, so a conserved mean alone does not give a symmetry

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
- **Not the component form beyond finite X.** Section 3 gives only the
  moment and commutator forms.
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
