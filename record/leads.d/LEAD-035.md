---
number: 35
status: Open
formerly:
- LEAD-tmp3ol4v
title: 'Check the SNR singular values against the predicted quarter-power law for neural collapse'
version: 1
stage: idea
priority: medium
method:
- empirical
tags:
- representation-learning
- learning-theory
date: '2026-11-19'
line:
- learned-structure
advances:
- QUESTION-051
summary: >-
  Named in [NOTE-783](../notes.d/NOTE-783.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CASE-tmpjn6f4 CLAIM-tmpcpr7t LIT-tmpxyq0h — new; the study, the claim and the registration this lead filed on 2026-11-22 -->
<!-- inactive-ok-file: NOTE-772 — Skimmed; cited in the backlog audit of 2026-11-19 -->

# LEAD-035: Check the SNR singular values against the predicted quarter-power law for neural collapse

## What it would do

Measure on trained networks, and register the work [NOTE-772](../notes.d/NOTE-772.md) names.

Where the record names it:

- [NOTE-783](../notes.d/NOTE-783.md): "A measurement of the SNR singular values in a trained
  network, against (4t/N)^(1/4), would settle whether the closed form
  describes training."

## What would count

Agreement says the closed form describes training by ordinary gradient
descent, which bears on [QUESTION-051](../questions.d/QUESTION-051.md); disagreement confines it to the
renormalized flow.

## Note of 2026-11-22: carried out

Done on branch claude/lead-035-snr-singular (scratch/studies/lead-035/,
with tests and per-item results).

- **Measured.** ω_j of Σ_W^(−1/2)M̃ against (4t/N)^(1/4) in three
  unconstrained-features dynamics and two small numpy ReLU networks (one
  with batch normalization), MSE, weight decay 0 and 5×10⁻⁴, three seeds:
  CASE-tmpjn6f4. The renormalized flow matches the law; nothing trained
  without re-whitening does. So, at this scale, "disagreement confines it
  to the renormalized flow", as "What would count" puts it:
  CLAIM-tmpcpr7t.
- **Registered.** "The work NOTE-772 names" is read as Mixon, Parshall
  and Pi (2020), the squared-error gradient-flow analysis of unconstrained
  features without renormalization that the review reports: LIT-tmpxyq0h,
  Deferred, not read. The review names other works; this one was chosen
  because it bears on what the lead measures.
- **Remains.** The same measurement in networks of the kind Han and
  colleagues trained (convolutional, image data, SGD with momentum),
  which needs more compute than this lead had; reading LIT-tmpxyq0h; the
  limiting direction of Corollary 2, not measured; and the cause of the
  late instability in the batch-normalized runs with weight decay.
