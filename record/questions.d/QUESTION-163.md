---
number: 163
status: Open
formerly:
- QUESTION-tmpujty6
title: "Do Blackwell-equivalent representations of trained networks carry different stitching penalties under the paper's own protocol, by more than the spread across stitching seeds and top networks, or does an independent treatment relate stitching to the comparison of experiments?"
version: 1
tags:
- representation-learning
- mathematical-statistics
date: '2026-10-19'
line: 'learned-structure'
summary: >-
  The promotion condition formerly on [THEORY-176](../theory.d/THEORY-176.md), moved here unchanged when
  [THEORY-176](../theory.d/THEORY-176.md) was promoted on 2026-10-19. That Blackwell-equivalent
  representations can stitch differently is shown by a constructed example.
  Whether they do, by a measurable margin, in trained networks under the
  paper's protocol is untested.
---

# QUESTION-163: Do Blackwell-equivalent representations of trained networks carry different stitching penalties under the paper's own protocol, by more than the spread across stitching seeds and top networks, or does an independent treatment relate stitching to the comparison of experiments?

## Why it is a question

[THEORY-176](../theory.d/THEORY-176.md), promoted on 2026-10-19, holds that Bansal, Nakkiran and
Barak's stitching penalty ([LIT-850](../literature.d/LIT-850.md)) compares representations in one
decision problem, through a fixed top network and a restricted map class,
and so is not Blackwell's order. Its clause that representations which are
functions of each other can stitch differently is an existence claim. A
two-position, one-channel example, in which a 1×1 stitcher cannot undo a
swap of positions, now shows it. Until that date [THEORY-176](../theory.d/THEORY-176.md)'s promote_when
asked for that possibility measured in trained networks. At the owner's
direction, from the promotion audit's batch 027 ([ADR-047](../decisions.d/ADR-047.md)), the THEORY was
promoted on the example, and the condition moved here unchanged.

It is open because the example shows the possibility, not its size in
practice. The paper argues that a pixel shuffle would stitch worse, and
does not run the experiment ([NOTE-653](../notes.d/NOTE-653.md)).

## What would answer it

The condition formerly on [THEORY-176](../theory.d/THEORY-176.md), unchanged. Two representations, each
an invertible function of the other (the paper's own case is a spatial
permutation of a layer's activations), stitched into the same top network
under the paper's protocol (1×1 convolutional stitcher, trained on the
task's training set, penalty on its test set), with the difference in
penalty larger than the spread across stitching seeds and across two top
networks. Or an independent published treatment that relates the stitching
penalty to the comparison of experiments, or to a usable-information order,
and reaches the same relation. The relation is refuted by a step of its
derivation shown wrong, or by the stitching order shown, for the paper's
map class, to be invariant under every invertible transformation of the
representation. More experiments in which a better-trained representation
lowers a weaker network's error cannot settle it, since they are
compatible with both readings.
