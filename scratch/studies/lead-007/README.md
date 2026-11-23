# LEAD-007 study: equal function, different later learning

A check of the inference the lead run of 2026-11-23 draws from Lippl and
Lindsey (arXiv 2310.02396): in their diagonal-linear-network setup for
pretraining then fine-tuning, a pretrained network and its rescaling
(first layer times c, auxiliary readout divided by c) compute the same
function, reach the same function under readout-only training, and learn
differently under full fine-tuning, with the best c depending on the
main task. Filed as CASE-tmpjn7jc.

Setup: D = 100, auxiliary teacher with 10 unit coefficients, 80
auxiliary samples, Gaussian inputs; pretraining by gradient descent from
weights 1e-3 to near-zero error; fine-tuning as in the paper's §3.3
(pathway weights set to their sum, readout re-initialized to γ = 0.01)
to training loss below 1e-9. Main tasks: "nested" (2 of the 10
auxiliary dimensions, 8 samples) and "dense" (all 10, coefficients of
magnitude 0.5-1.5 with random signs, 14 samples). c in {2, 1, 0.3, 0.1}.
Error is ‖β − β_main‖², the excess square loss for isotropic inputs.

Files:

- `diag_rescale.py`: the run; appends one JSON line per item to
  `results/runs.jsonl` and skips items already written.
- `test_diag_rescale.py`: tests (rescaling keeps the function, the
  fine-tuning start is the zero function, training interpolates, readout
  training reaches the same β from P_c and P_1).
- `analyze.py`: writes `results/summary.json` (cell means, paired sign
  tests, probe agreement).
- `check_lr.py`: reruns three seeds with the step size halved;
  `results/check_lr.json`.
- `check.py`: frontmatter, title and H1 checks for the record files.

Rerun (CPU, numpy, about ten minutes):

    OPENBLAS_NUM_THREADS=1 python3 -m pytest -q test_diag_rescale.py
    OPENBLAS_NUM_THREADS=1 python3 -I diag_rescale.py
    OPENBLAS_NUM_THREADS=1 python3 -I check_lr.py
    python3 -I analyze.py

The step size is set from the current weight scale. A first pass used the
same rule for readout-only training, whose c = 0.1 runs then did not
converge in 400,000 steps; those rows were dropped and rerun with the
rule taken from the first layer alone.
