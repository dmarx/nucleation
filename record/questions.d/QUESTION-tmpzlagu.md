---
status: Open
title: 'Do the effective dimensions of one system, the number of its stiff Fisher directions at a given resolution, the dimension of its predictive states, the number of its relevant renormalization-group directions and its fractal dimension, agree, and when do they come apart?'
version: 1
tags:
- information-geometry
- information-theory
- complex-systems
- learning-theory
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
summary: >-
  A's open question at the close of A19 and the table at A21 §1 of the
  exchange "Rich Get Richer Power Laws": "Is the effective dimensionality
  of a complex system fundamentally determined by how much information is
  required to predict its behavior?", with "several competing meanings of
  effective dimensionality: geometric dimension, the number of important
  Fisher-information eigenvectors, the number of predictive state
  variables, and the number of relevant RG directions. Understanding when
  these quantities agree—and when they diverge" is the task. The record
  holds pieces of each and no comparison; [QUESTION-217](QUESTION-217.md) asks a sibling
  question about orders, not counts. The wording is A's (the other
  assistant in the exchange "Rich Get Richer Power Laws", A19 and A21);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-777 — Proposed reading, the relevant-direction count -->
<!-- inactive-ok-file: CLAIM-tmpj0k4q CLAIM-tmpyxiwv TERM-tmpxml4k — filed with this question from the same exchange, Proposed or Open -->
<!-- inactive-ok-file: SYNTHESIS-084 THEORY-1558 — Proposed, cited as the open state of the RG–information correspondence and of rate-demarcated levels -->
<!-- inactive-ok-file: THEORY-tmp3gj1j THEORY-tmpgsgka — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# QUESTION-tmpzlagu: Do the effective dimensions of one system, the number of its stiff Fisher directions at a given resolution, the dimension of its predictive states, the number of its relevant renormalization-group directions and its fractal dimension, agree, and when do they come apart?

## Why it is a question

A21 §1 tabulates five quantities that "can legitimately be called its
dimensionality", microstate, parameter, relevant-RG, predictive-state and
fractal, and says "These are not generally equal." The 2D Ising model
shows the spread at once: 2^N configurations, two couplings K and H, two
relevant scalar perturbations, and geometric spin clusters of fractal dimension 187/96
at criticality. "**Simple laws don't imply simple realizations**" (A21
§1).

The record holds a piece of each and no comparison:

- **Stiff Fisher directions**: two stay under decimation of the critical
  Ising model, the field and the T_c gradient ([THEORY-777](../theory.d/THEORY-777.md)); and the count
  resolved grows with the data at a rate set by the spectrum
  ([CLAIM-tmpj0k4q](../claims.d/CLAIM-tmpj0k4q.md)), so it is a function of resolution, not a number.
- **Parameter count in learning**: (d/2) log n in a regular model, the
  learning coefficient in a singular one ([THEORY-087](../theory.d/THEORY-087.md), [THEORY-1253](../theory.d/THEORY-1253.md)).
- **Predictive states**: the causal states and their entropy
  ([TERM-062](../terms.d/TERM-062.md), [THEORY-756](../theory.d/THEORY-756.md)); predictive information as a function of window
  ([TERM-tmpxml4k](../terms.d/TERM-tmpxml4k.md)), whose growth a Fisher spectrum fixes in one model
  ([CLAIM-tmpyxiwv](../claims.d/CLAIM-tmpyxiwv.md)).
- **Relevant directions**: the RG account ([THEORY-777](../theory.d/THEORY-777.md), [THEORY-742](../theory.d/THEORY-742.md)) and the
  question whether information criteria find them ([QUESTION-232](QUESTION-232.md),
  [SYNTHESIS-084](../syntheses.d/SYNTHESIS-084.md)).

[CLAIM-tmpyxiwv](../claims.d/CLAIM-tmpyxiwv.md) joins two of them in a linear-Gaussian model: there the
resolved Fisher count and the growth of predictive information move
together. Whether that survives where the spectrum comes from
coarse-graining rather than from a prior, whether the relevant-direction
count is the T → ∞ limit of the stiff count under coarse observation, and
whether a fractal dimension of the realizations enters any of them, the
record cannot say.

## What would answer it

One system in which all four are computed under one observation scheme,
with the scheme stated ([LEAD-tmpl5wxz](../leads.d/LEAD-tmpl5wxz.md) proposes the 2D Ising model), and
either a pattern of agreement with its conditions or a pair that
provably comes apart. A partial answer: a proof that, under a stated
coarse-graining, the number of Fisher eigenvalues that do not decay with
scale equals the number of relevant directions, which [THEORY-777](../theory.d/THEORY-777.md) shows
numerically for one lattice and one family.

## Related

[QUESTION-217](QUESTION-217.md) asks whether orders of refinement, relevance and acquisition
in learning admit one chain; this asks whether counts agree. A21 §10's
further question, whether multiscale complexity lies in the number of
levels or in how freely information moves between them, is held in part
by [THEORY-581](../theory.d/THEORY-581.md), [THEORY-1558](../theory.d/THEORY-1558.md) and [QUESTION-219](QUESTION-219.md) and is not filed separately.

## Note of 2026-11-21: Bialek, Nemenman & Tishby and Transtrum, Machta & Sethna (2010, 2011), read

More effective dimensions the question does not list, and none resolves
it:

- **Bialek, Nemenman and Tishby** (NOTE-tmpilbkz, THEORY-tmp3gj1j) separate
  the parameter count K, a "phase space dimension" d that replaces K when
  the Fisher matrix is degenerate (Eq. 64), and the VC dimension, below
  which the (d/2) log N law does not hold. Their d is the regular-model
  counterpart of a learning coefficient's 2λ.
- **Transtrum, Machta and Sethna 2011** (NOTE-tmpzxtnv, THEORY-tmpgsgka)
  count the parameters not evaporated at a best fit, growing as
  log(W₀/σ)/|log ∆| for widths W₀∆ⁿ (Eq. 37), and summarize the manifold by
  "three numbers", W₀, ∆ and N.
- **The 2010 letter** speaks of "few effective degrees of freedom" without
  defining the count (NOTE-tmpamhd2).

Relations are written from THEORY-tmp3gj1j and THEORY-tmpgsgka.
