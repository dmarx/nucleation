# LEAD-081: CASE-099 with declared demands and a feasible-update oracle

The study LEAD-081 asks for: A39's "case study 2", the extension of CASE-099
(and CASE-092) with declared demands and an oracle for feasible updates,
intervening only on how influence is allocated, with search and information
held fixed. Filed as an executed-study CASE (see the record for its code).

## Model (`model.py`)

- State θ ∈ ℝ², three components, one per demand. Demand i is met when
  L_i(θ) = ½(θ − c_i)ᵀH(θ − c_i) ≤ τ_i. Centres spread round the unit circle;
  in the satisfiable instances a point near the origin is put inside every
  region (checked on a grid), in the structural ones no point is.
- Declared local requirement each step (CLAIM-365's form): ε_i + g_iᵀd ≤ 0
  with ε_i = min(L_i − τ_i, η), η = 0.05: an unmet demand asks for progress
  η, a met one asks only not to be broken.
- Admissible updates U_r = {‖d‖₂ ≤ r}.
- **Feasible-update oracle**: Φ_r = min_{d∈U_r} max_i(ε_i + g_iᵀd), computed
  exactly in 2-D by enumerating the vertices of the arrangement
  (`oracle_exact2d`), cross-checked against an SLSQP primal and the dual
  max_{λ∈Δ} λ·ε − r‖Gᵀλ‖ (CLAIM-365) in the tests.
- **Allocation oracle**: Φ_alloc = min_w m(d(w)) over a simplex grid of step
  1/60: the best the same update map and the same gradients achieve by
  changing only the allocation. Φ_alloc ≥ Φ_r always; in every run here,
  Φ_r ≤ 0 implied Φ_alloc ≤ 0 (the "unreachable" column is 0), so every
  realized violation was one some allocation would have avoided.
- **Governance**: influence weights w ∈ Δ; the actual update is
  d(w) = −g_w·min(1, r/‖g_w‖), g_w = Σ w_j g_j (A34's rule, clipped). This
  map ("search") and the gradients ("information") are the same under every
  allocation rule.
- **Allocation rules** (w ← δw + (1−δ)·softmax(γs)):
  - `A`: s_j = cos(−g_j, d), agreement of component j's own proposal with the
    update made: scored through the interpretation whose authority is being
    evaluated (CASE-092 Regime A; CASE-099's γ arrow, with d(w) its β arrow).
  - `B`: s_j = (ε_j + g_jᵀd)/η, how badly demand j fared under the update
    made: evidence that does not pass through agreement with d (Regime B).
  - `fixed_uniform`, `fixed_random` (Dirichlet(1), per instance): fixed
    weighting rules.
  - `oracle`: w = the allocation oracle's minimizer each step.
- **Measures**, over the last half of T = 200 steps: `violation` (m(d) > 0),
  `realized_violation` (m(d) > 0 with Φ_r ≤ 0, CLAIM-357's term),
  `gov_frustration` (m(d) > 0 with Φ_alloc ≤ 0), `structural` (Φ_r > 0),
  `regret` Γ = m(d) − Φ_r, demands all met at the end, capture (max w > 0.9).

## Sweep (`sweep.py`, ~3.5 min wall on 4 cores; `fixed_hindsight.py`, ~1 min)

Paired by seed: the same 200 satisfiable instances, starts (radius 2.2) and
initial weights (uniform ± 0.02) under every configuration.

1. Allocation rules at base (r = 0.1, γ = 8, δ = 0.9, no noise, H = I).
2. Optimizer and information controls, r ∈ {0.05, 0.2, 0.4}, gradient noise
   σ ∈ {0.1, 0.3} (the same noisy gradients feed the update and the scores),
   conditioning H = diag(1, 5), under fixed_uniform, A, B and oracle.
3. Regime A's conferral parameters, γ ∈ {0, 1, 2, 4, 8, 16} × δ ∈ {0.5, 0.8,
   0.9, 0.95}.
4. Structural control: 100 instances with no common region.
5. `fixed_hindsight.py`: on 60 instances, every fixed weighting on a 1/10
   simplex grid, keeping the best per instance, against A and B.

Results: `results/summary.md`, `results/summary.json`,
`results/fixed_hindsight.json`.

## Rerun

    python3 -I -m pytest -q -p no:cacheprovider test_model.py
    python3 -I sweep.py
    python3 -I fixed_hindsight.py

numpy 2.5.3, scipy 1.18.1, Python 3, CPU only. Seeds are fixed.
