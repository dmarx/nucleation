---
status: Active
status_note: >-
  read 2026-11-15 ([NOTE-tmp2munq](../notes.d/NOTE-tmp2munq.md)) from the arXiv preprint, v3: the main
  text, §§1–5, in full; the roughly 90-page proof appendix was skipped, so
  the theorems are carried as stated, not re-derived. Worth reading here as
  the derivation of softmax attention from an associative memory that
  [NOTE-242](../notes.d/NOTE-242.md) said the record lacked: a continuous Hopfield energy whose
  update rule ξ ← X softmax(βXᵀξ) is, at β = 1/√d_k with learned
  projections, one attention step, with proved convergence, exponential
  capacity for random patterns on a sphere and one-step retrieval of
  well-separated patterns. The venue, reported as ICLR 2021, is
  unconfirmed: neither the arXiv copy nor its record names one, and the
  registries that could confirm it refused on 2026-11-15.
title: 'Hopfield Networks is All You Need'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted continuation
    of the ChatGPT exchange "Explain String Theory", in A's turn on
    transformers as associative memories, where A says the paper
    "connects modern Hopfield retrieval with the attention update
    mechanism". Citation checked against the arXiv API: title, sixteen
    authors (Ramsauer first), v1 2020-07-16, v3 2021-04-28, no DOI, no
    journal reference, and a comment naming no venue. The ICLR 2021 venue
    that A and the citing literature give (Schlag et al.'s reference list
    has "Int. Conf. on Learning Representations (ICLR), Virtual only, May
    2021") was not confirmed in a registry: api.openreview.net raised a
    challenge (HTTP 403), OpenAlex's anonymous budget was exhausted, DBLP
    showed a bot check and Semantic Scholar returned 429, none retried. It
    is left unconfirmed. No email address was sent to any service.
    `published:` is the arXiv v1 date. Copy read: arxiv.org/pdf/2008.02217v3,
    text by pdftotext.
tags:
- representation-learning
- information-retrieval
- neuroscience
- anthology-candidate
date: '2026-11-15'
published: '2020-07-16'
arxiv: '2008.02217'
first_author: 'Ramsauer'
keywords:
- 'modern Hopfield networks'
- 'continuous states'
- 'energy function'
- 'update rule'
- 'attention mechanism'
- 'storage capacity'
- 'metastable states'
- 'Hopfield layers'
implementations: []
summary: >-
  Ramsauer et al. (2020; reported ICLR 2021, unconfirmed). A continuous
  modern Hopfield network, energy −lse(β, Xᵀξ) + ½ξᵀξ + const, whose
  update ξ ← X softmax(βXᵀξ) converges, stores exponentially many random
  patterns on a sphere and retrieves a well-separated one in one step; one
  update, through key, query and value projections at β = 1/√d_k, is
  transformer attention. Filed as the Hopfield derivation of attention that
  [NOTE-242](../notes.d/NOTE-242.md), the reading of the sparse-distributed-memory derivation
  ([LIT-269](LIT-269.md)), found missing. Bears on [THEORY-1030](../theory.d/THEORY-1030.md) by construction only (its
  HopfieldLayer is a softmax-normalized FFN memory) and, through the
  classical 0.138d capacity its introduction cites, on [QUESTION-201](../questions.d/QUESTION-201.md).
---
<!-- inactive-ok-file: THEORY-tmp7o7yb THEORY-1030 — Proposed readings, cited from the filing of Ramsauer et al. as open -->

# LIT-tmpxroua: Hopfield Networks is All You Need

Ramsauer, H., Schäfl, B., Lehner, J., Seidl, P., Widrich, M., Adler, T., Gruber, L., Holzleitner, M., Pavlović, M., Sandve, G. K., Greiff, V., Kreil, D., Kopp, M., Klambauer, G., Brandstetter, J. & Hochreiter, S. (2020). Hopfield Networks is All You Need. arXiv:2008.02217v3. Reported as ICLR 2021; the venue is unconfirmed. [ARXIV-2008.02217](https://arxiv.org/abs/2008.02217).

## Key takeaways

*From the reading, [NOTE-tmp2munq](../notes.d/NOTE-tmp2munq.md).*

- **The update rule** (§2, Eq. 3): ξ_new = X softmax(βXᵀξ), which "converges
  globally" (Theorem 1) to "stationary points (local minima or saddle
  points)" (Theorem 2).
- **Capacity** (Theorem 3): for random patterns on a sphere, the number
  that can be stored grows exponentially in d, with probability 1 − p;
  proved for stated constants at d = 20 and d = 75.
- **One-step retrieval** (Theorems 4–5): after one update the distance to a
  well-separated pattern "is exponentially small in the separation".
- **The identity** (§2, Eq. 10): "The Hopfield network update rule is the
  attention mechanism used in transformer and BERT models", at β = 1/√d_k,
  with learned projections and one update.
- **BERT heads** (§4): "predominantly in metastable states", averaging many
  patterns in the lower layers and few in the last ones, by thresholds the
  authors choose.

## Standing in the record

Filed from A's turn on transformers as associative memories. A's line,
that the paper "connects modern Hopfield retrieval with the attention
update mechanism", holds and is the paper's headline. The reader adds two
qualifications: "modern Hopfield" here is the authors' new continuous
model, and the strong results are proved for random or well-separated
patterns, not for trained keys. Nothing in A's line is wrong.

It fills the gap [NOTE-242](../notes.d/NOTE-242.md) named: the record held the sparse-distributed-
memory derivation of attention ([LIT-269](LIT-269.md), [THEORY-697](../theory.d/THEORY-697.md)) and no Hopfield one.
Hopfield (1982), [LIT-918](LIT-918.md), is its ancestor model, and the classical
capacity of "about 0.138d" that its introduction cites from other authors
is a lead for [QUESTION-201](../questions.d/QUESTION-201.md), not a reading of it. Its HopfieldLayer, with
learned stored patterns, is a softmax-normalized form of the feed-forward
memory [THEORY-1030](../theory.d/THEORY-1030.md) reads into trained FFN units; that is a construction,
not evidence that trained units act as memories. Schlag, Irie and
Schmidhuber ([LIT-tmpp9nhx](LIT-tmpp9nhx.md)) place it at the infinite-capacity end of the
scale on which linear attention sits. Its central account is
[THEORY-tmp7o7yb](../theory.d/THEORY-tmp7o7yb.md).
