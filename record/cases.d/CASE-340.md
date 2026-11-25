---
number: 340
status: Proposed
formerly:
- CASE-tmpczld2
title: "Many small closed groups of DeGroot averagers, each of size near the square root of log n, have a largest influence weight that vanishes while the chance that some group settles on a wrong consensus tends to one"
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-061 as a
    delegated worker. The construction is the promotion audit's sketch
    (batch 036, decision for THEORY-321); the computation and its tests are
    committed under scratch/studies/lead-061/.
standing: documented
kind: executed-study
tags:
- network-science
- probabilistic-modeling
- mathematics
date: '2026-11-22'
line:
- distributed-agency
- formal-apparatus
draws_on:
- THEORY-321
bears_on:
- QUESTION-184
summary: >-
  The audit's sketch for [QUESTION-184](../questions.d/QUESTION-184.md), checked against Golub and
  Jackson's definitions ([LIT-999](../literature.d/LIT-999.md), reread 2026-11-22) and computed
  exactly. n agents in m = n/k closed groups of k = ⌈√(ln n)⌉, equal
  weights inside each group, independent Bernoulli(1/2) signals. Under
  Theorem 3 every influence weight is 1/k, which tends to 0; under
  Definition 3 the society is wise only if the largest deviation over all
  agents tends to 0 in probability. The chance that some group's
  consensus is exactly 0 or 1, missing the truth by 1/2, is
  1 − (1 − 2^(1−k))^m, which tends to 1: 0.97 at n = 10, 0.9999 at
  n = 100, and 1 to six places from n = 10^4. A DeGroot iteration on a
  three-group matrix with transient members confirms Theorem 3's
  per-group normalization, and a Monte Carlo run agrees with the exact
  formula. With three groups, or with groups of size (ln n)², the same
  probability tends to 0. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---

# CASE-340: Many small closed groups of DeGroot averagers, each of size near the square root of log n, have a largest influence weight that vanishes while the chance that some group settles on a wrong consensus tends to one

## The case

**Construction.** For each n, split n agents into m = ⌊n/k⌋ minimal
closed groups of k = ⌈√(ln n)⌉ agents (take n a multiple of k). Inside a
group every agent weights every member, itself included, by 1/k, and no
one outside. Each T(n) is stochastic and strongly aperiodic (every group
has self-loops), so convergent by Golub and Jackson's Theorem 2. Signals
are independent Bernoulli(1/2): values in [0, 1], mean μ = 1/2, variance
1/4, so they meet the paper's assumptions with σ² = 1/4.

**What the paper's definitions give.** Theorem 3 (p. 137) defines the
influence vector s with Σ_{i∈B} s_i = 1 on *each* minimal closed group B
and s_i = 0 off them, so here every s_i = 1/k and s_1(n) = 1/k → 0.
Definition 3 (p. 123) calls the sequence wise if
plim_{n→∞} max_{i≤n} |p_i^(∞)(n) − μ| = 0, the maximum over all agents
("converge jointly in probability"). Each group's limit is its own
average of k signals.

**The computation** (scratch/studies/lead-061/, eight pytest tests,
results.md). The probability that some group is all ones or all zeros is
exactly 1 − (1 − 2^(1−k))^m:

| n | k | s_1 | log10 of expected groups at 0 or 1 | P(some group at 0 or 1) |
|---|---|---|---|---|
| 10 | 2 | 0.50 | 0.4 | 0.969 |
| 10^2 | 3 | 0.33 | 0.9 | 0.99993 |
| 10^4 | 4 | 0.25 | 2.5 | 1.000000 |
| 10^20 | 7 | 0.14 | 17.3 | 1.000000 |
| 10^400 | 31 | 0.032 | 389.5 | 1.000000 |

In general m·2^(1−k) ≥ (n/k − 1)·2^(−√(ln n)) → ∞, since
ln n − √(ln n)·ln 2 − ln k → ∞, and the groups are independent, so the
probability tends to 1 and the society is not wise although s_1 → 0.

**Checks.** A DeGroot iteration of 4,000 steps on a matrix with three
closed groups of four, random positive weights, and three transient
members reproduced Theorem 3: each group's limit is s_B·p_B with s
summing to 1 on each group (to 3 in all), and the transient members end
at mixtures of the three consensus values. A Monte Carlo run (2,000
replications each for m, k = 20, 3; 200, 4; 2,000, 5) agreed with the
exact formula (0.9955 against 0.9968 for the first).

**Contrasts that are wise** (ε = 0.1, exact): three groups of n/3 give
P(max deviation ≥ 0.1) of 9×10^−4 at n = 10^3 and 1.7×10^−30 at n = 10^4;
groups of k = ⌈(ln n)²⌉ give 10^−3 at n = 10^20 and 4×10^−72 at
n = 10^50, after staying near 1 up to n = 10^10.

## What it can show

That Golub and Jackson's Proposition 2, read with their own Theorem 3
and Definition 3, is false in its "if" direction for sequences whose
number of closed groups grows fast enough; the "only if" direction is
untouched. It is a construction inside the model, so it says nothing
about real groups, which is the other half of [QUESTION-184](../questions.d/QUESTION-184.md). The
contrasts show only that the failure needs the number of groups to grow
quickly relative to their sizes; the slow onset in the (ln n)² family is
a reminder that "tends to 0" can need astronomically large societies.
