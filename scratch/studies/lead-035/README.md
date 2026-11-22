# LEAD-035: SNR singular values against (4t/N)^(1/4)

Han, Papyan and Donoho (LIT-974, read in NOTE-783) derive, for
unconstrained features on the central path, with no weight decay and the
features re-whitened to Sigma_W = I after every step (their A3), that the
singular values omega_j of Sigma_W^(-1/2) M~ grow as (4t/N)^(1/4) and
tend to equality (Proposition 2, Corollary 1). This study measures omega_j
in models trained without that re-whitening.

## Files

- `snr.py`: the measures (omega_j, L_LS, NC1), the prediction (the
  asymptote and the exact implicit solution of Proposition 2), the
  unconstrained-features dynamics, and a numpy ReLU MLP with optional
  full-batch batch normalization.
- `test_snr.py`: pytest checks. Lemma 1 against the least-squares loss;
  invariance of omega to linear maps; gradients by finite differences;
  the exact solution; and that one step of the projected (renormalized)
  flow moves omega_j at Lemma 5's rate, which fixes the time unit:
  t = learning rate x steps, with gradients of the sample-averaged loss.
- `run.py`: the items (model, setting, seed); each appends one JSON line
  with its trajectory at log-spaced steps. Reruns skip items present.
- `analyze.py`: late-window (last decade of t) log-log slopes, the
  max/min ratio, omega against (4t/N)^(1/4), and L_perp/L_LS; writes
  `summary.json`.
- `results-*.jsonl`, `summary.json`: the results.

## Setting

C = 4 classes, N = 50 per class. Unconstrained features in R^16; MLP
inputs a four-class isotropic Gaussian mixture in R^20 (means at norm 3).
Full-batch gradient descent, MSE, three seeds per setting.

- `ufm-renorm`: Han et al.'s flow (projected gradient of L_LS, then
  re-whitening), eta 200, 20000 steps. The control.
- `ufm-lsplain`: plain gradient of L_LS (classifier at its least-squares
  optimum), no re-whitening: A3 dropped, nothing else. eta 20.
- `ufm-joint`: ordinary gradient descent on (W, b, H), lambda 0. eta 0.5.
- `mlp2-wd*`: ReLU MLP 20-64-32, linear readout; `mlp3bn-wd*`: 20-64-64-32
  with batch normalization (no affine) before each ReLU. lr 0.05,
  200000 steps, weight decay 0 or 5e-4.

Runs stop early once omega is past double precision (L_LS < 1e-11 or the
conditioning of Sigma_W below 1e-13).

## Rerun

    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider test_snr.py
    python3 -I run.py ufm --out=results-ufm.jsonl
    python3 -I run.py mlp2 --out=results-mlp2.jsonl
    python3 -I run.py mlp3bn --out=results-mlp3bn.jsonl
    python3 -I analyze.py .

`--quick` runs a tenth of the steps. The full set took about XX minutes
on a shared four-core machine.
