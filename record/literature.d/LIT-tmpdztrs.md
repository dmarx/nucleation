---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpq1itu](../notes.d/NOTE-tmpq1itu.md)); worth reading as the paper that moved compositional energy-based generation onto diffusion models: reading a diffusion model''s noise prediction as an energy gradient, concepts are composed at sampling time by adding one classifier-free-guidance term per concept (AND) or subtracting a concept''s prediction (NOT), with no retraining. The product-of-experts reading is exact only for conditionally independent concepts, unit weights and a conservative score, and is derived at zero noise but applied at every noise level. It wins clearly on composing CLEVR object positions (31.36% against an EBM''s 7.34% at three objects), not on relations (2.80% against 4.26%), and is shown on GLIDE and Stable Diffusion only qualitatively.'
title: 'Compositional Visual Generation with Composable Diffusion Models'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from arXiv v6 (17 January 2023, 30 pages), the latest version:
    main text in full, Appendix F (derivations) read, Appendices A–E read
    for setup, figure pages skimmed (NOTE-tmpq1itu). Details checked
    against arXiv (v1 submitted 3
    June 2022, ECCV 2022 per the comment; first three authors equal).
    `published:` is the arXiv v1 date. Not held in the Anthology of the
    SOTA as a LIT: a grep of its record/ (clone of 2026-10-09, commit
    1cffe8f) for the identifier, the title and the authors found the
    work named only in prose inside other entries, or not at all.
tags:
- compositionality
- probabilistic-modeling
- anthology-candidate
date: '2026-10-09'
published: '2022-06-03'
arxiv: '2206.01714'
first_author: 'Liu'
keywords:
- 'compositional generation'
- 'diffusion models'
- 'energy-based models'
- 'product of experts'
- 'attribute binding'
implementations: []
summary: >-
  Liu, Li, Du, Torralba & Tenenbaum (2022), ECCV. Reading diffusion
  models as energy-based models lets several of them be combined at
  sampling time, as conjunctions and negations of concepts, generating
  scenes more complex than any seen in training and binding attributes
  that a single text-conditioned model confuses. Read: strong on object
  positions in CLEVR, weak on relations, qualitative on text models.
compared_against:
- LIT-tmpvb4kp
---

# LIT-tmpdztrs: Compositional Visual Generation with Composable Diffusion Models

Nan Liu, Shuang Li, Yilun Du, Antonio Torralba and Joshua B. Tenenbaum (2022),
*ECCV 2022* — [ARXIV-2206.01714](https://arxiv.org/abs/2206.01714)

## Key takeaways

- **Composition by adding scores.** A diffusion model's noise prediction is
  read as the gradient of an energy, so a product of densities is a sum of
  predictions. Conjunction is ε(x,t) + Σᵢ wᵢ(ε(x,t|cᵢ) − ε(x,t)), the
  score of p(x)Πᵢ p(x|cᵢ)/p(x) when the concepts are conditionally
  independent given the image; with one concept it is classifier-free
  guidance. Negation divides by the negated concept's likelihood:
  ε(x,t) + w(ε(x,t|cᵢ) − ε(x,t|c̃ⱼ)). No retraining (Section 4,
  Appendix F).
- **Heuristic, not exact.** The learned field need not be conservative
  (set aside by citation), the weights are tuned, all terms must come from
  the same network, and the product rule is derived for the data
  distribution but used at every noise level, which the paper does not
  discuss.
- **Results.** CLEVR object positions, accuracy at one, two and three
  composed positions: 86.42, 59.20 and 31.36%, against the EBM baseline's
  70.54, 28.22 and 7.34%, with the best FID throughout (Table 1).
  Relations: 60.40, 21.84 and 2.80%, below the EBM's 78.14, 24.16 and
  4.26%, though with better FID (Table 2). FFHQ attributes: below LACE in
  accuracy at three attributes (68.86 against 80.88%), best FID (Table 3).
  Composed GLIDE and Stable Diffusion are shown in figures only.
- **Failure modes** the authors list: concepts the base model does not
  know, attribute confusion that composition does not cure, and fusion of
  two objects into one hybrid when objects are centred.

The record's reading of compositional generalization in recognition is
[LIT-667](LIT-667.md) and [THEORY-117](../theory.d/THEORY-117.md); the reading of this paper sets the two side
by side ([NOTE-tmpq1itu](../notes.d/NOTE-tmpq1itu.md)).

## Standing in the record

Filed on 2026-10-09 at the owner's request, as one of the works in the
reference list of the owner's working manuscript (October 2026) that the
record did not yet hold. See the curation entry of that day. It is a
machine-learning paper an anthology topic could hold (generative-modeling,
analysis-and-evaluation), so it carries the `anthology-candidate` flag
([ADR-005](../decisions.d/ADR-005.md)); it is here because the owner asked for
the manuscript's references to be filed in this record.
