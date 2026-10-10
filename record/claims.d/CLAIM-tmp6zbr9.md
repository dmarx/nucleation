---
status: Active
title: 'The compositional predictions are upper bounds whose constants cannot be estimated from serial-reproduction data in a metric fixed beforehand, so the compositional half of the success criterion cannot fail'
version: 2
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Conceded on 2026-10-10 for CLAIM-078 and CLAIM-059, restated with
    kernels estimated from independent retellers, a metric fixed in
    advance and a prediction interval tested on chains not used in the
    estimation. CLAIM-056's condition asks for prediction, which a
    loose bound fails, so it can fail as stated and is unchanged.
role: counter
tags:
- probabilistic-modeling
- philosophy-of-science
date: '2026-10-10'
line: pragmatic-transport
grounds:
- CASE-009
objects_to:
- CLAIM-078
- CLAIM-056
- CLAIM-059
summary: >-
  Found in the record's audit of the line on 2026-10-10 (empirical lens);
  no turn of the exchange raises it. The recursion e_n ≤ (∏κ_j)e_0 +
  Σε_i∏κ_j is a theorem once its constants are the true ones, so a chain
  cannot depart from it; it can only show a constant was misestimated. A
  sensitivity κ_i belongs to a reteller's kernel and needs many retellings
  of each of several inputs at every generation, where a chain gives one.
  And [CLAIM-059](CLAIM-059.md) says amplification "needs a metric other than total
  variation", so the regime depends on a metric chosen afterwards.
  [CLAIM-078](CLAIM-078.md) records that the compositional half was dropped from the
  manuscript, not that it cannot fail as stated. It does not say error
  propagation is unimportant.
---
<!-- inactive-ok-file: CLAIM-078 CLAIM-056 CLAIM-059 — Proposed; open, and cited as the claims this objection is to -->

# CLAIM-tmp6zbr9: The compositional predictions are upper bounds whose constants cannot be estimated from serial-reproduction data in a metric fixed beforehand, so the compositional half of the success criterion cannot fail

## The objection

[CLAIM-078](CLAIM-078.md) makes half of the theory's success that the measures "follow its
compositional predictions across reconstructions". It is defeated if "their
behaviour along reconstruction chains departs from the composition bounds".
[CLAIM-056](CLAIM-056.md) is defeated if "end-to-end drift is not predicted by per-step
discrepancies combined with the measured sensitivity of later steps", and
[CLAIM-059](CLAIM-059.md) if "Measured per-generation sensitivity of real reconstruction
chains shows no difference between conditions that the theory assigns to
different regimes".

**A bound, not a prediction.** The recursion is [CLAIM-056](CLAIM-056.md)'s. Let u_i be the
chain's state after step i and r_i the reference transport's, with
e_i = d(u_i, r_i). Let the chain's step be K̃_i and the reference's K_i, with
local discrepancy ε_i = d(K̃_i u_i, K_i u_i) and κ_i a Lipschitz constant of
K_i. By the triangle inequality,

e_(i+1) = d(K̃_i u_i, K_i r_i) ≤ d(K̃_i u_i, K_i u_i) + d(K_i u_i, K_i r_i)
≤ ε_i + κ_i e_i,

and unrolling from e_0 gives e_n ≤ (∏_(j<n) κ_j) e_0 + Σ_(i<n) ε_i ∏_(i<j<n) κ_j.
If the κ_i are true Lipschitz constants and the ε_i the true discrepancies,
this holds for every chain: it is a theorem, and no data can contradict it. A
measured e_n above the bound shows only that some κ_i or ε_i was estimated too
low. A measured e_n below it is consistent with it however far below. So
"departs from the composition bounds" has no outcome that counts against the
theory. Read as [CLAIM-056](CLAIM-056.md)'s "predicted", the recursion gives no point
prediction to compare with.

**The constants need kernels.** κ_i is a property of the reteller's kernel,
the distribution of retellings it produces for each input. To estimate it
needs the kernel at several inputs, with many retellings of each, at every
generation. Two errors then enter. A maximum over the input pairs sampled
can only fall short of the supremum, which biases the bound low. And each
distance between output distributions is itself estimated from finite
retellings, which adds a bias of its own (upward for a plug-in total
variation). Either can produce or hide a "violation". A serial
reproduction chain gives one retelling of one input at each node. The chain
designs ([CASE-009](../cases.d/CASE-009.md); manuscript §8; Case II's "heterogeneous-agent chains", as
[CLAIM-085](CLAIM-085.md) reports them) do not provide several independent retellings of one
input per generation.

**The metric.** No design fixes the metric d in which κ_i is computed.
[CLAIM-059](CLAIM-059.md) itself says amplification "needs a metric other than total
variation": for a Markov kernel acting on distributions, the contraction
coefficient in total variation is at most one, so in that metric no chain is
amplifying. A chain counted as amplifying is so only in some other metric,
chosen afterwards. Which regime a chain is in therefore depends on a choice
the theory does not make, and [CLAIM-059](CLAIM-059.md)'s defeat condition, about conditions
"the theory assigns to different regimes", has no assignment to test until
that choice is made.

[QUESTION-017](../questions.d/QUESTION-017.md) asks what bound holds when the distortion is directed and the
triangle inequality fails. That is a question about the theorem. This
objection is about measuring its constants.

## What it does not say

- It does not say error propagation along chains is unimportant, or that the
  three regimes are not real.
- It does not say the recursion is wrong. It is correct, and for that reason
  cannot be tested as stated.

## What would answer it

- A design that estimates each step's kernel from several independent
  retellers on held-out inputs and perturbed inputs at each generation.
- A metric fixed before the data, with the reason it is the right one.
- A prediction stated as a point estimate of end-to-end drift with an
  interval, computed from kernels estimated on one set of chains and tested
  on another, so that it can fail.
