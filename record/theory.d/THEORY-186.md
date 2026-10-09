---
number: 186
status: Proposed
formerly:
- THEORY-tmpuusea
promote_when: >-
  A proof that from small random, unbalanced initial weights the
  trajectory of a two-layer linear network converges to the decoupled
  solution as the initial scale goes to zero, so that the per-mode
  sigmoids and their strength ordering are a theorem rather than a
  simulated approximation. A reading of the authors' 2014 paper or of a
  later silent-alignment analysis that supplies one would serve. Further
  simulations of small hand-built datasets cannot settle it.
title: 'A deep linear network trained from small weights learns the singular modes of its input–output correlations one at a time in order of strength, each in a sharp sigmoidal transition, while a shallow network learns them all together; the stages come from the product of layers and the data''s spectrum, not from nonlinearity'
version: 1
tags:
- representation-learning
- learning-theory
date: '2026-10-09'
source:
- LIT-862
summary: >-
  Saxe, McClelland and Ganguli (2019), [LIT-862](../literature.d/LIT-862.md), restating their 2014
  solution (not held): exact for decoupled, balanced initial weights and
  white inputs, simulated for random small weights. With hierarchically
  generated data the spectrum falls with depth in the tree, so the schedule
  is coarse to fine. It is not a claim about nonlinear networks, about
  correlated inputs, or about learning that starts from prior knowledge.
---
<!-- inactive-ok-file: THEORY-182 THEORY-183 THEORY-039 — Proposed; accounts this one underlies or is set beside -->

# THEORY-186: A deep linear network trained from small weights learns the singular modes of its input–output correlations one at a time in order of strength, each in a sharp sigmoidal transition, while a shallow network learns them all together; the stages come from the product of layers and the data's spectrum, not from nonlinearity

## Source

Saxe, McClelland and Ganguli (2019), [LIT-862](../literature.d/LIT-862.md), Eqs. 2–11 and the
Supplementary Material's derivations, as read in [NOTE-666](../notes.d/NOTE-666.md). The solution
first appeared in the same authors' 2014 ICLR paper, *Exact solutions to the
nonlinear dynamics of learning in deep linear neural networks* (arXiv
1312.6120). Neither record holds that paper, and the 2019 paper does not
cite it.

## What was actually shown

Take ŷ = W₂W₁x with white inputs (Σx = I), squared error, and gradient
descent slow enough to average over an epoch. In the SVD basis of the
input–output correlation Σyx = Σ s_α u_α v_αᵀ, start the weights diagonal
and balanced between the layers. Then each mode's strength a_α obeys
τ ȧ_α = 2a_α(s_α − a_α). The solution, a_α(t) = s_α e^{2s_αt/τ} /
(e^{2s_αt/τ} − 1 + s_α/a_α⁰), is a sigmoid that reaches s_α at a time of
about (τ/s_α) ln(s_α/ε). The transition takes a vanishing fraction of that
time as the initial scale goes to zero. A single weight matrix trained on
the same data follows b_α(t) = s_α(1 − e^{−t/τ}) + b_α⁰e^{−t/τ}: every mode
on the timescale τ ln(s_α/ε), exponentially, with no stages and with every
individual prediction monotone. The derivation is exact under its
conditions, and the difference between the two architectures is proved.

What could have come out otherwise is the random-initialisation case. From
small random weights the paper simulates the network and finds the
trajectories on the decoupled curves (Fig. 3C). Off-diagonal couplings
could have persisted or reordered the modes; in these simulations they do
not.

The data enter only through the spectrum. For features diffusing down a
tree, the singular values fall with depth, so the schedule is coarse to
fine. For a ring the modes are Fourier modes, learned from low frequency up.
Between the stages of the deep network, single item–feature predictions
can move the wrong way for a time of order the gap between the singular
values.

## What this does not say

- **Not that random initialisation provably follows the solution.** The
  decoupled, balanced start is assumed. The random small-weight case rests
  on simulation of datasets with a handful of items.
- **Not that nonlinear networks learn this way.** The paper's evidence is a
  visual match between two MDS plots (Fig. 2). Depth here buys no
  expressive power; the claim concerns the training trajectory of a linear
  map.
- **Not for correlated inputs or prior knowledge.** With Σx ≠ I the input
  and output bases need not align. The SI says the solution does not
  describe learning that begins with substantial knowledge already in the
  weights.
- **Not that the order is always coarse to fine.** The order is by singular
  value. Fine distinctions come first whenever the data make them stronger;
  anticorrelated siblings at an intermediate level are the paper's own
  example (Fig. 8).
- **Not that stages are discontinuities.** Each transition is smooth. It is
  sharp only relative to the plateau before it, and only for small initial
  weights.
- **Not an explanation of children's development.** The paper offers it as
  a qualitative account and fits no developmental data.
- **Not an instruction.** It says what such a network learns and when, not
  how to train one.

## Where it sits

[THEORY-182](THEORY-182.md) is this dynamics applied to a symmetric factorisation, in a
quadratic proxy for word2vec ([LIT-855](../literature.d/LIT-855.md)). [LIT-859](../literature.d/LIT-859.md) obtains it in a
linear-attention layer, where the product is of two attention blocks rather
than two layers. [THEORY-183](THEORY-183.md)'s Fourier geometry has the ring case as its
precedent. [THEORY-039](THEORY-039.md) gains a derived kind of phase. [THEORY-086](THEORY-086.md) is the
contrast: in the kernel regime a network fits eigenspace by eigenspace at
exponential rates, which is this account's shallow case.
