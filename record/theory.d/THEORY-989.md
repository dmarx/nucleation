---
number: 989
status: Proposed
formerly:
- THEORY-tmpi9pkg
promote_when: >-
  A re-estimate of held-out likelihood on the JACM abstracts, or on another
  corpus of the same kind, with an estimator whose error is controlled
  (annealed importance sampling, a left-to-right or Chib-style estimator, or
  an exact computation on a small corpus), shows hLDA ahead of LDA at every
  fixed topic count near hLDA's posterior topic count. It is refuted if
  such an estimate puts LDA level with or ahead of hLDA there. A further
  harmonic-mean comparison cannot settle it, since that is the evidence it
  already rests on.
title: 'On the abstracts of the Journal of the ACM, the held-out likelihood of infinite-depth hierarchical LDA is higher than that of flat LDA at every fixed topic count in a range bracketing hLDA''s own posterior topic count, about 140, though the authors expect flat LDA to win once the topic count is free'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-1176. The comparison was read in full, but
    its held-out likelihoods are harmonic-mean estimates, which are
    unreliable, so the reading does not meet ADR-047 v3's condition that
    the study's design support the result as stated.
tags:
- probabilistic-modeling
- information-retrieval
date: '2026-10-26'
source:
- LIT-1542
summary: >-
  Blei, Griffiths and Jordan (2010), [LIT-1542](../literature.d/LIT-1542.md), §6.3 and Fig. 9, read in
  [NOTE-1176](../notes.d/NOTE-1176.md). One corpus, five-fold cross-validation, hyperparameters
  integrated out. It is evidence that a single-path hierarchy can earn its
  constraint in prediction, near its own size. It is not evidence that a
  hierarchy predicts better than a flat mixed-membership model in
  general: the paper itself says the flat model should dominate at large
  topic counts.
---

# THEORY-989: On the abstracts of the Journal of the ACM, the held-out likelihood of infinite-depth hierarchical LDA is higher than that of flat LDA at every fixed topic count in a range bracketing hLDA's own posterior topic count, about 140, though the authors expect flat LDA to win once the topic count is free

## Source

Blei, Griffiths and Jordan (2010), [LIT-1542](../literature.d/LIT-1542.md), §6.3 and Figs. 9–10, read
in full in [NOTE-1176](../notes.d/NOTE-1176.md) from arXiv 0710.0845v3.

## What was actually shown

The JACM corpus (536 abstracts) was split five ways. hLDA was run with
infinite depth, and LDA at a range of topic counts around hLDA's posterior
mean, with all hyperparameters given priors and integrated out. For each
of 100 posterior samples of the latent variables on the training
documents, 800 samples on the held-out documents gave a harmonic-mean
estimate of their conditional probability, and these were averaged. The
posterior over hLDA's topic count had its mode near 140. "At each fixed
topic cardinality in this range of topics, hLDA provides significantly
better predictive performance than LDA."

The authors frame it as an hLDA-centred test: LDA is "significantly more"
flexible, since a document can use any mixture of its topics, so "for
large corpora we can expect LDA to dominate hLDA in terms of predictive
performance". The finding is that, in the range near its own size, the
single-path constraint helps rather than hurts.

What could have come out otherwise: the flexible model could have won at
every topic count, as the authors expect at large ones.

## Why it is Proposed

The harmonic-mean estimator of a marginal likelihood (Kass and Raftery,
cited by the paper) is unstable, tends to overestimate, and can have
infinite variance. The margins in Fig. 9 are large, but no interval
on the estimator is given. One corpus was used.

## What this does not say

- **Not that hierarchies predict better than flat models.** The paper
  expects the reverse when the topic count is free, and says so.
- **Not that hLDA's topics are more interpretable.** That is Fig. 10's
  separate claim, by eye, against an LDA run with function words left in.
- **Not about multiple-path hierarchies.** The nested HDP ([LIT-002](../literature.d/LIT-002.md),
  [NOTE-023](../notes.d/NOTE-023.md)) is a different comparison.

## Connections

- **[QUESTION-276](../questions.d/QUESTION-276.md).** T21 asked that a hierarchy be allowed "to lose if
  it doesn't provide useful explanatory compression". This is the
  original paper's version of that test: it passes in a range, on one
  corpus, by an estimator that needs replacing. A hierarchy over members'
  activity would need the same test against a flat mixed-membership
  model, with held-out data the inference did not see.

## Note of 2026-10-30: what holds it back

The title states held-out likelihoods that the paper estimated only by the
harmonic-mean estimator, which can overestimate and have infinite variance,
with no interval given. A re-estimate with a controlled estimator is the
missing result. Narrowing to what the paper reports would free nothing, so
it is not narrowed ([ADR-065](../decisions.d/ADR-065.md) §7).
