---
status: Proposed
title: 'A residual network''s depth is a restatement chain whose skip connection copies the state and whose branches add to it, so the drift kinds of the linear Gaussian model apply: random branch contributions add diffusively and stay of order one under a branch scale of one over the square root of depth, systematic ones add linearly and need one over depth, and a network without skip connections contracts in depth and forgets its input over a depth scale'
version: 1
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
- LIT-tmpu5m2v
- LIT-tmp4peep
summary: >-
  The second link the owner asked for, between the record's time-scale
  results and depth scaling. A residual block x_(l+1) = x_l + L^(−α) f_l(x_l)
  is CLAIM-tmphedau's step with the skip as an exact copy and the branch
  as the error. The record's drift table then says why branch scales
  differ: zero-mean contributions accumulate as √L, systematic ones as L.
  Bordelon and colleagues' abstract states the 1/√depth branch scale; the
  assistant's recollection that depth-μP's learned changes land at order
  1/L per block is unverified until LIT-tmp4peep is read. Without skips,
  Schoenholz's ordered phase (THEORY-2041) is the contracting row. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-tmphedau LIT-tmpu5m2v LIT-tmp4peep THEORY-2041 CLAIM-tmpw6wkt CLAIM-tmpdx6l8 — Proposed or Deferred; the model this applies, the works it rests on until read, and the claims filed with it -->

# CLAIM-tmp2yj4t: A residual network's depth is a restatement chain whose skip connection copies the state and whose branches add to it, so the drift kinds of the linear Gaussian model apply: random branch contributions add diffusively and stay of order one under a branch scale of one over the square root of depth, systematic ones add linearly and need one over depth, and a network without skip connections contracts in depth and forgets its input over a depth scale

## The claim

A residual block maps x_l to x_(l+1) = x_l + L^(−α)·f_l(x_l). Read depth as
the steps of CLAIM-tmphedau's restatement chain: the skip connection is a = 1,
an exact copy, and the branch is what each step adds. Over L blocks the
representation drifts by the sum of the branch terms.

- **Random contributions: diffusive.** At initialization the branches'
  outputs are roughly independent across blocks with mean zero. They add as a
  random walk, total size √L·L^(−α)·σ. A total of order one needs α = ½: the
  branch scale 1/√depth that Bordelon and colleagues use with μP
  (LIT-tmpu5m2v, from its abstract).
- **Systematic contributions: linear.** During training the updates that
  each block's weights receive are correlated across blocks, since they
  answer the same loss. Their effects add as L·μ, so a total of order one
  needs a learned change of order 1/L per block. The assistant recalls that
  depth-μP arranges this: the 1/√L multiplier applied once in the forward
  pass and once in the gradient gives 1/L. That is unverified until
  LIT-tmp4peep is read, which is defeater (b).
- **No skip: contracting.** Without the identity, each layer maps
  representations toward a fixed point in the ordered phase, and the
  correlation between inputs converges over a depth scale that diverges only
  at the order-to-chaos transition (THEORY-2041). That is CLAIM-tmphedau's
  contracting row: the input is forgotten geometrically in depth. The skip
  connection moves the network to the copied-with-error row, where the input
  is lost only as 1/n (CLAIM-tmpw6wkt), or not at all as the error goes to
  zero.

So the choice of residual scaling is the choice, for each kind of
contribution, of which drift row keeps it of order one. In
CLAIM-tmpdx6l8's terms the skip puts the representation in the conserved
part of the step and the branch scale fixes how much error each step may
add.

## What it does not say

- Not that the depth-μP results are derived here. They are recalled and,
  for the 1/L part, unverified.
- Not that the linear Gaussian model describes trained networks. The branch
  terms are neither Gaussian nor independent of the state; the claim is about
  how contributions accumulate, which needs only their correlation across
  blocks.
- Not Tensor Programs VI's finding that deeper blocks meet "fundamental
  limitations" (LIT-tmp4peep, abstract). Whether that is a further drift
  kind is open.
