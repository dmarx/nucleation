---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpvzd8x](../notes.d/NOTE-tmpvzd8x.md)); worth reading as the analytic result behind iterated learning: a chain of learners who share a prior and each sample a hypothesis from their posterior is a Gibbs sampler, so the probability that a learner holds a language converges to its prior probability whatever the amount of data passed on, and the data produced converge to the prior predictive. Learners who take the MAP hypothesis run stochastic EM instead: the outcome centres on the prior''s mode but depends on data amount and noise, and in the two-language case is the same for every prior strength α between 0.5 and 1 − ε, so weak biases can be amplified. Equal-fitness populations share the equilibrium. Source of [THEORY-tmp0w0cu](../theory.d/THEORY-tmp0w0cu.md).'
title: 'Language Evolution by Iterated Learning With Bayesian Agents'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the authors' posted copy of the published article
    (cocosci.princeton.edu/tom/papers/iteratedcogsci.pdf, the typeset
    Cognitive Science pages 441–480; Wiley's PDF returned 403); see
    NOTE-tmpvzd8x. Details checked against Crossref (Cognitive
    Science 31(3):441–480, print 6 May 2007). `published:` is that date,
    the earliest full date Crossref gives. Not held in the Anthology of
    the SOTA: a grep of its record/ (clone of 2026-10-09, commit
    1cffe8f) for the authors, the identifier and the title found
    nothing.
tags:
- linguistics
- probabilistic-modeling
- cognition
- compositionality
date: '2026-10-09'
published: '2007-05-06'
doi: '10.1080/15326900701326576'
first_author: 'Griffiths'
keywords:
- 'iterated learning'
- 'language evolution'
- 'Bayesian inference'
- 'Gibbs sampling'
- 'inductive biases'
- 'linguistic universals'
implementations: []
summary: >-
  Griffiths & Kalish (2007), Cognitive Science 31(3):441–480. When
  Bayesian learners sample a language from their posterior, iterated
  learning is a Gibbs sampler and converges to the learners' prior; when
  they take the posterior mode, it behaves like a variant of EM and
  depends also on how much data passes between generations; in a
  two-language case the MAP outcome is the same for a wide range of prior
  strengths. Read in [NOTE-tmpvzd8x](../notes.d/NOTE-tmpvzd8x.md).
---

<!-- inactive-ok-file: LIT-tmp9f0fn — Deferred, no lawful full text; named as the classical case, not leaned on -->
<!-- inactive-ok-file: THEORY-tmp0w0cu — Proposed; the account this reading produced -->

# LIT-tmpdbgz6: Language Evolution by Iterated Learning With Bayesian Agents

Thomas L. Griffiths and Michael L. Kalish (2007), *Cognitive Science*
31(3):441–480 — DOI-10.1080/15326900701326576

## Key takeaways

- **Sampling learners converge to the prior** (§4, Eqs. 25–36). If every
  learner shares a prior P(h) and a likelihood matched to production, and
  samples h from P(h|d), the prior is the stationary distribution of the
  chain on hypotheses and the prior predictive that of the chain on data.
  The amount of data passed on changes only the speed (via the second
  eigenvalue), not the endpoint, so structure can emerge without a
  bottleneck, but only if the prior favours it.
- **It is a Gibbs sampler** (§4.2): alternately drawing h given d and d
  given h is the systematic-scan Gibbs sampler for P(d|h)P(h).
- **MAP learners run stochastic EM** (§5): the transmitted data are the
  latent variable and there are no observations, so the outcome
  concentrates near the prior's mode. In the two-language case (Table 1)
  the stationary probability of the favoured language is (s + (1 − s)ε) /
  (s + 2(1 − s)ε), independent of the prior α whenever ε < 1 − α: a weak
  bias does as much as a strong one.
- **Compositionality simulation** (§6): 4 compositional and 256 holistic
  languages. Under sampling, long-run frequencies match the prior at every
  data size; under MAP the prior's favourite dominates (no compositional
  language ever, when they get 1% of the prior mass; with half of it,
  holistic languages appear only once learners see three or more
  utterances).
- **Populations** (§7): with equal fitness, the same distribution is the
  stable equilibrium of an unbounded population. The authors warn that
  selection could break the correspondence, and close by extending the
  conclusion, unanalysed, to "legends, religious concepts, and social
  norms".

The laboratory counterpart is [LIT-tmpe93h7](LIT-tmpe93h7.md), which cites this paper only in a
block of model references ([NOTE-tmppvy0t](../notes.d/NOTE-tmppvy0t.md)). The paper does not cite
Bartlett ([LIT-tmp9f0fn](LIT-tmp9f0fn.md)), whose serial reproduction of a folk tale is the
classical case its closing extrapolation describes.

## Standing in the record

Filed on 2026-10-09 at the owner's request, as one of the works in the
reference list of the owner's working manuscript (October 2026) that the
record did not yet hold. See the curation entry of that day.
