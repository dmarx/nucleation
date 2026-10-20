---
number: 580
status: Active
formerly:
- THEORY-tmplzpix
title: 'On any cover of a space of input histories, the empirical models compatible with a causal structure are exactly the points of a polytope cut from a product of simplices by linear causality equations, so how much of a model a causal structure can explain is a linear program; causal separability is relative to an assumed ambient structure, and the causally separable fraction is never less than the separable local fraction'
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Promoted, carrying out the promotion audit's decision for THEORY-580
    (batch 055, ADR-047 v2). Its promote_when asked for a full reading that
    follows the proofs of Theorem 2.25 and Proposition 2.29. Both proofs
    (Gogioso and Pinzani §§2.10.11–2.10.18) were read and checked against the
    definitions they use, including those taken from The Topology of
    Causality. The title is unchanged; the dated note below gives the check.
tags:
- causality
- contextuality
- quantum-foundations
date: '2026-10-16'
source:
- LIT-788
summary: >-
  Gogioso and Pinzani (2023), [LIT-788](../literature.d/LIT-788.md), skimmed in [NOTE-624](../notes.d/NOTE-624.md), with the
  proofs of the causaltope theorems (2.18, 2.19, 2.25) and of the lower bound
  (2.29) read and checked on promotion (2026-10-20), against the
  definitions they take from The Topology of Causality. The proofs are short
  because the work is in the definitions; the one step left implicit closes.
  The quantum switches witness indefinite order only relative to an ambient
  space with known no-signalling constraints, not absolutely.
---
<!-- inactive-ok-file: NOTE-624 — Skimmed; the reading this account rests on, as it says -->
<!-- inactive-ok-file: LIT-813 — Superseded; the withdrawn predecessor whose results this paper proves -->

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

## Note of 2026-10-20: the proofs, checked

The proofs in §2.10 were read on promotion, with the definitions they cite
from "The Topology of Causality" (arXiv 2303.07148; its numbering differs
between versions).

- **Theorem 2.19.** A causal function on a lowerset λ assigns outputs at tip
  events, constant on each ∼ω class (Topology, Eq. 9). So causal functions
  correspond one-to-one with free assignments per class (Topology, Obs.
  2.12), and pushing distributions forward gives the convex-linear bijection
  d ↦ ⌈d⌉.
- **Theorem 2.25.** Injectivity is componentwise. For surjectivity, take u
  in the causaltope and set e_λ := ⌊u_λ⌋_λ. The causality equations range
  over every lowerset μ inside two contexts, λ ∩ λ′ among them. Restriction
  commutes with ⌈·⌉ because each tip class in μ lies in one in λ (Lemma
  2.20), so ⌈e_λ|_μ⌉ = ⌈e_λ′|_μ⌉. Theorem 2.19 on μ then gives
  e_λ|_μ = e_λ′|_μ, a step the printed proof leaves implicit. So e is a
  compatible family.
- **Fractions as linear programs.** A component is v with 0 ≤ v ≤ u in the
  cone of a causaltope, which is cut out by linear equations and v ≥ 0; its
  maximal mass is an LP, and so is a decomposition over several sub-spaces.
- **Proposition 2.29.** A separably local model is a mixture of
  deterministic models of separable causal functions, each arising on a
  causally complete Θ′ ≤ Θ, and the causal completions suffice (Topology,
  Def. 2.9, Obs. 2.6). So it decomposes over the completions, and scaling
  by p bounds the causally separable fraction below by p. The fraction is
  defined (Def. 2.15) when the sub-spaces share events, inputs and maximal
  extended histories with Θ, as under free choice.
