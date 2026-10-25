---
status: Deferred
status_note: >-
  filed 2026-10-25, not read. Registered as prior art for turns U45 and
  U46 of the owner's exchange of 2026-10-24/25, which did not cite it; the
  record's reading of those turns named it. No NOTE is filed.
title: 'MultiDiffusion: Fusing Diffusion Paths for Controlled Image Generation'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed, not read. The exchange (the continuation of "Review PR 327
    Improvements", shared at
    https://chatgpt.com/share/6add7ae3-1a38-83ea-ac83-4f490e399824) built
    at U45 a population of perspectives that propose denoising steps over
    a common latent within spatial jurisdictions, and did not cite this
    work; the record's reading of those turns named it from memory as the
    nearest prior art, and the lookup confirmed it. Checked on 2026-10-25
    against the arXiv record: Omer Bar-Tal, Lior Yariv, Yaron Lipman and
    Tali Dekel, arXiv 2302.08113, v1 submitted 16 February 2023, which is
    `published:`. Published at ICML 2023, PMLR 202: 1737–1752 (proceedings
    page, 3 July 2023). The summary follows the arXiv abstract.
tags:
- compositionality
- probabilistic-modeling
- anthology-candidate
date: '2026-10-25'
published: '2023-02-16'
arxiv: '2302.08113'
first_author: 'Bar-Tal'
keywords:
- 'MultiDiffusion'
- 'text-to-image diffusion'
- 'controllable generation'
- 'fusing diffusion paths'
- 'region-based generation'
- 'panorama'
implementations: []
summary: >-
  Bar-Tal, Yariv, Lipman & Dekel (2023). MultiDiffusion is a training-free
  generation process for a pre-trained text-to-image diffusion model that
  binds several diffusion generation processes together through an
  optimization task with shared parameters or constraints. It gives
  controllable generation, such as panoramas at a chosen aspect ratio and
  images following spatial guidance from segmentation masks to bounding
  boxes, without retraining or fine-tuning (abstract).
---
# LIT-tmp03agp: MultiDiffusion: Fusing Diffusion Paths for Controlled Image Generation

Bar-Tal, O., Yariv, L., Lipman, Y. & Dekel, T. (2023). MultiDiffusion:
Fusing diffusion paths for controlled image generation. *Proceedings of
the 40th International Conference on Machine Learning*, PMLR 202:
1737–1752. arXiv:2302.08113.

Not read. The summary is drawn from the abstract or from what the work
is standardly cited for. A reading should check it first.

## Why this is here

Filed as prior art the exchange did not name. At U45 the reply built a
population of perspectives, each proposing a denoising step within a
spatial jurisdiction over one shared latent, and presented combining their
noise predictions as new. Fusing several masked diffusion processes into
one image is this paper's method; the record already holds the composition
of noise predictions by concept, without masks, in Liu et al. ([LIT-770](LIT-770.md),
[THEORY-405](../theory.d/THEORY-405.md)) and classifier-free guidance ([LIT-839](LIT-839.md), [THEORY-611](../theory.d/THEORY-611.md)). It bears
on {{F-Q-INFL}}, whose geometric neighbourhoods and population of
denoisers are the exchange's mechanisms of influence. Filed for the
record's question about influence over a shared representation, not as an
instruction for practice.
