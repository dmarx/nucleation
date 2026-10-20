---
number: 497
status: Proposed
formerly:
- THEORY-tmpcxkrx
promote_when: >-
  Two kinds of result, one for each half. For the formal half: a
  first-hand reading of Rosas et al. (2020) that states the conditions of
  the iff theorem and of the exhaustive split into downward causation and
  causal decoupling, and finds them to hold for the redundancy functions
  used in practice. For the empirical half: the same system analysed with
  two or more redundancy functions, or with the redundancy-free sufficient
  criteria, giving the same verdict on whether a named macro feature is
  emergent. A verdict that flips with the redundancy function, or a
  theorem whose conditions exclude the systems it is applied to, would
  refute it as an account of those systems. More applications under one
  unnamed redundancy function cannot settle it.
title: "A macro feature can supervene on a system's present state and still carry information about its future that no small set of parts carries, because supervenience is instantaneous and prediction runs across time; on the integrated-information-decomposition account a system can host such a feature of order k exactly when its dynamics carry k-th-order synergy about their own future, relative to a fixed partition into parts and a chosen redundancy function"
version: 3
history:
- version: 2
  date: '2026-10-17'
  note: >-
    A Connections line: for three or more parts no identity-respecting redundancy gives nonnegative atoms (THEORY-713, CLAIM-343). The account is unchanged.
- version: 3
  date: '2026-10-20'
  note: >-
    Connections gain the reading of the primary paper, Rosas et al. 2020 (NOTE-987, THEORY-764). The account and its source are unchanged; whether the primary paper should join source and how its Proposition 1 gap bears on promotion are left to the owner.
tags:
- complex-systems
- information-theory
- causality
date: '2026-10-16'
source:
- LIT-025
summary: >-
  Mediano et al. (2022), [LIT-025](../literature.d/LIT-025.md), read in [NOTE-010](../notes.d/NOTE-010.md), a review of Rosas et
  al. (2020), which the record does not hold. A feature V_t is causally
  emergent of order k iff Un⁽ᵏ⁾(V_t; X_t′ | X_t) > 0, and a system has one
  iff Syn⁽ᵏ⁾(X_t; X_t′) > 0, split as downward causation plus causal
  decoupling. The review proves none of this and names no redundancy
  function. The quantities change with the partition, which the review
  calls intended, and they are predictive, not interventional, unless p(X′
  | X) is a do()-distribution.
---
<!-- inactive-ok-file: THEORY-240 THEORY-257 THEORY-268 — Proposed; neighbouring accounts named for comparison, nothing here rests on their being settled -->

# THEORY-497: A macro feature can supervene on a system's present state and still carry information about its future that no small set of parts carries, because supervenience is instantaneous and prediction runs across time; on the integrated-information-decomposition account a system can host such a feature of order k exactly when its dynamics carry k-th-order synergy about their own future, relative to a fixed partition into parts and a chosen redundancy function

## Source

Mediano et al. (2022), [LIT-025](../literature.d/LIT-025.md), "Greater than the parts",
read in full in [NOTE-010](../notes.d/NOTE-010.md). It restates Rosas et al. (2020), not held, and
credits Mediano et al. (2019) with the ΦID lattice. Every formal result
here comes to the record second-hand.

## What was actually shown

**The account (§III).** A macro feature V_t is a possibly noisy function
of the present microstate X_t, so it carries nothing about the future
that X_t lacks jointly. It can still predict the future in a way no
single part, or group of at most k parts, does on its own. V_t is
causally emergent of order k iff Un⁽ᵏ⁾(V_t; X_t′ | X_t) > 0 (Eq. 3).

**The theorem, restated.** X_t has causally emergent features of order k
iff Syn⁽ᵏ⁾(X_t; X_t′) > 0, its "emergence capacity" ([7, Thm 1]). That is
a property of the dynamics alone, and needs no candidate V to be named.
The capacity splits as Syn⁽ᵏ⁾ = D⁽ᵏ⁾ + G⁽ᵏ⁾ (Eq. 4): downward causation,
where the feature predicts particular parts, and causal decoupling, where
it predicts itself beyond the parts. A feature emergent at order k is
emergent at every lower order (§IV C).

**Applications (§V), reported without numbers.** Game of Life particles
and a flock's centre of mass pass the practical criteria. In human fMRI,
pairwise G⁽¹⁾ rises from sensory toward association cortex and is higher
than in macaques. G is computed only for pairs, because no efficient
estimator exists for three or more time series (fn. 5).

**What could have come out otherwise.** The theorem could have failed, so
that a system with synergistic dynamics hosted no emergent feature. The
record cannot check it, because the review states it "under relatively
general assumptions" without giving them.

## What this does not say

- **That the measures are causal.** They are neither Granger nor Pearl in
  themselves. They are interventional only if p(X_t′ | X_t) is a
  do()-distribution and faithfulness and the causal Markov condition hold,
  and predictive otherwise (§IV A, fn. 3).
- **That emergence is independent of the observer's choice of parts.**
  Recoding XOR's inputs as (X₁⊕X₂, X₁) turns 1 bit of synergy into 1 bit of
  unique information (fn. 4). The review calls coordinate dependence a
  feature of a mereological theory. It does not say which partition to
  choose.
- **That the verdicts are robust.** Syn⁽ᵏ⁾, D⁽ᵏ⁾ and G⁽ᵏ⁾ need a
  redundancy function (fn. 2), and the review does not say which one its
  applications use. The redundancy-free criteria are said to be
  sufficient, and are not stated.
- **That it compares two descriptions of a system at different
  resolutions.** It relates one macro feature to the parts of one
  description. Varley and Hoel say it lacks a macro–micro comparison; the
  review calls that a misunderstanding. [NOTE-010](../notes.d/NOTE-010.md) finds each right about a
  different thing.
- **That synergy in association cortex supports abstract reasoning.** The
  review says the evidence "suggests that it may". The brain results were
  preprints at the time.

## Connections

- **For three or more parts the redundancy function cannot be fully
  principled.** On the Williams–Beer lattice no redundancy function has
  both the identity property and nonnegative atoms from three sources up
  ([THEORY-713](THEORY-713.md)), so a three-part verdict depends on which axiom is
  dropped ([CLAIM-343](../claims.d/CLAIM-343.md)). For two parts the bivariate measures are
  consistent.

- **Effective-information emergence ([THEORY-222](THEORY-222.md))** is a different formal
  object under the same name: interventional, and comparing two models of
  a known mechanism. [NOTE-010](../notes.d/NOTE-010.md) gives a system on which the two can part:
  the two-bit permutation (X¹, X²) → (X¹⊕X², X¹) has no EI gain at any
  macroscale, but under the minimum-MI redundancy Syn⁽¹⁾ = 1 bit. With a
  redundancy function that has the identity property, Syn = 0 and they
  agree. So whether they disagree depends on the redundancy function, and
  no `rivals` edge is declared.
- **Synergy bias across scales ([THEORY-581](THEORY-581.md))** is Varley and Hoel's
  cross-scale use of the same ingredient. For two elements, Syn⁽¹⁾ is the
  top atom of the lattice their B_syn summarises.
- **Local values ([THEORY-268](THEORY-268.md)).** Varley shows that the expected ΦID synergy
  can be positive while its local value is negative at particular
  transitions, so emergence on this account belongs to the ensemble.
- **Applied to consciousness ([THEORY-240](THEORY-240.md)).** Luppi et al. use a
  synergy-defined workspace, built on ΦID, to locate where integrated
  information falls under propofol.
- **Dynamical independence ([THEORY-257](THEORY-257.md))** is the record's other criterion
  for a macro variable fixed by the dynamics. Both papers name it. The
  relation is now worked out for one-step criteria ([THEORY-764](THEORY-764.md), from
  the primary paper, read 2026-10-20 in [NOTE-987](../notes.d/NOTE-987.md)). Ψ is a whole-minus-sum
  term minus the one-step dependence, whose vanishing implies Barnett and
  Seth's independence. Neither condition implies the other, and both can
  hold with no interaction between the parts.
- **Interventional individuality ([THEORY-424](THEORY-424.md)).** Bourrat makes the
  same associational-versus-interventional point about Krakauer's
  measures, uncited here.

- **The primary paper (2026-10-20).** Rosas et al. 2020 ([LIT-1244](../literature.d/LIT-1244.md),
  [NOTE-987](../notes.d/NOTE-987.md)). Three of its findings bear on this account. Its
  applications compute no ΦID atom: they use only the redundancy-free
  sufficient criteria Ψ and Γ. Syn = D + G holds by definition. And its
  Proposition 1, that Ψ > 0 shows a *feature* emergent, proves only that
  the *system* has synergy. The reading gives a counterexample under MMI,
  a parity of two self-copying bits, with Ψ = 1 bit and no unique
  information.
