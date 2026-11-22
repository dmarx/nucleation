# LEAD-175 progress

- Lead: LEAD-175 (advances QUESTION-363)
- Branch: `claude/lead-175-superposition-sweep`, cut from origin/staging
- Task as understood: in the toy model of superposition (c = 6, r = 2,
  high-sparsity limit; Chen et al. 2023, LIT-1894, as checked in
  THEORY-1275 by scratch/formal/tms_critical_sizes_check.py), (a) run SGD
  at n = 1,000 and on both sides of n ≈ 600 across learning rates, batch
  sizes and initialisations, and say whether the 6-gon is reached
  ("inaccessible" against "not reached"); (b) sample the posterior across n
  and check the critical sample sizes of the chain 4⁺⁺⁻ → 4⁺ → 5 → 5⁺ (and
  5 → 6) that the free-energy formula gives.

## Done

- Step 1: target not already held (no CASE/CLAIM files an SGD sweep or
  posterior sampling across n for this model; QUESTION-363 and THEORY-1275
  name both as open tests).

- tms.py (closed-form population loss and gradient, minibatch gradient,
  classifier) and test_tms.py (19 tests pass).
- SGD sweep launched (results/sgd_b100_b20.jsonl, results/sgd_b5.jsonl);
  posterior PT launched (results/posterior_pt.jsonl); prior anchor
  (results/prior_regions.jsonl).
- Found: the dead sixth column of the 5-gon gets exactly zero gradient from
  every sample, so plain SGD can never revive it (test in test_tms.py;
  confirmed in every 5gon-initialised sweep run).
- Found: Chen et al.'s NUTS likelihood (Eq. 3) carries 1/2, their formula's
  n L does not (App. F.1; L = E||x - f||^2, Table 1). Their NUTS n is 2x the
  formula's n.

- All runs finished (main grid, three extensions, tempering, confined
  runs, prior anchor); results and summaries committed; README "Runs" and
  "Results" written.

## Next

- File: CASE-tmpgqbyq (executed-study, Proposed), CLAIM-tmpg8m7a (frozen
  dead feature, demonstrated), CLAIM-tmp9zqvq (sweep, empirical),
  CLAIM-tmpraadt (posterior critical sizes, empirical); dated notes on
  QUESTION-363, THEORY-1275, LEAD-175; changelog fragment.

## Choices

- Loss: sum over outputs of squared error, no 1/2 (matches Table 1); lr
  0.005 under PyTorch's mean-over-outputs MSELoss would be 0.00083 here, so
  the sweep covers 0.001 to 0.05 (and higher in the extension).
- Budget: 4500 epochs for every (n, B), as the paper; checkpoints record the
  label over training.
- n = 300, 500 (below 600), 700, 1000, 2000 (above); B = 100, 20 for all n,
  B = 5 for n = 500 and 1000 only (time).
- Inits: the paper's perturbed 4-gon (noise sd 0.01), perturbed 5-gon,
  perturbed 6-gon (control), N(0, 1) prior draw; 6 seeds each.
- Posterior: population loss in place of the empirical L_n (removes the
  dataset term; tests the formula's n L + λ log n + c directly); N(0, 1)
  prior as Chen et al.; n reported as the multiplier of L (the formula's n).
- Regions: Chen et al.'s convex-hull count k and positive non-vertex biases
  σ, with a finer count of switched-off vertices (the '-').
