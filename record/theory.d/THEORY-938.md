---
number: 938
status: Proposed
formerly:
- THEORY-tmphhvqf
promote_when: >-
  The working paper's Propositions 3–5 checked against the journal version
  (JET 1997), and Proposition 5's absorption confirmed by an independent
  proof or a simulation of the discrete Cross process in a game whose
  replicator dynamic cycles (matching pennies), showing every run absorbed
  in a pure profile at small step sizes while the finite-horizon path
  tracks the replicator orbit. It is refuted by an error in the
  application of Norman's theorems, or by a run of the unmodified process
  that stays interior. Results for other learning rules (with exploration,
  aspiration levels or softmax choice) neither promote nor refute it.
title: 'Cross learning has the expected motion of the replicator dynamic and follows it on any finite horizon in the continuous-time limit, but for every learning speed the discrete process converges with probability one to a pure strategy profile, even in games where the replicator dynamic cycles'
version: 1
tags:
- game-theory
- learning-and-conditioning
date: '2026-10-24'
source:
- LIT-1505
summary: >-
  Börgers & Sarin (JET 1997; working paper 1993), [LIT-1505](../literature.d/LIT-1505.md), read in
  full from the 1995 working paper in [NOTE-1149](../notes.d/NOTE-1149.md). Two players running
  Cross's rule with payoffs in (0, 1): expected change equals the discrete
  replicator step (Proposition 3); the slow-learning limit is the Taylor
  replicator dynamic at each finite time (Proposition 4); for every step
  size the process is absorbed in a pure profile with probability one
  (Proposition 5). The equivalence is pointwise in time, not uniform.
---
<!-- inactive-ok-file: NOTE-1149 THEORY-905 CLAIM-444 CLAIM-443 CLAIM-446 CLAIM-451 — Proposed or new; the source and the accounts this bears on, named -->

# THEORY-938: Cross learning has the expected motion of the replicator dynamic and follows it on any finite horizon in the continuous-time limit, but for every learning speed the discrete process converges with probability one to a pure strategy profile, even in games where the replicator dynamic cycles

## Source

Tilman Börgers and Rajiv Sarin, "Learning through reinforcement and
replicator dynamics", *Journal of Economic Theory* 77(1):1–14 (1997),
[LIT-1505](../literature.d/LIT-1505.md), read in full in [NOTE-1149](../notes.d/NOTE-1149.md) from the working paper of
October 1995 (Propositions 3–5, pp. 11–17). The journal version was not
read.

## What was actually shown

- **Expected motion.** A player who plays j and receives Ũ ∈ (0, 1) moves a
  fraction Ũ of the way to the vertex j. The conditional expected change is
  p_j(e_j Ũ q − p Ũ q), the discrete replicator step (Proposition 3). I
  re-derived it.
- **Finite horizons.** With steps scaled by θ, as θ → 0 and nθ → t the
  process converges in probability to the solution of the continuous Taylor
  replicator equation at t (Proposition 4, from Norman's theorem on slow
  learning).
- **Infinity.** For every θ > 0 and every initial state, the process
  converges almost surely to a pure strategy pair (Proposition 5), and from
  an interior start every pure pair can be the limit (footnote 20). In
  matching pennies the replicator dynamic cycles around the mixed
  equilibrium, and the learner is absorbed in a corner. The authors' word
  for the gap is that convergence is "pointwise, but not uniformly on the
  complete real line" (p. 17).

What could have come out otherwise: the slow-learning limit could have
carried the replicator dynamic's long-run behaviour with it. It does not,
for any step size.

## What this does not say

- **That learning in general is replicator dynamics.** One rule, with
  payoffs read as reinforcement strengths in (0, 1). With negative payoffs
  the limit changes ([THEORY-934](THEORY-934.md)).
- **That the long-run behaviour of the replicator dynamic predicts a
  learner's.** The theorem says the reverse.
- **That absorption is fast.** No rate is given. At small θ the process
  follows the replicator orbit for a long time before absorption.
- **Anything about populations of imitators.** The analogy is inside one
  learner; imitation is set aside as complementary (p. 6).

## Connections

- **[THEORY-899](THEORY-899.md).** Soma et al.'s Proposition 1 rests on this. The
  macro-agent identity is of expected motion, and inherits this theorem's
  limit at infinity.
- **[CASE-155](../cases.d/CASE-155.md) and [CLAIM-444](../claims.d/CLAIM-444.md).** The replicator reading of authority
  holds for finite horizons. Rest points, cycles and thresholds read off the
  mean dynamic say what a realized organization does on the way, not where
  a single learner ends.
- **[CLAIM-443](../claims.d/CLAIM-443.md) and [CLAIM-446](../claims.d/CLAIM-446.md).** Absorption with no feedback from
  evidence or authority: reinforcement of what was chosen, with no return
  path, suffices for lock-in. It narrows the claims' mechanism and supports
  their worry.
- **[THEORY-905](THEORY-905.md).** The single-learner counterpart of loss of types in a
  finite imitating population.
