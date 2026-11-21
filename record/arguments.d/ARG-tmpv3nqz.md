---
status: Rejected
title: "The hyper-ribbon's originators' applications to a small tanh network and to an autoencoder's code show that parameter and behavioural complexity come apart in overparameterized neural networks"
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Retitled to name its route before its conclusion, with a sentence on
    the conclusion's own standing, under ADR-tmp44npm at the owner's
    objection of 2026-11-21. The verdict is unchanged.
form: evidence
grounds:
- THEORY-tmpgsgka
- THEORY-tmpd7a4j
concludes:
- CLAIM-tmp7ijze
uses:
- TERM-tmp5z2du
tags:
- information-geometry
- learning-theory
date: '2026-11-21'
line:
- learned-structure
- formal-apparatus
summary: >-
  The readings of [LIT-tmpzkxka](../literature.d/LIT-tmpzkxka.md) and [LIT-tmpm1tji](../literature.d/LIT-tmpm1tji.md) show that the originators
  did apply the hyper-ribbon to neural networks, which the record's
  [ARG-tmpmvc5e](ARG-tmpmvc5e.md) (Rejected) did not know: a 4-4-2 tanh network's geodesic
  widths track its singular values (2011, Fig. 6b), and an autoencoder's
  code shows "a clear hyperribbon structure" (2015, unpublished). Neither
  carries [CLAIM-tmpficzj](../claims.d/CLAIM-tmpficzj.md) to overparameterized networks: the network is
  small and regular at the point measured, the autoencoder's parameters
  are its outputs, not its weights, and the 2011 paper's own count makes
  finite singular points generic exactly when data are fewer than twice
  the parameters. Rejected as an inference to the claim for
  overparameterized networks. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
  Standing of the conclusion apart from this route: held as the owner's
  CLAIM-tmp7ijze (Proposed); this argument rejects only the step from
  two small, regular cases to overparameterized networks (ADR-tmp44npm).
---
<!-- inactive-ok-file: ADR-tmp44npm CLAIM-tmp7ijze — Proposed; filed 2026-11-21 -->
<!-- inactive-ok-file: ARG-tmpmvc5e CLAIM-tmpficzj THEORY-tmpd7a4j THEORY-tmpgsgka — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# ARG-tmpv3nqz: The hyper-ribbon's originators' applications to a small tanh network and to an autoencoder's code show that parameter and behavioural complexity come apart in overparameterized neural networks

## The inference

[CLAIM-tmpficzj](../claims.d/CLAIM-tmpficzj.md), for regular models: parameter and behavioural complexity
come apart when predictions depend on few stiff combinations. Its "What it
does not say" declines to carry this to neural networks, and
[ARG-tmpmvc5e](ARG-tmpmvc5e.md) rejects A19 §10's analogy. The readings add the originators'
own network cases:

- 2011 ([THEORY-tmpgsgka](../theory.d/THEORY-tmpgsgka.md), §III, Fig. 6b): "a small network consisting of a
  layer of four input neurons, a layer of four hidden neurons, and an
  output layer of two neurons", tanh, connection weights as parameters,
  chosen because it "is not known to reduce to a linear model in any
  limit"; its geodesic widths "nicely track the singular values".
- 2015 ([THEORY-tmpd7a4j](../theory.d/THEORY-tmpd7a4j.md), §VII): an autoencoder viewed as "a fitting problem,
  with parameters θ_α giving the outputs of the digital neurons"; Hayden et
  al., unpublished, find "a clear hyperribbon structure".

## Critical questions

- **Would the evidence be expected if the conclusion were false?** Yes. A
  small network evaluated at a generic point, with more data than twice its
  weights, is a regular model, and regular nonlinear models with many
  parameters are what the sloppy picture already covers. Finding a
  hyper-ribbon there says nothing about the overparameterized regime.
- **Does it tell the conclusion apart from its rival?** The rival is
  [ARG-tmpmvc5e](ARG-tmpmvc5e.md)'s: an overparameterized network is singular, and its
  effective count is a learning coefficient, not a spread of nonzero
  eigenvalues. The 2011 paper's counting (Eq. 16) supports the rival: "if
  M < 2N there will exist nontrivial singular points of the metric at
  non-extreme values of the parameters", and an overparameterized network
  has M < 2N. The paper also equates network metric singularities with
  boundaries, citing Amari, Park and Ozeki.
- **Does the measure measure what it is said to?** The autoencoder case
  measures the manifold of the code, the network's outputs, as parameters
  of an image model; it is not the Fisher geometry of the weights that
  [CLAIM-tmpficzj](../claims.d/CLAIM-tmpficzj.md)'s network paragraph concerns. The 4-4-2 case measures the
  right object at a scale where the question does not arise.

## Verdict

The originators applied the hyper-ribbon to networks, and the record
should say so (dated notes on [CLAIM-tmpficzj](../claims.d/CLAIM-tmpficzj.md) and [ARG-tmpmvc5e](ARG-tmpmvc5e.md)). The
applications do not carry the claim to overparameterized networks; the
one quantitative statement about that regime, the M < 2N count, sides with
[ARG-tmpmvc5e](ARG-tmpmvc5e.md)'s reason for rejecting the analogy. Rejected.
