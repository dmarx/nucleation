# LEAD-049 progress

Branch: claude/lead-049-differentiated-equilibrium.

## Done

- Model class chosen, and `model.py` written: CLAIM-369's class, with
  bounded scalar traits moving up the rare-mutant selection gradient.
- `test_model.py` written: 14 tests, all passing.
- Part 1 run (Theorem B at fixed traits): `results/part1_*.json`.
- Part 3 run (two-resource counterexample): `results/part3_runs.json`
  and `results/part3_log.txt`.
- `generalist_check.py` run: `results/generalist_check.json`.
- CLAIM-tmp6kclm written: Theorems A, B and C, demonstrated.
- CLAIM-tmpdsv4t written: the counterexample, demonstrated.

## Next

- Part 2 (Gaussian niches, Theorems A and C, from near-identical starts).
  Resumable: it appends to `results/part2_runs.jsonl`. Rerun
  `python3 -I study.py part2` to continue it.
- CASE-tmp5sk3q (executed-study): write it from the results of parts 1–3.
  The file is still luria's template.
- Dated notes of 2026-11-22 on QUESTION-132, QUESTION-133, QUESTION-135,
  CLAIM-369, CASE-118 and LEAD-049, each with a history entry and a
  version bump. LEAD-049 gains `operationalized_in: CASE-tmp5sk3q`. No
  status or stage changes.
- Changelog fragment `record/changelog.d/lead-049.md`.
- Check frontmatter with yaml, check titles and H1s, then commit and push.
