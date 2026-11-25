# LEAD-030: the laboratory of genres

CASE-296's simulated engagement laboratory, as a small numpy/scipy
simulation. `lab.py` holds the model, the inference and the measures (its
docstring states the design); `run.py` runs worlds x arms x seeds and
appends one JSON line per run to `results.jsonl`; `summarise.py` writes
`results.md`; `test_lab.py` holds the unit tests.

## Rerun

    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider test_lab.py
    python3 -I run.py results.jsonl taste 0 1 2 3 &
    python3 -I run.py results.jsonl exposure 0 1 2 3 &
    wait
    python3 -I summarise.py results.jsonl > results.md

Each run takes one to two and a half minutes on a shared CPU; the 40 runs
took about 30 minutes in two processes. Runs already in `results.jsonl`
are skipped.

## Design in one paragraph

600 users, 400 items, 8-dimensional preference vectors, engagement
probability sigmoid(-2 + u.v + beta_i) given exposure, 30 exposures per
user per period. World "taste": vectors drawn around 6 cluster centres
(between-cluster sd 0.6, within 0.3), exposure popularity-weighted. World
"exposure": vectors with the same marginal spread and no clusters,
exposure channelled through 6 communities (weight 0.08 outside one's own).
Five burn-in periods under the base policy; classes (K = 6) inferred from
their raw engagement counts by regularized degree-normalized spectral
co-clustering and held fixed. Fifteen periods under one of five arms
(inferred; inferred+adapt; used; used+adapt; popular+adapt). Adaptation:
users move 10% a period toward the mean of the items they engaged with;
creators replace the 3% least-engaged items by noisy copies of engaged
ones. Measures at the start and end: concentration of engagements in the
user's target class; the random-exposure probe gap (in-class minus
out-of-class engagement rate under uniform exposure, which changes
nothing); the closure score and defect of a degree-corrected class
logistic model against a rank-8 ridge factor model, tested on the probe
and on a fresh policy draw; the unconditional Poisson gain of the block
model on raw counts; stability (ARI of classes re-inferred at the end);
and ground truth (between-class share of true preference variance, the
true in-class gap, within-class spread).

## Tuning done once, before the runs

On seeds 1 and 2 (not a search over results): between-cluster sd 0.45
gave inference ARI about 0.27 against the planted genres, 0.6 with five
burn-in periods about 0.5; the factor model's ridge was set to 2 (10 or
more shrinks it to the degree model, 0.3 overfits).
