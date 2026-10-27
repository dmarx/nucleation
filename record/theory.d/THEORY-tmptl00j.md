---
status: Proposed
promote_when: >-
  A comparison of the beam and Gibbs samplers for the infinite HMM per
  unit of computation, not per iteration, reported as numbers (effective
  sample sizes or autocorrelation times per second for the number of
  states and for the trajectory), over several data sets with persistent
  states and over several hyperprior settings, by a party other than the
  authors or by re-running their released software. It is refuted if,
  per second, a single-site or blocked Gibbs sampler matches the beam
  sampler on persistent sequences. More charts in iterations, or visual
  co-segmentation matrices, cannot settle it: that is the evidence it
  rests on now.
title: 'For the infinite hidden Markov model the beam sampler reaches the posterior in fewer iterations than the single-site Gibbs sampler, and is less sensitive to initialization and hyperpriors, particularly when hidden states persist and emissions are uninformative, at a cost per iteration close to the Gibbs sampler''s'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-tmp2597d. It is the paper's empirical claim,
    §5 of Van Gael, Saatci, Teh and Ghahramani (2008). Its evidence is
    charts (Figures 3, 4 and 7), a visual comparison of co-segmentation
    matrices (Figure 6), and one fixed hyperparameter setting chosen from
    the samplers' own results; no number was taken from the charts.
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-27'
source:
- LIT-tmp0oa8w
summary: >-
  Van Gael, Saatci, Teh and Ghahramani (2008), [LIT-tmp0oa8w](../literature.d/LIT-tmp0oa8w.md), read in
  [NOTE-tmp2597d](../notes.d/NOTE-tmp2597d.md). Two synthetic designs (an almost cyclic 4-state HMM,
  length 800, 20 runs; persistent 4-state HMMs with self-transitions to
  0.999, length 4000, 60 starts), a well-log series and a text task. The
  beam sampler is exact by construction ([THEORY-tmp7bmmi](THEORY-tmp7bmmi.md)); how much faster
  it mixes is shown only in iterations and by eye.
---

# THEORY-tmptl00j: For the infinite hidden Markov model the beam sampler reaches the posterior in fewer iterations than the single-site Gibbs sampler, and is less sensitive to initialization and hyperpriors, particularly when hidden states persist and emissions are uninformative, at a cost per iteration close to the Gibbs sampler's

## Source

Van Gael, Saatci, Teh and Ghahramani (2008), [LIT-tmp0oa8w](../literature.d/LIT-tmp0oa8w.md), read in full in
[NOTE-tmp2597d](../notes.d/NOTE-tmp2597d.md): §5.1 (two synthetic designs), §5.2 (well-log data) and
§5.3 (Alice in Wonderland).

## What was actually shown

- On the almost cyclic synthetic sequence, the beam sampler "discovers
  the underlying structure much faster" in Hamming error after greedy
  matching, averaged over 20 runs, and its curve does not move with the
  hyperprior, while Gibbs gets worse as the prior is strengthened
  (Figure 3).
- With uninformative emissions, as self-transition rises from 0.75 to
  0.999, "the beam sampler mixes increasingly well, the Gibbs sampler
  suffers from slow random walk behavior" (Figure 4, 60 starts).
- On 4050 well-log measurements with a Cauchy likelihood, after 10,000
  iterations Gibbs "hasn't discovered any structure while the beam
  sampler has" (Figure 6, by eye).
- After about 20 iterations the beam sampler sums over "a little more than
  one state" per step on the first synthetic set (Figure 3, bottom).
- On text, both converge to the same performance; the paper says that
  experiment does not compare the samplers.

## What would settle it

Numbers per unit of computation on persistent sequences, as stated in
promote_when. The paper reports neither timings nor effective sample
sizes.

## Connections

- **[THEORY-tmp7bmmi](THEORY-tmp7bmmi.md).** The exactness of the sampler is settled; this is
  the separate claim about speed.
- **[LIT-1577](../literature.d/LIT-1577.md).** The infinite factorial HMM's experiments rely on a sampler
  of this kind and report two single runs ([NOTE-1199](../notes.d/NOTE-1199.md)); they add no
  evidence on mixing.
