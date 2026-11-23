# LEAD-208: effective dimensions of the 2D Ising model

numpy only, CPU. From this directory:

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I -m pytest -q -p no:cacheprovider   # 13 tests, ~2 s
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I run_study.py all                   # ~10 min on one core
    python3 -I analyze.py                                                                  # writes results/summary.md, summary.json

`run_study.py` appends one JSON line per item to `results/*.jsonl` and skips
items already there, so an interrupted run resumes. Seeds are fixed.

## Files

- `ising.py`: Swendsen-Wang (with frozen sites, for compatible Monte Carlo),
  heat-bath, Metropolis, vectorized cluster labelling, the 13 statistics
  (field + 12 two-spin couplings, every offset in the 5 x 5 box up to sign),
  their exact conditional means given the black sublattice, and the masks of
  the sites kept after k checkerboard decimations (b = sqrt 2 per step).
- `fisher.py`: the decimated Fisher metric g^k = Cov(E[Phi | o_k]); exact at
  k = 0, 1; for k >= 2 the product of two compatible chains' means (burn 3,
  2 measurements each); jackknife errors over 16 blocks of whole chains.
- `strip.py`: exact transfer-matrix predictive information on a width-W
  periodic strip, for whole columns (Markov, so a function of W only) and
  for one row (hidden Markov, forward recursion over all row sequences).
- `clusters.py`: largest geometric (like-spin) cluster and box counting.
- `run_study.py`: L = 16, 32, 64 at T/T_c = 0.9, 1, 1.1 (8192, 4096, 1536
  configurations from 64, 64, 32 independent SW chains); strips W = 2..12;
  burn-in check at L = 32.
- `analyze.py`: spectra, per-step decay factors, relevant count, stiff
  counts (measured and extrapolated), cluster dimensions, strip tables.
- `results/`: the JSON lines and the generated summary (all under 100 kB).
