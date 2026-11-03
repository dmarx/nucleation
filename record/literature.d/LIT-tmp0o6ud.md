---
status: Active
status_note: >-
  read in full 2026-11-03 (NOTE-tmplt5sh), from the JMLR PDF; worth
  reading as the source of the per-document Dirichlet mixture that
  CLAIM-tmphbnqm makes the difference between the owner's H1 and H2, and
  for the authors' own contrast with the one-topic-per-document mixture of
  unigrams. The structure is definitional and checked; the empirical
  superiority rests on perplexity on two corpora.
title: 'Latent Dirichlet Allocation'
version: 2
history:
- version: 1
  date: '2026-11-02'
  note: >-
    Filed, not read. Citation checked against the JMLR page on 2026-11-02
    (pp. 993–1022, January 2003, no day given, so the first of the month
    per ADR-002; JMLR registers no DOI). The summary says why it is here,
    not what it shows.
- version: 2
  date: '2026-11-03'
  note: >-
    Read in full from the JMLR PDF, 30 pp., §§1–8 and Appendix A; the
    first NOTE on the work (NOTE-tmplt5sh). Status set from the reading:
    Active. The PDF confirms "Published 1/03". The summary is replaced by
    one from the text. The registration's account held. CLAIM-tmphbnqm's
    account of the model matches the paper, with one over-statement: in
    smoothed LDA each topic's word distribution is an independent draw
    from one shared exchangeable Dirichlet (§5.4), not "its own" prior.
    One THEORY is filed from it (THEORY-tmp37m50).
tags:
- probabilistic-modeling
date: '2026-11-02'
published: '2003-01-01'
url: 'https://jmlr.org/papers/v3/blei03a.html'
first_author: 'Blei'
keywords:
- 'latent Dirichlet allocation'
- 'topic models'
- 'admixture'
implementations: []
summary: >-
  Blei, Ng and Jordan (2003), JMLR 3. A generative model of a corpus in
  three levels: each document draws a topic mixture θ ~ Dir(α), and each
  word draws a topic from θ and then a word from that topic's
  distribution. Justified by de Finetti's theorem for exchangeable words,
  it is set against the unigram model, the mixture of unigrams (one topic
  per document) and pLSI (a mixture per training document with no model
  for it). Inference and estimation are variational EM. On two corpora it
  has the lowest held-out perplexity of the four, and its document
  features serve classification and collaborative filtering.
---
<!-- inactive-ok-file: LIT-677 — Proposed, Open, Deferred or Unavailable; cited from the exchange "Assess SDT Coverage" of 2026-11-02 as open, works registered unread among them -->

# LIT-tmp0o6ud: Latent Dirichlet Allocation

Blei, D. M., Ng, A. Y., Jordan, M. I. (2003). Latent Dirichlet Allocation. *Journal of Machine Learning Research 3(Jan): 993–1022*. https://jmlr.org/papers/v3/blei03a.html.

Read in full on 2026-11-03 (NOTE-tmplt5sh; THEORY-tmp37m50).

## Key takeaways

- θ_d, the topic mixture, is drawn once per document from Dir(α); a topic
  is drawn for every word (p. 996). Topics are the categories; the
  Dirichlet is over mixtures.
- The authors' own comparison is the two-level "Dirichlet-multinomial
  clustering model", one topic per document (p. 997), i.e. the mixture of
  unigrams (§4.2).
- Given θ_d the topic assignments are conditionally i.i.d.; nothing in the
  model lets one topic condition another.

## Standing in the record

The model the owner's U12 says H2 is. The record holds hLDA ([LIT-1542](LIT-1542.md)), the nested HDP ([LIT-002](LIT-002.md)) and [LIT-677](LIT-677.md), an ELBO paper about LDA, but not LDA itself. Grounds [CLAIM-tmphbnqm](../claims.d/CLAIM-tmphbnqm.md).
