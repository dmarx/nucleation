---
status: Proposed
promote_when: >-
  An experiment in Tetris or a task like it in which the cost or availability of
  the physical action is varied (a delay on the rotate key, or rotation disabled
  until a piece is fully in view) and the internal computation it is said to
  replace is measured directly, as decision time, placement errors or a
  working-memory probe. It promotes the account if extra and early rotations fall
  as the action gets dearer and placement time or error rises where they are
  blocked; it refutes the epistemic reading if blocking them costs nothing. More
  keystroke counts, or another comparison of physical with mental rotation time,
  cannot settle it: those re-establish that the moves happen and are fast, which
  is already held.
title: "Tetris players rotate pieces more often and earlier than planning a placement and then executing it requires, rotating within a few hundred milliseconds of a piece appearing and checking the column more the higher the drop; Kirsh and Maglio read these moves as physical action standing in for mental computation at the moment of use, a saving argued from timing, not measured"
version: 1
tags:
- cognition
- embodied-cognition
date: '2026-10-15'
source:
- LIT-1054
- LIT-1076
answers:
- QUESTION-095
summary: >-
  Kirsh and Maglio (1994), [LIT-1054](../literature.d/LIT-1054.md), read in [NOTE-878](../notes.d/NOTE-878.md), with Kirsh (1995), [LIT-1076](../literature.d/LIT-1076.md),
  read in [NOTE-871](../notes.d/NOTE-871.md). In Tetris keystroke data, pieces are rotated more than
  plan-then-act would need, rotation starts by 400–600 ms, and a translate-to-wall
  check precedes longer drops. The authors define an epistemic action as one whose
  primary function is to cut the space, time or unreliability of the agent's own
  computation, and argue these moves are of that kind. The saving is argued from a
  three-player pilot comparing physical with mental rotation, not measured in
  performance. The trade is offloading at the moment of use, once, with nothing
  stored; the paper sets itself against caching.
---

# THEORY-tmpzye1b: Tetris players rotate pieces more often and earlier than planning a placement and then executing it requires, rotating within a few hundred milliseconds of a piece appearing and checking the column more the higher the drop; Kirsh and Maglio read these moves as physical action standing in for mental computation at the moment of use, a saving argued from timing, not measured

## Source

Kirsh and Maglio (1994), [LIT-1054](../literature.d/LIT-1054.md) (Cognitive Science 18(4), 513–549), read in
[NOTE-878](../notes.d/NOTE-878.md) from the scan of the version of record: Figures 6, 7, 10 and 15,
Table 1, the Discussion. Kirsh (1995), [LIT-1076](../literature.d/LIT-1076.md), read in [NOTE-871](../notes.d/NOTE-871.md), restates the
Tetris case in §5.1.

## What was actually shown

**The definition.** "we use the term epistemic action to designate a physical
action whose primary function is to improve cognition by: 1. reducing the memory
involved in mental computation, that is, space complexity; 2. reducing the number
of steps involved in mental computation, that is, time complexity; 3. reducing
the probability of error of mental computation, that is, unreliability."
Pragmatic actions bring the agent closer to the physical goal.

**Over-rotation (Figure 6).** Each piece type is rotated more than the
plan-then-act expectation (1.5 rotations for a four-orientation piece, 0.5 for a
two-orientation one), with 95% confidence intervals: about 1.7–1.75 against 1.5,
and 0.6–0.65 against 0.5, read off the figure. The number of players and
episodes behind it is not stated.

**Early rotation (Figure 7).** "rotation begins in earnest by 400 to 600 ms and,
on occasion, at the very outset of an episode", some before the piece is fully
in view. Rotating an emerging piece exposes its hidden part "150 to 300 ms
earlier"; pieces ambiguous in both shape and starting column are rotated more
than others, with no test statistic reported. Over-rotation recovered by
backtracking would cost 75–750 ms, so the classical sequential and interleaved
models do not fit.

**Translate-to-wall (Table 1).** In about 1% of drops the player moves the piece
to the wall and back first. Drops after this routine are longer (about 19–20
against 13–16 squares, t tests at .05 within each skill level), and its use
rises with drop distance.

**The cost argued.** "zoids can be physically rotated 90° in as few as 100 ms,
whereas we estimate that it takes in the neighborhood of 800 to 1200 ms to
mentally rotate a zoid 90°", from a pilot with three players. On the figure,
800–1200 ms is total reaction time; the increment for 90° is about 300 ms. Kirsh
1995 gives 700–1500 ms and 150 ms for the same comparison. No score or placement
was compared with and without the moves.

**When it pays.** The Discussion names two conditions: the action is fast
relative to the computation it replaces, and its local effect is determinate
(Tetris has "no hidden states, exogenous influences, or other agents"). It says
the choice fits Stigler's economics of information in outline, but "simple
economic models of costs and benefits fail because the benefits of an epistemic
action depend in considerable detail on just what computations the agent is
performing".

## What this does not say

- **That the moves save computation.** That is the reading. Function is
  inferred: "an action can serve both epistemic and pragmatic purposes
  simultaneously", and which it served is "often hard to prove". The mechanisms
  offered (multiple-perspective representations, settling, decision-tree
  attention) are hypotheses, not tested.
- **That a result is stored for later.** Nothing is kept: a rotated piece is
  read within a few hundred milliseconds and used once. The paper sets itself
  against caching: "Agents do not simply cache associative rules describing what
  to do in particular circumstances." Amortization appears once, in a
  parenthesis about sorting bolts before assembly, unanalysed.
- **That offloading always pays.** The conditions named are speed and
  determinacy; where effects are uncertain, or the world can change, the argument
  is not made.
- **That a cost model exists.** The paper says one cannot be given without
  modelling the particular computation an action serves.
- **That experts do more of it, as a measured result.** Asserted without a table.

## Connections

- [QUESTION-095](../questions.d/QUESTION-095.md): this is the "offload at the moment of use" strategy, the
  opposite end from the cockpit's precomputed speed bugs. Staleness does not
  arise, because the result is used at once and the effect is determinate.
- [THEORY-tmpwrpnk](THEORY-tmpwrpnk.md) holds the maintained-arrangement case from the same author.
- [THEORY-tmp6oz2d](THEORY-tmp6oz2d.md): Ballard et al. defer and re-read the world; Kirsh and Maglio act
  on it to make the computation cheaper. In both nothing computed is stored.
