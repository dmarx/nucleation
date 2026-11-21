---
status: Proposed
title: "Transtrum and Qiu's reduction of sloppy models by evaluating the limits at their manifold's boundaries, as evidence, supports the reduction half of the proposed duality between model reduction and feature differentiation, and leaves its learning half and the single stratified space it needs unshown"
version: 1
form: evidence
grounds:
- THEORY-tmpt1tw7
concludes:
- CLAIM-833
uses:
- TERM-135
tags:
- information-geometry
- model-comparison
date: '2026-11-21'
line:
- learned-structure
summary: >-
  CLAIM-833 grounded LIT-2979 unread. Read (NOTE-tmphbnqd), the manifold
  boundary approximation moves from a sloppy interior to a boundary where
  the smallest Fisher eigenvalue "approaches zero" and evaluates the limit
  there, and its boundaries nest into edges and hypercorners: the
  reduction half as the claim states it. The paper says nothing of
  learning, networks or moves away from singular configurations, and does
  not call the boundary hierarchy a stratification. The reading replaces
  the LIT in the claim's grounds. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-833 THEORY-tmpt1tw7 — Proposed; filed 2026-11-21 from the exchange "Rich Get Richer Power Laws" or from this reading -->
<!-- inactive-ok-file: LIT-tmptm9ww — Deferred, registered 2026-11-21, unread -->

# ARG-tmpmou4i: Transtrum and Qiu's reduction of sloppy models by evaluating the limits at their manifold's boundaries, as evidence, supports the reduction half of the proposed duality between model reduction and feature differentiation, and leaves its learning half and the single stratified space it needs unshown

## The inference

CLAIM-833, A's supposition: reduction moves toward the manifold's
boundaries, differentiation away from singular strata, through one
stratified space. THEORY-tmpt1tw7: "Approximating the manifold by its
boundary" (Fig. 2); along the path "the smallest eigenvalue separates from
the others and approaches zero" (para. 11); the reduced model "is
represented by a hypercorner of the original manifold"; the method needs
"a hierarchy of boundaries", faces within faces.

## Critical questions

- **Does the evidence bear on the claim as stated?** On the reduction half,
  directly: reduction is a move to rank loss of the metric at a boundary,
  and the boundaries are nested. On the learning half, not at all: the
  nearest thing is the Ising section's move from a two-parameter
  Hamiltonian to a more flexible one, which is modelling, not training.
- **Is the boundary hierarchy the stratification the claim needs?** Not
  shown. Most of the paper's boundaries are at infinite parameter values
  (all of them for the Ising chain, two of three kinds for exponentials),
  finite points only in the closure of the manifold in prediction space;
  only the merging of two terms lies at finite parameters. Whether every
  boundary is a stratum in Watanabe's sense is the compactification gap
  the claim already names, and the paper does not close it. The authors'
  own account of the hierarchy as a topology (LIT-tmptm9ww) is registered
  and unread.
- **Would the evidence be expected otherwise?** That a bounded image has
  edges where its Jacobian loses rank is geometry. What is specific is that
  the edges are usable simpler models, which the EGFR and Ising examples
  show.

## Verdict

Supports the reduction half; leaves the learning half open and the shared
stratified space unshown. The claim stays supposed. Proposed.
