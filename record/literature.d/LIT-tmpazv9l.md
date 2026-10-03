---
status: Active
status_note: 'read 2026-10-03 ([NOTE-tmpp4hjy](../notes.d/NOTE-tmpp4hjy.md)); worth reading as the star domain conjecture: where SGD solutions are not convex modulo permutation, they still form a star domain, with a star model linearly connected, after weight matching, to every other solution. Starlight trains a candidate by sampling points on the lines to 50 permuted source models, and the candidate has lower barriers to held-out models than those models have to each other (ResNet-18 CIFAR-10 0.078 against 0.383; ImageNet-1k 2.794 against 5.948). Those barriers are lower, not zero, and the authors say the conjecture is unproved and the barriers are often significantly above zero. Preprint.'
title: 'Do Deep Neural Network Solutions Form a Star Domain?'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v2 (9 June 2024, 20 PDF pages; v1 was 12 March 2024)
    through the PDF text layer. v2 is marked "Preprint. Under review." and
    names no venue, so none is given here. Sections 1–5 and Appendices A–C
    and E read in full; Appendix D (interpolation plots for DenseNet, VGG
    and ImageNet) read from captions. `published:` is the arXiv v1 date.
    Not held in the Anthology of the SOTA: a grep of its record for the
    arXiv id, "Star Domain" and "Sonthalia" found nothing, and nucleation
    held nothing under that title.
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-03'
published: '2024-03-12'
arxiv: '2403.07968'
first_author: 'Sonthalia'
keywords:
- 'star domain'
- 'star model'
- 'linear mode connectivity'
- 'convexity conjecture'
- 'permutation invariance'
- 'weight matching'
- 'Bayesian model averaging'
- 'model fusion'
implementations:
- 'https://github.com/aktsonthalia/starlight'
summary: >-
  Sonthalia, Rubinstein, Abbasnejad & Oh (2024), preprint. Conjectures that
  SGD solution sets, modulo permutation, are star domains, which needs less
  width than convexity does. Starlight trains a star model by sampling
  points on the lines to permuted source models. The star model has much
  lower loss barriers to held-out solutions than those solutions have to
  each other, across ResNet-18, VGG, DenseNet, CIFAR and ImageNet-1k (e.g.
  0.078 against 0.383 on CIFAR-10). It gains with more source models, ranks
  uncertainty better in BMA than a deep ensemble, and is about 1 point more
  accurate than a single model.
extends:
- LIT-tmp2uwzo
- LIT-tmpd6bma
---


# LIT-tmpazv9l: Do Deep Neural Network Solutions Form a Star Domain?

Ankit Sonthalia, Alexander Rubinstein, Ehsan Abbasnejad and Seong Joon Oh
(2024), arXiv preprint — [ARXIV-2403.07968](https://arxiv.org/abs/2403.07968)

## Key takeaways

- **The star domain conjecture (Conjecture 2).** Let h be the width at
  which SGD solutions become convex modulo permutation. Then for some
  0 < α < 1, networks wider than αh have solution sets that are star domains
  modulo permutation. There is a star model θ⋆ such that every solution,
  after weight matching to θ⋆, has near-zero loss barrier with it.
- **Starlight.** Train θ by sampling a source model θ_n from Z and t from
  U[0, 1], taking a gradient step on the loss at (1 − t)θ + tπ(θ_n) scaled
  by (1 − t), and re-permuting all source models to θ by weight matching
  once per epoch (Algorithm 1).
- **Held-out solutions connect better to the star model than to each
  other.** Training-loss barriers between the star model and held-out
  models, against barriers between two regular models: ResNet-18 CIFAR-10
  0.078 vs 0.383, VGG19 0.336 vs 1.281, DenseNet CIFAR-100 3.735 vs 6.920,
  ResNet-18 ImageNet-1k 2.794 vs 5.948 (Table 1). The star-regular barrier
  falls as the number of source models grows from 2 to 50 and has not
  levelled off (Fig. 1). In a width sweep it is about a third of the
  regular-regular barrier (Fig. 2).
- **By-products.** Sampling along the lines from the star model gives
  better AUROC than a deep ensemble but worse ECE (Fig. 4). A star model
  trained with an added cross-entropy term beats a single model by about
  0.1–1.1 points but stays below the ensemble (CIFAR-100, 50 models: 78.4
  vs 77.3 single, 81.3 ensemble; Table 2).

## Standing in the record

Filed on 2026-10-03 with the owner's mode-connectivity batch ([ADR-027](../decisions.d/ADR-027.md)).
With Lin, Li and Wu ([LIT-tmpziwl2](LIT-tmpziwl2.md)) it is one of the batch's two star-domain
works. Lin et al. prove star-shaped connectivity in toy models without
permutation; this paper tests it on real networks with permutation, and
adds the held-out check that Lin et al. lack. The papers are concurrent, and
this one cites the other as such.

It extends two foundations held here. It takes Entezari et al.'s
([LIT-tmp2uwzo](LIT-tmp2uwzo.md)) conjecture, that SGD solutions are convex modulo permutation
once networks are wide enough, as its Conjecture 1. It then states its own
conjecture as a relaxation of that one, defined in terms of the width at
which Entezari's conjecture holds. The anthology reads Entezari et al. as
[ANTH-LIT-251](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-251.md). Its permutations are Git Re-Basin's ([LIT-tmpd6bma](LIT-tmpd6bma.md)) weight
matching, run inside Starlight, and its own regular-regular baselines,
which reconfirm that thin ResNets are not linearly connected after weight
matching, are Git Re-Basin's failure case ([ANTH-LIT-333](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-333.md) in the anthology).
Starlight's Monte Carlo sampling along lines is modelled, the paper says,
on Garipov et al.'s ([LIT-tmpotq71](LIT-tmpotq71.md)) curve fitting, and it places itself
beside Benton et al.'s ([LIT-tmp6yuwj](LIT-tmp6yuwj.md)) low-loss simplexes as another way to
connect many solutions at once.

On the relation to convexity: the paper does not refute Entezari's
conjecture. That conjecture is conditioned on width, and this paper's
evidence is that narrower networks fall short of it. The star domain is
offered as what holds below that width. So it is declared as `extends`,
not `rivals` or `corrects`.

It is flagged for the anthology because star models are offered as a
cheaper substitute for an ensemble at inference time, which bears on the
anthology's ensembling practice ([ANTH-SOTA-257](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-257.md)).
