---
status: Active
status_note: >-
  read 2026-11-15 ([NOTE-tmpss2fb](../notes.d/NOTE-tmpss2fb.md)) from the arXiv preprint, v3, which
  carries the ICML 2021 proceedings footer: the main text, §§1–6, in full,
  appendices A–F skipped. Worth reading here for three things: the
  equivalence, apart from normalisation, of linear attention with an
  outer-product fast weight programmer whose memory is the running sum of
  v ⊗ φ(k); the capacity limit that follows, no more than d_dot
  associations without crosstalk, shown on synthetic retrieval; and the
  delta-rule write with a learned rate β that replaces the additive one,
  which defines the delta-rule layer [QUESTION-159](../questions.d/QUESTION-159.md) names.
title: 'Linear Transformers Are Secretly Fast Weight Programmers'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted continuation
    of the ChatGPT exchange "Explain String Theory", in A's turn on
    transformers as associative memories, where A says the paper
    "establishes an equivalence between linearized attention and certain
    fast-weight memory systems". Citation checked against the arXiv API:
    title, Schlag, Irie and Schmidhuber (Schlag and Irie equal), v1
    2021-02-22, v3 2021-06-09, no DOI. The venue, ICML 2021 (PMLR 139),
    is from the PDF's own footer, "Proceedings of the 38th International
    Conference on Machine Learning"; OpenAlex, DBLP and Semantic Scholar
    refused on 2026-11-15 and were not retried, so it is not confirmed in
    a registry. No email address was sent to any service. `published:` is
    the arXiv v1 date. Copy read: arxiv.org/pdf/2102.11174v3, text by
    pdftotext.
tags:
- representation-learning
- learning-theory
- information-retrieval
- anthology-candidate
date: '2026-11-15'
published: '2021-02-22'
arxiv: '2102.11174'
first_author: 'Schlag'
keywords:
- 'fast weight programmers'
- 'linear transformers'
- 'linear attention'
- 'outer product'
- 'memory capacity'
- 'delta rule'
- 'deterministic parameter-free projection'
implementations: []
summary: >-
  Schlag, Irie & Schmidhuber (ICML 2021). Causal attention without softmax,
  or with a kernel φ, computes what an outer-product fast weight programmer
  computes, apart from normalisation: a fast weight matrix summing v ⊗ φ(k),
  read by the query. Hence a limit of d_dot associations before crosstalk,
  shown on synthetic retrieval, and a delta-rule write with a learned rate
  β that helps in an overcapacity regime. Filed for [QUESTION-159](../questions.d/QUESTION-159.md), whose
  delta-rule layers it defines; it sits beside [THEORY-169](../theory.d/THEORY-169.md)'s identities and
  the readings that rest on it ([LIT-792](LIT-792.md), [LIT-801](LIT-801.md)), and gives [THEORY-1030](../theory.d/THEORY-1030.md)'s
  memory form a lineage, by algebra only.
---
<!-- inactive-ok-file: THEORY-tmp36vfv THEORY-1030 — Proposed readings, cited from the filing of Schlag et al. as open -->

# LIT-tmpp9nhx: Linear Transformers Are Secretly Fast Weight Programmers

Schlag, I., Irie, K. & Schmidhuber, J. (2021). Linear Transformers Are Secretly Fast Weight Programmers. *Proceedings of the 38th International Conference on Machine Learning*, PMLR 139. arXiv:2102.11174v3. [ARXIV-2102.11174](https://arxiv.org/abs/2102.11174).

## Key takeaways

*From the reading, [NOTE-tmpss2fb](../notes.d/NOTE-tmpss2fb.md).*

- **The equivalence** (§3): with softmax removed, causal self-attention is
  a fast weight programmer, W(i) = W(i−1) + v(i) ⊗ k(i), y(i) = W(i) q(i);
  with a kernel φ and its normaliser, it is "a Fast Weight Programmer
  (Sec. 2) with normalisation". The derivation is reviewed from
  Katharopoulos et al. (2020) and Ba et al. (2016), not originated.
- **Capacity** (§4.1): "there cannot be more than ddot orthogonal vectors",
  so storing more than d_dot associations "will result in a retrieval
  error"; on synthetic retrieval linear attention "begins to accumulate
  errors with 60 or more associations" at d_dot = 64 (§6.1.1).
- **The delta rule** (§4.2, Eq. 24): W(i) = W(i−1) + β(i)(v(i) − v̄(i)) ⊗
  φ(k(i)), where v̄(i) is the value currently retrieved for k(i); it "is
  effectively a delta rule with a dynamic learning rate".
- **In use** (§6.3): on WikiText-103 in a deliberately overcapacity
  configuration, the delta rule lowers the small Linear Transformer's test
  perplexity from 38.3 to 35.5; softmax attention scores 34.1.

## Standing in the record

Filed from A's turn on transformers as associative memories. A's line
holds: the paper states and derives the equivalence, and the memory is a
running sum of outer products. The reader qualifies it three ways. The
equivalence is "apart from normalisation"; its derivation restates earlier
work, and the paper's own contributions (the capacity argument, the delta
rule, the DPFP feature map) are what A leaves out; and the paper's point is
that the purely additive write is a weakness.

Its bearing is on [QUESTION-159](../questions.d/QUESTION-159.md), which asks whether an exact
train-then-predict identity holds for delta-rule layers: this paper
defines that layer, and does not state such an identity. It is the source
of the identity that the record's readings of von Oswald et al. ([LIT-792](LIT-792.md),
[NOTE-621](../notes.d/NOTE-621.md)) and of TTT ([LIT-801](LIT-801.md), [NOTE-620](../notes.d/NOTE-620.md)) use. With Ramsauer et al.
([LIT-tmpxroua](LIT-tmpxroua.md)) it places linear and softmax attention on one scale of
memory capacity. Its memory is written from the context during the forward
pass, so it shares only the algebraic form with [THEORY-1030](../theory.d/THEORY-1030.md)'s memory in
trained FFN weights. Its central account is [THEORY-tmp36vfv](../theory.d/THEORY-tmp36vfv.md).
