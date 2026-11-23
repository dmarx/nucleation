# LEAD-105 progress

- Lead: LEAD-105 (advances CLAIM-367; design from CASE-113's interventions)
- Branch: claude/lead-105-crossed-intervention
- Task: on one conventionally trained small network with two conflicting
  tasks, (1) hold the network fixed and change the optimizer; (2) hold the
  optimizer fixed and disrupt a state the network learned; see which moves
  the network's characteristic responses to conflicting learning demands.
  CLAIM-367's defeat condition: (1) leaves them unchanged while (2)
  abolishes or alters them.

## Already held?

Checked 2026-11-23: no changelog fragment, case or claim runs the crossed
design. LEAD-045 (CASE-319) ran the optimizer arm only, on independent
skills, with no disruption arm.

## Done

- crossed.py (network, optimizers, disruptions, probe), run_all.py,
  analyze.py, test_lead105.py (8 tests pass).
- Grid run (2 training optimizers x 12 seeds x 6 states x 4 probe
  optimizers, plus the training optimizer with carried state on the intact
  net; 600 probes) in results/probes.jsonl; calibration.json; summary.json.

## Choices

- Response to a conflicting demand: task B's target is changed to
  b2 = (b - sqrt(3) a)/2 (cos -0.866 with A) and both tasks train jointly;
  measured by A's peak forgetting, A's level when B reaches 0.9, B's
  relearning time, the initial task-gradient cosine and segregation.
- Pace matched: each probe optimizer's step size calibrated (seeds
  100-103, separate from the study seeds) so the intact net relearns B in
  40 steps; differences are in path, not speed.
- Disruptions: permutation (null control), function-preserving rescaling
  (spread 2; spread 4 destabilized SGD), ablate-and-heal of the 8 most
  task-selective units or 8 random units (1000 healing steps under the
  training optimizer), continued training (control for healing).

## Next

- file CASE, CLAIMs, dated notes on LEAD-105 and CLAIM-367, changelog
