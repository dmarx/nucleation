---
status: Proposed
status_note: 'read in full 2026-09-30 ([NOTE-tmpio60n](../notes.d/NOTE-tmpio60n.md)); a compact, readable demonstration that an early, short chaotic phase gives way to a confined, stable one in both basin and kernel terms, but it rests on two architectures on one dataset, one run each with no error bars. The chaos half largely re-measures Frankle et al.''s (2020) spawning / linear-mode-connectivity result with a parameter perturbation in place of fresh SGD noise, and the claimed role of the cone in generalisation is asserted. What would settle it: seeds and error bars, the batch size, a stated perturbation norm, other domains, and a quantitative test of confinement (e.g. an angular radius that stops growing) rather than a 3-D picture.'
title: 'New Evidence of the Two-Phase Learning Dynamics of Neural Networks'
version: 2
history:
- version: 2
  date: '2026-09-30'
  note: >-
    Read in full (Full text of arXiv 2505.13900 v1 (20 May 2025, the only
    version; marked "Preprint. Under review."; it extends the authors' ICLR
    2025 DeLTa workshop paper "On the Cone Effect in the Learning Dynamics",
    which was not read), 11 pp., from the arXiv PDF. Read all of it:
    abstract, §§1–6 (including the Limitations paragraph) and the
    references. There are no appendices. Text was extracted with PyMuPDF.
    Pages 2 and 5–8 were rendered and Figs. 1 and 3–6 read from the images,
    because the results are carried almost entirely by heatmaps and curves.
    Not held in the Anthology of the SOTA: a grep of its literature.d for
    the arXiv id, the title and "cone effect" found nothing. `published:` is
    the arXiv v1 date.); the first NOTE on it, since it was seeded from the
    abstract alone. Status set from the reading: Proposed.
tags:
- learning-theory
- anthology-candidate
date: '2026-09-30'
published: '2025-05-20'
arxiv: '2505.13900'
first_author: 'Zhou'
keywords:
- 'training phases'
implementations: []
summary: >-
  Zhou et al. (2025), arXiv:2505.13900. VGG-16 and ResNet-20 on CIFAR-10
  (SGD with momentum, lr 0.1, 160 epochs) are compared across pairs of
  training times. Before an early "inflection point" (~2,500 iterations
  for VGG-16, ~100–500 for ResNet-20), a tiny parameter perturbation under
  identical SGD noise sends the run to a different basin by the end: loss
  barrier up to ~2, test disagreement ~0.15–0.5. After it, the same
  perturbation leaves the runs linearly connected. Also after it, the
  empirical NTK keeps changing step to step but stays within a bounded
  cosine distance of any later reference kernel (the "cone effect", e.g. S
  ≈ 0.05–0.1 for VGG-16 vs ≈ 0.15–0.2 from initialisation). Switching to
  linearised training later gives better test accuracy (VGG-16 0.13 → 0.82
  as the switch moves from ≤200 to 5,000 iterations).
---

# LIT-tmp9va7v: New Evidence of the Two-Phase Learning Dynamics of Neural Networks

Zhou et al. (2025), *arXiv preprint (v1 only; marked "Preprint. Under review."); extends the ICLR 2025 Workshop DeLTa paper "On the Cone Effect in the Learning Dynamics" (not read)* — arXiv:2505.13900

## Standing in the record

Filed on 2026-09-30 at the owner's request, as evidence on phases of training: whether they corroborate the
information-bottleneck account of a fitting then a compression phase ([LIT-324](LIT-324.md)), and what phase structure they show.
`published:` is the first appearance ([ADR-002](../decisions.d/ADR-002.md)).

It was filed `Deferred`, unread. [NOTE-tmpio60n](../notes.d/NOTE-tmpio60n.md) is the close reading of 2026-09-30, and it placed the work: **Proposed** — a compact, readable demonstration that an early, short chaotic phase gives way to a confined, stable one in both basin and kernel terms, but it rests on two architectures on one dataset, one run each with no error bars. The chaos half largely re-measures Frankle et al.'s (2020) spawning / linear-mode-connectivity result with a parameter perturbation in place of fresh SGD noise, and the claimed role of the cone in generalisation is asserted. What would settle it: seeds and error bars, the batch size, a stated perturbation norm, other domains, and a quantitative test of confinement (e.g. an angular radius that stops growing) rather than a 3-D picture.
