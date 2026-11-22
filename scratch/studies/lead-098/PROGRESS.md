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
- sim.py (Stuart-Landau network with connection maps, Heun integrator, readouts, linear-response fit, sheaf Kron reduction) and test_sim.py (7 tests pass).

## Next

- Read CASE-179, QUESTION-063, ARG-072, QUESTION-035/319/282/283, CLAIM-474/471/616.

## Choices

- "Three manipulations" read as CASE-179's three (coupling, maps, revision), run as its
  regime table; A12's three arms (forcing withdrawal, suppression, adaptive capacity
  knockout) run as well, since the lead names both.
- Units: Stuart-Landau oscillators; maps: U(1) phase offsets on a ring of 8 with one
  chord (two independent cycles); higher-dimensional stalks: linear cellular sheaves
  reduced by Kron reduction (Schur complement).
