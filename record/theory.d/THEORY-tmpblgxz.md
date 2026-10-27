---
status: Active
title: 'Causal scrubbing scores a hypothesis through the partitions of the dataset that its interpretation nodes induce, so two hypotheses that assign different features to a node but induce the same partition on the dataset, such as two features perfectly correlated on it, receive the same score'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmp4zrzd. It follows from the algorithm as the
    post defines it, which the authors state as a limitation; the record
    re-derived it from the pseudocode and checked it in a small simulation
    (ADR-047 v2).
tags:
- causality
- representation-learning
date: '2026-10-26'
source:
- LIT-tmpqtkua
summary: >-
  Chan et al. (2022), [LIT-tmpqtkua](../literature.d/LIT-tmpqtkua.md), read in [NOTE-tmp4zrzd](../notes.d/NOTE-tmp4zrzd.md). In the
  causal-scrubbing algorithm an interpretation node enters only through
  sample_agreeing_x, which draws a datum with an equal value of that node,
  so only the equivalence classes the node induces on the dataset matter.
  The authors say it themselves: the method "doesn't allow us to
  distinguish between two features that are perfectly correlated on our
  dataset". It does not say that a passing hypothesis is otherwise wrong,
  nor anything about features correlated only imperfectly.
---
<!-- inactive-ok-file: THEORY-802 CLAIM-tmpwr001 — Proposed; the account and claim this bears on, cited as open -->

# THEORY-tmpblgxz: Causal scrubbing scores a hypothesis through the partitions of the dataset that its interpretation nodes induce, so two hypotheses that assign different features to a node but induce the same partition on the dataset, such as two features perfectly correlated on it, receive the same score

## Source

Chan, Garriga-Alonso, Goldowsky-Dill, Greenblatt, Nitishinskaya,
Radhakrishnan, Shlegeris and Thomas (2022), *Causal scrubbing*,
[LIT-tmpqtkua](../literature.d/LIT-tmpqtkua.md), read in full in [NOTE-tmp4zrzd](../notes.d/NOTE-tmp4zrzd.md): §2 (hypotheses), §3.2 (the
algorithm and pseudocode) and §7 (limitations).

## What was actually shown

**The algorithm.** The scrubbed expectation is the mean of f over runs of
run_scrub from the output node of the interpretation I. At a node n_I with
image n_G = c(n_I), each important parent p_I is evaluated recursively on a
datum drawn by sample_agreeing_x(D, p_I, ref_x), which returns a uniform
draw from {x ∈ D : p_I(x) = p_I(ref_x)}; unimportant parents take their
values on one random datum. The interpretation enters at no other point.

**The re-derivation.** Let two hypotheses differ only in the function an
interpretation node computes, φ in one and ψ in the other, with the same
graph G and correspondence c. If φ(x) = φ(x′) exactly when ψ(x) = ψ(x′) for
all x, x′ in D, the agreeing sets are the same for every reference datum,
so every draw has the same distribution and the scrubbed expectations are
equal. Perfect correlation on D (a bijection between the values of φ and
ψ on D) is one case. The values the interpretation computes never reach
the model; only which data share a value does.

**The check.** In a toy where a hidden unit copies an input bit a, the
output is a ⊕ c, and a second input bit b equals a on every datum, the
hypothesis "the unit computes a" and the hypothesis "the unit computes b"
both score 1.0 over 20,000 scrubbed samples, while "the unit computes a
constant" scores 0.50 (record simulation, 2026-10-26).

**The authors' statement.** §7: causal scrubbing "doesn't allow us to
distinguish between two features that are perfectly correlated on our
dataset, since they would induce the same equivalence classes. In fact,
to the extent that two features A and B are highly correlated, causal
scrubbing will not complain if you misidentify an A-detector as a
B-detector." §2: the algorithm tests "that the equivalence classes on
inputs to n_I are the same as the equivalence classes on inputs to n_G",
which "is not strong enough to eliminate all incorrect hypotheses".

## What this does not say

- **Not that hypotheses inducing different partitions are well separated.**
  For features correlated imperfectly, the scores differ, by an amount
  this account does not bound.
- **Not that causal scrubbing is unsound otherwise.** Its other failure
  modes (omitted inhibitory circuits, independent resampling of correlated
  terms) are argued by the authors with examples and are not part of this
  account.
- **Not that the partition is all a hypothesis says.** The correspondence c
  and the choice of how G is rewritten are part of the hypothesis and do
  change the score; the account fixes them.
- **Not about other instruments.** Interchange intervention accuracy
  compares outputs of a high-level model, which do depend on the values
  the high-level variables take.

## Connections

- **[THEORY-802](THEORY-802.md) and [QUESTION-234](../questions.d/QUESTION-234.md).** A hypothesis may rewrite G, for
  example into rotated coordinates, before mapping into it. Two
  alignments related by a change of basis that induce the same partitions
  of D therefore tie under causal scrubbing by construction. That is a
  tie of the kind [THEORY-802](THEORY-802.md) asserts, but for a reason that holds of the
  instrument, not of trained networks, so it does not meet [THEORY-802](THEORY-802.md)'s
  promote_when.
- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** What passes the test is a partition of the data,
  not the variable that does the work.
