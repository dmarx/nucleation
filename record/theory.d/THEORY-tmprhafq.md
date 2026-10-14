---
status: Proposed
promote_when: >-
  A second, independent derivation or textbook statement of the bound
  and its attainability conditions, separating the deterministic case
  (attained iff the group distributions are permutations of one another)
  from the stochastic case (attained iff each group distribution is a
  deterministic coarsening of one common output distribution, which a
  quantile common refinement always supplies under disjoint supports).
  It is refuted by an erasure Z = f(X) with I(Z;A) = 0 and
  I(Z;X) > H(X|A), or by a deterministic erasure reaching the bound on
  groups that are not permutations of one another. What cannot settle
  it: benchmark comparisons of erasure algorithms on estimated
  distributions, which measure an estimator, not the limit.
title: "Perfect concept erasure caps what a representation can keep at the information not about the concept: if Z is independent of A then I(Z;X) is at most H(X|A), and a deterministic erasure reaches that cap only when the concept groups' distributions are permutations of one another"
version: 1
tags:
- information-theory
- representation-learning
date: '2026-10-14'
source:
- LIT-963
summary: >-
  Chowdhury et al. (2025), [LIT-963](../literature.d/LIT-963.md), read in full in [NOTE-tmpzvbap](../notes.d/NOTE-tmpzvbap.md). The cap
  (Lemma 3.3) is a two-line chain-rule argument that needs only the Markov
  condition A → X → Z. The permutation condition is proved necessary and
  sufficient for deterministic maps (Appendices A.3 and A.4), with finite
  supports and disjoint groups. The paper's further statement, that the
  cap cannot be reached when the groups are not permutations, is false for
  stochastic maps, which reach it for any finite distributions with
  disjoint supports.
answers:
- QUESTION-010
---
<!-- inactive-ok-file: THEORY-199 — Proposed; the partial answer of the same shape, open -->

# THEORY-tmprhafq: Perfect concept erasure caps what a representation can keep at the information not about the concept: if Z is independent of A then I(Z;X) is at most H(X|A), and a deterministic erasure reaches that cap only when the concept groups' distributions are permutations of one another

## Source

Chowdhury, Dubey, Beirami, Kidambi, Monath, Ahmed and Chaturvedi (2025),
[LIT-963](../literature.d/LIT-963.md), AISTATS 2025, read in full in [NOTE-tmpzvbap](../notes.d/NOTE-tmpzvbap.md): Lemma 3.3 with its
proof (A.2), Definition 4.1 with its justification (A.3), and Method 4.2
with its justification (A.4). The bounds build on Calmon et al. (2015,
2017), not held here.

## What was actually shown

- **The cap.** For any erasure Z = f(X), possibly stochastic, with
  A → X → Z, the chain rule gives I(Z;X) = I(Z;A) + I(Z;X|A) − I(Z;A|X).
  With I(Z;A) = 0 and I(Z;A|X) = 0 this is I(Z;X|A) ≤ H(X|A), with
  equality iff H(X|Z,A) = 0. Nothing else is assumed.
- **Deterministic attainment.** Under finite supports and disjoint group
  supports (A2–A4), a deterministic piecewise map attains the cap iff the
  groups' conditional distributions have equal support sizes and are
  permutations of each other. Equality forces each group's map to be
  one-to-one. Zero leakage forces equal output distributions across
  groups (strict concavity of entropy). Mapping each group bijectively
  onto a common Q achieves both.
- **Positive utility is possible.** With |𝒳| > |𝒜|, zero leakage is
  compatible with positive utility (Lemma 3.2, via Calmon et al.). A
  constant map is always perfectly erasing and useless.

The cap could have failed only through an error in the chain rule. The
attainment condition could have failed: A.3 is an argument that a weaker
condition does not suffice for deterministic maps, and it holds.

## What this does not say

- **Not that unequal groups put the cap out of reach.** The paper says
  so (§4), but its necessity argument covers deterministic maps only.
  Stochastic maps can reach the cap whenever each group's distribution
  is a coarsening of one common Q. Under disjoint supports a quantile
  common refinement always supplies such a Q; [NOTE-tmpzvbap](../notes.d/NOTE-tmpzvbap.md) gives the
  construction and a numerical check. The cost is a larger output
  support. The paper's own algorithm for unequal groups is stochastic and
  does not use this.
- **Not a statement about tasks.** Utility is I(Z;X), information about
  the whole representation. The task-level consequence, I(Z;B) ≤ H(B|A)
  for any B, follows by the same chain rule but is this record's step,
  not the paper's.
- **Not about overlapping concept groups.** Disjoint supports make A a
  function of X. Then the cap is H(X) − H(A): perfect erasure costs at
  least the concept's entropy. With overlap, the attainment analysis does
  not apply.
- **Not about relaxed erasure.** For leakage ε > 0 the paper has only
  Calmon et al.'s bracket max{0, u − H(X|A)} ≤ ε(u) ≤ u·I(A;X)/H(X), and
  defers the attaining functions.
- **Not that PEF is the best erasure in practice.** Its empirical lead
  rests on known or KDE-estimated distributions, V-information lower
  bounds and two real datasets. That comparison is ML practice and
  belongs to the anthology.

## Connections

- **[QUESTION-010](../questions.d/QUESTION-010.md).** A one-step partial answer. A representation can be
  made to carry nothing about one variable while keeping everything
  about the rest that is not shared with it, and no more. So one task
  family can be destroyed while another is kept, exactly to the extent
  the second does not run through the first. Like [THEORY-199](THEORY-199.md), it is
  single-step and about an ideal procedure that knows the distributions.
  It says nothing about chains or about relations as opposed to a
  categorical label.
- **[THEORY-199](THEORY-199.md).** The same shape of answer by a different route. There,
  noise destroys a top-level class while low-level features survive.
  Here, a designed map destroys a chosen label at a known information
  price.
