<!-- scratch/studies/lead-057/README.md: the materials of LEAD-057's study -->
# LEAD-057: three partitions of one dynamical model

The study filed as the CASE that carries out LEAD-057 (2026-11-22).

- `three_partitions.py`: the model (a four-unit linear Gaussian VAR(1) with intrinsic pairs 01 and 23 and a beam-like apparatus pairing 02 and 13), the three accounts (fixed F, recovered R, arrangement-dependent Arr), five scenarios, a gain sweep and a variant in which the apparatus has states of its own. A partition is scored by `block_loss`, the excess one-step error of block-local prediction over full prediction, computed exactly from the stationary covariance and checked by simulation. Writes `results.json`. Runs in seconds: `python3 -I three_partitions.py`.
- `test_three_partitions.py`: 9 tests (`python3 -m pytest -q test_three_partitions.py`).
- `results.json`: the output of the run filed.
- `PROGRESS.md`: what is done and what is next.
