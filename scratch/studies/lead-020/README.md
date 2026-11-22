# LEAD-020: a loop that does not lock in, with action held fixed, ablated

The study for LEAD-020 (QUESTION-121). The model is described in the
docstring of `loop.py`, and the choices made are listed in `PROGRESS.md`.

Files:

- `loop.py`: the model. `simulate(Config, Params, steps, block, seed)`.
- `test_loop.py`: pytest tests (CASE-106's score identity, the lock-in
  metric, that the world does not depend on the loop, that the bare
  Regime A loop locks in, that the post-hoc loop does not, and that no
  evidence means blindness).
- `run.py`: the factorial over the six switches (sense, capture, body,
  commit, fluency, others; capture needs sense) under 20 parameter variants
  (the default and one-at-a-time changes), plus the post-hoc reading of
  "no commitment". It writes 20 seeds per cell, 3000 steps, blocks of 300.
  It appends to `results.jsonl` and resumes from it.
- `analyse.py`: the summary, written to `summary.txt`.

Rerun (CPU only, about 35 minutes):

    cd scratch/studies/lead-020
    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider test_loop.py
    rm -f results.jsonl && python3 -I run.py
    python3 -I analyse.py > summary.txt

Statuses in `summary.txt`: *free* means a lock-in rate of 0.05 or less;
*locks* means 0.5 or more; *partial* means in between; *blind* means the
loop did not track even the first block, which happens when it has no
evidence channel. Lock-in is counted only on switches away from the
interpretation held at the switch.
