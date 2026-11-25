# LEAD-137 study

Does a variable chosen for **informativeness across a buffer** coincide with
CLAIM-157's **gap-isolated block**, in a NON-lattice coupled-agent system?

## Model (choices made; owner's to revisit)

Linear Gaussian VAR(1): `x_{t+1} = A x_t + xi`, `xi ~ N(0, I)`. Coupling graph
is modular and non-lattice: `K=4` communities on a PATH (community `c` couples
only to `c-1`, `c+1`); each community a sparse Erdos-Renyi subgraph (`n=8`,
`p_in=0.5`) — no lattice regularity inside. The path-of-communities gives
locality: region `R` = community 0 reaches the far environment `E` only through
the buffer `B` = community 1 (and 2 when `buffer_width=2`).

Two unit directions of `R` are compared:

- `u_info` — **informative across a buffer**: the direction `w` whose coarse
  variable `w.x_R` carries the most information about `x_E`. For Gaussians this
  is the top canonical-correlation direction of `(x_R, x_E)` under the
  stationary covariance `Sigma` (leading generalized eigenvector of
  `(Sigma_RE Sigma_EE^-1 Sigma_ER, Sigma_RR)`). This operationalizes
  QUESTION-065's "informativeness about its far environment across a buffer"
  and the analogue of THEORY-205's leading transfer-matrix eigenvector.
- `u_block` — **gap-isolated block** (CLAIM-157, CLAIM-164): `R`'s slow
  collective mode, the leading eigenvector of the dynamics restricted to `R`
  (`A_RR`), i.e. the projector onto the block's joint mode.

Headline metric: `overlap = |<u_info, u_block>|` in [0,1].

Sweep: `mode` in {symmetric, asymmetric one-way drive}, `rho` (spectral radius)
in {0.5, 0.8, 0.95}, `w_cross` (modularity) in {0.1 strong, 0.5 weak},
`buffer_width` in {1, 2}, `homogeneous_border` in {False generic, True
lattice-like slab edge}, 20 seeds. 960 items.

## Result

- Lattice-like homogeneous boundary: overlap mean **0.986** — the informative
  variable IS the gap-isolated block mode (reproduces QUESTION-065's lattice
  result).
- Generic non-lattice boundary: overlap mean **0.739**, down to **0.19**; only
  42% of items clear overlap 0.9. Split by coupling: generic **symmetric**
  mean **0.527**, generic **asymmetric (one-way)** mean **0.950**.
- Modularity does NOT drive the match (0.739 vs 0.738) though `R` clears
  near-decomposability by factors of 100+ throughout. Boundary homogeneity and
  coupling symmetry do.
- Mechanism (`mechanism.py`): in the generic symmetric case `u_info` puts 0.89
  of its mass on the ~24% of `R`-nodes that bridge to the buffer (a border
  mode); `u_block` is spread (border-mass ~0.23 = the border fraction). They
  coincide only when every node is a boundary node (homogeneous slab) or under
  pure one-way drive, where `R` has no incoming boundary coupling to localize
  `u_info`.

So in a generic local non-lattice coupled-agent system the two criteria come
apart; coincidence is special to the homogeneous boundary a lattice has.

## Files / rerun

- `study.py` — model and metrics.
- `test_study.py` — `python3 -I -m pytest -q test_study.py` (8 tests).
- `run_sweep.py` — `python3 -I run_sweep.py` writes `results.jsonl` (append-only,
  resumable; ~2 s).
- `analyze.py` — `python3 -I analyze.py` prints the summary above.
- `mechanism.py` — `python3 -I mechanism.py` the border-mass check.

Run with BLAS threads 1 (`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1`). numpy 2.5.3, scipy 1.18.1.
