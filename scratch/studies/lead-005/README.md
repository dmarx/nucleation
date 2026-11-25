# LEAD-005: the thermodynamics of prediction, reproduced, then with feedback

Reproduces Still, Sivak, Bell & Crooks (2012), "The thermodynamics of
prediction" (arXiv 1203.3271 v3; held as LIT-327, read in NOTE-295, account
THEORY-026), on small driven Markov systems, then adds feedback from the
system to its drive and compares memories that keep the predictive partition,
the interventional partition, both, all, or nothing.

## Rerun

    cd scratch/studies/lead-005
    python3 -I run_study.py            # ~30 s on one core; writes results/
    python3 -I -m pytest -q -p no:cacheprovider   # 15 tests, < 1 s

`run_study.py` appends one JSON line per random instance and skips ids
already written, so it resumes. Delete `results/*.jsonl` to recompute.

## Files

- `still2012.py`: exact bookkeeping of the paper's protocol (work step, then
  relaxation under a fixed kernel), from the joint law p(s, x) (the paper's
  Eq. 13 reading) and by enumerating drive paths (the per-protocol reading of
  Eqs. 9-10); a Monte Carlo sampler of trajectories as an independent check;
  random instances with or without feedback.
- `feedback_toy.py`: an 8-percept loop (u fresh context, v sticky nuisance,
  y outcome of the last action) in which the partitions differ; memories are
  physical two-level-per-class systems with an energy gap, re-equilibrated
  after each switch.
- `run_study.py`: the sweeps; `results/summary.md` is the readable result.
- `test_lead005.py`: identities, bounds, the reading-independence of W_ex,
  Monte Carlo agreement, the feedback sign failure, the 0.38-nat example of
  CLAIM-tmpcbdgm, and the toy's partitions and ranking.

## Conventions

beta = 1: energies in k_BT, information in nats. Index t follows the paper:
I_mem(t) = I[s_t; x_t], I_pred(t) = I[s_t; x_{t+1}], summed over t = 0..tau-1.
