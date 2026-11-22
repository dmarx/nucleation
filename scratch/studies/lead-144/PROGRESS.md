# PROGRESS: LEAD-144

- Lead: LEAD-144 (advances QUESTION-276; operationalized in CASE-165)
- Branch: claude/lead-144-ibp-null
- Task as understood: build a mechanistic organizational simulator that does
  not assume the IBP prior, with a shared-exogenous-driver null (no
  interaction); fit CASE-165's finite beta-Bernoulli feature model to both;
  compare against a relational baseline given communication/authorization
  relations and no modes; score on held-out interventions on the coupling.
  Scoped to about an hour of CPU, core arms first.

## Done

- Read lead, QUESTION-276, CASE-165, CASE-166 (opening).
- study.py (simulator, Gibbs sampler for CASE-165's finite beta-Bernoulli
  model, relational VAR, factor-augmented VAR, oracle, interventional arm),
  test_study.py (4 tests pass), README.md.
- Core run launched: `python3 -I study.py results.jsonl 8` (resumable).

## Next

- summarize.py; commit results.
- File CASE (executed-study), CLAIM if warranted, notes on CASE-165,
  QUESTION-276, LEAD-144; changelog fragment.

## Choices

- Linear-Gaussian worlds, N = 24, 6 overlapping groups, T = 600 days.
  Communication only; the authorization layer is left out (scope).
- Null matched: the driver gain is tuned so within-group correlation equals
  the coupled world's.
- Feature allocation static over the window (the sticky transition's
  stay-probability near 1); activations AR(1), fitted after the Gibbs run.
- The feature model alone has no intervention semantics; two readings are
  run as alternatives: 'exo' (features cause members) and 'con' (features
  are realized by holders). The owner's to choose between, if either.
- FR as a factor-augmented VAR after an alternating fit gave the same
  result in trial; FAVAR kept.
