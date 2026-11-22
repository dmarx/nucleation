# LEAD-029 progress

Branch: claude/lead-029-joint-prediction (cut from staging).

## Done
- Model, rivals, derivation and tests: `jointpred.py`, `test_jointpred.py` (9 pass).
- Runner `run_study.py`, resumable: appends each run to `runs.jsonl`, skips runs already there, then writes `results.json`.
- CASE-tmp66fkd (executed study) and CLAIM-tmpc4gyx (the finding) written and committed.

## Running / next
- Study: 4 generators x 2 designs x 6 seeds = 48 runs. To resume: `cd scratch/studies/lead-029 && OMP_NUM_THREADS=1 python3 -I run_study.py 6 results.json > run.log 2>&1`.
- Then: write the CASE and CLAIM from results.json; dated notes of 2026-11-22 on LEAD-029, CLAIM-336, CLAIM-286, QUESTION-088, ARG-065; changelog fragment record/changelog.d/lead-029.md; frontmatter checks; commit, push.
