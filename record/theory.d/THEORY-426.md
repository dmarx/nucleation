---
number: 426
status: Active
formerly:
- THEORY-tmp38ky3
title: "Evaluating expected free energy recursively over the beliefs an agent would hold after each plausible outcome makes active inference a pruned tree search over belief states, formally analogous to Bellman recursion; in single deterministic runs on a T-maze and an 8 × 8 maze it planned through short-term costs that agents with a shorter horizon did not; that the pruning keeps deep search tractable beyond toy problems is argued, not shown"
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed and promoted by the twenty-fourth status review, at the status
    review's ruling (the owner delegated these rulings); ADR-065, ADR-057.
    NOTE-454 read the paper in full, as prose, and nothing in the record
    contradicts it. The equations were not recoverable, so the
    construction is reported from the prose of Eq. 1.11. The planning
    result now keeps the paper's own scope: single deterministic runs on a
    T-maze and an 8 × 8 maze (NOTE-454, C2). The old title stated that
    result generally. The old title: Evaluating expected free energy recursively over the beliefs an agent would hold after each plausible outcome makes active inference a pruned tree search over belief states, formally analogous to Bellman recursion, which lets the agent plan through short-term costs that one-step agents cannot; that the pruning keeps deep search tractable beyond toy problems is argued, not shown. The old promote_when asked for
    more than the narrowed title claims: "A comparison on shared tasks
    larger than toy mazes, with variance over runs, between sophisticated
    active inference and a Bayes-adaptive planner (for example Monte Carlo
    tree search over belief states), that reports both what each solves
    and the number of belief states each evaluates as the horizon and the
    number of plausible outcomes grow. Promote if the pruned recursion
    solves problems one-step expected free energy cannot, at a cost that
    stays far below the full tree where many outcomes remain plausible.
    More single deterministic runs on toy problems cannot settle it, and
    neither can a further derivation of which objectives are special
    cases." The old title, as the wide form the paper asserts, moves with
    that condition, both word for word, to THEORY-tmpvevpl, Proposed, which extends
    this entry (ADR-065 §3; ADR-047, kind 1).
tags:
- probabilistic-modeling
- information-theory
date: '2026-10-16'
source:
- LIT-577
summary: >-
  Friston, Da Costa, Hafner, Hesp & Parr (2020), [LIT-577](../literature.d/LIT-577.md), read in
  [NOTE-454](../notes.d/NOTE-454.md) as prose: the equations were not recoverable from the text
  layer. The recursion is a construction (strong). That it plans through
  costs rests on single deterministic runs of a T-maze and an 8 × 8 maze.
  The title keeps that scope. Active as a report of the construction and
  of those runs; the general form is THEORY-tmpvevpl, Proposed.
---

<!-- inactive-ok-file: THEORY-045 THEORY-285 — Proposed; named as the record's other active-inference accounts, nothing here rests on them -->

# THEORY-426: Evaluating expected free energy recursively over the beliefs an agent would hold after each plausible outcome makes active inference a pruned tree search over belief states, formally analogous to Bellman recursion; in single deterministic runs on a T-maze and an 8 × 8 maze it planned through short-term costs that agents with a shorter horizon did not; that the pruning keeps deep search tractable beyond toy problems is argued, not shown

## Source

Friston, Da Costa, Hafner, Hesp & Parr (2020), "Sophisticated Inference",
[LIT-577](../literature.d/LIT-577.md), read in full as prose in [NOTE-454](../notes.d/NOTE-454.md). No equation is reproduced
there, so the account rests on the prose that states the recursion. The
simulation code was not run.

## What was actually shown

**The construction (Eq. 1.11, in prose).** The expected free energy of a
next action is its risk plus its ambiguity plus the average, over
predicted outcomes and then over subsequent actions, of the expected free
energy of those actions. A softmax of the accumulated average is the
prior over the next action. It has the recursive form of Bellman's
equation, over functionals of beliefs rather than functions of states,
and the paper says it recovers Bayes-adaptive RL in the zero-temperature
limit.

**Planning through costs.** In a T-maze (32 trials, 95% cue validity),
with the cue given a cost of 1, the sophisticated agent still visits the
cue and switches to exploitation at trial 12; the one-step agent never
leaves the centre. In an 8 × 8 maze, horizons one to three stick behind
the barrier nearest the target, and horizon four finds the eight-move
shortest path.

**Cost.** Of about 10¹⁰ (horizon four) or 10¹⁵ (horizon six) potential
paths, "usually several hundred" are evaluated, in "a few hundred
milliseconds", because predictive probabilities below 1/16 are not
expanded.

What could have come out otherwise: the horizon-four agent could have
failed the maze, and the costly cue could have stopped the sophisticated
agent too. Neither happened, in single deterministic runs.

## What this does not say

- **That the search scales.** Scaling is argued from pruning and
  sparsity. Where many outcomes stay plausible, the 1/16 threshold cuts
  little, and no such problem is tried ([NOTE-454](../notes.d/NOTE-454.md), Open questions).
- **That it beats reinforcement-learning planners.** No Bayes-adaptive or
  Monte Carlo planner is run on the same tasks.
- **That the special-case derivations ground it in physics.** The appendix
  casts expected utility, KL control, optimal design, curiosity,
  empowerment and the information bottleneck as special cases. The
  nonequilibrium steady-state grounding is cited, not developed (C6,
  weak), and it is what the critiques filed beside the paper ([LIT-603](../literature.d/LIT-603.md),
  [LIT-598](../literature.d/LIT-598.md)) dispute.
- **That information gain is intrinsic motivation.** The identification
  is by name; the record's self-determination holdings ([LIT-558](../literature.d/LIT-558.md), [LIT-559](../literature.d/LIT-559.md))
  define intrinsic motivation otherwise.
- **That the agent perceives or acts in any rich sense.** The rat is
  given A, B, C and D, its location is observed, and moves are primitive,
  which is Raja et al.'s point ([LIT-598](../literature.d/LIT-598.md)).
- **That it plans through costs in general.** That, with tractability, is
  [THEORY-tmpvevpl](THEORY-tmpvevpl.md), Proposed.

## Connections

- [THEORY-045](THEORY-045.md) and [THEORY-285](THEORY-285.md) are the record's other active-inference
  accounts, about affect and about post-traumatic context inference.
  Neither rests on this recursion.
- The planning analogy is to Bayes-adaptive RL (Åström, Duff, Ross et
  al.), which the record does not hold.
