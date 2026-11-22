# LEAD-016: adaptive operators, recovery when rare, removal and suppression

A reduced run of CASE-117's design: a population of identically
parameterized operators whose influence and training co-evolve, with
ordinary mixture-of-experts routing as the baseline. Filed as an
executed-study CASE.

## Model (`opmodel.py`)

- C = 4 contexts, p = (0.33, 0.33, 0.32, 0.02); context 3 is rare.
  In context c, y = β_c·x + 0.1·noise, x ~ N(0, I₈), the β_c orthonormal.
- K linear operators a_i = θ_i·x (fixed features), initialized
  N(0, 0.1²/8) and otherwise identical. K = 4 (one per context, no spare)
  and K = 6 (two spare).
- Context-conditioned influence shares π_ci = softmax(Z_c + b)_i; the
  collective outputs Σ_i π_ci a_i.
- Influence rules:
  - `moe`: Jacobs-style gating, logits up the gradient of the mixture
    log-likelihood (h − π), posterior temperature 0.25. Baseline.
  - `moe_aux`: `moe` plus a load-balancing loss 0.01·K·Σ u_i² on batch
    usage (imposed balancing inside the gradient).
  - `moe_bias`: `moe` plus a per-operator bias moved by ±10⁻³ a step
    toward equal batch usage (imposed balancing outside the gradient,
    modelled on auxiliary-loss-free balancing; here the bias enters the
    dense mixing weights, since there is no top-k selection).
  - `rep`: multiplicative context-sensitive contribution,
    Z_ci += 0.05·(collective loss − own loss) per sample.
  - `uniform`: Z fixed at 0 (reference).
- Training exposure: own squared loss weighted by the posterior h (moe
  rules) or the share π (rep, uniform): coupled to influence. Learning
  rate 0.01 per sample, minibatch 8.
- Held-out competence is the analytic risk on the generating
  distribution, (|θ_i − β_c|² + σ²)/(1 + σ²), so no sample the loop saw
  enters it.

## Protocol (`study.py`)

For each rule, K ∈ {4, 6} and 12 seeds: differentiate for 40,000 steps
(~6,400 rare samples). The specialist of R is the operator with the
largest share in R. From the snapshot:

- `rare_frozen_e2/e3/e5`: its share in R set to 10⁻², 10⁻³, 10⁻⁵,
  parameters frozen, 20,000 steps with no further intervention.
- `rare_train_e3`: as above at 10⁻³, parameters trainable.
- `sham_frozen_e3`: the specialist's parameters replaced by a copy of
  context 0's specialist (as incompetent in R as the residents), frozen,
  share 10⁻³: recovery that does not come from competence.
- `remove`: the specialist deleted; 20,000 steps.
- `suppress_*`: its share in R clamped at 10⁻³ for 20,000 steps, then
  released at 10⁻³ with no further intervention for 20,000 steps.
  Coupled: its exposure follows its (clamped) influence. Decoupled: its
  exposure in R stays at its pre-suppression share (QUESTION-134's
  control). `wd0`: no weight decay; `wd`: decay 10⁻⁴ a step in the test
  window, a maintenance cost; `wd_frozen`: coupled with decay, then
  parameters frozen at release.

## Rerun

    python3 -m pytest -q test_opmodel.py
    for r in moe moe_aux moe_bias rep uniform; do python3 -I study.py $r 12 & done; wait
    python3 -I analyze.py
    python3 -I residual.py   # the R specialist's residual direction (QUESTION-135)

Each arm appends one JSON line to `results/runs_<rule>.jsonl`; a restart
skips finished (rule, K, seed, arm) keys and rebuilds arms from the stored
snapshot. `results/summary.md` holds the tables. About 20 minutes on four
free cores; the run of 2026-11-22 shared its machine with other workers,
took 30 minutes, and was cut from 12 seeds to 6 (seeds 0-5; `uniform` has
12, differentiation only).
