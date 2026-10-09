---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpf93nl](../notes.d/NOTE-tmpf93nl.md)), in the conference version (arXiv v2); worth reading as a map of which compositions text-to-image models of 2023 get wrong and which automatic judges can tell: 6,000 prompts in six sub-categories (colour, shape and texture binding; spatial and non-spatial relations; complex), with spatial relations hardest and interactions easiest by human rating. Asking a VQA model one question per object–attribute pair ranks images far more like humans than CLIPScore does (Kendall τ 0.63 against 0.19 on colour), and detector boxes do so for spatial relations; nothing beat CLIPScore on interactions. A reward-weighted finetuning baseline (GORS) is rated best by humans, but its binding score falls sharply on attribute–noun pairs absent from its finetuning prompts (BLIP-VQA 0.55 to 0.34 on shape, 0.76 to 0.36 on texture), a gap the paper calls slight.'
title: 'T2I-CompBench: A Comprehensive Benchmark for Open-world Compositional Text-to-image Generation'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read on 2026-10-09 from arXiv v2 (30 October 2023, 25 pages), the
    conference version: main text in full; Appendices A, B, C, D.1,
    D.3, D.4 and E read, D.2, D.5 and D.6 skimmed (NOTE-tmpf93nl). v3
    was not read. The v2 PDF's first
    page carries "37th Conference on Neural Information Processing
    Systems (NeurIPS 2023) Track on Datasets and Benchmarks", which
    confirms the venue filed; the NeurIPS 2023 proceedings listing
    (papers.nips.cc) also files it under Datasets_and_Benchmarks.
    Details checked against arXiv: v1 submitted 12 July 2023, v2 30
    October 2023, v3 8 March 2025. The arXiv record now carries the
    journal version, T2I-CompBench++, whose comment says the conference version
    (T2I-CompBench, NeurIPS 2023) is v2. The title and author list here
    are the conference version's, as the manuscript cites it; the author
    list was checked against v2. `published:` is the arXiv v1 date. Not
    held in the Anthology of the SOTA as a LIT: a grep of its record/
    (clone of 2026-10-09, commit 1cffe8f) for the identifier, the title
    and the authors found the work named only in prose inside other
    entries, or not at all.
tags:
- representation-learning
- anthology-candidate
date: '2026-10-09'
published: '2023-07-12'
arxiv: '2307.06350'
first_author: 'Huang'
keywords:
- 'text-to-image'
- 'compositionality'
- 'benchmark'
- 'attribute binding'
- 'object relationships'
compared_against:
- LIT-tmpdztrs
implementations: []
summary: >-
  Huang et al. (2023). A benchmark of compositional text-to-image
  prompts in categories of attribute binding, object relationships and
  complex compositions, with category-specific automatic metrics, in
  the conference version (NeurIPS 2023 Datasets and Benchmarks).
  Disentangled BLIP-VQA and a UniDet box rule agree with human rankings
  far better than CLIPScore; spatial relations are hardest; a
  reward-weighted finetuning baseline, GORS, is rated best by humans.
---

# LIT-tmpvb4kp: T2I-CompBench: A Comprehensive Benchmark for Open-world Compositional Text-to-image Generation

Kaiyi Huang, Kaiyue Sun, Enze Xie, Zhenguo Li and Xihui Liu (2023), *NeurIPS
2023 Datasets and Benchmarks* —
[ARXIV-2307.06350](https://arxiv.org/abs/2307.06350)

## Key takeaways

Read in the conference version (arXiv v2), not the current
T2I-CompBench++.

- **Six kinds of composition, 1,000 prompts each** (Section 3). Colour,
  shape and texture binding; spatial relations (seven phrases); non-spatial
  relations (interactions); complex prompts with more objects or mixed
  attributes. Each sub-category is split 700 for training and 300 for
  testing, and the binding test sets are split again by whether the
  adjective–noun pair occurs in training. Most prompts are templated or
  written by ChatGPT from given word lists.
- **A judge per kind** (Sections 4, 6.4; Table 5). Disentangled BLIP-VQA,
  one question per object–attribute pair, ranks images like human raters
  (Kendall τ 0.63 on colour, 0.52 on texture, 0.27 on shape) where
  CLIPScore does poorly (0.19, 0.29, 0.06). A UniDet box rule does the
  same for spatial relations (0.48 against 0.27). Nothing beat CLIPScore
  on interactions (0.25). MiniGPT-4 as a judge is near zero on spatial and
  complex prompts, better with chain-of-thought prompting, never best.
- **What is hard** (Tables 2–4, human ratings). Spatial relations are
  hardest (0.31–0.46 across models), then shape binding; interactions are
  near ceiling (0.81–0.99). SD v2 beats SD v1-4 everywhere; methods built
  for binding help binding and not relations.
- **GORS** (Section 5). Finetune SD v2 with LoRA on its own generated
  images that score above a threshold, weighting the loss by the score. It
  is rated best by humans in every sub-category, and a variant selecting
  with rewards different from the evaluation metrics does about as well.
  On attribute–noun pairs absent from its 700 finetuning prompts, its
  BLIP-VQA score falls from 0.72 to 0.54 (colour), 0.55 to 0.34 (shape)
  and 0.76 to 0.36 (texture) (Table 12), which the text calls "slightly
  lower".

The record's account of compositional generalization is [THEORY-117](../theory.d/THEORY-117.md)
([LIT-667](LIT-667.md)), about classifiers trained on controlled concept grids. Table
12's gap points the same way but does not test it: the unseen pairs are
also rarer, and no model is reported on the split before finetuning
([NOTE-tmpf93nl](../notes.d/NOTE-tmpf93nl.md)). Its companion benchmark in the same track is GenEval
([LIT-tmptvh5d](LIT-tmptvh5d.md)). Among its baselines is Composable Diffusion
([LIT-tmpdztrs](LIT-tmpdztrs.md)), re-implemented on SD v2, which does worst on most
categories.

## Standing in the record

Filed on 2026-10-09 at the owner's request, as one of the works in the
reference list of the owner's working manuscript (October 2026) that the
record did not yet hold. See the curation entry of that day. It is a
machine-learning paper an anthology topic could hold (generative-modeling,
analysis-and-evaluation), so it carries the `anthology-candidate` flag
([ADR-005](../decisions.d/ADR-005.md)); it is here because the owner asked for
the manuscript's references to be filed in this record.

**After reading.** It is a benchmark, a set of evaluation metrics and a
finetuning method for text-to-image models; all three are
machine-learning practice, anthology material. The flag stays. Its primary
tag, `representation-learning`, is loose: the paper does not study how a
model represents its data, only whether its outputs match the prompt. The
closed vocabulary has no word for the evaluation of generative models,
which is an anthology subject.
