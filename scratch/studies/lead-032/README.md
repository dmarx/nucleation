# LEAD-032: literature search

Europe PMC search for dismantling trials of safety behaviour with exposure
held fixed, and for individual-level hysteresis in psychopathology. Run on
2026-11-22.

- `search.md`: the log: criteria, queries, counts, screening, obstacles.
- `search.py`: the queries. Rerun all with
  `python3 -I scratch/studies/lead-032/search.py`, or named ones with
  `python3 -I scratch/studies/lead-032/search.py D1_exposure_sb_trial ...`;
  results merge into `results/`. No email address is sent.
- `results/hits.jsonl`: one record per work, with the queries that found
  it; `results/counts.tsv`: hits per query per run. Abstracts go to
  `results/abstracts.jsonl`, which is not committed.
- `PROGRESS.md`: the worker's progress file.
