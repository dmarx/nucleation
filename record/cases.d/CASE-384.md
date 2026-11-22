---
number: 384
status: Proposed
formerly:
- CASE-tmp6hkf9
title: 'Three tabular agents on twenty 8x8 gridworld mazes, a planner on a learned transition table, a goal-conditioned value learner and a bank of occupancy-predicting demons, matched exactly in goal competence by one shared stream of experience: every query family can be read out of each with equal accuracy, but each answers a different family within its own per-decision computation; writing a blocked passage into the two units that carry it repairs every route of the planner and about a tenth of the others'', unless the block is propagated through all the demons, which repairs every route without a table; and the planner recovers fastest from change and damage and alone localizes the damage, though the same damage first costs it more'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-160 as a delegated
    lead worker. Code, tests, per-item results and their digest are
    committed under scratch/studies/lead-160/.
standing: documented
kind: executed-study
tags:
- agency
- cognition
- representation-learning
date: '2026-11-22'
line:
- distributed-agency
variant_of:
- CASE-187
illustrates:
- CLAIM-514
- CLAIM-519
- CLAIM-513
bears_on:
- QUESTION-362
summary: >-
  [CASE-187](CASE-187.md) run at toy scale for [LEAD-160](../leads.d/LEAD-160.md). Twenty 8x8 mazes with loops,
  deterministic and fully observed; goal family "reach cell g" for all 64
  cells. A planner (M) holds a learned transition table and plans by value
  iteration; a policy (P) is goal-conditioned Q-learning with hindsight
  relabelling; a distributed predictor (D) is one TD-learned demon per
  (state, action, goal) predicting discounted visits under random
  continuation, acting by ascent. All three learn from the same random walk
  and treat unknown moves as "stay", which matches their goal success
  exactly at every level (0.52, 0.83, 1.0, full coverage); M and P choose
  identical actions, D 93 to 98% the same on average. Queries answered by reading a
  transition table out of each agent are equally accurate for all three at
  every level; within each agent's per-decision computation, M answers next
  states and distances, P distances, D occupancies. A two-entry edit
  blocking a passage repairs all of M's failed routes, P's 9% and D's 14%;
  the same block propagated through every demon by the Woodbury identity
  repairs all of D's, without a table. After a change or damage M recovers
  fastest and its prediction error flags exactly the damaged units, where
  P's and D's TD errors flag 56 to 87% of undamaged ones too; 10% damage
  first costs M more (success 0.27 against 0.35). The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-991 CLAIM-990 — Proposed or new; the claims this study illustrates and the two it grounds -->

# CASE-384: Three tabular agents on twenty 8x8 gridworld mazes, a planner on a learned transition table, a goal-conditioned value learner and a bank of occupancy-predicting demons, matched exactly in goal competence by one shared stream of experience: every query family can be read out of each with equal accuracy, but each answers a different family within its own per-decision computation; writing a blocked passage into the two units that carry it repairs every route of the planner and about a tenth of the others', unless the block is propagated through all the demons, which repairs every route without a table; and the planner recovers fastest from change and damage and alone localizes the damage, though the same damage first costs it more

## What was done

[CASE-187](CASE-187.md) left its architectures, tasks and margins to a preregistration.
[LEAD-160](../leads.d/LEAD-160.md) asked for it to be run under matched competence. This is the
smallest version that keeps all four of its tests, run on 2026-11-22. The
code, its tests (12, passing), the per-item results and a digest are in
`scratch/studies/lead-160/`; the README there gives each choice and why.

- **World.** Twenty mazes of 8x8 cells. Each is a randomized depth-first
  maze with 8 extra walls removed, so routes have alternatives. Four
  moves, walls block, deterministic and fully observed.
- **Goal family.** Reach cell g from every start, for every g. Competence
  is the share of (start, goal) pairs reached within 64 steps. Path excess
  (steps over the shortest path) is reported beside it.
- **The three agents.** All are tabular, and all treat a move never tried
  as "stay".
  - The planner (M) keeps the last observed outcome of each move, a
    256-entry transition table, and runs value iteration on it for the
    goal in hand.
  - The policy (P) is a goal-conditioned action-value table learned by
    Q-learning, with each experience relabelled to every goal. It has no
    transition table.
  - The distributed predictor (D) is a bank of demons, one per (state,
    move, goal). Each predicts the discounted number of visits to the goal
    after that move, with random moves thereafter, and each is learned by
    its own TD rule. It acts by moving to wherever its demons predict most
    visits to the goal. It has neither a table nor a central simulator.
    It is an action-conditioned successor representation.
- **Matching.** All three learn from one random walk, trained to
  convergence on the same prefix of it. The prefix is the shortest at
  which the planner reaches success 0.5, 0.8 or 1.0, or at which every
  move has been tried. Sharing data and the "stay" prior gives every agent
  the same known graph, so success is matched exactly by construction.
  This was checked, not assumed. Memory, training updates and
  per-decision computation are reported rather than equalized, as
  [CASE-187](CASE-187.md) asks.

## The result

**Test 1: goals.** Success is identical across the three at every level:
0.52, 0.83, 1.0 and 1.0. M and P choose the same action in every
(state, goal) pair at every level: P is M's policy as a lookup table. D
chooses differently in 2 to 7% of pairs on average (at most 10%), with
path excess within 0.005 of M's. Memory differs: M holds 256 numbers, P and D 16,384 each. D needed
about 30 times the training updates of P to converge.

**Test 2: on-demand queries.** There were five families:
- Q1, the next state of a move;
- Q2, the shortest distance;
- Q3, discounted random-walk occupancy;
- Q4, the distances and occupancies after one passage is blocked.

Each agent answers by a fixed procedure on its own internals. It uses its
native readout where it has one: M its table; P the goal valued 1 for the
next state and log-value for distance; D the average of its demons for
occupancy and a Woodbury update of them for the blocked occupancy.
Otherwise it reads a transition table out of its internals and computes
from that.

- **Recoverable.** Read-out answers are exactly as accurate for all three
  at every level. At full coverage every family is answered perfectly by
  all three. At success 0.83 they are 93% on next states and 69% on
  distances for each. Without a read-out, P answers the blocked-distance
  query from its unchanged values, at 77% against 100%: the share of
  pairs the block leaves unchanged.
- **Available within the agent's own per-decision computation.** Costs
  are counted in elementary operations, with 64 states. The planner's
  budget is 256, the others' 4.
  - Within it, M answers next states and distances, P distances, D
    occupancies. No agent answers the interventional families within its
    own budget.
  - Within the planner's budget of 256, P also answers next states (64
    operations) and D blocked occupancies (20). Read-out answers cost 16,000 to a
    million operations.

So the competences are linked in what can be recovered and come apart in
what each agent can do within its own resources. Which families separate
depends on the budget.

**Test 3: targeted intervention on internals.** For five well-used
passages per maze, "blocked" was written into the two units that carry
each, in each agent's own terms:
- M: two table entries;
- P: the two units' value rows, set to their locally consistent values;
- D: the two units' demon rows, likewise.

The measure is the share of the pairs that the unedited agent fails in
the blocked maze that the edited one solves.

| agent | repaired | success after |
|---|---|---|
| M | 1.00 | 1.00 |
| P | 0.09 | 0.73 |
| D | 0.14 | 0.77 |
| D, block propagated through all demons | 1.00 | 1.00 |

M and P behave identically before the edit and differently after it. The
intervention separates what goals and read-out queries did not. The last
row is the qualification. The block was propagated through every demon
by the Woodbury identity, which reads the columns it needs off the demons
themselves. It reproduces retraining exactly (tested) and repairs every
route, with no transition table anywhere. Whether D responds "as a model
would" depends on whether the intervention is declared on a unit or on
the predictive content.

**Test 4: change and damage.** Recovery is by each agent's ordinary online
update from a fresh random walk, with no replay.
- **A passage blocked** (100 runs): success after 3,000 steps is M 0.98,
  P 0.81, D 0.85.
- **A shortcut opened** (100 runs): M's path excess reaches 1.000 by
  3,000 steps; P's is 1.008 and D's 1.014 there.
- **10% of units overwritten with other units' contents** (40 runs):
  - success right after is M 0.27, P 0.35, D 0.35, so a corrupted table
    entry misleads plans for every goal at once;
  - after 3,000 steps it is M 0.91, P 0.58, D 0.71, and after 10,000 steps
    M 1.00, P 0.87, D 0.89;
  - at the first revisit of each unit, M's prediction error flags every
    damaged unit and no other. P's and D's TD errors also flag every
    damaged unit, but they flag 56% and 58% of undamaged units too,
    because the damage has spread through their targets.
- **30% damage**: success right after is about 0.12 for all three, and
  after 3,000 steps M 0.87, P 0.44, D 0.53.

## What it can show

In this class, with matched goal competence:
- goal competence and recoverable query competence are linked;
- goal competence and within-budget query competence come apart, family
  by family;
- behaviour and the response to a unit-level intervention come apart;
- maintenance and revision went with the explicit local model. It
  recovered fastest and localized its damage, at the price of greater
  first fragility to the same damage.

These are the four readings [CASE-187](CASE-187.md) set out, each met once. For
[QUESTION-362](../questions.d/QUESTION-362.md)'s rows it gives a worked instance of "recoverable is not
available", and one of maintenance and corrigibility tied to a mechanism.
It gives two findings filed as claims, [CLAIM-991](../claims.d/CLAIM-991.md) on query
availability and [CLAIM-990](../claims.d/CLAIM-990.md) on the scope of an intervention.

## What it cannot show

- **Scale and generality.** It uses tabular agents, one deterministic maze
  family and random-walk experience. Nothing here is about function
  approximation, partial observation or stochastic dynamics.
- **Richens et al.'s theorem** ([CLAIM-513](../claims.d/CLAIM-513.md)) is not tested. Reading a
  next state out of P's values is the reach-goal shadow of their
  composite-goal extraction, and is trivial here.
- **The budgets are a choice.** Each agent's own per-decision computation,
  and the planner's as a common budget, are one choice among several. The
  operation counts are given so that others can be applied.
- **Replay.** With a replay buffer P and D would recover as M does, since
  replay is a nonparametric model. That variant was not run.
- **D's prior for untried moves** is not the "stay" fixed point. This
  lowers its native occupancy answers below the read-out ones at the
  partial levels (Q3 at success 1.0: 0.07 against 0.51).
