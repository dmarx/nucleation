# LEAD-090: CASE-092's coupled meaning–influence model, its linearization, and its predecessors

The study LEAD-090 asks for. Filed as an executed-study CASE with two
claims (see the record for their codes; the changelog fragment is
`record/changelog.d/lead-090.md`).

## Rerun

    cd scratch/studies/lead-090
    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider --rootdir=. test_model.py   # 13 tests, ~2 s
    python3 -I run.py            # all experiments, ~10 min on a loaded 4-core machine
    python3 -I run.py e3 e4      # or some of them

Each experiment writes `results/<name>.json` when it finishes.

## Model (`model.py`)

CASE-092 as read here. Two hypotheses A, B; a fixed corpus, balanced
(imbalance b = 0) except in the hysteresis sweep; two specialists, s_A = +1,
s_B = −1, specialization σ. State: p (collective weight on A; m = 2p − 1)
and w (A-specialist's authority; a = 2w − 1).

- Query framed for A with probability q = (1 − ε)p + ε/2 (ε: exploration).
- Each specialist draws k items; an item supports A with probability
  π_j = ½ + (b + s_jσ + φf)/2, f = ±1 the frame (φ: framing effect).
- Meaning: p ← (1 − ρ)p + ρ Σ_j w_j ê_j.
- Conferral score. Regime A soft (default): agreement of j's items with an
  interpretation drawn from the current meaning, p ê_j + (1 − p)(1 − ê_j).
  Regime A hard: share supporting the argmax hypothesis. Regime B: share
  judged relevant, probability r_j (equal under CASE-092's design).
- Conferral rule, two readings of "updated from apparent retrieval success,
  with an adjustable memory timescale": `ema`, w ← δw + (1 − δ)softmax(g·score)
  (LEAD-081's convention); `replicator`, w_A ∝ w_A e^{η s_A}.

Reduced form (mean field, k → ∞, frame averaged; `mean_field`, with the
closed form `mean_field_closed`, equal to 1e-12 in the tests):

    m' = (1 − ρ)m + ρ(b + σa + φ(1 − ε)m)
    a' = δa + (1 − δ) tanh(gσm/2)               Regime A, soft, ema

Linearization at (0, 0), b = 0 (`jacobian_analytic`, checked against
finite differences): α = 1 − ρ(1 − φ'), β = ρσ, γ = (1 − δ)gσ/2, δ, with
φ' = φ(1 − ε). CLAIM-330's condition βγ > (1 − α)(1 − δ) becomes
**gσ² > 2(1 − φ')**: ρ and δ cancel. Fixed points solve the Curie–Weiss
equation a = tanh(J a + h), J = gσ²/(2(1 − φ')), h = gσb/(2(1 − φ')).
Regime B: γ = 0. Replicator: δ_eff = 1 (authority neutral alone), so any
positive loop gives λ+ > 1.

## Predecessors

- `to_bc_params`, `adaptive_bc_step`: a weighted-averaging opinion model
  with one open-minded agent (the collective, self-weight 1 − λ) and two
  stubborn sources at o_j = (b + s_jσ)/(1 − φ'), whose weights relax with
  memory δ toward a homophily kernel. λ = ρ(1 − φ'), κ = g(1 − φ')/2.
  With the agreement kernel exp(κ m o_j) it equals the reduced Regime A map
  for every b; with the Gaussian bounded-confidence kernel
  exp(−κ(m − o_j)²/2) it equals it at b = 0 (δ = 0: memoryless smooth
  bounded confidence).
- `degroot_stubborn_step`: DeGroot / Friedkin–Johnsen with the same sources
  and fixed weights.
- `degroot_friedkin_step` (Jia et al. 2015) and `friedkin2011_step`
  (Friedkin 2011, FJ step) on the three-member system {collective, A, B}.
  Neither power map reads opinions.

## Experiments (`run.py`)

- e1 threshold vs the nonlinear map on 2000 random parameter sets; fixed
  points across ρ and δ; the Curie–Weiss check.
- e2 content-selected capture: mean field from small m0; agent-level from
  the symmetric state, 200 seeds; below threshold; Regime B.
- e3 hysteresis in b for CASE-092, the two adaptive-weight models and
  fixed-weight DeGroot.
- e4 reflected appraisal at symmetric structure; Regime B and Regime A
  with opposite meaning starts.
- e5 identifiability: two CASE-092 parameter sets with the same (λ, o, κ, δ).
- e6 the replicator reading.
