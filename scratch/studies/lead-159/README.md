# LEAD-159: CASE-188's agents with their slow structure ablated under matched information

A simulation, numpy only, CPU, one thread. Everything runs in about 1.5
minutes.

    cd scratch/studies/lead-159
    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider test_resolve_model.py   # 9 tests
    python3 -I run.py 400     # main design -> results.jsonl (252 cells)
    python3 -I sweep.py 200   # sensitivity  -> sweep.jsonl (360 cells)

Both runners append one JSON line per cell and skip cells already written,
so a stopped run resumes. Delete a results file to rerun it from scratch.

## Files

- `resolve_model.py`: the task, the four agents, the five conditions, the
  three visibilities and the endpoints. Its docstring is the specification.
- `run.py`: the main design. Ages 250, 1000, 4000; environments defeater,
  irrelevant, neither; agents R, E, P, I; conditions intact, lesion,
  perturb, yoked, timescale at full visibility; and the intact agents at
  partial and routed visibility. 400 runs per cell, seed 159 (yoke sources
  seed 10159).
- `sweep.py`: the ablation comparison at age 1000 under nine one-at-a-time
  parameter variants, 200 runs per cell.
- `results.jsonl`, `sweep.jsonl`: one line per cell. Fields: `p_revise`
  (share of runs choosing A on more than half of the last 200 trials of the
  1500 after the onset), `p_revise_at_250` and `_at_500` (the same read at
  those horizons), `t_revise_median` (median first trial after onset at
  which a 50-trial running share of A exceeds one half, among runs that
  cross), `p_ever`, `pre_shareB` (ordinary-condition share of B in the 200
  trials before the onset), `regret_per_trial` (long-run payoff lost per
  trial after onset), `lam_onset`, `a_onset`, `lam_end`, `a_end`,
  `c_onset`, `c_end`, `absorbed` (share of the defeater's shift in the
  commitment estimate reached by the end; confounded under routed
  visibility, where c drifts before the onset).

## Design, and every parameter choice

CASE-188 leaves every parameter to a preregistration; LEAD-159 adds A40
Study D's control. The choices below are the assistant's.

- **Task.** Two actions; B is the commitment. Each trial both actions yield
  an immediate payoff (the locally dominant evaluation) and a long-run
  payoff (what is scored), each with noise sd SIGMA = 1. Ordinary
  conditions: B better in the long run by DELTA = 0.5, A more tempting now
  by TAU0 = 0.2, so the commitment and the temptation conflict mildly and a
  governed agent keeps B. Why two channels: with one channel a defeater and
  an irrelevant fluctuation of matched size and duration are the same
  signal, and only a difference of duration separates them, which makes
  any slow learner look corrigible. The experimenter, not the agent, says
  which channel bears on the commitment (CASE-188's non-circularity).
- **Events** (CASE-188's environment factor). A step of 2·DELTA in the
  difference of the two actions' means, on the long-run channel (defeater)
  or the immediate one (irrelevant), at the same onset, persisting to the
  end: matched size, noise, onset and duration. A neither arm.
- **Agents**, all with the same state variables (capacity): per-action fast
  immediate estimates (ALPHA_F = 0.05), per-action long-run estimates (the
  commitment's evaluator, ALPHA_C = 0.01, times an admission weight a), a
  precedence lam mixing the two in the choice (softmax, BETA = 8).
  - R, corrigible resolve: lam = sigmoid(KAPPA·(e_q − e_c)), KAPPA = 5,
    with e_c, e_q slow (ETA = 0.002) traces of the squared error of the
    commitment and of the fast evaluation against the observed long-run
    difference: precedence goes to whichever predicts what is scored, and
    a = 1, so defeaters are always admitted. KAPPA was set so that the
    mature lam is about 0.9.
  - E, entrenchment: lam grows toward LAM_MAX = 0.95 at rate ETA, and a
    decays at rate ETA_E = 0.002, on each trial whose choice agrees with the
    commitment: enforcement improves while evidence loses its way in. The
    rates were set so that a is about 0.6, 0.17 and 0 at ages 250, 1000,
    4000, spanning the "falling first probability" CASE-188 predicts.
  - P, imposed protection: lam = 0.9 fixed from outside, a = 1. Added
    because CLAIM-344's defeated_if names "externally imposed protection".
  - I, inertia: lam = 0.5, a = 1, both estimators slow (ALPHA_SLOW = 0.001),
    and BETA_I = 21 so that its ordinary-condition share of B (0.96) equals
    the others'. Added because the defeated_if names "parameter inertia".
  - All four start with the commitment installed (estimates at the ordinary
    values). At ages 1000 and 4000 all four choose B on 0.96–0.98 of
    ordinary trials: they "decide alike under ordinary conditions". At age
    250 R and E have not matured (0.86, 0.81).
- **Conditions**, applied at the onset, with the observation stream and the
  choice noise identical to the intact run (common random numbers; matched
  information) and the same variables (matched capacity):
  lesion (slow structure reset to lam = 0.5, a = 1 and frozen),
  perturb (reset, then free: whether the agent re-establishes it),
  yoked (lam and a replaced by the trajectory of the same agent type in an
  independent neither run: matched values, coupling cut),
  timescale (every rate slower than ALPHA_F raised to it).
  The lead says "perturb or ablate"; these are four ways of doing so, and
  the result is that they disagree.
- **Visibility** (CASE-188's third factor), long-run channel only: full;
  partial (observed on a random quarter of trials, independent of choice,
  so information stays matched across agents); routed (disconfirming
  observations admitted to the commitment's evaluator with weight 1 − lam).
  The bandit reading of partial (only the chosen action observed) was not
  run, since it makes the information depend on the policy and breaks the
  matched-information control.
- **Legitimacy** (CASE-188's second factor) was not varied: none of these
  agents has access to how its commitment was adopted, so a badly adopted
  commitment can enter only as an evidence stream, which collapses it onto
  the environment factor. Varying it needs agents that can read their
  commitment's provenance.
- **Endpoints**: revision (majority of A in the last 200 of 1500 trials
  after onset, also read at 250 and 500), time to revision, regret,
  precedence and admission at onset, and the share of a defeater's shift
  that reached the commitment's evaluator (the evidence route).
- **Replicates**: 400 runs per cell (SE of a proportion at most 0.025).
  Sweep 200 runs.

## Result (full visibility; p of revision at 1500 trials, defeater / irrelevant)

| agent | intact | lesion | perturb | yoked | timescale |
|---|---|---|---|---|---|
| R resolve, age 1000 | 1.00 / 0.00 | 1.00 / 1.00 | 1.00 / 0.00 | 1.00 / 0.00 | 1.00 / 0.00 |
| E entrench, age 1000 | 0.99 / 0.00 (0.04 by 500) | 1.00 / 1.00 | 1.00 / 0.41 | 0.91 / 0.00 | 0.00 / 0.00 |
| E entrench, age 4000 | 0.00 / 0.00 | 1.00 / 1.00 | 1.00 / 0.49 | 0.00 / 0.00 | 0.00 / 0.00 |
| P imposed, age 1000 | 1.00 / 0.00 | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / 0.00 | 1.00 / 0.00 |
| I inertia, age 1000 | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / 1.00 (by 250) |

- Lesion: persistence under irrelevant change falls from 0 to 1 for R, E
  and P, and is unchanged for I. It separates inertia from the governed
  agents, but not resolve from imposed protection.
- Perturb: R re-establishes its precedence from the evidence and its
  persistence returns (0.00); P cannot (1.00); E slowly regrows it (0.41 to
  0.49 at 1500, 1.00 at 500). It separates resolve from imposed protection.
- Yoked: no change for any agent (R 0.00 at ages 1000, 4000; 0.09 at age
  250 read at 250 trials). A yoked control would read R's persistence as
  independent of its maintained structure.
- Timescale: R and P unchanged; E more entrenched; I loses its slow
  persistence (switches under both within 250 trials). A timescale ablation
  reads inertia as slow-structure-dependent and resolve as not.
- Selectivity over age: R revises under the defeater at every age (median
  ~90 trials) and never under irrelevant change; E revises at age 250
  (median 110), slowly at 1000 (577; 0.04 by 500), never at 4000, and the
  defeater's shift reaching its evaluator falls 0.99, 0.63, 0.00; I is
  non-selective (both, ~365 trials); P matches R.
- Visibility: partial slows revision a little for R and P and much for E;
  routed stops P revising (lam fixed) but not R, whose precedence, read
  from unrouted error, falls and reopens the route.
- Sweep (DELTA 0.3, TAU0 0.4, SIGMA 1.5, KAPPA 3, ETA 0.005, LAM_IMPOSED
  0.8, ALPHA_SLOW 0.002, BETA 4): the pattern of every ablation holds for
  R, P and I in every variant; the largest departure is R yoked at
  DELTA 0.3, 0.12 under irrelevant change.

These are numbers of a constructed model. They show what each ablation can
and cannot tell apart when the agents' governance is known; they are not
evidence about any trained learner.
