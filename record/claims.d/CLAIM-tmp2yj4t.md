---
status: Proposed
title: 'A residual network''s depth is a restatement chain whose skip connection copies the state and whose branches add to it, so the drift kinds of the linear Gaussian model apply: random branch contributions add diffusively and stay of order one under a branch scale of one over the square root of depth, systematic ones add linearly and need one over depth, and a network without skip connections contracts in depth and forgets its input over a depth scale'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Revised after the readings of 2026-11-21 of Tensor Programs VI
    (NOTE-tmppdqgb) and Bordelon and colleagues (NOTE-tmpo9k2m). Both
    confirm both rows, and the 1/L recollection; defeater (b) is not met.
    Grounds move from the unread works to the readings. Qualifications
    added: α = ½ is the smallest exponent keeping diffusion of order one,
    not one the random part needs; the drift term includes the correlated
    part of the initial weights' action; deeper blocks are a clash between
    the rows, not a new kind. Title unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  Either of two results. (a) A residual network at initialization whose
  representation changes over depth by an amount that does not grow as
  the square root of depth times the branch scale, with branches whose
  contributions are uncorrelated across blocks. (b) A reading of the
  depth-μP and depthwise-transfer papers (LIT-tmp4peep, LIT-tmpu5m2v)
  that finds the learned change per block is not of order one over depth
  under their parameterization, so that the systematic row does not
  describe it.
tags:
- learning-theory
- probabilistic-modeling
- anthology-candidate
date: '2026-11-20'
line:
- learned-structure
- nucleating-argument
rests_on:
- CLAIM-tmphedau
grounds:
- THEORY-2041
- THEORY-tmpbyw89
- THEORY-tmpybeh6
summary: >-
  The second link the owner asked for, between the record's time-scale
  results and depth scaling. A residual block x_(l+1) = x_l + L^(−α) f_l(x_l)
  is [CLAIM-tmphedau](CLAIM-tmphedau.md)'s step with the skip as an exact copy and the branch
  as the error. The record's drift table then says why branch scales
  differ: zero-mean contributions accumulate as √L, systematic ones as L.
  Both rows are confirmed by the readings of 2026-11-21 of Tensor Programs
  VI and Bordelon and colleagues, which name them noise or diffusion and
  drift. Without skips,
  Schoenholz's ordered phase ([THEORY-2041](../theory.d/THEORY-2041.md)) is the contracting row. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: THEORY-tmpbyw89 THEORY-tmpybeh6 THEORY-tmpky55f — Proposed; readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-tmphedau THEORY-2041 CLAIM-tmpw6wkt CLAIM-tmpdx6l8 — Proposed or Deferred; the model this applies, the works it rests on until read, and the claims filed with it -->

# CLAIM-tmp2yj4t: A residual network's depth is a restatement chain whose skip connection copies the state and whose branches add to it, so the drift kinds of the linear Gaussian model apply: random branch contributions add diffusively and stay of order one under a branch scale of one over the square root of depth, systematic ones add linearly and need one over depth, and a network without skip connections contracts in depth and forgets its input over a depth scale

## The claim

A residual block maps x_l to x_(l+1) = x_l + L^(−α)·f_l(x_l). Read depth as
the steps of [CLAIM-tmphedau](CLAIM-tmphedau.md)'s restatement chain: the skip connection is a = 1,
an exact copy, and the branch is what each step adds. Over L blocks the
representation drifts by the sum of the branch terms.

- **Random contributions: diffusive.** At initialization the branches'
  outputs are roughly independent across blocks with mean zero. They add as a
  random walk, total size √L·L^(−α)·σ. α = ½ is the smallest exponent that
  keeps that total of order one, and larger ones make it vanish: Tensor
  Programs VI ([THEORY-tmpbyw89](../theory.d/THEORY-tmpbyw89.md)): "each one of the L residual blocks
  contributes Θ(1/√L) to the main branch. These L contributions are
  independent of each other, so the sum of them is of size Θ(1)"; Bordelon
  and colleagues ([THEORY-tmpybeh6](../theory.d/THEORY-tmpybeh6.md)) derive the same as Brownian motion in
  layer time and allow any α ≥ ½ with a learning rate scaled as
  L^(2α−1).
- **Systematic contributions: linear.** During training the updates that
  each block's weights receive are correlated across blocks, since they
  answer the same loss. Their effects add as L·μ, so a total of order one
  needs a learned change of order 1/L per block. Confirmed in both readings:
  "During training, the contribution of the update of each residual block is
  Θ(1/L) due to the combining effect of the learning rate and multiplier.
  The contributions of the updates are highly correlated, so they sum up to
  Θ(1)" ([THEORY-tmpbyw89](../theory.d/THEORY-tmpbyw89.md)); for SGD the 1/√L enters twice, once as the
  multiplier and once in the gradient, so the learning rate needs no depth
  factor ([THEORY-tmpybeh6](../theory.d/THEORY-tmpybeh6.md), whose skip connections "generate long-range
  correlations across layers"). Both papers name the two terms as this
  claim does: a noise or diffusion term and a drift term. The drift term
  also includes the correlated part of the initial weights' action, so
  "systematic" means correlated across blocks, not only learned. The tuned
  lens finds trained residual updates aligned with the negative loss
  gradient at every layer ([THEORY-tmpky55f](../theory.d/THEORY-tmpky55f.md)), a small systematic component.
- **No skip: contracting.** Without the identity, each layer maps
  representations toward a fixed point in the ordered phase, and the
  correlation between inputs converges over a depth scale that diverges only
  at the order-to-chaos transition ([THEORY-2041](../theory.d/THEORY-2041.md)). That is [CLAIM-tmphedau](CLAIM-tmphedau.md)'s
  contracting row: the input is forgotten geometrically in depth. The skip
  connection moves the network to the copied-with-error row, where the input
  is lost only as 1/n ([CLAIM-tmpw6wkt](CLAIM-tmpw6wkt.md)), or not at all as the error goes to
  zero.

So the choice of residual scaling is the choice, for each kind of
contribution, of which drift row keeps it of order one. In
[CLAIM-tmpdx6l8](CLAIM-tmpdx6l8.md)'s terms the skip puts the representation in the conserved
part of the step and the branch scale fixes how much error each step may
add.

## What it does not say

- Not that the depth-μP results are derived here. They are the readings'
  ([THEORY-tmpbyw89](../theory.d/THEORY-tmpbyw89.md), [THEORY-tmpybeh6](../theory.d/THEORY-tmpybeh6.md)), both heuristic or at physics-level
  rigour.
- Not that the linear Gaussian model describes trained networks. The branch
  terms are neither Gaussian nor independent of the state; the claim is about
  how contributions accumulate, which needs only their correlation across
  blocks.
- Not a further drift kind for deeper blocks. Tensor Programs VI's
  "fundamental limitations" are a clash between the two rows: the 1/√L
  scaling keeps each block's interior in the kernel regime, and escaping it
  adds a drift term as large as the noise term, so a single multiplier either
  destabilizes or loses diversity ([THEORY-tmpbyw89](../theory.d/THEORY-tmpbyw89.md), §§9.2–9.3).
- Not that one multiplier is chosen per row. One multiplier serves both; the
  choice of α decides whether the diffusive row survives (α = ½) or vanishes
  (α > ½, the redundant or ODE scalings).
