# LEAD-173 progress

- Lead: LEAD-173 (advances QUESTION-252)
- Branch: claude/lead-173-five-conditions
- Task: in linear Gaussian VAR, declare target, projection, metric, horizon
  and budget; then for each of P, D, M, A, C either construct a case meeting
  the other four and failing it, or prove that the other four entail it;
  work the conditions pairwise; file a CASE and a CLAIM, a dated note on the
  lead and on QUESTION-252, and a changelog fragment.

## Done

- fivecond.py: exact defects of P, D, M, A, C for a VAR(p) (companion form).
- witnesses.py: constructions for every PDMA configuration the entailments
  allow (VAR(1), VAR(2), and eps > 0 leaks); first run shows each lands in
  its intended cell.
- run.py, test_fivecond.py (94 pass), results.json/.md, README.md.
  Result: entailments E1 D=>M (VAR(1) only), E2 P&D&M=>A (all), E3 A=>P
  (eps = 0) are the only ones: every other configuration has a witness, and
  3,000 random sparse models per class hit no forbidden cell.
  Leave-one-out at eps = 0: VAR(1) P no, D yes, M no, A no, C yes;
  VAR(2) M yes. At eps = 0.01 P becomes realizable.

- Filed CASE-tmpo5jhq (the study), CLAIM-tmp186gy (the table, external
  target), CLAIM-tmp9xo66 (alternative: target is Y, P and A collapse into
  D and M).

- Dated notes on LEAD-173 and QUESTION-252; changelog fragment
  record/changelog.d/lead-173.md.

## Next

- Nothing left on the branch; report to the lead (it opens the pull request).

## Choices made

- Class: stable stationary linear Gaussian VAR(1) with Sigma > 0 first,
  then VAR(2) (whose companion form has singular noise).
- Description: linear coarse-graining Y = LX.
- Target: an external linear functional Z = GX, one step ahead, not Y's own
  future (with Y's own future, P is D and M together by definition, A3's
  warning; reported as the alternative).
- Projection: Mori's, onto span(Y_t) in L2 of the stationary law.
- Metric: relative excess MSE of the memoryless reduced model over the
  optimal predictor from the full past; horizon h = 2 (at h = 1, A is P);
  tolerance eps = 0 primary, eps = 0.01 alternative.
- Budget: reduced state dimension m <= b = 2 (in this class every
  computation is polynomial, so size is the only budget that separates
  descriptions of one system; a sample budget makes C a parameter of A,
  CLAIM-401's reading).
