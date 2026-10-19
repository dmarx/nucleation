---
number: 736
status: Active
formerly:
- THEORY-tmpnp4vw
title: "Two ε-dropout-stable solutions of a multilayer ReLU net, under a loss convex in the output, are joined by a piecewise-linear path whose loss never exceeds the worse endpoint's by more than ε, and joined pairwise paths compose with no higher barrier than their worst"
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-109 and filed Active at the owner's direction,
    carrying out the promotion audit's decision for THEORY-109 (batch 030,
    ADR-047). THEORY-109 bundled a theorem with an extrapolation its own
    body disclaims ("'One set' is extrapolated"), and its promote_when tests
    only the extrapolation. This THEORY holds the theorem. NOTE-544 read
    the theorem's proof in full (LIT-671, Appendix A), so it meets the
    standard THEORY-014 was promoted on, a theorem proved in a work the
    record has read, and no re-derivation was needed. THEORY-109 keeps the
    rest and extends this one.
tags:
- loss-landscapes
- mathematics
- anthology-candidate
date: '2026-10-19'
source:
- LIT-671
- LIT-653
summary: >-
  Kuditipudi et al. (2019), [LIT-671](../literature.d/LIT-671.md), Theorem 1, read in full in [NOTE-544](../notes.d/NOTE-544.md),
  with Draxler et al.'s (2018) concatenation bound from [LIT-653](../literature.d/LIT-653.md). Dropout
  stability gives every solution a half-width copy with the same loss up
  to ε. Half the units are then free, so working units can be swapped in
  and permuted at no cost. That joins any two such solutions. It is a
  statement about dropout-stable solutions only: whether training
  produces them is [THEORY-109](THEORY-109.md)'s open question, and Theorem 4 of the same
  paper builds disconnected global minima.
extended_by:
- THEORY-109
---
<!-- inactive-ok-file: THEORY-109 — Proposed; the synthesis this theorem was split from and that extends it, cited as open -->

# THEORY-736: Two ε-dropout-stable solutions of a multilayer ReLU net, under a loss convex in the output, are joined by a piecewise-linear path whose loss never exceeds the worse endpoint's by more than ε, and joined pairwise paths compose with no higher barrier than their worst

## Source

- Kuditipudi, Wang, Lee, Zhang, Li, Hu, Arora & Ge (2019), [LIT-671](../literature.d/LIT-671.md), read in
  [NOTE-544](../notes.d/NOTE-544.md): §§1–6 and Appendix A, the proof of Theorem 1, in full (claims
  table C1, "strong (proof)").
- Draxler, Veschgini, Salmhofer & Hamprecht (2018), [LIT-653](../literature.d/LIT-653.md), read in
  [NOTE-531](../notes.d/NOTE-531.md), for the concatenation bound (§3).

## What was actually shown

**Setting.** A fully connected ReLU network with d layers, h_j units in
layer j, and a loss convex in the network's output. Cross-entropy over a
softmax qualifies. Two parameter settings θ_A and θ_B are ε-connected if
some continuous path π joins them with L(f_π(t)) ≤ max{L(θ_A), L(θ_B)} + ε
throughout. A solution is ε-dropout stable if, layer by layer from any
layer i up, keeping at most ⌊h_j/2⌋ units of each layer j, zeroing the
rest and rescaling the kept outputs costs at most ε in loss
(Definition 1).

**Theorem 1.** Two ε-dropout-stable solutions are ε-connected, by a path
of finitely many line segments. The proof combines three lemmas:

- *Lemma 1.* There is a path from θ to its dropout version, keeping loss
  at most L(θ) + ε. It uses two kinds of step. One changes the incoming
  weights of units whose outgoing weights are already zero, which leaves
  the function unchanged. The other linearly interpolates the top layer's
  weights, where the output is linear in the weights and the loss convex
  in the output, so the loss on the segment is at most the larger of its
  ends.
- *Lemma 4.* In a network with half its units zeroed, the live units can
  be permuted in five segments at constant loss, using the dead half as
  scratch space.
- *Lemma 2.* Two half-zeroed networks are joined by 8 segments with loss
  at most the larger of the two.

Chaining them (A to its dropout version, across to B's dropout version,
then to B) gives a path whose loss never exceeds max{L(θ_A), L(θ_B)} + ε.

**Composition.** Draxler et al.'s bound: if A and B are joined with
barrier L_AB and B and C with L_BC, then following one path and then the
other joins A and C with L*_AC ≤ max{L_AB, L_BC}. It is immediate from
concatenating the two paths. It is what turns pairwise ε-connectivity into
connectivity of any finite set of dropout-stable solutions, at the same ε.

## What this does not say

- **That trained networks are dropout-stable.** Kuditipudi et al. check
  this only roughly, for MNIST convnets and one VGG-11 (§6; [NOTE-544](../notes.d/NOTE-544.md) C4,
  weak to moderate). Whether SGD's solutions are dropout-stable, and so
  connected, is [THEORY-109](THEORY-109.md)'s claim, and it stays Proposed.
- **That all minima are connected.** Theorem 4 of the same paper builds
  disconnected global minima at any width. Its construction was read for
  statement and structure, not checked, and it stays with [THEORY-109](THEORY-109.md).
- **The noise-stable version.** Theorem 2 gives a 10-segment path with
  barrier Õ(ε) under noise stability. Its proof (Appendix B) was read for
  its statements only, and it is not held here.
- **That the path is short or straight.** Its segment count grows with
  depth, and nothing here explains Garipov et al.'s one-bend curves.
