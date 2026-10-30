---
number: 564
status: Proposed
formerly:
- THEORY-tmpk6k4p
promote_when: >-
  Structure-learning runs of the same scheme on larger problems (many
  more slots and features, several initialisations) that report how often
  Bayesian model reduction recovers the generating number of hidden
  causes, against a non-parametric Bayesian learner on the same data. The
  account is supported if recovery stays high when the likelihood is
  learned, and refuted if it stays near Table 1's 45–80% or worse, or
  depends on the symmetry-breaking initialisation. Further toy
  demonstrations that a spare slot gets filled cannot settle it, since
  expansion was never in doubt; the open part is reduction.
title: "A bounded generative model can learn its own structure with no machinery beyond inference and learning: spare hidden-state slots with flat likelihoods get filled when an observation fits none of the learned causes, and Bayesian model reduction on the learned prior over states can return unneeded slots, though in a toy concept-learning task it recovers the true number of causes in only 45–80% of runs with four to seven causes, and never with two or three, unless the likelihood is given"
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Title corrected to Table 1 by the sixteenth status review, at the
    status review's ruling (the owner delegated these rulings; ADR-047,
    kind 3): the true number of concepts won in 45–80% of runs for four
    to seven, never for two or three, as NOTE-485's version 2 and this
    entry's body already say. Version 1's title ended: "though in a toy
    concept-learning task it recovers the true number of causes only
    45–80% of the time unless the likelihood is given". The claim is
    otherwise unchanged.
tags:
- model-comparison
- cognition
- probabilistic-modeling
date: '2026-10-16'
source:
- LIT-615
presupposes:
- THEORY-081
summary: >-
  Smith, Schwartenbeck, Parr and Friston (2020), [LIT-615](../literature.d/LIT-615.md), read in
  [NOTE-485](../notes.d/NOTE-485.md). Expansion works in the toy domain over eight runs per
  condition, and only for novel stimuli. Reduction is the weak half: over
  100 runs, the true number of concepts won in 45–80% of runs for four to
  seven, never for two or three, and in every run when the likelihood was
  given. Table 1 is the record's only measurement of how often reduction
  picks the generating structure when the parent model was itself
  learned. One initialisation; eight concepts, six binary features.
supports:
- CLAIM-337
---
<!-- inactive-ok-file: THEORY-079 — Proposed; named as a caution about model reduction, not leaned on -->

# THEORY-564: A bounded generative model can learn its own structure with no machinery beyond inference and learning: spare hidden-state slots with flat likelihoods get filled when an observation fits none of the learned causes, and Bayesian model reduction on the learned prior over states can return unneeded slots, though in a toy concept-learning task it recovers the true number of causes in only 45–80% of runs with four to seven causes, and never with two or three, unless the likelihood is given

## Source

Smith, Schwartenbeck, Parr and Friston (2020), [LIT-615](../literature.d/LIT-615.md) (*Frontiers in
Computational Neuroscience*), read in full in [NOTE-485](../notes.d/NOTE-485.md). The supplementary
script was not run.

## What was actually shown

**Setting.** A partially observed MDP with one hidden-state factor of up to
eight animals (four birds, four fish), three binary features and a report
factor. Dirichlet learning on the likelihood A and, for reduction, on the
prior over states D. Learning is unsupervised: reporting is disabled, so
there is no feedback. Gaussian noise of variance 0.001 breaks symmetry in
flat columns.

**Expansion (Figs. 4–5).**

- One new concept from a flat column: reporting reached 100% after about
  50 exposures to all eight animals, over eight runs.
- Two new concepts: mean accuracy 98.75% (SD 2%) after 2,000 trials.
- Four new birds: six of eight runs reached 92.50–98.8%; two stalled at
  72.50% by overgeneralising.
- With seven concepts known and one spare, 80 trials of known animals left
  the spare unused, and 20 trials of a new one filled it.

**Reduction (Table 1, 100 runs each).** The winning reduced model kept the
true number of concepts in 56 runs of 100 with seven presented, 69 with
six, 80 with five and 45 with four. With three presented, a two-concept
model won in 89 runs and the true model was second-best in 55; with two
presented, five-concept and four-concept models won (57 and 43). As
[NOTE-485](../notes.d/NOTE-485.md) transcribes the table, the true count never won for two or three
(its summary, which said "rarely", is corrected in its version 2). Wrong winners usually learned a coarser
concept, with a small evidence gap. With
the likelihood given and only D learned, the correct model won in every
run.

**What could have come out otherwise.** The spare slot could have absorbed
known animals, duplicating states. It did not. Reduction could have
recovered the true count reliably. It did not when the likelihood was
learned.

## What this does not say

- **That expansion is model comparison.** New slots are engaged by state
  inference and are not scored by evidence. Only removal uses reduction
  ([NOTE-485](../notes.d/NOTE-485.md), Limitations).
- **That the structure is learned from scratch.** The number of slots and
  the features are supplied by the modeller; that is the open question the
  authors name.
- **That reduction failures come from likelihood learning.** That is
  inferred from the given-likelihood control, not isolated (C4, weak).
- **That it scales.** Eight concepts, six binary features, two time points.
  Other initialisations of the noise changed Table 1's pattern.
- **That the brain has reserve columns or prunes in sleep.** Both are
  predictions with no direct evidence (C6, C7).

## Connections

- It applies the reduction identity of [THEORY-081](THEORY-081.md), that a model differing
  only in its prior has its evidence from the full posterior, in its
  Dirichlet form, to a parent model that was itself learned. [THEORY-079](THEORY-079.md)
  shows where reduction can mislead in singular models under the Laplace
  approximation; the Dirichlet form here is not that case, but the
  imperfect recovery is a reminder that the identity is exact only for the
  posterior it is given.
- The Raja et al. critique ([LIT-598](../literature.d/LIT-598.md)) bears on it: what the agent "learns" is
  bounded by slots and features the modeller supplied.

## Note of 2026-10-29: what holds it back

Kept Proposed by the sixteenth status review. [NOTE-485](../notes.d/NOTE-485.md) read the paper in
full, but the first clause, that a bounded generative model can learn its
own structure with no further machinery, generalises past one toy domain
of eight concepts and six binary features under one symmetry-breaking
initialisation. No larger runs compared with a non-parametric learner are
in the record. Narrowing it to the toy runs would make it promotable on
one study, but would free nothing while [CLAIM-337](../claims.d/CLAIM-337.md)'s other grounds,
[THEORY-662](THEORY-662.md) and [THEORY-577](THEORY-577.md), are Proposed.
