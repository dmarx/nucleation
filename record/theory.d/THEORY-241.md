---
number: 241
status: Proposed
formerly:
- THEORY-tmp37j6t
promote_when: >-
  A quantitative measure of reuse and factoring (for example, the effect
  of single-weight or random-direction perturbations on a stated
  regularity of the output), applied across several seeds of SGD and
  several evolved networks per target, that separates the two by more
  than their seed-to-seed spread. Refuted if, with such a measure, SGD
  solutions of the same targets in the same architecture match the evolved
  ones. What cannot settle it: more selected neuron maps or sweeps, or
  behavioural anecdotes from large models, which are the kind of evidence
  the paper already has.
title: "Fitting the same function in the same architecture does not fix the internal decomposition: SGD reproduces three Picbreeder images from random weights without the reuse and factoring of the evolved networks, and perturbing its weights breaks the regularities that perturbing the evolved networks' weights preserves"
version: 1
tags:
- representation-learning
- learning-theory
date: '2026-10-14'
source:
- LIT-944
summary: >-
  Kumar, Clune, Lehman & Stanley (2025), [LIT-944](../literature.d/LIT-944.md), read in [NOTE-771](../notes.d/NOTE-771.md).
  For the skull, butterfly and apple CPPNs, SGD in the layerized evolved
  architecture fits the image, the network's whole function on the grid.
  It shows no reuse of the symmetric parts, and single-weight and
  random-direction sweeps distort the output, where the evolved networks'
  sweeps vary it meaningfully. Qualitative, curated and three images. The
  paper's account of why, the order of discovery in open-ended search,
  and its extension to large models are conjecture.
answers:
- QUESTION-060
---
<!-- inactive-ok-file: THEORY-210 THEORY-112 — Proposed; accounts this one bears on -->

# THEORY-241: Fitting the same function in the same architecture does not fix the internal decomposition: SGD reproduces three Picbreeder images from random weights without the reuse and factoring of the evolved networks, and perturbing its weights breaks the regularities that perturbing the evolved networks' weights preserves

## Source

Kumar, Clune, Lehman and Stanley (2025), [LIT-944](../literature.d/LIT-944.md), read in [NOTE-771](../notes.d/NOTE-771.md):
§§3–4 and 6, Appendices B–F.

## What was actually shown

**The comparison.** A CPPN maps a pixel's coordinates to its colour, so
its image on the grid is its whole input–output function. Three
networks found by Picbreeder's human-guided evolution (skull, butterfly,
apple) were rewritten exactly as dense MLPs ("layerization", App. B). In
each such architecture, a network was trained from LeCun-normal weights
by full-batch SGD on MSE to reproduce the evolved network's image. It did
so, "effectively identical" (Figs. 4, 13).

**The difference.** The two networks compute the same function in the
same architecture.
- **Neuron maps (Figs. 5, 14–15, 18–19).** The evolved skull is
  y-symmetric from early layers, with 24 novel maps and separate neurons
  for outline, eyes, nose and mouth. The SGD skull represents the two
  sides as symmetric only at the output and uses many high-frequency maps.
  The evolved apple separates background, body and stem; the SGD apple
  mixes them.
- **Weight sweeps (Figs. 6, 16, 20).** In the evolved networks, single
  weights produce coherent variations that keep the symmetry: a mouth
  opens, an eye winks, a stem swings. In the SGD networks they produce
  distortions that break it.
- **Basis checks (App. F).** In a PCA basis the SGD skull is only
  "slightly" more organised. Sweeps of a random weight-matrix column along
  a random unit vector, which do not depend on the choice of basis, show
  the same contrast (Fig. 25).
- **ReLU networks (App. E).** ReLU MLPs trained on the three images look
  fractured too.

What could have come out the other way: SGD, fitting a symmetric image
exactly, could have found the reuse, the shared computation for both
sides, that the evolved network has. In a space that contains that
solution, it did not.

## What this does not say

- **Not a measured difference.** There is no metric of fracture or
  factoring. The sweeps shown were selected, though the authors say they
  are representative and release all of them. Each target has one SGD
  network shown.
- **Not that SGD always fractures.** Three small targets, one optimiser
  setting, a single fixed objective. The authors themselves expect other
  uses of SGD may do better.
- **Not why.** The paper attributes the evolved networks' organisation to
  the order of discovery: symmetry first, then a face, then a skull. That
  is not tested against NEAT's gradual growth, or against selection for
  mutational robustness, which is what the sweeps measure.
- **Not large models.** The extension to LLMs rests on analogy and on
  behavioural anecdotes.
- **Not a fair search.** SGD failed in the sparse evolved architecture
  (Fig. 12). The evolved networks are a few celebrated finds of a very
  large human search.

## Connections

- **[QUESTION-060](../questions.d/QUESTION-060.md).** Holding both objective and architecture fixed leaves the
  internal variables undetermined. The training path is a further
  determinant. The evolved network was never trained on the objective, so
  the contrast is objective-trained against unobjective, not one
  objective against another.
- **[THEORY-197](THEORY-197.md).** The objective constrains what is kept but, satisfied
  exactly, does not determine it.
- **[THEORY-206](THEORY-206.md).** The evolved solution was representable in the sparse
  architecture but not reachable there by SGD.
- **[THEORY-210](THEORY-210.md) and [THEORY-112](THEORY-112.md).** Those concern solutions related by
  parameter symmetries. App. F's basis-agnostic sweeps argue that this
  difference is not one.
- **[THEORY-230](THEORY-230.md).** Its Prop. 3 constructs identical outputs with different
  hidden geometries through a GL(d) gauge. This is an empirical case
  beyond a gauge.
