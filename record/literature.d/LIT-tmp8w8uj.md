---
status: Active
status_note: >-
  read 2026-10-26 ([NOTE-tmpfpjyr](../notes.d/NOTE-tmpfpjyr.md)) in full, from the article's own page on
  the Transformer Circuits Thread; worth reading as the demonstration that
  sparse-autoencoder features of a production model are abstract
  (multilingual, multimodal) and can steer it, for the finding that a
  concept gets its own feature only once its training frequency passes
  about one over the number of live features ([THEORY-tmplbzq5](../theory.d/THEORY-tmplbzq5.md)), and for the
  observation that the most active features are mostly not the ones that
  matter to an answer ([THEORY-tmph7ceb](../theory.d/THEORY-tmph7ceb.md)). Read it knowing that its
  interpretability and steering evidence is shown on features the authors
  selected, that the model, its size and some plot units are withheld, that
  the reconstructions explain only at least 65% of the variance, and that
  its wider thesis that these features are the model's working concepts is
  open ([THEORY-tmp14ee2](../theory.d/THEORY-tmp14ee2.md)).
title: 'Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read, at the owner's request of 2026-10-26 ("go ahead and
    register and read those"), after the answer to "how's the record on
    neural circuit theory?" found the record held almost none of the core
    circuits literature. Checked on 2026-10-26 against the article's own
    page (transformer-circuits.pub/2024/scaling-monosemanticity): Adly
    Templeton, Tom Conerly, Jonathan Marcus, Jack Lindsey and 22 further
    authors (Anthropic), "Published May 21, 2024", which is `published:`
    (ADR-002). There is no arXiv deposit, so the source is the article's
    URL. The summary follows the article's key results.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmpfpjyr) from the HTML of the article, fetched
    2026-10-26, its text extracted by script; the figures, which are
    interactive or images, were read from captions and text. Status
    Deferred → Active. Three accounts filed: THEORY-tmph7ceb and
    THEORY-tmplbzq5 (Active) and THEORY-tmp14ee2 (Proposed). The summary
    is checked against the reading and given the site (the middle-layer
    residual stream) and the variance figure.
tags:
- representation-learning
- anthology-candidate
date: '2026-10-26'
published: '2024-05-21'
url: 'https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html'
first_author: 'Templeton'
keywords:
- 'sparse autoencoders'
- 'dictionary learning'
- 'scaling laws'
- 'feature steering'
- 'monosemanticity'
- 'mechanistic interpretability'
implementations: []
summary: >-
  Templeton et al. (2024), Transformer Circuits Thread. Sparse autoencoders
  of about 1M, 4M and 34M features, sized by scaling laws for the
  autoencoder's own loss, are trained on the middle-layer residual stream
  of Claude 3 Sonnet and explain at least 65% of its variance. They yield
  features that respond to the same concept across languages and in images,
  that steer the model when clamped, and that include features for unsafe
  code, bias, sycophancy and deception. Whether a concept has its own
  feature depends on its training frequency relative to the dictionary's
  size.
---
<!-- inactive-ok-file: THEORY-tmp14ee2 CLAIM-tmpwr001 — Proposed; the account filed from this reading and the claim it bears on, cited as open -->

# LIT-tmp8w8uj: Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet

Templeton, A., Conerly, T., Marcus, J., Lindsey, J., et al. (2024).
Scaling monosemanticity: Extracting interpretable features from Claude 3
Sonnet. *Transformer Circuits Thread*, 21 May 2024.
https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html

Read in full on 2026-10-26 ([NOTE-tmpfpjyr](../notes.d/NOTE-tmpfpjyr.md)). Three accounts were drawn from
it: [THEORY-tmph7ceb](../theory.d/THEORY-tmph7ceb.md), [THEORY-tmplbzq5](../theory.d/THEORY-tmplbzq5.md) and [THEORY-tmp14ee2](../theory.d/THEORY-tmp14ee2.md).

## Why this is here

Registered on 2026-10-26 at the owner's request, when the record was found
to hold almost none of the core circuits literature. It is the scaling of
Bricken et al.'s method ([LIT-tmpn9ui7](LIT-tmpn9ui7.md)) to a production model, and the
work most often cited for the view that sparse-autoencoder features are a
large model's concepts. The record held the contrary evidence first: in
MIB ([LIT-tmprlq7z](LIT-tmprlq7z.md), [THEORY-tmp4lqc8](../theory.d/THEORY-tmp4lqc8.md)) such features localize known causal
variables worse than neurons. It bears on [CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md), on
[QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md), and on the record's Gemma Scope reading ([LIT-611](LIT-611.md),
[THEORY-504](../theory.d/THEORY-504.md)) about residual-stream autoencoders.
