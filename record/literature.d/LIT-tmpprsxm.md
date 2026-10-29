---
status: Active
status_note: >-
  read in full 2026-10-29 (NOTE-tmpgvlkv); worth reading as the cleanest
  statement of correspondence recovered from within-space relations
  alone, and for what that costs: the objective cannot tell a
  correspondence from one composed with a symmetry of either space
  (THEORY-tmpa43ta), which the paper does not say.
title: 'Gromov-Wasserstein Alignment of Word Embedding Spaces'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed, not read, from A5, A6 of the exchange "Paper assessment"
    (2026-10-28 to 29). `published:` is arXiv v1 2018-08-31 (EMNLP 2018,
    doi 10.18653/v1/D18-1214) (ADR-002).
- version: 2
  date: '2026-10-29'
  note: >-
    Read in full from the arXiv preprint 1809.00013v1, 10 pp., in
    NOTE-tmpgvlkv; status Deferred → Active. The citation stands. The
    summary is rewritten from the text. Tagged anthology-candidate
    (ADR-005): the paper carries instructions for ML practice
    (normalise the cost matrices, use cosine, two values of λ).
tags:
- translation
- mathematics
- representation-learning
- anthology-candidate
date: '2026-10-29'
published: '2018-08-31'
arxiv: '1809.00013'
first_author: 'Alvarez-Melis'
keywords:
- 'optimal transport'
- 'Gromov-Wasserstein distance'
- 'word embeddings'
- 'unsupervised word translation'
- 'cross-lingual alignment'
implementations: []
summary: >-
  Alvarez-Melis & Jaakkola (2018). Casts unsupervised word translation
  as a Gromov–Wasserstein problem between the two languages'
  within-language cosine-similarity matrices, solved by entropic
  projected gradient with no anchors, and reads the optimal coupling as
  the translation. It matches adversarial-plus-refinement methods on
  related languages trained on comparable Wikipedia corpora (P@1 72–82)
  at about 4% of their CPU time, and does markedly worse on
  English–Russian (45) and English–Finnish (18). The objective sees only
  within-space relations, so it is unchanged by a rotation of either
  space and cannot distinguish couplings that differ by a symmetry of
  the data.
---

# LIT-tmpprsxm: Gromov-Wasserstein Alignment of Word Embedding Spaces

Alvarez-Melis, D., & Jaakkola, T. S. (2018). Gromov-Wasserstein alignment of word embedding spaces. *Proceedings of EMNLP 2018*, 1881–1890.

Read in full in NOTE-tmpgvlkv.

## Why this is here

The centre of A6: correspondence recovered from the relations elements bear to one another, without a shared coordinate system. That is the structuralist reading of [CLAIM-046](../claims.d/CLAIM-046.md) and [CLAIM-113](../claims.d/CLAIM-113.md) in computational form. A6 also gave its limit, kept here: GW finds relational resemblance under a chosen metric, which is not communicative identity ([CLAIM-135](../claims.d/CLAIM-135.md)). Read with [LIT-tmpqoytq](LIT-tmpqoytq.md). The reading bears A6's limit out and sharpens it: the relational resemblance is resemblance up to the symmetries of the similarity structure, so on symmetric data even a perfect fit leaves the correspondence open (THEORY-tmpa43ta). Against the paper's own claim (p. 9), GW does not dispense with an invariance assumption; under cosine similarity it builds in invariance to every rotation and rescaling of either space.
