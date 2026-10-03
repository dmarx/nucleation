---
status: Active
status_note: 'read 2026-10-03 ([NOTE-tmp3zzdt](../notes.d/NOTE-tmp3zzdt.md)); worth reading as the empirical taxonomy of loss landscapes by local and global structure: Hessian top eigenvalue and trace separate locally sharp from locally flat, Bezier-curve mode connectivity between independently trained models separates globally poorly-connected from well-connected, and CKA similarity of their outputs splits the well-connected, flat phase in two. Across a load-like by temperature-like grid (width, data amount or label noise against batch size, learning rate or weight decay), the best test accuracy sits in the flat, well-connected, high-similarity phase IV-B; the Hessian alone mispredicts, and where connectivity is poor, training to zero loss can lower test accuracy. Empirical only, mostly ResNet18 on CIFAR-10.'
title: 'Taxonomizing local versus global structure in neural network loss landscapes'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v2 (12 December 2021, 33 pages; v1 23 July 2021).
    Published at NeurIPS 2021 (the arXiv journal reference). Main text and
    Appendices A–D read; the per-pixel phase diagrams are read from their
    captions and the text, since the extracted text carries no plotted
    values. Not held in the Anthology of the SOTA: a grep of its record for
    "2107.11228" and "Taxonomizing" found nothing.
tags:
- loss-landscapes
- learning-theory
- anthology-candidate
date: '2026-10-03'
published: '2021-07-23'
arxiv: '2107.11228'
first_author: 'Yang'
keywords:
- 'loss landscape'
- 'local versus global structure'
- 'mode connectivity'
- 'CKA similarity'
- 'Hessian eigenvalue'
- 'Hessian trace'
- 'load-like parameter'
- 'temperature-like parameter'
- 'phase diagram'
- 'double descent'
- 'statistical mechanics of learning'
- 'rugged convexity'
extends:
- LIT-tmpms4ta
- LIT-tmpotq71
implementations: []
summary: >-
  Yang, Hodgkinson, Theisen, Zou, Gonzalez, Ramchandran & Mahoney (2021),
  NeurIPS. Thousands of trained networks are placed on a load-like by
  temperature-like grid and measured three ways: Hessian top eigenvalue and
  trace (local sharpness), Bezier-curve mode connectivity between two
  independently trained models (global connectivity), and CKA similarity of
  their outputs on mixup points. Two transitions give four phases: I sharp
  and poorly connected, II sharp and well connected, III flat and poorly
  connected, IV flat and well connected, with IV split by CKA into IV-A and
  IV-B. Test accuracy is best in IV-B. Sharpness alone mispredicts accuracy
  across phases, and in phase III training to zero loss does worse than
  stopping in the sharp phases. Double descent appears as a dark band at the
  phase boundary under label noise.
---


# LIT-tmpf3sak: Taxonomizing local versus global structure in neural network loss landscapes

Yaoqing Yang, Liam Hodgkinson, Ryan Theisen, Joe Zou, Joseph E. Gonzalez, Kannan Ramchandran and Michael W. Mahoney (2021), *NeurIPS 2021* — [ARXIV-2107.11228](https://arxiv.org/abs/2107.11228)

## Key takeaways

- **Three probes, two transitions, four phases.** Local curvature (top
  Hessian eigenvalue and trace from PyHessian), global connectivity
  (mc(θ, θ′) = ½(L(θ) + L(θ′)) − L(γ(t*)) along a trained quadratic Bezier
  curve, Eq. 4) and similarity (linear CKA of softmax outputs on mixup
  points, Eq. 3). A Hessian transition separates sharp (I/II) from flat
  (III/IV); a connectivity transition separates poorly connected (I, III,
  with mc < 0, a barrier) from well connected (II, IV). CKA splits IV into
  IV-A and IV-B, by a smooth crossover rather than a sharp transition
  (Section 3.1, Figure 2).
- **The central claim:** the best test accuracy is obtained when the
  landscape is "globally nice" (well connected and similar) and the model
  sits in a locally flat region, phase IV-B. It holds with learning-rate
  decay, with weight decay or learning rate as the temperature, with data
  amount or label noise as the load, on CIFAR-10, CIFAR-100, SVHN, VGG11 and
  a six-layer Transformer on IWSLT'16 (Sections 3.2–3.3, Appendix D).
- **Local flatness is not enough.** Phase III has about the same Hessian as
  IV-A and lower accuracy. With label noise, the Hessian barely changes
  while connectivity and CKA fall (Figure 8). On a column through phase III
  with 10% noisy labels, the sharp, not-converged phases I/II beat phase III
  (Figure 4). The authors read the observed correlation of sharpness with
  generalization as possibly confounded by studying good models on good
  data.
- **Width buys connectivity; data buys similarity.** Wider models are
  better connected; more data raises CKA but needs larger models to stay
  connected; cleaner labels raise connectivity (Section 5).
- **Double descent at a phase boundary.** With 10% random labels, test
  accuracy shows width-wise and temperature-wise double descent as a dark
  band whose shape follows the Hessian transition (Figure 4), read as the
  "bad fluctuations" between phases that the statistical-mechanics picture
  predicts.

## Standing in the record

Filed on 2026-10-03 with the owner's batch on mode connectivity and model
merging ([ADR-027](../decisions.d/ADR-027.md)). It is the batch's one paper that classifies whole
landscapes rather than pairs of minima, so it is the place the batch's
connectivity results meet its generalization results.

**It extends Martin and Mahoney ([LIT-tmpms4ta](LIT-tmpms4ta.md)).** That paper proposed that a
network's generalization is governed by a load-like and a temperature-like
control parameter, with sharp phases between them, and drew the phase
diagram as a cartoon. This paper takes the two control parameters and the
phase-diagram picture from it, names it as the source of its "rugged
convexity", and measures the diagram on real networks with three probes.

**It extends Garipov et al. ([LIT-tmpotq71](LIT-tmpotq71.md)).** It takes that paper's curve
finding as its instrument: a quadratic Bezier curve with one trainable bend,
trained by sampling t and minimizing the loss at γ(t), with Garipov's
learning-rate schedule (Appendix A.2). What it adds is to read the curve's
worst point as a scalar (Eq. 4) and map it across a phase diagram. There
the curve that Garipov found low everywhere has a barrier, in small models
and on noisy labels (Figure 12).

It names the rest of the batch's lineage in prose. Draxler et al. (filed as
[LIT-tmp3kyq9](LIT-tmp3kyq9.md)) is cited with Garipov as the origin of mode connectivity, and
its observation that connectivity improves with size is what this paper's
"larger width improves connectivity" reproduces. Frankle et al.'s linear
mode connectivity from a shared trained start ([LIT-tmp3owu9](LIT-tmp3owu9.md)), Kuditipudi et
al.'s dropout-stability proof ([LIT-tmplpsy5](LIT-tmplpsy5.md)) and Fort and Jastrzębski's
high-dimensional tunnels are cited in the related work only. The paper does
not use permutation alignment, so its "poorly connected" phases are
measured without asking whether the barriers are permutation barriers. That
question belongs to the re-basin line of the batch.

Its double-descent reading cites Liao, Couillet and Mahoney ([LIT-tmpufwlh](LIT-tmpufwlh.md))
and Dereziński, Liang and Mahoney ([LIT-tmpzk7ci](LIT-tmpzk7ci.md)) as the analyzable settings
where double descent was derived from a transition between phases. It
claims only that its empirical bands "corroborate" them, so no relation is
declared.

Against the anthology: it bears directly on its practice that sharpness in
the loss landscape correlates with test error ([ANTH-SOTA-012](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-012.md), from Li et
al.'s landscape visualization, [ANTH-LIT-014](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-014.md)). This paper's phase III, and
its noisy-label runs, are cases where the sharpness ordering and the
accuracy ordering disagree. The anthology's proposed alternative of
measuring degeneracy rather than curvature once the loss has saturated
([ANTH-SOTA-325](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-325.md)) is another answer to the same insufficiency. It cites
stochastic weight averaging ([ANTH-LIT-673](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-673.md)) among sharpness-based practical
methods. It is ML measurement with a training instruction attached (check
connectivity before training to zero loss), so `anthology-candidate`.
