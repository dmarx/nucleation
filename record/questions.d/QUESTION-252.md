---
number: 252
status: Open
formerly:
- QUESTION-tmp1nqby
title: 'For the conditions an effective description is asked to meet (predictive sufficiency for a declared target, dynamical independence of the omitted variables, memory closure under a declared projection, approximation fidelity in a declared metric and horizon, and tractability within a declared budget), which can fail while all the others hold, and which such configurations are impossible in which model classes?'
version: 6
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: A36's predictive-closure test for a population. The
    question is unchanged.
- version: 3
  date: '2026-10-26'
  note: >-
    A dated note added: pairwise separations on one exactly known kernel
    (CASE-164), not leave-one-out witnesses. The question is
    unchanged.
- version: 4
  date: '2026-10-29'
  note: >-
    Narrowed by the thirteenth status review (ADR-049): its last clause,
    which conditions are parameters of the others, is split off as
    QUESTION-324, Answered by CLAIM-401, which now bears on this
    question (ADR-060) rather than answering it. The old title ended:
    "..., which such configurations are impossible in which model classes,
    and which conditions turn out to be parameters of the others rather
    than conditions in their own right?". It stays Open.
- version: 5
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added: Eberhardt and Lee read
    (NOTE-1413), context and not a witness; Pfante et al. 2014
    registered, Unavailable. The question is unchanged.
- version: 6
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added: causal feature learning read
    (NOTE-1420, NOTE-1415), context and not a witness;
    predictive sufficiency for a declared target can hold where
    the causal reading fails. The question is unchanged.
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
  ([CLAIM-401](../claims.d/CLAIM-401.md)); that part is QUESTION-324, Answered. The same form as [QUESTION-093](QUESTION-093.md) and [QUESTION-115](QUESTION-115.md), on a new
  list.
---
<!-- inactive-ok-file: CLAIM-396 — Proposed; record precedents and partial witnesses, cited as open -->
<!-- inactive-ok-file: LIT-1837 — Unavailable since 2026-10-29; Pfante et al., cited in the note of that date as not reached, nothing here rests on it -->

# QUESTION-252: For the conditions an effective description is asked to meet (predictive sufficiency for a declared target, dynamical independence of the omitted variables, memory closure under a declared projection, approximation fidelity in a declared metric and horizon, and tractability within a declared budget), which can fail while all the others hold, and which such configurations are impossible in which model classes?

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
- **Which conditions are parameters.** Split off as [QUESTION-324](QUESTION-324.md),
  Answered. [CLAIM-401](../claims.d/CLAIM-401.md), after A4 and A5:
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
population "Not established". In the linear network of [CASE-160](../cases.d/CASE-160.md) the
influence-weighted coordinate is exactly closed. The question is
unchanged.

## Note of 2026-10-26: pairwise separations on one kernel

<!-- inactive-ok-file: CASE-164 CASE-163 — Proposed; the lab's runs filed 2026-10-26, cited as partial witnesses, nothing here rests on them -->

[CASE-164](../cases.d/CASE-164.md) adds pairwise non-implications on one exactly known
192-state kernel, like those the record already holds, and no
leave-one-out witness.

- **Dynamical independence without sufficiency for an intervention
  target.** The agents with phase are informationally closed on the
  declared law and lose 0.5051 bits about the next rule integrities under
  a declared intervention mixture, [CLAIM-407](../claims.d/CLAIM-407.md)'s shape.
- **Closure on a support without global strong lumpability** (defect
  0.42). Lumpability is not on this question's list, but [THEORY-822](../theory.d/THEORY-822.md) sets
  it beside dynamical independence.
- **A sample budget against the exact quantity.** At 300 training
  windows a fitted gain is negative where the exact defect is 0.0930 bits
  (dmarx/PerspectiveLab@9f82bfd).

Its refinement witness (authority lumpable, authority with one record bit
not, the full state lumpable again) is in strong lumpability, not in
informational closure. A strong one-step failure of Markov closure in the
lab's population (v1.4, dmarx/PerspectiveLab@7e2edc2
experiments/predictive_closure/) does not by itself show a positive
infinite-history defect. In [CASE-163](../cases.d/CASE-163.md), what a probe budget identifies
is a further budget-relative verdict, of a mechanism's class and
parameters. The question is unchanged.

## Note of 2026-10-29: lumpability does not fix the level effective information picks

Two items of this date, context and not witnesses.

- **Eberhardt and Lee**, [LIT-1839](../literature.d/LIT-1839.md) ([NOTE-1413](../notes.d/NOTE-1413.md)). Their example (17)
  has a strongly lumpable partition, so the block label is closed and
  Markov ([THEORY-822](../theory.d/THEORY-822.md)) and the coarse-graining commutes with time
  evolution. Yet EI picks that partition at one step and the micro at two.
  Strong lumpability does not make the EI-optimal choice stable under a
  change of time step. That is a property of EI, not one of this
  question's five conditions.
- **Pfante, Bertschinger, Olbrich, Ay and Jost 2014**, [LIT-1837](../literature.d/LIT-1837.md), which
  Rosas et al. ([NOTE-1030](../notes.d/NOTE-1030.md)) credit with the equivalence of informational
  closure and commutativity for Markov spatial coarse-grainings, is
  registered and Unavailable. The record still holds that result
  second-hand, through [THEORY-820](../theory.d/THEORY-820.md) and [THEORY-822](../theory.d/THEORY-822.md).

The question is unchanged and stays Open.

## Note of 2026-10-29: predictive sufficiency without the causal reading

Causal feature learning, [LIT-1833](../literature.d/LIT-1833.md) ([NOTE-1420](../notes.d/NOTE-1420.md)) and [LIT-1834](../literature.d/LIT-1834.md)
([NOTE-1415](../notes.d/NOTE-1415.md)), context and not a witness. It separates two sufficiency
conditions for a declared target: the observational partition, sufficient
for predicting it, and the causal partition, sufficient for it under
intervention. Its coarsening theorem says that, outside a set of measure
zero, the causal partition is a coarsening of the observational one. The
overview's toy shows the converse failing: "Warm", a confounded correlate,
is a partition sufficient for prediction that is not causal. So predictive
sufficiency for a declared target can hold where the causal reading fails.
The causal reading is not one of this question's five conditions, so this
is not a leave-one-out configuration. It suggests that the first
condition's declared target needs a declared regime too, observation or
intervention. Its subsidiary variables, coarser cause–effect pairs that
keep sufficiency only for a coarser declared target, are the
target-relativity the first condition already names.

The question is unchanged and stays Open.

## Note of 2026-11-19: follow-up turns of "Topological protection explained"
<!-- inactive-ok-file: CASE-297 — Proposed or Deferred; cited from the follow-up turns filed 2026-11-19 -->

ChatGPT (A84) names operative reification as one of two foundational programs: "What makes a distinction part of the world's operative organization rather than merely part of an observer's useful description?", with candidate criteria (predictive sufficiency, dynamical closure, causal effectiveness, organizational reuse, self-maintenance) that "are not equivalent". Its next advance without an experiment is this question's: "Establish which closure criteria imply which others, and identify counterexamples". The Reddit case ([CASE-297](../cases.d/CASE-297.md)) is offered as one that separates them: a subreddit may be a named category, a persistent practice, a governed institution, a cause of its members' behaviour and a source of further communities, "different achievements".

## Note of 2026-11-22: the table for linear Gaussian VAR(1) and VAR(2)
<!-- inactive-ok-file: CASE-tmpo5jhq CLAIM-tmp186gy CLAIM-tmp9xo66 — new; filed from LEAD-173 -->

[LEAD-173](../leads.d/LEAD-173.md) worked the answer form named here for the first class, with the
regime declared ([CASE-tmpo5jhq](../cases.d/CASE-tmpo5jhq.md)). [CLAIM-tmp186gy](../claims.d/CLAIM-tmp186gy.md) offers the table: three
entailments, D ⇒ M in VAR(1) only ([CLAIM-389](../claims.d/CLAIM-389.md)), P ∧ D ∧ M ⇒ A in every
regime, and A ⇒ P at zero tolerance, and a witness for each of the other
configurations, 16 of 32 in VAR(1) and 22 in VAR(2) at ε = 0. As leave-one-out
results: independence fails alone (the round trip without return of
[CLAIM-389](../claims.d/CLAIM-389.md), behind a target that reads an autonomous part of Y), and so does
tractability; memory closure fails alone only from VAR(2), where [CLAIM-389](../claims.d/CLAIM-389.md)'s
"impossible in VAR(1)" cell opens; sufficiency only at a positive tolerance;
fidelity never. The entailment that forbids the last is three-place, so no
pairwise table shows it.

On the conditions that dissolved into parameters: at h = 1 fidelity is
sufficiency; whether sufficiency can fail alone turns on ε; whether memory
can turns on the class. With the target declared as Y's own future,
sufficiency and fidelity are each D ∧ M ([CLAIM-tmp9xo66](../claims.d/CLAIM-tmp9xo66.md)), A3's collapse.
Whether these answer the question for this class, and so whether it
splits, is the owner's call. The question is unchanged and stays Open.

## Note of 2026-11-22: Widder and Schilling, read
<!-- inactive-ok-file: THEORY-tmpo4sos — Proposed; filed by LEAD-023 -->

Widder and Schilling ([THEORY-tmpo4sos](../theory.d/THEORY-tmpo4sos.md), bears_on; [NOTE-tmp2mtul](../notes.d/NOTE-tmp2mtul.md); [LIT-2250](../literature.d/LIT-2250.md)), the work A cited at A18. Two bearings on this question's list.

1. **Memory closure and independence.** "the memory term should be considered a coupling term that is not necessarily related to memory" (Conclusion). In their operator setting the convolution term is what the omitted subspace feeds back into the kept one, and it vanishes when the omitted subspace is invariant under the dynamics (§V). That is a link between memory closure under the declared projection and a form of dynamical independence of the omitted variables, in the direction independence ⇒ no memory, for linear evolution of observables. It is not the record's definition of either condition, so it supports the shape of the entailment the record found in VAR(1) ([CLAIM-389](../claims.d/CLAIM-389.md)) without testing the table's other cells.
2. **Sufficiency is not shown by having a closed equation.** For Mori's projection an exact generalized Langevin equation always exists and "does not reveal any non-trivial structure of the dynamics" (§III.A); fitted with Gaussian forces it reproduces only the autocorrelation put in (§III.C). A description can therefore meet a formal closure while carrying no predictive content beyond its inputs, which is a reason to keep predictive sufficiency and memory closure apart, as the question does.

The question stays open.
