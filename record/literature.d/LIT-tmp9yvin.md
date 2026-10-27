---
status: Active
status_note: >-
  read 2026-10-27 (NOTE-tmp8m63d) in full, from arXiv v4; worth reading as
  the source of the toy model the causal scrubbing appendix (LIT-1583, §6)
  analyses, and as an exactly solvable case of superposition: in a
  one-hidden-layer model with quadratic activations, the expected loss
  depends on the weights only through each feature's capacity and
  embedding length, and the optimal allocation has a closed form in which
  features are ignored, shared or given a whole dimension according to
  their importance and the inputs' fourth moment (THEORY-tmp68zar,
  re-derived and checked numerically). Read it knowing that its other
  models are shown only as phase-diagram figures, and that its bearing on
  trained networks is the authors' hope, not a result (THEORY-tmp2tsxo).
title: 'Polysemanticity and Capacity in Neural Networks'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read, at the owner's request of 2026-10-27 ("file the next
    readings"), one of the works the circuits readings merged in
    dmarx/nucleation#338 named and did not register (the curation entry
    of 2026-10-27 02:06, "Named by the readings, not registered"): the
    causal scrubbing appendix (LIT-1583, NOTE-1202) says in §6 "In our
    polysemanticity toy model paper, we introduced an analytically
    tractable setting", without naming it. The appendix's HTML (fetched
    by the reading of LIT-1583) links those words to the Alignment Forum
    post kWp4R9SYgKJFHAufB, "Polysemanticity and Capacity in Neural
    Networks", posted 2022-10-07 by Buck Shlegeris, which announces "an
    Arxiv paper" of that title; it is arXiv 2210.01892, by Adam Scherlis,
    Kshitij Sachan, Adam S. Jermyn, Joe Benton and Buck Shlegeris
    (Redwood Research; Jermyn at the Flatiron Institute). The model §6
    analyses, ỹ = (cx₁ + dx₂)² + e for y = ax₁² + bx₂², is this paper's
    with two features and one neuron, so the identification is
    confirmed. arXiv v1 was submitted 2022-10-04, which gives
    `published:` (ADR-002), three days before the post; v4 is of
    2025-03-25. The paper carries no journal DOI.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full (NOTE-tmp8m63d) from the arXiv PDF of v4 (23 pp.), text
    extracted with pdftotext; v1 to v3 were fetched and compared where
    the reading turned on them, and the Alignment Forum post was read in
    full. Figures were read from their captions and the text. Status
    Deferred → Active. Two accounts filed: THEORY-tmp68zar (Active, the
    quadratic model's solution, re-derived and checked numerically) and
    THEORY-tmp2tsxo (Proposed, the authors' wider account of
    polysemanticity as capacity allocation).
tags:
- representation-learning
- anthology-candidate
date: '2026-10-27'
published: '2022-10-04'
arxiv: '2210.01892'
url: 'https://www.alignmentforum.org/posts/kWp4R9SYgKJFHAufB/polysemanticity-and-capacity-in-neural-networks'
first_author: 'Scherlis'
keywords:
- 'polysemanticity'
- 'superposition'
- 'feature capacity'
- 'kurtosis'
- 'sparsity'
- 'phase diagram'
- 'semiorthogonal matrices'
- 'toy models'
extends:
- LIT-323
implementations: []
summary: >-
  Scherlis, Sachan, Jermyn, Benton and Shlegeris (2022), arXiv 2210.01892.
  Defines a feature's capacity, C_i = (w_i·w_i)²/Σ_j(w_i·w_j)², in [0, 1]
  with total at most the embedding dimension, and treats superposition as
  the optimal allocation of capacity. In a model computing Σ(W_i·x)² + b
  to fit y = Σ v_i x_i², the expected loss depends only on capacities and
  embedding lengths, and the optimum is in closed form: with fourth moment
  k ≤ 3 features are ignored or given a whole dimension; with k > 3 a
  feature is shared when its importance lies in an interval set by k.
  Efficient embeddings are exactly the block-semiorthogonal ones.
---
<!-- inactive-ok-file: THEORY-tmp2tsxo — Proposed; the authors' wider account filed from this reading, cited as open -->

# LIT-tmp9yvin: Polysemanticity and Capacity in Neural Networks

Scherlis, A., Sachan, K., Jermyn, A. S., Benton, J. and Shlegeris, B.
(2022). Polysemanticity and capacity in neural networks. arXiv:2210.01892
(v1 4 October 2022; v4 25 March 2025). Announced on the Alignment Forum,
7 October 2022.

Read in full on 2026-10-27 (NOTE-tmp8m63d). Two accounts were drawn from
it: THEORY-tmp68zar (Active) and THEORY-tmp2tsxo (Proposed).

## Why this is here

Registered and read at the owner's request of 2026-10-27 ("file the next
readings"), as one of the works the circuits readings named and did not
register. The causal scrubbing appendix (LIT-1583, NOTE-1202) shows how a
hypothesis handles superposition on this paper's toy model (NOTE-1202's
claim C4), and §6.1's point about splitting the interference term is the
mechanism THEORY-1029 finds in a real model. The record
held the descriptive study it builds on, Toy Models of Superposition
(LIT-323), but no model of superposition solved in closed form. Read
against the circuits line, it supplies the case the appendix assumes: when
two features of equal importance share one neuron, and why sparse inputs
make them share.
