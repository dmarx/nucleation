---
number: 1426
status: Active
formerly:
- THEORY-tmptcu66
title: 'Hua, Luo, Swersey and Wen solve the spatial hypercube queueing model with server-specific service rates by an iteration on a birth–death reformulation, and state a proof that, under their Assumption 3.1, a technical bound on how far the rates differ, it converges to the exact stationary distribution at a geometric rate'
version: 3
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Filed Proposed from NOTE-1618, which read §1, the model statement and
    §5's comparison, not the proof.
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted by the twenty-ninth status review, at the status
    review's ruling (the owner delegated these rulings); ADR-065; ADR-047,
    kind 3. NOTE-1618 v2 reads §§1–3 and the E-Companion's proofs. Theorem 1
    holds "Under Assumption 3.1", a bound on the rates' spread. The old
    title followed the abstract and left that condition out. That was a
    mis-statement, recorded here and in the note below. The title now
    reports the theorem as the authors state it. The old title: Hua, Luo,
    Swersey and Wen solve the spatial hypercube queueing model with
    server-specific service rates exactly, through a birth–death process
    and an equivalent reformulation whose iteration converges to the
    stationary distribution at a geometric rate. The old promote_when:
    "The convergence proof read and checked, confirming that for the
    spatial hypercube queueing model with server-specific exponential
    service rates the authors' iteration, built on a birth–death process
    and an equivalent reformulation, converges to the exact stationary
    distribution at a geometric rate." It was not met as worded: the proof
    checks for equal rates and has a gap for unequal ones. Whether the
    iteration converges for unequal rates, with or without the assumption,
    is QUESTION-434.
- version: 3
  date: '2026-11-11'
  note: >-
    Bears on QUESTION-434, from the reading review of 2026-11-11, by
    question, as a premise (ADR-060): the question asks whether the
    theorem this reading reports holds for unequal rates, and the
    reading's own text says so ("Whether the theorem holds for unequal
    rates, and whether the assumption is needed, is QUESTION-434"). No
    other change.
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-2111
summary: >-
  Hua, Luo, Swersey and Wen (2026), [LIT-2111](../literature.d/LIT-2111.md), read in [NOTE-1618](../notes.d/NOTE-1618.md) (§§1–3, §6
  and the E-Companion's proofs; §§4–5 skimmed). Theorem 1 states that their
  iteration converges geometrically to the exact stationary distribution,
  under Assumption 3.1, a technical bound on how far the rates differ. The
  abstract drops the condition. Active as a report of what the authors
  state. The proof checks for equal rates; for unequal rates it has a gap
  (see the note below). The reported speed-ups against a sparse solver,
  simulation and Larson's own method are not part of the account and were
  not checked.
bears_on:
- QUESTION-434
---

# THEORY-1426: Hua, Luo, Swersey and Wen solve the spatial hypercube queueing model with server-specific service rates by an iteration on a birth–death reformulation, and state a proof that, under their Assumption 3.1, a technical bound on how far the rates differ, it converges to the exact stationary distribution at a geometric rate

## Source

Hua, Luo, Swersey and Wen (2026), [LIT-2111](../literature.d/LIT-2111.md); read in [NOTE-1618](../notes.d/NOTE-1618.md).

## What was actually shown

- **The claim, as stated.** "we extend it to handle heterogeneous service
  rates by devising an exact solution through a birth-death process and an
  equivalent reformulation. We demonstrate that our algorithm converges to
  the exact solution at a geometric rate" (abstract). The introduction adds
  that the result extends to homogeneous rates and that the proof bounds
  the differences between consecutive iterations. Theorem 1 itself
  (p. 13): "Under Assumption 3.1, the CPU algorithm converges at a
  geometric rate". The authors call the assumption "a technical
  assumption. Its restrictiveness depends on the degree of heterogeneity
  in service rates among units". They say it holds automatically for equal
  rates and "is expected to hold for most real systems" (p. 12).
- **Its place.** Larson's alternating hyperplane approach is the earlier
  exact method for homogeneous rates (§1); against a reimplementation of
  it, "In the case of 20 units, our algorithm is approximately 83% faster
  in terms of total time" (§5).

The proof was read and checked in [NOTE-1618](../notes.d/NOTE-1618.md) v2; see the note below.

## What this does not say

- That the method scales without limit: exact solution still works over
  the 2^N states.
- That the geometric rate is fast. For equal rates the guaranteed factor
  is 1 − ∏ jν/∏(λ + jν), about 1 − 2 × 10⁻⁵ at a load of 5 with 20 units.
- That convergence for unequal rates is proved: see the note below.
- Anything about the approximation methods' accuracy, except that the
  authors say they lack convergence guarantees.
- Anything about facility location, districting or the value of a unit.

## Note of 2026-11-06: the proof, checked

The proof of Theorem 1 (E-Companion EC.1.3) bounds the change in each
layer's conditional probabilities as if the layer's departure rate were
fixed between iterations. It replaces |µ^{k+1}(n) p^{k+1} − µ^k(n) p^k| by
µ̄n |p^{k+1} − p^k|, citing only that both rates are at most µ̄n. That holds
when the rates are equal, since then µ(n) = nν, and there the argument
checks. For unequal rates the term |µ^{k+1}(n) − µ^k(n)| p^k is dropped
without a bound. So the published proof does not establish the theorem in
the case the paper is about.

The proof also says that ΦN = maxn Φn < 1 follows from Assumption 3.1.
That overreaches, harmlessly, since only layers 1 to N − 1 enter the
bound.

A re-implementation of the algorithm,
scratch/formal/hua_hypercube_convergence_check.py, uses the exact solution
of the full generator as a control. It converged in all 10 runs. Six of
them violate Assumption 3.1, one with rates within ±20% of each other.
Whether the theorem holds for unequal rates, and whether the assumption is
needed, is [QUESTION-434](../questions.d/QUESTION-434.md).
