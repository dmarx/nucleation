<!-- scratch/studies/lead-026/README.md: the materials of LEAD-026's study -->
# LEAD-026: CASE-101's three populations, QUESTION-115's search and a lagged block

The study filed as the CASE that carries out LEAD-026 (2026-11-22).
Simulation, numpy only; every information quantity is the linear-Gaussian
estimate, in nats.

- `model.py`: the populations. Six member slots with turnover r = 0.02 per
  step in every arm, one environmental variable e and an unrelated
  distractor z. Arm A: e is an exogenous driver, newcomers arrive naive.
  Arm B: e is inert; members learn from, and newcomers copy, other members'
  norms of L = 8 steps ago, with no synchronous coupling. Arm C: e is an
  institution that trains members, selects newcomers and answers to the
  members' mean. Arm C0: arm C with an institution deaf to its members.
- `calibrate.py`: fits each arm's (a, gain, s) so that member variance (1),
  mean member correlation (0.4) and the aggregate's lag-1 autocorrelation
  (0.9) match; writes `calibration.json`.
- `measures.py`: Krakauer et al.'s A*, A, nC at lags 1 to 64 (A11's lagged
  form), transfer entropy into a candidate (dynamical independence), and
  the priced lagged block: a VAR(W) over the observed variables, each group
  of couplings kept or pruned by CLAIM-154's rule with a unit-information
  prior (Occam ln n per coefficient); a candidate passes when every cut
  inside it is kept and its edge is pruned.
- `run.py`: per arm, the block test on all 255 subsets (127 with e hidden)
  at W in {1, 2, 4, 6, 7, 8, 10, 12, 16}; the information profile per
  symmetry class of candidate; Bourrat's Ahat by intervention (do(S) with
  values from S's population marginal, R = 20000). Appends to
  `results.jsonl` per item and resumes.
- `summarise.py`: writes `summary.txt`.
- `test_lead026.py`: 11 tests, among them: arm B's coupling is only at lag
  L; arm C's institution answers its members and C0's does not; with a
  common input observed the driven pair fails the block and the pair with
  its driver passes, and with it hidden the pair passes; a one-step VAR
  sees lag-3 coupling through the source's own persistence.

Rerun (calibration about 10 minutes, the run about 15, one CPU):

    cd scratch/studies/lead-026
    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -m pytest -q -p no:cacheprovider test_lead026.py
    python3 -I calibrate.py      # optional: calibration.json is committed
    rm -f results.jsonl && python3 -I run.py && python3 -I summarise.py

LEAD-167's code (scratch/studies/lead-167/) computes the same measures
exactly on a 256-state discrete kernel. These populations have continuous
norms, turnover and lag-8 transmission, so its definitions are
re-implemented here in Gaussian form rather than its code reused.
