---
status: Active
status_note: >-
  read 2026-10-26 ([NOTE-tmpz50gz](../notes.d/NOTE-tmpz50gz.md)) in full, from the article's own page on
  the Transformer Circuits Thread; worth reading as the paper that made
  sparse-autoencoder features the field's unit of analysis below the
  neuron, for its case that a feature is a causal unit and not only a
  pattern in the data (downstream effects the autoencoder never saw), and
  for feature splitting, which makes the feature set a resolution chosen by
  dictionary size ([THEORY-tmpz7jrx](../theory.d/THEORY-tmpz7jrx.md)). Read it knowing that everything is
  one 512-neuron MLP layer of a one-layer model, that the four deep-dive
  features are cherry-picked by the authors' own account, that the human
  ratings are one author's, and that the 79% of loss recovered is measured
  against zero-ablation, a baseline the authors call an overestimate
  ([THEORY-tmpkq43g](../theory.d/THEORY-tmpkq43g.md)).
title: 'Towards Monosemanticity: Decomposing Language Models With Dictionary Learning'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read, at the owner's request of 2026-10-26 ("go ahead and
    register and read those"), after the answer to "how's the record on
    neural circuit theory?" found the record held almost none of the core
    circuits literature. Checked on 2026-10-26 against the article's own
    page (transformer-circuits.pub/2023/monosemantic-features): Trenton
    Bricken, Adly Templeton, Joshua Batson, Brian Chen, Adam Jermyn and 20
    further authors (Anthropic), "Published Oct 4, 2023", which is
    `published:` (ADR-002). There is no arXiv deposit, so the source is the
    article's URL. The summary follows the article's own summary of
    results.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmpz50gz) from the HTML of the article, fetched
    2026-10-26, its text extracted by script; the interactive figures were
    read from captions and text. Status Deferred → Active. Two accounts
    filed: THEORY-tmpkq43g (Active) and THEORY-tmpz7jrx (Proposed). The
    summary is checked against the reading and narrowed to the one-layer
    model it measured.
tags:
- representation-learning
- anthology-candidate
date: '2026-10-26'
published: '2023-10-04'
url: 'https://transformer-circuits.pub/2023/monosemantic-features/index.html'
first_author: 'Bricken'
keywords:
- 'dictionary learning'
- 'sparse autoencoders'
- 'monosemanticity'
- 'superposition'
- 'feature splitting'
- 'mechanistic interpretability'
implementations: []
summary: >-
  Bricken et al. (2023), Transformer Circuits Thread. Sparse autoencoders
  trained on 8 billion MLP activations of a one-layer transformer with 512
  ReLU neurons, at widths from 512 to 131,072, yield features that are
  rated far more interpretable than the neurons, that mostly do not
  correspond to any neuron, whose downstream effects on the logits match
  their activations, and that recur in a second model trained from another
  seed. As the dictionary widens, features split into families of finer
  ones, and the authors conclude that there may be no single correct number
  of features.
---
<!-- inactive-ok-file: THEORY-tmpz7jrx CLAIM-tmpwr001 THEORY-017 — Proposed; the account filed from this reading and the claims it bears on, cited as open -->

# LIT-tmpn9ui7: Towards Monosemanticity: Decomposing Language Models With Dictionary Learning

Bricken, T., Templeton, A., Batson, J., Chen, B., Jermyn, A., et al.
(2023). Towards monosemanticity: Decomposing language models with
dictionary learning. *Transformer Circuits Thread*, 4 October 2023.
https://transformer-circuits.pub/2023/monosemantic-features/index.html

Read in full on 2026-10-26 ([NOTE-tmpz50gz](../notes.d/NOTE-tmpz50gz.md)). Two accounts were drawn from
it: [THEORY-tmpkq43g](../theory.d/THEORY-tmpkq43g.md) and [THEORY-tmpz7jrx](../theory.d/THEORY-tmpz7jrx.md).

## Why this is here

Registered on 2026-10-26 at the owner's request, when the record was found
to hold almost none of the core circuits literature. The record had the
superposition hypothesis ([LIT-323](LIT-323.md)) and a benchmark that tests
sparse-autoencoder features as causal units ([LIT-tmprlq7z](LIT-tmprlq7z.md),
[THEORY-tmp4lqc8](../theory.d/THEORY-tmp4lqc8.md)), but not the paper that proposed those features as the unit
below the neuron. It fills that gap. It bears on [CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md) (a recovered
feature is at most a constituent), on [THEORY-018](../theory.d/THEORY-018.md) and [THEORY-017](../theory.d/THEORY-017.md) (a basis of
features is the analyst's choice), and on [QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md).
