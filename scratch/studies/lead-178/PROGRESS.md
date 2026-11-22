# LEAD-178 progress

- Lead: LEAD-178 (advances QUESTION-221)
- Branch: claude/lead-178-var1-dependence (cut from origin/staging bea386791)
- Task: for a linear Gaussian VAR(1), bound the dynamical dependence
  (Barnett–Seth transfer entropy T(X -> Y), Y = LX) of a block's aggregate
  in terms of off-block coupling, gap and noise; or exhibit a nearly
  decomposable family where it stays bounded away from zero as coupling -> 0.
  Build on CLAIM-390 (block full state, O(eps^2)), CLAIM-386 (one-step
  deterministic defect), CLAIM-tmplsu2m (LEAD-084, Kalman augmentation).

## Done

- Step 1: target not held. CLAIM-390 bounds a block's full state only;
  CLAIM-386 is the deterministic one-step defect; QUESTION-221 says the
  aggregate's dependence is still open. No later filing found.
- dd.py + test_dd.py (57 pass); run.py -> results.jsonl (850 items);
  summarize.py -> results.md. Sandwich holds on all 600 items.

- Filed CLAIM-tmpllgpb, CASE-tmp2l6id; dated notes on QUESTION-221,
  LEAD-178, CLAIM-390; changelog fragment lead-178.md.

## Next

- Report to the lead (no PR opened by the worker).

## Choices

- Aggregate = block sum (CLAIM-386's Q), but the theorem is for any linear
  L, so the left-Perron-weighted aggregate is covered too (leftvec part).
- Horizon: Barnett-Seth one-step dependence given the whole past; longer
  horizons not done.
- Result: sandwich ½logdet(I+G⁻¹LA Σ_|L AᵀLᵀ) <= T <= same with Π_|L.
  Closed at eps=0 (L A* = B L): T = Θ(eps²), upper constant ~ 1/gap.
  Not closed: floor > 0 as eps -> 0, not removed by the fast gap.
  Simon scaling gap ∝ eps: T = Θ(eps).
