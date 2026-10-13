---
status: Active
status_note: 'read 2026-10-13 ([NOTE-tmp7y8us](../notes.d/NOTE-tmp7y8us.md)): main text in full, and Appendices F, I and J; Appendices A–E, G and H not checked. The first-hand source for the conservation laws and their breaking that [THEORY-210](../theory.d/THEORY-210.md) took from the [LIT-970](LIT-970.md) survey.'
title: 'Neural Mechanics: Symmetry and Broken Conservation Laws in Deep Learning Dynamics'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read at the owner's request ("read Neural Mechanics and Ziyin et al.
    2023a"), from arXiv v2 (29 March 2021, the ICLR 2021 version), text
    extracted with pdftotext. `published:` is the v1 date, 8 December 2020.
    Not held in the Anthology of the SOTA: a grep of its record for the
    identifier found nothing.
tags:
- learning-theory
- loss-landscapes
- anthology-candidate
date: '2026-10-13'
published: '2020-12-08'
arxiv: '2012.04728'
first_author: 'Kunin'
keywords:
- 'parameter symmetry'
- 'conservation law'
- 'Noether'
- 'modified gradient flow'
- 'weight decay'
- 'batch normalization'
implementations:
- 'https://github.com/danielkunin/neural-mechanics'
summary: >-
  Kunin, Sagastuy-Brena, Ganguli, Yamins & Tanaka (2021), ICLR. A
  differentiable symmetry of the loss makes the gradient orthogonal to the
  symmetry's generator and constrains the Hessian. Under gradient flow each
  symmetry then conserves a quantity: translation (softmax) the parameter
  sum, scale (batchnorm) the norm, and rescale (homogeneous activations)
  the difference of squared norms. Weight decay and finite learning rates
  break these laws, and a modified gradient flow gives exact integral
  expressions for the broken quantities, matched on VGG-16 trained on Tiny
  ImageNet. Gradient noise is orthogonal to the generators, so it is
  low-rank along symmetry directions.
---
<!-- inactive-ok-file: THEORY-210 THEORY-tmpdsy58 THEORY-209 — Proposed; the accounts this reading feeds, open -->

# LIT-tmpxnix4: Neural Mechanics: Symmetry and Broken Conservation Laws in Deep Learning Dynamics

Daniel Kunin, Javier Sagastuy-Brena, Surya Ganguli, Daniel L. K. Yamins, Hidenori Tanaka (2021), *ICLR 2021* — [ARXIV-2012.04728](https://arxiv.org/abs/2012.04728)

## Key takeaways

- **Symmetry constrains geometry.** If L(ψ(θ, α)) = L(θ), the gradient is
  orthogonal to the generator ∂_α ψ, and the Hessian obeys a matching
  constraint (Eqs. 1–2).
- **Three symmetries, three conservation laws.** Under gradient flow,
  translation conserves the parameter sum, scale conserves the norm, and
  rescale conserves the difference of squared norms (Theorem 1,
  Eqs. 11–13).
- **Weight decay and finite steps break them.** With weight decay λ and
  learning rate η, each quantity is an exponentially decaying memory of
  its initial value plus an integral of gradient norms (Eqs. 18–20). For
  scale-symmetric weights, weight decay pulls in and discretization pushes
  out, so at stationarity the angular speed is √(2λ/η).
- **Noise lies off the symmetry directions.** Batch gradients obey the
  same orthogonality, so the noise covariance annihilates the generators
  (§5, App. F).

## Standing in the record

Read for the null space that [THEORY-209](../theory.d/THEORY-209.md)'s limiting dynamics leave out,
and as the first-hand source for [THEORY-210](../theory.d/THEORY-210.md). The reading is [NOTE-tmp7y8us](../notes.d/NOTE-tmp7y8us.md).
Its stochastic term (App. F) is the mechanism Ziyin et al. ([LIT-tmppdo96](LIT-tmppdo96.md))
develop into a law of balance ([THEORY-tmpdsy58](../theory.d/THEORY-tmpdsy58.md)).
