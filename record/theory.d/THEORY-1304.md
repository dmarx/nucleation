---
number: 1304
status: Active
formerly:
- THEORY-tmp37m50
title: 'In latent Dirichlet allocation each document draws its own topic mixture from a Dirichlet shared across the corpus and draws a topic afresh for every word, a three-level model of conditionally independent assignments; the mixture of unigrams, which draws one topic per document, is its two-level comparison, and the Dirichlet is a distribution over mixtures, not over topics'
version: 1
tags:
- probabilistic-modeling
date: '2026-11-03'
source:
- LIT-1948
summary: >-
  Blei, Ng and Jordan (2003), [LIT-1948](../literature.d/LIT-1948.md), read in full in
  [NOTE-1519](../notes.d/NOTE-1519.md). Active as a statement of the model's structure, which is
  definitional and is stated in the text (pp. 996–1001); the variational
  updates were checked against Appendix A. It does not say LDA fits text
  well, which rests on perplexity on two corpora, or that its topics are
  anything beyond devices for representing word distributions, which the
  authors disclaim.
---

# THEORY-1304: In latent Dirichlet allocation each document draws its own topic mixture from a Dirichlet shared across the corpus and draws a topic afresh for every word, a three-level model of conditionally independent assignments; the mixture of unigrams, which draws one topic per document, is its two-level comparison, and the Dirichlet is a distribution over mixtures, not over topics

## Source

Blei, Ng and Jordan (2003), [LIT-1948](../literature.d/LIT-1948.md), JMLR 3: 993–1022; read in
[NOTE-1519](../notes.d/NOTE-1519.md).

## What was actually shown

**The model.** θ ~ Dir(α), then for each word zₙ ~ Multinomial(θ) and
wₙ ~ p(wₙ | zₙ, β) (p. 996). "There are three levels to the LDA
representation": α and β per corpus, θ_d per document, z_dn and w_dn per
word (p. 997). Given θ_d the assignments are independent and identically
distributed, and the authors place LDA among "conditionally independent
hierarchical models" (p. 997).

**The comparison the authors draw.** A "simple Dirichlet-multinomial
clustering model … restricts a document to being associated with a single
topic. LDA, on the other hand, involves three levels, and notably the topic
node is sampled *repeatedly* within the document" (p. 997). The mixture of
unigrams, p(w) = Σ_z p(z) Πₙ p(wₙ | z), assumes "each document exhibits
exactly one topic" (p. 1000).

**What is a topic.** The latent multinomial variable z, characterized by a
row βᵢ of the topic-word matrix (pp. 996, 1001). θ is "a topic mixture", a
point on the topic simplex. In smoothed LDA each row βᵢ is drawn
independently from one exchangeable Dirichlet with a single scalar η
(§5.4, footnote 2).

**Why this form.** Words exchangeable within a document must, by de Finetti,
have the form ∫ p(θ) Πₙ p(zₙ | θ) p(wₙ | zₙ) dθ; the Dirichlet is then a
choice made for conjugacy (pp. 996, 998).

It could have been otherwise as a design: the mixture could have been fixed
per corpus (the unigram model's limit) or per document without a prior
(pLSI). The paper chooses neither and says why.

## What this does not say

- That an LDA fit shows organization among topics: given θ_d, no topic
  conditions another, by construction.
- That the symmetric-Dirichlet limits reproduce the paper's mixture of
  unigrams exactly: a → 0 with Dir(a, …, a) gives a uniform p(z); the
  paper's version has a free p(z), the limit of Dir(sπ) as s → 0.
- That the Dirichlet prior is forced: de Finetti forces a mixing
  distribution, not this one.
