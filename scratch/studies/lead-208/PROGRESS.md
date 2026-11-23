# LEAD-208 progress

- Lead: LEAD-208 (compute the effective dimensions of the 2D Ising model at
  and away from T_c on one set of finite lattices, for QUESTION-517)
- Branch: `claude/lead-208-ising-dimensions`, cut from `origin/staging`
- Task as understood: on periodic L x L lattices (L = 16, 32, 64) at T_c and
  T_c(1 +/- 0.1), in one observation scheme (spins left after k checkerboard
  decimations, as in THEORY-777), compute (2) the count of Fisher eigenvalues
  with n*lambda >= 1 for n = 10..1e6, (3) predictive information along a
  transfer direction of a width-W strip, exactly, (4) the count of Fisher
  eigenvalues decaying slower than b^(-d) per step, (5) the box-counting
  dimension of the largest geometric spin cluster against 187/96. numpy only,
  CPU, pytest tests, total run under about 20 minutes. File an executed-study
  CASE, CLAIMs, dated notes and a changelog fragment.

## Done

- Step 1, held check (2026-11-23): nothing holds the computation. Grep of
  record/ and scratch/ for LEAD-208 finds only the lead, QUESTION-517,
  SYNTHESIS-119, the readings that note it, and the triage row
  (scratch/lead-triage/2026-11-22.tsv). No changelog fragment, CASE or claim.

## Next

- Write the Monte Carlo, Fisher estimator, transfer-matrix and cluster code
  with tests; run; file.
