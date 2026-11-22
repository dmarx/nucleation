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

## Next

- Library + pytest; SGD sweep; posterior sampling; filing.

## Choices

(filled in as made)
