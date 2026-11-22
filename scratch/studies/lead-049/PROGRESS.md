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

- Part 2 finished (`results/part2_runs.jsonl`, `part2_summary.json`), `condC_check.py`
  (`results/condC_check.jsonl`) and `analyze_part2.py` (`results/part2_analysis.json`).
- CASE-tmp5sk3q written from parts 1-3; notes refined with part-2 findings.

## Next

- Nothing in the lead's scope. Report to the coordinator. The owner decides on status,
  on the reading of the lone generalist (third outcome or another), and whether to mark
  LEAD-049 Done.
