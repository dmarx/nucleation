---
number: 66
status: Open
formerly:
- LEAD-tmpazs93
title: 'Bound the commutator of Conjecture A''s kind for the hierarchy question, reading Nadler and colleagues first'
version: 1
stage: idea
priority: medium
method:
- reading
- formal
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
line:
- learned-structure
advances:
- QUESTION-217
operationalized_in:
- CASE-tmp99n89
summary: >-
  Named in [NOTE-985](../notes.d/NOTE-985.md). Filed by the backlog audit of 2026-11-19.
---

# LEAD-066: Bound the commutator of Conjecture A's kind for the hierarchy question, reading Nadler and colleagues first

## What it would do

Register and read Nadler and colleagues, then attempt the commutator bound
[NOTE-985](../notes.d/NOTE-985.md) describes.

Where the record names it:

- [NOTE-985](../notes.d/NOTE-985.md): "Nadler et al. is the next reading"

## What would count

A bound gives [QUESTION-217](../questions.d/QUESTION-217.md) a formal half beside the synthetic-tree study.


## Note of 2026-11-22: carried out

<!-- inactive-ok-file: CASE-tmp99n89 CLAIM-tmpo8cwu — new; the study and claim of this lead, filed 2026-11-22 -->

The reading half was already done: Nadler and colleagues are LIT-1250,
read in NOTE-986, which found no bound there (the gap-to-cluster link is
heuristic). The formal half was done on 2026-11-22
(scratch/studies/lead-066/, with twelve tests), building on LEAD-052's
exact case, in which every kernel of inner products and norms commutes
with the level projectors on tree-symmetric data. CLAIM-tmpo8cwu
(demonstrated) proves the bound: for a learner whose residual obeys
ė = −A e with A symmetric positive semidefinite, ‖[A, P_ℓ]‖ is the coupling
between level ℓ and the rest, and level ℓ's relative residual departs from
a flow without cross-level coupling by at most ‖[A, P_ℓ]‖ over the level's
slowest rate and its share of the target, at every time, with a constant
that cannot be improved. It follows that acquisition times lie in
intervals, that the symmetric order survives perturbations below a
threshold proportional to the rate gaps, that below a risk of about the
square of that ratio the levels' times converge, and, for a moving
operator, that A2's ∫‖[A_t, P_ℓ]‖dt bounds the departure, more sharply when
damped at the level's own rate. CASE-tmp99n89 checks all of it on
perturbed tree data, three exact kernels and trained two-layer ReLU
networks; nothing failed, and the integral form was vacuous in the
networks while the damped form was not.

What remains: the order of the decoupled flow under a moving operator
(how each level's own block moves in feature learning), learners outside
squared loss and plain gradient descent, deviations from the tree that are
structured rather than Gaussian, and the relevance order, which this bound
does not touch.

