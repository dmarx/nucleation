---
status: Deferred
status_note: 'registered 2026-10-09 from arXiv, not read: only the abstract was seen. Filed from the reference list of the owner''s working manuscript. It stays Deferred until somebody reads it, not on merit.'
title: 'Compositional Visual Generation with Composable Diffusion Models'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Registered, not read. Details checked against arXiv (v1 submitted 3
    June 2022, ECCV 2022 per the comment; first three authors equal).
    `published:` is the arXiv v1 date. Not held in the Anthology of the
    SOTA as a LIT: a grep of its record/ (clone of 2026-10-09, commit
    1cffe8f) for the identifier, the title and the authors found the
    work named only in prose inside other entries, or not at all.
tags:
- probabilistic-modeling
- representation-learning
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
  that a single text-conditioned model confuses. Unread.
---

# LIT-tmpdztrs: Compositional Visual Generation with Composable Diffusion Models

Nan Liu, Shuang Li, Yilun Du, Antonio Torralba and Joshua B. Tenenbaum (2022),
*ECCV 2022* — [ARXIV-2206.01714](https://arxiv.org/abs/2206.01714)

## Key takeaways

*Registered, not read.* From the abstract only: large text-guided diffusion
models confuse the attributes of different objects and the relations between
them. Interpreting diffusion models as energy-based models, the paper composes
a set of diffusion models, each modelling one component of the image, by
combining their energy functions. The composition generates scenes
substantially more complex than those seen in training, composes sentence
descriptions, relations and facial attributes, and applies to pre-trained
text-guided models. The record's reading of compositional generalization in
vision models is [LIT-667](LIT-667.md).

## Standing in the record

Filed on 2026-10-09 at the owner's request, as one of the works in the
reference list of the owner's working manuscript (October 2026) that the
record did not yet hold. See the curation entry of that day. It is a
machine-learning paper an anthology topic could hold (generative-modeling,
analysis-and-evaluation), so it carries the `anthology-candidate` flag
([ADR-005](../decisions.d/ADR-005.md)); it is here because the owner asked for
the manuscript's references to be filed in this record.
