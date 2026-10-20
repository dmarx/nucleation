---
status: Active
title: 'Exact dynamical closure of a collective variable does not require a nearly decomposable block: in a linear Gaussian VAR(1) with uniform coupling among n units, the sum of all units is exactly dynamically independent at every stable coupling strength, while every partition of the units into two or more groups couples as strongly across its edges as within them'
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Note of 2026-10-20 added, from the reading of Shpak et al.
    (NOTE-tmpl2r9w): in the same system every partition is column-equitable,
    so the vector of block sums closes though no block does. The claim is
    unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a stable VAR(1) with uniform coupling, A =
  αI + β(11ᵀ − I), and non-degenerate Gaussian noise, in which the
  transfer entropy from X to 1ᵀX is not zero; or a partition of the units
  into two or more groups whose cross-group couplings are weaker than its
  within-group ones under this A.
tags:
- complex-systems
- individuation
- mathematics
date: '2026-10-19'
line:
- distributed-agency
- formal-apparatus
answers:
- QUESTION-tmpt64jh
grounds:
- THEORY-733
- CASE-tmpvt6wb
summary: >-
  From A5 of the exchange of 2026-10-19 on coarse-to-fine processes, which
  gave the two-unit continuous-time case (ż = (b − a)z for z = x₁ + x₂)
  and the boxed slogan "Exact aggregation ⇏ near-decomposability". Made
  exact here for n units with [THEORY-733](../theory.d/THEORY-733.md)'s sufficiency condition, and
  checked numerically. It answers the converse half of [QUESTION-tmpt64jh](../questions.d/QUESTION-tmpt64jh.md).
  It does not say the closed sum is one system ([QUESTION-tmplru2n](../questions.d/QUESTION-tmplru2n.md)), and it
  is about partitions of the units: in the eigenbasis of A the same system
  is exactly decomposable, which is the point.
illustrated_by:
- CASE-tmpvt6wb
---
<!-- inactive-ok-file: CLAIM-157 — Proposed; open claims and readings named for context, nothing here rests on their being settled -->
# CLAIM-tmpkoi6k: Exact dynamical closure of a collective variable does not require a nearly decomposable block: in a linear Gaussian VAR(1) with uniform coupling among n units, the sum of all units is exactly dynamically independent at every stable coupling strength, while every partition of the units into two or more groups couples as strongly across its edges as within them

## The claim

Take n ≥ 2 units with X_t = A X_{t−1} + ε_t, ε_t i.i.d. N(0, Σ), Σ ≻ 0,
and uniform coupling A = αI + β(11ᵀ − I), stable (|α + (n−1)β| < 1 and
|α − β| < 1). Let Y = 1ᵀX, the sum.

**Closure.** 1ᵀA = (α + (n−1)β)1ᵀ, so L = 1ᵀ meets [THEORY-733](../theory.d/THEORY-733.md)'s condition
L A = B L with B = α + (n−1)β. By its sufficiency step,
Y_t − B Y_{t−1} = 1ᵀε_t, which is independent of the whole past of X. So
the transfer entropy I(Y_t : X⁻ | Y⁻) is zero: Y is exactly dynamically
independent, for every β, including |β| ≥ |α|, and for any Σ.

**No block.** Every off-diagonal entry of A is β. For any partition of the
units into two or more groups, each cross-group coupling equals each
within-group coupling. So no partition makes the coupling across its edges
small against the coupling inside, which is what near-decomposability asks
([THEORY-661](../theory.d/THEORY-661.md)), and no proper group of units is a block for [CLAIM-157](CLAIM-157.md)'s test.

So closure of a collective variable does not imply that it is the
aggregate of a weakly coupled block. The converse failure, a block whose
aggregate is not exactly closed, is generic by [THEORY-733](../theory.d/THEORY-733.md) and is not the
interesting direction; whether near-decomposability bounds the dependence
is [QUESTION-tmpt64jh](../questions.d/QUESTION-tmpt64jh.md).

## The check

[CASE-tmpvt6wb](../cases.d/CASE-tmpvt6wb.md), n = 6, Σ = I unless stated. The dependence was computed as
½ log det Var(Y_t | Y_{t−1..t−60}) / det Var(Y_t | X_{t−1}) from the exact
stationary covariances. For the sum it was zero to machine precision
(|T| ≤ 2.3 × 10⁻¹⁶) at (α, β) = (0.2, 0.01), (0.2, 0.05), (0.2, 0.1),
(0.2, 0.13), (0.05, 0.15) and (0.3, −0.1), and with a random positive
definite Σ. For a single unit it was 2.7 × 10⁻⁴ to 8.1 × 10⁻², and for the
sum of three units 4.7 × 10⁻⁴ to 8.5 × 10⁻², rising with |β|.

## What it does not say

- **Not that the sum is one system.** Closure is not [CLAIM-157](CLAIM-157.md)'s notion of
  unity, and neither is an agent or a self. Which of them "one system"
  should track is [QUESTION-tmplru2n](../questions.d/QUESTION-tmplru2n.md).
- **Not that near-decomposability is coordinate-free.** In the eigenbasis
  of A (the sum and its orthogonal complement) the system is exactly
  decomposable. The claim is about partitions of the units, which is what
  [CLAIM-157](CLAIM-157.md) groups. The gap that makes the mode definite is the one
  [CLAIM-164](CLAIM-164.md) names, between A's eigenvalues α + (n−1)β and α − β. That is a
  gap between modes, not between groups of members.
- **Not anything beyond the model.** Linear maps, Gaussian noise and VAR(1).
  For VAR(p ≥ 2), lags that are all of the uniform form keep the condition;
  generic lags do not ([THEORY-733](../theory.d/THEORY-733.md)).

## Note of 2026-10-20: every partition aggregates, none is a block

Shpak, Stadler, Wagner and Hermisson ([LIT-tmp6vpg9](../literature.d/LIT-tmp6vpg9.md), read in [NOTE-tmpl2r9w](../notes.d/NOTE-tmpl2r9w.md))
give the exact condition for a partition's block sums to close jointly:
column-equitability ([THEORY-tmpj32n2](../theory.d/THEORY-tmpj32n2.md)). Under uniform coupling every
partition meets it. So in this system grouping the members does find closed
objects, namely the vector of block sums for any grouping, even though no
group is a weakly coupled block and no single group's sum closes on its own.
Re-checked: with six units split three and three, the transfer entropy into
the pair of block sums was 0 to machine precision, and into one block sum
5.0 × 10⁻² at (α, β) = (0.2, 0.1). The claim, which is about blocks and
about the sum of all units, stands. What changes is [QUESTION-tmplru2n](../questions.d/QUESTION-tmplru2n.md): its
choice between "a subset of members" and "a function of the whole state"
leaves out the equitable partition.
