# LEAD-029 progress

Branch: claude/lead-029-joint-prediction (cut from staging).

## Done
- Model, rivals, derivation and tests: `jointpred.py`, `test_jointpred.py` (9 pass).
- Runner `run_study.py`, resumable: appends each run to `runs.jsonl`, skips runs already there, then writes `results.json`.
- CASE-tmp66fkd (executed study) and CLAIM-tmpc4gyx (the finding) written and committed.

## Next
- Study done: 48 runs in runs.jsonl, summary in results.json.
- Dated notes on LEAD-029, CLAIM-336, CLAIM-286, QUESTION-088, ARG-065 and the changelog fragment are done. Remaining: report to the coordinator (no PR; the coordinator opens it).
