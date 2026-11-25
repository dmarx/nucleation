# LEAD-105: the crossed intervention on a conventionally trained network

Run on 2026-11-23. numpy on CPU; no downloads; about ten minutes on one core.

- `crossed.py`: data, the two-layer ReLU network (manual backprop), the
  optimizers (SGD, heavy ball, Adam, sign descent), the disruptions
  (permute, rescale, ablate-and-heal), the conflict probe and its measures.
- `run_all.py`: calibrates each probe optimizer's step size to matched pace
  (results/calibration.json), then runs the grid, appending one
  (trainer, seed) block at a time to results/probes.jsonl; it resumes.
  `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I run_all.py`
- `analyze.py`: paired differences with 95% intervals and the two-way
  variance shares; writes results/summary.json and prints the tables.
- `test_lead105.py`: `python3 -I -m pytest -q test_lead105.py` (8 tests):
  gradient check, permutation and rescaling invariances, the identity
  between SGD on rescaled weights and preconditioned SGD on the originals,
  optimizer updates.

The design, the results and their limits are in the record's executed-study
case for this lead; PROGRESS.md lists the choices.
