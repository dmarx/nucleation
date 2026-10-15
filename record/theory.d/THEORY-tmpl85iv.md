---
status: Active
title: "Belief bases with the same logical closure can revise to opposite conclusions on the same input, so a closed belief set does not fix its own revision; partial meet contraction of a base need not satisfy Recovery, and bases keep distinct inconsistent states apart, while a belief-set model reproduces the base difference only by attaching a different selection mechanism to the same set"
version: 1
tags:
- logic
- epistemology
date: '2026-10-15'
source:
- LIT-1072
- LIT-1050
answers:
- QUESTION-105
extends:
- THEORY-tmpr0fcd
summary: >-
  Hansson's Stanford Encyclopedia survey (2006, revised 2026), [LIT-1072](../literature.d/LIT-1072.md), read in
  [NOTE-866](../notes.d/NOTE-866.md), with Alchourrón, Gärdenfors and Makinson (1985), [LIT-1050](../literature.d/LIT-1050.md), read in
  [NOTE-874](../notes.d/NOTE-874.md). Bases {p, q} and {p, p ↔ q} have one closure, yet revised by ¬p one
  yields q and the other ¬q: statically but not dynamically equivalent. Base
  contraction escapes the Recovery that AGM proves for closed theories, and many
  inconsistent bases exist where there is one inconsistent closed set. A base
  marks which beliefs are held in their own right and recomputes the rest; it is
  not a record of reasons, sources or defeated alternatives, and the survey gives
  no result that bases handle iterated revision better.
supports:
- CLAIM-294
---

# THEORY-tmpl85iv: Belief bases with the same logical closure can revise to opposite conclusions on the same input, so a closed belief set does not fix its own revision; partial meet contraction of a base need not satisfy Recovery, and bases keep distinct inconsistent states apart, while a belief-set model reproduces the base difference only by attaching a different selection mechanism to the same set

## Source

Hansson, Logic of Belief Revision, [LIT-1072](../literature.d/LIT-1072.md), Stanford Encyclopedia of
Philosophy, revision of 29 July 2026, read in full in [NOTE-866](../notes.d/NOTE-866.md) (sections 2, 5,
7.7–7.8 and 8). It is a survey: results are stated, not proved. Alchourrón,
Gärdenfors and Makinson (1985), [LIT-1050](../literature.d/LIT-1050.md), read in [NOTE-874](../notes.d/NOTE-874.md), for Recovery over
closed theories (Lemma 2.1).

## What was actually shown

**Static against dynamic equivalence.** A base's "elements represent beliefs
that are held independently of any other belief or set of beliefs. Those
elements of the belief set that are not in the belief base are “merely
derived”". The bases {p, q} and {p, p ↔ q} "have the same logical closure. They
are therefore statically equivalent, in the sense of representing the same
beliefs." Abe holds the first, Bob the second; both revise by ¬p, and "Abe
believes that q whereas Bob believes that ¬q." The example is checkable by hand:
the only maximal subset of each base not implying p drops p and keeps the other
element.

**The belief-set reply.** "(In belief set models, cases like these are taken
care of by assuming that although Abe’s and Bob’s belief states are represented
by the same belief set, this belief set is associated with different selection
mechanisms in the two cases.)" The same difference can be carried by an
ordering attached to the closed set ([THEORY-tmpr0fcd](THEORY-tmpr0fcd.md)).

**Recovery.** Over a closed theory, even full meet contraction satisfies
Recovery ([LIT-1050](../literature.d/LIT-1050.md), Lemma 2.1). "Recovery does not hold for partial meet
contraction of belief bases." In Levi's coin example, contracting the base
{p_1, …, p_n, c, h}, with h implying c, by c removes h, and adding c back does
not restore h; on the closed set, Recovery would.

**Inconsistent states.** "There is only one inconsistent belief set (logically
closed inconsistent set), namely the whole language." Many inconsistent bases
exist, so operations such as consolidation, external revision and semi-revision
are defined on bases and have no counterpart on closed sets: "Once an
inconsistent belief set has been obtained, all distinctions have been lost, and
consolidation cannot restore them."

## What this does not say

- **That a base records why a belief is held.** A sentence is basic or derived,
  and support is logical implication from the base, computed, not stored. The
  survey does not discuss sources, derivations or defeated alternatives; truth
  maintenance systems appear once, as history.
- **That bases are needed for the difference.** For single revisions an ordering
  on the closed set does the same work. Which of the two retained states is
  smaller, or which an optimum resembles, is not addressed.
- **That bases do better under iteration.** The survey's iterated-revision
  section treats sets and bases alike and gives no base-specific result. Most
  proposals there carry an ordering of worlds or an entrenchment relation.
- **That rejecting Recovery is settled.** For closed sets "The construction of a
  plausible operation of contraction for belief sets that does not satisfy
  Recovery is still an open issue." The base characterizations the survey
  reports (Success, Inclusion, Relevance, Uniformity) are cited to Hansson 1999,
  which the record does not hold.
- **That the split is foundationalism against coherentism.** The survey says the
  distinction "should not be equated with that between foundationalism and
  coherentism."

## Connections

- For [QUESTION-105](../questions.d/QUESTION-105.md) it narrows the one-step answer: two retained states of
  different form, a base or an ordering, each suffice for single revisions, and
  neither is provenance, dependencies or defeated alternatives.
- [CLAIM-294](../claims.d/CLAIM-294.md) is the probabilistic form of the Abe and Bob case: same current
  conclusions, different revisions. [CLAIM-295](../claims.d/CLAIM-295.md)'s question, whether a record of
  justifications adds anything, is not answered here; bases widen the operations
  that stay well defined, which is not the same thing.
