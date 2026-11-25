# LEAD-160: CASE-187's three agents on small gridworld mazes

The study CASE-187 proposes, run 2026-11-22 at toy scale: an explicit
transition model with planning (M), a directly learned goal-conditioned
policy (P), and a distributed predictive-state controller (D), matched on
competence over a declared goal family, then tested four ways.

## Rerun

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I -m pytest -q -p no:cacheprovider test_gridagents.py
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I run_study.py 20   # about 3 minutes; resumes
    python3 -I summarize.py                                               # writes summary.md

`results.jsonl` holds one line per (maze seed, item). `summary.md` is the
digest the CASE cites.

## Design (choices made where CASE-187 and LEAD-160 leave them open)

- **World.** 20 mazes, 8x8 cells (64 states), each a randomized depth-first
  perfect maze with 8 extra walls removed, so there are loops. Four actions;
  walls block. Deterministic and fully observed. *Why:* the smallest world in
  which routes, detours and shortcuts exist; determinism makes "the right
  answer" to every query exact, and full observation is the setting of
  Richens et al. (CLAIM-513), whose open question the study is about.
- **Goal family.** Reach cell g, for every g, from every start; success
  within 64 steps. Competence = share of (start, goal) pairs reached; path
  excess = steps over the shortest path, reported separately.
- **Agents.** All tabular. Unknown units are "stay" for all three.
  - M: last-observed transition table Th[s,a]; value iteration on it per
    goal at decision time (gamma 0.9).
  - P: Q[s,a,g], Q-learning with hindsight relabelling to every goal
    (reward 1 on arrival), greedy. No transition table.
  - D: one occupancy demon per (s,a,g): Msr[s,a,g] predicts discounted
    visits to g after a in s and uniform-random actions thereafter (an
    action-conditioned successor representation, gamma 0.95), each learned
    by its own TD rule; acts by greedy ascent on Msr[x,:,g]. No table, no
    central simulator. *Why this for "distributed predictive-state
    controller":* it is the standard predictive-representation agent
    between model-based and model-free (Dayan 1993; Momennejad et al. 2017),
    its state is a bank of predictions each learned separately (a Horde of
    demons), and ascent on a discounted occupancy reaches any reachable goal
    (each non-goal value is gamma times a neighbour average, so some
    neighbour is strictly higher).
- **Matching.** All three learn from the same random-walk stream, trained
  to convergence by replay of the transitions seen (replay is discarded
  afterwards; online tests use no replay). Levels are the shortest prefix at
  which M reaches success 0.5, 0.8 and 1.0, and full coverage of all 256
  units. *Why:* same data and the same "unknown = stay" prior give every
  agent the same known graph, so success is matched exactly (verified, not
  assumed: test_same_data_gives_same_success, and Test 1). Memory, training
  updates and per-decision computation are reported, not equalized, as
  CASE-187 asks ("equal competence at unequal cost is itself a result").
- **Test 2 queries** (accuracy against the true maze, all pairs):
  Q1 next state of (s,a); Q2 shortest distance x to g; Q3 discounted
  random-walk occupancy of g from x (correct within 1e-6 relative);
  Q4 the same two after do(block a passage), for 5 passages per maze.
  Each agent answers by a fixed procedure on its own internals, with a cost
  in elementary operations: its native readout where it has one (M: its
  table; P: Q1 by the goal whose value is 1, Q2 from log Q; D: Q3 by
  averaging demons, Q4-occupancy by a Woodbury update of its demons), else
  by **extraction** (read a transition table out of Q or the demons, then
  compute). "P without extraction" is P answering the interventional query
  from its unchanged values. Availability is judged against two budgets:
  each agent's own per-decision computation (M 256, P 4, D 4) and a common
  budget of 256 (the planner's). *These budgets are a choice; the costs are
  given so that another budget can be applied.*
- **Test 3, targeted intervention on internals.** For each of the 5
  passages, write "blocked" into the units that carry it, by each agent's
  own representation: M writes 2 table entries; P sets the 2 units' Q rows
  to their locally consistent value (gamma times the best other action);
  D sets the 2 demons' rows to their locally consistent fixed point.
  Variant D_global propagates the block through every demon by the
  Woodbury identity, still without a transition table (exactly equal to
  retraining; tested). Measured: success in the blocked maze, and the
  share of the pairs the unedited agent failed that the edited one solves.
- **Test 4a, environmental change.** Block one of the 5 passages, or open
  one of the 5 most distance-saving walls; then a fresh 10,000-step random
  walk with each agent's ordinary online update (one write per
  transition, no replay); competence at 0, 30, 100, 300, 1000, 3000, 10000
  steps.
- **Test 4b, damage to the predictive machinery.** Overwrite 10% or 30%
  of the (s,a) units with the content of other randomly chosen units (same
  units for all three; 2 draws per maze); then recovery as in 4a in the
  unchanged maze. Detection: whether the agent's own error signal (M:
  prediction error; P and D: TD error) is nonzero at the first revisit of
  each unit; hit rate on damaged units, false-alarm rate on the rest.

## Limits

Tabular, deterministic, one small maze family; the random-walk exploration
stream is the only experience; costs are operation counts, not timings. P
and D with a replay buffer would be Dyna-like and recover as M does; that
variant was not run. Nothing here tests Richens et al.'s theorem itself.
