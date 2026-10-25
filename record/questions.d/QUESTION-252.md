---
number: 252
status: Open
formerly:
- QUESTION-tmp1nqby
title: 'For the conditions an effective description is asked to meet (predictive sufficiency for a declared target, dynamical independence of the omitted variables, memory closure under a declared projection, approximation fidelity in a declared metric and horizon, and tractability within a declared budget), which can fail while all the others hold, which such configurations are impossible in which model classes, and which conditions turn out to be parameters of the others rather than conditions in their own right?'
version: 2
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: A36's predictive-closure test for a population. The
    question is unchanged.
tags:
- complex-systems
- mathematics
- philosophy-of-science
date: '2026-10-21'
line: formal-apparatus
summary: >-
  The owner's idea at U3 of the exchange of 2026-10-20: "what if we censor
  or negate each virtue one at a time? that reduces our combinations from
  n! to n." A3 corrected the count (2ⁿ presence/absence configurations, not
  n!) and fixed five conditions, asking whether each leave-one-out case is
  realizable: "An impossible configuration is itself a substantive
  result." The record holds pairwise non-implications only, none a
  leave-one-out witness: [CLAIM-389](../claims.d/CLAIM-389.md) gives zero memory without independence
  in VAR(1), [CLAIM-304](../claims.d/CLAIM-304.md) retention without feasible recovery. A4 and A5 then
  found that some conditions are parameters rather than conditions
  ([CLAIM-401](../claims.d/CLAIM-401.md)). The same form as [QUESTION-093](QUESTION-093.md) and [QUESTION-115](QUESTION-115.md), on a new
  list.
answered_by:
- CLAIM-401
---
<!-- inactive-ok-file: CLAIM-353 CLAIM-396 — Proposed; record precedents and partial witnesses, cited as open -->
<!-- inactive-ok-file: CLAIM-401 — Proposed; the claim and the regime filed from the same exchange, cited as the question's own partial answer and framing -->
<!-- inactive-ok-file: CLAIM-348 — Proposed; the target-relativity of adequacy, cited for context, nothing here rests on it -->

# QUESTION-252: For the conditions an effective description is asked to meet (predictive sufficiency for a declared target, dynamical independence of the omitted variables, memory closure under a declared projection, approximation fidelity in a declared metric and horizon, and tractability within a declared budget), which can fail while all the others hold, which such configurations are impossible in which model classes, and which conditions turn out to be parameters of the others rather than conditions in their own right?

## Why it is a question

The owner, at U3 of the exchange of 2026-10-20: "I think we have something
like 5-ish distinctions here and so "matrixing" as I suggest would be at
least 5! cases to consider, which isn't feasible for a single paper ...
what if we censor or negate each virtue one at a time? that reduces our
combinations from n! to n."

A3 corrected the count: "for \(n\) binary virtues, there are \(2^n\)
possible presence/absence configurations, rather than \(n!\)". That is 32
for five, and the leave-one-out design is five cases beside the baseline.
It asks whether each condition is independent of the conjunction of the
others, which is stronger than asking whether any two are equivalent. A3
fixed the five conditions: predictive sufficiency (P), dynamical autonomy
(D), memory closure (M), approximation fidelity (A) and computational
tractability (C). It kept apart censoring a condition (not requiring it)
from negating it (requiring that it fail), and three outcomes:
constructive independence, logical dependence and independence only under
further conditions. And: "An impossible configuration is itself a
substantive result."

Two warnings from A3 belong to the question. "P and D must have different
conditioning sets ... Otherwise the distinction risks collapsing by
definition." And: "Without a fixed target, we could make an ablation
succeed simply by moving the goalposts." So the regime is fixed first
([TERM-065](../terms.d/TERM-065.md)).

The owner observed at U4 that the recommendation had fallen from five
ablations to three. A4 split that into structural reduction (some
conditions are definable from others) and epistemic selection (three are
easy to isolate with results the record holds), and found "the evidence
supports B more directly than A". A5 proposed a revised form of the
question: "remove one source of information or one class of operations,
then determine which properties remain identifiable" (the macro law only,
no history, no interventions, bounded computation). That form is part of
this question.

## What the record holds

Each item is pairwise. None is a leave-one-out witness.

- **¬D with M.** [CLAIM-389](../claims.d/CLAIM-389.md): in a VAR(1), zero Mori–Zwanzig memory without
  dynamical independence. P holds there only for prediction from Y's own
  past: Y's own past leaves residual variance 0.75 and the full past 0.59,
  a transfer entropy of 0.120 nats (checked on 2026-10-21). A3 offered it
  as a witness of every condition but D. It is not one, and A and C are
  not addressed in it.
- **D with ¬M.** Impossible in VAR(1) ([CLAIM-389](../claims.d/CLAIM-389.md)). Realizable in VAR(2), as
  [CLAIM-389](../claims.d/CLAIM-389.md)'s "What it does not say" reports. Checked on 2026-10-21: the
  autonomous AR(2) Y_t = 0.5 Y_{t−1} + 0.3 Y_{t−2} + ε has Mori memory
  c₁ = 0.147, c₂ = −0.0315, non-zero, with autocovariance of Hankel rank 2
  and memory of Hankel rank 1, as [CLAIM-397](../claims.d/CLAIM-397.md) says. A3 offered [CLAIM-398](../claims.d/CLAIM-398.md) for
  this case. In VAR(1) every [CLAIM-398](../claims.d/CLAIM-398.md) example with memory is also
  dependent, and its finite augmentation makes M hold under A3's own
  definition.
- **Retention without feasible recovery.** [CLAIM-304](../claims.d/CLAIM-304.md) and [CLAIM-302](../claims.d/CLAIM-302.md). That is
  a one-shot encoding, for which D, M and A are undefined.
- **Accuracy against dependence.** [THEORY-771](../theory.d/THEORY-771.md), [CLAIM-390](../claims.d/CLAIM-390.md), [CLAIM-386](../claims.d/CLAIM-386.md) and
  [CLAIM-388](../claims.d/CLAIM-388.md), all in [QUESTION-221](QUESTION-221.md), which holds the non-implication open.
- **Not identifiable from a restricted law.** From the coarse variable's
  own law: [CLAIM-397](../claims.d/CLAIM-397.md) and [CLAIM-389](../claims.d/CLAIM-389.md)'s note of 2026-10-20. From the passive
  joint law: [CLAIM-396](../claims.d/CLAIM-396.md), on the direction of coupling.
- **The same form on other lists.** [QUESTION-093](QUESTION-093.md) asks it of four autonomy
  criteria for agency ("can it have the first without the others?"), and
  [QUESTION-115](QUESTION-115.md) of four individuation criteria ("where these criteria
  disagree"). Axiom-independence precedents: [CLAIM-343](../claims.d/CLAIM-343.md) and [CLAIM-353](../claims.d/CLAIM-353.md).
- **Which conditions are parameters.** [CLAIM-401](../claims.d/CLAIM-401.md), after A4 and A5:
  P and A need a declared target, C restricts the operations, and M
  depends on the projection ([QUESTION-222](QUESTION-222.md), [THEORY-752](../theory.d/THEORY-752.md)). [CLAIM-152](../claims.d/CLAIM-152.md) and
  [CLAIM-348](../claims.d/CLAIM-348.md) give the target-relativity.

## What would count as an answer

For one stated model class, linear Gaussian VAR first, with the target,
projection, metric, horizon and budget declared: for each condition, a
construction meeting the other four and failing it, or a proof that the
other four entail it. And a report of which conditions dissolved into
parameters of the regime on the way. An answer in A5's revised form says,
for each restricted access regime, which of the conditions remain
identifiable.

## Note of 2026-10-25: predictive closure proposed for a population

A36 §8 of the exchange of 2026-10-24, continued, proposed predictive
closure, P(g(X_{t+1}) | X_t) = P(g(X_{t+1}) | g(X_t)), as the test of
whether (m, a, r) is a sufficient reduction of a population of
perspectives. That is this question's memory closure under a declared
projection. [CASE-124](../cases.d/CASE-124.md)'s witness 2 already shows a failure of it for (m, a).
A42 marked the derivation of the three macro-variables from the
population "Not established". In the linear network of [CASE-tmpvmjgd](../cases.d/CASE-tmpvmjgd.md) the
influence-weighted coordinate is exactly closed. The question is
unchanged.
