---
status: Active
status_note: >-
  read in part 2026-11-03 ([NOTE-tmp6wm7j](../notes.d/NOTE-tmp6wm7j.md), Skimmed: §§1, 2.1–2.2, 4.1
  and 5), from the published text on a Peking University course page;
  worth reading as the standard computation of most likely transition
  paths in small-noise systems, which confirms [QUESTION-071](../questions.d/QUESTION-071.md)'s note of
  2026-11-02 for gradient drift with identity noise and shows, in the
  Maier–Stein model, that the noise path stays the reversed relaxation
  path until the drift is far from gradient.
title: 'The geometric minimum action method: A least action principle on the space of curves'
version: 2
history:
- version: 1
  date: '2026-11-02'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-11-02 (no
    email address sent, ADR-008): dated 2008-01-29. The summary says why it
    is here, not what it shows.
- version: 2
  date: '2026-11-03'
  note: >-
    Read in part from the published CPAM text posted at
    math.pku.edu.cn/teachers/litj/notes/stoch_topics2017/lect06/gMAM.pdf
    (served over http; the https address failed TLS), 66 pp.: §§1,
    2.1–2.2, the start of 4.1, and 5; the proofs, the algorithm
    sections and the other examples not read (NOTE-tmp6wm7j,
    Skimmed). Status set from the reading: Active. A `url:` to the
    copy is added. The summary is replaced by one from the text. The
    registration's account held. One THEORY is filed from it
    (THEORY-tmp544fr).
tags:
- mathematics
- complex-systems
- anthology-candidate
date: '2026-11-02'
published: '2008-01-29'
doi: '10.1002/cpa.20238'
url: 'http://www.math.pku.edu.cn/teachers/litj/notes/stoch_topics2017/lect06/gMAM.pdf'
first_author: 'Heymann'
keywords:
- 'minimum action method'
- 'large deviations'
- 'Freidlin–Wentzell'
implementations: []
summary: >-
  Heymann and Vanden-Eijnden (2008), CPAM 61: 1052–1117. The
  Freidlin–Wentzell quasi-potential, a minimization over paths and
  their durations that has no minimizer between equilibria, is
  rewritten as a minimization of a parametrization-free action over
  curves, which has one; for a diffusion it is 2 inf ∫ |b| sin²(θ/2)
  ds. The minimizer is the maximum-likelihood transition curve in the
  small-noise limit. The geometric minimum action method computes it
  for nongradient SDEs, SPDEs and Markov jump processes. With gradient
  drift and identity noise transition paths run parallel to the drift;
  in the Maier–Stein model they leave the heteroclinic orbit for β >
  4.
---
<!-- inactive-ok-file: NOTE-tmp6wm7j — Proposed, Open, Deferred, Unfetched, Unavailable or new; cited as open -->

# LIT-tmpk8i57: The geometric minimum action method: A least action principle on the space of curves

Heymann, M., Vanden-Eijnden, E. (2008). The geometric minimum action method: A least action principle on the space of curves. *Communications on Pure and Applied Mathematics, 61(8), 1052-1117*. doi:10.1002/cpa.20238.

Read in part on 2026-11-03 ([NOTE-tmp6wm7j](../notes.d/NOTE-tmp6wm7j.md), Skimmed; [THEORY-tmp544fr](../theory.d/THEORY-tmp544fr.md)).

## Key takeaways

- V(x₁, x₂) = 2 inf ∫ |b|_a sin²(θ/2) ds over curves (eq. 1.18).
- Gradient drift, identity noise: the escape path is the reversed
  relaxation path (p. 1058).
- Maier–Stein: gradient only at β = 1, yet the path is the heteroclinic
  orbit up to β = 4 (§4.1).

## Standing in the record

Computes the most likely transition paths of a noisy system. Bears on the note of 2026-11-02 on [QUESTION-071](../questions.d/QUESTION-071.md), that a transition's path, not its end state, can tell a noise-driven escape from a directed one.
