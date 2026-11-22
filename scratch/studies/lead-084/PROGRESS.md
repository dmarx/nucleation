# LEAD-084 progress

- Lead: LEAD-084 (advances QUESTION-222)
- Branch: claude/lead-084-markov-augmentation (cut from origin/staging)
- Task: for a stated class beyond the scalar linear Gaussian case, give
  conditions under which the reduced process has a finite-dimensional
  Markovian augmentation, with its dimension k and its prediction error in
  terms of the eliminated dynamics; compare with the Kalman filter in the
  linear Gaussian case (NOTE-989, NOTE-1015); and rule whether the level
  criteria apply to the augmented state. numpy checks with pytest.
  File a demonstrated CLAIM for what is proved, a CASE for the numerical
  study, dated notes on QUESTION-222 and LEAD-084, a changelog fragment.

## Step 1: is the target already held?

Not held (checked 2026-11-22 on staging 49bd03d85). CLAIM-398 holds scalar
Y in VAR(1) (ARMA(n, n-1)) and says explicitly that the truncation bound and
vector Y are not part of it. NOTE-989 gives the augmentation sizes for the
linear class (Hankel rank, Krylov dimension) and leaves controlled-error
truncation open. NOTE-1015 names the Kalman comparison as open.
CASE-tmpo5jhq (LEAD-173) uses a Kalman predictor only to compute transfer
entropy. No claim or case states a finite-memory error bound.

## Choices

- Class: stable linear Gaussian VAR(1), vector coarse variable Y = LX
  (m >= 1), no observation noise. "Beyond the scalar case" taken as vector
  Y plus the truncation bound, which CLAIM-398 left open.
- Committed study files here, per the run-lead skill; transient files in
  the session scratchpad's lead-084/ directory.

## Done

- augment.py: exact covariances, Riccati recursion, steady filter (reduced
  DARE, cross-checked against iteration to 5e-13), finite-lag error,
  fixed-gain bound, Mori frame, reduced filter, k_min, MZ Hankel rank,
  Krylov dimension, transfer entropy of Y and of the augmented Z.
- Exploration (session scratchpad): Riccati p-step error equals the p-lag
  regression error to 1e-15; the bound 0 <= E_p - E_inf <= B_p holds; the
  Kalman augmentation (Y, k_min coords) is Markov and T(X->Z) = T(X->Y).
  On 2000 random models rho(A_cl) > rho(A22) (Mori frame) in 51%, and
  > rho(Atilde) in 3.4% (worst ratio 1.18); Atilde unstable in 28%.
  No violation with n - m = 1, where |a_cl| <= |atilde| is proved.

## Next

- run.py + test_augment.py + results; README.
- File CLAIM (demonstrated), CASE, notes on QUESTION-222 and LEAD-084,
  changelog.
