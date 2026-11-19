---
status: Skimmed
paper: LIT-tmp62j1j
title: 'Settles 2009 (rev. 2010) — Active Learning Literature Survey'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://burrsettles.com/pub/settles.activelearning.pdf (the
    author's own site; PDF, extracted with pdftotext). Kind: author's page.
    Date 2026-11-19. HTTP 200, no obstacle. Version: the PDF's title page
    reads "Computer Sciences Technical Report 1648, University of
    Wisconsin–Madison, Updated on: January 26, 2010". The LIT's published:
    2009-01-09 is the original report date as commonly cited; the copy
    served is the 2010 revision. The filer should note this; the published
    date was not verified against the 2009 original. Read: abstract and
    contents; §1.1 What is Active Learning?; §3 introduction and §3.4
    Expected Error Reduction (in part); §4.1 Empirical Analysis; §4.2
    Theoretical Analysis (first part); §6.3 Variable Labeling Costs; §6.6
    Changing (or Unknown) Model Classes; §6.7 Stopping Criteria; §7.1–7.5
    Related Research Areas; §8 Conclusion. Skimmed or skipped: §1.2–1.3, §2
    Scenarios, §3.1–3.3 and §3.5–3.6 (query strategies in detail), the rest
    of §4.2, §5, §6.1–6.2, §6.4–6.5, bibliography.
date: '2026-11-19'
---

# NOTE-tmpob2w3: Settles 2009 (rev. 2010) — Active Learning Literature Survey

## Contribution

The standard survey of active learning in machine learning as of 2010. It covers the scenarios (membership query synthesis, stream-based selective sampling, pool-based sampling) and the query-strategy frameworks (uncertainty sampling, query-by-committee, expected model change, expected error reduction, variance reduction, density weighting). It also covers empirical and theoretical evidence, problem variants, practical issues (batch mode, noisy oracles, variable costs, changing model classes, stopping), and related areas (semi-supervised learning, RL, submodular optimisation, equivalence queries).

## Key results

- §1.1, p. 4: "The key hypothesis is that if the learning algorithm is allowed to choose the data from which it learns—to be “curious,” if you will—it will perform better with less training." Active learning is "sometimes called “query learning” or “optimal experimental design” in the statistics literature".
- §4.1, p. 27, a caveat: actively chosen data are "a biased distribution, not drawn i.i.d. from the underlying natural density". And "Schein and Ungar (2007) showed that active learning can sometimes require more labeled instances than passive learning even when using the same model class".
- §4.2, p. 28: in a noiseless one-dimensional threshold task, binary search over a pool gives "an exponential reduction in the number of labeled instances". Generalising this is the theoretical programme.
- §6.3, pp. 37–38: "simply reducing the number of labeled instances does not necessarily guarantee a reduction in overall labeling cost". Settles et al. 2008a found that "active learning approaches which ignore cost may perform no better than random selection (i.e., passive learning)."
- §6.6, p. 43: when the model class is unknown, "random sampling (at least for pilot studies, until the task can be better understood) may be more advisable than taking one’s chances on active learning with an inappropriate learning model."
- §6.7, p. 44: "One way to think about this is the point at which the cost of acquiring new training data is greater than the cost of the errors made by the current model." In practice, "the real stopping criterion for practical applications is based on economic or other external factors, which likely come well before an intrinsic learner-decided threshold."
- §7.3, pp. 46–47: "a greedy algorithm to optimize a submodular function gives us a lower-bound performance guarantee of around 63% of optimal", but "Active learning strategies do not optimize to submodular functions in general".

## Assumptions

- The setting is mainly supervised: an oracle labels instances, and unlabeled data are cheap. Costs are mostly per-label and known in advance (§6.3 notes the exceptions).
- A survey. Claims are reported from the cited literature, with the author's own practical judgement flagged as such ("in my own experience").

## Concepts

- Query scenarios: membership query synthesis, stream-based, pool-based.
- Query strategies: uncertainty sampling, query-by-committee and version space, expected model change, expected error reduction, variance reduction, information density.
- Sampling bias of actively collected data; cost-sensitive active learning; stopping criteria; submodularity and greedy guarantees.

## Bearing on the record

- CLAIM-572: qualifies, from outside. CLAIM-572 demonstrates that, under one budget, stopping when the next probe does not pay can miss the least total, because a probe's worth depends on later ones. Settles reports that the field's greedy guarantees rest on submodularity (diminishing returns) and that active-learning objectives are generally not submodular. This is the same structural reason, stated generally. The stopping criteria he surveys are intrinsic stability heuristics. CLAIM-572's greedy-stopping point is the one place this literature's own guidance (stop when acquisition costs more than the errors it saves) is shown to fail. Not a corroboration: the survey proves nothing about CLAIM-572's model.
- QUESTION-tmprj00l: supports a premise. "a training set built in cooperation with an active learner is inherently tied to the model that was used to generate it". The data an active learner sees depend on its current model, which is the feedback that, by the question's summary, puts the no-feedback thermodynamic result out of reach.
- Verdict on the LIT's source (the owner at U30: the exchange was entering active-learning territory): the right entry point for the term as machine learning uses it. Note that the survey's active learning is mainly label-querying, not an agent acting on a world. Its link to active inference and optimal design is only by name (§1.1, §7.2).

## Limitations

- As of 2010. It predates deep active learning, Bayesian active learning by disagreement (BALD) and modern batch methods.
- Mostly supervised classification with an oracle. Little on causal or interventional queries (equivalence queries aside) or on structure learning.
- Skimmed: query strategies were not read in detail.
