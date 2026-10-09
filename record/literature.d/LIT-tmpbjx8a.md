---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmputb6d](../notes.d/NOTE-tmputb6d.md)); worth reading as the paper that names "catastrophic neglect" (a text-to-image model omits one of the subjects a prompt names) and links it to attribute binding: the subject token that no image patch attends to is the one that goes missing. Its fix is an inference-time correction of the latent: push up the maximum cross-attention of the most neglected subject token, smoothed over neighbouring patches, during the first half of sampling. Evidence is on 276 two-subject Stable Diffusion prompts, by CLIP similarities, BLIP captions and a 65-person preference study (77–91% preferred it). That it improves attribute binding is shown only in figures; no binding accuracy is measured, and relations are left out of scope.'
title: 'Attend-and-Excite: Attention-Based Semantic Guidance for Text-to-Image Diffusion Models'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read on 2026-10-09 (NOTE-tmputb6d) from arXiv v2 (31 May 2023, 24
    pages, the SIGGRAPH 2023 version): main text in full, Appendices A
    and B read, Appendix C.1 read in part and C.2–C.4 skimmed for their
    tables, figure pages skimmed. Details checked against arXiv (v1 submitted 31 January 2023;
    the comment says accepted to SIGGRAPH 2023) and Crossref (ACM
    Transactions on Graphics 42(4), pp. 1–10, DOI 10.1145/3592116,
    published online 26 July 2023, print August 2023). `published:` is
    the arXiv v1
    date. Not held in the Anthology of the SOTA: a grep of its record/
    (clone of 2026-10-09, commit d8b5ba5) for the authors, the
    identifier, the DOI and the title found nothing.
tags:
- compositionality
- anthology-candidate
date: '2026-10-09'
published: '2023-01-31'
arxiv: '2301.13826'
first_author: 'Chefer'
keywords:
- 'text-to-image generation'
- 'diffusion models'
- 'cross-attention'
- 'catastrophic neglect'
- 'attribute binding'
- 'generative semantic nursing'
implementations: []
compared_against:
- LIT-770
- LIT-tmp76md3
summary: >-
  Chefer et al. (2023), ACM TOG 42(4) (SIGGRAPH 2023). Stable Diffusion
  often omits one of two named subjects ("catastrophic neglect") and
  misbinds attributes. Shifting the latent at each early denoising step
  to raise the peak cross-attention of the most neglected subject token
  mitigates neglect, by CLIP and caption similarity and by human
  preference, with no training. Binding gains are shown in figures, not
  measured.
---

# LIT-tmpbjx8a: Attend-and-Excite: Attention-Based Semantic Guidance for Text-to-Image Diffusion Models

Hila Chefer, Yuval Alaluf, Yael Vinker, Lior Wolf and Daniel Cohen-Or
(2023), *ACM Transactions on Graphics* 42(4) (SIGGRAPH 2023) —
[ARXIV-2301.13826](https://arxiv.org/abs/2301.13826)

## Key takeaways

- **Two failures, one cause** (Section 1, Fig. 2). In Stable Diffusion,
  "catastrophic neglect": one or more subjects of the prompt are not
  generated; and "incorrect attribute binding": an attribute lands on the
  wrong subject or on none. The authors' account: the CLIP text encoder
  already mixes "blue" into the token "cat", so making the cat appear
  should also carry its colour.
- **The mechanism** (Section 4, Algorithm 1). Cross-attention gives each
  16×16 image patch a distribution over prompt tokens. Nothing makes every
  token dominant somewhere. At each of the first 25 of 50 steps, the loss
  L = max over subject tokens of (1 − max over patches of the
  Gaussian-smoothed attention map) is reduced by one gradient step on the
  latent; at steps 0, 10 and 20 the step is repeated until each subject
  reaches attention 0.05, 0.5 and 0.8. Without smoothing, one patch can
  satisfy the loss with a fragment (a crown-like patch on a rabbit's head;
  Appendix B).
- **The evidence** (Section 5). 276 prompts of three templates (two
  animals; an animal and a coloured object; two coloured objects), 64
  seeds each, against Stable Diffusion, Composable Diffusion and
  StructureDiffusion. Minimum per-subject CLIP similarity beats Stable
  Diffusion and StructureDiffusion by at least 7%; BLIP-caption
  similarity to the prompt beats all three by at least 4.7% (Table 1); in a 65-respondent study it is preferred 90.7%, 77.6% and
  77.2% of the time on the three subsets (Table 2). Composable Diffusion
  tends to fuse the two subjects into one object, which CLIP image–text
  similarity rewards and caption similarity does not.
- **What is not shown.** Binding is not measured: the improvements in
  colour binding are seen in figures. Relations ("riding on", "in front
  of", "beneath") are stated as out of scope.

## Standing in the record

Filed on 2026-10-09 from the manuscript bibliography of 2026-10-09 (work
`what-survives-translation`) at the owner's request: the manuscript
considered it and dropped it from the final reference list. It is read here
on its own merits. See the curation entry of that day.

It is a machine-learning paper an anthology topic could hold (an
inference-time method for text-to-image models), so it carries the
`anthology-candidate` flag ([ADR-005](../decisions.d/ADR-005.md)). It is filed under `compositionality`,
the subject it shares with this record: whether every part of a prompt
reaches the image, and whether the parts stay bound. The later benchmark
T2I-CompBench ([LIT-783](LIT-783.md)) and its journal version ([LIT-tmp76md3](LIT-tmp76md3.md)) measure it
re-implemented on Stable Diffusion v2, where it is the strongest of the
2022–2023 training-free methods on colour and texture binding and does not
help relations.
