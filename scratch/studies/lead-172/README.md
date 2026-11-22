# LEAD-172: modular-addition checkpoint study

numpy only (torch is not installed in this environment), CPU, one thread
per process.

- `modadd.py`: model, training, and the measures taken at checkpoints (see
  its docstring). Each arm appends JSON lines to `results/<arm>.jsonl.gz`
  (one gzip member per row, so the file stays readable after a kill).
  Weights and AdamW state go to `$LEAD172_STATE` (default `state/`, not
  committed) every kernel checkpoint, so a killed arm resumes there; rows
  written after the last saved state are written again, and readers keep
  the last row for each step. An arm with a `done` row is skipped.
- `analyze.py`: the prospective test; writes `analysis.json`.
- `test_modadd.py`: gradient check, the selection-rule masks and nulls,
  the closed-form kernel against explicit Jacobians.

Rerun (about 10 minutes on 4 cores):

    cd scratch/studies/lead-172
    python3 -m pytest -q test_modadd.py
    export OMP_NUM_THREADS=1 LEAD172_STATE=/tmp/l172state
    for i in 0 1 2 3; do timeout 1800 python3 modadd.py all $i 4 & done; wait
    python3 analyze.py
