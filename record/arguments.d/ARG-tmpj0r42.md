---
status: Proposed
title: 'The merging-mechanisms construction and the finite-sample contrast support the owner''s bet that Watanabe''s stratification connects to the hyperribbon account at the hyperribbon''s fold edges and in the learning coefficient measured at finite sample size, and not yet in the hyperribbon''s geometric widths'
version: 1
form: evidence
rests_on:
- CLAIM-tmpcg4uu
- CLAIM-tmpcgvcp
grounds:
- CASE-tmpb2gly
- THEORY-1253
concludes:
- CLAIM-tmpa8hb2
tags:
- information-geometry
- learning-theory
date: '2026-11-21'
line:
- learned-structure
- formal-apparatus
summary: >-
  How far the assistant's statement of where sloppiness and singular
  strata meet ([CLAIM-tmpcg4uu](../claims.d/CLAIM-tmpcg4uu.md)) and its construction ([CASE-tmpb2gly](../cases.d/CASE-tmpb2gly.md))
  support the owner's U24 in the exchange "Rich Get Richer Power Laws"
  (2026-11-21). In part: the connection holds at fold edges and at finite
  n, and the construction says nothing about the widths that define a
  hyperribbon. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmpcg4uu CLAIM-tmpcgvcp CLAIM-tmpa8hb2 CASE-tmpb2gly LIT-tmpdz70v — Proposed or new, filed with this argument, or Deferred works registered from the exchange and not yet read -->
<!-- inactive-ok-file: ARG-tmp97cwb THEORY-tmpgsgka THEORY-tmpkoje5 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# ARG-tmpj0r42: The merging-mechanisms construction and the finite-sample contrast support the owner's bet that Watanabe's stratification connects to the hyperribbon account at the hyperribbon's fold edges and in the learning coefficient measured at finite sample size, and not yet in the hyperribbon's geometric widths

## The inference

[CLAIM-tmpa8hb2](../claims.d/CLAIM-tmpa8hb2.md), the owner's, bets that the two accounts "connect nicely".
Two results bear on it.

- **At the edges.** In the textbook sloppy model, a sum of exponentials,
  equal rates are a fold edge of the image. There the smaller Fisher
  eigenvalue is proportional to the squared distance from the stratum and
  vanishes on it, and the learning coefficient at a true point on the edge
  is 3/4 against 1 ([CASE-tmpb2gly](../cases.d/CASE-tmpb2gly.md), [CLAIM-tmpcg4uu](../claims.d/CLAIM-tmpcg4uu.md)). A thin direction of
  the hyperribbon thus ends on a singular stratum, and its eigenvalue
  measures the distance to it.
- **At finite n.** A sloppy direction the data cannot resolve holds the
  learning coefficient below d/2, as a singular one does ([CLAIM-tmpcg4uu](../claims.d/CLAIM-tmpcg4uu.md);
  [THEORY-1253](../theory.d/THEORY-1253.md)'s freeze-out). The two accounts describe the same shortfall
  in Bayesian complexity at a given n, and come apart only as n grows.

If both hold, the stratification and the hyperribbon are connected: in
places a hyperribbon's thinness is the shadow of a stratum, and a single
learning-coefficient estimate measures both at once.

## Critical questions

- **Would the evidence be expected if the bet were false?** Partly. The
  finite-n coincidence is general: any parameter the data cannot yet
  pin down lowers the capacity, whatever its geometry. On its own it
  shows a shared effect, not a connection between the structures. The
  fold-edge result is specific: a stratum at the end of a sloppy
  direction is not what two unrelated accounts would predict.
- **Does it tell the bet apart from its rivals?** The rival is
  [CLAIM-tmpcgvcp](../claims.d/CLAIM-tmpcgvcp.md) read as "different and unrelated". Its own examples
  (a linear model sloppy and never singular; Y ∼ N(ab, 1) singular with no
  spread) show the properties can occur apart. They do not show they never
  meet, and the edge result shows they do. The rival "sloppiness is
  singularity" is refuted by the same linear model.
- **Does the measure measure what it is said to?** Here is the gap. A
  hyperribbon is defined by the geodesic widths of the model image
  ([LIT-tmpd3swn](../literature.d/LIT-tmpd3swn.md), [LIT-tmpzkxka](../literature.d/LIT-tmpzkxka.md), read on 2026-11-21: [THEORY-tmpkoje5](../theory.d/THEORY-tmpkoje5.md),
  [THEORY-tmpgsgka](../theory.d/THEORY-tmpgsgka.md)), not by Fisher eigenvalues at a
  point. The evidence is stated in eigenvalues. Whether the manifold
  boundaries that Transtrum and Qiu's reduction follows ([LIT-tmpdz70v](../literature.d/LIT-tmpdz70v.md),
  unread) are singular strata in general is open. Many lie at infinite
  parameter values, a rate going to 0 or ∞, where the model loses a
  parameter in the limit rather than folding at a finite point. A39 §6
  concedes: "model reduction does not always correspond to a literal
  singularity in finite parameter coordinates."

## Verdict

Supports the bet in two stated places, and leaves its strongest reading,
that the stratification organizes the hyperribbon's hierarchy of widths,
unsupported until a reading of the widths is filed. Proposed.

## Note of 2026-11-21: Transtrum, Machta & Sethna (2010, 2011), read

Read in [NOTE-tmpamhd2](../notes.d/NOTE-tmpamhd2.md) and [NOTE-tmpzxtnv](../notes.d/NOTE-tmpzxtnv.md). On the "measure" question: the
papers do define the hyper-ribbon by geodesic widths, measured from "some
central point" along the metric's eigendirections, and find them ≈ √λ only
in natural or log units, not in magnitude for PC12; so stating the
evidence in eigenvalues reaches the widths where those conditions hold.
The caveat that many boundaries lie at infinite parameter values is the
papers': "Since most boundaries occur at infinite parameter values" (2010,
p. 3); "Typical boundaries occur when parameters are near their extreme
values (such as ±∞ or zero)" (2011, p. 10). They add a count: finite
singular points are generic when the data number fewer than twice the
parameters, otherwise near-singular at best. A reading of the widths is now
filed, which this argument's verdict waited on; it explains the widths by
interpolation, not strata, so the strongest reading of the bet is still
unsupported. [ARG-tmp97cwb](ARG-tmp97cwb.md) takes this up; this argument's verdict stands.
