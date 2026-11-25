---
number: 805
status: Proposed
formerly:
- CLAIM-tmp99m8g
title: 'Entropy, correlation and scaling are distinct properties of a system, and a critical point is not the maximum of complexity: what is special there is the absence of a finite correlation scale, while entropy density, predictive information, the number of relevant directions and the cost of simulation need not peak there'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that, for a broad class of lattice or dynamical models with a
  continuous transition, every standard complexity measure (entropy
  density, pairwise or multi-information, predictive information,
  statistical complexity, neural complexity in Tononi, Sporns and
  Edelman's sense) peaks at the critical point, so that "maximally
  complex at criticality" is true of complexity in general and not of one
  chosen measure. A single measure that peaks there does not defeat it.
tags:
- complex-systems
- information-theory
- natural-sciences
date: '2026-11-21'
line:
- formal-apparatus
grounds:
- THEORY-262
uses:
- TERM-141
summary: >-
  A's thesis at A13 §1, §8 and A21 §8 of the exchange "Rich Get Richer
  Power Laws": order, randomness and complexity are three things; entropy
  measures uncertainty, correlation and mutual information measure shared
  structure, and scaling measures how that structure changes with
  observation scale; "neither criticality nor scale invariance guarantees
  a maximum of every sensible complexity measure", and "the special
  property of criticality is the absence of a finite intrinsic
  correlation scale". With it, A's derivation that pairwise mutual
  information at the 2D Ising critical point falls as r^(−1/2), which the
  assistant checked, and two corrections to the turn. The wording is A's
  (the other assistant in the exchange "Rich Get Richer Power Laws", A13
  and A21); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-262 — Proposed reading, the neural-complexity measure -->
<!-- inactive-ok-file: CLAIM-836 — filed with this claim from the same exchange, Proposed -->
<!-- inactive-ok-file: ARG-152 THEORY-2151 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->
<!-- inactive-ok-file: THEORY-2200 — Proposed; the reading of Crutchfield and Feldman, 2026-11-22 -->

# CLAIM-805: Entropy, correlation and scaling are distinct properties of a system, and a critical point is not the maximum of complexity: what is special there is the absence of a finite correlation scale, while entropy density, predictive information, the number of relevant directions and the cost of simulation need not peak there

## The claim

A13 §8 tabulates three properties "often conflated": entropy, "How
uncertain or variable the system is"; correlation and mutual
information, "How much structure is shared between components"; scaling
behaviour, "How those relationships change with observation scale". A
random system has the first without the second; an ordered one the
second without much of the first. Then: "neither criticality nor scale
invariance guarantees a maximum of every sensible complexity measure.
Rather, the special property of criticality is the absence of a finite
intrinsic correlation scale in the ideal infinite system."

A21 §8 lists what need not peak together: "A critical system may exhibit
a divergent correlation length while retaining only a few relevant RG
directions. Its predictive information may or may not diverge … Its
entropy density need not be maximal. And the computational resources
needed to simulate or predict it may depend strongly on the
representation." Its formula: "**Criticality describes a property of the
collective dynamics or statistical state. Complexity describes some
chosen aspect of the information required to represent, generate,
distinguish, or predict that state.**"

The record holds one measure of the "between order and randomness" shape,
Tononi, Sporns and Edelman's neural complexity ([THEORY-262](../theory.d/THEORY-262.md)), and no claim
on whether criticality maximizes complexity. This claim says it does not,
in general.

## A worked case (A's, checked)

A13 §2: for two ±1 spins of zero mean and correlation c, the mutual
information is I(c) = ((1+c)/2) ln(1+c) + ((1−c)/2) ln(1−c) ≈ c²/2 for
small c, so at the 2D Ising critical point, where C(r) ∝ r^(−1/4),
pairwise information falls as r^(−1/2), and off criticality
exponentially. The assistant checked the formula against the joint table
p(±,±) = (1+c)/4, p(±,∓) = (1−c)/4 (equal to machine precision at
c = 0.5, 0.1, 0.01; c²/2 within 0.5% at c = 0.1). A's own qualification:
"information still decreases with distance at criticality … the decline
does not have a finite characteristic distance".

## Corrections to the turn (the assistant's)

- **Relations and fluctuations are not separable.** A13 opens: "perhaps
  the fundamental feature of criticality isn't the presence of large
  fluctuations, but the persistence of *relationships* between
  fluctuations at different scales." A's own §3 then derives the large
  fluctuations from those relations. At the level of second moments they
  are one fact: Var(M)/N = Σ_r C(r), so a divergent susceptibility is a
  non-summable correlation function. The thesis this claim keeps is
  §8's, the absence of a finite correlation scale, not §0's contrast.
- **The shell sum's condition.** A13 §3: a shell at radius r contributes
  r^(d−1)C(r) ∝ r^(d−1−a), "r^(3/4)" for 2D Ising, so the susceptibility
  diverges. The sum Σ_r r^(d−1−a) up to L diverges only if a < d; with
  a = d − 2 + η that is η < 2, and in a finite system it gives
  χ ∝ L^(2−η), L^(7/4) for 2D Ising. The assistant computed the Fisher
  information about the field on L × L tori by transfer matrix, which is
  Var(M): per spin it grows with slope 1.756 in log L over L = 6 to 10,
  against 7/4 ([CLAIM-836](CLAIM-836.md)).
- **A's analogy to the owner's bulk and tail.** A13 §3 presses "Individually
  rare or weak effects can dominate aggregate behavior when there are
  sufficiently many opportunities for them to contribute", and grants
  "The mathematical mechanism isn't identical". The two are different
  sums, one over distances of a weight that falls slower than the number
  of terms grows, the other over event sizes of a probability times a
  size; the record keeps the analogy as A's and does not adopt it.

Predictive information, one of the measures A21 §8 says need not peak at
criticality, is Bialek, Nemenman and Tishby's ([LIT-3008](../literature.d/LIT-3008.md)), read on
2026-11-21 ([THEORY-2151](../theory.d/THEORY-2151.md); see the note below). The worked case and the
corrections above were checked in this session and do not depend on the
work.

## What it does not say

- Not that criticality is not special: the absence of a finite
  correlation scale is special, and some measures (pairwise information
  at long range, susceptibility) do peak there.
- Not that no measure peaks at criticality, nor which measures do: that
  depends on the measure and the observation (A21 §8).

## Note of 2026-11-21: Bialek, Nemenman & Tishby, read

Read in [NOTE-2243](../notes.d/NOTE-2243.md) ([THEORY-2151](../theory.d/THEORY-2151.md)). It was in this claim's grounds,
unread, for predictive information; it carries less than a ground for the
claim as titled, and moves to corroborating it ([ARG-152](../arguments.d/ARG-152.md)).

- **Supports** the separation of entropy from complexity:
  "predictability is a deviation from extensivity"; complexity "should be
  zero both for purely regular and for purely random systems"; "most of
  what we observe is irrelevant to the problem of predicting the future".
- **Leans against** A21 §8's "may or may not diverge" for predictive
  information: "At critical points the predictive information will diverge
  with the size of the system" (§6), with the link to scaling dimensions
  left "to be worked out" (fn. 9). Asserted, not shown; and about growth
  with size at the critical point, not about a maximum across parameters.
  The paper does not claim complexity in general peaks there, and notes
  logarithmic divergence in learning with no transition.
- The claim's thesis is about "every sensible complexity measure"; one
  measure asserted to diverge at criticality does not defeat it, by its
  own defeated_if.

## Note of 2026-11-22: Crutchfield and Feldman, read

**Supports the separation of entropy from memory, and is silent on
criticality** ([LIT-3010](../literature.d/LIT-3010.md), read in [NOTE-2286](../notes.d/NOTE-2286.md); [THEORY-2200](../theory.d/THEORY-2200.md) now
`corroborates` this claim). The golden mean, RRXOR and even processes
share an entropy rate of 2/3 bit and have excess entropies of about
0.2516, 2 and 0.902 bits; complexity measures "based on multiplying G by
hµ" fail "to capture structure or memory, since they are only a function
of disorder hµ" (§IV), which is the claim's point that entropy density
and predictive information are distinct properties. The paper says
nothing about where either peaks relative to a critical point. It cites
Feldman and Crutchfield's "Discovering noncritical organization" (1998)
for the critique, the authors' own work on this claim's subject; no
identifier could be verified for it, so it is not registered. Status
unchanged.
