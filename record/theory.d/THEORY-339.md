---
number: 339
status: Proposed
formerly:
- THEORY-tmpcy2pz
promote_when: >-
  A preregistered replication, outside the original group's paradigm or by
  another lab, in which query order and the overlap between successive queries
  are manipulated and, in the same participants, both the carry-over of an error
  induced in the first answer and the time or effort saved on the second are
  measured. It promotes the account if carry-over appears only where the second
  query can use the first answer and comes with a saving; it refutes the reuse
  reading if carry-over appears without overlap (anchoring) or if no saving is
  ever found. Another correlational order study, or a further simulation of
  sample against summary reuse, cannot settle it: dependence on the earlier
  answer is already held, and what is missing is the efficiency half.
title: "People's answers to a probability query depend on their own answers to an earlier query whose result it can use: a person's sub-answer predicts their later answer only when asked first, and a bias induced in a first judgment carries into a second only when the two share part of a hypothesis space, so reuse carries the earlier error with it; that reuse saves computation rests on one small response-time study and one secondary-task result"
version: 1
tags:
- cognition
- probabilistic-modeling
date: '2026-10-15'
source:
- LIT-1074
- LIT-1056
- LIT-1077
summary: >-
  Dasgupta, Schulz, Goodman and Gershman (2018), [LIT-1074](../literature.d/LIT-1074.md), read in [NOTE-875](../notes.d/NOTE-875.md);
  Gershman and Goodman (2014), [LIT-1056](../literature.d/LIT-1056.md), read in [NOTE-886](../notes.d/NOTE-886.md); Dasgupta and Gershman
  (2021), [LIT-1077](../literature.d/LIT-1077.md), read in [NOTE-865](../notes.d/NOTE-865.md). In five small online experiments, an earlier
  answer shapes a later one only when the later query can use it, and errors in the
  first carry into the second. The authors call this amortized inference, reuse of
  past computation bought at a cost in bias. The speed benefit is shown once
  (median log-RT facilitation, n ≈ 50 per order) and otherwise assumed; storage
  and retrieval are free in the models; the 2021 review adds stale cached values
  from the planning literature, second-hand. No paper prices when reuse pays or
  touches stores outside the head.
bears_on:
- QUESTION-095
---

# THEORY-339: People's answers to a probability query depend on their own answers to an earlier query whose result it can use: a person's sub-answer predicts their later answer only when asked first, and a bias induced in a first judgment carries into a second only when the two share part of a hypothesis space, so reuse carries the earlier error with it; that reuse saves computation rests on one small response-time study and one secondary-task result

## Source

Dasgupta, Schulz, Goodman and Gershman (2018), [LIT-1074](../literature.d/LIT-1074.md) (Cognition 178, 67–81),
read in [NOTE-875](../notes.d/NOTE-875.md): Experiments 1–3, the simulations of Figure 3, the General
Discussion. Gershman and Goodman (2014), [LIT-1056](../literature.d/LIT-1056.md) (CogSci 2014, 517–522), read in
[NOTE-886](../notes.d/NOTE-886.md): Experiments 1 and 2, Figure 7. Dasgupta and Gershman (2021), [LIT-1077](../literature.d/LIT-1077.md)
(Trends in Cognitive Sciences 25, 240–251), a review, read in [NOTE-865](../notes.d/NOTE-865.md).

## What was actually shown

**Dependence on an earlier sub-answer (2014).** On a five-node network of
defecting officers, each subject's answer to a sub-query, put through Bayes'
rule, predicted their answer to a complex query when the sub-query came first
(r = 0.28, n = 73) and not when it came after (r = −0.11). The difference between
the correlations was not tested. A structurally matched control query showed no
correlation in either order. In speeded choices, the complex query was answered
faster relative to the control when the sub-query came first (median log-RT
facilitation about 0.47 against 0.23; z = 2.09), analysing only subjects who gave
the more likely answer.

**Carry-over of an induced bias (2018).** Unpacking a first query with typical or
atypical examples raised or lowered the judged probability. A second, always
packed query carried the effect (Experiment 1, N = 78 analysed: regression 4.39
and −7.86), and errors on the two were correlated (r = 0.67 aggregated, 0.55
within participants). With no shared letter between the queries, nothing carried
over, which rules out simple numerical anchoring (Experiment 2, N = 80). Load
on the first query enlarged the carry-over, which the authors' simulations read
as reuse of a stored summary rather than of samples. With a new cue, carry-over
appeared for subadditivity only, when the cue's posterior was similar to the
first (Experiment 3; similar against dissimilar, p = 0.07).

**Efficiency, in 2018.** No response times were recorded. With load on the
second query, probe accuracy was higher on reusable trials (t(36) = 3.16). This
is the paper's only evidence that reuse saves anything.

**The framing.** "An inference engine may gain efficiency by incurring some
amount of bias due to reuse of past computations—a strategy we will refer to as
amortized inference". The 2014 paper calls it caching or "memoizing" of
"sub-computations that are invoked by multiple queries". The 2021 review extends
it: a learned recognition model is "a distributed form of memoization called
amortization", and the planning literature supplies decisions based on cached
values that have not been updated after devaluation.

**What could have come out otherwise.** Carry-over could have appeared without
overlap, which would make it anchoring; it did not. The order effect could have
been absent; it was present, but rests on one significant and one non-significant
correlation.

## What this does not say

- **That reuse is a pull toward earlier answers.** What carries is the earlier
  computation's error, and only where its result is usable. The no-overlap
  condition was built to rule out a numerical pull, and found none.
- **That reuse is faster, in general.** Speed is shown in one small study with
  selection on the outcome query; the 2018 paper measures no times, and the
  review assumes reuse is cheaper throughout.
- **That retrieval is computation.** The models give storage and retrieval no
  cost; the review mentions retrieval demands once. It says memory replaces
  computation, not that retrieval is a kind of it.
- **That the reused results went stale.** In the experiments the error is present
  when the first answer is computed, or comes from applying it to a different
  query. A result that was right and has since gone out of date appears only in
  the review's account of devaluation studies the record has not read.
- **When reuse pays.** The 2014 paper lists trade-offs (complexity, decomposability,
  frequency) in prose; the 2018 paper asks "What objective function is being
  optimized by amortization?"; the review lists when to cache as open.
- **That the brain uses either tested scheme.** "We do not claim that either
  extreme is plausible".
- **Anything about stores outside the head.** None of the three cites an
  offloading or distributed-cognition source.

## Connections

- [QUESTION-095](../questions.d/QUESTION-095.md): the "precompute and leave a result" strategy with the store in
  the head, though memoization here is lazy: results are cached when first
  computed, not ahead of a predicted query as the speed bugs are.
- [CLAIM-303](../claims.d/CLAIM-303.md)'s rider, that "persistence can preserve errors as efficiently as valid
  discoveries", has an empirical counterpart here, for errors present from the
  start.
- [CLAIM-295](../claims.d/CLAIM-295.md): keeping a summary in place of samples adds no information and narrows
  the queries it serves ([NOTE-875](../notes.d/NOTE-875.md)).
- [THEORY-355](THEORY-355.md) and [THEORY-346](THEORY-346.md) treat stores in the world.

## Note of 2026-10-30: what holds it back

The title states a general effect in people from five small online
experiments by one group, so it keeps its condition (ADR-065 §6): the
missing result is a preregistered replication outside the original
paradigm that measures, in the same participants, both the carry-over of an
induced error and the time or effort saved. The first finding also says
more than the 2014 study tested: the sub-answer predicted the later answer
when asked first (r = 0.28) and not when asked after (r = −0.11), but the
difference between the two correlations was not tested (NOTE-886), so "only
when asked first" is not shown.
