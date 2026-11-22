# LEAD-157: permutation-aligned barriers over several path families

Code and results for LEAD-157 (QUESTION-069, CLAIM-263, CLAIM-187).
Toy scale, numpy only, CPU.

## Files

- `lb.py`: task, two-hidden-layer ReLU MLP with hand-written backprop,
  alignments (weight matching, activation matching, ReLU-rescaling
  canonicalisation + weight matching, exhaustive permutation search plus
  optimised rescaling), path families (linear, trained quadratic Bezier,
  trained one-bend polychain), barrier, top Hessian eigenvalue, cue-reliance
  test, layerwise feature connectivity.
- `test_lb.py`: pytest (13 tests).
- `run.py`: `e1` (mechanism pairs) and `e2` (load x temperature grid);
  writes `results_e1.jsonl` / `results_e2.jsonl` one item per line and
  resumes by skipping items already written.
- `summarize.py`: writes `summary.md` from the JSONL files.

## Rerun

    cd scratch/studies/lead-157
    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider test_lb.py   # or via pytest.main
    python3 -I run.py e1     # about 15 min on one core
    python3 -I run.py e2     # about 5 min
    python3 -I summarize.py

## Design

- Task: 4 classes, 16 inputs. Cue A (dims 0-3) and cue B (dims 4-7) each
  place an example near one of 3 Gaussian centres of its class; dims 8-15
  are noise. `both`: both cues carry the label; `A`: cue B drawn from a random
  class; `B`: cue A drawn from a random class.
- Mechanism test, independent of any barrier: accuracy when only cue A
  carries the label and when only cue B does.
- e1 pairs (4 per cell; widths 5, 8, 16, 64, 256): `sameA` (two seeds on
  `A`), `sameB`, `both`, `diff` (an `A` net and a `B` net), `twin` (an `A`
  net and a copy permuted and rescaled per unit by factors in
  [e^-1.4, e^1.4]: the same function exactly).
- e2 cells (3 pairs each; widths 4, 6, 8, 16, 64; batch 256, 32, 8 at lr
  0.02): all on `both`; top Hessian eigenvalue for flatness.
- Barrier: max over 25 values of t of L(t) minus the linear interpolation of
  the endpoint values, in cross-entropy and in 0-1 error; e1 on the both-cue
  test set, e2 on the both-cue train set (Yang et al. use training error).
