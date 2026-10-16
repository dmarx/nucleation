---
number: 580
status: Proposed
formerly:
- THEORY-tmplzpix
promote_when: >-
  A full reading that follows the proofs of the causaltope theorem
  (Theorem 2.25) and of the lower bound by the separable local fraction
  (Proposition 2.29), or an independent proof of either. Either would
  promote it as stated; a gap in either proof would send it back. The
  computed examples cannot settle it, since they are checks of the
  framework on chosen models, and neither can agreement with the withdrawn
  LIT-813, whose corresponding results were stated with proofs deferred.
title: "On any cover of a space of input histories, the empirical models compatible with a causal structure are exactly the points of a polytope cut from a product of simplices by linear causality equations, so how much of a model a causal structure can explain is a linear program; causal separability is relative to an assumed ambient structure, and the causally separable fraction is never less than the separable local fraction"
version: 1
tags:
- causality
- contextuality
- quantum-foundations
date: '2026-10-16'
source:
- LIT-788
summary: >-
  Gogioso and Pinzani (2023), [LIT-788](../literature.d/LIT-788.md), skimmed in [NOTE-624](../notes.d/NOTE-624.md): the
  introduction, the causaltope theorems, standard causal separability and
  the quantum-switch examples, with the proofs unread. It proves in general
  the polytope and causal-fraction claims that the withdrawn [LIT-813](../literature.d/LIT-813.md) made
  with proofs deferred. Proposed because it rests on a skim of proved
  results. The quantum switches witness indefinite order only relative to
  an ambient space with known no-signalling constraints, not absolutely.
---
<!-- inactive-ok-file: NOTE-624 — Skimmed; the reading this account rests on, as it says -->
<!-- inactive-ok-file: LIT-813 — Superseded; the withdrawn predecessor whose results this paper proves -->
<!-- inactive-ok-file: THEORY-165 THEORY-171 — Proposed; named to say this reading does not test them -->

# THEORY-580: On any cover of a space of input histories, the empirical models compatible with a causal structure are exactly the points of a polytope cut from a product of simplices by linear causality equations, so how much of a model a causal structure can explain is a linear program; causal separability is relative to an assumed ambient structure, and the causally separable fraction is never less than the separable local fraction

## Source

Gogioso and Pinzani (2023), [LIT-788](../literature.d/LIT-788.md), "The Geometry of Causality", arXiv
2303.09017v2, skimmed in [NOTE-624](../notes.d/NOTE-624.md). Sections 1, 2.3, 2.4 and the examples of
2.6.6 and 2.7 were read; the proofs (2.10) were not. The skim is the whole
basis of this document.

## What was actually shown

**Causaltopes (Theorems 2.18–2.19, 2.25; Definition 2.12).** A causal
constraint is a marginal equation: two contexts sharing a lowerset of input
histories must agree on it. The pseudo-empirical models (one conditional
distribution per context, no cross-context constraint) form a product of
simplices. Slicing it by the causality equations gives the causaltope, and
empirical models on a cover correspond convex-linearly to its points. On
the standard cover, equations indexed by histories suffice.

**Fractions (Definitions 2.14–2.16).** The supported fraction, the causal
fraction over a family of spaces and the causally separable fraction are
maximal-weight decompositions, so each is a linear program.

**Relative separability (Proposition 2.26, §2.4).** Refining a space gives
inclusion of standard causaltopes. The no-signalling polytope lies inside
every one, and the indiscrete one is the full pseudo-empirical polytope. So
whether a model is causally separable depends on the ambient space assumed.

**Lower bound (Proposition 2.29).** The causally separable fraction is at
least the separable local fraction. Conjecture 2.30, that local and
causally separable implies local in a causally separable way, is open.

**Examples (§§2.6.6, 2.7), computed.** The BFW model is 0% supported by every
causally complete 3-event space and 100% by each of three "one party first,
two indefinite" orders. A switch with Bell-entangled control has a causally
separable fraction of about 63.2% for the model shown; with GHZ control,
about 41.2%. Two contextually controlled classical switches give 75%, equal
to the local fraction of the controlling Bell model. Every example is fully
separable once the no-signalling constraints to the measuring parties are
dropped.

**What could have come out otherwise.** The causally compatible models
could have formed a non-convex set, as they do for causal Bayesian networks
with factorisable sources, which the paper sets itself against. The
theorem says they do not here.

## What this does not say

- **That the proofs were checked.** They were not read ([NOTE-624](../notes.d/NOTE-624.md)).
- **That quantum switches show indefinite causal order outright.** The
  witnesses are conditional on assuming part of the causal structure; with
  the indiscrete ambient space everything is separable.
- **What quantum theory allows.** The causaltopes are theory-independent and
  over-approximate the quantum-realisable models.
- **That the separable fraction always equals the local fraction.** It is a
  lower bound, not always tight. In the contextually controlled switch they
  coincide "by construction".
- **Exact values.** The fractions in §2.7 come from grids of angles and are
  reported "at the angular resolution" used.

## Connections

- It proves, in general, Proposition 16 of the withdrawn [LIT-813](../literature.d/LIT-813.md) ([NOTE-629](../notes.d/NOTE-629.md))
  as Theorem 2.25, and computes its deferred BFW claim. [LIT-813](../literature.d/LIT-813.md)'s
  construction of the locale of inputs fails as stated, and this paper does
  not cite it.
- Its examples are on the standard cover, where the solipsistic
  contextuality of [THEORY-171](THEORY-171.md) does not show, so they neither support nor
  test it.
- Its fractions are linear-programming values over polytopes, the setting of
  [THEORY-165](THEORY-165.md) on the contextual fraction, which this reading does not test.
