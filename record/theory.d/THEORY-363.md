---
number: 363
status: Active
formerly:
- THEORY-tmp3ren6
title: "For finding the top k objects under a monotone combining function from m lists each sorted by one attribute, with sorted and random accesses the only costs, the threshold algorithm is correct and on every database costs at most a constant times what any correct algorithm that makes no wild guesses costs; the constant is m + m(m−1)c_R/c_S, no deterministic algorithm does better when the function is strict, and once wild guesses are allowed no algorithm has such a guarantee on databases with ties"
version: 1
tags:
- databases
- information-retrieval
date: '2026-10-15'
source:
- LIT-1115
summary: >-
  Fagin, Lotem and Naor (2001; full version read as arXiv cs/0204046v1),
  [LIT-1115](../literature.d/LIT-1115.md), read in [NOTE-924](../notes.d/NOTE-924.md). The threshold algorithm reads m
  attribute-sorted lists in parallel, looks up each new object's other
  grades, and stops when k seen objects score at least the combined score
  of the last grades read. For every monotone combining function it is
  instance optimal among correct algorithms that make no wild guesses
  (Theorem 6.1), with ratio m + m(m−1)c_R/c_S, tight for strict functions
  (Corollary 6.2, Theorem 9.1). It is a guarantee relative to a class of
  algorithms under an access-cost model. It does not say that top-k queries
  are cheap: the absolute cost depends on the data, and is linear in N for
  some conjunctive queries.
supports:
- CLAIM-311
- CLAIM-312
bears_on:
- QUESTION-114
---

# THEORY-363: For finding the top k objects under a monotone combining function from m lists each sorted by one attribute, with sorted and random accesses the only costs, the threshold algorithm is correct and on every database costs at most a constant times what any correct algorithm that makes no wild guesses costs; the constant is m + m(m−1)c_R/c_S, no deterministic algorithm does better when the function is strict, and once wild guesses are allowed no algorithm has such a guarantee on databases with ties

## Source

Fagin, Lotem and Naor (2001), [LIT-1115](../literature.d/LIT-1115.md), registered as the PODS 2001
paper. Read in full in [NOTE-924](../notes.d/NOTE-924.md) from the authors' full version, arXiv
cs/0204046v1 (2002), which the PODS paper abridges: Sections 1–12, all
theorems and proofs, and Table 1. The JCSS 2003 journal text was not
obtained.

## What was actually shown

**The model.** N objects with m grades in [0, 1]. Each of m lists holds
every object, sorted by one attribute's grade. Sorted access reads the next
entry of a list; random access fetches one named object's grade in one
list. Cost is s·c_S + r·c_R for s sorted and r random accesses. Computation,
and building or keeping the lists, are not counted. The combining function
t is monotone, so raising every grade never lowers the score. k and m are
constants.

**The algorithm and its correctness.** TA's threshold τ is t applied to the
last grade read in each list. No unseen object can score above τ, so TA
halts once k seen objects reach it (Theorem 4.1). Its buffers do not grow
with N (Theorem 4.2), and it never makes more sorted accesses than Fagin's
Algorithm.

**Instance optimality.** B is instance optimal over a class A of
algorithms and a class D of databases if B is in A and, for all A and D,
cost(B, D) ≤ c·cost(A, D) + c′; c is the optimality ratio. The paper notes
that this "is formally the same definition as is used in competitive
analysis", with B required to be in A. Theorem 6.1: for monotone t, over
all databases, TA is instance optimal among correct algorithms that make no
wild guesses, that is, that never random-access an object before seeing it
under sorted access. The ratio is at most m + m(m−1)c_R/c_S. With strict t
(score 1 exactly when every grade is 1, the paper's mark of a conjunction)
that ratio is exact and no deterministic algorithm does better (Corollary
6.2, Theorem 9.1). For max, which is not strict, TA stops after k rounds,
ratio m.

**The limits of the class.** If wild guesses are allowed, no algorithm is
instance optimal for min of two lists (Theorem 6.4), because of ties. If
every list's grades are distinct and t is strictly monotone, TA is instance
optimal even against guessing algorithms, with ratio at most c·m²,
c = max{c_R/c_S, c_S/c_R} (Theorem 6.5). Variants carry the result to
approximate answers (TA_θ), to lists without sorted access (TA_Z), and to
no random access (NRA, ratio m, tight for strict t).

**What could have come out otherwise.** A database on which some correct,
non-guessing algorithm stopped with fewer than a constant fraction of TA's
accesses, beyond the additive constant, would refute Theorem 6.1; a
deterministic algorithm with a ratio below m + m(m−1)c_R/c_S for a strict
t would refute Theorem 9.1.

## What this does not say

- **That top-k retrieval over sorted lists is cheap.** Instance
  optimality bounds TA's cost relative to the best possible on the same
  database. For some databases the best possible is about half the objects
  ([THEORY-361](THEORY-361.md)).
- **That the ratio is small.** It is quadratic in m when random access
  costs anything: with c_R = c_S and ten lists it is 100. The preprint's
  Table 1 prints the random-access term as m(m−1)/2 · c_R/c_S, half what
  its theorems and proofs give; the theorems are followed here.
- **Anything about the cost of building, choosing or keeping the lists.**
  The lists are given. Which attributes to sort on, and what an
  arrangement costs to make or maintain, are outside the model.
- **Anything for non-monotone scores.** A score that rises and then falls
  with one grade, such as a preference single-peaked in a ratio
  ([CLAIM-309](../claims.d/CLAIM-309.md)), gives no threshold, and none of these results applies.
- **Fagin's Algorithm's sublinear cost.** That bound is Fagin's, needs
  probabilistically independent orderings, and is reported, not proved,
  here ([THEORY-379](THEORY-379.md)).
- **Anything about perception.** The model counts accesses to sorted
  lists. Nothing in it is a claim about how a visual system searches.

## Connections

- [QUESTION-114](../questions.d/QUESTION-114.md): a cost model for querying a fixed set of single-attribute
  orders, with sequential and random reads priced separately. It is the
  query-side term only; build cost, upkeep and space are absent.
- [THEORY-348](THEORY-348.md): both are per-instance ratio guarantees with an additive
  constant. There the rival knows the future; here it is any correct
  algorithm on the same data, and against the best nondeterministic one
  the cost is the length of the shortest proof that the answer is right.
  In both the guaranteed ratio grows with the number of options, here with
  the number of lists.
- [THEORY-361](THEORY-361.md) is the paper's counterexample, and the case that bears on
  [THEORY-358](THEORY-358.md).
