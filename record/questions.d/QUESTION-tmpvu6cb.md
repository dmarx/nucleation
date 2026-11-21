---
status: Open
title: 'Can the representational manifold a deep network learns be modelled as an active-matter system in high dimension, and if so in which sense: coupled motion under optimization, sustained nonequilibrium currents, or critical collective dynamics?'
version: 1
tags:
- representation-learning
- complex-systems
- learning-theory
date: '2026-11-21'
line:
- learned-structure
summary: >-
  The owner's, at U18 of the exchange "Rich Get Richer Power Laws"
  (2026-11-21): "how about if high dimensional systems? consider a
  representational manifold learned by a DNN modeled as an active matter
  system". The other assistant's answer (A29) grades the idea into three
  hypotheses of increasing strength, and the owner's next turn (U19) adds
  concentration of measure as the baseline any such model has to beat
  ([CLAIM-tmpfwwfy](../claims.d/CLAIM-tmpfwwfy.md)).
---
<!-- inactive-ok-file: CLAIM-tmpfwwfy CLAIM-tmp526xr CLAIM-tmpet76z CLAIM-tmpu6t8z TERM-tmplplcf CLAIM-tmp41gfr CLAIM-tmpqqngq THEORY-1095 THEORY-2051 THEORY-209 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21; Proposed entries the record already held, cited for context -->

# QUESTION-tmpvu6cb: Can the representational manifold a deep network learns be modelled as an active-matter system in high dimension, and if so in which sense: coupled motion under optimization, sustained nonequilibrium currents, or critical collective dynamics?

## Why it is a question

The owner, at U18: "how about if high dimensional systems? consider a
representational manifold learned by a DNN modeled as an active matter
system".

The record holds Toner and Tu's theory of flocks ([THEORY-1085](../theory.d/THEORY-1085.md), [THEORY-1095](../theory.d/THEORY-1095.md)),
a reading on symmetry breaking and Goldstone modes in deep networks
([THEORY-2051](../theory.d/THEORY-2051.md)), and readings on the probability currents of SGD ([THEORY-209](../theory.d/THEORY-209.md),
[THEORY-779](../theory.d/THEORY-779.md)). It has nothing on what would make a population of learned
representations an active-matter system, or on which dimension would govern
its collective behaviour.

A29 §11 separates three things the question could mean, "of increasing
strength", and warns that "these hypotheses shouldn't be collapsed into a
single assertion":

1. **Collective representation dynamics**: embeddings "behave like coupled
   particles whose movements are mediated by shared parameters". A29: "This
   follows naturally from the gradient-flow formulation" ([CLAIM-tmp526xr](../claims.d/CLAIM-tmp526xr.md)).
2. **Nonequilibrium self-organization**: a "driven, noisy process with
   measurable irreversible dynamics", which "needs to be demonstrated rather
   than assumed".
3. **Critical or scale-free active representation dynamics**: collective
   rearrangements, relaxation times or correlations obeying universal
   scaling laws, which "requires dynamical and finite-size evidence beyond a
   power-law covariance spectrum".

## What would count as an answer

- For the second sense: a source of broken detailed balance in training,
  identified and measured, such as nonzero probability currents or
  time-reversal asymmetry in the trajectories of a fixed probe set's
  representations. Gradient flow alone cannot supply one ([CLAIM-tmpet76z](../claims.d/CLAIM-tmpet76z.md)); [THEORY-209](../theory.d/THEORY-209.md)
  and [THEORY-779](../theory.d/THEORY-779.md) say where SGD's currents come from in the parameters.
- For the third: velocity correlations, slow modes and finite-size collapse
  that neither the high-dimensional concentration null ([CLAIM-tmp41gfr](../claims.d/CLAIM-tmp41gfr.md), [CLAIM-tmpqqngq](../claims.d/CLAIM-tmpqqngq.md)) nor
  the correlations the representation kernel predicts already explain
  ([LEAD-tmpp88ld](../leads.d/LEAD-tmpp88ld.md)).
- Or a dissolution: an argument that representations lack the
  self-propulsion or orientational degrees of freedom any active-matter
  theory needs, so that only the first sense survives and "active" adds
  nothing to "coupled".

Which dimension governs the collective behaviour is part of the question:
A29 argues it is the spectral dimension of the interaction geometry, not
layer width ([CLAIM-tmpu6t8z](../claims.d/CLAIM-tmpu6t8z.md); the senses are [TERM-tmplplcf](../terms.d/TERM-tmplplcf.md)).
