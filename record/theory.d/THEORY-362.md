---
number: 362
status: Proposed
formerly:
- THEORY-tmp2ber8
promote_when: >-
  A proof, read by the record, of Theorem 4.1 and its extensions to negation
  and aggregation (Theorems 6.1 and 6.2) under the stated conditions, in the
  1992 AT&T report or a later published treatment of counting-based
  maintenance. Further worked examples or experiments do not settle a
  correctness claim.
title: "For nonrecursive Datalog or SQL views with safe stratified negation and stratified aggregation, under set or duplicate semantics, storing with each derived tuple only the number of its derivations is stated to suffice to maintain the view under insertions and deletions of base tuples: signed counts propagated through delta rules stratum by stratum give each tuple's change as its new count minus its old, and a tuple leaves when its count reaches zero; the proof is not in the paper, and counting is set aside for recursive views because counts can be infinite"
version: 1
tags:
- databases
- logic
date: '2026-10-15'
source:
- LIT-1114
answers:
- QUESTION-105
summary: >-
  Gupta, Mumick and Subrahmanian (1993), [LIT-1114](../literature.d/LIT-1114.md), read in [NOTE-915](../notes.d/NOTE-915.md).
  Algorithm 4.1 evaluates delta rules in order of rule stratum and combines
  signed counts; Theorem 4.1 states it derives count(t^ν) − count(t) for
  every tuple, and Theorems 6.1 and 6.2 extend this to negated and
  aggregate subgoals. Its cost is argued to be close to evaluating the view
  and is not measured. All three theorems are stated without proof in this
  extended abstract. It does not say that a count suffices when support is
  cyclic: the paper keeps counting to nonrecursive views.
---

# THEORY-362: For nonrecursive Datalog or SQL views with safe stratified negation and stratified aggregation, under set or duplicate semantics, storing with each derived tuple only the number of its derivations is stated to suffice to maintain the view under insertions and deletions of base tuples: signed counts propagated through delta rules stratum by stratum give each tuple's change as its new count minus its old, and a tuple leaves when its count reaches zero; the proof is not in the paper, and counting is set aside for recursive views because counts can be infinite

## Source

Gupta, Mumick and Subrahmanian (1993), [LIT-1114](../literature.d/LIT-1114.md), SIGMOD '93 extended
abstract, pp. 157–166, read in full in [NOTE-915](../notes.d/NOTE-915.md) from a course-hosted
copy of the ACM PDF. The proofs are referred to a 1992 AT&T report the
record has not seen.

## What was actually shown

Stated, not proved. For a rule p :- s_1 & … & s_n the delta rules are
Δ(p) :- s_1^ν & … & s_{i−1}^ν & Δ(s_i) & s_{i+1} & … & s_n, new values
before position i and old after it. Algorithm 4.1 processes rules in
increasing stratum and sets P^ν = P ⊎ Δ(P), where ⊎ adds counts and drops
tuples whose count is 0, and a join multiplies counts. Theorem 4.1: the
algorithm derives Δ(t) with count count(t^ν) − count(t). Lemma 4.1: if the
deleted base tuples were in the database, no tuple loses more derivations
than it had. Theorems 6.1 and 6.2: the algorithm "works correctly" with
negated and with aggregate subgoals.

"Note that we store only the number of derivations, not the derivations
themselves." Under set semantics only changes in set membership are passed
to higher strata, which the abstract calls optimal: "it computes exactly
those view tuples that are inserted or deleted".

Cost is argued: since select, join, project and union derive one tuple per
derivation, "tracking counts for a nonrecursive view is almost as
efficient as evaluating the nonrecursive view." There are no experiments.

Could have come out otherwise: a nonrecursive program and change on which
the propagated counts differ from the recounted ones would refute
Theorem 4.1.

## What this does not say

- **That counts suffice under recursion.** Recursive queries "may have
  infinite counts associated with them", and counting "may not terminate
  on some views"; the paper proposes it for nonrecursive views only.
- **That it is cheap, as measured.** The cost claims are arguments.
- **That every aggregate is maintained from its old value.** The paper
  lists MIN and MAX as incrementally computable; deleting a group's current
  minimum or maximum needs the group's remaining tuples (the NOTE's
  observation, not the paper's).
- **That derived conclusions can be retracted directly.** Changes are to
  base tuples; a derived tuple leaves only when its derivations do.
- **That a count is provenance.** It says how many supports a tuple has,
  not which.

## Connections

- [QUESTION-105](../questions.d/QUESTION-105.md): for revisions given as base changes under a fixed acyclic
  program, a count per conclusion is a sufficient retained state beyond the
  base, the rules and the view; that is less than a dependency graph.
- [THEORY-347](THEORY-347.md): the edb plays the part of a belief base, and the revision is
  base revision with derived facts following their support.
- [CLAIM-303](../claims.d/CLAIM-303.md): dependency tracking paid at derivation time, argued to be
  nearly free for nonrecursive views.
- [THEORY-387](THEORY-387.md): the recursive case, where the paper drops counts.
