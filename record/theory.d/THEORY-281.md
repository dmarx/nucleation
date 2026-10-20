---
number: 281
status: Active
formerly:
- THEORY-tmprhafq
title: 'Perfect concept erasure caps what a representation can keep at the information not about the concept: for X of finite support, if Z is independent of A then I(Z;X) is at most H(X|A), and a deterministic erasure reaches that cap only when the concept groups'' distributions are permutations of one another'
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision
    for THEORY-281 (batch 051, ADR-047 v2). The dated note below
    re-derives the cap, the necessity of the permutation condition for
    deterministic erasure, its sufficiency under disjoint groups, and
    the stochastic attainment condition the body states. The title is
    narrowed to X of finite support, where every entropy is finite.
    The promote_when's request for an independent derivation is met by
    the note.
tags:
- information-theory
- representation-learning
date: '2026-10-14'
source:
- LIT-963
summary: >-
  Chowdhury et al. (2025), [LIT-963](../literature.d/LIT-963.md), read in full in [NOTE-820](../notes.d/NOTE-820.md). The cap
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

# THEORY-281: Perfect concept erasure caps what a representation can keep at the information not about the concept: for X of finite support, if Z is independent of A then I(Z;X) is at most H(X|A), and a deterministic erasure reaches that cap only when the concept groups' distributions are permutations of one another

## Source

Chowdhury, Dubey, Beirami, Kidambi, Monath, Ahmed and Chaturvedi (2025),
[LIT-963](../literature.d/LIT-963.md), AISTATS 2025, read in full in [NOTE-820](../notes.d/NOTE-820.md): Lemma 3.3 with its
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
  common refinement always supplies such a Q; [NOTE-820](../notes.d/NOTE-820.md) gives the
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

## Note of 2026-10-20: the cap and its attainment, re-derived

Re-derived for the promotion audit (batch 051, [ADR-047](../decisions.d/ADR-047.md) v2). X has finite
support; A is the concept; Z is produced from X alone, possibly with
independent randomness, so A → X → Z.

1. **The cap.** I(Z; X, A) expands two ways, as I(Z;X) + I(Z;A|X) and as
   I(Z;A) + I(Z;X|A). The Markov condition gives I(Z;A|X) = 0, and
   perfect erasure gives I(Z;A) = 0. So I(Z;X) = I(Z;X|A) = H(X|A) −
   H(X|Z,A) ≤ H(X|A), with equality iff H(X|Z,A) = 0, that is, iff X is a
   function of (Z, A).
2. **Deterministic necessity.** Let Z = f(X). Equality forces f to be
   one-to-one on the support of each group's distribution p_a. Zero leakage
   forces Z given A = a to have one law Q for every a. A one-to-one image of
   p_a is p_a relabelled, so every p_a has the point masses of Q: the
   groups' distributions are permutations of one another. This direction
   uses neither disjoint groups nor strict concavity of entropy.
3. **Deterministic sufficiency.** Under disjoint group supports, if the
   p_a are permutations of a common Q, map each group's support one-to-one
   onto Q's support, matching masses. Then Z given A = a is Q for every a,
   and f is one-to-one on each group, so both conditions in 1 hold.
4. **Stochastic attainment.** H(X|Z,A) = 0 means x = g_a(z) on group a, so
   each p_a is a deterministic coarsening of the common law Q of Z.
   Conversely, given such a Q and g_a, draw Z from Q conditioned on
   g_A(Z) = X. Under disjoint finite supports, the common refinement of the
   groups' cumulative partitions of [0, 1] supplies Q. This is the
   correction the body makes to the paper's §4.
