---
number: 362
status: Active
formerly:
- THEORY-tmp2ber8
title: "For nonrecursive Datalog or SQL views with safe stratified negation and stratified aggregation, under set or duplicate semantics, storing with each derived tuple only the number of its derivations suffices to maintain the view under insertions and deletions of base tuples: signed counts propagated through delta rules stratum by stratum give each tuple's change as its new count minus its old, a tuple leaves when its count reaches zero, and a MIN or MAX group whose extreme is deleted is recomputed from the stored lower stratum"
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Promoted, carrying out the promotion audit's decision for THEORY-362
    (batch 053, ADR-047 v2). The paper states Theorems 4.1, 6.1 and 6.2
    without proof; the dated note below re-derives them for nonrecursive
    programs, which meets the promote_when. The title now states the result
    as proved rather than as stated, and names what MIN and MAX need when a
    group's extreme is deleted.
tags:
- databases
- logic
date: '2026-10-15'
source:
- LIT-1114
summary: >-
  Gupta, Mumick and Subrahmanian (1993), [LIT-1114](../literature.d/LIT-1114.md), read in [NOTE-915](../notes.d/NOTE-915.md).
  Algorithm 4.1 evaluates delta rules in order of rule stratum and combines
  signed counts; Theorem 4.1 states it derives count(t^ν) − count(t) for
  every tuple, and Theorems 6.1 and 6.2 extend this to negated and
  aggregate subgoals. Its cost is argued to be close to evaluating the view
  and is not measured. All three theorems are stated without proof in this
  extended abstract. It does not say that a count suffices when support is
  cyclic: the paper keeps counting to nonrecursive views.
bears_on:
- QUESTION-105
---

# THEORY-362: For nonrecursive Datalog or SQL views with safe stratified negation and stratified aggregation, under set or duplicate semantics, storing with each derived tuple only the number of its derivations suffices to maintain the view under insertions and deletions of base tuples: signed counts propagated through delta rules stratum by stratum give each tuple's change as its new count minus its old, a tuple leaves when its count reaches zero, and a MIN or MAX group whose extreme is deleted is recomputed from the stored lower stratum

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

## Note of 2026-10-20: Theorems 4.1, 6.1 and 6.2, re-derived

Re-derived for the promotion audit (batch 053, [ADR-047](../decisions.d/ADR-047.md) v2).

1. **Counts are multiplicities.** Join multiplies them, union adds them,
   and projection sums over the tuples it merges. By induction on strata,
   a derived tuple's count is its number of derivations.
2. **The delta rule is an identity.** For a body s_1 & … & s_n with
   s_i^ν = s_i + Δ(s_i) as signed multiplicities, the product telescopes:
   Π s_i^ν − Π s_i = Σ_i (Π_{j<i} s_j^ν) Δ(s_i) (Π_{j>i} s_j). These are the
   paper's delta rules, with new values before position i and old ones
   after. Joins and sums distribute over the identity, so Δ(p) =
   count(p^ν) − count(p) exactly (Theorem 4.1). If the deleted base tuples
   were present, each new count is a count of derivations and so is never
   negative (Lemma 4.1).
3. **Strata and set semantics.** A stratum is evaluated only once those
   below it are complete, so each subgoal's old and new values are known.
   Under set semantics a subgoal enters as its membership indicator, with
   Δ ∈ {−1, 0, +1}. The same identity holds, which is why passing only
   membership changes upward is correct.
4. **Negation (Theorem 6.1).** A safe ¬q(t), with q lower, is the factor
   [count q^ν(t) = 0], and its old and new values are known. It is one more
   factor in step 2.
5. **Aggregation (Theorem 6.2).** A grouped aggregate over a lower stratum
   is a derived relation. Its change, deleting (g, a_old) and inserting
   (g, a_new) for each affected group, enters step 2 like any other Δ.
   COUNT, SUM and AVG update from the old value and the delta. MIN and MAX
   need the group's remaining tuples when the current extreme is deleted,
   and those tuples are in the stored lower stratum.

A check, with the recipe in the decision file: on 3,000 random instances
and changes, Algorithm 4.1 matched full re-evaluation every time. The
program had a bag join, a set-semantics stratum with negation and union,
and a grouped count.
