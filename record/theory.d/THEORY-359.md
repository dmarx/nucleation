---
number: 359
status: Proposed
formerly:
- THEORY-tmpyd8k7
promote_when: >-
  A resource-rational model whose cost of computation and architectural
  constraints are measured independently of the behaviour it is fitted to,
  which then predicts out of sample which strategy people use across
  conditions that change the cost or the stakes, and does so better than a
  rival model with as many free parameters that has no cost term. It is
  weakened if constraints fitted in one condition fail to predict another.
  More reviews that recast known biases in the framework cannot settle it,
  because step 5 of the method lets constraints be refitted until a model
  fits; nor can a demonstration that people are not optimal, which the
  framework does not claim.
title: "Cognitive mechanisms can be derived as the one, among those a brain can execute, that best trades the expected utility of its result against the opportunity cost of the time and resources it uses; the review shows the derivation reproducing many heuristics and biases, not that people are optimal, and the objective is per episode"
version: 1
tags:
- cognition
- learning-theory
date: '2026-10-15'
source:
- LIT-1071
answers:
- QUESTION-095
summary: >-
  Lieder & Griffiths (2020; online 2019), [LIT-1071](../literature.d/LIT-1071.md), read in [NOTE-873](../notes.d/NOTE-873.md).
  Resource rationality picks the heuristic that maximizes expected utility of
  its result minus the expected opportunity cost of the time and resources it
  uses (Eq. 3), averaged over environments consistent with what is known
  (Eq. 4), and a five-step method derives process models from it. The
  support is a review of others' models recast in this frame, with numbers
  from those studies. The authors offer optimality as a methodological
  device, not a claim about people, and the method lets constraints be
  refitted to data. The objective is per episode, with no terms for storing,
  retrieving or reusing a result, or for its going stale.
---
<!-- inactive-ok-file: CLAIM-303 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# THEORY-359: Cognitive mechanisms can be derived as the one, among those a brain can execute, that best trades the expected utility of its result against the opportunity cost of the time and resources it uses; the review shows the derivation reproducing many heuristics and biases, not that people are optimal, and the objective is per episode

## Source

Lieder & Griffiths (2020), [LIT-1071](../literature.d/LIT-1071.md) (Behavioral and Brain Sciences 43,
e1), read in [NOTE-873](../notes.d/NOTE-873.md): the target article and the Authors' Response in
full, and four commentaries (Bates, Sims & Jacobs; Dimov; Dingemanse; Ma &
Woodford). The other commentaries were searched by keyword only, and the
primary studies the review cites were not read.

## What was actually shown

**The objective.** Eq. 3 defines the resource-rational heuristic for a
known environment as the h, among "the set of heuristics that brain B can
execute", that maximizes the expected utility of its result minus the
expected cost(t_h, ρ, λ), "the total opportunity cost of investing the
cognitive resources ρ used or blocked by the heuristic h for the duration
t_h of its execution". Eq. 4 averages the same trade over the environments
consistent with what is known. Eq. 3 follows from the lifetime form (Eq. 2)
only "if we assume that life can be partitioned into a sequence of
episodes". A fixed budget is the special case of a cost constant across
heuristics.

**The method.** Five steps (Box 2): state the problem, posit a class of
algorithms with their costs, find the one that trades resources against
accuracy best, test its predictions, and refine the problem or the
constraints. The authors call step 5 "a double-edged sword": constraints
postulated carelessly can overfit, so fitted constraints should be judged
out of sample and measured independently.

**The support.** A review that recasts prior models as instances, so that
cheap, approximate and biased mechanisms fall out as the price of
frugality. Its numbers are others': people's planning reached "about 86% of
the best possible trade-off between decision quality and time cost"
(Callaway et al. 2018a; Lieder et al. 2017). Nothing in the article is a
new experiment.

**Where the optimization happens.** Not in the head at decision time: "for
most of our decisions the problem of finding a good decision mechanism has
already been solved by evolution …, learning, and cognitive development".
The cost of that search is not in Eq. 3 or 4.

## What this does not say

- **That people are optimal.** The Response calls the optimality
  assumption "a methodological device to efficiently search through the
  endless space of possible mechanisms". The review's 86% and 55% figures
  are departures from optimality, reported from other work.
- **That the account has been tested as a whole.** What could fail is each
  derived model, and step 5 allows the constraints to be revised after a
  failure. The paper's own guard against that, independent measurement of
  constraints, is stated as a standard, not shown met.
- **That the currency of cost is known.** The framework specifies "the
  terms of the tradeoff between utility and computational costs but not the
  kinds of computations or the way that those costs are denominated."
- **That it models reuse of computation.** The objective is per episode.
  Precomputing for a later episode, storing a result, retrieving it and its
  going stale have no terms. The value of what a computation leaves behind
  enters only through the utility of the episode's result, which the
  Response says scores the belief state too. Reuse appears only in the
  review, qualitatively: habits, Dasgupta et al. 2018's memorized
  hypotheses, Anderson and Milson's need probability.
- **That it models offloading to the world.** The target article mentions
  "cognitive prostheses" once, as an intervention. Dingemanse's commentary
  names offloading and distributed cognition as a frontier; the Response
  agrees and does not extend the formalism.
- **That Howes et al. 2016 is a memorize-or-look-up trade.** The review
  describes it so; the record's reading of that paper ([LIT-1062](../literature.d/LIT-1062.md), [NOTE-882](../notes.d/NOTE-882.md))
  found no look-up option in the task.

## Connections

- [QUESTION-095](../questions.d/QUESTION-095.md) asks for one cost model covering precompute, storage,
  retrieval, staleness and expected reuse. This objective could host such a
  model as a net of benefit and opportunity cost, and supplies the shared
  currency, but has none of those terms. The search for a heuristic, paid
  once by evolution and learning and then used in every episode, is the
  plainest amortization in the paper, and it is left out of the objective
  on purpose.
- [CLAIM-303](../claims.d/CLAIM-303.md)'s break-even F + n(c_a + u) < n·c_r is a net of the form Eq. 3
  licenses, summed over n uses rather than taken per episode. The paper
  gives no support to the claim's staleness term.
- [THEORY-343](THEORY-343.md): the decision to offload, as people make it, follows belief
  about the cost; the review here says the trade is optimized offline, by
  evolution and learning, not computed by the person, which leaves room for
  that belief to be wrong.
- [THEORY-331](THEORY-331.md): the scaling-law papers price two of the terms this
  objective lacks, expected reuse and per-use cost, in a different domain.
