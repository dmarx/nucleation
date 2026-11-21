---
number: 833
status: Proposed
formerly:
- CLAIM-tmpnu4ar
title: "Model reduction and feature differentiation may be movements in opposite directions through one stratified space of effective models: reduction moves toward the boundaries of the model manifold, where parameters stop mattering, and differentiation moves away from singular strata, where redundant features become separately usable"
version: 1
role: supposed
warrant: interpretive
tags:
- information-geometry
- learning-theory
date: '2026-11-21'
line:
- learned-structure
complements:
- CLAIM-808
grounds:
- LIT-2979
summary: >-
  A39 §6 of the exchange "Rich Get Richer Power Laws" (2026-11-21),
  answering the owner's U24 on Watanabe's stratification and the
  hyperribbon: Transtrum and Qiu's manifold boundary approximation "moves
  toward model boundaries to obtain simpler effective theories", while a
  network "may move away from a singular configuration, making those
  features independently useful", so "learning and compression could
  sometimes be understood as movements in opposite directions through the
  same stratified space of effective models". Supposed: A calls it "a
  proposed duality, not an established general law", and its ground is
  unread. The wording is A's (the other assistant in the exchange "Rich
  Get Richer Power Laws", A39); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-808 ARG-138 CLAIM-812 CLAIM-802 LIT-2979 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21, or a Deferred work registered from it and not yet read -->
<!-- inactive-ok-file: THEORY-2154 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# CLAIM-833: Model reduction and feature differentiation may be movements in opposite directions through one stratified space of effective models: reduction moves toward the boundaries of the model manifold, where parameters stop mattering, and differentiation moves away from singular strata, where redundant features become separately usable

## The claim

A39 §6 sets two processes side by side:

- **Model reduction**: "Many distinguishable mechanisms → fewer effective
  mechanisms. Move toward a reduced limiting model, often located at a
  manifold boundary." This is Transtrum and Qiu's manifold boundary
  approximation method, which "deliberately moves toward model boundaries
  to obtain simpler effective theories" ([LIT-2979](../literature.d/LIT-2979.md), Deferred:
  registered, not read).
- **Feature differentiation**: "Redundant mechanisms → separately
  distinguishable features. Move away from a degenerate configuration into
  a richer functional regime." A network "with two indistinguishable
  hidden features may move away from a singular configuration, making
  those features independently useful."

Then: "the contrast suggests that **learning and compression could
sometimes be understood as movements in opposite directions through the
same stratified space of effective models**."

## A's caveats, which the claim keeps

"This is a proposed duality, not an established general law." Two limits
follow in A's own words: "Learning can also move toward singular strata,
for example through pruning, feature collapse, or effective model
compression", and "model reduction does not always correspond to a literal
singularity in finite parameter coordinates."

## Where it stands in the record

The duality needs the two endpoints to lie in one space: the boundaries
reduction approaches and the strata differentiation leaves. [ARG-138](../arguments.d/ARG-138.md)
finds that this is not yet shown. Many of the boundaries the reduction
method follows lie at infinite parameter values, a rate going to 0 or ∞,
where the model loses a parameter in the limit rather than folding at a
finite point; only some are singular strata at finite coordinates, as the
fold edge of a sum of exponentials is ([CLAIM-812](CLAIM-812.md)). So the claim is
supposed: it holds where the boundary is a stratum, and elsewhere it needs
a compactification of the parameter space in which boundaries at infinity
become strata, which neither A nor the record supplies.

It complements the owner's bet at U24 ([CLAIM-808](CLAIM-808.md)) by naming a
direction of travel through the shared space, where the bet names a
connection between two accounts of it.

## What it does not say

- Not that training never compresses. A names pruning and collapse as
  moves toward strata.
- Not that feature differentiation is a resolution of a singularity in
  the algebraic sense ([CLAIM-802](CLAIM-802.md) and its argument).

## Note of 2026-11-21: Transtrum, Machta & Sethna (2010, 2011) and Transtrum et al. (2015), read

- **The reduction half is corroborated** by the 2015 review
  ([THEORY-2154](../theory.d/THEORY-2154.md)): the manifold boundary approximation "approximate[s] a
  high-dimensional, but thin model manifold by its boundary", reducing the
  EGFR model from 48 parameters to 12 (§IV). The 2010 letter: "Most
  parameters in these models have bounded effects", settable to limiting
  values with finite predictions.
- **The gap is theirs too, unresolved.** "Since most boundaries occur at
  infinite parameter values" (2010, p. 3); in log parameters all of them do,
  and the model graph stretches them to infinity (2011, §IV). The finite
  ones are fold lines, generic only with fewer data than twice the
  parameters. So "boundaries at infinity become strata" still needs the
  compactification this claim's gap names. The duality stays supposed.
- **The boundaries are singular.** "Model boundaries correspond to points
  on the manifold where the metric is singular" (2011, p. 10): reduction
  moves toward rank loss of the metric, which fits the claim's picture of
  one stratified space.
