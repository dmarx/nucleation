# LEAD-049: a restricted theorem for differentiated, recoverable specialists

Numerical checks for CLAIM-tmp6kclm (Theorems A, B and C) and
CLAIM-tmpdsv4t (the two-resource counterexample), filed as CASE-tmp5sk3q.

## Model (`model.py`)

k operators, abundance n_i ≥ 0, scalar niche trait θ_i in [0, 1], niche
vector u(θ_i) ≥ 0 in R^m, supply b, cost c_i:

    R      = b − Σ_j n_j u(θ_j)
    dn_i   = n_i (u_i·R − c_i)
    dθ_i   = ε κ_i Proj[u'(θ_i)·R]      κ_i = n_i (canonical equation) or 1

This is gradient flow of L = ½|b − Un|² + c·n in the metric
D = diag(n, εκ/n). Two niche maps: `GaussianNiche` (m resources on [0, 1],
Gaussian utilization of width w) and `TradeoffNiche` (two resources,
u(θ) = (a(θ), a(1 − θ))). Integration is RK4 in (log n, θ), with dt = 0.02,
ε = 0.1 (Gaussian) or 0.2 (trade-off), and the trait clipped to its box.

## Parts (`study.py`)

- **part1**: Theorem B at fixed traits. 2,000 random nonnegative U
  (7 × k, k = 2–6) with an interior n*. Every −i community is found
  exactly, by support enumeration. Then 30 are simulated: the −i
  community, then reinvasion from 10⁻⁶.
- **part2**: Theorems A and C. Gaussian niches (m = 12, b = 1, c = 0.2),
  k = 2–6, w ∈ {0.08, 0.12, 0.2}, 3 seeds. All operators start at
  θ = 0.5 + 10⁻³ noise, and the run lasts T = 400. At the endpoint the
  script checks Theorem A, comparing the numerical Jacobian with −D H.
  Then, for each survivor i: the frozen recovery rate and its bound; the
  adaptive −i run (T = 400) and i's growth against it with its old
  trait; Theorem C's hypothesis; and reinvasion from 10⁻⁶ (T = 800).
- **part3**: the trade-off counterexample. 4 shapes × c/B = 0.1–0.9.
  Theorem A at the corner pair, then the lone resident after removal
  (T = 300), the specialist's growth against it, and reinvasion (T = 400).
- `generalist_check.py`: the lone generalist at θ = 1/2. It checks that
  this is an equilibrium meeting Theorem A, and gives the specialist's
  growth there.

## Rerun

    python3 -I -m pytest -q test_model.py      # 14 tests, ~10 s
    python3 -I study.py part1                  # ~1 min
    python3 -I study.py part3                  # ~5 min (4 processes)
    python3 -I study.py part2                  # ~15–30 min (4 processes)
    python3 -I generalist_check.py

Results are written to `results/` (JSON; the `*_log.txt` files are stdout).
