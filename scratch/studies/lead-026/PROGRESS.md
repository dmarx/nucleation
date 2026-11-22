# LEAD-026 progress

- Lead: LEAD-026
- Branch: claude/lead-026-case101-populations (cut from origin/staging)

## Task as understood

Simulate CASE-101's three populations (A common input, B norm
transmission, C institution that selects and trains), matched in
turnover and aggregate statistics. Apply QUESTION-115's search
procedure (Krakauer's A*, A, nC and lagged A(Δ); Bourrat's Â;
dynamical independence; a priced block) and a lagged block criterion
(QUESTION-116) to each. File a CASE (executed-study), a CLAIM if
warranted, and dated notes on the advanced entries and LEAD-026.

## Step 1 check

Target not already held: no executed study of CASE-101 and no lagged
block criterion on staging (grep of LEAD-026, CASE-101, "lagged block"
on 2026-11-22). LEAD-037 also names the lagged criterion (dancing
couple), unfiled.

## Choices

- LEAD-167's code is exact over a 256-state discrete kernel; CASE-101's
  arms need continuous norms, turnover and lag-L transmission, so its
  definitions (A*, A, nC; Ahat by NOTE-027's do-route) are re-implemented
  in linear-Gaussian form (measures.py), estimated from simulation.
- Eight variables per arm: six member slots, one environmental variable
  e (A: exogenous driver; B: inert; C: institution, two-way; C0: same,
  one-way), one distractor z. Turnover r = 0.02 in every arm.
- Matched: member variance 1, mean member correlation 0.4, lag-1
  autocorrelation of mean(x) 0.9 (calibrate.py -> calibration.json).
- Lagged block: VAR(W) over all variables; coupling groups priced by
  CLAIM-154 with a unit-information prior (ln n per coefficient); S
  passes when every internal cut is kept and its edge is pruned.
- Arm B's transmission is at lag L = 8 only (no synchronous coupling).

## Incidents

- The first run's intervention values were drawn from the same RNG
  stream that the deep-copied simulator then used for its noise, which
  inflated Ahat at lag 1 for some candidates (up to 7.5 nats). Fixed in
  run.py (separate generators); the faulty Ahat lines were deleted and
  recomputed.
- The PID saved with `echo $!` was a wrapper's; the first run went on
  writing after the stop. Found by `ps` and /proc/PID/cwd and stopped by
  its own PIDs (25089, 25090). Its buggy B Ahat line is to be deleted and
  recomputed. The skill's step 5 now says to check the saved PID.

## Done

- Step 1 check; branch pushed.
- model, calibration, measures, 11 tests passing, run complete
  (results.jsonl, 84 items, deduplicated; summary.txt), README.

## Results (summary.txt, key table)

- Block membership: A, C, C0 -> members + e at every window; B ->
  members alone at every window. With e hidden, every arm's members pass.
- B's internal ln BF peaks at W = 8 = L (10909 at W = 7, 18290 at W = 8).
- C's members -> institution coupling kept at W <= 4 only (373, 85), then
  priced out; C0 and A agree on every measure.
- Members' A(D) with e in E: B 0.20 nats at D = 64; A, C, C0 zero by D = 8.
- Ahat of B's members falls to 0.02 by D = 32 against A = 0.31: an
  intervention on the present slice misses the stored norms of the last
  L steps.
- TE into members: A 0.15, C 0.11, C0 0.16, B 0.00 (e observed); 0 in all
  with e hidden.

## Filed

- CASE-tmprsqvj (executed-study, Proposed), CLAIM-tmp2jbb1 (thesis,
  demonstrated, Proposed).
- Dated notes: QUESTION-115, QUESTION-116, CLAIM-157, CLAIM-194, CASE-101,
  LEAD-026 (version bumped with a history line, as the record does).
- Changelog fragment record/changelog.d/lead-026.md.

## Next

- Nothing on the branch. Report; the lead opens the pull request.
