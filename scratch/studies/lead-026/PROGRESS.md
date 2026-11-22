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

## Done

- Step 1 check; branch pushed.
- model.py, calibrate.py, calibration.json (done), measures.py (draft).

## Next

- tests; run.py (block search over all 255 subsets, W = 1..16; Krakauer
  profile; TE; Ahat by intervention; hidden-driver variant).
