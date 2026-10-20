---
number: 759
status: Proposed
formerly:
- THEORY-tmpon8ox
promote_when: >-
  Per-frequency fitting times, with their spread over runs, from a rerun
  of Rahaman et al.'s Experiment 1 with rising amplitudes (6 × 256 ReLU,
  full-batch Adam, sinusoids at 5–50 cycles on 200 points of [0, 1]).
  The rerun must show the order by frequency in each run, not only in the
  ten-run average the paper plots. A theorem for the kernel regime does
  not settle it, because THEORY-086 already covers that regime and this
  entry concerns a network trained with Adam outside it. Experiments in
  other settings bear on a wider claim, not on this one.
title: 'A six-layer, 256-unit ReLU network trained by full-batch Adam to regress a sum of sinusoids at 5 to 50 cycles on [0, 1] fits the components in order of frequency, and keeps that order when the amplitudes rise tenfold with frequency, so in this setting the order of acquisition is set by the learner and not by the strength of the target''s components'
version: 1
tags:
- learning-theory
- representation-learning
date: '2026-10-20'
source:
- LIT-1261
answers:
- QUESTION-217
summary: >-
  Rahaman et al. (2019), [LIT-1261](../literature.d/LIT-1261.md), Experiment 1, read in full in
  [NOTE-983](../notes.d/NOTE-983.md). With equal amplitudes, and with amplitudes rising from 0.1
  at 5 cycles to 1 at 50, the normalised fit |f̃(k_i)|/A_i reaches 1 at low
  frequency first. This is the reverse of the order by strength that
  [THEORY-186](THEORY-186.md) gives for a deep linear network. One architecture, one optimiser,
  a 1-D input, ten runs averaged. The paper's theory gives a bound on
  speed, not this order.
---
<!-- inactive-ok-file: THEORY-186 THEORY-481 — Proposed; accounts this is contrasted with, nothing here rests on their being settled -->

# THEORY-759: A six-layer, 256-unit ReLU network trained by full-batch Adam to regress a sum of sinusoids at 5 to 50 cycles on [0, 1] fits the components in order of frequency, and keeps that order when the amplitudes rise tenfold with frequency, so in this setting the order of acquisition is set by the learner and not by the strength of the target's components

## Source

Rahaman et al. (2019), "On the Spectral Bias of Neural Networks", ICML,
[LIT-1261](../literature.d/LIT-1261.md), §3.1 Experiment 1, Figs. 1, 2 and 10, and Appendix A.1, read
in full in [NOTE-983](../notes.d/NOTE-983.md). The figures were read from renders at low
resolution, so the heatmaps were read qualitatively.

## What was actually shown

The target is λ(z) = Σ_i A_i sin(2πk_i z + φ_i), with k_i = 5, 10, …, 50 and
φ_i drawn uniformly. It is sampled on 200 equally spaced points of
[0, 1]. A 6-layer, 256-unit ReLU network is trained for 80 000 full-batch
Adam steps. Every 100 steps the single-sided DFT of the network on the
grid is taken at each k_i. The plot shows |f̃(k_i)|/A_i, averaged over 10
runs that differ in the phases. In setting (a), A_i = 1. In setting (b),
A_i = 0.1, 0.2, …, 1, so the 50-cycle component is ten times the
5-cycle one. In both, the normalised fit fills in from low frequency to
high (Fig. 1). In the paper's words, "lower frequencies (i.e. smaller
k_i's) are regressed first, regardless of their amplitudes". The spectral
norm of every layer rises throughout training.

What could have come out otherwise: in (b), an order by strength, as in
a deep linear network ([THEORY-186](THEORY-186.md)), would fit the 50-cycle component
first. It came last.

## What this does not say

- **Not a theorem.** The paper's account is Eq. 9: the speed at frequency
  k is at most O(k^(−Δ)) at each instant. Its constant grows as the weights
  do. It bounds high frequencies from above and gives no lower bound for
  low ones, so it does not imply the order. The proved part of the paper
  is a bound on the Fourier content of piecewise-linear functions
  ([THEORY-761](THEORY-761.md)), which is not about training.
- **Not for any amplitude ratio.** A tenfold ratio did not reverse the
  order. Whether a larger one would is untested.
- **Not beyond this setting.** It covers one architecture, Adam rather
  than gradient descent, a 1-D input on a grid, and frequencies up to half
  the Nyquist limit. The paper's MNIST experiments use proxy frequencies
  and do not vary amplitude against frequency.
- **Not "one at a time".** The heatmap shows overlapping fills, not
  stages. Nothing here says the components are learned in separate
  transitions, as in [THEORY-186](THEORY-186.md).
- **Not a refinement order.** Fourier bands are not nested
  representations: no band is a function of another. This is an order of
  acquisition only.
- **Not a property of the target alone.** The paper's §4 shows that the
  same latent signal is fitted more easily on a curve the input space
  crosses faster. "Frequency" here is frequency in the network's input
  coordinates.

## Connections

- **[QUESTION-217](../questions.d/QUESTION-217.md): answers in part.** In A2's terms this is an
  acquisition order with no structural partner. Set beside [THEORY-186](THEORY-186.md), it
  shows that what orders acquisition need not be the target's strength.
  In a deep linear network with white inputs the learner has no
  preference, and the data's singular values decide. Here the learner's
  frequency preference overrode a tenfold difference in strength. So
  Conjecture A's "effective eigenvalues" must be the learner's and the
  data's together, and the record has no formula for that product outside
  the kernel regime.
- **[THEORY-086](THEORY-086.md).** In the kernel regime the order is by NTK eigenvalue,
  independent of the target's amplitudes. That is the same pattern,
  proved, in a regime this experiment is not known to be in.
- **[THEORY-481](THEORY-481.md).** In linear attention the order is by input variance,
  another case where it is set by the data. This entry is the contrasting
  case.
