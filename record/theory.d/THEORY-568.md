---
number: 568
status: Active
formerly:
- THEORY-tmpkqoc2
title: "Whatever redundancy measure a partial information decomposition uses, provided its atoms satisfy the consistency equation, the average number of single sources an atom can be read from is Σᵢ I(Xᵢ;Y)/I(X;Y) and the average number of sources it cannot do without is Σⱼ I(Xⱼ;Y|X₋ⱼ)/I(X;Y); so the redundancy–synergy index equals (r̄ − 1)·I(X;Y), and for three or more sources it counts a k-way redundancy k − 1 times but synergy once"
version: 1
tags:
- information-theory
- mathematics
date: '2026-10-16'
source:
- LIT-042
summary: >-
  Gutknecht et al. (2025), [LIT-042](../literature.d/LIT-042.md), read in full in [NOTE-045](../notes.d/NOTE-045.md), with the
  combinatorial proofs of Props. 1–4 and 6 checked by hand. The averages
  need only the consistency equation and I(X;Y) > 0; reading them as
  average degrees, and the bounds of Appendix B, need non-negative atoms.
  Corollary 5 overstates Prop. 6 (⇔ for ⇐). The network results are on
  tiny quantised models evaluated on their own training sets, and are not
  part of this account.
---

# THEORY-568: Whatever redundancy measure a partial information decomposition uses, provided its atoms satisfy the consistency equation, the average number of single sources an atom can be read from is Σᵢ I(Xᵢ;Y)/I(X;Y) and the average number of sources it cannot do without is Σⱼ I(Xⱼ;Y|X₋ⱼ)/I(X;Y); so the redundancy–synergy index equals (r̄ − 1)·I(X;Y), and for three or more sources it counts a k-way redundancy k − 1 times but synergy once

## Source

Gutknecht et al. (2025), "Shannon
invariants: A scalable approach to information decomposition", arXiv
2504.15779v1, [LIT-042](../literature.d/LIT-042.md), read in full in [NOTE-045](../notes.d/NOTE-045.md).

## What was actually shown

**The assumption (A7).** For every source subset a, I(a;Y) is the sum of
the atoms Π(α) reachable from a. Nothing else is assumed for Props. 1–4,
in particular no particular redundancy measure.

**The counting argument.** Each I(Xᵢ;Y) contains exactly the atoms
reachable from source i, so Σᵢ I(Xᵢ;Y) counts each atom once per single
source it is reachable from. Each I(Xⱼ;Y|X₋ⱼ) contains exactly the atoms
that need source j.

- **Prop. 1.** The average degree of redundancy r̄ = Σᵢ I(Xᵢ;Y)/I(X;Y).
- **Prop. 2.** The average degree of vulnerability v̄ =
  Σⱼ I(Xⱼ;Y|X₋ⱼ)/I(X;Y).
- **Prop. 3 / Cor. 1.** RSI = Σᵢ I(Xᵢ;Y) − I(X;Y) =
  Σ_{k=2}^n (k−1)·I_r^{(k)} − I_r^{(0)} = (r̄ − 1)·I(X;Y). For n = 2 it is
  the interaction information, redundancy minus synergy. For n ≥ 3 it is
  not.
- **Prop. 4 / Cor. 2.** A dual index, DRSI = I(X;Y) − Σⱼ I(Xⱼ;Y|X₋ⱼ) =
  (1 − v̄)·I(X;Y).

**With non-negative atoms (Appendix B).** r̄ < 1 forces some synergy
(Prop. 5), and r̄ > 1 forces some redundancy of degree two or more, at
least a fraction (r̄ − 1)/(n − 1) (Prop. 6). Atoms redundant across
sources are never vulnerable, so source-level redundancy implies
robustness.

What could have come out otherwise: some choice of redundancy measure
could have changed these averages. The proof shows none can, given (A7).

## What this does not say

- **That the atoms are known.** The invariants fix averages, not the
  individual atoms. The redundancy measure is still needed for those.
- **That PID is now scalable.** The number of Shannon terms is linear in
  n, but each needs a high-dimensional entropy. The paper sidesteps
  estimation by treating the training set as the population (C5, weak).
- **That redundancy rises with depth in networks generally.** The MNIST
  and autoencoder trends come from 5-unit quantised layers, one
  architecture each, measured on the training set (C6–C7).
- **That redundancy aids generalization.** An explicit, untested
  conjecture (C8).
- **That Corollary 5 holds as an equivalence.** Only the sufficient
  direction follows from Prop. 6; [NOTE-045](../notes.d/NOTE-045.md) gives a counterexample to the
  other.
- **That r̄ and v̄ separate orders.** r̄ does not distinguish orders of
  synergy, and v̄ does not distinguish orders of robustness.

## Connections

- Varley & Hoel's synergy bias ([LIT-027](../literature.d/LIT-027.md)) is a lattice-weighted average
  computed with the I_min redundancy, so its sign depends on that choice.
  r̄ is the measure-free analogue. Whether r̄ or v̄ of past→future
  information changes under coarse-graining is computable from entropies
  alone, and neither paper asks it ([NOTE-045](../notes.d/NOTE-045.md)).
- The ΦID emergence criteria ([LIT-025](../literature.d/LIT-025.md)) are stated on the double lattice;
  this paper's setting is single-target and static, so it does not supply
  them.
- Transfer entropy is one summand of v̄'s numerator when the sources are
  two pasts and the target the present ([NOTE-053](../notes.d/NOTE-053.md)); [THEORY-641](THEORY-641.md) gives
  it a likelihood-ratio estimator.
- Baudot & Bennequin read I₃ < 0 as synergy ([LIT-053](../literature.d/LIT-053.md)); for n = 2 that
  interaction information is exactly redundancy minus synergy here.
