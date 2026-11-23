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

- Code written (ising.py, fisher.py, strip.py, clusters.py, run_study.py,
  analyze.py) with 13 pytest tests, all passing.
- Choices made:
  - Parameters: field + 12 two-spin couplings (every offset in the 5x5 box up
    to sign) = 13, the main-text count of THEORY-777's source.
  - Sampler: Swendsen-Wang at all three temperatures (they are within 10% of
    T_c, and SW keeps the symmetric ensemble below T_c); Metropolis is
    checked against exact enumeration in the tests only.
  - Fisher estimator: level 0 Cov(Phi); level 1 exact conditional means
    given the black sublattice; level >= 2 two compatible chains (SW +
    heat-bath, observed sites frozen, burn 3, 2 measurements) per config,
    cross product. Burn 1 vs 8 checked at L = 32.
  - Relevant count: eigenvalue rank whose fitted per-step factor has its
    2-sigma lower bound above 2^(-1/2), midway in log between b^(-d) = 1/2
    and 1.
  - Predictive information: both the lead's column-block definition and a
    single-row definition, exact by transfer matrix.
- Runs: strip (W <= 12) and Monte Carlo L = 16, 32 done; L = 64 running.

## Next

- Finish L = 64 and the burn check; analyse; file CASE, CLAIMs, notes,
  changelog.
