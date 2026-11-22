# LEAD-049 progress

Branch: claude/lead-049-differentiated-equilibrium. The task: state a
model class; derive sufficient conditions for a stable differentiated
equilibrium and for each specialist's recovery when rare; check them
numerically; file a CLAIM, a CASE and dated notes.

## Choices made

- Model class: CLAIM-369's symmetric resource competition, with niche
  vectors u(θ_i), a box-bounded trait, and rare-mutant selection-gradient
  adaptation. This keeps the potential L. The own-fitness gradient is
  excluded, because of its self-crowding term.
- "Recovery" is measured with frozen residents (Theorem B), and against
  re-adapted residents (Theorem C, and the counterexample).
- Whether the lone generalist is QUESTION-132's third outcome is left to
  the owner.

## Done

- `model.py` and `test_model.py`: 14 tests, all passing.
- Part 1 (Theorem B, random fixed traits): `results/part1_*.json`.
- Part 3 (two-resource trade-off): `results/part3_*`.
- `generalist_check.py`: `results/generalist_check.json`.
- CLAIM-tmp6kclm (Theorems A, B and C) and CLAIM-tmpdsv4t (the
  counterexample).
- Dated notes: QUESTION-132, QUESTION-133, QUESTION-135, CLAIM-369,
  CASE-118, and LEAD-049, which also gains `operationalized_in`.
- Changelog fragment `record/changelog.d/lead-049.md`.

## Next

- Part 2 is running and resumable (`results/part2_runs.jsonl`). Rerun
  `python3 -I study.py part2` to continue or finish it. It writes
  `results/part2_summary.json`.
- Then run `python3 -I condC_check.py`, which is resumable. The `condC`
  field in part 2 omits the stationarity requirement, so this script
  computes Theorem C's full hypothesis.
- Write CASE-tmp5sk3q, which is still luria's template. Kind
  executed-study, standing documented. It takes the numbers from parts
  1–3, part 2's summary and condC_check.
- Final checks: yaml, titles, H1s, inactive-ok lists. Then commit and
  push, and report.
