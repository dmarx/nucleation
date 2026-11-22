# LEAD-065: removing the core of Ito and Kaneko's network

This reimplements the coupled-map network of Ito and Kaneko (PRL 88, 028701,
2002; arXiv:cond-mat/0108408 v1; the record's LIT-1842, read in NOTE-1414).
It then removes core units, or makes them rare in influence, and asks whether
the core is refilled.

## Model

These are eqs. (1)–(2) of the preprint, as NOTE-1414 transcribes them,
checked against arXiv's v1:

    x_{n+1}^i = f[(1 - c) x_n^i + c Σ_j w_n^{ij} x_n^j],   f(x) = a x (1 - x)
    w_{n+1}^{ij} = [1 + δ g(x_n^i, x_n^j)] w_n^{ij} / Σ_j [1 + δ g(x_n^i, x_n^j)] w_n^{ij}
    g(x, y) = 1 - 2|x - y|

The paper's settings are used: N = 100, a = 3.97, c = 0.12, δ = 0.1,
w_ii = 0, w_ij = 1/(N − 1) and x ~ U(0, 1). Both updates use the values at
time n. The preprint writes both right-hand sides with x_n and w_n, so the
update is simultaneous.

## Protocol (`removal.py`)

1. Each of 12 seeds is grown for t0 = 3 × 10⁶ steps, the time by which the
   paper sees no more migration between groups. The core is the set of
   units whose total outgoing weight W_out, averaged over the last 50,000
   steps, exceeds 1. The mean of W_out is 1 by construction. The paper's
   own criterion is recorded alongside: a snapshot out-degree above 20,
   with a link counted when w > 1/(N − 1), scaled to 20 (M − 1)/99 for a
   network of M units. Table I's four block counts are recorded with it.
2. Five arms run from the same grown state, each for t1 = 10⁶ steps:
   - **control**: no intervention.
   - **remove_periph**: delete k random periphery units, where k is the
     size of the core. This arm controls for the smaller network.
   - **remove_core**: delete every core unit, then renormalize each
     survivor's incoming weights.
   - **remove_half_core**: delete a random half of the core, rounded up.
   - **suppress_core**: keep the core units but multiply every weight given
     to them by ε = 10⁻³, then renormalize. This is QUESTION-132's test of
     recovery from small positive influence.
3. At 6 × 10⁴, 2 × 10⁵, 5 × 10⁵ and 10⁶ steps after the intervention, each
   arm is classified again from a 50,000-step average. The units now in the
   core are counted by origin: core at t0 or periphery at t0.

## Rerun

    python3 -m pytest -q -p no:cacheprovider test_ikmodel.py   # 8 tests, < 1 s
    python3 -I removal.py --seeds 12 --t0 3000000 --t1 1000000 --procs 4
    python3 -I analyze.py results/runs.json                    # writes results/summary.md

The full run takes about 25 minutes on 4 CPU cores with numpy alone.
`results/runs.json` holds every checkpoint of every arm and seed, with the
core's members by original index and the sorted W_out profile.
`results/summary.md` holds the tables.

## Result

Results are for 12 seeds, 10⁶ steps after the intervention. The tables
are in `results/summary.md`, and the case is CASE-tmpvn7wm (with
CLAIM-tmpf11gs).

- **Reproduction.** The snapshot core is 15.6 ± 1.2 units. There are
  1.6 ± 2.6 periphery-to-core links (paper: 2), and 532 ± 24
  core-to-periphery links (paper: 792).
- **remove_core.** In 12 of 12 seeds, former periphery units form a new
  core of 17.2 ± 0.8 units. The same-sized remove_periph control has one
  of 17.0 ± 1.1. The one-way structure is kept.
- **remove_half_core.** 8.8 ± 0.8 periphery units join the 8.5
  survivors.
- **suppress_core.** The old core regains the role, and its members are
  0.92 ± 0.07 of the core.
