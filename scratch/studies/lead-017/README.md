# LEAD-017: registration measured apart from the experimenter's setting

Three synthetic organizations of matched pursuit and different endorsement
relations between the consummatory process H and pursuit P, after A13
(QUESTION-270's note of 2026-11-04), and a measure of the organization's
registration of H's evaluation that reads only observables. Filed as an
executed-study CASE.

## Files

- `orgmodel.py`: the generator. `simulate(world, n, seed)` returns
  `Observables` (what a measure may read: pursuit, the outcome schedule,
  the liking assay, the experimenter's perturbation of H, the mixed
  record, the report, P's value) and `Latent` (the setting: registration
  gain g, authority, tolerance; used only to score).
- `measures.py`: the measures, which take `Observables` only.
- `test_orgmodel.py`: 8 tests (`python3 -I -m pytest -q -p no:cacheprovider test_orgmodel.py`).
- `study.py`: calibration, scoring, behaviour check; writes
  `results/results.jsonl` one item per line, skipping items already done.
- `summarize.py`: thresholds on the calibration split, applied unchanged
  to the test split and held-out worlds; writes `results/summary.json`.

## Rerun

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 -I study.py
    python3 -I summarize.py

About ten seconds on one core. Delete `results/results.jsonl` to rerun
from scratch.

## Organizations

| world | registration gain g | H's authority over P | tolerance |
|---|---|---|---|
| denied (unliked pursuit) | U(0.5, 1) | none | fixed |
| unregistered (evaluative isolation) | 0 | uptake beyond tolerance, from the record | fixed |
| accommodation (tolerated hardship) | U(0.5, 1) | uptake beyond tolerance, from the record | revised by reciprocal compensation |

Held out: an unregistered world whose record carries the physiological
state behind H's evaluation by another route (decoy); an unregistered
world where H acts on pursuit directly, bypassing the record (direct
authority); a denied world with weak registration g ∈ U(0.1, 0.25); a
denied world whose persistence is habit, not cue drive.

Every world's base logit is calibrated, from behaviour only, so that mean
pursuit after devaluation (steps 140–239) is 0.6 under the probe protocol.

## Measures

- `reg_int` (the proposed measure): F-test, per agent, that the record
  predicts the experimenter's randomized perturbation δ of H's evaluation
  beyond the outcome, the action and P's value. δ perturbs the evaluation,
  not g or the authority.
- `reg_pas`: the same for the liking assay on unperturbed steps (passive).
- `reg_int_report`: `reg_int` on the one-dimensional report alone.
- `reg_naive`: the record decodes the assay, with no covariates.
- `auth`: F-test that δ at t moves pursuit at t+1 (linear and quadratic).

Scores are −log10 p. Thresholds maximize balanced accuracy on seed 10.
