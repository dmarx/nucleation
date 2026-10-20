---
number: 713
status: Active
formerly:
- THEORY-tmp06heo
title: "No redundancy measure on the Williams–Beer partial-information lattice can satisfy symmetry, self-redundancy, monotonicity, the identity axiom and non-negative atoms once there are three sources: for two independent bits, their XOR and a target that copies all three, identity forces three one-bit atoms under a two-bit total, so one atom is at most −1 bit, and a multivariate decomposition that keeps identity must give up non-negativity or the lattice"
version: 1
tags:
- information-theory
- mathematics
date: '2026-10-17'
source:
- LIT-1202
summary: >-
  Rauh, Bertschinger, Olbrich & Jost (2014), [LIT-1202](../literature.d/LIT-1202.md), read in full in
  [NOTE-965](../notes.d/NOTE-965.md). A proved impossibility, checked by hand and by script. It
  also uses invariance of redundancy under relabelling the target, which
  is not stated as an axiom. I_min escapes it by failing identity, Ince's
  I_ccs by accepting the −1-bit atom.
supports:
- CLAIM-343
---

<!-- inactive-ok-file: THEORY-497 — Proposed; named as the account the theorem bears on and as one escape route, nothing here rests on either being settled -->

# THEORY-713: No redundancy measure on the Williams–Beer partial-information lattice can satisfy symmetry, self-redundancy, monotonicity, the identity axiom and non-negative atoms once there are three sources: for two independent bits, their XOR and a target that copies all three, identity forces three one-bit atoms under a two-bit total, so one atom is at most −1 bit, and a multivariate decomposition that keeps identity must give up non-negativity or the lattice

## Source

Rauh, Bertschinger, Olbrich & Jost (2014), "Reconsidering unique
information: Towards a multivariate information decomposition", ISIT 2014,
arXiv 1404.3146v1, [LIT-1202](../literature.d/LIT-1202.md), read in full in [NOTE-965](../notes.d/NOTE-965.md).

## What was actually shown

**The axioms.** Williams and Beer's symmetry, self-redundancy and
monotonicity with subset equality ([THEORY-706](THEORY-706.md)); local positivity,
non-negative atoms after Möbius inversion; and Harder, Salge and Polani's
identity, I∩((Y, Z): Y; Z) = MI(Y: Z) ([THEORY-708](THEORY-708.md)).

**The counterexample (Theorem 2).** Y1, Y2 independent uniform bits,
Y3 = Y1 ⊕ Y2, X = (Y1, Y2, Y3). Any pair determines the third, so X is a
relabelling of each pair.

- Identity and relabelling give I∩(X: Yi; Yj) = MI(Yi; Yj) = 0, so by
  monotonicity the lattice's lower two levels are zero.
- Identity with a pair as one source gives I∩(X: Yi; YjYk) = MI(Yi; YjYk)
  = 1, so each of the three atoms {i}{jk} is 1 bit.
- Monotonicity bounds I∩(X: {12}{13}{23}) by MI(X; Y1Y2Y3) = 2. That node
  sits above all three {i}{jk}, so its atom is at most 2 − 3 = −1.

Checked: every information value above, and the lattice order, by script
([NOTE-965](../notes.d/NOTE-965.md)).

**Bivariate side results.** Bertschinger et al.'s unique information is
monotone in each argument (Lemma 3). Their shared information increases
with a source (Lemma 4). Shared and synergistic information violate left
monotonicity (AND, XOR), so neither has a chain rule in the target.

What could have come out otherwise: XORCOPY could have admitted a
non-negative assignment consistent with identity. It does not, and the
deficit is exactly one bit.

## What this does not say

- **That no multivariate decomposition with identity exists.** Only that
  it cannot be a non-negative decomposition on the Williams–Beer lattice.
  The authors call for a different structure and do not give one.
- **That the theorem binds a two-source analysis.** On the bivariate
  lattice Bertschinger et al.'s measures satisfy every axiom
  ([THEORY-705](THEORY-705.md)). The record's transfer-entropy examples are bivariate
  ([CLAIM-335](../claims.d/CLAIM-335.md)).
- **That it is free of further premises.** It uses invariance under
  relabelling the target, and identity applied to a pair as one source.
  A weaker identity on single variables only is not refuted by it.
- **Which axiom to drop.** I_min drops identity and keeps non-negative
  atoms; on XORCOPY it gives {1}{2}{3} = {12}{13}{23} = 1. I_ccs drops
  monotonicity and local positivity; it gives {i}{jk} = 1 and
  {12}{13}{23} = −1 ([THEORY-714](THEORY-714.md)). The theorem does not choose.

## Connections

- [THEORY-497](THEORY-497.md): ΦID's lattice is a product of Williams–Beer lattices,
  so for three or more parts an identity-respecting redundancy function
  must produce negative atoms. That is the record's inference
  ([NOTE-965](../notes.d/NOTE-965.md)).
- [THEORY-568](THEORY-568.md) is the redundancy-measure-free route: its Shannon invariants
  are fixed by mutual informations once the atoms satisfy the consistency
  equations, so they do not depend on which axiom is dropped. That they
  survive negative atoms is the record's reading of that account, not
  checked against its source.
