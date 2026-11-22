# LEAD-052: acquisition order on a known tree, with each level's strength set independently of the tree

Run on 2026-11-22. numpy on CPU, BLAS threads 1; no downloads.

## Files

- `phases.py`: the data, the four kinds of learner, the acquisition measure
  and the order classifier.
- `run_all.py`: every arm; appends one JSON line per item to
  `results/runs.jsonl` and skips items already written, so it resumes.
  `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I run_all.py` (about
  seven minutes on one core; `E1`, `E2` or `E3` alone).
- `compact.py`: rounds the results file to five significant figures (run
  once after `run_all.py`; the committed file is the rounded one).
- `analyse.py`: phase maps and summary numbers, `python3 -I analyse.py
  [delta] [tol]`; writes `results/summary_<delta>_<tol>.json`. Committed
  for (0.1, 1.25), the main setting, and for (0.5, 1.25), (0.02, 1.25),
  (0.1, 1.1) and (0.1, 1.5).
- `test_lead052.py`: `python3 -I -m pytest -q test_lead052.py` (11 tests,
  under a second).
- `PROGRESS.md`: the worker's log of steps and choices.

## Design

**Tree and levels.** Eight items are the leaves of a binary tree of depth
3. The Haar basis of R⁸ splits by level: level 0 is the constant vector;
level ℓ = 1, 2, 3 holds 2^(ℓ−1) vectors, each ± on the two children of one
node at depth ℓ − 1. Level ℓ is the set of distinctions the tree draws at
depth ℓ: level 1 the root split (coarse), level 3 the leaf pairs (fine).

**Strength per level, independent of the tree.** Inputs and targets are
written in that basis with their own strength per level, then rotated at
random: X = √N H diag(c) R_in, Y = √N H diag(g) R_out (c₀ = 1, g₀ = 0). So
the input covariance has eigenvalue c_ℓ² on level ℓ and the input–output
correlation has singular value s_ℓ = c_ℓ g_ℓ there. The tree fixes the
vectors; c and g fix the strengths, freely.

**Acquisition.** With P_ℓ the projector onto level ℓ's span in item space
and F the network's outputs on the items, level ℓ's relative risk is
r_ℓ = ‖P_ℓ(F − Y)‖² / ‖P_ℓY‖², and T_ℓ(δ) is the first time r_ℓ ≤ δ:
QUESTION-217's T_ℓ(δ), with the network's own output as the decoder. Main
δ = 0.1. Time is gradient-flow time (a step of size η advances it by η);
loss (1/2N) Σ‖f(x_i) − y_i‖², full batch.

**Order classes.** Two levels tie when the later time is at most 1.25
times the earlier. Coarse-first: some coarser level ahead of a finer one,
none behind. Fine-first: the reverse. Simultaneous: all tied. Mixed: both
directions present (for example level 1, then 3, then 2).

**Learners.**

| name | what |
|---|---|
| `kernel_linear` | the linear kernel, i.e. a single linear layer, exact gradient flow |
| `kernel_relu_ntk` | infinite-width NTK of a two-layer ReLU network, exact gradient flow |
| `relu_ntk_2048`, `relu_ntk_64` | two-layer ReLU, NTK parametrization, width 2048 and 64, η = 0.05 |
| `deep_linear_2`, `deep_linear_3` | linear, 2 and 3 weight layers, width 16, per-layer init scale 0.01 and 0.05 |
| `relu_small` | two-layer ReLU, standard parametrization, width 64, init scale 0.01 |
| `relu_std_1` | the same at init scale 1, η = 2·10⁻⁴ |

The ReLU networks start at zero output (antisymmetric pairs of hidden
units, as in LEAD-045's network.py). Three seeds (data rotation and
initialization) per network cell.

**Grids.**

- E1, target strengths varied, inputs flat (c = 1): g = (0, 1, a, b),
  log₂ a, log₂ b ∈ {−2, −1.5, …, 2}; 81 cells.
- E2, input and target strengths varied together, geometric in the level:
  c_ℓ = ρ_in^(ℓ−1), g_ℓ = ρ_out^(ℓ−1), log₂ ρ ∈ {−0.5, −1/3, …, 0.5}; 49
  cells. ρ < 1 makes coarse levels stronger.
- E3, on three target profiles with flat inputs (g = 1, ½, ¼; ¼, ½, 1;
  1, ¼, ½): the standard-parametrization ReLU at init scale 0.003 to 3,
  and the NTK-parametrized one at width 64 to 4096.

## Derivation: what is exact here

**1. The levels commute with every kernel of the inputs.** Every item has
the same norm, and the inner product of two items depends only on the
depth of their lowest common ancestor. So any kernel that is a function of
the inner product and the two norms (every dot-product kernel, and the
infinite-width NTK of any fully connected network) gives a Gram matrix
whose entries depend only on that depth: K = Σ_d a_d B_d, with B_d the
block matrix of ones on the depth-d subtrees (B₃ = I). A level-ℓ Haar
vector is constant on each depth-d block when ℓ ≤ d, so B_d acts on it as
N/2^d, and sums to zero on each depth-d block when ℓ > d, so B_d kills it.
Hence each level span is an eigenspace: [K, P_ℓ] = 0 exactly, with
eigenvalue μ_ℓ = Σ_{d ≥ ℓ} a_d N/2^d. This is QUESTION-217's Conjecture A
condition, holding by symmetry. (Test: commutator below 10⁻¹⁰ for tree
inputs, above 10⁻³ for random ones.)

**2. Kernel regime.** Gradient flow from zero output gives
F(t) = Y − exp(−Kt/N) Y, so r_ℓ(t) = exp(−2μ_ℓ t/N) exactly and
T_ℓ(δ) = N ln(1/δ) / (2μ_ℓ). The order of acquisition is the order of
μ_ℓ, which is a function of the inputs alone: the target strengths g do
not enter. For the linear kernel μ_ℓ ∝ c_ℓ², so acquisition is coarse-first
exactly when c_ℓ falls with depth, whatever g does.

**3. Deep linear network, decoupled balanced start.** With mode strength a
on level ℓ, ȧ = 2a(s_ℓ − c_ℓ²a) (Saxe, McClelland and Ganguli; THEORY-186),
so b = c_ℓ²a/s_ℓ is logistic at rate 2s_ℓ and
T_ℓ(δ) = (1/2s_ℓ)[ln(b₁/(1 − b₁)) − ln(b₀/(1 − b₀))], with b₁ = 1 − √δ and
b₀ = c_ℓ²ε/s_ℓ for a common small initial strength ε. As ε → 0,
T_ℓ/T_m → s_m/s_ℓ: the order is by the cross-covariance s_ℓ = c_ℓ g_ℓ.
At ε = 10⁻⁴ the formula gives 4.99, 9.29, 17.2 for g = (1, ½, ¼); the
trained two-layer network from random small weights gave 5.29, 9.59, 19.0.

So the two learners' phase boundaries lie on different surfaces: for the
kernel, on the input profile alone (in E2, ρ_in = 1); for the deep linear
network, on the product (ρ_in ρ_out = 1). The decoupled start is assumed
in 3; 1 and 2 need no assumption beyond the tree-symmetric data and the
kernel limit.

## Results (δ = 0.1, tie at 1.25; three seeds per network cell)

Agreement is the fraction of cells whose majority class matches the
class predicted by ordering levels by s_ℓ = c_ℓ g_ℓ ("by cross-covariance")
or by c_ℓ² ("by input variance"). Exponents: within-cell least squares of
log T_ℓ on log g_ℓ and log c_ℓ, pooled over cells and seeds (T ∝ g^βg c^βc).

**E1 (target strengths varied, inputs flat).**

| learner | C / F / S / M cells | agrees: cross-cov | βg (R²) | seed-split cells |
|---|---|---|---|---|
| kernel_linear, kernel_relu_ntk | 0 / 0 / 81 / 0 | 0.01 | 0 | 0 |
| relu_ntk_2048 | 1 / 0 / 79 / 1 | 0.03 | −0.04 | 6 |
| deep_linear_2 | 14 / 14 / 1 / 52 | 1.00 | −0.92 (1.00) | 0 |
| deep_linear_3 | 14 / 14 / 1 / 52 | 1.00 | −1.26 (0.96) | 11 |
| relu_small | 35 / 12 / 18 / 16 | 0.42 | −0.36 (0.65) | 15 |
| relu_std_1 | 8 / 18 / 10 / 45 | 0.80 | −0.43 (0.85) | 39 |
| relu_ntk_64 | 32 / 19 / 2 / 28 | 0.64 | −0.41 (0.77) | 58 |

With flat inputs every exact kernel acquires all three levels at the same
time in every cell (the levels share one eigenvalue), and the width-2048
network does the same in 79 of 81. The two-layer deep linear network's
map is the cross-covariance map cell for cell: coarse-first in the 14
cells where g falls with depth, fine-first in the 14 where it rises, mixed
elsewhere. Its map (rows log₂ a from −2 to 2, columns log₂ b from −2 to 2):

    CMMMMMMMM      (log2 a = -2; log2 b = -2 ... 2 across)
    CCMMMMMMM
    CCCMMMMMM
    CCCCMMMMM
    CCCCSFFFF      (a = 1)
    MMMMMFFFF
    MMMMMMFFF
    MMMMMMMFF
    MMMMMMMMF      (log2 a = 2)

The small-initialization ReLU network orders the levels the same way
wherever it orders them (no cell is coarse-first where the deep linear
network is fine-first, or the reverse), but its acquisition times are
compressed: T ∝ g^(−0.36) against g^(−0.92), so 18 cells the deep linear
network separates are simultaneous for it, and much of the mixed region
becomes coarse-first. The weaker levels are pulled along by the strongest:
at g = (1, 1, 4) the deep linear network took 5.5, 5.5 and 1.5 to acquire
levels 1, 2 and 3, the ReLU network 2.4, 2.5 and 2.1. The compression is
stronger when the strong level is fine than when it is coarse (at
g = (1, ¼, ¼), times 8.1, 16, 17 against the deep linear network's 5.3, 19,
19).

    CmMMMMMMm      relu_small, E1, same layout
    CCmMMMmmm
    CCCCcsfFF
    CCCSSSSfF
    CCCSSSSSS
    CCCCSSSSS
    CCCCCSSff
    CCCCCCfFF
    CCCCCcmFF

**E2 (inputs and targets both geometric in the level).** Rows log₂ ρ_in
from −0.5 (coarse inputs stronger) to 0.5; columns log₂ ρ_out likewise.

    kernel_relu_ntk   deep_linear_2   relu_small   relu_ntk_2048
    CCCCCCC           CCCCCCS         CCCCCSS      CCCCCCC
    CCCCCCC           CCCCCSS         CCCCSSS      CCCCCCC
    CCCCCCC           CCCcSsF         CCcSSSS      CCCCCCC
    SSSSSSS           CCSSFFF         CsSSSSS      SSSSSSS
    FFFFFFF           CSSFFFF         SSSSSSS      FFFFFFF
    FFFFFFF           SSFFFFF         SSSSSSf      FFFFFFF
    FFFFFFF           SFFFFFF         SSSSSSF      FFFFFFF

| learner | βg | βc | R² | agrees: cross-cov / input variance |
|---|---|---|---|---|
| kernel_linear | 0 | −2.00 | 1.00 | 0.63 / 1.00 |
| kernel_relu_ntk | 0 | −1.14 | 0.94 | 0.63 / 1.00 |
| relu_ntk_2048 | −0.00 | −1.15 | 0.94 | 0.63 / 1.00 |
| deep_linear_2 | −0.95 | −1.12 | 1.00 | 0.90 / 0.65 |
| deep_linear_3 | −1.83 | −1.07 | 0.85 | 0.76 / 0.51 |
| relu_small | −0.42 | −0.43 | 0.71 | 0.45 / 0.41 |
| relu_std_1 | −0.34 | −1.10 | 0.85 | 0.76 / 0.82 |
| relu_ntk_64 | −0.34 | −0.98 | 0.65 | 0.63 / 0.82 |

The kernel's boundary is horizontal here (set by ρ_in alone), the
two-layer deep linear network's is the anti-diagonal ρ_in ρ_out = 1, and
the small-initialization ReLU network weighs inputs and targets equally,
as the deep linear network does (βg ≈ βc), at about 0.4 of its exponent,
so most of its map is simultaneous. The order-one ReLU networks at width
64 lie between: their input exponent is the kernel's, their target
exponent is not zero.

**E3 (the transition).** NTK parametrization, by width: 64 follows the
target strengths in all three profiles and all seeds (C, F, M; βg = −0.45);
256 is mostly simultaneous (βg = −0.10); 1024 and 4096 are simultaneous in
every run (βg = −0.01). Standard parametrization at width 64 follows the
target strengths at every init scale from 0.003 to 3 (βg between −0.36
and −0.44): at this width, scale alone did not bring the kernel order.

**Robustness.** At δ = 0.5 and 0.02, and with ties at 1.1 or 1.5, the
kernel and width-2048 maps and the deep linear maps hold their pattern
(agreement with their predicted order 0.88 to 1.00 in E1, except
deep_linear_3 at a 1.5 tie, 0.75; 0.88 to 0.98 for deep_linear_2 in E2),
and in no setting is a small-initialization ReLU cell coarse-first where
the two-layer deep linear network is fine-first, or the reverse; the size of the
simultaneous region of the ReLU network moves with the tie threshold
(E1: 2 cells at 1.1, 47 at 1.5), as it must for compressed times.

## What it does and does not show

- In this tree-symmetric family the conjectured commutation condition
  holds exactly for every kernel learner, and the order is then set by the
  kernel's per-level eigenvalue, which here depends on input strengths
  only. A kernel learner never "sees" which level the targets make strong.
- A deep linear network orders by the cross-covariance per level, so the
  same data can be coarse-first for one learner and simultaneous or
  fine-first for the other: acquisition order is a joint property of data
  and learning operator, not of the tree.
- Where the tree's coarse levels are weaker than its fine ones, every
  learner here that depends on strength acquires fine before coarse:
  depth in the tree set no order by itself in any arm.
- A small two-layer ReLU network from small initialization keeps the deep
  linear network's direction but compresses the spread of acquisition
  times by more than half (in log), so simultaneity is common for it.
  Not explained here.
- The three-layer linear network weighs target strength more than input
  strength (βg −1.8 against βc −1.1 in E2), which the decoupled solution
  for two layers does not predict; not explained here.
- Not shown: larger trees, noisy or sampled items, hidden-layer probes as
  decoders (acquisition here is the network's own output), stochastic
  batches, other optimizers, non-symmetric data where [K, P_ℓ] ≠ 0, and
  any network wider or deeper than those listed.
