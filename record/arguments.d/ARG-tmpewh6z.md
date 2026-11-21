---
status: Rejected
title: "Transtrum, Machta and Sethna's equation of the metric singularities of network training with manifold boundaries, citing Amari, Park and Ozeki, carries to neural networks the owner's connection between Watanabe's stratification and the hyperribbon at the manifold's edges"
version: 1
form: evidence
grounds:
- THEORY-2155
- THEORY-tmpbobud
concludes:
- CLAIM-808
uses:
- TERM-135
- TERM-140
tags:
- information-geometry
- learning-theory
date: '2026-11-21'
line:
- learned-structure
- formal-apparatus
summary: >-
  The 2011 paper writes that "in the context of training neural networks,
  ... metric singularities (i.e. model boundaries) can have a strong
  influence on the fitting", citing Amari, Park and Ozeki 2006. Read
  ([NOTE-tmptlwkf](../notes.d/NOTE-tmptlwkf.md)), that source places network singularities at finite
  parameter values inside parameter space (a unit off, two units equal),
  which collapse in the space of distributions to a cone apex or a point
  joining two components; it never uses the word "boundary". So the
  picture of a regular interior with singular edges, which [ARG-131](ARG-131.md) finds
  in the sloppy-model literature's own models, does not carry to networks
  on this citation. Rejected as a route to the owner's bet for networks.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
  Standing of the conclusion apart from this route: held as the owner's
  [CLAIM-808](../claims.d/CLAIM-808.md) (Proposed), supported at the edges of the Transtrum group's
  models by [ARG-131](ARG-131.md); in networks the singular sets are interior strata,
  where the connection, if any, is not at an edge ([ADR-136](../decisions.d/ADR-136.md)).
---
<!-- inactive-ok-file: CLAIM-808 ARG-131 THEORY-2155 THEORY-tmpbobud — Proposed; filed 2026-11-21 from the exchange "Rich Get Richer Power Laws" or from the readings of its works -->

# ARG-tmpewh6z: Transtrum, Machta and Sethna's equation of the metric singularities of network training with manifold boundaries, citing Amari, Park and Ozeki, carries to neural networks the owner's connection between Watanabe's stratification and the hyperribbon at the manifold's edges

## The inference

[ARG-131](ARG-131.md) supports [CLAIM-808](../claims.d/CLAIM-808.md) at the edges: in the sloppy-model literature's
models the metric is singular at the manifold's boundaries, so the
hyperribbon has a regular interior and singular edges. The 2011 paper
([THEORY-2155](../theory.d/THEORY-2155.md), [NOTE-2247](../notes.d/NOTE-2247.md)) extends the identification to networks: "It has
been observed in the context of training neural networks, that metric
singularities (i.e. model boundaries) can have a strong influence on the
fitting [42]", [42] being Amari, Park and Ozeki 2006. If that holds, the
edge connection reaches networks.

## Critical questions

- **Does the cited source say it?** No. [THEORY-tmpbobud](../theory.d/THEORY-tmpbobud.md): the Fisher matrix
  degenerates on "the critical set C : vw = 0", and for k units on
  wᵢ = ±wⱼ, sets that are "not isolated but form a continuum" of finite
  parameter values. In the space of distributions the critical set is "a
  single point" joining "two components", or "the apex" of a cone. The
  word "boundary" does not occur.
- **Is a cone apex a boundary in the 2011 sense?** Only definitionally. The
  2011 paper calls any point where the metric is singular a boundary; in
  the ordinary sense, an edge where the manifold ends, the source's
  pictures show none, except that one half of the cone model ends at its
  apex. Under the definitional reading the claim is true by stipulation
  and carries nothing; under the ordinary one it is false for networks.
- **Does it matter to the bet?** Yes. In networks the degenerate sets are
  interior strata at finite parameters, the kind Watanabe treats, and the
  generic point near them is not a sloppy regular interior with a spread
  spectrum but a neighbourhood of rank loss. So the meeting place of the
  two accounts in networks, if any, is not "at the manifold's edges".

## Verdict

Rejected as a route from the sloppy-model geometry to networks. It leaves
[ARG-131](ARG-131.md) untouched for the models it is about.
