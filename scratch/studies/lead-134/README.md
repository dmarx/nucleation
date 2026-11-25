# LEAD-134 study: CASE-114, "The imagined owner"

Build CASE-114's distributed-control system with a centralized self-model and
log the self-model's reports of what caused what against the true causes.

## Files
- `model.py` -- the plant, the two self-models, the measures, the grid driver.
- `test_model.py` -- pytest (8 tests).
- `results.jsonl` -- one JSON record per (K, sigma-profile, seed) config.
- `summary.json` -- aggregate across the grid.

## Rerun
    cd scratch/studies/lead-134
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
        python3 -I -m pytest -q          # tests (~0.5s)
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
        python3 -I model.py              # grid + summary (~2.5s)

`run_grid` appends per config and skips configs already in `results.jsonl`, so
it resumes if interrupted. Delete `results.jsonl` to start clean.

## What it builds
A plant with K independent components, each emitting an independent drive
deviation. The aggregate outcome is their sum. Faults are single-component
excursions; the simulator records (timestep, component) as the TRUE cause,
apart from any self-model.

Two self-models observe the SAME per-component signals (equal input, equal
parameter count) and both reconstruct the aggregate outcome EXACTLY. They
differ only in the assumed causal graph:
- `accurate`    -- K parallel autonomous components (the true graph).
- `centralized` -- one owner command driving all effectors uniformly (a star
  graph); it explains every outcome as the owner's doing, spread over effectors.

Because both reproduce the outcome exactly on identical inputs with equal
params, any attribution divergence is wrong-about-control, not merely-coarser
-- which is CASE-114's main threat to inference, met head on.

Phase 1 (open loop): the self-model narrates; the plant's control is held
fixed and identical across the two systems, only the reports differ. Phase 2
(closed loop): the self-model's blame drives governance revision (reduce the
blamed component's gain). This is A27 section 12's loop, which CASE-114 warns
breaks the held-fixed equivalence; that divergence is A27's fourth measure.

## Result (summary.json, 60 configs: K in {3,5,8} x {equal,graded} x 10 seeds)
- Aggregate reconstruction error: accurate 0.0, centralized ~1e-15. Equal
  behavioral capacity -- the coarseness objection is defeated empirically.
- Localization accuracy (argmax attribution == true culprit): accurate 0.94,
  centralized 0.21 (~ chance 1/K). The centralized model names the wrong cause
  ~79% of the time, in a predictable direction: it spreads blame uniformly and
  credits the owner's global command.
- Attribution mass on true cause: accurate 0.56, centralized 0.22 (uniform).
- Governance: innocent-component gain stripped -- accurate 0.34, centralized
  0.46 (accurate lower on 60/60 configs); cumulative error during revision --
  accurate 0.167, centralized 0.217 (accurate lower on 54/60). The centralized
  model cannot localize the rogue, so to cut errors it suppresses the whole
  system, degrading innocent components.

## Reading
A unified (centralized) self-model, matched in capacity and reproducing
behavior exactly, systematically misdescribes who controls what. The error is
located in the attribution and belongs to the system that holds the self-model
-- as CLAIM-355 says it must. It answers Drayson's horn (the represented owner
always has a truthmaker in the distribution of control) unconditionally FOR
THIS MODEL: here the owner the centralized model presents has no truthmaker in
the true, distributed division of labor.

Limits (honest, per CASE-114 and CLAIM-288): the modeller writes both
self-models, so this shows what the centralized CONTENT does once present, not
that a distributed agent would come to hold it. It is a stipulated
construction, and it bears on attribution of control, not on phenomenal
properties.
