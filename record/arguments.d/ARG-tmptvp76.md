---
status: Proposed
title: 'Stringer and colleagues'' smoothing account of spectral decay, by analogy from a sensory population code to a learned spectrum, suggests that the fine end is damped for generalization and that the measured floor is estimator noise, a rival to the floor and band of the truncated-band account'
version: 1
form: analogy
grounds:
- THEORY-tmpwtoad
concludes:
- CLAIM-tmpufbx6
tags:
- representation-learning
- neuroscience
date: '2026-11-22'
line:
- learned-structure
summary: >-
  Whether Stringer and colleagues' account transfers to the owner's
  truncated-band claim. In V1, successive principal components encode
  finer features, the decay rate trades fine discrimination against
  generalization, and below the resolved range the cross-validated
  eigenvalues fall to zero as noise. By analogy, a learned spectrum's fine
  end is damped by design and its floor is the estimator's. The respect is
  the one the rival needs; the evidence is a neural code and a kernel
  argument, not an unembedding. Weak: it makes the rival testable, not
  preferable. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpwtoad CLAIM-tmpufbx6 CLAIM-tmp2r6ur ARG-tmpabk16 — Proposed or new; the reading, the rival claim, the owner's claim it rivals, the support it meets and the test -->

# ARG-tmptvp76: Stringer and colleagues' smoothing account of spectral decay, by analogy from a sensory population code to a learned spectrum, suggests that the fine end is damped for generalization and that the measured floor is estimator noise, a rival to the floor and band of the truncated-band account

## The inference

THEORY-tmpwtoad: "Successive PC dimensions encode finer stimulus
features"; "the rate of eigenspectrum decay can be seen as a smoothing
parameter"; the resolved range ends at about half the number of stimuli,
below which "the remaining eigenvectors correspond to or are corrupted by
additive noise". By analogy, in a learned spectrum discrimination per unit
grows toward the fine end, the fine end's low variance is the price of
generalization, and the floor below the "band" is where the estimator
stops resolving it: CLAIM-tmpufbx6.

## Critical questions

- **In what respect are they alike?** Both are spectra of a code read out
  by a learner, where low-variance directions carry fine distinctions. The
  kernel argument (SI §2.4) is general to any fixed code with a linear
  readout, which is the respect the rival needs.
- **What relevant difference is there?** The owner's spectrum is the
  unembedding's, a weight matrix, not a population response to stimuli,
  and its discriminating measure is Xu's per-direction effect on
  predictions, not tuning. Xu's Qwen floor comes from normalization
  coordinates with near-zero weight (ARG-tmpabk16), a property of the
  model, which the rival must treat as an exception with its own mechanism.
  Stringer's noise floor is removed by cross-validation; an unembedding is
  measured without trial noise, so its floor, if any, is not this one
  unless the estimator is a sample spectrum.
- **What transfers?** The test: whether the floor moves when the
  measurement improves. Not the V1 numbers.

## Verdict

A weak analogy that makes CLAIM-tmpufbx6 a live alternative to part of
CLAIM-tmp2r6ur; it does not prefer it, and Xu's Qwen evidence tells
against it where it applies. Proposed.
