# LEAD-175: SGD sweep and posterior across n in the toy model of superposition

For QUESTION-363 and THEORY-1275 (Chen, Lau, Mendel, Wei and Murfet 2023,
LIT-1894, arXiv 2310.06301v1). The model: c = 6 features, r = 2 hidden
dimensions, high-sparsity limit (x = μ e_i, i uniform, μ ~ U[0, 1]),
f(x) = ReLU(WᵀWx + b), loss ‖x − f(x)‖² (Table 1's L, no factor ½).

## Files

- `tms.py`: closed-form population loss and its gradient (the integrand is
  piecewise quadratic in μ), the minibatch loss and gradient vectorised over
  runs, the critical points of the checker's script, and the region
  classifier (Chen et al.'s convex-hull count k and positive biases σ of
  non-vertex columns, with a finer count of switched-off vertices, written
  as '−').
- `test_tms.py`: pytest (losses against Table 1 and against quadrature,
  gradients against finite differences, classifier on every critical point,
  the dead column of the 5-gon frozen under SGD, the posterior energy and
  the confined sampler). Run: `python3 -I -m pytest -q scratch/studies/lead-175`.
- `sgd_sweep.py`: the SGD sweep; one JSON line per run in
  `results/sgd_*.jsonl`, written per (n, batch) job; resumable.
- `posterior.py`: HMC on p_n(w) ∝ exp(−n L(w)) N(w; 0, I₁₈) over a ladder
  of n: `pt` (parallel tempering, occupancy of each region) and
  `restricted` (sampling confined to one region, for thermodynamic
  integration); one JSON line per block; resumable.
- `prior_regions.py`: prior mass and prior mean of L of each region (the
  n = 0 anchor of the integration).
- `run_restricted.sh`: the confined runs, region by region.
- `analyze_sgd.py`, `analyze_posterior.py`: the summaries;
  `results/posterior_summary.json` is written by the latter.

## Rerun

    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    cd scratch/studies/lead-175
    python3 -I sgd_sweep.py results/sgd_b100_b20.jsonl --batches 100,20
    python3 -I sgd_sweep.py results/sgd_b5.jsonl --batches 5 --ns 500,1000
    python3 -I posterior.py pt results/posterior_pt.jsonl --chains 16 --blocks 30 --iters 400 --burn 4
    python3 -I prior_regions.py results/prior_regions.jsonl --chunks 40
    sh run_restricted.sh
    python3 -I analyze_sgd.py results/sgd_*.jsonl
    python3 -I analyze_posterior.py

Extensions run afterwards are listed under "Runs" below with their commands.

## Choices

- **Units of n.** Chen et al.'s formula f_α(n) = nL_α + λ_α log n + c_α
  (App. F.1) uses Table 1's L = E‖x − f‖². Their likelihood (Eq. 3) is
  exp(−½‖x − f‖²), and their NUTS runs (App. F) sample the posterior of
  that likelihood, which is exp(−(n/2)L_n)φ. The sampler here uses
  exp(−nL)φ, the formula's n; their NUTS sample size n corresponds to n/2
  here.
- **Population loss** in place of the empirical L_n: it removes the dataset
  fluctuation and tests the formula's terms directly.
- **Prior** N(0, I₁₈), as Chen et al. (App. F).
- **SGD loss scale.** The sum of squared errors over the six outputs, mean
  over the batch. Under PyTorch's default MSELoss (mean over outputs too)
  the paper's rate 0.005 would be 0.00083 here; the sweep's rates 0.001 to
  0.05 cover both readings.
- **Budget** 4,500 epochs for every (n, batch), as the paper; checkpoints
  record the region at epochs 10, 100, 300, 1,000, 2,000, 3,000 and 4,500.
- **Grid.** n = 300, 500 (below the paper's 600), 700, 1,000, 2,000; batch
  100 and 20 at every n, batch 5 at n = 500 and 1,000 (time); rates 0.001,
  0.005, 0.02, 0.05; initialisations: the paper's perturbed 4-gon (s.d.
  0.01), the perturbed 5-gon, the perturbed 6-gon (a control), a draw from
  the N(0, 1) prior; six seeds each. Each seed has its own training set,
  shared across rates and initialisations.

## Runs (2026-11-22)

- **Main grid**: 1,152 runs (288 of them the 6-gon control), in
  `results/sgd_b100_b20.jsonl` and `results/sgd_b5.jsonl`; summary
  `results/sgd_summary_main.txt`.
- **Extensions** (`sh run_extensions.sh short`, `sh run_extensions.sh long`):
  batch 1 at rates 0.05, 0.1, 0.2 for 1,000 epochs at n = 500 and 1,000
  (72 runs); the 5⁺-gon initialisation on the main grid at n = 1,000 (48
  runs); 45,000 epochs at n = 1,000, batch 20, rates 0.02 and 0.05 (24
  runs). Summary `results/sgd_summary_extensions.txt`.
- **Posterior**: parallel tempering, 16 chains × 44 rungs (n = 20 to
  10,000), 30 blocks of 400 HMC iterations, 4 discarded; confined runs, 8
  chains × 64 rungs (n = 0.5 to 10,000), 12 blocks for regions 6 and 5, 9
  for the others, 3 discarded; prior anchor 2,000,000 draws. Summary
  `results/posterior_summary.json`.

## Results

**SGD.** Of 1,008 runs not started at the 6-gon, none ended at it, and
none passed through it at any checkpoint (35 checkpoints of one prior draw
read 6⁻⁻, a hull of six with two features off, which lost them). All 288
control runs started at the 6-gon stayed there. Every 5-gon start ended at
the 5-gon (288 of 288); every 5⁺-gon start stayed at the 5⁺-gon (48 of
48 at 4,500 epochs, 8 of 8 at 45,000). Higher noise (batch 1, rates to
0.2) ended with fewer features, not more. No n, batch, rate or
initialisation differs.

**Why the 5-gon cannot go on.** A feature whose output is silenced
(W_k·W_i + b_i ≤ 0 for every input k) and whose input excites nothing
(W_i·W_j + b_j ≤ 0 for every j ≠ i) gets an exactly zero gradient in
(W_i, b_i) from every sample; at the 5-gon, W₆ = 0 and b₆ < 0 hold for
as long as the other biases stay non-positive. SGD's noise is zero in
those coordinates, so no rate, batch or time moves them
(`test_dead_column_of_the_5gon_is_frozen_under_sgd`; in the sweep, 386 of
the 476 5-gon endings have the dropped column frozen outright and 460 have
its output silenced).

**Posterior** (n is the formula's, the multiplier of L; Chen et al.'s NUTS
n is twice it). Region free energies by integration agree with the
tempering run's occupancy (114 (pair, n) points, rms 0.13 nats). The local
learning coefficients n(E[L] − L_crit) at n = 10,000 are 7.2 (5-gon), 8.5
(5⁺) and 8.6 (6), against Table 1's 7, 8.5, 8.5.

| transition | formula, λ̂ | formula, λ theory | tempering | integration |
|---|---|---|---|---|
| 4⁺⁺⁻ → 4⁺ | 190 | 190 | — | none: 4⁺ ahead from n ≈ 3 |
| 4⁺ → 5 | 370 | 237 | — | ≈ 1: 5 ahead from the prior on |
| 5 → 5⁺ | 2,477 | 1,593 | — | 781 |
| 5 → 6 | 538 | 601 | 265 | 279 |
| 5⁺ → 6 | 17 | 202 | 34 | 45 |

The dominant region (of those integrated) runs 4⁺, 4 (from n ≈ 1), 5
(from 77), 6 (from 315). The regions of the 4-gon family, as classified,
are not dominated by their critical points at large n (their n(E[L] −
L_crit) goes negative): their free energies are those of the regions,
which is what the tempering run and Chen et al.'s Fig. 2 count.
