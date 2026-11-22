# LEAD-084: finite Markovian augmentation beyond the scalar linear Gaussian case

Class: stable VAR(1) X_{t+1} = A X_t + w_t, w_t ~ N(0, Σ), Σ ≻ 0, and a
linear coarse variable Y = LX of any dimension m < n, observed without
noise. All numbers come from exact stationary covariances; nothing is
simulated.

- `augment.py`: the functions (Riccati recursion from the stationary prior,
  steady filter by the reduced algebraic Riccati equation, finite-lag error
  and its bound, Mori frame, reduced filter of the eliminated variables,
  k_min, Mori–Zwanzig Hankel rank, Krylov dimension, transfer entropy of Y
  and of the augmented state, Markov test).
- `test_augment.py`: 308 pytest checks.
- `run.py`: the study; writes `results.json` and `results.md`.

Rerun (about ten seconds):

    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider test_augment.py
    python3 -I run.py

Needs numpy, scipy and pytest. Seeds are fixed in the scripts.
