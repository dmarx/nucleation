# LEAD-144 study: the feature model against a shared-driver null

`study.py` simulates three linear organizational worlds over the same
overlapping working groups and communication graph (coupled, shared driver
with no interaction, mixed), with the driver gain tuned so that every world
shows the same within-group correlation. It fits CASE-165's finite
beta-Bernoulli feature model (K = 16, alpha = 3) and relational comparators on
observational data, and scores each on interventions none was fitted to:
pulses to members and cuts of a group's internal ties. See the module
docstring for the arms.

Rerun (CPU, about 20 s per item; resumes from `results.jsonl`):

    python3 -I -m pytest -q test_study.py
    python3 -I study.py results.jsonl 8        # 8 seeds x 3 worlds
    python3 -I summarize.py results.jsonl

`results.jsonl` holds one line per (world, seed), appended as each finishes.
The run of 2026-11-22 used seeds 0-7; seed 5 is dropped by `summarize.py`
because its coupled world is not stationary. `summary.txt` is its output.
With OMP_NUM_THREADS=1, worlds can run as separate processes
(`study.py results.jsonl 8 mixed`).
