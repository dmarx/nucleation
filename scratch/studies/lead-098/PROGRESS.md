# LEAD-098 progress

- Lead: LEAD-098
- Branch: claude/lead-098-case179-network
- Task: simulate CASE-179's network; run its three manipulations (coupling,
  correspondence maps, revision apparatus) with A12's arms; run QUESTION-063's
  displacement (shared drive displaced for one member only) and perturbation
  (perturb one member, measure the others) arms; say which of QUESTION-035's
  tests separate common drive from coupling. Budget about an hour of CPU,
  core arms first. File a CASE (executed-study), a CLAIM if warranted, and
  dated notes on CASE-179, QUESTION-063, the advanced entries and LEAD-098.

## Done

- Read the lead, CASE-179, QUESTION-063, ARG-072, CLAIM-616, CASE-225 and the summaries of QUESTION-319/282/283/035, CLAIM-474/471.
- sim.py and test_sim.py (8 tests pass).
- run.py and README.md; full run (about 6 min CPU), a resumed run adding revision_passive items, and sheaf2 items after a rank-tolerance fix (the sheaf: lines are superseded). results.jsonl committed.
- Filed CASE-tmp69rk8 (executed-study, Proposed, documented) and CLAIM-tmpo7igy (Proposed, thesis, demonstrated).
- Dated notes on CASE-179, QUESTION-063, QUESTION-035, QUESTION-319, QUESTION-282, QUESTION-283, CLAIM-474, CLAIM-471, CLAIM-616, LEAD-098.
- Changelog fragment record/changelog.d/lead-098.md.

## Next

- Report. Not done: the arms of CASE-179's notes of 2026-11-03 and 2026-11-19; reruns across seeds and graphs.

## Choices

- "Three manipulations" read as CASE-179's three (coupling, maps, revision), run as its
  regime table; A12's three arms (forcing withdrawal, suppression, adaptive capacity
  knockout) run as well, since the lead names both.
- Units: Stuart-Landau oscillators; maps: U(1) phase offsets on a ring of 8 with one
  chord (two independent cycles); higher-dimensional stalks: linear cellular sheaves
  reduced by Kron reduction (Schur complement), not oscillator dynamics.
- Common drive phases set to the apparatus's section, so the drive alone realizes the
  apparatus's maps (the hardest case for passive tests).
- Revision: a linear phase-response model; "consistency" = maps set to observed offsets,
  and separately gains fitted to passive fluctuations; "checked" = gains and pinning
  fitted from apparatus-chosen kicks (units 0-3), kept only if better on held-out kicks
  (units 4-7).
- CASE status Proposed (as other executed-study cases filed by leads); CLAIM warrant
  demonstrated (an existence result by construction in a model).
