---
status: Rejected
title: "The behaviour of sloppy models carries over to overparameterized neural networks, so that a network's behavioural complexity is set by a few stiff combinations of its parameters as in a sloppy model"
version: 1
form: analogy
grounds:
- THEORY-774
- THEORY-777
concludes:
- CLAIM-tmpficzj
tags:
- information-geometry
- learning-theory
date: '2026-11-21'
line:
- learned-structure
- formal-apparatus
summary: >-
  A's analogy at A19 §10 of the exchange "Rich Get Richer Power Laws": "A
  neural network may contain billions of parameters, but only some
  combinations may significantly affect particular outputs or tasks", with
  "the conceptual connection is strong" though "The analogy isn't exact".
  It would carry [CLAIM-tmpficzj](../claims.d/CLAIM-tmpficzj.md), stated for regular sloppy models, to
  networks. It fails in its strong form: sloppiness counts behavioural
  complexity by the spread of a full-rank Fisher spectrum, and an
  overparameterized network is singular, its Fisher matrix degenerate on
  whole sets of parameters, where the effective count is the learning
  coefficient and the spectrum does not give it ([CLAIM-tmpcgvcp](../claims.d/CLAIM-tmpcgvcp.md)). What
  survives is the weak point that few combinations matter, which is not
  sloppiness. Rejected. The argument is A's (the other assistant in the
  exchange "Rich Get Richer Power Laws", A19); the verdict is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpficzj CLAIM-tmpcgvcp CLAIM-tmpcg4uu ARG-tmpj0r42 THEORY-777 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21, or a Proposed reading the record already held -->

# ARG-tmpmvc5e: The behaviour of sloppy models carries over to overparameterized neural networks, so that a network's behavioural complexity is set by a few stiff combinations of its parameters as in a sloppy model

## The inference

A19 builds the sloppy-model picture on two cases the record holds: the
hopping model, whose Fisher eigenvalues separate by a factor of order t
when the density is seen after t steps ([THEORY-774](../theory.d/THEORY-774.md)), and the critical
Ising model under decimation, where two stiff directions survive and the
irrelevant ones fall by up to six decades ([THEORY-777](../theory.d/THEORY-777.md)). From them,
[CLAIM-tmpficzj](../claims.d/CLAIM-tmpficzj.md): parameter and behavioural complexity come apart when
predictions depend on a few stiff combinations. A19 §10 then carries this
to networks: "A neural network may contain billions of parameters, but
only some combinations may significantly affect particular outputs or
tasks. Identifying those combinations is related to sensitivity analysis,
effective dimensionality, and model compression. The analogy isn't
exact—neural networks introduce additional issues of training,
overparameterization, and generalization—but the conceptual connection is
strong."

## Critical questions

- **In what respect are they alike, and is it the respect the conclusion
  needs?** Both have many parameters and outputs sensitive to few
  combinations of them. The conclusion needs more: that the network's
  behavioural complexity is measured as a sloppy model's is, by the
  number of Fisher eigenvalues above the resolution the data give, with
  the rest spread over decades below. That is the respect in which the
  record's two cases are sloppy.
- **What relevant difference is there?** Regularity. A sloppy model, as
  [CLAIM-tmpficzj](../claims.d/CLAIM-tmpficzj.md) states it, has a Fisher matrix of full rank whose
  eigenvalues are small but nonzero. An overparameterized network is
  singular: its Fisher matrix loses rank on whole sets of parameters
  (permutations, dead units, merged units, rescalings), and at such points
  the decisive structure is at higher order than the Fisher matrix sees.
  [CLAIM-tmpcgvcp](../claims.d/CLAIM-tmpcgvcp.md): "at a singular point the Fisher spectrum does not give
  the learning coefficient", and the record's measure of a singular
  model's effective complexity is that coefficient, which falls below half
  the parameter count where the optimal set is degenerate ([THEORY-087](../theory.d/THEORY-087.md),
  [THEORY-1253](../theory.d/THEORY-1253.md)). A model can be singular with no spread of eigenvalues at
  all (Y ∼ N(ab, 1)).
- **What transfers, and what does not?** Transfers: that a network's
  outputs can be sensitive to few combinations of its parameters, and
  that fitting all parameters is not needed to predict well. Does not
  transfer: the account of why, through a hierarchy of nonzero Fisher
  eigenvalues, and the count of behavioural complexity it gives. Where
  sloppiness and singularity do meet, at a fold edge and at finite sample
  size ([CLAIM-tmpcg4uu](../claims.d/CLAIM-tmpcg4uu.md), [ARG-tmpj0r42](ARG-tmpj0r42.md)), the network's sloppy directions end
  on strata, and the stratum, not the spread, decides the count.

## Verdict

The analogy does not carry [CLAIM-tmpficzj](../claims.d/CLAIM-tmpficzj.md) to overparameterized networks
in the strong form A19 §10 calls "strong". Its weak form, that few
combinations matter, holds of networks but is not the sloppy-model claim
and does not need it. Rejected as an inference to [CLAIM-tmpficzj](../claims.d/CLAIM-tmpficzj.md) for
networks; [CLAIM-tmpficzj](../claims.d/CLAIM-tmpficzj.md) itself, for regular models, is untouched.
