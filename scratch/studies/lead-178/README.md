# LEAD-178: dynamical dependence of a block's aggregate, linear Gaussian VAR(1)

Class: stable VAR(1) X_t = A X_{t-1} + e_t, e_t ~ N(0, S), S ≻ 0, and a
linear aggregate Y = LX observed without noise. Dynamical dependence is
T(X → Y) = ½ log det Var(Y_t | Y⁻) / det(LSLᵀ) (THEORY-257, THEORY-733).
All numbers come from exact stationary covariances and the steady
noise-free Kalman filter; nothing is simulated.

- `dd.py`: exact T (filter), the cross-check from lagged autocovariances,
  the two-sided bound (lower with Cov(e | Le), upper with Cov(X | LX)),
  and the block constructors.
- `test_dd.py`: 57 pytest checks (filter = lag regression, the sandwich on
  40 random systems, closed aggregate gives 0, unclosed floor positive,
  the upper bound equals CLAIM-390's for a block's full state).
- `run.py`: the study; appends one JSON line per item to `results.jsonl`
  and skips items already written.
- `summarize.py`: writes `results.md`.

Rerun (a few seconds):

    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider test_dd.py
    rm -f results.jsonl && python3 -I run.py && python3 -I summarize.py

Needs numpy and pytest. Seeds are
fixed in the scripts.
