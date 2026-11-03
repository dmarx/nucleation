---
status: Active
status_note: >-
  read in full 2026-11-03 ([NOTE-tmp2mbd7](../notes.d/NOTE-tmp2mbd7.md)), from arXiv v7; worth
  reading as the source of query–key–value attention, whose
  factorization into compatibility weights and transported values is
  the structure [TERM-064](../terms.d/TERM-064.md)'s note of 2026-11-02 compares to legibility.
  The QK/OV vocabulary is Elhage et al.'s, not this paper's.
title: 'Attention Is All You Need'
version: 2
history:
- version: 1
  date: '2026-11-02'
  note: >-
    Filed, not read. Citation checked against the arXiv API on 2026-11-02
    (v1 submitted 2017-06-12). The summary says why it is here, not what it
    shows.
- version: 2
  date: '2026-11-03'
  note: >-
    Read in full from arXiv:1706.03762v7 (2 August 2023), 15 pp.;
    the first NOTE on the work (NOTE-tmp2mbd7). Status set from the
    reading: Active. The summary is replaced by one from the text.
    v7 gives the English–French result as 41.8 BLEU in the abstract
    and Table 2 and 41.0 in §6.1. One THEORY is filed from it
    (THEORY-tmpu6kk8).
tags:
- representation-learning
- anthology-candidate
date: '2026-11-02'
published: '2017-06-12'
arxiv: '1706.03762'
first_author: 'Vaswani'
keywords:
- 'transformer'
- 'attention'
- 'query key value'
implementations: []
summary: >-
  Vaswani et al. (2017), arXiv:1706.03762; NeurIPS 2017. The
  Transformer, an encoder–decoder built only from multi-head scaled
  dot-product attention, position-wise feed-forward layers and
  sinusoidal position encodings. Attention maps a query and key–value
  pairs to a weighted sum of the values, the weights set by query–key
  compatibility, softmax(QKᵀ/√d_k)V; several heads attend to different
  subspaces. It reached 28.4 BLEU on WMT 2014 English–German and 41.8
  on English–French at a fraction of earlier training cost, and
  transferred to constituency parsing.
---

# LIT-tmp91wxa: Attention Is All You Need

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., et al. (2017). Attention Is All You Need. *arXiv preprint; NeurIPS 2017*. arXiv:1706.03762.

Read in full on 2026-11-03 ([NOTE-tmp2mbd7](../notes.d/NOTE-tmp2mbd7.md); [THEORY-tmpu6kk8](../theory.d/THEORY-tmpu6kk8.md)).

## Key takeaways

- Attention(Q, K, V) = softmax(QKᵀ/√d_k)V: which positions are read is set
  by queries and keys, what is read by values (pp. 3–4).
- Multiple heads because one head's convex averaging cannot attend to
  several subspaces at once (p. 5).
- Its training recipes are practice, the anthology's.

## Standing in the record

The source of query–key–value attention, the other side of the owner's U23 analogy. The record holds the QK/OV analysis of it ([LIT-1534](LIT-1534.md), [THEORY-988](../theory.d/THEORY-988.md)) but not the paper.
