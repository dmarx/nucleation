---
number: 708
status: Active
formerly:
- THEORY-tmpim3f9
title: "The I_min redundancy credits two independent sources with shared information whenever each reduces surprise about the same target outcomes, so it gives two independent bits copied into the target 1 bit of redundancy; a bivariate redundancy built from reverse information projections, each source's information less what is lost when its posteriors are replaced by mixtures of the other's, satisfies symmetry, self-redundancy, monotonicity and the identity property, gives a nonnegative decomposition, and agrees with I_min on XOR, AND and their compositions but can reverse the state-independent/state-dependent split of a transfer entropy"
version: 1
tags:
- information-theory
- complex-systems
date: '2026-10-17'
source:
- LIT-1168
summary: >-
  Harder, Salge & Polani (2013), [LIT-1168](../literature.d/LIT-1168.md), read in full in [NOTE-944](../notes.d/NOTE-944.md).
  The counterexample, the axioms and the nonnegativity proof are exact;
  every Table I value and both transfer-entropy examples were recomputed.
  The identity axiom and "mechanistic redundancy" are positions, not
  results, and the measure is bivariate only.
---

# THEORY-708: The I_min redundancy credits two independent sources with shared information whenever each reduces surprise about the same target outcomes, so it gives two independent bits copied into the target 1 bit of redundancy; a bivariate redundancy built from reverse information projections, each source's information less what is lost when its posteriors are replaced by mixtures of the other's, satisfies symmetry, self-redundancy, monotonicity and the identity property, gives a nonnegative decomposition, and agrees with I_min on XOR, AND and their compositions but can reverse the state-independent/state-dependent split of a transfer entropy

## Source

Harder, Salge & Polani (2013), "A Bivariate Measure of Redundant
Information", arXiv 1207.2080v3 (Phys. Rev. E 87, 012130), [LIT-1168](../literature.d/LIT-1168.md),
read in full in [NOTE-944](../notes.d/NOTE-944.md). The PRE version was not compared.

## What was actually shown

**The counterexample.** For Z = (X, Y), X and Y independent uniform bits,
I_min(Z; X, Y) = 1 bit. Recomputed: 1.0000, and I_min stays 1 as the
correlation between X and Y varies, while I(X; Y) goes from 1 to 0.

**The measure.** Project each p(z|x) by reverse KL onto
conv{p(z|y)}; the projected information is
Σ_x p(x)[D_KL(p(z|x) ‖ p(z)) − D_KL(p(z|x) ‖ projection)].
I_red is the smaller of the two directions.

**Its properties.** Symmetry, self-redundancy, monotonicity, identity
(I_red((X,Y); X, Y) = I(X; Y)), and nonnegative synergy (Lemma 7), all
proved.

**Comparison.** Same as I_min on XOR (0), AND (0.311), RdnXor (1) and
XorAnd (0.5); different on copying (I(X; Y) against 1) and RdnUnqXor (1
against 2). All recomputed.

**Transfer entropy.** Williams and Beer's coupled pair: same
decomposition under both measures, at every d (recomputed at five
values). A process with an independent bystander: at d = 1, all
state-independent under I_red, all state-dependent under I_min
(recomputed at d = 0.75 and 1).

What could have come out otherwise: a measure satisfying the identity
axiom could have broken monotonicity or produced negative synergy. This
one does neither, for two sources.

## What this does not say

- **That I_red is the right redundancy.** It is one measure that satisfies
  four axioms. The identity axiom is argued for, not derived, and other
  measures with it exist.
- **That independent sources share nothing.** The paper says they can, by
  the mechanism (AND keeps 0.311 bit). That is a position.
- **Anything for three or more sources.** No multivariate I_red is given,
  so it cannot replace I_min in ΦID or in the three-source lattice.
- **That I_min always overstates.** Fig. 3's upper-bound pattern has
  unexplained exceptions.

## Connections

- It corrects [THEORY-706](THEORY-706.md)'s I_min on shared information, and keeps its
  lattice and inversion.
- It leaves [THEORY-712](THEORY-712.md)'s two-term split and [THEORY-707](THEORY-707.md)'s examples
  unchanged in value. It confirms that the SITE/SDTE amounts depend on
  the redundancy measure.
- [THEORY-581](THEORY-581.md)'s synergy bias is computed with I_min, the measure this
  corrects.
- [THEORY-568](THEORY-568.md)'s invariants hold for I_red too, since its atoms satisfy the
  consistency equations.
