# LEAD-159 progress

- Lead: LEAD-159 (CASE-188 with A40 Study D's control: ablate the slow
  influence structure with task information and capacity held fixed).
- Branch: claude/lead-159-slow-structure (cut from origin/staging bea386791).
- Task as understood: build CASE-188's two agents (corrigible resolve,
  entrenchment) in numpy, add a slow-structure-ablated version of each that
  sees exactly the same inputs and has the same parameter count, and measure
  persistence under irrelevant fluctuation, revision under a warranted
  defeater, and their change over time. File an executed-study CASE and a
  CLAIM for the finding; dated notes on LEAD-159, CASE-188, CLAIM-344.

## Done

- Step 1: target not held (no executed-study case cites CASE-188, CLAIM-344
  or LEAD-159; grep of record/ on 2026-11-22).

- Step 2: model (resolve_model.py), runner, 9 pytest tests passing.
- Step 3: main run, results.jsonl (252 cells x 400 runs, ~50 s).
- Step 4: sensitivity sweep, sweep.jsonl (9 variants, ~40 s).
- Step 5: README with every parameter choice and the result.

## Next

- File: executed-study CASE (variant_of CASE-188), a CLAIM (demonstrated),
  dated notes on LEAD-159, CASE-188, CLAIM-344; changelog fragment.

## Choices

See README.md, "Design, and every parameter choice". Two readings of the
lead's "returns under corrigible conditions" are both measured (perturb
recovery; selectivity under a defeater) and left to the owner.
