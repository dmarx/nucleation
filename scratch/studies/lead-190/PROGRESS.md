# LEAD-190 progress

- Lead: LEAD-190 (advances CLAIM-281, CLAIM-285)
- Branch: claude/lead-190-role-indexed-grants (from origin/staging)

## Task as understood

In the built model of LEAD-090 (scratch/studies/lead-090/model.py, CASE-363),
loaded by path and unmodified, run two population comparisons:

1. role-indexed against scalar grants (CLAIM-281): factions or retained
   disagreement under each;
2. operators bound by A2's two grant conditions against unbound operators
   (CLAIM-285): whether they delegate, and to aligned others beyond chance,
   recording whom they delegate to beyond one hop.

File an executed-study CASE, CLAIMs, dated notes, a changelog fragment.

## Choices made

- Each operator is both a LEAD-090 reader (meaning m_i, critic weights W_i
  over all sources, itself included) and a LEAD-090 specialist (retrieval
  biased toward its own side by sigma). A source's own lean (phi_s) is the
  one new coupling; phi_s = 0 makes each reader an independent LEAD-090
  institution (tested to 1e-12 against lead-090's mean_field).
- Critic score = zeta * agreement (LEAD-090 Regime A soft) + (1 - zeta) *
  observed relevance (Regime B); relevance r_j drawn independent of side.
- Decision layer: CLAIM-375's weighted-mean decision; grants under one-hop,
  leave-one-out (CLAIM-502) or damped recursive (CLAIM-282) aggregation, all
  with damping eta = 0.5; objective realized policy or authority held;
  operators move grants by projected gradient ascent (exact gradients,
  tested). Quadratic grant cost by default (the game converges); linear cost
  as a robustness check (it cycles; time averages used).
- Five grant schemes for CLAIM-281: scalar-agree, scalar-comp,
  scalar-policy, role (critic by relevance, decision by policy), role-agree.
- Population sides shuffled and initial grants jittered, after a pilot run
  in which index order aligned with side produced spurious alignment.

## Done

- Checked the record: not already held.
- model.py, test_model.py (27 tests pass), run.py (e1-e6), README.md.
- All six experiments run; results/*.json committed.
- Filed: CASE-tmpw3vii (executed-study), CLAIM-tmp5wozo (role vs scalar),
  CLAIM-tmppm30v (where a relevance-scored meaning goes), CLAIM-tmpdpnid
  (bound vs unbound), CLAIM-tmpoc6mo (delegation to the extremes), all
  Proposed, demonstrated; changelog fragment record/changelog.d/lead-190.md.
- Dated notes of 2026-11-23 on LEAD-190, CLAIM-281, CLAIM-285, CASE-092,
  CASE-363, CLAIM-375, CLAIM-502, QUESTION-089, QUESTION-090.
- Alternatives filed inside CLAIM-tmp5wozo (two readings of CLAIM-281's
  role indexing; lean A) and CLAIM-tmpoc6mo (two readings of CLAIM-285's
  "aligned"; lean A).
- LEAD-015's two-institution model was not needed (one population) and was
  not loaded.

## Next

- Nothing for the worker. For the owner: the readings, statuses, and
  whether LEAD-190 is done. Not run: other decision rules, unbalanced
  populations, coalitions, noisy or side-correlated relevance.
