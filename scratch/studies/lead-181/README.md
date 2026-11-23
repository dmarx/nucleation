# LEAD-181: does penalizing newly recognized violations produce avoidance of inquiry?

CASE-249's simulated institution (A44 §7), built and run. 30 fixed
requirements, 10 visible and 20 hidden, each violated at the start with
probability 0.3. Each of T = 20 periods the institution splits a budget of
B = 10 units among inquiry (a units; each hidden requirement found with
probability 1 - 0.9^a per period), remediation (up to b fixes, one unit
each, possible only L = 1 period after recognition) and output (alpha per
unit). Optionally, hidden requirements surface from outside (s per period)
and a violation still unmet when it surfaces costs sigma. The internal
evaluator counts recognized violations; the independent one counts all.

Governance regimes, `model.py`:

- `pen`: every recognized violation penalized (lam = 1 per period),
  newly recognized ones included, discovery not rewarded (CLAIM-662);
- `amnesty`: a violation is penalized only once recognized for g = L
  periods, so newly recognized violations are not penalized;
- `none`: no violation penalty;
- `disc`: `pen` plus mu = 0.5 per requirement found by inquiry;
- `ext`: every true violation penalized, recognized or not.

The institution's policy is a stationary (a, b) on a grid of 28. For each
setting and regime, `study.py` finds the Monte Carlo optimum (2000 runs,
common random numbers, and the policies tied with it within two paired
standard errors) and trains 16 gradient-bandit learners for 4000 episodes
each. `sweep.py` varies sigma and L for `pen` against `amnesty`.

Rerun (CPU, about two minutes in all):

    cd scratch/studies/lead-181
    OPENBLAS_NUM_THREADS=1 python3 -I -m pytest -q test_model.py
    OPENBLAS_NUM_THREADS=1 python3 -I study.py   # results.json, results.md
    OPENBLAS_NUM_THREADS=1 python3 -I sweep.py   # sweep.md

The construction is stipulated and calibrated to nothing.
