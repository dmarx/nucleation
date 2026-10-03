---
status: Active
status_note: 'read 2026-10-03 ([NOTE-tmprwelh](../notes.d/NOTE-tmprwelh.md)); worth reading as the paper that ties a loss barrier to a difference in what two models compute. It defines two models as mechanistically similar when they are invariant to the same interventions on the data-generating process, finds that models relying on a spurious cue and models ignoring it are connected by quadratic paths but not by linear ones, even after permutation, and conjectures that a linear barrier always signals mechanistic dissimilarity. The conjecture is proved only for a one-hidden-layer ReLU network on a synthetic process; the evidence is synthetic cues on CIFAR-10, CIFAR-100 and Dominoes.'
title: 'Mechanistic Mode Connectivity'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v3 (1 June 2023, 40 PDF pages, the ICML 2023
    camera-ready, PMLR 202) through the PDF text layer. Sections 1–8 and
    Appendices C, D, E and F (the proofs of Propositions 1–2, Lemma 2 and
    the one-hidden-layer case of Conjecture 1) were read in full; Appendices
    A, B, G and H (related work, training curves and the figure galleries
    for other datasets) were skimmed. Table 1's numbers were taken from the
    text layer. `published:` is the arXiv v1 date, 15 November 2022. Not
    held in the Anthology of the SOTA: a grep of its record for the arXiv
    id, "Mechanistic Mode Connectivity" and "Lubana" found nothing, and
    nucleation held nothing under that title.
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-10-03'
published: '2022-11-15'
arxiv: '2211.08422'
first_author: 'Lubana'
keywords:
- 'mode connectivity'
- 'linear mode connectivity'
- 'mechanistic similarity'
- 'invariance'
- 'counterfactuals'
- 'spurious attributes'
- 'fine-tuning'
- 'connectivity-based fine-tuning'
implementations:
- 'https://github.com/EkdeepSLubana/MMC'
summary: >-
  Lubana, Bigelow, Dick, Krueger & Tanaka (2022), ICML 2023. Two models are
  mechanistically similar if they are invariant to the same interventions on
  the data-generating process. Models that use a spurious cue and models
  that ignore it are mode connected along quadratic paths but not along
  linear ones, even after permutation matching, and the paper conjectures
  that a linear barrier implies mechanistic dissimilarity (proved for a
  one-hidden-layer ReLU network). Naive fine-tuning on clean data stays
  linearly connected to the pretrained model and keeps its reliance on the
  cue; a fine-tune that forces a barrier removes it.
extends:
- LIT-tmpotq71
- LIT-tmp3owu9
---


# LIT-tmpl64hd: Mechanistic Mode Connectivity

Ekdeep Singh Lubana, Eric J. Bigelow, Robert P. Dick, David Krueger and
Hidenori Tanaka (2022), Proceedings of the 40th International Conference on
Machine Learning (ICML 2023), PMLR 202 — [ARXIV-2211.08422](https://arxiv.org/abs/2211.08422)

## Key takeaways

- **Mechanistic similarity is defined by shared invariances.** Model a
  dataset as generated from independent latents; a model is invariant to an
  intervention on one latent if setting it to random values does not raise
  its loss. Two models are mechanistically similar when they are invariant
  to the same set of such interventions (Definitions 2–4).
- **Mechanistically dissimilar minimizers are mode connected, but not
  linearly.** A model trained with a label-correlated box cue and one
  trained without it are joined by a quadratic Bezier path of low loss on
  the training data, but that path does not hold on counterfactual data, and
  the linear path has a barrier even after activation-matching permutation
  (Fig. 4).
- **Conjecture 1: no linear connectivity, up to symmetries, implies
  mechanistic dissimilarity.** It is proved only for a one-hidden-layer
  ReLU network with interpolating minimizers, through Lemma 2: linear
  connectivity forces the two models to share activation patterns on the
  data (Appendix F.3).
- **Naive fine-tuning keeps the pretrained mechanism.** After fine-tuning on
  cue-free data with small or medium learning rates, the model stays
  linearly connected to the pretrained one and still relies on the cue;
  only a large learning rate or a perfectly correlated cue gives both a
  barrier and a changed mechanism (Fig. 5).
- **Connectivity-based fine-tuning (CBFT)** adds a loss that pushes the
  linear path to the pretrained model up to a barrier and a loss that pulls
  class-mean representations with and without the cue together. On
  CIFAR-10 with 60% cue data it drops accuracy with a randomized image from
  83.4% (medium-LR fine-tuning) to 8.75% while clean accuracy stays at 74.1%
  (Table 1).

## Standing in the record

Filed on 2026-10-03 with the owner's batch of mode-connectivity readings
([ADR-027](../decisions.d/ADR-027.md)). It is the batch's clearest statement that a barrier can mean
the two models compute different things, not only that their units are
labelled differently.

It builds on two foundations held here. From Garipov et al. ([LIT-tmpotq71](LIT-tmpotq71.md))
it takes the quadratic Bezier path, trained to low loss on a dataset, as
its non-linear connection, and its Appendix C.1 makes the point that such
a path is fitted to the data it was trained on and need not hold on
counterfactual data. From Frankle et al. ([LIT-tmp3owu9](LIT-tmp3owu9.md)) it takes linear
mode connectivity as the test, and it follows them in plotting accuracy
rather than loss along paths (Appendix C.3). It also takes the activation
matching of Git Re-Basin ([LIT-tmpd6bma](LIT-tmpd6bma.md)) to permute before interpolating, and
its Remark 1 reads Lemma 2 as a precise condition under which the
permutation conjecture of Entezari et al. ([LIT-tmp2uwzo](LIT-tmp2uwzo.md)) holds: if two
networks' activation patterns are a permutation of each other, unpermuting
them makes them linearly connected.

Across the boundary it complicates the anthology's
[ANTH-THEORY-010](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-010.md) (most of the barrier between independently trained networks
is permutation, not disagreement). This paper's barriers are disagreement
by construction: the two endpoints rely on different input attributes. That
is a different setting from two seeds on one dataset, so it does not refute
the theory, but it names the case the theory's account leaves out. Its
fine-tuning results bear on the anthology's weight-averaging practice,
which assumes a fine-tuned model is still in its parent's basin (WiSE-FT,
[ANTH-LIT-674](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-674.md); model soups, [ANTH-LIT-675](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-675.md)). The paper says so in its
conclusion, and adds that averaging can only move between mechanisms of
similar complexity.

The paper carries an instruction for practice, which is that naive
fine-tuning on clean data may not remove a spurious mechanism, so it is
flagged for the anthology.
