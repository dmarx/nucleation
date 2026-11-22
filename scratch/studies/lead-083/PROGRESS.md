# PROGRESS: LEAD-083

Branch: claude/lead-083-closed-mode

## Task as understood

LEAD-083: simulate a mode that is dynamically closed but is not a
gap-isolated block, perturb it, and measure compensation and entrainment;
set the result beside CLAIM-157's block test. Scoped to about an hour of
CPU, core arms first. File a CASE (executed-study), a CLAIM if warranted,
and dated notes on LEAD-083, QUESTION-218 and CLAIM-157.

## Done

- Read CLAIM-157, QUESTION-218, QUESTION-219, CASE-269, CLAIM-388,
  CLAIM-172, CLAIM-164, CLAIM-154, CASE-tmpfktyl (LEAD-069's study).
- study.py and test_study.py written; 6 tests pass.
- Arm A (kink) complete in results.jsonl: spectrum, block test by
  segment length, compensation at t = 5 and 50 for kink centres 0 and 6,
  h = 1, 0.5, 0.25. Kink centred between sites (on-site is the PN saddle).
  Compensation read on the overdamped flow, not by minimization (L-BFGS
  jumped Peierls-Nabarro wells).
- Arm B coupling lowered to K = 1.9 (K = 2.5 locked 194 of 200; 1.9 locks
  156, leaving 44 drifting as the environment).
- One run was killed by the memory limit (cause not found; reruns go under
  ulimit -v).
- CASE-tmpwyp15 and CLAIM-tmpjwc0h created by luria new (templates).

- All arms complete (results.jsonl, 18 items). summarize.py prints the tables.
- Filed: CASE-tmpwyp15 (executed-study), CLAIM-tmpjwc0h (thesis,
  demonstrated), dated notes on LEAD-083, QUESTION-218, QUESTION-219,
  CLAIM-157; changelog fragment record/changelog.d/lead-083.md.

## Next

- Report. Nothing else on this branch; the lead worker's parent opens the PR.

## Choices

- Arm A, field excitation: overdamped phi^4 lattice kink, lattice spacing
  h = 1, 0.5, 0.25. Simplest nonlinear field with a localized excitation,
  and the kink of CASE-269's testbed. Coupling is uniform nearest
  neighbour, so no grouping of sites is set off by coupling strength.
- Arm B, collective mode: Kuramoto partial synchrony, N = 200, uniform
  coupling K/N = 2.5/200, Gaussian frequency quantiles. The nonlinear
  twin of CLAIM-388 (uniform coupling), with an environment (the drifting
  oscillators), so the form is a proper part. Gives timing, which
  CLAIM-172's entrainment needs.
- Arm C, block control: two Kuramoto clusters, Kin = 4, Kout = 0.1.
- Compensation: LIT-902's jaw-load design, sustained load on members S,
  task variable read with the others free and frozen; kappa = share of
  the damage the others undo. Entrainment: detune S, read frequency shifts
  (CLAIM-172's timing sense). An overdamped kink has no timing, so
  entrainment there is recorded as having no observable; co-movement
  (the whole kink shifts) is reported instead.
- Block test: spectral rho = delta/eps for the group, plus entrywise ratio;
  for Kuramoto read three ways (structural K, realized mean signed
  Jacobian, realized mean absolute).
