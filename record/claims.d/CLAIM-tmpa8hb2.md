---
status: Proposed
title: 'Watanabe''s stratification of a model''s parameter space connects to the hyperribbon account of sloppy models'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that in the models both accounts treat, the strata, their
  learning coefficients and the hyperribbon's widths or Fisher eigenvalues
  vary independently, so that neither constrains the other anywhere: no
  sloppy direction ending at a stratum, and no regime in which an
  unresolved sloppy direction and a singular one have the same effect on
  learning. A pair of models in which one property occurs without the
  other does not defeat it; the owner's claim is a connection, not an
  identity.
tags:
- information-geometry
- learning-theory
date: '2026-11-21'
line:
- learned-structure
- formal-apparatus
grounds:
- CASE-tmpb2gly
- THEORY-087
- THEORY-774
- THEORY-tmpkoje5
- THEORY-tmpgsgka
bears_on:
- QUESTION-tmpsy8qn
summary: >-
  The owner's U24 in the exchange "Rich Get Richer Power Laws"
  (2026-11-21), after A37's account of singular strata and the exchange's
  earlier hyperribbon (A19 §4): "i bet wattanabe's stratification account
  connects nicely to that hyperribbon account from earlier". The thesis is
  the owner's. A39 took it up and added that the two are "related but not
  the same" ([CLAIM-tmpcgvcp](CLAIM-tmpcgvcp.md)); where they meet and part is
  [CLAIM-tmpcg4uu](CLAIM-tmpcg4uu.md), the assistant's.
---

<!-- inactive-ok-file: CLAIM-tmpcgvcp CLAIM-tmpcg4uu CASE-tmpb2gly ARG-tmpj0r42 LIT-354 — Proposed or new, or Deferred works not yet read, or Unavailable; filed with this claim -->
<!-- inactive-ok-file: ARG-tmp97cwb CLAIM-tmpnu4ar THEORY-tmpgsgka THEORY-tmpkoje5 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# CLAIM-tmpa8hb2: Watanabe's stratification of a model's parameter space connects to the hyperribbon account of sloppy models

## The claim

U24, verbatim: "i bet wattanabe's stratification account connects nicely
to that hyperribbon account from earlier".

Watanabe's account (his book [LIT-354](../literature.d/LIT-354.md) is Unavailable; its core is read in [LIT-616](../literature.d/LIT-616.md) and [THEORY-087](../theory.d/THEORY-087.md)) divides a model's
parameter space into strata on which the map from parameters to
distributions has different local structure. The learning coefficient
on a stratum sets the Bayesian complexity penalty. The hyperribbon account
(Transtrum, Machta and Sethna, [LIT-tmpd3swn](../literature.d/LIT-tmpd3swn.md) and [LIT-tmpzkxka](../literature.d/LIT-tmpzkxka.md), registered
from the exchange and read on 2026-11-21: [THEORY-tmpkoje5](../theory.d/THEORY-tmpkoje5.md), [THEORY-tmpgsgka](../theory.d/THEORY-tmpgsgka.md)) describes a sloppy model's image as a
ribbon whose widths fall off geometrically, so that most parameter
combinations barely move the predictions. The record holds the
eigenvalue spread behind it for one model ([THEORY-774](../theory.d/THEORY-774.md)). The owner bets
that the two connect.

## Where it stands

- **A's development (A39).** The connection is "especially clear at the
  boundaries of model manifolds": in F(a, b) = (a + b, ab), a sloppy
  direction becomes exactly degenerate as two mechanisms merge
  ([CASE-tmpb2gly](../cases.d/CASE-tmpb2gly.md)). But "a model can be highly sloppy without being
  singular", and the reverse; that part is [CLAIM-tmpcgvcp](CLAIM-tmpcgvcp.md).
- **The assistant's statement ([CLAIM-tmpcg4uu](CLAIM-tmpcg4uu.md)).** They meet at fold edges,
  where the sloppy eigenvalue is the squared distance to a stratum. This
  includes the textbook sloppy model, the sum of exponentials, at equal
  rates. They also meet at finite sample size, where an unresolved sloppy
  direction and a singular one both hold the learning coefficient below
  d/2. They part in how the coefficient moves as data grow. [ARG-tmpj0r42](../arguments.d/ARG-tmpj0r42.md)
  weighs how far this supports the bet.
- **Not yet shown.** Any connection between the hyperribbon's geometric
  widths, as distinct from its local Fisher eigenvalues, and the
  stratification. The record holds no reading of the widths. (2026-11-21: it now does,
  [THEORY-tmpgsgka](../theory.d/THEORY-tmpgsgka.md), which explains the widths by interpolation and not by
  strata; see the note below.)

## What it does not say

It does not say that sloppiness is singularity, nor that the
stratification explains the hyperribbon's geometric hierarchy. The
owner's word is "connects".

## Note of 2026-11-21: Transtrum, Machta & Sethna (2010, 2011), read

A dated note on the owner's claim; its text and status are not changed
beyond the bracketed update above. Read in [NOTE-tmpamhd2](../notes.d/NOTE-tmpamhd2.md) and
[NOTE-tmpzxtnv](../notes.d/NOTE-tmpzxtnv.md); the THEORYs replace the unread LITs in its grounds.

- **Supports the connection at the edges, now from the originators.**
  "Model boundaries correspond to points on the manifold where the metric
  is singular" (2011, p. 10), including the finite "fold line" at equal
  rates, the edge of [CASE-tmpb2gly](../cases.d/CASE-tmpb2gly.md). Every edge of a hyper-ribbon is a locus
  of rank loss of the metric whose spectrum makes the model sloppy.
- **Leaves the widths unconnected.** The papers derive the geometric fall
  of the widths from the interpolation error of analytic functions, a
  property of sampling, with no strata in it; and the widths match √λ only
  in natural units from a central point.
- **Qualifies "stratification".** Most boundaries lie at infinite parameter
  values ("Since most boundaries occur at infinite parameter values",
  2010, p. 3; in log parameters all of them), where Watanabe's strata, at
  finite points, would need a compactification ([CLAIM-tmpnu4ar](CLAIM-tmpnu4ar.md)'s gap).
  [ARG-tmp97cwb](../arguments.d/ARG-tmp97cwb.md) weighs this: support at the edges, none yet for the
  widths.
